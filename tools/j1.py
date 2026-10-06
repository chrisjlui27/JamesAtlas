"""j1.py — the receipt tape: what each licensed step costs in 𝕁₁ (LEGISLATION 30; SPEC §5.5).

The derivation checker (prover.py) tells us which rule took a row to the next, in which orientation, at which
position. This module grades every such step for the enriched calculus 𝕁₁:

  strict     a strict rule — the counit ([A]) ≡ A, Distribution, Inversion, the medium, the hole rules — or a
             theorem whose own tape is empty; the unit on pole-valued content (the pole has no winding to record)
  absorbed   the unit [(A)] ↔ A, absorption (ω A) ↔ (A), or a theorem with receipts, applied directly inside an
             instance (through angles at most): the instance pays the receipt on the spot — value-exact; or a
             theorem whose own receipts were all absorbed (its reuse replays the paid moves)
  posted     a unit step or a posted theorem at depth 0 (through angles and juxtaposition only): the receipt
             stays on the tape; the two forms agree mod Λ
  import     a unit step or a posted theorem under a square before any instance, whose receipt is void on the
             whole domain: ≃ is not a congruence through [ ], so the step is sound only by that fact of the
             reading (the classical decree's by-content clause), which 𝕁₁ cannot see
  absent     under a square with a non-void receipt (the step is false in 𝕁₁), or a rule 𝕁₁ does not have

A node's 𝕁₁ grade is the worst grade among its steps. The `holds` cell it implies: strict or absorbed → holds;
posted → holds-mod-Λ; import → guarded; absent → fails.

Receipts are read in the 𝕁₁ reading (forms.OMEGA = 2πi: the log of exactly one is the chosen lift, every other
log principal — LEGISLATION 30b as amended). The receipt of a step is the lattice element the step forgets:
value(redex) − value(result) in units of ω, sampled over the node's domain; `?` when the content is the pole or
the difference is not a lattice element.
"""
from __future__ import annotations
import math
from dataclasses import dataclass, field

import forms as F
import prover as P

GRADE_ORDER = ["strict", "absorbed", "posted", "import", "absent"]
CELL_OF = {"strict": "holds", "absorbed": "holds", "posted": "holds-mod-Λ", "import": "guarded", "absent": "fails"}
BY_POSITION = {"absorbing": "absorbed", "depth-0": "posted", "under-square": "import"}

UNIT_RULES = {"mult.involution", "mult.log-of-one", "J1.unit"}     # rules whose unit-shaped steps post receipts
STRICT_J1 = {"J1.counit", "J1.closure", "J1.period-form"}            # strict rules of the J1 rung itself
ABSORB_J1 = {"J1.absorption", "J1.absorption-mirror"}                 # witnessed moves inside an instance
# The strict rules of 𝕁₁ among the trunk's axioms and primitives (theorems are graded from their derivations).
# Dominion is strict by LEGISLATION 30(f): the pole has no winding, so a unit step on pole-valued content posts
# nothing — see pole_valued().
STRICT_NODES = {"void.page", "void.space", "Z.inversion", "mult.distribution", "mult.hole-instance",
                "mult.zero-annihilates", "mult.dominion", "mult.black-hole"}
ABSENT_NODES: set = set()

OMEGA = 2j * math.pi


def _unit_shape(step: P.Step):
    """If the step is a unit step [(X)] ↔ X, return X's form; else None."""
    red, res = step.redex, step.result
    for a, b in ((red, res), (res, red)):
        if len(a) == 1 and a[0][0] == F.SQUARE and len(a[0][1]) == 1 and a[0][1][0][0] == F.ROUND:
            if F.canon(a[0][1][0][1]) == F.canon(b):
                return a[0][1][0][1]
    return None


def _counit_shape(step: P.Step) -> bool:
    red, res = step.redex, step.result
    for a, b in ((red, res), (res, red)):
        if len(a) == 1 and a[0][0] == F.ROUND and len(a[0][1]) == 1 and a[0][1][0][0] == F.SQUARE:
            if F.canon(a[0][1][0][1]) == F.canon(b):
                return True
    return False


