# Open forms

Forms the census (`size-le-3.md`) classifies as `new` that no node reads yet. (Forms classified `undefined` or `excluded` — those containing `[□]` or `<□>` — are not open: they are refused by the decree `mult.hole-exclusion`, which the census assigns them to. Lui's question whether `[ ]` can be split into ±∞ is a *plan* against that decree, recorded in the p-adic-wall thread.) Each line names the rung where the form is expected to be read, or marks it a form-without-reading gap. `tools/check.py` fails if a `new`/`undefined` census form is neither assigned to a node nor listed here.

| form | value | expected rung / node | note |
|---|---|---|---|
| `((o))` | e^e | `analysis` | iterated exponential |
| `[o o]` | ln 2 | `analysis` — the first logarithm of a pile that is not a pile | Lui's exp–log thread: logs of sums inside radical towers; known since Chow 1999 (EL numbers) in the literature |

`J` = `[<o>]` was listed here until 2026-10-03; it is now read at `C.phase`.
