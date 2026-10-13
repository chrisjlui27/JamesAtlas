---
id: Q.negative-fraction
title: A sign on top is a sign in front
type: theorem
level: object
kind: law
rung: Q
order: 620
setting: classical
equality: ≐
domain: complex
law: "([<A>] <[B]>) ≐ <([A] <[B]>)>"
units: (−a)/b = −(a/b)
gloss_check: -A/B
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: holds
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: 1993 (James); the sign rule is ancient
entered: 2026-10-03
guide: shape-led
band: 6–8
uses: [Q.division, mult.inverse-promotion]
see_also: [Q.negative-denominator, Q.reciprocal-of-negative, mult.product-of-negatives, Q.rational]
aliases: [(−a)/b = −(a/b), sign of a fraction]
concepts: [fraction, negation]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([<A>] <[B]>) ≐ <([A] <[B]>)>` | — | (−a)/b = −(a/b) |

The sign on the *bottom*, a/(−b) = −(a/b), is **not** the same promotion: it needs the reciprocal of a negative, which costs a trip through the seam ([[Q.reciprocal-of-negative]], [[Q.negative-denominator]]).

## Plain

A minus on the top of a fraction is the same as a minus in front of it.

## Derivation

| form | rule | note |
|---|---|---|
| `([<A>] <[B]>)` | given | (−a) ÷ b, [[Q.division]] |
| `<([A] <[B]>)>` | [[mult.inverse-promotion]] | `<(X [Y])> ≐ (X [<Y>])` with X = `<[B]>` and Y = A, used right to left |

## Confirms

The sign rule for fractions as one instance of inverse promotion — no unit step at all, so it is exact on all of ℂ× even though `[<A>]` is `ln a + iπ`; the engine samples positive a and b, where the mirror is the only sign.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, JO | holds | the Inversion cluster |
| JH | replaced | as [[mult.product-of-negatives]]: the sign of a quotient passes a pinned half-turn, which fails on generic quaternions (census/h-ledger.md); [[H.central-sign]] in the ordered square |
| J1 | holds | per the survival ledger (promotion unchanged); the chart's own derivation of [[mult.inverse-promotion]] routes through zero-annihilates, whose J1 cell is untested |
| JP | guarded | the denominator must be a unit at p |

| reading | cell | why |
|---|---|---|
| C | EXACT | exact on all of ℂ×, not only on the sampled positive domain |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

- ~~a/(−b) = −(a/b) follows "by the same promotion with the roles exchanged"~~ — the first draft (2026-10-03) claimed this in prose; the referee pass the same day showed no instantiation of inverse promotion matches `([A] <[<B>]>)`. The bottom-sign law is [[Q.negative-denominator]] and needs [[Q.reciprocal-of-negative]].

## Notes

Domain `complex` (widened 2026-10-03, C referee pass): [[Q.negatives-cancel]] instantiates this law at B := `<B>`, and a law may be cited only inside its declared domain ([[mult.consistency]], Confirms); every row of its derivation is exact on ℂ×, as the engine confirms. The home band and reading are unchanged.
