---
id: H.reversal
title: Reversal
type: theorem
level: object
kind: law
rung: H
order: 1655
setting: JH
equality: "≃"
domain: complex
law: "<[A ; B]> ≃ [(<[B]>) ; (<[A]>)]"
units: "−log(AB) ≡ log(B⁻¹A⁻¹) mod Λ: the inverse of a product reverses the order — the anti-automorphism, sound modulo the seam"
gloss_check: ""
holds:
  classical: replaced
  J1: replaced
  JH: holds-mod-Λ
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
known_since: "2026-08 (JH report, Layer 3: 'reversal <[x₁;…;xₙ]> ≐ [(<[xₙ]>) ; … ; (<[x₁]>)] (the anti-automorphism, sound modulo the seam)')"
entered: 2026-10-07
guide: shape-led
band: "beyond"
uses: [H.ordered-cancellation, H.splice, H.unit-entry, J1.unit, Q.reciprocal]
see_also: [Q.reciprocal-of-product, H.ordered-cancellation, H.conjugate, H.seam-guard]
aliases: [reversal, the anti-automorphism, (AB)⁻¹ = B⁻¹A⁻¹, "<[x₁;…;xₙ]> = [xₙ⁻¹;…;x₁⁻¹]"]
concepts: [ordered-product, division]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `<[A ; B]> ≃ [(<[B]>) ; (<[A]>)]` | the mirror of an ordered log is the log of the reversed reciprocals | (AB)⁻¹ = B⁻¹A⁻¹, mod the period |

The trunk's [[Q.reciprocal-of-product]] says 1/(AB) = (1/A)(1/B) and does not care about order; in ℍ the order reverses. The derivation inserts the pair (AB), (AB)⁻¹ by [[H.ordered-cancellation]] read right to left, splices AB open, cancels A against A⁻¹ and B against B⁻¹, and is left with the log of (AB)⁻¹ under one unit step: the equality is mod Λ, as the report says — "sound modulo the seam" — and the receipt prover posts the two unit steps at depth 0.

## Plain

To undo "first a, then b" you undo b, then a. The order flips when you take reciprocals, and the chart proves it by making the pair appear and cancel.

## Derivation

| form | rule | note |
|---|---|---|
| `[(<[B]>) ; (<[A]>)]` | given | the reversed reciprocals ([[Q.reciprocal]] is the shape of each) |
| `[(<[B]>) ; (<[A]>) ; o]` | [[H.unit-entry]] | the entry one adjoined, right to left |
| `[(<[B]>) ; (<[A]>) ; ([A ; B]) ; (<[([A ; B])]>)]` | [[H.ordered-cancellation]] | the pair (AB), (AB)⁻¹ created in its place, right to left |
| `[(<[B]>) ; (<[A]>) ; A ; B ; (<[([A ; B])]>)]` | [[H.splice]] | AB spliced open |
| `[(<[B]>) ; o ; B ; (<[([A ; B])]>)]` | [[H.ordered-cancellation]] | A⁻¹, A cancel |
| `[(<[B]>) ; B ; (<[([A ; B])]>)]` | [[H.unit-entry]] | the entry one struck |
| `[o ; (<[([A ; B])]>)]` | [[H.ordered-cancellation]] | B⁻¹, B cancel |
| `[(<[([A ; B])]>)]` | [[H.unit-entry]] | one entry left: the square |
| `<[([A ; B])]>` | [[J1.unit]] | the unit at depth 0: posted (receipt 0 at the generic points; the seam is the exception) |
| `<[A ; B]>` | [[J1.unit]] | the unit again, inside the angle: posted |

## Confirms

The anti-automorphism q ↦ q⁻¹ (and q ↦ q̄, [[H.conjugate]]) of ℍ reverses products. It is **not** strict: the two unit steps post, and on the seam — AB a negative real — the log of (AB)⁻¹ is not minus the log of AB but differs by a period, which is exactly what ≃ allows.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | [[Q.reciprocal-of-product]], where order does not exist |
| JH | holds-mod-Λ | two posted unit steps |
| JO | guarded | needs ordered cancellation at every position, which the octonions grant only in a slice |
| JP | guarded | for units of the page whose reciprocals and logs exist ([[H.split-place]]), and off the seam: the negated logs land on the pinned direction, and the ledger reads `seam` at the odd places and `none` at 2 ([[H.collapse]], JP; census/h-place-ledger.md) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

Stated for two entries; the n-entry reversal follows by the same moves, pair by pair.
