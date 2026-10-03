---
id: N.order
title: Order — m < n
type: gap
level: meta
kind: concept
rung: N
order: 190
setting: classical
equality: "≐"
domain: natural
law: "GAP — 'oo < ooo' is not a form; order is a predicate on normal forms, not an equation"
units: "m < n"
holds:
  classical: fails
  J1: fails
  JH: fails
  JO: fails
  JP: fails
readings:
  C: PARTIAL
  finset: PARTIAL
  lambda: untested
  CC: untested
  logic: ABSENT
status: ABSENT
verified: hand
known_since: "ancient (order); the boundary-analysis thread 2026-09/10 found order native on piles up to a choice of base"
entered: 2026-10-03
guide: need-led
band: "1–2"
uses: []
see_also: [Z.normal-form, N.induction]
aliases: [inequality, comparison, less-than, positivity]
concepts: [order]
understood: partial
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| none | — | m < n |

The calculus has one relation, ≐. "Less than" is not an equation. On piles it has an obvious shadow — `oo < ooo` because `ooo ≐ oo o` with a non-void remainder — and after the angle boundary a cleaner one: `m < n` iff the normal form of `n <m>` is a positive pile ([[Z.normal-form]]). But "is a positive pile" is a predicate on *normal forms*, i.e. a statement about the rewriting system, not an equation inside it.

## Plain

The page can say two piles are equal; it has no sign for "smaller than." You can see it — the leftover circles — but you cannot write it.

## Derivation

none — gap.

## Confirms

That order is *meta* in James's calculus: it is read off normal forms, exactly as it is read off tallies. The boundary-analysis thread (2026-09-29 → 10-01) found the same: order is native on piles but needs a free choice of base for general forms, pinned by the derivative. Trichotomy, the triangle inequality and the metric all wait on this gap.

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | fails | no setting has a relation other than its equality |

| reading | cell | why |
|---|---|---|
| C | PARTIAL | the real line is ordered; the complex plane is not — so the ℂ reading itself only orders the real slice |
| finset | PARTIAL | injections between finite sets *are* the order; `m ≤ n` iff there is an injection — a reading-level statement with no form yet |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The `1–2` band is the curriculum's: comparison is taught alongside counting. The chart's inability to write it at that band is itself a teaching point about what an equation is.

## Plan

| field | content |
|---|---|
| candidate form(s) | positivity of a normal form: define `Pos(A)` := "the normal form of A is a pile of `o`" (meta); then `A < B` := `Pos(B <A>)`. Candidate object-level shadow: the *witness* form `W` with `A W ≐ B`, `W` a non-void pile — order as the existence of a difference pile |
| law(s) to add, and type | a `definition` at the meta level (order via normal forms) — no new axiom; or an `import` (the order of ℝ) for general forms |
| nativity criterion | the definition may use only normal forms produced by the calculus's own rewriting ([[Z.normal-form]]) and no external valuation |
| refutation test | two forms with the same normal-form sign but opposite ℂ order — impossible on piles; the test bites on general real forms (where the boundary-analysis thread found a base choice is needed) |
| meta-move? | yes, mild: a predicate on normal forms is a statement *about* the calculus. The finset reading suggests the deeper move — order as the existence of a morphism (an injection), i.e. order lives in a category of readings, not in the forms |
| owner thread | boundary analysis (james-algebra); geometry-refoundation for the metric |
| rank | meta-definition (normal-form positivity) < import (order of ℝ) < new primitive |
