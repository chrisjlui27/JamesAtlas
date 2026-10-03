---
id: mult.consistency
title: The pilot calculus does not collapse
type: theorem
level: meta
kind: law
rung: mult
order: 480
setting: classical
equality: "≐"
domain: positive
law: "with the undefined forms excluded, the laws of rungs void–mult do not prove o ≐ void; in particular distinct piles stay distinct"
units: "the calculus has a model; Peano 3 and 4 survive the arrival of the axioms"
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
known_since: "1993 (James, Chapter 5, soundness in ℂ); the two collapse routes that make the decree load-bearing: referee pass 2026-10-03"
entered: 2026-10-03
guide: need-led
band: beyond
uses: [mult.c-reading, mult.hole-exclusion, mult.involution, mult.distribution, Z.inversion, N.freeness]
see_also: [mult.dominion-independence, N.induction]
aliases: [consistency, soundness, no collapse, Peano 3 and 4 in the full calculus]
concepts: [consistency, natural-number]
understood: partial
understood_note: "I see the two collapse routes; the status of Involution-down beyond the pilot is the part I want to watch at rung C"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `oo ≐ ooo` is **not** derivable from the laws of rungs void, N, Z, mult, read as admissible derivations | — | the calculus is consistent relative to ℂ |

## Plain

Even after all three axioms arrive, the page still never confuses two with three — but only because it refuses the two undefined forms. Allow either of them and everything becomes nothing.

## Derivation

| statement | rule | note |
|---|---|---|
| Every axiom and theorem of the pilot, instantiated on admissible forms with real positive content, holds in the ℂ reading | [[mult.c-reading]] | Involution-up and Inversion unconditionally; Distribution unconditionally; Involution-down on the principal strip, which contains all real positive content; the engine samples each |
| Admissibility — no row contains `<□>` or `[□]`, up to ≐ — is the decree | [[mult.hole-exclusion]] | without it, two derivations collapse the calculus (recorded there and under Refuted readings below) |
| A sound, total reading separates `oo` (value 2) from `ooo` (value 3) | — | so no admissible derivation equates them; this extends [[N.freeness]] from the fragment to the full pilot |
| The import is genuine: nothing in the forms constructs the reading | [[mult.involution]] [[mult.distribution]] [[Z.inversion]] | the price of this theorem is the import plus the decree — it is NATIVE-BY-DECREE, not NATIVE |

## Confirms

James's soundness result, scoped exactly: the calculus is consistent *as a calculus of admissible forms*, and the two undefined forms are not an afterthought but the hinge. Beyond the pilot, at rung C, the content stops being real-positive, Involution-down leaves the principal strip (`[(J J)] ≐ J J` would give `J J ≐ void` and then, through `[J J] ≐ □`, a second collapse), and James's **J-discipline** — convert `[<A>]` to `[A] J` on sight; J-cancellation only inside an instance, last — becomes the next load-bearing decree. The chart will state it there and recompute this theorem's price.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | for the pilot rungs; to be re-established at rung C with the J-discipline |
| J1, JH, JO, JP | untested | each extension changes the reading and the axioms; consistency is re-proved per setting (JH-22 is the JH version: consistency relative to ℍ) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| logic | ABSENT | — |
| others | untested | — |

## Refuted readings

- ~~the unrestricted equational theory of the pilot's laws is consistent~~ — refuted 2026-10-03 (referee pass). Route A: with `[□]` admitted, `W` = `(o [□])` satisfies `W ≐ W (o [C])` by Dominion-under-square and Distribution, so Inversion gives `(o [C]) ≐ void` for every `C`, hence `o ≐ void`. Route B (needs rung C): Involution-down at `J J` gives James's J-cancellation `J J ≐ void`, then `[J J] ≐ □`, Dominion and Inversion on `[J J]` give `A ≐ void` for every `A`. Both are blocked by the decree read up to ≐, and B additionally by the J-discipline.

## Notes

The engine enforces the decree by exception (`Undefined`, `Excluded`) and samples Involution-down only on the node's declared domain; that is why the collapse routes were invisible to it. A meta-theorem is never `engine`-verified without a witness script, and this one has none yet: the obligation is a checker that walks a derivation and refuses any row whose value is □ under a mirror or a square — which `tools/forms.py` already does per step, but not as a stated rule.
