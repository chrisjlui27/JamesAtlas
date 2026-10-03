---
id: void.space
title: Space — juxtaposition is unordered
type: primitive
level: object
kind: medium
rung: void
order: 20
setting: classical
equality: "≐"
domain: real
law: "A B ≐ B A"
units: "a + b = b + a"
gloss_check: "A + B"
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
known_since: "1993 (James): 'space is the first operator'"
entered: 2026-10-03
guide: shape-led
band: K
uses: [void.page]
see_also: [N.addition, N.add-comm]
aliases: [juxtaposition, breadth, the medium]
concepts: [addition, space]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `A B ≐ B A` | — | a + b = b + a |

Forms standing together in the same space make a form. Space has no order and no grouping: a juxtaposition is a **multiset**. Commutativity is this law; associativity is not even statable, because `A B C` has no brackets to move.

## Plain

Things sitting together on a page have no first or second; so adding is the same in either order, for free.

## Derivation

none — adjoined. A fact of the medium; its unit is the void, [[void.page]].

## Confirms

The additive layer of arithmetic is a *commutative monoid* with the void as unit — before any number has been written. It is **not** multiplication: juxtaposition becomes multiplication only under an instance boundary, `([A][B])`, at [[mult.multiplication]]. And it is the deepest design decision in the calculus: because breadth is unordered, no non-commutative product can ever live in it (the No-Go theorem, JH-1 — a later node).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | medium |
| J1 | holds | juxtaposition is addition; receipts live on a tape, not in breadth |
| JH, JO | holds | the ordered bracket `[ ; ]` is a new primitive in *depth*; breadth is untouched |
| JP | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | + |
| finset | EXACT | disjoint union, commutative up to isomorphism |
| logic | EXACT | Laws of Form shares the unordered medium — but adds Calling, `o o ≐ o`, which James refuses (see [[N.numeral]]) |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Because this is a primitive of the medium rather than an axiom, the chart's price ledger counts commutativity as *free*. Every later law that depends on rearranging forms cites this node once under the rule name `medium`.
