---
id: Q.cancel-common-factor
title: Equivalent fractions — a common factor cancels
type: theorem
level: object
kind: law
rung: Q
order: 580
setting: classical
equality: ≐
domain: positive
law: "([([A] [C])] <[([B] [C])]>) ≐ ([A] <[B]>)"
units: (ac)/(bc) = a/b
gloss_check: A / B
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
known_since: 1993 (James); the fact is Euclid VII
entered: 2026-10-03
guide: shape-led
band: 3–5
uses: [Q.division, mult.multiplication, mult.involution, Z.collection, Z.inversion, void.space]
see_also: [Q.lowest-terms, Q.fraction, Q.quotient-of-numerals]
aliases: [equivalent fractions, reducing a fraction, cancelling]
concepts: [fraction, division]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([([A] [C])] <[([B] [C])]>) ≐ ([A] <[B]>)` | — | (a·c) ÷ (b·c) = a ÷ b |

## Plain

A factor shared by the top and bottom of a fraction disappears: under the box it is a plus and a minus of the same thing.

## Derivation

| form | rule | note |
|---|---|---|
| `([([A] [C])] <[([B] [C])]>)` | given | (a·c) ÷ (b·c): [[Q.division]] of two products, [[mult.multiplication]] |
| `([A] [C] <[([B] [C])]>)` | [[mult.involution]] | `[(X)] ≐ X` on the numerator |
| `([A] [C] <[B] [C]>)` | [[mult.involution]] | the same on the denominator |
| `([A] [C] <[B]> <[C]>)` | [[Z.collection]] | split the mirror; regroup by [[void.space]] |
| `([A] <[B]>)` | [[Z.inversion]] | `[C] <[C]>` cancels |

## Confirms

Equivalent fractions. With it, and with [[Q.division-by-one]], `6 ÷ 2 ≐ 3` becomes the theorem [[Q.quotient-of-numerals]]. The schoolroom "cancel the common factor" is literally Inversion on the abstracts. What it does **not** give is a *canonical* reduced form — see [[Q.lowest-terms]].

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the Involution-down steps sit at depth 1 under the instance (depth-1 criterion, [[mult.involution]] Notes) |
| JH, JO | replaced | a common factor cancels only where it meets its own inverse — the right factor of `x·y⁻¹`, the left factor of `y⁻¹·x`; on the other side it conjugates instead |
| JP | guarded | cancelling a factor that is the prime involves `<[p]>`, which is not a form at p |

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
