"""Witness for H.hurwitz-units — the 24 units. (1) ±1, ±i, ±j, ±k, (±1 ± i ± j ± k)/2 are closed under the product
and the inverse: a group of order 24; (2) the orders are {1, 2, 3, 4, 6} with the counts 1, 1, 8, 6, 8; (3) Q₈ is
normal, ζ = (−1 + i + j + k)/2 has order 3, and 2T = ⟨ζ⟩ ⋉ Q₈ (every element is ζ^a q uniquely); (4) the
de-collapse (JH-19): the sixteen states {±1 ± i ± j ± k} are closed under the Q₈ operators but not under addition;
their additive-multiplicative closure is the checkerboard {x ∈ ℤ⁴ : all coordinates of one parity} = 2·O, and halving
by (<[oo]>) reaches the 24 units; (5) the norm of every Hurwitz unit is one — so each has the inverse q̄. Exits 0 iff
all hold."""
from h_common import *  # noqa: F401,F403
import quatplace as QP
from fractions import Fraction as Fr

U = QP.hurwitz_units()
S = set(U)
checks = []
checks.append(("24 elements, closed under product and inverse", len(S) == 24 and all((x * y) in S for x in U for y in U) and all(x.inverse() in S for x in U)))
def order(x):
    y, n = x, 1
    while y != QP.ONE:
        y = y * x; n += 1
    return n
orders = sorted(order(x) for x in U)
from collections import Counter
cnt = Counter(orders)
checks.append((f"orders: {dict(cnt)}", cnt == {1: 1, 2: 1, 3: 8, 4: 6, 6: 8}))
Q8 = [x for x in U if x.a == 0 or x in (QP.ONE, -QP.ONE)]
normal = all((g * q * g.inverse()) in set(Q8) for g in U for q in Q8)
zeta = QP.HQ(Fr(-1, 2), Fr(1, 2), Fr(1, 2), Fr(1, 2))
decomp = set()
for a in range(3):
    za = QP.ONE
    for _ in range(a):
        za = za * zeta
    for q in Q8:
        decomp.add(za * q)
checks.append(("Q₈ is normal, ζ has order 3, and 2T = ⟨ζ⟩·Q₈ (24 distinct products)", len(Q8) == 8 and normal and order(zeta) == 3 and decomp == S))
states = [QP.HQ(a, b, c, d) for a in (1, -1) for b in (1, -1) for c in (1, -1) for d in (1, -1)]
SS = set(states)
# the Q8 operators: right multiplication by ±1, ±i, ±j, ±k
closed_ops = all((s * q) in SS for s in states for q in Q8)
add_closed = all((s + t) in SS for s in states for t in states)
checks.append(("the 16 states {±1±i±j±k} close under the Q₈ operators (right multiplication) and not under addition", closed_ops and not add_closed))
# the closure under + and ×, inside the box |coords| ≤ 2: the checkerboard
box = [QP.HQ(a, b, c, d) for a in range(-2, 3) for b in range(-2, 3) for c in range(-2, 3) for d in range(-2, 3)]
check_lattice = {q for q in box if len({int(x) % 2 for x in q.coords()}) == 1}
gen = set(states)
changed = True
while changed:
    changed = False
    new = set()
    for x in list(gen):
        for y in list(gen):
            for z in (x + y, x - y, x * y):
                if all(abs(c) <= 2 for c in z.coords()) and z not in gen:
                    new.add(z)
    if new:
        gen |= new; changed = True
checks.append((f"the additive–multiplicative closure of the 16 states in the box |coords| ≤ 2 is the checkerboard (equal-parity coordinates): {len(gen)} = {len(check_lattice)} points, = 2·O", gen == check_lattice))
halved = {QP.HQ(*[c / 2 for c in s.coords()]) for s in states}
checks.append(("halving the 16 states by (<[oo]>) gives the 16 non-Lipschitz Hurwitz units; with ±1, ±i, ±j, ±k the 24", len(halved | set(Q8)) == 24 and (halved | set(Q8)) == S))
checks.append(("every Hurwitz unit has norm 1, so its inverse is its conjugate", all(x.norm() == 1 and x.inverse() == x.conj() for x in U)))
report("H.hurwitz-units", checks)
