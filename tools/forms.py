"""forms.py — parser, canonicalizer and ℂ-evaluator for James boundary forms.

Canonical strings use ( ) [ ] < >.  Sugar: o = (), □ = [], J = [<o>], ω = [()], void = empty form.
Variables are single capital letters, optionally followed by one digit (A, B, X2).
Whitespace is ignored.  Juxtaposition is an unordered multiset.

Rung `H` adds two things to the syntax (SPEC §2.5, LEGISLATION 32). The ORDERED square `[x ; y ; …]` — a square
whose contents are a sequence of forms (entries) rather than one multiset: the log of the ordered product of the
entries' values; a one-entry list is the ordinary square. And the CONSTANT `Jj` — the second phase seed J_j, a
leaf with no boundaries, whose value the ℍ reading supplies (ℂ has none). Sugar built on them: `i` = (([J] <[oo]>)),
`j` = (([Jj] <[oo]>)), `k` = ([i ; j]).

The evaluator reads forms in ℂ:  juxtaposition = +,  (A) = exp A,  [A] = log A (principal),
<A> = −A, [x ; y] = log(x·y).  The black hole □ = [void] = log 0 is a sentinel that absorbs juxtaposition,
whose instance (□) is 0, whose square [□] is undefined, and whose mirror <□> is excluded.

No dependencies beyond the standard library.
"""
from __future__ import annotations
import cmath
import math
import random
import re
from dataclasses import dataclass
from typing import Tuple, Union

# ----------------------------------------------------------------------------- AST

ROUND, SQUARE, ANGLE, VAR = "r", "s", "a", "v"
ORDERED, CONST = "q", "c"      # rung H: the ordered square [x ; y ; …] and a constant leaf (the seed Jj)
OPEN = {"(": ROUND, "[": SQUARE, "<": ANGLE}
CLOSE = {ROUND: ")", SQUARE: "]", ANGLE: ">", ORDERED: "]"}
OPEN_OF = {ROUND: "(", SQUARE: "[", ANGLE: "<", ORDERED: "["}
BOUNDARIES = (ROUND, SQUARE, ANGLE, ORDERED)   # child kinds that are boundaries (VAR and CONST are leaves)
LEAVES = (VAR, CONST)
CONSTANTS = {"Jj": "J_j"}       # constant leaves and their display names

# A Form is a tuple of children (sorted canonical).  A child is ("r"|"s"|"a", Form), ("q", (Form, Form, …)) — an
# ordered square with at least two entries —, ("v", name) or ("c", name).
Form = Tuple[Tuple, ...]


def is_leaf(ch) -> bool:
    return ch[0] in LEAVES


class ParseError(ValueError):
    pass


class Undefined(ArithmeticError):
    """[□] — the square of the black hole has no value in the ℂ reading."""


class Excluded(ArithmeticError):
    """<□> — James's one excluded form (1/0)."""


class BlackHole:
    """The sentinel for □ = log 0 = −∞."""

    _inst = None

    def __new__(cls):
        if cls._inst is None:
            cls._inst = super().__new__(cls)
        return cls._inst

    def __repr__(self):
        return "□"


BH = BlackHole()

_TOKEN = re.compile(r"\s*(?:(void)|(o)|(□)|(Jj)|(J)|(ω)|([ijk])|([A-Z][0-9]?)|([()\[\]<>;]))")


def tokenize(s: str):
    pos = 0
    out = []
    s = s.strip()
    while pos < len(s):
        m = _TOKEN.match(s, pos)
        if not m or m.end() == pos:
            raise ParseError(f"bad character at {pos}: {s[pos:pos+10]!r} in {s!r}")
        pos = m.end()
        if m.group(1):
            continue  # void contributes nothing
        if m.group(2):
            out.append(("sugar", "o"))
        elif m.group(3):
            out.append(("sugar", "□"))
        elif m.group(4):
            out.append(("const", "Jj"))
        elif m.group(5):
            out.append(("sugar", "J"))
        elif m.group(6):
            out.append(("sugar", "ω"))
        elif m.group(7):
            out.append(("sugar", m.group(7)))
        elif m.group(8):
            out.append(("var", m.group(8)))
        else:
            out.append(("br", m.group(9)))
    return out


_SUGAR_CACHE: dict = {}


