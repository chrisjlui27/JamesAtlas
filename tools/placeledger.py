"""placeledger.py — the chart at every place: each law read at p = 2, 3, 5, 7, 13 (tools/place.py), and each
derivation's licensed path re-graded there by the receipt prover (tools/j1.py) with the place's period ω_p.

Written by check.py as census/place-ledger.md (rung `place`, SPEC §4.4). For a node the ledger records

  * per place, the **law**: `exact` (equal as stated on every sample), `mod-Λ` (a strict law that holds only mod
    the place's period), `guarded` (holds where its forms exist; some sample is not a form at p), `none` (no
    sample is a form at p), `fails` (a sample where both sides are forms and differ);
  * per place, the **tape**: the derivation's licensed steps (found once, in ℂ) graded again with the receipts
    read at p — strict / absorbed / posted / import / absent — the same wall, with the place's own receipts
    (the trunk's derivations cite no law of the page, so the grade `page` of tools/j1.py occurs only on the
    tapes of rung `place` itself, graded at their own place as they are checked);
  * the **JP cell** these imply, compared with the hand-written cell: `replaced` when the law is a form at no
    tested place (the place names the law that takes over: the radius, the void pile); `fails` when it fails
    somewhere it is a form; `guarded` when some instance, somewhere, is not a form, or the tape imports; else
    the tape's grade — strict or absorbed `holds`, posted `holds-mod-Λ` — or, for a node without a derivation,
    `holds` / `holds-mod-Λ` from the law alone.

A path re-graded at p is the path the search found cheapest at ∞; a cheaper path at p may exist, so a tape at p
can be too pessimistic, never too generous (the heuristic caveat of SPEC §5.5, once more).
"""
from __future__ import annotations
import os
import random

import forms as F
import j1 as J1
import place as PL
import schema as S

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

PLACE_RUNG_ROWS: list = []    # (node id, tape, hand JP cell, reading name) for the nodes of rung `place` themselves
TRIALS = 20

# a hand-written JP cell may say more than the computation, never less
ACCEPT = {
    "holds": {"holds"},
    "holds-mod-Λ": {"holds-mod-Λ"},
    "guarded": {"holds", "holds-mod-Λ", "guarded"},
    "replaced": {"holds", "holds-mod-Λ", "guarded", "fails", "replaced"},
    "fails": {"fails"},
}


def _law_forms(node):
    """(lhs, rhs) of an equation law, (form, None) of a definition or primitive, or None."""
    law = str(node.get("law", ""))
    if node.get("level") == "meta" or node.get("type") == "gap":
        return None
    if law.startswith(("GAP", "DISCIPLINE", "DECLARATION")) or node.get("kind") in ("discipline", "declaration", "guard"):
        return None
    if F.split_law(law)[1] is not None:
        l, r, _ = F.split_law(law)
        try:
            return F.parse(l), F.parse(r)
        except Exception:
            return None
    if ":=" in law:
        l, r = [x.strip() for x in law.split(":=", 1)]
        for side in (r, l):
            try:
                return F.parse(side), None
            except Exception:
                continue
        return None
    if " is a form" in law and "is not a form" not in law:
        try:
            return F.parse(law.split(" is a form")[0].strip()), None
        except Exception:
            return None
    return None


