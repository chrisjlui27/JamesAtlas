---
id: C.cosine-even
title: Cosine is even
type: theorem
level: object
kind: law
rung: C
order: 1072
setting: classical
equality: "≐"
domain: positive
law: "([(([J] [<T>])) (<[(([J] [<T>]))]>)] <[oo]>) ≐ ([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)"
units: "cos(−πt) = cos πt"
gloss_check: "cos(pi*T)"
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
known_since: "classical; from the exponential forms, Euler 1748"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [C.cosine, C.reverse-turn, mult.involution, Z.cancellation]
guarded_by: [mult.seam-decree]
see_also: [C.cosine, C.sine-odd, C.reverse-turn, C.conjugate-of-turn]
aliases: [cosine is even, "cos(−θ) = cos θ"]
concepts: [trigonometry, phase]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([(([J] [<T>])) (<[(([J] [<T>]))]>)] <[oo]>) ≐ ([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)` | cos(−πT) ≐ cos πT | cos(−θ) = cos θ |

The cosine of a mirrored count is the cosine of the count: the turn and its reverse trade places inside the sum, which does not care.

## Plain

Turning the other way gives the same how-far-along: the cosine does not see the sign of the angle.

## Derivation

| form | rule | note |
|---|---|---|
| `([(([J] [<T>])) (<[(([J] [<T>]))]>)] <[oo]>)` | given | the cosine of −t: [[C.cosine]] with the count `<T>` |
| `([(<[(([J] [T]))]>) (<[(<[(([J] [T]))]>)]>)] <[oo]>)` | [[C.reverse-turn]] | the turn by −t is 1 over the turn by t, right to left — at both occurrences |
| `([(<[(([J] [T]))]>) (<<[(([J] [T]))]>>)] <[oo]>)` | [[mult.involution]] | the unit on `[(<[X]>)]`, inside an angle directly inside an instance — absorbing through the angle |
| `([(<[(([J] [T]))]>) ([(([J] [T]))])] <[oo]>)` | [[Z.cancellation]] | two mirrors cancel |
| `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)` | [[mult.involution]] | the counit `([X]) ≐ X`: what is left is the cosine of t |

## Confirms

cos(−θ) = cos θ, from the definition: the cosine is (X + X̄)/2 and replacing t by −t swaps X and X̄ ([[C.reverse-turn]]). It is **not** a geometric fact here — no triangle — and it is the first of the two symmetry laws Euler's formula needs to produce the conjugate of a turn ([[C.conjugate-of-turn]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | all unit steps absorbing; inherits [[C.reverse-turn]] |
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

Guarded by position (Amendment A2): the unit on `[(<[X]>)]` has content −Ln X, which is −iπ — off the half-open strip — whenever t is an odd integer; it sits inside an angle directly inside an instance — a seam step, admitted by the decree's position clause, so the law carries the decree in its price while its statement is exact in ℂ.
