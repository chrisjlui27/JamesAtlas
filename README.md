# boundary-chart

A step-by-step exposition of mathematics in James boundary arithmetic, from the void toward F₁, as a chart of laws. One law per file; back-links are the rules each derivation cites; everything else is computed.

- `SPEC.md` — the data model, the node format, links, settings and readings, status, price, gaps, scope, verification, build plan.
- `LEGISLATION.md` — the binding decisions, numbered.
- `nodes/<rung>.<slug>.md` — one law each. Open `nodes/` as an Obsidian vault to get the graph view.
- `concepts/<slug>.md` — one paragraph per concept (optional; the index is computed from nodes' `concepts:` fields).
- `census/` — the small-form census (generated) and the hand-kept list of open forms.
- `tools/` — `check.py` (the engine), `build.py` (the site), `census.py`, `forms.py` (parser + ℂ evaluator), `nodes.py` (file parser), `models/` (witnesses for meta theorems).
- `site/index.html` — generated; the pilot chart.

## Use

```
python3 tools/check.py      # must exit 0 before any node is marked `verified: engine`
python3 tools/build.py      # regenerates site/index.html
python3 tools/census.py     # regenerates census/size-le-3.md and lists unassigned forms
```

No dependencies beyond Python 3.

## Adding a law

1. Copy the nearest node file; give it the next free `order` in its rung (spaced by 10) and an `id` of the form `<rung>.<slug>` that matches the filename.
2. Write the `law:` in canonical `( ) [ ] < >` strings (sugar `o`, `□`, `J`, `void` is accepted) and the `units:` in standard notation; add a `gloss_check:` Python expression where the ℂ value can be stated.
3. Write the Given–Rule derivation as a table whose first column is a form and whose second column cites the licensing node as `[[id]]` (or `given`, `medium`, `congruence`, `substitution`, `definition`, `name` for a standard-notation naming row). Set `uses:` to exactly the ids cited anywhere in the Derivation section — the checker enforces it.
4. Fill the `holds:` (per setting) and `readings:` (per reading) tables; `untested` is a legal cell, a blank is not.
5. Run `tools/check.py`. A theorem becomes `verified: engine` only when it passes.
6. Run `tools/build.py` and look at the card.

## Status

2026-10-03 (fifth round, against the thesis): rungs `void`, `N`, `Z`, `mult`, `Q`, `alg`, `C` — 138 laws, 907 engine checks, 6 named gaps (induction, order, lowest terms, a native seam signature, irrationality of √2, non-radical algebraic numbers). James's thesis is now in `references/` and every citation has been checked against it: J and the J-discipline are Chapter 6 ("Phase", pp. 43–50), not 4–5; the crack has an address — the last step of James's proof of Theorem 1, *phase independence* `[<(A)>] ≐ A J` (p. 44), which is the unit step at depth 0 on `A J`, and his Theorem 2 `J J ≐ void` is Theorem 1 at A = J (p. 45); his two constraints (p. 47) are quoted verbatim and he himself calls them "not exhaustive"; `<□>` is excluded by his rule 3 (p. 31), `[□]` is his "beyond scope" and the chart's exclusion; his proof of Dominion rests on "collection is assumed additive" (p. 26), which is exactly what the 3-element independence model violates; his trigonometry is in radians (the chart counts half-turns); his π is `(J [J] ([J] <[oo]>))`, "the radian unit … devoid of numerical value". New this round: `C.phase-independence` (James's Theorem 1 with his proof, row for row, guarded on the last row) and `C.quadratic-formula` (Appendix B.5 as a factorization identity — the ± is a mirror, so no order gap is involved). Rung `C` is complete as the classical James algebra of the thesis plus the standard toolkit of a first course in complex numbers, five referee passes applied. Amendments A1 and A2 pending Lui's confirmation. Still owed on this rung: general n-th roots of unity and general De Moivre (induction gap); the complex logarithm of a turn as a law with a bounded variable (domain vocabulary — `C.reverse-turn`, Notes); conj(zw), |zw|, the equality of James's π with the chart's as rows; the base boundary `{A} ≐ ([b][A])` and James's number formats (A.3, B.1 — place value with carry) as `N`/`mult` nodes; an independent J1 derivation of the phase rule; a cheaper branch-reading import than ℂ. Next: `J1`.
