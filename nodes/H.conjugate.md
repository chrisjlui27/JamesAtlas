---
id: H.conjugate
title: The conjugate mirrors the pure part
type: definition
level: object
kind: law
rung: H
order: 1725
setting: JH
equality: "≐"
domain: real
law: "conj(A + Bi + Cj + Dk) := A <([B ; i])> <([C ; j])> <([D ; k])>"
units: "q̄ = a − bi − cj − dk; q + q̄ = 2a; conj(pq) = conj(q) conj(p) — an anti-automorphism (witnessed with the norm, tools/models/h_four_squares.py)"
gloss_check: ""
holds:
  classical: replaced
  J1: replaced
  JH: holds
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
known_since: "Hamilton 1843 ('the conjugate quaternion', K q); at odd p the adjugate of a 2×2 matrix; this rung, 2026-10-07"
entered: 2026-10-07
guide: shape-led
band: "beyond"
uses: [H.central-sign, H.quaternion, Z.subtraction]
see_also: [C.conjugate, H.norm, H.inverse, H.reversal, H.four-squares]
aliases: [quaternion conjugate, q̄, a − bi − cj − dk, the adjugate, conj q]
concepts: [quaternion, negation]
owed: ["2026-10-07: the anti-automorphism conj(pq) = conj(q) conj(p) as a derivation (with H.four-squares)"]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `A <([B ; i])> <([C ; j])> <([D ; k])>` | `A <B·i> <C·j> <D·k>` | q̄ = a − bi − cj − dk |

The quaternion of [[H.quaternion]] with its pure part mirrored: each of the three counts negated ([[Z.subtraction]]). By the central sign ([[H.central-sign]]) `<([B ; i])>` is also `([B ; <i>])` and `([<B> ; i])`: negating the count, negating the unit, or negating the product are one form up to that law, so the conjugate is equally "the quaternion with −i, −j, −k" — which is how it reverses products: conj(pq) = conj(q)·conj(p), the anti-automorphism the witness of [[H.four-squares]] checks exactly and whose derivation on the page is owed (it is [[H.reversal]]'s shape at the level of values). What the conjugate is for: the product of a quaternion with its conjugate is real ([[H.norm]]), which gives the inverse ([[H.inverse]]).

## Plain

Keep the ordinary part, flip the sign of the i, j and k parts. Multiplying a quaternion by its flipped twin gives an ordinary number, and that is how you divide.

## Derivation

| form | rule | note |
|---|---|---|
| `A <([B ; i])> <([C ; j])> <([D ; k])>` | [[Z.subtraction]] | a minus b·i minus c·j minus d·k: the quaternion of [[H.quaternion]] with its three counts mirrored — the sign on the product, which by [[H.central-sign]] is also the sign on the count or on the unit |
| `conj(A + Bi + Cj + Dk)` | name | — |

## Confirms

q + q̄ = 2a: the real part is half the sum, `(A V) (A <V>) ≐ A A` by Inversion, which is the page's reason for calling `A` the real part. At odd p, where the quaternions of the page are 2×2 matrices ([[H.split-place]]), the conjugate is the adjugate — tr(M)·1 − M — and the norm is the determinant: the same law in a matrix dress. It is **not** complex conjugation on each slice independently: the conjugate of a quaternion lies in the slice of its own pure part and mirrors that slice's imaginary axis, so restricted to any one slice C_u it is [[C.conjugate]] with i replaced by u.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | [[C.conjugate]] when C and D are void |
| JH | holds | the definition |
| JO | holds | the octonions have the same conjugation, mirroring seven parts; it is an anti-automorphism there too |
| JP | holds | the quaternions of the page at 2 and at odd p (the adjugate) |

| reading | cell | why |
|---|---|---|
| C | ABSENT | j and k have no value in ℂ |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The chart writes the conjugate's three mirrored counts as `<([B ; i])>` — the negation outside the product — rather than `([<B> ; i])`, so that the norm's derivation can move the signs out with the central sign in one step each; the three spellings are one law apart.
