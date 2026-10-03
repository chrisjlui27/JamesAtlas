---
id: Q.cross-multiplication
title: Two fractions are equal when their cross products are
type: theorem
level: meta
kind: law
rung: Q
order: 655
setting: classical
equality: ≐
domain: positive
law: "([A] <[B]>) ≐ ([C] <[D]>)  iff  ([A] [D]) ≐ ([C] [B])"
units: a/b = c/d ⟺ ad = cb
witness: tools/models/cross_multiplication.py
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE-BY-DECREE
verified: engine
known_since: Euclid VII (proportion); the fact is ancient
entered: 2026-10-03
guide: need-led
band: 3–5
uses: [Q.division, mult.multiplication, mult.involution, Z.inversion, Q.cancel-common-factor, mult.product-of-numerals, mult.consistency]
see_also: [Q.lowest-terms, Z.normal-form, N.freeness]
aliases: [cross-multiply, proportion, a/b = c/d iff ad = bc]
concepts: [fraction, normal-form]
understood: partial
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A] <[B]>) ≐ ([C] <[D]>)` iff `([A] [D]) ≐ ([C] [B])` | — | a/b = c/d ⟺ ad = cb |

An *iff* is two implications, and an implication between equations is not itself an equation: this is a meta-level law, stated about the calculus. Each direction is a derivation schema.

## Plain

Two fractions are the same number exactly when top-times-other-bottom matches on both sides — the page can run either direction, but "exactly when" is a sentence about the page, not a form on it.

## Derivation

| statement | rule | note |
|---|---|---|
| (⇒) Suppose `([A] <[B]>) ≐ ([C] <[D]>)`. Multiply both sides by `([B] [D])`: on the left, `([([A]<[B]>)] [([B][D])]) ≐ ([A] <[B]> [B] [D]) ≐ ([A] [D])` — two unit steps and one Inversion; on the right, likewise `([C] <[D]> [B] [D]) ≐ ([C] [B])` | [[mult.multiplication]] [[mult.involution]] [[Z.inversion]] | congruence: equals multiplied by equals are equal; the unit steps are on real content |
| (⇐) Suppose `([A] [D]) ≐ ([C] [B])`. Divide both sides by `([B] [D])`: on the left, `([([A][D])] <[([B][D])]>) ≐ ([A] <[B]>)` by [[Q.cancel-common-factor]] with the common factor D; on the right, the same with the common factor B gives `([C] <[D]>)` | [[Q.division]] | congruence again |
| On numerals each side of `([A][D]) ≐ ([C][B])` is a pile by [[mult.product-of-numerals]], and two piles are ≐ iff they have the same count — in the full calculus by [[mult.consistency]]; so equality of fractions of numerals is decidable | — | the fact the lowest-terms gap relies on; it inherits consistency's price |

## Confirms

Euclid's criterion for proportion, and the decidability of equality in ℚ. The chart keeps it meta because its content is an *iff*; each direction's instances are engine-checkable, and the object-level laws it leans on are. It is **not** a canonical form: it decides equality without choosing a representative.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the two directions use only laws that hold in J1 |
| JH, JO | replaced | with two quotients there are two criteria |
| JP | guarded | for unit denominators |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The witness `tools/models/cross_multiplication.py` instantiates both directions on all 1296 numeral quadruples up to 6, checks that the two equalities agree, and runs the engine on each direction's derivation rows — the shape of every future "iff" node's witness.
