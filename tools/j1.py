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

At a finite place one more grade sits between strict and absorbed:

  page       a law of the page (PAGE_RULES: the void pile and what follows from it by the page's equality alone)
             applied with NO square anywhere above it — at depth 0, through angles, juxtaposition and instances:
             the two forms agree mod p^n, which IS the page's equality. That equality is not a congruence through
             a square (the log of p^n is n·[p], the log of the void is the pole; the log of a non-unit loses
             shells; the log of exactly one is the period where the log of a 1-unit ≡ 1 is not), and an instance
             does not pay a page difference — it only page-equalizes it — so a page step with a square anywhere
             above it is measured at EVERY square above it (page_under_square, innermost first): where no
             square's value changes at the generic points of the domain the step is an import (sound by content,
             as a unit step under a square is); where some change, each by one lattice element, the outermost
             changed square posts that receipt and its own position grades the step (absorbed when it sits
             directly inside an instance, posted at depth 0); otherwise absent. A theorem whose tape carries a
             page step (its own or inherited, measured or not) is itself a page law: its reuse with a square above
             is measured in the same way.

In the ℍ reading (tools/quat.py, rung `H`; LEGISLATION 32(c)) a receipt carries a direction, and an instance pays
a receipt 2πu only when the rest of its content commutes with u — so every step graded `absorbed` by position is
checked BY VALUE there: the paying instance before and after (a unit step directly inside it), or the step's own
two sides (an absorption rule, a theorem reused): if they differ at the generic points of the domain the step is
`absent` with `where = cross-slice` — the first non-commutative wall, as the tape sees it. A step whose receipt is
no lattice element (`?` — the seam: L(e^{πj}) = πi ≠ πj) is `absent` in that reading as well. A conditional rule
(H.collapse: `[A ; B] ≃ [A] [B]` only for commuting entries) is checked at its use site: the reading evaluates the
premise on the matched entries, and a failing premise makes the step `absent`.

A node's grade is the worst grade among its steps. The `holds` cell it implies: strict, page or absorbed → holds;
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

GRADE_ORDER = ["strict", "page", "absorbed", "posted", "import", "absent"]
CELL_OF = {"strict": "holds", "page": "holds", "absorbed": "holds", "posted": "holds-mod-Λ", "import": "guarded", "absent": "fails"}
BY_POSITION = {"absorbing": "absorbed", "depth-0": "posted", "under-square": "import"}
# The laws of the page at a finite place (rung `place`): equalities mod p^n that are not congruences through a
# square. Graded by position — see the module docstring. A theorem derived from one inherits the grade `page`.
PAGE_RULES = {"place.void-pile", "place.residue", "place.negation-is-a-pile", "place.fermat", "place.division-by-unit",
              "place.prime-power", "place.geometric-doll"}

UNIT_RULES = {"mult.involution", "mult.log-of-one", "J1.unit"}     # rules whose unit-shaped steps post receipts
STRICT_J1 = {"J1.counit", "J1.closure", "J1.period-form"}            # strict rules of the J1 rung itself
ABSORB_J1 = {"J1.absorption", "J1.absorption-mirror"}                 # witnessed moves inside an instance
# Rung H: the strict rules of the ordered bracket (bookkeeping of an ordered log: exact in ℍ at every position), and
# the conditional rule whose premise the reading checks at the use site (SPEC §4.5).
STRICT_H = {"H.ordered-bracket", "H.splice", "H.unit-entry", "H.list-distribution", "H.anticommutation", "H.seed",
            "H.ordered-product", "H.j", "H.k", "H.commutation"}
# Witnessed rules of rung H: a ≃ law whose use posts a receipt by position exactly as the unit does — the collapse
# `[P ; Q] ≃ [P] [Q]` differs from a strict equality by a lattice element (log(PQ) against log P + log Q).
WITNESSED_H = {"H.collapse"}
# Conditional rules: rule -> premise name; the reading's `premise(name, env, domain, rng)` decides at the use site on
# the entries matched as P and Q. `cosliced`: the logs of P and Q commute (the collapse); `commute`: the values of P
# and Q commute (the ordered commutation).
CONDITIONAL = {"H.collapse": "cosliced", "H.commutation": "commute"}
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
    """Walk outward from the redex: angles are transparent; the first instance absorbs; the first square (ordered or
    not) refuses."""
    for k in reversed(path):
        if k == F.ANGLE:
            continue
        if k == F.ROUND:
            return "absorbing"
        if k in (F.SQUARE, F.ORDERED):
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


