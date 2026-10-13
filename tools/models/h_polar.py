"""Witness for H.polar-form — every q ≠ 0 is r·e^{tπu} (JH-17). (1) q = |q| exp(tπu), t ∈ [0, 1], u the direction of
Im q, on 60 random quaternions; (2) the negative reals are the non-uniqueness locus (t = 1, u free); (3) the unit
quaternions are the suspension of the phase sphere: at t = 0 and t = 1 every u gives one point (±1), between them
the points are distinct. Exits 0 iff all hold."""
from h_common import *  # noqa: F401,F403

checks = []
ok1 = True
for _ in range(60):
    q = rand_q()
    r = abs(q)
    L = log(q)
    t = L.imag_abs() / PI
    u = L.imag().scale(1.0 / L.imag_abs())
    ok1 = ok1 and 0 <= t <= 1 + 1e-9 and close(Q(r) * exp(u.scale(t * PI)), q, 1e-7)
checks.append(("q = |q|·e^{tπu} with t ∈ [0, 1], u = the direction of Im q", ok1))
checks.append(("the negative reals: t = 1 and every u gives the same q (non-uniqueness only there)",
               all(close(Q(r) * exp(unit().scale(PI)), Q(-r), 1e-7) for r in (0.5, 2.0, 7.0))))
ok3 = True
for _ in range(40):
    u, v = unit(), unit()
    ok3 = ok3 and close(exp(u.scale(0.0)), exp(v.scale(0.0)), 1e-9) and close(exp(u.scale(PI)), exp(v.scale(PI)), 1e-9)
    t = RNG.uniform(0.05, 0.95)
    ok3 = ok3 and (close(u, v, 1e-6) or not close(exp(u.scale(t * PI)), exp(v.scale(t * PI)), 1e-6))
checks.append(("S³ is the suspension of the phase sphere: the poles t = 0, 1 pinch every direction to ±1, the rest are distinct", ok3))
report("H.polar-form", checks)
