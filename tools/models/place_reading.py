"""Witness for place.reading — the reading at a place (tools/place.py) at p = 2, 3, 5, 7, 13:
 (1) the counit ([A]) ≐ A is exact on random residues;
 (2) the three counts of [A] — the number part, the count of [p], the count of J_p — reassemble A, and the count
     of [p] is v_p(A);
 (3) the period: [()] reads (p−1)·J_p (2·J_2 at 2), is not void, its instance is one, and (ω A) ≐ (A) on the radius.
Exits 0 iff all hold."""
import os, sys, random
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import forms as F, place as PL

rng = random.Random(13)
fails = []
for p in PL.PLACES:
    P = PL.Place(p)
    ev = lambda s, env=None: PL.evaluate(F.parse(s), env or {}, P)
    for _ in range(40):
        A = Fraction(rng.randint(1, P.M - 1))
        env = {"A": A}
        if not P.equal(ev("([A])", env), ev("A", env)):
            fails.append((p, "counit", A))
        la = ev("[A]", env)
        if la.v != PL.v_p(int(A), p, P.N):
            fails.append((p, "valuation", A, la.v))
        if not P.equal(ev("([A])", env), P.number(A)):
            fails.append((p, "reassembly", A))
    om = ev("ω")
    if om.k != P.torsion or om.v != 0 or om.a != 0:
        fails.append((p, "period", P.fmt(om)))
    if P.equal(om, P.zero()):
        fails.append((p, "ω void"))
    if not P.equal(ev("(ω)"), P.number(1)):
        fails.append((p, "(ω) ≠ 1"))
    for _ in range(20):
        A = Fraction(p ** P.radius * rng.randint(1, 1000))
        env = {"A": A}
        if not P.equal(ev("(ω A)", env), ev("(A)", env)):
            fails.append((p, "wall", A))
if fails:
    print("FAIL", fails[:6]); sys.exit(1)
print("ok: at p = 2, 3, 5, 7, 13 the counit is exact, the three counts reassemble A with the count of [p] its valuation, [()] reads (p−1)·J_p (2·J_2 at 2) and is absorbed by the instance")
