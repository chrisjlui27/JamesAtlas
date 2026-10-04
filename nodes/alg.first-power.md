---
id: alg.first-power
title: The first power is the number
type: theorem
level: object
kind: law
rung: alg
order: 742
setting: classical
equality: "≐"
domain: positive
law: "(([[A]] [o])) ≐ A"
units: "a¹ = a"
gloss_check: "A"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James); the fact is ancient"
entered: 2026-10-03
guide: shape-led
band: "6–8"
uses: [mult.exponentiation, void.page, mult.involution, mult.log-of-one]
see_also: [alg.zeroth-power, mult.square-is-product]
aliases: ["a^1 = a"]
concepts: [exponentiation, one]
understood: "yes"
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[A]] [o])) ≐ A` | — | a¹ = a |

## Plain

A number to the first power is itself: the box around one is empty, and the two circles undo the two boxes.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[A]] [o]))` | given | a^1, [[mult.exponentiation]] |
| `(([[A]] void))` | [[mult.log-of-one]] | `[o] ≐ void` |
| `(([[A]]))` | [[void.page]] | — |
| `([A])` | [[mult.involution]] | the counit |
| `A` | [[mult.involution]] | the counit again |

## Confirms

a¹ = a by two counits — the exponent 1 disappears because its abstract is void. The companion facts a⁰ = 1 ([[alg.zeroth-power]]) and 1ᵇ = 1 ([[alg.one-to-power]]) are black-hole facts and cost Dominion.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, JH, JO, JP | holds | — |
| J1 | holds | the `[o] → ω` step sits directly inside the inner instance — absorbing (depth-1 criterion, [[mult.involution]] Notes) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | EXACT | A^1 ≅ A |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