def position_class(path: tuple) -> str:
    """Walk outward from the redex: angles are transparent; the first instance absorbs; the first square refuses."""
    for k in reversed(path):
        if k == F.ANGLE:
            continue
        if k == F.ROUND:
            return "absorbing"
        if k == F.SQUARE:
            return "under-square"
    return "depth-0"


def _in_j1_reading(fn, *args):
    old = F.OMEGA
    F.OMEGA = OMEGA
    try:
        return fn(*args)
    finally:
        F.OMEGA = old


PROBES = [1.0, -1.0, 0.5, 2.0, 1j]   # the exceptional points of the reading: where a content can be exactly one
GENERIC = 2.0                        # the other variables' value in a probe, so the tape names a readable point


def _sample(names, domain, rng, trials):
    """Random values of the node's domain — the generic points."""
    return [F.random_env(names, domain, rng) for _ in range(trials if names else 1)]


def _in_domain(p, domain: str) -> bool:
    if isinstance(p, complex):
        return domain == "complex"
    if domain == "natural":
        return p == int(p) and p >= 1
    if domain == "positive":
        return p > 0
    if domain == "negative":
        return p < 0
    return True  # real, complex


def _probes(names, domain, rng):
    """Probe environments: every variable at each probe value of the domain — the others at a generic value first,
    then random — and all variables equal to the same probe: the lattice points a random sampler never hits, where
    the log of exactly one reads ω."""
    names = sorted(names)
    if not names:
        return []
    out = []
    generic = -GENERIC if domain == "negative" else GENERIC
    for p in PROBES:
        if not _in_domain(p, domain):
            continue
        out.append({n: complex(p) for n in names})
        for n in names:
            fixed = {m: complex(generic) for m in names}
            fixed[n] = complex(p)
            out.append(fixed)
            env = F.random_env(names, domain, rng)
            env[n] = complex(p)
            out.append(env)
    return out


def pole_valued(x: F.Form, domain: str, rng, trials: int = 12) -> bool:
    """Does the content x evaluate to the pole on every sampled value (the hole, or a form dominion makes it)?"""
    if not x:
        return False
    names = F.variables(x)
    seen = False
    for env in _sample(names, domain, rng, trials):
        try:
            v = _in_j1_reading(F.evaluate, x, env)
        except (F.Undefined, F.Excluded, OverflowError):
            continue
        seen = True
        if v is not F.BH:
            return False
    return seen


def _single_instance(form: F.Form):
    return len(form) == 1 and form[0][0] == F.ROUND


def _k_at(redex, result, env):
    try:
        a = _in_j1_reading(F.evaluate, redex, env)
        b = _in_j1_reading(F.evaluate, result, env)
    except (F.Undefined, F.Excluded, OverflowError):
        return "skip"
    if a is F.BH or b is F.BH:
        return None
    k = (a - b) / OMEGA
    if abs(k.imag) > 1e-6 * (1 + abs(k)) or abs(k.real - round(k.real)) > 1e-6 * (1 + abs(k)):
        return None
    return int(round(k.real))


def receipt_values(redex: F.Form, result: F.Form, domain: str, rng, trials: int = 24, with_probes: bool = False):
    """The receipt of a step, in units of ω: value(redex) − value(result) in the 𝕁₁ reading, over the generic
    points of the domain. When both sides are a single instance the contents are compared instead (an absorbed
    period is invisible at the instance level and is exactly what the receipt records). An entry of None stands
    for `?` — the pole, or a difference that is not a lattice element. With with_probes=True the exceptional
    points (PROBES) are sampled as well and returned separately as {k: [env, …]} for the non-void ones."""
    if _single_instance(redex) and _single_instance(result):
        redex, result = redex[0][1], result[0][1]
    names = F.variables(redex) | F.variables(result)
    ks = set()
    for env in _sample(names, domain, rng, trials):
        k = _k_at(redex, result, env)
        if k != "skip":
            ks.add(k)
    if not with_probes:
        return ks
    exceptional = {}
    for env in _probes(names, domain, rng):
        k = _k_at(redex, result, env)
        if k != "skip" and k != 0:
            exceptional.setdefault(k, []).append(env)
    return ks, exceptional


