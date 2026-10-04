"""j1.py — the receipt tape: what each licensed step costs in 𝕁₁ (LEGISLATION 30).

The derivation checker (prover.py) tells us which rule took a row to the next, in which orientation, at which
position. This module grades every such step for the enriched calculus 𝕁₁:

  strict     a strict rule — the counit ([A]) ≡ A, Distribution, Inversion, the medium, the hole rules, and any
             theorem whose own tape is empty or wholly absorbed
  absorbed   the unit [(A)] ↔ A (or a theorem with a posted receipt) applied directly inside an instance, through
             angles at most: the instance pays the receipt on the spot — value-exact, tape unchanged
  posted     the same at depth 0 (through angles and juxtaposition only): the receipt stays on the tape; the
             two forms agree mod Λ
  import     the same under a square before any instance: ≃ is not a congruence through [ ], so the step is
             sound only when the receipt is void — a fact of the reading (the classical decree's by-content
             clause), which 𝕁₁ cannot see
  absent     a cited rule that 𝕁₁ does not have

A node's 𝕁₁ grade is the worst grade among its steps: ≡ (all strict), ≃₀ (absorbed), ≃ (posted), import,
absent. The `holds` cell reads: ≡ and ≃₀ → holds; ≃ → holds-mod-Λ; import → guarded; absent → fails.

Receipt values are the reading's business: for a unit step on content A the receipt is kω with
k = (a − Ln e^a)/2πi, the winding of a, sampled over the node's domain.
"""
from __future__ import annotations
import cmath
import math
from collections import Counter
from dataclasses import dataclass, field

import forms as F
import prover as P

GRADE_ORDER = ["strict", "absorbed", "posted", "import", "absent"]
CELL_OF = {"strict": "holds", "absorbed": "holds", "posted": "holds-mod-Λ", "import": "guarded", "absent": "fails"}


def step_grade(step, grades: dict) -> str:
    """The 𝕁₁ grade of one licensed step, from its rule and position alone (no reading)."""
    x = _unit_shape(step)
    if x is not None and (step.rule in ("mult.involution", "mult.log-of-one") or step.rule.startswith("lemma")):
        if _is_hole_content(x):
            return "strict"
        return {"absorbing": "absorbed", "depth-0": "posted", "under-square": "import"}[position_class(step.path)]
    if step.rule == "mult.involution" and _counit_shape(step):
        return "strict"
    if step.rule in STRICT_NODES or step.rule == "hypothesis" or step.rule.startswith("lemma"):
        return "strict"
    if step.rule in ABSENT_NODES:
        return "absent"
    g = grades.get(step.rule)
    if g is None or g.grade in ("strict", "absorbed"):
        return "strict"
    if g.grade in ("absent",):
        return "absent"
    if g.grade == "import":
        return "import"
    return {"absorbing": "absorbed", "depth-0": "posted", "under-square": "import"}[position_class(step.path)]


def phases(grades: dict):
    """Search phases for the prover: cheapest tape first."""
    return [lambda s: GRADE_ORDER.index(step_grade(s, grades)) <= 1,
            lambda s: GRADE_ORDER.index(step_grade(s, grades)) <= 2,
            None]

# The strict rules of 𝕁₁ among the trunk's axioms and primitives (everything else is graded from its derivation).
STRICT_NODES = {"void.page", "void.space", "Z.inversion", "mult.distribution", "mult.hole-instance",
                "mult.zero-annihilates", "mult.dominion", "mult.black-hole"}
# Nodes 𝕁₁ does not have as rules at all.
ABSENT_NODES = set()

UNIT_L = F.parse("[(A)]")
COUNIT_L = F.parse("([A])")


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


def _is_hole_content(x: F.Form) -> bool:
    """void or the black hole: the unit on such content is a theorem of the hole rules (SPEC §5.4) — except that in
    𝕁₁ the unit on *void* content is the receipt ω itself, so only the hole is exempt here."""
    return len(x) == 1 and x[0][0] == F.SQUARE and len(x[0][1]) == 0


