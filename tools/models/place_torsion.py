"""Witness for place.torsion — J_p at p = 3, 5, 7, 13 (and J_2 at 2): the Teichmüller generator τ has τ^{p−1} ≐ o and
τ^{(p−1)/2} ≐ <o>; [<o>] reads (p−1)/2·J_p (J_2 at 2); [τ] reads J_p with a void number part; (J) ≐ <o> and
<A> ≐ ([A] J) hold at every place for random A. Exits 0 iff so."""
import os, sys, random
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import forms as F, place as PL

rng = random.Random(17)
fails = []
for p in PL.PLACES:
    P = PL.Place(p)
    ev = lambda s, env=None: PL.evaluate(F.parse(s), env or {}, P)
    tau = P.teich(P.g) if p != 2 else P.M - 1   # at 2 the torsion is ±1: τ = −1
    env = {"T": Fraction(tau)}
    if not P.equal(ev("(([[T]] [A]))", {"T": Fraction(tau), "A": Fraction(P.torsion)}), P.number(1)):
        fails.append((p, "τ^{p−1} ≠ 1"))
    if p != 2 and not P.equal(ev("(([[T]] [A]))", {"T": Fraction(tau), "A": Fraction((p - 1) // 2)}), P.number(-1)):
        fails.append((p, "τ^{(p−1)/2} ≠ −1"))
    J = ev("J")
    if J.v != 0 or J.a != 0 or J.k != Fraction(P.torsion, 2):
        fails.append((p, "J", P.fmt(J)))
    lt = ev("[T]", env)
    if lt.a != 0 or lt.v != 0 or lt.k != 1:
        fails.append((p, "[τ]", P.fmt(lt)))
    if not P.equal(ev("(J)"), P.number(-1)):
        fails.append((p, "(J) ≠ −1"))
    for _ in range(30):
        A = Fraction(rng.randint(1, P.M - 1))
        e2 = {"A": A}
        if not P.equal(ev("<A>", e2), ev("([A] J)", e2)):
            fails.append((p, "phase rule", A))
if fails:
    print("FAIL", fails[:6]); sys.exit(1)
print("ok: at every tested place the Teichmüller generator has order p − 1 with −1 its half, [<o>] is half the period, [τ] is the torsion log alone, (J) ≐ <o> and the Phase rule holds")
