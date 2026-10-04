"""prover.py — a derivation checker for James forms: does the cited law really take one row to the next?

The engine's shadow check (check.py) verifies that consecutive rows of a derivation are equal in ℂ; it does not
verify that the rule a row cites licenses the step. This module does: a row is *licensed* when the next form is
obtained from the previous one by applying a cited law — as a rewrite, in either direction, at some position,
once or a small number of times. Matching is associative-commutative, because a form is a multiset of
boundaries; variables of a law match sub-multisets (forms), possibly void unless the law says otherwise.

It is also the receipt prover of 𝕁₁ (LEGISLATION 30c): j1.py grades each licensed step as strict, witnessed
(a receipt on the tape) or imported, from the rule it used and the position it used it at.

No dependencies beyond the standard library and forms.py.
"""
from __future__ import annotations
import itertools
from collections import Counter
from dataclasses import dataclass, field
from typing import Iterator, Optional

import forms as F

Form = tuple

# ----------------------------------------------------------------------------- matching


def _is_var(ch) -> bool:
    return ch[0] == F.VAR


def _mult(form: Form) -> Counter:
    return Counter(form)


def _elements(c: Counter) -> Form:
    return F.canon(tuple(c.elements()))


def match(pattern: Form, subject: Form, env: Optional[dict] = None, nonempty: frozenset = frozenset()) -> Iterator[dict]:
    """Yield every substitution σ (name -> Form) with substitute(pattern, σ) == subject, extending env.
    Variables match sub-multisets of the subject at their level (the void sub-multiset too, unless the
    variable is in `nonempty`)."""
    env = dict(env or {})
    concrete = [ch for ch in pattern if not _is_var(ch)]
    var_occ = Counter(ch[1] for ch in pattern if _is_var(ch))
    yield from _match_concrete(concrete, 0, _mult(subject), env, var_occ, nonempty)


def _match_concrete(concrete, i, remaining: Counter, env, var_occ: Counter, nonempty):
    if i == len(concrete):
        yield from _match_vars(remaining, env, var_occ, nonempty)
        return
    pch = concrete[i]
    kind, psub = pch
    tried = set()
    for sch in list(remaining.elements()):
        if sch[0] != kind or sch in tried:
            continue
        tried.add(sch)
        for env2 in match(psub, sch[1], env, nonempty):
            rem2 = remaining.copy()
            rem2[sch] -= 1
            if rem2[sch] == 0:
                del rem2[sch]
            yield from _match_concrete(concrete, i + 1, rem2, env2, var_occ, nonempty)


