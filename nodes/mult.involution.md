---
id: mult.involution
title: Involution
type: axiom
level: object
kind: law
rung: mult
order: 310
setting: classical
equality: "≐"
domain: positive
law: "([A]) ≐ A"
units: "e^{ln a} = a = ln e^a"
gloss_check: "A"
holds:
  classical: holds
  J1: holds-mod-Λ
  JH: guarded
  JO: guarded
  JP: holds
readings:
  C: EXACT
  finset: PARTIAL
  lambda: untested
  CC: untested
  logic: ANALOGY
status: NATIVE
verified: engine
known_since: "1993 (James), axiom 1 of three"
entered: 2026-10-03
guide: shape-led
band: "3–5"
uses: [N.round, mult.square]
see_also: [mult.distribution, mult.unit-law, N.round, mult.square]
aliases: [Involution, James axiom 1, A1, A2, counit, unit]
concepts: [logarithm, exponential]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A]) ≐ A` | — | e^{ln a} = a (the counit, "Involution-up") |
| `[(A)] ≐ A` | — | ln e^a = a (the unit, "Involution-down") |

The two boundaries undo one another. James states both directions as one axiom; the extensions split them — only the second direction ever misbehaves.

## Plain

Circle a box, or box a circle, and you are back where you started.

## Derivation

none — adjoined. The first of James's three axioms, stated in terms of the two boundaries [[N.round]] and [[mult.square]]. The chart checks both directions numerically; the second only on the domain where the principal logarithm is a two-sided inverse.

## Confirms

exp and ln as mutual inverses — but with the asymmetry that analysis also finds: `e^{ln a} = a` is unconditional, while `ln e^a = a` holds only on a strip (the principal branch). The whole enriched program is the study of the second direction's failure: in J1 it holds *mod Λ* (the period lattice ℤ·2πi); in JH it is *guarded* at the seam (JH-3). It is **not** a statement about a particular base.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | axiom |
| J1 | holds-mod-Λ | strict counit `([A]) ≐ A`; weakened unit `[(A)] ≐ A mod Λ` — the defining move of 𝕁₁ |
| JH, JO | guarded | Involution-down `[(A)] → A` permitted only when `L(exp V(A)) = V(A)` (the seam guard, JH-3); Involution-up unconditional |
| JP | holds | the axiom audit passes at every tested place; at a place the two closures sit on opposite sides of involution (Part II, Ch. 9) |

| reading | cell | why |
|---|---|---|
| C | EXACT | on the principal strip |
| finset | PARTIAL | the counit of `Sym ⊣ Ch` is strict, the unit is Λ-graded — Lui's identification of the hinge |
| logic | ANALOGY | LoF's Crossing `((A)) ≐ A` is an involution on *one* boundary; this is an adjunction between two |
| lambda, CC | untested | — |

## Refuted readings

- ~~the tower `[[[A]]] ≃ [[A]]` stabilizes~~ — refuted 2026-08-22 (collapse theorem: with `()`-congruence it forces total transparency); stabilization relocated to the mixed closure `[(−)]` at depth 1.

## Notes

The chart's own equality field is this axiom's shadow: `≐` classical, `≡/≃` in J1 where the unit is weakened.
