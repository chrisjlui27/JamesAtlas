---
id: Q.reciprocal-of-product
title: The reciprocal of a product is the product of reciprocals
type: theorem
level: object
kind: law
rung: Q
order: 610
setting: classical
equality: ≐
domain: positive
law: "(<[([A] [B])]>) ≐ (<[A]> <[B]>)"
units: 1/(ab) = (1/a)(1/b)
gloss_check: 1/(A*B)
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
status: NATIVE
verified: engine
known_since: 1993 (James); the fact is ancient
entered: 2026-10-03
guide: shape-led
band: 6–8
uses: [Q.reciprocal, mult.multiplication, mult.involution, Z.collection]
see_also: [Z.collection, Q.multiply-fractions]
aliases: [1/(ab), reciprocal of a product]
concepts: [division, inverse]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(<[([A] [B])]>) ≐ (<[A]> <[B]>)` | — | 1/(ab) = (1/a)(1/b) |

The right-hand side is the product `([(<[A]>)] [(<[B]>)])` with its two Involutions already taken: inverse collection ([[Z.collection]]), one level deeper, becomes the law of reciprocals.

## Plain

One over a product is the product of the one-overs — the mirror splits over the two boxes.

## Derivation

| form | rule | note |
|---|---|---|
| `(<[([A] [B])]>)` | given | 1/(ab): [[Q.reciprocal]] of a product, [[mult.multiplication]] |
| `(<[A] [B]>)` | [[mult.involution]] | `[(X)] ≐ X` |
| `(<[A]> <[B]>)` | [[Z.collection]] | split the mirror |

## Confirms

(ab)⁻¹ = a⁻¹b⁻¹ — true here because breadth commutes. In ℍ the same law reads (xy)⁻¹ = y⁻¹x⁻¹ and *reverses the order*: JH's Reversal rule. The chart records that as `replaced`: the law survives with its factors reversed, which the unordered page cannot express — the commutative case restricts back.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | depth-1 criterion ([[mult.involution]], Notes) |
| JH, JO | replaced | by Reversal, `<[x₁;…;xₙ]> ≐ [(<[xₙ]>);…;(<[x₁]>)]` — the order flips; this law is its commutative case |
| JP | guarded | for units |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
