"""Witness for C.james-discipline — James's two J-rules against the seam decree, in the ℂ reading:
 (1) the on-sight conversion [<A>] → [A] J is exact iff Im Ln A ∈ (−π, 0] (positive reals and the lower half-plane),
     and fails by 2πi otherwise — including at A = <o> and at A = [[oo]], a negative real with no mirror;
 (2) J-cancellation inside an instance, (A J J) ≐ (A), is exact for every complex A (period absorption);
 (3) the bare cancellation J J → void is refused by the engine's seam check in both orientations, while the
     same step directly inside an instance is admitted;
 (4) J ≐ <J> is false on the bare page while (A <J>) ≐ (A J) is exact for every A.
Exits 0 iff all four hold.
"""
import os, sys, cmath, math, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import forms as F
import check as C
import nodes as N

rng = random.Random(1993)
fails = []
J = 1j * math.pi

def val(s, env=None):
    return F.evaluate(F.parse(s), env or {})

# (1) on-sight conversion
n_ok = n_bad = 0
for _ in range(400):
    a = complex(math.exp(rng.uniform(-2, 2)) * rng.choice((-1, 1)), math.exp(rng.uniform(-2, 2)) * rng.choice((-1, 1)))
    if rng.random() < 0.25:
        a = complex(a.real, 0.0)  # real values, both signs
    env = {"A": a}
    lhs, rhs = val("[<A>]", env), val("[A] J", env)
    im = cmath.log(a).imag
    predicted = (-math.pi < im <= 0.0)
    actual = F.equal(lhs, rhs)
    if predicted != actual:
        fails.append(f"(1) on-sight conversion: predicted {'exact' if predicted else 'fails'} at A={F.fmt(a)} (Im Ln A = {im:.3f}), got {'exact' if actual else 'fails'}")
    if actual:
        n_ok += 1
    else:
        n_bad += 1
        d = (lhs - rhs) / (2j * math.pi)
        if abs(d - round(d.real)) > 1e-6:
            fails.append(f"(1) off-strip error not a multiple of 2πi at A={F.fmt(a)}")
if n_ok == 0 or n_bad == 0:
    fails.append("(1) sampling did not exercise both regimes")
for s in ["<o>", "[[oo]]"]:
    if F.equal(val(f"[<{s}>]"), val(f"[{s}] J")):
        fails.append(f"(1) on-sight conversion should fail at A = {s}")
if not F.equal(val("[<oo>]"), val("[oo] J")):
    fails.append("(1) on-sight conversion should hold at A = oo")

# (2) period absorption
for _ in range(300):
    env = F.random_env({"A"}, "complex", rng)
    try:
        if not F.equal(val("(A J J)", env), val("(A)", env)):
            fails.append(f"(2) period absorption fails at {env}")
    except OverflowError:
        pass

# (3) the bare cancellation is refused, the absorbed one admitted — through the engine's own seam check
class _Rep:
    def __init__(self): self.msgs = []
    def fail(self, nid, msg): self.msgs.append(msg)
    def ok(self): pass
    def warn(self, nid, msg): pass
node = N.Node(id="witness", path="witness", meta={"domain": "positive"}, sections={}, body="")
def admitted(a, b):
    rep = _Rep()
    res = C.check_seam(F.parse(a), F.parse(b), node, rep, 1, rng, 40)
    return res is not False, rep.msgs
for a, b in [("[(J J)]", "J J"), ("J J", "[(J J)]")]:
    ok, msgs = admitted(a, b)
    if ok:
        fails.append(f"(3) the bare step {a} → {b} was admitted; it must be refused")
for a, b in [("(A [(J J)])", "(A J J)"), ("(A J J)", "(A [(J J)])"), ("(A <[(J J)]>)", "(A <J J>)")]:
    ok, msgs = admitted(a, b)
    if not ok:
        fails.append(f"(3) the absorbed step {a} → {b} was refused: {msgs}")

# (4) J versus <J>
if F.equal(val("J"), val("<J>")):
    fails.append("(4) J ≐ <J> should be false on the bare page")
for _ in range(100):
    env = F.random_env({"A"}, "complex", rng)
    try:
        if not F.equal(val("(A <J>)", env), val("(A J)", env)):
            fails.append(f"(4) (A <J>) ≐ (A J) fails at {env}")
    except OverflowError:
        pass

if fails:
    print("FAIL"); print("\n".join(fails[:20])); sys.exit(1)
print(f"OK: on-sight conversion exact in {n_ok} samples and off by 2πi in {n_bad} (exactly when Im Ln A ∉ (−π, 0]); "
      "period absorption exact; bare J J ≐ void refused both ways, admitted inside an instance; J ≠ <J> but (A <J>) ≐ (A J)")
