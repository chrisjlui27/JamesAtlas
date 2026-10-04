---
id: alg.rational-exponent
title: A rational exponent is a root raised to a power
type: theorem
level: object
kind: instance
rung: alg
order: 810
setting: classical
equality: ≐
domain: positive
law: "([(([[A]] <[oo]>))] [(([[A]] <[oo]>))] [(([[A]] <[oo]>))]) ≐ (([[A]] [([ooo] <[oo]>)]))"
units: "(√a)³ = a^{3/2} ; in general (ⁿ√a)^m = a^{m/n}"
gloss_check: A ** 1.5
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
band: 9–12
uses: [alg.root, mult.multiplication, mult.involution, mult.cardinality, Q.fraction, mult.unit-law, mult.distribution]
see_also: [alg.nth-root, alg.power-of-power]
aliases: [a^{m/n}, (√a)³ = a^{3/2}, rational exponents]
concepts: [root, exponentiation, fraction]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([(([[A]] <[oo]>))] [(([[A]] <[oo]>))] [(([[A]] <[oo]>))]) ≐ (([[A]] [([ooo] <[oo]>)]))` | — | (√a)³ = a^{3/2} |

## Plain

Three copies of the square root multiply into a-to-the-three-halves: the three half-counts collect into a count of three halves.

## Derivation

| form | rule | note |
|---|---|---|
| `([(([[A]] <[oo]>))] [(([[A]] <[oo]>))] [(([[A]] <[oo]>))])` | given | √a × √a × √a, [[alg.root]] and [[mult.multiplication]] |
| `(([[A]] <[oo]>) ([[A]] <[oo]>) ([[A]] <[oo]>))` | [[mult.involution]] | the unit, three times, directly under the instance |
| `(([([[A]] <[oo]>)] [ooo]))` | [[mult.cardinality]] [[mult.unit-law]] [[mult.distribution]] | three copies are one copy with count 3: two copies become the count 2, the third gets the count 1, Distribution collects the counts |
| `(([[A]] <[oo]> [ooo]))` | [[mult.involution]] | the unit, directly under the inner instance |
| `(([[A]] [([ooo] <[oo]>)]))` | [[mult.involution]] | the unit right to left on `[ooo] <[oo]>`: the exponent as the fraction 3/2, [[Q.fraction]] |

## Confirms

a^{m/n} = (ⁿ√a)^m, the rule that makes rational exponents consistent with roots — here a theorem of cardinality and the unit, with the count 3/2 appearing as the fraction form of rung Q sitting in the exponent. Every level of the tower reuses the level below it.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | all unit steps directly under an instance: depth-1 criterion ([[mult.involution]], Notes) |
| JH, JO | replaced | within one slice |
| JP | guarded | where the root is a form at p |

| reading | cell | why |
|---|---|---|
| C | EXACT | exact for positive bases; the form fixes the branch for others |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
