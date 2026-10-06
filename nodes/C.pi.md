---
id: C.pi
title: π is J divided by i
type: definition
level: object
kind: law
rung: C
order: 1010
setting: classical
equality: "≐"
domain: positive
law: "π := ([J] <[(([J] <[oo]>))]>)"
units: "π = iπ / i"
gloss_check: "pi"
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: replaced
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James)"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [Q.division, C.phase, C.imaginary-unit]
see_also: [C.phase, C.imaginary-unit, C.euler-identity, alg.base]
aliases: [π, pi, "J/i"]
concepts: [phase, constant]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([J] <[(([J] <[oo]>))]>)` | `([J] <[i]>)` | iπ / i = π |

π is J with the i taken out: the quotient of two phases, and a real number. James's own form (Table 6.1, p. 49) is `(J [J] ([J] <[oo]>))`, "−1 × i × iπ"; the two agree, since `<[i]>` and `J ([J] <[oo]>)`-less-`[J]` differ by a whole period inside the instance — see Notes.

## Plain

The log of minus one is i times π. Divide out the i and π is what is left — so π is on the page as soon as J and i are.

## Derivation

| form | rule | note |
|---|---|---|
| `([J] <[(([J] <[oo]>))]>)` | [[Q.division]] | J ÷ i: `([A] <[B]>)` with A = J ([[C.phase]]) and B = i ([[C.imaginary-unit]]) |
| `π` | name | — |

## Confirms

That π is not a primitive of the calculus but a quotient — the last of Euler's five constants to be found rather than adjoined: 0 is the void, 1 is `o`, e is `(o)`, and i and π are fractions of J. It is **not** a construction that computes π: the value is read in ℂ, and the form says no more about the digits of π than `[<o>]` says about those of iπ. The form has 17 boundaries.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | `[J]` is the principal log of the half-period, a definite value; the whole form is an instance and absorbs any receipt — the reading evaluates π exactly. What 𝕁₁ adds is that `[J]`, a log of non-instance content, carries the usual Λ-ambiguity, which the instance pays |
| JH, JO | replaced | per slice the quotient `([J_u] <[u]>)` is π for every u, so π is the one slice-independent *value* of the phase sphere; but it is not a single form |
| JP | replaced | there is no π at a finite place: `([J] <[i]>)` scales the log of a formal element by i, which is not a count (`place.reading`: weight 2); π belongs to ∞ |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

James's π (p. 49, glossary p. 64) is `(J [J] ([J] <[oo]>))` = (−1)·(iπ)·i, read as "the radian unit": he insists it "treats it not as a real number but as the radian unit. Its semantic value comes out of this algebraic construction and has no relation to its numerical value of π = 3.14159…" — the chart's "π is read, not computed" in his words. The two forms are equal: `([J] <[i]>)` has `<[i]>` = −iπ/2 beside `[J]`, and James's has `J H` = 3iπ/2 beside `[J]`, with H = `([J] <[oo]>)`; the difference is a whole period, absorbed by the instance ([[C.period-absorption]] with `<H> J J ≐ <H> H H J ≐ H J` by [[Q.fractional-cardinality]]). Writing that equality as rows is owed.
