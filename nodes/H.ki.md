---
id: H.ki
title: k times i
type: theorem
level: object
kind: law
rung: H
order: 1705
setting: JH
equality: "≃"
domain: complex
law: "([k ; i]) ≃ j"
units: "ki = j: (ij)i = i(ji) = −i(ij) = −(ii)j = j"
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
uses: [H.central-sign, H.i-squared, H.ji, H.k, H.splice, H.unit-entry, J1.counit, Z.cancellation]
see_also: [H.k, H.ji, H.jk, H.kj, H.ik]
aliases: [ki = j, "([k ; i]) = j"]
concepts: [quaternion, ordered-product]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([k ; i]) ≃ j` | k then i is j | ki = j |

## Plain

k times i is j — the third step of the cycle.

## Derivation

| form | rule | note |
|---|---|---|
| `([k ; i])` | given | k then i |
| `([([i ; j]) ; i])` | definition | k unfolded ([[H.k]]) |
| `([i ; j ; i])` | [[H.splice]] | spliced open |
| `([i ; ([j ; i])])` | [[H.splice]] | ji gathered, right to left |
| `([i ; <k>])` | [[H.ji]] | ji is −k |
| `<([i ; k])>` | [[H.central-sign]] | the sign out |
| `<([i ; ([i ; j])])>` | definition | k unfolded ([[H.k]]) |
| `<([i ; i ; j])>` | [[H.splice]] | spliced open |
| `<([([i ; i]) ; j])>` | [[H.splice]] | ii gathered, right to left |
| `<([<o> ; j])>` | [[H.i-squared]] | i² is minus one |
| `<<([o ; j])>>` | [[H.central-sign]] | the sign out |
| `([o ; j])` | [[Z.cancellation]] | the mirrors cancel |
| `([j])` | [[H.unit-entry]] | one times j |
| `j` | [[J1.counit]] | —  |

## Confirms

ki = j. **Not** an axiom.

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
