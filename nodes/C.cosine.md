---
id: C.cosine
title: Cosine — half the sum of a turn and its reverse
type: definition
level: object
kind: law
rung: C
order: 1060
setting: classical
equality: "≐"
domain: real
law: "cos πT := ([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)"
units: "cos πt = (e^{iπt} + e^{−iπt}) / 2"
gloss_check: "cos(pi*T)"
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
known_since: "Euler 1748 for cos as half the sum of the exponentials; 1993 (James, Ch. 6 §6.5.3 p. 49) for its spelling in forms, in radians"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [Q.division, Q.reciprocal, C.polar-form, N.numeral]
see_also: [C.sine, C.euler-formula, C.polar-form]
aliases: [cosine, cos, "cos θ"]
concepts: [trigonometry, phase, complex-number]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)` | — | cos πt = (e^{iπt} + e^{−iπt}) / 2 |

Write X for the pure phase `(([J] [T]))`, a turn of t half-turns. Then the cosine is (X + 1/X) ÷ 2: the turn and its reverse added, halved. Cosine is *defined* here, from the phase; it is not a ratio of sides. James's cosine (p. 49) is the same construction in radians: `([(([x] ([J] <[oo]>))) ((<[x]> ([J] <[oo]>)))] <[oo]>)`, with e^{ix} as the instance of x times i — the chart's half-turn count T is his x/π.

## Plain

Turn by some angle, and also by the opposite angle; add the two results and halve. What is left is how far along the real line you went: the cosine.

## Derivation

| form | rule | note |
|---|---|---|
| `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>)` | [[Q.division]] | (X + 1/X) ÷ 2 with X = `(([J] [T]))` the pure phase of [[C.polar-form]], 1/X = `(<[X]>)` by [[Q.reciprocal]], and 2 the pile `oo` ([[N.numeral]]) |
| `cos πT` | name | — |

## Confirms

Euler's cos θ = (e^{iθ} + e^{−iθ})/2 taken as the definition, with θ = πt — the order of exposition of a complex-analysis course, not of a geometry one. The angle is in half-turns because the count is of J. It is **not** a geometric definition and does not need one: the right triangle enters the chart, if at all, at the rung `analysis` where lengths are. The form has 23 boundaries.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | a definition with no Λ-step |
| JH, JO | replaced | per slice, cos is slice-independent as a *value* (the real part of a turn is the same in every slice) but the form carries the slice's J_u |
| JP | guarded | for integer turns, where the turn is a torsion power ±1 and the cosine ±1; a fractional turn is a form only by the selection rule ([[place.selection]]); the analytic p-adic cosine on the radius is another object, owed to rung `analysis` |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

At t = ½ the sum X + 1/X is void, its abstract is the black hole, and the whole is `(□ <[oo]>) ≐ void` — cos(π/2) = 0 is reached through the hole rules.
