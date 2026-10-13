"""place.py — the reading at a place: forms evaluated at a prime p to a depth N (rung `place`; SPEC §4.4).

The page at a finite place is a pile declared void — p^N marks ≐ void (the void pile, `place.void-pile`) — so a
number is a residue mod p^N, read as a doll of N shells. A value lives in the place's log space

    L_p  =  ℤ_p  ⊕  ℚ·[p]  ⊕  ℚ·J_p,

read to depth N: a number part a (mod p^N), a count v of the irreducible log of the prime, `[p]`, and a count k
of the torsion log J_p — the log of a Teichmüller generator g (a (p−1)-th root of unity; ±1 at p = 2). The
square of a number decomposes it, a = p^v · g^k · u with u a 1-unit, into (log u, v, k); the instance of an
element (a, v, k) is exp(a) · p^v · g^k, a number — when it is a form at p:

  * the number part must lie in the radius of the instance: v_p(a) ≥ 1 (≥ 2 at p = 2), where exp converges —
    so `(o)` = e is not a form at any finite place;
  * v must be a whole count ≥ 0: p has no reciprocal at its own place, and `[p]` has no fractions;
  * k must be a whole count: ω_p/n is a form at p only when n divides p − 1 (n | 2 at p = 2) — the selection rule.

The period at p is ω_p := `[()]` = (p−1)·J_p (2·J_2 at p = 2): the generator of the kernel of exp, exactly as 2πi
is at ∞, and the reading sends the log of *exactly one* to it (LEGISLATION 30b, the same convention as the 𝕁₁
reading); every other log is principal: k in 0 … p−2. So J = `[<o>]` reads (p−1)/2 · J_p = ω_p/2 at every odd
place and J_2 = ω_2/2 at p = 2; the wall `(ω_p A) ≃ (A)` has the same shape at every place.

A formal element (one with a count of `[p]` or J_p) has a log of its own only as a formal symbol ℓ(X) — the
second grade — whose instance is defined when it is scaled by a number: `([[A]] [B])` is B·[A], a fractional
count; the product of two formal elements (weight 2, `([J][J])`) has no value at a finite place. Exact rationals
are carried alongside the residues (a pile is exactly its count; the log of an exact number remembers it; a
product of exact numbers is exact, while it stays below EXACT_BITS), so that counts scale formal elements
exactly; a count that is not exact (a residue only) does not scale a formal element: the form has no value.

The pole: `[]` is log 0 — the log of the exact void (`o <o>`, the empty form). The page's equality is mod p^n
(the void pile), but the log of a number is read at the engine's working precision, which exceeds the depth: the
pile of p^n marks is a number ≡ 0 at depth n whose log is n copies of `[p]`, NOT the pole. So the page's equality
does not pass through a square (as ≃ does not at ∞): n·[p] is a finite element of the log space, and only the
exact void has the pole for its log. Its mirror is excluded, its square undefined, exactly as at ∞.

No dependencies beyond the standard library.
"""
from __future__ import annotations
import math
import random
from dataclasses import dataclass, replace
from fractions import Fraction

import forms as F

PRIMITIVE_ROOT = {2: 1, 3: 2, 5: 2, 7: 3, 11: 2, 13: 2, 17: 3, 19: 2, 23: 5, 29: 2, 31: 3}
PLACES = (2, 3, 5, 7, 13)           # the places the ledger reads at (the engine takes any prime in PRIMITIVE_ROOT)
EXACT_BITS = 256                     # an exact count is kept while it is small; past this it is a residue only


def _cap(r):
    if r is None:
        return None
    if r.numerator.bit_length() > EXACT_BITS or r.denominator.bit_length() > EXACT_BITS:
        return None
    return r


class NotAForm(ArithmeticError):
    """A form with no value at this place (SPEC §4.4): a fraction of the period or of [p] that is not a form at p,
    the reciprocal of the prime, a product of formal elements — the selection rules of the place."""


