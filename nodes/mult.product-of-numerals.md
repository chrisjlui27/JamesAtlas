---
id: mult.product-of-numerals
title: The product of piles is a pile
type: theorem
level: object
kind: schema
rung: mult
order: 350
setting: classical
equality: "≐"
domain: natural
law: "([ooo] [oo]) ≐ oooooo"
units: "3 × 2 = 6 ; in general ([o^m][o^n]) ≐ o^{mn}"
gloss_check: "6"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James, §3 worked example)"
entered: 2026-10-03
guide: shape-led
band: "3–5"
uses: [mult.multiplication, mult.distribution, mult.unit-law, mult.involution, N.numeral]
see_also: [mult.cardinality, N.addition]
aliases: [3 × 2, times table, multiplication of naturals]
concepts: [multiplication, natural-number]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([ooo] [oo]) ≐ oooooo` | — | 3 × 2 = 6 |

The defined multiplication agrees with repeated addition on numerals. This is the law that makes [[mult.multiplication]] *multiplication* and not merely a shape.

## Plain

Three times two really is six: the box-and-circle recipe, run on piles, gives back the pile you would get by adding.

## Derivation

| form | rule | note |
|---|---|---|
| `([ooo] [oo])` | [[mult.multiplication]] | 3 × 2, [[N.numeral]] |
| `([ooo] [o o])` | definition | the pile 2 is two units |
| `([ooo] [o]) ([ooo] [o])` | [[mult.distribution]] | distribute the instance over the abstract's two units |
| `([ooo]) ([ooo])` | [[mult.unit-law]] | `[o] ≐ void` in each factor |
| `ooo ooo` | [[mult.involution]] | `([A]) ≐ A`, twice |
| `oooooo` | definition | the pile 6 |

## Confirms

That James's definition recovers the multiplication table — the one computation a reader should run by hand before trusting the rest of the chart. It also shows *how* the conversion works: Distribution turns one circle-around-two into two circles, and Involution strips them; multiplication by `n` is `n` copies, which is [[mult.cardinality]] read backwards. The "for every m, n" is a schema ([[N.induction]]); each instance is a finite derivation.

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | holds | real content is slice-pure in every extension |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | EXACT | a 3-set times a 2-set is a 6-set |
| logic | ABSENT | no numbers |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
