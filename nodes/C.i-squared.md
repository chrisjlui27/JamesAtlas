---
id: C.i-squared
title: i times i is minus one
type: theorem
level: object
kind: law
rung: C
order: 1000
setting: classical
equality: "≐"
domain: positive
law: "([(([J] <[oo]>))] [(([J] <[oo]>))]) ≐ <o>"
units: "i · i = −1"
gloss_check: "-1"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James); Bombelli 1572 for the rule of signs of i"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.multiplication, C.imaginary-unit, mult.involution, Q.fractional-cardinality, C.phase-value]
see_also: [C.imaginary-unit, Q.fractional-cardinality, C.phase-value, alg.root-squared]
aliases: ["i² = −1", i squared]
concepts: [phase, complex-number, negation, multiplication]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([(([J] <[oo]>))] [(([J] <[oo]>))]) ≐ <o>` | `([i] [i]) ≐ <o>` | i · i = −1 |

Two quarter turns are a half-turn: the defining property of i is a theorem here.

## Plain

Half of J plus half of J is J; circle it and you have minus one. That is all i² = −1 says.

## Derivation

| form | rule | note |
|---|---|---|
| `([(([J] <[oo]>))] [(([J] <[oo]>))])` | given | i × i, [[mult.multiplication]] with i = `(([J] <[oo]>))` ([[C.imaginary-unit]]) |
| `(([J] <[oo]>) ([J] <[oo]>))` | [[mult.involution]] | the unit `[(X)] ≐ X` twice, with X = `([J] <[oo]>)` — both directly inside the outer instance, absorbing, and X = iπ/2 is on the strip besides |
| `(J)` | [[Q.fractional-cardinality]] | half of J and half of J make J: `([A] <[oo]>) ([A] <[oo]>) ≐ A` with A = J |
| `<o>` | [[C.phase-value]] | `(J) ≐ <o>` |

## Confirms

i² = −1, derived rather than posited: the "half of J plus half of J is J" step is [[Q.fractional-cardinality]] with A = J — a schema first met for piles, whose derivation is exact on all of ℂ× (its domain was widened to say so when this rung first cited it). Compare [[alg.root-squared]], the same fact for √A: `√A · √A ≐ A` with A = `<o>` would *also* give i² = −1 — but `(([[<o>]] <[oo]>))` is `(([J] <[oo]>))`, the same form, so the two roads agree on which square root is meant. What the law is **not**: a proof that i is *the* square root of −1. Its mirror `<(([J] <[oo]>))>` squares to −1 as well (two mirrors cancel across a product, [[mult.product-of-negatives]]), and the calculus keeps the two apart as forms; "√−1" names one of them only by the principal-branch convention of the reading.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step sits directly under an instance (depth-1 criterion); ω/4 + ω/4 = ω/2 exactly |
| JH, JO | holds | per slice: u · u = −1 for every unit imaginary direction u — the one statement about i that is slice-independent (the central sign) |
| JP | guarded | as [[C.imaginary-unit]]: the count 2 must be a unit at p and the form a value there |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
