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
import nodes as N
import schema as S  # noqa: E402
import licences as LC  # noqa: E402
import j1 as J1  # noqa: E402
import census as C  # noqa: E402

ROOT = os.path.dirname(HERE)
BANDS = {"K", "1–2", "3–5", "6–8", "9–12", "beyond"}
REQUIRED = ["id", "title", "type", "level", "kind", "rung", "order", "setting", "equality", "domain", "law", "units",
            "holds", "readings", "status", "verified", "known_since", "entered", "guide", "band", "uses", "see_also",
            "aliases", "concepts", "understood", "reentry"]
NAMING_RULES = {"name"}
ALLOWED_RULES = {"given", "medium", "substitution", "congruence", "definition", "name", "lemma", "hypothesis"}


class Report:
    def __init__(self):
        self.fails, self.warns, self.oks = [], [], 0

    def fail(self, nid, msg):
        line = f"{nid}: {msg}"
        if line not in self.fails:
            self.fails.append(line)

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
    if m.get("type") == "schema":
        if not m.get("schema_range"):
            rep.fail(nid, "schema nodes need schema_range (e.g. n=2..8)")
        if m.get("status") != "NATIVE-BY-SCHEMA":
            rep.fail(nid, "schema nodes have status NATIVE-BY-SCHEMA")
        if not N.parse_tables(node.sections.get("Derivation", "")):
            rep.fail(nid, "schema nodes need a derivation table (the induction step)")
        uses = m.get("uses") or []
        if "N.induction" not in uses and not any(u in nodes and nodes[u].get("type") == "schema" for u in uses):
            rep.fail(nid, "a schema cites [[N.induction]] in its hypothesis row, or rests on another schema (the price of the meta-move)")
        text = node.sections.get("Derivation", "")
        has_hyp = any(len(r) > 1 and "hypothesis" in rule_tokens(r[1]) for t in N.parse_tables(text) for r in t[1:])
        try:
            envs = S.parse_range(m.get("schema_range", ""))
            bases = S.base_values(text)
        except ValueError as ex:
            rep.fail(nid, f"schema_range: {ex}")
            envs, bases = [], {}
        if has_hyp and not bases:
            rep.fail(nid, "an induction (a `hypothesis` row) needs a base-case table headed `| form (n = 1) | rule | note |`")
        if has_hyp and "N.induction" not in uses:
            rep.fail(nid, "a `hypothesis` row cites [[N.induction]]: the passage to all n is the gap, and it is priced")
        if len(bases) > 1:
            rep.fail(nid, f"base cases in more than one parameter: {sorted(bases)}")
        for var, vals in bases.items():
            if envs and var not in envs[0]:
                rep.fail(nid, f"base case in {var}, which schema_range does not bind")
                continue
            seen = sorted({e[var] for e in envs})
            for v in vals:
                if v not in seen:
                    rep.fail(nid, f"base case {var} = {v} lies outside schema_range, so it is never checked")
            if seen and has_hyp and seen[0] not in vals:
                rep.fail(nid, f"the induction starts at {var} = {seen[0]} but the base case is {var} = {vals[0]}")
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


SETTINGS = ["classical", "J1", "JH", "JO", "JP"]
READINGS = ["C", "finset", "lambda", "CC", "logic"]


def check_tables_agree(node: N.Node, rep: Report):
    """The body's 'Settings and readings' tables must agree with the front-matter holds/readings maps."""
    nid = node.id
    text = node.sections.get("Settings and readings", "")
    tables = N.parse_tables(text)
    if not tables:
        return
    meta_h = node.get("holds") or {}
    meta_r = node.get("readings") or {}
    for t in tables:
        if not t:
            continue
        head = [c.lower() for c in t[0]]
        if not head or head[0] not in ("setting", "reading"):
            continue
        is_setting = head[0] == "setting"
        universe = SETTINGS if is_setting else READINGS
        meta = meta_h if is_setting else meta_r
        seen = set()
        for row in t[1:]:
            if len(row) < 2:
                continue
            names = [x.strip() for x in row[0].replace("and", ",").split(",") if x.strip()]
            cell = row[1].strip().split()[0] if row[1].strip() else ""
            cell = cell.strip("*`")
            if names == ["all"]:
                names = list(universe)
            elif names == ["others"]:
                names = [u for u in universe if u not in seen]
            for nme in names:
                if nme not in universe:
                    rep.fail(nid, f"settings/readings table names unknown column {nme!r}")
                    continue
                seen.add(nme)
                if nme in meta and str(meta[nme]) != cell:
                    rep.fail(nid, f"front matter says {nme}: {meta[nme]} but the body table says {cell}")
        for nme in universe:
            if nme not in seen and nme in meta:
                rep.fail(nid, f"{'settings' if is_setting else 'readings'} table has no row for {nme}")


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


