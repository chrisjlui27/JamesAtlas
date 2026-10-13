---
id: C.omega-sum
title: One plus ω plus ω squared is nothing
type: theorem
level: object
kind: law
rung: C
order: 1035
setting: classical
equality: "≐"
domain: positive
law: "([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) o ≐ void"
units: "1 + ω + ω² = 0, ω = e^{2πi/3}"
gloss_check: "0"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "the relation of the cube roots of unity: Euler 1748 (Introductio); the general cyclotomic polynomial, Gauss 1801"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [C.cube-root-of-unity, mult.multiplication, N.unit, mult.unit-law, Q.self-division, mult.involution, mult.distribution, mult.inverse-promotion, Z.collection, Z.inversion, mult.black-hole, mult.zero-annihilates]
guarded_by: [mult.seam-decree]
see_also: [C.cube-root-of-unity, Q.self-division, alg.irrationality, schema.roots-sum]
aliases: ["1 + ω + ω² = 0", cyclotomic relation, omega sum]
concepts: [root, phase, one, zero]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([ω] [ω]) ω o ≐ void` | with ω = `(([J] [oo] <[ooo]>))` | 1 + ω + ω² = 0 |

The three cube roots of unity sum to nothing — the first cyclotomic relation with a non-real root (the relation for −1, 1 + (−1) = 0, is [[C.euler-identity]]), and the first law of the rung whose two sides are a pile of three complex terms and the void.

## Plain

Take two thirds of a half-turn, its double, and one: the three point in three directions a third of a turn apart, and pull against each other to nothing.

## Derivation

| form | rule | note |
|---|---|---|
| `([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) o` | given | ω² + ω + 1 with ω = `(([J] [oo] <[ooo]>))` ([[C.cube-root-of-unity]]): a product by [[mult.multiplication]], the unit [[N.unit]] |
| `([([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) o] [o])` | [[mult.unit-law]] [[mult.zero-annihilates]] | `A ≐ ([A] [o])`, right to left — and since S is void, `[S]` is the hole and `(□ [o]) ≐ void` by the hole rules, so the row holds outside the unit law's domain too |
| `([([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) o] [([(([J] [oo] <[ooo]>)) <o>] <[(([J] [oo] <[ooo]>)) <o>]>)])` | [[Q.self-division]] | `o ≐ ([B] <[B]>)` with B = `ω <o>` = ω − 1, which is not void — right to left, inside the square |
| `([([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) o] [(([J] [oo] <[ooo]>)) <o>] <[(([J] [oo] <[ooo]>)) <o>]>)` | [[mult.involution]] | the unit on `[(…)]`, directly inside the instance — absorbing (and its content is void besides) |
| `([([([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) o] [(([J] [oo] <[ooo]>)) <o>])] <[(([J] [oo] <[ooo]>)) <o>]>)` | [[mult.involution]] | the unit right to left on `[S] [ω − 1]`, directly inside the instance — absorbing; the content is the hole, since S is void |
| `([([([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) o] [(([J] [oo] <[ooo]>))]) ([([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) o] [<o>])] <[(([J] [oo] <[ooo]>)) <o>]>)` | [[mult.distribution]] | distribute S over `ω <o>` |
| `([([([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) o] [(([J] [oo] <[ooo]>))]) <([([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) o] [o])>] <[(([J] [oo] <[ooo]>)) <o>]>)` | [[mult.inverse-promotion]] | `(C [<o>]) ≐ <(C [o])>` |
| `([([([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) o] [(([J] [oo] <[ooo]>))]) <([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) o>] <[(([J] [oo] <[ooo]>)) <o>]>)` | [[mult.unit-law]] [[mult.zero-annihilates]] | `([S] [o]) ≐ S` — by the hole rules at S void, as in row 2 |
| `([([(([J] [oo] <[ooo]>))] [([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))])]) ([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) ([(([J] [oo] <[ooo]>))] [o]) <([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) o>] <[(([J] [oo] <[ooo]>)) <o>]>)` | [[mult.distribution]] | distribute ω over the three summands of S — Distribution twice |
| `([([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) ([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) <([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) o>] <[(([J] [oo] <[ooo]>)) <o>]>)` | [[mult.involution]] [[mult.unit-law]] | the unit on `[([ω][ω])]` directly inside its instance — absorbing; and `([ω] [o]) ≐ ω` |
| `([o ([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) <([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) o>] <[(([J] [oo] <[ooo]>)) <o>]>)` | [[C.cube-root-of-unity]] | ω³ ≐ o |
| `([o ([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))]) (([J] [oo] <[ooo]>)) <([(([J] [oo] <[ooo]>))] [(([J] [oo] <[ooo]>))])> <(([J] [oo] <[ooo]>))> <o>] <[(([J] [oo] <[ooo]>)) <o>]>)` | [[Z.collection]] | the mirror of the pile is the pile of mirrors, right to left — Collection twice |
| `(□ <[(([J] [oo] <[ooo]>)) <o>]>)` | [[Z.inversion]] | three pairs cancel: (ω − 1)(ω² + ω + 1) is ω³ − 1, which is nothing — and the abstract of nothing is the black hole ([[mult.black-hole]]) |
| `void` | [[mult.zero-annihilates]] | `(□ C) ≐ void`: dividing nothing by ω − 1 leaves nothing |

## Confirms

1 + ω + ω² = 0, proved as the textbook proves it — (ω − 1)(ω² + ω + 1) = ω³ − 1 = 0 and ω ≠ 1 — but with the division made explicit: the sum S is multiplied by (ω − 1)/(ω − 1), which is `o` by [[Q.self-division]], the product collapses to nothing by ω³ ≐ o ([[C.cube-root-of-unity]]) and three Inversions, and `(□ <[ω − 1]>)` is void by the hole rules. The forms do not need "no zero divisors": what carries that weight is the invertibility of ω − 1 — a reading-level fact, ω ≠ 1, of the same kind as [[alg.irrationality]] — together with `(□ C) ≐ void`. The same cancellation for the n-th roots of unity, every n, is [[schema.roots-sum]]. It is **not** a proof that ω is irrational or that it generates a field of degree 2: those are statements about which *other* forms equal `ω`, i.e. about the reading, like [[alg.irrationality]].

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step directly under an instance; the rest exact — except that the last rows route through [[mult.black-hole]] and [[mult.zero-annihilates]], whose J1 cells are untested (the caveat of [[C.phase-rule]]) |
| JH, JO | holds | per slice |
| JP | guarded | 3 a unit at p and ω a value at p (p ≡ 1 mod 3), as [[C.cube-root-of-unity]] |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Guarded by position (Amendment A2): the unit on `[([ω] [ω])]` has content 2 ln ω = 4πi/3, off the strip; it sits directly inside an instance, which absorbs the difference — a seam step, admitted by the decree's position clause, so the law carries the decree in its price while its statement is exact in ℂ.

Every row of this derivation has the value 0 (or passes through the black hole), so the engine's row check is less informative here than usual: it certifies 0 = 0 thirteen times, while the seam check still runs and is what finds the seam step at `[([ω] [ω])]`. That each rewrite is an instance of the cited law is checked by the referee, not the engine (SPEC §3.4). The companion fact that `ω <o>` is not void — needed for the self-division step — is a reading-level fact (ω ≠ 1 in ℂ) of the same kind as [[alg.irrationality]].
