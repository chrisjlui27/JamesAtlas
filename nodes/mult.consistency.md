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
law: "with the undefined forms excluded and the seam discipline in force, the laws of rungs void–alg do not prove o ≐ void; in particular distinct piles stay distinct"
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
verified: engine
witness: tools/models/consistency_check.py
known_since: "1993 (James, Chapter 5, soundness in ℂ under the J-discipline); the two collapse routes and this scoping: referee passes 2026-10-03"
entered: 2026-10-03
guide: need-led
band: beyond
uses: [mult.c-reading, mult.hole-exclusion, mult.seam-decree, mult.involution, mult.distribution, Z.inversion, N.freeness]
see_also: [mult.dominion-independence, mult.seam-signature, N.induction, Q.reciprocal-of-negative]
aliases: [consistency, soundness, no collapse, Peano 3 and 4 in the full calculus]
concepts: [consistency, natural-number]
understood: partial
understood_note: "I see the two collapse routes and the two decrees; the real/phased split is the part to watch"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `oo ≐ ooo` is **not** derivable from the laws of rungs void–alg, read as admissible derivations | — | the calculus is consistent relative to ℂ |

## Plain

Even after all three axioms arrive, the page still never confuses two with three — but only because it refuses the two undefined forms and keeps the half-turn rule, which it cannot state without help. Drop either and everything becomes nothing.

## Derivation

| statement | rule | note |
|---|---|---|
| In the ℂ reading every rule except the unit is exact for *all* values: the counit `([X]) ≐ X` (exp ∘ log = id on ℂ×), Distribution, Inversion, and the black-hole rules | [[mult.c-reading]] [[mult.involution]] [[mult.distribution]] [[Z.inversion]] | identities of complex arithmetic; sampled by the witness |
| The unit `[(X)] ≐ X` is exact when X is on the principal strip, and off the strip it errs by a multiple of 2πi | [[mult.involution]] | the definition of the principal logarithm |
| The seam decree admits the unit only on the strip or in an absorbing position, where the enclosing instance's exp cancels any multiple of 2πi; so every admissible step preserves the value of the whole form | [[mult.seam-decree]] | the decree is semantic — it is stated in the reading — which is the gap `mult.seam-signature` |
| Admissibility — no row contains `<□>` or `[□]`, up to ≐ — keeps the reading total on every row | [[mult.hole-exclusion]] | without it, Route A below collapses the calculus |
| A sound, total reading separates `oo` (value 2) from `ooo` (value 3), so no admissible derivation equates them; this extends [[N.freeness]] from the fragment to all of rungs void–alg | — | — |
| The price: the import of the reading and two decrees, one of which is itself stated in the import. NATIVE-BY-DECREE, not NATIVE | — | — |

## Confirms

Two cautions the argument needs. The guard covers the unit in **both** orientations (`[(X)] ≐ X` is false off the strip either way). And the admissible calculus is not substitution-closed: a derived schema such as [[alg.log-law]] is admissible only on the domain where its own derivation is — instantiated at A = B = `<o>` it *is* the collapse step — so a law may be cited only inside its declared domain; the engine re-evaluates every row, which is how it catches a bad instantiation.


James's soundness result, scoped exactly: the calculus is consistent *as a calculus of admissible derivations under the J-discipline*, and both devices are hinges, not afterthoughts. Once the unit is guarded, soundness is immediate — every other rule is an identity of complex arithmetic — so the whole weight of consistency rests on a guard the calculus cannot state in its own terms. It is **not** yet re-established for the enriched settings, each of which changes the reading and the axioms (JH-22 is the JH version: consistency relative to ℍ).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | for rungs void–alg; to be re-checked at rung C, where the phase element is named and the discipline restated |
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

The engine enforces the undefined-form decree by exception and the seam decree as a rule (`check_seam`: every unit step's content is evaluated on the node's sampled domain and refused off the strip outside an absorbing position); near-real values are snapped onto the axis before a log so the branch cut is not decided by rounding. The witness `tools/models/consistency_check.py` is a property test of the lemmas — the exactness of the other rules on complex content, absorption in absorbing positions, non-vacuity of the decree, separation of piles — not a proof; the `engine` tier here means that much and no more. Its first run refuted the syntactic signature (`[[[oo]]]`), which is how [[mult.seam-signature]] came to exist.
