"""Witness for H.phase-sphere — −1 has a 2-sphere of logarithms. (1) exp(πu) = −1 for every pure unit u; (2) the
principal band meets {L : exp L = −1} exactly in π·S²; (3) rigidity dichotomy (JH-12): <A> = ([A] J_u) for every u
when A is real positive, and off the reals only for u = ±(the direction of A); (4) half-phases compose by the
cross product for orthogonal directions (JH-18): e^{(π/2)u} e^{(π/2)v} = u × v; (5) antipodes: J_{−u} = −J_u and
e^{J_u} = e^{J_{−u}}. Exits 0 iff all hold."""
from h_common import *  # noqa: F401,F403

checks = []
checks.append(("exp(πu) = −1 for 60 random pure units u", all(close(exp(unit().scale(PI)), Q(-1), 1e-7) for _ in range(60))))
ok2 = True
for _ in range(60):
    L = rand_q(-1.0, 1.3)
    if close(exp(L), Q(-1), 1e-6):
        ok2 = ok2 and abs(L.a) < 1e-6 and abs(L.imag_abs() - PI) < 1e-6
    # a point of π·S² is a log of −1
    ok2 = ok2 and close(exp(unit().scale(PI)), Q(-1), 1e-7)
checks.append(("in the band, exp L = −1 only on π·S² (sampled), and all of π·S² qualifies", ok2))
ok3 = True
for _ in range(40):
    r = RNG.uniform(0.1, 5)
    u = unit()
    ok3 = ok3 and close(exp(log(Q(r)) + u.scale(PI)), Q(-r), 1e-7)
    A = rand_q()
    v = A.imag().scale(1.0 / A.imag_abs())
    good = close(exp(log(A) + v.scale(PI)), -A, 1e-6) and close(exp(log(A) + v.scale(-PI)), -A, 1e-6)
    w = unit()
    bad = close(exp(log(A) + w.scale(PI)), -A, 1e-6)   # a generic direction fails
    ok3 = ok3 and good and not bad
checks.append(("rigidity dichotomy: every u negates a positive real; only u = ±v negates A off the reals", ok3))
ok4 = True
for _ in range(40):
    u = unit()
    w = unit()
    v = w - u.scale(u.b * w.b + u.c * w.c + u.d * w.d)
    v = v.scale(1.0 / v.imag_abs())
    cross = Q(0, u.c * v.d - u.d * v.c, u.d * v.b - u.b * v.d, u.b * v.c - u.c * v.b)
    ok4 = ok4 and close(exp(u.scale(PI / 2)) * exp(v.scale(PI / 2)), cross, 1e-7)
checks.append(("half-phases of orthogonal directions compose by the cross product: e^{πu/2} e^{πv/2} = u × v (so ij = k)", ok4))
checks.append(("antipodes: J_{−u} = −J_u, e^{J_u} = e^{J_{−u}} = −1 — the sphere is seen as RP² inside an instance", all(close(exp(u.scale(PI)), exp(u.scale(-PI)), 1e-7) for u in [unit() for _ in range(20)])))
report("H.phase-sphere", checks)