def rule_tokens(rule: str):
    """The rule words of a derivation row's rule cell, lower-cased, with the [[links]] removed."""
    return [r.lower() for r in re.split(r"[,;]\s*|\s+", N.LINK.sub("", rule).strip()) if r]


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
    if law.startswith(("GAP", "DISCIPLINE")) or node.get("kind") in ("discipline", "declaration", "guard"):
        return  # a rule about derivations, not an equation between forms
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
    firsts, lasts = [], []
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
            rules_named = rule_tokens(rule)
            for rn in rules_named:
                if rn not in ALLOWED_RULES and rn not in ("—", "-", ""):
                    rep.fail(nid, f"derivation row {i+1} uses unknown rule {rn!r}")
            if rule.strip().lower() == "given" or prev is None:
                prev = f
                firsts.append(f)
                continue
            ok, msg = check_equal_forms(prev, f, node, rng, trials)
            if not ok:
                rep.fail(nid, f"derivation step {i+1} is not an equality: {msg}")
            else:
                rep.ok()
            if "hypothesis" in rules_named:
                note = r[2] if len(r) > 2 else ""
                if node.get("type") != "schema":
                    rep.fail(nid, f"derivation row {i+1}: the rule `hypothesis` belongs to schema nodes")
                elif "[[N.induction]]" not in note + rule:
                    rep.fail(nid, f"derivation row {i+1}: a hypothesis row cites [[N.induction]]")
                else:
                    hok, hmsg = hypothesis_ok(prev, f, node)
                    if not hok:
                        rep.fail(nid, f"derivation row {i+1}: {hmsg}")
                    else:
                        rep.ok()
            if node.get("type") != "decree":
                seam = check_seam(prev, f, node, rep, i + 1, rng, trials)
                if seam:
                    rep.ok()
            prev = f
        if prev is not None:
            lasts.append(prev)
    # endpoints: for an object-level theorem the tables must start at one side of the law and end at the other
    law = str(node.get("law", ""))
    if node.get("type") in ("theorem", "schema") and node.get("level") == "object" and "≐" in law and firsts and lasts:
        lhs, rhs = (parse_or_none(x.strip()) for x in law.split("≐", 1))
        if lhs is not None and rhs is not None:
            def hits(cands, target):  # syntactic: the same canonical form, not merely the same value
                return any(c == target for c in cands)
            forward = hits(firsts, lhs) and hits(lasts, rhs)
            backward = hits(firsts, rhs) and hits(lasts, lhs)
            if not (forward or backward):
                rep.fail(nid, f"derivation tables do not start at one side of the law and end at the other (as forms): law {F.to_string(lhs, True)} ≐ {F.to_string(rhs, True)}; first rows {[F.to_string(x, True) for x in firsts]}; last rows {[F.to_string(x, True) for x in lasts]}")
            else:
                rep.ok()


# ----------------------------------------------------------------------------- seam decree (mult.seam-decree)
# Enforcement is semantic, as the decree itself is: find every unit step in a row's difference and refuse it if its
# content leaves the principal strip on wide sampling while the position is not absorbing (mult.seam-signature says
# why no syntactic test can do this job).

