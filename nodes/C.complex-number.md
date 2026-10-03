---
id: C.complex-number
title: A complex number is a pile beside a scaled quarter turn
type: definition
level: object
kind: law
rung: C
order: 1040
setting: classical
equality: "≐"
domain: real
law: "A + iB := A ([B] [(([J] <[oo]>))])"
units: "a + bi"
gloss_check: "A + B*1j"
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
known_since: "1993 (James); Hamilton 1837 for ℂ as pairs of reals"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.multiplication, C.imaginary-unit, N.addition]
see_also: [C.polar-form, C.imaginary-unit, mult.consistency]
aliases: [complex number, "a + bi", rectangular form]
concepts: [complex-number, addition, multiplication]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `A ([B] [(([J] <[oo]>))])` | `A ([B] [i])` | a + bi |

A real part beside an imaginary part: the imaginary part is a real count of i. Nothing is adjoined — the ℂ reading has been the model since `[<o>]` could be written; this is the rectangular spelling of its points that the forms reach (countably many of them: the forms are a language for ℂ, not ℂ).

## Plain

A complex number is an ordinary number next to "some amount of i", and "some amount of i" is a product like any other.

## Derivation

| form | rule | note |
|---|---|---|
| `A ([B] [(([J] <[oo]>))])` | [[N.addition]] | a juxtaposed with b × i — [[mult.multiplication]], with i = `(([J] <[oo]>))` ([[C.imaginary-unit]]) |
| `A + iB` | name | — |

## Confirms

ℂ = ℝ + ℝi, the rectangular form, with the arithmetic of complex numbers being the arithmetic of forms — addition is juxtaposition, multiplication is `([X][Y])`, and the laws of the earlier rungs apply unchanged. What the page does **not** do is make the spelling canonical: the same number has many forms (the polar spelling [[C.polar-form]] is another), and "two complex numbers are equal iff their parts are" is a statement about the ℂ *reading* ([[mult.consistency]]), not a law of the forms. The forms do not know that they are pairs.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | a product and a juxtaposition; no Λ-step |
| JH, JO | replaced | with i replaced by a direction u the same shape spells a + bu in the slice of u; the quaternions need three such parts, and the product of two of them leaves the slice (JH's non-commutativity is exactly the failure of this shape to close) |
| JP | guarded | as [[C.imaginary-unit]] |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The domain is `real`: a and b are sampled as nonzero reals; b = 0 would make `[B]` the black hole and the imaginary part `(□ [i]) ≐ void` by [[mult.zero-annihilates]] — the right value, reached by the hole rules rather than by multiplication.
