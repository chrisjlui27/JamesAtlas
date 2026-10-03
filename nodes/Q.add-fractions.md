---
id: Q.add-fractions
title: Adding fractions
type: theorem
level: object
kind: law
rung: Q
order: 590
setting: classical
equality: ≐
domain: positive
law: "([A] <[B]>) ([C] <[D]>) ≐ ([([A] [D]) ([C] [B])] <[B]> <[D]>)"
units: a/b + c/d = (ad + cb)/(bd)
gloss_check: A/B + C/D
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
known_since: 1993 (James); the rule is ancient
entered: 2026-10-03
guide: need-led
band: 3–5
uses: [Q.division, mult.multiplication, mult.distribution, mult.involution, Z.inversion, void.space]
see_also: [Q.multiply-fractions, Q.cancel-common-factor, Q.negative-fraction]
aliases: [common denominator, a/b + c/d]
concepts: [fraction, addition]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A] <[B]>) ([C] <[D]>) ≐ ([([A] [D]) ([C] [B])] <[B]> <[D]>)` | — | a/b + c/d = (ad + cb)/(bd) |

The denominator bd is written `<[B]> <[D]>`, which is `<[([B][D])]>` by Involution and collection (an equality of bare abstracts: exact classically, mod Λ in J1); the chart keeps the split form because that is the shape Distribution produces.

## Plain

To add two fractions you bring them to a common bottom — and on the page that is one use of Distribution, read backwards: two circles sharing the same mirrored boxes collect into one.

## Derivation

| form | rule | note |
|---|---|---|
| `([([A] [D]) ([C] [B])] <[B]> <[D]>)` | given | (ad + cb) ÷ (bd): [[Q.division]] with the products of [[mult.multiplication]] |
| `([([A] [D])] <[B]> <[D]>) ([([C] [B])] <[B]> <[D]>)` | [[mult.distribution]] | `(X [Y Z]) ≐ (X [Y]) (X [Z])` with X = `<[B]> <[D]>` |
| `([A] [D] <[B]> <[D]>) ([C] [B] <[B]> <[D]>)` | [[mult.involution]] | `[(Y)] ≐ Y`, in each factor |
| `([A] <[B]>) ([C] <[D]>)` | [[Z.inversion]] | `[D] <[D]>` cancels in the first, `[B] <[B]>` in the second; regroup by [[void.space]] |

## Confirms

The common-denominator rule, derived in the direction that explains it: start from the single fraction and *distribute*. The "cross-multiplication" the rule is usually taught as is the Involution rows. Tagged *need-led*: the forms do not ask for a common denominator; the wish to see a sum of fractions as one fraction does. Subtraction of fractions is this law with [[Q.negative-fraction]].

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the Involution-down steps sit at depth 1 under their instances (depth-1 criterion, [[mult.involution]] Notes) |
| JH, JO | replaced | Distribution is replaced by its two-sided list form; the sum of two quotients needs sides |
| JP | guarded | for unit denominators |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
