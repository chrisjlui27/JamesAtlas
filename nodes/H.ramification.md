---
id: H.ramification
title: The quaternions ramify at two and at infinity
type: import
level: meta
kind: law
rung: H
order: 1770
setting: JH
equality: "≡"
domain: natural
law: "(−1, −1)_p = +1 for every odd p and −1 at p = 2 and at ∞: Hamilton's quaternions (−1, −1)_ℚ ramify at exactly {2, ∞} — the Hurwitz places — and split, ℍ ⊗ ℚ_p ≅ M₂(ℚ_p), at every odd p"
units: "x² + y² ≡ −1 (mod p) is solvable for every odd p and lifts; it has no solution in ℝ and no primitive solution in ℚ₂ (squares are 0, 1, 4 mod 8); the product formula ∏_v (−1, −1)_v = 1 makes the ramified set even"
gloss_check: ""
witness: tools/models/h_ramification.py
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: fails
  JP: holds
readings:
  C: ABSENT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: IMPORTED
verified: engine
known_since: "Hilbert 1897 (the norm residue symbol); Hasse 1923–24 (the local–global principle for quaternion algebras; the product formula); Hurwitz 1896 (the maximal order at 2); JP v0.3 (2026-09) for the chart's two readings"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.norm, H.quaternion, place.ostrowski, place.reading]
see_also: [H.split-place, H.ramified-place, place.two-ends, H.octonion-gap, H.hurwitz-units]
aliases: [the Hurwitz places, "(−1,−1)_ℚ", the Hilbert symbol, ramification of ℍ, ℍ splits at odd p, the discriminant of ℍ is 2]
concepts: [place, prime, quaternion]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| ℍ ⊗ ℚ_v is a division algebra for v ∈ {2, ∞} and ≅ M₂(ℚ_v) for every odd prime v | (−1, −1)_v = −1 at 2 and ∞, +1 elsewhere | the Hilbert symbol of (−1, −1)_ℚ; the discriminant of ℍ is 2 |

The import that tells the rung where to read. Ostrowski ([[place.ostrowski]]) lists the places of ℚ; the quaternions of [[H.quaternion]], carried to each place by the page's reading ([[place.reading]]), are a division algebra at exactly two of them — 2 and ∞, the **Hurwitz places** — and a matrix algebra at every odd prime. The criterion is whether the norm ([[H.norm]]) is isotropic: at an odd p the congruence x² + y² ≡ −1 has a solution (the witness finds one for p ≤ 23 and Chevalley–Warning gives it for all), which lifts and splits the algebra; in ℝ a sum of squares is never −1; in ℚ₂ the squares are 0, 1, 4 mod 8 and x² + y² + z² = 0 has no primitive solution. The two ramified places are the chart's two readings: [[H.ramified-place]] at 2 (half-shells, the Hurwitz order, 𝔽₄) and the ℍ reading at ∞ (SPEC §4.5); the odd places are [[H.split-place]]. That the ramified set is even — two places, not one — is the product formula, which the chart borrows with the rest.

## Plain

Hamilton's quaternions are "really" quaternions in only two places: over the reals and over the 2-adic numbers. At every odd prime they are secretly two-by-two matrices, and some of them multiply to zero.

## Derivation

none — adjoined, as an import: [[place.ostrowski]] lists the places, [[place.reading]] carries the quaternion ([[H.quaternion]]) and its norm ([[H.norm]]) to each, and the witness computes the Hilbert symbols.

| statement | rule | note |
|---|---|---|
| x² + y² ≡ −1 (mod p) solvable for p = 3, 5, 7, 11, 13, 17, 19, 23 | — | witness part (1): split at odd p |
| x² + y² + z² ≡ 0 (mod 8) has no primitive solution | — | witness part (2): (−1, −1)₂ = −1 |
| x² + y² = −1 has no real solution | — | witness part (3): (−1, −1)_∞ = −1 |
| the ramified set {2, ∞} has even size | — | witness part (4): the product of the computed symbols over these places is +1 |

## Confirms

That "read against the places" has two answers for ℍ, and the chart's two witnesses are those two: the half-shell reading at 2 and the matrix reading at odd p. It is **not** a theorem of the forms: the forms are the same at every place; what differs is which of them have values, and that is the reading's business ([[place.two-ends]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | replaced | ℂ splits ℍ: ℍ ⊗ ℂ ≅ M₂(ℂ) — the classical setting is the one place the quaternions are matrices "for free" |
| J1 | replaced | likewise, in the slice |
| JH | holds | ∞ is ramified: ℍ ⊗ ℝ = ℍ, a division algebra |
| JO | fails | the octonions ramify only at ∞: at every finite place, 2 included, their norm form is isotropic (eight variables over ℚ_p) and they split (Zorn's vector matrices) — the Hurwitz places are the quaternions' own |
| JP | holds | the law is about the places |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

Ramified at 2 is why rung `H` meets rung `place` at the half-period: the place that is "a prime of ℍ" with v(π) = ½ is the one whose residue field is 𝔽₄ and whose torsion is the full 2T ([[H.hurwitz-units]]); the odd places see only the matrix shadow.
