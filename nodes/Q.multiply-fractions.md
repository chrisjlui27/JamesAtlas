---
id: Q.multiply-fractions
title: Multiplying fractions
type: theorem
level: object
kind: law
rung: Q
order: 600
setting: classical
equality: ≐
domain: positive
law: "([([A] <[B]>)] [([C] <[D]>)]) ≐ ([([A] [C])] <[([B] [D])]>)"
units: (a/b)(c/d) = (ac)/(bd)
gloss_check: (A*C)/(B*D)
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: 1993 (James); the rule is ancient
entered: 2026-10-03
guide: shape-led
band: 6–8
uses: [mult.multiplication, Q.division, mult.involution, Z.collection, void.space]
see_also: [Q.division-as-product, Q.reciprocal-of-product, Q.divide-by-fraction]
aliases: [(a/b)(c/d), multiply across]
concepts: [fraction, multiplication]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([([A] <[B]>)] [([C] <[D]>)]) ≐ ([([A] [C])] <[([B] [D])]>)` | — | (a/b)(c/d) = (ac)/(bd) |

## Plain

Multiply tops together and bottoms together — because under the box everything is a sum, and the mirrors gather.

## Derivation

| form | rule | note |
|---|---|---|
| `([([A] <[B]>)] [([C] <[D]>)])` | given | (a/b) × (c/d): [[mult.multiplication]] of two quotients, [[Q.division]] |
| `([A] <[B]> [C] <[D]>)` | [[mult.involution]] | `[(X)] ≐ X`, twice |
| `([A] [C] <[B] [D]>)` | [[Z.collection]] | gather the mirrors; regroup by [[void.space]] |
| `([([A] [C])] <[([B] [D])]>)` | [[mult.involution]] | the unit `X ≐ [(X)]`, twice, right to left — writing the numerator and denominator as products again |

## Confirms

"Multiply across". Dividing by a fraction is [[Q.divide-by-fraction]]. The whole fraction arithmetic of grades 3–8 is a handful of theorems of Involution, Distribution, Inversion and their two corollaries (collection, cardinality).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the unit steps (both directions) sit at depth 1 under the instance (depth-1 criterion, [[mult.involution]] Notes) |
| JH, JO | replaced | order of factors matters; the ordered bracket's Splice carries the product |
| JP | guarded | for unit denominators |

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
