---
id: Q.one-over-a
title: One divided by a number is its reciprocal
type: theorem
level: object
kind: law
rung: Q
order: 512
setting: classical
equality: ≐
domain: positive
law: "([o] <[A]>) ≐ (<[A]>)"
units: 1 ÷ a = 1/a
gloss_check: 1/A
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
uses: [Q.division, Q.reciprocal, void.page, mult.log-of-one]
see_also: [Q.reciprocal]
aliases: [1 ÷ a]
concepts: [division, inverse]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([o] <[A]>) ≐ (<[A]>)` | — | 1 ÷ a = 1/a |

## Plain

One divided by a number is one over that number — the box around one vanishes and leaves the reciprocal's shape.

## Derivation

| form | rule | note |
|---|---|---|
| `([o] <[A]>)` | given | 1 ÷ A, [[Q.division]] |
| `(void <[A]>)` | [[mult.log-of-one]] | `[o] ≐ void` |
| `(<[A]>)` | [[void.page]] | the reciprocal, [[Q.reciprocal]] |

## Confirms

That [[Q.reciprocal]] is the special case of [[Q.division]] it ought to be. In J1 the step `[o] ≐ void` becomes `[o] → ω`, a Λ-step the instance absorbs.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, JH, JO | holds | — |
| J1 | holds | the `[o] ≐ void` step sits at depth 1 under the instance (depth-1 criterion, [[mult.involution]] Notes) |
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
