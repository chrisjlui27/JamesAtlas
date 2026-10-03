---
id: alg.sqrt4
title: The square root of four is two
type: theorem
level: object
kind: law
rung: alg
order: 788
setting: classical
equality: "≐"
domain: natural
law: "(([[oooo]] <[oo]>)) ≐ oo"
units: "√4 = 2"
gloss_check: "2"
holds:
  classical: holds
  J1: holds-mod-Λ
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
known_since: "1993 (James); the fact is ancient"
entered: 2026-10-03
guide: shape-led
band: "6–8"
uses: [alg.root, mult.product-of-numerals, mult.involution, mult.cardinality, Z.inversion]
see_also: [alg.sqrt2, alg.root-squared]
aliases: ["√4 = 2"]
concepts: [root, natural-number]
understood: "yes"
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[oooo]] <[oo]>)) ≐ oo` | — | √4 = 2 |

The confirming instance before the irrational one ([[alg.sqrt2]]): the root form, run on a square number, gives back a pile.

## Plain

The square root of four is two: four is two twos, the double log collects the two copies into a count of two, and that count cancels the mirrored two.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[oooo]] <[oo]>))` | given | √4, [[alg.root]] |
| `(([[([oo] [oo])]] <[oo]>))` | [[mult.product-of-numerals]] | 4 = 2 × 2, right to left |
| `(([[oo] [oo]] <[oo]>))` | [[mult.involution]] | the unit; content 2 ln 2, real |
| `(([([[oo]] [oo])] <[oo]>))` | [[mult.cardinality]] | two copies of `[oo]` are one copy with count 2 |
| `(([[oo]] [oo] <[oo]>))` | [[mult.involution]] | the unit; content ln ln 2 + ln 2 = ln(2 ln 2), real |
| `(([[oo]]))` | [[Z.inversion]] | `[oo] <[oo]>` cancels |
| `([oo])` | [[mult.involution]] | the counit |
| `oo` | [[mult.involution]] | the counit |

## Confirms

That the root of a perfect square is its base, by the mechanism itself (not by a table): the half-count meets a doubled log and they cancel. Note the unit step on content `[[oo]] [oo]` = ln ln 2 + ln 2 — ln ln 2 is negative, but the sum ln(2 ln 2) = 0.327 is real; that step is absorbing anyway. The step the engine strip-tests is row 3, on content 2 ln 2.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, JH, JO | holds | real content |
| J1 | holds-mod-Λ | row 3's unit step sits under a square inside the instance — not absorbing; its receipt is posted. The cardinality step's hidden `[o] → ω` is absorbing |
| JP | guarded | needs the count 2 to be a unit (odd p) and the p-adic log of 2 to converge |

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