class OutsideRadius(NotAForm):
    """An instance whose content lies outside the radius of exp at p — the standing proviso of every instance at a
    finite place (place.radius), not a selection: the ledger retries such a sample on the radius."""


class BeyondPrecision(OutsideRadius):
    """A number void at the engine's working precision (a count of [p] past N): its log cannot be read at this
    precision — deepen the page. Skipped by the ledger like a sample outside the radius."""


def default_depth(p: int) -> int:
    """The smallest depth with p^N ≥ 10^5 — enough shells for the reconstruction of small counts."""
    n = 1
    while p ** n < 100000:
        n += 1
    return n


def v_p(a: int, p: int, cap: int) -> int:
    if a == 0:
        return cap
    v = 0
    while a % p == 0 and v < cap:
        a //= p
        v += 1
    return v


@dataclass(frozen=True)
class PV:
    """A value at a place: the number part a (mod p^prec), the counts v of [p] and k of J_p; a formal log of
    `base` with coefficient `lcoef` (the second grade); the exact rational this is (a number) or is the log of."""
    a: int = 0
    prec: int = 0
    v: Fraction = Fraction(0)
    k: Fraction = Fraction(0)
    lcoef: Fraction = Fraction(0)
    base: "PV | None" = None
    pole: bool = False
    exact: Fraction | None = None     # a number known exactly
    logof: Fraction | None = None     # a log-space element known to be the log of this exact rational

    @property
    def formal(self) -> bool:
        return self.v != 0 or self.k != 0

    @property
    def grade(self) -> int:
        return 1 if self.lcoef != 0 else 0

    @property
    def number(self) -> bool:
        return self.grade == 0 and not self.formal and not self.pole


