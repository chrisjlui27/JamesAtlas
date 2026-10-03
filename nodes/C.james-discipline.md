---
id: C.james-discipline
title: James's J-discipline sits inside the seam decree
type: theorem
level: meta
kind: law
rung: C
order: 1090
setting: classical
equality: "≐"
domain: positive
law: "James's two J-rules, as the chart records them — convert [<A>] to [A] J on sight; cancel J J only inside an instance, and last — sit inside the seam decree: rule 1 is admitted exactly on content with Im Ln A ∈ (−π, 0] and refuted elsewhere, rule 2 is period absorption, and the decree is strictly stronger than both, since it adjudicates every unit step and not only those through J"
units: "ln(−a) = ln a + iπ only for Im Ln a ∈ (−π, 0]; e^{z + 2πi} = e^z always; 2πi ≠ 0; the Involution route to J J = 0 is closed by neither J-rule"
witness: tools/models/j_discipline.py
holds:
  classical: holds
  J1: replaced
  JH: replaced
  JO: replaced
  JP: untested
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE-BY-DECREE
verified: engine
known_since: "1993 (James, Chapter 5: the 'crack' and its repair); the comparison with the semantic guard: this chart, 2026-10-03"
entered: 2026-10-03
guide: need-led
band: beyond
uses: [C.log-of-negative, C.log-of-negative-below, C.period-absorption, C.double-phase, C.phase-sign, mult.seam-decree, mult.seam-signature, Q.reciprocal-of-negative]
see_also: [mult.seam-decree, mult.consistency, C.log-of-negative, C.period-absorption]
aliases: [J-discipline, "James's disciplinary rules", the crack, J-cancellation, on-sight conversion]
concepts: [consistency, phase, logarithm]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| rule 1, `[<A>] → [A] J` ⊂ the content clause (and only for Im Ln A ∈ (−π, 0]); rule 2, J-cancellation inside an instance ⊂ the position clause; decree ⊋ rules | — | the J-discipline is a special case of the seam decree, not the same rule |

James found that his three axioms, read naively, prove `J J ≐ void` and from it collapse the calculus (the "crack", Chapter 5), and repaired it with two rules of procedure about J. The chart's repair is a decree about the unit step, stated two rungs earlier and without mentioning J ([[mult.seam-decree]]). This node records how the two relate: everything James's rules *soundly* admit, the decree admits — a restriction of rule 1 and all of rule 2 — and the decree refuses more, including a route to the crack that the J-rules, as the chart has them, do not close.

## Plain

James patched the crack by giving rules for handling J. The chart patched it by giving a rule for undoing a circle with a box. The chart's patch covers James's and more — and James's first rule, taken literally, is itself cracked.

## Derivation

The J-rules compared here are the chart's paraphrase of Chapter 5 (page citations owed); the comparison is against that paraphrase.

| statement | rule | note |
|---|---|---|
| **Rule 1 ⊂ content clause, restricted.** "Convert `[<A>]` to `[A] J` on sight" is the law [[C.log-of-negative]], whose one step is the unit at depth 0 on content `[A] J`. The decree admits it exactly when Im Ln A ∈ (−π, 0] — positive A and the lower half-plane — and the equation is false by 2πi otherwise, so James's rule *as stated* is unsound: it fails at A = `<o>` and at A = `[[oo]]`, a negative real with no mirror in sight. The chart's rule 1 is the restriction to positive A, with [[C.log-of-negative-below]] as its companion on the other side | [[C.log-of-negative]] [[C.log-of-negative-below]] [[mult.seam-decree]] | witness part (1): on wide complex sampling the conversion is exact in roughly half the samples and off by exactly 2πi in the rest, with the boundary predicted by the strip test in every sample |
| **Rule 2 ⊂ position clause.** "Cancel `J J` only inside an instance, and last" is [[C.period-absorption]] `(A J J) ≐ (A)`: the unit step it hides is a seam step taken in an absorbing position, which the decree admits; the ordering clause is unnecessary once admissibility is decided by position | [[C.period-absorption]] [[C.double-phase]] | witness part (2): exact on 300 complex samples |
| **The decree is strictly stronger.** (a) It adjudicates unit steps that involve no J at all: the seam steps of [[Q.reciprocal-of-negative]] have content −ln a − iπ and 2πi, and the J-rules say nothing about them. (b) The collapse route of [[mult.seam-decree]] reaches `J J ≐ void` not by cancelling `J J` but by one Involution step `[(J J)] → J J` at depth 0 — a step neither J-rule, as paraphrased, forbids; the decree refuses it by content, in both orientations | [[mult.seam-decree]] [[Q.reciprocal-of-negative]] | witness part (3): the engine's own seam check refuses `[(J J)] ↔ J J` both ways and admits the same step directly inside an instance, through an angle too |
| What the J-rules leave implicit — that `J` and `<J>` differ on the page and agree under an instance — is [[C.phase-sign]] | [[C.phase-sign]] | witness part (4) |
| Where the two repairs differ in kind: James's rules are syntactic ("on sight", "inside an instance") and the first is unsound for that reason — the content `[A] J` leaves the strip for some A without any visible sign; the decree is semantic, and that it must be is the gap [[mult.seam-signature]] | [[mult.seam-signature]] | — |

