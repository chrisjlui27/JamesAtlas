"""Witness for H.ramification — the Hilbert symbol (−1, −1)_p: +1 at every odd p (x² + y² ≡ −1 mod p is solvable, and
lifts), −1 at 2 (−1 is not a sum of two squares in ℚ₂: x² + y² + z² = 0 has no primitive 2-adic solution, since
squares are ≡ 0, 1, 4 mod 8) and at ∞ (x² + y² = −1 has no real solution). So Hamilton's quaternions ramify exactly
at {2, ∞}: the Hurwitz places. Exits 0 iff all hold."""
from h_common import *  # noqa: F401,F403

checks = []
for p in (3, 5, 7, 11, 13, 17, 19, 23):
    sol = any((x * x + y * y + 1) % p == 0 for x in range(p) for y in range(p))
    checks.append((f"p = {p}: x² + y² ≡ −1 solvable (split)", sol))
# at 2: no primitive solution of x² + y² + z² ≡ 0 mod 8 with not all even
prim = any((x * x + y * y + z * z) % 8 == 0 and (x % 2 or y % 2 or z % 2) for x in range(8) for y in range(8) for z in range(8))
checks.append(("p = 2: x² + y² + z² ≡ 0 mod 8 has no primitive solution — (−1, −1)₂ = −1 (ramified)", not prim))
real = all(x * x + y * y + 1 > 0 for x in range(-50, 51) for y in range(-50, 51))
checks.append(("∞: x² + y² + 1 > 0 on a grid of reals — x² + y² = −1 has no real solution, (−1, −1)_∞ = −1 (ramified)", real))
symbols = {p: 1 for p in (3, 5, 7, 11, 13, 17, 19, 23)}
symbols[2] = -1 if not prim else 1
symbols["∞"] = -1 if real else 1
prod = 1
for v in symbols.values():
    prod *= v
checks.append((f"the product formula on these places: ∏ (−1, −1)_v = {prod} — the ramified set {{2, ∞}} has even size", prod == 1 and sorted((str(k) for k, v in symbols.items() if v == -1)) == ["2", "∞"]))
report("H.ramification", checks)
