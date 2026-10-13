"""Witness for H.120-law (JH-15) — two juxtaposed half-turn logs are a third exactly when their directions are 120°
apart: |u + v| = 1 ⟹ exp(π(u + v)) = −1, J_u J_v = J_{u+v}. (1) 40 random pairs at 120°; (2) pairs at other angles
fail; (3) the triangle: three directions at mutual 120° in a plane sum to zero, so J_u J_v J_w is the log of 1.
Exits 0 iff all hold."""
from h_common import *  # noqa: F401,F403


def at_angle(u, theta):
    w = unit()
    w = w - u.scale(u.b * w.b + u.c * w.c + u.d * w.d)
    w = w.scale(1.0 / w.imag_abs())
    return u.scale(math.cos(theta)) + w.scale(math.sin(theta)), w


checks = []
ok1 = ok2 = True
for _ in range(40):
    u = unit()
    v, w = at_angle(u, 2 * PI / 3)
    s = u + v
    ok1 = ok1 and abs(s.imag_abs() - 1.0) < 1e-9 and close(exp(s.scale(PI)), Q(-1), 1e-7)
    theta = RNG.uniform(0.2, 2.9)
    if abs(theta - 2 * PI / 3) > 0.05:
        v2, _ = at_angle(u, theta)
        ok2 = ok2 and not close(exp((u + v2).scale(PI)), Q(-1), 1e-6)
checks.append(("|u + v| = 1 ⟹ π(u + v) ∈ π·S²: (J_u J_v) = −1, J_u J_v = J_{u+v}", ok1))
checks.append(("at any other angle the juxtaposition is not a half-turn log: (J_u J_v) ≠ −1", ok2))
ok3 = True
for _ in range(20):
    u = unit()
    v, w0 = at_angle(u, 2 * PI / 3)
    w = u.scale(math.cos(4 * PI / 3)) + w0.scale(math.sin(4 * PI / 3))
    s = u + v + w
    ok3 = ok3 and s.imag_abs() < 1e-9 and close(exp(s.scale(PI)), Q(1), 1e-9)
checks.append(("three directions at mutual 120° sum to zero: (J_u J_v J_w) = 1", ok3))
report("H.120-law", checks)
