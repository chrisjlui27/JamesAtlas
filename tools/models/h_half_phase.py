"""Witness for H.half-phase (JH-18) — quarter turns in orthogonal planes compose by the cross product:
e^{(π/2)u} e^{(π/2)v} = u × v for u ⟂ v; with u = i, v = j the product is k. (1) 40 random orthogonal pairs;
(2) the chart's own forms: ([i ; j]) = k, and (([J] <[oo]>)), (([Jj] <[oo]>)) — the instances of half the seeds' logs — are i and j. Exits 0 iff
all hold."""
from h_common import *  # noqa: F401,F403

checks = []
ok1 = True
for _ in range(40):
    u = unit()
    w = unit()
    v = w - u.scale(u.b * w.b + u.c * w.c + u.d * w.d)
    v = v.scale(1.0 / v.imag_abs())
    cross = Q(0, u.c * v.d - u.d * v.c, u.d * v.b - u.b * v.d, u.b * v.c - u.c * v.b)
    ok1 = ok1 and close(exp(u.scale(PI / 2)) * exp(v.scale(PI / 2)), cross, 1e-7)
checks.append(("half-phases of orthogonal directions compose by the cross product: e^{πu/2} e^{πv/2} = u × v", ok1))
e = lambda s: QT.evaluate(F.parse(s), {})  # noqa: E731
checks.append(("on the page: (([J] <[oo]>)) = i, (([Jj] <[oo]>)) = j — the half-phases e^{πi/2}, e^{πj/2} — and ([i ; j]) = k = i × j",
               close(e("(([J] <[oo]>))"), I, 1e-9) and close(e("(([Jj] <[oo]>))"), Jq, 1e-9) and close(e("([i ; j])"), K, 1e-9)))
report("H.half-phase", checks)
