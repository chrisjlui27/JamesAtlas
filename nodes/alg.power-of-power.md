---
id: alg.power-of-power
title: A power of a power multiplies the exponents
type: theorem
level: object
kind: law
rung: alg
order: 750
setting: classical
equality: ≐
domain: positive
law: "(([[(([[A]] [B]))]] [C])) ≐ (([[A]] [([B] [C])]))"
units: "(a^b)^c = a^{bc}"
gloss_check: A**(B * C)
holds:
  classical: holds
  J1: holds-mod-Λ
  JH: replaced
  JO: replaced
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: 1993 (James); the rule is ancient
entered: 2026-10-03
guide: shape-led
band: 6–8
uses: [mult.exponentiation, mult.multiplication, mult.involution]
guarded_by: [mult.seam-decree]
see_also: [alg.product-of-powers, alg.rational-exponent]
aliases: [(a^b)^c = a^{bc}, power rule for exponents]
concepts: [exponentiation, multiplication]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[(([[A]] [B]))]] [C])) ≐ (([[A]] [([B] [C])]))` | — | (a^b)^c = a^{bc} |

## Plain

A power of a power multiplies the exponents: the inner power's double box unwraps twice, and what is left is the two exponents multiplied.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[(([[A]] [B]))]] [C]))` | given | (a^b)^c, [[mult.exponentiation]] |
| `(([([[A]] [B])] [C]))` | [[mult.involution]] | the unit on content `([[A]] [B])`, under a square — not absorbing, admitted because the content is real: (ln a)·b |
| `(([[A]] [B] [C]))` | [[mult.involution]] | the unit on content `[[A]] [B]`, directly under the inner instance |
| `(([[A]] [([B] [C])]))` | [[mult.involution]] | the unit right to left on `[B] [C]`: the exponent as the product b × c, [[mult.multiplication]] |

## Confirms

The power rule, as three unit steps; its second row is the law ln aᵇ = b ln a ([[alg.log-of-power]]). The content (ln a)·b is real whatever the sign of ln a, so the step is admitted on its content, not its position — which is why the engine checks it on both sides of a = 1.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds-mod-Λ | the second unit step sits under a square: its receipt is not absorbed by the inner instance — the first exponent law whose J1 cell is weaker than its classical one |
| JH, JO | replaced | within one slice |
| JP | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | exact for positive bases and all exponents; for other bases the power is defined by the form, `(([[A]][B]))` = e^{b·Ln a}, and (e^{2πi})^{½} ≠ e^{iπ} shows why the bases must be positive |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
