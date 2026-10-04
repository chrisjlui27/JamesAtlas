---
id: schema.roots-of-negation
title: The n-th roots of minus one, for every n
type: schema
level: object
kind: law
rung: schema
order: 1140
setting: classical
equality: "≐"
domain: positive
law: "([(([J] [o^{2k+1}] <[o^{n}]>))]^{n}) ≐ <o>"
units: "(e^{(2k+1)πi/n})ⁿ = −1"
gloss_check: ""
schema_range: "n=1..6; k=0..n-1"
schema_draw: "n=3; k=1"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE-BY-SCHEMA
verified: engine
known_since: "1993 (James: roots as fractional counts of J); the n-th roots of −1 as e^{(2k+1)πi/n}: De Moivre 1707–22, Euler 1748"
entered: 2026-10-03
guide: need-led
band: "9–12"
uses: [mult.multiplication, C.phase, mult.involution, schema.cardinality, Z.inversion, C.phase-under-instance, schema.period-multiple]
guarded_by: [mult.seam-decree]
see_also: [C.cube-root-of-negation, C.i-squared, schema.roots-of-unity, C.phase-under-instance]
aliases: [roots of negation, roots of −1, "ρⁿ = −1"]
concepts: [root, phase, negation, induction]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([ρ]^{n}) ≐ <o>`, ρ = `(([J] [o^{2k+1}] <[o^{n}]>))` | the n-th power of J with the odd count (2k+1)/n, instanced, is minus one | (e^{(2k+1)πi/n})ⁿ = −1 |

The other half of the fractions of J: with an odd numerator, the n-th power lands on −1. [[C.cube-root-of-negation]] is n = 3, k = 0; [[C.i-squared]] is n = 2, k = 0.

## Plain

Cut a half-turn into n equal parts, take an odd number of parts, and do it n times: you have gone round some whole turns and one half-turn more — minus one.

## Derivation

| form | rule | note |
|---|---|---|
| `([(([J] [o^{2k+1}] <[o^{n}]>))]^{n})` | given | the n-th power of `(([J] [2k+1] <[n]>))`, J with an odd count over n ([[mult.multiplication]], [[C.phase]]) |
| `(([J] [o^{2k+1}] <[o^{n}]>)^{n})` | [[mult.involution]] | the unit on each abstract, directly inside the instance — absorbing |
| `(([([J] [o^{2k+1}] <[o^{n}]>)] [o^{n}]))` | [[schema.cardinality]] | n copies are one copy with the count n |
| `(([J] [o^{2k+1}] <[o^{n}]> [o^{n}]))` | [[mult.involution]] | the unit, directly inside the inner instance — absorbing |
| `(([J] [o^{2k+1}]))` | [[Z.inversion]] | the count n and its mirror cancel |
| `(J^{2k+1})` | [[schema.cardinality]] | right to left, with A = J |
| `(J^{2k} J)` | medium | one J set apart |
| `<(J^{2k})>` | [[C.phase-under-instance]] | `(A J) ≐ <(A)>` with A = `J^{2k}`: the odd J is a sign |
| `<o>` | [[schema.period-multiple]] | k whole turns inside an empty instance are `o`; the n-th power of an odd fraction of J is minus one |

## Confirms

The n-th roots of −1 as fractional counts of J: `(([J] [2k+1] <[n]>))` for k = 0, …, n − 1. The derivation differs from [[schema.roots-of-unity]] in one row: the odd J left over after the whole turns are forgotten becomes a sign by [[C.phase-under-instance]]. Together the two schemas say that μ_{2n} = μ_n ⊔ (the roots of negation) — the unity/negation split that J1 reads as group and torsor. It is **not** a proof that the real cube root of −1, which is `<o>` itself, is among these for odd n: it is (k = (n − 1)/2 gives the count 1), but "which of the n forms is real" is a question for the reading.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step directly under an instance |
| JH, JO | holds | per slice |
| JP | guarded | as [[schema.roots-of-unity]]: n a unit at p and the fraction a form at p |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Guarded by position (Amendment A2): as [[schema.roots-of-unity]]. Checked for n = 1…6 and k = 0…n − 1 (21 instances); the card draws n = 3, k = 1.
