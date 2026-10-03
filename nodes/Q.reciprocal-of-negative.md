---
id: Q.reciprocal-of-negative
title: The reciprocal of a negative is the negative of the reciprocal
type: theorem
level: object
kind: law
rung: Q
order: 622
setting: classical
equality: ≐
domain: positive
law: "(<[<A>]>) ≐ <(<[A]>)>"
units: 1/(−a) = −(1/a)
gloss_check: -1/A
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE-BY-DECREE
verified: engine
known_since: 1993 (James); the fact is ancient; the seam-crossing noted here 2026-10-03
entered: 2026-10-03
guide: need-led
band: 6–8
uses: [Q.reciprocal, mult.multiplication, mult.product-of-negatives, Q.reciprocal-law, mult.involution, Z.inversion, N.unit, mult.unit-law, void.space, mult.seam-decree]
see_also: [Q.negative-denominator, Q.negative-fraction, mult.involution]
aliases: [1/(−a) = −(1/a), sign of a reciprocal]
concepts: [inverse, negation]
understood: partial
understood_note: the seam steps are the part I want to watch at rung C
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(<[<A>]>) ≐ <(<[A]>)>` | — | 1/(−a) = −(1/a) |

The first law of the chart whose derivation crosses the **seam**: `[<A>]`, the abstract of a negative, is ln a + iπ in the ℂ reading, and the unit `[(X)] ≐ X` applied to content carrying it is exact only up to the period 2πi. Three such steps occur below; each sits in an absorbing position, so the seam decree ([[mult.seam-decree]]) admits it and the enclosing instance cancels the period. No seam-free classical derivation is known; James's own route is through the phase rule `[<A>] ≐ [A] J` at rung C, which relocates the one unavoidable crossing to a J-cancellation inside the instance — exactly where his discipline permits it.

## Plain

One over minus-a is minus one-over-a. The page can show it, but only by passing through the place where "the log of a negative" lives — which is where the imaginary numbers are about to come from.

## Derivation

First, `<(<[A]>)>` is an inverse of `<A>`:

| form | rule | note |
|---|---|---|
| `([<A>] [<(<[A]>)>])` | given | (−a) × (−(1/a)), [[mult.multiplication]] |
| `([A] [(<[A]>)])` | [[mult.product-of-negatives]] | two mirrors cancel across the product |
| `o` | [[Q.reciprocal-law]] | a × (1/a) = 1 |

Second, `(<[<A>]>)` is an inverse of `<A>`:

| form | rule | note |
|---|---|---|
| `([<A>] [(<[<A>]>)])` | given | (−a) × (1/(−a)), [[Q.reciprocal]] |
| `([<A>] <[<A>]>)` | [[mult.involution]] | `[(X)] ≐ X` with X = `<[<A>]>` — phased content, absorbing position: admitted by [[mult.seam-decree]] (seam step 1) |
| `(void)` | [[Z.inversion]] | `[<A>] <[<A>]>` cancels |
| `o` | [[N.unit]] | — |

Inverses are unique:

| form | rule | note |
|---|---|---|
| `(<[<A>]>)` | given | X, the left-hand side |
| `([(<[<A>]>)] [o])` | [[mult.unit-law]] | X × 1, right to left |
| `([(<[<A>]>)] [([<A>] [<(<[A]>)>])])` | lemma | 1 ≐ (−a) × (−(1/a)), the first table right to left |
| `([(<[<A>]>)] [<A>] [<(<[A]>)>])` | [[mult.involution]] | `[(Z)] ≐ Z` on the inner product — Z = `[<A>] [<(<[A]>)>]` has value 2πi, so this is seam step 2, absorbing position; regroup by [[void.space]] |
| `([([(<[<A>]>)] [<A>])] [<(<[A]>)>])` | [[mult.involution]] | `Z ≐ [(Z)]` on `[X][<A>]` (value 2πi), right to left — seam step 3, absorbing position |
| `([o] [<(<[A]>)>])` | lemma | X × (−a) ≐ 1, the second table |
| `<(<[A]>)>` | [[mult.unit-law]] | 1 × Y = Y |

## Confirms

(−a)⁻¹ = −a⁻¹, by uniqueness of inverses, as in any field. What the chart adds is the *price*: three of the steps are the unit on content off the principal strip, admitted only by the seam decree — so the law is NATIVE-BY-DECREE, the first sign law to cost a decree. In J1 the same three steps post receipts of ±2πi, and the law holds exactly by the depth-1 criterion; these are the first ℚ laws whose receipts do not vanish. The engine passes every row because it evaluates whole rows: the periods cancel inside the instance.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | under the seam decree, which admits the three marked steps |
| J1 | holds | exact by the depth-1 criterion ([[mult.involution]], Notes); the three receipts are ±2πi — the first ℚ law whose receipts do not vanish |
| JH, JO | holds | the Inversion cluster plus guarded Involution; the semantic seam guard JH-3 blocks the three marked steps and the route is through the left-inverse theorem |
| JP | guarded | for units |

| reading | cell | why |
|---|---|---|
| C | EXACT | the law is exact on ℂ×; the three seam steps are exact only mod 2πi |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The three seam steps, in the ℂ reading: (1) `[(<[<A>]>)]` has value −ln a + iπ while `<[<A>]>` has value −ln a − iπ; (2) `[(Z)]` with Z = `[<A>][<(<[A]>)>]` has value 0 while Z has value 2πi; (3) `[X][<A>]` sums to 2πi while `[([X][<A>])]` is 0. Each difference is the period. Tagged *need-led*: nothing in the shape of the forms asks for this law; the sign rules of fractions ([[Q.negative-denominator]]) do, and the shape answers by pointing at the seam.
