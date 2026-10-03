---
id: alg.sqrt2
title: The square root of two
type: definition
level: object
kind: law
rung: alg
order: 790
setting: classical
equality: ≐
domain: natural
law: "√2 := (([[oo]] <[oo]>))"
units: √2 = 1.41421…
gloss_check: sqrt(2)
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: 1993 (James); the Pythagoreans for the number
entered: 2026-10-03
guide: shape-led
band: 6–8
uses: [alg.root, N.numeral]
see_also: [alg.irrationality, alg.root-squared]
aliases: [√2, root two, the diagonal]
concepts: [root, constant]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[oo]] <[oo]>))` | — | √2 |

The first *algebraic* irrational the walk meets (the base, [[alg.base]], came first), written with ten boundaries and no new rule. Its square is `oo` by [[alg.root-squared]].

## Plain

The square root of two: box two twice, add a mirrored two, circle twice. The page writes it as easily as it writes two.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[oo]] <[oo]>))` | [[alg.root]] | √A with A the pile of two, [[N.numeral]] |
| `√2` | name | — |

## Confirms

√2 as a closed form. That it is **not** a fraction is a different kind of fact, and the calculus cannot state it ([[alg.irrationality]]): the page writes √2 and writes 7/5 and has no law that says they differ.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1, JH, JO | holds | real content |
| JP | guarded | √2 exists in ℤ_p iff 2 is a square mod p (p = 7 yes, p = 3 no); whether *this form* evaluates at p is the separate question of the p-adic logarithm of 2 converging — the wall parameterization's criterion (p-adic-wall) |

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
