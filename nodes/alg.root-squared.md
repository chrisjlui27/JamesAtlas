---
id: alg.root-squared
title: A square root, squared, is the number
type: theorem
level: object
kind: law
rung: alg
order: 770
setting: classical
equality: ≐
domain: positive
law: "([(([[A]] <[oo]>))] [(([[A]] <[oo]>))]) ≐ A"
units: (√a)² = a
gloss_check: A
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
known_since: 1993 (James); the fact is ancient
entered: 2026-10-03
guide: shape-led
band: 6–8
uses: [alg.root, mult.multiplication, mult.involution, mult.cardinality, Z.inversion]
see_also: [Q.fractional-cardinality, alg.sqrt2]
aliases: [(√a)² = a, root squared]
concepts: [root, multiplication]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([(([[A]] <[oo]>))] [(([[A]] <[oo]>))]) ≐ A` | — | (√a)² = a |

## Plain

A square root times itself gives the number back: the two half-counts collect into a whole count, which cancels.

## Derivation

| form | rule | note |
|---|---|---|
| `([(([[A]] <[oo]>))] [(([[A]] <[oo]>))])` | given | √a × √a, [[alg.root]] and [[mult.multiplication]] |
| `(([[A]] <[oo]>) ([[A]] <[oo]>))` | [[mult.involution]] | the unit twice, directly under the instance |
| `(([([[A]] <[oo]>)] [oo]))` | [[mult.cardinality]] | two copies are one copy with count 2 |
| `(([[A]] <[oo]> [oo]))` | [[mult.involution]] | the unit on content `[[A]] <[oo]>`, directly under the inner instance |
| `(([[A]]))` | [[Z.inversion]] | `<[oo]> [oo]` cancels |
| `A` | [[mult.involution]] | the counit, twice |

## Confirms

(√a)² = a, by exactly the derivation of [[Q.fractional-cardinality]] one level down. The converse, √(a²) = a, is **not** a law: `(([[([A][A])]] <[oo]>))` is the principal root, |a|, and for negative a the two differ by a mirror — the calculus keeps the sign information the schoolroom loses.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | all unit steps directly under an instance: depth-1 criterion ([[mult.involution]], Notes) |
| JH, JO | replaced | within one slice, with the polar form |
| JP | guarded | where the root is a form at p |

| reading | cell | why |
|---|---|---|
| C | EXACT | exact on ℂ× for the principal root |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

For 0 < a < 1 the content `[[A]]` is the log of a negative (ln a < 0) and carries iπ; every unit step on it in this derivation is in an absorbing position, so the law is exact there too — the engine samples both sides of a = 1.
