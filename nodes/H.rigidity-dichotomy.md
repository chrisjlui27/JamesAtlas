---
id: H.rigidity-dichotomy
title: A negation is a half-turn in which planes?
type: theorem
level: meta
kind: law
rung: H
order: 1761
setting: JH
equality: "≐"
domain: complex
law: "<A> ≐ ([A] J_u) for every pure unit u when A is a positive real, and for a non-real A only for u = ±(the direction of A): the rigidity dichotomy (JH-12)"
units: "e^{ln r + πu} = −r for every u; e^{log A + πu} = −A only in A's own plane"
gloss_check: ""
witness: tools/models/h_rigidity.py
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: holds
  JP: untested
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "2026-08 (the JH-Calculus report, JH-12); this rung, 2026-10-07; its own node 2026-10-13"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [C.phase-under-instance, H.phase-sphere, H.slice-wall]
see_also: [H.half-phase, H.seam-guard, J1.phase-independence, C.phase-under-instance]
aliases: [JH-12, the rigidity dichotomy, which half-turns negate]
concepts: [quaternion, negation, logarithm]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `<A> ≐ ([A] J_u)` for every u when A is real positive; only for u = ±dir(A) otherwise | −A = e^{log A + πu} | a negation is a half-turn, and off the reals the plane of the turn is forced |

On the trunk, phase under an instance ([[C.phase-under-instance]]) says `(A J) ≐ <(A)>`: adding a half-turn to a log negates the instance. In ℍ there is a sphere of half-turns ([[H.phase-sphere]]), and the question is which of them negate a given A. The answer is a dichotomy: a positive real is negated by a half-turn in *every* plane (its log is real and commutes with every direction); a quaternion off the reals is negated only by the half-turn in its *own* plane, u = ±(the direction of its pure part) — any other direction lands somewhere else, because exp(log A + πu) is −A only when log A and πu commute ([[H.slice-wall]]). So "a negation is a half-turn" is true in ℍ, but the plane is not free: it is the slice of the thing being negated.

## Plain

Turning a positive number half-way round in any plane gives its negative. Turning any other quaternion half-way round gives its negative only if you turn in its own plane.

## Derivation

none — a theorem of the reading, witnessed.

| statement | rule | note |
|---|---|---|
| e^{ln r + πu} = −r for every pure unit u and positive r | [[H.phase-sphere]] | witness part (1): 40 random pairs |
| e^{log A + πv} = −A for v = ±dir(Im A) | [[C.phase-under-instance]] | witness part (2): the trunk's law in A's own slice |
| e^{log A + πw} ≠ −A for a generic direction w | [[H.slice-wall]] | witness part (3): the two logs do not commute |

## Confirms

That the trunk's phase rule is slice-bound in ℍ, which is why [[C.phase-under-instance]] and [[J1.phase-independence]] are `replaced` there: the half-turn that negates A is in A's plane, and the pinned J = πi is in the plane of i. It is **not** a failure of negation — `<A>` is one form with one value — only of the *spelling* of negation as a half-turn.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | one plane: `(A J) ≐ <(A)>` always ([[C.phase-under-instance]]) |
| JH | holds | the witness |
| JO | holds | the same dichotomy with a 6-sphere of planes |
| JP | untested | the places pin −1 to one direction and read no sphere; owed with [[H.phase-sphere]]'s place cell |

| reading | cell | why |
|---|---|---|
| C | EXACT | one plane |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

Split from [[H.phase-sphere]] on 2026-10-13 (LEGISLATION 32(g), one law per node); the witness is the sphere's third part made its own script.