class CReading:
    """The 𝕁₁ reading in ℂ (ω = 2πi): the default reading of the receipt prover. A reading at a finite place
    (tools/place.py, `Reading`) and the ℍ reading (tools/quat.py) offer the same hooks, so that the same tape is
    computed at every place and in ℍ."""
    name = "C"
    period_name = "ω"
    noncommutative = False
    skip_errors = (F.Undefined, F.Excluded, OverflowError)

    def evaluate(self, form, env):
        return _in_j1_reading(F.evaluate, form, env)

    def random_env(self, names, domain, rng):
        return F.random_env(names, domain, rng)

    def probes(self, names, domain, rng):
        return _probes(names, domain, rng)

    def is_pole(self, v):
        return v is F.BH

    def k(self, a, b):
        """a − b in units of ω when it is a lattice element, else None."""
        k = (a - b) / OMEGA
        if abs(k.imag) > 1e-6 * (1 + abs(k)) or abs(k.real - round(k.real)) > 1e-6 * (1 + abs(k)):
            return None
        return int(round(k.real))

    def fmt(self, v):
        return F.fmt(v)


READING = CReading()


def _sample(names, domain, rng, trials, reading=None):
    """Random values of the node's domain — the generic points."""
    R = reading or READING
    return [R.random_env(names, domain, rng) for _ in range(trials if names else 1)]


def _in_domain(p, domain: str) -> bool:
    if isinstance(p, complex):
        return domain in ("complex", "slice", "plane")
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


def pole_valued(x: F.Form, domain: str, rng, trials: int = 12, reading=None) -> bool:
    """Does the content x evaluate to the pole on every sampled value (the hole, or a form dominion makes it)?"""
    R = reading or READING
    if not x:
        return False
    names = F.variables(x)
    seen = False
    for env in _sample(names, domain, rng, trials, R):
        try:
            v = R.evaluate(x, env)
        except R.skip_errors:
            continue
        seen = True
        if not R.is_pole(v):
            return False
    return seen


def _single_instance(form: F.Form):
    return len(form) == 1 and form[0][0] == F.ROUND


def _k_at(redex, result, env, reading=None):
    R = reading or READING
    try:
        a = R.evaluate(redex, env)
        b = R.evaluate(result, env)
    except R.skip_errors:
        return "skip"
    if R.is_pole(a) and R.is_pole(b):
        return "skip"   # both sides at the pole: nothing to record
    if R.is_pole(a) or R.is_pole(b):
        return None
    try:
        return R.k(a, b)
    except R.skip_errors:
        return "skip"   # at a place: a value that cannot be judged at the depth (shells lost past the margin)


def receipt_values(redex: F.Form, result: F.Form, domain: str, rng, trials: int = 24, with_probes: bool = False,
                   reading=None):
    """The receipt of a step, in units of ω: value(redex) − value(result) in the 𝕁₁ reading, over the generic
    points of the domain. When both sides are a single instance the contents are compared instead (an absorbed
    period is invisible at the instance level and is exactly what the receipt records). An entry of None stands
    for `?` — the pole, or a difference that is not a lattice element. With with_probes=True the exceptional
    points (PROBES) are sampled as well and returned separately as {k: [env, …]} for the non-void ones."""
    R = reading or READING
    if _single_instance(redex) and _single_instance(result):
        redex, result = redex[0][1], result[0][1]
    names = F.variables(redex) | F.variables(result)
    ks = set()
    for env in _sample(names, domain, rng, trials, R):
        k = _k_at(redex, result, env, R)
        if k != "skip":
            ks.add(k)
    if not with_probes:
        return ks
    exceptional = {}
    for env in R.probes(names, domain, rng):
        k = _k_at(redex, result, env, R)
        if k != "skip" and k != 0:
            exceptional.setdefault(k, []).append(env)
    return ks, exceptional


