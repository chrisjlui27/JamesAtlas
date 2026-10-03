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

2026-10-03 (third round): rungs `void`, `N`, `Z`, `mult`, `Q`, `alg`, `C` — 118 laws, 611 engine checks, 6 named gaps (induction, order, lowest terms, a native seam signature, irrationality of √2, non-radical algebraic numbers). Two referee passes per rung. Rung `C` names J and reads what was already writable: `(J) ≐ <o>`, Euler's identity, the phase rule, both halves of the log of a negative, J under an instance as a sign, the period (`(J J) ≐ o`, `(A J J) ≐ (A)`), i as half of J with i² = −1 derived, π as J/i, i^i, the cube roots of −1 and of 1, rectangular and polar forms, (−1)^x as the pure phase, cosine and sine defined from the phase, Euler's formula as a theorem, and James's J-discipline placed *inside* the seam decree (a restriction of his rule 1 and all of rule 2; the decree is strictly stronger, and rule 1 as stated is refuted at `[[oo]]`). Findings so far: Dominion is independent of Involution + Distribution (3-element witness); both undefined forms must be excluded; the seam decree is needed from rung `mult` on, in both orientations, stated in the ℂ reading (`[[[oo]]]` carries iπ with no mirror); the base is not fixed by the axioms; J is the only survivor among the sixteen forms that use each boundary once — but not in J1, where `[()]` is ω. Amendment A2 (pending Lui's confirmation): `guarded_by` now records *every* reliance on the decree — by content (a unit step at depth 0 or under a square) or by position (a seam step inside an instance) — and the status of a guarded theorem stays NATIVE; `NATIVE-BY-DECREE` is reserved for statements that hold because a decree exists. Owed: the Pythagorean identity, ω² + ω + 1 ≐ 0, the conjugate and modulus, the angle-addition formulas, general n-th roots of unity (blocked by the induction gap), a cheaper branch-reading import than ℂ for the decree, an independent J1 derivation of the phase rule, James 1993 Ch. 5 page citations. Next: `J1` — the enriched calculus, where `[()]` is the period ω and the discipline becomes bookkeeping — or the owed rung-C laws first.
