---
id: Q.negative-denominator
title: A sign on the bottom is a sign in front
type: theorem
level: object
kind: law
rung: Q
order: 624
setting: classical
equality: ≐
domain: positive
law: "([A] <[<B>]>) ≐ <([A] <[B]>)>"
units: a/(−b) = −(a/b)
gloss_check: -A/B
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
status: NATIVE
verified: engine
known_since: 1993 (James); the sign rule is ancient
entered: 2026-10-03
guide: shape-led
band: 6–8
uses: [Q.division, mult.involution, Q.reciprocal-of-negative, mult.inverse-promotion, mult.seam-decree]
guarded_by: [mult.seam-decree]
see_also: [Q.negative-fraction, Q.negatives-cancel]
aliases: [a/(−b) = −(a/b)]
concepts: [fraction, negation]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A] <[<B>]>) ≐ <([A] <[B]>)>` | — | a/(−b) = −(a/b) |

## Plain

A minus on the bottom of a fraction is the same as a minus in front — but, unlike the minus on top, the page needs the reciprocal of a negative to show it.

## Derivation

| form | rule | note |
|---|---|---|
| `([A] <[<B>]>)` | given | a ÷ (−b), [[Q.division]] |
| `([A] [(<[<B>]>)])` | [[mult.involution]] | `X ≐ [(X)]` with X = `<[<B>]>`, right to left — a seam step in an absorbing position, admitted by [[mult.seam-decree]] |
| `([A] [<(<[B]>)>])` | [[Q.reciprocal-of-negative]] | 1/(−b) = −(1/b) |
| `<([A] [(<[B]>)])>` | [[mult.inverse-promotion]] | `(X [<Y>]) ≐ <(X [Y])>` with X = `[A]`, Y = `(<[B]>)`, used right to left |
| `<([A] <[B]>)>` | [[mult.involution]] | `[(Y)] ≐ Y` with Y = `<[B]>`, on the strip |

## Confirms

The second sign rule for fractions. Its asymmetry with [[Q.negative-fraction]] is real: a sign on top moves out by inverse promotion alone (no guard); a sign on the bottom must first be turned into a sign on a reciprocal, and that crosses the seam (`guarded_by` the decree, by position). With both, [[Q.negatives-cancel]] follows.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | under the seam decree |
| J1 | holds | exact by the depth-1 criterion; inherits the receipts of [[Q.reciprocal-of-negative]] and posts one more at its own seam step |
| JH, JO | holds | guarded Involution; the route is through the left-inverse theorem |
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
