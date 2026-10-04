"""Witness for J1.wall-census (and the import J1.von-staudt-clausen) — the ψ-wall selection computed natively:
ω/n survives at level k iff (ψ^r − 1)(ω/n) ∈ Λ for every r coprime to n, i.e. n | r^{2k} − 1 for all such r,
i.e. the Carmichael function λ(n) divides 2k. M(2k) = the largest such n: M(2) = 24, M(4) = 240, M(6) = 504.
The import: M(2k) equals the denominator of B_{2k}/4k (von Staudt–Clausen / Adams), checked here numerically
for k = 1, 2, 3 with exact rationals. Exits 0 iff both agree.
"""
import sys
from fractions import Fraction
from math import gcd


def carmichael(n):
    from math import lcm
    def lam_pp(p, e):
        if p == 2:
            return 1 if e == 1 else (2 if e == 2 else 2 ** (e - 2))
        return (p - 1) * p ** (e - 1)
    out, m, p = 1, n, 2
    while p * p <= m:
        if m % p == 0:
            e = 0
            while m % p == 0:
                m //= p; e += 1
            out = lcm(out, lam_pp(p, e))
        p += 1
    if m > 1:
        out = lcm(out, lam_pp(m, 1))
    return out


def survives(n, k):
    """n | r^{2k} − 1 for all r coprime to n — by brute force, the native statement."""
    if n == 1:
        return True
    return all(pow(r, 2 * k, n) == 1 for r in range(1, n + 1) if gcd(r, n) == 1)


def M(k, bound=3000):
    best = 1
    for n in range(1, bound):
        if survives(n, k):
            best = n
    return best


def bernoulli(m):
    """B_0..B_m by the Akiyama–Tanigawa algorithm, exact."""
    A = [Fraction(0)] * (m + 1)
    B = []
    for i in range(m + 1):
        A[i] = Fraction(1, i + 1)
        for j in range(i, 0, -1):
            A[j - 1] = j * (A[j - 1] - A[j])
        B.append(A[0])
    return B


B = bernoulli(6)
results = {}
for k in (1, 2, 3):
    m = M(k)
    denom = (B[2 * k] / (4 * k)).denominator
    results[k] = (m, denom)
expected = {1: 24, 2: 240, 3: 504}
ok = all(results[k][0] == expected[k] == results[k][1] for k in results)
# the Carmichael characterisation agrees with brute force on 1..600
for k in (1, 2, 3):
    for n in range(1, 600):
        if survives(n, k) != ((2 * k) % carmichael(n) == 0):
            ok = False
print({k: f"M({2*k}) = {v[0]}, denom(B_{2*k}/{4*k}) = {v[1]}" for k, v in results.items()})
sys.exit(0 if ok else 1)
