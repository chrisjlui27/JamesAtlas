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
law: "A ≐ (([p]^{v}) T^{k} ([p][B])) — the three counts of [A] instanced: v copies of [p], k of J_p, and the principal unit, which is the instance of a multiple of p"
units: "a = p^v · τ^k · u, u ∈ 1 + pℤ_p = exp(pℤ_p): the p-adic polar form"
gloss_check: ""
witness: tools/models/place_polar.py
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
known_since: "Hensel 1908; on the page 2026-10-06 (the C.polar-form JP cell asked whether this form reaches it)"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [place.reading, place.prime-log, place.torsion, place.radius]
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
| a number at p is the instance of its three counts: p^v (v copies of `[p]`, instanced), a torsion element (k copies of J_p, instanced), and a principal unit `([p][B])` — the instance of a multiple of p | — | a = p^{v_p(a)} · τ(a) · ⟨a⟩ |

The polar form of ∞ ([[C.polar-form]]) is a modulus and a turn: r·e^{iθ}, the instance of a log that is a real part and a count of J. At a finite place the log is three counts ([[place.reading]]), and so the polar form is three factors: a power of the prime (the size), a root of unity (the phase, [[place.torsion]]) and a principal unit (the instance of a number in the radius, [[place.radius]]) — the part that behaves like a positive real. The chart's rung-C polar form reaches the finite place only for integer turns, where the turn is a torsion power (the ledger); the place's own polar form is this one.

## Plain

Every p-adic number is p to a power, times a root of unity, times something congruent to 1 mod p. Size, phase, and the rest — the rest being where exp and log are honest inverses.

## Derivation

| statement | rule | note |
|---|---|---|
| `[A]` at p is three counts ([[place.reading]]): v of `[p]` ([[place.prime-log]]), k of J_p ([[place.torsion]]), and the log of the principal unit, in the radius ([[place.radius]]) | [[place.reading]] | — |
| the instance of the three is A: p^v times T^k times the instance of a multiple of p — the polar form of the place | [[place.radius]] | witness: random residues at p = 2, 3, 5, 7, 13 split by `[ ]` and reassembled by `( )` come back; the principal unit is the instance of a multiple of p |

## Confirms

ℚ_p^× = p^ℤ × μ_{p−1} × (1 + pℤ_p). It is **not** a modulus: |a|_p = p^{−v} needs the metric rung; here v is a count.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | replaced | [[C.polar-form]] at ∞: modulus and turn |
| J1 | replaced | as classical |
| JH, JO | untested | — |
| JP | holds | witness |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | EXACT | — |
| lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The law's right-hand side is written with the names `[p]^{v}`, `T^{k}` for the counts; it is not an engine law (the counts depend on A), and the node is meta: the witness is its check.
