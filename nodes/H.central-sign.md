---
id: H.central-sign
title: The central sign
type: theorem
level: object
kind: law
rung: H
order: 1645
setting: JH
equality: "≡"
domain: complex
law: "([A ; <B>]) ≡ <([A ; B])>"
units: "A·(−B) = −(A·B), and (−A)·B = −(A·B): the sign is central and comes out of any position"
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
known_since: "2026-08 (JH report, Layer 3: 'central sign ([x⃗ ; <y> ; z⃗]) ≐ <([x⃗ ; y ; z⃗])>'; JH-9, negation as slotwise phase, derivable from Inverse Promotion alone — here from list distribution)"
entered: 2026-10-07
guide: shape-led
band: "beyond"
uses: [H.list-distribution, H.zero-entry, Z.inversion, mult.hole-instance]
see_also: [mult.inverse-promotion, C.phase-under-instance, H.list-distribution, H.k-squared, H.phase-sphere]
aliases: [central sign, JH-9, negation as slotwise phase, the portable carrier of −1, sign promotion in a list]
concepts: [ordered-product, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A ; <B>]) ≡ <([A ; B])>` | a mirror on an entry is a mirror on the product; the family: any entry of a list of two or three | A(−B) = −(AB) = (−A)B |

The trunk's [[mult.inverse-promotion]] promotes a mirror out of a classical product; the ordered calculus does the same from any entry, and the reason is distribution: `([A ; B]) ([A ; <B>])` is `([A ; B <B>])` by [[H.list-distribution]], the entry cancels to the void by [[Z.inversion]], the empty entry is the pole ([[H.zero-entry]]) and its instance is void ([[mult.hole-instance]]). So the two products are mirrors of each other. The JH report's point (JH-12, the rigidity dichotomy) is that *this* is the portable carrier of −1 in ℍ — the mirror — while the phase rule `<A> ≐ ([A] J)` of the trunk ([[C.phase-rule]]) is slice-local: J = πi negates only what lies in the slice of i, and a general A is negated by its own J_u ([[H.phase-sphere]]).

## Plain

A minus sign anywhere in the ordered row can be pulled out in front of the whole product. The sign commutes with everything, even in the quaternions.

## Derivation

| form | rule | note |
|---|---|---|
| `([A ; <B>])` | given | the product with a mirrored entry |
| `([A ; <B>]) ([A ; B]) <([A ; B])>` | [[Z.inversion]] | a pair created beside it |
| `([A ; B <B>]) <([A ; B])>` | [[H.list-distribution]] | the two products collected: the entry `B <B>` |
| `([A ; void]) <([A ; B])>` | [[Z.inversion]] | the entry cancels |
| `(□) <([A ; B])>` | [[H.zero-entry]] | the empty entry is the pole |
| `<([A ; B])>` | [[mult.hole-instance]] | the instance of the pole is void |

The mirrored entry in the other position, `([<A> ; B]) ≐ <([A ; B])>`, has the same derivation with the roles exchanged; the three-entry shapes follow by splice from these two, and the prover's family states them.

## Confirms

−1 is central in ℍ: (−1)q = q(−1) = −q. It is **not** the phase rule: `([A] J)` negates A only in the slice of i ([[H.phase-sphere]]); the mirror negates everything.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | [[mult.inverse-promotion]] |
| JH | holds | strict: distribution, inversion, the hole rules |
| JO | holds | the octonions have a central −1 too |
| JP | guarded | at every place, exact wherever the ordered squares have a value ([[H.ordered-bracket]]; census/h-place-ledger.md) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The k² derivation of [[H.k-squared]] uses this law twice and no J-cancellation at all — the JH repair round's rebuilt route.
