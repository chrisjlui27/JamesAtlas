---
id: C.modulus-squared
title: A number times its conjugate is the sum of two squares
type: theorem
level: object
kind: law
rung: C
order: 1058
setting: classical
equality: "≐"
domain: real
law: "([A ([B] [(([J] <[oo]>))])] [A <([B] [(([J] <[oo]>))])>]) ≐ ([A] [A]) ([B] [B])"
units: "(a + bi)(a − bi) = a² + b²"
gloss_check: "A*A + B*B"
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
known_since: "Bombelli 1572; the modulus as a named quantity, Argand 1806"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.multiplication, C.complex-number, C.conjugate, mult.distribution, mult.inverse-promotion, Z.inversion, mult.involution, C.i-squared, C.phase-under-instance, Z.cancellation]
guarded_by: [mult.seam-decree]
see_also: [C.conjugate, C.modulus, C.complex-quotient, C.i-squared]
aliases: ["z z̄ = a² + b²", modulus squared, norm]
concepts: [complex-number, multiplication]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A ([B] [i])] [A <([B] [i])>]) ≐ ([A] [A]) ([B] [B])` | with i = `(([J] <[oo]>))` | (a + bi)(a − bi) = a² + b² |

z z̄ = a² + b²: the product of a complex number with its conjugate is real and non-negative. The i² = −1 that makes the cross term change sign is [[C.i-squared]], inside an instance, becoming a sign by way of J.

## Plain

Multiply a complex number by its flipped twin: the i-parts cancel in the middle, and the last term, minus b times b times i times i, comes out as plus b squared.

## Derivation

| form | rule | note |
|---|---|---|
| `([A ([B] [(([J] <[oo]>))])] [A <([B] [(([J] <[oo]>))])>])` | given | z times its conjugate, [[mult.multiplication]]: [[C.complex-number]] and [[C.conjugate]] with the same a, b |
| `([A ([B] [(([J] <[oo]>))])] [A]) ([A ([B] [(([J] <[oo]>))])] [<([B] [(([J] <[oo]>))])>])` | [[mult.distribution]] | distribute `[a + bi]` over `a <bi>` |
| `([A] [A]) ([A] [([B] [(([J] <[oo]>))])]) ([<([B] [(([J] <[oo]>))])>] [A]) ([<([B] [(([J] <[oo]>))])>] [([B] [(([J] <[oo]>))])])` | [[mult.distribution]] | distribute `[a]` and `[<bi>]` over `a bi` |
| `([A] [A]) ([A] [([B] [(([J] <[oo]>))])]) <([([B] [(([J] <[oo]>))])] [A])> ([<([B] [(([J] <[oo]>))])>] [([B] [(([J] <[oo]>))])])` | [[mult.inverse-promotion]] | `([A] [<Y>]) ≐ <([A] [Y])>` with Y = bi |
| `([A] [A]) ([<([B] [(([J] <[oo]>))])>] [([B] [(([J] <[oo]>))])])` | [[Z.inversion]] | the cross terms a·bi and −a·bi cancel |
| `([A] [A]) <([([B] [(([J] <[oo]>))])] [([B] [(([J] <[oo]>))])])>` | [[mult.inverse-promotion]] | the remaining mirror comes out: −(bi)(bi) |
| `([A] [A]) <([B] [(([J] <[oo]>))] [B] [(([J] <[oo]>))])>` | [[mult.involution]] | the unit on each `[([B] [i])]`, directly inside the instance — absorbing |
| `([A] [A]) <([B] [B] [([(([J] <[oo]>))] [(([J] <[oo]>))])])>` | [[mult.involution]] | the unit right to left on `[i] [i]`, directly inside the instance — absorbing (content iπ, on the edge of the strip) |
| `([A] [A]) <([B] [B] [<o>])>` | [[C.i-squared]] | `([i] [i]) ≐ <o>` — and `[<o>]` is J |
| `([A] [A]) <<([B] [B])>>` | [[C.phase-under-instance]] | `(Y J) ≐ <(Y)>` with Y = `[B] [B]`: the J becomes a sign |
| `([A] [A]) ([B] [B])` | [[Z.cancellation]] | two mirrors cancel: a² + b² |

## Confirms

The identity behind the modulus and behind division: (a + bi)(a − bi) = a² − (bi)² = a² + b². On the page, Distribution twice, two cancellations by inverse promotion, and the i² step — which is [[C.i-squared]] followed by J becoming a sign under an instance ([[C.phase-under-instance]]). It is **not** yet the modulus |z| = √(a² + b²): that is the root of this ([[C.modulus]]), and the triangle inequality for it is analysis, not algebra.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step directly under an instance |
| JH, JO | replaced | the quaternionic norm is a sum of four squares, and `x conj(x)` is central; the two-term identity is one slice of it |
| JP | guarded | as [[C.imaginary-unit]] |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Guarded by position (Amendment A2): the units on `[([B] [i])]` have content ln b + iπ/2, which for negative b is ln|b| + 3πi/2, off the strip; they sit directly inside an instance — a seam step, admitted by the decree's position clause, so the law carries the decree in its price while its statement is exact in ℂ.
