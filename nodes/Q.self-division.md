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
domain: complex
law: "([A] <[A]>) ≐ o"
units: a ÷ a = 1
gloss_check: 1
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
| JP | holds | the form cancels before any reciprocal is taken: `[A] <[A]>` is void for every A, the prime included; `(<[A]>)` alone is a form only for a unit (`place.no-inverse-of-the-prime`) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Domain `complex` (widened 2026-10-03, C referee pass): [[C.omega-sum]] instantiates this law at ω − 1, and a law may be cited only inside its declared domain ([[mult.consistency]], Confirms); every row of its derivation is exact on ℂ×. The home band and reading are unchanged.
