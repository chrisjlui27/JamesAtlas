---
id: H.interference
title: Juxtaposed half-turns interfere
type: theorem
level: meta
kind: law
rung: H
order: 1767
setting: JH
equality: "≐"
domain: complex
law: "(J_{u₁} … J_{uₙ}) ≐ o when |u₁ + … + uₙ| is an even integer, ≐ <o> when odd, and is not real otherwise: half-turn logs in different planes do not add up to whole turns the way they do in ℂ (JH-16)"
units: "e^{π Σuᵢ} = ±1 iff |Σuᵢ| ∈ ℤ, with the sign of (−1)^{|Σu|}; (J_i J_j J_k) has phase π√3 about (i + j + k)/√3"
gloss_check: ""
witness: tools/models/h_interference.py
holds:
  classical: replaced
  J1: replaced
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
known_since: "2026-08 (the JH-Calculus report, JH-16); this rung, 2026-10-07; its own node 2026-10-13"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.120-law, H.phase-sphere, J1.half-period]
see_also: [H.polar-form, schema.period-multiple, H.slice-wall]
aliases: [JH-16, phase interference, interference of half-turns]
concepts: [quaternion, period, addition]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(J_{u₁} … J_{uₙ})` ≐ `o` iff \|Σu\| is an even integer, ≐ `<o>` iff odd, otherwise not real | e^{π Σuᵢ} | the sum of unit vectors has integer length only by coincidence |

A juxtaposition of half-turn logs is the log π·Σuᵢ ([[void.space]]), and its instance is e^{πs} for s = Σuᵢ: a rotation by π\|s\| about s/\|s\|. That is 1 when π\|s\| is an even multiple of π, −1 when an odd one, and otherwise a non-real unit. On the trunk every uᵢ is i, \|s\| = n, and the law collapses to the parity of n — `J J ≃ ω` and whole turns absorb ([[J1.half-period]], [[schema.period-multiple]]). In ℍ the lengths of sums of unit vectors are generic, so juxtaposed half-turns in different planes *interfere*: they add as vectors, and the whole turn is the exception, not the rule. The 120° case ([[H.120-law]]) is where \|s\| = 1.

## Plain

Half-turns in different planes add like arrows, not like counts: two of them make a full turn only if the arrows point the same way, and three seeds' worth of half-turns — i, j, k — make neither a full turn nor a half one.

## Derivation

none — a theorem of the reading, witnessed.

| statement | rule | note |
|---|---|---|
| e^{π Σu} = 1 iff \|Σu\| is an even integer, −1 iff odd, else non-real | [[H.phase-sphere]] | witness part (1): 60 random juxtapositions of 2–5 directions |
| `(J_i J_j J_k)` has phase π√3 about (i + j + k)/√3, neither 1 nor −1 | [[H.120-law]] | witness part (2): \|i + j + k\| = √3 |
| in one plane the trunk's law: `(J J)` = 1 | [[J1.half-period]] | witness part (3) |

## Confirms

That the period lattice of ℍ is not a group: 2πi + 2πj is not a period though each summand is ([[H.slice-wall]]), and the sum of two half-turn logs is a half-turn log only at 120°. It is **not** a failure of the trunk's absorption on its own slice — in one plane the law is exactly `J J ≃ ω` — but the reason the trunk's phase laws are `replaced` off the plane.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | one plane: the law is the parity of the count of half-turns, [[J1.half-period]] and [[schema.period-multiple]] |
| JH | holds | the witness |
| JO | holds | the same vector addition on a 6-sphere |
| JP | untested | the places read no sphere of half-turns; owed with [[H.phase-sphere]]'s place cell |

| reading | cell | why |
|---|---|---|
| C | ABSENT | one direction |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

Split from [[H.polar-form]] on 2026-10-13 (LEGISLATION 32(g), one law per node).
