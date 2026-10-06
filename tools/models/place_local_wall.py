"""Witness for place.local-wall — e_p(k) = the largest e with λ(p^e) | 2k, computed locally for each prime, and the
product ∏_p p^{e_p(k)} against M(2k) = 24, 240, 504, 480, 264, 65520, 24, 16320 (J1.wall-census) for k = 1 … 8;
and the closed forms e_p = 1 + v_p(k) for odd p with (p−1) | 2k, e_2 = 3 + v_2(k). Exits 0 iff all agree."""
import sys
from math import gcd

M = {1: 24, 2: 240, 3: 504, 4: 480, 5: 264, 6: 65520, 7: 24, 8: 16320}


def carmichael_pp(p, e):
    if p == 2:
        return 1 if e == 1 else (2 if e == 2 else 2 ** (e - 2))
    return (p - 1) * p ** (e - 1)


def v(p, n):
    c = 0
    while n % p == 0:
        n //= p; c += 1
    return c


fails = []
primes = [q for q in range(2, 200) if all(q % d for d in range(2, q))]
for k, m in M.items():
    prod = 1
    for p in primes:
        e = 0
        while (2 * k) % carmichael_pp(p, e + 1) == 0:
            e += 1
        closed = (3 + v(2, k)) if p == 2 else ((1 + v(p, k)) if (2 * k) % (p - 1) == 0 else 0)
        if e != closed:
            fails.append((k, p, e, closed))
        prod *= p ** e
    if prod != m:
        fails.append((k, prod, m))
if fails:
    print("FAIL", fails[:6]); sys.exit(1)
print("ok: M(2k) = ∏_p p^{e_p(k)} for k = 1 … 8 with e_p the largest e such that λ(p^e) | 2k; e_2 = 3 + v_2(k), e_p = 1 + v_p(k) when (p−1) | 2k")
