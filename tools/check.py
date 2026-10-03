#!/usr/bin/env python3
"""check.py — the chart's engine check (SPEC §10).

For every node:
  schema      required fields, enums, id = filename, unique walk order, required sections
  links       every [[id]] resolves; `uses` equals the set of ids cited in the Derivation section
  dag         every cited node has a smaller walk order (except the one marked re-entry edge)
  law         the law in `law:` is numerically true in the ℂ reading (object level), and
              matches `gloss_check` when given
  derivation  every consecutive pair of forms in every Given–Rule table is equal in the declared
              sense, on random instantiations of its variables in the node's domain
  witness     a `witness:` script (meta theorems) exits 0
  exact       a theorem whose `verified` is below `engine` is reported (SPEC §5.2: Exact withheld)
Then:
  census      every `new`/`undefined` census form is assigned to a node or listed in open-forms.md

Exit 0 iff no failures.  Run from anywhere: python3 tools/check.py [--seed N] [--trials N]
"""
from __future__ import annotations
import argparse
import os
import random
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import forms as F  # noqa: E402
import nodes as N  # noqa: E402
import census as C  # noqa: E402

ROOT = os.path.dirname(HERE)
BANDS = {"K", "1–2", "3–5", "6–8", "9–12", "beyond"}
REQUIRED = ["id", "title", "type", "level", "kind", "rung", "order", "setting", "equality", "domain", "law", "units",
            "holds", "readings", "status", "verified", "known_since", "entered", "guide", "band", "uses", "see_also",
            "aliases", "concepts", "understood", "reentry"]
NAMING_RULES = {"name"}


class Report:
    def __init__(self):
        self.fails, self.warns, self.oks = [], [], 0

    def fail(self, nid, msg):
        self.fails.append(f"{nid}: {msg}")

    def warn(self, nid, msg):
        self.warns.append(f"{nid}: {msg}")

    def ok(self):
        self.oks += 1


def check_schema(node: N.Node, nodes, rep: Report):
    m = node.meta
    nid = node.id
    fn = os.path.basename(node.path)[:-3]
    if fn != nid:
        rep.fail(nid, f"id does not match filename {fn}")
    for k in REQUIRED:
        if k not in m:
            rep.fail(nid, f"missing field {k}")
    if m.get("type") not in N.TYPES:
        rep.fail(nid, f"bad type {m.get('type')}")
    if m.get("level") not in N.LEVELS:
        rep.fail(nid, f"bad level {m.get('level')}")
    if m.get("rung") not in N.RUNGS:
        rep.fail(nid, f"bad rung {m.get('rung')}")
    if not nid.startswith(str(m.get("rung")) + "."):
        rep.fail(nid, f"id prefix does not match rung {m.get('rung')}")
    if not isinstance(m.get("order"), int):
        rep.fail(nid, "order must be an integer")
    if m.get("status") not in N.STATUS:
        rep.fail(nid, f"bad status {m.get('status')}")
    if m.get("verified") not in N.VERIFIED:
        rep.fail(nid, f"bad verified {m.get('verified')}")
    if m.get("guide") not in N.GUIDE:
        rep.fail(nid, f"bad guide {m.get('guide')}")
    if m.get("equality") not in N.EQUALITIES:
        rep.fail(nid, f"bad equality {m.get('equality')}")
    if m.get("domain") not in N.DOMAINS:
        rep.fail(nid, f"bad domain {m.get('domain')}")
    if str(m.get("band")) not in BANDS:
        rep.fail(nid, f"bad band {m.get('band')}")
    if m.get("understood") not in ("yes", "no", "partial"):
        rep.fail(nid, f"bad understood {m.get('understood')}")
    for setting, cell in (m.get("holds") or {}).items():
        if cell not in N.HOLDS:
            rep.fail(nid, f"bad holds cell {setting}: {cell}")
    for reading, cell in (m.get("readings") or {}).items():
        if cell not in N.READING_CELLS:
            rep.fail(nid, f"bad readings cell {reading}: {cell}")
    if m.get("type") == "gap":
        if m.get("status") != "ABSENT":
            rep.fail(nid, "gap nodes have status ABSENT")
        if "Plan" not in node.sections:
            rep.fail(nid, "gap node lacks a Plan section")
        else:
            plan = node.sections["Plan"]
            for field in ("candidate form", "law(s) to add", "nativity criterion", "refutation test", "meta-move", "owner thread", "rank"):
                if field not in plan:
                    rep.fail(nid, f"Plan lacks field '{field}'")
    elif "Plan" in node.sections:
        rep.fail(nid, "only gap nodes carry a Plan section")
    for sec in ("Law", "Plain", "Derivation", "Confirms", "Settings and readings", "Refuted readings", "Notes"):
        if sec not in node.sections:
            rep.fail(nid, f"missing section '{sec}'")
    plain = node.sections.get("Plain", "")
    if len(plain.split()) > 45:
        rep.warn(nid, f"Plain statement is long ({len(plain.split())} words)")
    if m.get("type") in ("primitive", "axiom") and node.derivations:
        rep.fail(nid, "primitives and axioms carry no derivation table (write 'none — adjoined')")
    if m.get("type") in ("theorem", "definition") and not node.derivations:
        rep.fail(nid, "theorems and definitions need a derivation table")
    if m.get("type") == "theorem" and m.get("verified") in ("none", "hand"):
        rep.warn(nid, f"theorem verified only '{m.get('verified')}' — Exact withheld (SPEC §5.2)")
    if m.get("type") == "decree" and m.get("status") != "NATIVE-BY-DECREE":
        rep.fail(nid, "decrees have status NATIVE-BY-DECREE")


