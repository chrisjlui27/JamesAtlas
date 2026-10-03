---
id: Q.halves
title: Two halves make one
type: theorem
level: object
kind: law
rung: Q
order: 560
setting: classical
equality: ≐
domain: natural
law: "(<[oo]>) (<[oo]>) ≐ o"
units: ½ + ½ = 1
gloss_check: 1
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
known_since: 1993 (James); the fact is ancient
entered: 2026-10-03
guide: shape-led
band: 3–5
uses: [Q.half, mult.cardinality, mult.involution, Z.inversion, N.unit]
see_also: [Q.fractional-cardinality]
aliases: [½ + ½ = 1]
concepts: [fraction, addition]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(<[oo]>) (<[oo]>) ≐ o` | — | ½ + ½ = 1 |

## Plain

Two halves side by side are one whole — the two copies collect into a count of two, which cancels the mirrored two.

## Derivation

| form | rule | note |
|---|---|---|
| `(<[oo]>) (<[oo]>)` | given | two halves, [[Q.half]] |
| `([(<[oo]>)] [oo])` | [[mult.cardinality]] | two copies of X are X with count 2 |
| `(<[oo]> [oo])` | [[mult.involution]] | `[(X)] ≐ X` |
| `(void)` | [[Z.inversion]] | `<[oo]> [oo]` cancels |
| `o` | [[N.unit]] | — |

## Confirms

The first arithmetic of fractions, and the mechanism behind all of it: *repetition becomes a count, and a count cancels its mirror*. Every "n copies of 1/n make 1" is this derivation with `oo` replaced by the pile of n.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1, JH, JO | holds | in J1 the Involution-down step sits at depth 1 under the instance (depth-1 criterion, [[mult.involution]] Notes) |
| JP | guarded | needs ½ to be a form at the place (odd p) |

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