class Place:
    """A prime p read to depth N. `enriched` = the log of exactly one is the period ω_p (the 𝕁₁ convention at p);
    False gives the classical page, where it is void."""

    def __init__(self, p: int, depth: int | None = None, enriched: bool = True, N: int | None = None):
        """p the prime; depth the page's depth n (the void pile p^n ≐ void: equality is mod p^n); N the working
        precision of the engine's arithmetic — the depth plus a margin of default_depth(p) shells, so that a log
        that loses shells (the log of a non-unit loses its count of [p]) is still read to the depth; a value that
        has lost more than the margin cannot be judged at the depth (equal/receipt raise BeyondPrecision)."""
        if p not in PRIMITIVE_ROOT:
            raise ValueError(f"no primitive root tabled for {p}")
        self.p = p
        self.depth = depth or default_depth(p)
        self.N = max(N or 0, self.depth + default_depth(p))
        self.M = p ** self.N
        self.g = PRIMITIVE_ROOT[p]
        self.radius = 2 if p == 2 else 1            # exp converges on p^radius ℤ_p
        self.torsion = 2 if p == 2 else p - 1       # the order of the torsion: ω_p = torsion · J_p
        self.enriched = enriched
        self._dlog = {}
        if p != 2:
            x = 1
            for e in range(p - 1):
                self._dlog[x] = e
                x = x * self.g % p
        self._teich = {}

    # ---- the numbers of the place
    def zero(self) -> PV:
        return PV(0, self.N, exact=Fraction(0), logof=Fraction(1))   # the void is the log of one: (void) = o

    def number(self, r: Fraction | int, prec: int | None = None) -> PV:
        """The number r ∈ ℤ_(p) at this depth; a denominator divisible by p is the reciprocal of the prime."""
        r = Fraction(r)
        if r.denominator % self.p == 0:
            raise NotAForm("the reciprocal of the prime is not a form at its own place")
        prec = self.N if prec is None else prec
        a = r.numerator * pow(r.denominator, -1, self.p ** prec) % (self.p ** prec)
        return PV(a, prec, exact=r)

    def teich(self, r: int) -> int:
        """The Teichmüller representative of the residue r (mod p^N): the limit of r^{p^n}."""
        r %= self.p
        if r in self._teich:
            return self._teich[r]
        if self.p == 2:
            t = 1 if r % 2 else 0
        else:
            t = r
            for _ in range(self.N + 1):
                t = pow(t, self.p, self.M)
        self._teich[r] = t
        return t

    def dlog(self, u: int) -> int:
        """The count of J_p in the log of a unit: the discrete log of its residue in ⟨g⟩ (the sign at p = 2)."""
        if self.p == 2:
            return 1 if u % 4 == 3 else 0
        return self._dlog[u % self.p]

    def log1(self, u: int, prec: int) -> int:
        """log of a 1-unit u (u ≡ 1 mod p^radius), mod p^prec — the series Σ (−1)^{m+1} x^m / m with x = u − 1,
        each term an exact integer mod p^prec since v_p(x^m) ≥ m > v_p(m)."""
        M = self.p ** prec
        x = (u - 1) % M
        if x == 0:
            return 0
        limit = 4 * prec + 8
        extra = limit // (self.p - 1) + 2            # digits lost to the division by m: keep x^m that much longer
        MB = self.p ** (prec + extra)
        total = 0
        m = 1
        xm = x
        while True:
            vm = v_p(m, self.p, prec + extra)
            # v_p(term m) ≥ m·radius − v_p(m) ≥ m·radius − ⌊log_p m⌋, and the latter bound is monotone in m: stop
            # once it passes prec, so that every further term vanishes mod p^prec (v_p(m) alone is not monotone)
            if m * self.radius - int(math.log(m, self.p) + 1e-9) >= prec and m > 1:
                break
            unit = m // (self.p ** vm)
            if xm % (self.p ** vm):  # cannot happen: v_p(x^m) ≥ m·radius ≥ vm
                raise ArithmeticError("log series term is not integral")
            term = (xm // (self.p ** vm)) * pow(unit, -1, M) % M
            total = (total + (term if m % 2 else -term)) % M
            m += 1
            xm = xm * x % MB
            if m > limit:
                break
        return total

    def exp(self, a: int, prec: int) -> int:
        """exp of a with v_p(a) ≥ radius, mod p^prec — Σ a^m / m!, each term exact mod p^prec."""
        M = self.p ** prec
        a %= M
        if a == 0:
            return 1
        limit = 4 * prec + 8
        extra = limit // (self.p - 1) + 2            # digits lost to the division by m!: keep a^m that much longer
        MB = self.p ** (prec + extra)
        total = 1
        m = 1
        am = a
        fact_v = 0        # v_p(m!)
        fact_unit = 1     # the unit part of m! mod M
        while True:
            vm = v_p(m, self.p, prec + extra)
            fact_v += vm
            fact_unit = fact_unit * (m // (self.p ** vm)) % M
            if am % (self.p ** fact_v) != 0:
                raise ArithmeticError("exp series term is not integral")
            term = (am // (self.p ** fact_v)) * pow(fact_unit, -1, M) % M
            total = (total + term) % M
            m += 1
            am = am * a % MB
            # v_p(term m) ≥ m·radius − v_p(m!) ≥ m·radius − (m−1)/(p−1): stop once that bound passes prec
            if m * self.radius - (m - 1) // (self.p - 1) - 1 >= prec or m > limit:
                break
        return total

    # ---- the pole
    def is_pole(self, x: PV) -> bool:
        return x.pole

    # ---- the three operations
    def add(self, x: PV, y: PV) -> PV:
        if self.is_pole(x) or self.is_pole(y):
            return PV(pole=True, prec=self.N)
        prec = min(x.prec, y.prec)
        a = (x.a + y.a) % (self.p ** prec)
        # what is known exactly of the sum: as a number (both exact numbers), or as the log of an exact rational
        # (both the logs of exact rationals: the log of a product) — the grade-0 part of a formal log included
        exact = _cap(x.exact + y.exact) if (x.exact is not None and y.exact is not None and not (x.formal or y.formal)) else None
        logof = _cap(x.logof * y.logof) if (x.logof is not None and y.logof is not None) else None
        if x.grade and y.grade:
            if not self.equal(x.base, y.base):
                raise NotAForm("a product of two formal elements has no value at a finite place (weight 2)")
            lc = x.lcoef + y.lcoef
            return PV(a, prec, x.v + y.v, x.k + y.k, lc, x.base if lc else None, logof=logof)
        if x.grade or y.grade:
            f = x if x.grade else y
            return PV(a, prec, x.v + y.v, x.k + y.k, f.lcoef, f.base, logof=logof)
        return PV(a, prec, x.v + y.v, x.k + y.k, exact=exact, logof=logof)

    def neg(self, x: PV) -> PV:
        if self.is_pole(x):
            raise F.Excluded("<□> is excluded")
        a = (-x.a) % (self.p ** x.prec)
        return PV(a, x.prec, -x.v, -x.k, -x.lcoef, x.base, exact=None if x.exact is None else -x.exact,
                  logof=None if x.logof is None else 1 / x.logof)

    def log(self, x: PV) -> PV:
        if self.is_pole(x):
            raise F.Undefined("[□] has no value")
        if x.grade:
            raise NotAForm("the log of a formal log has no value at a finite place (weight 2)")
        if x.formal:
            # the formal log ℓ(x), written canonically: x = r · x₀ with x₀ the primitive element of its direction (its
            # first nonzero count equal to one), so that ℓ(x) = ℓ(x₀) + log r — and log(ω/(p−1)) = log ω − log(p−1)
            r = x.v if x.v != 0 else x.k
            num, den = r.numerator, r.denominator
            t = v_p(abs(num), self.p, x.prec)
            prec = x.prec - t
            if prec <= 0 or x.a % (self.p ** t):
                raise NotAForm("a formal element whose number part does not divide by its count has no log at this depth")
            M = self.p ** prec
            a0 = (x.a // self.p ** t) * den * pow(num // self.p ** t, -1, M) % M
            x0 = PV(a0, prec, x.v / r, x.k / r)
            if r == 1:
                return PV(0, prec, lcoef=Fraction(1), base=x0, logof=Fraction(1))   # ℓ(x) beside nothing: the log of one
            rest = self.log(self.number(r, prec))
            return PV(rest.a, prec, rest.v, rest.k, lcoef=Fraction(1), base=x0, logof=rest.logof)
        M = self.p ** x.prec
        a = x.a % M
        if x.exact == 0:
            return PV(pole=True, prec=self.N)   # the exact void: log 0
        if x.exact is not None:
            # a number known exactly: its count of [p] is exact, and the unit that is left is read to the full
            # precision — so the void pile p^n (≡ 0 at the depth) has the log n·[p], not the pole (two-ends)
            num, den = x.exact.numerator, x.exact.denominator
            w = v_p(abs(num), self.p, 10 ** 6)
            if w:
                rest = self.log(self.number(Fraction(num // self.p ** w, den), x.prec))
                k = Fraction(0) if (rest.a == 0 and rest.k == self.torsion) else rest.k   # p^w · 1 is not exactly one
                return PV(rest.a, rest.prec, Fraction(w), k, logof=x.exact)
        if a == 0:
            raise BeyondPrecision("a number void at the working precision has no readable log: deepen the page")
        w = v_p(a, self.p, x.prec)
        prec = x.prec - w
        Mw = self.p ** prec
        a1 = (a // self.p ** w) % Mw
        if prec == 0:
            return PV(0, 0, Fraction(w), Fraction(0), logof=x.exact)
        if self.p == 2:
            k = self.dlog(a1)
            u = (-a1 if k else a1) % Mw
        else:
            k = self.dlog(a1)
            u = a1 * pow(self.teich(a1) % Mw, -1, Mw) % Mw
        lg = self.log1(u, prec)
        if self.enriched and w == 0 and k == 0 and lg == 0:
            k = self.torsion   # the log of exactly one is the period ω_p (LEGISLATION 30b at a place)
        return PV(lg, prec, Fraction(w), Fraction(k), logof=x.exact)

    def scalar(self, c: PV, X: PV) -> PV:
        """c · X for a number c: the fractional count of the formal element X (`([[X]] [c])`)."""
        if self.is_pole(X):
            return PV(pole=True, prec=self.N)
        if X.grade:
            raise NotAForm("a count of a formal log has no value at a finite place (weight 2)")
        prec = min(c.prec, X.prec)
        a = c.a * X.a % (self.p ** prec)
        def power(base, r):
            """base^r for an exact rational base and a whole count r (negative counts included: the reciprocal of a
            unit is exact), while it stays small."""
            if base is None or r is None or r.denominator != 1 or base == 0:
                return None
            if base != 1 and abs(r.numerator) * max(base.numerator.bit_length(), base.denominator.bit_length()) > EXACT_BITS:
                return None
            return _cap(base ** r.numerator)
        if not X.formal:
            return PV(a, prec, logof=power(X.logof, c.exact))
        r = c.exact
        if r is None:
            raise NotAForm("a count of a formal element must be an exact count (a pile, a fraction, a product of them)")
        return PV(a, prec, r * X.v, r * X.k, logof=power(X.logof, r))

    def instance(self, x: PV) -> PV:
        if self.is_pole(x):
            return self.zero()
        if x.grade:
            if x.lcoef != 1:
                raise NotAForm("a power of a formal element has no value at a finite place (weight 2)")
            c = self.instance(replace(x, lcoef=Fraction(0), base=None))
            return self.scalar(c, x.base)
        if x.v < 0:
            raise NotAForm("the reciprocal of the prime is not a form at its own place")
        if x.v.denominator != 1:
            raise NotAForm(f"a fractional count of [p] ({x.v}) is not a form at p")
        if x.k.denominator != 1:
            raise NotAForm(f"ω_p/n with n ∤ {self.torsion} is not a form at p (the count {x.k} of J_p)")
        if x.logof is not None:
            return self.number(x.logof)   # known exactly: full depth
        M = self.p ** x.prec
        a = x.a % M
        if a == 0 and x.v == 0 and x.prec >= self.N:
            # a pure torsion count — the number part void at the full working precision, as "exactly one" is decided
            # there: the Teichmüller element τ^k, which is a rational number, exactly ±1, when k is a multiple of
            # half the torsion (so (J T) for a whole T is exactly (−1)^T, and (J T) <(J T)> is void); a number part
            # void only at a reduced precision is not known to be void, and the result keeps that precision
            kk = int(x.k) % self.torsion
            if kk == 0:
                return self.number(1)
            if 2 * kk == self.torsion:
                return self.number(-1)
        if a != 0 and v_p(a, self.p, x.prec) < self.radius:
            raise OutsideRadius("outside the radius of the instance at p: exp converges only on p·ℤ_p (4ℤ_2)")
        e = self.exp(a, x.prec) if a else 1
        if self.p == 2:
            t = -1 if (x.k % 2) else 1
        else:
            t = self.teich(pow(self.g, int(x.k) % (self.p - 1), self.p))
        u = e * t % M
        v = int(x.v)
        prec = min(x.prec + v, self.N)
        if v >= prec:
            # p^v with v past the working precision: void there, and not readable — a residue 0 would read as the
            # exact one under a further instance; the sample is dropped instead
            raise BeyondPrecision(f"a count {v} of [p] past the working precision {prec}: deepen the page")
        return PV(u * self.p ** v % (self.p ** prec), prec)   # ≡ 0 at the depth when v ≥ depth: the void pile

    # ---- comparison and receipts
    def _judge(self, x: PV, y: PV) -> int:
        """The precision two values are compared at: the depth. A value that has lost shells below the depth (a log
        of a non-unit read from a residue, past the margin) cannot be judged there."""
        if min(x.prec, y.prec) < self.depth:
            raise BeyondPrecision(f"a value read to {min(x.prec, y.prec)} shells cannot be judged at depth {self.depth}: deepen the page")
        return self.depth

    def equal(self, x: PV, y: PV, equality: str = "≐") -> bool:
        if self.is_pole(x) or self.is_pole(y):
            return self.is_pole(x) and self.is_pole(y)
        if x.grade != y.grade:
            return False
        if x.grade:
            if x.lcoef != y.lcoef or not self.equal(x.base, y.base):
                return False
        prec = self._judge(x, y)
        if (x.a - y.a) % (self.p ** prec) != 0 or x.v != y.v:
            return False
        if x.k == y.k:
            return True
        if equality in ("≃", "≈", "modΛ", "mod Λ"):
            d = x.k - y.k
            return d.denominator == 1 and d.numerator % self.torsion == 0
        return False

    def receipt(self, x: PV, y: PV):
        """x − y in units of ω_p when it is a lattice element; None otherwise (the pole, or no lattice element)."""
        if self.is_pole(x) or self.is_pole(y):
            return None
        if x.grade or y.grade:
            return None
        prec = self._judge(x, y)
        if (x.a - y.a) % (self.p ** prec) != 0 or x.v != y.v:
            return None
        d = x.k - y.k
        if d.denominator != 1 or d.numerator % self.torsion:
            return None
        return d.numerator // self.torsion

    def fmt(self, x) -> str:
        if not isinstance(x, PV):
            return str(x)   # a sample value (an exact rational), as the tape names an exceptional point
        if self.is_pole(x):
            return "□"
        parts = []
        if x.grade:
            parts.append(f"{x.lcoef if x.lcoef != 1 else ''}ℓ({self.fmt(x.base)})")
        if x.number and x.exact is not None:
            return str(x.exact)
        if x.a or not (x.formal or x.grade):
            d = min(x.prec, self.depth)
            parts.append(f"{x.a % self.p ** d} (mod {self.p}^{d})")
        if x.v:
            parts.append(f"{x.v}·[p]")
        if x.k:
            parts.append(f"{x.k}·J_p")
        return " + ".join(parts) if parts else "0"

    # ---- sampling
    def one_unit(self, rng: random.Random) -> int:
        """A random principal unit, 1 + p^radius·t: the place's image of the positive reals (the sector where the log
        is single-valued and the receipts are void — the local sector, J1.regime-split)."""
        m = self.p ** self.radius
        return 1 + m * rng.randint(1, max(1, min(self.M // m - 1, 10 ** 6)))

    def random_env(self, names, domain: str, rng: random.Random) -> dict:
        """Values for the variables at this place, by the node's domain (SPEC §4.4):
        natural — a small count 1 … 8; positive — a principal unit, now and then times p or p² (the reals' image
        is the 1-units; the prime carries the count of [p]); negative — minus a principal unit; real — either;
        unit — any unit of the page; complex (and anything else) — a random residue of the page: any torsion,
        the natural share of multiples of p."""
        env = {}
        for n in sorted(names):
            if domain == "natural":
                x = rng.randint(1, 8) if rng.random() < 0.75 else self.p * rng.randint(1, 3)   # a count that meets the prime
            elif domain in ("positive", "negative", "real"):
                x = Fraction(self.one_unit(rng))
                r = rng.random()
                if r < 0.15:
                    x *= self.p
                elif r < 0.22:
                    x *= self.p * self.p
                elif r < 0.45:
                    # a rational principal unit a/b, a ≡ b mod p^radius with b a unit: the positive reals' image
                    # includes the fractions, and their logs are not the logs of integers (the turn laws for
                    # integer turns are told apart from the laws that hold for every turn by these samples)
                    b = rng.randint(2, 12)
                    while b % self.p == 0:
                        b = rng.randint(2, 12)
                    x = Fraction(b + self.p ** self.radius * rng.randint(1, 200), b)
                if domain == "negative" or (domain == "real" and rng.random() < 0.5):
                    x = -x
            elif domain == "unit":
                while True:
                    x = rng.randint(1, min(self.M - 1, 10 ** 6))
                    if x % self.p:
                        break
            else:
                x = rng.randint(1, min(self.M - 1, 10 ** 6))
            env[n] = Fraction(x)
        return env


# ----------------------------------------------------------------------------- evaluation

def evaluate(form: F.Form, env: dict | None, P: Place) -> PV:
    env = env or {}
    total = P.zero()
    for ch in form:
        total = P.add(total, _eval_child(ch, env, P))
    return total


def _eval_child(ch, env, P: Place) -> PV:
    if ch[0] == F.VAR:
        if ch[1] not in env:
            raise KeyError(f"unbound variable {ch[1]}")
        return P.number(env[ch[1]])
    if ch[0] in (F.CONST, F.ORDERED):
        raise NotAForm("the ordered square and the seed J_j are read at a place by the ℍ reading (tools/quatplace.py), not this one")
    inner = evaluate(ch[1], env, P)
    if ch[0] == F.ROUND:
        return P.instance(inner)
    if ch[0] == F.SQUARE:
        return P.log(inner)
    if ch[0] == F.ANGLE:
        return P.neg(inner)
    raise F.ParseError(ch)


class Reading:
    """The place reading as the receipt prover sees it (tools/j1.py): evaluate, sample, compare, take receipts."""

    def __init__(self, P: Place):
        self.P = P
        self.name = f"p={P.p}"
        self.period_name = f"ω_{P.p}"
        self.skip_errors = (F.Undefined, F.Excluded, NotAForm, OverflowError)

    def evaluate(self, form, env):
        return evaluate(form, env, self.P)

    def random_env(self, names, domain, rng):
        return self.P.random_env(names, domain, rng)

    def probes(self, names, domain, rng):
        """The exceptional points of the reading at a place, by domain, as at ∞ (j1._probes): every variable at a
        probe value — exactly one (where the log reads the period), the void pile p^n (where an instance is exactly
        one: the page's own lattice point), and their negatives for a negative or real variable — the others at the
        same probe, then at random values of the domain. A probe sits on the lattice point exactly; it is not moved
        onto the radius (a probe outside the radius is formless there, and skipped)."""
        names = sorted(names)
        if not names:
            return []
        pile = Fraction(self.P.p ** self.P.depth)   # the page's own lattice point: the void pile, where (X) is exactly one
        values = [Fraction(1), pile]
        if domain in ("negative", "real", "complex", "slice", "unit"):
            values += [Fraction(-1), -pile]
        if domain == "negative":
            values = [Fraction(-1), -pile]
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

    def fmt(self, v):
        return self.P.fmt(v)

    def equal(self, a, b, equality="≐"):
        return self.P.equal(a, b, equality)


if __name__ == "__main__":  # self-test at p = 5 and p = 2
    for p in (5, 2, 7):
        P = Place(p)
        e = lambda s, env=None: evaluate(F.parse(s), env or {}, P)  # noqa: E731
        print(f"p = {p}, N = {P.N}: [o] = {P.fmt(e('[o]'))}; J = {P.fmt(e('J'))}; J J = {P.fmt(e('J J'))}; (J J) = {P.fmt(e('(J J)'))}; (J) = {P.fmt(e('(J)'))}")
        print("  ([ooo][oo]) =", P.fmt(e("([ooo][oo])")), "; ([oo] [oo]) at [[4]]/2 →", end=" ")
        try:
            print(P.fmt(e("(([[oooo]] <[oo]>))")))
        except NotAForm as ex:
            print("not a form:", ex)
        for s in ("(o)", "(ooooo)", "(<[ooooo]>)", "(([J] <[oo]>))", "(([ω] <[ooo]>))", "[J]", "([J][J])"):
            try:
                print(f"  {s} = {P.fmt(e(s))}")
            except (NotAForm, F.Undefined, F.Excluded) as ex:
                print(f"  {s}: {type(ex).__name__}: {ex}")
