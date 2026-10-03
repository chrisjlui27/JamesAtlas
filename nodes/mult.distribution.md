---
id: mult.distribution
title: Distribution
type: axiom
level: object
kind: law
rung: mult
order: 320
setting: classical
equality: "≐"
domain: positive
law: "(A [B C]) ≐ (A [B]) (A [C])"
units: "e^{a}·(b + c) = e^{a}·b + e^{a}·c"
gloss_check: "exp(A)*(B + C)"
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
known_since: "1993 (James), axiom 2 of three"
entered: 2026-10-03
guide: shape-led
band: "3–5"
uses: [N.round, mult.square, void.space]
see_also: [mult.multiplication, mult.cardinality, mult.hole-instance]
aliases: [Distribution, James axiom 2, arrangement, A4]
concepts: [multiplication, distributive-law]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(A [B C]) ≐ (A [B]) (A [C])` | — | e^a (b + c) = e^a b + e^a c |

An instance boundary holding an abstract distributes over the abstract's contents. Read right to left: two instances sharing a context collect into one.

## Plain

Multiplying a sum is the same as multiplying each part and adding — written as: a circle around a box of two piles may be split into two circles.

## Derivation

none — adjoined. The second of James's three axioms, stated in terms of [[N.round]], [[mult.square]] and juxtaposition [[void.space]].

## Confirms

The ring law a(b + c) = ab + ac "wearing exponential clothing": with multiplication as `([x][y])`, this axiom *is* distributivity. It is **not** the exponential law e^{x+y} = e^x e^y — that is a consequence of the *definition* of multiplication plus Involution, not of this axiom — and in ℍ the two part ways: exp-splitting fails while ring distributivity holds on both sides, which is why JH *replaces* this axiom by a two-sided list distribution rather than weakening it (JH Ch. 12).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | axiom |
| J1 | holds | the critical pairs (counit, distribution, inversion × period) converge once A5′ is adopted (james-algebra, O3 completion); "Arrangement retained, possibly mod Λ" (legislation 2026-08-22) |
| JH, JO | replaced | two-sided list distribution `([x⃗ ; y z ; w⃗]) ≐ ([x⃗;y;w⃗]) ([x⃗;z;w⃗])`; the classical law is its one-slot, slice-pure case |
| JP | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | PARTIAL | distributivity of × over ⊔ in finite sets is exact; the *exponential clothing* (reading `(A[·])` as a functor) is the open part |
| logic | untested | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

With the void as `C` this axiom degenerates to `(A [B]) ≐ (A [B]) (A [])`, which is the engine of the black-hole theorems [[mult.hole-instance]] and [[mult.zero-annihilates]].
