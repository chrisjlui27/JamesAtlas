---
id: C.complex-quotient
title: Dividing complex numbers — multiply by the conjugate
type: theorem
level: object
kind: law
rung: C
order: 1061
setting: classical
equality: "≐"
domain: real
law: "([A ([B] [(([J] <[oo]>))])] <[C ([D] [(([J] <[oo]>))])]>) ≐ ([([A] [C]) ([B] [D])] <[([C] [C]) ([D] [D])]>) ([([B] [C]) <([A] [D])>] [(([J] <[oo]>))] <[([C] [C]) ([D] [D])]>)"
units: "(a + bi)/(c + di) = ((ac + bd) + (bc − ad)i)/(c² + d²)"
gloss_check: "(A + B*1j)/(C + D*1j)"
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
known_since: "Bombelli 1572; Euler 1770 (Elements of Algebra)"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [Q.division, C.complex-number, Z.inversion, C.conjugate, Z.collection, mult.involution, C.modulus-squared, mult.distribution, mult.inverse-promotion, C.i-squared, C.phase-under-instance, Z.cancellation]
guarded_by: [mult.seam-decree]
see_also: [Q.division, C.conjugate, C.modulus-squared, C.complex-number]
aliases: [complex division, realize the denominator, "(a + bi)/(c + di)"]
concepts: [complex-number, division, fraction]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([z] <[w]>) ≐ ([([A] [C]) ([B] [D])] <[c² + d²]>) ([([B] [C]) <([A] [D])>] [i] <[c² + d²]>)` | with z = `A ([B] [(([J] <[oo]>))])`, w = `C ([D] [(([J] <[oo]>))])` and c² + d² = `([C] [C]) ([D] [D])` | (a + bi)/(c + di) = (ac + bd)/(c² + d²) + i (bc − ad)/(c² + d²) |

The textbook division of complex numbers, as a theorem: multiply above and below by the conjugate, and the denominator becomes real by [[C.modulus-squared]]. On the page the quotient `([z] <[w]>)` already *is* a complex number — this law only spells it out in rectangular parts.

## Plain

To divide by a complex number, multiply top and bottom by its flipped twin: the bottom turns into an ordinary positive number, and the top is an ordinary product.

## Derivation

| form | rule | note |
|---|---|---|
| `([A ([B] [(([J] <[oo]>))])] <[C ([D] [(([J] <[oo]>))])]>)` | given | z ÷ w, [[Q.division]], with z = a + bi and w = c + di ([[C.complex-number]]) |
| `([A ([B] [(([J] <[oo]>))])] <[C ([D] [(([J] <[oo]>))])]> [C <([D] [(([J] <[oo]>))])>] <[C <([D] [(([J] <[oo]>))])>]>)` | [[Z.inversion]] | create the pair `[w̄] <[w̄]>` ([[C.conjugate]]) |
| `([A ([B] [(([J] <[oo]>))])] [C <([D] [(([J] <[oo]>))])>] <[C ([D] [(([J] <[oo]>))])] [C <([D] [(([J] <[oo]>))])>]>)` | [[Z.collection]] | the two mirrored abstracts collect |
| `([A ([B] [(([J] <[oo]>))])] [C <([D] [(([J] <[oo]>))])>] <[([C ([D] [(([J] <[oo]>))])] [C <([D] [(([J] <[oo]>))])>])]>)` | [[mult.involution]] | the unit right to left on `[w] [w̄]`, inside an angle directly inside the instance — absorbing (for a negative real w the content is 2 ln|w| + 2πi, off the strip: guarded by position) |
| `([A ([B] [(([J] <[oo]>))])] [C <([D] [(([J] <[oo]>))])>] <[([C] [C]) ([D] [D])]>)` | [[C.modulus-squared]] | w w̄ ≐ c² + d² |
| `([A] [C <([D] [(([J] <[oo]>))])>] <[([C] [C]) ([D] [D])]>) ([([B] [(([J] <[oo]>))])] [C <([D] [(([J] <[oo]>))])>] <[([C] [C]) ([D] [D])]>)` | [[mult.distribution]] | distribute over z = a + bi, with the context `[w̄] <[c² + d²]>` |
| `([A] [C] <[([C] [C]) ([D] [D])]>) ([A] [<([D] [(([J] <[oo]>))])>] <[([C] [C]) ([D] [D])]>) ([([B] [(([J] <[oo]>))])] [C] <[([C] [C]) ([D] [D])]>) ([([B] [(([J] <[oo]>))])] [<([D] [(([J] <[oo]>))])>] <[([C] [C]) ([D] [D])]>)` | [[mult.distribution]] | distribute each over w̄ = c <di> |
| `([A] [C] <[([C] [C]) ([D] [D])]>) <([A] [([D] [(([J] <[oo]>))])] <[([C] [C]) ([D] [D])]>)> ([([B] [(([J] <[oo]>))])] [C] <[([C] [C]) ([D] [D])]>) <([([B] [(([J] <[oo]>))])] [([D] [(([J] <[oo]>))])] <[([C] [C]) ([D] [D])]>)>` | [[mult.inverse-promotion]] | the mirrors come out of the two terms with <di> |
| `([A] [C] <[([C] [C]) ([D] [D])]>) <([A] [D] [(([J] <[oo]>))] <[([C] [C]) ([D] [D])]>)> ([B] [(([J] <[oo]>))] [C] <[([C] [C]) ([D] [D])]>) <([B] [(([J] <[oo]>))] [D] [(([J] <[oo]>))] <[([C] [C]) ([D] [D])]>)>` | [[mult.involution]] | the unit on each `[([D] [i])]` and `[([B] [i])]`, directly inside its instance — absorbing |
| `([A] [C] <[([C] [C]) ([D] [D])]>) <([A] [D] [(([J] <[oo]>))] <[([C] [C]) ([D] [D])]>)> ([B] [(([J] <[oo]>))] [C] <[([C] [C]) ([D] [D])]>) <([B] [D] [([(([J] <[oo]>))] [(([J] <[oo]>))])] <[([C] [C]) ([D] [D])]>)>` | [[mult.involution]] | the unit right to left on `[i] [i]` — absorbing |
| `([A] [C] <[([C] [C]) ([D] [D])]>) <([A] [D] [(([J] <[oo]>))] <[([C] [C]) ([D] [D])]>)> ([B] [(([J] <[oo]>))] [C] <[([C] [C]) ([D] [D])]>) <([B] [D] [<o>] <[([C] [C]) ([D] [D])]>)>` | [[C.i-squared]] | `([i] [i]) ≐ <o>`, and `[<o>]` is J |
| `([A] [C] <[([C] [C]) ([D] [D])]>) <([A] [D] [(([J] <[oo]>))] <[([C] [C]) ([D] [D])]>)> ([B] [(([J] <[oo]>))] [C] <[([C] [C]) ([D] [D])]>) <<([B] [D] <[([C] [C]) ([D] [D])]>)>>` | [[C.phase-under-instance]] | the J becomes a sign |
| `([A] [C] <[([C] [C]) ([D] [D])]>) <([A] [D] [(([J] <[oo]>))] <[([C] [C]) ([D] [D])]>)> ([B] [(([J] <[oo]>))] [C] <[([C] [C]) ([D] [D])]>) ([B] [D] <[([C] [C]) ([D] [D])]>)` | [[Z.cancellation]] | −(−bd) = bd |
| `([([A] [C])] <[([C] [C]) ([D] [D])]>) <([([A] [D])] [(([J] <[oo]>))] <[([C] [C]) ([D] [D])]>)> ([([B] [C])] [(([J] <[oo]>))] <[([C] [C]) ([D] [D])]>) ([([B] [D])] <[([C] [C]) ([D] [D])]>)` | [[mult.involution]] | the unit right to left on each real product, directly inside its instance — absorbing |
| `([([A] [C])] <[([C] [C]) ([D] [D])]>) ([<([A] [D])>] [(([J] <[oo]>))] <[([C] [C]) ([D] [D])]>) ([([B] [C])] [(([J] <[oo]>))] <[([C] [C]) ([D] [D])]>) ([([B] [D])] <[([C] [C]) ([D] [D])]>)` | [[mult.inverse-promotion]] | right to left: the mirror goes onto the product ad |
| `([([A] [C]) ([B] [D])] <[([C] [C]) ([D] [D])]>) ([([B] [C]) <([A] [D])>] [(([J] <[oo]>))] <[([C] [C]) ([D] [D])]>)` | [[mult.distribution]] | collect the two real terms over `<[c² + d²]>` and the two imaginary terms over `[i] <[c² + d²]>`, right to left |

## Confirms

The rectangular formula for a quotient — the only law of the rung with four real variables. What the derivation shows is that division needs nothing new: `([z] <[w]>)` was a form at rung `Q` for any nonzero w, and the "realize the denominator" trick is one Inversion, one Collection, and the modulus identity. It is **not** a definition of division in ℂ — division was defined once, at [[Q.division]], for all forms — and it is **not** needed to *compute* with the chart's forms; it is needed to *read* them in the way the textbook does.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step directly under an instance, through an angle at most |
| JH, JO | replaced | division in ℍ is two-sided: `([z] <[w]>)` must say which side, and the conjugate trick needs the norm's four squares |
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

Guarded by position (Amendment A2). Two kinds of seam step: the unit right to left on `[w] [w̄]`, inside an angle directly inside the instance, whose content is 2 ln|w| + 2πi exactly at d = 0 with c < 0 (for every d ≠ 0 the two arguments cancel and the content is real); and the units on `[([B] [i])]` and `[([D] [i])]`, whose content ln b + iπ/2 is ln|b| + 3πi/2 for negative b. The instances absorb both, and the law carries the decree in its price while its statement is exact in ℂ.