@dataclass
class Receipt:
    rule: str
    content: str        # what the step rewrote, as a string
    where: str          # absorbing | depth-0 | under-square | inherited (a theorem's own tape) | pole (strict, 30f) |
                        # cross-slice (ℍ: the paying instance does not pay) | premise (a conditional rule's premise fails)
    grade: str          # strict (pole only) | absorbed | posted | import | absent
    k: set = field(default_factory=set)   # sampled receipt values in units of ω (None = ?)
    exceptional: dict = field(default_factory=dict)   # under a square: non-void receipts at probe points {k: [env…]}
    page: bool = False  # a page step (a law of the page, or a page theorem reused): the tape that holds it is a page law
    direction: str = ""  # ℍ: the direction the receipt winds about, when one was sampled


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

    @property
    def is_page(self) -> bool:
        """A page law: some step of the tape is a page step (whatever the tape's worst grade)."""
        return any(r.page for r in self.receipts)

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


def is_page(step: P.Step, grades: dict) -> bool:
    """A step by a law of the page: one of PAGE_RULES, or a theorem (or lemma table) whose own tape carries a page
    step — whatever its worst grade: a tape mixing absorbed and page steps is still the page's."""
    g = grades.get(step.rule)
    return step.rule in PAGE_RULES or (g is not None and g.is_page)


def _worse(a: str, b: str) -> str:
    return a if GRADE_ORDER.index(a) >= GRADE_ORDER.index(b) else b


def page_floor(step: P.Step, grades: dict) -> str:
    """The least grade a page step can earn: `page` for a law of the page itself or a theorem whose own tape is
    strict, page or absorbed; a posted page theorem keeps its posted receipt (posted at depth 0, absorbed directly
    inside an instance, import under a square — as a posted theorem is reused anywhere); an import or absent one
    stays so. The measurement at the squares above can only make this worse, never better."""
    g = grades.get(step.rule)
    if step.rule in PAGE_RULES or g is None or g.grade in ("strict", "page", "absorbed"):
        return "page"
    if g.grade == "posted":
        return BY_POSITION[position_class(step.path)]
    return g.grade   # import, absent


def page_under_square(step: P.Step, node, rng, reading=None, with_probes: bool = False):
    """A page step with a square above it, measured at every square above the redex (innermost first — the prover
    records each square's content before and after on the step, through instances and angles alike, because an
    instance only page-equalizes a page difference and a square above the instance can still read it as a period
    at the exactly-one point). Each square's value either does not change at the generic points of the domain,
    or changes by one lattice element (a receipt), or changes otherwise (absent). Returns (grade, receipts,
    exceptional, where): no square changes → `import` (sound by content; the exceptional points are recorded);
    some change → the OUTERMOST changed square posts its receipt and its own position grades the step —
    `posted` at depth 0; `absorbed` directly inside an instance (through angles) when no square lies above that
    instance, `import` when one does (the instance pays the period and only page-equalizes the rest, which the
    square above reads as equal at the generic points: by content); `absent` under another square.
    `where` names the measurement: `square:unchanged`, `square:absorbing`, `square:absorbing-under-square`,
    `square:depth-0`, `square:under-square`."""
    domain = node.get("domain", "positive")
    if not step.squares:   # no square recorded above the redex: measure the step itself, as a unit step is
        ks, exc = (receipt_values(step.redex, step.result, domain, rng, with_probes=True, reading=reading)
                   if with_probes else (receipt_values(step.redex, step.result, domain, rng, reading=reading), {}))
        return ("import" if ks == {0} else "absent"), ks, exc, "square:unchanged" if ks == {0} else "square:under-square"
    exceptional: dict = {}
    measured = []
    for before, after, distance, *rest in step.squares:
        kind = rest[0] if rest else F.SQUARE
        a, b = ((kind, before),), ((kind, after),)
        idx = len(step.path) - 1 - distance          # the square's index in the path from the root
        where = position_class(step.path[:idx])       # the square's own position
        if with_probes:
            ks, exc = receipt_values(a, b, domain, rng, with_probes=True, reading=reading)
            for k, envs in exc.items():
                exceptional.setdefault(k, []).extend(envs)
        else:
            ks = receipt_values(a, b, domain, rng, reading=reading)
        measured.append((ks, where))
    if any(None in ks or len(ks) != 1 for ks, _ in measured):
        bad = next((ks, w) for ks, w in measured if None in ks or len(ks) != 1)
        return "absent", bad[0], exceptional, "square:under-square"
    changed = [i for i, (ks, _) in enumerate(measured) if ks != {0}]
    if not changed:
        return "import", {0}, exceptional, "square:unchanged"
    j = changed[-1]            # the outermost changed square decides
    ks, where = measured[j]
    if where == "depth-0":
        return "posted", ks, exceptional, "square:depth-0"
    if where == "absorbing":
        if j < len(measured) - 1:
            # the instance directly outside pays the period, but only page-equalizes the rest, and a square above
            # that instance reads the two sides as equal at the generic points only: sound by content — an import
            return "import", ks, exceptional, "square:absorbing-under-square"
        return "absorbed", ks, exceptional, "square:absorbing"
    return "absent", ks, exceptional, "square:under-square"


