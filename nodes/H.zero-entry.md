---
id: H.zero-entry
title: An empty entry is the pole
type: theorem
level: object
kind: law
rung: H
order: 1640
setting: JH
equality: "≡"
domain: complex
law: "[A ; void] ≡ □"
units: "log(A·0) = log 0: the black hole; at any position"
gloss_check: ""
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "this chart, 2026-10-07 (the JH report notes 'an empty-list/black-hole notation collision' and leaves it)"
entered: 2026-10-07
guide: shape-led
band: "beyond"
uses: [H.list-distribution, J1.unit, Z.inversion, mult.black-hole, void.page]
see_also: [mult.black-hole, mult.zero-annihilates, H.list-distribution, H.central-sign]
aliases: [the empty entry, zero in a list, "[x ; void] = □", the empty-list collision]
concepts: [ordered-product, zero, pole]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[A ; void] ≡ □` | an entry that is nothing makes the product nothing, and the log of nothing is the black hole | log(A·0) = log 0 = −∞ |

The void entry is the number 0, and a product with 0 is 0, whose log is the pole ([[mult.black-hole]]). On the chart the fact is a theorem of list distribution: an entry `B void` is the entry `B` ([[void.page]]), so `([A ; B]) ≐ ([A ; B]) ([A ; void])`, and cancelling gives `([A ; void]) ≐ void`, whose log is the empty square. The family covers either position.

## Plain

Multiply anything by zero and you get zero; the log of zero is the black hole. The ordered box with an empty slot is that black hole.

## Derivation

| form | rule | note |
|---|---|---|
| `[A ; void]` | given | an ordered square with an empty entry ([[H.list-distribution]] will split it off) |
| `[([A ; void])]` | [[J1.unit]] | the unit, right to left, on pole-valued content: strict (LEGISLATION 30f — the pole has no winding) |
| `[([A ; void]) ([A ; o]) <([A ; o])>]` | [[Z.inversion]] | a pair created beside it |
| `[([A ; o void]) <([A ; o])>]` | [[H.list-distribution]] | the two instances collected into one: the entry `o void` |
| `[([A ; o]) <([A ; o])>]` | [[void.page]] | `o void` is `o` — the same form |
| `[void]` | [[Z.inversion]] | the pair cancels |
| `□` | [[mult.black-hole]] | the empty square is the black hole |

## Confirms

0 annihilates in ℍ and the black hole is its log, as on the trunk ([[mult.zero-annihilates]]). It is **not** a new rule: the JH report flagged an empty list as a notational collision with the black hole; here the collision is a theorem.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | [[mult.zero-annihilates]] and the hole rules |
| JH | holds | strict: the unit on pole-valued content and the strict rules |
| JO | holds | the octonions annihilate by 0 too |
| JP | holds | at every place: the void entry is the void pile's number, 0 |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The prover's family (`_family_zero_entry`) covers lists of two and three entries with the void in any position.
