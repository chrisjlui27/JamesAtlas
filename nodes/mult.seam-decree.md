---
id: mult.seam-decree
title: The seam discipline
type: decree
level: object
kind: discipline
rung: mult
order: 465
setting: classical
equality: "≐"
domain: positive
law: "DISCIPLINE — the unit step [(X)] → X on a phased X is admissible only in an absorbing position: directly inside an instance boundary, through angle boundaries at most"
units: "log e^z = z only on the principal strip; a 2πi error is harmless exactly where an exp will swallow it"
holds:
  classical: holds
  J1: replaced
  JH: replaced
  JO: replaced
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE-BY-DECREE
verified: hand
known_since: "1993 (James, Ch. 5: the J-discipline — convert [<A>] to [A] J on sight; J-cancellation only inside an instance, last); JH-3 (2026-08) for the semantic seam guard; this syntactic form and the rung-mult collapse route: referee pass 2026-10-03"
entered: 2026-10-03
guide: need-led
band: beyond
uses: [mult.involution, mult.square, Z.angle, N.round, void.space, mult.unit-law, mult.product-of-negatives]
see_also: [mult.hole-exclusion, mult.consistency, Q.reciprocal-of-negative]
aliases: [J-discipline, seam guard, JH-3, Involution-down guard, phase discipline]
concepts: [consistency, logarithm, negation]
understood: partial
understood_note: "the shape is clear; whether 'phased' is the right syntactic signature is the question for rung C"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[(X)] → X` refused when X is *phased* and the redex is not in an absorbing position | — | log e^z = z fails off the principal strip; the failure is a multiple of 2πi, which only an enclosing exp cancels |

**Phased** form: one that contains a square boundary with an angle boundary somewhere inside it — the syntactic signature of the logarithm of a negative, `[<…>]`, whose ℂ value carries iπ. **Absorbing position**: the redex is a member of the multiset directly inside an instance boundary, or inside angle boundaries that are. The counit `([X]) ≐ X` is never restricted; the unit on *unphased* content is never restricted.

## Plain

The box undoes the circle only where the answer could not have been a different turn of the circle. The page may still undo it after a half-turn has crept in, but only right inside another circle, which forgets whole turns.

## Derivation

none — adjoined, as a decree about the unit direction of [[mult.involution]], stated in terms of [[mult.square]], [[Z.angle]], [[N.round]] and position in space [[void.space]]. It is legislated because without it the calculus collapses using only laws already on the chart:

| form | rule | note |
|---|---|---|
| `o` | given | — |
| `([o] [o])` | [[mult.unit-law]] | 1 = 1 × 1, right to left |
| `([<o>] [<o>])` | [[mult.product-of-negatives]] | = (−1)(−1), right to left |

Abstract both sides: `void ≐ [o] ≐ [([<o>] [<o>])]`, and one **unguarded** unit step, `[([<o>][<o>])] → [<o>] [<o>]`, gives `[<o>] [<o>] ≐ void` — James's J-cancellation `J J ≐ void`, whose content is 2πi. From it: `J ≐ <J>` by Inversion; with H = `([J] <[oo]>)` (half of J), cardinality gives `H H ≐ J`, and the ℚ sign rule for a mirrored numerator turns `H ≐ ([H H] <[oo]>) ≐ ([<H H>] <[oo]>)` into `<H>`; so `J ≐ H H ≐ H <H> ≐ void`, `<o> ≐ ([<o>]) ≐ (void) ≐ o`, and `oo ≐ o <o> ≐ void`. Every step but the marked one is exact in ℂ and is a law of rungs ≤ Q. The marked step is refused by this decree: its content is phased and its position (depth 0) is not absorbing.

## Confirms

James's own repair of the "crack" in his calculus (Chapter 5): J-cancellation permitted only inside an instance boundary, and only after other reductions. The chart states it one rung earlier and without naming J, because the collapse can be written as soon as `[<o>]` can — at rung `mult`, before J is a named form. Soundness under the decree is the theorem [[mult.consistency]]: unphased forms have real values, so the unit is exact on them; a phased unit step in an absorbing position is off by a multiple of 2πi, which the enclosing instance kills. JH's seam guard — `[(A)] → A` only when `L(exp V(A)) = V(A)` — is the semantic version of the same rule; this is the syntactic, over-cautious one (it also refuses some sound steps, e.g. on `[<oo> ooo]`, whose value is real).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | this is the classical setting's second decree; James's J-discipline is its special case once J is named |
| J1 | replaced | by the weakened unit `[(A)] ≐ A mod Λ` with receipts: J1 does not refuse the step, it *prices* it — the depth-1 criterion ([[mult.involution]], Notes) says when the price is absorbed |
| JH, JO | replaced | by the semantic seam guard JH-3 |
| JP | holds | the axiom audit at a finite place passed with the discipline in force |

| reading | cell | why |
|---|---|---|
| C | EXACT | the decree is exactly the restriction under which the principal logarithm is a left inverse of exp |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

- ~~the pilot's rungs need no guard on Involution-down; the J-discipline is rung C's business~~ — refuted 2026-10-03 (second referee pass): `J J = [<o>][<o>]` is writable at rung `mult`, and the collapse above uses only rungs ≤ Q.

## Notes

"Phased" is a conservative syntactic approximation to "off the principal strip". Whether it is the *right* signature — whether some sound and needed step is refused by it, or some unsound step slips through — is the first question of rung C, where the phase element is named and the discipline can be restated in James's own terms. The engine does not yet refuse unguarded phased steps; it refuses them only when their 2πi shows in a row's value, which (second referee pass, item 5) it does not always at the branch cut. A checker rule for the decree is owed.
