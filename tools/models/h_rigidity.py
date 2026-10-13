"""Witness for H.rigidity-dichotomy (JH-12) — a negation is a half-turn in which planes? (1) <A> = ([A] J_u) for every
pure unit u when A is a positive real; (2) for A off the reals only for u = ±(the direction of Im A); (3) a generic
direction fails. Exits 0 iff all hold."""
from h_common import *  # noqa: F401,F403

checks = []
ok1 = ok2 = ok3 = True
for _ in range(40):
    r = RNG.uniform(0.1, 5)
    u = unit()
    ok1 = ok1 and close(exp(log(Q(r)) + u.scale(PI)), Q(-r), 1e-7)
    A = rand_q()
    v = A.imag().scale(1.0 / A.imag_abs())
    ok2 = ok2 and close(exp(log(A) + v.scale(PI)), -A, 1e-6) and close(exp(log(A) + v.scale(-PI)), -A, 1e-6)
    w = unit()
    ok3 = ok3 and not close(exp(log(A) + w.scale(PI)), -A, 1e-6)
checks.append(("a positive real is negated by a half-turn in every plane: e^{ln r + πu} = −r for every u", ok1))
checks.append(("A off the reals is negated by the half-turn in its own plane, u = ±dir(Im A)", ok2))
checks.append(("— and by no other: a random direction w gives e^{log A + πw} ≠ −A", ok3))
report("H.rigidity-dichotomy", checks)
