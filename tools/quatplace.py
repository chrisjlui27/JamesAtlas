"""quatplace.py — the quaternions at a finite place: the ℍ reading of tools/quat.py moved to a prime (rung `H`, read
against the places; SPEC §6.4, LEGISLATION 32(e)).

The page at p is the quaternion order over ℤ/pⁿ: Hamilton's quaternions with coordinates mod pⁿ at an odd p —
where ℍ ⊗ ℚ_p SPLITS, ℍ_p ≅ M₂(ℚ_p), the norm is isotropic and there are zero divisors — and the Hurwitz order O
(coordinates all integral or all half-integral) at p = 2, where ℍ ⊗ ℚ₂ is a division algebra RAMIFIED over ℚ₂:
the valuation takes half-integer values, v(q) = v₂(N(q))/2, the uniformizer is π = 1 + i with v(π) = ½, the page to
depth n is O/πⁿO (q ≡ q' iff v₂(N(q − q')) ≥ n), and the residue field O/πO is 𝔽₄.

A value is read as at a commutative place (tools/place.py): a NUMBER PART — a quaternion in the radius of the
instance (v ≥ 1 at odd p, v ≥ 3/2 at 2: where exp converges, as a quaternion power series) —, a COUNT of the log
of the prime (whole at odd p; at 2 a count of [π], with [2] = 2[π]), and a TORSION PART: formal logs of the torsion
the reading knows, each a (direction, count) pair as at ∞ — the central Teichmüller log J_p of the page's own
torsion (odd p; count in units of J_p), and the directional logs of the Hurwitz units: ±i, ±j, ±k (direction an
axis, count a half-integer), the sixteen (±1 ± i ± j ± k)/2 (direction (±1, ±1, ±1), count ±1/3 or ±2/3) — so the
24 units of 2T and their central multiples are exactly the torsion elements with a log here. The log of a
negative principal unit is pinned to the direction i (as L(−r) = ln r + πi at ∞), the log of exactly one reads the
page's own period (the central (p−1)·J_p at odd p; 2·J_i at 2) — the same wall at every place — and every other log
is principal: counts in (−1, 1]. Two torsion logs juxtapose only when they commute (one direction, or central): the
sum of two non-commuting logs has no value — the no-go, at a finite place. The instance of a value is
p^v · τ^k · t(direction, count) · exp(number part) (π^m at 2); the square of a number finds that decomposition —
strip the prime, find the torsion factor among the ones the reading knows, take the log of the principal rest —
or refuses (a unit whose torsion the reading does not know is not a form here: owed).

Equality is mod the page (coordinates mod pⁿ; v₂ of the norm of the difference ≥ n at 2) on the number part, exact
on the counts (≃: mod the lattice Λ_p = the kernel of the instance on the torsion part, commuting components
only). Receipts count the periods in a difference: central Δk/(p−1) plus directional Δc/2.

No dependencies beyond the standard library, forms.py and place.py (for the central torsion tables).
"""
from __future__ import annotations
import math
import random
from dataclasses import dataclass, field
from fractions import Fraction as Fr

import forms as F
import place as PL

PLACES = (2, 3, 5, 7, 13)


class NotAForm(PL.NotAForm):
    """A form with no value at this place in the ℍ reading."""


# ----------------------------------------------------------------------------- exact quaternions

class HQ:
    """A quaternion with exact rational coordinates."""
    __slots__ = ("a", "b", "c", "d")

    def __init__(self, a=0, b=0, c=0, d=0):
        self.a, self.b, self.c, self.d = Fr(a), Fr(b), Fr(c), Fr(d)

    def coords(self):
        return (self.a, self.b, self.c, self.d)

    def __add__(self, o): return HQ(self.a + o.a, self.b + o.b, self.c + o.c, self.d + o.d)
    def __sub__(self, o): return HQ(self.a - o.a, self.b - o.b, self.c - o.c, self.d - o.d)
    def __neg__(self): return HQ(-self.a, -self.b, -self.c, -self.d)

    def __mul__(self, o):
        if not isinstance(o, HQ):
            o = HQ(o)
        a1, b1, c1, d1 = self.coords()
        a2, b2, c2, d2 = o.coords()
        return HQ(a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
                  a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                  a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
                  a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2)

    def scale(self, t): t = Fr(t); return HQ(self.a * t, self.b * t, self.c * t, self.d * t)
    def conj(self): return HQ(self.a, -self.b, -self.c, -self.d)
    def norm(self): return self.a * self.a + self.b * self.b + self.c * self.c + self.d * self.d
    def is_zero(self): return not (self.a or self.b or self.c or self.d)
    def is_central(self): return not (self.b or self.c or self.d)
    def pure(self): return (self.b, self.c, self.d)

    def inverse(self):
        n = self.norm()
        if n == 0:
            raise ZeroDivisionError("a quaternion of norm zero has no inverse")
        return self.conj().scale(1 / n)

    def __eq__(self, o):
        return isinstance(o, HQ) and self.coords() == o.coords()

    def __hash__(self):
        return hash(self.coords())

    def __repr__(self):
        return fmt_q(self)

    def commutes(self, o: "HQ") -> bool:
        return (self * o - o * self).is_zero()


ONE, I, J, K = HQ(1), HQ(0, 1), HQ(0, 0, 1), HQ(0, 0, 0, 1)


