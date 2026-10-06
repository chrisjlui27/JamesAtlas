---
id: place.prime-log
title: The log of the prime is irreducible at its own place
type: definition
level: meta
kind: declaration
rung: place
order: 1430
setting: JP
equality: "≡"
domain: natural
law: "[p] := [o^{p}]"
units: "log p, formal at p: no strict rule reduces it, and the count of [p] in a log is the valuation v_p"
gloss_check: ""
witness: tools/models/place_prime_log.py
holds:
  classical: replaced
  J1: replaced
  JH: untested
  JO: untested
  JP: holds
readings:
  C: ABSENT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE-BY-DECREE
verified: engine
known_since: "2026-09-13 (Forms at Every Place: 'the irreducible [p] — valuation = count of [p]'); the p-adic valuation, Hensel 1897"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [mult.square, N.numeral, place.reading]
see_also: [place.reading, place.radius, place.no-inverse-of-the-prime, place.pole, place.polar-form, J1.period-form]
aliases: ["[p]", the log of the prime, the valuation, v_p, the uniformizer's log, "the irreducible [p]"]
concepts: [place, logarithm, prime]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| `[p] := [o^{p}]`, the log of the pile of p marks: at the place p it has no number part — it is a *count*, and the count of `[p]` in `[A]` is how many times p divides A | — | log p is not a p-adic number; v_p(a) = the exponent of p in a |

At ∞, `[oo]` is ln 2 = 0.693…, a number like any other. At the place 2 the same form is not a number at all: the log of the prime has no value on the page, because no instance reaches 2 from the radius — e^x is a principal unit for every x in the radius, and 2 is not a unit. So `[p]` stays as it is written, a formal count, and the log of any number carries some whole number of copies of it: the **valuation**. The log space at p is three counts ([[place.reading]]), and this is the second of them. `[p]` is the only log that is irreducible for *size* (the torsion log [[place.torsion]] is irreducible for phase): at p = 2 it is the uniformizer's log, where at odd p the uniformizer is p itself.

## Plain

How many times does p go into a number? At the place p that count is part of the number's logarithm, and it is the only part you cannot take the exponential of.

## Derivation

| statement | rule | note |
|---|---|---|
| `[o^{p}]` is a form: the square ([[mult.square]]) around the pile of p marks ([[N.numeral]]) | [[mult.square]] | — |
| at the place p it has no number part: no instance reaches p from the radius — every instance there is a principal unit times a power of p that the content's count of `[p]` supplies — so the log of p is a count, not a number | [[place.reading]] | the second of the three counts; the radius is `place.radius`, further down the rung |
| the count of `[p]` in `[A]` is v_p(A): the log law `[([A][B])] ≐ [A] [B]` adds counts, and `[o^{p}]` has count one | [[place.reading]] | witness: at p = 2, 3, 5, 7, 13, the count of `[p]` in `[A]` is v_p(A) for random A; `[o^{p}]` has no number part and no torsion count; `[o^{p}]^{k}` is the log of p^k |

## Confirms

The p-adic valuation as a count on the page, and its three axioms for free: v(ab) = v(a) + v(b) is the log law (`[([A][B])] ≐ [A] [B]`, exact at p as an equation of counts), v(a + b) ≥ min(v(a), v(b)) is the doll's shared shells ([[place.doll]]), v(p) = 1 is this definition. It is **not** the absolute value |·|_p: that is the metric rung's (`analysis`), where the valuation becomes a size.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | replaced | at ∞ the log of a pile is a real number: `[oo]` = ln 2 |
| J1 | replaced | as classical |
| JH, JO | untested | owed |
| JP | holds | witness |

| reading | cell | why |
|---|---|---|
| C | ABSENT | ℂ has no irreducible log of a number |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

~~"the mirror ⟨⟩ is the uniformizer"~~ — refuted 2026-09-13: the mirror gives J at every place and has zero count of `[p]`; size is `[p]`'s alone.

## Notes

The chart writes the prime as the pile `o^{p}` and its log as `[o^{p}]`; `[p]` is the name. At depth n, n copies of `[p]` are the pole ([[place.pole]]).
