---
id: alg.negative-exponent
title: A negative exponent is a reciprocal
type: theorem
level: object
kind: law
rung: alg
order: 747
setting: classical
equality: "≐"
domain: positive
law: "(([[A]] [<B>])) ≐ (<[(([[A]] [B]))]>)"
units: "a^{−b} = 1/aᵇ"
gloss_check: "A**(-B)"
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James); Chuquet 1484 for negative exponents, Wallis and Newton for the notation"
entered: 2026-10-03
guide: shape-led
band: "6–8"
uses: [mult.exponentiation, Q.reciprocal, mult.involution, mult.inverse-promotion]
see_also: [alg.product-of-powers, Q.reciprocal]
aliases: ["a^{-b} = 1/a^b", negative exponents]
concepts: [exponentiation, inverse, negation]
understood: "yes"
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[A]] [<B>])) ≐ (<[(([[A]] [B]))]>)` | — | a^{−b} = 1/aᵇ |

## Plain

A minus in the exponent flips the power upside down — the mirror on the exponent moves out through the inner circle and becomes the mirror of a reciprocal.

## Derivation

| form | rule | note |
|---|---|---|
| `(<[(([[A]] [B]))]>)` | given | the reciprocal ([[Q.reciprocal]]) of a^b ([[mult.exponentiation]]) |
| `(<([[A]] [B])>)` | [[mult.involution]] | the unit on the inner instance; content b · ln a, real |
| `(([[A]] [<B>]))` | [[mult.inverse-promotion]] | `<(X [Y])> ≐ (X [<Y>])` with X = `[[A]]`, Y = B |

## Confirms

a^{−b} = 1/aᵇ as inverse promotion one level up: the same law that moved a sign through a product ([[mult.inverse-promotion]]) moves it through an exponent. With [[alg.product-of-powers]] this gives aᵇ · a^{−b} = a⁰ = 1, closing the loop with [[alg.zeroth-power]].

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the unit step sits directly under the outer instance through an angle — absorbing (depth-1 criterion, [[mult.involution]] Notes) |
| JH, JO | replaced | ordered bases |
| JP | guarded | where the p-adic log converges |

| reading | cell | why |
|---|---|---|
| C | EXACT | exact on ℂ× once the power is defined by the form: the unit step is absorbing |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
