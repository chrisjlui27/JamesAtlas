"""Witness for place.polar-form — at p = 2, 3, 5, 7, 13 random residues split by [ ] into the three counts and
reassembled by ( ) come back; the principal unit is the instance of a multiple of p; and the law's right-hand side
([p]^{v} [T]^{k} ([p][B])) is a form that reads p^v·τ^k·exp(pB) (4B at p = 2). Exits 0 iff so."""
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
# the law's right-hand side as a form: ([p]^{v} [T]^{k} ([p][B])) — [p] = [o^{p}], [T] the torsion log (the log of
# the instance of ω/(p−1); [<o>] at 2), ([p][B]) a multiple of p (of 4 at 2) — evaluates to p^v·τ^k·exp(pB)
for p in PL.PLACES:
    P = PL.Place(p)
    pile = "o" * p
    T = "[<o>]" if p == 2 else f"[(([ω] <[{'o' * (p - 1)}]>))]"
    mult = "[oooo]" if p == 2 else f"[{pile}]"
    for _ in range(20):
        v, k, B = rng.randint(0, 2), rng.randint(0, P.torsion - 1), rng.randint(1, 500)
        form = "(" + f"[{pile}]" * v + T * k + f"({mult}[{'o' * B}])" + ")"
        val = PL.evaluate(F.parse(form), {}, P)
        t = (-1 if k else 1) if p == 2 else P.teich(pow(P.g, k, p))
        want = p ** v * t * P.exp(p ** P.radius * B, P.N) % P.M
        if not val.number or (val.a - want) % (p ** P.depth) != 0:
            fails.append((p, form[:40], P.fmt(val), want))
if fails:
    print("FAIL", fails[:6]); sys.exit(1)
print("ok: every residue at every tested place is p^v · τ^k · exp(a) with a in the radius — the three counts reassemble; "
      "the form ([p]^{v} [T]^{k} ([p][B])) reads p^v·τ^k·exp(pB) at p = 2, 3, 5, 7, 13 (4B at 2)")
