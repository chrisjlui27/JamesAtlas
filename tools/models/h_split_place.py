"""Witness for H.split-place — the quaternions at an odd prime, where ℍ ⊗ ℚ_p ≅ M₂(ℚ_p). At p = 3, 5, 7, 13, in the
quaternion reading at the place (tools/quatplace.py): (1) Hamilton's relations hold on the page; (2) the norm is
isotropic — a nonzero quaternion of the page with norm ≡ 0 mod p exists, is a zero divisor, has no reciprocal, and
has no log (the norm-null species, JH-20); (3) the split: a² + b² ≡ −1 mod pⁿ is solvable, so i ↦ [[0,1],[−1,0]],
j ↦ [[a,b],[b,−a]] is a ring map onto 2×2 matrices satisfying Hamilton's relations; (4) Fermat–Euler
U^{φ(pⁿ)} ≡ 1 fails for the unit U = i when p ≡ 3 mod 4 (i has order 4), so the page's Fermat law holds on the
centre only; (5) the trunk's `([A][B])` is formless or false for non-commuting A, B — the no-go at the place —
while `([A ; B])` is the product. Exits 0 iff all hold."""
from h_common import *  # noqa: F401,F403
import quatplace as QP
from fractions import Fraction as Fr

checks = []
for p in (3, 5, 7, 13):
    P = QP.HPlace(p)
    e = lambda s, env=None: QP.evaluate(F.parse(s), env or {}, P)  # noqa: E731
    ham = all(P.equal(e(a), e(b)) for a, b in [("([i ; j])", "k"), ("([j ; k])", "i"), ("([k ; i])", "j"), ("([i ; i])", "<o>"), ("([j ; j])", "<o>"),
                                                 ("([k ; k])", "<o>"), ("([j ; i])", "<k>"), ("([i ; j ; k])", "<o>")])
    checks.append((f"p = {p}: Hamilton's relations hold on the page", ham))
    # a zero divisor: find a, b with a² + b² ≡ −1 mod p; then z = 1 + a i + b j has norm 1 + a² + b² ≡ 0
    sol = next(((a, b) for a in range(p) for b in range(p) if (a * a + b * b + 1) % p == 0), None)
    z = QP.HQ(1, sol[0], sol[1], 0)
    zero_div = z.norm() % p == 0 and not all(x % p == 0 for x in z.coords())
    no_log = False
    try:
        P.log(P.number(z))
    except QP.NotAForm:
        no_log = True
    w = z.conj()
    prod = P.reduce(z * w)
    checks.append((f"p = {p}: 1 + {sol[0]}i + {sol[1]}j has norm ≡ 0 — a zero divisor (z·z̄ ≡ 0 mod p), with no log and no reciprocal", zero_div and no_log and all(x % p == 0 for x in prod.coords())))
    # the split: matrices
    a, b = sol
    import itertools
    def mat(q):
        w_, x, y, zz = [int(c) for c in q.coords()]
        # q = w + x i + y j + z k ↦ w I + x Mi + y Mj + z Mi Mj
        Mi = ((0, 1), (-1, 0)); Mj = ((a, b), (b, -a))
        def mm(A, B):
            return tuple(tuple(sum(A[r][t] * B[t][c] for t in range(2)) % p for c in range(2)) for r in range(2))
        def ad(A, B):
            return tuple(tuple((A[r][c] + B[r][c]) % p for c in range(2)) for r in range(2))
        def sc(s, A):
            return tuple(tuple((s * A[r][c]) % p for c in range(2)) for r in range(2))
        Mk = mm(Mi, Mj)
        return ad(ad(sc(w_, ((1, 0), (0, 1))), sc(x, Mi)), ad(sc(y, Mj), sc(zz, Mk)))
    def mm(A, B):
        return tuple(tuple(sum(A[r][t] * B[t][c] for t in range(2)) % p for c in range(2)) for r in range(2))
    ok_hom = True
    for _ in range(30):
        q1 = QP.HQ(*[RNG.randint(0, p - 1) for _ in range(4)]); q2 = QP.HQ(*[RNG.randint(0, p - 1) for _ in range(4)])
        ok_hom = ok_hom and mat(q1 * q2) == mm(mat(q1), mat(q2))
    checks.append((f"p = {p}: a² + b² ≡ −1 at (a, b) = {sol}; q ↦ matrices is a ring map mod p (the split, on 30 products)", ok_hom))
    phi = (p - 1)
    i_pow = QP.ONE
    for _ in range(phi):
        i_pow = i_pow * QP.I
    fermat_i = i_pow == QP.ONE
    checks.append((f"p = {p}: Fermat for the unit i, i^{{p−1}} = 1: {'holds' if fermat_i else 'FAILS'} (p ≡ {p % 4} mod 4)", fermat_i == (p % 4 == 1)))
    # the no-go at the place: ([A][B]) vs ([A ; B]) on units of the page with logs
    formless = false = equal = 0
    rng = random.Random(p)
    for _ in range(30):
        env = P.random_env({"A", "B"}, "complex", rng)
        try:
            v1 = e("([A][B])", env)
            v2 = e("([A ; B])", env)
        except QP.NotAForm:
            formless += 1
            continue
        if P.equal(v1, v2):
            equal += 1
        else:
            false += 1
    checks.append((f"p = {p}: ([A][B]) against the product ([A ; B]) on generic units: {formless} formless (non-commuting logs), {false} false, {equal} equal", false + formless >= 25))
report("H.split-place", checks)
