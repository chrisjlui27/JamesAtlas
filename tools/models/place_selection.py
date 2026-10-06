"""Witness for place.selection — for the primes p ≤ 31 and n ≤ 12: (([ω] <[o^{n}]>)) has a value at p exactly when n
divides p − 1 (n divides 2 at p = 2); its n-th power is then one; i = (([J] <[oo]>)) exists exactly at p ≡ 1 mod 4
and ζ₃ = (([ω] <[ooo]>)) exactly at p ≡ 1 mod 3. Exits 0 iff so."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import forms as F, place as PL

fails = []
primes = [q for q in range(2, 32) if all(q % d for d in range(2, q))]
for p in primes:
    P = PL.Place(p)
    ev = lambda s: PL.evaluate(F.parse(s), {}, P)
    for n in range(1, 13):
        s = f"(([ω] <[{'o' * n}]>))"
        try:
            z = ev(s); exists = True
        except PL.NotAForm:
            exists = False
        expected = (P.torsion % n == 0)
        if exists != expected:
            fails.append((p, n, "exists" if exists else "absent"))
        if exists and not P.equal(ev(f"([{s}]{'[' + s + ']' if False else ''})") if False else ev(f"({' '.join(['[' + s + ']'] * n)})"), P.number(1)):
            fails.append((p, n, "power ≠ 1"))
    for s, cond in (("(([J] <[oo]>))", p % 4 == 1), ("(([ω] <[ooo]>))", p % 3 == 1)):
        try:
            ev(s); ex = True
        except PL.NotAForm:
            ex = False
        if ex != cond:
            fails.append((p, s, ex))
if fails:
    print("FAIL", fails[:8]); sys.exit(1)
print("ok: for p ≤ 31 and n ≤ 12, ω/n is a form at p exactly when n | p − 1 (n | 2 at 2) and its n-th power is one; i at p ≡ 1 mod 4, ζ₃ at p ≡ 1 mod 3")
