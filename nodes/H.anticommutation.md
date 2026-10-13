---
id: H.anticommutation
title: Anticommutation (O9)
type: axiom
level: object
kind: law
rung: H
order: 1670
setting: JH
equality: "≐"
domain: complex
law: "([i ; j]) ≐ <([j ; i])>"
units: "ij = −ji: the one non-commutativity axiom, which One-J Rigidity says cannot be derived"
gloss_check: ""
holds:
  classical: fails
  J1: fails
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
known_since: "2026-08 (JH report, Layer 3: 'O9 (anticommutation): ([i ; j]) ≐ <([j ; i])> — the one non-commutativity axiom, necessarily posited'); Hamilton, Brougham Bridge, 1843"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [C.imaginary-unit, H.j, H.ordered-product, Z.angle]
see_also: [H.no-go, H.seed, H.j, H.k, H.ji, H.central-sign]
aliases: [O9, anticommutation, ij = −ji, the non-commutativity axiom]
concepts: [quaternion, ordered-product, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([i ; j]) ≐ <([j ; i])>` | i then j is the mirror of j then i | ij = −ji |

The one axiom of non-commutativity. Hamilton's i and j ([[C.imaginary-unit]], [[H.j]]) are two halves of two seeds; nothing about the seeds says how their halves multiply, and [[H.no-go]]'s corollary (One-J Rigidity, JH-2) says nothing in the calculus can derive it — so it is posited, as an equation between two ordered products ([[H.ordered-product]]) and a mirror ([[Z.angle]]). With it, every relation of Hamilton's table is a theorem ([[H.k]] names ij, [[H.ji]] reverses it, [[H.k-squared]] squares it).

## Plain

i times j is minus j times i. This is the fact Hamilton carved into the bridge; the chart cannot prove it from the seeds, so it is the rung's axiom.

## Derivation

none — adjoined: the law relating the two ordered products ([[H.ordered-product]]) of the units [[C.imaginary-unit]] and [[H.j]] through the mirror ([[Z.angle]]). Checked in ℍ: k against −(−k).

## Confirms

ij = −ji. It is **not** derivable from `i² = j² = −1`: a commutative algebra with two square roots of −1 (ℂ × ℂ, or ℂ with j = i) satisfies those and not this.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | fails | the forms `([i ; j])` and `([j ; i])` read as one product there (or have no value: `Jj` is not in ℂ); the law is the quaternions' |
| JH | holds | the axiom of the setting |
| JO | holds | the octonions anticommute too |
| JP | holds | at every place: k = −(−k) on the page |

| reading | cell | why |
|---|---|---|
| C | ABSENT | no j |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The classical cell is `fails` and not `replaced`: there is no classical law in its place; commutativity is the medium's, and this law contradicts it on these contents.
