---
id: alg.exp-of-pile
title: A pile under a circle is a power of the base
type: theorem
level: object
kind: instance
rung: alg
order: 730
setting: classical
equality: ≐
domain: natural
law: "(o o) ≐ ([(o)] [(o)])"
units: e² = e · e ; in general (o^n) = eⁿ
gloss_check: e**2
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: replaced
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: 1993 (James)
entered: 2026-10-03
guide: shape-led
band: 9–12
uses: [alg.exp-law, alg.base, N.numeral]
see_also: [mult.exponentiation, mult.square-is-product]
aliases: [e², powers of e, (oo) = e²]
concepts: [exponential, constant]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(o o) ≐ ([(o)] [(o)])` | — | e² = e · e |

## Plain

Circle a pile of two and you get e times e — the circle turns the pile's count into a power.

## Derivation

| form | rule | note |
|---|---|---|
| `([(o)] [(o)])` | given | e × e, with e = `(o)`, [[alg.base]] |
| `(o o)` | [[alg.exp-law]] | exponents add: the pile of two, [[N.numeral]] |

## Confirms

eⁿ as the instance of the pile n — the census's size-3 constant `(o o)` read. Compare [[mult.square-is-product]]: a² = a·a was cardinality one level down; e² = e·e is the exponential law, one level up. The two squares are the same fact seen from either side of the round boundary.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1, JH, JO | holds | real content |
| JP | replaced | `(o^{n})` is a form at p only when p divides n (4 | n at p = 2) — the radius (`place.radius`): e^p is p-adic, e is not |

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
