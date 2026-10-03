---
id: mult.square
title: The square boundary
type: primitive
level: object
kind: boundary
rung: mult
order: 300
setting: classical
equality: "≐"
domain: positive
law: "[A] is a form"
units: "[A] = ln a"
gloss_check: "log(A)"
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: holds
readings:
  C: EXACT
  finset: PARTIAL
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "1993 (James)"
entered: 2026-10-03
guide: shape-led
band: "3–5"
uses: [void.page]
see_also: [N.round, mult.involution, mult.black-hole]
aliases: [abstract boundary, square, "[ ]", ln, log]
concepts: [logarithm, abstract]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[A]` | — | ln a |

For any form `A`, `[A]` is a form: the *abstract* of `A`. Read in ℂ it is the logarithm. It is the functional inverse of the round boundary — but that is an axiom ([[mult.involution]]), not part of the primitive.

## Plain

The square box asks "what would I have to circle to get this?" — that it really undoes the circle is the next law, not this one.

## Derivation

none — adjoined. The boundary may be drawn around any form, beginning with the void, [[void.page]].

## Confirms

The *existence* of a logarithm as a primitive, so that multiplication can be *defined* ([[mult.multiplication]]) rather than posited. In standard mathematics the logarithm arrives after months of analysis; here it is the second boundary, and the exp–log relation is structural from the start. What it does **not** give is a choice of base: `(o)` is a named constant e, and `[A]` is ln, only in the ℂ reading.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the boundary stays; its unit with `( )` is weakened mod Λ |
| JH, JO | replaced | the square becomes the singleton case `[x ;]` of the ordered bracket `[ ; ]` (JH Ch. 12): the old square is recovered, the new one carries order in depth |
| JP | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | ln |
| finset | PARTIAL | the hinge `() ⊣ []` as Sym ⊣ Ch (the Chern-character linearization) is Lui's proposed F₁ reading; a reading, not yet a law |
| logic | untested | the naive logical meaning of `[ ]` is unclear (james-algebra notes); this is where the affine-logic question lives |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

James's `[[ ]]` (the square of the black hole) was left undefined; Bricken (Iconic Arithmetic) equates it to complex infinity. The chart treats `[[ ]]` as excluded ([[mult.hole-exclusion]]) rather than adopting either reading.
