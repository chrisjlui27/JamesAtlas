"""Witness for H.no-go — the Slice theorem (JH-1). (a) `[A][B]` and `[B][A]` are one form, so a reading sound for the
multiplication encoding is commutative on its domain; (b) in ℍ the encoding fails for generic contents and holds for
co-sliced ones; (c) commuting quaternions have parallel pure parts, so pairwise-commuting sets lie in one slice;
(d) in-band rigidity: for X, Y in the band |Im| < π, exp(X + Y) = exp X · exp Y iff XY = YX — and the bound is
sharp: out of band, X = 4πu, Y = 3πv (u ⟂ v) gives exp(X+Y) = exp X · exp Y = −1 though [X, Y] ≠ 0. Exits 0 iff
all hold."""
from h_common import *  # noqa: F401,F403

checks = []
checks.append(("[A][B] and [B][A] are the same form", F.parse("[A][B]") == F.parse("[B][A]")))
generic_fail = 0
sliced_ok = 0
for _ in range(60):
    A, B = rand_q(), rand_q()
    if not close(exp(log(A) + log(B)), A * B, 1e-6):
        generic_fail += 1
    u = unit()
    x, y = (Q(RNG.uniform(0.2, 3)) + u.scale(RNG.uniform(-2, 2))), (Q(RNG.uniform(0.2, 3)) + u.scale(RNG.uniform(-2, 2)))
    # co-sliced: the logs lie in the slice of u only when the pinning agrees (positive real part keeps them in band)
    if close(exp(log(x) + log(y)), x * y, 1e-6) or close(exp(log(x) + log(y)), -(x * y), 1e-6):
        sliced_ok += 1
checks.append((f"generic contents: exp(log A + log B) ≠ AB on {generic_fail}/60 samples (the encoding fails)", generic_fail >= 55))
checks.append((f"co-sliced contents: exp(log x + log y) = xy up to the seam's sign on {sliced_ok}/60 samples", sliced_ok >= 58))
par = 0
for _ in range(60):
    u = unit()
    p, q = Q(RNG.uniform(-2, 2)) + u.scale(RNG.uniform(-2, 2)), Q(RNG.uniform(-2, 2)) + u.scale(RNG.uniform(-2, 2))
    if p.commutes(q):
        par += 1
    r = rand_q()
    if (p * r - r * p).imag_abs() < 1e-9:   # a generic r commutes with p only if parallel
        par -= 100
checks.append(("commuting ⟺ parallel pure parts (pq − qp = 2 P×Q)", par == 60))
rig_ok = True
for _ in range(80):
    X, Y = rand_q(-1.5, 0.3), rand_q(-1.5, 0.3)
    if not (in_band(X) and in_band(Y) and in_band(X + Y)):
        continue
    lhs, rhs = exp(X + Y), exp(X) * exp(Y)
    if close(lhs, rhs, 1e-7) != X.commutes(Y, 1e-7):
        rig_ok = False
checks.append(("in-band rigidity: exp(X+Y) = exp X exp Y iff [X, Y] = 0 (sampled in the band)", rig_ok))
u, v = I, Jq
X, Y = u.scale(4 * PI), v.scale(3 * PI)
coincide = close(exp(X + Y), exp(X) * exp(Y), 1e-6) and not X.commutes(Y)
checks.append(("sharpness: X = 4πi, Y = 3πj — exp(X+Y) = exp X exp Y = −1 though [X, Y] ≠ 0 (out of band)", coincide and close(exp(X) * exp(Y), Q(-1), 1e-6)))
report("H.no-go", checks)
