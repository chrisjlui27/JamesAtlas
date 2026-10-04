"""Witness for J1.regime-split — where the lattice enters. A form built from ( ), [ ], positive variables and
piles, with (i) no angle boundary, (ii) no count of one — no `[()]`, which is ω — and (iii) no square directly
inside a square, has a void receipt at every unit redex [(X)]: its content is a sum of positive reals. Each of
the three doors admits the lattice: [(J J)] (an angle), [(ω ω)] (the count of one), and
[([[[oo]]] [[[oo]]])] (a square inside a square: ln ln 2 is negative, so its log carries iπ with no mirror in
sight — the signature failure of mult.seam-signature). Exits 0 iff 3000 random forms of the class have only
void receipts and the three doors each show a non-void one.
"""
import os, sys, cmath, math, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import forms as F

F.OMEGA = 2j * math.pi
rng = random.Random(7)


def random_form(depth=0, in_square=False):
    """A random form of the class: no angle, no [()], no square directly inside a square."""
    k = rng.random()
    if depth > 3 or k < 0.3:
        return rng.choice(["A", "B", "oo", "ooo", "(A)", "(A B)"] + ([] if in_square else ["[A]", "[oo]", "[A B]"]))
    n = rng.randint(1, 3)
    parts = [random_form(depth + 1, in_square=True) for _ in range(n)]
    inner = " ".join(parts)
    choices = ["(" + inner + ")", inner]
    if not in_square:
        choices.append("[(" + inner + ")]")          # a unit redex: the thing being measured
        if all(not p.startswith("[") for p in parts):
            choices.append("[" + inner + "]")
    return rng.choice(choices)


def windings(form, env):
    """Windings of the contents of every unit redex [(X)] inside the form."""
    out = []
    def walk(f):
        for ch in f:
            if ch[0] == F.VAR:
                continue
            if ch[0] == F.SQUARE and len(ch[1]) == 1 and ch[1][0][0] == F.ROUND:
                x = ch[1][0][1]
                if not x:
                    out.append(1)  # the unit on void content: the receipt is ω itself (LEGISLATION 30b)
                    walk(ch[1])
                    continue
                try:
                    a = F.evaluate(x, env)
                except Exception:
                    a = None
                if a is not None and a is not F.BH and a.real < 700:
                    w = cmath.exp(a)
                    if w != 0:
                        out.append(round(((a - cmath.log(w)) / (2j * math.pi)).real))
            walk(ch[1])
    walk(form)
    return out


bad, seen = [], 0
for _ in range(20000):
    s = random_form()
    try:
        f = F.parse(s)
    except Exception:
        continue
    env = {"A": math.exp(rng.uniform(-3, 3)), "B": math.exp(rng.uniform(-3, 3))}
    try:
        ws = windings(f, env)
    except Exception:
        continue
    seen += len(ws)
    if any(w != 0 for w in ws):
        bad.append((s, ws, env))
doors = {"angle": windings(F.parse("[(J J)]"), {}), "count of one": windings(F.parse("[(ω ω)]"), {}),
         "square in square": windings(F.parse("[([[[oo]]] [[[oo]]])]"), {})}
if bad or seen < 1000 or any(not any(w != 0 for w in ws) for ws in doors.values()):
    print("FAIL", bad[:3], seen, doors)
    sys.exit(1)
print(f"ok: {seen} unit redexes in 20000 forms of the class, all with void receipts; the three doors: {doors}")
