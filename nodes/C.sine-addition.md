---
id: C.sine-addition
title: The sine of a sum
type: theorem
level: object
kind: law
rung: C
order: 1086
setting: classical
equality: "≐"
domain: real
law: "([([(([J] [S])) <(<[(([J] [S]))]>)>] <[oo]> <[(([J] <[oo]>))]>)] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)]) ([([(([J] [S])) (<[(([J] [S]))]>)] <[oo]>)] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)]) ≐ ([(([J] [S T])) <(<[(([J] [S T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)"
units: "sin π(s+t) = sin πs cos πt + cos πs sin πt"
gloss_check: "sin(pi*(S+T))"
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
known_since: "Ptolemy (c. 150); Euler 1748 for the exponential derivation"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.multiplication, C.sine, C.cosine, mult.involution, mult.distribution, mult.inverse-promotion, Z.inversion, mult.cardinality, Z.collection, C.turn-of-sum, Q.reciprocal-of-product]
guarded_by: [mult.seam-decree]
see_also: [C.turn-of-sum, C.cosine-addition, C.cosine, C.sine]
aliases: [sine addition formula, "sin(s+t)", angle addition]
concepts: [trigonometry, phase, addition]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([sin πS] [cos πT]) ([cos πS] [sin πT]) ≐ sin π(S T)` | sin π(S+T) = `([(([J] [S T])) <(<[(([J] [S T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)` | sin(s+t) = sin s cos t + cos s sin t |

The addition formula for sine, the companion of [[C.cosine-addition]]: here the mirrored terms survive as the reverse turn and the positive ones as the turn, and the difference over 2i is the sine of the sum.

## Plain

The sine of a combined turn is sine times cosine plus cosine times sine. Spell out both sides in turns, and the cross terms cancel again — the other half of them this time.

## Derivation

| form | rule | note |
|---|---|---|
| `([([(([J] [S])) <(<[(([J] [S]))]>)>] <[oo]> <[(([J] <[oo]>))]>)] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)]) ([([(([J] [S])) (<[(([J] [S]))]>)] <[oo]>)] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])` | given | sin s cos t + cos s sin t: [[mult.multiplication]], [[C.sine]], [[C.cosine]] |
| `([(([J] [S])) <(<[(([J] [S]))]>)>] <[oo]> <[(([J] <[oo]>))]> [(([J] [T])) (<[(([J] [T]))]>)] <[oo]>) ([(([J] [S])) (<[(([J] [S]))]>)] <[oo]> [(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)` | [[mult.involution]] | the unit on each of the four abstracts, directly inside its instance — absorbing |
| `([(([J] [S])) <(<[(([J] [S]))]>)>] <[oo]> <[oo]> <[(([J] <[oo]>))]> [(([J] [T]))]) ([(([J] [S])) <(<[(([J] [S]))]>)>] <[oo]> <[oo]> <[(([J] <[oo]>))]> [(<[(([J] [T]))]>)]) ([(([J] [S])) (<[(([J] [S]))]>)] <[oo]> <[oo]> <[(([J] <[oo]>))]> [(([J] [T]))]) ([(([J] [S])) (<[(([J] [S]))]>)] <[oo]> <[oo]> <[(([J] <[oo]>))]> [<(<[(([J] [T]))]>)>])` | [[mult.distribution]] | distribute each product over its second factor |
| `(<[oo]> <[oo]> <[(([J] <[oo]>))]> [(([J] [S]))] [(([J] [T]))]) (<[oo]> <[oo]> <[(([J] <[oo]>))]> [<(<[(([J] [S]))]>)>] [(([J] [T]))]) (<[oo]> <[oo]> <[(([J] <[oo]>))]> [(([J] [S]))] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> <[(([J] <[oo]>))]> [<(<[(([J] [S]))]>)>] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> <[(([J] <[oo]>))]> [(([J] [S]))] [(([J] [T]))]) (<[oo]> <[oo]> <[(([J] <[oo]>))]> [(<[(([J] [S]))]>)] [(([J] [T]))]) (<[oo]> <[oo]> <[(([J] <[oo]>))]> [(([J] [S]))] [<(<[(([J] [T]))]>)>]) (<[oo]> <[oo]> <[(([J] <[oo]>))]> [(<[(([J] [S]))]>)] [<(<[(([J] [T]))]>)>])` | [[mult.distribution]] | and over the first: eight terms |
| `(<[oo]> <[oo]> <[(([J] <[oo]>))]> [(([J] [S]))] [(([J] [T]))]) <(<[oo]> <[oo]> <[(([J] <[oo]>))]> [(<[(([J] [S]))]>)] [(([J] [T]))])> (<[oo]> <[oo]> <[(([J] <[oo]>))]> [(([J] [S]))] [(<[(([J] [T]))]>)]) <(<[oo]> <[oo]> <[(([J] <[oo]>))]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)])> (<[oo]> <[oo]> <[(([J] <[oo]>))]> [(([J] [S]))] [(([J] [T]))]) (<[oo]> <[oo]> <[(([J] <[oo]>))]> [(<[(([J] [S]))]>)] [(([J] [T]))]) <(<[oo]> <[oo]> <[(([J] <[oo]>))]> [(([J] [S]))] [(<[(([J] [T]))]>)])> <(<[oo]> <[oo]> <[(([J] <[oo]>))]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)])>` | [[mult.inverse-promotion]] | the four mirrors come out |
| `(<[oo]> <[oo]> <[(([J] <[oo]>))]> [(([J] [S]))] [(([J] [T]))]) (<[oo]> <[oo]> <[(([J] <[oo]>))]> [(([J] [S]))] [(([J] [T]))]) <(<[oo]> <[oo]> <[(([J] <[oo]>))]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)])> <(<[oo]> <[oo]> <[(([J] <[oo]>))]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)])>` | [[Z.inversion]] | two pairs cancel |
| `([(<[oo]> <[oo]> <[(([J] <[oo]>))]> [(([J] [S]))] [(([J] [T]))])] [oo]) <(<[oo]> <[oo]> <[(([J] <[oo]>))]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> <[(([J] <[oo]>))]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)])>` | [[mult.cardinality]] [[Z.collection]] | the positive pair becomes a count; the mirrored pair collects under one mirror |
| `([(<[oo]> <[oo]> <[(([J] <[oo]>))]> [(([J] [S]))] [(([J] [T]))])] [oo]) <([(<[oo]> <[oo]> <[(([J] <[oo]>))]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)])] [oo])>` | [[mult.cardinality]] | and becomes a count too |
| `(<[oo]> <[oo]> <[(([J] <[oo]>))]> [(([J] [S]))] [(([J] [T]))] [oo]) <(<[oo]> <[oo]> <[(([J] <[oo]>))]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)] [oo])>` | [[mult.involution]] | the unit, directly inside each instance (through the angle for the second) — absorbing |
| `(<[oo]> <[(([J] <[oo]>))]> [(([J] [S]))] [(([J] [T]))]) <(<[oo]> <[(([J] <[oo]>))]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)])>` | [[Z.inversion]] | a `<[oo]>` cancels the count in each |
| `(<[oo]> <[(([J] <[oo]>))]> [([(([J] [S]))] [(([J] [T]))])]) <(<[oo]> <[(([J] <[oo]>))]> [([(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)])])>` | [[mult.involution]] | the unit right to left on each product — absorbing |
| `(<[oo]> <[(([J] <[oo]>))]> [(([J] [S T]))]) <(<[oo]> <[(([J] <[oo]>))]> [([(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)])])>` | [[C.turn-of-sum]] | the product of the turns is the turn of the sum |
| `(<[oo]> <[(([J] <[oo]>))]> [(([J] [S T]))]) <(<[oo]> <[(([J] <[oo]>))]> [(<[(([J] [S]))]> <[(([J] [T]))]>)])>` | [[mult.involution]] | the unit on `[(<[X]>)]` and `[(<[Y]>)]`, directly inside their instance — absorbing |
| `(<[oo]> <[(([J] <[oo]>))]> [(([J] [S T]))]) <(<[oo]> <[(([J] <[oo]>))]> [(<[([(([J] [S]))] [(([J] [T]))])]>)])>` | [[Q.reciprocal-of-product]] | the product of reciprocals is the reciprocal of the product |
| `(<[oo]> <[(([J] <[oo]>))]> [(([J] [S T]))]) <(<[oo]> <[(([J] <[oo]>))]> [(<[(([J] [S T]))]>)])>` | [[C.turn-of-sum]] | again, under the mirror |
| `(<[oo]> <[(([J] <[oo]>))]> [(([J] [S T]))]) (<[oo]> <[(([J] <[oo]>))]> [<(<[(([J] [S T]))]>)>])` | [[mult.inverse-promotion]] | the mirror moves inside, onto the reciprocal turn |
| `([(([J] [S T])) <(<[(([J] [S T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)` | [[mult.distribution]] | collect over the shared `<[oo]> <[i]>`, right to left: the sine of the sum |

## Confirms

sin(s+t) = sin s cos t + cos s sin t. Compared with the cosine formula, the i² step is not needed: there is one `<[i]>` in each product and it is carried through unchanged. It is **not** the only route — the formula is also the imaginary part of [[C.turn-of-sum]] expanded by Euler's formula — but that route needs "imaginary part", which is a reading, not a form; this one stays on the page.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step directly under an instance, through an angle at most |
| JH, JO | replaced | per slice |
| JP | guarded | needs i (p ≡ 1 mod 4, [[place.selection]]) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Guarded by position (Amendment A2): as [[C.cosine-addition]] — a seam step, admitted by the decree's position clause, so the law carries the decree in its price while its statement is exact in ℂ.
