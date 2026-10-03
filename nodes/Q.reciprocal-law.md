---
id: Q.reciprocal-law
title: A number times its reciprocal is one
type: theorem
level: object
kind: law
rung: Q
order: 520
setting: classical
equality: ≐
domain: positive
law: "([A] [(<[A]>)]) ≐ o"
units: a · (1/a) = 1
gloss_check: 1
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
status: NATIVE
verified: engine
known_since: 1993 (James); the fact is ancient
entered: 2026-10-03
guide: shape-led
band: 6–8
uses: [mult.multiplication, Q.reciprocal, mult.involution, Z.inversion, N.unit]
see_also: [Z.inversion, mult.unit-law]
aliases: [multiplicative inverse law, x · x⁻¹ = 1]
concepts: [division, inverse, one]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A] [(<[A]>)]) ≐ o` | — | a · (1/a) = 1 |

## Plain

A number times one-over-itself is one — because, under the box, "times the reciprocal" is just "plus the opposite", and opposites cancel.

## Derivation

| form | rule | note |
|---|---|---|
| `([A] [(<[A]>)])` | [[mult.multiplication]] | A × (1/A), [[Q.reciprocal]] |
| `([A] <[A]>)` | [[mult.involution]] | `[(X)] ≐ X` with X = `<[A]>` — Involution-down; X is real |
| `(void)` | [[Z.inversion]] | `[A] <[A]>` cancels |
| `o` | [[N.unit]] | the empty round boundary is the unit |

## Confirms

The multiplicative-inverse law of a field, derived from the additive one: the multiplicative group of ℚ⁺ is the additive group of its logarithms, and Inversion serves both. It is the cleanest instance of the chart's refrain that every multiplicative law is an additive law one level deeper.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the Involution-down step sits at depth 1 under the instance: the depth-1 criterion ([[mult.involution]], Notes) |
| JH, JO | holds | `x · x⁻¹ ≐ o` is the Cancellation axiom OC there (right inverse); the left inverse `x⁻¹ · x ≐ o` is a three-line theorem — an axiom, because the ordered product no longer reduces to a sum of abstracts |
| JP | guarded | for units at the place |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Price comparison worth seeing in the chart: here this law is a theorem of Involution + Inversion; in JH it must be *posited* (axiom OC) because Splice and the ordered bracket cut the route through the sum of abstracts. The same fact, two prices, one setting apart.
