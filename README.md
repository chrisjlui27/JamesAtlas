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

Pilot (2026-10-03): rungs `void`, `N`, `Z`, and the opening of `mult` — 39 laws, 92 derivation steps checked, 2 named gaps (induction, order), one small James-specific fact (Dominion is independent of Involution + Distribution; a 3-element witness), one load-bearing decree made explicit by the referee pass (both undefined forms `<□>` and `[□]` must be excluded, or the calculus collapses). Next: the `Q` rung, then `alg`, then `C` — see SPEC §13.
