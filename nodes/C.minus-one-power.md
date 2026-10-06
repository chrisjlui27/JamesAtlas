---
id: C.minus-one-power
title: Minus one to a power is the pure phase
type: definition
level: object
kind: law
rung: C
order: 1055
setting: classical
equality: "≐"
domain: real
law: "(−1)^X := (([[<o>]] [X]))"
units: "(−1)^x = e^{iπx}"
gloss_check: "exp(1j*pi*X)"
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "Euler, E168 (1747/1751), where the branches of (−1)^x and the principal choice are explicit; 1993 (James)"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.exponentiation, Z.negative-numeral, C.phase]
see_also: [C.polar-form, C.imaginary-unit, C.phase-value, alg.root]
aliases: ["(−1)^x", pure phase, "e^{iπx}", power of minus one]
concepts: [phase, exponentiation, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[<o>]] [X]))` | `(([J] [X]))` | (−1)^x = e^{iπx} |

The exponential schema `A ^ B := (([[A]] [B]))` at the base −1. Since `[<o>]` *is* J, the form is `(([J] [X]))`: the pure phase of the polar form, a turn of x half-turns. "A power of minus one" and "a turn" are the same form, not two forms that happen to agree.

## Plain

Minus one to the x is "x half-turns": at x = 1 it is minus one, at x = ½ it is i, at x = 2 it is one again. The page needs no separate idea of angle; it has powers of minus one.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[<o>]] [X]))` | [[mult.exponentiation]] | (−1) ^ x, with −1 the mirrored unit ([[Z.negative-numeral]]) |
| `(([J] [X]))` | definition | `[<o>]` is J ([[C.phase]]) — the same form, written with the abbreviation |
| `(−1)^X` | name | — |

## Confirms

(−1)^x = e^{iπx}, the principal value. At x = ½ this is `(([J] [(<[oo]>)]))`, which one absorbing unit step turns into `(([J] <[oo]>))` = i ([[C.imaginary-unit]]): so i = (−1)^{½} = √−1 is a theorem of the definitions, not a slogan. At x = 1 it is `(([J] [o]))` → `(([J]))` → `(J)` = −1 ([[C.phase-value]]); at x = 2, `o` ([[C.double-phase]]). It is **not** multivalued on the page: (−1)^{1/3} here is e^{iπ/3} ([[C.cube-root-of-negation]]), not −1 — the real cube root is a different form, `<o>` itself; the standard notation's ambiguity is resolved by the forms, which say which root they mean.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | a definition; `(([J] [X]))` with J = ω/2 is the same shape |
| JH, JO | replaced | one pure phase per slice, `(([J_u] [X]))` |
| JP | holds | (−1)^x at a place, for the integer samples of the page: the torsion power |

| reading | cell | why |
|---|---|---|
| C | EXACT | the principal value |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The two rows of the derivation are the *same* canonical form — the engine's equality check between them is trivial — and that is the content of the node: there is no step from "a power of −1" to "a turn".
