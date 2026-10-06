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

That 1 is the unit for multiplication, in one step from the log of one ([[mult.log-of-one]]) and the counit. In 𝕁₁ this theorem is where absorption first shows: James proves `([()][A]) ≐ A` using the strict `[()] ≐ void`; enriched, `[()]` is ω, and the step `([A] ω) → ([A])` is the unit at void content directly inside the instance — absorbed, with the receipt ω paid by the instance ([[J1.absorption]] is this step as a law). In the July presentation preserving `1·A = A` was what *forced* A5′; with receipts it is a theorem. The humblest theorem of the rung is the one where the enriched calculus first pays.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the log of one inside the instance is absorbed: the receipt ω is paid by the instance (the card's 𝕁₁ tape); exact in value |
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
