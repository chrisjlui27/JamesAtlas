---
id: alg.one-to-power
title: One to any power is one
type: theorem
level: object
kind: law
rung: alg
order: 744
setting: classical
equality: "≐"
domain: positive
law: "(([[o]] [B])) ≐ o"
units: "1ᵇ = 1"
gloss_check: "1"
holds:
  classical: holds
  J1: replaced
  JH: holds
  JO: holds
  JP: replaced
readings:
  C: EXACT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James); the fact is ancient"
entered: 2026-10-03
guide: shape-led
band: "6–8"
uses: [mult.exponentiation, mult.black-hole, mult.dominion, mult.hole-instance, N.unit, mult.log-of-one]
see_also: [alg.zeroth-power, alg.first-power]
aliases: ["1^b = 1"]
concepts: [exponentiation, one, zero]
understood: "yes"
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[o]] [B])) ≐ o` | — | 1ᵇ = 1 |

## Plain

One to any power is one: the log of one is nothing, the log of nothing is the pit, and the pit swallows the exponent.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[o]] [B]))` | given | 1^B, [[mult.exponentiation]] |
| `(([void] [B]))` | [[mult.log-of-one]] | `[o] ≐ void` |
| `((□ [B]))` | [[mult.black-hole]] | `[void]` is □ |
| `((□))` | [[mult.dominion]] | □ swallows `[B]` |
| `(void)` | [[mult.hole-instance]] | — |
| `o` | [[N.unit]] | — |

## Confirms

1ᵇ = 1 for every exponent, including fractional and negative ones — the same two black-hole laws as [[alg.zeroth-power]]. The base 1 is the only base whose powers the calculus cannot distinguish: every exponent falls into the hole.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, JH, JO | holds | — |
| JP | replaced | fails as derived at every place, as at 𝕁₁: `[o]` is ω_p under a square. The instances hold for a whole count B; for a fraction 1/n the receptacle takes over ([[J1.receptacle]]), with the place's selection rule — ω_p/n is a form only for n | p − 1 ([[place.selection]]) |
| J1 | replaced | **fails** as stated, and the prover says where: the log of one `[()] → void` is taken *under a square*, where ≃ does not pass, with receipt ω ≠ void. In 𝕁₁ `[[o]]` is `[ω]`, and `(([[o]] [B]))` is e^{Bω}: `o` when B is a count (the outer instance absorbs Bω), a root of unity when B is a fraction — 1^{1/3} is ω₃. The law is replaced by the receptacle (`J1.receptacle`): the value 1 has a lattice of logs, and the classical law was its shadow |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | EXACT | 1^B is the one-point set |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The J1 cell is worth a pause: in the enriched calculus `[o]` is the period ω rather than nothing, so `[[o]]` is `[ω]` — the log of the period — and 1ᵇ becomes `(([ω][B]))`, a form that depends on b. This is the roots-of-unity story seen from the base 1: `1^{1/n}` has n values. The classical black hole flattens exactly that.
