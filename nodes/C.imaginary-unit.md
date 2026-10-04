---
id: C.imaginary-unit
title: i is half of J, instanced
type: definition
level: object
kind: law
rung: C
order: 990
setting: classical
equality: "≐"
domain: positive
law: "i := (([J] <[oo]>))"
units: "i = e^{iπ/2}"
gloss_check: "1j"
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James: i as a fractional count of J); Euler 1748 for e^{iπ/2} = i"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [Q.division, mult.cardinality, C.phase, N.numeral, N.round]
see_also: [C.i-squared, Q.half, Q.fractional-cardinality, C.pi]
aliases: [i, imaginary unit, "√−1", quarter turn, "e^{iπ/2}"]
concepts: [phase, complex-number, constant]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([J] <[oo]>))` | `i` | e^{iπ/2} = i |

Half of J — the phase element with the count ½ — circled. A quarter turn. Nothing is adjoined: i is a form the calculus could write at rung `Q`, read here.

## Plain

Half of the log of minus one, circled, is i: a quarter of a turn. Two of them make the half-turn that is minus one — which is the next law, not this one.

## Derivation

| form | rule | note |
|---|---|---|
| `(([J] <[oo]>))` | [[Q.division]] | the instance ([[N.round]]) of J ÷ 2 — `([A] <[B]>)` with A = J ([[C.phase]]) and B the pile `oo` ([[N.numeral]]); a fractional count of J in the sense of [[mult.cardinality]] |
| `i` | name | — |

## Confirms

i = e^{iπ/2}, which is how i is *found* once J is: James's reading of i as "half of J". It is **not** a definition of i as "the square root of −1": that i squares to −1 is the theorem [[C.i-squared]], and the other square root is the mirror `<(([J] <[oo]>))>` = e^{−iπ/2}, which the calculus does not confuse with this one. Nor is anything new adjoined to the calculus to admit i — the ℂ reading was already the model at rung `mult`, as the consistency theorem shows; this rung only *reads* forms that were already writable.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | `([J] <[oo]>)` is the quarter-period ω/4; the definition takes no Λ-step |
| JH, JO | replaced | one i per slice: `(([J_u] <[oo]>))` = u, so "i" is the 2-sphere of unit imaginary directions, not a point (JH Ch. 14) |
| JP | guarded | the count 2 must be a unit at p (odd p), and whether `(([J_p] <[oo]>))` is a value at p is the wall criterion; the classical fact to check it against is that ℚ_p contains i exactly when p ≡ 1 (mod 4) |

| reading | cell | why |
|---|---|---|
| C | EXACT | the principal e^{iπ/2} |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

James, §6.2.3 p. 46: "Interpreting (([J]<[oo]>)) as i reveals the oscillation function to be a multiplication by i"; glossary p. 63: "i — a complex number formed with a half cardinality of J". His route to i is the four-step oscillation `o → ((…)) → (J) → … `, i.e. the powers of i.

The form has 10 boundaries. In the census it is the first of the fractional counts of J; the n-th roots of unity and of −1 are the others ([[C.cube-root-of-negation]], [[C.cube-root-of-unity]]).
