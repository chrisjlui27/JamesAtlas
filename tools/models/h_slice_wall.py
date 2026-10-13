"""Witness for H.slice-wall — the first non-commutative wall. (1) (ω A) = (A) for A in the slice of i (ω = 2πi);
(2) it fails for generic A; (3) in general (2πu + A) = (A) iff [A, u] = 0; (4) the J1 rung's absorption, re-graded
by the receipt prover in ℍ: absorbed on co-sliced contents, absent (cross-slice) on generic ones. Exits 0 iff all
hold."""
from h_common import *  # noqa: F401,F403
import j1 as J1, prover as P, licences as LC, nodes as N  # noqa: E402

checks = []
om = QT.OMEGA
ok1 = all(close(exp(om + a), exp(a), 1e-7) for a in [Q(RNG.uniform(-1, 1), RNG.uniform(-3, 3)) for _ in range(40)])
checks.append(("(ω A) = (A) for A in the slice of i", ok1))
bad = sum(1 for _ in range(40) if not close(exp(om + rand_q()), exp(rand_q() * 0 + rand_q()), 1e-7))
fails = 0
for _ in range(40):
    A = rand_q()
    if not close(exp(om + A), exp(A), 1e-7):
        fails += 1
checks.append((f"(ω A) ≠ (A) for generic A ({fails}/40 samples fail)", fails >= 36))
ok3 = True
for _ in range(60):
    u = unit()
    A = rand_q()
    lhs = close(exp(u.scale(2 * PI) + A), exp(A), 1e-6)
    rhs = A.commutes(u, 1e-6)
    if lhs != rhs:
        ok3 = False
    B = Q(RNG.uniform(-2, 2)) + u.scale(RNG.uniform(-2, 2))
    if not close(exp(u.scale(2 * PI) + B), exp(B), 1e-6):
        ok3 = False
checks.append(("(2πu + A) = (A) iff [A, u] = 0; always for A in the slice of u", ok3))
# (4) the prover: J1.absorption's own derivation graded in ℍ on the two domains
nodes = N.load_nodes(os.path.join(os.path.dirname(os.path.dirname(HERE)), "nodes"))
node = nodes["J1.absorption"]
class ISlice(QT.Reading):
    """The ℍ reading sampling the slice of i for the domain `slice` — the slice of the receipt ω = 2πi."""
    def random_env(self, names, domain, rng):
        if domain != "slice":
            return QT.random_env(names, domain, rng)
        return {n: Q(math.exp(rng.uniform(-2, 2)) * rng.choice((-1, 1)), math.exp(rng.uniform(-2, 2)) * rng.choice((-1, 1))) for n in sorted(names)}
R = QT.Reading()
lic, unl, skip, det = LC.check_node(node, nodes, {})
def grade_on(domain, reading):
    meta = dict(node.meta); meta["domain"] = domain
    n2 = N.Node(id=node.id, path=node.path, meta=meta, sections=node.sections, body=node.body)
    tape = J1.Tape()
    for ti, i, status, msg, steps in det:
        if status == "ok":
            tape.merge(J1.grade_steps(steps, n2, {}, random.Random(5), reading))
    return tape
t_generic, t_slice, t_other = grade_on("complex", R), grade_on("slice", ISlice()), grade_on("slice", R)
checks.append((f"J1.absorption graded in ℍ: generic quaternions → {t_generic.grade} ({J1.describe(t_generic, R)[:80]}…)", t_generic.grade == "absent"))
checks.append((f"J1.absorption graded in ℍ: contents in the slice of i (the receipt's direction) → {t_slice.grade}", t_slice.grade == "absorbed"))
checks.append((f"J1.absorption graded in ℍ: contents co-sliced in a random other slice → {t_other.grade} (the receipt winds about i, the content about u)", t_other.grade == "absent"))
report("H.slice-wall", checks)
