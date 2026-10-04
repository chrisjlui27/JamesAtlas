---
id: mult.seam-signature
title: A native signature for the seam
type: gap
level: meta
kind: concept
rung: mult
order: 467
setting: classical
equality: "≐"
domain: positive
law: "GAP — the calculus cannot say in its own terms which contents are off the principal strip, so the seam discipline has to be stated in the ℂ reading"
units: "'Im X ∉ (−π, π]' has no form"
holds:
  classical: fails
  J1: replaced
  JH: fails
  JO: fails
  JP: fails
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: ABSENT
status: ABSENT
verified: hand
known_since: "James 1993, Ch. 6 §6.3 pp. 46–47 ('J has ambiguous sign and ambiguous (multi-valued) cardinality'; the constraints 'approximate the constraints on collapsing complex numbers to radian values'); the gap as stated: 2026-10-03"
entered: 2026-10-03
guide: need-led
band: beyond
uses: []
see_also: [mult.seam-decree, mult.consistency, mult.involution, N.induction]
aliases: [phase signature, off-strip detection, native seam, where the receipt comes from]
concepts: [consistency, logarithm, gap]
understood: partial
understood_note: "this is the hinge of the whole enrichment program, seen from below"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| none | — | which forms have a logarithm off the principal strip |

The seam discipline ([[mult.seam-decree]]) refuses the unit step on content that is off the strip. "Off the strip" is a statement about values. The natural syntactic surrogate — content containing a square with an angle inside it, the written log of a negative — is **not enough**: `[[oo]]` is negative with no mirror in sight (ln ln 2 < 0), so `[[[oo]]]` carries iπ and `[[[oo]]] [[[oo]]]` is off the strip. Whether an iterated square loses sign depends on *values* (`[[ooo]]` is positive): `[[oo]]` and `[[ooo]]` have the same shape and opposite signs, so no shape-based signature is exact. The exact predicate — "the value's imaginary part lies in (−π, π]" — asks whether an exp–log constant is exactly a negative real, which is Richardson–Schanuel territory: plausibly undecidable, certainly unproven.

## Plain

The page can draw the log of the log of the log of two, but it cannot tell, from the drawing alone, that a half-turn has crept in. It needs someone who can see the numbers to say so.

## Derivation

none — gap.

## Confirms

That James's "crack" is deeper than the phase element: it is the absence, in an equational calculus of forms, of any term for the *branch* of a logarithm. The classical calculus is consistent only relative to a guard it imports. This is exactly the place where the enrichment program enters: 𝕁₁ does not guard the unit, it weakens it to `[(A)] ≐ A mod Λ` and records that the discrepancy lies in Λ as a receipt. A receipt is bookkeeping of an unknown, not detection — the calculus never determines *which* λ without the reading — but it dissolves the gap wherever an instance encloses the step (A5′ absorbs every λ) and leaves it open exactly for bare abstracts, which is what the J1 cells of [[alg.log-law]] and [[alg.power-of-power]] say. Seen from below, the receipt calculus is what this gap becomes.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, JH, JO, JP | fails | the guard is semantic in each (JH-3 evaluates `L(exp V(A))`) |
| J1 | replaced | the receipt replaces the guard: no detection is needed because nothing is refused |

| reading | cell | why |
|---|---|---|
| C | EXACT | the reading is where the signature lives |
| logic | ABSENT | — |
| others | untested | — |

## Refuted readings

- ~~"phased" (a square with an angle inside) is the signature~~ — refuted 2026-10-03 by `[[[oo]]]`; recorded at [[mult.seam-decree]].

## Notes

—

## Plan

| field | content |
|---|---|
| candidate form(s) | (i) a *receipt*: the J1 move — replace refusal by `[(A)] ≐ A λ` with λ ∈ Λ = ℤ·ω recorded, so the signature is read off the tape afterwards; (ii) a *normal form before the unit*: require the content to be written as `R` or `R J` with R unphased-and-positive by a decidable syntactic class (piles, instances, logs of piles ≥ 2, their sums and mirrors), and refuse the unit on anything else — a restriction of the calculus, not an extension; (iii) a phase boundary that tracks the branch explicitly — a new primitive, ranked last |
| law(s) to add, and type | (i) axioms (the J1 weakened unit and A5′); (ii) a decree narrowing admissible contents; (iii) a primitive |
| nativity criterion | stated using forms, juxtaposition and ≐ only, with no evaluation; (ii) is native but may refuse needed steps (`[[A]]` content in the exponent laws); (i) is native and refuses nothing |
| refutation test | for (ii): a needed derivation (an exponent law of rung `alg`) whose unit steps leave the admissible class; for (i): a derivation whose receipts fail to cancel under an instance — i.e. a failure of the depth-1 criterion |
| meta-move? | yes: the gap is about the *reading*; the receipt calculus is the moduli-of-readings move made native (Lui's framing: the calculus fibered over its own lattice) |
| owner thread | james-algebra (𝕁₁, A5′, the depth-1 criterion); kn-program (Λ as K(1)-localization) |
| rank | receipt (axioms, J1) < syntactic restriction (decree) < new primitive |
