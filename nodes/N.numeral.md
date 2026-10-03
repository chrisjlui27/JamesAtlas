---
id: N.numeral
title: Numerals are piles
type: definition
level: object
kind: schema
rung: N
order: 120
setting: classical
equality: "≐"
domain: natural
law: "ooo := 3"
units: "n = o o … o (n copies)"
gloss_check: "3"
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
known_since: "1993 (James); tally marks are the oldest numerals"
entered: 2026-10-03
guide: shape-led
band: K
uses: [N.unit, void.space]
see_also: [N.freeness, mult.cardinality]
aliases: [number rewrite, pile, tally]
concepts: [counting, natural-number]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `o o o` | `ooo` | 3 |

A natural number is a pile of units. The *number rewrite* replaces the numeral `n` by `n` copies of `o` standing together.

## Plain

Three is three circles on the page. Counting is piling.

## Derivation

| form | rule | note |
|---|---|---|
| `o o o` | [[N.unit]] | three units in one space, [[void.space]] |
| `ooo` | name | the numeral 3 — the same multiset, written without spaces |

## Confirms

The natural numbers as *unary* numerals: every `n ≥ 1` is a pile, and `0` is the void ([[void.page]]). This is **not** positional notation — the calculus has no base — and it is **not** Laws of Form: there `o o ≐ o` (the law of Calling), so LoF has no natural numbers. James's refusal of Calling is where number begins.

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | n |
| finset | EXACT | an n-element set, up to isomorphism |
| logic | ABSENT | Calling collapses every pile to one mark |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The chart writes numerals as piles in canonical strings (`ooo`, never `3`) so that the engine never needs a base. Positional notation is a *gap* of a later rung (compression of piles), not of this one.