def step_grade(step: P.Step, grades: dict, node=None, rng=None, reading=None) -> str:
    """The 𝕁₁ grade of one licensed step, from its rule and position (the reading decides only pole-valued
    content, and whether an under-square receipt is void)."""
    x = _unit_shape(step)
    if x is not None and (step.rule in UNIT_RULES or step.rule.startswith("lemma") or step.rule == "hypothesis"):
        if node is not None and rng is not None and pole_valued(x, node.get("domain", "positive"), rng, reading=reading):
            return "strict"
        where = position_class(step.path)
        if where == "under-square" and node is not None and rng is not None:
            ks = receipt_values(step.redex, step.result, node.get("domain", "positive"), rng, reading=reading)
            return "import" if ks == {0} else "absent"  # void at the generic points: an import (exceptional points are recorded by grade_steps)
        return BY_POSITION[where]
    if step.rule == "mult.involution" and _counit_shape(step):
        return "strict"
    if is_page(step, grades):
        floor = page_floor(step, grades)
        if F.SQUARE not in step.path:
            return floor     # no square above: the page's equality passes through instances, angles, juxtaposition
        if node is not None and rng is not None:
            return _worse(page_under_square(step, node, rng, reading)[0], floor)
        return _worse("import", floor)
    if step.rule in WITNESSED_H:
        # a witnessed rule of rung H, graded by position like the unit (its premise, if any, is checked by grade_steps)
        where = position_class(step.path)
        if where == "under-square" and node is not None and rng is not None:
            ks = receipt_values(step.redex, step.result, node.get("domain", "positive"), rng, reading=reading)
            return "import" if ks == {0} else "absent"
        return BY_POSITION[where]
    if step.rule in STRICT_J1 or step.rule in STRICT_NODES or step.rule in STRICT_H:
        return "strict"
    if step.rule in ABSORB_J1:
        return "absorbed"
    if step.rule in ABSENT_NODES:
        return "absent"
    return _theorem_grade(step, grades)


def phases(grades: dict, node=None, rng=None, reading=None):
    """Search phases for the prover, cheapest tape first: strict only; then absorbed; then posted; then anything.
    The search is heuristic (SPEC §5.5): a path the search misses can make a grade worse, never better."""
    def at_most(level):
        return lambda s: GRADE_ORDER.index(step_grade(s, grades, node, rng, reading)) <= level
    levels = [0, 1, 2, 3] if (reading is not None and reading is not READING) else [0, 2, 3]   # `page` only at a place
    return [at_most(l) for l in levels] + [None]


def _values_agree(redex, result, domain, rng, reading, trials: int = 16) -> bool:
    """Do two forms have the same value at the generic points of the domain (exactly, not mod Λ)? Samples on which
    either has no value are skipped; False when nothing could be compared — agreement is certified by samples, never
    by their absence (the rung-H referee pass, 2026-10-07)."""
    R = reading or READING
    names = F.variables(redex) | F.variables(result)
    judged = 0
    for env in _sample(names, domain, rng, trials, R):
        try:
            a, b = R.evaluate(redex, env), R.evaluate(result, env)
        except R.skip_errors:
            continue
        if R.is_pole(a) and R.is_pole(b):
            judged += 1
            continue
        if R.is_pole(a) or R.is_pole(b) or not R.equal(a, b, "≐"):
            return False
        judged += 1
    return judged > 0