def law_at_place(node, forms, R: PL.Reading, rng, trials: int = TRIALS):
    """(status, exceptional): the law at the generic points of its domain at this place, and whether it fails at
    the lattice points (a variable exactly one, where the log reads ω_p — the exceptional points, named rather
    than counted, as the tape names them at ∞)."""
    f1, f2 = forms
    names = F.variables(f1) | (F.variables(f2) if f2 is not None else set())
    domain = node.get("domain", "positive")
    eq = str(node.get("equality", "≐"))

    scale = R.P.p ** R.P.radius

    def verdict(env, retry=True):
        try:
            v1 = R.evaluate(f1, env)
            v2 = R.evaluate(f2, env) if f2 is not None else None
        except PL.BeyondPrecision:
            return "radius"   # a count of [p] past the working precision: dropped — a limit of the engine, not of the place
        except PL.OutsideRadius:
            # the radius is the standing proviso of the instance at a finite place (place.radius): try the same
            # sample on the radius — every variable times p (4 at p = 2) — before calling the law formless there;
            # a sample outside the radius even then has no value at p (a unit ≡ 5 mod 8 has no root at 2), and
            # counts as formless, like a selection failure
            if retry and env:
                return verdict({n: v * scale for n, v in env.items()}, retry=False)
            return "none"
        except (PL.NotAForm, F.Undefined, F.Excluded, OverflowError):
            return "none"
        try:
            if f2 is None or R.equal(v1, v2, eq):
                return "exact"
            if R.equal(v1, v2, "≃"):
                return "mod-Λ"
        except PL.BeyondPrecision:
            return "radius"   # a value that cannot be judged at the depth (shells lost past the margin): dropped
        return "fails"

    counts = {"exact": 0, "mod-Λ": 0, "fails": 0, "none": 0, "radius": 0}
    for _ in range(trials if names else 1):
        counts[verdict(R.random_env(names, domain, rng))] += 1
    # the probes sit on the lattice points exactly: no retry on the radius (that would move them off the point)
    exceptional = any(verdict(env, retry=False) == "fails" for env in R.probes(names, domain, rng)) if names else False
    # samples past the working precision are dropped, not judged (`radius`): a law all of whose samples are
    # dropped has no status here — it is `none` (a form at no sampled point), as its JP cell then says
    if counts["fails"]:
        status = "fails"
    elif not counts["exact"] and not counts["mod-Λ"]:
        status = "none"
    elif counts["none"]:
        status = "guarded"
    elif counts["mod-Λ"]:
        status = "mod-Λ"
    else:
        status = "exact"
    return status, exceptional


def regrade(details, node, grades: dict, R: PL.Reading, rng) -> J1.Tape:
    """Grade a derivation's licensed steps again at a place (lemma tables priced as they close)."""
    tape = J1.Tape()
    local = dict(grades)
    by_table: dict = {}
    for ti, i, status, msg, steps in details:
        t = by_table.setdefault(ti, J1.Tape())
        if status == "UNLICENSED":
            t.worse("absent")
            t.absent.append(f"row {i+1} unlicensed")
            continue
        t.merge(J1.grade_steps(steps, node, local, rng, R))
        local[f"lemma#{ti}"] = t
    for ti in sorted(by_table):
        tape.merge(by_table[ti])
    return tape


def jp_cell(laws: dict, tapes: dict) -> str:
    """The JP cell implied by the per-place law statuses and tapes."""
    ls = list(laws.values())
    if ls and all(x == "none" for x in ls):
        return "replaced"
    if any(x == "fails" for x in ls):
        return "fails"
    worst = "strict"
    for t in tapes.values():
        g = t.grade
        if g == "absent" and not any("unlicensed" in a for a in t.absent) and all(
                not r.k for r in t.receipts if r.grade == "absent"):
            g = "import"   # every absent step is formless at p (no sample has a value: not a false step — a receipt
                           # set {?} would be one, a difference that is no lattice element): the law is guarded there
        if J1.GRADE_ORDER.index(g) > J1.GRADE_ORDER.index(worst):
            worst = g
    if worst == "absent":
        return "fails"
    if any(x in ("none", "guarded") for x in ls) or worst == "import":
        return "guarded"
    if worst == "posted" or any(x == "mod-Λ" for x in ls):
        return "holds-mod-Λ"
    return "holds"


