---
id: C.phase
title: The phase element J
type: definition
level: object
kind: law
rung: C
order: 900
setting: classical
equality: "≐"
domain: positive
law: "J := [<o>]"
units: "J = ln(−1) = iπ"
gloss_check: "1j*pi"
holds:
  classical: holds
  J1: replaced
  JH: replaced
  JO: replaced
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James, Ch. 6 §6.2, p. 43: J ≐ [<o>], the phase element); the question of ln(−1) was posed in the Leibniz–Bernoulli exchange of 1712–13, taken up by Euler and Bernoulli in 1727–31, and settled by Euler as iπ plus the other branches in E168 (1747/1751)"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.square, Z.angle, N.unit]
see_also: [C.phase-unique, C.phase-value, C.phase-rule, mult.seam-decree]
aliases: [J, phase element, "[<o>]", log of minus one, iπ]
concepts: [phase, negation, logarithm]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[<o>]` | `J` | ln(−1) = iπ |

The abstract of the mirrored unit: the logarithm of −1. James names it J — "the inverse boundary … separated from what it previously contained, into the encapsulated form `[<o>]`" (p. 43) — and reads it as "the radian value iπ". It is the form the whole program turns on — the one place the three boundaries meet once each and survive ([[C.phase-unique]]).

## Plain

Box the mirror of one: that is the log of minus one, which no real number is. The page writes it as easily as it writes one.

## Derivation

| form | rule | note |
|---|---|---|
| `[<o>]` | [[mult.square]] | the square boundary around the mirror ([[Z.angle]]) of the unit [[N.unit]] |
| `J` | name | James's name |

## Confirms

ln(−1) = iπ, Euler's answer to Bernoulli's question — not a new number adjoined to the calculus but a form it could already write at rung `mult`, now read. What this is **not**: a value fixed by the forms. Its reading iπ is the principal branch's; the chart's seam decree ([[mult.seam-decree]]) is what keeps J's other branches (3iπ, −iπ) from being derived as equal to it at depth 0.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | replaced | J = [⟨()⟩] remains, but as the half-period ω/2 of the lattice Λ = ℤω, with [()] = ω no longer void — the group/torsor split (unity vs negation) of the enriched program |
| JH, JO | replaced | one J per slice: a 2-sphere of phase elements J_u, with (J_u) ≐ <o> for every u (JH Ch. 14) |
| JP | holds | J = [<o>] ≐ ω_v/2 at every place; J_p is the torsion element at p (p-adic-wall) |

| reading | cell | why |
|---|---|---|
| C | EXACT | iπ |
| finset | ABSENT | finite sets have no −1 to take the log of. On the group-completion road the candidate for J's role is η, the generator of π₁ of the sphere spectrum — but 2η = 0 there, which matches the *refuted* `J J ≐ void`, not the classical J whose double is the non-void period; so the analogy, if it holds, is to J1's torsion reading of J (a reading, not a law) |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

In the census, `[<o>]` is the size-3 form of value iπ that every earlier rung left open; it is read here.