@dataclass
class Receipt:
    rule: str
    content: str        # what the step rewrote, as a string
    where: str          # absorbing | depth-0 | under-square | inherited (a theorem's own tape) | pole (strict, 30f)
    grade: str          # strict (pole only) | absorbed | posted | import | absent
    k: set = field(default_factory=set)   # sampled receipt values in units of ω (None = ?)
    exceptional: dict = field(default_factory=dict)   # under a square: non-void receipts at probe points {k: [env…]}


@dataclass
class Tape:
    grade: str = "strict"
    receipts: list = field(default_factory=list)
    absent: list = field(default_factory=list)

    def worse(self, g: str):
        if GRADE_ORDER.index(g) > GRADE_ORDER.index(self.grade):
            self.grade = g

    def merge(self, other: "Tape", dedupe: bool = False):
        """Combine tapes. Within one derivation every receipt is kept (no contraction on the tape, L0); across a
        schema's instances the same step at the same position is one entry (dedupe=True)."""
        self.worse(other.grade)
        seen = {(r.rule, r.where, r.grade, r.content) for r in self.receipts} if dedupe else set()
        for r in other.receipts:
            if dedupe and (r.rule, r.where, r.grade, r.content) in seen:
                continue
            self.receipts.append(r)
            seen.add((r.rule, r.where, r.grade, r.content))
        self.absent += [a for a in other.absent if a not in self.absent]

    @property
    def cell(self) -> str:
        return CELL_OF[self.grade]

def _theorem_grade(step: P.Step, grades: dict):
    """The grade a theorem (or lemma table) contributes when used as a rule at this step's position."""
    g = grades.get(step.rule)
    if g is None:
        return "strict"  # an axiom of the setting, a definition, or a node without a derivation grade
    if g.grade in ("strict", "absorbed"):
        return g.grade
    if g.grade == "absent":
        return "absent"
    if g.grade == "import":
        return "import"  # the import sits inside the theorem; no position of use heals it
    where = position_class(step.path)
    if where == "under-square":
        return "import"  # refined at the use site by grade_steps: void receipt there → import, else fails
    return BY_POSITION[where]


def step_grade(step: P.Step, grades: dict, node=None, rng=None) -> str:
    """The 𝕁₁ grade of one licensed step, from its rule and position (the reading decides only pole-valued
    content, and whether an under-square receipt is void)."""
    x = _unit_shape(step)
    if x is not None and (step.rule in UNIT_RULES or step.rule.startswith("lemma") or step.rule == "hypothesis"):
        if node is not None and rng is not None and pole_valued(x, node.get("domain", "positive"), rng):
            return "strict"
        where = position_class(step.path)
        if where == "under-square" and node is not None and rng is not None:
            ks = receipt_values(step.redex, step.result, node.get("domain", "positive"), rng)
            return "import" if ks == {0} else "absent"  # void at the generic points: an import (exceptional points are recorded by grade_steps)
        return BY_POSITION[where]
    if step.rule == "mult.involution" and _counit_shape(step):
        return "strict"
    if step.rule in STRICT_J1 or step.rule in STRICT_NODES:
        return "strict"
    if step.rule in ABSORB_J1:
        return "absorbed"
    if step.rule in ABSENT_NODES:
        return "absent"
    return _theorem_grade(step, grades)


def phases(grades: dict, node=None, rng=None):
    """Search phases for the prover, cheapest tape first: strict only; then absorbed; then posted; then anything.
    The search is heuristic (SPEC §5.5): a path the search misses can make a grade worse, never better."""
    def at_most(level):
        return lambda s: GRADE_ORDER.index(step_grade(s, grades, node, rng)) <= level
    return [at_most(0), at_most(1), at_most(2), None]


