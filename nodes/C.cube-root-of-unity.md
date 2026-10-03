---
id: C.cube-root-of-unity
title: Two thirds of J, cubed, is one
type: theorem
level: object
kind: law
rung: C
order: 1030
setting: classical
equality: "≐"
domain: positive
law: "([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) ≐ o"
units: "ω³ = 1, ω = e^{2πi/3}"
gloss_check: "1"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James); the roots of unity as e^{2πik/n}: De Moivre 1707–22, Euler 1748; their cyclotomic structure: Gauss 1801"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.multiplication, C.phase, mult.involution, mult.cardinality, mult.unit-law, mult.distribution, Z.inversion, C.double-phase]
see_also: [C.cube-root-of-negation, C.double-phase, C.period-absorption]
aliases: [cube root of unity, ω, "e^{2πi/3}", roots of unity]
concepts: [phase, root, one, period]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) ≐ o` | — | ω³ = 1 |

The roots of unity are fractional counts of J with an even numerator: e^{2πik/n} is J with the count 2k/n, instanced. Here k = 1, n = 3.

## Plain

Two thirds of a half-turn, three times over, is two half-turns — a whole turn, which the circle forgets.

## Derivation

| form | rule | note |
|---|---|---|
| `([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))])` | given | three copies of the instance of J × 2 ÷ 3, multiplied — [[mult.multiplication]], [[C.phase]] |
| `(([J] [oo] <[ooo]>) ([J] [oo] <[ooo]>) ([J] [oo] <[ooo]>))` | [[mult.involution]] | the unit three times, directly inside the outer instance — absorbing |
| `(([([J] [oo] <[ooo]>)] [oo]) ([J] [oo] <[ooo]>))` | [[mult.cardinality]] | two copies become the count 2 |
| `(([([J] [oo] <[ooo]>)] [oo]) ([([J] [oo] <[ooo]>)] [o]))` | [[mult.unit-law]] | the third gets the count 1 |
| `(([([J] [oo] <[ooo]>)] [ooo]))` | [[mult.distribution]] | collect: the count 3 |
| `(([J] [oo] <[ooo]> [ooo]))` | [[mult.involution]] | the unit, directly inside the inner instance — absorbing |
| `(([J] [oo]))` | [[Z.inversion]] | `<[ooo]> [ooo]` cancels |
| `(J J)` | [[mult.cardinality]] | right to left, with A = J: J with the count 2 is two J |
| `o` | [[C.double-phase]] | `(J J) ≐ o` |

## Confirms

ω³ = 1, and with it the pattern: the n-th roots of unity are `(([J] [2k] <[n]>))` for k = 0, …, n−1, and their multiplication is the addition of counts, with [[C.period-absorption]] reducing the count mod 2 — the cyclic group ℤ/n as the arithmetic of fractions of J under an instance. This node is the case n = 3, k = 1, written out; the general statement is a schema the chart will need the induction gap for ([[N.induction]]). It is **not** yet a theory of cyclotomic fields: that ω satisfies ω² + ω + 1 = 0 is a further law, owed.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step directly under an instance; the final step is the period, which A5′ absorbs |
| JH, JO | holds | per slice |
| JP | guarded | the count 3 must be a unit at p (p ≠ 3); ℚ_p contains ω exactly when p ≡ 1 (mod 3), which is what the wall criterion must reproduce |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