def absorbing(path) -> bool:
    """A redex position is absorbing if, after stripping angle boundaries from the end of the path,
    the nearest enclosing boundary is an instance."""
    p = list(path)
    while p and p[-1] == F.ANGLE:
        p.pop()
    return bool(p) and p[-1] == F.ROUND


def _unit_shaped(e):
    return e[0] == F.SQUARE and len(e[1]) == 1 and e[1][0][0] == F.ROUND


def find_unit_steps(f1, f2, path=()):
    """Walk the whole difference between two forms and collect every unit step [(X)] <-> X it contains,
    as (path, X). Same-kind differing children are paired (trying all pairings when ambiguous, keeping the
    one that explains the most) and recursed into; leftovers are matched as unit steps where possible.
    Returns (steps, unexplained) where unexplained counts leftover children no rule of ours accounts for."""
    from collections import Counter
    import itertools
    k1, k2 = Counter(f1), Counter(f2)
    common = k1 & k2
    r1 = list((k1 - common).elements())
    r2 = list((k2 - common).elements())
    if not r1 and not r2:
        return [], 0
    # 1. unit steps at this level: [(X)] on one side whose X-children all lie on the other side
    steps = []
    def take_units(src, dst):
        nonlocal steps
        dst_c = Counter(dst)
        rest = []
        for e in src:
            if _unit_shaped(e):
                cx = Counter(e[1][0][1])
                # cx empty is the unit on nothing, [()] <-> void. It is deliberately NOT collected: SPEC §5.4 exempts
                # void/hole content from the decree (`[o] ≐ void` is a theorem of the hole rules), and a vacuous match
                # here would preempt the pairing of a genuine redex standing next to it (e.g. [[(o)]] -> [o]).
                if cx and all(dst_c[k] >= v for k, v in cx.items()):
                    dst_c -= cx
                    steps.append((path, e[1][0][1]))
                    continue
            rest.append(e)
        return rest, list(dst_c.elements())
    r1, r2 = take_units(r1, r2)
    r2, r1 = take_units(r2, r1)
    # 2. pair remaining same-kind boundaries and recurse. The cost of pairing a with b is structural — the number
    # of children the recursive match leaves unexplained — never a string similarity, so a decoy sibling whose
    # content merely resembles the result of a unit step does not steal the pairing. Each kind is independent
    # (costs add), so the best assignment is chosen kind by kind: exactly, by enumerating the injections of the
    # smaller side into the larger when there are at most 20 000 of them, and greedily by cost beyond that.
    by_kind1, by_kind2 = {}, {}
    for e in r1:
        by_kind1.setdefault(e[0], []).append(e)
    for e in r2:
        by_kind2.setdefault(e[0], []).append(e)
    kinds = [k for k in (F.ROUND, F.SQUARE, F.ANGLE) if k in by_kind1 and k in by_kind2]
    best_steps, used_total, sub_unexplained_total = [], 0, 0
    for k in kinds:
        a, b = by_kind1[k], by_kind2[k]
        if len(a) > len(b):
            a, b, swapped = b, a, True
        else:
            swapped = False
        n, m = len(a), len(b)
        cost, stepsof = {}, {}
        for i in range(n):
            for j in range(m):
                x, y = (b[j][1], a[i][1]) if swapped else (a[i][1], b[j][1])
                st, un = find_unit_steps(x, y, path + (k,))
                cost[i, j], stepsof[i, j] = un, st
        count = 1
        for t in range(n):
            count *= (m - t)
        best = None
        if count <= 20000:
            for perm in itertools.permutations(range(m), n):
                pairs = list(zip(range(n), perm))
                tot = sum(cost[p] for p in pairs)
                nst = sum(len(stepsof[p]) for p in pairs)
                if best is None or tot < best[0] or (tot == best[0] and nst > best[1]):
                    best = (tot, nst, pairs)
        else:
            order = sorted(cost, key=lambda p: (cost[p], -len(stepsof[p])))
            ua, ub, pairs = set(), set(), []
            for i, j in order:
                if i in ua or j in ub:
                    continue
                ua.add(i); ub.add(j); pairs.append((i, j))
                if len(pairs) == n:
                    break
            best = (sum(cost[p] for p in pairs), sum(len(stepsof[p]) for p in pairs), pairs)
        for p in best[2]:
            best_steps += stepsof[p]
        sub_unexplained_total += best[0]
        used_total += 2 * len(best[2])
    best_unexplained = len(r1) + len(r2) - used_total + sub_unexplained_total
    return steps + best_steps, best_unexplained


