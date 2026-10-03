---
id: mult.hole-instance
title: The instance of the black hole is the void
type: theorem
level: object
kind: law
rung: mult
order: 400
setting: classical
equality: "≐"
domain: positive
law: "(□) ≐ void"
units: "e^{−∞} = 0"
gloss_check: "0"
holds:
  classical: holds
  J1: untested
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "1993 (James)"
entered: 2026-10-03
guide: shape-led
band: beyond
uses: [mult.distribution, mult.involution, void.page, mult.black-hole]
see_also: [N.zero, mult.zero-annihilates, mult.dominion]
aliases: ["(□) = void", exp of minus infinity, zero as a value]
concepts: [zero, infinity]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(□) ≐ void` | — | e^{−∞} = 0 |

The black hole, circled, is nothing. This is the theorem that gives the number zero an inscription: `(□)` is 0 *as a value*, where the void is 0 as an absence.

## Plain

Circle the empty box and you get nothing — the first time zero shows up as something you can write.

## Derivation

| form | rule | note |
|---|---|---|
| `(□)` | given | — |
| `([])` | definition | unfold □, [[mult.black-hole]] |
| `([void void])` | [[void.page]] | the void is two voids |
| `([void]) ([void])` | [[mult.distribution]] | `(A [B C]) ≐ (A[B]) (A[C])` with A, B, C all void |
| `([]) ([])` | [[void.page]] | — |

So `([]) ≐ ([]) ([])`. Now apply Involution to the *general* instance: for any `B`, `([B]) ≐ ([B void]) ≐ ([B]) ([])` by [[mult.distribution]], and `([B]) ≐ B` by [[mult.involution]], giving `B ≐ B ([])` for every `B`. With `B` the void: `void ≐ ([])`.

| form | rule | note |
|---|---|---|
| `([B])` | given | any B |
| `([B void])` | [[void.page]] | — |
| `([B]) ([void])` | [[mult.distribution]] | — |
| `B ([])` | [[mult.involution]] | `([B]) ≐ B` |

Taking `B` = void in `B ≐ B ([])` gives `void ≐ ([])`.

## Confirms

e^{−∞} = 0 — the limit analysis takes, here an equation. Note the price: this needs **only** Involution and Distribution, no Inversion, so zero-as-a-value exists in the ℕ-with-× fragment. Its sibling `(A □) ≐ void` ("a · 0 = 0", [[mult.zero-annihilates]]) does *not*: that needs Inversion, and the chart proves it ([[mult.dominion-independence]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | untested | depends on the status of □ in J1 |
| JH, JO, JP | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | untested | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The engine evaluates `□` as a sentinel absorbing juxtaposition, with `(□) = 0`; this node is the justification for that evaluation rule.
