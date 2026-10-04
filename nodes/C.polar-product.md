---
id: C.polar-product
title: Polar numbers multiply by multiplying moduli and adding angles
type: theorem
level: object
kind: law
rung: C
order: 1053
setting: classical
equality: "≐"
domain: positive
law: "([([R1] ([J] [T1]))] [([R2] ([J] [T2]))]) ≐ ([([R1] [R2])] ([J] [T1 T2]))"
units: "r₁e^{iπt₁} · r₂e^{iπt₂} = (r₁r₂) e^{iπ(t₁+t₂)}"
gloss_check: "R1*R2*exp(1j*pi*(T1+T2))"
holds:
  classical: holds
  J1: holds
  JH: guarded
  JO: guarded
  JP: untested
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "Euler 1748; geometrically, Wessel 1797 and Argand 1806"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.multiplication, C.polar-form, mult.involution, mult.distribution, C.turn-of-sum]
guarded_by: [mult.seam-decree]
see_also: [C.turn-of-sum, C.polar-form, C.complex-product]
aliases: [polar product, moduli multiply, angles add]
concepts: [complex-number, multiplication, phase]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([([R1] ([J] [T1]))] [([R2] ([J] [T2]))]) ≐ ([([R1] [R2])] ([J] [T1 T2]))` | — | (r₁e^{iπt₁})(r₂e^{iπt₂}) = r₁r₂ e^{iπ(t₁+t₂)} |

The product rule for the polar form: moduli multiply, counts of J add. [[C.turn-of-sum]] is the case r₁ = r₂ = 1; here the moduli ride along.

## Plain

To multiply two numbers given as size-and-turn: multiply the sizes, add the turns. On the page both happen in one instance.

## Derivation

| form | rule | note |
|---|---|---|
| `([([R1] ([J] [T1]))] [([R2] ([J] [T2]))])` | given | the product of two numbers in polar form, [[mult.multiplication]], [[C.polar-form]] |
| `([R1] ([J] [T1]) [R2] ([J] [T2]))` | [[mult.involution]] | the unit on each `[([R] ([J] [T]))]`, directly inside the instance — absorbing (content ln r + iπt, off the strip for |t| > 1: guarded by position) |
| `([R1] [R2] ([J] [T1 T2]))` | [[mult.distribution]] | the two turns collect over the shared `[J]`, right to left: the counts add ([[C.turn-of-sum]] is this step alone) |
| `([([R1] [R2])] ([J] [T1 T2]))` | [[mult.involution]] | the unit right to left on `[R1] [R2]`, directly inside the instance — absorbing (content ln r₁ + ln r₂, real): the moduli multiply |

## Confirms

The polar product rule, which is why the polar form exists: multiplication, awkward in rectangular parts ([[C.complex-product]]), is two additions here — of logs and of counts — under one instance. It is **not** canonical about the angle: t₁ + t₂ may exceed a half-turn, and the form keeps it that way; reducing it is [[C.period-absorption]], applied if wanted.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step directly under the instance |
| JH, JO | guarded | within a slice, as [[C.turn-of-sum]]: moduli multiply in any case, turns add only about a common axis |
| JP | untested | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Guarded by position (Amendment A2): the units on `[([R] ([J] [T]))]` have content ln r + iπt, off the strip for |t| > 1; they sit directly inside the instance, which absorbs the difference.
