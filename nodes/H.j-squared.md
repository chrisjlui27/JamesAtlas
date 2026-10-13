---
id: H.j-squared
title: j squared
type: theorem
level: object
kind: law
rung: H
order: 1685
setting: JH
equality: "≃"
domain: complex
law: "([j ; j]) ≃ <o>"
units: "j·j = −1: half the second seed, twice, is the second seed, whose instance is minus one"
gloss_check: ""
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: holds
  JP: holds
readings:
  C: ABSENT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "2026-08 (JH report: Hamilton's relations are theorems of Layer 3); Hamilton 1843"
entered: 2026-10-07
guide: shape-led
band: "beyond"
uses: [H.collapse, H.j, H.seed, J1.unit, Q.fractional-cardinality]
see_also: [C.i-squared, H.i-squared, H.k-squared, H.seed, H.j]
aliases: [j² = −1, "([j ; j]) = <o>"]
concepts: [quaternion, ordered-product, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([j ; j]) ≃ <o>` | j times j is minus one | j² = −1 |

The derivation of [[C.i-squared]] with the second seed in place of the first: the ordered square collapses (j is co-sliced with itself), the two unit steps open the halves inside the instance, half of J_j and half of J_j make J_j ([[Q.fractional-cardinality]]), and the seed's instance is minus one ([[H.seed]]). Every step is paid by the outer instance: absorbed. One of them is a *seam* payment — `[j ; j]` is the log of −1, pinned to πi, while `[j][j]` is πj; the contents differ by no period, and the instance pays the difference because e^{πi} = e^{πj}: recorded on the tape as `absorbed [seam]` (SPEC §6.4).

## Plain

Half of the second log of minus one, taken twice, is the whole of it; its instance is minus one. So j squared is minus one, for the same reason i squared is.

## Derivation

| form | rule | note |
|---|---|---|
| `([j ; j])` | given | j ([[H.j]]) beside itself |
| `([j] [j])` | [[H.collapse]] | co-sliced: the ordered square collapses — a seam displacement, paid by the instance |
| `(([Jj] <[oo]>) ([Jj] <[oo]>))` | [[J1.unit]] | the unit twice, directly inside the instance: absorbed |
| `(Jj)` | [[Q.fractional-cardinality]] | two halves of J_j make J_j |
| `<o>` | [[H.seed]] | the seed's instance is minus one |

## Confirms

j² = −1. It is **not** a consequence of i² = −1: it needs the second seed's declaration.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | no j |
| JH | holds | absorbed, with one seam payment |
| JO | holds | — |
| JP | holds | at every place: the Hurwitz unit j squares to −1 on the page |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The seam payment is the first on the chart: in ℍ an instance can pay a difference that is no lattice element, because −1 has many logs. LEGISLATION 32(c) admits it exactly where the instance's values agree, and the tape says so.
