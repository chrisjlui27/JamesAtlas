---
id: mult.unit-law
title: One is the multiplicative unit
type: theorem
level: object
kind: law
rung: mult
order: 340
setting: classical
equality: "≐"
domain: complex
law: "([A] [o]) ≐ A"
units: "a · 1 = a"
gloss_check: "A"
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
band: "3–5"
uses: [mult.multiplication, mult.log-of-one, void.page, mult.involution]
see_also: [N.unit, mult.log-of-one, mult.product-of-numerals]
aliases: [multiplicative identity, a · 1 = a]
concepts: [one, multiplication, logarithm]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A] [o]) ≐ A` | — | a · 1 = a |

## Plain

Multiplying by one changes nothing, because the box around one circle is empty.

## Derivation

| form | rule | note |
|---|---|---|
| `([A] [o])` | [[mult.multiplication]] | a × 1 |
| `([A])` | [[mult.log-of-one]] | `[o] ≐ void`: the abstract of one is nothing, and void is transparent ([[void.page]]) |
| `A` | [[mult.involution]] | the counit `([A]) ≐ A` |

## Confirms

That 1 is the unit for multiplication *and* that ln 1 = 0, in one law — the two facts are the same step. In J1 this theorem is exactly what forces the completion A5′: James proves `([()][A]) ≐ A` using the strict unit `[()] ≐ void`; enriched, `[()] → ω`, and preserving `1·A = A` *forces* `(ωA) → (A)` — exp kills the whole kernel Λ (james-algebra, O3 completion). The humblest theorem of the rung is the one that legislates the enriched calculus.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | preserved **exactly** by A5′ — and it is the theorem that forced A5′ |
| JH, JO | holds | the Unit rule `[x⃗ ; o ; z⃗] ≐ [x⃗ ; z⃗]` |
| JP | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | EXACT | the one-point set is the unit for × |
| logic | untested | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Domain `complex` (widened 2026-10-03, C referee pass): rung C instantiates this law at complex content, and under the chart's citation discipline ([[mult.consistency]], Confirms) a law may be cited only inside its declared domain; every row of its derivation is exact on ℂ×, as the engine confirms. The law's home band and reading are unchanged.
