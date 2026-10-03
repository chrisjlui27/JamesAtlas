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
  J1: untested
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

π is J with the i taken out: the quotient of two phases, and a real number.

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
| J1 | untested | the J1 reading of `[J]` — the log of the half-period ω/2 — is not in the survival ledger; what `([J] <[i]>)` is there is owed |
| JH, JO | replaced | per slice the quotient `([J_u] <[u]>)` is π for every u, so π is the one slice-independent *value* of the phase sphere; but it is not a single form |
| JP | untested | there is no π at a finite place; whether the form `([J_p] <[i_p]>)` converges at p, and to what, is untested |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
