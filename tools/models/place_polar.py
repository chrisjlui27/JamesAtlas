"""Witness for place.polar-form — at p = 2, 3, 5, 7, 13 random residues split by [ ] into the three counts and
reassembled by ( ) come back; the principal unit is the instance of a multiple of p. Exits 0 iff so."""
import os, sys, random
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import forms as F, place as PL

rng = random.Random(21)
fails = []
for p in PL.PLACES:
    P = PL.Place(p)
    for _ in range(40):
        A = rng.randint(1, P.M - 1)
        x = P.log(P.number(Fraction(A)))
        v, k, a = int(x.v), int(x.k) % P.torsion, x.a
        t = P.teich(pow(P.g, k, p)) if p != 2 else (-1 if k else 1)
        u = P.exp(a, x.prec)
        back = u * t * p ** v % P.M
        if (back - A) % (p ** min(x.prec + v, P.N)) != 0:
            fails.append((p, A, back))
        if a % p ** P.radius != 0:
            fails.append((p, A, "principal unit's log not in the radius"))
if fails:
    print("FAIL", fails[:6]); sys.exit(1)
print("ok: every residue at every tested place is p^v · τ^k · exp(a) with a in the radius — the three counts reassemble")
