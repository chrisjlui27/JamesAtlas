---
id: H.twenty-four
title: Twenty-four, twice
type: theorem
level: meta
kind: law
rung: H
order: 1790
setting: JH
equality: "≡"
domain: natural
law: "|2T| = 24 = M(2): the order of the Hurwitz unit group is the first wall number (place.local-wall at k = 1: 24 = 2³·3, e₂(1) = 3, e₃(1) = 1), and the match is factor by factor — Q₈ ↔ 2³, ⟨ζ⟩ ↔ 3 — but not place by place: the 3 of 2T is the order of ζ in the residue field 𝔽₄ of the place 2, the 3 of M(2) is contributed by the place 3. An ANALOGY until a form equates them (LEGISLATION 19)"
units: "24 = |2T| = denom(B₂/4) = |im J in π₃ˢ| = M(2); the next pair, 240 = |units of Coxeter's integral octonions| and M(4) = 240, is noted and not checked"
gloss_check: ""
witness: tools/models/h_twenty_four.py
holds:
  classical: replaced
  J1: holds
  JH: holds
  JO: untested
  JP: holds
readings:
  C: ABSENT
  finset: ANALOGY
  lambda: untested
  CC: untested
  logic: untested
status: ANALOGY
verified: engine
known_since: "Hurwitz 1896 (|2T| = 24); Adams 1965–66 (|im J| in π₃ˢ is 24); the pairing, marked as an analogy: Number at Height One (2026-07) and LEGISLATION 19; this rung, 2026-10-07"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.hurwitz-units, H.ramified-place, J1.wall-census, place.local-wall]
see_also: [J1.von-staudt-clausen, J1.psi-wall, H.octonion-gap, place.two-ends]
aliases: [24 ↔ ν, |2T| = M(2), the analogy at 24, the division-algebra branch rejoins at 24, 24 twice]
concepts: [quaternion, torsion, period, selection]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| \|2T\| = 24 = M(2); the factors match (2³ · 3 both sides) and the places do not (ζ's 3 lives at 2 in ℍ, the wall's 3 at the place 3) | — | 24 = \|π₃ˢ\| = denom(B₂/4) = \|2T\| |

The place where the division-algebra branch and the trunk show the same number, recorded as what it is. The trunk's wall at level one lets through M(2) = 24 of the roots of unity ([[J1.wall-census]]), and does so one place at a time ([[place.local-wall]]): 2³ from the place 2 (e₂(1) = 3) and 3 from the place 3 (e₃(1) = 1, since (3 − 1) | 2). The quaternions' integers select 24 units ([[H.hurwitz-units]]): 2³ from Q₈ and 3 from ⟨ζ⟩. The orders match factor by factor. The *places* do not: ζ is a unit of the residue field 𝔽₄ of the Hurwitz place 2 ([[H.ramified-place]]) — the 3 of 2T is the 3 of 𝔽₄^× = |𝔽₄| − 1, a fact about the place 2 — while the wall's 3 is the place 3's contribution and the wall's place 2 gives only 2³. So the two 24s are built from the same primes at different places, and no form on the chart equates them. LEGISLATION 19: an analogy is recorded as `ANALOGY`, with its match and its mismatch, until a form does; the witness checks the numbers, not the correspondence.

## Plain

Twenty-four appears twice: the count of special quaternion units, and the first number the trunk's wall lets through. Both are eight times three, but the three comes from a different prime each time. The chart records both without equating them.

## Derivation

none — an analogy; the witness computes both sides.

| statement | rule | note |
|---|---|---|
| \|2T\| = 24 = 8 · 3 | [[H.hurwitz-units]] | witness part (1) |
| M(2) = 24 = 2³ · 3, with e₂(1) = 3 and e₃(1) = 1 | [[place.local-wall]], [[J1.wall-census]] | witness part (2): Carmichael's λ, place by place |
| the 3 of 2T is the order of ζ, a unit of 𝔽₄ at the place 2; the 3 of M(2) is the place 3's | [[H.ramified-place]] | witness part (3): the mismatch |

## Confirms

The ROADMAP's sentence: "the division-algebra branch (JH/JO/JS) rejoins at 24, marked ANALOGY until a form equates them." It is **not** a coincidence the chart dismisses — the next pair, 240 units of Coxeter's integral octonions beside M(4) = 240, suggests a pattern along the Hurwitz–Cayley line — and it is **not** an equation: the chart has no form whose value is "the torsion of a maximal order" and none whose value is "the image of J".

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | replaced | ℤ[i] has 4 units; the trunk's wall at level 1 has nothing to compare them with |
| J1 | holds | M(2) = 24 is the trunk's number ([[J1.wall-census]]) |
| JH | holds | \|2T\| = 24 is the rung's number ([[H.hurwitz-units]]) |
| JO | untested | Coxeter's order has 240 units and M(4) = 240 ([[J1.wall-census]]); the second coincidence is noted here and not checked |
| JP | holds | both 24s are products over places, and the witness computes M(2) that way |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | ANALOGY | the 24 of the finite-set road is ν's: π₃ˢ = ℤ/24, the e-invariant ([[J1.von-staudt-clausen]]) |
| lambda, CC, logic | untested | — |

## Refuted readings

~~"the Hurwitz units are the image of J"~~ — not refuted, not asserted: the chart has no form for either side, and the places disagree.

## Notes

What a form equating them would have to do: carry the 3 from the place 3 to the place 2, which on the trunk is the business of the ψ-wall's Carmichael condition λ(n) | 2k and in ℍ of the residue field's cardinality 4 = 2² — the two 3s are 4 − 1 and 3 itself. The chart leaves the sentence there.
