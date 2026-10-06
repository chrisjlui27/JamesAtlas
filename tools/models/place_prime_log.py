"""Witness for place.prime-log — [p] := [o^{p}] at p = 2, 3, 5, 7, 13: the count of [p] in [A] is v_p(A) for random A;
[o^{p}] has no number part and no torsion count; k copies of [p] are the log of p^k. Exits 0 iff so."""
import os, sys, random
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import forms as F, place as PL

rng = random.Random(5)
fails = []
for p in PL.PLACES:
    P = PL.Place(p)
    ev = lambda s, env=None: PL.evaluate(F.parse(s), env or {}, P)
    lp = ev("o" * p and "[" + "o" * p + "]")
    if lp.a != 0 or lp.v != 1 or lp.k != 0:
        fails.append((p, "[p]", P.fmt(lp)))
    for _ in range(40):
        A = Fraction(rng.randint(1, P.M - 1))
        la = ev("[A]", {"A": A})
        if la.v != PL.v_p(int(A), p, P.N):
            fails.append((p, "count", A, la.v))
    for k in range(1, 4):
        if not P.equal(ev("[" + "o" * p + "]" * 1 + " " + " ".join(["[" + "o" * p + "]"] * (k - 1))), ev("[A]", {"A": Fraction(p ** k)})):
            fails.append((p, "k copies", k))
if fails:
    print("FAIL", fails[:6]); sys.exit(1)
print("ok: [o^{p}] is a pure count of [p] at every tested place; the count of [p] in [A] is v_p(A); k copies of [p] are the log of p^k")
