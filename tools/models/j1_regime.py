"""Witness for J1.regime-split — where the lattice enters. A form built from ( ), [ ], positive variables and
piles, with (i) no angle boundary, (ii) no count of one — no `[()]`, which is ω — and (iii) no square directly
inside a square, has a void receipt at every unit redex [(X)] at every generic point of the positive domain: its
content is a sum of positive reals. Each of the three doors admits the lattice: [(J J J)] (an angle), [(ω ω)]
(the count of one), and [([[[oo]]] [[[oo]]])] (a square inside a square: ln ln 2 is negative, so its log carries
iπ with no mirror in sight — the signature failure of mult.seam-signature). The exceptional points of the
reading open the second door by value: at B = 1 the square `[B]` reads ω, and `[(A [B])]` has receipt −ω.

The receipt of a unit redex is value([(X)]) − value(X) in units of ω (SPEC §5.5), read in the 𝕁₁ reading: the
log of exactly one is 2πi, every other log principal.

Exits 0 iff 20 000 random forms of the class have only void receipts at generic points, the three doors each
show a non-void receipt with the signs stated on the card, and the exceptional sweep finds the door by value.
"""
import os, sys, cmath, math, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import forms as F

F.OMEGA = 2j * math.pi
rng = random.Random(7)


def random_form(depth=0, in_square=False):
    """A random form of the class: no angle, no [()], no square directly inside a square. The wrapper is chosen
    first, so that squares appear at every depth — only never directly inside another square. Inside a square
    the only wrappers are an instance or none: a unit redex `[( )]` or a square there would put a square directly
    inside a square; a bare juxtaposition stays inside the square, so its parts are generated in the square too."""
    k = rng.random()
    if depth > 3 or k < 0.3:
        return rng.choice(["A", "B", "oo", "ooo", "(A)", "(A B)"] + ([] if in_square else ["[A]", "[oo]", "[A B]"]))
    wrapper = rng.choice(["round", "none", "unit", "square"] if not in_square else ["round", "none"])
    n = rng.randint(1, 3)
    inside = (wrapper == "square") or (wrapper == "none" and in_square)
    parts = [random_form(depth + 1, in_square=inside) for _ in range(n)]
    inner = " ".join(parts)
    if wrapper == "round":
        return "(" + inner + ")"
    if wrapper == "unit":
        return "[(" + inner + ")]"          # a unit redex: the thing being measured
    if wrapper == "square":
        return "[" + inner + "]"
    return inner


def nested_square(f, in_square=False):
    """Does the form put a square directly inside a square? (A check on the generator, not on the class.)"""
    for ch in f:
        if ch[0] == F.VAR:
            continue
        if ch[0] == F.SQUARE and in_square:
            return True
        if nested_square(ch[1], in_square=(ch[0] == F.SQUARE)):
            return True
    return False


def windings(form, env):
    """Receipts of every unit redex [(X)] inside the form, in the 𝕁₁ reading (SPEC §5.5): the value of [(X)]
    minus the value of X, in units of ω — the lattice element the unit step forgets."""
    out = []
    def walk(f):
        for ch in f:
            if ch[0] == F.VAR:
                continue
            if ch[0] == F.SQUARE and len(ch[1]) == 1 and ch[1][0][0] == F.ROUND:
                x = ch[1][0][1]
                try:
                    a = F.evaluate(x, env)
                    u = F.evaluate((ch,), env)
                except Exception:
                    a = u = None
                if a is not None and u is not None and a is not F.BH and u is not F.BH:
                    out.append(round(((u - a) / (2j * math.pi)).real))
            walk(ch[1])
    walk(form)
    return out


forms, bad, seen, malformed = [], [], 0, 0
for _ in range(20000):
    s = random_form()
    try:
        f = F.parse(s)
    except Exception:
        continue
    if nested_square(f) or "[()]" in s.replace(" ", ""):
        malformed += 1
        continue
    forms.append((s, f))
    env = {"A": math.exp(rng.uniform(-3, 3)), "B": math.exp(rng.uniform(-3, 3))}
    try:
        ws = windings(f, env)
    except Exception:
        continue
    seen += len(ws)
    if any(w != 0 for w in ws):
        bad.append((s, ws, env))

# the exceptional points: a variable at exactly one makes its square read ω — the count-of-one door, by value
exceptional = []
for s, f in forms:
    for env in ({"A": 1.0, "B": 2.0}, {"A": 2.0, "B": 1.0}, {"A": 1.0, "B": 1.0}):
        try:
            ws = windings(f, env)
        except Exception:
            continue
        if any(w != 0 for w in ws):
            exceptional.append((s, ws, env))
            break
door_by_value = windings(F.parse("[(A [B])]"), {"A": 2.0, "B": 1.0})

doors = {"angle": windings(F.parse("[(J J J)]"), {}), "count of one": windings(F.parse("[(ω ω)]"), {}),
         "square in square": windings(F.parse("[([[[oo]]] [[[oo]]])]"), {})}
expected = {"angle": [-1], "count of one": [-1, 1, 1], "square in square": [-1]}
if bad or seen < 1000 or malformed or doors != expected or door_by_value != [-1] or not exceptional:
    print("FAIL", bad[:3], seen, malformed, doors, door_by_value, exceptional[:2])
    sys.exit(1)
print(f"ok: {seen} unit redexes in {len(forms)} forms of the class, all with void receipts at generic points; "
      f"the three doors: {doors} (outer receipt first, then the two [()] inside); "
      f"the door by value: [(A [B])] at B = 1 has receipt {door_by_value}, and {len(exceptional)} of the {len(forms)} "
      f"forms have a non-void receipt at an exceptional point (A = 1 or B = 1)")
