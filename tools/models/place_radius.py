"""Witness for place.radius — at p = 2, 3, 5, 7, 13: (o), (oo) [odd p], ((o)) have no value; (o^{p} A) is a form for A
in the radius and (o^{p}) is one; at p = 2, (oooo) is a form and (oo) is not. Exits 0 iff so."""
import os, sys, random
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import forms as F, place as PL

rng = random.Random(3)
fails = []
for p in PL.PLACES:
    P = PL.Place(p)
    ev = lambda s, env=None: PL.evaluate(F.parse(s), env or {}, P)
    for s in ("(o)", "((o))") + (("(oo)",) if p != 2 else ()):
        try:
            ev(s); fails.append((p, "a form", s))
        except PL.OutsideRadius:
            pass
    pile = "o" * (p if p != 2 else 4)
    try:
        ev(f"({pile})")
    except PL.NotAForm as ex:
        fails.append((p, "radius", str(ex)))
    for _ in range(20):
        A = Fraction(p ** P.radius * rng.randint(1, 500))
        try:
            ev(f"({pile} A)", {"A": A})
        except PL.NotAForm as ex:
            fails.append((p, "(p A)", A, str(ex)))
    if p == 2:
        try:
            ev("(oo)"); fails.append((2, "(oo) a form at 2"))
        except PL.OutsideRadius:
            pass
if fails:
    print("FAIL", fails[:6]); sys.exit(1)
print("ok: e is not p-adic at any tested place; the instance of a multiple of p (of 4 at 2) is a number; (oooo) is a form at 2 and (oo) is not")
