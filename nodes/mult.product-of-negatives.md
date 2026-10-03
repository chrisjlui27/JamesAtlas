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
domain: complex
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

The sign rule for integer multiplication, *derived*: the two mirrors are promoted to the outside and annihilate by [[Z.cancellation]]. This is the chart's first answer to a question the curriculum usually settles by fiat, and the completion of ℤ as a ring: with [[mult.product-of-numerals]] and [[mult.inverse-promotion]], products of integers are integers. In the ℂ reading the law is exact for every nonzero A, B — the engine checks it on complex content — because `([X][Y])` is the product of the *values* whatever branch each log takes; what the law does **not** say is anything about `[<A>]` on its own, which is where branch care begins ([[C.log-of-negative]]).

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

Domain `complex` (widened 2026-10-03, C referee pass): rung C instantiates this law at complex content, and under the chart's citation discipline ([[mult.consistency]], Confirms) a law may be cited only inside its declared domain; every row of its derivation is exact on ℂ×, as the engine confirms. The law's home band and reading are unchanged.

The pilot's object-level laws end here; two meta-level nodes follow ([[mult.c-reading]], [[mult.consistency]]). Next rung (`Q`): division as `(<[A]>)`, fractional cardinality, and the first appearance of `(<[oo]>)` = ½.
