---
id: place.negation-is-a-pile
title: Minus one is a pile
type: schema
level: object
kind: law
rung: place
order: 1420
setting: JP
equality: "≃"
domain: natural
law: "<o> ≃ o^{p**n - 1}"
units: "−1 ≡ p^n − 1 (mod p^n): …111 in base 2, …444 in base 5 — the angle boundary is eliminable on a finite page"
gloss_check: ""
schema_range: "p=2,3,5; n=1..3"
schema_draw: "p=2; n=3"
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
known_since: "2026-09-19 (the doll of −1: x ≐ o ([oo][x]) converges to <o> at p = 2); Part II Ch. 10 (Floor, Predecessor); as the p-adic −1 = …(p−1)(p−1)(p−1), Hensel 1897"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [place.void-pile, Z.inversion, void.space, place.ostrowski]
see_also: [Z.negative-numeral, Z.angle, place.residue, place.doll, place.geometric-doll]
aliases: [−1 = …111, the mirror is a pile, negation at a place, Floor, Predecessor]
concepts: [place, negation, zero]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `<o> ≃ o^{p**n - 1}` | the mirror of one is a pile of p^n − 1 marks at depth n | −1 = p^n − 1 mod p^n: …1111₂, …2222₃ |

At ∞ the angle boundary is irreducible: no pile is a negative number ([[Z.negative-numeral]]). At a finite place it reduces: minus one is the pile one short of the void pile, and so every negative integer is a pile. The angle boundary is still *drawn* — the law says what it equals, not that it is absent — but its arithmetic at a finite depth is the arithmetic of piles. A page law (≃): the two sides agree at depth n, and — both being units — so do their logs at the depth for an odd p or a depth n ≥ 2: `[<o>]` is J, and `[o^{p**n - 1}]` is J beside a principal part that vanishes at the depth (at p = 2, depth 1 the pile is `o`, whose log is the period ω₂ where `[<o>]` is J₂: the torsion is invisible mod 2 and visible in the log, the reason [[place.division-by-unit]] and [[place.geometric-doll]] leave that instance out); what the page's equality does not survive in general is a square around a non-unit ([[place.void-pile]]). Chapter 10 of the JP ledger calls the two faces of this *Floor* and *Predecessor*: the pile just below the void pile is the predecessor of nothing.

## Plain

On a clock with p^n hours, going back one hour from midnight lands on the last hour: minus one is a whole pile of hours.

## Derivation

| form | rule | note |
|---|---|---|
| `<o>` | given | minus one; at every place ([[place.ostrowski]]) |
| `<o> o^{p**n}` | [[place.void-pile]] | the void pile adjoined, right to left: it is nothing at depth n — a page step at depth 0 |
| `<o> o o^{p**n - 1}` | medium | one mark set apart from the pile: the same form, [[void.space]] |
| `o^{p**n - 1}` | [[Z.inversion]] | `<o> o` cancels |

## Confirms

−1 = …111 in base 2 and the two's-complement representation of negatives; at every p, −1 = (p−1) + (p−1)p + (p−1)p² + ⋯, the doll with every digit p − 1 ([[place.doll]]). It is **not** a statement about J: `[<o>]` is still J = ω_p/2 at the place ([[place.torsion]]) — the log of this pile has a torsion count, because the pile is the Teichmüller element −1 = g^{(p−1)/2} times a principal unit.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | fails | at ∞ no pile is negative ([[Z.negative-numeral]], [[N.freeness]]) |
| J1 | fails | as classical |
| JH, JO | untested | owed to rung `H` |
| JP | holds | a page step at depth 0 at every instance: the page's equality, ≃ |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | EXACT | the wrapping of the finite clock |
| lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The schema is drawn at p = 2, depth 3: `<o> ≐ ooooooo`, seven marks — 111₂. The JP ledger's *Wrap* theorem is the same law read for any pile: `<o^{k}> ≐ o^{p**n − k}`.
