---
id: C.phase-under-instance
title: J under an instance is a sign
type: theorem
level: object
kind: law
rung: C
order: 950
setting: classical
equality: "≐"
domain: complex
law: "(A J) ≐ <(A)>"
units: "e^{a + iπ} = −e^a"
gloss_check: "-exp(A)"
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: guarded
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James, Ch. 6 §6.2.1 p. 45: 'the inverse jumping inside of the instance boundary', <(A)> = (A J))"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [C.phase-rule, mult.involution]
guarded_by: [mult.seam-decree]
see_also: [C.log-of-negative, C.phase-value, C.period-absorption, C.phase-sign]
aliases: [phase under an instance, "e^{a+iπ} = −e^a", J as a sign]
concepts: [phase, negation, exponential]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(A J) ≐ <(A)>` | — | e^{a + iπ} = −e^a |

Adding J inside a circle flips the sign outside it. This is the law that makes J a *phase*: on instances it acts as the sign, for every content whatever.

## Plain

Put the log of minus one in with the exponent and the result comes out negated — a half-turn, seen from outside the circle, is a minus sign.

## Derivation

| form | rule | note |
|---|---|---|
| `<(A)>` | given | the mirror of an instance |
| `([(A)] J)` | [[C.phase-rule]] | `<X> ≐ ([X] J)` with X = `(A)` |
| `(A J)` | [[mult.involution]] | the unit `[(A)] ≐ A` directly inside the instance — an absorbing position, so admitted for every A; for complex A with Im a outside (−π, π] the local equation is off by 2πik and the instance absorbs it: a seam step, guarded by position |

## Confirms

e^{a + iπ} = −e^a for every complex a, exactly, with no condition on a. The *statement* is exact in ℂ; the *derivation* leans on the decree's position clause for |Im a| > π (its one unit step is a seam step there), which is why the law carries `guarded_by` while staying NATIVE (Amendment A2). It is **not** the same law under a square: `[<(A)>] ≐ A J` (the log of a negated exponential) needs the unit at depth 0 and holds exactly when a + iπ lies on the strip, i.e. Im a ∈ (−2π, 0] — a guarded corollary of [[C.log-of-negative]], not written as a node.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the unit step is directly under an instance: the receipt is absorbed (depth-1 criterion, [[mult.involution]] Notes) |
| JO | guarded | slice-local: `(A J_u) ≐ <(A)>` when A lies in the slice of u — for real A every u serves; a J from another slice does not commute with A (the rigidity dichotomy, JH-12) |
| JH | replaced | `(A J)` is −e^A only when A commutes with the pinned J = πi: the rigidity dichotomy, JH-12 ([[H.phase-sphere]]) — a negation is a half-turn in the plane of A, `<(A)> ≐ (A J_u)` for u = ±dir(A); fails on generic quaternions (census/h-ledger.md) |
| JP | holds | the Phase rule and the absorbing unit both pass the audit at a place |

| reading | cell | why |
|---|---|---|
| C | EXACT | on all of ℂ |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
