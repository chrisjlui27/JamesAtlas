---
id: H.list-distribution
title: Two-sided list distribution
type: axiom
level: object
kind: law
rung: H
order: 1625
setting: JH
equality: "≐"
domain: complex
law: "([A ; B C]) ≐ ([A ; B]) ([A ; C])"
units: "A(B + C) = AB + AC, and (B + C)A = BA + CA: the product distributes over juxtaposition on both sides — ring distributivity, not exp-splitting"
gloss_check: ""
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: holds
  JP: guarded
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "2026-08 (JH report, Layer 3: 'two-sided list distribution — notably two-sided, since what dies in ℍ is exp-splitting, not distributivity')"
entered: 2026-10-07
guide: shape-led
band: "beyond"
uses: [H.ordered-bracket, H.ordered-product, mult.distribution]
see_also: [mult.distribution, H.central-sign, H.zero-entry, H.norm]
aliases: [list distribution, two-sided distribution, ordered distribution, ring distributivity]
concepts: [ordered-product, multiplication]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A ; B C]) ≐ ([A ; B]) ([A ; C])` | an entry that is a sum splits the product into a sum of products — on the right, and (the family) on the left: `([B C ; A]) ≐ ([B ; A]) ([C ; A])` | A(B + C) = AB + AC; (B + C)A = BA + CA |

James's Distribution ([[mult.distribution]]), `(A [B C]) ≐ (A [B]) (A [C])`, is the quaternionic casualty (JH report §3): read in ℍ it fails for generic contents, because what it secretly uses is exp(X + Y) = exp X · exp Y. What survives is distributivity itself — a ring law, true in ℍ on both sides — and the ordered square states it directly: a sum inside an entry distributes the product over the sum. The family runs over the position of the split entry in lists of two or three entries.

## Plain

Multiplying by a sum is the sum of the multiplications, whether the sum is on the left or the right. That much the quaternions keep; what they lose is the trick of turning a product into an exponential of a sum of logs.

## Derivation

none — adjoined, as a rule of the ordered square ([[H.ordered-bracket]]) about its instances ([[H.ordered-product]]); on commuting contents it restricts to [[mult.distribution]].

## Confirms

ℍ is a ring: multiplication distributes over addition on both sides. It is **not** [[mult.distribution]]: that law is the one-slot, slice-pure case, and the trunk's JH cell for it says so (`replaced`).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | [[mult.distribution]], with the single entry read through the counit |
| JH, JO | holds | an axiom of the setting; the octonions distribute too |
| JP | guarded | the page at every place is a ring, and the law is exact wherever its ordered squares have a value ([[H.ordered-bracket]]; census/h-place-ledger.md) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

~~"Distribution survives in ℍ as stated"~~ — refuted in the JH audit (witness A = (π/2)i, B = i, C = j: −1.374 + 0.309i + 0.128j against −1.606 + 0.563i + 0.563j); it survives for real (central) A or co-sliced contents only.

## Notes

With [[H.zero-entry]] (an empty entry is the pole) the central sign [[H.central-sign]] is a theorem of this law, as negation-under-instance was a theorem of Distribution on the trunk.
