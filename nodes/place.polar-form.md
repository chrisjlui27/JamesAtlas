---
id: place.polar-form
title: Every number at p is a power of p, a root of unity and a principal unit
type: definition
level: meta
kind: declaration
rung: place
order: 1510
setting: JP
equality: "≡"
domain: complex
law: "A ≐ ([p]^{v} [T]^{k} ([p][B])) — the three counts of [A] instanced together: v copies of [p], k of J_p = [T], and the log of the principal unit, a multiple of p (of 4 at p = 2: ([oooo][B]))"
units: "a = p^v · τ^k · u, u ∈ exp(pℤ_p) = 1 + pℤ_p at odd p; at 2, u ∈ exp(4ℤ_2) = 1 + 4ℤ_2 and τ ∈ {±1}: the p-adic polar form"
gloss_check: ""
witness: tools/models/place_polar.py
holds:
  classical: replaced
  J1: replaced
  JH: replaced
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
known_since: "Hensel 1908; on the page 2026-10-06 (the C.polar-form JP cell asked whether this form reaches it)"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [place.reading, place.prime-log, place.torsion, place.radius, place.void-pile]
see_also: [C.polar-form, C.modulus, place.reading, place.teichmuller]
aliases: [the polar form at p, p-adic polar decomposition, valuation · torsion · principal unit, the three counts instanced]
concepts: [place, logarithm, phase, one]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| a number at p is the instance of its three counts at once: `([p]^{v} [T]^{k} ([p][B]))` — v copies of `[p]`, k of the torsion log `[T]`, and `([p][B])`, a multiple of p, whose instance is the principal unit (at p = 2 the multiple is of 4, `([oooo][B])`, and T = −1) | — | a = p^{v_p(a)} · τ(a) · ⟨a⟩ |

The polar form of ∞ ([[C.polar-form]]) is a modulus and a turn: r·e^{iθ}, the instance of a log that is a real part and a count of J. At a finite place the log is three counts ([[place.reading]]), and so the polar form is three factors: a power of the prime (the size), a root of unity (the phase, [[place.torsion]]) and a principal unit (the instance of a number in the radius, [[place.radius]]) — the part that behaves like a positive real. The radius is pℤ_p at an odd place and 4ℤ_2 at 2, so the principal unit is exp of a multiple of p — of 4 at 2, where 1 + 2ℤ_2 is ±1 times exp(4ℤ_2) and the torsion sign carries the rest. The chart's rung-C polar form reaches the finite place only for integer turns, where the turn is a torsion power (the ledger); the place's own polar form is this one.

## Plain

Every p-adic number is p to a power, times a root of unity, times something congruent to 1 mod p. Size, phase, and the rest — the rest being where exp and log are honest inverses.

## Derivation

| statement | rule | note |
|---|---|---|
| `[A]` at p is three counts ([[place.reading]]): v of `[p]` ([[place.prime-log]]), k of J_p ([[place.torsion]]), and the log of the principal unit, in the radius ([[place.radius]]) | [[place.reading]] | on the page the void pile declares ([[place.void-pile]]), the decree the definition rests on |
| the instance of the three is A: `([p]^{v} [T]^{k} ([p][B]))` — p^v times T^k times the instance of a multiple of p (of 4 at 2) — the polar form of the place | [[place.radius]] | witness: random residues at p = 2, 3, 5, 7, 13 split by `[ ]` and reassembled by `( )` come back; the form `([p]^{v} [T]^{k} ([p][B]))` evaluates to p^v·τ^k·exp(pB) with the three counts of A, and the principal unit is the instance of a multiple of p |

## Confirms

ℚ_p^× = p^ℤ × μ_{p−1} × (1 + pℤ_p). It is **not** a modulus: |a|_p = p^{−v} needs the metric rung; here v is a count.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | replaced | [[C.polar-form]] at ∞: modulus and turn |
| J1 | replaced | as classical |
| JO | untested | — |
| JH | replaced | at 2 by a power of π, a Hurwitz unit and a principal unit in half-shells ([[H.ramified-place]]); at odd p by the matrix decomposition ([[H.split-place]]); the quaternionic polar form at ∞ is [[H.polar-form]] |
| JP | holds | witness |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | EXACT | — |
| lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The law's right-hand side is written with the names `[p]^{v}`, `[T]^{k}` for the counts (`[T]` = J_p); it is not an engine law (the counts depend on A), and the node is meta: the witness is its check, and it evaluates the right-hand side as a form at each place.
