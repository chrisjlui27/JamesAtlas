---
id: C.polar-form
title: Polar form — the angle is a count of J
type: definition
level: object
kind: law
rung: C
order: 1050
setting: classical
equality: "≐"
domain: real
law: "R·e^{iπT} := ([R] ([J] [T]))"
units: "r e^{iπt}  (t in half-turns)"
gloss_check: "R*exp(1j*pi*T)"
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James: angle measured in units of J); Euler 1748; Argand 1806"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.multiplication, C.phase, mult.involution]
guarded_by: [mult.seam-decree]
see_also: [C.complex-number, C.period-absorption, C.cosine, C.sine]
aliases: [polar form, "r e^{iθ}", modulus and argument, half-turns]
concepts: [complex-number, phase, exponential]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([R] ([J] [T]))` | — | r · e^{iπt}, the angle t measured in half-turns |

The log of a modulus beside a count of J, under one instance (a negative R folds its sign into the phase: `[R]` then carries a J of its own). The chart measures angles as counts of J — half-turns — which is why no π appears in the form; James's own trigonometry (p. 49) measures in radians, writing e^{ix} as `(([x] ([J] <[oo]>)))`, x times i; the two conventions differ by the factor π = `([J] <[i]>)`.

## Plain

Any complex number is a size and a turn. The size goes in as a log, the turn as "so many J", and one circle around both makes the number.

## Derivation

| form | rule | note |
|---|---|---|
| `([R] [(([J] [T]))])` | [[mult.multiplication]] | r × e^{iπt}: the magnitude times the pure phase `(([J] [T]))`, J with the count t ([[C.phase]]) |
| `([R] ([J] [T]))` | [[mult.involution]] | the unit on `[(([J] [T]))]`, directly inside the instance — absorbing; for |t| > 1 the content iπt is off the strip and the instance absorbs the difference (a seam step: guarded by position) |
| `R·e^{iπT}` | name | — |

## Confirms

The polar form r e^{iθ} with θ = πt. Multiplication of complex numbers in polar form is the addition of logs and of counts — `([R₁] ([J][T₁])) × ([R₂] ([J][T₂]))` collects under one instance by the exponential law — and division is the mirror. The angle-addition formulas of trigonometry follow from these two moves applied to the cosine and sine forms ([[C.turn-of-sum]], [[C.cosine-addition]], [[C.sine-addition]]); the product with moduli is [[C.polar-product]]. It is **not** canonical: t and t + 2 give the same value by [[C.period-absorption]], and the form does not reduce one to the other; a principal t ∈ (−1, 1] is a choice made in the reading.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the unit step is directly under an instance |
| JH, JO | replaced | `([r] ([J_u][t]))` per slice — the polar form of a quaternion needs the direction u as a third datum, and products across slices do not stay in polar form (JH Ch. 14) |
| JP | holds | for the integer turns of the page: `(([T][J]))` is the torsion power (−1)^T at p. The place's own polar form — a power of p, a torsion element, a principal unit — is [[place.polar-form]] |

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
