---
id: Q.division
title: Division is the instance of a difference of abstracts
type: definition
level: object
kind: law
rung: Q
order: 500
setting: classical
equality: ≐
domain: complex
law: "A ÷ B := ([A] <[B]>)"
units: "a ÷ b = e^{ln a − ln b}"
gloss_check: A / B
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
known_since: 1993 (James); division is ancient
entered: 2026-10-03
guide: shape-led
band: 3–5
uses: [N.round, mult.square, Z.angle, void.space]
see_also: [mult.multiplication, Q.reciprocal, Q.division-as-product]
aliases: [quotient, ÷, fraction bar]
concepts: [division]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A] <[B]>)` | — | a ÷ b |
| `([oooooo] <[oo]>)` | — | 6 ÷ 2 |

To divide, abstract both, mirror the divisor's abstract, put them together, take the instance. Division is multiplication with one abstract mirrored — subtraction one level deeper, exactly as multiplication was addition one level deeper.

## Plain

Dividing is the times recipe with the second box turned to its mirror.

## Derivation

| form | rule | note |
|---|---|---|
| `([A] <[B]>)` | [[N.round]] | the instance of the abstract of A ([[mult.square]]) beside the mirror ([[Z.angle]]) of the abstract of B, in one space ([[void.space]]) |
| `A ÷ B` | name | — |

## Confirms

a ÷ b = e^{ln a − ln b}: the slide-rule's subtraction. There is no new symbol and no new axiom; division is a shape. It is **not** yet shown that `6 ÷ 2` is a pile — that follows from [[Q.cancel-common-factor]] with the numerator written as `([ooo][oo])` — and it is **not** commutative in ℍ, where JH needs two quotients, `x·y⁻¹` and `y⁻¹·x`, and the ordered bracket.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the form is the same; its laws below hold exactly thanks to A5′ |
| JH, JO | replaced | two quotients in a non-commutative algebra; `x⁻¹ ≐ (<[x]>)` survives, the single `÷` does not |
| JP | guarded | at a finite place one cannot divide by the prime ([[Q.reciprocal]]); the form exists for unit divisors |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | finite sets have no quotients; see [[Q.half]] for the groupoid-cardinality analogy |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Domain `complex` (widened 2026-10-03, C referee pass): rung C instantiates this law at complex content, and under the chart's citation discipline ([[mult.consistency]], Confirms) a law may be cited only inside its declared domain; every row of its derivation is exact on ℂ×, as the engine confirms. The law's home band and reading are unchanged.

The Iconic Mathematics scope puts division at grades 3–5 as "the inverse boundary meets the abstract boundary": the angle boundary, additive since grade 1, gains its multiplicative power here.
