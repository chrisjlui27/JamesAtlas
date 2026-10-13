---
id: place.completion
title: The limit of the pages is not yet a form
type: gap
level: meta
kind: gap
rung: place
order: 1590
setting: JP
equality: "≡"
domain: natural
law: "GAP — ℤ_p is the compatible tower of the pages at every depth; the chart has the pages and not the tower: a doll with a shell at every depth, a re-entry's limit, and the lens that reads a form to n shells as a form of its own are all owed"
units: "ℤ_p = lim ℤ/p^n; the lens {n A} (JP v0.2) and the ordered lens [x ; y] (2026-09-19); completion as a rule, not a construction"
gloss_check: ""
holds:
  classical: fails
  J1: fails
  JH: fails
  JO: untested
  JP: fails
readings:
  C: ABSENT
  finset: PARTIAL
  lambda: untested
  CC: untested
  logic: untested
status: ABSENT
verified: hand
known_since: "2026-09-14 (JP v0.2: the LENS boundary {n A} with rules L1–L8; re-entry systems JP-3); 2026-09-19 ('completion has to enter as a rule; the natural place is the lens'); the ordered lens [x ; y] settled as the notation to fix first"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: []
see_also: [N.induction, place.doll, place.geometric-doll, place.lift, place.two-ends]
aliases: [completion, the lens, {n A}, the ordered lens, ℤ_p as a tower, the infinite doll, JP-2, JP-3]
concepts: [place, induction, zero]
owed: ["2026-10-13: whether the ordered square `[x ; y]` of rung H is the lens of this gap — to be settled at `analysis` or `J2`"]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| the chart's finite pages do not contain their limit: no form on the page is a p-adic integer with a shell at every depth, and no rule makes a compatible tower of readings one form | — | ℤ_p = lim ℤ/p^n; a p-adic number is an infinite doll |

Every law of this rung is at a depth. The doll ([[place.doll]]) has finitely many shells; the geometric doll ([[place.geometric-doll]]) is the sum below the depth; the lift ([[place.lift]]) doubles the depth and never ends. The limit — the one p-adic integer that all the pages agree on, ℤ_p = lim ℤ/p^n — is not on any page. The JP ledger met this twice: the re-entry `x ≐ A ([p][x])` names a doll by an equation, and finite re-entry systems name only countably many (the rationals and the algebraic points, by Newton), so completion "has to enter as a rule"; the **lens** `{n A}` — observe A to n shells — was proposed as that rule (JP v0.2, L1–L8), a boundary that reads a form at a resolution, with a compatible tower of readings counting as a form; and the *ordered* lens `[x ; y]` was settled as the notation to fix first (2026-09-19), because it also carries the ordered bracket of rung `H`. The chart does not yet draw it.

## Plain

The pages show a p-adic number to one, two, three decimal places. The number itself, with all its places, is not on any page — and the rule that would say "all the pages at once" has not been written.

## Derivation

none — a gap.

## Plan

| field | content |
|---|---|
| candidate form(s) | (i) the lens as a boundary, `{n A}` — observe A to n shells — with the void pile as its depth and the rules L1–L8 of JP v0.2 (`( )` gains a shell, `[ ]` spends one, obligations as lens equations); (ii) the ordered lens `[x ; y]` of 2026-09-19, one notation for the lens and for rung `H`'s ordered bracket; (iii) no new boundary: a re-entry `x ≐ A ([p][x])` names the doll and the completion is a decree on re-entries alone (JP-1/JP-3) — refuted as the whole answer (finite re-entry systems are countable), kept as the nameable part |
| law(s) to add, and type | a completion decree: a compatible tower of readings `{n A}`, one at every depth, is a form; the re-entry convention JP-1/JP-3 as a theorem of the lens (a guarded cycle settles one shell per pass; an unguarded one oscillates — the LoF imaginary value, which the mirror already shows at [[place.torsion]]) |
| nativity criterion | the tower must be a form the rewrite rules act on, not a limit the reading takes: [[place.lift]]'s doubling and [[place.geometric-doll]]'s unfolding must become derivations at every depth at once, with the depth a count on the page |
| refutation test | a law true at every depth n whose tower form is not a form under the candidate: the geometric doll's limit, 1/(1 − p), must be reachable; if the lens cannot state Hensel's lemma for x² = a as one derivation, the candidate is not the completion |
| meta-move? | yes — the same meta-move as the schema machinery's ([[N.induction]]): a law at every depth, and the passage to the tower; the lens would make the depth a boundary where the schema keeps it a parameter |
| owner thread | p-adic-wall (the JP ledger: v0.2 lens, 2026-09-19 ordered lens); this chart, rung `H` for the ordered bracket |
| rank | second of the rung's two open items, after the derivation owed to [[place.fermat]]; it lands with `H` if the ordered lens serves both |

## Confirms

That the chart is honest about what it has: residues, dolls to a depth, roots to a depth, and the same wall at every depth. It is **not** a limitation of the reading at p — `tools/place.py` reads any depth — but of the *forms*: no form is a tower.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | fails | ∞ has the same gap in another dress: the real numbers are also limits the page does not draw ([[alg.irrationality]]: √2 is reached by a form only because the root form is one) |
| JO | untested | the quaternionic dolls converge (JP v0.3); owed |
| JH | fails | the same gap: no form is a tower of quaternion pages either; at 2 the tower runs in half-shells and the quaternionic dolls converge (JP v0.3), but a tower is not a form ([[H.ramified-place]]) |
| JP | fails | the gap |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | PARTIAL | each page is a finite set; the tower is not |
| lambda, CC, logic | untested | — |

## Refuted readings

~~"every p-adic number is a re-entry"~~ — refuted 2026-09-19.

## Notes

Priced as a gap: nothing on the chart depends on it, and the laws that approach it ([[place.lift]], [[place.geometric-doll]]) are stated at a depth.
