---
id: place.division-by-unit
title: The reciprocal of a unit is a power of it
type: schema
level: object
kind: law
rung: place
order: 1460
setting: JP
equality: "≃"
domain: unit
law: "(<[U]>) ≃ (([[U]] [o^{(p-1)*p**(n-1) - 1}]))"
units: "U^{−1} ≡ U^{φ(p^n) − 1} (mod p^n): division by a unit is a multiplication on the finite page"
gloss_check: ""
schema_range: "(p,n)=(2,2),(3,1),(3,2),(5,1),(5,2),(7,1),(7,2)"
schema_draw: "p=3; n=1"
holds:
  classical: fails
  J1: fails
  JH: guarded
  JO: untested
  JP: holds
readings:
  C: ABSENT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE-BY-SCHEMA
verified: engine
known_since: "Part II Ch. 10 (Division-by-unit); the inverse by Euler's theorem, Euler 1763"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [Q.reciprocal, place.fermat, mult.log-of-one, mult.distribution, J1.unit, J1.counit, Z.inversion, place.ostrowski]
see_also: [Q.reciprocal, Q.reciprocal-law, place.no-inverse-of-the-prime, place.fermat, place.geometric-doll]
aliases: [division by a unit, the reciprocal as a power, U^{−1} = U^{φ−1}, Division-by-unit]
concepts: [place, division, power]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(<[U]>) ≃ (([[U]] [o^{(p-1)*p**(n-1) - 1}]))` | the reciprocal of a unit is its (φ(p^n) − 1)-th power at depth n | U^{−1} = U^{φ−1} since U^φ = 1 |

What [[place.no-inverse-of-the-prime]] refuses for the prime, this grants for every unit, and more: the reciprocal is not a new number but a power of the old one. The derivation inserts U^φ = 1 ([[place.fermat]]) beside the reciprocal, splits off one factor of U by Distribution, and cancels it against the mirror — Inversion, the chart's division ([[Q.reciprocal-law]]), doing the work. The Fermat step is a page step under a square, and the prover measures it at the squares above it — here one: `[o]` is the period, `[U^{φ}]` a principal part that vanishes at the depth — the square's value changes by ω_p, and the instance directly around it pays that receipt (absorbed), with nothing above the instance to read the page difference again. So the law is ≃: the page's equality, and a period absorbed.

## Plain

On a finite clock, dividing by a number coprime to p is the same as multiplying by it a fixed number of times — one less than the number of times that brings it back to 1.

## Derivation

| form | rule | note |
|---|---|---|
| `(<[U]>)` | given | the reciprocal of the unit U ([[Q.reciprocal]]); at every place ([[place.ostrowski]]) |
| `(<[U]> [o])` | [[mult.log-of-one]] | the log of one inserted inside the instance (absorbed at the place as at 𝕁₁) |
| `(<[U]> [(([[U]] [o^{(p-1)*p**(n-1)}]))])` | [[place.fermat]] | one is U^φ, right to left, inside the square: a page step, measured at the square above it — its value changes by the period, which the instance directly outside absorbs |
| `(<[U]> ([[U]] [o^{(p-1)*p**(n-1)}]))` | [[J1.unit]] | the unit, directly inside the instance: absorbed |
| `(<[U]> ([[U]] [o^{(p-1)*p**(n-1) - 1}]) ([[U]] [o]))` | [[mult.distribution]] | the count φ split as (φ − 1) + 1: `[o^{φ-1} o]` is the pile `[o^{φ}]` regrouped |
| `(<[U]> ([[U]] [o^{(p-1)*p**(n-1) - 1}]) ([[U]]))` | [[mult.log-of-one]] | the count one erased, inside the instance |
| `(<[U]> ([[U]] [o^{(p-1)*p**(n-1) - 1}]) [U])` | [[J1.counit]] | `([[U]]) ≡ [U]` |
| `(([[U]] [o^{(p-1)*p**(n-1) - 1}]))` | [[Z.inversion]] | `<[U]> [U]` cancels: the reciprocal was the power all along |

## Confirms

Modular inverses by Euler's theorem, and that the finite page is a ring in which the units divide: every fraction with a unit denominator is a form at p, as rung `Q`'s JP cells say ("for units"). It is **not** the extended Euclidean algorithm — the gap of [[Q.lowest-terms]] is still open; this inverse is a power, not a Bézout pair.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | fails | at ∞ a reciprocal is not a power of the number ([[place.fermat]] fails there) |
| J1 | fails | as classical |
| JO | untested | owed |
| JH | guarded | on the centre: for a non-central unit U the quotient's log is not `[A] <[U]>` unless A and U commute — the no-go at the place ([[H.split-place]]); exact on the centre, fails on generic quaternions (census/h-place-ledger.md) |
| JP | holds | engine-checked at p = 3, 5, 7, depths 1, 2, and at p = 2, depth 2; absorbed receipts (the inserted log of one, the page step measured at its square, the unit inside the instance) |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | EXACT | the inverse in (ℤ/p^n)^× |
| lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

At p = 2, depth 1, φ − 1 = 0 and the right side reads through the hole rules: `[o^{0}]` is the empty square, `([[U]] □)` is □ by Dominion and `((□))` is `(void)` = o — every odd number is its own reciprocal mod 2, and the form says so; the law is true there and its rows are licensed, but the Fermat step's square, `[o]` → `[U]`, changes by J₂ — half the period — for U ≡ 3 mod 4 (the torsion −1 is invisible on the page mod 2 and visible in the log), which no instance absorbs, so the prover grades that instance absent and it is left out of the range. The schema is drawn at p = 3, depth 1: the reciprocal of a unit mod 3 is the unit itself (φ − 1 = 1).
