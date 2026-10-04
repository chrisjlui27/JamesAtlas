---
id: mult.square-is-product
title: A square is a product
type: theorem
level: object
kind: law
rung: mult
order: 380
setting: classical
equality: "≐"
domain: positive
law: "(([[A]] [oo])) ≐ ([A] [A])"
units: "a² = a · a"
gloss_check: "A*A"
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
  logic: untested
status: NATIVE
verified: engine
known_since: "1993 (James)"
entered: 2026-10-03
guide: shape-led
band: "6–8"
uses: [mult.exponentiation, mult.cardinality, mult.multiplication]
see_also: [schema.power]
aliases: [squaring, "a^2 = a·a", powers as repeated multiplication]
concepts: [exponentiation, multiplication]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[A]] [oo])) ≐ ([A] [A])` | — | a² = a · a |

Cardinality applied one level down: two copies of `[A]` collect into `[A]` with count 2, and the instance of either is the square.

## Plain

A number squared is the number times itself — the power recipe and the times recipe give the same thing.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[A]] [oo]))` | [[mult.exponentiation]] | a ^ 2 |
| `([A] [A])` | [[mult.cardinality]] | inside the outer instance, `([[A]][oo]) ≐ [A] [A]` — cardinality with `[A]` as the repeated form |

The result `([A][A])` is a × a by [[mult.multiplication]].

## Confirms

a^n = a·a·…·a for natural n — repeated multiplication is cardinality one level deeper, exactly as multiplication is cardinality of addition. The law of exponents a^{m+n} = a^m a^n is the same observation and will follow at rung Q with the general count. It is **not** the case that the calculus "knows" a² ≥ 0 — that is order, a gap ([[N.order]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | holds | real content |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | EXACT | — |
| logic | untested | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