def seam_env(names, domain, rng):
    """Sampling for the seam check: wide, log-uniform over the whole domain, with boundary probes."""
    import math
    env = {}
    for n in sorted(names):
        r = rng.random()
        if domain == "natural":
            env[n] = complex(rng.randint(1, 12))
        elif domain == "positive":
            env[n] = complex(math.exp(rng.uniform(math.log(0.01), math.log(100.0))))
        elif domain == "real":
            env[n] = complex(math.exp(rng.uniform(math.log(0.01), math.log(100.0))) * rng.choice((-1, 1)))
        elif domain == "negative":
            env[n] = complex(-math.exp(rng.uniform(math.log(0.01), math.log(100.0))))
        elif domain == "complex":
            env[n] = complex(math.exp(rng.uniform(-3, 3)) * rng.choice((-1, 1)), math.exp(rng.uniform(-3, 3)) * rng.choice((-1, 1)))
        else:
            raise ValueError(domain)
    return env


PROBES = {"natural": [1, 2, 3, 7, 12], "positive": [0.01, 0.5, 0.999, 1.0, 1.001, 2.0, 10.0, 100.0],
          "negative": [-100.0, -2.0, -1.001, -1.0, -0.999, -0.5, -0.01],
          "real": [-100.0, -2.0, -1.0, -0.5, 0.5, 1.0, 2.0, 100.0], "complex": [1j, -1j, -1 + 0j, 2 + 3j]}


def off_strip(x, node: N.Node, rng, trials: int):
    """Does the content x leave the principal strip (-π, π] on any sampled instantiation of its variables?
    Values whose evaluation overflows are reported as unknown (counted as off-strip, conservatively)."""
    import math
    names = sorted(F.variables(x))
    domain = node.get("domain", "positive")
    envs = [seam_env(names, domain, rng) for _ in range(trials if names else 1)]
    if names:
        for p in PROBES.get(domain, []):
            envs.append({n: complex(p) for n in names})
    for env in envs:
        try:
            v = F.evaluate(x, env)
        except (F.Undefined, F.Excluded):
            continue
        except OverflowError:
            return True, env
        if v is F.BH:
            continue
        if v.imag > math.pi + 1e-12 or v.imag <= -math.pi + 1e-9:
            return True, env
    return False, None


def check_seam(prev, cur, node: N.Node, rep: Report, rownum: int, rng=None, trials: int = 60):
    """Enforce mult.seam-decree on a derivation step: every unit step [(X)] <-> X anywhere in the row's
    difference is admissible only if X is on the principal strip (on every sampled instance, over the whole
    domain) or the redex is in an absorbing position. Returns None when the row contains no unit step."""
    import random
    rng = rng or random.Random(7)
    steps, _ = find_unit_steps(prev, cur)
    if not steps:
        return None
    for path, x in steps:
        if absorbing(path):
            continue
        bad, env = off_strip(x, node, rng, trials)
        if bad:
            where = f" at {{{', '.join(f'{k}={F.fmt(v)}' for k, v in env.items())}}}" if env else ""
            rep.fail(node.id, f"derivation step {rownum}: unit step on content {F.to_string(x, True)!r} off the principal strip{where}, outside an absorbing position — refused by mult.seam-decree")
            return False
    return True


