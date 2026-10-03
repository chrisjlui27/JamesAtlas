---
id: alg.root-of-quotient
title: The root of a quotient is the quotient of roots
type: theorem
level: object
kind: law
rung: alg
order: 785
setting: classical
equality: "≐"
domain: positive
law: "(([[([A] <[B]>)]] <[oo]>)) ≐ ([(([[A]] <[oo]>))] <[(([[B]] <[oo]>))]>)"
units: "√(a/b) = √a / √b"
gloss_check: "sqrt(A/B)"
holds:
  classical: holds
  J1: holds-mod-Λ
  JH: replaced
  JO: replaced
  JP: guarded
readings:
  C: PARTIAL
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James); the rule is ancient"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [alg.root, Q.division, mult.involution, mult.inverse-promotion, mult.distribution]
see_also: [alg.root-of-product, Q.flip]
aliases: ["√(a/b) = √a/√b"]
concepts: [root, division]
understood: "yes"
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[([A] <[B]>)]] <[oo]>)) ≐ ([(([[A]] <[oo]>))] <[(([[B]] <[oo]>))]>)` | — | √(a/b) = √a / √b |

## Plain

The root of a fraction is the root of the top over the root of the bottom: halving a difference of logs is the difference of the halves.

## Derivation

| form | rule | note |
|---|---|---|
| `([(([[A]] <[oo]>))] <[(([[B]] <[oo]>))]>)` | given | √a ÷ √b, [[Q.division]] of two roots, [[alg.root]] |
| `(([[A]] <[oo]>) <([[B]] <[oo]>)>)` | [[mult.involution]] | the unit, twice; both contents real |
| `(([[A]] <[oo]>) (<[oo]> [<[B]>]))` | [[mult.inverse-promotion]] | `<(X [Y])> ≐ (X [<Y>])` with X = `<[oo]>`, Y = `[B]` |
| `((<[oo]> [[A] <[B]>]))` | [[mult.distribution]] | collect, right to left, context `<[oo]>`: half a difference is the difference of halves |
| `((<[oo]> [[([A] <[B]>)]]))` | [[mult.involution]] | the unit right to left on `[A] <[B]>`, content ln a − ln b, real |

The last form is `(([[([A] <[B]>)]] <[oo]>))`, the square root of a ÷ b.

## Confirms

√(a/b) = √a/√b, the quotient twin of [[alg.root-of-product]], with a caveat of its own: it is exact for positive a, b and fails for a positive numerator over a negative denominator — √(1/−1) = i but √1/√(−1) = −i (content −iπ, which the half-open strip excludes); two negatives agree here, unlike the product's trap. Hence `C: PARTIAL`.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds-mod-Λ | the last unit step sits under a square inside the instance — not absorbing; the receipt is posted, as in [[alg.root-of-product]] |
| JH, JO | replaced | ordered quotients |
| JP | guarded | needs 2 a unit and the p-adic logs to converge |

| reading | cell | why |
|---|---|---|
| C | PARTIAL | exact for positive a and b; fails for a positive numerator over a negative denominator (√(1/−1) = i ≠ −i) |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
