---
id: C.modulus
title: The modulus is the root of z times its conjugate
type: definition
level: object
kind: law
rung: C
order: 1059
setting: classical
equality: "≐"
domain: real
law: "mod(A + iB) := (([[([A] [A]) ([B] [B])]] <[oo]>))"
units: "|a + bi| = √(a² + b²)"
gloss_check: "sqrt(A*A + B*B)"
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
known_since: "Argand 1806 (modulus); Cauchy 1821"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [alg.root, C.modulus-squared]
see_also: [C.modulus-squared, C.polar-form, alg.root]
aliases: [modulus, absolute value, "|z|"]
concepts: [complex-number, root]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[([A] [A]) ([B] [B])]] <[oo]>))` | — | √(a² + b²) |

The size of a complex number: the positive square root of z z̄. In the polar spelling it is the R of [[C.polar-form]]; here it is computed from the rectangular parts.

## Plain

How long a complex number is: square the two parts, add, take the root — Pythagoras, with the vertical side measured in i.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[([A] [A]) ([B] [B])]] <[oo]>))` | [[alg.root]] | the square root of a² + b², which is z z̄ by [[C.modulus-squared]] |
| `mod(A + iB)` | name | the modulus, written |a + bi| in standard notation |

## Confirms

|z| = √(a² + b²), the Euclidean length, and the r of r e^{iθ}. It is **not** derived from a geometry: the chart has no lengths yet, so this is a *definition*; its agreement with the polar R — |R e^{iπt}| = R for positive R — is the theorem [[C.modulus-of-polar]], rung-C algebra through the Pythagorean identity. Only the triangle inequality waits for the rung `analysis`.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | no Λ-step |
| JH, JO | replaced | the quaternionic norm, four squares |
| JP | guarded | as [[alg.root]] and [[C.imaginary-unit]] |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
