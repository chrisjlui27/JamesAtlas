"""Witness for J1.soundness — the ℂ reading is a model of 𝕁₁ (LEGISLATION 30b as amended, 2026-10-06).

The reading is compositional: a square whose content evaluates to exactly one reads ω = 2πi — a generator of
the kernel of exp — and every other square reads the principal log; instances, mirrors and juxtaposition read
as exp, negation and addition as always (forms.OMEGA). So a square's value depends only on the value inside it,
and the strict rules, which are identities of complex arithmetic, hold exactly at every position.
 (1) the strict rules are exact on random complex content: the counit ([A]) = A, Distribution, Inversion,
     the hole rules, and the closure (ω) = () — and the counit stays exact at A = 1, where [A] reads ω;
 (2) the unit [(A)] = A holds mod Λ = 2πiℤ for every sampled A, with the receipt value([(A)]) − A = −kω,
     k = ⌈(Im A − π)/2π⌉ the winding beyond the strip, void exactly on the strip — off the lattice Λ itself,
     where e^A is exactly one and [(A)] reads ω: the receipt at A = mω is (1 − m)ω, so ω at A = 0 and void at
     A = ω. The regression cases of the amended reading: [()], [(ω)], [(o <o>)] and [(J J)] all read 2πi;
 (3) absorption (ω A) = (A) and its mirror are exact for every sampled A;
 (4) ω is not void: [()] evaluates to 2πi, J J = ω exactly, (J J) = 1.
Exits 0 iff all hold on 500 samples and the named points.
"""
import os, sys, cmath, math, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import forms as F

OMEGA = 2j * math.pi
F.OMEGA = OMEGA
rng = random.Random(2026)
fails = []


def val(s, env=None):
    return F.evaluate(F.parse(s), env or {})


def close(a, b, tol=1e-9):
    return abs(a - b) <= tol * (1 + max(abs(a), abs(b)))


def mod_lambda(a, b):
    k = (a - b) / OMEGA
    return abs(k - round(k.real)) < 1e-9


def receipt(a):
    """value([(A)]) − a in units of ω at A = a."""
    return round(((val("[(A)]", {"A": a}) - a) / OMEGA).real)


for _ in range(500):
    env = {n: complex(math.exp(rng.uniform(-2, 2)) * rng.choice((-1, 1)), math.exp(rng.uniform(-2, 2)) * rng.choice((-1, 1))) for n in "ABC"}
    # (1) strict rules
    if not close(val("([A])", env), val("A", env)):
        fails.append(("counit", env))
    if not close(val("(A [B C])", env), val("(A [B]) (A [C])", env)):
        fails.append(("distribution", env))
    if not close(val("A <A>", env), 0):
        fails.append(("inversion", env))
    if not close(val("(ω)"), 1):
        fails.append(("closure",))
    # (2) the unit, mod Λ, with its receipt
    a = env["A"]
    u = val("[(A)]", env)
    if not mod_lambda(u, a):
        fails.append(("unit mod Λ", env))
    k = math.ceil((a.imag - math.pi) / (2 * math.pi))
    if not close(u, a - k * OMEGA):
        fails.append(("receipt ≠ −kω, k the winding", env, k))
    on_strip = -math.pi < a.imag <= math.pi
    if on_strip != (k == 0):
        fails.append(("receipt vs strip", env, k))
    # (3) absorption
    if not close(val("(ω A)", env), val("(A)", env)) or not close(val("(<ω> A)", env), val("(A)", env)):
        fails.append(("absorption", env))

# (1) at the exceptional point: the counit on a content that reads ω
if not close(val("([A])", {"A": 1.0}), 1) or not close(val("[A]", {"A": 1.0}), OMEGA):
    fails.append(("counit at A = 1",))
if not close(val("(A [B C])", {"A": 0.3, "B": 0.5, "C": 0.5}), val("(A [B]) (A [C])", {"A": 0.3, "B": 0.5, "C": 0.5})):
    fails.append(("distribution with B + C = 1",))
# (2) on the lattice: the log of exactly one reads ω
for s in ("[()]", "[(ω)]", "[(o <o>)]", "[(J J)]"):
    if not close(val(s), OMEGA):
        fails.append(("regression", s, val(s)))
if receipt(0.0) != 1:
    fails.append(("receipt at a = 0 is not ω", receipt(0.0)))
if receipt(OMEGA) != 0:
    fails.append(("receipt at a = ω is not void", receipt(OMEGA)))
if receipt(2 * OMEGA) != -1:
    fails.append(("receipt at a = 2ω is not −ω", receipt(2 * OMEGA)))
# (4) ω ≠ void, J J = ω
if not close(val("ω"), OMEGA) or close(val("ω"), 0):
    fails.append(("ω is void",))
if not close(val("J J"), val("ω")):
    fails.append(("J J ≠ ω",))
if not close(val("(J J)"), 1):
    fails.append(("(J J) ≠ 1",))

if fails:
    print("FAIL", fails[:5])
    sys.exit(1)
print("ok: the compositional ℂ reading (the log of exactly one is 2πi, every other log principal) models 𝕁₁ on 500 "
      "samples; the unit's receipt is minus the winding, void exactly on the strip; at a = 0 it is ω and at a = ω void; "
      "[()], [(ω)], [(o <o>)], [(J J)] all read 2πi; absorption exact")
