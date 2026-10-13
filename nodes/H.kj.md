---
id: H.kj
title: k times j
type: theorem
level: object
kind: law
rung: H
order: 1710
setting: JH
equality: "≃"
domain: complex
law: "([k ; j]) ≃ <i>"
units: "kj = −i: (ij)j = i(jj) = −i"
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
uses: [H.central-sign, H.j-squared, H.k, H.splice, H.unit-entry, J1.counit]
see_also: [H.k, H.jk, H.ik, H.ji]
aliases: [kj = −i, "([k ; j]) = <i>"]
concepts: [quaternion, ordered-product, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([k ; j]) ≃ <i>` | k then j is minus i | kj = −i |

## Plain

k times j is minus i: against the cycle, a sign appears.

## Derivation

| form | rule | note |
|---|---|---|
| `([k ; j])` | given | k then j |
| `([([i ; j]) ; j])` | definition | k unfolded ([[H.k]]) |
| `([i ; j ; j])` | [[H.splice]] | spliced open |
| `([i ; ([j ; j])])` | [[H.splice]] | jj gathered, right to left |
| `([i ; <o>])` | [[H.j-squared]] | j² is minus one |
| `<([i ; o])>` | [[H.central-sign]] | the sign out |
| `<([i])>` | [[H.unit-entry]] | times one |
| `<i>` | [[J1.counit]] | —  |

## Confirms

kj = −i. **Not** an axiom.

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
