---
id: schema.de-moivre
title: De Moivre's formula, for every n
type: schema
level: object
kind: law
rung: schema
order: 1150
setting: classical
equality: "≐"
domain: real
law: "(([[(([J] [T]))]] [o^{n}])) ≐ (([J] [T] [o^{n}]))"
units: "(e^{iπt})ⁿ = e^{iπnt}"
gloss_check: ""
schema_range: "n=1..6"
schema_draw: "n=3"
holds:
  classical: holds
  J1: holds
  JH: guarded
  JO: guarded
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE-BY-SCHEMA
verified: engine
known_since: "De Moivre 1707–1722; Euler 1748 for the exponential form"
entered: 2026-10-03
guide: need-led
band: "9–12"
uses: [mult.exponentiation, C.polar-form, schema.power, mult.involution, schema.cardinality]
guarded_by: [mult.seam-decree]
see_also: [C.de-moivre, schema.power, schema.cardinality, C.euler-formula]
aliases: [De Moivre schema, "(cos θ + i sin θ)ⁿ"]
concepts: [trigonometry, phase, exponentiation, induction]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[X]] [o^{n}])) ≐ (([J] [T] [o^{n}]))`, X = `(([J] [T]))` | the n-th power of the turn by t is the turn by nt | (cos πt + i sin πt)ⁿ = cos nπt + i sin nπt |

[[C.de-moivre]] for every n: raising a turn to a numeral power multiplies its count of J. Through Euler's formula, (cos θ + i sin θ)ⁿ = cos nθ + i sin nθ.

## Plain

Turn by t, n times over: you have turned by nt. The page unfolds the power into n turns and adds the counts.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[(([J] [T]))]] [o^{n}]))` | given | the n-th power of the turn, [[mult.exponentiation]], [[C.polar-form]] |
| `([(([J] [T]))]^{n})` | [[schema.power]] | the power is the n-fold product |
| `(([J] [T])^{n})` | [[mult.involution]] | the unit on each `[(([J] [T]))]`, directly inside the instance — absorbing (content iπt: a seam step for t ∉ (−1, 1]) |
| `(([([J] [T])] [o^{n}]))` | [[schema.cardinality]] | n copies are one copy with the count n |
| `(([J] [T] [o^{n}]))` | [[mult.involution]] | the unit on `[([J] [T])]`, directly inside the inner instance — absorbing (content ln π + ln t + iπ/2, off the strip for t < 0: a second seam step): the turn by nt |

## Confirms

De Moivre's formula as a schema over n, with no principal-branch condition on t: the power is unfolded into a product by [[schema.power]] *before* any abstract of the turn is taken, so the only unit steps sit inside the instance. It is **not** true for a non-numeral exponent without a condition (see [[C.de-moivre]], Confirms), and it is **not** the formula with cosines and sines on the page — that spelling needs [[C.euler-formula]] on both sides, which is a further row the chart leaves to the reader.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step directly under an instance |
| JH, JO | guarded | within a slice, as [[C.turn-of-sum]] |
| JP | guarded | for integer turns, at every tested place; a fractional turn is a form only by the selection rule ([[place.selection]]) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Guarded by position (Amendment A2): the units on `[(([J] [T]))]` in row 3 have content iπt, off the strip for t ∉ (−1, 1], and the unit on `[([J] [T])]` in row 5 has content ln π + ln t + iπ/2, off the strip for t < 0; all sit directly inside an instance. Checked for n = 1 … 6; the card draws n = 3.
