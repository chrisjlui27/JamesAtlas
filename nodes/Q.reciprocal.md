---
id: Q.reciprocal
title: The reciprocal is the mirror of the abstract
type: definition
level: object
kind: law
rung: Q
order: 510
setting: classical
equality: ≐
domain: complex
law: "1/A := (<[A]>)"
units: "1/a = e^{−ln a}"
gloss_check: 1 / A
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: guarded
readings:
  C: EXACT
  finset: ANALOGY
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: 1993 (James); reciprocals are ancient
entered: 2026-10-03
guide: shape-led
band: 6–8
uses: [N.round, Z.angle, mult.square]
see_also: [Q.one-over-a, Q.reciprocal-law, Q.half, mult.hole-exclusion]
aliases: [multiplicative inverse, 1/x, x⁻¹, (<[x]>)]
concepts: [division, inverse]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(<[A]>)` | — | 1/a |

The angle boundary threaded between the other two: mirror the abstract, take the instance. Placed directly, `<A>` was −a; placed between, it is 1/a. One boundary, two inverses, the depth deciding which.

## Plain

One over a number is the number's box, mirrored, then circled.

## Derivation

| form | rule | note |
|---|---|---|
| `(<[A]>)` | [[N.round]] | the instance of the mirror ([[Z.angle]]) of the abstract ([[mult.square]]) of A |
| `1/A` | name | — |

## Confirms

x⁻¹ = e^{−ln x}; that `1 ÷ A` reduces to this form is the theorem [[Q.one-over-a]]. In JH this exact form is kept — "with x⁻¹ ≐ (<[x]>)" — where the right-inverse law is the axiom OC and the left-inverse law is a theorem ([[Q.reciprocal-law]]). What this is **not**: a form for 1/0. With A the void, `[A]` is □ and `<□>` is excluded ([[mult.hole-exclusion]]); the reciprocal of zero is not undefined-by-convention, it is unwritable ([[Q.no-division-by-zero]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the form is the same; note that `[o] ≐ void`, used by [[Q.one-over-a]], becomes `[o] → ω` in J1 — a Λ-step absorbed by the instance |
| JH, JO | holds | `x⁻¹ ≐ (<[x]>)` is the inverse used throughout the JH guide |
| JP | guarded | at a finite place the prime has no inverse (Part II, Ch. 10: No-inverse-of-the-prime); reciprocals exist for units only |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ANALOGY | Baez–Dolan groupoid cardinality gives 1/n to a one-object groupoid with n automorphisms — a reading in which fractional counts are counts of symmetry; an analogy here, a candidate law at the `struct` rung |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Domain `complex` (widened 2026-10-03, C referee pass): rung C instantiates this law at complex content, and under the chart's citation discipline ([[mult.consistency]], Confirms) a law may be cited only inside its declared domain; every row of its derivation is exact on ℂ×, as the engine confirms. The law's home band and reading are unchanged.