def _paying_instance(step: P.Step):
    """For a step at an absorbing position: the innermost instance above the redex (through angles only), as its
    content before and after; None when the step has no recorded instance there."""
    trailing = 0
    for k in reversed(step.path):
        if k == F.ANGLE:
            trailing += 1
        else:
            break
    for before, after, distance in step.rounds:
        if distance == trailing:
            return before, after
    return None


def _direction_of(redex, result, domain, rng, reading):
    """ℍ: the direction of the receipt of a step, at one generic sample (for the tape's description)."""
    R = reading
    if not getattr(R, "noncommutative", False) or not hasattr(R, "direction"):
        return ""
    if _single_instance(redex) and _single_instance(result):
        redex, result = redex[0][1], result[0][1]
    names = F.variables(redex) | F.variables(result)
    for env in _sample(names, domain, rng, 4, R):
        try:
            a, b = R.evaluate(redex, env), R.evaluate(result, env)
        except R.skip_errors:
            continue
        if R.is_pole(a) or R.is_pole(b):
            continue
        u = R.direction(a, b)
        if u is not None:
            return R.fmt(u)
    return ""


def premise_holds(step: P.Step, node, rng, reading=None) -> bool:
    """A conditional rule (CONDITIONAL) licenses a step only where its premise holds; the reading decides it on the
    matched substitution, at the generic points of the node's domain (ℂ: every premise of commutation holds)."""
    name = CONDITIONAL.get(step.rule)
    if name is None:
        return True
    R = reading or READING
    if not hasattr(R, "premise"):
        return True
    return R.premise(name, dict(step.env), node.get("domain", "positive"), rng)


