---
id: N.round
title: The round boundary
type: primitive
level: object
kind: boundary
rung: N
order: 100
setting: classical
equality: "≐"
domain: real
law: "(A) is a form"
units: "(A) = e^A"
gloss_check: "exp(A)"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: PARTIAL
  lambda: untested
  CC: untested
  logic: PARTIAL
status: NATIVE
verified: engine
known_since: "1993 (James)"
entered: 2026-10-03
guide: shape-led
band: K
uses: [void.page]
see_also: [N.unit, mult.square, mult.involution]
aliases: [instance boundary, round, "( )", exp]
concepts: [exponential, instance]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(A)` | — | e^A |

For any form `A`, `(A)` is a form: the *instance* of `A`. Read in ℂ it is the exponential of `A`. The base is unconstrained by anything at this rung; nothing below depends on it until the square boundary fixes `(o)` as a named constant.

## Plain

Drawing a circle around something makes a new thing; the empty circle is the first thing you can count.

## Derivation

none — adjoined. The boundary may be drawn around any form, beginning with the void, [[void.page]].

## Confirms

The *existence* of an exponential: a map from the additive layer to the multiplicative one. It is **not** yet a function with an inverse — that is Involution, [[mult.involution]] — and `(A)` has no arithmetic meaning on its own at this rung beyond the one case `()`, which is the unit [[N.unit]].

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | holds | the boundary is never withdrawn; in J1 its *unit* with `[ ]` is weakened, not the boundary |

| reading | cell | why |
|---|---|---|
| C | EXACT | exp |
| finset | PARTIAL | `o` is a point; `(A)` as the free symmetric construction (Sym) is the proposed F₁ reading — see the `struct` rung when it is laid |
| logic | PARTIAL | Bricken reads the single boundary of boundary logic as NOT; James's round is not that — only `o` as "the mark" is shared |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

James's name is *instance*; Bricken's unit-ensemble presentations (Iconic Arithmetic I) use the same boundary as the "unit" with the same reading.
