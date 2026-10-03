---
id: mult.inverse-promotion
title: Inverse promotion
type: theorem
level: object
kind: law
rung: mult
order: 450
setting: classical
equality: "≐"
domain: real
law: "<(A [B])> ≐ (A [<B>])"
units: "−(e^a · b) = e^a · (−b)"
gloss_check: "-(exp(A)*B)"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "1993 (James)"
entered: 2026-10-03
guide: shape-led
band: "6–8"
uses: [mult.distribution, mult.zero-annihilates, Z.inversion, void.page, void.space]
see_also: [Z.collection, mult.product-of-negatives]
aliases: [inverse promotion, "−(xy) = x(−y)", sign through a product]
concepts: [negation, multiplication]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `<(A [B])> ≐ (A [<B>])` | — | −(e^a · b) = e^a · (−b) |
| `<([X] [B])> ≐ ([X] [<B>])` | — | −(x · y) = x · (−y) |

A mirror outside a product may be *promoted* onto one factor inside it. This is how negatives enter multiplication: `<A>` is `−1 × A` only after this law, when the phase element J arrives.

## Plain

A minus sign in front of a product can be moved onto either factor.

## Derivation

First, `(A [B]) (A [<B>]) ≐ void`:

| form | rule | note |
|---|---|---|
| `(A [B]) (A [<B>])` | given | — |
| `(A [B <B>])` | [[mult.distribution]] | collect — Distribution right to left |
| `(A [void])` | [[Z.inversion]] | `B <B>` cancels |
| `(A [])` | [[void.page]] | — |
| `void` | [[mult.zero-annihilates]] | `(A □) ≐ void` |

So `(A [<B>])` is an inverse of `(A [B])`; inverses are unique:

| form | rule | note |
|---|---|---|
| `<(A [B])>` | given | — |
| `<(A [B])> (A [B]) (A [<B>])` | [[Z.inversion]] | create — the pair just shown to be void, regrouped by [[void.space]] |
| `(A [<B>])` | [[Z.inversion]] | cancel `(A [B]) <(A [B])>` |

## Confirms

−(xy) = x(−y) = (−x)y, the law that lets signs move through products, derived from the ring axioms exactly as a first algebra course does (via x·0 = 0). In JH this law *is* the scalar equivariance of the braid action (JH-7). It is **not** the phase rule `<A> ≐ ([A] J)` — that needs the logarithm of −1, rung C.

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | holds | the Inversion cluster, verbatim in every extension (JH Ch. 15) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | untested | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
