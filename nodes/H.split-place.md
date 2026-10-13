---
id: H.split-place
title: At an odd prime the quaternions are matrices
type: theorem
level: meta
kind: law
rung: H
order: 1775
setting: JH
equality: "≡"
domain: natural
law: "at an odd p, i ↦ [[0, 1], [−1, 0]] and j ↦ [[a, b], [b, −a]] with a² + b² ≡ −1 (mod pⁿ) is a ring map onto the 2×2 matrices satisfying Hamilton's relations: every law of the rung holds on the page at p as a matrix law, the norm is the determinant and is isotropic — the norm-null quaternions of the page are zero divisors, with no reciprocal and no log (JH-20 on the page)"
units: "ℍ ⊗ ℚ_p ≅ M₂(ℚ_p) for odd p; N(q) = det; a nonzero q with det ≡ 0 is a zero divisor; U^{φ(pⁿ)} ≡ 1 fails for U = i when p ≡ 3 mod 4"
gloss_check: ""
witness: tools/models/h_split_place.py
holds:
  classical: replaced
  J1: replaced
  JH: replaced
  JO: holds
  JP: holds
readings:
  C: ABSENT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "Hamilton 1843 (the matrix representation, in substance: Cayley 1858); Hasse 1923–24 (ℍ splits at odd p); JP v0.3 (2026-09) for the page's reading; this rung, 2026-10-07"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.inverse, H.k, H.no-go, H.norm, H.quaternion, H.ramification, place.fermat, place.reading, place.teichmuller]
see_also: [H.ramified-place, H.no-go, H.ordered-cancellation, place.division-by-unit, place.torsion, H.hurwitz-units]
aliases: [the split places, M₂(ℚ_p), quaternions mod pⁿ, the norm-null species, JH-20, zero divisors on the page, the matrix reading]
concepts: [place, quaternion, prime, division]
owed: ["2026-10-07: the log of a unit whose reduction mod p has order divisible by p (a unipotent part) — refused by name", "2026-10-13: the log of a unit whose torsion factor does not commute with its principal rest — refused by name; the extension with negation by conjugation, −(t, L) := (t⁻¹, −tLt⁻¹), is LEGISLATION 32(e)(ii)'s alternative"]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| at odd p the quaternions of the page are M₂(ℤ/pⁿ): the rung's laws hold there, the norm is the determinant, and it is isotropic | — | ℍ ⊗ ℚ_p ≅ M₂(ℚ_p) |

The reading of the rung at an odd place, as tools/quatplace.py computes it and the witness checks at p = 3, 5, 7, 13: the four parts of [[H.quaternion]] are residues mod pⁿ, i and j are the two matrices in the law (the congruence a² + b² ≡ −1 is solvable at every odd p — [[H.ramification]] — and lifts to every depth), k = ij, and Hamilton's relations hold on the page. Every law of the rung is then a matrix identity. What the place adds is **isotropy**: the norm ([[H.norm]]) is the determinant and vanishes on nonzero quaternions of the page — q = 1 + i·c + j·d with c² + d² ≡ −1, for instance — and those are zero divisors: no reciprocal ([[H.inverse]] is guarded), no log (the reading refuses `[q]` for them, by name: the norm-null species, JH-20 read on the page), and ordered cancellation ([[H.ordered-cancellation]]) fails for them, which is the `guarded` cell of that law at JP. Two more facts the witness records: Fermat's law of the page ([[place.fermat]]) fails off the centre — U = i has order 4, and 4 ∤ p − 1 when p ≡ 3 mod 4 — so it holds on the centre only, which is its JH cell; and the trunk's `([A][B])` is formless or false for non-commuting A, B of the page while `([A ; B])` is their product: [[H.no-go]] at the place.

## Plain

At an odd prime a quaternion is the same thing as a two-by-two matrix of residues. Most of them can be divided by; the ones whose determinant is zero cannot, and that is new — over the reals every nonzero quaternion divides.

## Derivation

none — a theorem of the reading ([[place.reading]] of the quaternions [[H.quaternion]] at p), witnessed at p = 3, 5, 7, 13.

| statement | rule | note |
|---|---|---|
| Hamilton's relations hold in the quaternion reading at p | [[H.k]] | witness part (1): i² = j² = k² = −1, ij = k, ji = −k on the page |
| a nonzero q of the page with N(q) ≡ 0 exists, is a zero divisor, has no reciprocal and no log | [[H.norm]], [[H.inverse]] | witness part (2): JH-20 on the page |
| a² + b² ≡ −1 (mod pⁿ) is solvable and i ↦ [[0,1],[−1,0]], j ↦ [[a,b],[b,−a]] respects the relations | [[H.ramification]] | witness part (3): the split |
| U^{φ(pⁿ)} ≡ 1 fails for U = i at p ≡ 3 mod 4 | [[place.fermat]] | witness part (4): Fermat on the centre only — the Teichmüller units of the page ([[place.teichmuller]]) are the centre's |
| ([A][B]) formless or false for non-commuting A, B of the page; ([A ; B]) their product | [[H.no-go]] | witness part (5) |

## Confirms

That the ordered square is needed at the places as much as at ∞, and that the page's wall is the same wall with new inhabitants: the Teichmüller units ([[place.teichmuller]]) of the page are now a matrix group's semisimple part, and the units with no log are those whose reduction mod p has order divisible by p (the unipotent part) — the reading's owed cases, listed in census/h-place-ledger.md. It is **not** a different calculus: the forms are the trunk's and rung H's, read at p.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | the places are not in those settings |
| JH | replaced | ∞ is a ramified place: no zero divisors, [[H.inverse]] unguarded |
| JO | holds | the octonions split at every finite place too (Zorn's vector matrices) — with zero divisors likewise |
| JP | holds | the reading at p = 3, 5, 7, 13 |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The reading's log at an odd p: a torsion log is a (direction, count) pair for the units of finite order prime to p, with J_p central; units whose reduction has order divisible by p have no log in the reading, and neither have units whose torsion factor does not commute with their principal rest (the log must be a sum whose negation is the log of the inverse) — owed. The log is read at the working precision, not the depth, so the digits past the depth decide whether a unit has one. The ledger's cells for rung H at the odd places (census/h-place-ledger.md) are computed on the quaternions of the page that *have* values; where a law is formless on some samples the cell is `guarded`.
