---
id: mult.c-reading
title: The ℂ reading
type: import
level: meta
kind: law
rung: mult
order: 470
setting: classical
equality: "≐"
domain: positive
law: "forms are valued in ℂ ∪ {□} by (A) = e^A, [A] = ln A (principal), <A> = −A, juxtaposition = +; the admissible axioms hold on positive real content"
units: "exp and log on ℂ, with □ = ln 0 absorbing"
holds:
  classical: holds
  J1: replaced
  JH: replaced
  JO: replaced
  JP: replaced
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: IMPORTED
verified: engine
known_since: "Euler, for exp and log; 1993 (James, Chapter 5) for the reading of the three boundaries"
entered: 2026-10-03
guide: need-led
band: beyond
uses: [N.round, mult.square, Z.angle, void.space, mult.hole-exclusion]
see_also: [mult.consistency, mult.involution]
aliases: [the standard reading, shadow model, calc_shadow, the engine's model]
concepts: [consistency, exponential, logarithm]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(A)` ↦ e^A, `[A]` ↦ ln A, `<A>` ↦ −A, `A B` ↦ a + b, void ↦ 0, `□` ↦ −∞ | — | the model every node's `units:` column is written in |

An **import**: the real and complex exponential and logarithm, with their known identities, are borrowed from analysis to give every form a value. The import is what the chart's `units` column, its `gloss_check` fields, and the engine's shadow check all presuppose.

## Plain

Every drawing on the page can be read as an ordinary number by treating circles as "e to the", boxes as "log of", and mirrors as "minus" — and that reading is borrowed, not built.

## Derivation

none — adjoined, as an import. It interprets the three boundaries [[N.round]], [[mult.square]], [[Z.angle]] and the medium [[void.space]]; it is a *partial* reading — undefined exactly on the forms the decree [[mult.hole-exclusion]] excludes — and it is a model of Involution-down only on the principal strip, which on the pilot's rungs (real, positive content) is everywhere.

## Confirms

That the classical calculus has a model: this is the content of James's Chapter 5 ("the calculus is sound in ℂ"). It is **not** native — the calculus does not construct e or ln; it names them — and the chart counts it as a price wherever a meta-claim leans on it ([[mult.consistency]]). The engine (`tools/forms.py`) is this reading mechanized: a derivation step is checked by evaluating both forms here.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | replaced | ℂ with the period lattice Λ tracked on a tape (the receipt calculus); the K(1) thesis reads the lattice as K(1)-localization |
| JH, JO | replaced | ℍ per slice; 𝕆 with priced receipts |
| JP | replaced | ℤ_p at a finite place; `jadic.js` is that engine |

| reading | cell | why |
|---|---|---|
| C | EXACT | it is the reading |
| finset | ABSENT | a different reading altogether |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The chart's own `verified: engine` badge means "every derivation step holds in this reading on sampled values"; it never means that a rule was correctly *cited* — that is the referee's job (SPEC §10).
