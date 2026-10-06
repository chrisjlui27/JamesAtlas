---
id: Q.quotient-of-numerals
title: A quotient of piles that divides evenly is a pile
type: theorem
level: object
kind: instance
rung: Q
order: 585
setting: classical
equality: ≐
domain: natural
law: "([oooooo] <[oo]>) ≐ ooo"
units: "6 ÷ 2 = 3 ; in general ([o^{mn}] <[o^n]>) ≐ o^m"
gloss_check: 3
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: holds
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
uses: [Q.division, mult.product-of-numerals, mult.involution, Z.inversion, N.numeral]
see_also: [Q.cancel-common-factor, mult.product-of-numerals]
aliases: [6 ÷ 2 = 3, exact division]
concepts: [division, natural-number]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([oooooo] <[oo]>) ≐ ooo` | — | 6 ÷ 2 = 3 |

The defined division agrees with the schoolroom's on numerals that divide evenly: write the dividend as a product and cancel. This is the law that makes [[Q.division]] *division* and not merely a shape — the counterpart of [[mult.product-of-numerals]].

## Plain

Six divided by two really is three: six is three-times-two, and the two cancels against its mirror.

## Derivation

| form | rule | note |
|---|---|---|
| `([oooooo] <[oo]>)` | given | 6 ÷ 2, [[Q.division]] with the piles of [[N.numeral]] |
| `([([ooo] [oo])] <[oo]>)` | [[mult.product-of-numerals]] | 6 is 3 × 2, right to left |
| `([ooo] [oo] <[oo]>)` | [[mult.involution]] | `[(X)] ≐ X` |
| `([ooo])` | [[Z.inversion]] | `[oo] <[oo]>` cancels |
| `ooo` | [[mult.involution]] | `([A]) ≐ A` |

## Confirms

Exact division of naturals. What happens when the division is *not* exact — `7 ÷ 2` — is a fraction, [[Q.fraction]], and the calculus does not prefer the mixed-number spelling `ooo (<[oo]>)` over it: the two inscriptions are convertible (≐) by Distribution with the context `<[oo]>`, this law, and the unit law.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1, JH, JO | holds | real content; the Involution-down step is on the strip |
| JP | holds | a quotient that divides evenly is a pile at every place; a reciprocal on its own needs a unit denominator (`place.no-inverse-of-the-prime`) |

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
