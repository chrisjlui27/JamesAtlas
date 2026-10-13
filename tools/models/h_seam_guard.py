"""Witness for H.seam-guard — the sphere seam (JH-3). (1) L(exp(πu)) = πi ≠ πu for u ≠ i: the involution-down
`[(A)] → A` is false on the angle-π sphere off the pinned ray; (2) the blow-up it would license if unguarded:
with a second seed J_v = πv, the unguarded step proves (−1)·(−1) ≐ e^{π(i + v)}, a non-real unit ≠ 1; (3) the guard
L(exp V(A)) = V(A) holds exactly on the band (|Im A| < π) plus the pinned ray, and the receipt prover refuses the
step elsewhere (its receipt is no lattice element). Exits 0 iff all hold."""
from h_common import *  # noqa: F401,F403

checks = []
ok1 = True
for _ in range(40):
    u = unit()
    L = log(exp(u.scale(PI)))
    ok1 = ok1 and close(L, I.scale(PI), 1e-7) and (close(u, I, 1e-6) or not close(L, u.scale(PI), 1e-6))
checks.append(("L(e^{πu}) = πi for every pure unit u: the seam is pinned to i, and [(J_u)] → J_u is false off that ray", ok1))
v = Jq
blow = exp(I.scale(PI) + v.scale(PI))
checks.append(("unguarded: (−1)(−1) = e^{J_i} e^{J_v} 'equals' e^{J_i + J_v} = e^{π(i+j)}, a non-real unit ≠ 1 — the blow-up the guard blocks",
               not close(blow, Q(1), 1e-6) and close(exp(I.scale(PI)) * exp(v.scale(PI)), Q(1), 1e-7)))
ok3 = True
for _ in range(60):
    A = rand_q(-1.5, 1.4)
    guard = close(log(exp(A)), A, 1e-6)
    band = A.imag_abs() < PI - 1e-6
    on_ray = abs(A.imag_abs() - PI) < 1e-6 and close(A.imag().scale(1 / A.imag_abs()), I, 1e-6)
    if band or on_ray:
        ok3 = ok3 and guard
    elif A.imag_abs() > PI + 1e-6 or (abs(A.imag_abs() - PI) < 1e-6 and not on_ray):
        ok3 = ok3 and not guard
R = QT.Reading()
checks.append(("the guard L(exp V(A)) = V(A) holds exactly on the band and the pinned ray (sampled)", ok3))
k_seam = R.k(log(exp(Jq.scale(PI))), Jq.scale(PI))
checks.append(("the receipt of [(J_j)] → J_j is no lattice element (k = ?)", k_seam is None))
# the prover itself: a unit step on the seam content Jj at depth 0, and the same step directly inside an instance
import random
import j1 as J1, prover as P, nodes as N
node = N.Node(id="seam-probe", path="", meta={"id": "seam-probe", "domain": "complex", "setting": "JH", "type": "theorem", "level": "object", "equality": "≃"}, sections={}, body="")
red, res = F.parse("[(Jj)]"), F.parse("Jj")
step0 = P.Step(rule="J1.unit", direction="→", path=(), env=(), redex=red, result=res, squares=(), rounds=())
t0 = J1.grade_steps([step0], node, {}, random.Random(1), R)
inst = P.Step(rule="J1.unit", direction="→", path=(F.ROUND,), env=(), redex=red, result=res, squares=(), rounds=((red, res, 0),))
t1 = J1.grade_steps([inst], node, {}, random.Random(1), R)
checks.append((f"the prover grades the seam step [(Jj)] → Jj `{t0.grade}` at depth 0 and `{t1.grade}` [{t1.receipts[0].where if t1.receipts else '—'}] directly inside an instance (paid by the instance, whose values agree)",
               t0.grade == "absent" and t1.grade == "absorbed" and bool(t1.receipts) and t1.receipts[0].where == "seam"))
report("H.seam-guard", checks)
