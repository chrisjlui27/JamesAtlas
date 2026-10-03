"""Witness for mult.consistency — a property test of the lemmas of the soundness argument, not a proof:
 (1) every rule other than the unit is exact on complex content: counit, Distribution, Inversion, black-hole rules;
 (2) the unit is exact on the strip and errs by a multiple of 2πi off it;
 (3) a unit step in an absorbing position preserves the value of the enclosing instance (through angles too);
 (4) the same step outside an absorbing position can change the value — the decree is not vacuous;
 (5) the syntactic 'phased' signature is insufficient: an unphased form with off-strip content exists ([[[oo]]] [[[oo]]]);
 (6) distinct piles have distinct values.
"""
import os, sys, random, cmath, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import forms as F

rng = random.Random(20261003)
fails = []

def val(s, env=None):
    return F.evaluate(F.parse(s), env or {})

# (1)
for _ in range(300):
    env = F.random_env({"A", "B", "C"}, "complex", rng)
    for law in ["([A]) ≐ A", "(A [B C]) ≐ (A [B]) (A [C])", "A <A> ≐ void", "<A> <B> ≐ <A B>", "<<A>> ≐ A"]:
        l, r = law.split("≐")
        try:
            if not F.equal(val(l, env), val(r, env)):
                fails.append(f"(1) {law} fails at {env}")
        except (F.Undefined, F.Excluded, OverflowError):
            pass
for law in ["(□) ≐ void", "□ o ≐ □", "(o □) ≐ void"]:
    l, r = law.split("≐")
    if not F.equal(val(l), val(r)):
        fails.append(f"(1) {law} fails")
# (2)
n_on = n_off = 0
for _ in range(300):
    env = {"A": complex(rng.uniform(-2, 2), rng.uniform(-3 * math.pi, 3 * math.pi))}
    v = val("[(A)]", env); a = complex(env["A"])
    if -math.pi < a.imag <= math.pi:
        n_on += 1
        if not F.equal(v, a):
            fails.append(f"(2) unit not exact on the strip at {a}")
    else:
        n_off += 1
        d = (v - a) / (2j * math.pi)
        if abs(d - round(d.real)) > 1e-6:
            fails.append(f"(2) off-strip error not a multiple of 2πi at {a}")
# (3) and (4)
n_abs = n_changed = 0
for _ in range(200):
    env = F.random_env({"A", "B"}, "positive", rng)
    for X in ["<[<A>]>", "[<A>] [<B>]", "[<A>] [<(<[A]>)>]", "<<[<A>]> [B]>", "[[[oo]]] [[[oo]]]"]:
        try:
            if not F.equal(val(f"(B [({X})])", env), val(f"(B {X})", env)):
                fails.append(f"(3) absorbing position did not absorb: X={X}")
            else:
                n_abs += 1
            if not F.equal(val(f"(B <[({X})]>)", env), val(f"(B <{X}>)", env)):
                fails.append(f"(3) absorbing through an angle did not absorb: X={X}")
            if not F.equal(val(f"[({X})]", env), val(X, env)):
                n_changed += 1
        except (F.Undefined, F.Excluded, OverflowError):
            pass
# (5)
w = val("[[[oo]]] [[[oo]]]")
syntactic_unphased = "<" not in "[[[oo]]]"
if not (syntactic_unphased and abs(w.imag) > math.pi):
    fails.append("(5) the [[[oo]]] witness did not leave the strip")
# (6)
vals = [val("o" * n) for n in range(1, 10)]
if len({round(v.real, 9) for v in vals}) != 9:
    fails.append("(6) piles not separated")
# (7) the enforcement itself: both orientations of the collapse step must be refused by the engine's seam check,
#     and an absorbing position must be admitted
import check as C
import nodes as N_
class _Rep:
    def __init__(self): self.fails = []
    def fail(self, nid, msg): self.fails.append(msg)
    def warn(self, nid, msg): pass
    def ok(self): pass
dummy = N_.Node(id="witness", path="", meta={"domain": "positive"}, sections={}, body="")
r = _Rep(); C.check_seam(F.parse("[([<o>] [<o>])]"), F.parse("[<o>] [<o>]"), dummy, r, 1, rng, 20)
if not r.fails: fails.append("(7) the collapse step [([<o>][<o>])] → [<o>][<o>] was not refused")
r = _Rep(); C.check_seam(F.parse("[<o>] [<o>]"), F.parse("[([<o>] [<o>])]"), dummy, r, 1, rng, 20)
if not r.fails: fails.append("(7) the reversed collapse step [<o>][<o>] → [([<o>][<o>])] was not refused")
r = _Rep(); C.check_seam(F.parse("[([[[oo]]] [[[oo]]])]"), F.parse("[[[oo]]] [[[oo]]]"), dummy, r, 1, rng, 20)
if not r.fails: fails.append("(7) the mirror-free collapse step was not refused")
r = _Rep(); C.check_seam(F.parse("([<A>] [(<[<A>]>)])"), F.parse("([<A>] <[<A>]>)"), dummy, r, 1, rng, 20)
if r.fails: fails.append("(7) an absorbing seam step was refused: " + r.fails[0])
ok = not fails and n_changed > 0 and n_off > 0
print(f"(7) both orientations of the collapse step refused, absorbing step admitted; (1) other rules exact on complex content; (2) unit exact on {n_on} on-strip samples, 2πi-error on {n_off} off-strip samples; (3) {n_abs} absorbing positions absorbed; (4) {n_changed} non-absorbing unit steps changed the value; (5) [[[oo]]] [[[oo]]] has Im = {w.imag:.4f} with no mirror; (6) piles separated")
for f_ in fails[:6]:
    print("  FAIL:", f_)
print("OK" if ok else "FAIL")
sys.exit(0 if ok else 1)
