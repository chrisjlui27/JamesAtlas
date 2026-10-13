---
id: H.polar-form
title: Every quaternion is a modulus times a phase in some plane
type: theorem
level: meta
kind: law
rung: H
order: 1765
setting: JH
equality: "≐"
domain: complex
law: "q ≐ ([R] ([J_u] [T])) for q ≠ 0: q = r·e^{tπu} with r = |q|, u the direction of the pure part and t ∈ [0, 1] — unique off the negative reals, where t = 1 and u is free; S³ is the suspension of the phase sphere (JH-17); the 120° law (JH-15): |u + v| = 1 ⟹ J_u J_v is again a half-turn, e^{π(u+v)} = −1; interference (JH-16): e^{π Σu_i} = ±1 iff |Σu_i| is an even/odd integer"
units: "q = r(cos θ + u sin θ), θ = tπ; two juxtaposed phases are a third exactly when their directions are 120° apart"
gloss_check: ""
witness: tools/models/h_polar.py
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: holds
  JP: replaced
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "Hamilton 1843–44 (tensor and versor: q = Tq·Uq, Uq = cos θ + u sin θ); 2026-08 (the JH-Calculus report, JH-15, JH-16, JH-17); this rung, 2026-10-07"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [C.polar-form, H.norm, H.phase-sphere, H.quaternion]
see_also: [place.polar-form, H.ramified-place, H.split-place, C.euler-formula, C.phase-unique, H.seam-guard]
aliases: [quaternion polar form, r·e^{tπu}, JH-17, the suspension of the phase sphere, JH-15, the 120° law, JH-16, phase interference, Hamilton's versor]
concepts: [quaternion, polar-form, modulus, period]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `q ≐ ([R] ([J_u] [T]))`, R = \|q\|, u = dir(Im q), T ∈ [0, 1] | q = r e^{tπu} | Hamilton: q = Tq · Uq, the versor a rotation in the plane of u |

Every nonzero quaternion lies in the slice of its own pure part, C_u = ℝ + ℝu, and in that slice the trunk's polar form applies verbatim with J replaced by J_u ([[C.polar-form]], the Slice Principle): q = r·e^{tπu}. The modulus is `([R])` with R² the norm ([[H.norm]]); the phase is a fraction T of the half-turn J_u ([[H.phase-sphere]]). The spelling is unique except on the negative reals, where t = 1 and *every* u serves — the seam again — and at the positive reals, where t = 0 and u is idle; so the unit quaternions S³ are the sphere of directions with its two poles ±1 pinched: the suspension of the phase sphere (JH-17). Two laws about juxtaposed phases follow and are witnessed: the **120° law** (JH-15) — `J_u J_v`, the juxtaposition of two half-turn logs, is again the log of −1 exactly when |u + v| = 1, i.e. when u and v are 120° apart (then π(u + v) is π times a unit); and **interference** (JH-16) — e^{π Σ u_i} is +1 or −1 according as |Σ u_i| is an even or odd integer, and otherwise is not real at all: juxtaposed half-turns in different planes do not add up to whole turns the way they do in ℂ.

## Plain

Pick the plane a quaternion lives in; inside that plane it is an ordinary complex number, a size times a turn. Turns in different planes do not simply add: two half-turns make a half-turn only when their planes are at 120°.

## Derivation

none — a theorem of the reading, witnessed; on the page it is [[C.polar-form]] read in the slice of u.

| statement | rule | note |
|---|---|---|
| q = \|q\| exp(tπu), t ∈ [0, 1], u = dir(Im q) | [[C.polar-form]] | witness part (1): 60 random quaternions ([[H.quaternion]]), \|q\|² the norm ([[H.norm]]) |
| non-uniqueness exactly on the negative reals (t = 1, u free) | [[H.phase-sphere]] | witness part (2) |
| \|u + v\| = 1 ⟹ exp(π(u + v)) = −1 | — | witness part (3): JH-15 |
| exp(π Σu_i) = 1 iff \|Σu\| even integer, −1 iff odd, else non-real | — | witness part (4): JH-16 |
| J_i J_j J_k has phase π√3 in the direction (i + j + k)/√3 | — | witness part (5): three seeds juxtaposed are not a turn |

## Confirms

Hamilton's tensor–versor decomposition and his picture of unit quaternions as rotations; and the Slice Principle in its most useful form — to compute with one quaternion, work in ℂ. It is **not** a form with a variable direction: `J_u` is a form only for the directions the seeds name ([[H.seed]]); the law is a statement of the reading, and the chart records it at the meta level for that reason.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | [[C.polar-form]], u = i |
| JH | holds | the witness |
| JO | holds | every octonion lies in a complex subalgebra too |
| JP | replaced | at 2 by the polar form of [[H.ramified-place]] — a power of π, a Hurwitz unit, a principal unit, in the half-shells; at odd p by the matrix decomposition of [[H.split-place]] (Cartan: a unit of the page is a product of a diagonal and an orthogonal part); the trunk's [[place.polar-form]] is the centre's |

| reading | cell | why |
|---|---|---|
| C | EXACT | the slice of i |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The plan's `H.120-law` and the interference law are folded in here: they are statements about the phases of this form and share its witness. Their place cells are the polar form's `replaced`: the sphere of phases has no finite-place analogue the chart can read yet (LEGISLATION 32 (g), pending).
