---
id: schema.cardinality
title: Cardinality for every n
type: schema
level: object
kind: law
rung: schema
order: 1100
setting: classical
equality: "≐"
domain: complex
law: "A^{n} ≐ ([A] [o^{n}])"
units: "a + … + a (n times) = n·a"
gloss_check: ""
schema_range: "n=1..12"
schema_draw: "n=3"
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE-BY-SCHEMA
verified: engine
known_since: "1993 (James, Ch. 4 §4.4, p. 27, Theorem 1 'Cardinality': base A = ([A]) = ([A][o]), then A…AA = ([A][o…o])([A][o]) = ([A][o…oo])"
entered: 2026-10-03
guide: need-led
band: "9–12"
uses: [void.space, N.induction, mult.unit-law, mult.distribution, N.numeral]
see_also: [mult.cardinality, N.induction, schema.power, schema.roots-of-unity]
aliases: [cardinality schema, n copies, "A…A = ([A][o…o])"]
concepts: [counting, multiplication, induction]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `A^{n} ≐ ([A] [o^{n}])` | n copies of A ≐ A with the count n | a + … + a = n a |

James's Theorem 1 in full: n copies of a form, standing together, are one copy with the count n — for *every* n. The chart's [[mult.cardinality]] is the case n = 2; this node is the schema, proved as James proves it — base n = 1, then one copy at a time — by an induction the calculus cannot take on its own. It is the first `schema` node, and the first law whose price shows the induction gap.

## Plain

One more copy raises the count by one, so n copies are one copy with the count n. The "and so on" is the step the page cannot write — the chart writes it once, here, and charges for it.

## Derivation

| form (n = 1) | rule | note |
|---|---|---|
| `A` | given | one copy — James's base (p. 27): "Everything has a count of one, shown directly by involution: A = ([A]) = ([A][o])" |
| `([A] [o])` | [[mult.unit-law]] | `([A] [o]) ≐ A`, right to left: the count 1 |

| form | rule | note |
|---|---|---|
| `A^{n}` | given | n copies of A |
| `A^{n-1} A` | medium | one copy set apart — the same multiset ([[void.space]]) |
| `([A] [o^{n-1}]) A` | hypothesis | the schema at n − 1: n − 1 copies are one copy with the count n − 1 ([[N.induction]] — the step the calculus cannot take by itself) |
| `([A] [o^{n-1}]) ([A] [o])` | [[mult.unit-law]] | the last copy gets the count 1, right to left |
| `([A] [o^{n-1} o])` | [[mult.distribution]] | collect the two counts over the shared `[A]`, right to left |
| `([A] [o^{n}])` | definition | the pile n is the pile n − 1 beside a unit ([[N.numeral]]) — the same form |

## Confirms

James's cardinality theorem (p. 27): "Multiple references in the same context may be reduced to a single reference with multiple units signifying its quantity, as A…A = ([A][o…o])" — his base `A = ([A]) = ([A][o])` is the base table (one row, since the chart's [[mult.unit-law]] is already `([A][o]) ≐ A`), and his step `A…AA = ([A][o…o])([A][o]) = ([A][o…oo])` is the step table. [[mult.cardinality]], the chart's n = 2, is the first derived instance. The engine checks the base at n = 1, the step at every n from 2 to 12, and that the hypothesis row is this law at n − 1; what it does **not** check is the passage to all n — that is [[N.induction]], cited in the hypothesis row, and the reason the status is NATIVE-BY-SCHEMA rather than NATIVE. Everything in rung `C` that was written out for n = 2 or 3 by hand ([[C.i-squared]], [[C.cube-root-of-unity]], [[C.de-moivre]]) is an instance of what this rung states once.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | each instance by the engine; all n by the induction |
| J1 | holds | survival ledger: cardinality unchanged, read as the graded exponential |
| JO | holds | per slice |
| JH | replaced | at n = 1 it is the unit law `([A] [o]) ≐ A`, whose receipt is the pinned period ([[H.slice-wall]]); for n ≥ 2 the count's log is real and the law is exact on every quaternion; the schema as a whole fails on generic quaternions (census/h-ledger.md) |
| JP | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | EXACT | n copies of a set is its product with an n-set, as for [[mult.cardinality]] |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The schema machinery (SPEC §2.7): `A^{n}` is n juxtaposed copies, `o^{n}` the pile n; the base table is the instance n = 1, the step table the instances n = 2 … 12 (so the hypothesis row always points at an instance already checked). The card draws the instance n = 3.
