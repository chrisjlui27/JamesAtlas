"""Witness for J1.classical-floor (T-L1: 𝕁₀ = 𝕁₁ + weakening + contraction on receipts) — reads the receipt
prover's ledger (census/j1-ledger.md, written by check.py) and asserts that every graded derivation of the
classical trunk holds in 𝕁₁ strictly, with absorbed receipts, mod Λ, or under a stated guard — i.e. that
forgetting receipts recovers every classical law — except the laws the chart records as *replaced* in 𝕁₁,
which are listed here by name and must be exactly those. Exits 0 iff so.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
REPLACED = {"alg.one-to-power"}   # 1^B: the receptacle replaces it (the log of one under a square has receipt ω)

path = os.path.join(ROOT, "census", "j1-ledger.md")
if not os.path.exists(path):
    print("no ledger yet (run tools/check.py first)")
    sys.exit(1)
rows = []
for line in open(path):
    if line.startswith("| `"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append((cells[0].strip("`"), cells[1], cells[2]))
bad = []
counts = {}
for nid, computed, hand in rows:
    if nid.startswith("J1."):
        continue
    counts[computed] = counts.get(computed, 0) + 1
    if computed == "fails" and nid not in REPLACED:
        bad.append((nid, computed))
    if nid in REPLACED and computed != "fails":
        bad.append((nid, "expected to fail, graded " + computed))
if bad or not rows:
    print("FAIL", bad or "empty ledger")
    sys.exit(1)
print(f"ok: {len(rows)} trunk derivations graded in 𝕁₁ — {counts}; the only law that fails is replaced: {sorted(REPLACED)}")
