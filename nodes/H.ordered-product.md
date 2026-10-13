---
id: H.ordered-product
title: The ordered product
type: definition
level: object
kind: law
rung: H
order: 1610
setting: JH
equality: "≐"
domain: complex
law: "A · B := ([A ; B])"
units: "A·B, the Hamilton product: the instance of the log of the ordered product"
gloss_check: ""
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: holds
  JP: guarded
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "2026-08 (JH report, Layer 3: 'ordered multiplication x·y := ([x ; y])'); Hamilton 1843"
entered: 2026-10-07
guide: shape-led
band: "beyond"
uses: [H.ordered-bracket, N.round]
see_also: [mult.multiplication, H.ordered-bracket, H.collapse, H.anticommutation]
aliases: [ordered multiplication, x·y, the Hamilton product as a form, ordered instance]
concepts: [quaternion, ordered-product, multiplication]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `A · B := ([A ; B])` | the instance of the ordered square: A times B, in that order | the Hamilton product AB |

The classical product `([A][B])` ([[mult.multiplication]]) is the instance of two logs beside each other; the ordered product is the instance of the ordered square ([[H.ordered-bracket]], [[N.round]]). The two agree when the logs commute ([[H.collapse]]) and differ otherwise: `([i ; j])` is k and `([i][j])` is not ([[H.anticommutation]], [[H.no-go]]).

## Plain

To multiply two quaternions in order, put them in the ordered box and take the instance. The old recipe — log each, add, exponentiate — only works when they commute.

## Derivation

| form | rule | note |
|---|---|---|
| `([A ; B])` | given | the instance ([[N.round]]) of the ordered square ([[H.ordered-bracket]]) |
| `A · B` | name | — |

## Confirms

The Hamilton product. It is **not** a second operation on the chart beside `×`: on commuting contents the two coincide, and the chart writes the classical product where the contents commute and the ordered one where they do not.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | `([A][B])` is the product there |
| JH | holds | the definition |
| JO | holds | the octonions multiply in order too; what they lose is splice |
| JP | guarded | the product on the quaternion page at every place — exact wherever the ordered square has a value, formless where the page's log is owed ([[H.ordered-bracket]]; census/h-place-ledger.md) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The sugar `i`, `j`, `k` of canonical strings: `i` = `(([J] <[oo]>))` ([[C.imaginary-unit]]), `j` = `(([Jj] <[oo]>))` ([[H.j]]), `k` = `([i ; j])` ([[H.k]]).
