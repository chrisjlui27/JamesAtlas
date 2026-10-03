---
id: C.phase-rule
title: The phase rule — negation is multiplication by minus one
type: theorem
level: object
kind: law
rung: C
order: 930
setting: classical
equality: "≐"
domain: complex
law: "<A> ≐ ([A] J)"
units: "−a = e^{ln a + iπ} = a · (−1)"
gloss_check: "-A"
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James, Chapter 4: 'negative cardinality')"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [C.phase, void.page, Z.inversion, mult.unit-law, mult.distribution, mult.black-hole, mult.zero-annihilates]
see_also: [C.log-of-negative, mult.cardinality, mult.product-of-negatives]
aliases: [phase rule, negative cardinality, "−a = a · (−1)", "<A> = ([A] J)"]
concepts: [phase, negation, multiplication]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `<A> ≐ ([A] J)` | `<A> ≐ ([A] [<o>])` | −a = a · (−1) = e^{ln a + iπ} |

Negation is multiplication by −1: the mirror is a *count* of −1, read through [[mult.cardinality]] with the count mirrored. Equivalently, negation is a half-turn of phase. James calls this negative cardinality; the chart takes it as the phase rule.

## Plain

Minus a number is the number times minus one — and times minus one is "add the log of minus one under the circle": a half-turn.

## Derivation

Directly, by creating the pair `A <A>` beside the product and collecting:

| form | rule | note |
|---|---|---|
| `([A] J)` | given | A with count −1, [[C.phase]] |
| `([A] [<o>]) void` | definition | unfold J; and `A ≐ A void` by [[void.page]], right to left |
| `([A] [<o>]) A <A>` | [[Z.inversion]] | create the pair `A <A>` |
| `([A] [<o>]) ([A] [o]) <A>` | [[mult.unit-law]] | `A ≐ ([A][o])`, right to left |
| `([A] [<o> o]) <A>` | [[mult.distribution]] | collect the two instances sharing the context `[A]` |
| `([A] [void]) <A>` | [[Z.inversion]] | `<o> o` cancels |
| `([A] □) <A>` | [[mult.black-hole]] | — |
| `void <A>` | [[mult.zero-annihilates]] | `(X □) ≐ void` |
| `<A>` | [[void.page]] | — |

## Confirms

(−1)·a = −a, derived as in a first algebra course (a + (−1)a = (1 + (−1))a = 0·a = 0). No unit step anywhere: the phase rule is exact on all of ℂ×, and it is the bridge from the additive mirror to the multiplicative phase. What it is **not**: `[<A>] ≐ [A] J`, the same law under a square, which *does* need a unit step and is the next node.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | no Λ-step in the derivation; it routes through [[mult.zero-annihilates]] and [[mult.black-hole]], whose J1 cells are untested, and through [[Z.inversion]] (guarded) — the survival ledger asserts the Phase rule directly, and an independent J1 derivation is owed, as for [[mult.inverse-promotion]] |
| JH, JO | replaced | the phase rule is slice-local in ℍ: `<A> ≐ ([A] J_u)` for *every* direction u when A is real, only for the content's own slice otherwise (the rigidity dichotomy, JH-12); the portable carrier of −1 there is the central sign, not J |
| JP | holds | the Phase rule is Book One's and the audit at a place passes |

| reading | cell | why |
|---|---|---|
| C | EXACT | exact on ℂ× |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Domain `complex` (widened 2026-10-03, C referee pass): rung C instantiates this law at complex content, and under the chart's citation discipline ([[mult.consistency]], Confirms) a law may be cited only inside its declared domain; every row of its derivation is exact on ℂ×, as the engine confirms. The law's home band and reading are unchanged.