def fmt_q(q: HQ, modulus=None) -> str:
    parts = []
    coords = q.coords()
    if modulus:
        coords = tuple(v - modulus if (v.denominator == 1 and v > modulus // 2) or (v.denominator == 2 and v > modulus // 2) else v for v in coords)
    for v, name in zip(coords, ("", "i", "j", "k")):
        if v == 0:
            continue
        s = str(v) if name == "" or abs(v) != 1 else ("" if v > 0 else "-")
        if parts and not s.startswith("-"):
            s = "+" + s
        parts.append(s + name)
    return "".join(parts) if parts else "0"


def vp(x: Fr, p: int, cap: int = 10 ** 6) -> int:
    """The p-adic valuation of a rational (cap for 0)."""
    if x == 0:
        return cap
    n, d = x.numerator, x.denominator
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v


# ----------------------------------------------------------------------------- the Hurwitz units and their logs

def hurwitz_units():
    """The 24 units of the Hurwitz order: ±1, ±i, ±j, ±k and (±1 ± i ± j ± k)/2 — the binary tetrahedral group 2T."""
    out = []
    for s in (1, -1):
        for u in (ONE, I, J, K):
            out.append(u.scale(s))
    for a in (1, -1):
        for b in (1, -1):
            for c in (1, -1):
                for d in (1, -1):
                    out.append(HQ(Fr(a, 2), Fr(b, 2), Fr(c, 2), Fr(d, 2)))
    return out


UNITS = hurwitz_units()


def torsion_log(t: HQ):
    """The (direction, count) of a Hurwitz unit t = exp(count·π·direction/|direction|), count in the principal band
    (−1, 1]: 1 → None; −1 → ((0, 1, 0, 0) pinned to i, 1); ±i, ±j, ±k → (axis, ±½); (±1 ± i ± j ± k)/2 →
    (the pure part's signs, 1/3 or 2/3). The direction is an integer vector (b, c, d) with gcd 1."""
    if t == ONE:
        return None
    if t == -ONE:
        return ((1, 0, 0), Fr(1))
    b, c, d = t.pure()
    if t.a == 0:
        # an axis: the direction is the axis with the sign of the coordinate, the count ½ (angle π/2); keep the
        # count positive and let the direction carry the sign, as at ∞
        return (tuple(int(x) for x in (b, c, d)), Fr(1, 2))
    # (±1 ± i ± j ± k)/2: cos θ = a = ±½ → θ = π/3 (a = ½) or 2π/3 (a = −½); direction the signs of the pure part
    return (tuple(int(2 * x) for x in (b, c, d)), Fr(1, 3) if t.a > 0 else Fr(2, 3))


TORSION_LOG = {t: torsion_log(t) for t in UNITS}


def torsion_element(direction, count: Fr):
    """exp(count·π·u) for u the unit direction, as a Hurwitz unit when it is one: the unit whose torsion_log has
    this direction, raised to the power count / base count; None when no such unit exists."""
    if count == 0:
        return ONE
    base = None
    for t, dc in TORSION_LOG.items():
        if dc is not None and dc[0] == tuple(direction) and dc[1] > 0 and (base is None or dc[1] < base[1]):
            base = (t, dc[1])
    if base is None:
        return None
    t, c0 = base
    m = count / c0
    if m.denominator != 1:
        return None
    m = m.numerator
    out = ONE
    if m < 0:
        t = t.inverse()
        m = -m
    for _ in range(m):
        out = out * t
    return out


def reduce_log(direction, count: Fr):
    """A torsion count brought into the principal band (−1, 1] in its direction (the instance is unchanged: the
    period in a direction is 2); the pinned direction of −1 keeps count 1."""
    c = count
    while c > 1:
        c -= 2
    while c <= -1:
        c += 2
    return c


# ----------------------------------------------------------------------------- values at the place

CENTRAL = ("c",)     # the key of the central torsion log J_p in a torsion part (a tuple, like a direction)
# A torsion part is a dict {key: count}: CENTRAL for J_p (the Teichmüller scalar's log); a direction (b, c, d) for
# the log of a Hurwitz unit, counts in ℚ as at ∞; and a CARRIER ("e", coords) for the formal log of any other unit
# of finite order prime to p — its Teichmüller lift, found by iterating the p^N-th power (p^N ≡ 1 mod the order) —
# with whole counts only: the reading knows the element and not its fractions.


@dataclass(frozen=True)
class HV:
    """A value at the place: the number part (a quaternion in the radius), the count of the prime's log (of [π] at 2),
    the torsion part {direction: count} (direction CENTRAL for J_p), and the exact quaternion this is when it is a
    plain number. `pole` marks the black hole. A FORMAL LOG — the square of a value with counts, `[J]`, `[Jj]` — is
    the second grade (as in tools/place.py): a symbol ℓ(base) with a coefficient, which the instance reads as the
    base scaled by the count the rest of the value is the log of (`([[A]] [B])` is B·[A])."""
    n: HQ = field(default_factory=HQ)
    v: Fr = Fr(0)
    tor: tuple = ()          # sorted ((direction, count), …)
    pole: bool = False
    exact: HQ | None = None  # a plain number known exactly (no counts): the quaternion itself
    logof: Fr | None = None  # a central value known to be the log of this exact rational (so a count can be recovered)
    lcoef: Fr = Fr(0)        # the second grade: coefficient of the formal log of `base`
    base: "HV | None" = None

    @property
    def number(self) -> bool:
        return not self.pole and self.v == 0 and not self.tor and self.exact is not None and self.lcoef == 0

    @property
    def formal(self) -> bool:
        return self.v != 0 or bool(self.tor)

    @property
    def grade(self) -> int:
        return 1 if self.lcoef else 0

    def torsion(self) -> dict:
        return dict(self.tor)


def _signed(d: dict) -> dict:
    """A torsion part with antipodal directions identified: (−u, c) is (u, −c) — the count carries the sign, the
    direction's first nonzero coordinate is positive (the convention of tools/quat.py, `signed_count`). Carriers and
    the central key are left as they are."""
    out: dict = {}
    for k, c in d.items():
        if c == 0:
            continue
        if k == CENTRAL or k[0] == "e":
            out[k] = out.get(k, Fr(0)) + c
            continue
        first = next((x for x in k if x != 0), 0)
        if first < 0:
            k, c = tuple(-x for x in k), -c
        out[k] = out.get(k, Fr(0)) + c
    return {k: c for k, c in out.items() if c != 0}


def _tor(d: dict) -> tuple:
    return tuple(sorted(((k, c) for k, c in d.items() if c != 0), key=lambda kc: (len(kc[0]), kc[0])))


class HPlace:
    """Hamilton's quaternions at the prime p, to depth n (shells of p at odd p; half-shells — powers of π — at 2)."""

    def __init__(self, p: int, depth: int | None = None):
        if p not in PL.PRIMITIVE_ROOT:
            raise ValueError(f"no primitive root tabled for {p}")
        self.p = p
        self.center = PL.Place(p, depth=depth)            # the page's own numbers: the central torsion and its tables
        if p == 2:
            self.depth = depth or 2 * PL.default_depth(2)  # in half-shells: π^depth
            self.N = self.depth + 2 * PL.default_depth(2)  # working precision, in half-shells
        else:
            self.depth = depth or PL.default_depth(p)
            self.N = self.depth + PL.default_depth(p)
        self.radius = Fr(3, 2) if p == 2 else Fr(1)        # exp converges for v(x) ≥ radius

    # ---- valuations and the page
    def val(self, q: HQ) -> Fr:
        """v(q): at odd p the least coordinate valuation (the order is M₂(ℤ_p): q ∈ pⁿ·O iff every coordinate is);
        at 2, v₂(N(q))/2 for q in the Hurwitz order (q ∈ πⁿO iff v₂(N(q)) ≥ n)."""
        if q.is_zero():
            return Fr(10 ** 6)
        if self.p == 2:
            # the valuation of the division algebra ℍ ⊗ ℚ₂, defined on every nonzero element (the order is its
            # valuation ring, v ≥ 0): the terms of the log series leave the order and still have a valuation
            return Fr(vp(q.norm(), 2), 2)
        return Fr(min(vp(x, self.p) for x in q.coords()))

    def in_order(self, q: HQ) -> bool:
        if self.p == 2:
            cs = q.coords()
            if all(x.denominator == 1 for x in cs):
                return True
            return all(x.denominator == 2 and x.numerator % 2 == 1 for x in cs)
        return all(x.denominator % self.p for x in q.coords())

    def congruent(self, q: HQ, r: HQ, shells: Fr | int) -> bool:
        """q ≡ r on the page to `shells` (p-shells at odd p, half-shells at 2)."""
        d = q - r
        if d.is_zero():
            return True
        if self.p == 2:
            return self.val(d) * 2 >= shells
        return self.val(d) >= shells

    def reduce(self, q: HQ) -> HQ:
        """The quaternion reduced to the working precision (its coordinates as p-adic integers mod p^N; at 2 the
        doubled coordinates mod 2^{N+1}), to keep exact arithmetic small."""
        if self.p == 2:
            M = 2 ** (self.N // 2 + 2)
            out = []
            for x in q.coords():
                y = x * 2
                if y.denominator % 2 == 0:
                    raise NotAForm("not in the Hurwitz order")
                # an odd denominator is a 2-adic unit (the log series divides by n): invert it mod 2M
                out.append(Fr(y.numerator * pow(y.denominator, -1, 2 * M) % (2 * M), 2))
            return HQ(*out)
        M = self.p ** self.N
        out = []
        for x in q.coords():
            if x.denominator % self.p == 0:
                raise NotAForm("the reciprocal of the prime is not a form at its own place")
            out.append(Fr(x.numerator * pow(x.denominator, -1, M) % M))
        return HQ(*out)

    # ---- the series
    def exp(self, x: HQ) -> HQ:
        """exp x = Σ xⁿ/n!, for v(x) ≥ radius (terms shrink: v(xⁿ/n!) ≥ n·radius − v_p(n!) → ∞), to the precision."""
        if self.val(x) < self.radius:
            raise PL.OutsideRadius("outside the radius of the instance at p")
        total, term = ONE, ONE
        for n in range(1, 400):
            term = (term * x).scale(Fr(1, n))
            total = total + term
            if self._val_safe(term) > self.N + 2:
                break
        return self.reduce(total)

    def log1(self, u: HQ) -> HQ:
        """log u = Σ (−1)^{n+1} yⁿ/n with y = u − 1, for v(y) ≥ radius, to the precision."""
        y = u - ONE
        if y.is_zero():
            return HQ()
        if self.val(y) < self.radius:
            raise NotAForm("not a principal unit: the log series does not converge")
        total, power = HQ(), ONE
        for n in range(1, 400):
            power = power * y
            term = power.scale(Fr((-1) ** (n + 1), n))
            total = total + term
            if self._val_safe(term) > self.N + 2:
                break
        return self.reduce(total)

    def _val_safe(self, q: HQ) -> Fr:
        return Fr(10 ** 6) if q.is_zero() else (self.val(q) * (2 if self.p == 2 else 1))

    # ---- the torsion the reading knows
    def torsion_candidates(self):
        """(torsion dict, element) for every torsion element the reading knows: the central Teichmüller powers τ^k
        (odd p) times the Hurwitz units; the identity first, the central ones next, so that a number's log takes
        the central reading where it can (the page's own torsion) and a Hurwitz direction only when it must."""
        if hasattr(self, "_cands"):
            return self._cands
        out = []
        if self.p == 2:
            ks = [0]
        else:
            ks = list(range(self.p - 1))
        hurwitz = sorted(UNITS, key=lambda t: (t != ONE, t != -ONE, TORSION_LOG[t] is None or TORSION_LOG[t][1]))
        for t in hurwitz:
            for k in ks:
                tor = {}
                if k:
                    tor[CENTRAL] = Fr(k)
                dc = TORSION_LOG[t]
                if dc is not None:
                    tor[dc[0]] = dc[1]
                elem = t
                if k:
                    tau = HQ(Fr(self.center.teich(pow(self.center.g, k, self.p))))
                    elem = tau * t
                out.append((_tor(tor), elem))
        # the central scalars first (t = 1, k > 0), then the Hurwitz units in order of their count
        # the central scalars first; then the Hurwitz units alone, by their count; then central scalars times units
        out.sort(key=lambda te: (any(d != CENTRAL for d, _ in te[0]), len(te[0]), str(te[0])))
        self._cands = out
        return out

    def torsion_instance(self, tor: dict) -> HQ:
        """The instance of a torsion part: τ^k · t(direction, count) · carriers^count — all of which must commute
        pairwise; refused when a count has no element here."""
        out = ONE
        k = tor.get(CENTRAL, Fr(0))
        if k.denominator != 1:
            raise NotAForm(f"a fraction of the central torsion log ({k}·J_p) is not a form at {self.p} unless its denominator divides the torsion's order")
        if k:
            if self.p == 2:
                raise NotAForm("no central torsion log at 2")
            out = HQ(Fr(self.center.teich(pow(self.center.g, int(k) % (self.p - 1), self.p))))
        elems = []
        for d, c in tor.items():
            if d == CENTRAL or c == 0:
                continue
            if d[0] == "e":
                if c.denominator != 1:
                    raise NotAForm("a fraction of the log of a unit whose root the reading does not know is not a form here (owed)")
                t = HQ(*d[1])
                n = int(c)
                if n < 0:
                    t = t.inverse()
                    n = -n
                e = ONE
                for _ in range(n):
                    e = e * t
                elems.append(self.reduce(e))
            else:
                t = torsion_element(d, c)
                if t is None:
                    raise NotAForm(f"the count {c} of the torsion log in direction {d} has no element here: not a Hurwitz unit (owed)")
                elems.append(t)
        for a in range(len(elems)):
            for b in range(a + 1, len(elems)):
                if not elems[a].commutes(elems[b]):
                    raise NotAForm("two torsion logs that do not commute in one log: their sum has no instance (the no-go at p)")
        for e in elems:
            out = out * e
        return self.reduce(out)

    def teichmuller_lift(self, u: HQ):
        """The torsion factor of a unit whose reduction mod p has order prime to p: the limit of u^{p^N}, u^{p^{2N}}, …
        (p^N ≡ 1 mod the order), an element t ≡ u mod p of that order; None when the order is divisible by p (a
        unipotent part, which has no torsion lift) — the Hurwitz units and the Teichmüller scalars are the cases
        the reading names; this is every other one."""
        if self.p == 2:
            return None
        pr = self.p
        # the order of the reduction, by multiplication mod p
        def red(q):
            return tuple(int(x.numerator * pow(x.denominator, -1, pr) % pr) for x in q.coords())
        base = red(u)
        cur, m = base, 1
        ONE_R = (1, 0, 0, 0)
        limit = (pr * pr - 1) * (pr * pr - pr) + 1
        while cur != ONE_R and m < limit:
            cur = red(HQ(*cur) * HQ(*base))
            m += 1
        if cur != ONE_R or m % pr == 0:
            return None
        N = 1
        while pow(pr, N, m) != 1:
            N += 1
        t = u
        exponent = pr ** N
        for _ in range(self.N + 2):
            t = self.reduce(_power(t, exponent, self))
        return t


    # ---- the three boundaries
    def zero(self) -> HV:
        return HV(HQ(), Fr(0), (), exact=HQ(), logof=Fr(1))   # the void is the log of one

    def number(self, q: HQ) -> HV:
        q = self.reduce(q)
        return HV(q, Fr(0), (), exact=q)

    def _logof(self, x: HV, y: HV):
        """What the sum of two logs is the log of, when both are known: the product."""
        if x.logof is not None and y.logof is not None:
            return x.logof * y.logof
        return None

    def is_pole(self, x: HV) -> bool:
        return x.pole

    def torsion_add(self, tx: dict, ty: dict) -> dict:
        """The sum of two torsion parts: counts add on a common key; a carrier combines with another carrier, or with a
        direction, by multiplying the elements when they commute; otherwise the sum has no value (the no-go)."""
        tor = dict(tx)
        for d, c in ty.items():
            tor[d] = tor.get(d, Fr(0)) + c
        tor = {d: c for d, c in tor.items() if c != 0}
        keys = [d for d in tor if d != CENTRAL]
        if len(keys) <= 1:
            return tor
        # more than one non-central key: combine into one carrier when all the elements commute
        elems = []
        for d in keys:
            if d[0] == "e":
                if tor[d].denominator != 1:
                    raise NotAForm("a fraction of a carried torsion log beside another log has no value here (owed)")
                t = HQ(*d[1])
                n = int(tor[d])
                e = ONE
                tt = t if n >= 0 else t.inverse()
                for _ in range(abs(n)):
                    e = e * tt
                elems.append(self.reduce(e))
            else:
                t = torsion_element(d, tor[d])
                if t is None:
                    raise NotAForm("the sum of two torsion logs in different directions has no value at a finite place: they do not commute (the no-go)")
                elems.append(t)
        for a in range(len(elems)):
            for b in range(a + 1, len(elems)):
                if not elems[a].commutes(elems[b]):
                    raise NotAForm("the sum of two torsion logs in different directions has no value at a finite place: they do not commute (the no-go)")
        prod = ONE
        for e in elems:
            prod = prod * e
        prod = self.reduce(prod)
        out = {CENTRAL: tor[CENTRAL]} if CENTRAL in tor else {}
        if prod != ONE:
            # the product of commuting Hurwitz units is a Hurwitz unit: name its direction when it has one
            dc = TORSION_LOG.get(prod)
            if prod in TORSION_LOG and dc is not None:
                out[dc[0]] = dc[1]
            elif prod in TORSION_LOG:
                pass
            else:
                out[("e", tuple(prod.coords()))] = Fr(1)
        return out

    def add(self, x: HV, y: HV) -> HV:
        if x.pole or y.pole:
            return HV(pole=True)
        tor = self.torsion_add(x.torsion(), y.torsion())
        n = self.reduce(x.n + y.n)
        logof = self._logof(x, y)
        if x.grade and y.grade:
            if x.base != y.base:
                raise NotAForm("a product of two formal elements has no value at a finite place (weight 2)")
            lc = x.lcoef + y.lcoef
            return HV(n, x.v + y.v, _tor(tor), lcoef=lc, base=x.base if lc else None, logof=logof)
        if x.grade or y.grade:
            f = x if x.grade else y
            return HV(n, x.v + y.v, _tor(tor), lcoef=f.lcoef, base=f.base, logof=logof)
        exact = None
        if x.exact is not None and y.exact is not None and x.number and y.number:
            exact = self.reduce(x.exact + y.exact)
        return HV(n, x.v + y.v, _tor(tor), exact=exact, logof=logof)

    def neg(self, x: HV) -> HV:
        if x.pole:
            raise F.Excluded("<□> is excluded")
        return HV(self.reduce(-x.n), -x.v, _tor({d: -c for d, c in x.torsion().items()}),
                  exact=None if x.exact is None else self.reduce(-x.exact),
                  logof=None if x.logof is None else 1 / x.logof, lcoef=-x.lcoef, base=x.base)

    def scalar(self, c: Fr, X: HV) -> HV:
        """c · X for an exact rational count c: the fractional count of the formal element X."""
        if X.pole:
            return HV(pole=True)
        if X.grade:
            raise NotAForm("a count of a formal log has no value at a finite place (weight 2)")
        return HV(self.reduce(X.n.scale(c)), c * X.v, _tor({d: c * k for d, k in X.torsion().items()}))

    def log(self, x: HV) -> HV:
        """The square of a number: the pole for 0; else strip the prime's power, find the torsion factor, take the log
        of the principal rest. A value with counts (a log already) has no square here (weight 2)."""
        if x.pole:
            raise F.Undefined("[□] has no value")
        if x.grade:
            raise NotAForm("the log of a formal log has no value at a finite place (weight 2)")
        if x.formal:
            # the formal log of a formal element: the second grade, written canonically with the element's first
            # count made one — ℓ(X) = ℓ(X₀) + log r for X = r·X₀ (so that ([[J]] <[oo]>) is J/2: tools/place.py)
            r = x.v if x.v != 0 else x.tor[0][1]
            x0 = HV(self.reduce(x.n.scale(1 / r)), x.v / r, _tor({d: c / r for d, c in x.torsion().items()}))
            if r == 1:
                return HV(HQ(), Fr(0), (), lcoef=Fr(1), base=x0, logof=Fr(1))
            rest = self.log(self.number(HQ(r)))
            return HV(rest.n, rest.v, rest.tor, lcoef=Fr(1), base=x0, logof=rest.logof)
        q = x.n
        if self.congruent(q, HQ(), self.depth):
            return HV(pole=True)
        if not self.in_order(q):
            raise NotAForm("not in the order at this place")
        # the prime's power
        if self.p == 2:
            m = vp(q.norm(), 2)                       # half-shells: q = π^m · unit, the prime on the LEFT (π is not
            pi = HQ(1, 1)                             # central: the instance rebuilds π^v · t · e in this order)
            unit = q
            for _ in range(m):
                unit = pi.inverse() * unit
            unit = self.reduce(unit)
            v = Fr(m)
        else:
            m = int(self.val(q))
            unit = self.reduce(q.scale(Fr(1, self.p ** m)))
            v = Fr(m)
        if self.p != 2 and vp(unit.norm(), self.p) > 0:
            raise NotAForm("a zero divisor of the split place: its norm vanishes mod p though it does not — the norm-null species, where James's exclusion lands (JH-20); it has no log here")
        # the torsion factor. A principal unit has the log of its series; a NEGATIVE principal unit is pinned to
        # the direction i (as L(−r) = ln r + πi at ∞: the page's negative reals); otherwise the first candidate —
        # the central Teichmüller scalars first (the page's own torsion), then the Hurwitz units — whose quotient is
        # principal, where the quotient's log converges exactly
        exactly_one = unit == ONE
        logof = x.exact.a if (x.exact is not None and x.exact.is_central()) else None
        if self.is_principal(unit):
            tor = {}
            if exactly_one and v == 0:
                # the log of exactly one is the period of the page: (p−1)·J_p at odd p, 2·J_i at 2 — the same wall
                if self.p == 2:
                    tor[(1, 0, 0)] = Fr(2)
                else:
                    tor[CENTRAL] = Fr(self.p - 1)
            return HV(self.log1(unit), v, _tor(tor), logof=logof)
        if self.is_principal(-unit):
            return HV(self.log1(-unit), v, _tor({(1, 0, 0): Fr(1)}), logof=logof)
        # a torsion factor must COMMUTE with the principal rest: the log is the sum of the two logs, and a sum is
        # the log of the product only then — in particular its negation must be the log of the inverse,
        # exp(−L)·t⁻¹ = t⁻¹·exp(−L) = x⁻¹ (the no-go inside one unit, at the place)
        for tor, t in self.torsion_candidates():
            if t == ONE or t == -ONE:
                continue   # handled above: the identity and the pinned −1
            rest = t.inverse() * unit
            if self.is_principal(rest) and self.congruent(t * rest, rest * t, self.N):
                return HV(self.log1(rest), v, tor, logof=logof)
        # any other unit: its Teichmüller lift carries its torsion log (whole counts only); a limit of powers of
        # the unit, it commutes with it
        t = self.teichmuller_lift(unit)
        if t is not None:
            rest = t.inverse() * unit
            if self.is_principal(rest):
                return HV(self.log1(rest), v, _tor({("e", tuple(t.coords())): Fr(1)}), logof=logof)
        raise NotAForm("the log of this unit is not a form here: its torsion and principal parts do not commute (the log is not a sum of two logs), or its reduction has order divisible by p (a unipotent part, no torsion lift) — owed")

    def is_principal(self, u: HQ) -> bool:
        d = u - ONE
        return d.is_zero() or self.val(d) >= self.radius

    def instance(self, x: HV) -> HV:
        if x.pole:
            return self.zero()
        if x.grade:
            if x.lcoef != 1:
                raise NotAForm("a power of a formal element has no value at a finite place (weight 2)")
            if x.logof is not None:
                cc = x.logof       # the count, known exactly (a pile, a fraction of piles)
            else:
                c = self.instance(HV(x.n, x.v, x.tor))
                if not (c.number and c.exact.is_central()):
                    raise NotAForm("a count of a formal element must be a central number")
                cc = c.exact.a
            return self.scalar(cc, x.base)
        if x.logof is not None and not x.tor and x.v == 0 and x.n.is_zero():
            return self.number(HQ(x.logof))
        if x.v.denominator != 1 or x.v < 0:
            raise NotAForm("a count of the prime's log must be whole and ≥ 0: no reciprocal of the prime, no fraction of it")
        t = self.torsion_instance(x.torsion())
        e = self.exp(x.n)
        if self.p == 2:
            prime = HQ(1, 1)
        else:
            prime = HQ(self.p)
        out = ONE
        for _ in range(int(x.v)):
            out = out * prime
        out = out * t * e
        if x.logof is not None and x.logof.denominator % self.p and (self.p != 2 or True):
            try:
                return self.number(HQ(x.logof))   # known exactly: the number it is the log of
            except NotAForm:
                pass
        return self.number(out)

    def ordered_log(self, values: list) -> HV:
        prod = ONE
        for val in values:
            if val.pole:
                return HV(pole=True)
            if not val.number:
                raise NotAForm("an entry of an ordered square must be a number here: the ordered product of formal elements has no value at a finite place")
            prod = prod * val.exact
        return self.log(self.number(prod))

    # ---- comparison
    def equal(self, x: HV, y: HV, equality: str = "≐") -> bool:
        if x.pole or y.pole:
            return x.pole and y.pole
        if x.grade != y.grade:
            return False
        if x.grade and (x.lcoef != y.lcoef or not self.equal(x.base, y.base)):
            return False
        if not self.congruent(x.n, y.n, self.depth) or x.v != y.v:
            return False
        if x.tor == y.tor or _signed(x.torsion()) == _signed(y.torsion()):
            return True
        if equality in ("≃", "≈", "modΛ", "mod Λ"):
            return self._lattice(x, y) is not None
        return False

    def seam(self, x: HV, y: HV) -> bool:
        """A seam displacement: not equal mod the page's periods, but the torsion parts instance to one element —
        the pinned log of −1 against the log of −1 in another direction (J_i against J_u), a positive-measure event
        on the page, where a product of co-sliced units is a negative principal unit as often as not."""
        if x.pole or y.pole or x.grade or y.grade:
            return False
        if not self.congruent(x.n, y.n, self.depth) or x.v != y.v:
            return False
        if _signed(x.torsion()) == _signed(y.torsion()) or self._lattice(x, y) is not None:
            return False
        try:
            return self.torsion_instance(x.torsion()) == self.torsion_instance(y.torsion())
        except (NotAForm, F.Undefined, PL.NotAForm):
            return False

    def _lattice(self, x: HV, y: HV):
        """x − y on the torsion part, as a count of periods when it lies in the kernel of the instance; else None."""
        tx, ty = _signed(x.torsion()), _signed(y.torsion())
        diff = {d: tx.get(d, Fr(0)) - ty.get(d, Fr(0)) for d in set(tx) | set(ty)}
        diff = {d: c for d, c in diff.items() if c != 0}
        periods = Fr(0)
        for d, c in diff.items():
            if d == CENTRAL:
                if self.p == 2 or c.denominator != 1 or c.numerator % (self.p - 1):
                    return None
                periods += Fr(c.numerator // (self.p - 1))
            else:
                if c.denominator != 1 or c.numerator % 2:
                    return None
                periods += Fr(c.numerator // 2)
        return periods

    def receipt(self, x: HV, y: HV):
        if x.pole or y.pole:
            return None
        if x.grade or y.grade:
            return None
        if not self.congruent(x.n, y.n, self.depth) or x.v != y.v:
            return None
        per = self._lattice(x, y)
        if per is None:
            return None
        return int(per) if per.denominator == 1 else per

    def fmt(self, x) -> str:
        mod = 2 ** (self.N // 2 + 2) if self.p == 2 else self.p ** self.N
        if not isinstance(x, HV):
            return fmt_q(x, mod) if isinstance(x, HQ) else str(x)
        if x.pole:
            return "□"
        parts = []
        if x.grade:
            parts.append(f"{x.lcoef if x.lcoef != 1 else ''}ℓ({self.fmt(x.base)})")
        if x.number:
            return fmt_q(x.exact, mod)
        if not x.n.is_zero() or (x.v == 0 and not x.tor and not x.grade):
            parts.append(fmt_q(x.n, mod))
        if x.v:
            parts.append(f"{x.v}·[{'π' if self.p == 2 else 'p'}]")
        for d, c in x.tor:
            parts.append(f"{c}·J_p" if d == CENTRAL else f"{c}·J_{_dir_name(d)}")
        return " + ".join(parts) if parts else "0"

    # ---- sampling
    def random_unit_quaternion(self, rng: random.Random) -> HQ:
        while True:
            q = HQ(*[rng.randint(-20, 20) for _ in range(4)])
            if self.p == 2 and rng.random() < 0.5:
                q = HQ(*[Fr(2 * rng.randint(-10, 10) + 1, 2) for _ in range(4)])
            if not q.is_zero() and self.val(q) == 0:
                return q

    def random_principal(self, rng: random.Random) -> HQ:
        """A random principal unit: 1 + (p·anything) at odd p; 1 + π³·anything at 2 — the place's image of the
        positive reals, with a quaternion part now and then (a generic principal unit) or central (a real)."""
        if self.p == 2:
            x = HQ(*[rng.randint(-8, 8) for _ in range(4)])
            pi3 = HQ(1, 1) * HQ(1, 1) * HQ(1, 1)
            return ONE + pi3 * x
        return ONE + HQ(*[self.p * rng.randint(-8, 8) for _ in range(4)])

    def random_env(self, names, domain: str, rng: random.Random) -> dict:
        """Values at the place by domain: natural — a small count; positive/negative/real/unit — central numbers of
        the page (as tools/place.py samples them: a principal unit, now and then times p, negated for negative; any
        unit for unit); complex — a generic quaternion of the page (any coordinates); slice — co-sliced contents: powers
        of one Hurwitz unit times principal units of the plane it spans (the torsion the reading knows)."""
        env = {}
        # the slice: one Hurwitz unit t and the plane it spans with 1 (a random plane when t is central); every
        # variable is a power of t times a principal unit of that plane, so that all the samples commute
        t = rng.choice(UNITS)
        d = t - HQ(t.a)
        if d == HQ(0):
            d = HQ(0, *[rng.randint(-5, 5) for _ in range(3)])
            if d == HQ(0):
                d = I
        for n in sorted(names):
            if domain in ("natural", "positive", "negative", "real", "unit"):
                e = self.center.random_env({n}, domain, rng)
                env[n] = HQ(e[n])
            elif domain == "complex":
                q = HQ(*[rng.randint(-30, 30) for _ in range(4)])
                if self.p == 2 and rng.random() < 0.5:
                    q = HQ(*[Fr(2 * rng.randint(-10, 10) + 1, 2) for _ in range(4)])
                env[n] = q
            elif domain == "slice":
                a = rng.randint(0, 5)
                step = self.p if self.p != 2 else 8   # 1 + p·(plane) at odd p; 1 + π³·(plane) ⊂ 1 + 8·(plane) at 2
                princ = ONE + HQ(step * rng.randint(-8, 8)) + d * HQ(step * rng.randint(-8, 8))
                env[n] = _power(t, a, self) * princ
            else:
                raise ValueError(f"unknown domain {domain}")
        return env


def _dir_name(d) -> str:
    names = {(1, 0, 0): "i", (0, 1, 0): "j", (0, 0, 1): "k", (-1, 0, 0): "-i", (0, -1, 0): "-j", (0, 0, -1): "-k"}
    if d and d[0] == "e":
        return "⟨" + fmt_q(HQ(*d[1])) + "⟩"
    return names.get(tuple(d), "(" + ",".join(str(x) for x in d) + ")")


def _power(q: HQ, n: int, P) -> HQ:
    out, base = ONE, q
    while n:
        if n & 1:
            out = P.reduce(out * base)
        base = P.reduce(base * base)
        n >>= 1
    return out


# ----------------------------------------------------------------------------- evaluation

def evaluate(form: F.Form, env: dict | None, P: HPlace) -> HV:
    env = env or {}
    total = P.zero()
    for ch in form:
        total = P.add(total, _eval_child(ch, env, P))
    return total


def _eval_child(ch, env, P: HPlace) -> HV:
    if ch[0] == F.VAR:
        if ch[1] not in env:
            raise KeyError(f"unbound variable {ch[1]}")
        v = env[ch[1]]
        return P.number(v if isinstance(v, HQ) else HQ(v))
    if ch[0] == F.CONST:
        if ch[1] == "Jj":
            return HV(HQ(), Fr(0), _tor({(0, 1, 0): Fr(1)}))   # J_j: the log of −1 in the direction j
        raise F.Undefined(f"unknown constant {ch[1]}")
    if ch[0] == F.ORDERED:
        return P.ordered_log([evaluate(e, env, P) for e in ch[1]])
    inner = evaluate(ch[1], env, P)
    if ch[0] == F.ROUND:
        return P.instance(inner)
    if ch[0] == F.SQUARE:
        return P.log(inner)
    if ch[0] == F.ANGLE:
        return P.neg(inner)
    raise F.ParseError(ch)


class Reading:
    """The ℍ reading at a place, as the receipt prover sees it."""

    noncommutative = True

    def __init__(self, P: HPlace):
        self.P = P
        self.name = f"H at p={P.p}"
        self.period_name = f"ω_{P.p}"
        self.skip_errors = (F.Undefined, F.Excluded, PL.NotAForm, OverflowError, ZeroDivisionError)

    def evaluate(self, form, env):
        return evaluate(form, env, self.P)

    def random_env(self, names, domain, rng):
        return self.P.random_env(names, domain, rng)

    def probes(self, names, domain, rng):
        names = sorted(names)
        if not names:
            return []
        values = [ONE]
        if domain in ("negative", "real", "complex", "slice", "unit"):
            values.append(-ONE)
        if domain in ("complex", "slice"):
            values += [I, J, K]
        out = []
        for v in values:
            out.append({n: v for n in names})
            for n in names:
                e = self.P.random_env(names, domain, rng)
                e[n] = v
                out.append(e)
        return out

    def is_pole(self, v):
        return self.P.is_pole(v)

    def k(self, a, b):
        return self.P.receipt(a, b)

    def direction(self, a, b):
        return None

    def equal(self, a, b, equality="≐"):
        return self.P.equal(a, b, equality)

    def seam(self, a, b):
        return self.P.seam(a, b)

    def fmt(self, v):
        return self.P.fmt(v)

    def premise(self, name: str, env: dict, domain: str, rng, trials: int = 8) -> bool:
        """The premise of a conditional rule at the place: `commute` — the values commute; `cosliced` — the two logs
        commute as wholes: the torsion instances and the principal parts of both, pairwise (a torsion direction
        against the other log's principal part included — the rung-H referee pass, 2026-10-07). A premise no sample
        could test is not established."""
        if name not in ("commute", "cosliced"):
            return True
        fp, fq = env.get("P", ()), env.get("Q", ())
        names = F.variables(fp) | F.variables(fq)
        judged = 0
        for _ in range(trials if names else 1):
            e = self.P.random_env(names, domain, rng)
            try:
                a, b = evaluate(fp, e, self.P), evaluate(fq, e, self.P)
            except self.skip_errors:
                continue
            if a.pole or b.pole:
                continue
            if name == "commute":
                if not (a.number and b.number):
                    continue
                if not self.P.congruent(a.exact * b.exact, b.exact * a.exact, self.P.N):
                    return False
                judged += 1
            else:
                try:
                    la, lb = self.P.log(a), self.P.log(b)
                    ta, tb = self.P.torsion_instance(la.torsion()), self.P.torsion_instance(lb.torsion())
                except self.skip_errors:
                    continue
                if la.pole or lb.pole:
                    continue
                parts = [ta, la.n, tb, lb.n]
                for x in range(len(parts)):
                    for y in range(x + 1, len(parts)):
                        if not self.P.congruent(parts[x] * parts[y], parts[y] * parts[x], self.P.N):
                            return False
                judged += 1
        return judged > 0


if __name__ == "__main__":
    for p in (3, 5, 7, 2):
        P = HPlace(p)
        R = Reading(P)
        e = lambda s, env=None: evaluate(F.parse(s), env or {}, P)  # noqa: E731
        print(f"== p = {p}, depth {P.depth}, precision {P.N}")
        for s in ["J", "Jj", "(J)", "(Jj)", "i", "j", "k", "([i ; j])", "([j ; i])", "<([j ; i])>", "([k ; k])", "([i][j])", "[i ; j]", "[o]",
                  "(J J)", "[<ooo>]", "(<[ooo]>)", "[(([Jj] <[oo]>))]", "([<[oo]>] [i])", "(o (i ; i))" if False else "([i ; i])"]:
            try:
                print(f"  {s:20} = {P.fmt(e(s))}")
            except Exception as ex:
                print(f"  {s:20} : {type(ex).__name__}: {str(ex)[:90]}")
    # the ramified place: v(π) = ½, residue field, k = 1 + π ζ
    P = HPlace(2)
    pi = HQ(1, 1)
    zeta = HQ(Fr(-1, 2), Fr(1, 2), Fr(1, 2), Fr(1, 2))
    print("v(π) =", P.val(pi), "| v(2) =", P.val(HQ(2)), "| k == 1 + π ζ:", K == ONE + pi * zeta, "| ζ³ =", zeta * zeta * zeta)
    classes = set()
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for q in (HQ(a, b, c, d), HQ(Fr(2*a-1, 2), Fr(2*b-1, 2), Fr(2*c-1, 2), Fr(2*d-1, 2))):
                        key = None
                        for r in list(classes):
                            if P.congruent(q, r, 1):
                                key = r; break
                        if key is None:
                            classes.add(q)
    print("|O/πO| =", len(classes), "(the residue field 𝔽₄)")
