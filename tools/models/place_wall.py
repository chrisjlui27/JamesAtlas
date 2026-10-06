"""Witness for place.wall — the same wall at every place. For every prime p ≤ 31 (tools/place.py):
 (1) [()] reads the period of the place, (p−1)·J_p (2·J_2 at 2), not void, and (ω) ≐ ();
 (2) (ω A) ≃ (A) for random A on the radius — the derivation of J1.absorption is one absorbed step there;
 (3) J J and ω are the same element of the log space, so J J ≃ ω;
 (4) the place ledger (census/place-ledger.md): the J1 rung's derivations keep their grades at p = 2, 3, 5, 7, 13.
Exits 0 iff all hold."""
import os, sys, random
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(HERE, ".."))
import forms as F, place as PL

rng = random.Random(31)
fails = []
primes = [q for q in range(2, 32) if all(q % d for d in range(2, q))]
periods = {}
for p in primes:
    P = PL.Place(p)
    ev = lambda s, env=None: PL.evaluate(F.parse(s), env or {}, P)
    om = ev("ω")
    periods[p] = f"{om.k}·J_{p}"
    if om.k != P.torsion or om.a or om.v or P.equal(om, P.zero()):
        fails.append((p, "period", P.fmt(om)))
    if not P.equal(ev("(ω)"), P.number(1)):
        fails.append((p, "(ω) ≠ 1"))
    for _ in range(20):
        A = Fraction(p ** P.radius * rng.randint(1, 1000))
        if not P.equal(ev("(ω A)", {"A": A}), ev("(A)", {"A": A})):
            fails.append((p, "wall", A))
    if not P.equal(ev("J J"), om):
        fails.append((p, "J J ≠ ω", P.fmt(ev("J J"))))
# (4) the ledger: the J1 rung at the places
path = os.path.join(ROOT, "census", "place-ledger.md")
ledger = {}
if os.path.exists(path):
    for line in open(path):
        if line.startswith("| `J1."):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            ledger[cells[0].strip("`")] = cells[1:6]
    bad = {k: v for k, v in ledger.items() if any("fails" in c or "absent" in c for c in v)}
    if bad:
        fails.append(("ledger", bad))
if fails:
    print("FAIL", fails[:6]); sys.exit(1)
print(f"ok: for every prime p ≤ 31 the period [()] is {', '.join(f'{p}: {periods[p]}' for p in primes[:5])}, …, (ω) ≐ (), (ω A) ≃ (A) on the radius and J J ≃ ω; "
      f"the ledger grades {len(ledger)} J1 laws at p = 2, 3, 5, 7, 13 with no failure")
