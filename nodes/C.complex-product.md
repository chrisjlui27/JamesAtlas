---
id: C.complex-product
title: Multiplying complex numbers in rectangular form
type: theorem
level: object
kind: law
rung: C
order: 1057
setting: classical
equality: "≐"
domain: real
law: "([A ([B] [(([J] <[oo]>))])] [C ([D] [(([J] <[oo]>))])]) ≐ ([A] [C]) <([B] [D])> ([([A] [D]) ([B] [C])] [(([J] <[oo]>))])"
units: "(a + bi)(c + di) = (ac − bd) + (ad + bc)i"
gloss_check: "(A + B*1j)*(C + D*1j)"
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
known_since: "Bombelli 1572 (the rules of sign for 'più di meno' and 'meno di meno'); Euler 1770"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.multiplication, C.complex-number, mult.distribution, mult.involution, C.i-squared, C.phase-under-instance]
guarded_by: [mult.seam-decree]
see_also: [C.complex-number, C.i-squared, C.modulus-squared, C.complex-quotient, C.polar-product]
aliases: [complex product, FOIL, "(a + bi)(c + di)"]
concepts: [complex-number, multiplication]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A ([B] [i])] [C ([D] [i])]) ≐ ([A] [C]) <([B] [D])> ([([A] [D]) ([B] [C])] [i])` | with i = `(([J] <[oo]>))` | (a + bi)(c + di) = (ac − bd) + (ad + bc) i |

The rectangular product: FOIL, with i² = −1 turning the last term's sign. Here the textbook's rule "i² = −1" is used in anger: it is [[C.i-squared]] followed by J becoming a sign under an instance.

## Plain

Multiply out the four pairs; the pair of i-terms picks up i times i, which is minus one, so it changes sign and joins the real part; the two mixed terms join into the i-part.

## Derivation

| form | rule | note |
|---|---|---|
| `([A ([B] [(([J] <[oo]>))])] [C ([D] [(([J] <[oo]>))])])` | given | (a + bi)(c + di), [[mult.multiplication]], [[C.complex-number]] |
| `([A ([B] [(([J] <[oo]>))])] [C]) ([A ([B] [(([J] <[oo]>))])] [([D] [(([J] <[oo]>))])])` | [[mult.distribution]] | distribute over c + di |
| `([A] [C]) ([([B] [(([J] <[oo]>))])] [C]) ([A] [([D] [(([J] <[oo]>))])]) ([([B] [(([J] <[oo]>))])] [([D] [(([J] <[oo]>))])])` | [[mult.distribution]] | and over a + bi: four terms |
| `([A] [C]) ([B] [(([J] <[oo]>))] [C]) ([A] [D] [(([J] <[oo]>))]) ([B] [(([J] <[oo]>))] [D] [(([J] <[oo]>))])` | [[mult.involution]] | the unit on each `[([B] [i])]`, `[([D] [i])]`, directly inside its instance — absorbing |
| `([A] [C]) ([B] [(([J] <[oo]>))] [C]) ([A] [D] [(([J] <[oo]>))]) ([B] [D] [([(([J] <[oo]>))] [(([J] <[oo]>))])])` | [[mult.involution]] | the unit right to left on `[i] [i]` — absorbing (content iπ, on the edge) |
| `([A] [C]) ([B] [(([J] <[oo]>))] [C]) ([A] [D] [(([J] <[oo]>))]) ([B] [D] [<o>])` | [[C.i-squared]] | `([i] [i]) ≐ <o>`, and `[<o>]` is J |
| `([A] [C]) ([B] [(([J] <[oo]>))] [C]) ([A] [D] [(([J] <[oo]>))]) <([B] [D])>` | [[C.phase-under-instance]] | the J becomes a sign: −bd |
| `([A] [C]) ([([B] [C])] [(([J] <[oo]>))]) ([([A] [D])] [(([J] <[oo]>))]) <([B] [D])>` | [[mult.involution]] | the unit right to left on the real products `[B] [C]`, `[A] [D]`, directly inside their instances — absorbing |
| `([A] [C]) <([B] [D])> ([([A] [D]) ([B] [C])] [(([J] <[oo]>))])` | [[mult.distribution]] | collect the two i-terms over the shared `[i]`, right to left |

## Confirms

(a + bi)(c + di) = (ac − bd) + (ad + bc)i. Nine rows: two Distributions, four absorbing unit steps, the i² step, and two collections. It is **not** needed for the page to multiply — `([z] [w])` *is* the product — but to *read* the product in rectangular parts; [[C.modulus-squared]] is this law at c = a, d = −b, and [[C.complex-quotient]] rests on it.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step directly under an instance |
| JH, JO | replaced | the quaternion product has sixteen terms and does not commute; in a slice it is this law with u for i |
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

Guarded by position (Amendment A2): the units on `[([B] [i])]` and `[([D] [i])]` have content ln b + iπ/2, which for negative b is ln|b| + 3πi/2 — off the strip; they sit directly inside their instances, which absorb the difference. The engine computes the guard from the derivation.
