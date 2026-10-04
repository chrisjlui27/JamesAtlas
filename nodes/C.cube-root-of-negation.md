---
id: C.cube-root-of-negation
title: A third of J, cubed, is minus one
type: theorem
level: object
kind: law
rung: C
order: 1020
setting: classical
equality: "≐"
domain: positive
law: "([(([J] <[ooo]>))] [(([J] <[ooo]>))] [(([J] <[ooo]>))]) ≐ <o>"
units: "(e^{iπ/3})³ = −1"
gloss_check: "-1"
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
known_since: "1993 (James: roots as fractional counts of J); the roots of unity as e^{2πik/n}: De Moivre 1707–22, Euler 1748 (Introductio)"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.multiplication, C.phase, mult.involution, mult.cardinality, mult.unit-law, mult.distribution, Z.inversion, C.phase-value]
see_also: [C.i-squared, C.cube-root-of-unity, alg.nth-root, alg.rational-exponent, schema.roots-of-negation]
aliases: [cube root of minus one, "e^{iπ/3}", third of J]
concepts: [phase, root, complex-number]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([(([J] <[ooo]>))] [(([J] <[ooo]>))] [(([J] <[ooo]>))]) ≐ <o>` | — | (e^{iπ/3})³ = −1 |

A third of J, instanced, is a cube root of −1 — the one in the upper half-plane. Three copies multiplied give the half-turn.

## Plain

Cut the half-turn into three. Three of the pieces make the half-turn again: minus one.

## Derivation

| form | rule | note |
|---|---|---|
| `([(([J] <[ooo]>))] [(([J] <[ooo]>))] [(([J] <[ooo]>))])` | given | a product of three copies, [[mult.multiplication]], of the instance of J ÷ 3 ([[C.phase]]) |
| `(([J] <[ooo]>) ([J] <[ooo]>) ([J] <[ooo]>))` | [[mult.involution]] | the unit three times, each directly inside the outer instance — absorbing |
| `(([([J] <[ooo]>)] [oo]) ([J] <[ooo]>))` | [[mult.cardinality]] | two of the three copies become one copy with the count 2 |
| `(([([J] <[ooo]>)] [oo]) ([([J] <[ooo]>)] [o]))` | [[mult.unit-law]] | the third copy gets the count 1, right to left |
| `(([([J] <[ooo]>)] [oo o]))` | [[mult.distribution]] | collect the two counts over the shared context — the count is now the pile 3 |
| `(([J] <[ooo]> [ooo]))` | [[mult.involution]] | the unit on `[([J] <[ooo]>)]`, directly inside the inner instance — absorbing |
| `(([J]))` | [[Z.inversion]] | `<[ooo]> [ooo]` cancels: three thirds of J are J |
| `(J)` | [[mult.involution]] | the counit |
| `<o>` | [[C.phase-value]] | — |

## Confirms

(e^{iπ/3})³ = −1. The rows that take two copies to the count 2 and then to the count 3 are [[schema.cardinality]] at n = 3, written out; the n-th roots of −1 for every n are [[schema.roots-of-negation]], which pays the induction gap ([[N.induction]]) once. It is **not** "the" cube root of −1: the three cube roots are the counts ⅓, 1 and ⁵⁄₃ of J, instanced — `(([J] <[ooo]>))`, `(J)` = `<o>` and `(([J] [ooooo] <[ooo]>))` — and the calculus names each one separately; [[alg.nth-root]] names the real one when the radicand is positive.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step is directly under an instance (depth-1 criterion) |
| JH, JO | holds | per slice |
| JP | guarded | the count 3 must be a unit at p (p ≠ 3), and the form a value at p |

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
