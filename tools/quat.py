"""quat.py — the ℍ reading at ∞: James forms valued in Hamilton's quaternions (rung `H`; SPEC §4.5, LEGISLATION 32).

The reading is the ℂ reading of tools/forms.py moved to ℍ:

  juxtaposition   addition in ℍ (the abelian group (ℍ, +) — breadth is commutative: JH-5)
  ( A )           exp A — entire on ℍ: exp(a + v) = e^a (cos|v| + (v/|v|) sin|v|)
  [ A ]           the principal log, L(q) = ln|q| + (v/|v|)·arccos(a/|q|), the angle in [0, π]; on the SEAM —
                  the negative reals, where every pure unit u gives e^{πu} = q/|q| — the direction is pinned to i:
                  L(−r) = ln r + π i (the J-pinning of JH-1(C): J = [<o>] reads π i, so that James's i = e^{J/2}
                  is Hamilton's i). The log of exactly one reads the period ω = 2π i (LEGISLATION 30b, in the slice
                  of i).
  < A >           −A
  [x ; y ; …]     the log of the ORDERED Hamilton product x·y·⋯ (the ordered square; rung H)
  Jj              the second seed J_j = π j (a constant); so j = (([Jj] <[oo]>)) = e^{πj/2} and k = ([i ; j]) = ij
  □               the black hole, as in ℂ

Receipts (tools/j1.py) are read in the lattice Λ_ℍ = {2πk·u : k ∈ ℤ, u a pure unit} — the kernel of exp — and a
receipt carries a DIRECTION: k(a, b) is the number of periods in a − b (signed by the direction's first nonzero
coordinate, so that the i-slice agrees with ℂ), and direction(a, b) the unit it winds about. The first
non-commutative wall: an instance pays a receipt in direction u only if the rest of its content commutes with u
(exp(X + 2πu) = exp X iff [X, u] = 0 — in-band rigidity, JH-1); the receipt prover checks the paying instance by
value (grade_steps, LEGISLATION 32(c)).

No dependencies beyond the standard library and forms.py.
"""
from __future__ import annotations
import math
import random

import forms as F

TOL = 1e-9


class Q:
    """A quaternion a + b i + c j + d k (floats). Immutable by convention."""
    __slots__ = ("a", "b", "c", "d")

    def __init__(self, a=0.0, b=0.0, c=0.0, d=0.0):
        self.a, self.b, self.c, self.d = float(a), float(b), float(c), float(d)

    # ---- construction
    @staticmethod
    def of(x) -> "Q":
        if isinstance(x, Q):
            return x
        if isinstance(x, complex):
            return Q(x.real, x.imag)     # ℂ embedded as the slice of i
        return Q(float(x))

    # ---- arithmetic
    def __add__(self, o): o = Q.of(o); return Q(self.a + o.a, self.b + o.b, self.c + o.c, self.d + o.d)
    __radd__ = __add__
    def __neg__(self): return Q(-self.a, -self.b, -self.c, -self.d)
    def __sub__(self, o): return self + (-Q.of(o))
    def __rsub__(self, o): return Q.of(o) + (-self)

    def __mul__(self, o):
        o = Q.of(o)
        a1, b1, c1, d1 = self.a, self.b, self.c, self.d
        a2, b2, c2, d2 = o.a, o.b, o.c, o.d
        return Q(a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
                 a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                 a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
                 a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2)

    def __rmul__(self, o): return Q.of(o) * self
    def scale(self, t: float): return Q(self.a * t, self.b * t, self.c * t, self.d * t)
    def conj(self): return Q(self.a, -self.b, -self.c, -self.d)
    def norm2(self): return self.a * self.a + self.b * self.b + self.c * self.c + self.d * self.d
    def __abs__(self): return math.sqrt(self.norm2())
    def imag(self): return Q(0.0, self.b, self.c, self.d)
    def imag_abs(self): return math.sqrt(self.b * self.b + self.c * self.c + self.d * self.d)
    def real(self): return self.a

    def inverse(self):
        n = self.norm2()
        if n == 0:
            raise ZeroDivisionError("the inverse of 0")
        return self.conj().scale(1.0 / n)

    def is_real(self, tol=TOL) -> bool:
        return self.imag_abs() <= tol * (1.0 + abs(self))

    def is_zero(self, tol=1e-300) -> bool:
        return abs(self) < tol

    def __eq__(self, o):
        if not isinstance(o, Q):
            return NotImplemented
        return close(self, o)

    def __hash__(self):
        return hash((round(self.a, 6), round(self.b, 6), round(self.c, 6), round(self.d, 6)))

    def __repr__(self):
        return fmt(self)

    def commutes(self, o: "Q", tol=1e-7) -> bool:
        """[self, o] = 0 — iff the pure parts are parallel (or one is void)."""
        c = self * o - o * self
        return abs(c) <= tol * (1.0 + abs(self) * abs(o))


