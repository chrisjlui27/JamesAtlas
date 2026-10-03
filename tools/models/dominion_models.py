"""Witness for mult.dominion-independence.

Enumerate commutative monoids (M, +, 0) of order 2..4 together with a bijection e : M -> M
(the round boundary; l = e^-1 is the square boundary).  Involution holds automatically.
Keep the structures in which Distribution  e(a + l(b+c)) == e(a + l b) + e(a + l c)  holds
for all a, b, c.  In each, test Dominion  l(0) + a == l(0)  and the theorem (□) ≐ void,
i.e. e(l(0)) == 0.

Exit status 0 iff (i) a model of Involution+Distribution in which Dominion FAILS and □ ≠ void
exists (so Dominion is not derivable from those two axioms), and (ii) (□) ≐ void holds in
every model found (as the derivation in mult.hole-instance predicts).
"""
import itertools
import sys


def comm_monoids(n):
    pairs = [(i, j) for i in range(1, n) for j in range(i, n)]
    for vals in itertools.product(range(n), repeat=len(pairs)):
        t = [[0] * n for _ in range(n)]
        for i in range(n):
            t[0][i] = t[i][0] = i
        for (i, j), v in zip(pairs, vals):
            t[i][j] = t[j][i] = v
        if all(t[t[a][b]][c] == t[a][t[b][c]] for a in range(n) for b in range(n) for c in range(n)):
            yield t


def main():
    witness = None
    hole_instance_everywhere = True
    report = []
    for n in (2, 3, 4):
        models = fails = 0
        for t in comm_monoids(n):
            for e in itertools.permutations(range(n)):
                l = [0] * n
                for i, v in enumerate(e):
                    l[v] = i
                ok = all(
                    e[t[a][l[t[b][c]]]] == t[e[t[a][l[b]]]][e[t[a][l[c]]]]
                    for a in range(n) for b in range(n) for c in range(n)
                )
                if not ok:
                    continue
                models += 1
                box = l[0]
                if e[box] != 0:
                    hole_instance_everywhere = False
                if not all(t[box][a] == box for a in range(n)):
                    fails += 1
                    if witness is None and box != 0:
                        witness = (n, t, list(e), box)
        report.append((n, models, fails))
    for n, m, f in report:
        print(f"order {n}: {m} models of Involution+Distribution, Dominion fails in {f}")
    print("(□) ≐ void holds in every model:", hole_instance_everywhere)
    if witness:
        n, t, e, box = witness
        print(f"witness (order {n}): + table {t}; e = {e}; □ = l(0) = {box} ≠ 0; (□) = e(□) = {e[box]}")
        bad = [a for a in range(n) if t[box][a] != box]
        print(f"  Dominion fails at A = {bad}: □ + {bad[0]} = {t[box][bad[0]]} ≠ {box}")
        print("RESULT: Dominion is INDEPENDENT of Involution + Distribution.")
    ok = witness is not None and hole_instance_everywhere
    print("OK" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
