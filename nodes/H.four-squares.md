---
id: H.four-squares
title: The norm of a product is the product of the norms
type: theorem
level: meta
kind: law
rung: H
order: 1745
setting: JH
equality: "≡"
domain: real
law: "N(([P ; Q])) ≡ ([N(P)] [N(Q)]): the norm of an ordered product is the product of the norms — a sum of four squares times a sum of four squares is a sum of four squares (Euler 1748)"
units: "(a² + b² + c² + d²)(e² + f² + g² + h²) = (ae − bf − cg − dh)² + (af + be + ch − dg)² + (ag − bh + ce + df)² + (ah + bg − cf + de)²"
gloss_check: ""
witness: tools/models/h_four_squares.py
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
known_since: "Euler 1748 (letter to Goldbach, 4 May: the four-square identity); Hamilton 1843 (T(pq) = Tp·Tq); Lagrange 1770 (every natural number is a sum of four squares — re-proved by Hurwitz 1896 with the units of [[H.hurwitz-units]], the seal the ROADMAP owes); this rung, 2026-10-07"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.commutation, H.conjugate, H.norm, H.splice]
see_also: [H.hurwitz-units, H.twenty-four, C.modulus-of-polar, H.inverse, H.octonion-gap]
aliases: [Euler's four-square identity, N(pq) = N(p) N(q), the norm is multiplicative, composition of sums of four squares, Hamilton's modulus theorem]
concepts: [quaternion, modulus, ordered-product]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| N(p·q) = N(p)·N(q), with N the norm of [[H.norm]] — so the product of two sums of four squares is a sum of four squares, with the four squares given by the parts of `([P ; Q])` | — | Euler's identity; Hamilton's modulus theorem |

The chain is short and every link is a law of the rung: N(pq) = (pq)(pq)‾ = p q q̄ p̄ = p N(q) p̄ = N(q) p p̄ = N(p) N(q) — the conjugate of a product is the product of the conjugates reversed, q q̄ is the real N(q) ([[H.norm]]), a real commutes out ([[H.commutation]]), and splice ([[H.splice]]) regroups. The one link not yet a node is the first, conj(pq) = conj(q) conj(p); it is checked exactly by the witness (with the two-sided norm, 100 random rational quaternions, no rounding) and its derivation on the page is owed — it is [[H.reversal]]'s shape for the conjugate, and the ROADMAP lists it. Read as an identity of integers it is Euler's: the sixteen products of the parts regroup into four squares, which is why the sums of four squares are closed under multiplication and why Lagrange's theorem reduces to the primes.

## Plain

The size of a product is the product of the sizes. Written out in the four parts it says that a sum of four squares times a sum of four squares is again a sum of four squares, and shows which four.

## Derivation

| statement | rule | note |
|---|---|---|
| N(pq) = (pq)(pq)‾ | [[H.norm]] | the norm as q q̄ |
| (pq)‾ = q̄ p̄ | — | the conjugate reverses products: witness part (c); the page derivation is owed ([[H.conjugate]]) |
| p (q q̄) p̄ = p N(q) p̄ | [[H.norm]], [[H.splice]] | regrouped: q q̄ is the real N(q) |
| = N(q) p p̄ = N(q) N(p) | [[H.commutation]], [[H.norm]] | a real commutes with p; p p̄ is N(p) |

## Confirms

That ℍ is a *composition* algebra: its norm composes with its product, as |zw| = |z||w| in ℂ ([[C.modulus-of-polar]]) and, one rung on, as the eight-square identity in the octonions (Degen 1818) — and Hurwitz's theorem that 1, 2, 4, 8 are the only dimensions in which this happens is the fence around [[H.octonion-gap]]. The Hurwitz units ([[H.hurwitz-units]]) are the elements of norm one, closed under the product by this law. It is **not** an identity of the old product: `([P][Q])` has no value for generic P, Q ([[H.no-go]]), and the identity is about the ordered one.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | the two-square identity (Brahmagupta–Fibonacci), \|zw\| = \|z\|\|w\| |
| JH | holds | the witness: exact over ℚ-quaternions, 100 random pairs, both orders |
| JO | holds | the octonions compose too (the eight-square identity) |
| JP | holds | the determinant is multiplicative at odd p; at 2 the norm of the division algebra is multiplicative and v(pq) = v(p) + v(q) ([[H.ramified-place]]) |

| reading | cell | why |
|---|---|---|
| C | ABSENT | j and k have no value in ℂ |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The witness checks three things exactly: N(pq) = N(p)N(q) and N(qp) = N(p)N(q) on 100 random pairs of rational quaternions; q q̄ = q̄ q = N(q) as quaternions (not only as numbers); and conj(pq) = conj(q) conj(p). Status NATIVE because every link but one is a law of the rung and the one is witnessed exactly; the owed derivation of the anti-automorphism would make the node object-level.
