# boundary-chart

A step-by-step exposition of mathematics in James boundary arithmetic, from the void toward F₁, as a chart of laws. One law per file; back-links are the rules each derivation cites; everything else is computed.

- `SPEC.md` — the data model, the node format, links, settings and readings, status, price, gaps, scope, verification, build plan.
- `LEGISLATION.md` — the binding decisions, numbered.
- `ROADMAP.md` — the path from the classical algebra to the F₁ / motivic / Berkovich pictures, and the proposed rung order (pending confirmation).
- `references/` — James 1993, the ground truth for the classical setting.
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
5. Run `tools/check.py`. A theorem becomes `verified: engine` only when it passes — every step value-equal in ℂ *and* licensed by the rule it cites (the derivation checker, `tools/prover.py`; `python3 tools/licences.py --verbose` shows which rule, in which orientation, at which position, took each row to the next).
6. Run `tools/build.py` and look at the card.
7. A law over every n is a `type: schema` node (SPEC §2.7): write the law and the form cells as templates (`A^{n}`, `o^{2k}`, `Σ{j=1..n: …}`), give `schema_range:` (e.g. `n=2..8` or `n=1..6; k=1..n`), head the base-case table `| form (n = 1) | rule | note |` (the base must be the first value of the range), and let the step's `hypothesis` row cite `[[N.induction]]`. The engine checks the base at its value, the step at every other value in the range, and that the hypothesis row is the law at a smaller parameter; the status is `NATIVE-BY-SCHEMA`.

## Status

2026-10-04, later (the derivation checker): every one of the 951 derivation rows on the chart is now *licensed* — `tools/prover.py` reproduces each step from the previous row by the rule the row cites, as a rewrite in either orientation at any position (associative-commutative matching over the multiset of boundaries), and `check.py` fails a node whose step it cannot. The engine's standing caveat ("it does not check that the cited rule licenses the step") is retired. Running it over the chart found twenty-one rows that cited `mult.unit-law` for a step that law does not state — the log of one, `[o] ≐ void` — and five rows that cited a numeral instance (`mult.product-of-numerals`, `Z.normal-form`, `mult.cardinality`) for a different numeral; the first became a node of its own, `mult.log-of-one` (146 laws), the second now cite the Distribution, log-of-one and counit steps they actually take. 2750 engine checks. LEGISLATION 30 settles the shape of `J1`: total space, ω ↦ 2πi, the receipt prover now (this checker is its strict half), stratified annihilation decided in-program, the ψ-wall at height one, the pole polarity-dependent.

2026-10-04 (rung `schema`, one referee pass applied): 145 laws, 1796 engine checks (schemas are checked once per instance; the endpoint check is now syntactic for every theorem, and a `hypothesis` row is verified to be the law at a smaller parameter). Amendments A1 and A2 confirmed and the rung order decided (LEGISLATION 27–29: `void N Z mult Q alg C` · `schema` · `J1` · `place` · `H` · `analysis` · `J2` · `logic` `struct` · `F1`; `O`, `S` a branch). The seam decree's ℂ import is marked provisional until `J1`. New: the `schema` node type (SPEC §2.7) — a law with a count parameter, written as a template, instantiated by the engine over a declared range, derived by an induction step in James's style whose hypothesis row cites the induction gap — and seven schema laws: cardinality (James's Theorem 1, p. 27, with his induction), powers, whole turns, the n-th roots of unity and of negation, De Moivre, and the vanishing sum of the n-th roots. The hand-written instances — `mult.cardinality` (n = 2), `C.cube-root-of-unity`, `C.cube-root-of-negation`, `C.de-moivre` (n = 3) and `C.omega-sum` — stay on the chart as the cases the reader meets first and point at their schemas; the thirteen older nodes that state one value of a family are now `kind: instance` (formerly `kind: schema`, a name the node type has taken). What a schema does **not** give: the passage to all n, which stays a priced gap (`N.induction`), and the claim that the n-th roots found are *all* of them (`N.order`). Next: `J1`.

2026-10-03 (fifth round, against the thesis): rungs `void`, `N`, `Z`, `mult`, `Q`, `alg`, `C` — 138 laws, 907 engine checks, 6 named gaps (induction, order, lowest terms, a native seam signature, irrationality of √2, non-radical algebraic numbers). James's thesis is now in `references/` and every citation has been checked against it: J and the J-discipline are Chapter 6 ("Phase", pp. 43–50), not 4–5; the crack has an address — the last step of James's proof of Theorem 1, *phase independence* `[<(A)>] ≐ A J` (p. 44), which is the unit step at depth 0 on `A J`, and his Theorem 2 `J J ≐ void` is Theorem 1 at A = J (p. 45); his two constraints (p. 47) are quoted verbatim and he himself calls them "not exhaustive"; `<□>` is excluded by his rule 3 (p. 31), `[□]` is his "beyond scope" and the chart's exclusion; his proof of Dominion rests on "collection is assumed additive" (p. 26), which is exactly what the 3-element independence model violates; his trigonometry is in radians (the chart counts half-turns); his π is `(J [J] ([J] <[oo]>))`, "the radian unit … devoid of numerical value". New this round: `C.phase-independence` (James's Theorem 1 with his proof, row for row, guarded on the last row) and `C.quadratic-formula` (Appendix B.5 as a factorization identity — the ± is a mirror, so no order gap is involved). Rung `C` is complete as the classical James algebra of the thesis plus the standard toolkit of a first course in complex numbers, five referee passes applied. Amendments A1 and A2 confirmed 2026-10-03 (LEGISLATION 27–28). Still owed on this rung (general n-th roots of unity and general De Moivre moved to rung `schema`, 2026-10-04): the complex logarithm of a turn as a law with a bounded variable (domain vocabulary — `C.reverse-turn`, Notes); conj(zw), |zw|, the equality of James's π with the chart's as rows; the base boundary `{A} ≐ ([b][A])` and James's number formats (A.3, B.1 — place value with carry) as `N`/`mult` nodes; an independent J1 derivation of the phase rule; a cheaper branch-reading import than ℂ. Next: `J1`.
