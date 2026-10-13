---
id: H.hurwitz-units
title: The twenty-four units
type: theorem
level: meta
kind: law
rung: H
order: 1780
setting: JH
equality: "≐"
domain: natural
law: "the units of the Hurwitz order are the 24 quaternions ±1, ±i, ±j, ±k, (±1 ± i ± j ± k)/2: a group 2T of order 24 with element orders {1, 2, 3, 4, 6} (counts 1, 1, 8, 6, 8); Q₈ = {±1, ±i, ±j, ±k} is normal and 2T = ⟨ζ⟩ ⋉ Q₈ with ζ = (−1 + i + j + k)/2 of order 3; each has norm one and inverse q̄"
units: "the binary tetrahedral group 2T ≅ SL₂(𝔽₃); the vertices of the 24-cell; the elements of norm 1 in the Hurwitz order"
gloss_check: ""
witness: tools/models/h_hurwitz_units.py
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: replaced
  JP: holds
readings:
  C: ABSENT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "Hurwitz 1896 (the order and its 24 units, with the four-square theorem re-proved from them); 2026-08 (the JH-Calculus report, JH-19: the de-collapse of the 16-valued world); this rung, 2026-10-07"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.four-squares, H.inverse, H.k, H.norm, H.quaternion, Q.half]
see_also: [H.twenty-four, H.ramified-place, place.local-wall, schema.roots-of-unity, H.conjugate]
aliases: [the Hurwitz units, 2T, the binary tetrahedral group, the 24-cell, Q₈, ζ = (−1 + i + j + k)/2, JH-19, the de-collapse]
concepts: [quaternion, torsion, root, selection]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| the 24 quaternions ±1, ±i, ±j, ±k, (±1 ± i ± j ± k)/2 form a group under the ordered product, with the orders and structure stated | — | the binary tetrahedral group 2T |

The torsion of the rung. The quaternions of [[H.quaternion]] with integer or all-half-integer parts form Hurwitz's order, and its units — the elements of norm one ([[H.norm]]), each its own conjugate's inverse ([[H.inverse]]) — are twenty-four: the eight of Q₈ (the units of the Lipschitz order ℤ + ℤi + ℤj + ℤk) and the sixteen half-integer ones. Closed under the product by [[H.four-squares]] (norm one times norm one), they are a group, 2T, with ζ = (−1 + i + j + k)/2 of order three normalizing Q₈: 2T = ⟨ζ⟩ ⋉ Q₈, every element uniquely ζ^a·q. The element orders are 1, 2, 3, 4, 6 — eight elements of order 3 (the half-integer units with real part −½), six of order 4 (±i, ±j, ±k), eight of order 6 (real part +½) — and no element of order 8 or 12: the roots of unity ([[schema.roots-of-unity]]) that ℍ's integers select. The **de-collapse** (JH-19): the sixteen states {±1 ± i ± j ± k} of the report's "16-valued world" are closed under the Q₈ operators but not under addition; their additive-multiplicative closure is the checkerboard {x ∈ ℤ⁴ : all parts of one parity} = 2·O, and halving ([[Q.half]], `(<[oo]>)`) brings it to O and the 16 states to the 16 half-integer units — the 24 are what the 16 become once addition is allowed.

## Plain

Among the quaternions with whole-number or all-half-number parts, exactly twenty-four have size one. They multiply among themselves, they come in orders one, two, three, four and six, and they are the vertices of the 24-cell.

## Derivation

none — a theorem of the reading, witnessed exactly over the ℚ-quaternions of [[H.quaternion]].

| statement | rule | note |
|---|---|---|
| the 24 are closed under the product and the inverse | [[H.four-squares]], [[H.inverse]] | witness part (1) |
| the orders are {1, 2, 3, 4, 6} with counts 1, 1, 8, 6, 8 | — | witness part (2) |
| Q₈ is normal; ζ has order 3; 2T = ⟨ζ⟩ ⋉ Q₈ uniquely | [[H.k]] | witness part (3) |
| the 16 states are closed under Q₈, not under addition; their closure is 2·O; halving reaches the 24 | [[Q.half]] | witness part (4): JH-19 |
| every Hurwitz unit has norm one and inverse q̄ | [[H.norm]] | witness part (5) |

## Confirms

Hurwitz's order is the one whose units are "enough": with them the order is Euclidean and Lagrange's four-square theorem follows (the seal the ROADMAP owes to a later rung). At the place 2 the 24 are the elements of norm 1 of the global order and the torsion the reading names — the local order O₂ has infinitely many more, their conjugates ([[H.ramified-place]]); at an odd place they are a subgroup of GL₂ of the page. And 24 is the first wall number of the trunk, M(2) ([[place.local-wall]]) — an ANALOGY the chart records and does not equate, [[H.twenty-four]]. It is **not** the whole torsion of ℍ^×: every unit quaternion has finite order or not as its angle is rational or not, and the sphere of them is S³; the 24 are the torsion the *integers* of ℍ select, as ±1, ±i are what ℤ[i] selects in ℂ.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | the units of ℤ[i], four of them |
| JH | holds | the witness |
| JO | replaced | Coxeter's integral octonions have 240 units — the roots of E₈ — and the 24 are the quaternionic ones among them |
| JP | holds | the 24 are units of the page at every place: at 2 the torsion of the global order, named by the reading, inside the larger torsion of the local order ([[H.ramified-place]]); at odd p a subgroup of GL₂(ℤ/pⁿ), with 2T ≅ SL₂(𝔽₃) at p = 3 |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

Of the sixteen half-integer units, those with an even number of minus signs among the four parts and those with an odd number split 8 : 8 into the orders 3 and 6 as the real part's sign decides (−½ gives order 3, +½ order 6); the witness counts rather than argues.
