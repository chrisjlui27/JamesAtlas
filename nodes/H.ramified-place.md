---
id: H.ramified-place
title: At two the quaternions are a division algebra with half-shells
type: theorem
level: meta
kind: law
rung: H
order: 1785
setting: JH
equality: "≐"
domain: natural
law: "at 2 the quaternions of the page are a division algebra and the Hurwitz order O is its unique maximal order: π := o i (= 1 + i) has v(π) = ½ and ([π ; π]) ≐ ([oo] [i]) (π² = 2i); v takes values in ½ℤ; the residue field O/πO is 𝔽₄ = {0, o, ζ, ζ²} with ζ = (<o> i j k)/2 of order 3; the radius of the instance is the half-shell v ≥ 3/2; i and j are not principal (v(i − o) = ½) and μ₃ is the Teichmüller part — the roles of rung place inverted; k ≐ o ([π ; ζ]) exactly, the quaternionic doll of one shell"
units: "ℍ ⊗ ℚ₂ is the division algebra of invariant ½; e = f = 2; the 24 Hurwitz units are the torsion of the global order O — its elements of norm 1 — and the torsion the reading names; the torsion of the local order O₂ is their conjugacy classes, infinitely many square roots of −1 among them; exp converges on v ≥ 3/2 and not at v = 1"
gloss_check: ""
witness: tools/models/h_ramified_place.py
holds:
  classical: replaced
  J1: replaced
  JH: replaced
  JO: fails
  JP: holds
readings:
  C: ABSENT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "Hurwitz 1896 (the maximal order and its 24 units); Hasse 1931 (the local division algebras; invariant ½ at 2); JP v0.3 (3) (2026-09: 'at 2 the roles invert — i, j principal-adjacent, μ₃ the torsion'); this rung, 2026-10-07"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.hurwitz-units, H.k, H.no-go, H.quaternion, H.ramification, place.radius, place.reading, place.residue, place.teichmuller, place.torsion]
see_also: [H.split-place, place.prime-log, place.void-pile, place.doll, place.no-inverse-of-the-prime, H.twenty-four, place.polar-form]
aliases: [the ramified place, the Hurwitz order at 2, π = 1 + i, v(π) = ½, half-shells, 𝔽₄, the quaternionic doll, JP v0.3 (3)]
concepts: [place, quaternion, prime, torsion, period]
owed: ["2026-10-13: the torsion of the local order O₂ beyond the 24 Hurwitz units — the conjugates of i, j, ζ — which the reading does not read", "2026-10-13: the log of a unit of O₂ whose torsion factor does not commute with its principal rest (a few per cent of O₂^× read today)"]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| at 2 the quaternions of the page form a division algebra whose maximal order is Hurwitz's O, with prime π = 1 + i, v(π) = ½, residue field 𝔽₄ and torsion 2T | — | the local division algebra of invariant ½; e = f = 2 |

The other ramified place ([[H.ramification]]), read as rung `place` reads a prime ([[place.reading]]) with everything halved. The **prime** of the order is π = 1 + i, not 2: π² = 2i, so v(π) = ½ and the valuation ([[place.radius]]) runs in half-shells — v(2) = 1 is the second shell. The **residue field** ([[place.residue]]) O/πO has four elements, 𝔽₄ = {0, 1, ζ, ζ²} with ζ = (−1 + i + j + k)/2, a Hurwitz unit of order 3: so the **Teichmüller part** ([[place.teichmuller]]) of the unit group is μ₃ — at 2 the roles of rung `place` invert, i and j are not principal units (i − 1 = iπ has v = ½, below the radius) and the order-3 unit is the torsion the trunk's place 2 did not have ([[place.torsion]]). The **radius** of the instance is v ≥ 3/2: exp converges there and not at v = 1 (the terms of exp(2) do not shrink). The 24 units ([[H.hurwitz-units]]) are exactly the elements of norm 1 in the *global* order O and its torsion, 2T — and they are the torsion the reading names; in the local order O₂ the torsion is their conjugacy classes, infinitely many ((3i + 4j)/5 squares to −1 in O₂ and is none of the 24: the 2-adic phase sphere of [[H.phase-sphere]]), which the reading does not read. And the third unit of [[H.k]] is a **doll of one shell**: k = 1 + πζ exactly, a principal-looking unit written as one plus the prime times a residue — the quaternionic [[place.doll]]. The no-go holds here too: `([i][j])` has no value, the two torsion logs do not commute.

