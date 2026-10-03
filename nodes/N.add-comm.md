---
id: N.add-comm
title: Addition commutes and associates — for free
type: theorem
level: object
kind: law
rung: N
order: 140
setting: classical
equality: "≐"
domain: natural
law: "oo ooo ≐ ooo oo"
units: "2 + 3 = 3 + 2"
gloss_check: "5"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: EXACT
status: NATIVE
verified: engine
known_since: "1993 (James); the facts are ancient"
entered: 2026-10-03
guide: shape-led
band: K
uses: [N.addition, void.space]
see_also: []
aliases: [commutativity of addition, associativity of addition]
concepts: [addition]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `oo ooo ≐ ooo oo` | — | 2 + 3 = 3 + 2 |
| `A B ≐ B A` | — | a + b = b + a |

## Plain

It does not matter which pile you put down first, or how you group them; there is no "first" on a page.

## Derivation

| form | rule | note |
|---|---|---|
| `oo ooo` | [[N.addition]] | 2 + 3 |
| `ooo oo` | medium | the same multiset, [[void.space]] |

## Confirms

Commutativity and associativity of addition on ℕ — the two laws a Peano-style development proves by induction. Here they are inherited from the medium and cost nothing. What this does **not** give is the *inductive* proof: the chart records that absence at [[N.induction]].

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | holds | medium |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | EXACT | — |
| logic | EXACT | the medium is shared with LoF |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The thinnest theorem in the chart, kept because it is a *law gained*: the two most-cited axioms of additive arithmetic are free in this medium, and the chart's price ledger should say so.
