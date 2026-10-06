"""Witness for place.no-inverse-of-the-prime — at p = 2, 3, 5, 7, 13: (<[o^{p}]>) has no value; ([o^{p}] [(<[o^{p}]>)])
has none either; every unit's reciprocal is a form, and times the unit gives one. Exits 0 iff so."""
import os, sys, random
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import forms as F, place as PL

rng = random.Random(9)
fails = []
for p in PL.PLACES:
    P = PL.Place(p)
    ev = lambda s, env=None: PL.evaluate(F.parse(s), env or {}, P)
    pp = "[" + "o" * p + "]"
    for s in (f"(<{pp}>)", f"({pp} [(<{pp}>)])"):
        try:
            ev(s); fails.append((p, "a form", s))
        except PL.NotAForm:
            pass
    for _ in range(30):
        U = rng.randint(1, P.M - 1)
        if U % p == 0:
            continue
        env = {"U": Fraction(U)}
        try:
            r = ev("(<[U]>)", env)
        except PL.NotAForm as ex:
            fails.append((p, "unit reciprocal", U, str(ex))); continue
        if not P.equal(ev("([U] [(<[U]>)])", env), P.number(1)):
            fails.append((p, "U · 1/U", U))
if fails:
    print("FAIL", fails[:6]); sys.exit(1)
print("ok: the reciprocal of the prime is not a form at any tested place; every unit's reciprocal is, and multiplies back to one")
