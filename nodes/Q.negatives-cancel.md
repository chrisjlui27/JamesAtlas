---
id: Q.negatives-cancel
title: Two signs on a fraction cancel
type: theorem
level: object
kind: law
rung: Q
order: 626
setting: classical
equality: ≐
domain: positive
law: "([<A>] <[<B>]>) ≐ ([A] <[B]>)"
units: (−a)/(−b) = a/b
gloss_check: A/B
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
status: NATIVE-BY-DECREE
verified: engine
known_since: 1993 (James); the sign rule is ancient
entered: 2026-10-03
guide: shape-led
band: 6–8
uses: [Q.division, Q.negative-fraction, Q.negative-denominator, Z.cancellation]
see_also: [mult.product-of-negatives]
aliases: [(−a)/(−b) = a/b]
concepts: [fraction, negation]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([<A>] <[<B>]>) ≐ ([A] <[B]>)` | — | (−a)/(−b) = a/b |

## Plain

A minus on top and a minus on the bottom cancel each other — each moves out front, and two minuses in front are none.

## Derivation

| form | rule | note |
|---|---|---|
| `([<A>] <[<B>]>)` | given | (−a) ÷ (−b), [[Q.division]] |
| `<([A] <[<B>]>)>` | [[Q.negative-fraction]] | the top sign moves out, with B := `<B>` |
| `<<([A] <[B]>)>>` | [[Q.negative-denominator]] | the bottom sign moves out |
| `([A] <[B]>)` | [[Z.cancellation]] | two mirrors cancel |

## Confirms

The quotient counterpart of [[mult.product-of-negatives]], and the end of the sign rules: with this, every signed fraction is a fraction or the mirror of one ([[Q.rational]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | under the seam decree, through [[Q.negative-denominator]] |
| J1 | holds | exact; no Λ-step of its own, inherits the receipts of [[Q.negative-denominator]] |
| JH, JO | holds | — |
| JP | guarded | for units |

| reading | cell | why |
|---|---|---|
| C | EXACT | exact on ℂ× |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
