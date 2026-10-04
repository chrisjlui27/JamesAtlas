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
domain: complex
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
| `[([] A)]` | [[mult.involution]] | `X ≐ [(X)]`, right to left, on the content `□ A` — the hole, whose instance is void, so the step is exact |
| `[void]` | [[mult.zero-annihilates]] | `(A □) ≐ void`, regrouped by [[void.space]] |
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

Against the thesis: James's Theorem 2 (Ch. 4 §4.4.1, p. 28) proves Dominion as `□A = [(□A)] = □`, "from void multiplication with an involution", and void multiplication `([a][]) = void` (p. 26) by the argument that `([a][])([a][]) = ([a][])` by Distribution and "the equation ee = e is true when e is void or when collection of e is idempotent. Since collection is assumed additive, ee ≠ e unless e is void." That assumption — collection has no idempotents — is outside the three axioms, and it is exactly what the independence witness violates: in the 3-element model of [[mult.dominion-independence]] the element 1 satisfies 1 + 1 = 1. The chart's derivation routes instead through [[mult.zero-annihilates]], i.e. through Inversion, which James's two-boundary calculus does not yet have.

Whether James's own thesis proof routes through Inversion is to be checked against the 1993 text; Bricken's Iconic Arithmetic presentations sometimes take Dominion as an axiom, which the independence result explains. The engine's shadow check of the law itself evaluates `□ A` as □ by its own rule — i.e. by this law — so the evidence for the law is the derivation, not the check; the check guards the derivation's steps.