ONE = Q(1.0)
I, Jq, K = Q(0, 1), Q(0, 0, 1), Q(0, 0, 0, 1)
PI = math.pi
OMEGA = Q(0.0, 2 * PI)        # the period, in the slice of i (LEGISLATION 30b at ℍ)
J_SEED = Q(0.0, PI)           # J = [<o>] pinned to π i (JH-1(C))
JJ_SEED = Q(0.0, 0.0, PI)     # the second seed J_j = π j (LEGISLATION 32(a))


def close(x: Q, y: Q, tol=TOL) -> bool:
    return abs(x - y) <= tol * (1.0 + max(abs(x), abs(y)))


def exp(q: Q) -> Q:
    """exp on ℍ: e^a (cos θ + u sin θ), θ = |Im q|, u = Im q / θ."""
    if q.a > 700:
        raise OverflowError("exp overflow")
    theta = q.imag_abs()
    ea = math.exp(q.a)
    if theta <= 1e-300:
        return Q(ea)
    s = ea * math.sin(theta) / theta
    return Q(ea * math.cos(theta), s * q.b, s * q.c, s * q.d)


def log(q: Q, enriched: bool = True) -> Q:
    """The principal log, with the seam pinned to i and (enriched) the log of exactly one read as ω = 2π i."""
    r = abs(q)
    if r < 1e-300:
        return F.BH
    theta = q.imag_abs()
    if theta <= 1e-9 * r:   # a real number up to rounding: snapped onto the axis
        if q.a > 0:
            if enriched and abs(q.a - 1.0) <= 1e-9:
                return OMEGA
            return Q(math.log(q.a))
        return Q(math.log(-q.a), PI)   # the seam: L(−r) = ln r + π i
    phi = math.atan2(theta, q.a)        # in (0, π)
    s = phi / theta
    return Q(math.log(r), s * q.b, s * q.c, s * q.d)


def fmt(q) -> str:
    if q is F.BH:
        return "□"
    if not isinstance(q, Q):
        return str(q)
    def f(x):
        if abs(x - round(x)) < 1e-9:
            return str(int(round(x)))
        return f"{x:.6g}"
    parts = []
    if abs(q.a) >= 1e-9 or q.imag_abs() < 1e-9:
        parts.append(f(q.a))
    for v, name in ((q.b, "i"), (q.c, "j"), (q.d, "k")):
        if abs(v) >= 1e-9:
            parts.append(("+" if v >= 0 and parts else ("-" if v < 0 else "")) + (("" if abs(abs(v) - 1) < 1e-9 else f(abs(v))) if v != 0 else "") + name)
    return "".join(parts) if parts else "0"


# ----------------------------------------------------------------------------- evaluation


def evaluate(form: F.Form, env: dict | None = None, enriched: bool = True):
    """Value of a form in ℍ ∪ {□}. A juxtaposition whose summands cancel to within rounding is snapped to 0."""
    env = env or {}
    total = Q()
    scale = 0.0
    for ch in form:
        v = _eval_child(ch, env, enriched)
        if v is F.BH:
            return F.BH
        total = total + v
        scale = max(scale, abs(v))
    if scale and abs(total) <= 1e-9 * scale:
        total = Q()
    return total


def _eval_child(ch, env, enriched: bool):
    if ch[0] == F.VAR:
        if ch[1] not in env:
            raise KeyError(f"unbound variable {ch[1]}")
        return Q.of(env[ch[1]])
    if ch[0] == F.CONST:
        if ch[1] == "Jj":
            return JJ_SEED
        raise F.Undefined(f"unknown constant {ch[1]}")
    if ch[0] == F.ORDERED:
        prod = ONE
        for e in ch[1]:
            v = evaluate(e, env, enriched)
            if v is F.BH:
                return F.BH
            prod = prod * v
        return log(prod, enriched)
    inner = evaluate(ch[1], env, enriched)
    if ch[0] == F.ROUND:
        if inner is F.BH:
            return Q()
        return exp(inner)
    if ch[0] == F.SQUARE:
        if inner is F.BH:
            raise F.Undefined("[□] has no value")
        return log(inner, enriched)
    if ch[0] == F.ANGLE:
        if inner is F.BH:
            raise F.Excluded("<□> is excluded")
        return -inner
    raise F.ParseError(ch)


