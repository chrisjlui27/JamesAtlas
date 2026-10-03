---
id: mult.dominion
title: Dominion
type: theorem
level: object
kind: law
rung: mult
order: 420
setting: classical
equality: "≐"
domain: positive
law: "□ A ≐ □"
units: "−∞ + a = −∞"
gloss_check: "BH"
holds:
  classical: holds
  J1: untested
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "1993 (James), listed among the theorems of the three axioms"
entered: 2026-10-03
guide: shape-led
band: beyond
uses: [mult.involution, mult.zero-annihilates, void.space, mult.black-hole]
see_also: [mult.hole-instance, mult.dominion-independence, mult.hole-exclusion]
aliases: [Dominion, black-hole absorption, "□ A = □"]
concepts: [infinity, zero]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `□ A ≐ □` | — | −∞ + a = −∞ |

The black hole annihilates its context: anything standing beside it is swallowed.

## Plain

Nothing you add to the bottomless pit fills it.

## Derivation

| form | rule | note |
|---|---|---|
| `□ A` | given | — |
| `[] A` | definition | unfold □, [[mult.black-hole]] |
| `[([] A)]` | [[mult.involution]] | `[(X)] ≐ X`, right to left |
| `[([(A)] [])]` | [[mult.involution]] | inside, `A ≐ [(A)]`; regroup by [[void.space]] |
| `[void]` | [[mult.zero-annihilates]] | `(B []) ≐ void` with B = `[(A)]` |
| `[]` | definition | which is □ |

## Confirms

−∞ absorbs under addition — the extended-real convention, here a theorem. And its exact price: Dominion needs **Inversion** (through [[mult.zero-annihilates]]); it is not a consequence of Involution and Distribution alone, by the finite model of [[mult.dominion-independence]]. In the stable/spectral *reading* of the calculus dominion fails outright (2026-10-01 session: dominion holds classically, fails in Sp, is deferred in J1), so this is a law whose fate separates the readings.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | untested | deferred in the three-way dominion check (classical / stable / J1) |
| JH, JO | holds | "black hole: □A ≐ □, (□) ≐ void, <□> undefined" survive verbatim (JH rule card) |
| JP | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | untested | — |
| lambda, CC | untested | — |

## Refuted readings

- ~~Dominion is a theorem of Involution and Distribution alone~~ — refuted 2026-10-03 by the 3-element model in `tools/models/dominion_models.py` ([[mult.dominion-independence]]).

## Notes

Whether James's own thesis proof routes through Inversion is to be checked against the 1993 text; Bricken's Iconic Arithmetic presentations sometimes take Dominion as an axiom, which the independence result explains.
