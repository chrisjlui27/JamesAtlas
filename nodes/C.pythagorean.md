---
id: C.pythagorean
title: Cosine squared plus sine squared is one
type: theorem
level: object
kind: law
rung: C
order: 1082
setting: classical
equality: "≐"
domain: real
law: "([([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)]) ([([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)]) ≐ o"
units: "cos² πt + sin² πt = 1"
gloss_check: "1"
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
known_since: "Pythagoras, for the triangle; from the exponential forms, Euler 1748"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.multiplication, C.cosine, C.sine, mult.involution, Z.collection, C.i-squared, C.phase-sign, C.phase-under-instance, mult.distribution, mult.inverse-promotion, Z.cancellation, Z.inversion, mult.cardinality, mult.product-of-numerals]
guarded_by: [mult.seam-decree]
see_also: [C.cosine, C.sine, C.euler-formula, Q.reciprocal-law, C.turn-of-sum]
aliases: [Pythagorean identity, "cos² + sin² = 1"]
concepts: [trigonometry, phase, one]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([cos πT] [cos πT]) ([sin πT] [sin πT]) ≐ o` | with cos πT = `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)` and sin πT = `([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)` | cos² θ + sin² θ = 1 |

The Pythagorean identity, as the statement that a turn times its reverse is one. Every term of the two squares cancels except four copies of X X̄/4.

## Plain

How-far-along squared plus how-far-up squared is one: a turn has length one. On the page, the squares expand, almost everything cancels, and what is left is a turn times the reverse turn.

## Derivation

| form | rule | note |
|---|---|---|
| `([([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)]) ([([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])` | given | cos² + sin²: [[mult.multiplication]], [[C.cosine]], [[C.sine]] |
| `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]> [(([J] [T])) (<[(([J] [T]))]>)] <[oo]>) ([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]> [(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)` | [[mult.involution]] | the unit on each of the four abstracts, directly inside its instance — absorbing |
| `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]> <[oo]> [(([J] [T])) (<[(([J] [T]))]>)]) ([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[oo]> [(([J] [T])) <(<[(([J] [T]))]>)>] <[(([J] <[oo]>))] [(([J] <[oo]>))]>)` | [[Z.collection]] | `<[i]> <[i]> ≐ <[i] [i]>` |
| `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]> <[oo]> [(([J] [T])) (<[(([J] [T]))]>)]) ([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[oo]> [(([J] [T])) <(<[(([J] [T]))]>)>] <[([(([J] <[oo]>))] [(([J] <[oo]>))])]>)` | [[mult.involution]] | the unit right to left on `[i] [i]`, inside an angle directly inside the instance — absorbing |
| `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]> <[oo]> [(([J] [T])) (<[(([J] [T]))]>)]) ([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[oo]> [(([J] [T])) <(<[(([J] [T]))]>)>] <J>)` | [[C.i-squared]] | `([i] [i]) ≐ <o>`, whose abstract is J: dividing by i² is a mirrored half-turn |
| `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]> <[oo]> [(([J] [T])) (<[(([J] [T]))]>)]) ([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[oo]> [(([J] [T])) <(<[(([J] [T]))]>)>] J)` | [[C.phase-sign]] | `(Y <J>) ≐ (Y J)` |
| `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]> <[oo]> [(([J] [T])) (<[(([J] [T]))]>)]) <([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[oo]> [(([J] [T])) <(<[(([J] [T]))]>)>])>` | [[C.phase-under-instance]] | the J becomes a sign: cos² + sin² is (X + X̄)²/4 − (X − X̄)²/4 |
| `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]> <[oo]> [(([J] [T]))]) ([(([J] [T])) (<[(([J] [T]))]>)] <[oo]> <[oo]> [(<[(([J] [T]))]>)]) <([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[oo]> [(([J] [T]))]) ([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[oo]> [<(<[(([J] [T]))]>)>])>` | [[mult.distribution]] | distribute each square over its second factor |
| `(<[oo]> <[oo]> [(([J] [T]))] [(([J] [T]))]) (<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> [(<[(([J] [T]))]>)] [(<[(([J] [T]))]>)]) <(<[oo]> <[oo]> [(([J] [T]))] [(([J] [T]))]) (<[oo]> <[oo]> [(([J] [T]))] [<(<[(([J] [T]))]>)>]) (<[oo]> <[oo]> [<(<[(([J] [T]))]>)>] [(([J] [T]))]) (<[oo]> <[oo]> [<(<[(([J] [T]))]>)>] [<(<[(([J] [T]))]>)>])>` | [[mult.distribution]] | and over the first: four terms each |
| `(<[oo]> <[oo]> [(([J] [T]))] [(([J] [T]))]) (<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> [(<[(([J] [T]))]>)] [(<[(([J] [T]))]>)]) <(<[oo]> <[oo]> [(([J] [T]))] [(([J] [T]))]) <(<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)])> <(<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)])> (<[oo]> <[oo]> [(<[(([J] [T]))]>)] [(<[(([J] [T]))]>)])>` | [[mult.inverse-promotion]] [[Z.cancellation]] | mirrors out of the two cross terms by inverse promotion; the two mirrors of the last term come out the same way, one after the other, and cancel — the product of negatives, done with its context in place |
| `(<[oo]> <[oo]> [(([J] [T]))] [(([J] [T]))]) (<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> [(<[(([J] [T]))]>)] [(<[(([J] [T]))]>)]) <(<[oo]> <[oo]> [(([J] [T]))] [(([J] [T]))])> (<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)]) <(<[oo]> <[oo]> [(<[(([J] [T]))]>)] [(<[(([J] [T]))]>)])>` | [[Z.collection]] [[Z.cancellation]] | the outer mirror distributes over the four terms, right to left; double mirrors cancel |
| `(<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)]) (<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)])` | [[Z.inversion]] | X²/4 and X̄²/4 cancel against their mirrors: four copies of X X̄/4 remain |
| `([(<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)])] [oo]) ([(<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)])] [oo])` | [[mult.cardinality]] | two pairs, each one copy with the count 2 |
| `([(<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)])] [oo oo])` | [[mult.distribution]] | collect the counts: 4 |
| `(<[oo]> <[oo]> [(([J] [T]))] [(<[(([J] [T]))]>)] [oooo])` | [[mult.involution]] | the unit, directly inside the instance — absorbing |
| `(<[oo] [oo]> [(([J] [T]))] [(<[(([J] [T]))]>)] [oooo])` | [[Z.collection]] | the two mirrored counts collect |
| `(<[([oo] [oo])]> [(([J] [T]))] [(<[(([J] [T]))]>)] [oooo])` | [[mult.involution]] | the unit right to left on `[oo] [oo]`, inside an angle directly inside the instance — absorbing |
| `(<[oooo]> [(([J] [T]))] [(<[(([J] [T]))]>)] [oooo])` | [[mult.product-of-numerals]] | 2 × 2 = 4 — an instance of that law's schema (its stated case is 3 × 2) |
| `([(([J] [T]))] [(<[(([J] [T]))]>)])` | [[Z.inversion]] | the count 4 and its mirror cancel: X X̄ |
| `([(([J] [T]))] <[(([J] [T]))]>)` | [[mult.involution]] | the unit on `[(<[X]>)]`, directly inside the instance — absorbing |
| `o` | [[Z.inversion]] | `[X] <[X]>` cancels, leaving the instance of nothing — which is `o` |

## Confirms

cos² + sin² = 1 from the exponential definitions: (X + X̄)²/4 − (X − X̄)²/4 = X X̄ = 1. Twenty-one rows, because the page expands the squares by hand; but the content is one fact, `([X] [(<[X]>)]) ≐ o`, which is the reciprocal law. It is **not** the theorem of Pythagoras about triangles — no lengths, no right angle — but the identity that will *become* it when the rung `analysis` reads lengths into moduli; and it is **not** a definition of the circle, which the page does not have.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step directly under an instance, through an angle at most |
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

Guarded by position (Amendment A2): the units on the two sine abstracts have content ln|sin πt| − iπ when the sine is negative, off the half-open strip; so does `[(<[X]>)]` at odd t (content −iπ) and the unit on `[P]` in row 15 (P the product term; content 2πi at odd t); all sit directly inside an instance — a seam step, admitted by the decree's position clause, so the law carries the decree in its price while its statement is exact in ℂ.

The i² = −1 that turns the minus of the sine-square into a plus is [[C.i-squared]] followed by [[C.phase-sign]] and [[C.phase-under-instance]]: `<[i] [i]>` is `<J>`, and `<J>` under an instance is J, which is a sign.
