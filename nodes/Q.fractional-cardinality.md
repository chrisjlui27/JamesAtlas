---
id: Q.fractional-cardinality
title: Fractional cardinality — half of a form, twice, is the form
type: theorem
level: object
kind: schema
rung: Q
order: 570
setting: classical
equality: ≐
domain: positive
law: "([A] <[oo]>) ([A] <[oo]>) ≐ A"
units: "a/2 + a/2 = a ; in general n copies of ([A]<[o^n]>) ≐ A"
gloss_check: A
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
known_since: "1993 (James) for the mechanism; 'fractional cardinality' is the name Book One uses; the arithmetic is ancient"
entered: 2026-10-03
guide: shape-led
band: 3–5
uses: [Q.division, mult.cardinality, mult.involution, Z.inversion]
see_also: [Q.halves, mult.cardinality]
aliases: [fractional cardinality, a/n, mirrored count]
concepts: [fraction, division, counting]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A] <[oo]>) ([A] <[oo]>) ≐ A` | — | a/2 + a/2 = a |

Cardinality with a mirrored count: `([A] <[o^n]>)` is "A with count 1/n", and n copies of it collect back to A. This is James's fractional cardinality, the mechanism that will give roots one level down (`(([[A]] <[oo]>))` = √a at rung `alg`) and, when the form is J, the roots of −1 — `(([J] <[o^n]>))` is e^{iπ/n}, a 2n-th root of unity.

## Plain

Half of something, twice, is the thing — and "half of" is just "with a mirrored count of two".

## Derivation

| form | rule | note |
|---|---|---|
| `([A] <[oo]>) ([A] <[oo]>)` | given | two copies of A ÷ 2, [[Q.division]] |
| `([([A] <[oo]>)] [oo])` | [[mult.cardinality]] | two copies are one copy with count 2 |
| `([A] <[oo]> [oo])` | [[mult.involution]] | `[(X)] ≐ X` |
| `([A])` | [[Z.inversion]] | `<[oo]> [oo]` cancels |
| `A` | [[mult.involution]] | `([A]) ≐ A` |

## Confirms

That counts need not be piles: a mirrored pile is a count too, and the same two theorems (Cardinality, Inversion) govern it. Nothing is added to admit fractions of arbitrary forms; the "for every n" is the usual schema ([[N.induction]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1, JH, JO | holds | in J1 the Involution-down step sits at depth 1 under the instance (depth-1 criterion, [[mult.involution]] Notes) |
| JP | guarded | `([A]<[o^n]>)` is a form at p iff n is a unit at p (Division-by-unit, Part II Ch. 10); the separate selection `d | p−1` (and `d | 2` at p = 2) concerns fractional counts of ω — which roots of unity exist at p — and belongs to rung C |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | the ψ-road: `ψ^r` is a cardinality-power; fractional counts are where the (b) road and the chart's trunk first share a form |

## Refuted readings

none

## Notes

—