def seam_reliance(node: N.Node, rng=None, trials: int = 60):
    """Which clauses of mult.seam-decree a derivation relies on (LEGISLATION Amendment A2):
    'content'  — a unit step at a non-absorbing position (admitted only because its content stays on the strip,
                 which the ℂ reading certifies);
    'position' — a unit step in an absorbing position whose content leaves the strip for some sampled value of the
                 node's domain (a *seam step*: the local equation is false and only the enclosing instance saves it).
    A unit step that is absorbing AND on the strip relies on neither clause and is free. Returns a set."""
    import random
    rng = rng or random.Random(11)
    rel = set()
    for t in N.parse_tables(node.sections.get("Derivation", "")):
        if not t or t[0][0].lower() != "form":
            continue
        prev = None
        for r in t[1:]:
            cell = r[0].strip().strip("`").strip() if r else ""
            rule = r[1] if len(r) > 1 else ""
            if rule.strip().lower() in NAMING_RULES:
                continue
            f = parse_or_none(cell)
            if f is None:
                prev = None
                continue
            if prev is not None and rule.strip().lower() != "given":
                steps, _ = find_unit_steps(prev, f)
                for path, x in steps:
                    try:
                        v = F.evaluate(x, {n: 1.7 for n in F.variables(x)})
                    except (F.Undefined, F.Excluded, OverflowError):
                        v = None
                    if v is F.BH or not x:
                        continue  # void or hole content: [(void)] ≐ void and [(□)] ≐ □ are theorems of the hole rules
                        # (mult.unit-law, mult.hole-instance + mult.black-hole), so the step relies on neither clause — SPEC §5.4
                    if not absorbing(path):
                        rel.add("content")
                    else:
                        bad, _env = off_strip(x, node, rng, trials)
                        if bad:
                            rel.add("position")
            prev = f
    return rel


def schema_instances(node: N.Node):
    """The engine-checked instances of a schema node: one Node copy per parameter environment in schema_range,
    with the law and the Derivation expanded. At a base-case value the instance's derivation is the base table
    alone; at every other value it is the step tables alone (SPEC §2.7), so a `hypothesis` row always refers to
    a value at or above the base. The instance carries the template and its environment for the hypothesis check."""
    out = []
    text = node.sections.get("Derivation", "")
    for env in S.parse_range(node.get("schema_range", "n=2..6")):
        meta = dict(node.meta)
        meta["law"] = S.expand(str(node.get("law", "")), env)
        meta["schema_env"] = env
        meta["schema_template"] = str(node.get("law", ""))
        secs = dict(node.sections)
        secs["Derivation"] = S.expand_derivation(text, env, keep_fixed="match")
        out.append(N.Node(id=f"{node.id}@{S.describe(env)}", path=node.path, meta=meta, sections=secs, body=node.body))
    return out


def _subtract(counter, sub):
    """Multiset difference, or None when sub is not contained in counter."""
    if any(counter[k] < v for k, v in sub.items()):
        return None
    return counter - sub


def rewrites_by(prev, cur, lhs, rhs) -> bool:
    """Is `cur` obtained from `prev` by replacing one occurrence of the multiset `lhs` by `rhs` (variables kept
    as literal atoms), at the root or inside exactly one boundary? A purely syntactic check."""
    from collections import Counter
    cp, cc = Counter(prev), Counter(cur)
    rest = _subtract(cp, Counter(lhs))
    if rest is not None and rest + Counter(rhs) == cc:
        return True
    # otherwise prev and cur must differ in exactly one child of the same kind; recurse into it
    only_p = list((cp - cc).elements())
    only_c = list((cc - cp).elements())
    if len(only_p) == 1 and len(only_c) == 1 and only_p[0][0] == only_c[0][0] and only_p[0][0] != F.VAR:
        return rewrites_by(only_p[0][1], only_c[0][1], lhs, rhs)
    return False


def hypothesis_ok(prev, cur, node: N.Node):
    """A `hypothesis` row of a schema instance must be the schema's own law at a smaller parameter in range,
    applied once in either direction. Returns (ok, message)."""
    env = node.get("schema_env")
    template = node.get("schema_template", "")
    if env is None or "≐" not in template:
        return False, "hypothesis rows belong to schema nodes"
    tl, tr = (x.strip() for x in template.split("≐", 1))
    tried = []
    for e2 in S.parse_range(node.get("schema_range", "")):
        if e2 == env or any(e2[k] > env[k] for k in env) or any(k not in e2 for k in env):
            continue
        try:
            lhs, rhs = F.parse(S.expand(tl, e2)), F.parse(S.expand(tr, e2))
        except Exception:
            continue
        tried.append(S.describe(e2))
        if rewrites_by(prev, cur, lhs, rhs) or rewrites_by(prev, cur, rhs, lhs):
            return True, S.describe(e2)
    return False, f"not the schema's law at any smaller parameter in range (tried {', '.join(tried) or 'none'})"


