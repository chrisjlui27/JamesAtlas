---
id: C.phase-independence
title: Phase independence — James's Theorem 1, and where the crack is
type: theorem
level: object
kind: law
rung: C
order: 935
setting: classical
equality: "≐"
domain: real
law: "[<(A)>] ≐ A J"
units: "ln(−e^a) = a + iπ  (a real)"
gloss_check: "A + 1j*pi"
holds:
  classical: holds
  J1: holds-mod-Λ
  JH: replaced
  JO: replaced
  JP: holds-mod-Λ
readings:
  C: PARTIAL
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James, Ch. 6 §6.2.1, p. 44, Theorem 1 'Phase Independence', stated for all A ∈ B; its failure off the strip and the location of the crack in its last step: this chart, 2026-10-03)"
entered: 2026-10-03
guide: need-led
band: "9–12"
uses: [C.phase, mult.hole-instance, mult.dominion, Z.inversion, mult.distribution, mult.involution, mult.log-of-one]
guarded_by: [mult.seam-decree]
see_also: [C.log-of-negative, C.phase-under-instance, C.double-phase, C.james-discipline, mult.seam-decree]
aliases: [phase independence, phase operator, "[<(A)>] = A J", James's Theorem 1]
concepts: [phase, logarithm, negation, consistency]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[<(A)>] ≐ A J` | — | ln(−e^a) = a + iπ, for real a |

James's *phase operator* is the nesting `[<(A)>]` — abstract, inverse, instance — and his Theorem 1 says its content can be moved out beside a bare J. The chart states it with the condition James's proof needs and his statement omits: it holds exactly when a + iπ is on the principal strip, i.e. for real a (and for Im a ∈ (−2π, 0]), and it fails by a period otherwise.

## Plain

Box the mirror of a circled number, and the number steps outside, leaving a J behind. True for the numbers you meet first — and the place where the whole calculus cracked, because James stated it for every form.

## Derivation

James's own proof (p. 44), row for row; the chart's engine adjudicates the last row.

| form | rule | note |
|---|---|---|
| `[<(A)>]` | given | the phase operator, James's name for this nesting ([[C.phase]] names the J it produces) |
| `[<(A)> ([])]` | [[mult.hole-instance]] | `(□) ≐ void`, right to left — James writes "Involution", since `(□) = ([void])` |
| `[<(A)> (A [])]` | [[mult.dominion]] | `□ ≐ □ A`, right to left, inside the instance |
| `[<(A)> (A [() <()>])]` | [[Z.inversion]] | a unit and its mirror created inside the hole |
| `[<(A)> (A [()]) (A [<()>])]` | [[mult.distribution]] | — |
| `[<(A)> (A) (A [<()>])]` | [[mult.log-of-one]] | `[o] ≐ void` — James writes "Involution" |
| `[(A [<()>])]` | [[Z.inversion]] | `<(A)> (A)` cancels |
| `A [<()>]` | [[mult.involution]] | the unit `[(X)] ≐ X` at depth 0 with X = `A J`: admitted by the seam decree exactly when a + iπ is on the strip — for real a, on its closed edge. **This is the row.** For A = J the content is 2πi and the step is refused |

## Confirms

ln(−e^a) = a + iπ for real a — the principal branch's rule for the exponential of a negated exponential — and James's observation that the phase operator is "independent of its contents". What it is **not**: a law for every form A, as James states it (p. 44). At A = J the left side is `[<(J)>] = [<<o>>] = [o]`, which is void, and the right side is `J J`, which is 2πi; James's Theorem 2, "J Cancellation" `J J ≐ void` (p. 45), is *exactly* this theorem at A = J, run right to left — and it is from Theorem 2 that the ambiguous sign and cardinality of J follow (§6.3). So the crack in the calculus is one row long and has an address: the last line of the proof above, taken on content off the strip. Everything else in James's proof is exact. The chart's [[C.log-of-negative]] (`[<A>] ≐ [A] J`, James's rule 1) and [[C.phase-under-instance]] (`<(A)> ≐ (A J)`) are the two "concise forms of inverse promotion" he derives from this theorem on p. 45; the second is exact for every A because its unit step sits inside an instance.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | on real content, by the seam decree's content clause |
| J1 | holds-mod-Λ | the bare depth-0 unit: `[<(A)>] ≃ A J` with a receipt — J1's reading of James's theorem, and the reason J1 exists |
| JH, JO | replaced | the phase operator in ℍ moves the content out beside the J of the content's own slice (JH's O6) |
| JP | holds-mod-Λ | exact as an equation for the samples of the page; the receipt posted at p is the one posted at ∞, by position — J = ω_p/2 at every place ([[place.torsion]]) |

| reading | cell | why |
|---|---|---|
| C | PARTIAL | exact for Im a ∈ (−2π, 0] (all real a); false by 2πi otherwise |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

- ~~phase independence holds for every form A~~ — James's statement of Theorem 1 (p. 44, "For all A ∈ B"); refuted 2026-10-03 at A = J (and at every A with Im a outside (−2π, 0]): the proof's last step is the seam step. Its consequence `J J ≐ void` is struck at [[C.double-phase]].

## Notes

Guarded by content (Amendment A2): the last row is the unit at depth 0 on `A J`; for real a its content a + iπ lies on the closed edge of the strip, which the decree admits. The chart could not have stated this theorem for complex A at all: on `domain: complex` the engine refuses the row, which is the crack made mechanical.
