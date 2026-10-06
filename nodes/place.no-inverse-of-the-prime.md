---
id: place.no-inverse-of-the-prime
title: The prime has no reciprocal at its own place
type: theorem
level: meta
kind: law
rung: place
order: 1440
setting: JP
equality: "≡"
domain: natural
law: "(<[o^{p}]>) is not a form at the place p"
units: "1/p ∉ ℤ_p: the page at p is ℤ_p's, where p is a zero divisor at every finite depth (p · p^{n−1} ≐ void)"
gloss_check: ""
witness: tools/models/place_no_inverse.py
holds:
  classical: replaced
  J1: replaced
  JH: untested
  JO: untested
  JP: holds
readings:
  C: ABSENT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE-BY-DECREE
verified: engine
known_since: "Part II Ch. 10 (No-inverse-of-the-prime); as ℤ_p versus ℚ_p, Hensel 1908"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [Q.reciprocal, place.void-pile, place.prime-log, place.reading]
see_also: [Q.no-division-by-zero, mult.hole-exclusion, place.division-by-unit, place.pole, place.two-ends]
aliases: [no inverse of the prime, 1/p is not a form, zero divisor, the page is ℤ_p]
concepts: [place, division, zero, prime]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(<[o^{p}]>)` is not a form at the place p | the instance of a negative count of `[p]` has no value: p^{−1} is not on the page | ℤ_p is not a field; 1/p ∈ ℚ_p ∖ ℤ_p |

The chart's one exclusion for division is [[Q.no-division-by-zero]]: `(<□>)` is not a form anywhere. A finite place adds one more, and it is not a new kind of exclusion but the same one seen at depth: at depth n the prime is a zero divisor — `([o^{p}] [o^{p**(n-1)}])` is the void pile — so its reciprocal would be a reciprocal of (a divisor of) nothing. The instance of a count of `[p]` is a form only for a whole count ≥ 0 ([[place.reading]]); the mirror of `[p]` is a legitimate *log* (a count of −1), whose instance is not a number. Units, by contrast, always have reciprocals, and the reciprocal is a power ([[place.division-by-unit]]).

## Plain

On a clock with p^n hours you cannot divide by p: p times something is never 1 o'clock, because p times p^{n−1} is midnight.

## Derivation

| statement | rule | note |
|---|---|---|
| `(<[o^{p}]>)` is the shape of 1/p: the instance of the mirror of the log of the prime | [[Q.reciprocal]] | — |
| its content is a count of −1 of `[p]` ([[place.prime-log]]); at depth n the prime is a zero divisor — `([o^{p}] [o^{p**(n-1)}])` is the void pile — so a reciprocal would be a reciprocal of a divisor of nothing | [[place.void-pile]] | p · p^{n−1} ≐ void |
| the reading admits no negative count of `[p]` in an instance: the form has no value at p, at every depth | [[place.reading]] | witness: at p = 2, 3, 5, 7, 13, `(<[o^{p}]>)` has no value; `([o^{p}] [(<[o^{p}]>)])` has none either; every unit's reciprocal is a form |

## Confirms

ℤ_p against ℚ_p: the page is the ring of integers of the place. The numbers with a negative count of `[p]` — the fractions with p in the denominator — are the other end of the page ([[place.two-ends]]): where the pole is a positive count of `[p]` past the depth, these are negative counts, and the page admits neither. It is **not** a limitation of the reading: 1/p has no residue mod p^n for any n.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | replaced | at ∞ every nonzero number has a reciprocal ([[Q.reciprocal-law]]) |
| J1 | replaced | as classical |
| JH, JO | untested | owed |
| JP | holds | witness: the reciprocal of the prime is not a form at any tested place |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | EXACT | ℤ/p^n: p has no inverse |
| lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

Rung `Q`'s "for units" guards on the JP cells of the division laws are this node: a fraction is a form at p when its denominator is a unit ([[place.division-by-unit]]), and `([A] <[A]>)` cancels before any reciprocal is taken, so the self-division laws hold for the prime too.
