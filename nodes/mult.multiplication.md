---
id: mult.multiplication
title: Multiplication is the instance of collected abstracts
type: definition
level: object
kind: law
rung: mult
order: 330
setting: classical
equality: "≐"
domain: complex
law: "A × B := ([A] [B])"
units: "a·b = e^{ln a + ln b}"
gloss_check: "A * B"
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: holds
readings:
  C: EXACT
  finset: PARTIAL
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "1993 (James)"
entered: 2026-10-03
guide: shape-led
band: "3–5"
uses: [N.round, mult.square, void.space]
see_also: [mult.product-of-numerals, mult.cardinality, mult.exponentiation]
aliases: [product, times, "([A][B])"]
concepts: [multiplication]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A] [B])` | — | a · b |

To multiply, abstract both factors, put the abstracts together, and take the instance. Multiplication is not a primitive: it is addition one level deeper.

## Plain

Times is plus, done inside a box-and-circle: box each pile, put the boxes together, circle the result.

## Derivation

| form | rule | note |
|---|---|---|
| `([A] [B])` | [[N.round]] | the instance of the juxtaposition ([[void.space]]) of the two abstracts, [[mult.square]] |
| `A × B` | name | — |

## Confirms

ab = e^{ln a + ln b}: the slide-rule identity made structural. Lui's slogan — juxtaposition is addition and *becomes* multiplication on instance wrapping; the round boundary is the conversion between the layers. It is **not** yet shown that this agrees with repeated addition on numerals — that is the theorem [[mult.product-of-numerals]] — and it is **not** non-commutative: `([A][B])` and `([B][A])` are the same form, which is exactly why ℍ needs an ordered bracket (JH-1, the No-Go theorem).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the multiplicative layer `([A][B])`; A5′ keeps `1·A = A` exact |
| JH, JO | replaced | the ordered product `([x ; y])`; the commuting case restricts back (the Collapse rule) |
| JP | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | PARTIAL | the product of finite sets is exact; the exp–log *route* to it is the reading still to be written |
| logic | untested | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Domain `complex` (widened 2026-10-03, C referee pass): rung C instantiates this law at complex content, and under the chart's citation discipline ([[mult.consistency]], Confirms) a law may be cited only inside its declared domain; every row of its derivation is exact on ℂ×, as the engine confirms. The law's home band and reading are unchanged.