def check_links(node: N.Node, nodes, rep: Report):
    nid = node.id
    all_links = set(N.LINK.findall(node.body))
    for link in all_links:
        if link not in nodes:
            rep.fail(nid, f"link to unknown node [[{link}]]")
    for fld in ("uses", "see_also"):
        for ref in node.get(fld, []) or []:
            if ref not in nodes:
                rep.fail(nid, f"{fld} refers to unknown node {ref}")
    cited = set(N.LINK.findall(node.sections.get("Derivation", "")))
    uses = set(node.get("uses", []) or [])
    if cited != uses:
        rep.fail(nid, f"uses {sorted(uses)} != cited in Derivation {sorted(cited)}")
    if nid in uses:
        rep.fail(nid, "a node cannot cite itself")


def check_dag(node: N.Node, nodes, rep: Report):
    nid = node.id
    order = node.get("order")
    for ref in node.get("uses", []) or []:
        if ref in nodes and isinstance(order, int):
            other = nodes[ref].get("order")
            if isinstance(other, int) and other >= order and not node.get("reentry"):
                rep.fail(nid, f"cites [[{ref}]] (order {other}) which does not precede it (order {order})")


def parse_or_none(s: str):
    try:
        return F.parse(s)
    except Exception:
        return None


def check_equal_forms(f1, f2, node: N.Node, rng, trials: int):
    """Return (ok, message) comparing two forms on random instantiations."""
    names = F.variables(f1) | F.variables(f2)
    eq = node.get("equality", "≐")
    domain = node.get("domain", "positive")
    for _ in range(trials if names else 1):
        env = F.random_env(names, domain, rng)
        try:
            v1 = F.evaluate(f1, env)
            v2 = F.evaluate(f2, env)
        except (F.Undefined, F.Excluded) as ex:
            return False, f"{type(ex).__name__} evaluating {F.to_string(f1)} / {F.to_string(f2)}"
        except OverflowError:
            continue
        if not F.equal(v1, v2, eq):
            return False, f"{F.to_string(f1, True)} = {F.fmt(v1)} but {F.to_string(f2, True)} = {F.fmt(v2)} at {{{', '.join(f'{k}={F.fmt(v)}' for k, v in env.items())}}}"
    return True, ""


def check_law(node: N.Node, rep: Report, rng, trials):
    nid = node.id
    if node.get("level") == "meta" or node.get("type") == "gap":
        return
    law = str(node.get("law", ""))
    gloss = node.get("gloss_check")
    form = None
    if "≐" in law:
        lhs, rhs = [x.strip() for x in law.split("≐", 1)]
        f1, f2 = parse_or_none(lhs), parse_or_none(rhs)
        if f1 is None or f2 is None:
            rep.fail(nid, f"law sides do not parse: {law}")
            return
        ok, msg = check_equal_forms(f1, f2, node, rng, trials)
        if not ok:
            rep.fail(nid, f"law fails: {msg}")
            return
        form = f1
    elif ":=" in law:
        lhs, rhs = [x.strip() for x in law.split(":=", 1)]
        form = parse_or_none(rhs) or parse_or_none(lhs)
        if form is None:
            rep.fail(nid, f"definition has no parseable side: {law}")
            return
    elif re.search(r"\bis a form\b", law):
        form = parse_or_none(law.split(" is a form")[0].strip())
        if form is None:
            rep.fail(nid, f"primitive law does not parse: {law}")
            return
    elif re.search(r"is not a form", law):
        return  # exclusion decree
    else:
        rep.warn(nid, f"law not checked (unrecognized shape): {law}")
        return
    if gloss and form is not None:
        names = F.variables(form)
        domain = node.get("domain", "positive")
        for _ in range(trials if names else 1):
            env = F.random_env(names, domain, rng)
            try:
                v = F.evaluate(form, env)
                g = F.gloss_value(str(gloss), env)
            except (F.Undefined, F.Excluded) as ex:
                rep.fail(nid, f"gloss check raised {type(ex).__name__}")
                return
            except OverflowError:
                continue
            if g is F.BH or v is F.BH:
                if not (g is F.BH and v is F.BH):
                    rep.fail(nid, f"gloss check: form = {F.fmt(v)} but gloss = {F.fmt(g) if g is F.BH else g}")
                    return
                continue
            if not F.equal(v, complex(g), node.get("equality", "≐")):
                rep.fail(nid, f"gloss check: form = {F.fmt(v)} but gloss {gloss} = {F.fmt(complex(g))} at {env}")
                return
    rep.ok()