def grade_steps(steps: list, node, grades: dict, rng, reading=None) -> Tape:
    """Grade the licensed steps of one derivation row and record their receipts."""
    tape = Tape()
    domain = node.get("domain", "positive")
    R = reading or READING
    noncomm = getattr(R, "noncommutative", False)
    for s in steps:
        g = step_grade(s, grades, node, rng, reading)
        if s.rule in CONDITIONAL and not premise_holds(s, node, rng, reading):
            # a conditional rule whose premise fails at the use site: the step is not licensed by the law as stated
            tape.receipts.append(Receipt(s.rule, F.to_string(s.redex, True) or "void", "premise", "absent", {None}))
            tape.absent.append(s.rule)
            tape.worse("absent")
            continue
        if g == "strict":
            x = _unit_shape(s)
            if x is not None and (s.rule in UNIT_RULES or s.rule.startswith("lemma") or s.rule == "hypothesis"):
                # a unit step graded strict is one on pole-valued content (LEGISLATION 30f): on the tape, no receipt
                tape.receipts.append(Receipt(s.rule, F.to_string(x, True) or "void", "pole", "strict", set()))
            continue
        if noncomm and g == "absorbed":
            # ℍ: an absorbed step is checked by value — the instance that pays the receipt must still agree
            # (LEGISLATION 32(c), the first non-commutative wall). A unit step or an absorption rule directly inside an
            # instance: that instance, before and after; a theorem reused, or a rule whose own sides are instances:
            # the two sides themselves.
            # a primitive witnessed rule (the unit, the collapse) is paid by the instance above it, and so is a
            # unit-shaped step of a theorem (the log of one, a lemma that is a unit step): the receipt is the
            # content's, and only the instance above can pay it; a theorem reused on other shapes, or an absorption
            # rule, has its own two sides to compare
            pay = _paying_instance(s) if (s.rule not in ABSORB_J1 and (grades.get(s.rule) is None or _unit_shape(s) is not None)) else None
            if pay is not None:
                ok = _values_agree(((F.ROUND, pay[0]),), ((F.ROUND, pay[1]),), domain, rng, R)
            else:
                ok = _values_agree(s.redex, s.result, domain, rng, R)
            if not ok:
                content = F.to_string(_unit_shape(s), True) if _unit_shape(s) is not None else F.to_string(s.redex, True)
                direction = _direction_of(s.redex, s.result, domain, rng, R)
                tape.receipts.append(Receipt(s.rule, content or "void", "cross-slice", "absent", receipt_values(s.redex, s.result, domain, rng, reading=R), direction=direction))
                tape.absent.append(s.rule)
                tape.worse("absent")
                continue
        where = position_class(s.path) if s.rule not in ABSORB_J1 else "absorbing"
        if _unit_shape(s) is None and s.rule not in ABSORB_J1 and grades.get(s.rule) is not None and (
                grades[s.rule].grade in ("absorbed", "import") or (grades[s.rule].is_page and g == "page")):
            where = "inherited"  # the grade comes from the theorem's own tape, whatever this position
        if g == "page":
            # a law of the page with no square above it: no lattice receipt — the forms agree mod p^n, the page's
            # own equality; recorded so that the tape shows the law is the page's and not the calculus's
            tape.receipts.append(Receipt(s.rule, F.to_string(s.redex, True) or "void", where, "page", set(), page=True))
            tape.worse(g)
            continue
        if is_page(s, grades):
            floor = page_floor(s, grades)
            if F.SQUARE in s.path:
                # a page step with a square above it, measured at every square above (page_under_square), with the
                # exceptional points: the step's content is recorded, the receipt is the squares'; a page theorem's
                # own standing (a posted receipt of its own) is the floor of what the measurement can earn
                g, ks, exceptional, where = page_under_square(s, node, rng, reading, with_probes=True)
                g = _worse(g, floor)
            else:
                # a posted (or import, absent) page theorem reused with no square above: its own receipt posts again
                ks, exceptional = receipt_values(s.redex, s.result, domain, rng, reading=reading), {}
                where = "inherited"
            tape.receipts.append(Receipt(s.rule, F.to_string(s.redex, True) or "void", where, g, ks, exceptional, page=True))
            if g == "absent":
                tape.absent.append(s.rule)
            tape.worse(g)
            continue
        exceptional = {}
        if g == "import" and position_class(s.path) == "under-square":
            # under a square the step is sound only where its receipt is void: decide at the generic points of this
            # node's domain (a posted theorem is judged here, at its use site, not on its own domain) and record
            # the exceptional points — lattice values of the content, where the log of exactly one reads ω.
            # (An import theorem reused elsewhere keeps its grade: the import sits inside it, and its posted
            # receipts post again at the use site — no use-site test there.)
            ks, exceptional = receipt_values(s.redex, s.result, domain, rng, with_probes=True, reading=reading)
            if ks != {0}:
                g = "absent"
        else:
            ks = receipt_values(s.redex, s.result, domain, rng, reading=reading)
        if s.rule in WITNESSED_H and where == "absorbing" and not (_unit_shape(s) is None and grades.get(s.rule) is not None):
            where = "absorbing"
        if noncomm and g == "posted" and None in ks:
            g = "absent"   # ℍ: a receipt that is no lattice element at depth 0 — the seam (L(e^{πu}) = πi ≠ πu): the two
                           # forms differ on the page by a displacement no period measures, and the step is false there
        if noncomm and g == "absorbed" and None in ks:
            where = "seam"  # ℍ: the paying instance agrees (checked above) though the contents differ by no period — a
                            # seam displacement, e^{πu} = e^{πi}: paid by the instance, as James's J-discipline pays it,
                            # and recorded as such (SPEC §4.5)
        content = F.to_string(_unit_shape(s), True) if _unit_shape(s) is not None else F.to_string(s.redex, True)
        if _unit_shape(s) is not None and not _unit_shape(s):
            content = "void"
        direction = _direction_of(s.redex, s.result, domain, rng, R) if (noncomm and g in ("posted", "absorbed")) else ""
        tape.receipts.append(Receipt(s.rule, content or "void", where, g, ks, exceptional, direction=direction))
        if g == "absent":
            tape.absent.append(s.rule)
        tape.worse(g)
    return tape


