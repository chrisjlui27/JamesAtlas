---
id: C.euler-identity
title: Euler's identity
type: theorem
level: object
kind: law
rung: C
order: 920
setting: classical
equality: "≐"
domain: positive
law: "o (J) ≐ void"
units: "1 + e^{iπ} = 0"
gloss_check: "0"
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
known_since: "1993 (James); Euler 1748"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [C.phase-value, Z.inversion, N.unit]
see_also: [C.phase-value, C.pi]
aliases: ["e^{iπ} + 1 = 0", Euler's identity]
concepts: [phase, zero, one]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `o (J) ≐ void` | — | 1 + e^{iπ} = 0 |

Five constants — 0, 1, e, i, π — in the standard telling; on the page, two forms and nothing, with the base e hidden in the circle and i and π both folded into J.

## Plain

One, next to the circled log of minus one, is nothing: the two cancel like a pile and its mirror, because that is what they are.

## Derivation

| form | rule | note |
|---|---|---|
| `o (J)` | given | the unit [[N.unit]] beside the instance of J |
| `o <o>` | [[C.phase-value]] | `(J) ≐ <o>` |
| `void` | [[Z.inversion]] | `o <o>` cancels |

## Confirms

Euler's identity in two rows, which tells you what it *is*: Inversion with the −1 spelled as e^{iπ}. The identity's reputation for mystery is the reputation of the counit `([<o>]) ≐ <o>`, i.e. of exp ∘ log being the identity even at −1. What it is **not**: a relation among five independent constants — on the page e is the circle, and i and π are not separately present at all; they appear only when J is factored at [[C.imaginary-unit]] and [[C.pi]].

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

James, p. 48: "Interpreting the abstract boundary as the natural logarithm makes J = ln −1 = iπ. This interpretation fulfills Euler's formula translated to J wrapped by instance: 1 + e^{iπ} = 0 versus o([<o>]) ="; and Appendix A.5, p. 73: "Euler's formula works because the form [<o>] was defined that way."
