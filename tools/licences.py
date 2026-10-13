"""licences.py — run the prover over every derivation on the chart: is each row licensed by the rule it cites?

Usage: python3 tools/licences.py [--node ID] [--verbose]

For each form-derivation row the cited nodes' laws become rewrite rules (both orientations, any position); a
row passes when the next form is reached in at most a few applications. `given`, `medium`, `definition`,
`name`, `substitution` and `congruence` rows are identity rows or outside the prover's scope and are reported
as such; `lemma` cites an earlier table of the same node; `hypothesis` is the schema's own law at a smaller
parameter.
"""
from __future__ import annotations
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import forms as F  # noqa: E402
import nodes as N  # noqa: E402
import prover as P  # noqa: E402
import schema as S  # noqa: E402

ROOT = os.path.dirname(HERE)

# Laws whose variables may not be void when used as rewrite rules (the degenerate instance is not the law).
NONEMPTY = {}  # Distribution with a void part is valid (zero annihilates, void is transparent)

# A node that states one half of an equation that the chart uses in both halves.
EXTRA_RULES = {
    "mult.involution": ["[(A)] ≐ A"],  # James's Involution is ([A]) ≐ A ≐ [(A)]; the law field carries the counit
    # the norm is two-sided: H.norm's second table derives q̄·q ≃ N, and the left inverse (H.inverse, table 2) cites it
    "H.norm": ["([A <([B ; i])> <([C ; j])> <([D ; k])> ; A ([B ; i]) ([C ; j]) ([D ; k])]) ≃ ([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])"],
}


# ----------------------------------------------------------------------------- rung H: families over the entries
# A law of the ordered bracket written with vector entries (x⃗ ; … ; z⃗ in the JH report) is a FAMILY of rules, one
# per shape of the list; the engine instantiates each family for lists of up to five entries (SPEC §6.4). The node's
# derivation proves the shape its `law:` states; the other shapes are the same law read at another position, and
# the prose says so.

_X = ["A", "B", "C", "D", "E"]
_Y = ["P", "Q", "R"]


def _lst(entries):
    return "[" + " ; ".join(entries) + "]"


def _family_splice():
    out = []
    for n in range(1, 4):            # entries around the spliced one (at least one: a one-entry splice is the unit)
        for m in (2, 3):             # entries of the spliced list
            inner = _Y[:m]
            for pos in range(n + 1):
                outer = _X[:n]
                lhs = _lst(outer[:pos] + ["(" + _lst(inner) + ")"] + outer[pos:])
                rhs = _lst(outer[:pos] + inner + outer[pos:])
                out.append((lhs, rhs))
    return out


def _family_unit_entry():
    out = []
    for n in range(2, 6):            # the list with the unit entry, 2 … 5 entries
        xs = _X[:n - 1]
        for pos in range(n):
            lhs = _lst(xs[:pos] + ["o"] + xs[pos:])
            rhs = _lst(xs)
            out.append((lhs, rhs))
    return out


def _family_zero_entry():
    out = []
    for n in range(2, 4):
        xs = _X[:n - 1]
        for pos in range(n):
            lhs = _lst(xs[:pos] + ["void"] + xs[pos:])
            out.append((lhs, "□"))
    return out


def _family_list_distribution():
    out = []
    for n in (2, 3):                 # the list, 2 or 3 entries, one of them a sum of two
        xs = _X[:n - 1]
        for pos in range(n):
            lhs = "(" + _lst(xs[:pos] + ["P Q"] + xs[pos:]) + ")"
            rhs = "(" + _lst(xs[:pos] + ["P"] + xs[pos:]) + ") (" + _lst(xs[:pos] + ["Q"] + xs[pos:]) + ")"
            out.append((lhs, rhs))
    return out


def _family_central_sign():
    out = []
    for n in (2, 3):
        xs = _X[:n - 1]
        for pos in range(n):
            lhs = "(" + _lst(xs[:pos] + ["<P>"] + xs[pos:]) + ")"
            rhs = "<(" + _lst(xs[:pos] + ["P"] + xs[pos:]) + ")>"
            out.append((lhs, rhs))
    return out


