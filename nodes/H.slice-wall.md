---
id: H.slice-wall
title: A receipt is paid only in its own slice
type: theorem
level: meta
kind: law
rung: H
order: 1760
setting: JH
equality: "≃"
domain: complex
law: "(ω_u A) ≃ (A) for A in the slice of u, where ω_u = 2πu is the period in the direction u: absorbed, as on the trunk; across slices it is not — exp(2πu + A) = exp(A) iff Au = uA. The first non-commutative wall: a receipt carries a direction, and an instance pays only a receipt co-sliced with its content"
units: "exp(2πu + A) = exp A iff [A, u] = 0 (in-band rigidity); the trunk's (ω A) ≃ (A) is the case u = i, A in ℂ"
gloss_check: ""
witness: tools/models/h_slice_wall.py
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "2026-08 (the JH-Calculus report: in-band rigidity, JH-1 proof B); the receipt prover in ℍ: this rung, 2026-10-07"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.collapse, H.no-go, J1.absorption, J1.unit]
see_also: [J1.absorption-mirror, C.period-absorption, H.seam-guard, place.wall, H.phase-sphere]
aliases: [the slice wall, directional receipts, cross-slice absorption, the first non-commutative wall, ω_u, Λ_ℍ]
concepts: [period, lattice, quaternion, consistency]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(ω_u A) ≃ (A)` when A is in the slice of u; not otherwise | exp(2πu + A) = exp(A) iff Au = uA | the period lattice of ℍ is Λ_ℍ = {2πk·u}, a sphere of directions, and absorption is slice-wise |

On the trunk the receipt of a unit step is a lattice element 2πik and an enclosing instance absorbs it ([[J1.absorption]]: `(ω A) ≃ (A)`). In ℍ the lattice is Λ_ℍ = {2πk·u : u a pure unit}, so a **receipt carries a direction**, and the instance absorbs it only when the content commutes with that direction — when A lies in the slice C_u = ℝ + ℝu. Across slices it does not: exp(2πu + A) ≠ exp(A) when [A, u] ≠ 0, by in-band rigidity (the proof of [[H.no-go]]). The receipt prover implements exactly this (SPEC §4.5): every receipt has a direction, an absorbed step is value-checked in ℍ, and a cross-slice absorption is graded `absent [cross-slice]`. The trunk's absorption is the case u = i with A in ℂ. This is where non-commutativity meets the tape: not in a false equation, but in a receipt nobody pays.

## Plain

A full turn is forgotten by the circle around it only if the turn and the thing inside lie in the same plane. The quaternions have many planes, and a turn in one is not forgotten by a circle around something in another.

## Derivation

none — a theorem of the reading, witnessed.

| statement | rule | note |
|---|---|---|
| (ω A) = (A) for A in the slice of i | [[J1.absorption]] | witness part (1): 40 samples |
| (ω A) ≠ (A) for generic A | — | witness part (2): the cross-slice failure |
| (2πu + A) = (A) iff [A, u] = 0 | [[H.no-go]] | witness part (3): in-band rigidity (the no-go's proof B), both directions; the co-sliced case is the premise of [[H.collapse]] |
| the trunk's absorption re-graded in ℍ: absorbed on co-sliced contents, absent [cross-slice] on generic ones | [[J1.unit]] | witness part (4): the prover's grades |

## Confirms

That [[H.collapse]] and this wall are one fact seen from two sides: co-sliced logs commute, so their ordered square collapses and their receipts are paid; cross-sliced ones neither collapse nor pay. On the trunk, where there is one slice, every receipt is paid by some instance ([[C.period-absorption]]) and the J1 cells are `holds-mod-Λ` at worst; here the same laws read on generic quaternions acquire `absent` cells, recorded in census/h-ledger.md — which is why the ledger reads each trunk law twice, on its domain and on generic ℍ. It is **not** a failure of the law `(ω A) ≃ (A)` as a form: the form `ω` is `[()]`, one form, whose value in ℍ is the pinned 2πi; the wall is about the *other* periods, which the page cannot write without a direction.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | replaced | one slice: no wall |
| J1 | replaced | one direction: [[J1.absorption]] |
| JH | holds | the witness and the prover |
| JO | holds | the same wall with a 6-sphere of directions |
| JP | holds | at the places the torsion logs carry a direction too (tools/quatplace.py: (direction, count) pairs), and a receipt in the direction of i is not paid by an instance of a j-sliced content |

| reading | cell | why |
|---|---|---|
| C | EXACT | the slice of i: the trunk's absorption |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The engine's grade for a cross-slice absorption is `absent [cross-slice]` (tools/j1.py); a step whose receipt is a *seam* displacement — contents differing by no lattice element but with equal instance values, as in [[H.j-squared]]'s collapse — is paid by the instance and recorded `where = seam`. The wall at the places ([[place.wall]]) is the same shape: a receipt (there a torsion count) paid only by an instance whose content lies in its slice.