def _match_vars(remaining: Counter, env, var_occ: Counter, nonempty):
    # bound variables consume their value, once per occurrence
    rem = remaining.copy()
    unbound = []
    for name, c in var_occ.items():
        if name in env:
            need = Counter()
            for _ in range(c):
                need.update(env[name])
            if any(rem[k] < v for k, v in need.items()):
                return
            rem -= need
        else:
            unbound.append((name, c))
    if not unbound:
        if not rem:
            yield env
        return
    # distribute the leftover among the unbound variables (each element to one variable); an occurrence count
    # c means the variable's value appears c times, so the share must be divisible by c
    names = [n for n, _ in unbound]
    counts = dict(unbound)
    elems = list(rem.elements())
    if len(elems) > 14 and len(names) > 1:
        # too many assignments to enumerate blindly: give everything to each variable in turn, or split by
        # the cheapest rule — the chart's rows never need a genuine many-way split of a long multiset
        candidates = []
        for n in names:
            candidates.append({m: ([] if m != n else elems) for m in names})
    else:
        candidates = ({n: [] for n in names} for _ in [0])
        candidates = []
        for assignment in itertools.product(range(len(names)), repeat=len(elems)):
            shares = {n: [] for n in names}
            for e, j in zip(elems, assignment):
                shares[names[j]].append(e)
            candidates.append(shares)
    seen = set()
    for shares in candidates:
        env2 = dict(env)
        ok = True
        for n in names:
            share = Counter(shares[n])
            c = counts[n]
            if any(v % c for v in share.values()):
                ok = False
                break
            value = _elements(Counter({k: v // c for k, v in share.items()}))
            if not value and n in nonempty:
                ok = False
                break
            env2[n] = value
        if not ok:
            continue
        key = tuple(sorted((n, env2[n]) for n in names))
        if key in seen:
            continue
        seen.add(key)
        yield env2


# ----------------------------------------------------------------------------- rules and rewriting


@dataclass(frozen=True)
class Rule:
    id: str                 # node id (or a synthetic name)
    lhs: Form
    rhs: Form
    nonempty: frozenset = frozenset()
    label: str = ""

    def oriented(self):
        """The two orientations, as (direction, from, to); a bare-variable side is not used as a redex
        (it would match everything) — that orientation is only reachable backwards."""
        out = []
        if not _bare_var(self.lhs):
            out.append(("→", self.lhs, self.rhs))
        if not _bare_var(self.rhs):
            out.append(("←", self.rhs, self.lhs))
        return out


def _bare_var(form: Form) -> bool:
    return len(form) == 1 and _is_var(form[0]) or len(form) == 0


@dataclass(frozen=True)
class Step:
    rule: str
    direction: str          # → (law left to right) or ←
    path: tuple             # boundary kinds from the root down to the multiset the redex sits in
    env: tuple              # the substitution, as sorted (name, Form) pairs
    redex: Form             # the matched sub-multiset (instantiated lhs)
    result: Form            # the instantiated rhs


def rewrite_all(form: Form, rule: Rule, limit: int = 4000) -> list:
    """Every one-step rewrite of `form` by `rule` (either orientation, any position): list of (new_form, Step)."""
    out = []
    for direction, frm, to in rule.oriented():
        _rewrite_at(form, (), rule, direction, frm, to, out, limit)
        if len(out) >= limit:
            break
    return out


def _rewrite_at(form: Form, path: tuple, rule: Rule, direction: str, frm: Form, to: Form, out: list, limit: int):
    # at this level: match frm against a sub-multiset of form (context variable _C takes the rest)
    ctx = frm + ((F.VAR, "_C"),)
    for env in match(ctx, form, None, rule.nonempty):
        rest = env.pop("_C")
        red = F.substitute(frm, env)
        res = F.substitute(to, env)
        new_here = F.canon(rest + res)
        out.append((_rebuild(form, path, new_here) if False else new_here, Step(rule.id, direction, path, tuple(sorted(env.items())), red, res)))
        if len(out) >= limit:
            return
    # inside each boundary
    seen = set()
    for i, ch in enumerate(form):
        if _is_var(ch) or ch in seen:
            continue
        seen.add(ch)
        sub_out = []
        _rewrite_at(ch[1], path + (ch[0],), rule, direction, frm, to, sub_out, limit)
        for new_sub, step in sub_out:
            lst = list(form)
            lst[i] = (ch[0], new_sub)
            out.append((F.canon(tuple(lst)), step))
            if len(out) >= limit:
                return


def _rebuild(form, path, new_here):  # kept for clarity; rebuilding is done by the recursion above
    return new_here


def rewrite_with_rules(form: Form, rules: list) -> list:
    out = []
    for r in rules:
        out.extend(rewrite_all(form, r))
    return out


# ----------------------------------------------------------------------------- row checking


@dataclass
class Licence:
    ok: bool
    steps: list = field(default_factory=list)   # the Step objects, in order from prev to cur
    note: str = ""


def distance(a: Form, b: Form) -> int:
    """A structural distance between two forms: leftover children after pairing, weighted by size."""
    ca, cb = Counter(a), Counter(b)
    common = ca & cb
    ra, rb = list((ca - common).elements()), list((cb - common).elements())
    if not ra and not rb:
        return 0
    total = 0
    # pair same-kind leftovers greedily by distance
    used = set()
    for x in ra:
        best = None
        for j, y in enumerate(rb):
            if j in used or y[0] != x[0] or _is_var(x) or _is_var(y):
                continue
            d = distance(x[1], y[1])
            if best is None or d < best[0]:
                best = (d, j)
        if best is None:
            total += 1 + (F.size(x[1]) if not _is_var(x) else 0)
        else:
            used.add(best[1])
            total += best[0]
    for j, y in enumerate(rb):
        if j not in used:
            total += 1 + (F.size(y[1]) if not _is_var(y) else 0)
    return total


def rewrites_toward(form: Form, target: Form, rules: list, limit: int = 3000, allow=None) -> list:
    """One-step rewrites of `form` by `rules`, tried at this level and inside every child that differs from
    `target` (a rewrite inside a child both forms share would not bring them closer). Each differing child is
    guided toward the most similar differing child of the target."""
    out = []
    for r in rules:
        for direction, frm, to in r.oriented():
            ctx = frm + ((F.VAR, "_C"),)
            for env in match(ctx, form, None, r.nonempty):
                rest = env.pop("_C")
                red = F.substitute(frm, env)
                if not red:
                    continue  # a redex that is nothing (every variable void) rewrites nothing into something: noise
                res = F.substitute(to, env)
                step = Step(r.id, direction, (), tuple(sorted(env.items())), red, res)
                if allow is not None and not allow(step):
                    continue
                out.append((F.canon(rest + res), step))
                if len(out) >= limit:
                    return out
    ca, cb = Counter(form), Counter(target)
    common = ca & cb
    ra = [x for x in (ca - common).elements() if not _is_var(x)]
    rb = [y for y in (cb - common).elements() if not _is_var(y)]
    done = set()
    for x in ra:
        if x in done:
            continue
        done.add(x)
        cands = [y for y in rb if y[0] == x[0]]
        # with no counterpart of the same kind in the target the child must still be rewritten (it may be about
        # to disappear, e.g. by a counit or a cancellation): descend unguided
        y_sub = min(cands, key=lambda y: distance(x[1], y[1]))[1] if cands else ()
        for new_sub, step in rewrites_toward(x[1], y_sub, rules, limit, allow=_shift_allow(allow, x[0])):
            lst = list(form)
            lst[lst.index(x)] = (x[0], new_sub)
            out.append((F.canon(tuple(lst)), Step(step.rule, step.direction, (x[0],) + step.path, step.env, step.redex, step.result)))
            if len(out) >= limit:
                return out
    return out


def _shift_allow(allow, kind):
    """The predicate sees paths from the root: prepend this level's boundary kind for the recursive call."""
    if allow is None:
        return None
    return lambda step: allow(Step(step.rule, step.direction, (kind,) + step.path, step.env, step.redex, step.result))


def licence(prev: Form, cur: Form, rules: list, max_steps: int = 14, beam: int = 8, allow=None) -> Licence:
    """Is `cur` obtained from `prev` by at most `max_steps` applications of the given rules? One step is decided
    exactly; longer chains by a greedy beam search guided by the structural distance, run from both ends.
    `allow(step)` restricts the steps that may be used (the receipt prover grades by phases)."""
    if prev == cur:
        return Licence(True, [], "identity")
    if not rules:
        return Licence(False, [], "no rule cited")
    for a, b, back in ((prev, cur, False), (cur, prev, True)):
        res = _greedy(a, b, rules, max_steps, beam, _flip_allow(allow) if back else allow)
        if res is not None:
            steps = _reverse_steps(res) if back else res
            return Licence(True, steps, f"{len(steps)} step(s)")
    return Licence(False, [], f"not reached in {max_steps} step(s) by {', '.join(sorted({r.id for r in rules}))}")


def _flip_allow(allow):
    """Searching backwards, a step is the forward step with the opposite orientation (and redex/result swapped)."""
    if allow is None:
        return None
    return lambda s: allow(Step(s.rule, "←" if s.direction == "→" else "→", s.path, s.env, s.result, s.redex))


def _greedy(a: Form, b: Form, rules: list, max_steps: int, beam: int, allow=None):
    frontier = [(a, [])]
    seen = {a}
    for _ in range(max_steps):
        scored = []
        for f, steps in frontier:
            for g, step in rewrites_toward(f, b, rules, allow=allow):
                if g == b:
                    return steps + [step]
                if g in seen:
                    continue
                seen.add(g)
                scored.append((distance(g, b), g, steps + [step]))
        if not scored:
            return None
        scored.sort(key=lambda t: (t[0], F.size(t[1])))
        frontier = [(g, st) for _, g, st in scored[:beam]]
    return None


def _reverse_steps(steps: list) -> list:
    """Steps found from cur toward prev, read forwards: the same rules in the opposite orientation, reversed."""
    out = []
    for s in reversed(steps):
        out.append(Step(s.rule, "←" if s.direction == "→" else "→", s.path, s.env, s.result, s.redex))
    return out


# ----------------------------------------------------------------------------- rules from node laws


def rule_from_law(node_id: str, law: str, nonempty=()) -> Optional[Rule]:
    """A node's `law:` as a rewrite rule, when it is an equation between two parseable forms."""
    if "≐" not in law and "≡" not in law and "≃" not in law:
        return None
    sym = "≐" if "≐" in law else ("≡" if "≡" in law else "≃")
    l, r = (x.strip() for x in law.split(sym, 1))
    try:
        lf, rf = F.parse(l), F.parse(r)
    except Exception:
        return None
    return Rule(node_id, lf, rf, frozenset(nonempty), law)


if __name__ == "__main__":
    # smoke tests
    inv = Rule("Z.inversion", F.parse("A <A>"), F.parse("void"))
    dist = Rule("mult.distribution", F.parse("(A [B C])"), F.parse("(A [B]) (A [C])"), frozenset({"B", "C"}))
    counit = Rule("mult.counit", F.parse("([A])"), F.parse("A"))
    unit = Rule("mult.unit", F.parse("[(A)]"), F.parse("A"))
    card = Rule("mult.cardinality", F.parse("A A"), F.parse("([A] [oo])"))
    tests = [
        ("B A <A>", "B", [inv]),
        ("B", "B C <C>", [inv]),
        ("(X [Y Z])", "(X [Y]) (X [Z])", [dist]),
        ("(([[A]] [ooo]))", "(([[A]] [o]) ([[A]] [o]) ([[A]] [o]))", [dist]),
        ("<([B])>", "<B>", [counit]),
        ("[([A][B])]", "[A][B]", [unit]),
        ("J J", "([J] [oo])", [card]),
        ("(A J J J J)", "(A ([J] [oo]) J J)", [card]),
        ("[A] [B]", "[A B]", [unit]),  # must fail: not a law
    ]
    for p, c, rules in tests:
        L = licence(F.parse(p), F.parse(c), rules)
        print(f"{p!r:34} -> {c!r:40} {L.ok} {L.note} {[ (s.rule, s.direction, s.path) for s in L.steps]}")
