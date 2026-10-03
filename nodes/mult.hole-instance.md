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
domain: complex
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
uses: [mult.involution, void.page, mult.black-hole]
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
| `([])` | definition | unfold □, [[mult.black-hole]]; this is `([void])`, [[void.page]] |
| `void` | [[mult.involution]] | `([A]) ≐ A` with A = void — Involution-up at the void |

## Confirms

e^{−∞} = 0 — the limit analysis takes, here one instance of Involution. Its price is the smallest possible: the counit at the void, nothing else. Its sibling `(A □) ≐ void` ("a · 0 = 0", [[mult.zero-annihilates]]) is not so cheap: that needs Inversion, and the chart shows why ([[mult.dominion-independence]]).

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

- ~~needs Distribution as well as Involution~~ — the first draft (2026-10-03) derived this through a Distribution detour; the referee pass the same day pointed out it is Involution-up at `A` = void in one step. Price corrected.

## Notes

Domain `complex` (widened 2026-10-03, C referee pass): rung C instantiates this law at complex content, and a law may be cited only inside its declared domain ([[mult.consistency]], Confirms); the law is exact on ℂ ∪ {□}. The home band and reading are unchanged.

The engine evaluates `□` as a sentinel absorbing juxtaposition, with `(□) = 0`; this node is the justification for that evaluation rule. In the finite models of [[mult.dominion-independence]] the law reads e(l(0)) = 0 and holds in every one, as it must: it is Involution at 0.