def check_guarded_by(node: N.Node, nodes, rep: Report, rng=None, trials: int = 60):
    """`guarded_by` is mechanical (Amendment A2): a node declares guarded_by: [mult.seam-decree] iff its derivation
    relies on a clause of the decree (seam_reliance non-empty) — and only then. A schema's reliance is the union over
    its instances."""
    nid = node.id
    if node.get("type") == "schema":
        rel = set()
        try:
            insts = schema_instances(node)
        except ValueError as ex:
            rep.fail(nid, f"schema does not expand: {ex}")
            return
        for inst in insts:
            rel |= seam_reliance(inst, rng, trials)
    else:
        rel = seam_reliance(node, rng, trials)
    declared = list(node.get("guarded_by", []) or [])
    for g in declared:
        if g not in nodes:
            rep.fail(nid, f"guarded_by refers to unknown node {g}")
        elif isinstance(node.get("order"), int) and isinstance(nodes[g].get("order"), int) and nodes[g].get("order") >= node.get("order"):
            rep.fail(nid, f"guarded_by {g} does not precede this node")
    if node.get("type") == "decree":
        return
    if rel and "mult.seam-decree" not in declared:
        rep.fail(nid, f"relies on the seam decree by {' and '.join(sorted(rel))}: must declare guarded_by: [mult.seam-decree]")
    elif not rel and "mult.seam-decree" in declared:
        rep.fail(nid, "declares guarded_by mult.seam-decree but no unit step relies on it (all unit steps absorbing and on the strip)")
    else:
        rep.ok()


J1_GRADES: dict = {}     # node id -> j1.Tape, filled in walk order (cited theorems are graded before their users)
J1_ROWS: list = []       # (node id, tape, hand cell) for census/j1-ledger.md
GRADED_TYPES = {"theorem", "schema"}


def check_licences(node: N.Node, nodes, rep: Report, cache: dict, rng, parent=None):
    """Every form row of a derivation must be obtained from the previous row by the rule it cites (tools/prover.py):
    the step is *licensed*, not merely value-equal. The search asks for the cheapest 𝕁₁ tape first (strict and
    absorbed steps, then posted, then anything), and the steps it finds grade the node in 𝕁₁ (tools/j1.py)."""
    if node.get("level") != "object":
        return None
    lic, unl, skip, details = LC.check_node(node, nodes, cache, phases=J1.phases(J1_GRADES))
    for ti, i, status, msg, _steps in details:
        if status == "UNLICENSED":
            rep.fail(node.id, f"derivation table {ti+1} row {i+1} is not licensed by the rule it cites: {msg}")
    rep.oks += lic
    if (parent or node).get("type") not in GRADED_TYPES:
        return None
    tape = J1.Tape()
    for ti, i, status, msg, steps in details:
        if status == "UNLICENSED":
            tape.worse("absent")
            tape.absent.append(f"row {i+1} unlicensed")
            continue
        row = J1.grade_steps(steps, node, J1_GRADES, rng)
        tape.receipts += row.receipts
        tape.absent += row.absent
        tape.worse(row.grade)
    return tape


# a hand-written J1 cell may say more than the derivation's grade, never less
J1_ACCEPT = {
    "holds": {"holds"},
    "holds-mod-Λ": {"holds-mod-Λ"},
    "guarded": {"holds", "holds-mod-Λ", "guarded"},      # a legislative guard (the stratification) may tighten a grade
    "replaced": {"holds", "holds-mod-Λ", "guarded", "fails"},  # replaced says what takes the law's place
    "fails": {"fails"},
}


