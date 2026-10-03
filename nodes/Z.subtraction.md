---
id: Z.subtraction
title: Subtraction is adding the inverse
type: definition
level: object
kind: law
rung: Z
order: 240
setting: classical
equality: "≐"
domain: complex
law: "A − B := A <B>"
units: "a − b = a + (−b)"
gloss_check: "A - B"
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
known_since: "1993 (James)"
entered: 2026-10-03
guide: shape-led
band: "1–2"
uses: [Z.angle, N.addition]
see_also: [Z.normal-form, Z.inversion]
aliases: [difference, minus]
concepts: [subtraction, negation]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `A <B>` | — | a − b |
| `ooooo <oo>` | `ooooo <oo>` | 5 − 2 |

There is no symbol for subtraction. To take `B` away from `A`, put `B`'s mirror beside `A`; the cancelling is Inversion's business ([[Z.normal-form]]).

## Plain

Taking away two is the same as adding minus two; the page does it by placing the mirrored pile next to the first.

## Derivation

| form | rule | note |
|---|---|---|
| `A <B>` | [[N.addition]] | A plus the mirror of B, [[Z.angle]] |
| `A − B` | name | — |

## Confirms

a − b := a + (−b), the definition every algebra text gives and every child resists: subtraction is not a second operation. The calculus makes the resistance pointless — there is nothing else subtraction *could* be. It is **not** a rewrite; the computation `5 − 2 = 3` happens at [[Z.normal-form]].

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Domain `complex` (widened 2026-10-03, C referee pass): rung C instantiates this law at complex content, and under the chart's citation discipline ([[mult.consistency]], Confirms) a law may be cited only inside its declared domain; every row of its derivation is exact on ℂ×, as the engine confirms. The law's home band and reading are unchanged.
