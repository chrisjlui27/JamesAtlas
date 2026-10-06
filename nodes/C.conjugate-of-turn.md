---
id: C.conjugate-of-turn
title: The conjugate of a turn is the reverse turn
type: theorem
level: object
kind: law
rung: C
order: 1081
setting: classical
equality: "≐"
domain: positive
law: "([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>) <([(([J] <[oo]>))] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])> ≐ (([J] [<T>]))"
units: "cos πt − i sin πt = e^{−iπt}"
gloss_check: "exp(-1j*pi*T)"
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
known_since: "Euler 1748"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [C.conjugate, C.cosine, C.sine, C.imaginary-unit, mult.multiplication, mult.inverse-promotion, C.cosine-even, C.sine-odd, C.euler-formula]
see_also: [C.conjugate, C.euler-formula, C.cosine-even, C.sine-odd, C.reverse-turn]
aliases: [conjugate of a turn, "e^{−iθ} = cos θ − i sin θ"]
concepts: [trigonometry, phase, complex-number]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>) <([i] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])> ≐ (([J] [<T>]))` | cos πT <([i] [sin πT])> ≐ the turn by −T | cos θ − i sin θ = e^{−iθ} |

Euler's formula for the conjugate: the rectangular conjugate of cos + i sin ([[C.conjugate]]) is the polar conjugate, the turn by −t. The two spellings of "conjugate" agree.

## Plain

Flip the up-and-down part of a turn and you have turned the other way. The rectangular flip and the polar flip are the same flip.

## Derivation

| form | rule | note |
|---|---|---|
| `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>) <([(([J] <[oo]>))] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])>` | given | the conjugate of cos πt + i sin πt, in the shape of [[C.conjugate]]: [[C.cosine]], [[C.sine]], [[C.imaginary-unit]], [[mult.multiplication]] |
| `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>) ([(([J] <[oo]>))] [<([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)>])` | [[mult.inverse-promotion]] | the mirror moves onto the sine |
| `([(([J] [<T>])) (<[(([J] [<T>]))]>)] <[oo]>) ([(([J] <[oo]>))] [([(([J] [<T>])) <(<[(([J] [<T>]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])` | [[C.cosine-even]] [[C.sine-odd]] | cos πt is cos(−πt), and −sin πt is sin(−πt): right to left, both |
| `(([J] [<T>]))` | [[C.euler-formula]] | Euler's formula at the count `<T>`, right to left: the turn by −t |

## Confirms

cos θ − i sin θ = e^{−iθ}: Euler's formula at −θ, with the evenness of cosine and oddness of sine carrying the sign. This is the theorem that lets the conjugate of a number be read off either spelling; with [[C.modulus-squared]] it gives z z̄ = r² for the polar form, since `([turn] [reverse turn])` is `o` by [[C.turn-of-sum]]. It is **not** a new definition of the conjugate — there is none for a general form — but the agreement of the two the chart has.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | inherits [[C.euler-formula]], [[C.cosine-even]] and [[C.sine-odd]], all exact |
| JH, JO | replaced | per slice, with u for i |
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

—
