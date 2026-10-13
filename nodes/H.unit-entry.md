---
id: H.unit-entry
title: The unit entry
type: axiom
level: object
kind: law
rung: H
order: 1620
setting: JH
equality: "≐"
domain: complex
law: "[A ; o ; B] ≐ [A ; B]"
units: "A·1·B = A·B: the entry one is deleted; at any position; a one-entry result is the square"
gloss_check: ""
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: holds
  JP: guarded
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "2026-08 (JH report, Layer 3: unit-deletion)"
entered: 2026-10-07
guide: shape-led
band: "beyond"
uses: [H.ordered-bracket, N.unit, mult.unit-law]
see_also: [mult.unit-law, H.splice, H.ordered-cancellation]
aliases: [unit deletion, the entry one, "[x ; o ; z] = [x ; z]"]
concepts: [ordered-product, one]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[A ; o ; B] ≐ [A ; B]` | an entry `o` = 1 ([[N.unit]]) leaves the product as it was | A·1·B = AB |

The ordered analogue of [[mult.unit-law]], `([A][o]) ≐ A`: the entry one is a multiplicative unit on either side of anything. A family over the position and the length (2 … 5 entries); when the deletion leaves one entry the result is the ordinary square (`[A ; o] ≐ [A]`).

## Plain

Multiplying by one, in any position, changes nothing — so the entry "one" can be struck from the row.

## Derivation

none — adjoined, as a rule of the ordered square ([[H.ordered-bracket]]) about the unit ([[N.unit]]); the one-entry case is [[mult.unit-law]] read through the counit.

## Confirms

1 is the two-sided unit of ℍ. It is **not** derivable from splice: splice relates lists to their products, and `o` is the instance of the void, not of a list.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | [[mult.unit-law]] |
| JH, JO | holds | an axiom of the setting; the octonions have a two-sided unit too |
| JP | guarded | at every place, exact wherever the ordered square has a value ([[H.ordered-bracket]]; census/h-place-ledger.md) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

With [[H.ordered-cancellation]] the two together are the cancellation rules of the ordered calculus: a pair y ; y⁻¹ becomes the entry one, and the entry one disappears.
