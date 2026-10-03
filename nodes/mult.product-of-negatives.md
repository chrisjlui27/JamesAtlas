---
id: mult.product-of-negatives
title: A negative times a negative is positive
type: theorem
level: object
kind: law
rung: mult
order: 460
setting: classical
equality: "≐"
domain: positive
law: "([<A>] [<B>]) ≐ ([A] [B])"
units: "(−a)(−b) = ab"
gloss_check: "A*B"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "1993 (James, §3 worked example); Brahmagupta 628 for the fact"
entered: 2026-10-03
guide: shape-led
band: "6–8"
uses: [mult.multiplication, mult.inverse-promotion, Z.cancellation]
see_also: [Z.negative-numeral, mult.product-of-numerals, mult.consistency]
aliases: ["(−3)(−2) = 6", sign rule, negative times negative]
concepts: [negation, multiplication, integer]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([<A>] [<B>]) ≐ ([A] [B])` | — | (−a)(−b) = ab |
| `([<ooo>] [<oo>]) ≐ oooooo` | — | (−3)(−2) = 6 |

## Plain

Two minuses make a plus — not by rule, but because each mirror can be pushed out of the product and the two mirrors then cancel.

## Derivation

| form | rule | note |
|---|---|---|
| `([<A>] [<B>])` | [[mult.multiplication]] | (−a) × (−b) |
| `<([<A>] [B])>` | [[mult.inverse-promotion]] | promote the mirror on B outward — right to left, with the context `[<A>]` |
| `<<([A] [B])>>` | [[mult.inverse-promotion]] | promote the mirror on A outward |
| `([A] [B])` | [[Z.cancellation]] | two mirrors cancel |

## Confirms

The sign rule for integer multiplication, *derived*: the two mirrors are promoted to the outside and annihilate by [[Z.cancellation]]. This is the chart's first answer to a question the curriculum usually settles by fiat, and the completion of ℤ as a ring: with [[mult.product-of-numerals]] and [[mult.inverse-promotion]], products of integers are integers. It is **not** yet shown that `([<A>][<B>])` has the *value* ab for non-positive content in the ℂ reading without branch care — the engine checks it on positive A, B, where the mirrors are the only sign.

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | holds | Inversion cluster |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | untested | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The pilot's object-level laws end here; two meta-level nodes follow ([[mult.c-reading]], [[mult.consistency]]). Next rung (`Q`): division as `(<[A]>)`, fractional cardinality, and the first appearance of `(<[oo]>)` = ½.
