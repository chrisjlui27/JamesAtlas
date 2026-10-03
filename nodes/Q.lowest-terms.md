---
id: Q.lowest-terms
title: Lowest terms — a canonical fraction
type: gap
level: meta
kind: concept
rung: Q
order: 660
setting: classical
equality: ≐
domain: natural
law: "GAP — 'the reduced form of a fraction' is not an equation: deciding it needs a greatest common divisor, which is an iteration"
units: gcd(m, n) ; m/n in lowest terms
holds:
  classical: fails
  J1: fails
  JH: fails
  JO: fails
  JP: fails
readings:
  C: ABSENT
  finset: PARTIAL
  lambda: untested
  CC: untested
  logic: ABSENT
status: ABSENT
verified: hand
known_since: Euclid VII (the algorithm); the gap named here 2026-10-03
entered: 2026-10-03
guide: need-led
band: 3–5
uses: []
see_also: [Q.cancel-common-factor, Q.cross-multiplication, Z.normal-form, N.order, N.induction]
aliases: [reduced fraction, gcd, "Euclid's algorithm", canonical form of a rational]
concepts: [fraction, normal-form]
understood: partial
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| none | — | m/n with gcd(m, n) = 1 |

[[Q.cancel-common-factor]] proves that two fractions with a common factor are ≐; it does not say *which* fraction is the canonical one, nor how to find the common factor. Both are the job of Euclid's algorithm, and an algorithm is an iteration — "repeat until the remainder is void" — which no single equation states. The integers had a normal form by a terminating rewrite ([[Z.normal-form]]); the rationals do not, yet.

## Plain

The page can show that 2/4 and 1/2 are equal; it cannot by itself say that 1/2 is the "real" name, because finding the shared factor takes a repeated step the page has no form for.

## Derivation

none — gap.

## Confirms

That for the rationals a *canonical* name needs factoring, not a local rewrite: given two fraction forms, ≐ is decidable by [[Q.cross-multiplication]] (compare two piles), but a reduced representative needs the greatest common divisor, which no single cancellation finds. The gap is the same shape as [[N.induction]] — a "repeat" the equational calculus cannot say — and it is the first place the chart meets the re-entry idea from the place calculus (a guarded iteration that converges).

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | fails | no setting has an iteration construct; JP's guarded re-entry (JP-1) is the nearest thing and is not in the classical setting |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | PARTIAL | in finite sets a fraction m/n is a class of pairs; the canonical representative is a choice, and the groupoid-cardinality reading ([[Q.half]]) suggests the class, not the representative, is the object |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—

## Plan

| field | content |
|---|---|
| candidate form(s) | none as an equation. Candidate *meta-form*: Euclid as a guarded re-entry on piles — `x ≐ remainder(y, x)` iterated — in the style of the place calculus's JP-1 convention, where a re-entry with a shrinking guard converges |
| law(s) to add, and type | a `definition` at the meta level (the reduced form := the result of repeated [[Q.cancel-common-factor]] until no common pile divides both), or a `decree` (choose the representative with the smallest denominator pile) |
| nativity criterion | the procedure may use only cancel-common-factor, the normal form of piles, and a termination argument on pile size — no external gcd |
| refutation test | two fraction forms equal in ℂ whose cancellation sequences reach different "irreducible" forms (impossible if gcd is well-defined; the test bites on the termination argument) |
| meta-move? | yes: iteration / re-entry. The gap is a statement about a *process* on forms, not about a form; it is the first appearance of the fixed-point idea Lui favours for constructive computation |
| owner thread | p-adic-wall (re-entry, JP-1); boundary-lean-game |
| rank | meta-definition (iterated cancellation) < decree (smallest denominator) < new primitive (an iteration boundary — not proposed) |
