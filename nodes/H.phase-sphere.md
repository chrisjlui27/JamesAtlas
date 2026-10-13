---
id: H.phase-sphere
title: Minus one has a sphere of logarithms
type: theorem
level: meta
kind: law
rung: H
order: 1750
setting: JH
equality: "≐"
domain: complex
law: "(J_u) ≐ <o> for every pure unit u, with J_u := πu: the logs of −1 in the principal band form the 2-sphere π·S²; and the rigidity dichotomy (JH-12): <A> ≐ ([A] J_u) for every u when A is real positive, and only for u = ±(the direction of A) otherwise"
units: "exp(πu) = −1 for every unit pure quaternion u; J_j = πj, J_k = πk are the seeds' logs; e^{(π/2)u} e^{(π/2)v} = u × v for u ⟂ v (JH-18: ij = k from James's own i)"
gloss_check: ""
witness: tools/models/h_phase_sphere.py
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
known_since: "Hamilton 1843 (every unit pure quaternion squares to −1); 2026-08 (the JH-Calculus report, JH-12 rigidity dichotomy, JH-18 half-phase cross product); this rung, 2026-10-07"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [C.euler-identity, H.k, H.pure-square, H.seed, J1.half-period]
see_also: [H.polar-form, H.seam-guard, H.slice-wall, schema.roots-of-negation, H.anticommutation, C.phase-unique]
aliases: [the phase sphere, J_u, the sphere of logs of −1, π·S², JH-12, the rigidity dichotomy, JH-18, half-phases, the square roots of −1]
concepts: [quaternion, negation, logarithm, period]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(J_u) ≐ <o>` for every pure unit u, J_u = πu | e^{πu} = −1 | the square roots of −1 in ℍ are the 2-sphere of pure units |

On the trunk −1 has one log in the band, J = πi ([[J1.half-period]]); the equation `(J) ≐ <o>` is Euler's identity ([[C.euler-identity]]). In ℍ every pure unit u is a square root of −1 ([[H.pure-square]] with b² + c² + d² = 1), so e^{πu} = −1 for every u, and the logs of −1 in the band |Im| ≤ π form the whole sphere π·S² — the second seed J_j = πj ([[H.seed]]) is one point of it, J_k another, and the page has a form for exactly those the seeds name. Two consequences the report proves and the witness checks: the **rigidity dichotomy** (JH-12) — `<A> ≐ ([A] J_u)` holds for every direction u when A is real positive, and for a non-real A only for u = ±(the direction of A), so a negation can be "a half-turn in any plane" only of a real; and the **half-phase law** (JH-18) — e^{(π/2)u} e^{(π/2)v} = u × v for orthogonal u, v, so that `([((J_i/2)) ; ((J_j/2))])`, the product of James's own i with the j the seed gives, is k: Hamilton's ij = k is a statement about quarter turns composing across planes, which is what the ordered square ([[H.k]]) encodes.

## Plain

In the complex numbers there is one way to turn half-way round. In the quaternions there is a whole sphere of planes to turn in, and a half-turn in any of them lands on minus one.

## Derivation

none — a theorem of the reading, witnessed.

| statement | rule | note |
|---|---|---|
| exp(πu) = −1 for every pure unit u | [[H.pure-square]] | witness part (1): 60 random units; algebraically (πu)² = −π², so exp(πu) = cos π + u sin π — at u = i Euler's identity ([[C.euler-identity]]) with J = πi ([[J1.half-period]]), at u = j the seed ([[H.seed]]) |
| the band meets {L : exp L = −1} exactly in π·S² | — | witness part (2): random logs in the band, exp L = −1 iff \|L\| = π and Re L = 0 |
| <A> ≐ ([A] J_u) for every u iff A is real positive; else only u = ±dir(A) | — | witness part (3): JH-12 |
| e^{(π/2)u} e^{(π/2)v} = u × v for u ⟂ v | [[H.k]] | witness part (4): JH-18; with u = i, v = j the product is k |
| J_{−u} = −J_u and e^{J_u} = e^{J_{−u}} | — | witness part (5): antipodes give the same −1 |

## Confirms

The sphere is the seam of [[H.seam-guard]] and the sphere of directions of [[H.slice-wall]]: three faces of one fact, that −1's log is not unique in direction. The unit quaternions S³ are the suspension of this sphere ([[H.polar-form]], JH-17). It is **not** a statement that the *form* `J` has many values: `J = [<o>]` is one form with the pinned value πi, and the other points of the sphere are forms only when a seed names them — `Jj` for πj ([[H.seed]]), `[k]`-shaped forms for πk — or when the direction is written out as a quaternion.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | one point, J = πi: [[C.euler-identity]], [[J1.half-period]] |
| JH | holds | the witness |
| JO | holds | a 6-sphere of pure units, each squaring to −1 |
| JP | holds | at 2 the square roots of −1 in the Hurwitz order at 2 form the conjugacy class of i, all in 1 + πO ([[H.ramified-place]]); at odd p the pure square roots of −1 are the quadric b² + c² + d² ≡ 1 (and the centre adds ±√−1 when p ≡ 1 mod 4) — read by hand from the places' witnesses, not computed as a sphere (owed) |

| reading | cell | why |
|---|---|---|
| C | EXACT | the slice of i: one point of the sphere |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The plan's three nodes — the sphere, the rigidity dichotomy (JH-12) and the half-phase law (JH-18) — are one node here: the two laws are properties of the sphere and share its witness. [[schema.roots-of-negation]] on the trunk counts the roots of −1 of each order in ℂ; in ℍ the count is a sphere for every even order, which is the first place the chart's counting schemas stop counting.
