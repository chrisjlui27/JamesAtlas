---
id: Z.void-inverse
title: The inverse of nothing is nothing
type: theorem
level: object
kind: law
rung: Z
order: 220
setting: classical
equality: "≐"
domain: real
law: "<> ≐ void"
units: "−0 = 0"
gloss_check: "0"
holds:
  classical: holds
  J1: guarded
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
known_since: "1993 (James)"
entered: 2026-10-03
guide: shape-led
band: "1–2"
uses: [Z.inversion, void.page]
see_also: [N.zero, mult.hole-exclusion]
aliases: ["<>", empty angle, negative zero]
concepts: [zero, negation]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `<> ≐ void` | — | −0 = 0 |

## Plain

The opposite of nothing is nothing.

## Derivation

| form | rule | note |
|---|---|---|
| `<>` | given | the empty angle |
| `void <>` | [[void.page]] | void is transparent |
| `void` | [[Z.inversion]] | `A <A>` with A = void, cancelled |

## Confirms

−0 = 0: the one element of ℤ that is its own inverse. It also shows the chart's smallest size-1 census entry `<>` *reducing*: of the three empty boundaries, `()` is 1, `[]` is the black hole, and `<>` is nothing new.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | guarded | inherits the stratification of [[Z.inversion]]: `void<void>` is exactly the hinge Lui flagged |
| JH, JO, JP | holds | — |

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
