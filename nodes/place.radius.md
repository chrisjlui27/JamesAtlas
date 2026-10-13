---
id: place.radius
title: The instance has a radius
type: theorem
level: meta
kind: law
rung: place
order: 1480
setting: JP
equality: "≡"
domain: natural
law: "(o^{p}) is a form at the place p for odd p, and (oooo) at p = 2: the instance converges on p·ℤ_p (4ℤ_2 at 2) and nowhere else"
units: "e^p ∈ ℤ_p for odd p, e^4 ∈ ℤ_2: exp converges on p·ℤ_p (on 4ℤ_2 at p = 2) and nowhere else — e itself is not p-adic, so (o) is not a form at any finite place"
gloss_check: ""
witness: tools/models/place_radius.py
holds:
  classical: replaced
  J1: replaced
  JH: replaced
  JO: untested
  JP: holds
readings:
  C: ABSENT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
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

| statement | units | standard |
|---|---|---|
| `(o^{p})` is a form at an odd place p, and `(oooo)` at p = 2; `(o)` is a form at no finite place | the instance of a multiple of p has a value at p (of a multiple of 4 at 2): e^p is p-adic for odd p, e^4 is 2-adic, e is neither | exp(x) converges for v_p(x) ≥ 1 (v_2(x) ≥ 2 at p = 2) and for no other x |

At ∞ the instance of anything is a number: `(o)` is e, `(oo)` is e², `((o))` is e^e ([[alg.base]]). At a finite place the instance converges only on a disc, the **radius**: the content must be divisible by p (by 4 at p = 2). So e is not p-adic, `(o)` is not a form at any finite place — nor is `(oo)` at 2 — and the chart's base laws ([[alg.base]], [[alg.log-of-base]], [[alg.power-of-base]], [[alg.exp-of-pile]]) are replaced at p by this one: *the instance of a multiple of p (of 4 at 2) is a number*. The radius is the third place-datum, and like the other two it is a fact of the reading ([[place.reading]], the import that reads the page the void pile declares): the series for exp converges where its terms shrink, and they shrink where the content is divisible by the prime — by 4 at 2, where the denominators of the series carry an extra power of 2.

## Plain

At a finite place e^x only makes sense when x is a multiple of p (of 4 at the place 2). So e^p is a p-adic number and e is not: every circle on the page holds a multiple of p, or nothing.

## Derivation

| statement | rule | note |
|---|---|---|
| **A fact of the reading.** `(o^{p})` is the instance ([[N.round]]) of the pile of p marks; the series for exp converges where its terms shrink, and at p they shrink exactly when the content is divisible by p (by 4 at 2), because the void pile ([[place.void-pile]]) swallows the tail of a series whose terms gain a shell each | [[place.reading]] | the witness checks, at p = 2, 3, 5, 7, 13, that `(o)`, `(oo)`, `((o))` have no value; that `(o^{p} A)` is a form for every A in the radius (`(oooo A)` at 2); and that `(oooo)` is a form at 2 where `(oo)` is not |

## Confirms

The domain of the p-adic exponential and the fact that ℚ_p is not ℝ: no number plays e's part. It is **not** the radius of the *log*: the log converges on every unit — on the principal units 1 + pℤ_p (1 + 4ℤ_2 at 2), which are exp's image, the two are inverse, and that sector is the one the chart's `positive` variables are read in at a place (SPEC §4.4).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | replaced | at ∞ every instance is a number: [[N.round]] |
| J1 | replaced | as classical |
| JO | untested | owed |
| JH | replaced | at 2 the radius of the instance is the half-shell v ≥ 3/2, the series converging where it does not at v = 1 ([[H.ramified-place]], witness part (3)); at odd p v ≥ 1 as on the centre |
| JP | holds | witness, at p = 2, 3, 5, 7, 13 |

| reading | cell | why |
|---|---|---|
| C | ABSENT | exp is entire on ℂ |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

A meta theorem of the reading, with a witness (`tools/models/place_radius.py`): the engine's instance refuses a content outside the radius at every tested place, and the radius is 4ℤ_2 at p = 2. The standing proviso for every instance at a finite place — its content on the radius — is what the place ledger retries a sample for, and otherwise drops rather than judges (SPEC §4.4).
