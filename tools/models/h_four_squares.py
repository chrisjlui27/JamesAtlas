"""Witness for H.four-squares — N(pq) = N(p) N(q) (Euler 1748), exactly, over rational quaternions; the two-sided
norm q q̄ = q̄ q = N(q); and the conjugate as an anti-automorphism, conj(pq) = conj(q) conj(p) (the link of the chain
whose page derivation is owed). Exits 0 iff all hold."""
from h_common import *  # noqa: F401,F403
from fractions import Fraction as Fr
import quatplace as QP

checks = []
ok = True
for _ in range(100):
    p = QP.HQ(*[Fr(RNG.randint(-30, 30), RNG.randint(1, 7)) for _ in range(4)])
    q = QP.HQ(*[Fr(RNG.randint(-30, 30), RNG.randint(1, 7)) for _ in range(4)])
    ok = ok and (p * q).norm() == p.norm() * q.norm() and (q * p).norm() == p.norm() * q.norm()
    ok = ok and (p * p.conj()) == QP.HQ(p.norm()) and (p.conj() * p) == QP.HQ(p.norm())
checks.append(("N(pq) = N(p)N(q) = N(qp) and q q̄ = q̄ q = N(q), exactly, on 100 rational samples", ok))
anti = True
for _ in range(100):
    p = QP.HQ(*[Fr(RNG.randint(-30, 30), RNG.randint(1, 7)) for _ in range(4)])
    q = QP.HQ(*[Fr(RNG.randint(-30, 30), RNG.randint(1, 7)) for _ in range(4)])
    anti = anti and (p * q).conj() == q.conj() * p.conj()
    anti = anti and (((p * q).conj() == p.conj() * q.conj()) == (p * q == q * p))  # the unreversed order only when they commute
checks.append(("conj(pq) = conj(q) conj(p) on 100 rational samples — and not conj(p) conj(q) unless p, q commute", anti))
a = (1, 2, 3, 4); b = (5, 6, 7, 8)
pa, pb = QP.HQ(*a), QP.HQ(*b)
checks.append(("Euler's identity at (1,2,3,4)·(5,6,7,8): 30·174 = 5220", (pa * pb).norm() == 5220))
report("H.four-squares", checks)
