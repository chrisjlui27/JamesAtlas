---
id: N.addition
title: Addition is juxtaposition
type: definition
level: object
kind: law
rung: N
order: 130
setting: classical
equality: "≐"
domain: natural
law: "A + B := A B"
units: "a + b"
gloss_check: "A + B"
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
known_since: "1993 (James)"
entered: 2026-10-03
guide: shape-led
band: K
uses: [void.space, N.numeral]
see_also: [N.add-comm, mult.multiplication]
aliases: [sum, plus]
concepts: [addition]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `A B` | — | a + b |
| `oo ooo` | `ooooo` | 2 + 3 = 5 |

To add two forms, write them in the same space. There is no symbol for +.

## Plain

Put two piles together and you have the sum; nothing has to be done.

## Derivation

| form | rule | note |
|---|---|---|
| `oo ooo` | [[N.numeral]] | the piles 2 and 3 in one space, [[void.space]] |
| `ooooo` | definition | which is the pile 5 — the same multiset |

## Confirms

Addition of natural numbers as *concatenation of tallies*; the Peano recursion `m + S(n) = S(m + n)` is here a non-event. It is **not** a rewrite — nothing happens — which is why the chart records it as a definition and not a theorem.

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | + |
| finset | EXACT | disjoint union |
| logic | ABSENT | with Calling, juxtaposition is OR, not + |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Lui's working phrase: juxtaposition is addition, and it *becomes* multiplication on instance wrapping — the round boundary is the conversion between the additive and multiplicative layers (the law of exponents). That is the theorem [[mult.product-of-numerals]], not this definition.
