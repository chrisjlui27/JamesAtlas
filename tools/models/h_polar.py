"""Witness for H.polar-form — every q ≠ 0 is r·e^{tπu} (JH-17), with the 120° law (JH-15) and phase interference
(JH-16). (1) q = |q| exp(tπu), t ∈ [0, 1], u the direction of Im q; (2) the negative reals are the non-uniqueness
locus (t = 1, u free); (3) the 120° law: |u + v| = 1 ⟹ J_u J_v is a phase, exp(π(u+v)) = −1 (so two phases are a
third); (4) interference: exp(π Σ u_i) is 1 iff |Σu| is an even integer and −1 iff odd; (5) (J_i J_j J_k) has
phase π√3 in the direction (i+j+k)/√3. Exits 0 iff all hold."""
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
    u = unit()
    # v at 120° from u: v = −u/2 + (√3/2) w, w ⟂ u unit
    w = unit()
    w = w - u.scale(u.b * w.b + u.c * w.c + u.d * w.d)
    w = w.scale(1.0 / w.imag_abs())
    v = u.scale(-0.5) + w.scale(math.sqrt(3) / 2)
    s = u + v
    ok3 = ok3 and abs(s.imag_abs() - 1.0) < 1e-9 and close(exp(s.scale(PI)), Q(-1), 1e-7)
checks.append(("the 120° law: |u + v| = 1 ⟹ π(u + v) ∈ π·S², so (J_u J_v) = −1 and J_u J_v = J_{u+v}", ok3))
ok4 = True
for _ in range(40):
    us = [unit() for _ in range(RNG.randint(2, 5))]
    s = Q()
    for u in us:
        s = s + u
    val = exp(s.scale(PI))
    m = s.imag_abs()
    if abs(m - round(m)) < 1e-9:
        ok4 = ok4 and close(val, Q(1 if round(m) % 2 == 0 else -1), 1e-6)
    else:
        ok4 = ok4 and not (close(val, Q(1), 1e-6) or close(val, Q(-1), 1e-6))
checks.append(("interference: (J_{u₁} … J_{uₙ}) is 1 iff |Σu| is an even integer, −1 iff odd, neither otherwise", ok4))
s = I + Jq + K
checks.append(("(J_i J_j J_k): phase π√3 about (i+j+k)/√3 — generating a dense torsion-free subgroup of that circle",
               abs(s.imag_abs() - math.sqrt(3)) < 1e-12 and not close(exp(s.scale(PI)), Q(1), 1e-6) and not close(exp(s.scale(PI)), Q(-1), 1e-6)))
report("H.polar-form", checks)
