---
id: C.de-moivre
title: De Moivre — the cube of a turn is the turn tripled
type: theorem
level: object
kind: law
rung: C
order: 1088
setting: classical
equality: "≐"
domain: real
law: "(([[(([J] [T]))]] [ooo])) ≐ (([J] [T] [ooo]))"
units: "(e^{iπt})³ = e^{3iπt}"
gloss_check: "exp(3j*pi*T)"
holds:
  classical: holds
  J1: holds
  JH: guarded
  JO: guarded
  JP: untested
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "De Moivre 1707–1722; Euler 1748 for the exponential form"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.exponentiation, N.numeral, mult.distribution, mult.unit-law, mult.involution, mult.cardinality]
guarded_by: [mult.seam-decree]
see_also: [C.turn-of-sum, mult.exponentiation, C.cube-root-of-unity, N.induction]
aliases: [De Moivre, "(cos θ + i sin θ)^n"]
concepts: [trigonometry, phase, exponentiation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[(([J] [T]))]] [ooo])) ≐ (([J] [T] [ooo]))` | — | (cos πt + i sin πt)³ = cos 3πt + i sin 3πt |

De Moivre's formula for n = 3: raising a turn to a numeral power multiplies its count of J. Through Euler's formula this is (cos θ + i sin θ)³ = cos 3θ + i sin 3θ, for every real θ.

## Plain

Cube a turn and you have turned three times as far. The page proves it by turning the cube into a triple product and adding up the three counts.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[(([J] [T]))]] [ooo]))` | given | the cube of the turn: [[mult.exponentiation]] with exponent 3 ([[N.numeral]]) |
| `(([[(([J] [T]))]] [o]) ([[(([J] [T]))]] [o]) ([[(([J] [T]))]] [o]))` | [[mult.distribution]] | distribute over the three units of the pile, twice |
| `(([[(([J] [T]))]]) ([[(([J] [T]))]]) ([[(([J] [T]))]]))` | [[mult.unit-law]] | `[o] ≐ void`, three times |
| `([(([J] [T]))] [(([J] [T]))] [(([J] [T]))])` | [[mult.involution]] | the counit `([Y]) ≐ Y` with Y = `[X]`, three times: the cube is the triple product |
| `(([J] [T]) ([J] [T]) ([J] [T]))` | [[mult.involution]] | the unit on each `[(([J] [T]))]`, directly inside the instance — absorbing; for |t| > 1 the content is off the strip (guarded by position) |
| `(([([J] [T])] [oo]) ([J] [T]))` | [[mult.cardinality]] | two copies become the count 2 |
| `(([([J] [T])] [oo]) ([([J] [T])] [o]))` | [[mult.unit-law]] | the third gets the count 1, right to left |
| `(([([J] [T])] [ooo]))` | [[mult.distribution]] | collect: the count 3 |
| `(([J] [T] [ooo]))` | [[mult.involution]] | the unit, directly inside the inner instance — absorbing: the turn by 3t |

## Confirms

(cos θ + i sin θ)^n = cos nθ + i sin nθ, at n = 3 and for every real θ — with no principal-branch condition, because the power is unfolded into a product *before* any log is taken: the only unit steps are inside the instance. It is **not** the general law: for a general numeral n the unfolding `(([[X]] [n])) ≐ ([X] … [X])` and the cardinality of n copies are schemas over n, which is the induction gap ([[N.induction]]); each n is a node like this one until then. And it is **not** true for a non-numeral exponent without a condition: `(([[X]] [N]))` with N a real count is X^N in the principal sense, e^{N·Ln X}, which equals the turn by Nt exactly when N(t − τ) is an even integer, τ being t reduced into (−1, 1] — always for integer N (which *is* De Moivre), and for every N when t is already in (−1, 1].

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step directly under an instance |
| JH, JO | guarded | within a slice, as [[C.turn-of-sum]] |
| JP | untested | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Guarded by position (Amendment A2): the units on `[(([J] [T]))]` have content iπt, off the strip for |t| > 1; they sit directly inside the instance — a seam step, admitted by the decree's position clause, so the law carries the decree in its price while its statement is exact in ℂ.
