---
id: H.norm
title: A quaternion times its conjugate is real
type: theorem
level: object
kind: law
rung: H
order: 1735
setting: JH
equality: "≃"
domain: real
law: "([A ([B ; i]) ([C ; j]) ([D ; k]) ; A <([B ; i])> <([C ; j])> <([D ; k])>]) ≃ ([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])"
units: "q q̄ = a² + b² + c² + d² = N(q) = |q|², and q̄ q = N(q) too (the second table); at odd p the determinant"
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
known_since: "Hamilton 1843 (the 'tensor' T q, with q·Kq = (Tq)²); this rung, 2026-10-07"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.central-sign, H.collapse, H.commutation, H.conjugate, H.list-distribution, H.pure-square, H.quaternion, Z.cancellation, Z.collection, Z.inversion]
see_also: [C.modulus-squared, H.inverse, H.four-squares, H.polar-form, H.split-place]
aliases: [the norm, N(q), q q̄ = N, |q|², a² + b² + c² + d², the reduced norm]
concepts: [quaternion, ordered-product, modulus]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A ([B ; i]) ([C ; j]) ([D ; k]) ; A <([B ; i])> <([C ; j])> <([D ; k])>]) ≃ ([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])` | q·q̄ ≃ a² + b² + c² + d² | q q̄ = N(q) |

Multiply a quaternion ([[H.quaternion]]) by its conjugate ([[H.conjugate]]) and the pure parts cancel: distribution opens the product into `A·A`, the pair `A·V` and `−A·V` — equal because A is real and real counts commute with everything ([[H.commutation]]) — and `−V·V`, which [[H.pure-square]] makes `+(b² + c² + d²)`. Twelve rows, one absorbed collapse (`[A ; A]` to `[A][A]`), the rest strict. The second table runs the other order, `q̄·q`, to the same real number: the norm is **two-sided**, which is what the two-sided inverse ([[H.inverse]]) needs and what the engine's rule for this node offers (both orders license a step, tools/licences.py). At rung `C` the same computation is [[C.modulus-squared]], `z z̄ = a² + b²`; at an odd place the quaternions are matrices and the norm is their determinant ([[H.split-place]]), where it can vanish on a nonzero quaternion — the isotropy that [[H.inverse]] guards against.

## Plain

A quaternion times its flipped twin is an ordinary number: the sum of the squares of its four parts. In either order.

## Derivation

| form | rule | note |
|---|---|---|
| `([A ([B ; i]) ([C ; j]) ([D ; k]) ; A <([B ; i])> <([C ; j])> <([D ; k])>])` | given | q ([[H.quaternion]]) times its conjugate ([[H.conjugate]]), in order |
| `([A ([B ; i]) ([C ; j]) ([D ; k]) ; A]) ([A ([B ; i]) ([C ; j]) ([D ; k]) ; <([B ; i])> <([C ; j])> <([D ; k])>])` | [[H.list-distribution]] | the conjugate split: its real part, and its mirrored pure part |
| `([A ([B ; i]) ([C ; j]) ([D ; k]) ; A]) ([A ([B ; i]) ([C ; j]) ([D ; k]) ; <([B ; i]) ([C ; j])> <([D ; k])>])` | [[Z.collection]] | the three negatives collected — |
| `([A ([B ; i]) ([C ; j]) ([D ; k]) ; A]) ([A ([B ; i]) ([C ; j]) ([D ; k]) ; <([B ; i]) ([C ; j]) ([D ; k])>])` | [[Z.collection]] | — into the negation of V |
| `([A ([B ; i]) ([C ; j]) ([D ; k]) ; A]) <([A ([B ; i]) ([C ; j]) ([D ; k]) ; ([B ; i]) ([C ; j]) ([D ; k])])>` | [[H.central-sign]] | the sign out of the ordered square |
| `([A ; A]) ([([B ; i]) ([C ; j]) ([D ; k]) ; A]) <([A ([B ; i]) ([C ; j]) ([D ; k]) ; ([B ; i]) ([C ; j]) ([D ; k])])>` | [[H.list-distribution]] | q split on the left of A |
| `([A ; A]) ([([B ; i]) ([C ; j]) ([D ; k]) ; A]) <([A ; ([B ; i]) ([C ; j]) ([D ; k])]) ([([B ; i]) ([C ; j]) ([D ; k]) ; ([B ; i]) ([C ; j]) ([D ; k])])>` | [[H.list-distribution]] | q split on the left of V |
| `([A ; A]) ([A ; ([B ; i]) ([C ; j]) ([D ; k])]) <([A ; ([B ; i]) ([C ; j]) ([D ; k])]) ([([B ; i]) ([C ; j]) ([D ; k]) ; ([B ; i]) ([C ; j]) ([D ; k])])>` | [[H.commutation]] | A is real: V·A is A·V |
| `([A ; A]) ([A ; ([B ; i]) ([C ; j]) ([D ; k])]) <([A ; ([B ; i]) ([C ; j]) ([D ; k])])> <([([B ; i]) ([C ; j]) ([D ; k]) ; ([B ; i]) ([C ; j]) ([D ; k])])>` | [[Z.collection]] | the negation distributed |
| `([A ; A]) <([([B ; i]) ([C ; j]) ([D ; k]) ; ([B ; i]) ([C ; j]) ([D ; k])])>` | [[Z.inversion]] | A·V and its negative cancel |
| `([A] [A]) <([([B ; i]) ([C ; j]) ([D ; k]) ; ([B ; i]) ([C ; j]) ([D ; k])])>` | [[H.collapse]] | A beside itself: co-sliced, the ordered square collapses — absorbed |
| `([A] [A]) <<([B] [B]) ([C] [C]) ([D] [D])>>` | [[H.pure-square]] | the pure part squared is minus the sum of three squares |
| `([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])` | [[Z.cancellation]] | minus minus: a² + b² + c² + d² |

The other order:

| form | rule | note |
|---|---|---|
| `([A <([B ; i])> <([C ; j])> <([D ; k])> ; A ([B ; i]) ([C ; j]) ([D ; k])])` | given | the conjugate times q, in order |
| `([A <([B ; i]) ([C ; j])> <([D ; k])> ; A ([B ; i]) ([C ; j]) ([D ; k])])` | [[Z.collection]] | the three negatives collected — |
| `([A <([B ; i]) ([C ; j]) ([D ; k])> ; A ([B ; i]) ([C ; j]) ([D ; k])])` | [[Z.collection]] | — into the negation of V |
| `([A <([B ; i]) ([C ; j]) ([D ; k])> ; A]) ([A <([B ; i]) ([C ; j]) ([D ; k])> ; ([B ; i]) ([C ; j]) ([D ; k])])` | [[H.list-distribution]] | q split on the right |
| `([A ; A]) ([<([B ; i]) ([C ; j]) ([D ; k])> ; A]) ([A <([B ; i]) ([C ; j]) ([D ; k])> ; ([B ; i]) ([C ; j]) ([D ; k])])` | [[H.list-distribution]] | the conjugate split on the left of A |
| `([A ; A]) ([<([B ; i]) ([C ; j]) ([D ; k])> ; A]) ([A ; ([B ; i]) ([C ; j]) ([D ; k])]) ([<([B ; i]) ([C ; j]) ([D ; k])> ; ([B ; i]) ([C ; j]) ([D ; k])])` | [[H.list-distribution]] | the conjugate split on the left of V |
| `([A ; A]) <([([B ; i]) ([C ; j]) ([D ; k]) ; A])> ([A ; ([B ; i]) ([C ; j]) ([D ; k])]) ([<([B ; i]) ([C ; j]) ([D ; k])> ; ([B ; i]) ([C ; j]) ([D ; k])])` | [[H.central-sign]] | the sign out of the first entry |
| `([A ; A]) <([([B ; i]) ([C ; j]) ([D ; k]) ; A])> ([A ; ([B ; i]) ([C ; j]) ([D ; k])]) <([([B ; i]) ([C ; j]) ([D ; k]) ; ([B ; i]) ([C ; j]) ([D ; k])])>` | [[H.central-sign]] | — and of the other |
| `([A ; A]) <([A ; ([B ; i]) ([C ; j]) ([D ; k])])> ([A ; ([B ; i]) ([C ; j]) ([D ; k])]) <([([B ; i]) ([C ; j]) ([D ; k]) ; ([B ; i]) ([C ; j]) ([D ; k])])>` | [[H.commutation]] | A is real: V·A is A·V |
| `([A ; A]) <([([B ; i]) ([C ; j]) ([D ; k]) ; ([B ; i]) ([C ; j]) ([D ; k])])>` | [[Z.inversion]] | A·V and its negative cancel |
| `([A] [A]) <([([B ; i]) ([C ; j]) ([D ; k]) ; ([B ; i]) ([C ; j]) ([D ; k])])>` | [[H.collapse]] | A beside itself collapses — absorbed |
| `([A] [A]) <<([B] [B]) ([C] [C]) ([D] [D])>>` | [[H.pure-square]] | the pure part squared |
| `([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])` | [[Z.cancellation]] | the same real number: the norm is two-sided |

## Confirms

Hamilton's T q (the "tensor", today the norm or modulus squared), real and multiplicative — multiplicativity is [[H.four-squares]]. The computation uses no commutation of i, j, k with each other: the only exchanges are of the real `A` past V, licensed by [[H.commutation]] on values that commute; the non-commutative content is all inside [[H.pure-square]]. It is **not** derived through `([q][q̄])`, the old product, though here that form is legitimate — q and q̄ are co-sliced, so by [[H.collapse]] the ordered square *could* collapse to it, and it reads N(q) exactly — because the collapse would have to be paid at the top of the form, where no instance absorbs it; the ordered derivation never collapses q against q̄ at all.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | [[C.modulus-squared]], the two-square case |
| JH | holds | one absorbed collapse per table, the rest strict (census/h-ledger.md) |
| JO | holds | the octonion norm is q q̄ = q̄ q too (a composition algebra) |
| JP | holds | at 2 the norm of the Hurwitz order, with v(N) = 2 v(q); at odd p the determinant — the same congruence, read on the page (census/h-place-ledger.md) |

| reading | cell | why |
|---|---|---|
| C | ABSENT | j and k have no value in ℂ |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

`N` in the prose is the form `{Nf}`; it is real and nonnegative, and void only when all four parts are void — on the `real` domain it is positive. Its log `[N]` is therefore a real, and `<[N]>` the reciprocal's log: [[H.inverse]].
