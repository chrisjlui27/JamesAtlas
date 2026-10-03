# Open forms

Forms the census (`size-le-3.md`) classifies as `new` or `undefined` that no pilot node reads yet. Each line names the rung where the form is expected to be read, or marks it a form-without-reading gap. `tools/check.py` fails if a `new`/`undefined` census form is neither assigned to a node nor listed here.

| form | value | expected rung / node | note |
|---|---|---|---|
| `(o)` | e | `alg` — the base: e is simply `(o)` (James) | the first transcendental the calculus writes; whether the base is *constrained* is the exp–log completeness question |
| `((o))` | e^e | `analysis` | iterated exponential |
| `(o o)` | e² | `alg` — a power of the base | — |
| `(o) o` | e + 1 | `alg` | the first *sum* of a transcendental and a numeral; `o (J)` = 1 + e^{iπ} = 0 is its famous sibling at rung `C` |
| `(<o>)` | 1/e | `Q` — reciprocal: `(<[A]>)` with A = `(o)`, i.e. `(<o>)` | compare `<(o)>` below: *depth order matters* (JH Depth Principle) |
| `<(o)>` | −e | `Z` × `alg` — the mirror of the base | — |
| `[o o]` | ln 2 | `analysis` — the first logarithm of a pile that is not a pile | Lui's exp–log thread: logs of sums inside radical towers; known since Chow 1999 (EL numbers) in the literature |
| `J` = `[<o>]` | iπ | `C` — the phase element, James's unique stable three-boundary form | the hinge of the whole program; not in the pilot |
| `[□]` and every form containing it | undefined | **form-without-reading gap** | James left `[[ ]]` undefined; Bricken (Iconic Arithmetic) reads it as complex infinity; Lui's open question (p-adic-wall, 2026-09) is whether `[ ]` can be split into ±∞ and what that does to `<[ ]>`. Eleven census forms of size ≤ 3 contain it: `[□]`, `o [□]`, `([□])`, `<> [□]`, `<[□]>`, `[o □]`, `[<> □]`, `[[<>]]`, `[[□]]`, `[□ □]`, `[□] □` — all reduce to the one question |
