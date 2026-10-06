---
id: place.lift
title: A root at depth one lifts to every depth
type: theorem
level: meta
kind: law
rung: place
order: 1560
setting: JP
equality: "≡"
domain: unit
law: "for a unit A at an odd place p: (([[A]] <[oo]>)) is a form at p iff A is a square mod p; the Newton step X ↦ (([X ([A] <[X]>)] <[oo]>)) doubles the depth at which X² ≐ A"
units: "Hensel's lemma for x² = a: a root mod p with 2x a unit lifts uniquely to ℤ_p; Newton's iteration converges quadratically — the depths 1, 2, 4, 8, 16, 32"
gloss_check: ""
witness: tools/models/place_lift.py
holds:
  classical: replaced
  J1: replaced
  JH: untested
  JO: untested
  JP: holds
readings:
  C: ABSENT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "Hensel 1908; 2026-09-13 (Forms at Every Place, EXACT: 'Hensel = Newton step written natively with depths 1, 2, 4, 8, 16, 32'); JP v0.3 (the grade of a re-entry: superguarded = Newton)"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [alg.root, alg.root-squared, place.division-by-unit, place.reading, place.doll]
see_also: [alg.root, alg.sqrt2, alg.sqrt4, place.selection, place.geometric-doll, place.completion]
aliases: [Hensel's lemma, the lift theorem, Newton at p, guarded re-entry, superguarded, √2 at 7]
concepts: [place, root, induction]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| a square root of a unit A exists at an odd place p exactly when A is a square mod p, and the root form `(([[A]] <[oo]>))` reads it; the Newton step `(([X ([A] <[X]>)] <[oo]>))` — half of X + A/X — carries a root mod p^k to a root mod p^{2k} | — | Hensel's lemma; quadratic convergence of Newton's method in ℤ_p |

At ∞ the root form of [[alg.root]] reads a root of any positive number. At a finite place it reads a root when there is one on the page, and the test for that happens at depth one: a unit is a square at p (odd) if and only if it is a square mod p. The reason is the **lift**: a root x₀ mod p with 2x₀ a unit improves to a root mod p², then p⁴, then p⁸ — each Newton step `x ↦ (x + a/x)/2` (division by the unit x: [[place.division-by-unit]]) doubles the number of shells that are right, the *superguarded* re-entry of the JP ledger's grade table. The root form does the same thing in one stroke: `[[A]]` splits A's log into its three counts, halves them, and the instance reassembles — which is a form exactly when the torsion count is even and the count of `[p]` is whole ([[place.reading]]): A a square mod p, and A's valuation even. So √2 is a form at 7 (3² ≡ 2) and at 17 (6² ≡ 2) and at 23, 31; not at 3, 5, 11, 13 — and the chart's [[alg.sqrt2]] guard "where the root is a form at p" is this criterion.

## Plain

To find a square root at a finite place, find one on the clock with p hours; then Newton's step fixes twice as many digits each time. If there is no root on the small clock, there is none at the place at all.

## Derivation

| statement | rule | note |
|---|---|---|
| **The root form at p.** `(([[A]] <[oo]>))` ([[alg.root]]) halves the three counts of A ([[place.reading]]): it is a form iff the torsion count is even — A a square mod p — and the count of `[p]` is whole; where it is, its square is A ([[alg.root-squared]]) | [[alg.root]] | witness part (1): at p = 3, 5, 7, 11, 13, 17 and the units a ≤ 40, the root form has a value exactly when a is a square mod p, and squares back to a |
| **The lift.** From a root mod p, Newton's step `(([X ([A] <[X]>)] <[oo]>))` — division by the unit X ([[place.division-by-unit]]) — gives a root to twice the depth: shells 1, 2, 4, 8, 16, 32, a doll filled two shells for one ([[place.doll]]) | [[place.division-by-unit]] | witness part (2): the Newton step from the root mod p agrees with the root form to 2, 4, 8, 16, 32 shells in turn. The induction over depths needs the lens (`place.completion`, the gap that closes the rung) |

## Confirms

Hensel's lemma in its first case and the quadratic residues: a unit is a square in ℤ_p iff it is a square mod p (odd p). It is **not** the general lemma (f'(x₀) a unit, for any polynomial): the chart has the square root as a form and the rest as the quadratic formula's JP guard ([[C.quadratic-formula]]). It is **not** p = 2, where a unit is a square iff it is ≡ 1 mod 8 and the root form's radius says so (SPEC §4.4; [[place.radius]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | replaced | at ∞ every positive number has a root; the test at depth one has no analogue |
| J1 | replaced | as classical |
| JH, JO | untested | owed |
| JP | holds | witness |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | EXACT | the squares in (ℤ/p)^× are half the units |
| lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The chart's earlier JP guard on [[alg.sqrt4]] ("the p-adic log of 2 must converge") was too strong a worry and the wrong one: the log of any unit converges after the torsion is split off; the obstruction is the torsion count's parity. At p = 3, 4 is a square and its principal root is −2 ([[alg.sqrt4]]).
