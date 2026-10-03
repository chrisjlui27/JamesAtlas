"""Witness for Q.cross-multiplication: for random numerals a, b, c, d (1..6) the two sides of
  ([a] <[b]>) ≐ ([c] <[d]>)   iff   ([a][d]) ≐ ([c][b])
agree — both equalities are decided in the ℂ reading and compared; and both directions' derivation
shapes are instantiated and checked row by row with the engine (the (⇒) route: two unit steps and an
Inversion; the (⇐) route: cancel-common-factor on each side)."""
import os, sys, random, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import forms as F

def pile(n): return "o" * n
bad = 0; total = 0; rows_checked = 0
for a, b, c, d in itertools.product(range(1, 7), repeat=4):
    total += 1
    lhs = F.evaluate(F.parse(f"([{pile(a)}] <[{pile(b)}]>)")); rhs = F.evaluate(F.parse(f"([{pile(c)}] <[{pile(d)}]>)"))
    l2 = F.evaluate(F.parse(f"([{pile(a)}] [{pile(d)}])")); r2 = F.evaluate(F.parse(f"([{pile(c)}] [{pile(b)}])"))
    if F.equal(lhs, rhs) != F.equal(l2, r2):
        bad += 1
    # (⇒) route instantiated: ([([a]<[b]>)] [([b][d])]) → ([a] <[b]> [b] [d]) → ([a] [d])
    chain = [f"([([{pile(a)}] <[{pile(b)}]>)] [([{pile(b)}] [{pile(d)}])])", f"([{pile(a)}] <[{pile(b)}]> [{pile(b)}] [{pile(d)}])", f"([{pile(a)}] [{pile(d)}])"]
    vals = [F.evaluate(F.parse(x)) for x in chain]
    if not (F.equal(vals[0], vals[1]) and F.equal(vals[1], vals[2])):
        bad += 1
    rows_checked += 2
    # (⇐) route instantiated: ([([a][d])] <[([b][d])]>) → ([a] <[b]>)
    v1 = F.evaluate(F.parse(f"([([{pile(a)}] [{pile(d)}])] <[([{pile(b)}] [{pile(d)}])]>)")); v2 = F.evaluate(F.parse(f"([{pile(a)}] <[{pile(b)}]>)"))
    if not F.equal(v1, v2):
        bad += 1
    rows_checked += 1
ok = bad == 0
print(f"{total} numeral quadruples: iff agrees in all, {rows_checked} derivation rows checked, {bad} failures")
print("OK" if ok else "FAIL")
sys.exit(0 if ok else 1)
