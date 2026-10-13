"""hledger.py — the chart in ℍ: every law of the trunk read in the ℍ reading (tools/quat.py) on its own domain and on
generic quaternions, and each derivation's licensed path re-graded there by the receipt prover with directional
receipts (rung `H`; SPEC §6.4, §7.4, LEGISLATION 32).

Written by check.py as census/h-ledger.md. For a node the ledger records

  * the **law on its domain** in ℍ — `exact` (as stated on every sample), `mod-Λ` (holds only mod Λ_ℍ),
    `guarded` (holds where its forms have a value; some sample has none), `none` (no sample has a value), `fails`;
    on a real domain (natural, positive, negative, real, unit) the contents are central and the law holds as it
    holds in ℝ; on `complex` the contents are generic quaternions; on `slice` they are co-sliced;
  * the **law on generic quaternions** (every variable a generic quaternion whatever the declared domain) — the
    same five words: where a trunk law fails here and holds on its domain, non-commutativity is what it fails by
    (Distribution, the log laws, the phase rule off its slice: the Slice Principle, JH-4);
  * the **tape in ℍ**: the licensed path found at ∞ in ℂ, graded again with directional receipts: an absorbed
    step whose paying instance no longer pays (its content not co-sliced with the receipt) is `absent`
    (cross-slice), a receipt that is no lattice element (the seam) is `absent`;
  * the **JH cell** these imply, compared with the hand-written cell: `replaced` when the law has a value on no
    sample of its domain; `fails` when it fails on its domain, or its tape is absent; `guarded` when some sample
    has no value or the tape imports; `holds-mod-Λ` when the tape posts or the law holds mod Λ; else `holds`.
    The hand cell may say more (`guarded` over `holds`; `replaced` over anything), never less, and `untested` is
    no longer legal where the ledger computes.

A path re-graded in ℍ is the path the search found cheapest in ℂ; a cheaper one in ℍ may exist, so a tape in ℍ
can be too pessimistic, never too generous (SPEC §7.3).
"""
from __future__ import annotations
import os
import random

import forms as F
import j1 as J1
import nodes as N
import placeledger as PLG
import quat as QT

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

H_RUNG_ROWS: list = []    # (node id, tape, hand JH cell) for the nodes of rung `H` themselves
TRIALS = 20
READING = QT.Reading()

# a hand-written JH cell may say more than the computation, never less
ACCEPT = {
    "holds": {"holds"},
    "holds-mod-Λ": {"holds-mod-Λ"},
    "guarded": {"holds", "holds-mod-Λ", "guarded"},
    "replaced": {"holds", "holds-mod-Λ", "guarded", "fails", "replaced"},
    "fails": {"fails"},
}


def law_in_h(node, forms, rng, domain=None, trials: int = TRIALS):
    """The law in ℍ at the generic points of a domain (the node's own by default): exact · mod-Λ · guarded · none
    · fails."""
    f1, f2 = forms
    names = F.variables(f1) | (F.variables(f2) if f2 is not None else set())
    domain = domain or node.get("domain", "positive")
    eq = str(node.get("equality", "≐"))
    R = READING

    def verdict(env):
        try:
            v1 = R.evaluate(f1, env)
            v2 = R.evaluate(f2, env) if f2 is not None else None
        except R.skip_errors:
            return "none"
        if f2 is None:
            return "exact"
        if R.is_pole(v1) or R.is_pole(v2):
            return "exact" if (R.is_pole(v1) and R.is_pole(v2)) else "fails"
        if R.equal(v1, v2, eq):
            return "exact"
        if R.equal(v1, v2, "≃"):
            return "mod-Λ"
        if R.seam(v1, v2):
            return "seam"
        return "fails"

    counts = {"exact": 0, "mod-Λ": 0, "fails": 0, "none": 0, "seam": 0}
    for _ in range(trials if names else 1):
        counts[verdict(R.random_env(names, domain, rng))] += 1
    return _status(counts)


def _status(counts: dict) -> str:
    """The five words from the sample counts — and `seam`, a sixth: the law holds everywhere but on the seam, where
    the two sides differ by the pinning's displacement (a receipt only a paying instance absorbs); a seam is a
    guard, not a failure."""
    if counts["fails"]:
        return "fails"
    if not counts["exact"] and not counts["mod-Λ"] and not counts["seam"]:
        return "none"
    if counts["seam"]:
        return "seam"
    if counts["none"]:
        return "guarded"
    if counts["mod-Λ"]:
        return "mod-Λ"
    return "exact"


