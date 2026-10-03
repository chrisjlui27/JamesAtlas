---
id: mult.exponentiation
title: Powers are multiplication one level deeper
type: definition
level: object
kind: law
rung: mult
order: 370
setting: classical
equality: "≐"
domain: positive
law: "A ^ B := (([[A]] [B]))"
units: "a^b = e^{e^{ln ln a + ln b}}"
gloss_check: "A ** B"
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: holds
readings:
  C: EXACT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "1993 (James)"
entered: 2026-10-03
guide: shape-led
band: "6–8"
uses: [mult.multiplication, N.round, mult.square]
see_also: [mult.square-is-product, mult.cardinality]
aliases: [power, exponent, "a^b"]
concepts: [exponentiation]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[A]] [B]))` | — | a^b |

A power is a product of abstracts one level deeper: `a^b = e^{(ln a)·b}`, and `(ln a)·b` is the multiplication `([[A]][B])` of `[A]` by `B`.

## Plain

Raising to a power is multiplying, with the first number boxed one more time and the whole thing circled one more time.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[A]] [B]))` | [[N.round]] | the instance of a product, [[mult.multiplication]], whose first factor is the abstract `[A]`, [[mult.square]] |
| `A ^ B` | name | — |

## Confirms

a^b = exp(b · ln a), the definition analysis gives for real exponents — here the *only* definition, so there is nothing to extend when b stops being an integer. Each level of the tower + → × → ^ is the previous one wrapped once more. It is **not** yet shown that `A^2 ≐ A × A`; that is [[mult.square-is-product]].

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | — |
| JH, JO | replaced | with non-commuting bases, powers need the ordered bracket; the polar form `([r] ([J_u][t]))` is the quaternionic power |
| JP | holds | depth bookkeeping lives here: Hensel's lemma is written natively with depths 1, 2, 4, 8, 16, 32 (p-adic-wall) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | EXACT | a^b as the set of functions from a b-element set to an a-element set |
| logic | untested | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The convention `A ^ B` with `A` the base (double square) and `B` the exponent (single square) follows the JH Exposition Guide's dictionary.
