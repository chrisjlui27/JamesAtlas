---
id: Q.fraction
title: Fractions are quotients of piles
type: definition
level: object
kind: instance
rung: Q
order: 540
setting: classical
equality: ≐
domain: natural
law: "([oo] <[ooo]>) := 2/3"
units: "m/n = ([o^m] <[o^n]>)"
gloss_check: 2/3
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: guarded
readings:
  C: EXACT
  finset: ANALOGY
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: 1993 (James); fractions are Egyptian
entered: 2026-10-03
guide: shape-led
band: 3–5
uses: [Q.division, N.numeral]
see_also: [Q.half, Q.cancel-common-factor, Q.rational]
aliases: [m/n, numerator and denominator]
concepts: [fraction, division]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([oo] <[ooo]>)` | — | 2/3 |

A fraction is a pile divided by a pile: the numerator's abstract and the mirrored abstract of the denominator, under one instance.

## Plain

Two-thirds is the pile of two, boxed, next to the mirrored box of the pile of three, all circled.

## Derivation

| form | rule | note |
|---|---|---|
| `([oo] <[ooo]>)` | [[Q.division]] | 2 ÷ 3, with the piles of [[N.numeral]] |
| `2/3` | name | — |

## Confirms

The positive rationals as inscriptions. Equality of fractions is **not** visible yet — `([oo]<[oooo]>)` and `([o]<[oo]>)` are different inscriptions of ½ — and becomes a theorem at [[Q.cancel-common-factor]]; the choice of a canonical one is the gap [[Q.lowest-terms]].

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1, JH, JO | holds | real content |
| JP | guarded | a fraction is a form at p only when its denominator is a unit at p; `([o]<[oo]>)` is not a 2-adic integer |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ANALOGY | m · (1/n) as the cardinality of an action groupoid (m points, a ℤ/n acting freely) — the Baez–Dolan reading of [[Q.half]], extended |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