## Confirms

That the classical setting of the chart — three boundaries, three axioms, two decrees — contains the classical James algebra of the thesis: three boundaries, three axioms, J, and the J-discipline. The discipline is not a fourth axiom and not a convention about J; it is a procedural shadow of the condition under which the unit step is *harmless* — true on the strip, absorbed inside an instance — and J is where the condition first bites: `<J>` (four boundaries, value −iπ) is the smallest form whose content leaves the half-open strip, and `J J` the smallest whose content leaves it by a whole period. What this node does **not** show: that the two repairs are equivalent (they are not — the decree is strictly stronger, and rule 1 is refuted as stated); that the decree is the *only* repair (J1 prices the step with a receipt instead of refusing it, and JH guards one orientation semantically); or that the decree follows from the axioms (it is adjoined, in both tellings). Nor does it certify James's own text: the rules compared are the chart's paraphrase, and the thesis may restrict Involution-down as well — the page citations are owed.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | replaced | J1 does not refuse the bare step; it weakens the unit to `[(A)] ≐ A mod Λ` and lets `J J = ω` stand as a non-void element of the kernel — the discipline becomes bookkeeping |
| JH, JO | replaced | by the seam guard JH-3, one orientation, and the slice-local J_u; James's rule 1 is unsound in ℍ even for positive content in a foreign slice (JH's O6) |
| JP | untested | the audit at a place passed with the discipline in force; the comparison with James's rules there is untested |

| reading | cell | why |
|---|---|---|
| C | EXACT | the inclusion is a statement about the ℂ reading, where both repairs are stated |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

- ~~the J-discipline and the seam decree are the same rule~~ — the first statement of this node (2026-10-03, same day); refuted by its own body in the C referee pass: the decree adjudicates non-J seam steps and the Involution route to the crack, which the J-rules do not, and rule 1 as stated is false off the lower half-plane. Struck, and the node restated as an inclusion.
- ~~the J-discipline is a convention about a special symbol J, separate from the axioms~~ — it is a special case of the admissibility condition on the unit step of [[mult.involution]], which the chart states before J is named (an interpretive thesis, recorded rather than witnessed).

The refutations of `J J ≐ void` and `J ≐ <J>` as depth-0 laws, and of the on-sight rule for every A, live at [[C.double-phase]], [[C.phase-sign]] and [[C.log-of-negative]] respectively.

## Notes

The witness `tools/models/j_discipline.py` tests four facts of the ℂ reading and one behaviour of the engine (`check_seam`, the chart's implementation of the decree); it witnesses the rows above, not a theorem about two derivation systems — that would need James's rules formalized from the text. James 1993, Chapter 5, page citations are owed (the chart's copy of the thesis is the 2026 transcription). The 2026-10-01 and 2026-10-03 sessions found the collapse route independently and legislated the decree at rung `mult` under referee pressure; this node closes that loop by placing James's own rules inside it.
