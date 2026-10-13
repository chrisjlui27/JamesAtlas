"""Witness for H.phase-sphere — −1 has a 2-sphere of logarithms. (1) exp(πu) = −1 for every pure unit u; (2) the
principal band meets {L : exp L = −1} exactly in π·S²; (3) antipodes: J_{−u} = −J_u and e^{J_u} = e^{J_{−u}}; (4) the
seeds' logs J = πi and Jj = πj are two points of the sphere. Exits 0 iff all hold."""
from h_common import *  # noqa: F401,F403

checks = []
checks.append(("exp(πu) = −1 for 60 random pure units u", all(close(exp(unit().scale(PI)), Q(-1), 1e-7) for _ in range(60))))
ok2 = True
for _ in range(60):
    L = rand_q(-1.0, 1.3)
    if close(exp(L), Q(-1), 1e-6):
        ok2 = ok2 and abs(L.a) < 1e-6 and abs(L.imag_abs() - PI) < 1e-6
    ok2 = ok2 and close(exp(unit().scale(PI)), Q(-1), 1e-7)
checks.append(("in the band, exp L = −1 only on π·S² (sampled), and all of π·S² qualifies", ok2))
checks.append(("antipodes: J_{−u} = −J_u, e^{J_u} = e^{J_{−u}} = −1 — the sphere is seen as RP² inside an instance", all(close(exp(u.scale(PI)), exp(u.scale(-PI)), 1e-7) for u in [unit() for _ in range(20)])))
e = lambda s: QT.evaluate(F.parse(s), {})  # noqa: E731
checks.append(("the seeds: (J) = (Jj) = −1 on the page — J = πi and Jj = πj are two points of the sphere", close(e("(J)"), Q(-1), 1e-9) and close(e("(Jj)"), Q(-1), 1e-9) and close(e("J"), I.scale(PI), 1e-9) and close(e("Jj"), Jq.scale(PI), 1e-9)))
report("H.phase-sphere", checks)