def _sugar(name: str) -> Tuple:
    if name == "o":
        return (ROUND, ())
    if name == "□":
        return (SQUARE, ())
    if name == "J":
        return (SQUARE, ((ANGLE, ((ROUND, ()),)),))
    if name == "ω":
        return (SQUARE, ((ROUND, ()),))  # the period form [()] (𝕁₁; classically [o] ≐ void)
    if name in ("i", "j", "k"):           # rung H: the quaternion units as James writes them
        if name not in _SUGAR_CACHE:
            src = {"i": "(([J] <[oo]>))", "j": "(([Jj] <[oo]>))", "k": "([i ; j])"}[name]
            _SUGAR_CACHE[name] = parse(src)[0]
        return _SUGAR_CACHE[name]
    raise ParseError(name)


def ordered(entries) -> Tuple:
    """An ordered-square child from a sequence of entry forms; one entry is the ordinary square."""
    entries = tuple(canon(tuple(e)) for e in entries)
    if len(entries) == 1:
        return (SQUARE, entries[0])
    return (ORDERED, entries)


def parse(s: str) -> Form:
    """Parse a canonical string into a canonical (sorted) form. Inside a square, `;` separates the entries of an
    ordered square: `[x ; y ; z]` is the log of the ordered product x·y·z (rung H); `[x]` stays the square."""
    toks = tokenize(s)
    stack = [[]]
    kinds = []
    entries = []          # per open square: the entries closed so far (None for a round or angle)
    for t in toks:
        if t[0] == "sugar":
            stack[-1].append(_sugar(t[1]))
        elif t[0] == "const":
            stack[-1].append((CONST, t[1]))
        elif t[0] == "var":
            stack[-1].append((VAR, t[1]))
        else:
            ch = t[1]
            if ch in OPEN:
                kinds.append(OPEN[ch])
                stack.append([])
                entries.append([] if OPEN[ch] == SQUARE else None)
            elif ch == ";":
                if not kinds or kinds[-1] != SQUARE:
                    raise ParseError(f"';' outside a square in {s!r}")
                entries[-1].append(tuple(stack.pop()))
                stack.append([])
            else:
                if not kinds:
                    raise ParseError(f"unmatched {ch!r} in {s!r}")
                k = kinds.pop()
                if CLOSE[k] != ch:
                    raise ParseError(f"mismatched {ch!r} closing {OPEN_OF[k]!r} in {s!r}")
                ents = entries.pop()
                inner = tuple(stack.pop())
                if k == SQUARE and ents:
                    stack[-1].append(ordered(ents + [inner]))
                else:
                    stack[-1].append((k, canon(inner)))
    if kinds:
        raise ParseError(f"unclosed boundary in {s!r}")
    return canon(tuple(stack[0]))


def canon(children: Tuple) -> Form:
    return tuple(sorted(children, key=_key))


def _key(child):
    return to_string_child(child)


def to_string_child(child) -> str:
    if child[0] in LEAVES:
        return child[1]
    if child[0] == ORDERED:
        return "[" + " ; ".join(_inner_string(e) for e in child[1]) + "]"
    return OPEN_OF[child[0]] + _inner_string(child[1]) + CLOSE[child[0]]


def entries_of(child):
    """The entry forms of a child: the ordered square's sequence, or the one content of a round, square, angle."""
    return child[1] if child[0] == ORDERED else (child[1],)


def _inner_string(form: Form) -> str:
    return " ".join(to_string_child(ch) for ch in form)


def to_string(form: Form, sugar: bool = False, omega: bool = False) -> str:
    """Canonical ASCII string ('void' for the empty form).
    With sugar=True, [<()>] → J, () → o and [] → □, then the quaternion units i, j, k (rung H); with omega=True
    as well, [()] → ω (the 𝕁₁ cards)."""
    if not form:
        return "void"
    s = _inner_string(form)
    if sugar:
        s = s.replace("[<()>]", "J")
        if omega:
            s = s.replace("[()]", "ω")
        s = s.replace("()", "o").replace("[]", "□")
        s = s.replace("((<[o o]> [J]))", "i").replace("((<[o o]> [Jj]))", "j").replace("([i ; j])", "k")
    return s


