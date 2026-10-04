---
id: C.turn-of-sum
title: Turns multiply by adding their angles
type: theorem
level: object
kind: law
rung: C
order: 1052
setting: classical
equality: "≐"
domain: real
law: "([(([J] [S]))] [(([J] [T]))]) ≐ (([J] [S T]))"
units: "e^{iπs} · e^{iπt} = e^{iπ(s+t)}"
gloss_check: "exp(1j*pi*(S+T))"
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
known_since: "Euler 1748; as the geometric product of turns, Wessel 1797 and Argand 1806"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.multiplication, C.polar-form, mult.involution, mult.distribution]
guarded_by: [mult.seam-decree]
see_also: [C.polar-form, C.cosine-addition, C.sine-addition, alg.exp-law]
aliases: [turn of a sum, angle addition, "e^{iθ}e^{iφ} = e^{i(θ+φ)}"]
concepts: [phase, multiplication, addition]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([(([J] [S]))] [(([J] [T]))]) ≐ (([J] [S T]))` | — | e^{iπs} e^{iπt} = e^{iπ(s+t)} |

The product of two turns is the turn of the summed angle. This is the whole content of the angle-addition formulas, a few laws before they are spelled out in cosines and sines.

## Plain

Turn by s, then by t: you have turned by s + t. Multiplying the turns adds the counts of J.

## Derivation

| form | rule | note |
|---|---|---|
| `([(([J] [S]))] [(([J] [T]))])` | given | the product of two turns, [[mult.multiplication]], each a pure phase of [[C.polar-form]] |
| `(([J] [S]) ([J] [T]))` | [[mult.involution]] | the unit on each `[(([J] [S]))]`, directly inside the instance — absorbing; for |s| > 1 the content leaves the strip (guarded by position) |
| `(([J] [S T]))` | [[mult.distribution]] | collect over the shared context `[J]`, right to left: the counts add |

## Confirms

e^{iθ}e^{iφ} = e^{i(θ+φ)}, as one Distribution. On the page the law is as short as the fact deserves; the trigonometric addition formulas ([[C.cosine-addition]], [[C.sine-addition]]) are what it becomes when a turn is split into its two parts. It is **not** a law about the *abstracts*: `[X] [Y] ≐ [XY]` at depth 0 would be the log law for complex content, which is false by 2πi when the angles add past a half-turn — the unit steps here sit inside the instance, where the period is forgotten.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | both unit steps directly under the instance (depth-1 criterion) |
| JH, JO | guarded | within a slice: two turns about the same axis u compose by adding angles; about different axes they do not, and the product leaves both slices (JH Ch. 14) |
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

Guarded by position (Amendment A2): the units on `[(([J] [S]))]` have content iπs, off the strip for |s| > 1; they sit directly inside the instance — a seam step, admitted by the decree's position clause, so the law carries the decree in its price while its statement is exact in ℂ.
