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
}

IDENTITY_RULES = {"medium", "definition", "name", "substitution", "congruence", "given"}


def rules_for(nid: str, nodes, cache: dict) -> list:
    if nid in cache:
        return cache[nid]
    out = []
    node = nodes.get(nid)
    if node is not None:
        law = str(node.get("law", ""))
        if node.get("type") == "schema":
            tl, tr, _sym = F.split_law(law)
            try:
                for env in S.parse_range(node.get("schema_range", "")):
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
    cache[nid] = out
    return out


def table_rows(text: str):
    for t in N.parse_tables(text):
        if not t:
            continue
        hdr = [c.lower() for c in t[0]]
        if hdr and hdr[0] == "statement":
            continue
        yield t[1:] if hdr and hdr[0] == "form" else t


def check_node(node: N.Node, nodes, cache, verbose=False, max_steps=14, phases=None):
    """Returns (licensed, unlicensed, skipped, details). `phases` is an optional list of step predicates tried in
    order; the first phase whose steps suffice licenses the row (the receipt prover asks for the cheapest tape)."""
    text = node.sections.get("Derivation", "")
    lic = unl = skip = 0
    details = []
    tables = list(table_rows(text))
    lemma_rules = []
    for ti, rows in enumerate(tables):
        prev = None
        first = last = None
        for i, r in enumerate(rows):
            cell = r[0].strip().strip("`").strip() if r else ""
            rule_cell = r[1] if len(r) > 1 else ""
            note = r[2] if len(r) > 2 else ""
            try:
                f = F.parse(cell)
            except Exception:
                prev = None
                continue
            tokens = [x.lower() for x in re.split(r"[,;]\s*|\s+", N.LINK.sub("", rule_cell).strip()) if x]
            cited = N.LINK.findall(rule_cell) + [c for c in N.LINK.findall(note) if c not in N.LINK.findall(rule_cell)]
            if "name" in tokens:
                continue  # a naming row: standard notation, not a form
            if first is None:
                first = f
            last = f
            if prev is None or "given" in tokens:
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
            for c in cited:
                rules += rules_for(c, nodes, cache)
            if "lemma" in tokens:
                rules += lemma_rules
            if "hypothesis" in tokens and node.get("schema_env") is not None:
                env = node.get("schema_env")
                tl, tr, _sym = F.split_law(str(node.get("schema_template")))
                for e2 in S.parse_range(node.get("schema_range", "")):
                    if e2 != env and all(e2[k] <= env[k] for k in env):
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
