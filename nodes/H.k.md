---
id: H.k
title: The third unit
type: definition
level: object
kind: law
rung: H
order: 1675
setting: JH
equality: "≐"
domain: complex
law: "k := ([i ; j])"
units: "k = ij: the ordered product of the first two units"
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
known_since: "2026-08 (JH report, Layer 3: 'k := ([i ; j])'); Hamilton 1843"
entered: 2026-10-07
guide: shape-led
band: "beyond"
uses: [C.imaginary-unit, H.j, H.ordered-product]
see_also: [H.anticommutation, H.ji, H.k-squared, H.jk, H.ki]
aliases: [k, the unit k, ij, k = ij]
concepts: [quaternion, ordered-product]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `k := ([i ; j])` | the product of i and j in that order | k = ij |

The third unit is not a third seed: it is the product of the first two ([[H.ordered-product]], [[C.imaginary-unit]], [[H.j]]). In ℍ: e^{(π/2)i} e^{(π/2)j} = k, the cross product of orthogonal half-phases ([[H.phase-sphere]]). Its log is (π/2)k, so k is also e^{J_k/2} for J_k = 2[k] — a third log of −1, derived rather than adjoined.

## Plain

k is i times j. Nothing new has to be assumed for it; it falls out of the other two.

## Derivation

| form | rule | note |
|---|---|---|
| `([i ; j])` | given | the ordered product ([[H.ordered-product]]) of [[C.imaginary-unit]] and [[H.j]] |
| `k` | name | — |

## Confirms

k = ij; and k² = −1, jk = i, ki = j are theorems ([[H.k-squared]], [[H.jk]], [[H.ki]]). It is **not** a seed: `(([Jk] <[oo]>))` would be the same unit, and the chart does not adjoin a constant it can derive.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | no j to multiply |
| JH, JO | holds | the definition |
| JP | holds | at every place: the Hurwitz unit k |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

Canonical strings accept the sugar `k`.
