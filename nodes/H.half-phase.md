---
id: H.half-phase
title: Quarter turns in orthogonal planes compose by the cross product
type: theorem
level: meta
kind: law
rung: H
order: 1762
setting: JH
equality: "≐"
domain: complex
law: "([((J_u/2)) ; ((J_v/2))]) ≐ (u × v) for orthogonal pure units u, v: e^{(π/2)u} e^{(π/2)v} = u × v — with u = i and v = j, James's own i times the seed's j is k (JH-18)"
units: "e^{πu/2} e^{πv/2} = u × v for u ⟂ v; i·j = k is a statement about quarter turns composing across planes"
gloss_check: ""
witness: tools/models/h_half_phase.py
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: holds
  JP: holds
readings:
  C: ABSENT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "Hamilton 1843 (ij = k); 2026-08 (the JH-Calculus report, JH-18: the cross product from half-phases); this rung, 2026-10-07; its own node 2026-10-13"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [C.imaginary-unit, H.j, H.k, H.phase-sphere]
see_also: [H.rigidity-dichotomy, H.anticommutation, H.ordered-product, H.k]
aliases: [JH-18, the half-phase law, the half-phase cross product, ij = k from quarter turns]
concepts: [quaternion, ordered-product, period]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([((J_u/2)) ; ((J_v/2))]) ≐ (u × v)` for u ⟂ v | e^{πu/2} e^{πv/2} = u × v | the quaternion product of two orthogonal pure units is their cross product |

A quarter turn in the plane of u is e^{(π/2)u} = u itself (the instance of half the half-turn log, as i = `(([J] <[oo]>))` on the trunk, [[C.imaginary-unit]], and j = `(([Jj] <[oo]>))` here, [[H.j]]). Two quarter turns in orthogonal planes, taken in order, compose to the cross product of their axes — which is Hamilton's ij = k ([[H.k]]) read as a fact about phases: the i of James's calculus and the j of the second seed are both half-phases on the sphere of [[H.phase-sphere]], and the ordered product of the two is the third axis. The order matters because the cross product is antisymmetric: ji = −k is the same law with the axes exchanged ([[H.anticommutation]]).

## Plain

Turn a quarter in one plane, then a quarter in a plane at right angles to it: the result is a quarter turn about the third axis. That is what i times j equals k means.

## Derivation

none — a theorem of the reading, witnessed.

| statement | rule | note |
|---|---|---|
| e^{πu/2} e^{πv/2} = u × v for 40 random orthogonal pairs | [[H.phase-sphere]] | witness part (1) |
| on the page `(([J] <[oo]>))` = i, `(([Jj] <[oo]>))` = j, and `([i ; j])` = k = i × j | [[C.imaginary-unit]], [[H.j]], [[H.k]] | witness part (2): the chart's own forms |

## Confirms

Hamilton's rule as a consequence of the sphere of phases rather than a table to memorize: the product of two unit pure quaternions is −(u·v) + u × v, and for orthogonal ones the dot product vanishes. It is **not** a derivation of [[H.k]] from the trunk alone — the seed is still needed to *name* j — but it says why the seed had to anticommute with i: quarter turns in perpendicular planes do.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | one plane, no second axis |
| JH | holds | the witness |
| JO | holds | the octonions' seven axes compose pairwise by the same rule (the Fano plane) |
| JP | holds | the Hamilton table holds on the page at every place ([[H.split-place]], [[H.ramified-place]]) |

| reading | cell | why |
|---|---|---|
| C | ABSENT | no second plane |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

Split from [[H.phase-sphere]] on 2026-10-13 (LEGISLATION 32(g), one law per node).
