---
id: mult.consistency
title: The calculus does not collapse
type: theorem
level: meta
kind: law
rung: mult
order: 480
setting: classical
equality: "≐"
domain: positive
law: "with the undefined forms excluded and the seam discipline in force, the laws of rungs void–Q do not prove o ≐ void; in particular distinct piles stay distinct"
units: "the admissible calculus has a model; Peano 3 and 4 survive the arrival of the axioms and of the abstracts of negatives"
holds:
  classical: holds
  J1: untested
  JH: untested
  JO: untested
  JP: untested
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE-BY-DECREE
verified: hand
known_since: "1993 (James, Chapter 5, soundness in ℂ under the J-discipline); the two collapse routes and this scoping: referee passes 2026-10-03"
entered: 2026-10-03
guide: need-led
band: beyond
uses: [mult.c-reading, mult.hole-exclusion, mult.seam-decree, mult.involution, mult.distribution, Z.inversion, N.freeness]
see_also: [mult.dominion-independence, N.induction, Q.reciprocal-of-negative]
aliases: [consistency, soundness, no collapse, Peano 3 and 4 in the full calculus]
concepts: [consistency, natural-number]
understood: partial
understood_note: "I see the two collapse routes and the two decrees; the real/phased split is the part to watch"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `oo ≐ ooo` is **not** derivable from the laws of rungs void–Q, read as admissible derivations | — | the calculus is consistent relative to ℂ |

## Plain

Even after all three axioms arrive, and even once the page can write the logarithm of a negative, it still never confuses two with three — but only because it refuses the two undefined forms and keeps the half-turn rule. Drop either and everything becomes nothing.

## Derivation

| statement | rule | note |
|---|---|---|
| Unphased forms — no angle boundary inside any square — have values in ℝ ∪ {□} in the ℂ reading: piles and `(X)` are positive, `[X]` of a non-negative real is real or □, angles and juxtaposition keep reals real | [[mult.c-reading]] | by induction on the form; □ absorbs by [[mult.hole-exclusion]]'s evaluation rules |
| On real content every axiom is exact: Involution-up and Inversion unconditionally, Distribution unconditionally, Involution-down because the principal log is a two-sided inverse on the real line | [[mult.involution]] [[mult.distribution]] [[Z.inversion]] | — |
| On phased content Involution-down is exact up to a multiple of 2πi, and the seam decree admits it only in an absorbing position — directly under an instance through angles at most — where the instance's exp cancels any multiple of 2πi; so every admissible step preserves the value of the whole form | [[mult.seam-decree]] | the depth-1 argument of the J1 notes, used here as a soundness argument |
| Admissibility — no row contains `<□>` or `[□]`, up to ≐ — keeps the reading total on every row | [[mult.hole-exclusion]] | without it, Route A below collapses the calculus |
| A sound, total reading separates `oo` (value 2) from `ooo` (value 3), so no admissible derivation equates them; this extends [[N.freeness]] from the fragment to all of rungs void–Q | — | — |
| The price: the import of the reading and two decrees. The theorem is NATIVE-BY-DECREE, not NATIVE | — | — |

## Confirms

James's soundness result, scoped exactly: the calculus is consistent *as a calculus of admissible derivations under the J-discipline*, and both devices are hinges, not afterthoughts. It is **not** a proof that the decrees are the weakest possible — the seam decree is over-cautious by design — and it is **not** yet re-established for the enriched settings, each of which changes the reading and the axioms (JH-22 is the JH version: consistency relative to ℍ).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | for rungs void–Q; to be re-checked at rung C, where the phase element is named and the discipline restated |
| J1, JH, JO, JP | untested | each extension changes the reading and the axioms; consistency is re-proved per setting |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| logic | ABSENT | — |
| others | untested | — |

## Refuted readings

- ~~the unrestricted equational theory of the pilot's laws is consistent~~ — refuted 2026-10-03 (first referee pass). Route A: with `[□]` admitted, `W` = `(o [□])` satisfies `W ≐ W (o [C])` by Dominion-under-square and Distribution, so Inversion gives `(o [C]) ≐ void` for every `C`, hence `o ≐ void`.
- ~~Route B needs rung C (a named J)~~ — refuted the same day (second referee pass): `J J = [<o>][<o>]` is writable at rung `mult`; one unguarded unit step gives `J J ≐ void`, and the ℚ sign rules finish the collapse (recorded at [[mult.seam-decree]]). The first draft of this node deferred the guard to rung C; it is needed from rung `mult` on.

## Notes

The engine enforces the undefined-form decree by exception and samples Involution-down only on each node's declared domain; it does **not** yet enforce the seam decree as a rule, and at the branch cut its floating-point log can land on either side (second referee pass, item 5). Two checker obligations follow: refuse any unit step on phased content outside an absorbing position; snap near-real values onto the axis before taking a log. The second is done; the first is owed. A meta-theorem is never `engine`-verified without a witness, and this one has none.
