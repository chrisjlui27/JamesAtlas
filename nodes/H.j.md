---
id: H.j
title: The second imaginary unit
type: definition
level: object
kind: law
rung: H
order: 1665
setting: JH
equality: "≐"
domain: complex
law: "j := (([Jj] <[oo]>))"
units: "j = e^{J_j/2} = e^{πj/2}: half the second seed, instanced — as i is half of J"
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
known_since: "2026-08 (JH report, Layer 3: 'j := (([J_j] <[oo]>))'); Hamilton 1843"
entered: 2026-10-07
guide: shape-led
band: "beyond"
uses: [C.imaginary-unit, H.seed, Q.half]
see_also: [C.imaginary-unit, H.seed, H.k, H.j-squared]
aliases: [j, the unit j, half of J_j, e^{πj/2}]
concepts: [quaternion, phase]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `j := (([Jj] <[oo]>))` | half the second seed, instanced | j = e^{πj/2} |

Exactly as i is half of J ([[C.imaginary-unit]]: `(([J] <[oo]>))`), j is half of the second seed ([[H.seed]]): the log of J_j beside the log of a half ([[Q.half]]), instanced. In ℍ: e^{(π/2)j} = j.

## Plain

Take half of the second log of minus one and exponentiate: a second square root of minus one, in a new direction.

## Derivation

| form | rule | note |
|---|---|---|
| `(([Jj] <[oo]>))` | given | the seed ([[H.seed]]) halved, as i is halved in [[C.imaginary-unit]] ([[Q.half]]) |
| `j` | name | — |

## Confirms

j² = −1 ([[H.j-squared]]), by the same derivation as i² = −1. It is **not** yet anticommuting with i: that is O9 ([[H.anticommutation]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | there is one imaginary unit |
| JH, JO | holds | the definition |
| JP | holds | at every place: the Hurwitz unit j is the instance of half the seed (`tools/quatplace.py`) |

| reading | cell | why |
|---|---|---|
| C | ABSENT | no J_j in ℂ |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

Canonical strings accept the sugar `j`.
