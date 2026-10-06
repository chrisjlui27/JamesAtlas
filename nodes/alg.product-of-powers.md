---
id: alg.product-of-powers
title: Powers with a common base multiply by adding exponents
type: theorem
level: object
kind: law
rung: alg
order: 740
setting: classical
equality: ≐
domain: positive
law: "([(([[A]] [B]))] [(([[A]] [C]))]) ≐ (([[A]] [B C]))"
units: "a^b · a^c = a^{b+c}"
gloss_check: A**(B + C)
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: 1993 (James); the rule is ancient
entered: 2026-10-03
guide: shape-led
band: 6–8
uses: [mult.exponentiation, mult.multiplication, mult.involution, mult.distribution]
see_also: [alg.exp-law, alg.power-of-power]
aliases: [a^b a^c = a^{b+c}, product rule for exponents]
concepts: [exponentiation, multiplication]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([(([[A]] [B]))] [(([[A]] [C]))]) ≐ (([[A]] [B C]))` | — | a^b · a^c = a^{b+c} |

## Plain

To multiply two powers of the same number, add the exponents: under the circles, the two products share a factor, and Distribution gathers them.

## Derivation

| form | rule | note |
|---|---|---|
| `([(([[A]] [B]))] [(([[A]] [C]))])` | given | a^b × a^c, [[mult.exponentiation]] and [[mult.multiplication]] |
| `(([[A]] [B]) ([[A]] [C]))` | [[mult.involution]] | the unit twice, directly under the instance |
| `(([[A]] [B C]))` | [[mult.distribution]] | collect: `(X [B]) (X [C]) ≐ (X [B C])` with X = `[[A]]` |

## Confirms

The product rule for exponents is **Distribution** — the ring law a(b + c) = ab + ac — read one level up, where "a" is ln a and the sum is the sum of exponents. The exponential law ([[alg.exp-law]]) did the same job for the base e with two unit steps; here the base is arbitrary and Distribution is needed. The two routes are the two layers of the calculus.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the unit steps sit directly under an instance: depth-1 criterion ([[mult.involution]], Notes) |
| JH, JO | replaced | powers of a non-real quaternion need the ordered bracket; the law holds within one slice |
| JP | guarded | for whole counts A, B the law is exact at every place; a count that is a fraction of principal units (a positive variable at a place is one a fifth of the time) makes `(([[X]] [A]))` a fractional count of the torsion log, which is a form at p only when its denominator divides p − 1 ([[place.selection]]) — the place ledger: guarded at p = 5 among the tested places, exact at the others |

| reading | cell | why |
|---|---|---|
| C | EXACT | exact on all of ℂ× once the power is defined by the form, `(([[A]][B]))` = e^{b·Ln a}: both unit steps are absorbing and Distribution is exact |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
