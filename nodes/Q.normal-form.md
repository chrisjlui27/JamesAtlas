---
id: Q.normal-form
title: Fraction arithmetic closes — a worked reduction
type: theorem
level: object
kind: instance
rung: Q
order: 657
setting: classical
equality: "≐"
domain: natural
law: "([oo] <[ooo]>) <([o] <[oo]>)> ≐ ([o] <[oooooo]>)"
units: "2/3 − 1/2 = 1/6 ; every juxtaposition of instances, mirrored or not, whose contents are juxtapositions of [pile] and <[pile]>, reduces to a fraction, its mirror, or the void"
gloss_check: "1/6"
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
known_since: "1993 (James); the arithmetic is ancient"
entered: 2026-10-03
guide: need-led
band: "3–5"
uses: [Q.rational, Z.subtraction, Q.negative-fraction, Q.add-fractions, mult.product-of-numerals, mult.inverse-promotion, mult.unit-law, Z.normal-form, Z.collection, mult.involution]
see_also: [Q.lowest-terms, Q.cross-multiplication, Z.normal-form]
aliases: [subtracting fractions, closure of ℚ, fraction normal form]
concepts: [fraction, normal-form, subtraction]
understood: no
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([oo] <[ooo]>) <([o] <[oo]>)> ≐ ([o] <[oooooo]>)` | — | 2/3 − 1/2 = 1/6 |

The schema: any juxtaposition of (mirrored) instances whose contents are juxtapositions of `[pile]` and `<[pile]>` reduces, by the laws of this rung, to a single fraction, the mirror of one, or the void. The instance shown is the walk's first full computation in ℚ: every rung-Q law is used once.

## Plain

Two-thirds take away a half is a sixth — and the page gets there by moving the minus onto the top, finding a common bottom, multiplying the piles, cancelling, and gathering the mirrors.

## Derivation

| form | rule | note |
|---|---|---|
| `([oo] <[ooo]>) <([o] <[oo]>)>` | given | 2/3 and the mirror of 1/2, [[Q.rational]]: a difference by [[Z.subtraction]] |
| `([oo] <[ooo]>) ([<o>] <[oo]>)` | [[Q.negative-fraction]] | the sign in front moves onto the numerator, right to left |
| `([([oo] [oo]) ([<o>] [ooo])] <[ooo]> <[oo]>)` | [[Q.add-fractions]] | a common denominator: A = `oo`, B = `ooo`, C = `<o>`, D = `oo` |
| `([oooo ([<o>] [ooo])] <[ooo]> <[oo]>)` | [[mult.product-of-numerals]] | 2 × 2 = 4 |
| `([oooo <([o] [ooo])>] <[ooo]> <[oo]>)` | [[mult.inverse-promotion]] | the mirrored numerator's sign comes out of its product, right to left |
| `([oooo <ooo>] <[ooo]> <[oo]>)` | [[mult.unit-law]] | 1 × 3 = 3 |
| `([o] <[ooo]> <[oo]>)` | [[Z.normal-form]] | 4 − 3 = 1 |
| `([o] <[ooo] [oo]>)` | [[Z.collection]] | gather the mirrors |
| `([o] <[([ooo] [oo])]>)` | [[mult.involution]] | the unit, right to left: the denominator as a product |
| `([o] <[oooooo]>)` | [[mult.product-of-numerals]] | 3 × 2 = 6 |

## Confirms

That ℚ is closed under its four operations, shown rather than stated: the general case is this derivation with the piles replaced by variables and the instances multiplied out by [[Q.add-fractions]], [[Q.negative-fraction]] and [[mult.product-of-numerals]], then normalized by [[Z.normal-form]]. What it does **not** give is *lowest terms* ([[Q.lowest-terms]]): the result `([o] <[oooooo]>)` happens to be reduced; `([oo] <[oooooooooooo]>)` would be just as correct and no law prefers one to the other.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the single unit step sits under an angle under the instance: depth-1 criterion ([[mult.involution]], Notes) |
| JH, JO | replaced | add-fractions and product-of-numerals are replaced there |
| JP | guarded | unit denominators only |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Tagged *need-led*: nothing in the shape of the forms asks for a single fraction at the end; the wish to read the answer does. This is the node the walk should pause on: three of the rung's laws and five of the earlier rungs' are exercised in ten lines. In 𝕁₁ the ninth line (the unit, right to left) posts a receipt, and so do the `[o] ≐ void` steps hidden inside the unit law and the product of numerals (rows 4, 6, 10); all are absorbed, by the depth-1 criterion.
