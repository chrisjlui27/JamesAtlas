"""Witness for H.interference (JH-16) — juxtaposed half-turn logs in different planes: exp(π Σ uᵢ) is 1 iff |Σuᵢ| is
an even integer, −1 iff odd, and not real otherwise. (1) 60 random juxtapositions of 2–5 directions; (2) the three
seeds' logs J_i J_j J_k have phase π√3 about (i + j + k)/√3 — neither 1 nor −1; (3) in one plane the law is the
trunk's: J J = ω. Exits 0 iff all hold."""
from h_common import *  # noqa: F401,F403

checks = []
ok1 = True
for _ in range(60):
    us = [unit() for _ in range(RNG.randint(2, 5))]
    s = Q()
    for u in us:
        s = s + u
    val = exp(s.scale(PI))
    m = s.imag_abs()
    if abs(m - round(m)) < 1e-9:
        ok1 = ok1 and close(val, Q(1 if round(m) % 2 == 0 else -1), 1e-6)
    else:
        ok1 = ok1 and not (close(val, Q(1), 1e-6) or close(val, Q(-1), 1e-6))
checks.append(("(J_{u₁} … J_{uₙ}) is 1 iff |Σu| is an even integer, −1 iff odd, neither otherwise", ok1))
s = I + Jq + K
checks.append(("(J_i J_j J_k): phase π√3 about (i+j+k)/√3 — neither 1 nor −1",
               abs(s.imag_abs() - math.sqrt(3)) < 1e-12 and not close(exp(s.scale(PI)), Q(1), 1e-6) and not close(exp(s.scale(PI)), Q(-1), 1e-6)))
e = lambda s: QT.evaluate(F.parse(s), {})  # noqa: E731
checks.append(("in one plane the trunk's law: (J J) = 1, and the chart's (J J) reads 1", close(exp(I.scale(2 * PI)), Q(1), 1e-9) and close(e("(J J)"), Q(1), 1e-9)))
report("H.interference", checks)
