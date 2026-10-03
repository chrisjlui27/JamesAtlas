---
id: Q.self-division
title: A number divided by itself is one
type: theorem
level: object
kind: law
rung: Q
order: 502
setting: classical
equality: ≐
domain: positive
law: "([A] <[A]>) ≐ o"
units: a ÷ a = 1
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
band: 3–5
uses: [Q.division, Z.inversion, N.unit]
see_also: [Q.reciprocal-law, Q.division-by-one]
aliases: [a/a = 1]
concepts: [division, one]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A] <[A]>) ≐ o` | — | a ÷ a = 1 |

## Plain

Anything divided by itself is one: under the box, a thing and its mirror cancel, and the circle around nothing is one.

## Derivation

| form | rule | note |
|---|---|---|
| `([A] <[A]>)` | given | a ÷ a, [[Q.division]] |
| `(void)` | [[Z.inversion]] | `[A] <[A]>` cancels |
| `o` | [[N.unit]] | — |

## Confirms

The most basic fact of division, as one Inversion. It is **not** `0 ÷ 0`: with A the void the form contains `<□>` and is excluded ([[Q.no-division-by-zero]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1, JH, JO | holds | Inversion only; it survives verbatim in JH (the inverse cluster) |
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
