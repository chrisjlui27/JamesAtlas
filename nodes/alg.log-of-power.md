---
id: alg.log-of-power
title: The log of a power is the exponent times the log
type: theorem
level: object
kind: law
rung: alg
order: 745
setting: classical
equality: "≐"
domain: positive
law: "[(([[A]] [B]))] ≐ ([[A]] [B])"
units: "ln(aᵇ) = b · ln a"
gloss_check: "B*log(A)"
holds:
  classical: holds
  J1: holds-mod-Λ
  JH: replaced
  JO: replaced
  JP: guarded
readings:
  C: PARTIAL
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James); Napier 1614"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.exponentiation, mult.involution]
guarded_by: [mult.seam-decree]
see_also: [alg.log-law, alg.power-of-power]
aliases: ["ln a^b = b ln a", power rule for logs]
concepts: [logarithm, exponentiation]
understood: "yes"
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[(([[A]] [B]))] ≐ ([[A]] [B])` | — | ln(aᵇ) = b · ln a |

The right-hand side is the product `([[A]][B])` of ln a by b ([[mult.multiplication]] one level down).

## Plain

The log of a power is the exponent times the log — one box undoes the outer circle, and what is left is the exponent multiplying the log.

## Derivation

| form | rule | note |
|---|---|---|
| `[(([[A]] [B]))]` | given | ln(a^b), [[mult.exponentiation]] |
| `([[A]] [B])` | [[mult.involution]] | the unit `[(X)] ≐ X` with X = `([[A]] [B])`, whose value b · ln a is real for positive a and b |

## Confirms

Napier's power rule, as a single unit step at depth 0 — admitted by the seam decree on its *content* (real), not its position. For a < 1 the content is negative but still real: on the strip. It is **not** exact on ℂ×: for a negative base the content carries b·iπ, which leaves the strip for b > 1 or b ≤ −1 — hence `C: PARTIAL`; [[alg.power-of-power]], whose second row is this step under a square, inherits the same restriction to positive bases.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds-mod-Λ | a bare unit step; the receipt is not absorbed |
| JH, JO | replaced | powers with non-commuting bases live in the ordered bracket |
| JP | guarded | where the p-adic log converges |

| reading | cell | why |
|---|---|---|
| C | PARTIAL | exact for positive a and real b; for negative bases off the strip when b > 1 or b ≤ −1 |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