def record_j1(node: N.Node, tape, rep: Report):
    """Store the computed grade and compare it with the node's hand-written J1 cell."""
    J1_GRADES[node.id] = tape
    hand = (node.get("holds") or {}).get("J1", "")
    J1_ROWS.append((node.id, tape, hand))
    if node.get("setting") != "classical":
        return
    if hand == "untested":
        rep.fail(node.id, f"J1 cell is untested but the receipt prover grades the derivation {tape.cell}: {J1.describe(tape)[:160]}")
    elif tape.cell not in J1_ACCEPT.get(hand, set()):
        rep.fail(node.id, f"J1 cell says {hand} but the receipt prover grades the derivation {tape.cell}: {J1.describe(tape)[:200]}")
    else:
        rep.ok()


def write_j1_ledger():
    path = os.path.join(ROOT, "census", "j1-ledger.md")
    out = ["# 𝕁₁ ledger — computed by the receipt prover (tools/j1.py)", "",
           "Grade of each derivation in 𝕁₁ (LEGISLATION 30): ≡ strict · absorbed (receipts paid by an instance) · posted (receipts on the tape, mod Λ) · import (a unit step under a square: sound only by the reading) · fails. Written by `tools/check.py`; do not edit.", "",
           "| node | computed cell | hand cell | tape |", "|---|---|---|---|"]
    for nid, tape, hand in J1_ROWS:
        out.append(f"| `{nid}` | {tape.cell} | {hand} | {J1.describe(tape).replace('|', '/')} |")
    open(path, "w").write("\n".join(out) + "\n")
    return path


def check_witness(node: N.Node, rep: Report):
    w = node.get("witness")
    if not w:
        return
    parts = str(w).split()
    path = os.path.join(ROOT, parts[0])
    if not os.path.exists(path):
        rep.fail(node.id, f"witness script missing: {parts[0]}")
        return
    proc = subprocess.run([sys.executable, path] + parts[1:], capture_output=True, text=True, timeout=600)
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
    ap.add_argument("--no-licences", action="store_true", help="skip the derivation checker (tools/prover.py)")
    args = ap.parse_args(argv)
    rng = random.Random(args.seed)
    nodes = N.load_nodes(os.path.join(ROOT, "nodes"))
    rep = Report()
    lic_cache = {}
    check_orders(nodes, rep)
    for node in sorted(nodes.values(), key=lambda n: n.get("order", 0) if isinstance(n.get("order"), int) else 0):
        check_schema(node, nodes, rep)
        check_links(node, nodes, rep)
        check_tables_agree(node, rep)
        check_dag(node, nodes, rep)
        check_guarded_by(node, nodes, rep, rng, max(60, args.trials))
        if node.get("type") == "schema":
            try:
                insts = schema_instances(node)
            except ValueError as ex:
                rep.fail(node.id, f"schema does not expand: {ex}")
                insts = []
            tape = J1.Tape() if insts else None
            for inst in insts:
                check_law(inst, rep, rng, max(10, args.trials // 2))
                check_derivations(inst, rep, rng, max(10, args.trials // 2))
                if not args.no_licences:
                    t = check_licences(inst, nodes, rep, lic_cache, rng, parent=node)
                    if t is not None:
                        tape.worse(t.grade)
                        seen = {(r.rule, r.where, r.grade, r.content) for r in tape.receipts}
                        for r in t.receipts:
                            if (r.rule, r.where, r.grade, r.content) not in seen:
                                tape.receipts.append(r)
                                seen.add((r.rule, r.where, r.grade, r.content))
                        tape.absent += [a for a in t.absent if a not in tape.absent]
            if tape is not None and not args.no_licences:
                record_j1(node, tape, rep)
        else:
            check_law(node, rep, rng, args.trials)
            check_derivations(node, rep, rng, args.trials)
            if not args.no_licences:
                tape = check_licences(node, nodes, rep, lic_cache, rng)
                if tape is not None:
                    record_j1(node, tape, rep)
        check_witness(node, rep)
    if not args.no_licences:
        write_j1_ledger()
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
