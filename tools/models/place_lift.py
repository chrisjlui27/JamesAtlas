"""Witness for place.lift — at p = 3, 5, 7, 11, 13, 17 and the units a ≤ 40: the root form (([[A]] <[oo]>)) has a
value exactly when a is a square mod p, and squares back to a; Newton's step ([X ([A] <[X]>)] <[oo]>) from the
root mod p agrees with the root form to 2, 4, 8, 16, 32 shells in turn (depth 33 at 3, …). Exits 0 iff so."""
import os, sys
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import forms as F, place as PL

fails = []
checked = 0
for p in (3, 5, 7, 11, 13, 17):
    P = PL.Place(p, N=34)
    ev = lambda s, env: PL.evaluate(F.parse(s), env, P)
    squares = {x * x % p for x in range(1, p)}
    for a in range(1, 41):
        if a % p == 0:
            continue
        env = {"A": Fraction(a)}
        try:
            r = ev("(([[A]] <[oo]>))", env); exists = True
        except PL.NotAForm:
            exists = False
        if exists != (a % p in squares):
            fails.append((p, a, "root form", exists)); continue
        if not exists:
            continue
        checked += 1
        if not P.equal(ev("([R] [R])", {"R": Fraction(r.a)}), P.number(a)):
            fails.append((p, a, "root squared ≠ a"))
        # Newton from a root mod p, agreeing with the root form to 2, 4, 8, 16, 32 shells
        x0 = next(x for x in range(1, p) if (x * x - a) % p == 0)
        if (x0 - r.a) % p:
            x0 = p - x0   # the other root mod p: the one the root form lifts
        x = Fraction(x0)
        for shells in (2, 4, 8, 16, 32):
            x = Fraction(ev("([X ([A] <[X]>)] <[oo]>)", {"X": x, "A": Fraction(a)}).a)
            if (int(x) - r.a) % p ** shells:
                fails.append((p, a, "newton", shells)); break
if fails:
    print("FAIL", fails[:6]); sys.exit(1)
print(f"ok: {checked} roots at p = 3, 5, 7, 11, 13, 17 — the root form exists exactly for the squares mod p, squares back, and Newton's step from the root mod p reaches it to 2, 4, 8, 16, 32 shells")
