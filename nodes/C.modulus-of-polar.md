---
id: C.modulus-of-polar
title: The modulus of the polar form is its r
type: theorem
level: object
kind: law
rung: C
order: 1083
setting: classical
equality: "≐"
domain: positive
law: "(([[([([R] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)])] [([R] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)])]) ([([R] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])] [([R] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])])]] <[oo]>)) ≐ R"
units: "|r cos πt + i r sin πt| = r  (r > 0)"
gloss_check: "R"
holds:
  classical: holds
  J1: guarded
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
known_since: "Wessel 1797 (length and direction); Argand 1806 (the modulus by name)"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [C.polar-form, mult.involution, C.euler-formula, mult.distribution, C.complex-number, C.modulus, C.pythagorean, alg.log-law, mult.cardinality, Z.inversion, mult.log-of-one]
guarded_by: [mult.seam-decree]
see_also: [C.modulus, C.pythagorean, C.polar-form, alg.log-law]
aliases: [modulus of the polar form, "|r e^{iθ}| = r"]
concepts: [complex-number, root, trigonometry]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[([([R] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)])] [([R] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)])]) ([([R] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])] [([R] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])])]] <[oo]>)) ≐ R` | the modulus of the rectangular parts of `([R] ([J] [T]))`, which the bridge below shows are `([R] [cos πT])` and `([R] [sin πT])` | √((r cos θ)² + (r sin θ)²) = r |

The two spellings of size agree: the polar form `([R] ([J] [T]))` is, by Euler's formula, the rectangular number with parts r cos πt and r sin πt (the bridge table), and the modulus of that number ([[C.modulus]]) is r. The Pythagorean identity does the work.

## Plain

Measure the length of a size-and-turn number by squaring its two parts and adding: the turn drops out, because cosine squared plus sine squared is one, and the length is the size.

## Derivation

First, the bridge: the polar form's rectangular parts are r cos πt and r sin πt —

| form | rule | note |
|---|---|---|
| `([R] ([J] [T]))` | given | the polar form, [[C.polar-form]] |
| `([R] [(([J] [T]))])` | [[mult.involution]] | the unit right to left on the turn `([J] [T])`, directly inside the instance — absorbing (content iπt, off the strip for |t| > 1: guarded by position) |
| `([R] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>) ([(([J] <[oo]>))] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])])` | [[C.euler-formula]] | the turn is its cosine plus i times its sine, inside the square |
| `([R] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)]) ([R] [([(([J] <[oo]>))] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])])` | [[mult.distribution]] | distribute `[R]` over the two parts |
| `([R] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)]) ([R] [(([J] <[oo]>))] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])` | [[mult.involution]] | the unit on `[([i] [sin])]`, directly inside its instance — absorbing |
| `([R] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)]) ([([R] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])] [(([J] <[oo]>))])` | [[mult.involution]] | the unit right to left on `[R] [sin πT]` — absorbing: the rectangular parts are r cos πt and r sin πt, in the shape of [[C.complex-number]] |

Then the modulus of that rectangular number:

| form | rule | note |
|---|---|---|
| `(([[([([R] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)])] [([R] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)])]) ([([R] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])] [([R] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])])]] <[oo]>))` | given | the modulus of r cos πt + i r sin πt, [[C.modulus]] with a = `([R] [cos πT])`, b = `([R] [sin πT])` |
| `(([[([R] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)] [R] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)]) ([R] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)] [R] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])]] <[oo]>))` | [[mult.involution]] | the unit on each of the four `[([R] [cos])]`, `[([R] [sin])]`, directly inside its instance — absorbing |
| `(([[([R] [R] [([([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)])]) ([R] [R] [([([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])])]] <[oo]>))` | [[mult.involution]] | the unit right to left on `[cos] [cos]` and on `[sin] [sin]`, directly inside their instances — absorbing |
| `(([[([R] [R] [([([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)] [([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)]) ([([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])])]] <[oo]>))` | [[mult.distribution]] | collect over the shared `[R] [R]`, right to left: r²(cos² + sin²) |
| `(([[([R] [R] [o])]] <[oo]>))` | [[C.pythagorean]] | cos² + sin² ≐ 1 |
| `(([[([R] [R])]] <[oo]>))` | [[mult.log-of-one]] | `[o] ≐ void`: the square of the modulus is r² |
| `(([[R] [R]] <[oo]>))` | [[alg.log-law]] | `[([R] [R])] ≐ [R] [R]` — the log of the product, under a square where nothing absorbs: admitted because 2 ln r is real (guarded by content, inherited) |
| `(([([[R]] [oo])] <[oo]>))` | [[mult.cardinality]] | `[R] [R] ≐ ([[R]] [oo])`: two copies of the log are the log with the count 2 |
| `(([[R]] [oo] <[oo]>))` | [[mult.involution]] | the unit on `[([[R]] [oo])]`, directly inside the inner instance — absorbing |
| `(([[R]]))` | [[Z.inversion]] | the count 2 and its mirror cancel: the half of the double log |
| `([R])` | [[mult.involution]] | the counit `([Y]) ≐ Y` with Y = `[R]` |
| `R` | [[mult.involution]] | and again: the modulus of r e^{iπt} is r |

## Confirms

|r e^{iθ}| = r, for positive r: r²(cos² + sin²) = r², and √(r²) = r. The last step is the one that costs: `√(r²) ≐ r` goes through the log law under a square — a unit step nothing absorbs, admitted because 2 ln r is real — so the law is guarded by content — the same step as [[alg.log-law]], taken here on `[R] [R]` — and would be *false* for negative r (√(r²) = |r|). It is **not** the triangle inequality or any other metric fact: those wait for the rung `analysis`.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | guarded | the log-law step ([[alg.log-law]], a law with a posted receipt) is used under a square, where ≃ does not pass — an import of the reading's receipt check; every other unit step is absorbed by an instance (the prover lists them, with the receipts paid on the spot, on the card's 𝕁₁ tape) |
| JH, JO | replaced | per slice; the quaternionic modulus has four parts |
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

Guarded by content and by position (Amendment A2). By content: the log-law step `[([R] [R])] → [R] [R]` sits under a square, where nothing absorbs, and is admitted because its content 2 ln r is real. By position: the right-to-left units on `[cos πT] [cos πT]` and `[sin πT] [sin πT]` in the second table have content 2 Ln(cos πt), resp. 2 Ln(sin πt), which is 2 ln|cos πt| + 2πi whenever the cosine is negative (t = 0.75: −0.693 + 6.283i) — off the strip — and sit directly inside an instance; so does the unit on the turn in the bridge for |t| > 1. The units on `[([R] [cos πT])]` themselves are free: their content ln r + Ln(cos πt) has imaginary part 0 or π, on the strip. The law carries the decree in its price on both counts.
