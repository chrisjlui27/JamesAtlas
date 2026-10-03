---
id: C.i-to-the-i
title: i to the power i is real
type: theorem
level: object
kind: law
rung: C
order: 1015
setting: classical
equality: "≐"
domain: positive
law: "(([[(([J] <[oo]>))]] [(([J] <[oo]>))])) ≐ (<([J] <[(([J] <[oo]>))]> <[oo]>)>)"
units: "i^i = e^{−π/2}"
gloss_check: "exp(-pi/2)"
holds:
  classical: holds
  J1: holds-mod-Λ
  JH: replaced
  JO: replaced
  JP: untested
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "Euler: the 1746 letter to Goldbach as commonly reported, and E168 (presented 1747, printed 1751) for i^i = e^{−π/2} with its other values; 1993 (James) for the spelling"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.exponentiation, C.imaginary-unit, mult.involution, Z.inversion, Q.fractional-cardinality, C.phase-under-instance, C.pi]
guarded_by: [mult.seam-decree]
see_also: [C.imaginary-unit, C.pi, mult.exponentiation, C.log-of-negative]
aliases: ["i^i", "e^{−π/2}", i to the i]
concepts: [phase, exponentiation, complex-number, constant]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[i]] [i])) ≐ (<([π] <[oo]>)>)` | with i = `(([J] <[oo]>))` and `[π]` = `[J] <[i]>` | i^i = e^{−π/2} ≈ 0.2079 |

An imaginary number raised to an imaginary power, and the answer is a plain positive real. In forms: the exponential `A ^ B := (([[A]] [B]))` at A = B = i, which the calculus reduces to the instance of minus half of π.

## Plain

i to the i: take the log of i — a quarter turn, iπ/2 — multiply by i, which turns it a further quarter to land on the negative real line at −π/2, and circle: e^{−π/2}. A turn times a turn is a straight line.

## Derivation

Write H for `([J] <[oo]>)`, half of J, so that i = `(H)`:

| form | rule | note |
|---|---|---|
| `(([[(([J] <[oo]>))]] [(([J] <[oo]>))]))` | given | i ^ i, [[mult.exponentiation]], with i = `(([J] <[oo]>))` ([[C.imaginary-unit]]) |
| `(([([J] <[oo]>)] [(([J] <[oo]>))]))` | [[mult.involution]] | the unit on the inner `[(H)]` of `[[i]]` → `[H]`: the redex sits directly inside a *square*, not an instance, so nothing absorbs it — admitted because its content H = iπ/2 is on the strip (guarded by content: the one place in this rung where the content clause is used under a square) |
| `(([([J] <[oo]>)] ([J] <[oo]>)))` | [[mult.involution]] | the unit on `[i]` = `[(H)]` → H, directly inside the inner instance — absorbing |
| `(([J] <[oo]> ([J] <[oo]>)))` | [[mult.involution]] | the unit on `[H]` = `[([J] <[oo]>)]` → `[J] <[oo]>`, directly inside the inner instance — absorbing |
| `(([J] <[oo]> ([J] <[oo]>) ([J] <[oo]>) <([J] <[oo]>)>))` | [[Z.inversion]] | create the pair `H <H>` |
| `(([J] <[oo]> J <([J] <[oo]>)>))` | [[Q.fractional-cardinality]] | `H H ≐ J`: two halves of J make J |
| `(([J] <[oo]> J <[(([J] <[oo]>))]>))` | [[mult.involution]] | the unit right to left on `<H>` → `<[(H)]>` = `<[i]>`, inside an angle directly inside the instance — absorbing |
| `(<([J] <[oo]> <[(([J] <[oo]>))]>)>)` | [[C.phase-under-instance]] | `(X J) ≐ <(X)>` with X = `[J] <[oo]> <[i]>` — and `[J] <[i]>` is `[π]` by [[C.pi]], so this is the instance of −π/2 |

## Confirms

Euler's i^i = e^{−π/2}, the principal value, with every step on the page. The content clause of the seam decree does real work exactly once: `[[i]]`, the log of the log of i, is reached by a unit step under a *square*, where no instance can absorb a mistake, and it is admitted because ln i = iπ/2 lies on the strip. It is **not** a statement that i^i has one value: the other values e^{−π/2 − 2πk} belong to other branches of `[i]`, which the forms do not write — the calculus reads the principal one, as it reads J as iπ and not 3iπ. And it is **not** a coincidence of the base: the e is the circle itself, so "i^i is real" is a fact about the three boundaries.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds-mod-Λ | the step under the square is a bare Λ-step that nothing absorbs (depth-1 criterion fails there); all the others are absorbed |
| JH, JO | replaced | u^u per slice, the same real number e^{−π/2} for every unit direction u — a slice-independent value reached through slice-dependent forms |
| JP | untested | p-adic i^i needs the p-adic logarithm of i, which exists only where i does (p ≡ 1 mod 4) and converges only if i is a 1-unit; untested |

| reading | cell | why |
|---|---|---|
| C | EXACT | the principal value |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