def winding(x: F.Form, domain: str, rng, trials: int = 24):
    """The receipt of the unit on content x, in units of ω, over sampled values: a set of integers. The unit on
    void content is the generator itself — `[()]` is ω, not void (LEGISLATION 30b) — so its receipt is 1."""
    if not x:
        return {1}
    names = F.variables(x)
    ks = set()
    for _ in range(trials if names else 1):
        env = F.random_env(names, domain, rng)
        try:
            a = F.evaluate(x, env)
        except (F.Undefined, F.Excluded, OverflowError):
            continue
        if a is F.BH:
            continue
        try:
            w = cmath.exp(a)
        except OverflowError:
            continue
        if w == 0:
            continue
        k = (a - cmath.log(w)) / (2j * math.pi)
        ks.add(int(round(k.real)))
    return ks


@dataclass
class Receipt:
    rule: str
    content: str        # the content of the unit step, as a string
    where: str          # absorbing | depth-0 | under-square
    grade: str          # absorbed | posted | import
    k: set = field(default_factory=set)   # winding values sampled (units of ω)


@dataclass
class Tape:
    grade: str = "strict"
    receipts: list = field(default_factory=list)
    absent: list = field(default_factory=list)

    def worse(self, g: str):
        if GRADE_ORDER.index(g) > GRADE_ORDER.index(self.grade):
            self.grade = g

    @property
    def cell(self) -> str:
        return CELL_OF[self.grade]


def grade_steps(steps: list, node, grades: dict, rng) -> Tape:
    """Grade the licensed steps of one derivation row."""
    tape = Tape()
    domain = node.get("domain", "positive")
    for s in steps:
        x = _unit_shape(s)
        if x is not None and s.rule in ("mult.involution", "mult.log-of-one") or (x is not None and s.rule.startswith("lemma")):
            if _is_hole_content(x):
                continue  # the unit on the hole: a theorem of the hole rules, strict
            where = position_class(s.path)
            g = {"absorbing": "absorbed", "depth-0": "posted", "under-square": "import"}[where]
            ks = winding(x, domain, rng)
            if g == "import" and ks and ks != {0}:
                g = "absent"  # under a square with a non-void receipt: the step is false in 𝕁₁ (the import fails)
            tape.receipts.append(Receipt(s.rule, F.to_string(x, True) or "void", where, g, ks))
            tape.worse(g)
            continue
        if s.rule == "mult.involution" and _counit_shape(s):
            continue  # the counit is strict
        if s.rule in STRICT_NODES or s.rule in ("hypothesis",) or s.rule.startswith("lemma"):
            continue
        if s.rule in ABSENT_NODES:
            tape.absent.append(s.rule)
            tape.worse("absent")
            continue
        # a theorem used as a rule: inherits its own grade, re-positioned
        g = grades.get(s.rule)
        if g is None:
            continue  # definitions, instances with no grade: strict by default
        if g.grade in ("strict", "absorbed"):
            continue
        if g.grade == "absent":
            tape.absent.append(s.rule)
            tape.worse("absent")
            continue
        # posted or import receipts of the theorem, used here at this position
        where = position_class(s.path)
        if g.grade == "import":
            tape.receipts.append(Receipt(s.rule, f"(the import inside {s.rule})", where, "import"))
            tape.worse("import")
            continue
        gg = {"absorbing": "absorbed", "depth-0": "posted", "under-square": "import"}[where]
        tape.receipts.append(Receipt(s.rule, f"(the receipt of {s.rule})", where, gg))
        tape.worse(gg)
    return tape


def grade_node(node, nodes, cache: dict, grades: dict, rng, check_node_fn) -> Tape:
    """Grade a whole node from its licensed derivation; theorems it cites must already be graded. The prover is
    asked for the cheapest tape (strict and absorbed steps first, then posted, then anything)."""
    lic, unl, skip, details = check_node_fn(node, nodes, cache, phases=phases(grades))
    tape = Tape()
    for ti, i, status, msg, steps in details:
        if status == "UNLICENSED":
            tape.worse("absent")
            tape.absent.append(f"row {i+1} unlicensed")
            continue
        row = grade_steps(steps, node, grades, rng)
        tape.receipts += row.receipts
        tape.absent += row.absent
        tape.worse(row.grade)
    return tape


def describe(tape: Tape) -> str:
    if tape.grade == "strict":
        return "≡ — no unit step: strict in 𝕁₁"
    parts = []
    for r in tape.receipts:
        ks = ",".join(str(k) for k in sorted(r.k)) if r.k else "?"
        parts.append(f"{r.grade} [{r.where}] on `{r.content}` (k = {ks})")
    if tape.absent:
        parts.append("absent: " + ", ".join(tape.absent))
    return f"{tape.cell}: " + "; ".join(parts)
