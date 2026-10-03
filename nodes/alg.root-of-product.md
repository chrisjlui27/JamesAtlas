---
id: alg.root-of-product
title: The root of a product is the product of roots
type: theorem
level: object
kind: law
rung: alg
order: 780
setting: classical
equality: ≐
domain: positive
law: "(([[([A] [B])]] <[oo]>)) ≐ ([(([[A]] <[oo]>))] [(([[B]] <[oo]>))])"
units: √(ab) = √a · √b
gloss_check: sqrt(A*B)
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
known_since: 1993 (James); the fact is ancient
entered: 2026-10-03
guide: shape-led
band: 6–8
uses: [alg.root, mult.multiplication, alg.log-law, mult.distribution, alg.exp-law]
see_also: [alg.product-of-powers]
aliases: [√(ab) = √a √b, root of a product]
concepts: [root, multiplication]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[([A] [B])]] <[oo]>)) ≐ ([(([[A]] <[oo]>))] [(([[B]] <[oo]>))])` | — | √(ab) = √a · √b |

## Plain

The root of a product is the product of the roots: halving a sum of logs is halving each, which is Distribution, and the two halves multiply by the exponential law.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[([A] [B])]] <[oo]>))` | given | √(a · b), [[alg.root]] of a product [[mult.multiplication]] |
| `(([[A] [B]] <[oo]>))` | [[alg.log-law]] | ln(ab) = ln a + ln b — the unit on content `[A] [B]`, under a square, admitted because the content is real |
| `((<[oo]> [[A]]) (<[oo]> [[B]]))` | [[mult.distribution]] | `(W [Y Z]) ≐ (W [Y]) (W [Z])` with W = `<[oo]>`, Y = `[A]`, Z = `[B]`: half of a sum is the sum of halves |
| `([(([[A]] <[oo]>))] [(([[B]] <[oo]>))])` | [[alg.exp-law]] | exponents add, right to left: the two halves multiply |

## Confirms

√(ab) = √a √b for positive a, b. For negatives the law is the classic trap √(−1)√(−1) ≠ √1, and the chart shows exactly where it breaks: the second row's unit step is admitted only because `[A] [B]` is real; for a = b = −1 its content is 2πi, off the strip, and the seam decree refuses the step — correctly, since the law is false there.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | on positive content, by the seam decree |
| J1 | holds-mod-Λ | the second row's unit step sits under a square and posts an unabsorbed receipt |
| JH, JO | replaced | within one slice |
| JP | guarded | where the roots are forms at p |

| reading | cell | why |
|---|---|---|
| C | PARTIAL | exact for positive reals; false by a sign for two negatives (the √(−1)√(−1) trap) |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
