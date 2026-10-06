---
id: place.fermat
title: A unit to the power φ(p^n) is one
type: schema
level: object
kind: law
rung: place
order: 1450
setting: JP
equality: "≡"
domain: unit
law: "(([[U]] [o^{(p-1)*p**(n-1)}])) ≐ o"
units: "U^{φ(p^n)} ≡ 1 (mod p^n) for p ∤ U — Euler's theorem; at depth 1, Fermat's little theorem"
gloss_check: ""
schema_range: "p=2,3,5,7; n=1..2"
schema_draw: "p=5; n=1"
holds:
  classical: fails
  J1: fails
  JH: untested
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
known_since: "Fermat 1640, Euler 1763; on the page: Part II Ch. 10 (Division-by-unit rests on it)"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [mult.exponentiation, place.void-pile, place.reading]
see_also: [place.division-by-unit, place.teichmuller, place.torsion, J1.receptacle, schema.power, N.order]
aliases: [Fermat's little theorem, Euler's theorem, U^φ = 1, the order of the unit group, φ(p^n) = (p−1)p^{n−1}]
concepts: [place, power, one, prime]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[U]] [o^{(p-1)*p**(n-1)}])) ≐ o` | a unit raised to the count φ(p^n) = (p−1)p^{n−1} is one at depth n | U^{φ(p^n)} ≡ 1 mod p^n |

The first law of the place that is *about* the place's numbers rather than its page: the units of ℤ/p^n form a group of order φ(p^n), and a power with that count returns to one. On the page it reads: the torsion count of U times φ is a multiple of p − 1 (the torsion is absorbed, [[place.teichmuller]]) and the principal part's log times p^{n−1} lands beyond the depth. It is the engine's statement; the chart has no derivation for it yet, because the counting argument behind it (Lagrange: the order of an element divides the order of the group) needs an order or a count of forms the chart does not have ([[N.order]]).

## Plain

Multiply any number coprime to p by itself (p − 1)p^{n−1} times and, on the clock with p^n hours, you are back at 1.

## Derivation

| statement | rule | note |
|---|---|---|
| **Taken on the engine's word.** The law is the power form of [[mult.exponentiation]] with the count φ(pⁿ); the engine checks it on random units at every instance. Its derivation is a counting argument — the order of an element divides the order of the group — that the chart cannot yet make, and the rung records it as its one law without a derivation on the page | [[place.void-pile]] | at depth n the units are the residues coprime to p, φ(p^n) of them; the reading ([[place.reading]]) sees the torsion count times φ as a multiple of p − 1 and the principal part's log times p^{n−1} past the depth |

## Confirms

Fermat's little theorem at depth 1 and Euler's at depth n; the order p − 1 of the torsion ([[place.torsion]]: at depth 1, φ(p) = p − 1 is the (p−1)-th roots of unity, [[J1.receptacle]] at the place). It is **not** a statement about which units have which order (the primitive roots): the torsion log's *generator* is chosen by the reading ([[place.reading]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | fails | at ∞ no power of a number other than 1 is 1 (for positive reals); the law is the finite clock's |
| J1 | fails | as classical |
| JH, JO | untested | owed |
| JP | holds | engine-checked on units at p = 2, 3, 5, 7, depths 1, 2 |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | EXACT | the group (ℤ/p^n)^× of order φ(p^n) |
| lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The domain is `unit`: the engine samples U coprime to p. At p = 2, depth 1, φ = 1 and the law reads `U ≐ o`: every odd number is one mod 2.
