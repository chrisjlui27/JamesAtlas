# The Boundary Chart — notes for a Claude Code session

This repository is Lui's Boundary Chart: James boundary arithmetic built up one law per node, from `void` to the quaternions, with an engine that checks every derivation. Read these before doing anything:

1. `SPEC.md` — the rules, in force (v2.1). §11.2 is the protocol for adding a rung; §11.3 for adding a setting; §11.4 for iterating the spec; §14 says what is decided, forked and deferred.
2. `LEGISLATION.md` — the decisions, numbered. **Never edit an item; change a decision only by adding a dated amendment under its number.** Decisions are Lui's: a session proposes, implements as proposed, marks it pending, and he confirms by number.
3. `ROADMAP.md` §4 — what is next (`analysis`, LEGISLATION 33(e)); §6–§7 — how the last two rungs were built.
4. `README.md` — the layout and "adding a law".
5. `docs/plans/H.md` and `docs/referee/H.md` — a worked example of the protocol: the plan a rung starts from, and the referee report it ends with.

## Layout

- `nodes/*.md` — one law per node, Markdown with YAML front matter (schema in SPEC §3). `uses:` must be exactly the ids cited in the Derivation; `owed:` is a list of `YYYY-MM-DD: what is owed` strings.
- `tools/check.py` — the engine. The chart is released only at **0 failures**. `python3 tools/check.py` runs everything (minutes); `python3 tools/check.py --only H.` runs one rung.
- `tools/build.py` — writes `site/index.html`, the chart as a single page.
- `tools/models/*.py` — witnesses for meta theorems; each exits 0 iff its checks hold.
- `census/*.md` — ledgers (the trunk read in 𝕁₁, at the places, in ℍ). **Computed, never hand-edited**; the ACCEPT rule is SPEC §8.
- `concepts/`, `references/` — the concept nodes and the source texts (James 1993 and the reports).
- `docs/plans/`, `docs/referee/` — one file per rung.
- `app/` — James Atlas, the Windows desktop app over the chart (Electron + a Python bridge that imports `tools/`). It is not part of the SPEC; its own README says how it is built and tested (`npm test`, end-to-end on a scratch copy of the chart). If you change the signatures of `build.render_node`, `licences.rules_for`, `prover.rewrite_all` or `check.main`, run its tests too.

Python 3, standard library only. No network needed.

## How a rung is added (SPEC §11.2, in short)

plan (`docs/plans/<rung>.md`) → nodes and any engine work → full check at 0 failures → an independent referee pass (two passes if the rung adds a boundary), findings graded BLOCKER / MAJOR / MINOR, blockers and majors repaired before the commit, minors repaired or recorded as `owed:` → documents (the SPEC increment with new rules only; the LEGISLATION item, pending; ROADMAP "as built" and "next"; README Status, latest first) → release (check, build, commit, zip).

A new setting comes with a `Reading`, a ledger and computed cells (SPEC §11.3). Equality symbols are earned by the tape, never typed (SPEC §2.1). A conditional law carries the bare equation in `law:` and its premise in `units:`.

## Working with Lui

- He confirms decisions by number ("32(e) confirmed"), pushes to GitHub himself, and walks the chart. A session commits; it does not push unless told to.
- Keep explanations accessible — say what a result means before how it was got; the mathematics stays rigorous, the prose should not need the jargon to be followed.
- His typographic notation, when writing to him: *italics* for a reduction (emptying), ***bold-italic*** for something emergent, **bold** for something settled, ~~strikethrough~~ for an idea marked wrong, "scare quotes" for a term held at arm's length.
