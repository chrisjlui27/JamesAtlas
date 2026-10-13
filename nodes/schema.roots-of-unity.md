---
id: schema.roots-of-unity
title: The n-th roots of unity, for every n
type: schema
level: object
kind: law
rung: schema
order: 1130
setting: classical
equality: "≐"
domain: positive
law: "([(([J] [o^{2k}] <[o^{n}]>))]^{n}) ≐ o"
units: "(e^{2πik/n})ⁿ = 1"
gloss_check: ""
schema_range: "n=1..6; k=1..n"
schema_draw: "n=3; k=1"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE-BY-SCHEMA
verified: engine
known_since: "1993 (James, Ch. 6 §6.2.3 p. 46: 'other cardinalities of J can be taken to produce other periodicities, forming the roots of unity' — stated, not derived); the roots of unity as e^{2πik/n}: De Moivre 1707–22, Euler 1748"
entered: 2026-10-03
guide: need-led
band: "9–12"
uses: [mult.multiplication, C.phase, mult.involution, schema.cardinality, Z.inversion, schema.period-multiple]
guarded_by: [mult.seam-decree]
see_also: [C.cube-root-of-unity, schema.cardinality, schema.period-multiple, schema.roots-sum, N.order]
aliases: [roots of unity, ζ_n, "ωⁿ = 1"]
concepts: [root, phase, one, induction]
owed: ["2026-10-04: the multiplication of the n-th roots of unity as a schema in two parameters, and that they are all the roots (needs N.order, or a reading)"]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([ω]^{n}) ≐ o`, ω = `(([J] [o^{2k}] <[o^{n}]>))` | the n-th power of J with the count 2k/n, instanced, is one | (e^{2πik/n})ⁿ = 1 |

The roots of unity are the fractional counts of J with an even numerator, instanced — J with the count 2k/n — and this schema says each one, raised to the n, is one. [[C.cube-root-of-unity]] is the case n = 3, k = 1; here every n and every k from 1 to n.

## Plain

Cut a whole turn into n equal parts and take k of them; do that n times over and you have gone round k whole turns, which the circle forgets.

## Derivation

| form | rule | note |
|---|---|---|
| `([(([J] [o^{2k}] <[o^{n}]>))]^{n})` | given | the n-th power of ω^k = `(([J] [2k] <[n]>))`, a fractional count of J ([[mult.multiplication]], [[C.phase]]) — n copies of its abstract under one instance |
| `(([J] [o^{2k}] <[o^{n}]>)^{n})` | [[mult.involution]] | the unit on each abstract, directly inside the instance — absorbing (content 2kπi/n, off the strip for 2k > n: a seam step) |
| `(([([J] [o^{2k}] <[o^{n}]>)] [o^{n}]))` | [[schema.cardinality]] | n copies are one copy with the count n |
| `(([J] [o^{2k}] <[o^{n}]> [o^{n}]))` | [[mult.involution]] | the unit, directly inside the inner instance — absorbing |
| `(([J] [o^{2k}]))` | [[Z.inversion]] | the count n and its mirror cancel: n copies of 2k/n of J are 2k of J |
| `(J^{2k})` | [[schema.cardinality]] | right to left, with A = J: J with the count 2k is 2k copies of J |
| `o` | [[schema.period-multiple]] | k whole turns inside an empty instance: `(J^{2k}) ≐ ()`, which is `o` |

## Confirms

The n-th roots of unity as James gestured at them (p. 46) and as the chart can now state them: `(([J] [2k] <[n]>))` for k = 1, …, n, each satisfying ωⁿ = 1. Their multiplication is the addition of counts, and [[schema.period-multiple]] reduces the count modulo 2 — so they form the cyclic group ℤ/n, with k = n the identity `o`. What this schema is **not**: a proof that these are *all* the n-th roots of unity, or that they are distinct — the first needs that a polynomial of degree n has at most n roots, which is a statement about the reading, and the second needs an order or a count of forms up to ≐, which the chart does not have ([[N.order]]). It also is **not** yet the cyclotomic relation that they sum to nothing; that is [[schema.roots-sum]].

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step directly under an instance; the final period step is A5′ |
| JH, JO | holds | per slice: the n-th roots of unity in the slice of u |
| JP | guarded | ω/n is a form at p iff n divides p − 1 (and n divides 2 at p = 2): the place's selection rule for fractions of ω (JP, 'Forms at Every Place') |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Guarded by position (Amendment A2): the units on the abstracts have content 2kπi/n, off the strip when 2k > n; they sit directly inside the instance. Checked for n = 1…6 and k = 1…n (21 instances); the card draws n = 3, k = 1.