def lattice_element(d: Q, tol=1e-6):
    """If d ∈ Λ_ℍ = {2πk·u}: (k, u) with k ≥ 0 and u the unit direction (None for k = 0); else None."""
    if abs(d) <= tol:
        return (0, None)
    if abs(d.a) > tol * (1.0 + abs(d)):
        return None
    theta = d.imag_abs()
    k = theta / (2 * PI)
    if abs(k - round(k)) > tol * (1.0 + k):
        return None
    k = int(round(k))
    if k == 0:
        return (0, None)
    u = d.imag().scale(1.0 / theta)
    return (k, u)


def signed_count(k: int, u) -> int:
    """A signed period count: the sign of the direction's first nonzero coordinate (i, then j, then k), so that in
    the slice of i the count agrees with the ℂ reading's (a − b = 2πi → +1, −2πi → −1)."""
    if k == 0 or u is None:
        return 0
    for v in (u.b, u.c, u.d):
        if abs(v) > 1e-9:
            return k if v > 0 else -k
    return k


def equal(v1, v2, equality: str = "≐", tol: float = TOL) -> bool:
    """≐ / ≡: exact (within tolerance). ≃ / ≈: equal modulo Λ_ℍ — the difference is a lattice element 2πk·u."""
    if v1 is F.BH or v2 is F.BH:
        return v1 is v2
    if close(v1, v2, tol):
        return True
    if equality in ("modΛ", "≃", "mod Λ", "≈"):
        return lattice_element(v1 - v2) is not None
    return False


# ----------------------------------------------------------------------------- sampling


def random_quaternion(rng: random.Random, lo=-2.0, hi=2.0) -> Q:
    return Q(*[math.exp(rng.uniform(lo, hi)) * rng.choice((-1, 1)) for _ in range(4)])


def random_pure_unit(rng: random.Random) -> Q:
    while True:
        v = Q(0, rng.gauss(0, 1), rng.gauss(0, 1), rng.gauss(0, 1))
        n = abs(v)
        if n > 1e-3:
            return v.scale(1.0 / n)


def random_env(names, domain: str, rng: random.Random) -> dict:
    """Values for the variables, by domain (SPEC §4.5): natural, positive, negative, real, unit — real numbers, as
    in ℂ (the centre of ℍ, where every law of the trunk holds as it holds in ℝ); complex — a generic quaternion, all
    four coordinates random (the JH analogue of 'any complex number'); slice — co-sliced quaternions: every
    variable in one random slice C_u = ℝ + ℝu (the Slice Principle's domain, where the classical calculus holds
    verbatim with J → J_u); plane — complex numbers, the slice of the pinned J (internal: the ledger grades the
    trunk's derivations there, tools/hledger.py)."""
    env = {}
    names = sorted(names)
    if domain == "plane":
        # the slice of the pinned J, ℂ ⊂ ℍ: where the trunk's derivations are read in ℍ (tools/hledger.py, on_slice)
        for n in names:
            x = math.exp(rng.uniform(-2, 2)) * rng.choice((-1, 1))
            y = math.exp(rng.uniform(-2, 2)) * rng.choice((-1, 1))
            env[n] = Q(x, y)
        return env
    if domain == "slice":
        u = random_pure_unit(rng)
        for n in names:
            x = math.exp(rng.uniform(-2, 2)) * rng.choice((-1, 1))
            y = math.exp(rng.uniform(-2, 2)) * rng.choice((-1, 1))
            env[n] = Q(x) + u.scale(y)
        return env
    for n in names:
        if domain == "natural":
            env[n] = Q(rng.randint(1, 8))
        elif domain == "positive":
            env[n] = Q(math.exp(rng.uniform(math.log(0.05), math.log(20.0))))
        elif domain in ("real", "unit"):
            env[n] = Q(math.exp(rng.uniform(math.log(0.05), math.log(20.0))) * rng.choice((-1, 1)))
        elif domain == "negative":
            env[n] = Q(-math.exp(rng.uniform(math.log(0.05), math.log(20.0))))
        elif domain == "complex":
            env[n] = random_quaternion(rng)
        else:
            raise ValueError(f"unknown domain {domain}")
    return env


PROBES = {"natural": [Q(1), Q(2)], "positive": [Q(1), Q(0.5), Q(2)], "negative": [Q(-1), Q(-2)],
          "real": [Q(1), Q(-1), Q(0.5), Q(2)], "unit": [Q(1), Q(-1), Q(0.5), Q(2)],
          "complex": [Q(1), Q(-1), Q(0.5), Q(2), I, Jq, K, -I, -Jq, -K, Q(1, 1), Q(0, 1, 1), Q(1, 1, 1, 1)],
          "slice": [Q(1), Q(-1), Q(0.5), Q(2), I, Jq, K],
          "plane": [Q(1), Q(-1), Q(0.5), Q(2), I, -I, Q(1, 1)]}
GENERIC = Q(2.0)


