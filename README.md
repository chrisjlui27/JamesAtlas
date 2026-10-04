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

2026-10-03 (fourth round): rungs `void`, `N`, `Z`, `mult`, `Q`, `alg`, `C` — 136 laws, 859 engine checks, 6 named gaps (induction, order, lowest terms, a native seam signature, irrationality of √2, non-radical algebraic numbers). Rung `C` is complete as the classical James algebra — relative to the chart's paraphrase of the 1993 thesis, Chapters 3–5 (the thesis is not in the repository and its page citations are owed) — plus the standard toolkit of a first course in complex numbers, four referee passes applied: J and the sixteen-form uniqueness census; `(J) ≐ <o>`, Euler's identity, the phase rule, both halves of the log of a negative, J under an instance as a sign, the period laws; i as half of J with i² = −1 derived, π = J/i, i^i, √(−a) = i√a, the cube roots of −1 and of 1 with 1 + ω + ω² = 0; rectangular and polar forms, the turn of a sum, the reverse turn, the polar product, (−1)^x as the pure phase; conjugate, modulus, z z̄ = a² + b², the rectangular product and quotient; cosine and sine defined from the phase, their parity, Euler's formula and its conjugate, the Pythagorean identity, both addition formulas, |r e^{iπt}| = r, De Moivre at n = 3; and James's J-discipline placed *inside* the seam decree (a restriction of his rule 1 and all of rule 2 — the decree is strictly stronger, and rule 1 as stated is refuted at `[[oo]]`). Amendment A2 (pending Lui's confirmation): `guarded_by` records every reliance on the decree, by content or by position, and a guarded theorem stays NATIVE. Still owed on this rung, none blocked except as marked: general n-th roots of unity and general De Moivre (induction gap); the complex logarithm of a turn as a law with a bounded variable (the domain vocabulary — see `C.reverse-turn`, Notes); conj(zw) = conj(z) conj(w) and |zw| = |z||w| (routine four-variable theorems); √(a + bi) and the quadratic formula over ℂ (a sign choice: the order gap); an independent J1 derivation of the phase rule; a cheaper branch-reading import than ℂ for the decree; James 1993 Ch. 5 page citations. Next: `J1`, the enriched calculus, where `[()]` is the period ω and the discipline becomes bookkeeping.
