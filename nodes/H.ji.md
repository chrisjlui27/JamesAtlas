---
id: H.ji
title: j times i
type: theorem
level: object
kind: law
rung: H
order: 1690
setting: JH
equality: "≡"
domain: complex
law: "([j ; i]) ≡ <k>"
units: "ji = −k: anticommutation read the other way"
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
uses: [H.anticommutation, H.k, Z.cancellation]
see_also: [H.anticommutation, H.k, H.k-squared, H.kj, H.ik]
aliases: [ji = −k, "([j ; i]) = <k>"]
concepts: [quaternion, ordered-product, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([j ; i]) ≡ <k>` | j then i is minus k | ji = −k |

O9 ([[H.anticommutation]]) says ij = −(ji); double the mirror ([[Z.cancellation]]) and read O9 right to left.

## Plain

Since ij = −ji and ij is k, ji is −k.

## Derivation

| form | rule | note |
|---|---|---|
| `([j ; i])` | given | j then i |
| `<<([j ; i])>>` | [[Z.cancellation]] | two mirrors, right to left |
| `<([i ; j])>` | [[H.anticommutation]] | O9 inside the mirror, right to left |
| `<k>` | definition | k is `([i ; j])` ([[H.k]]) |

## Confirms

ji = −k. It is **not** a second axiom: it is O9 and the double mirror.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | no j |
| JH | holds | strict |
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
