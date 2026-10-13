---
id: H.120-law
title: Two half-turns make a half-turn at 120°
type: theorem
level: meta
kind: law
rung: H
order: 1766
setting: JH
equality: "≐"
domain: complex
law: "J_u J_v ≐ J_{u+v} when |u + v| = 1: two juxtaposed half-turn logs are the log of −1 again exactly when their directions are 120° apart, e^{π(u+v)} = −1 (JH-15)"
units: "|u + v| = 1 iff the angle between u and v is 120°; then π(u + v) lies on the sphere of logs of −1"
gloss_check: ""
witness: tools/models/h_120_law.py
holds:
  classical: fails
  J1: fails
  JH: holds
  JO: holds
  JP: untested
readings:
  C: ABSENT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "2026-08 (the JH-Calculus report, JH-15); this rung, 2026-10-07; its own node 2026-10-13"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.phase-sphere, void.space]
see_also: [H.interference, H.polar-form, J1.half-period, C.cube-root-of-unity]
aliases: [JH-15, the 120° law, two phases are a third]
concepts: [quaternion, period, addition]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `J_u J_v ≐ J_{u+v}` when \|u + v\| = 1 | π u + π v = π(u + v), a half-turn log iff \|u + v\| = 1 | two unit vectors sum to a unit vector iff they are 120° apart |

Juxtaposition is addition ([[void.space]]), so `J_u J_v` is the log π(u + v), and it is a log of −1 — a point of the sphere of [[H.phase-sphere]] — exactly when u + v is again a unit vector, which happens exactly when the angle between u and v is 120°. On the trunk two half-turns make a whole turn, `J J ≃ ω`: that is the degenerate case u = v, where \|u + v\| = 2 and the sum is a *whole* turn, not a half one. In ℍ the half-turns are a sphere, and two of them add to a third only at the one angle where the triangle of directions closes.

## Plain

In the plane, two half-turns always make a full turn. In the quaternions two half-turns in different planes make a half-turn again when the planes are at 120° to each other — and three such make a full turn.

## Derivation

none — a theorem of the reading, witnessed.

| statement | rule | note |
|---|---|---|
| \|u + v\| = 1 ⟹ e^{π(u+v)} = −1 | [[H.phase-sphere]] | witness part (1): 40 random pairs at 120° |
| at any other angle `(J_u J_v)` ≠ −1 | — | witness part (2) |
| three directions at mutual 120° in a plane sum to zero: `(J_u J_v J_w)` = 1 | [[void.space]] | witness part (3) |

## Confirms

A new arithmetic of phases that ℂ does not have: on the trunk the only relation among half-turn logs is `J J ≃ ω` ([[J1.half-period]]); in ℍ the half-turn logs form a sphere and *add* along it. The three directions at mutual 120° that sum to zero are the quaternionic shadow of the three cube roots of unity summing to zero ([[C.cube-root-of-unity]]). It is **not** a law of the forms: `J_u` is a form only for the seeds' directions, and `Jj J` (πj + πi) has \|i + j\| = √2 — the chart's two named half-turns are at 90°, not 120°, and their juxtaposition is not a half-turn ([[H.interference]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | fails | one direction: \|u + v\| is 0 or 2, never 1 |
| JH | holds | the witness |
| JO | holds | the same geometry on a 6-sphere |
| JP | untested | the places read no sphere of half-turns; owed with [[H.phase-sphere]]'s place cell |

| reading | cell | why |
|---|---|---|
| C | ABSENT | no second direction |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

Split from [[H.polar-form]] on 2026-10-13 (LEGISLATION 32(g), one law per node).