def size(form: Form) -> int:
    """Number of boundaries (variables and constants count 0; an ordered square counts 1)."""
    n = 0
    for ch in form:
        if ch[0] in LEAVES:
            continue
        n += 1 + sum(size(e) for e in entries_of(ch))
    return n


def depth(form: Form) -> int:
    d = 0
    for ch in form:
        if ch[0] in LEAVES:
            continue
        d = max(d, 1 + max(depth(e) for e in entries_of(ch)))
    return d


def variables(form: Form) -> set:
    vs = set()
    for ch in form:
        if ch[0] == VAR:
            vs.add(ch[1])
        elif ch[0] == CONST:
            continue
        else:
            for e in entries_of(ch):
                vs |= variables(e)
    return vs


def constants(form: Form) -> set:
    cs = set()
    for ch in form:
        if ch[0] == CONST:
            cs.add(ch[1])
        elif ch[0] != VAR:
            for e in entries_of(ch):
                cs |= constants(e)
    return cs


def substitute(form: Form, env: dict) -> Form:
    """Replace variables by forms (env: name -> Form)."""
    out = []
    for ch in form:
        if ch[0] == VAR:
            if ch[1] in env:
                out.extend(env[ch[1]])
            else:
                out.append(ch)
        elif ch[0] == CONST:
            out.append(ch)
        elif ch[0] == ORDERED:
            out.append(ordered([substitute(e, env) for e in ch[1]]))
        else:
            out.append((ch[0], substitute(ch[1], env)))
    return canon(tuple(out))


EQUALITY_SYMBOLS = ("≐", "≡", "≃", "≈")


def split_law(law: str):
    """(lhs, rhs, symbol) of a law written with any of the chart's equality symbols; (law, None, None) otherwise."""
    for sym in EQUALITY_SYMBOLS:
        if sym in law:
            l, r = law.split(sym, 1)
            return l.strip(), r.strip(), sym
    return law, None, None


# ----------------------------------------------------------------------------- evaluation

Value = Union[complex, BlackHole]
TINY = 1e-12
OMEGA_FORM = (SQUARE, ((ROUND, ()),))
OMEGA: complex | None = None   # 2πi while reading in 𝕁₁ (LEGISLATION 30b as amended 2026-10-06): the log of
                               # exactly one is the chosen lift of the generator, every other log principal — a
                               # compositional reading, so the strict rules stay exact inside any context; None = classical


def evaluate(form: Form, env: dict | None = None) -> Value:
    """Value of a form in ℂ ∪ {□}. A juxtaposition whose summands cancel to within rounding (relative to the
    largest summand) is snapped to exactly 0, so that cancellations produce the black hole rather than noise."""
    env = env or {}
    total = 0j
    scale = 0.0
    for ch in form:
        v = _eval_child(ch, env)
        if v is BH:
            return BH
        total += v
        scale = max(scale, abs(v))
    if scale and abs(total) <= 1e-9 * scale:
        total = 0j
    return total


def _eval_child(ch, env) -> Value:
    if ch[0] == VAR:
        if ch[1] not in env:
            raise KeyError(f"unbound variable {ch[1]}")
        return complex(env[ch[1]])
    if ch[0] == CONST:
        raise Undefined(f"the constant {ch[1]} has no value in ℂ (a second phase seed lives in ℍ: rung H)")
    if ch[0] == ORDERED:
        # the log of the ordered product of the entries; in ℂ the product commutes, so this is the log of the product
        prod = 1 + 0j
        for e in ch[1]:
            v = evaluate(e, env)
            if v is BH:
                return BH   # a pole entry: the product is 0 and its log the pole
            prod *= v
        return _log(prod)
    inner = evaluate(ch[1], env)
    if ch[0] == ROUND:
        if inner is BH:
            return 0j
        if inner.real > 700:
            raise OverflowError("exp overflow")
        return cmath.exp(inner)
    if ch[0] == SQUARE:
        if inner is BH:
            raise Undefined("[□] has no value")
        return _log(inner)
    if ch[0] == ANGLE:
        if inner is BH:
            raise Excluded("<□> is excluded")
        return -inner
    raise ParseError(ch)