def _family_commutation():
    out = []
    for n in range(2, 6):            # adjacent entries P, Q exchanged in a list of 2 … 5 entries
        xs = _X[:n - 2]
        for pos in range(n - 1):
            lhs = _lst(xs[:pos] + ["P", "Q"] + xs[pos:])
            rhs = _lst(xs[:pos] + ["Q", "P"] + xs[pos:])
            out.append((lhs, rhs))
    return out


def _family_ordered_cancellation():
    out = []
    for n in range(2, 6):            # the list with the cancelling pair, 2 … 5 entries
        xs = _X[:n - 2]
        for pos in range(n - 1):
            for pair in (["P", "(<[P]>)"], ["(<[P]>)", "P"]):
                lhs = _lst(xs[:pos] + pair + xs[pos:])
                rhs = _lst(xs[:pos] + ["o"] + xs[pos:])
                out.append((lhs, rhs))
    return out


FAMILIES = {
    "H.commutation": _family_commutation,
    "H.splice": _family_splice,
    "H.unit-entry": _family_unit_entry,
    "H.zero-entry": _family_zero_entry,
    "H.list-distribution": _family_list_distribution,
    "H.central-sign": _family_central_sign,
    "H.ordered-cancellation": _family_ordered_cancellation,
}

IDENTITY_RULES = {"medium", "definition", "name", "substitution", "congruence", "given"}


def rules_for(nid: str, nodes, cache: dict, at: dict | None = None) -> list:
    """The rewrite rules a cited node offers. `at` is the citing instance's own place and depth ({p, n}, when it has
    one): a law written over the place is a different law at each (p, n), and only the instances at the citing
    instance's own place (and, when both bind it, its own depth) license a step there — the void pile of p = 2 does
    not act at p = 5, nor Fermat at depth 1 at depth 2."""
    key = (nid, tuple(sorted(at.items())) if at else None)
    if key in cache:
        return cache[key]
    out = []
    node = nodes.get(nid)
    if node is not None:
        law = str(node.get("law", ""))
        if node.get("schema_range"):   # a schema, or a decree/import written over the place and the depth
            tl, tr, _sym = F.split_law(law)
            try:
                for env in S.parse_range(node.get("schema_range", "")):
                    if at and "p" in env and env["p"] != at.get("p"):
                        continue
                    if at and "n" in env and "n" in at and "p" in env and env["n"] != at["n"]:
                        continue
                    out.append(P.Rule(nid, F.parse(S.expand(tl, env)), F.parse(S.expand(tr, env))))
            except Exception:
                pass
        r = P.rule_from_law(nid, law, NONEMPTY.get(nid, ()))
        if r is not None:
            out.append(r)
        for extra in EXTRA_RULES.get(nid, []):
            r = P.rule_from_law(nid, extra, NONEMPTY.get(nid, ()))
            if r is not None:
                out.append(r)
        if nid in FAMILIES:
            seen = {(x.lhs, x.rhs) for x in out}
            for lhs, rhs in FAMILIES[nid]():
                r = P.Rule(nid, F.parse(lhs), F.parse(rhs), frozenset(), f"{lhs} ≐ {rhs}")
                if (r.lhs, r.rhs) not in seen:
                    out.append(r)
                    seen.add((r.lhs, r.rhs))
    cache[key] = out
    return out


def table_rows(text: str):
    for t in N.parse_tables(text):
        if not t:
            continue
        hdr = [c.lower() for c in t[0]]
        if hdr and hdr[0] == "statement":
            continue
        yield t[1:] if hdr and hdr[0] == "form" else t


