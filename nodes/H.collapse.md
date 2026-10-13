---
id: H.collapse
title: Co-sliced entries collapse to the square
type: axiom
level: object
kind: law
rung: H
order: 1635
setting: JH
equality: "≃"
domain: slice
law: "[P ; Q] ≃ [P] [Q]"
units: "PREMISE the logs of P and Q commute — log(PQ) = log P + log Q mod Λ when log P and log Q lie in one slice: the classical calculus is the co-sliced fragment (JH-4, the Slice Principle); a conditional law, its premise checked at each use; a witnessed step, posting a receipt by position"
gloss_check: ""
holds:
  classical: replaced
  J1: replaced
  JH: holds-mod-Λ
  JO: holds-mod-Λ
  JP: guarded
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "2026-08 (JH report, Layer 3: 'a conditional commutative-collapse rule, which recovers classical James algebra exactly on co-slicing contents'; JH-4 the Slice Principle)"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.ordered-bracket, J1.unit, alg.log-law, mult.multiplication]
see_also: [alg.log-law, mult.multiplication, H.commutation, H.no-go, H.ordered-cancellation, J1.unit]
aliases: [the collapse, comm-collapse, the Slice Principle, JH-4, co-sliced contents, slice-pure]
concepts: [ordered-product, multiplication, period]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[P ; Q] ≃ [P] [Q]` **when the logs of P and Q commute** — when both lie in one slice C_u | log(PQ) ≡ log P + log Q mod Λ_u | the log law of a commutative algebra, restricted to a slice |

The trunk's log law ([[alg.log-law]]) says `[([A][B])] ≐ [A][B]`: the log of a product is the sum of the logs, mod the period. In ℍ it survives on each slice — C_u = ℝ + ℝu is a copy of ℂ with J → J_u, and inside it the whole classical calculus holds verbatim (the Slice Principle, JH-4) — and fails across slices ([[H.no-go]]). The collapse is that fact as a rule: an ordered square whose entries' logs commute *collapses* to the classical square. The rule is **conditional**, like [[H.commutation]], and its premise is stronger: it is the logs that must commute, not the values — the pinned log of a negative real lies in the slice of i, so `[<o> ; j]` does not collapse to `[<o>] [j]` (the values −1 and j commute; the pinned logs πi and (π/2)j do not, and the two sides differ: `([<o> ; j])` is −j while `([<o>] [j])` is exp(πi + (π/2)j) ≈ −0.93 − 0.32i − 0.16j, a unit in the direction of 2i + j). And it is **witnessed**: log(PQ) and log P + log Q differ by a lattice element even on a slice (the receipt of [[J1.unit]]), so a collapse posts a receipt by position exactly as the unit does — absorbed directly inside an instance, posted at depth 0, an import under a square (SPEC §7.3).

## Plain

If two quaternions live in the same complex plane inside ℍ, they multiply like complex numbers, and the ordered box may be replaced by the old pair of boxes — up to a whole turn, as always.

## Derivation

none — adjoined: the log law [[alg.log-law]] read on a slice, stated for the ordered square ([[H.ordered-bracket]]) and the classical product ([[mult.multiplication]]), with the unit's receipt ([[J1.unit]]). The engine checks the premise at every use and grades the step by position.

## Confirms

The Slice Principle: the embedding x + iy ↦ x + yu carries ℂ onto C_u with its branch cut and period lattice, so every trunk law holds there with J → J_u. It is **not** a congruence through the ordered square's position: a collapse under a further square is an import, as a unit step is.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | [[alg.log-law]]: there is only one slice |
| JH | holds-mod-Λ | an axiom of the setting; ≃ by its own receipt |
| JO | holds-mod-Λ | on a slice of the octonions likewise |
| JP | guarded | on a slice of the page, mod the place's period — except on the seam, which at a finite place has positive measure: a product of co-sliced units is a negative principal unit as often as not, and its log is pinned to the direction i (LEGISLATION 31) while the sum of the two logs lies in the slice: the two sides then differ by a seam displacement, which only a paying instance absorbs ([[H.seam-guard]]); the ledger reads `seam` at every place (census/h-place-ledger.md) |

| reading | cell | why |
|---|---|---|
| C | EXACT | the premise always holds; the law is the log law |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

~~"the premise is that P and Q commute"~~ — refuted while drafting [[H.norm]] (2026-10-07): −1 and j commute, and `[<o> ; j] ≃ [<o>] [j]` is false in the pinned reading (log(−j) = −(π/2)j against πi + (π/2)j); the premise is on the logs.

## Notes

The domain of the law is `slice`: the engine samples both entries in one random slice, where the premise holds; the `law:` field carries the equation and the `units:` field the premise (SPEC §6.4). The premise function (`tools/quat.py`, `premise("cosliced")`) evaluates the two logs and tests their commutator.
