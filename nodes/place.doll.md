---
id: place.doll
title: A pile is a digit beside a shell
type: schema
level: object
kind: law
rung: place
order: 1470
setting: JP
equality: "≃"
domain: natural
law: "o^{k + p*j} ≃ o^{k} ([o^{p}] [o^{j}])"
units: "k + p·m: the base-p expansion begins — the digit k outside, the rest m one shell in; iterated, the doll a₀ + p(a₁ + p(a₂ + ⋯))"
gloss_check: ""
schema_range: "p=2,3,5; k=0..p-1; j=1..3"
schema_draw: "p=2; k=1; j=3"
holds:
  classical: holds
  J1: holds
  JH: untested
  JO: untested
  JP: holds
readings:
  C: EXACT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE-BY-SCHEMA
verified: engine
known_since: "2026-09-13 (the doll: nesting read as shrinking — closeness is shared shells, □ the doll with no pile); James 1993 Appendix (number formats, place value); Hensel 1897 (p-adic digits)"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [schema.cardinality, void.space, place.ostrowski]
see_also: [N.numeral, place.residue, place.geometric-doll, place.prime-log, place.completion]
aliases: [the doll, base-p digits, place value at p, shells, Horner form, number formats]
concepts: [place, numeral, one]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `o^{k + p*j} ≃ o^{k} ([o^{p}] [o^{j}])` | a pile of k + pj marks is k marks beside the product p·j — the first shell of the doll (≃: the cardinality step's receipts are absorbed, as at ∞) | k + p·j, the start of the base-p expansion |

The place-value form of a number at p: a digit k (fewer than p marks) outside, and the rest, j, one shell deeper, multiplied by the prime. Iterate on j and the number becomes a **doll** — `a₀ ([p][a₁ ([p][a₂ ([p][⋯])])])` — nested shells each holding a digit, the innermost the most significant. The doll is the chart's picture of what the place *means*: nesting read as shrinking. Two numbers are close at p when their dolls share their outer shells; the void pile is a doll whose first n shells are empty ([[place.void-pile]]); the valuation is the number of empty shells outside ([[place.prime-log]]). The law is true at every place including ∞ — it is only arithmetic — but it is at a finite place that it is the *normal form* ([[N.numeral]]'s pile of marks is a doll of one shell).

## Plain

Write a number in base p: the last digit, then p times the rest. Keep going and you get a nest of boxes, each holding one digit — a doll. At a finite place the nest is the number.

## Derivation

| form | rule | note |
|---|---|---|
| `o^{k + p*j}` | given | k + pj marks; at every place ([[place.ostrowski]]) |
| `o^{k} o^{p*j}` | medium | the digit set apart: the same pile, [[void.space]] |
| `o^{k} ([o^{p}] [o^{j}])` | [[schema.cardinality]] | the pj marks are j copies of the pile of p marks: cardinality, right to left, at count j |

## Confirms

Base-p positional notation, James's own number formats (the thesis's Appendix A.3, p. 70: a numeral in any base is a nest of products), and the p-adic digits of Hensel. It is **not** yet the infinite doll: a finite form has finitely many shells, and the limit — the doll with a shell at every depth, ℤ_p — is the gap [[place.completion]]. It is **not** canonical either: the law allows k ≥ p, and the carry (p marks in one shell are one mark in the next) is the law read at k = p.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | arithmetic: k + pm is k + pm at every place |
| J1 | holds | as classical; the cardinality step's receipts are absorbed |
| JH, JO | untested | — |
| JP | holds | the cardinality step's receipts are absorbed, as at ∞ (the tape inherits [[schema.cardinality]]'s); at p this is the normal form |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | EXACT | — |
| lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The schema runs over the digit k = 0 … p − 1 and the rest j = 1 … 3 at p = 2, 3, 5; at k = 0 the law reads `o^{p*j} ≐ ([o^{p}] [o^{j}])`, the carry alone. Drawn at p = 2: 7 = 1 + 2·3.
