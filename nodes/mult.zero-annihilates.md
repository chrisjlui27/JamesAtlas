---
id: mult.zero-annihilates
title: Zero annihilates a product
type: theorem
level: object
kind: law
rung: mult
order: 410
setting: classical
equality: "≐"
domain: complex
law: "(A □) ≐ void"
units: "e^{a} · 0 = 0  (a · 0 = 0)"
gloss_check: "0"
holds:
  classical: holds
  J1: holds
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
known_since: "1993 (James); the ring fact is ancient"
entered: 2026-10-03
guide: need-led
band: "3–5"
uses: [mult.distribution, Z.inversion, void.page, void.space, mult.black-hole]
see_also: [mult.hole-instance, mult.dominion, mult.dominion-independence]
aliases: ["a·0 = 0", zero product, "(A □) = void"]
concepts: [zero, multiplication]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(A □) ≐ void` | — | e^a · 0 = 0 |
| `([B] □) ≐ void` | — | b · 0 = 0 |

Anything multiplied by zero is zero: an instance containing the black hole is the void, whatever else it contains.

## Plain

Times zero is zero — and the page needs the mirror to prove it.

## Derivation

| form | rule | note |
|---|---|---|
| `(A □)` | given | — |
| `(A [])` | definition | unfold □, [[mult.black-hole]] |
| `(A []) void` | [[void.page]] | — |
| `(A []) (A []) <(A [])>` | [[Z.inversion]] | create the pair `X <X>` with X = `(A [])` |
| `(A [void void]) <(A [])>` | [[mult.distribution]] | collect `(A [])(A [])` into `(A [void void])` — Distribution right to left; regroup by [[void.space]] |
| `(A []) <(A [])>` | [[void.page]] | `[void void]` is `[]` |
| `void` | [[Z.inversion]] | cancel |

## Confirms

The ring theorem a · 0 = 0, and its standard proof: a·0 = a·(0+0) = a·0 + a·0, then *subtract* a·0. The subtraction is the step the calculus cannot do without the angle boundary — Distribution alone only gives `(A []) ≐ (A []) (A [])`, an idempotent, which is not void in every model ([[mult.dominion-independence]]). So "times zero is zero" costs Inversion. That is why absorption is an *axiom* of semirings — it does not follow from the other semiring laws — and a *theorem* of rings; the chart's price ledger shows the same fact as a cost.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | inside an instance the pole empties whatever holds it: strict, no unit step (receipt prover: ≡); the stratification of Inversion does not touch this derivation |
| JH, JO | holds | the norm-form argument of JH-20 uses exactly this: `N(q) ≐ void` forces `[N] ≐ □` |
| JP | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | untested | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

James proves "void multiplication" `([a][]) = void` (p. 26) from Distribution plus the principle that collection has no idempotents; the chart proves it from Inversion. The two routes come apart in the 3-element model of [[mult.dominion-independence]].

Domain `complex` (widened 2026-10-03, C referee pass): rung C instantiates this law at complex content, and a law may be cited only inside its declared domain ([[mult.consistency]], Confirms); the law is exact on ℂ ∪ {□}. The home band and reading are unchanged.

Tagged *need-led*: the shape of the forms gives the idempotent for free; arithmetic insists on void, and insisting costs an axiom.
