---
id: alg.log-of-base
title: The log of the base is one
type: theorem
level: object
kind: law
rung: alg
order: 705
setting: classical
equality: "≐"
domain: natural
law: "[(o)] ≐ o"
units: "ln e = 1"
gloss_check: "1"
holds:
  classical: holds
  J1: holds-mod-Λ
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
known_since: "1993 (James); Mercator 1668 for the natural logarithm, Euler 1748 for e as the base with ln e = 1"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [alg.base, mult.involution]
guarded_by: [mult.seam-decree]
see_also: [alg.power-of-base, mult.unit-law]
aliases: ["ln e = 1"]
concepts: [logarithm, exponential]
understood: "yes"
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[(o)] ≐ o` | — | ln e = 1 |

## Plain

Box the base and you get one back — the base is the thing whose log is one.

## Derivation

| form | rule | note |
|---|---|---|
| `[(o)]` | given | the abstract of the base, [[alg.base]] |
| `o` | [[mult.involution]] | the unit `[(X)] ≐ X` with X = `o`; content 1, on the strip |

## Confirms

ln e = 1, the companion of [[mult.unit-law]]'s ln 1 = 0: the two facts that pin the logarithm's scale, both one Involution. Note that nothing here says *which* number e is ([[alg.base]]): in any base b the same law reads log_b b = 1.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds-mod-Λ | a bare unit step: the law's sides are not under an instance, so the receipt is not absorbed — `[(o)] ≃ o` with receipt |
| JH, JO, JP | holds | — |

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
