---
id: Q.flip
title: The reciprocal of a fraction is the fraction flipped
type: theorem
level: object
kind: law
rung: Q
order: 602
setting: classical
equality: ≐
domain: positive
law: "(<[([C] <[D]>)]>) ≐ ([D] <[C]>)"
units: 1/(c/d) = d/c
gloss_check: D/C
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
band: 6–8
uses: [Q.reciprocal, Q.division, mult.involution, Z.collection, Z.cancellation]
see_also: [Q.divide-by-fraction, Q.double-reciprocal]
aliases: [flip the fraction, 1/(c/d) = d/c]
concepts: [fraction, inverse]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(<[([C] <[D]>)]>) ≐ ([D] <[C]>)` | — | 1/(c/d) = d/c |

## Plain

One over a fraction is the fraction upside down: the outer mirror splits over top and bottom, and the bottom's two mirrors cancel.

## Derivation

| form | rule | note |
|---|---|---|
| `(<[([C] <[D]>)]>)` | given | the reciprocal ([[Q.reciprocal]]) of c/d ([[Q.division]]) |
| `(<[C] <[D]>>)` | [[mult.involution]] | `[(X)] ≐ X` |
| `(<[C]> <<[D]>>)` | [[Z.collection]] | split the mirror |
| `(<[C]> [D])` | [[Z.cancellation]] | two mirrors cancel on D |

The result is `([D] <[C]>)`, which is d ÷ c by [[Q.division]].

## Confirms

"Flip it": the rule behind dividing by a fraction ([[Q.divide-by-fraction]]). It is inverse collection and cancellation, one level deeper, exactly as [[Q.reciprocal-of-product]] was collection one level deeper.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | depth-1 criterion ([[mult.involution]], Notes) |
| JH, JO | holds | the law survives per quotient type by Reversal, `(xy⁻¹)⁻¹ = yx⁻¹`; the collection step inside the bracket does not transfer verbatim |
| JP | guarded | for units |

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
