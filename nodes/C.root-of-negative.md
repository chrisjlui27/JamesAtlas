---
id: C.root-of-negative
title: The square root of a negative is i times the root
type: theorem
level: object
kind: law
rung: C
order: 1017
setting: classical
equality: "≐"
domain: positive
law: "(([[<A>]] <[oo]>)) ≐ ([(([[A]] <[oo]>))] [(([J] <[oo]>))])"
units: "√(−a) = i √a  (a > 0)"
gloss_check: "1j*sqrt(A)"
holds:
  classical: holds
  J1: holds-mod-Λ
  JH: replaced
  JO: replaced
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "Bombelli 1572 for the arithmetic of √−1; Euler 1770 (Elements of Algebra, §147) for √(−a) = √a·√(−1), and 1777 for the letter i"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [alg.root, C.log-of-negative, mult.distribution, mult.involution]
see_also: [alg.root, C.imaginary-unit, C.log-of-negative, alg.root-of-product]
aliases: ["√(−a) = i√a", root of a negative, imaginary root]
concepts: [root, phase, complex-number]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[<A>]] <[oo]>)) ≐ ([(([[A]] <[oo]>))] [(([J] <[oo]>))])` | `√<A> ≐ ([√A] [i])` | √(−a) = √a · i, for a > 0 |

The root schema of [[alg.root]] applied to a mirrored pile: the radicand's half-turn is halved into a quarter-turn, which is i. The textbook's √−4 = 2i, as a theorem.

## Plain

Take the square root of minus a number: it is the square root of the number, times i. Half of a half-turn is a quarter-turn.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[<A>]] <[oo]>))` | given | √(−a): [[alg.root]] with the radicand `<A>` |
| `(([[A] J] <[oo]>))` | [[C.log-of-negative]] | `[<A>] ≐ [A] J` under the outer square (A positive) |
| `(([[A]] <[oo]>) ([J] <[oo]>))` | [[mult.distribution]] | half of a sum is the sum of halves: `(<[oo]> [[A] J]) ≐ (<[oo]> [[A]]) (<[oo]> [J])` |
| `([(([[A]] <[oo]>))] [(([J] <[oo]>))])` | [[mult.involution]] | the unit right to left on each summand, directly inside the instance — absorbing: the instance of a sum is the product of the instances (the exponential law, as a step) — √a times i |

## Confirms

√(−a) = i√a for positive a, the principal root. The derivation is the log of a negative ([[C.log-of-negative]]) halved and split by Distribution — so the law inherits that guard, and with it its scope: for a negative *radicand that is itself the mirror of a positive pile*. It is **not** the rule √(−a)√(−b) = √(ab): that one is false (at a = b = 1 it would equate i·i = −1 with √((−1)(−1)) = √1 = 1), and the forms do not prove it because [[alg.root-of-product]] is stated for positive radicands only; the chart's √ is one-valued, and the other root is the mirror.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds-mod-Λ | inherits the bare unit of [[C.log-of-negative]], here under two squares — nothing absorbs the receipt |
| JH, JO | replaced | one square root of −1 per slice: `(([[<A>]] <[oo]>))` picks the slice of the seed J_u |
| JP | guarded | as [[alg.root]] and [[C.imaginary-unit]]: 2 a unit at p, and i a value at p (p ≡ 1 mod 4) |

| reading | cell | why |
|---|---|---|
| C | EXACT | the principal root |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Euler's *Elements of Algebra* (1770) writes √(−a) = √a·√(−1) in §147 — the letter i is from 1777 — and in §148 commits √(−1)·√(−4) = √4 = 2, the very error the Confirms warns against; the chart's one-valued √ cannot make it.