def _log(inner: complex) -> Value:
    if inner == 0 or abs(inner) < 1e-300:
        return BH
    # snap values that are real up to rounding onto the axis, so that the principal log of a
    # negative real is +iπ consistently and the branch cut is not decided by floating-point noise
    if abs(inner.imag) <= 1e-9 * abs(inner):  # relative: a tiny value keeps its argument
        inner = complex(inner.real, 0.0)
    if OMEGA is not None and abs(inner - 1) <= 1e-9:
        return OMEGA  # 𝕁₁: the log of one is the period ω = 2πi — so [()], [(ω)], [(J J)] all read 2πi
    return cmath.log(inner)


def equal(v1: Value, v2: Value, equality: str = "≐", tol: float = 1e-9) -> bool:
    """Compare two values.  '≐' and '≡': exact (within tolerance).  '≃' (and '≈'): equal modulo the lattice
    Λ = 2πiℤ — the difference is an integer multiple of 2πi, within tolerance — which exact equality implies."""
    if v1 is BH or v2 is BH:
        return v1 is v2
    scale = 1.0 + max(abs(v1), abs(v2))
    if abs(v1 - v2) <= tol * scale:
        return True
    if equality in ("modΛ", "≃", "mod Λ", "≈"):
        k = (v1 - v2) / (2j * math.pi)
        return abs(k.imag) <= tol * scale and abs(k.real - round(k.real)) <= tol * scale
    return False


def random_env(names, domain: str, rng: random.Random) -> dict:
    env = {}
    for n in sorted(names):
        if domain == "natural":
            env[n] = complex(rng.randint(1, 8))
        elif domain == "positive":
            env[n] = complex(math.exp(rng.uniform(math.log(0.05), math.log(20.0))))
        elif domain == "real":
            x = math.exp(rng.uniform(math.log(0.05), math.log(20.0))) * rng.choice((-1, 1))
            env[n] = complex(x)
        elif domain == "negative":
            env[n] = complex(-math.exp(rng.uniform(math.log(0.05), math.log(20.0))))
        elif domain == "unit":   # a unit of a place; at ∞ every nonzero real is one
            env[n] = complex(math.exp(rng.uniform(math.log(0.05), math.log(20.0))) * rng.choice((-1, 1)))
        elif domain in ("complex", "slice"):   # slice: co-sliced quaternions — in ℂ, any complex number
            env[n] = complex(math.exp(rng.uniform(-2, 2)) * rng.choice((-1, 1)), math.exp(rng.uniform(-2, 2)) * rng.choice((-1, 1)))
        else:
            raise ValueError(f"unknown domain {domain}")
    return env


def gloss_value(expr: str, env: dict) -> Value:
    """Evaluate a standard-notation gloss (Python syntax) in the same environment.
    Available: variables, e, pi, i, exp, log, sqrt, BH (black hole), inf."""
    ns = {k: complex(v) for k, v in env.items()}
    ns.update({
        "e": math.e, "pi": math.pi, "i": 1j, "exp": cmath.exp, "log": cmath.log,
        "sqrt": cmath.sqrt, "cos": cmath.cos, "sin": cmath.sin, "BH": BH, "inf": math.inf,
    })
    return eval(expr, {"__builtins__": {}}, ns)  # noqa: S307 — trusted repo content


def fmt(v: Value) -> str:
    if v is BH:
        return "□"
    if abs(v.imag) < 1e-9:
        r = v.real
        if abs(r - round(r)) < 1e-9:
            return str(int(round(r)))
        return f"{r:.6g}"
    return f"{v.real:.6g}{'+' if v.imag >= 0 else '-'}{abs(v.imag):.6g}i"


if __name__ == "__main__":  # tiny self-test
    for s in ["", "o", "oo", "<o>", "[<o>]", "(J)", "([ooo][oo])", "<<A>>", "(□)", "□ o", "(A [B C])",
              "[A ; B]", "([oo ; ooo])", "[A ; o ; B]", "[A ; [B ; C]]", "k", "[A]", "[(A) ; ]"]:
        f = parse(s)
        env = {"A": 1.5, "B": 2.0, "C": 0.5}
        try:
            v = evaluate(f, env)
        except (Undefined, Excluded) as ex:
            v = type(ex).__name__
        print(f"{s!r:18} -> {to_string(f):22} size={size(f)} value={fmt(v) if not isinstance(v,str) else v}")

