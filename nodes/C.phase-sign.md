---
id: C.phase-sign
title: Under an instance the sign of J is immaterial
type: theorem
level: object
kind: law
rung: C
order: 980
setting: classical
equality: "≐"
domain: complex
law: "(A <J>) ≐ (A J)"
units: "e^{a − iπ} = e^{a + iπ}"
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
known_since: "1993 (James)"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [C.period-absorption, Z.inversion]
see_also: [C.period-absorption, C.phase-under-instance, mult.seam-decree]
aliases: [phase sign, "e^{−iπ} = e^{iπ}", J versus −J]
concepts: [phase, negation, period]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(A <J>) ≐ (A J)` | — | e^{a − iπ} = e^{a + iπ} |

A half-turn one way or the other: under an instance they agree. Not on the bare page — `J` and `<J>` are iπ and −iπ, and the calculus keeps them apart.

## Plain

Turning half way left or half way right lands you in the same place — as long as you are inside a circle, which only knows where you landed.

## Derivation

| form | rule | note |
|---|---|---|
| `(A <J>)` | given | the mirrored phase |
| `(A <J> J J)` | [[C.period-absorption]] | right to left, with A := `A <J>`: a whole turn is created inside the instance |
| `(A J)` | [[Z.inversion]] | `<J> J` cancels |

## Confirms

e^{−iπ} = e^{iπ} = −1: the two half-periods ±iπ land on the same point. The law is exact, and it is as far as the calculus goes toward `J ≐ <J>` — which is **false** (iπ ≠ −iπ) and is the confusion the collapse route turns into `oo ≐ void` ([[mult.seam-decree]], Notes). A useful instance: `(<J>) ≐ <o>`, with A void.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | −ω/2 ≡ ω/2 mod Λ, and the instance absorbs the difference (A5′) |
| JO | guarded | slice-local, as [[C.period-absorption]] |
| JH | replaced | −J and J are antipodes on the sphere of phases ([[H.phase-sphere]]), and the instance identifies them only in the slice of i ([[H.slice-wall]]): fails on generic quaternions (census/h-ledger.md) |
| JP | holds | by the same absorbing step at a place |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

- ~~`J ≐ <J>`~~ — false on the bare page (iπ ≠ −iπ); only its instance holds. Refuted 2026-10-03 as a step of the collapse route ([[mult.seam-decree]]).

## Notes

—