def grade_node(node, nodes, cache: dict, grades: dict, rng, check_node_fn, reading=None) -> Tape:
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
            t.merge(grade_steps(steps, node, local, rng, reading))
        local[f"lemma#{ti}"] = t  # priced before a later table's search cites it

    check_node_fn(node, nodes, cache, phases=phases(local, node, rng, reading), on_table=on_table)
    tape = Tape()
    for ti in sorted(by_table):
        tape.merge(by_table[ti])
    return tape


def describe(tape: Tape, reading=None) -> str:
    R = reading or READING
    if tape.grade == "strict" and not tape.receipts:
        return "≡ — no unit step: strict in 𝕁₁" if R is READING else f"≡ — no unit step: strict at {R.name}"
    parts = []
    for r in tape.receipts:
        where = f"{r.where} {r.rule}" if r.where == "inherited" else r.where
        if r.grade == "strict":
            parts.append(f"strict [{r.where}] on `{r.content}` (the pole has no winding: no receipt, LEGISLATION 30f)")
            continue
        if r.grade == "page":
            parts.append(f"page [{where}] on `{r.content}` (the page's equality, mod p^n: not through a square)")
            continue
        if r.where.startswith("square:"):
            ks = ",".join("?" if k is None else str(k) for k in sorted(r.k, key=lambda v: (v is None, v))) if r.k else "?"
            exc = ""
            if r.exceptional:
                pts = []
                for k, envs in list(r.exceptional.items())[:3]:
                    e = envs[0]
                    pts.append(f"k = {'?' if k is None else k} at " + ", ".join(f"{n}={R.fmt(v)}" for n, v in sorted(e.items())))
                exc = "; except " + " / ".join(pts)
            what = {"square:unchanged": "no square above it changes", "square:absorbing": "the outermost changed square posts, directly inside an instance",
                    "square:absorbing-under-square": "the outermost changed square posts inside an instance that a further square reads: by content",
                    "square:depth-0": "the outermost changed square posts at depth 0", "square:under-square": "a square above it changes by no one period"}[r.where]
            parts.append(f"{r.grade} [page step, measured at the squares above it: {what}] on `{r.content}` (k = {ks}{exc})")
            continue
        ks = ",".join("?" if k is None else str(k) for k in sorted(r.k, key=lambda v: (v is None, v))) if r.k else "?"
        exc = ""
        if r.exceptional:
            pts = []
            for k, envs in list(r.exceptional.items())[:3]:   # in order of discovery: the simplest points first
                e = envs[0]
                pts.append(f"k = {'?' if k is None else k} at " + ", ".join(f"{n}={R.fmt(v)}" for n, v in sorted(e.items())))
            more = "" if len(r.exceptional) <= 3 else f" / … {len(r.exceptional) - 3} more"
            exc = "; except " + " / ".join(pts) + more
        if r.where == "cross-slice":
            parts.append(f"absent [cross-slice] on `{r.content}` (the instance does not pay a receipt in direction {r.direction or '?'}: its content is not co-sliced — the first non-commutative wall)")
            continue
        if r.where == "premise":
            parts.append(f"absent [premise] on `{r.content}` (the rule's premise fails at the use site: the entries do not commute)")
            continue
        if r.where == "seam":
            parts.append(f"absorbed [seam] on `{r.content}` (the instance pays a seam displacement — the contents differ by no period, e^{{πu}} = e^{{πi}} — and agrees by value)")
            continue
        if r.grade == "absent" and not r.k and R is not READING:
            # at a place: the step's content has no value on any sample (the base e, a root the place refuses) — the
            # step is formless, not false; a receipt set {?} is the other thing, a difference that is no lattice
            # element at every sample, and that step is false
            parts.append(f"formless [{where}] on `{r.content}` (no value at {R.name} on any sample)")
            continue
        dirn = f", about {r.direction}" if r.direction else ""
        parts.append(f"{r.grade} [{where}] on `{r.content}` (k = {ks}{exc}{dirn})")
    if tape.absent:
        parts.append("absent: " + ", ".join(sorted(set(tape.absent))))
    head = "≡" if tape.grade == "strict" else tape.cell
    return f"{head}: " + "; ".join(parts)
