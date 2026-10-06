---
id: C.sine
title: Sine — half the difference of a turn and its reverse, over i
type: definition
level: object
kind: law
rung: C
order: 1070
setting: classical
equality: "≐"
domain: real
law: "sin πT := ([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)"
units: "sin πt = (e^{iπt} − e^{−iπt}) / 2i"
gloss_check: "sin(pi*T)"
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
known_since: "Euler 1748; 1993 (James) for the spelling"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [Q.division, Q.reciprocal, Z.subtraction, C.polar-form, C.imaginary-unit, N.numeral]
see_also: [C.cosine, C.euler-formula]
aliases: [sine, sin, "sin θ"]
concepts: [trigonometry, phase, complex-number]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)` | `([X <(<[X]>)>] <[oo]> <[i]>)` | sin πt = (e^{iπt} − e^{−iπt}) / 2i |

With X the pure phase: (X − 1/X) ÷ 2 ÷ i. The turn minus its reverse leaves only the imaginary part, doubled; halve it and take out the i.

## Plain

Turn by an angle and by the opposite angle; subtract. Only the up-and-down part survives, twice over, in the direction of i: halve it and divide the i out, and you have how far up you went.

## Derivation

| form | rule | note |
|---|---|---|
| `([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)` | [[Q.division]] | (X − 1/X) ÷ 2 ÷ i, with X = `(([J] [T]))` ([[C.polar-form]]), 1/X = `(<[X]>)` ([[Q.reciprocal]]), the difference by [[Z.subtraction]], 2 the pile ([[N.numeral]]) and i = `(([J] <[oo]>))` ([[C.imaginary-unit]]) |
| `sin πT` | name | — |

## Confirms

Euler's sin θ = (e^{iθ} − e^{−iθ})/2i as the definition. Together with [[C.cosine]] this gives trigonometry its two functions with no geometry spent; that they reassemble the turn is [[C.euler-formula]]. The form has 36 boundaries, the largest *named* form in the chart so far (the sides of the cube-root laws are larger) — a reminder that the calculus is an *assembly language* for ℂ, in which the standard names are abbreviations worth having. What sine is **not**, here: a ratio of lengths, or anything periodic *by definition* — its period is inherited from [[C.period-absorption]] through the phase.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | a definition with no Λ-step |
| JH, JO | replaced | as [[C.cosine]]: the imaginary part of a turn is in the slice's direction u, so `sin` divided by u is slice-independent as a value |
| JP | guarded | needs i: a form at p ≡ 1 mod 4 only ([[place.selection]]); there, for integer turns, it is 0 or ±i |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

At integer t the difference X − 1/X is void and the value passes through the black hole to 0, as for the cosine at half-integers.
