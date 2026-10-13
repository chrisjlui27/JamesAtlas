---
id: H.ik
title: i times k
type: theorem
level: object
kind: law
rung: H
order: 1715
setting: JH
equality: "≃"
domain: complex
law: "([i ; k]) ≃ <j>"
units: "ik = −j: i(ij) = (ii)j = −j"
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
known_since: "Hamilton 1843; this rung, 2026-10-07"
entered: 2026-10-07
guide: shape-led
band: "beyond"
uses: [H.central-sign, H.i-squared, H.k, H.splice, H.unit-entry, J1.counit]
see_also: [H.k, H.ki, H.kj, H.ji]
aliases: [ik = −j, "([i ; k]) = <j>"]
concepts: [quaternion, ordered-product, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([i ; k]) ≃ <j>` | i then k is minus j | ik = −j |

## Plain

i times k is minus j.

## Derivation

| form | rule | note |
|---|---|---|
| `([i ; k])` | given | i then k |
| `([i ; ([i ; j])])` | definition | k unfolded ([[H.k]]) |
| `([i ; i ; j])` | [[H.splice]] | spliced open |
| `([([i ; i]) ; j])` | [[H.splice]] | ii gathered, right to left |
| `([<o> ; j])` | [[H.i-squared]] | i² is minus one |
| `<([o ; j])>` | [[H.central-sign]] | the sign out |
| `<([j])>` | [[H.unit-entry]] | one times j |
| `<j>` | [[J1.counit]] | —  |

## Confirms

ik = −j. With [[H.jk]], [[H.ki]], [[H.kj]], [[H.ji]] and the three squares, Hamilton's table is complete.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | no j, k |
| JH | holds | every step of its own strict; the square it cites ([[H.i-squared]]) is an absorbed theorem, and the node inherits that grade — absorbed, k = 0: the receipts were paid inside their own instances |
| JO | holds | — |
| JP | holds | at every place |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

none
