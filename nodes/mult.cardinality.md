---
id: mult.cardinality
title: Cardinality — repetition is a form
type: theorem
level: object
kind: schema
rung: mult
order: 360
setting: classical
equality: "≐"
domain: complex
law: "A A ≐ ([A] [oo])"
units: "a + a = 2a ; in general n copies of A ≐ ([A][o^n])"
gloss_check: "2*A"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James)"
entered: 2026-10-03
guide: shape-led
band: "3–5"
uses: [mult.distribution, mult.unit-law, mult.involution, void.space]
see_also: [mult.product-of-numerals, mult.square-is-product, mult.exponentiation, schema.cardinality]
aliases: [Cardinality, repetition, scalar multiple, "n·A"]
concepts: [multiplication, counting]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `A A ≐ ([A] [oo])` | — | a + a = 2a |
| `A A … A` (n) | `([A][n])` | n copies of A = n·a |

Repetition itself becomes a form: n copies of `A` standing together may be written as one copy of `A` with a count. The same mechanism one level deeper gives powers ([[mult.square-is-product]]).

## Plain

"Two of a thing" can be written as the thing with a count attached — and the count is an ordinary pile.

## Derivation

| form | rule | note |
|---|---|---|
| `([A] [oo])` | given | A with count 2 |
| `([A] [o o])` | definition | the pile 2 |
| `([A] [o]) ([A] [o])` | [[mult.distribution]] | distribute over the two units |
| `([A]) ([A])` | [[mult.unit-law]] | `[o] ≐ void` |
| `A A` | [[mult.involution]] | strip the instance-of-abstract, twice; regroup by [[void.space]] |

## Confirms

n·a as a form, and with it the possibility of *fractional* and *negative* counts — `([A]<[oo]>)` will be a/2 at rung Q, and fractional counts of J give the roots of unity at rung C. In J1, cardinality `([A][n])` is read as the graded exponential `!ₙ` (contraction priced by a count). It is **not** a new axiom: James's "cardinality" is a theorem schema of Distribution and Involution — this node is its first instance, n = 2, and [[schema.cardinality]] is the statement for every n with James's own induction (p. 27).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | survival ledger: cardinality unchanged; `([A][n])` read as the graded exponential `!ₙ` (the notes write it `(n[A])`) |
| JH, JO | holds | per slice |
| JP | holds | counts that are piles are forms at every place; a *fractional* count `<[o^n]>` needs n to be a unit at p (rung Q), and the selection `d | p−1` of which `ω/d` exist at p is rung C's |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | EXACT | n copies of a set is its product with an n-set |
| logic | ABSENT | — |
| lambda, CC | untested | the ψ-operations of the λ-road act *through* cardinality (`ψ^r` = cardinality-power); the first place the (b) road touches the trunk |

## Refuted readings

none

## Notes

James's Theorem 1 (Ch. 4 §4.4, p. 27): "Multiple references in the same context may be reduced to a single reference with multiple units signifying its quantity, as A…A = ([A][o…o])", proved for 2 and then by the induction step `A…AA = ([A][o…o])([A][o]) = ([A][o…oo])` — the schema over n is an induction in the thesis too, which is the chart's [[N.induction]] gap. "Cardinality applies at any depth" (p. 27) is the congruence rule, and "everything has a count of one, A = ([A]) = ([A][o])" is [[mult.unit-law]] read backwards.

Domain `complex` (widened 2026-10-03, C referee pass): rung C instantiates this law at complex content, and under the chart's citation discipline ([[mult.consistency]], Confirms) a law may be cited only inside its declared domain; every row of its derivation is exact on ℂ×, as the engine confirms. The law's home band and reading are unchanged.
