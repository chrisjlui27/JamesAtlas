---
id: Q.division-as-product
title: Dividing is multiplying by the reciprocal
type: theorem
level: object
kind: law
rung: Q
order: 530
setting: classical
equality: ≐
domain: positive
law: "([A] [(<[B]>)]) ≐ ([A] <[B]>)"
units: a · (1/b) = a ÷ b
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
known_since: 1993 (James); the rule is ancient
entered: 2026-10-03
guide: shape-led
band: 6–8
uses: [mult.multiplication, Q.reciprocal, mult.involution, Q.division]
see_also: [Q.multiply-fractions]
aliases: [invert and multiply, a/b = a · b⁻¹]
concepts: [division, multiplication]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A] [(<[B]>)]) ≐ ([A] <[B]>)` | — | a · (1/b) = a ÷ b |

## Plain

Dividing by a number is the same as multiplying by one over it — the boxed reciprocal unboxes to a mirrored box.

## Derivation

| form | rule | note |
|---|---|---|
| `([A] [(<[B]>)])` | [[mult.multiplication]] | A × (1/B), [[Q.reciprocal]] |
| `([A] <[B]>)` | [[mult.involution]] | `[(X)] ≐ X` with X = `<[B]>`; the result is A ÷ B by [[Q.division]] |

## Confirms

"Invert and multiply", as one Involution. The schoolroom rule for dividing by a fraction is this law followed by [[Q.flip]] and [[Q.multiply-fractions]] — see [[Q.divide-by-fraction]].

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the Involution-down step sits at depth 1 under the instance — the depth-1 criterion ([[mult.involution]], Notes) |
| JH, JO | replaced | `x · y⁻¹` and `y⁻¹ · x` differ; the ordered bracket carries both |
| JP | guarded | for unit divisors |

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
