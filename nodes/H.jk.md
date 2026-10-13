---
id: H.jk
title: j times k
type: theorem
level: object
kind: law
rung: H
order: 1700
setting: JH
equality: "≃"
domain: complex
law: "([j ; k]) ≃ i"
units: "jk = i: j(ij) = (ji)j = −(k j)… the cyclic relation, from O9 and j² = −1"
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
uses: [H.central-sign, H.j-squared, H.ji, H.k, H.splice, H.unit-entry, J1.counit, Z.cancellation]
see_also: [H.k, H.ji, H.ki, H.kj, H.ik, H.k-squared]
aliases: [jk = i, "([j ; k]) = i", the cyclic relations]
concepts: [quaternion, ordered-product]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([j ; k]) ≃ i` | j then k is i | jk = i |

k is ij, so jk = j(ij); gather ji, which is −k = −(ij); the sign comes out; splice; j·j is −1, and the two signs cancel, leaving i.

## Plain

j times k is i: the units go round in a cycle, i → j → k → i, and the chart derives each step of the cycle from O9 and the squares.

## Derivation

| form | rule | note |
|---|---|---|
| `([j ; k])` | given | j then k |
| `([j ; ([i ; j])])` | definition | k unfolded ([[H.k]]) |
| `([j ; i ; j])` | [[H.splice]] | spliced open |
| `([([j ; i]) ; j])` | [[H.splice]] | ji gathered, right to left |
| `([<k> ; j])` | [[H.ji]] | ji is −k |
| `<([k ; j])>` | [[H.central-sign]] | the sign out |
| `<([([i ; j]) ; j])>` | definition | k unfolded ([[H.k]]) |
| `<([i ; j ; j])>` | [[H.splice]] | spliced open |
| `<([i ; ([j ; j])])>` | [[H.splice]] | jj gathered, right to left |
| `<([i ; <o>])>` | [[H.j-squared]] | j² is minus one |
| `<<([i ; o])>>` | [[H.central-sign]] | the sign out |
| `([i ; o])` | [[Z.cancellation]] | the two mirrors cancel |
| `([i])` | [[H.unit-entry]] | times one |
| `i` | [[J1.counit]] | —  |

## Confirms

jk = i. It is **not** a new axiom: the cycle is a theorem of O9 and the squares.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | no j, k |
| JH | holds | every step of its own strict; the square it cites ([[H.j-squared]]) is an absorbed theorem, and the node inherits that grade — absorbed, k = 0: the receipts were paid inside their own instances |
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
