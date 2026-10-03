---
id: Q.divide-by-fraction
title: Dividing by a fraction
type: theorem
level: object
kind: law
rung: Q
order: 604
setting: classical
equality: ≐
domain: positive
law: "([([A] <[B]>)] <[([C] <[D]>)]>) ≐ ([([A] [D])] <[([B] [C])]>)"
units: (a/b) ÷ (c/d) = (ad)/(bc)
gloss_check: (A*D)/(B*C)
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
uses: [Q.division, mult.involution, Z.collection, Z.cancellation, void.space]
see_also: [Q.flip, Q.multiply-fractions, Q.division-as-product]
aliases: [invert and multiply, (a/b) ÷ (c/d)]
concepts: [fraction, division]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([([A] <[B]>)] <[([C] <[D]>)]>) ≐ ([([A] [D])] <[([B] [C])]>)` | — | (a/b) ÷ (c/d) = (ad)/(bc) |

## Plain

To divide by a fraction, flip it and multiply — on the page, the divisor's mirror splits over its top and bottom and the bottom's mirrors cancel, leaving top and bottom exchanged.

## Derivation

| form | rule | note |
|---|---|---|
| `([([A] <[B]>)] <[([C] <[D]>)]>)` | given | (a/b) ÷ (c/d), [[Q.division]] |
| `([A] <[B]> <[C] <[D]>>)` | [[mult.involution]] | `[(X)] ≐ X`, twice |
| `([A] <[B]> <[C]> <<[D]>>)` | [[Z.collection]] | split the divisor's mirror |
| `([A] [D] <[B]> <[C]>)` | [[Z.cancellation]] | `<<[D]>> ≐ [D]`; regroup by [[void.space]] |
| `([A] [D] <[B] [C]>)` | [[Z.collection]] | gather the two remaining mirrors |
| `([([A] [D])] <[([B] [C])]>)` | [[mult.involution]] | the unit `X ≐ [(X)]`, twice, right to left |

## Confirms

"Keep, change, flip" as three moves of the Inversion cluster and a regroup, under two Involutions. It is [[Q.flip]] followed by [[Q.multiply-fractions]], written out in one table.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | depth-1 criterion ([[mult.involution]], Notes) |
| JH, JO | replaced | order of factors matters |
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
