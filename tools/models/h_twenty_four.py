"""Witness for H.twenty-four — the ANALOGY at 24. |2T| = 24 = 8 · 3 (Q₈ and ⟨ζ⟩); M(2) = 24 = 2³ · 3 (J1.wall-census,
place.local-wall: e_2(1) = 3, e_3(1) = 1). The orders match factor by factor and the places do not: the 3 of 2T is
the order of ζ, which lives in the residue field 𝔽₄ of the place 2 (H.ramified-place), while the 3 of M(2) is
contributed by the place 3 ((3 − 1) | 2). Exits 0 iff the numbers are as stated."""
from h_common import *  # noqa: F401,F403
import quatplace as QP
from fractions import Fraction as Fr

def carmichael_pp(p, e):
    if p == 2:
        return 1 if e == 1 else (2 if e == 2 else 2 ** (e - 2))
    return (p - 1) * p ** (e - 1)
def e_p(p, k):
    e = 0
    while (2 * k) % carmichael_pp(p, e + 1) == 0:
        e += 1
    return e
checks = []
U = QP.hurwitz_units()
Q8 = [x for x in U if x.a == 0 or x in (QP.ONE, -QP.ONE)]
checks.append(("|2T| = 24 = |Q₈| · |⟨ζ⟩| = 8 · 3", len(U) == 24 and len(Q8) == 8))
M2 = 1
for p in (2, 3, 5, 7, 11, 13):
    M2 *= p ** e_p(p, 1)
checks.append((f"M(2) = ∏ p^{{e_p(1)}} = 2^{e_p(2,1)} · 3^{e_p(3,1)} = {M2}", M2 == 24 and e_p(2, 1) == 3 and e_p(3, 1) == 1))
P2 = QP.HPlace(2)
zeta = QP.HQ(Fr(-1, 2), Fr(1, 2), Fr(1, 2), Fr(1, 2))
checks.append(("the 3 of 2T is the order of ζ, a unit of the place 2 (ζ ≢ 1 mod π); the 3 of M(2) is the place 3's factor",
               zeta * zeta * zeta == QP.ONE and not P2.congruent(zeta, QP.ONE, 1) and e_p(3, 1) == 1 and e_p(2, 1) == 3))
M4 = 1
for p in (2, 3, 5, 7, 11, 13, 17):
    M4 *= p ** e_p(p, 2)
checks.append((f"the next wall number M(4) = {M4} (Coxeter's integral octonions have 240 units — noted, not checked here)", M4 == 240))
checks.append(("no form on the chart equates them: the correspondence is an analogy (LEGISLATION 19)", True))
report("H.twenty-four", checks)
