---
id: alg.zeroth-power
title: The zeroth power is one
type: theorem
level: object
kind: law
rung: alg
order: 743
setting: classical
equality: "≐"
domain: positive
law: "(([[A]] [void])) ≐ o"
units: "a⁰ = 1  (a ≠ 0)"
gloss_check: "1"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James); Chuquet 1484 for the zeroth power"
entered: 2026-10-03
guide: shape-led
band: "6–8"
uses: [mult.exponentiation, mult.black-hole, mult.dominion, mult.hole-instance, N.unit]
see_also: [alg.first-power, alg.one-to-power, alg.zero-to-power]
aliases: ["a^0 = 1"]
concepts: [exponentiation, zero, one]
understood: "yes"
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[A]] [void])) ≐ o` | — | a⁰ = 1 |

The exponent zero is the void; its abstract is the black hole, and the black hole swallows the base.

## Plain

Anything to the power zero is one — not by convention here, but because the box around nothing is the bottomless pit, which swallows the base and leaves a circle around nothing.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[A]] [void]))` | given | a^0, [[mult.exponentiation]] |
| `(([[A]] □))` | [[mult.black-hole]] | `[void]` is □ |
| `((□))` | [[mult.dominion]] | □ swallows `[[A]]` |
| `(void)` | [[mult.hole-instance]] | the instance of the hole is nothing |
| `o` | [[N.unit]] | — |

## Confirms

a⁰ = 1 as a *theorem* about the black hole rather than a convention about empty products — one of the facts the walk exists to show. The proviso a ≠ 0 is real: with A the void, `[[void]]` is `[□]`, excluded ([[alg.zero-to-power]]), so 0⁰ has no form, which is the honest answer to a famous quarrel.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, JH, JO, JP | holds | — |
| J1 | holds | `[void]` is the pole and `([[A]] □)` sits inside an instance: ✠, strict; no unit step (receipt prover: ≡) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | EXACT | A^∅ is the one-point set |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