def grade_steps(steps: list, node, grades: dict, rng) -> Tape:
    """Grade the licensed steps of one derivation row and record their receipts."""
    tape = Tape()
    domain = node.get("domain", "positive")
    for s in steps:
        g = step_grade(s, grades, node, rng)
        if g == "strict":
            x = _unit_shape(s)
            if x is not None and (s.rule in UNIT_RULES or s.rule.startswith("lemma") or s.rule == "hypothesis"):
                # a unit step graded strict is one on pole-valued content (LEGISLATION 30f): on the tape, no receipt
                tape.receipts.append(Receipt(s.rule, F.to_string(x, True) or "void", "pole", "strict", set()))
            continue
        where = position_class(s.path) if s.rule not in ABSORB_J1 else "absorbing"
        if _unit_shape(s) is None and s.rule not in ABSORB_J1 and grades.get(s.rule) is not None and grades[s.rule].grade in ("absorbed", "import"):
            where = "inherited"  # the grade comes from the theorem's own tape, whatever this position
        exceptional = {}
        if g == "import" and position_class(s.path) == "under-square":
            # under a square the step is sound only where its receipt is void: decide at the generic points of this
            # node's domain (a posted theorem is judged here, at its use site, not on its own domain) and record
            # the exceptional points — lattice values of the content, where the log of exactly one reads ω.
            # (An import theorem reused elsewhere keeps its grade: the import sits inside it, and its posted
            # receipts post again at the use site — no use-site test there.)
            ks, exceptional = receipt_values(s.redex, s.result, domain, rng, with_probes=True)
            if ks != {0}:
                g = "absent"
        else:
            ks = receipt_values(s.redex, s.result, domain, rng)
        content = F.to_string(_unit_shape(s), True) if _unit_shape(s) is not None else F.to_string(s.redex, True)
        if _unit_shape(s) is not None and not _unit_shape(s):
            content = "void"
        tape.receipts.append(Receipt(s.rule, content or "void", where, g, ks, exceptional))
        if g == "absent":
            tape.absent.append(s.rule)
        tape.worse(g)
    return tape


def grade_node(node, nodes, cache: dict, grades: dict, rng, check_node_fn) -> Tape:
    """Grade a whole node from its licensed derivation; theorems it cites must already be graded. Lemma tables
    are graded first and their tapes used where a later table cites them."""
    local = dict(grades)
    by_table: dict = {}

    def on_table(ti, rows):
        t = by_table.setdefault(ti, Tape())
        for _ti, i, status, msg, steps in rows:
            if status == "UNLICENSED":
                t.worse("absent")
                t.absent.append(f"row {i+1} unlicensed")
                continue
            t.merge(grade_steps(steps, node, local, rng))
        local[f"lemma#{ti}"] = t  # priced before a later table's search cites it

    check_node_fn(node, nodes, cache, phases=phases(local, node, rng), on_table=on_table)
    tape = Tape()
    for ti in sorted(by_table):
        tape.merge(by_table[ti])
    return tape


def describe(tape: Tape) -> str:
    if tape.grade == "strict" and not tape.receipts:
        return "≡ — no unit step: strict in 𝕁₁"
    parts = []
    for r in tape.receipts:
        where = f"{r.where} {r.rule}" if r.where == "inherited" else r.where
        if r.grade == "strict":
            parts.append(f"strict [{r.where}] on `{r.content}` (the pole has no winding: no receipt, LEGISLATION 30f)")
            continue
        ks = ",".join("?" if k is None else str(k) for k in sorted(r.k, key=lambda v: (v is None, v))) if r.k else "?"
        exc = ""
        if r.exceptional:
            pts = []
            for k, envs in list(r.exceptional.items())[:3]:   # in order of discovery: the simplest points first
                e = envs[0]
                pts.append(f"k = {'?' if k is None else k} at " + ", ".join(f"{n}={F.fmt(v)}" for n, v in sorted(e.items())))
            more = "" if len(r.exceptional) <= 3 else f" / … {len(r.exceptional) - 3} more"
            exc = "; except " + " / ".join(pts) + more
        parts.append(f"{r.grade} [{where}] on `{r.content}` (k = {ks}{exc})")
    if tape.absent:
        parts.append("absent: " + ", ".join(sorted(set(tape.absent))))
    head = "≡" if tape.grade == "strict" else tape.cell
    return f"{head}: " + "; ".join(parts)
