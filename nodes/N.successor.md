---
id: N.successor
title: Successor is adjoining a unit
type: definition
level: object
kind: law
rung: N
order: 160
setting: classical
equality: "≐"
domain: natural
law: "S(A) := A o"
units: "n + 1"
gloss_check: "A + 1"
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
known_since: "Peano 1889 for the concept; 1993 for the form"
entered: 2026-10-03
guide: need-led
band: K
uses: [N.unit, N.addition]
see_also: [N.induction, N.freeness]
aliases: [successor, S, next number]
concepts: [counting, natural-number]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `A o` | — | S(a) = a + 1 |

## Plain

The next number is one more circle.

## Derivation

| form | rule | note |
|---|---|---|
| `A o` | [[N.addition]] | the pile A with one more unit, [[N.unit]] |
| `S(A)` | name | Peano's successor, as a name |

## Confirms

Peano's successor function, and therefore the shape of the Peano axioms: 0 = void; S is injective and never hits 0 ([[N.freeness]]); every numeral is reached from the void by S. What is missing is the *induction schema* — the fifth axiom — which is [[N.induction]], the first gap of the chart.

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | n + 1 |
| finset | EXACT | adjoin a point |
| logic | ABSENT | Calling |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Tagged *need-led*: nothing in the shape of the forms asks for a name for "one more"; Peano's development does, and the Lean expansion will need it under the name `Nat.succ`.
