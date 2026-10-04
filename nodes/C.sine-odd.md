---
id: C.sine-odd
title: Sine is odd
type: theorem
level: object
kind: law
rung: C
order: 1074
setting: classical
equality: "≐"
domain: positive
law: "([(([J] [<T>])) <(<[(([J] [<T>]))]>)>] <[oo]> <[(([J] <[oo]>))]>) ≐ <([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)>"
units: "sin(−πt) = −sin πt"
gloss_check: "-sin(pi*T)"
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
uses: [C.sine, mult.inverse-promotion, Z.collection, Z.cancellation, mult.involution, C.reverse-turn]
guarded_by: [mult.seam-decree]
see_also: [C.sine, C.cosine-even, C.reverse-turn, C.conjugate-of-turn]
aliases: [sine is odd, "sin(−θ) = −sin θ"]
concepts: [trigonometry, phase, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([(([J] [<T>])) <(<[(([J] [<T>]))]>)>] <[oo]> <[(([J] <[oo]>))]>) ≐ <([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)>` | sin(−πT) ≐ <sin πT> | sin(−θ) = −sin θ |

The sine of a mirrored count is the mirror of the sine: the difference X − X̄ changes sign when the turn and its reverse trade places.

## Plain

Turning the other way gives the opposite how-far-up: the sine flips with the angle.

## Derivation

| form | rule | note |
|---|---|---|
| `<([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)>` | given | minus the sine of t, [[C.sine]] |
| `([<(([J] [T])) <(<[(([J] [T]))]>)>>] <[oo]> <[(([J] <[oo]>))]>)` | [[mult.inverse-promotion]] | `<(C [Y])> ≐ (C [<Y>])` with C = `<[oo]> <[i]>` and Y = `X <X̄>` |
| `([<(([J] [T]))> (<[(([J] [T]))]>)] <[oo]> <[(([J] <[oo]>))]>)` | [[Z.collection]] | the mirror of the pile is the pile of mirrors, right to left; then [[Z.cancellation]] removes the double mirror on X̄ |
| `([<([(([J] [T]))])> (<[(([J] [T]))]>)] <[oo]> <[(([J] <[oo]>))]>)` | [[mult.involution]] | the counit right to left: X ≐ `([X])` |
| `([<(<<[(([J] [T]))]>>)> (<[(([J] [T]))]>)] <[oo]> <[(([J] <[oo]>))]>)` | [[Z.cancellation]] | right to left: a double mirror inside the instance |
| `([<(<[(<[(([J] [T]))]>)]>)> (<[(([J] [T]))]>)] <[oo]> <[(([J] <[oo]>))]>)` | [[mult.involution]] | the unit right to left on `<[X]>` → `<[(<[X]>)]>`, inside an angle directly inside an instance — absorbing through the angle |
| `([(([J] [<T>])) <(<[(([J] [<T>]))]>)>] <[oo]> <[(([J] <[oo]>))]>)` | [[C.reverse-turn]] | right to left at both occurrences of `(<[X]>)`: this is the sine of −t |

## Confirms

sin(−θ) = −sin θ, from the definition. The derivation runs from −sin t to sin(−t): the outer mirror is promoted into the difference, where it swaps the two turns. It is **not** derived from cos(−θ) = cos θ, nor the other way round; the two are the even and odd parts of the same swap.

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

Guarded by position (Amendment A2): as [[C.cosine-even]] — a seam step, admitted by the decree's position clause, so the law carries the decree in its price while its statement is exact in ℂ.

The derivation is written from the right-hand side to the left; the engine accepts either direction.
