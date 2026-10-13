---
id: alg.power-of-base
title: The exponential is a power of the base
type: theorem
level: object
kind: law
rung: alg
order: 712
setting: classical
equality: "≐"
domain: positive
law: "(([[(o)]] [B])) ≐ (B)"
units: "e^b as the b-th power of e"
gloss_check: "exp(B)"
holds:
  classical: holds
  J1: guarded
  JH: guarded
  JO: holds
  JP: replaced
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James); Euler for the identification"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.exponentiation, alg.base, mult.involution, void.page, mult.log-of-one]
guarded_by: [mult.seam-decree]
see_also: [alg.log-of-base, alg.exp-law]
aliases: ["e^b", "exp as a power"]
concepts: [exponential, exponentiation]
understood: "yes"
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[(o)]] [B])) ≐ (B)` | — | e^b, as the power `(([[A]][B]))` with A = e, is the instance `(B)` |

The law that ties [[alg.base]] to [[mult.exponentiation]]: raising the base to a power is the round boundary itself.

## Plain

"e to the b" is just a circle around b — the base is the number whose powers are the circles.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[(o)]] [B]))` | given | e^B by [[mult.exponentiation]], with the base [[alg.base]] |
| `(([o] [B]))` | [[mult.involution]] | the unit on `(o)`: content 1, on the strip |
| `((void [B]))` | [[mult.log-of-one]] | `[o] ≐ void` |
| `(([B]))` | [[void.page]] | — |
| `(B)` | [[mult.involution]] | the counit |

## Confirms

exp(b) = e^b — in analysis a theorem that takes some work (the series and the power agree); here two Involutions and the unit law. It is **not** base-independent: in a base-b reading the same form is b^B, and `(B)` still means b^B.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | guarded | the unit on `(o)` sits under a square inside the inner instance. ≃ does not pass through `[ ]` (a lattice offset inside a log is not a lattice offset of the log), so the step is sound only because its receipt is void — k = 0, the content `o` on the strip — which 𝕁₁ cannot see and the reading can: the classical by-content guard survives as an import (receipt prover, `census/j1-ledger.md`) |
| JO | holds | — |
| JH | guarded | as in 𝕁₁: the unit step under the square imports; the receipt is void on the domain (census/h-ledger.md) |
| JP | replaced | `(o)` is not a form at a finite place ([[place.radius]]) |

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
