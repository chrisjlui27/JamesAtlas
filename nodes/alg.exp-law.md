---
id: alg.exp-law
title: The exponential law
type: theorem
level: object
kind: law
rung: alg
order: 710
setting: classical
equality: ≐
domain: complex
law: "([(A)] [(B)]) ≐ (A B)"
units: "e^a · e^b = e^{a+b}"
gloss_check: exp(A + B)
holds:
  classical: holds
  J1: holds
  JH: guarded
  JO: guarded
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James); the integer-exponent law is Archimedes', the logarithmic side Napier 1614"
entered: 2026-10-03
guide: shape-led
band: 9–12
uses: [mult.multiplication, mult.involution]
guarded_by: [mult.seam-decree]
see_also: [alg.log-law, alg.product-of-powers, N.addition]
aliases: [e^a e^b = e^{a+b}, exponents add, the law of exponents]
concepts: [exponential, multiplication, addition]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([(A)] [(B)]) ≐ (A B)` | — | e^a · e^b = e^{a+b} |

Lui's slogan as a theorem: juxtaposition is addition, and it *becomes* multiplication on instance wrapping. The round boundary is the conversion between the two layers.

## Plain

Multiplying two circled things is the same as circling them side by side: the circle turns adding into multiplying.

## Derivation

| form | rule | note |
|---|---|---|
| `([(A)] [(B)])` | given | e^a × e^b, [[mult.multiplication]] |
| `(A B)` | [[mult.involution]] | the unit `[(X)] ≐ X`, twice — on real content, in an absorbing position |

## Confirms

The law of exponents for one base. It is **not** an axiom here and it is **not** Distribution: it is two unit steps, which is why in ℍ — where exp-splitting fails for non-commuting exponents — the same two steps are *guarded* (JH-1: exp(X+Y) = exp X exp Y iff XY = YX), while Distribution survives two-sided. The chart keeps the two laws apart because the quaternions do.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the unit steps sit directly under an instance: depth-1 criterion ([[mult.involution]], Notes) |
| JH, JO | guarded | holds only for commuting exponents (one slice); the in-band rigidity lemma of JH-1 |
| JP | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | exact on all of ℂ: the error of each unit step is a multiple of 2πi, cancelled by the enclosing instance |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | the λ-road: a λ-ring's `ψ^r` is a ring map, so this law is where the ψ-operations will be seen to respect the two layers |

## Refuted readings

none

## Notes

Domain `complex` (widened 2026-10-03, C referee pass): the exponential law is the complex exponent law, e^{a}e^{b} = e^{a+b} for all complex a, b; its unit steps sit directly inside the instance and are seam steps for content off the strip, so the law is guarded by position. The home band and reading are unchanged.
