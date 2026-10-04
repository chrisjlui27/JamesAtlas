---
id: schema.power
title: A power is an n-fold product, for every n
type: schema
level: object
kind: law
rung: schema
order: 1110
setting: classical
equality: "≐"
domain: complex
law: "(([[A]] [o^{n}])) ≐ ([A]^{n})"
units: "aⁿ = a · … · a (n factors)"
gloss_check: ""
schema_range: "n=1..7"
schema_draw: "n=3"
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
status: NATIVE-BY-SCHEMA
verified: engine
known_since: "1993 (James, Ch. 4 §4.4.2, p. 28: 'cardinality of multiplication translates to exponentiation')"
entered: 2026-10-03
guide: need-led
band: "9–12"
uses: [mult.exponentiation, mult.involution, mult.distribution, N.induction, N.numeral, mult.log-of-one]
guarded_by: [mult.seam-decree]
see_also: [mult.exponentiation, mult.square-is-product, schema.cardinality, schema.de-moivre]
aliases: [power schema, "xⁿ = x ⋯ x"]
concepts: [exponentiation, multiplication, induction]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[A]] [o^{n}])) ≐ ([A]^{n})` | a^n ≐ the product of n copies of `[A]` | aⁿ = a × … × a |

Cardinality one level down: the n-th power, defined as the exponential `(([[A]] [n]))` ([[mult.exponentiation]]), is the product of n factors. [[mult.square-is-product]] is the case n = 2.

## Plain

A to the n is a times a, n times over. The page proves it by peeling one factor off the count at a time.

## Derivation

| form (n = 1) | rule | note |
|---|---|---|
| `(([[A]] [o]))` | given | a to the first, [[mult.exponentiation]] |
| `(([[A]]))` | [[mult.log-of-one]] | `[o] ≐ void` |
| `([A])` | [[mult.involution]] | the counit on `([[A]])`: one factor |

| form | rule | note |
|---|---|---|
| `(([[A]] [o^{n}]))` | given | a to the n, [[mult.exponentiation]] |
| `(([[A]] [o^{n-1} o]))` | definition | the pile n is the pile n − 1 beside a unit ([[N.numeral]]) — the same multiset |
| `(([[A]] [o^{n-1}]) ([[A]] [o]))` | [[mult.distribution]] | distribute over the two counts |
| `(([[A]] [o^{n-1}]) ([[A]]))` | [[mult.log-of-one]] | `[o] ≐ void` |
| `(([[A]] [o^{n-1}]) [A])` | [[mult.involution]] | the counit `([[A]]) ≐ [A]` |
| `([(([[A]] [o^{n-1}]))] [A])` | [[mult.involution]] | the unit right to left on the first factor, directly inside the instance — absorbing (content (n − 1) ln a: on the strip at n = 2, off it for n ≥ 3 when |arg a| > π/(n − 1) — a seam step) |
| `([([A]^{n-1})] [A])` | hypothesis | the schema at n − 1: a^{n−1} is the product of n − 1 copies of `[A]` ([[N.induction]]) |
| `([A]^{n-1} [A])` | [[mult.involution]] | the unit on `[([A]^{n−1})]`, directly inside the instance — absorbing, with the same content (n − 1) ln a as row 6: the second seam step; n factors |

## Confirms

x ⋯ x = xⁿ as James states it (p. 28: `([x]…[x]) = (([[x]][o…o]))`), proved by induction on n: the count n is the count n − 1 beside a unit, Distribution splits the two, the hypothesis handles the n − 1, and one absorbing unit step puts the last factor in. It is **not** valid for a non-numeral exponent — `(([[A]] [B]))` with B a general form is the exponential, and "B factors" means nothing — and it is **not** restricted to positive a: every unit step sits inside an instance, so the schema is exact on ℂ× (guarded by position for complex a, where (n − 1) ln a leaves the strip).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step directly under an instance |
| JH, JO | replaced | powers of non-commuting factors keep their order; the n-fold product is `[x ; … ; x]` in the ordered bracket |
| JP | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | EXACT | aⁿ = a × … × a, the n-fold product of sets, as for [[mult.square-is-product]] |
| logic | untested | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Guarded by position (Amendment A2): rows 6 and 8 are unit steps on the content (n − 1) ln a — the unit right to left on `([[A]] [o^{n−1}])` and then the unit on `[([A]^{n−1})]` — off the strip for complex a with |arg a| > π/(n − 1) once n ≥ 3 (at n = 2 the content is ln a itself, on the strip, so the instance n = 2 is free of the decree); both sit directly inside the instance. Checked for n = 1 … 7; the card draws n = 3.
