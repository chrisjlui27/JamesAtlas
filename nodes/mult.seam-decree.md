---
id: mult.seam-decree
title: The seam discipline
type: decree
level: meta
kind: discipline
rung: mult
order: 465
setting: classical
equality: "≐"
domain: positive
law: "DISCIPLINE — a unit step, in either orientation ([(X)] → X or X → [(X)]), is admissible only when X lies on the principal strip in the ℂ reading (−π < Im X ≤ π), or when the redex is in an absorbing position: directly inside an instance boundary, through angle boundaries at most"
units: "log e^z = z only for −π < Im z ≤ π; a 2πi error is harmless exactly where an exp will swallow it"
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
known_since: "1993 (James, Ch. 6 §6.3 p. 47: the two constraints on J — convert [<A>] to [A] J on sight; cancel Js only within an instance boundary and after other reductions); JH-3 (2026-08) for the semantic seam guard; the rung-mult collapse route and the failure of the syntactic signature: referee and witness passes 2026-10-03"
entered: 2026-10-03
guide: need-led
band: beyond
uses: [mult.involution, mult.square, Z.angle, N.round, void.space, mult.c-reading]
see_also: [mult.hole-exclusion, mult.consistency, mult.seam-signature, Q.reciprocal-of-negative]
aliases: [J-discipline, seam guard, JH-3, Involution-down guard, phase discipline]
concepts: [consistency, logarithm, negation]
understood: partial
understood_note: "the shape is clear; that it cannot be said in forms is the part that bites"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[(X)] → X` and `X → [(X)]` admitted iff X is on the principal strip, or the redex is in an absorbing position | — | log e^z = z fails off the strip by a multiple of 2πi, in either direction, which only an enclosing exp cancels |

A **seam step** is a unit step whose content leaves the strip for some value in the node's domain: there the equation `[(X)] ≐ X` is locally false and only an enclosing instance saves the derivation, so a law that takes one declares `guarded_by` (*by position*); a unit step at a non-absorbing position is admitted on its content and declares `guarded_by` too (*by content*); an absorbing on-strip step is free (Amendment A2). **Absorbing position**: the redex is a member of the multiset directly inside an instance boundary, or inside angle boundaries that are. The counit `([X]) ≐ X` is never restricted, and the unit on void or hole content — `[(void)] ≐ void`, `[(□)] ≐ □` — is a theorem of the hole rules ([[mult.unit-law]], [[mult.hole-instance]]) rather than an instance of this decree, wherever it stands. The equation `[(X)] ≐ X` is false off the strip in *both* directions, so both orientations are guarded — the first statement of this decree guarded only `[(X)] → X` and was bypassed by running the collapse below backwards (alg referee pass). The guard is stated in the ℂ reading ([[mult.c-reading]]): this decree *imports* a condition the forms cannot yet express — see [[mult.seam-signature]] for why the obvious syntactic surrogate fails.

## Plain

The box may undo the circle only where no hidden turn has crept in, or right inside another circle, which forgets whole turns — and the page cannot itself see the hidden turn; it has to be told.

## Derivation

none — adjoined, as a decree about the unit direction of [[mult.involution]], stated in terms of [[mult.square]], [[Z.angle]], [[N.round]], position in space [[void.space]], and the ℂ reading [[mult.c-reading]]. The collapse it is legislated against is recorded under Notes.

## Confirms

James's own repair of the "crack" in his calculus (Ch. 6 §6.3, p. 47): J-cancellation permitted only inside an instance boundary, and only after other reductions — constraints he himself calls "not exhaustive". The chart states a stronger rule one rung earlier, and semantically — James's two J-rules sit inside it as special cases ([[C.james-discipline]]) — because the collapse can be written as soon as `[<o>]` or `[[[oo]]]` can — at rung `mult`, before J is a named form — and because no syntactic signature of "off the strip" is available in the calculus (the witness `[[[oo]]]` refutes the natural one). Soundness under the decree is the theorem [[mult.consistency]]. JH's seam guard — `[(A)] → A` only when `L(exp V(A)) = V(A)` — is the same rule; J1's answer is different in kind: it does not refuse the step, it *prices* it with a receipt, and the depth-1 criterion ([[mult.involution]], Notes) says when the price is absorbed.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | this is the classical setting's second decree; James's J-discipline is a special case of it stated through J ([[C.james-discipline]]) — and his on-sight conversion `[<A>] ≐ [A] J`, taken literally, is unsound: at A = `[[oo]]` the left side is −1.0037 and the right −1.0037 + 2πi, so the conversion holds only for Im Ln A ∈ (−π, 0] |
| J1 | replaced | by the weakened unit `[(A)] ≐ A mod Λ` with receipts — the native alternative to a semantic guard |
| JH, JO | replaced | by the semantic seam guard JH-3 — the one-orientation form of this guard; whether JH admits the reverse unit step unguarded is to be checked against the JH ledger |
| JP | holds | the axiom audit at a finite place passed with the discipline in force |

| reading | cell | why |
|---|---|---|
| C | EXACT | the decree is exactly the restriction under which the principal logarithm is a left inverse of exp |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

- ~~the guard need only cover the orientation `[(X)] → X`~~ — the first statement of this decree (2026-10-03); refuted the same day by the alg referee pass: the collapse runs backwards through `X → [(X)]` (Notes).
- ~~the pilot's rungs need no guard on Involution-down; the J-discipline is rung C's business~~ — refuted 2026-10-03 (second referee pass): `J J = [<o>][<o>]` is writable at rung `mult`, and the collapse above uses only rungs ≤ Q.
- ~~"phased" — a square with an angle somewhere inside it — is a sufficient syntactic signature for off-strip content, so the decree can be stated in forms alone~~ — refuted the same day by the consistency witness (`tools/models/consistency_check.py`): `[[[oo]]]` = ln(ln ln 2) has imaginary part π with no angle anywhere, and `[[[oo]]] [[[oo]]]` is off the strip. Sign is lost under iterated squares, not only under mirrors; which iterated squares lose it depends on values (`[[ooo]]` is positive, `[[oo]]` negative). The decree is therefore semantic, and its nativity is the gap [[mult.seam-signature]].

## Notes

**The collapse the decree blocks**, using only laws of rungs ≤ Q. Start from `o`; by the unit law right to left, `o ≐ ([o] [o])`; by the product of negatives right to left, `≐ ([<o>] [<o>])`. Abstract both sides: `void ≐ [o] ≐ [([<o>] [<o>])]`, and one **unguarded** unit step, `[([<o>][<o>])] → [<o>] [<o>]`, gives `[<o>] [<o>] ≐ void` — James's J-cancellation `J J ≐ void`, whose content is 2πi. From it: `J ≐ <J>` by Inversion; with H = `([J] <[oo]>)` (half of J), cardinality gives `H H ≐ J`, and the ℚ sign rule for a mirrored numerator turns `H ≐ ([H H] <[oo]>) ≐ ([<H H>] <[oo]>)` into `<H>`; so `J ≐ H H ≐ H <H> ≐ void`, `<o> ≐ ([<o>]) ≐ (void) ≐ o`, and `oo ≐ o <o> ≐ void`. Every step but the marked one is exact in ℂ. The marked step is refused by this decree: its content has imaginary part 2π and its position (depth 0) is not absorbing. (An earlier Refuted entry spoke of "the collapse above"; it is this one.) Run backwards — `[<o>] [<o>] → [([<o>] [<o>])] → [([o] [o])] → [o] → void` — the same collapse uses the unit in the *other* orientation, which is why both are guarded. The same route runs, mutatis mutandis, from N = `[[oo]]`, a negative number reached with no mirror: `([N][N]) ≐ ([<N>][<N>])` (both 0.1343), the unguarded step `[([N][N])] → [N][N]` (content −2.007 + 2πi), and J′ = `[N] <[<N>]>` (value iπ) in J's role — which is why the guard must look at values and not at mirrors ([[mult.seam-signature]]). The "ℚ sign rule for a mirrored numerator" above is [[Q.negative-fraction]].

**Price.** The guard imports the ℂ reading, which overcharges: only Im X — the branch index — is needed, not the whole value (and *not* Im X mod 2π, which destroys exactly the information the strip test uses); a cheaper `branch-reading` import would price the sign laws more exactly. Laws whose unit steps are admitted *by content* at non-absorbing positions ([[alg.log-law]] and [[C.log-of-negative]] at depth 0; [[alg.root-of-product]] and [[alg.power-of-power]] under a square), and laws whose unit steps are seam steps admitted *by position* ([[Q.reciprocal-of-negative]], [[C.period-absorption]], [[C.euler-formula]]), declare `guarded_by: [mult.seam-decree]` — a field the checker computes from the derivation and enforces both ways — and so carry the guard in their price; their descendants inherit it through `uses`. Their status stays NATIVE: the decree adjudicates the step, it does not make the law true (Amendment A2, after the C referee pass found the two clauses priced inconsistently between rungs Q and C).

The engine enforces this decree directly (`tools/check.py`, `check_seam`): for every step that is a unit step, it evaluates the content on the node's sampled domain and refuses the step if the content leaves the strip in any sample while the position is not absorbing. Schemas are checked on their sampled instances; a law whose derivation needs an unguarded unit step for some instances must either restructure the step into an absorbing position or restrict its domain and say so.