def check_node(node: N.Node, nodes, cache, verbose=False, max_steps=14, phases=None, on_table=None):
    """Returns (licensed, unlicensed, skipped, details). `phases` is an optional list of step predicates tried in
    order; the first phase whose steps suffice licenses the row (the receipt prover asks for the cheapest tape).
    `on_table(ti, details_of_table)` is called as each table closes, so that a caller grading tables can price a
    lemma before a later table's search cites it."""
    text = node.sections.get("Derivation", "")
    lic = unl = skip = 0
    details = []
    tables = list(table_rows(text))
    lemma_rules = []
    for ti, rows in enumerate(tables):
        prev = None
        first = last = None
        start = len(details)
        for i, r in enumerate(rows):
            cell = r[0].strip().strip("`").strip() if r else ""
            rule_cell = r[1] if len(r) > 1 else ""
            note = r[2] if len(r) > 2 else ""
            tokens = [x.lower() for x in re.split(r"[,;]\s*|\s+", N.LINK.sub("", rule_cell).strip()) if x]
            cited = N.LINK.findall(rule_cell) + [c for c in N.LINK.findall(note) if c not in N.LINK.findall(rule_cell)]
            if "name" in tokens:
                continue  # a naming row: standard notation, not a form; the chain continues past it
            try:
                f = F.parse(cell)
            except Exception:
                unl += 1
                details.append((ti, i, "UNLICENSED", f"row does not parse: {cell!r}", []))
                prev = None
                continue
            if first is None:
                first = f
            last = f
            if prev is None or "given" in tokens:
                if "given" in tokens and first is not None and first is not f:
                    unl += 1
                    details.append((ti, i, "UNLICENSED", "`given` may only open a table — a chain cannot restart", []))
                prev = f
                continue
            if not cited and set(tokens) <= IDENTITY_RULES:
                if f == prev:
                    skip += 1
                    details.append((ti, i, "identity", "", []))
                else:
                    unl += 1
                    details.append((ti, i, "UNLICENSED", f"rule {tokens} but the form changed", []))
                prev = f
                continue
            rules = []
            here = node.get("schema_env") if isinstance(node.get("schema_env"), dict) and "p" in node.get("schema_env") else None
            if here is None and node.get("place") is not None:   # a node of the rung read at one place (place:/depth:)
                here = {"p": int(node.get("place"))}
                if node.get("depth") is not None:
                    here["n"] = int(node.get("depth"))
            for c in cited:
                rules += rules_for(c, nodes, cache, here)
            if "lemma" in tokens:
                rules += lemma_rules
            if "hypothesis" in tokens and node.get("schema_env") is not None:
                env = node.get("schema_env")
                tl, tr, _sym = F.split_law(str(node.get("schema_template")))
                for e2 in S.parse_range(node.get("schema_range", "")):
                    if e2 != env and all(e2[k] <= env[k] for k in env) and e2.get("p", env.get("p")) == env.get("p") and ("p" not in env or e2.get("n") == env.get("n")):
                        try:
                            rules.append(P.Rule("hypothesis", F.parse(S.expand(tl, e2)), F.parse(S.expand(tr, e2))))
                        except Exception:
                            pass
            if phases:
                L = None
                for allow in phases:
                    L = P.licence(prev, f, rules, max_steps=max_steps, allow=allow)
                    if L.ok:
                        break
            else:
                L = P.licence(prev, f, rules, max_steps=max_steps)
            if L.ok:
                lic += 1
                details.append((ti, i, "ok", L.note + " " + " ".join(f"{s.rule}{s.direction}@{''.join(s.path) or 'root'}" for s in L.steps), L.steps))
            else:
                unl += 1
                details.append((ti, i, "UNLICENSED", L.note, []))
            prev = f
        if first is not None and last is not None and first != last:
            lemma_rules.append(P.Rule(f"lemma#{ti}", first, last))
        if on_table is not None:
            on_table(ti, details[start:])
    return lic, unl, skip, details


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--node")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--max-steps", type=int, default=14)
    args = ap.parse_args(argv)
    nodes = N.load_nodes(os.path.join(ROOT, "nodes"))
    cache = {}
    tot_l = tot_u = tot_s = 0
    import check as K  # for schema_instances
    for node in sorted(nodes.values(), key=lambda n: n.get("order", 0) if isinstance(n.get("order"), int) else 0):
        if args.node and node.id != args.node:
            continue
        if node.get("level") != "object":
            continue
        targets = [node]
        if node.get("type") == "schema":
            try:
                targets = K.schema_instances(node)
            except ValueError:
                targets = []
        for t in targets:
            l, u, s, det = check_node(t, nodes, cache, args.verbose, args.max_steps)
            tot_l += l; tot_u += u; tot_s += s
            if u or args.verbose:
                print(f"{t.id}: licensed {l}, unlicensed {u}, identity {s}")
                for ti, i, status, msg, _steps in det:
                    if status == "UNLICENSED" or args.verbose:
                        print(f"    table {ti+1} row {i+1}: {status} {msg}")
    print(f"TOTAL licensed {tot_l} · unlicensed {tot_u} · identity rows {tot_s}")


if __name__ == "__main__":
    main()