def on_slice(node):
    """The node with its `complex` domain read on the plane ℂ ⊂ ℍ, the slice of the pinned J: a trunk derivation is
    the classical calculus, which ℍ carries verbatim on that slice (JH-4) — its receipts ω = 2πi are paid there and
    on no other slice, since the forms `[()]` and `[<o>]` have one value each — and conjugation by a unit
    quaternion, an automorphism of ℍ, carries the same derivation to every other slice with J → J_u. So the path is
    graded on the plane; on a real domain the contents are central and nothing changes. The law itself is still
    read on generic quaternions (law_in_h), and a theorem reused in rung H is value-checked at its use site, on
    the citing node's own contents (tools/j1.py, grade_steps)."""
    if node.get("domain") == "complex":
        return N.Node(id=node.id, path=node.path, meta={**node.meta, "domain": "plane"}, sections=node.sections, body=node.body)
    return node


def regrade(details, node, grades: dict, rng) -> J1.Tape:
    """Grade a derivation's licensed steps again in ℍ (lemma tables priced as they close), on the plane."""
    return PLG.regrade(details, on_slice(node), grades, READING, rng)


def jh_cell(law: str, tape) -> str:
    if law == "none":
        return "replaced"
    if law == "fails":
        return "fails"
    g = tape.grade if tape is not None else "strict"
    if g == "absent":
        if not any("unlicensed" in a for a in tape.absent) and all(not r.k for r in tape.receipts if r.grade == "absent"):
            g = "import"   # every absent step is formless in ℍ (no sample has a value): guarded, not false
        else:
            return "fails"
    if law in ("guarded", "seam") or g == "import":
        return "guarded"
    if law == "mod-Λ" or g == "posted":
        return "holds-mod-Λ"
    return "holds"


def grade_cited_in_h(nodes, order, want: set, lic_cache, rng, lic_steps: dict, schema_instances_fn, h_grades: dict):
    """Re-grade in ℍ the trunk theorems that rung H cites (their licensed paths come from the ℂ run, `lic_steps`), in
    walk order, so that an H node reusing a trunk theorem prices it at its grade in ℍ — not at its grade in ℂ."""
    for node in order:
        if node.id not in want or node.get("type") not in ("theorem", "schema") or node.get("level") != "object":
            continue
        if node.get("setting") in ("JP", "JH"):
            continue
        insts = [node]
        if node.get("type") == "schema":
            try:
                insts = schema_instances_fn(node)
            except ValueError:
                insts = []
        tape = J1.Tape()
        srng = random.Random(rng.randint(0, 10 ** 9))
        for inst in insts:
            if inst.id in lic_steps:
                g = dict(h_grades)
                g["hypothesis"] = tape
                tape.merge(regrade(lic_steps[inst.id], inst, g, srng), dedupe=(inst is not node))
        h_grades[node.id] = tape


def _short(law, generic, tape) -> str:
    return f"law {law}, on ℍ {generic}" + (f", tape {tape.grade}" if tape is not None else "")


def compute(nodes, rep, rng, lic_steps: dict, schema_instances_fn):
    """The ledger for every object-level node outside rungs `H` and `place`. Writes census/h-ledger.md and compares
    the JH cells with the hand-written ones."""
    grades: dict = {}
    rows = []
    order = sorted(nodes.values(), key=lambda n: n.get("order", 0) if isinstance(n.get("order"), int) else 0)
    for node in order:
        if node.get("level") != "object" or node.get("setting") in ("JP", "JH"):
            continue
        forms = PLG._law_forms(node)
        has_tape = node.get("type") in ("theorem", "schema")
        if forms is None and not has_tape:
            continue
        insts = [node]
        if node.get("type") == "schema":
            try:
                insts = schema_instances_fn(node)
            except ValueError:
                insts = []
        srng = random.Random(rng.randint(0, 10 ** 9))
        statuses, generics = [], []
        tape = J1.Tape() if has_tape else None
        for inst in insts:
            iforms = PLG._law_forms(inst) if inst is not node else forms
            if iforms is not None:
                statuses.append(law_in_h(inst, iforms, srng))
                generics.append(law_in_h(inst, iforms, srng, domain="complex"))
            if has_tape and inst.id in lic_steps:
                g = dict(grades)
                g["hypothesis"] = tape
                tape.merge(regrade(lic_steps[inst.id], inst, g, srng), dedupe=(inst is not node))
        if tape is not None:
            grades[node.id] = tape

        law, generic = _combine(statuses), _combine(generics)
        cell = jh_cell(law if law != "—" else "exact", tape)
        hand = (node.get("holds") or {}).get("JH", "")
        rows.append((node.id, law, generic, tape, cell, hand))
        if hand == "untested":
            rep.fail(node.id, f"JH cell is untested but the ℍ ledger computes {cell}: " + _short(law, generic, tape))
        elif cell not in ACCEPT.get(hand, set()):
            rep.fail(node.id, f"JH cell says {hand} but ℍ computes {cell}: " + _short(law, generic, tape))
        else:
            rep.ok()
    write(rows)
    return rows


