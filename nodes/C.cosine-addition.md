---
id: C.cosine-addition
title: The cosine of a sum
type: theorem
level: object
kind: law
rung: C
order: 1084
setting: classical
equality: "≐"
domain: real
law: "([([(([J] [S])) (<[(([J] [S]))]>)] <[oo]>)] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)]) <([([(([J] [S])) <(<[(([J] [S]))]>)>] <[oo]> <[(([J] <[oo]>))]>)] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])> ≐ ([(([J] [S T])) (<[(([J] [S T]))]>)] <[oo]>)"
units: "cos π(s+t) = cos πs cos πt − sin πs sin πt"
gloss_check: "cos(pi*(S+T))"
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: untested
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "Ptolemy (c. 150) for the addition theorems; Euler 1748 for the exponential derivation"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.multiplication, C.cosine, C.sine, Z.subtraction, mult.involution, Z.collection, C.i-squared, C.phase-sign, C.phase-under-instance, Z.cancellation, mult.distribution, mult.inverse-promotion, Z.inversion, mult.cardinality, C.turn-of-sum, Q.reciprocal-of-product]
guarded_by: [mult.seam-decree]
see_also: [C.turn-of-sum, C.sine-addition, C.cosine, C.sine, C.euler-formula]
aliases: [cosine addition formula, "cos(s+t)", angle addition]
concepts: [trigonometry, phase, addition]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([cos πS] [cos πT]) <([sin πS] [sin πT])> ≐ cos π(S T)` | cos π(S+T) = `([(([J] [S T])) (<[(([J] [S T]))]>)] <[oo]>)` | cos(s+t) = cos s cos t − sin s sin t |

The addition formula for cosine, derived by expanding the product side: the mixed terms cancel, the pure terms double, and what remains is the cosine of the summed turn by [[C.turn-of-sum]].

## Plain

The cosine of a combined turn is the cosines multiplied minus the sines multiplied. Spell out both sides in turns and reverse turns, and all the cross terms die.

## Derivation

| form | rule | note |
|---|---|---|
| `([([(([J] [S])) (<[(([J] [S]))]>)] <[oo]>)] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)]) <([([(([J] [S])) <(<[(([J] [S]))]>)>] <[oo]> <[(([J] <[oo]>))]>)] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])>` | given | cos s cos t − sin s sin t: [[mult.multiplication]], [[C.cosine]], [[C.sine]], [[Z.subtraction]] |
| `([(([J] [S])) (<[(([J] [S]))]>)] <[oo]> [(([J] [T])) (<[(([J] [T]))]>)] <[oo]>) <([(([J] [S])) <(<[(([J] [S]))]>)>] <[oo]> <[(([J] <[oo]>))]> [(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)>` | [[mult.involution]] | the unit on each of the four abstracts, directly inside its instance — absorbing |
| `([(([J] [S])) (<[(([J] [S]))]>)] <[oo]> <[oo]> [(([J] [T])) (<[(([J] [T]))]>)]) <([(([J] [S])) <(<[(([J] [S]))]>)>] <[oo]> <[oo]> [(([J] [T])) <(<[(([J] [T]))]>)>] <[(([J] <[oo]>))] [(([J] <[oo]>))]>)>` | [[Z.collection]] | `<[i]> <[i]> ≐ <[i] [i]>` |
| `([(([J] [S])) (<[(([J] [S]))]>)] <[oo]> <[oo]> [(([J] [T])) (<[(([J] [T]))]>)]) <([(([J] [S])) <(<[(([J] [S]))]>)>] <[oo]> <[oo]> [(([J] [T])) <(<[(([J] [T]))]>)>] <[([(([J] <[oo]>))] [(([J] <[oo]>))])]>)>` | [[mult.involution]] | the unit right to left on `[i] [i]`, inside an angle directly inside the instance — absorbing |
| `([(([J] [S])) (<[(([J] [S]))]>)] <[oo]> <[oo]> [(([J] [T])) (<[(([J] [T]))]>)]) <([(([J] [S])) <(<[(([J] [S]))]>)>] <[oo]> <[oo]> [(([J] [T])) <(<[(([J] [T]))]>)>] <J>)>` | [[C.i-squared]] | `([i] [i]) ≐ <o>`, whose abstract is J |
| `([(([J] [S])) (<[(([J] [S]))]>)] <[oo]> <[oo]> [(([J] [T])) (<[(([J] [T]))]>)]) <([(([J] [S])) <(<[(([J] [S]))]>)>] <[oo]> <[oo]> [(([J] [T])) <(<[(([J] [T]))]>)>] J)>` | [[C.phase-sign]] | `(Y <J>) ≐ (Y J)` |
| `([(([J] [S])) (<[(([J] [S]))]>)] <[oo]> <[oo]> [(([J] [T])) (<[(([J] [T]))]>)]) <<([(([J] [S])) <(<[(([J] [S]))]>)>] <[oo]> <[oo]> [(([J] [T])) <(<[(([J] [T]))]>)>])>>` | [[C.phase-under-instance]] | the J becomes a sign |
| `([(([J] [S])) (<[(([J] [S]))]>)] <[oo]> <[oo]> [(([J] [T])) (<[(([J] [T]))]>)]) ([(([J] [S])) <(<[(([J] [S]))]>)>] <[oo]> <[oo]> [(([J] [T])) <(<[(([J] [T]))]>)>])` | [[Z.cancellation]] | two mirrors cancel: the difference has become a sum |
| `([(([J] [S])) (<[(([J] [S]))]>)] <[oo]> <[oo]> [(([J] [T]))]) ([(([J] [S])) (<[(([J] [S]))]>)] <[oo]> <[oo]> [(<[(([J] [T]))]>)]) ([(([J] [S])) <(<[(([J] [S]))]>)>] <[oo]> <[oo]> [(([J] [T]))]) ([(([J] [S])) <(<[(([J] [S]))]>)>] <[oo]> <[oo]> [<(<[(([J] [T]))]>)>])` | [[mult.distribution]] | distribute each product over its second factor |
| `(<[oo]> <[oo]> [(([J] [S]))] [(([J] [T]))]) (<[oo]> <[oo]> [(<[(([J] [S]))]>)] [(([J] [T]))]) (<[oo]> <[oo]> [(([J] [S]))] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> [(([J] [S]))] [(([J] [T]))]) (<[oo]> <[oo]> [<(<[(([J] [S]))]>)>] [(([J] [T]))]) (<[oo]> <[oo]> [(([J] [S]))] [<(<[(([J] [T]))]>)>]) (<[oo]> <[oo]> [<(<[(([J] [S]))]>)>] [<(<[(([J] [T]))]>)>])` | [[mult.distribution]] | and over the first: eight terms |
| `(<[oo]> <[oo]> [(([J] [S]))] [(([J] [T]))]) (<[oo]> <[oo]> [(<[(([J] [S]))]>)] [(([J] [T]))]) (<[oo]> <[oo]> [(([J] [S]))] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> [(([J] [S]))] [(([J] [T]))]) <(<[oo]> <[oo]> [(<[(([J] [S]))]>)] [(([J] [T]))])> <(<[oo]> <[oo]> [(([J] [S]))] [(<[(([J] [T]))]>)])> (<[oo]> <[oo]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)])` | [[mult.inverse-promotion]] [[Z.cancellation]] | mirrors out of the two mixed terms by inverse promotion; the doubly mirrored term loses both the same way, one after the other, and they cancel |
| `(<[oo]> <[oo]> [(([J] [S]))] [(([J] [T]))]) (<[oo]> <[oo]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> [(([J] [S]))] [(([J] [T]))]) (<[oo]> <[oo]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)])` | [[Z.inversion]] | the mixed terms cancel in pairs |
| `([(<[oo]> <[oo]> [(([J] [S]))] [(([J] [T]))])] [oo]) ([(<[oo]> <[oo]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)])] [oo])` | [[mult.cardinality]] | two copies of each survivor become the count 2 |
| `(<[oo]> <[oo]> [(([J] [S]))] [(([J] [T]))] [oo]) (<[oo]> <[oo]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)] [oo])` | [[mult.involution]] | the unit, directly inside each instance — absorbing |
| `(<[oo]> [(([J] [S]))] [(([J] [T]))]) (<[oo]> [(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)])` | [[Z.inversion]] | a `<[oo]>` cancels against the count in each: halves |
| `(<[oo]> [([(([J] [S]))] [(([J] [T]))])]) (<[oo]> [([(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)])])` | [[mult.involution]] | the unit right to left on each product, directly inside its instance — absorbing |
| `(<[oo]> [(([J] [S T]))]) (<[oo]> [([(<[(([J] [S]))]>)] [(<[(([J] [T]))]>)])])` | [[C.turn-of-sum]] | the product of the turns is the turn of the sum |
| `(<[oo]> [(([J] [S T]))]) (<[oo]> [(<[(([J] [S]))]> <[(([J] [T]))]>)])` | [[mult.involution]] | the unit on `[(<[X]>)]` and `[(<[Y]>)]`, directly inside their instance — absorbing |
| `(<[oo]> [(([J] [S T]))]) (<[oo]> [(<[([(([J] [S]))] [(([J] [T]))])]>)])` | [[Q.reciprocal-of-product]] | `(<[X]> <[Y]>) ≐ (<[([X] [Y])]>)`: the product of reciprocals is the reciprocal of the product |
| `(<[oo]> [(([J] [S T]))]) (<[oo]> [(<[(([J] [S T]))]>)])` | [[C.turn-of-sum]] | again, under the mirror |
| `([(([J] [S T])) (<[(([J] [S T]))]>)] <[oo]>)` | [[mult.distribution]] | collect over the shared `<[oo]>`, right to left: the cosine of the sum |

## Confirms

cos(s+t) = cos s cos t − sin s sin t, with the usual exponential proof made into rows. The whole formula is a shadow of [[C.turn-of-sum]]: XY is the turn of s + t and X̄Ȳ its reverse, and the cosine is half their sum. It is **not** proved for angles given geometrically — s and t are counts of J. The engine samples real counts; the same rows are exact for complex counts too (the cosine form is then the complex cosine, which is cosh along the imaginary axis), so the restriction is one of sampling, not of the law.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step directly under an instance |
| JH, JO | replaced | per slice |
| JP | untested | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Guarded by position (Amendment A2): the units on the abstracts of the four products, and on `[([X] [Y])]`, have content whose imaginary part is a sum of two principal arguments, off the strip when the angles add past a half-turn; all sit directly inside an instance — a seam step, admitted by the decree's position clause, so the law carries the decree in its price while its statement is exact in ℂ.

With [[C.pythagorean]], the longest derivation on the chart so far (21 rows); the engine checks every row on sampled real s, t, including the rows with eight summands.
