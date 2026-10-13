"""Witness for H.ramified-place — the quaternions at 2, where ℍ ⊗ ℚ₂ is a division algebra (JP v0.3 (3)). In the
Hurwitz order O: (1) v(π) = ½ for π = 1 + i and v(2) = 1 — the valuation takes half-integer values; (2) O/πO has four
elements and is a field, 𝔽₄ = {0, 1, ζ, ζ²} with ζ = (−1 + i + j + k)/2 of order 3; (3) exp converges on v ≥ 3/2 and
not at v = 1 (the terms of exp(2) do not shrink); (4) the 24 Hurwitz units are exactly the elements of norm 1 in the
GLOBAL Hurwitz order O (the torsion of O^×): the torsion the reading names — in the 2-adic order O₂ the torsion is
their conjugacy classes, infinitely many square roots of −1 among them ((3i + 4j)/5 is one), which the reading does
not read; (5) k = 1 + π ζ exactly — the quaternionic doll of one shell; (6) i and j are not principal (v(i − 1) = ½)
while the principal units start at v ≥ 3/2; (7) the no-go at 2: ([i][j]) has no value, the two torsion logs do not
commute; (8) the units of O₂ the reading reads are few: of the 48 classes of O^×/(1 + π³O) half have a Hurwitz
representative, and of 2000 random units of O₂ only those whose torsion and principal parts commute have a log
(a few per cent). Exits 0 iff all hold."""
from h_common import *  # noqa: F401,F403
import quatplace as QP
from fractions import Fraction as Fr
import random

P = QP.HPlace(2)
pi = QP.HQ(1, 1)
zeta = QP.HQ(Fr(-1, 2), Fr(1, 2), Fr(1, 2), Fr(1, 2))
checks = []
checks.append(("v(π) = ½ for π = 1 + i, v(2) = 1, v(π²) = 1 with π² = 2i", P.val(pi) == Fr(1, 2) and P.val(QP.HQ(2)) == 1 and pi * pi == QP.HQ(0, 2)))
reps = []
cands = [QP.HQ(a, b, c, d) for a in range(2) for b in range(2) for c in range(2) for d in range(2)]
cands += [QP.HQ(Fr(a, 2), Fr(b, 2), Fr(c, 2), Fr(d, 2)) for a in (1, -1) for b in (1, -1) for c in (1, -1) for d in (1, -1)]
for q in cands:
    if not any(P.congruent(q, r, 1) for r in reps):
        reps.append(q)
field = len(reps) == 4
z3 = zeta * zeta * zeta == QP.ONE
nonzero = [r for r in reps if not P.congruent(r, QP.HQ(), 1)]
mult_closed = all(any(P.congruent(x * y, r, 1) for r in nonzero) for x in nonzero for y in nonzero)
checks.append((f"O/πO has {len(reps)} elements, its nonzero classes close under multiplication (a field, 𝔽₄), and ζ³ = 1", field and z3 and mult_closed))
def converges(x, terms=40):
    term, vals = QP.ONE, []
    for n in range(1, terms):
        term = (term * x).scale(Fr(1, n))
        vals.append(Fr(QP.vp(term.norm(), 2), 2) if not term.is_zero() else Fr(10 ** 6))   # v = v₂(N)/2 on all of ℍ₂
    return vals[-1] > vals[0] + 5
checks.append(("exp converges for v(x) ≥ 3/2 (x = π³) and not at v = 1 (x = 2): the radius is the half-shell 3/2", converges(pi * pi * pi) and not converges(QP.HQ(2))))
units24 = QP.hurwitz_units()
norm1 = []
for a2 in range(-2, 3):
    for b2 in range(-2, 3):
        for c2 in range(-2, 3):
            for d2 in range(-2, 3):
                q = QP.HQ(Fr(a2, 2), Fr(b2, 2), Fr(c2, 2), Fr(d2, 2))
                if P.in_order(q) and q.norm() == 1:
                    norm1.append(q)
closed = all((x * y) in units24 for x in units24 for y in units24)
checks.append((f"the elements of norm 1 in the global Hurwitz order O are exactly the 24 Hurwitz units ({len(norm1)} found), closed under the product: 2T, the torsion of O^×", len(norm1) == 24 and set(norm1) == set(units24) and closed))
q45 = QP.HQ(0, Fr(3, 5), Fr(4, 5), 0)
checks.append(("in O₂ the torsion is larger: (3i + 4j)/5 has v = 0, squares to −1 and is none of the 24 — the reading names the 24 only",
               P.val(q45) == 0 and q45 * q45 == -QP.ONE and q45 not in units24))
checks.append(("k = 1 + π ζ exactly — the quaternionic doll with one shell (JP v0.3)", QP.ONE + pi * zeta == QP.K))
checks.append(("i and j are not principal (v(i − 1) = ½); 1 + π³x is principal: the log converges there",
               P.val(QP.I - QP.ONE) == Fr(1, 2) and P.is_principal(QP.ONE + pi * pi * pi * QP.HQ(1, 2, 0, 1)) and not P.is_principal(QP.I)))
e = lambda s: QP.evaluate(F.parse(s), {}, P)  # noqa: E731
nogo = False
try:
    e("([i][j])")
except QP.NotAForm:
    nogo = True
checks.append(("the no-go at 2: ([i][j]) has no value (the logs of i and j do not commute), while ([i ; j]) = k", nogo and P.equal(e("([i ; j])"), e("k"))))
# the index of 2T·(1 + π³O) in O^×: 2 (half the units have no log in this reading)
classes = []
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for q in (QP.HQ(a, b, c, d), QP.HQ(Fr(2*a+1, 2), Fr(2*b+1, 2), Fr(2*c+1, 2), Fr(2*d+1, 2))):
                    if P.val(q) != 0:
                        continue
                    if not any(P.congruent(q, r, 3) for r in classes):
                        classes.append(q)
with_log = sum(1 for r in classes if any(P.is_principal(t.inverse() * r) for t in units24))
checks.append((f"O^×/(1 + π³O) has {len(classes)} classes; {with_log} of them are a Hurwitz unit times a principal unit: index 2 — the first filter on the logs the reading knows", len(classes) == 48 and with_log == 24))
rng = random.Random(2026)
read = 0
N = 2000
for _ in range(N):
    q = QP.HQ(*[rng.randint(-40, 40) for _ in range(4)])
    if rng.random() < 0.5:
        q = QP.HQ(*[Fr(2 * rng.randint(-20, 20) + 1, 2) for _ in range(4)])
    if P.val(q) != 0:
        continue
    try:
        P.log(P.number(q))
        read += 1
    except (QP.NotAForm, QP.F.Undefined):
        pass
checks.append((f"of {N} random units of O₂, {read} have a log in the reading (torsion and principal parts commuting): a few per cent — the rest are owed", 0 < read < N // 10))
report("H.ramified-place", checks)
