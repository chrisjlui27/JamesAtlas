---
id: Z.normal-form
title: Every additive form is an integer
type: theorem
level: object
kind: instance
rung: Z
order: 270
setting: classical
equality: "≐"
domain: natural
law: "ooooo <oo> ≐ ooo"
units: "5 − 2 = 3 ; every form in o, space and < > reduces to a pile, a mirrored pile, or the void"
gloss_check: "3"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James); the fact is the construction of ℤ"
entered: 2026-10-03
guide: need-led
band: "1–2"
uses: [Z.collection, Z.cancellation, Z.void-inverse, Z.inversion, void.space, N.numeral]
see_also: [Z.subtraction, N.order]
aliases: [integer normal form, computing a difference]
concepts: [integer, subtraction]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `ooooo <oo> ≐ ooo` | — | 5 − 2 = 3 |
| in general | — | `o^m <o>^n` reduces to `o^(m−n)` or `<o>^(n−m)` or void |

Any form built from `o`, space, and the angle boundary has a normal form: a pile, a mirrored pile, or nothing. These are the integers, and the reduction is subtraction.

## Plain

Circles and mirrored circles cancel in pairs; what is left over is the answer.

## Derivation

| form | rule | note |
|---|---|---|
| `ooooo <oo>` | given | 5 − 2, [[N.numeral]] |
| `ooooo <o> <o>` | [[Z.collection]] | split the mirror (right to left) |
| `ooo o <o> o <o>` | medium | pair each mirrored unit with a unit, [[void.space]] |
| `ooo` | [[Z.inversion]] | cancel both pairs `o <o>` |

The general case: split every mirror down to single units by [[Z.collection]] (this phase grows the form), remove double mirrors by [[Z.cancellation]] and empty mirrors by [[Z.void-inverse]], then cancel `o <o>` pairs by [[Z.inversion]] until one kind remains (this phase shrinks it).

## Confirms

ℤ = ℕ ∪ {0} ∪ −ℕ, together with the algorithm for subtraction. The *schema* ("for every m, n") is a meta-statement — see [[N.induction]] — but each instance is a finite derivation the engine checks. The normal form is also where order would be read off, if the calculus could write it ([[N.order]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1, JH, JO | holds | the additive, mirror-only fragment is identical in all of them |
| JP | holds | the identity holds at every place; the integer it names is a residue mod p^N there — integers that agree mod p^N are one form at depth N ([[place.void-pile]]) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Tagged *need-led*: nothing in the shape of the forms demands a normal form; arithmetic does. Termination: splitting terminates because mirrors nest finitely, and after it every cancellation shrinks the form — the first place the chart leans on an argument about the rewriting system rather than a derivation in it.
