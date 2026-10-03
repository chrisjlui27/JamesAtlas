"""Witness for N.freeness (fragment): in the fragment {void, o, juxtaposition} there are no rewrite
rules, so ≐ is multiset identity; the canonical forms of piles of different counts differ, and no
pile is the void. Enumerates piles up to count 12 and checks pairwise distinctness of canonical strings."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import forms as F

piles = [F.parse("o" * n) for n in range(0, 13)]
canon = [F.to_string(p) for p in piles]
ok = len(set(canon)) == len(canon) and all(F.size(p) == n for n, p in enumerate(piles)) and piles[0] == ()
print("piles 0..12 pairwise distinct as canonical forms:", ok)
print("OK" if ok else "FAIL")
sys.exit(0 if ok else 1)
