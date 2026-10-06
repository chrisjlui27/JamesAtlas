---
id: alg.base
title: The base
type: definition
level: object
kind: law
rung: alg
order: 700
setting: classical
equality: ≐
domain: natural
law: "e := (o)"
units: e = e^1 = 2.71828…
gloss_check: e
forms: [(o), (<o>), <(o)>, (o) o]
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: replaced
readings:
  C: EXACT
  finset: PARTIAL
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James): 'e is simply (o)'; Bernoulli 1683 for the constant, Euler 1731 for the letter"
entered: 2026-10-03
guide: shape-led
band: 9–12
uses: [N.round, N.unit]
see_also: [alg.exp-of-pile, alg.exp-law, mult.square]
aliases: [e, "Euler's number", (o), the base of the exponential]
concepts: [exponential, constant]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(o)` | — | e |

The circle around one circle. Until now the base of the round boundary was unconstrained — nothing in rungs ℕ through ℚ depended on it. Here it is named: the instance of the unit is the base, and `(o o)` is e², `(<o>)` is 1/e, `<(o)>` is −e, `(o) o` is e + 1 — the first constants the calculus writes that are not rational.

## Plain

A circle around a circle is the number e — the first number on the page that no fraction can name.

## Derivation

| form | rule | note |
|---|---|---|
| `(o)` | [[N.round]] | the round boundary around the unit, [[N.unit]] |
| `e` | name | — |

## Confirms

e as e^1, the value the exponential takes at the unit. What this does **not** do is *constrain* the base: the three axioms never mention a value for `(o)` — read with `(A) = b^A` and `[A] = log_b A`, every object-level law of the chart holds for any base b > 0, b ≠ 1 (checked for b = 2, 10, ½ by the alg referee pass), so the calculus cannot even refute `e ≐ oo`: in the base-2 reading `(o)` and `oo` have the same value. Where the classical *setting* does commit to e is the ℂ reading it imports ([[mult.c-reading]], `(A) = e^A`) and the seam decree that inherits it, whose strip (−π, π] is base e's. Whether the rules determine every true identity of exp and log is a different question, the exp–log completeness question of the `analysis` rung. Transcendence of e (Hermite 1873) is an import the calculus cannot state ([[alg.irrationality]] is the simpler version of the same gap).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1, JH, JO | holds | — |
| JP | replaced | `(o)` = e is not a form at any finite place: the instance has a radius there, p·ℤ_p (4ℤ_2 at p = 2), and 1 lies outside it ([[place.radius]]) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | PARTIAL | the exponential of a one-point set in the Sym reading is the free commutative monoid on one generator — ℕ itself; the reading in which `(o)` is "e" and the reading in which it is "ℕ" are the two ends of the chart meeting (the re-entry edge, not yet laid) |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

James, p. 47 and p. 50: "The base of these operations is not constrained by the calculus … An equality could be introduced that defined this to be non-transcendental, such as base two with the definition `(o) ≐ oo`. Everything in the calculus would still hold as none of it is dependent on this value." — the chart's base finding, in his words; `(o)` is his e (p. 48, glossary p. 63), "incommensurable with any other boundary construction".

The census's size-3 constants `(<o>)` (1/e) and `<(o)>` (−e) are the chart's smallest illustration of the JH Depth Principle: the same two boundaries, nested the other way, name different numbers. Both are assigned to this node; `(o) o` likewise.
