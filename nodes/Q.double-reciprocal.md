---
id: Q.double-reciprocal
title: The reciprocal of the reciprocal
type: theorem
level: object
kind: law
rung: Q
order: 524
setting: classical
equality: ≐
domain: positive
law: "(<[(<[A]>)]>) ≐ A"
units: 1/(1/a) = a
gloss_check: A
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
uses: [Q.reciprocal, mult.involution, Z.cancellation]
see_also: [Z.cancellation, Q.flip]
aliases: [1/(1/a) = a]
concepts: [inverse, division]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(<[(<[A]>)]>) ≐ A` | — | 1/(1/a) = a |

Inverse cancellation ([[Z.cancellation]]) one level deeper: the multiplicative inverse is an involution because the additive one is.

## Plain

One over one-over-a-number is the number again: unbox the inner circle and the two mirrors cancel.

## Derivation

| form | rule | note |
|---|---|---|
| `(<[(<[A]>)]>)` | given | the reciprocal of 1/A, [[Q.reciprocal]] |
| `(<<[A]>>)` | [[mult.involution]] | `[(X)] ≐ X` with X = `<[A]>` |
| `([A])` | [[Z.cancellation]] | two mirrors cancel |
| `A` | [[mult.involution]] | `([A]) ≐ A` |

## Confirms

(a⁻¹)⁻¹ = a. In JH it is the lemma inside the "left inverse needs three lines" argument (x⁻¹x = x⁻¹(x⁻¹)⁻¹ = 1), with the Involution-down guarded off the seam.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, JH, JO | holds | — |
| J1 | holds | depth-1 criterion ([[mult.involution]], Notes) |
| JP | guarded | for units |

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