def probes(names, domain: str, rng: random.Random):
    """The exceptional points of the reading: every variable at each probe value — exactly one (where the log reads
    ω), minus one (the seam), the units i, j, k (where a content of the form J_u sits) — the others at a generic
    value, then random; and all variables at the same probe."""
    names = sorted(names)
    if not names:
        return []
    out = []
    for p in PROBES.get(domain, PROBES["complex"]):
        out.append({n: p for n in names})
        for n in names:
            fixed = {m: GENERIC for m in names}
            fixed[n] = p
            out.append(fixed)
            env = random_env(names, domain, rng)
            env[n] = p
            out.append(env)
    return out


# ----------------------------------------------------------------------------- the Reading for the receipt prover


class Reading:
    """The ℍ reading as tools/j1.py sees it: the same hooks as CReading and place.Reading, plus `noncommutative`,
    which makes the prover check every absorbed step by value (the first non-commutative wall)."""
    name = "H"
    period_name = "ω"
    noncommutative = True
    skip_errors = (F.Undefined, F.Excluded, OverflowError, ZeroDivisionError)

    def evaluate(self, form, env):
        return evaluate(form, env)

    def random_env(self, names, domain, rng):
        return random_env(names, domain, rng)

    def probes(self, names, domain, rng):
        return probes(names, domain, rng)

    def is_pole(self, v):
        return v is F.BH

    def k(self, a, b):
        """a − b in units of ω when it is a lattice element (in any direction), else None."""
        le = lattice_element(a - b)
        if le is None:
            return None
        return signed_count(*le)

    def direction(self, a, b):
        le = lattice_element(a - b)
        if le is None or le[1] is None:
            return None
        return le[1]

    def equal(self, a, b, equality="≐"):
        return equal(a, b, equality)

    def seam(self, a, b, tol: float = 1e-6) -> bool:
        """A seam displacement: the two values are not equal mod Λ_ℍ, but their instances agree — e^{πu} = e^{πi}
        with πu − πi no lattice element. Measure zero at ∞ (the negative reals); positive measure at a finite place."""
        if a is F.BH or b is F.BH:
            return False
        if equal(a, b, "≃"):
            return False
        try:
            return close(exp(a), exp(b), tol * (1.0 + abs(exp(a))))
        except (OverflowError, ValueError):
            return False

    def fmt(self, v):
        return fmt(v)

    def premise(self, name: str, env: dict, domain: str, rng, trials: int = 12) -> bool:
        """The premise of a conditional rule on a matched substitution (name -> Form), at the generic points of the
        domain: `commute` — the VALUES bound to P and Q commute (H.commutation, `[P ; Q] ≐ [Q ; P]`: PQ = QP makes the
        two logs one); `cosliced` — the LOGS of P and Q commute (H.collapse, `[P ; Q] ≃ [P] [Q]`: log P + log Q is a
        log of PQ only when the two logs lie in one slice — and the pinned log of a negative real lies in the slice
        of i, so −1 and j do not satisfy it though they commute)."""
        if name not in ("commute", "cosliced"):
            return True
        fp, fq = env.get("P", ()), env.get("Q", ())
        names = F.variables(fp) | F.variables(fq)
        judged = 0
        for _ in range(trials if names else 1):
            e = random_env(names, domain, rng)
            try:
                a, b = evaluate(fp, e), evaluate(fq, e)
            except self.skip_errors:
                continue
            if a is F.BH or b is F.BH:
                continue
            if name == "cosliced":
                a, b = log(a), log(b)
                if a is F.BH or b is F.BH:
                    continue
            if not a.commutes(b):
                return False
            judged += 1
        return judged > 0   # a premise no sample could test is not established


if __name__ == "__main__":
    e = lambda s, env=None: evaluate(F.parse(s), env or {})  # noqa: E731
    for s in ["J", "Jj", "(J)", "(Jj)", "i", "j", "k", "([i ; j])", "([j ; i])", "<([j ; i])>", "([k ; k])", "([i ; i])",
              "([j ; j])", "([i][j])", "[i ; j]", "[i][j]", "(J J)", "[o]", "[(Jj)]", "([k ; i])", "([j ; k])", "([i ; j ; k])"]:
        try:
            print(f"{s:14} = {fmt(e(s))}")
        except Exception as ex:
            print(f"{s:14} : {type(ex).__name__}: {ex}")
    rng = random.Random(1)
    A, B = random_quaternion(rng), random_quaternion(rng)
    print("exp(logA+logB) == AB ?", close(exp(log(A) + log(B)), A * B), "| log(AB) == logA+logB mod Λ ?", equal(log(A * B), log(A) + log(B), "≃"))
    print("exp(log A) == A ?", close(exp(log(A)), A), "| L(exp(πj)) =", fmt(log(exp(Q(0, 0, PI)))))
