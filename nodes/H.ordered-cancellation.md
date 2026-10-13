---
id: H.ordered-cancellation
title: Ordered cancellation
type: theorem
level: object
kind: law
rung: H
order: 1650
setting: JH
equality: "≃"
domain: complex
law: "[A ; B ; (<[B]>) ; C] ≃ [A ; o ; C]"
units: "A·B·B⁻¹·C = A·1·C: a neighbouring pair y, y⁻¹ (in either order) becomes the entry one; at any position of a list of up to five"
gloss_check: ""
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: guarded
  JP: guarded
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "2026-08 (JH report: OC 'added in the repair round after the referee found the original derived inverses circular'); 2026-09-05 (JS-ARITY-AND-IMPORTS: OC at rung four is derivable from Splice and the size-way reciprocal — demoted here from axiom to theorem)"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.collapse, H.splice, Q.reciprocal, Q.reciprocal-law]
see_also: [Q.reciprocal-law, Q.reciprocal, H.splice, H.collapse, H.unit-entry, H.inverse, H.reversal]
aliases: [OC, ordered cancellation, two-sided inverses in a list, y ; y⁻¹ = o, the size-way reciprocal]
concepts: [ordered-product, division]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[A ; B ; (<[B]>) ; C] ≃ [A ; o ; C]` | a neighbouring pair B, B⁻¹ in the row is the entry one; the family covers either order and any position | A B B⁻¹ C = A·1·C |

The JH report adjoined ordered cancellation as an axiom after its referee found the "derived inverses" circular. The chart derives it: the pair is gathered into one entry by [[H.splice]] (read right to left), that entry's two factors are co-sliced — B⁻¹ is `(<[B]>)` ([[Q.reciprocal]]), a power of B, whose log is −log B — so the entry collapses to the classical square by [[H.collapse]], and there [[Q.reciprocal-law]] makes it one. JS-ARITY-AND-IMPORTS called the route "Quadratic + Splice via the size-way reciprocal"; this is it, with the collapse where the size-way reciprocal was. The equality is ≃ because the collapse posts a receipt, paid by the instance the entry sits in — absorbed, so `holds`.

## Plain

A quaternion next to its own reciprocal cancels to one, wherever the pair stands in the row — because a thing and its reciprocal always lie in the same complex plane, where the old rules work.

## Derivation

| form | rule | note |
|---|---|---|
| `[A ; B ; (<[B]>) ; C]` | given | a pair B, B⁻¹ ([[Q.reciprocal]]) in the row |
| `[A ; ([B ; (<[B]>)]) ; C]` | [[H.splice]] | the pair gathered into one entry, right to left |
| `[A ; ([B] [(<[B]>)]) ; C]` | [[H.collapse]] | the logs of B and B⁻¹ commute (B⁻¹ is a power of B): the entry collapses to the classical product — absorbed, inside the entry's instance |
| `[A ; o ; C]` | [[Q.reciprocal-law]] | B × B⁻¹ ≐ o |

## Confirms

Two-sided inverses in ℍ: every nonzero quaternion has one, equal on both sides (the family's other order). It is **not** the four-entry shape alone: the prover's family (`_family_ordered_cancellation`) gives the pair at any position of a list of two to five entries, in either order, each by the same derivation.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | [[Q.reciprocal-law]] |
| JH | holds | absorbed: the collapse's receipt is paid by the entry's instance |
| JO | guarded | in the octonions a pair cancels only when the rest of the list is in its slice — the alternative laws, not associativity (JO-16, owed) |
| JP | guarded | at a finite place the reciprocal exists for the units of the page only: a quaternion whose norm vanishes mod p — the norm-null species ([[H.split-place]]) — has none |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

~~"OC is independent: an axiom of the ordered calculus"~~ — the JH report's own status; refuted 2026-09-05 (JS-ARITY-AND-IMPORTS) and here by derivation.

## Notes

The receipt of the collapse step is k = 1 (about i) at the generic points: log(B·B⁻¹) is the log of exactly one, the period, while log B + log B⁻¹ is void — the same period the trunk's [[Q.reciprocal-law]] pays.