def write(rows):
    path = os.path.join(ROOT, "census", "h-ledger.md")
    out = ["# The chart in ℍ — computed by the ℍ reading (tools/quat.py) and the receipt prover (tools/j1.py)", "",
           "Each law read in Hamilton's quaternions: on its own domain (real domains are central, where the law holds as in ℝ; `complex` is a generic quaternion; `slice` co-sliced), and on generic quaternions whatever the domain (exact · mod-Λ · guarded · none · fails), with its derivation's licensed path re-graded in ℍ with directional receipts (strict · absorbed · posted · import · absent; an absorbed step whose instance no longer pays is absent, cross-slice) and the JH cell they imply beside the hand-written one. Written by `tools/check.py`; do not edit. Rung `H`'s own nodes are graded in ℍ as they are checked and listed last.", "",
           "| node | on its domain | on generic ℍ | tape in ℍ | computed JH | hand JH |", "|---|---|---|---|---|---|"]
    for nid, law, generic, tape, cell, hand in rows:
        t = J1.describe(tape, READING).replace("|", "/") if tape is not None else "—"
        out.append(f"| `{nid}` | {law} | {generic} | {t} | {cell} | {hand} |")
    out += ["", "## Rung `H`", "", "| node | computed JH | hand JH | tape |", "|---|---|---|---|"]
    for nid, tape, hand in H_RUNG_ROWS:
        out.append(f"| `{nid}` | {tape.cell} | {hand} | {J1.describe(tape, READING).replace('|', '/')} |")
    open(path, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    return path


# ----------------------------------------------------------------------------- the rung at the places (LEGISLATION 29)

import quatplace as QP  # noqa: E402

H_PLACES = QP.PLACES


def law_at_hplace(node, forms, R, rng, domain=None, trials: int = 40):
    """The law in the quaternion reading at a place, at the generic points of a domain (the node's own by default:
    a real domain is the centre — the page's own numbers; `complex` a generic quaternion of the page; `slice` a
    Hurwitz unit times a principal unit): exact · mod-Λ · guarded · none · fails."""
    f1, f2 = forms
    names = F.variables(f1) | (F.variables(f2) if f2 is not None else set())
    domain = domain or node.get("domain", "positive")
    eq = str(node.get("equality", "≐"))

    def verdict(env):
        try:
            v1 = R.evaluate(f1, env)
            v2 = R.evaluate(f2, env) if f2 is not None else None
        except R.skip_errors:
            return "none"
        if f2 is None:
            return "exact"
        if R.is_pole(v1) or R.is_pole(v2):
            return "exact" if (R.is_pole(v1) and R.is_pole(v2)) else "fails"
        try:
            if R.equal(v1, v2, eq):
                return "exact"
            if R.equal(v1, v2, "≃"):
                return "mod-Λ"
            if R.seam(v1, v2):
                return "seam"
        except R.skip_errors:
            return "none"
        return "fails"

    counts = {"exact": 0, "mod-Λ": 0, "fails": 0, "none": 0, "seam": 0}
    for _ in range(trials if names else 1):
        counts[verdict(R.random_env(names, domain, rng))] += 1
    return _status(counts)


def _combine(sts):
    if not sts:
        return "—"
    if any(x == "fails" for x in sts):
        return "fails"
    if all(x == "none" for x in sts):
        return "none"
    if any(x == "seam" for x in sts):
        return "seam"
    if any(x in ("none", "guarded") for x in sts):
        return "guarded"
    if any(x == "mod-Λ" for x in sts):
        return "mod-Λ"
    return "exact"


def _cell_from_laws(laws: dict) -> str:
    ls = list(laws.values())
    if ls and all(x == "none" for x in ls):
        return "replaced"
    if any(x == "fails" for x in ls):
        return "fails"
    if any(x in ("none", "guarded", "seam") for x in ls):
        return "guarded"
    if any(x == "mod-Λ" for x in ls):
        return "holds-mod-Λ"
    return "holds"


def compute_places(nodes, rep, rng, lic_steps: dict, schema_instances_fn, places=H_PLACES):
    """Two tables, written to census/h-place-ledger.md: rung H's laws read at p = 2, 3, 5, 7, 13 in the quaternion
    reading (their JP cell: the law at the Hurwitz places), and rung place's laws read in that reading at their own
    place (their JH cell: holds on generic quaternions of the page, guarded when only on the centre)."""
    readings = {p: QP.Reading(QP.HPlace(p)) for p in places}
    order = sorted(nodes.values(), key=lambda n: n.get("order", 0) if isinstance(n.get("order"), int) else 0)
    h_rows, p_rows = [], []
    for node in order:
        if node.get("level") != "object":
            continue
        setting = node.get("setting")
        if setting not in ("JH", "JP"):
            continue
        forms = PLG._law_forms(node)
        insts = [node]
        if node.get("schema_range"):
            try:
                insts = schema_instances_fn(node)   # a law written over the place parses at each instance
            except ValueError:
                insts = []
        elif forms is None:
            continue
        srng = random.Random(rng.randint(0, 10 ** 9))
        if setting == "JH":
            laws = {}
            for p, R in readings.items():
                laws[p] = _combine([law_at_hplace(inst, PLG._law_forms(inst) if inst is not node else forms, R, srng) for inst in insts
                                    if (PLG._law_forms(inst) if inst is not node else forms) is not None])
            cell = _cell_from_laws(laws)
            hand = (node.get("holds") or {}).get("JP", "")
            h_rows.append((node.id, laws, cell, hand))
            if hand == "untested":
                rep.fail(node.id, f"JP cell is untested but the quaternion reading at the places computes {cell}: " + "; ".join(f"p={p}: {laws[p]}" for p in sorted(laws)))
            elif cell not in PLG.ACCEPT.get(hand, set()):
                rep.fail(node.id, f"JP cell says {hand} but the quaternion reading at the places computes {cell}: " + "; ".join(f"p={p}: {laws[p]}" for p in sorted(laws)))
            else:
                rep.ok()
        else:
            # a node of rung place: read in the quaternion reading at its own place(s) — on its domain (the centre)
            # and on generic quaternions of the page
            centre, generic = [], []
            for inst in insts:
                env = inst.get("schema_env") or {}
                p = env.get("p", inst.get("place"))
                n = env.get("n", inst.get("depth"))
                if p is None:
                    continue
                p = int(p)
                if p not in readings:
                    continue
                try:
                    R = QP.Reading(QP.HPlace(p, depth=(2 * int(n) if (n and p == 2) else (int(n) if n else None))))
                except ValueError:
                    continue
                iforms = PLG._law_forms(inst) if inst is not node else forms
                if iforms is None:
                    continue
                centre.append(law_at_hplace(inst, iforms, R, srng))
                generic.append(law_at_hplace(inst, iforms, R, srng, domain="complex"))
            if not centre:
                continue
            c, g = _combine(centre), _combine(generic)
            if c == "none":
                cell = "replaced"
            elif c == "fails":
                cell = "fails"
            elif g == "exact" and c == "exact":
                cell = "holds"
            elif g == "mod-Λ" and c in ("exact", "mod-Λ"):
                cell = "holds-mod-Λ"
            else:
                cell = "guarded"
            hand = (node.get("holds") or {}).get("JH", "")
            p_rows.append((node.id, c, g, cell, hand))
            if hand == "untested":
                rep.fail(node.id, f"JH cell is untested but the quaternion reading at the place computes {cell} (centre {c}, generic {g})")
            elif cell not in ACCEPT.get(hand, set()):
                rep.fail(node.id, f"JH cell says {hand} but the quaternion reading at the place computes {cell} (centre {c}, generic {g})")
            else:
                rep.ok()
    write_places(h_rows, p_rows, places)
    return h_rows, p_rows


def write_places(h_rows, p_rows, places):
    path = os.path.join(ROOT, "census", "h-place-ledger.md")
    ps = list(places)
    out = ["# Rung H at the places, and rung place in ℍ — computed by the quaternion reading at a place (tools/quatplace.py)", "",
           "**Rung H at the places.** Each law of rung `H` read at p = " + ", ".join(str(p) for p in ps) +
           " in the quaternion reading — the Hurwitz order at 2 (ramified: half-shells, the uniformizer 1 + i, the residue field 𝔽₄, the 24 units), the quaternions over ℤ/pⁿ at an odd p (split: the norm isotropic) — on the law's own domain (exact · mod-Λ · guarded · none · fails), and the JP cell these imply beside the hand-written one. Written by `tools/check.py`; do not edit.", "",
           "| node | " + " | ".join(f"p = {p}" for p in ps) + " | computed JP | hand JP |",
           "|---|" + "---|" * len(ps) + "---|---|"]
    for nid, laws, cell, hand in h_rows:
        out.append(f"| `{nid}` | " + " | ".join(laws.get(p, "—") for p in ps) + f" | {cell} | {hand} |")
    out += ["", "**Rung place in ℍ.** Each law of rung `place` read at its own place in the quaternion reading: on its domain (the centre — the page's own numbers) and on generic quaternions of the page; the JH cell these imply (holds on generic quaternions; guarded when only on the centre) beside the hand-written one.", "",
            "| node | on the centre | on generic ℍ_p | computed JH | hand JH |", "|---|---|---|---|---|"]
    for nid, c, g, cell, hand in p_rows:
        out.append(f"| `{nid}` | {c} | {g} | {cell} | {hand} |")
    open(path, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    return path
