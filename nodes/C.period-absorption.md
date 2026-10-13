---
id: C.period-absorption
title: Period absorption — J J cancels inside an instance
type: theorem
level: object
kind: law
rung: C
order: 970
setting: classical
equality: "≐"
domain: complex
law: "(A J J) ≐ (A)"
units: "e^{a + 2πi} = e^a"
gloss_check: "exp(A)"
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
known_since: "1993 (James, Ch. 6 §6.3 p. 47, constraint 2: 'Allow Js to cancel only within an instance boundary and after applying other reductions')"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.involution, C.double-phase, mult.log-of-one]
guarded_by: [mult.seam-decree]
see_also: [C.double-phase, C.phase-sign, mult.seam-decree, C.james-discipline, schema.period-multiple]
aliases: [period absorption, J-cancellation inside an instance, "e^{a+2πi} = e^a", periodicity of exp]
concepts: [phase, period, exponential]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(A J J) ≐ (A)` | — | e^{a + 2πi} = e^a |

A pair of J standing directly inside an instance may be erased — and only there. This is the periodicity of the exponential, and it is James's second disciplinary rule written as a law with its condition built into the shape.

## Plain

Inside a circle, a whole turn is nothing. Outside one, it is a whole turn, and must not be thrown away.

## Derivation

| form | rule | note |
|---|---|---|
| `(A J J)` | given | — |
| `(A [(J J)])` | [[mult.involution]] | the unit right to left on `J J`, directly inside the instance — an absorbing position |
| `(A [o])` | [[C.double-phase]] | `(J J) ≐ o` |
| `(A)` | [[mult.log-of-one]] | `[o] ≐ void` |

## Confirms

The period of exp: e^{a + 2πi} = e^a for every complex a. This is the sound content of James's "J-cancellation": the pair cancels inside an instance because the instance forgets whole turns, and the derivation says exactly where that happens — the unit step is taken in the absorbing position, which the seam decree admits unconditionally. Its content 2πi is off the strip, so the step is a *seam step* and the law carries the decree in its price (`guarded_by`, by position): a law whose statement is an exact identity of ℂ while its derivation leans on the decree, as [[Q.reciprocal-of-negative]] and [[C.phase-under-instance]] before it. It is **not** `J J ≐ void`, and it is **not** `[A J J] ≐ [A]`: under a square `J J` is just the summand 2πi, and ln(a + 2πi) is not ln a. In J1 this law is the completion axiom A5′ itself, `(λ A) ≐ (A)` for λ ∈ Λ, at λ = ω.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | this is A5′ at λ = ω: exp kills the kernel Λ |
| JO | guarded | slice-local: `(A J_u J_u) ≐ (A)` when A lies in the slice of u (for real A, any u); across slices J_u does not commute with A |
| JH | replaced | `(A J J)` is `(A)` only in the slice of i — the first non-commutative wall, [[H.slice-wall]]: fails on generic quaternions (census/h-ledger.md) |
| JP | holds | `(ω_v A) ≐ (A)` at every place, by the same absorbing step |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none here — the bare `J J ≐ void` is struck at [[C.double-phase]], its home; note that under a square `[A J J]` is ln(a + 2πi), not ln a, so the pair is not cancellable there either.

## Notes

James's rule adds "and last": cancel J J only after other reductions. The chart does not need the ordering clause — admissibility is decided by position, so the step may be taken at any time it is available — but the clause is a sound heuristic for reaching the instance in the first place.
