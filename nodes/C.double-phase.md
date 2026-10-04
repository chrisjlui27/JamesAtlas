---
id: C.double-phase
title: Two J under an instance is one
type: theorem
level: object
kind: law
rung: C
order: 960
setting: classical
equality: "≐"
domain: positive
law: "(J J) ≐ o"
units: "e^{2πi} = 1"
gloss_check: "1"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James, Ch. 6 §6.2.2 p. 45, Theorem 2 'J Cancellation' — stated there without its instance; in its sound form here)"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [C.phase-under-instance, C.phase-value, Z.cancellation]
see_also: [C.period-absorption, C.phase-sign, mult.seam-decree, C.james-discipline]
aliases: [double phase, the period, "e^{2πi} = 1", J-cancellation]
concepts: [phase, period, one]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(J J) ≐ o` | — | e^{2πi} = 1 |

Two half-turns under one instance are a whole turn, which is nothing to the circle: the period of the exponential, as a theorem.

## Plain

Turn half way round twice and you face where you started — but only the circle can see that; written on the bare page, two J are still two J.

## Derivation

| form | rule | note |
|---|---|---|
| `(J J)` | given | two half-turns under one instance |
| `<(J)>` | [[C.phase-under-instance]] | with A = J: one J becomes the sign outside |
| `<<o>>` | [[C.phase-value]] | `(J) ≐ <o>` |
| `o` | [[Z.cancellation]] | two mirrors cancel |

## Confirms

e^{2πi} = 1 — the periodicity of the exponential — as (−1)·(−1) = 1 read through J. The same law comes out of the product of negatives directly: `(J J)` is `([<o>] [<o>])`, which is `([o] [o])` by [[mult.product-of-negatives]] and `o` by the unit law. What it is **not**: `J J ≐ void`. The content 2πi of `(J J)` is not nothing, and the step that would strip the instance off this law — `[(J J)] → J J` at depth 0 — is the seam step the decree refuses ([[mult.seam-decree]]). `(J J) ≐ o` is James's J-cancellation in the only form in which it is sound, and [[C.period-absorption]] is its general shape.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | J J = ω, the generator of Λ, and `(ω) ≐ (void) = o` by A5′ — while `J J ≐ void` *fails* in J1 (ω is not void), which is the point of the enriched calculus |
| JH, JO | holds | per slice: `(J_u J_u) ≐ o` for every unit direction u, each slice being a copy of ℂ |
| JP | holds | `(ω_v) ≐ o` at every place, with J_p = ω_v/2 ([[C.phase]]) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

- ~~`J J ≐ void`~~ — James's J-cancellation stated without its instance; refuted as a depth-0 law 2026-10-03 (its content is 2πi; the collapse it causes is recorded at [[mult.seam-decree]], its restatement in James's terms at [[C.james-discipline]]).

## Notes

—
