---
id: C.euler-formula
title: Euler's formula — the turn is cosine plus i sine
type: theorem
level: object
kind: law
rung: C
order: 1080
setting: classical
equality: "≐"
domain: real
law: "(([J] [T])) ≐ ([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>) ([(([J] <[oo]>))] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])"
units: "e^{iπt} = cos πt + i sin πt"
gloss_check: "exp(1j*pi*T)"
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: untested
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "Euler 1748 (Introductio, §138); Cotes 1714 in logarithmic form"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [C.cosine, C.sine, C.imaginary-unit, mult.multiplication, mult.involution, Z.inversion, mult.distribution, void.space, mult.cardinality]
guarded_by: [mult.seam-decree]
see_also: [C.euler-identity, C.polar-form, C.cosine, C.sine]
aliases: [Euler's formula, "e^{iθ} = cos θ + i sin θ", cis]
concepts: [trigonometry, phase, complex-number, exponential]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([J] [T])) ≐ cos πT ([i] [sin πT])` | — | e^{iπt} = cos πt + i sin πt |

With X the pure phase `(([J] [T]))`: X is its cosine beside i times its sine. The two halves into which [[C.cosine]] and [[C.sine]] cut the turn reassemble it.

## Plain

A turn is "how far along" plus i times "how far up". Having defined the two parts by splitting the turn, the law checks that the split loses nothing.

## Derivation

Read from the right-hand side back to the turn:

| form | rule | note |
|---|---|---|
| `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>) ([(([J] <[oo]>))] [([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)])` | given | cos πt + i × sin πt — [[C.cosine]], [[C.sine]], [[C.imaginary-unit]], the product by [[mult.multiplication]] |
| `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>) ([(([J] <[oo]>))] [(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]> <[(([J] <[oo]>))]>)` | [[mult.involution]] | the unit on `[sin πT]` — the sine is an instance, and its abstract stands directly inside the instance `([i] [sin πT])`: absorbing. Its content has imaginary part −π whenever sin πt < 0, off the strip, so this is a seam step: the law is guarded by position |
| `([(([J] [T])) (<[(([J] [T]))]>)] <[oo]>) ([(([J] [T])) <(<[(([J] [T]))]>)>] <[oo]>)` | [[Z.inversion]] | `[i] <[i]>` cancels: the i that made the sine real is divided back out |
| `(<[oo]> [(([J] [T])) (<[(([J] [T]))]>) (([J] [T])) <(<[(([J] [T]))]>)>])` | [[mult.distribution]] | collect the two instances over their shared context `<[oo]>` (Distribution right to left); regroup by [[void.space]] |
| `(<[oo]> [(([J] [T])) (([J] [T]))])` | [[Z.inversion]] | `(<[X]>) <(<[X]>)>` cancels: the reverse turns annihilate |
| `(<[oo]> [([(([J] [T]))] [oo])])` | [[mult.cardinality]] | two copies of the turn are the turn with the count 2 |
| `(<[oo]> [(([J] [T]))] [oo])` | [[mult.involution]] | the unit on `[([X] [oo])]`, directly inside the instance — absorbing |
| `([(([J] [T]))])` | [[Z.inversion]] | `<[oo]> [oo]` cancels: the halving and the doubling |
| `(([J] [T]))` | [[mult.involution]] | the counit `([X]) ≐ X` |

## Confirms

e^{iθ} = cos θ + i sin θ, with θ = πt, as a theorem of the three axioms — every step exact as a row, every unit step in an absorbing position, so the law holds for every t; the first unit step is a seam step (the sine's interior is off the strip when the sine is negative), so the derivation leans on the decree's position clause and the law carries it in its price. What the derivation *is*: the algebra (X + 1/X)/2 + i·(X − 1/X)/(2i) = X, done in forms. What it is **not**: Euler's own route, which defines cos and sin by their series and proves the formula analytically — the chart has no series until rung `analysis`, so here cos and sin were *defined* from the exponential, and the formula records that the definitions are the right ones. The Pythagorean identity cos² + sin² = 1 is the natural companion and is owed (it is `([cos][cos]) ([sin][sin]) ≐ o`, the product X · 1/X = 1 in disguise). At t = 1 the sine vanishes into the hole and the law reads `(J) ≐ <o>`, which is [[C.phase-value]]; [[C.euler-identity]] is one Inversion further.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the two unit steps are directly under instances (depth-1 criterion); every other step is exact |
| JH, JO | replaced | per slice, with i replaced by the slice's direction u: e^{uθ} = cos θ + u sin θ — the quaternionic Euler formula, one per slice (JH Ch. 14) |
| JP | untested | as [[C.cosine]]: the p-adic exp, cos and sin exist only on a small disc, where the identity is a formal one |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The left side has 7 boundaries and the right 72: the standard notation's economy is bought with the names cos, sin and i, each of which is a sizeable form. The chart's view is that the names are worth having and the forms are worth having once.