def compute(nodes, rep, rng, lic_steps: dict, schema_instances_fn, places=PL.PLACES):
    """The ledger for every object-level node outside rung `place` (whose nodes are graded at their own place as
    they are checked). Writes census/place-ledger.md and compares the JP cells with the hand-written ones."""
    readings = {p: PL.Reading(PL.Place(p)) for p in places}
    grades = {p: {} for p in places}   # per place: node id -> tape, in walk order
    rows = []
    mismatches = 0
    order = sorted(nodes.values(), key=lambda n: n.get("order", 0) if isinstance(n.get("order"), int) else 0)
    for node in order:
        if node.get("level") != "object" or node.get("setting") == "JP":
            continue
        forms = _law_forms(node)
        has_tape = node.get("type") in ("theorem", "schema")
        if forms is None and not has_tape:
            continue
        insts = [node]
        if node.get("type") == "schema":
            try:
                insts = schema_instances_fn(node)
            except ValueError:
                insts = []
        laws, tapes, excs = {}, {}, {}
        for p, R in readings.items():
            srng = random.Random(rng.randint(0, 10 ** 9))
            statuses = []
            tape = J1.Tape() if has_tape else None
            for inst in insts:
                iforms = _law_forms(inst) if inst is not node else forms
                if iforms is not None:
                    st, exc = law_at_place(inst, iforms, R, srng)
                    statuses.append(st)
                    excs[p] = excs.get(p, False) or exc
                if has_tape and inst.id in lic_steps:
                    g = dict(grades[p])
                    g["hypothesis"] = tape
                    tape.merge(regrade(lic_steps[inst.id], inst, g, R, srng), dedupe=(inst is not node))
            if statuses:
                # a schema's law over its instances: fails if any fails; none if all none; guarded if mixed
                if any(x == "fails" for x in statuses):
                    laws[p] = "fails"
                elif all(x == "none" for x in statuses):
                    laws[p] = "none"
                elif any(x in ("none", "guarded") for x in statuses):
                    laws[p] = "guarded"
                elif any(x == "mod-Λ" for x in statuses):
                    laws[p] = "mod-Λ"
                else:
                    laws[p] = "exact"
            if tape is not None:
                tapes[p] = tape
                grades[p][node.id] = tape
        cell = jp_cell(laws, tapes)
        hand = (node.get("holds") or {}).get("JP", "")
        rows.append((node.id, laws, tapes, cell, hand, excs))
        if hand == "untested":
            rep.fail(node.id, f"JP cell is untested but the place ledger computes {cell}: " + _short(laws, tapes, readings))
            mismatches += 1
        elif cell not in ACCEPT.get(hand, set()):
            rep.fail(node.id, f"JP cell says {hand} but the places compute {cell}: " + _short(laws, tapes, readings))
            mismatches += 1
        else:
            rep.ok()
    write(rows, readings)
    return rows


def _short(laws, tapes, readings) -> str:
    parts = []
    for p in sorted(laws):
        t = tapes.get(p)
        parts.append(f"p={p}: law {laws[p]}" + (f", tape {t.grade}" if t else ""))
    return "; ".join(parts)


def write(rows, readings):
    path = os.path.join(ROOT, "census", "place-ledger.md")
    ps = sorted(readings)
    out = ["# The chart at every place — computed by the place reading (tools/place.py) and the receipt prover (tools/j1.py)", "",
           "Each law read at p = " + ", ".join(str(p) for p in ps) + " (page depth = working precision " + ", ".join(f"{p}: {readings[p].P.N}" for p in ps) +
           " shells): the law's status at the generic points of the place (exact · mod-Λ · guarded · none · fails; ·exc when it fails at a lattice point, a variable exactly one, where the log reads ω_p; "
           "a sample outside the radius of the instance is retried on the radius and, if still outside, counts as formless; a sample past the working precision is dropped) and the grade of its derivation re-graded there "
           "(strict · absorbed · posted · import · absent), with the JP cell they imply beside the hand-written one. "
           "Written by `tools/check.py`; do not edit. The place rung's own nodes are graded at their own place and listed last.", "",
           "| node | " + " | ".join(f"p = {p}" for p in ps) + " | computed JP | hand JP |",
           "|---|" + "---|" * len(ps) + "---|---|"]
    for nid, laws, tapes, cell, hand, excs in rows:
        cells = []
        for p in ps:
            l = laws.get(p, "—")
            t = tapes.get(p)
            cells.append(l + (" ·exc" if excs.get(p) else "") + (f" · {t.grade}" if t is not None else ""))
        out.append(f"| `{nid}` | " + " | ".join(cells) + f" | {cell} | {hand} |")
    out += ["", "## Rung `place`", "", "| node | place | computed JP | hand JP | tape |", "|---|---|---|---|---|"]
    for nid, tape, hand, rname in PLACE_RUNG_ROWS:
        out.append(f"| `{nid}` | {rname} | {tape.cell} | {hand} | {J1.describe(tape).replace('≡ — no unit step: strict in 𝕁₁', '≡ — no unit step: strict at the place').replace('|', '/')} |")
    open(path, "w").write("\n".join(out) + "\n")
    return path
