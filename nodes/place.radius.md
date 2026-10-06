---
id: place.radius
title: The instance has a radius
type: schema
level: object
kind: law
rung: place
order: 1480
setting: JP
equality: "≡"
domain: natural
law: "(o^{p}) is a form at the place p"
units: "e^p ∈ ℤ_p: exp converges on p·ℤ_p (on 4ℤ_2 at p = 2) and nowhere else — e itself is not p-adic, so (o) is not a form at any finite place"
gloss_check: ""
witness: tools/models/place_radius.py
schema_range: "p=3,5,7,13"
schema_draw: "p=3"
holds:
  classical: replaced
  J1: replaced
  JH: untested
  JO: untested
  JP: holds
readings:
  C: ABSENT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE-BY-SCHEMA
verified: engine
known_since: "2026-09-13 (Forms at Every Place: 'the radius of ( ) — the evaluable part in ℤ_p'); the convergence of the p-adic exponential, Hensel 1908"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [N.round, place.reading, place.void-pile]
see_also: [alg.base, alg.exp-of-pile, place.reading, place.polar-form, place.selection]
aliases: [the radius of the instance, e is not p-adic, exp converges on pℤ_p, the radius of ( )]
concepts: [place, instance, one]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(o^{p})` is a form at the place p | the instance of the pile of p marks has a value at p: e^p is p-adic | exp(x) converges for v_p(x) ≥ 1 (v_2(x) ≥ 2 at p = 2) |

At ∞ the instance of anything is a number: `(o)` is e, `(oo)` is e², `((o))` is e^e ([[alg.base]]). At a finite place the instance converges only on a disc, the **radius**: the content must be divisible by p (by 4 at p = 2). So e is not p-adic, `(o)` is not a form at any finite place, and the chart's base laws ([[alg.base]], [[alg.log-of-base]], [[alg.power-of-base]], [[alg.exp-of-pile]]) are replaced at p by this one: *the instance of a multiple of p is a number*. The law is drawn for the pile of p marks; the witness extends it to the whole radius and checks the exclusion at every tested place. The radius is the third place-datum, and like the other two it follows from the void pile ([[place.reading]]): the series for exp converges where the terms shrink, and they shrink where the content is divisible by the prime.

## Plain

At a finite place e^x only makes sense when x is a multiple of p. So e^p is a p-adic number and e is not. Every circle on the page has to hold a multiple of p, or it holds nothing.

## Derivation

| statement | rule | note |
|---|---|---|
| **A fact of the reading.** `(o^{p})` is the instance ([[N.round]]) of the pile of p marks; the series for exp converges where its terms shrink, and at p they shrink exactly when the content is divisible by p (by 4 at 2) — because the void pile ([[place.void-pile]]) swallows the tail | [[place.reading]] | the engine evaluates `(o^{p})` at each instance; the witness checks that `(o)`, `(oo)`, `((o))` have no value at p = 2, 3, 5, 7, 13, that `(o^{p} A)` is a form for every A in the radius, and that `(oooo)` is a form at 2 where `(oo)` is not |

## Confirms

The domain of the p-adic exponential and the fact that ℚ_p is not ℝ: no number plays e's part. It is **not** the radius of the *log*: the log converges on the principal units 1 + pℤ_p, which is exp's image, so on that sector the two are inverse — the sector the chart's `positive` variables are read in at a place (SPEC §4.4).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | replaced | at ∞ every instance is a number: [[N.round]] |
| J1 | replaced | as classical |
| JH, JO | untested | owed |
| JP | holds | at p = 3, 5, 7, 13 (the schema) and, by the witness, 2 |

| reading | cell | why |
|---|---|---|
| C | ABSENT | exp is entire on ℂ |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The schema does not run at p = 2, where the radius is 4ℤ_2 and `(oo)` is *not* a form: the witness checks `(oooo)` there. The standing proviso for every instance at a finite place — its content on the radius — is what the place ledger retries a sample for before calling a law formless (SPEC §4.4).
