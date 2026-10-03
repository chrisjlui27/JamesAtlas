---
id: alg.nth-root
title: Roots of every order
type: definition
level: object
kind: schema
rung: alg
order: 800
setting: classical
equality: ≐
domain: positive
law: "∛A := (([[A]] <[ooo]>))"
units: "ⁿ√a = a^{1/n} = (([[A]] <[o^n]>))"
gloss_check: A ** (1/3)
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: 1993 (James)
entered: 2026-10-03
guide: shape-led
band: 9–12
uses: [mult.exponentiation, Q.reciprocal, mult.involution, N.numeral]
see_also: [alg.root, alg.rational-exponent]
aliases: [cube root, nth root, a^{1/n}]
concepts: [root, exponentiation]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[A]] <[ooo]>))` | — | ∛a |

The count under the double abstract can be any mirrored pile: the n-th root is the 1/n count one level down.

## Plain

A cube root is the same as a square root with a pile of three instead of two in the mirror.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[A]] [(<[ooo]>)]))` | [[mult.exponentiation]] | a ^ (1/3), with 1/3 = `(<[ooo]>)`, [[Q.reciprocal]] of the pile of three, [[N.numeral]] |
| `(([[A]] <[ooo]>))` | [[mult.involution]] | the unit on content `<[ooo]>` (real), directly under the inner instance |
| `∛A` | name | — |

## Confirms

All radicals, by one mechanism. With [[alg.rational-exponent]] the calculus writes every a^{m/n}; with [[alg.product-of-powers]] and [[alg.power-of-power]] it manipulates them. What it does **not** reach is the algebraic numbers that are not radicals — [[alg.non-radical]].

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the unit step is directly under an instance |
| JH, JO | replaced | within one slice |
| JP | guarded | n must be a unit at p and the p-adic logarithm of a must converge (the wall parameterization's criterion, p-adic-wall) |

| reading | cell | why |
|---|---|---|
| C | EXACT | the principal root |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
