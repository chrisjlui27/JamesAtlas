---
id: place.reading
title: The reading at a place
type: import
level: meta
kind: law
rung: place
order: 1405
setting: JP
equality: "≡"
domain: complex
law: "DECLARATION — at the place p, to depth n, a form is read in the log space ℤ_p ⊕ ℚ·[p] ⊕ ℚ·J_p: a number part (a residue mod p^n), a count of the prime's log [p], a count of the torsion log J_p; the square of a number splits it into the three counts, the instance of a triple is a number when the number part is in the radius and the counts are whole"
units: "a = p^v · τ · u: valuation v, Teichmüller τ = g^k, principal unit u; log a = log u + v·[p] + k·J_p; exp converges on p·ℤ_p (4ℤ_2)"
gloss_check: ""
witness: tools/models/place_reading.py
holds:
  classical: replaced
  J1: replaced
  JH: untested
  JO: untested
  JP: holds
readings:
  C: ABSENT
  finset: PARTIAL
  lambda: untested
  CC: untested
  logic: untested
status: IMPORTED
verified: engine
known_since: "2026-09-13 (Forms at Every Place, jadic.js: 'log space at p: ℤ_p ⊕ ℤ[p] ⊕ ℤJ_p, ω_p = (p−1)J_p'); this engine, 2026-10-06"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [mult.c-reading, place.void-pile]
see_also: [mult.c-reading, J1.period-form, place.prime-log, place.torsion, place.radius, place.polar-form]
aliases: [the place reading, the log space at p, the three counts, tools/place.py, the p-adic reading]
concepts: [place, reading, logarithm, period]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| a form at p reads as (number part, count of `[p]`, count of J_p); `[ ]` splits a number into the three; `( )` reassembles them when it can | — | ℤ_p^× = μ_{p−1} × (1 + pℤ_p); log and exp inverse on the principal units |

The chart's ℂ reading ([[mult.c-reading]]) reads juxtaposition as addition, `( )` as exp and `[ ]` as log, in one space ℂ where numbers and their logs live together. At a finite place the two come apart. A number is a residue of the page ([[place.void-pile]]); its log has three parts — the log of its **principal unit** (a number again, in the radius p·ℤ_p), the **count of [p]** (its valuation, with `[p]` the log of the prime, irreducible at its own place: [[place.prime-log]]) and the **count of J_p** (the log of the Teichmüller part, a torsion element: [[place.torsion]]). The instance of a triple is exp of the number part, which converges only on the radius ([[place.radius]]), times p to the count of `[p]`, which must be a whole count ≥ 0 ([[place.no-inverse-of-the-prime]]), times the torsion to the count of J_p, which must be whole ([[place.selection]]).

Five conventions, declared here and nowhere else. (1) **The period**: the log of *exactly one* — a residue exactly one at the engine's working precision N, the page's depth n plus a margin of as many shells again, so that a log that loses shells is still read at the depth — reads ω_p = (p−1)·J_p (2·J_2 at p = 2) — the generator of the kernel of the instance at p, as 2πi is at ∞ — and every other log is principal, its torsion count in 0 … p−2 (0 or 1 at p = 2): LEGISLATION 30(b) at a place. So J = `[<o>]` reads ω_p/2 at every place ([[J1.half-period]] holds there), and the wall `(ω A) ≃ (A)` is the same wall ([[place.wall]]). (2) **Fractions of the period** are fractional counts of J_p and of `[p]`; a fraction that is not a whole count is not a form ([[place.selection]]). (3) **A formal element** — one with a count of `[p]` or J_p — has a log only as a formal symbol, which scales it by a count (`([[A]] [B])` is B·[A]); the product of two formal elements, `([J] [J])`, has no value at a finite place, where at ∞ it is −π²: *weight* is visible at finite places exactly because periods do not multiply to numbers there (JP v0.3). (4) **The generator**: the torsion log J_p is the log of the Teichmüller lift of the *least primitive root* mod p (2 at 3, 5, 11, 13; 3 at 7; the table `PRIMITIVE_ROOT` in `tools/place.py`), and −1 at p = 2 — a convention, as the choice of 2πi over −2πi is at ∞: another generator relabels the torsion counts, and nothing a law says depends on it except through (5). (5) **The principal root**: a fraction of a torsion count is taken in 0 … p−2 (0, 1 at 2), so the root form `(([[A]] <[oo]>))` reads the root whose torsion exponent is half of A's — the *principal* root of the place, the analogue of the positive root at ∞. On a principal unit (torsion count 0) it is canonical: the principal unit whose square is A — at p = 3, √4 = −2, since 4 ≡ 1 mod 3 and −2 is the 1-unit with that square ([[alg.sqrt4]]). On any other unit it picks one of the two roots by the generator of (4), and a cell that depends on which is marked so (LEGISLATION 31(h)).

## Plain

At a finite place a number is a residue on a clock face, and its log is three counts: how often p divides it, which root of unity it points at, and the log of the rest.

## Derivation

none — adjoined, as an import: the ℂ reading ([[mult.c-reading]]) moved to a finite place, on the page the void pile declares ([[place.void-pile]]); implemented as `tools/place.py`. The witness checks its claims on random residues at p = 2, 3, 5, 7, 13: the counit `([A]) ≐ A` exact; the three counts reassemble A; the period reads as declared and is absorbed.

## Confirms

The p-adic logarithm and exponential (Hensel), the Teichmüller lift, the decomposition ℤ_p^× = μ_{p−1} × (1 + pℤ_p): the standard analysis of a local field, read off a page. It is **not** ℚ_p: the reciprocal of the prime is not a form ([[place.no-inverse-of-the-prime]]), so the page is ℤ_p's, and the numbers with a negative count of `[p]` wait for a decree that admits them. It is **not** ℂ_p either: only the roots of unity that are forms at p exist there ([[place.selection]]); i at p = 3 is not a form, and no extension of the page is drawn.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | replaced | the ℂ reading at ∞ ([[mult.c-reading]]) |
| J1 | replaced | the ℂ reading with ω = 2πi; this is the same reading with ω_p = (p−1)J_p |
| JH, JO | untested | the Hurwitz places need a quaternionic log; owed to rung `H` |
| JP | holds | the declaration of the setting; witness |

| reading | cell | why |
|---|---|---|
| C | ABSENT | ℂ is the reading at ∞ |
| finset | PARTIAL | the number part is a finite set of residues; the counts are not |
| lambda, CC, logic | untested | — |

## Refuted readings

~~"⟨⟩ is the uniformizer at p"~~ — refuted 2026-09-13: the mirror gives J at every place; size lives in `[p]`, the log of the uniformizer p — `[oo]` at 2. ~~"every p-adic number is a re-entry"~~ — refuted 2026-09-19: finite re-entry systems are countable and ℤ_p is not; completion enters as a rule ([[place.completion]]).

## Notes

The chart's domains are read at a place by a dictionary (SPEC §4.4): a *positive* variable is a principal unit, now and then times p or p² — the place's image of the positive reals, the sector where the log is single-valued and every receipt is void ([[J1.regime-split]]); *negative* is minus a principal unit; *real* either; *complex* is any residue of the page; *natural* a small count; *unit* any unit; and a positive or real variable is a *fraction* of principal units a fifth of the time, so that a count that is not whole is sampled (the turn laws that hold only for integer turns are told apart there). The exceptional points are probed as at ∞ — a variable exactly one, and minus one for a negative variable. The radius is the standing proviso of every instance at a finite place, not a failure of a law: the ledger retries a sample on the radius and otherwise drops it, unjudged.