def check_derivations(node: N.Node, rep: Report, rng, trials):
    nid = node.id
    text = node.sections.get("Derivation", "")
    tables = N.parse_tables(text)
    for t in tables:
        if not t:
            continue
        header = [c.lower() for c in t[0]]
        if header and header[0] == "statement":
            continue  # prose/meta derivation: not shadow-checked
        rows = t[1:] if header and header[0] == "form" else t
        prev = None
        for i, r in enumerate(rows):
            cell = r[0].strip().strip("`").strip() if r else ""
            rule = r[1] if len(r) > 1 else ""
            f = parse_or_none(cell)
            if rule.strip().lower() in NAMING_RULES:
                continue  # a naming row (A × B, S(A), −3 …): standard notation, not a form
            if f is None:
                rep.fail(nid, f"derivation row {i+1} does not parse: {cell!r}")
                prev = None
                continue
            if rule.strip().lower() == "given" or prev is None:
                prev = f
                continue
            ok, msg = check_equal_forms(prev, f, node, rng, trials)
            if not ok:
                rep.fail(nid, f"derivation step {i+1} is not an equality: {msg}")
            else:
                rep.ok()
            prev = f


def check_witness(node: N.Node, rep: Report):
    w = node.get("witness")
    if not w:
        return
    path = os.path.join(ROOT, w)
    if not os.path.exists(path):
        rep.fail(node.id, f"witness script missing: {w}")
        return
    proc = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=600)
    if proc.returncode != 0:
        rep.fail(node.id, f"witness {w} exited {proc.returncode}: {proc.stdout[-300:]} {proc.stderr[-300:]}")
    else:
        rep.ok()


def check_orders(nodes, rep: Report):
    seen = {}
    for n in nodes.values():
        o = n.get("order")
        if o in seen:
            rep.fail(n.id, f"walk order {o} duplicates {seen[o]}")
        seen[o] = n.id
    re_entries = [n.id for n in nodes.values() if n.get("reentry")]
    if len(re_entries) > 1:
        rep.fail("chart", f"more than one re-entry edge: {re_entries}")


def check_census(rep: Report):
    rows, unassigned = C.run(write=True)
    listed = set()
    path = os.path.join(ROOT, "census", "open-forms.md")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r"\|\s*`([^`]+)`", line)
                if m:
                    try:
                        listed.add(F.to_string(F.parse(m.group(1))))
                    except Exception:
                        pass
    for s, cls in unassigned:
        canon = F.to_string(F.parse(s))
        if canon in listed:
            continue
        if cls == "undefined" and F.to_string(F.parse("[□]")) in listed:
            continue  # every undefined form contains [□]; the family is listed once
        rep.fail("census", f"{cls} form `{s}` is neither assigned to a node nor listed in census/open-forms.md")
    rep.ok()


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=20261003)
    ap.add_argument("--trials", type=int, default=40)
    ap.add_argument("--no-census", action="store_true")
    args = ap.parse_args(argv)
    rng = random.Random(args.seed)
    nodes = N.load_nodes(os.path.join(ROOT, "nodes"))
    rep = Report()
    check_orders(nodes, rep)
    for node in sorted(nodes.values(), key=lambda n: n.get("order", 0) if isinstance(n.get("order"), int) else 0):
        check_schema(node, nodes, rep)
        check_links(node, nodes, rep)
        check_dag(node, nodes, rep)
        check_law(node, rep, rng, args.trials)
        check_derivations(node, rep, rng, args.trials)
        check_witness(node, rep)
    if not args.no_census:
        check_census(rep)
    print(f"{len(nodes)} nodes · {rep.oks} checks passed · {len(rep.warns)} warnings · {len(rep.fails)} failures")
    for w in rep.warns:
        print("  warn:", w)
    for f in rep.fails:
        print("  FAIL:", f)
    return 0 if not rep.fails else 1


if __name__ == "__main__":
    sys.exit(main())
