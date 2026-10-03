---
id: Q.division-by-one
title: Dividing by one changes nothing
type: theorem
level: object
kind: law
rung: Q
order: 504
setting: classical
equality: ≐
domain: positive
law: "([A] <[o]>) ≐ A"
units: a ÷ 1 = a
gloss_check: A
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: holds
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
band: 3–5
uses: [Q.division, mult.unit-law, Z.void-inverse, void.page, mult.involution]
see_also: [Q.self-division, mult.unit-law]
aliases: [a/1 = a]
concepts: [division, one]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A] <[o]>) ≐ A` | — | a ÷ 1 = a |

## Plain

Dividing by one does nothing, because the box around one is empty and the mirror of nothing is nothing.

## Derivation

| form | rule | note |
|---|---|---|
| `([A] <[o]>)` | given | a ÷ 1, [[Q.division]] |
| `([A] <>)` | [[mult.unit-law]] | `[o] ≐ void` |
| `([A] void)` | [[Z.void-inverse]] | `<> ≐ void` |
| `([A])` | [[void.page]] | — |
| `A` | [[mult.involution]] | `([A]) ≐ A` |

## Confirms

a/1 = a, and a small reunion: two of the three empty boundaries appear — `()` as the divisor and `<>` on the way — and the third, `[]`, must not: `[o]` is `[()]`, which is void, not the black hole, and `<[]>` would be the excluded form.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, JH, JO, JP | holds | — |
| J1 | holds | the `[o] → ω` step sits under an angle under the instance: depth-1 criterion ([[mult.involution]], Notes) |

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
