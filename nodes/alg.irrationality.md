---
id: alg.irrationality
title: Irrationality — √2 is not a fraction
type: gap
level: meta
kind: concept
rung: alg
order: 820
setting: classical
equality: ≐
domain: natural
law: "GAP — '(([[oo]] <[oo]>)) is not ≐ any fraction of piles' is a negative statement about all derivations, and the calculus has no form for it"
units: √2 ∉ ℚ
holds:
  classical: fails
  J1: fails
  JH: fails
  JO: fails
  JP: fails
readings:
  C: ABSENT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: ABSENT
verified: hand
known_since: "the Pythagoreans; the descent proof is the interpolated Euclid X.117 (earliest witness Aristotle, Prior Analytics I.23); the gap named here 2026-10-03"
entered: 2026-10-03
guide: need-led
band: 6–8
uses: []
see_also: [alg.sqrt2, Q.lowest-terms, N.induction, N.freeness]
aliases: [irrational, √2 is irrational, incommensurability]
concepts: [root, gap, normal-form]
understood: partial
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| none | — | √2 ≠ m/n for all m, n |

[[N.freeness]] showed that two *piles* are different when their counts differ, and [[Q.cross-multiplication]] decides when two *fractions* are equal. Neither reaches this: to say that `(([[oo]] <[oo]>))` is not ≐ any `([o^m] <[o^n]>)` one must quantify over all fractions and argue by descent — Euclid's proof squares both sides and uses parity, which needs divisibility and induction ([[N.induction]]), and a normal form for fractions in lowest terms ([[Q.lowest-terms]]).

## Plain

The page can write the square root of two and can write any fraction, but it has no way to say "and none of those fractions is this."

## Derivation

none — gap.

## Confirms

That inequality is as hard as order ([[N.order]]): an equational calculus proves equations and can refute one only through a model. The ℂ reading refutes `√2 ≐ 7/5` instance by instance (1.4142… ≠ 1.4), but "no fraction at all" is a statement about the whole set of forms, which only a meta-level argument makes.

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | fails | no setting of the program states a negative universal |

| reading | cell | why |
|---|---|---|
| C | ABSENT | the reading refutes each instance; it does not state the universal |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—

## Plan

| field | content |
|---|---|
| candidate form(s) | none as an equation. Candidate meta-statement: "the normal form of `([√2 … ])`-type forms is not of fraction shape" — requires a confluent normal form for radical forms, which the calculus does not yet have |
| law(s) to add, and type | a `theorem` at the meta level, once [[Q.lowest-terms]] (lowest terms) and the induction schema ([[N.induction]]) are available: Euclid's descent written as a statement about piles; or an `import` (irrationality as a known theorem) with the ℂ reading as its witness |
| nativity criterion | the descent argument must be expressible as a schema over piles using only the chart's own laws (cross-multiplication, product-of-numerals, Z.normal-form) plus the induction schema |
| refutation test | a derivation `(([[oo]] <[oo]>)) ≐ ([o^m] <[o^n]>)` — which would be a collapse of the calculus, since the ℂ reading separates the two sides |
| meta-move? | yes: induction (descent) and a negative universal, both meta |
| owner thread | boundary-lean-game (the Lean expansion proves this natively: `irrational_sqrt_two` in Mathlib) |
| rank | import (the irrationality of √2, with the ℂ reading as witness) < theorem (needs the induction schema, which is axiom-level — see [[N.induction]]) |
