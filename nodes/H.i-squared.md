---
id: H.i-squared
title: i squared, in order
type: theorem
level: object
kind: law
rung: H
order: 1680
setting: JH
equality: "≃"
domain: complex
law: "([i ; i]) ≃ <o>"
units: "i·i = −1 as an ordered product: the trunk's i² = −1 read through the collapse"
gloss_check: ""
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "1993 (James, i² = −1 in the complex calculus); this rung, 2026-10-07"
entered: 2026-10-07
guide: shape-led
band: "beyond"
uses: [C.i-squared, C.imaginary-unit, H.collapse]
see_also: [C.i-squared, H.j-squared, H.k-squared, H.collapse]
aliases: [i² = −1 (ordered), "([i ; i]) = <o>"]
concepts: [quaternion, ordered-product, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([i ; i]) ≃ <o>` | i times i, in order, is minus one | i² = −1 |

The trunk already has i² = −1 as a classical product ([[C.i-squared]]); an entry beside itself is co-sliced with itself, so the ordered square collapses to the classical one ([[H.collapse]]) and the trunk finishes. The collapse's receipt is paid by the instance: absorbed.

## Plain

i times i is minus one, in the ordered box too — i commutes with itself, so the old box can take over.

## Derivation

| form | rule | note |
|---|---|---|
| `([i ; i])` | given | i ([[C.imaginary-unit]]) beside itself, in order |
| `([i] [i])` | [[H.collapse]] | the two logs are one log: co-sliced; absorbed by the instance |
| `<o>` | [[C.i-squared]] | the trunk's i × i |

## Confirms

i² = −1. It is **not** new: the content is the trunk's, and the rung's only addition is that the ordered product agrees with the classical one on a single entry repeated.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | [[C.i-squared]] |
| JH | holds | absorbed |
| JO | holds | — |
| JP | holds | on the quaternion page at every place: i exists there as the Hurwitz unit, whatever p ([[H.split-place]]: not the central √−1 of [[place.selection]], which exists only at p ≡ 1 mod 4) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The trunk's [[C.i-squared]] is re-graded in ℍ before this node uses it (`tools/hledger.py`, `grade_cited_in_h`): its unit steps sit inside an instance whose content is in the slice of i, so they are absorbed there too.