## Plain

Over the 2-adic numbers the quaternions behave like a number field whose prime is 1 + i, a square root of 2i: distances come in half-steps, the residues form the four-element field, and the unit of order three that the ordinary 2-adics lack is here.

## Derivation

none — a theorem of the reading ([[place.reading]]) at the ramified place ([[H.ramification]]) of the quaternions ([[H.quaternion]]), witnessed in the Hurwitz order at 2.

| statement | rule | note |
|---|---|---|
| v(π) = ½ for π = 1 + i, v(2) = 1 | [[place.radius]] | witness part (1): π² = 2i |
| O/πO has four elements and is a field, 𝔽₄ = {0, 1, ζ, ζ²}, ζ³ = 1 | [[place.residue]] | witness part (2) |
| exp converges on v ≥ 3/2 and not at v = 1 | [[place.radius]] | witness part (3): the radius of the instance |
| the 24 Hurwitz units are the elements of norm 1 in the global order O and its torsion; in O₂ the torsion is larger — (3i + 4j)/5 squares to −1 and is none of the 24 | [[H.hurwitz-units]], [[place.torsion]] | witness part (4) |
| k = 1 + πζ | [[H.k]] | witness part (5): the doll of one shell |
| i, j are not principal (v(i − 1) = ½); the principal units start at v ≥ 3/2 | [[place.teichmuller]] | witness part (6): the roles inverted |
| ([i][j]) has no value at 2; ([i ; j]) = k | [[H.no-go]] | witness part (7) |

## Confirms

That the half-period of 𝕁₁ ([[J1.half-period]]) and the half-shell of ℍ at 2 are the same ½ seen twice: the prime log `[π]` has count ½ ([[place.prime-log]] read here), and the void pile at 2 is `π^{2n} ≐ void` on O/2ⁿO ([[place.void-pile]]) — the back-fill of rung `place`'s JH cells, census/h-place-ledger.md. It is **not** the trunk's place 2 with quaternion coefficients: the prime, the residue field, the radius and the torsion all change, which is why the chart reads it in its own witness and not by re-running tools/place.py.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | the places are not in those settings |
| JH | replaced | ∞ is the other ramified place, with the sphere of phases where 2 has the half-shells |
| JO | fails | the octonions split at 2: no division algebra there ([[H.ramification]]) |
| JP | holds | the reading at 2 |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The reading's log at 2 (tools/quatplace.py): the prime's power is stripped on the left (q = πᵐ·unit, as the instance rebuilds it — and since π is not central, a central number acquires a torsion part from its spelling: 2 = π²·(−i), 4 = π⁴·(−1), so `[oo][oo]` and `[oooo]` agree mod the period at 2, not exactly); principal units (v ≥ 3/2) have the series log; negative principal units are pinned to the direction i; the torsion logs are (direction, count) pairs over 2T, antipodal directions one direction with a signed count; the log of exactly one is the page period 2·J_i. The reading reads few units of O₂: half of O^× — the coset of the principal units times 2T, index 2 — has no Hurwitz representative, and of the other half only the units whose torsion and principal parts commute have a log (the witness samples 2000 units and finds a few per cent); the rest, and the torsion of O₂ beyond the 24, are owed and listed with the odd places' owed cases in census/h-place-ledger.md. The log is read at the working precision, not the depth: two representatives equal at the depth can differ in whether a commuting torsion factor exists, so the digits past the depth decide the *existence* of a log — the page's own equality does not pass through the square (LEGISLATION 31(g)), and at 2 it does not even decide whether there is one.
