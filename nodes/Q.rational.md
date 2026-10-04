---
id: Q.rational
title: The rational numbers
type: definition
level: object
kind: schema
rung: Q
order: 630
setting: classical
equality: ≐
domain: natural
law: "<([oo] <[ooo]>)> := −2/3"
units: "ℚ = { ([o^m] <[o^n]>) with n ≥ 1, their mirrors, and the void }"
gloss_check: -2/3
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
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
band: 6–8
uses: [Z.angle, Q.fraction, void.page]
see_also: [Z.normal-form, Q.lowest-terms, Q.cross-multiplication, N.order]
aliases: [ℚ, rational number, signed fraction]
concepts: [fraction, integer, negation, normal-form]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `<([oo] <[ooo]>)>` | — | −2/3 |

A rational number is a fraction of piles, the mirror of one, or the void. The class is closed under the arithmetic of this rung: a juxtaposition of instances, mirrored or not, whose contents are juxtapositions of `[pile]` and `<[pile]>`, reduces to one of these — the normal-form theorem [[Q.normal-form]] (see Notes).

## Plain

The rationals are the fractions, their mirror images, and zero.

## Derivation

| form | rule | note |
|---|---|---|
| `<([oo] <[ooo]>)>` | [[Z.angle]] | the mirror of a fraction, [[Q.fraction]]; the void is [[void.page]] |
| `−2/3` | name | — |

## Confirms

ℚ as a set of inscriptions. Two things are **not** given: that two inscriptions name the same rational ([[Q.cancel-common-factor]] decides it instance by instance; a canonical form is [[Q.lowest-terms]]), and the order and density of ℚ ([[N.order]]). The field laws are all above this node — as axioms (Inversion, Distribution), medium facts (commutativity, identity), theorems (the rest), and one meta node (0 ≠ 1, [[mult.consistency]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1, JH, JO | holds | — |
| JP | guarded | fractions with unit denominators are integers at the place — the re-entrant "dolls" (periodic expansions) of the p-adic-wall thread, whose completion is ℤ_p; fractions with the prime in the denominator are not forms at p at all (No-inverse-of-the-prime) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

- ~~every form in which each pile occurs only as `[pile]` or `<[pile]>` directly under an instance is rational~~ — refuted 2026-10-03 (second referee pass): `(([oo]))` = e² fits that description. The class must be stated as juxtapositions of (mirrored) instances of such contents.

## Notes

The normal-form theorem for this class — derivable from [[Q.add-fractions]], [[Q.negative-fraction]], [[mult.product-of-numerals]], [[Z.normal-form]], [[Q.zero-divided]] for a void numerator, and the degenerate shapes [[Q.division-by-one]] and [[Q.one-over-a]] — is the node [[Q.normal-form]].
