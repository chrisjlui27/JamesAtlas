---
id: alg.root
title: The square root is a half count one level down
type: definition
level: object
kind: law
rung: alg
order: 760
setting: classical
equality: ≐
domain: positive
law: "√A := (([[A]] <[oo]>))"
units: "√a = a^{1/2} = e^{(ln a)/2}"
gloss_check: sqrt(A)
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
known_since: "1993 (James, 'fractional cardinality'); roots are Babylonian"
entered: 2026-10-03
guide: shape-led
band: 6–8
uses: [mult.exponentiation, Q.half, mult.involution]
see_also: [alg.root-squared, alg.nth-root, Q.fractional-cardinality]
aliases: [square root, √, a^{1/2}, radical]
concepts: [root, exponentiation]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[A]] <[oo]>))` | — | √a |

The fractional count of [[Q.fractional-cardinality]], one level deeper: half of the *abstract* of A, instanced twice. Where `([A] <[oo]>)` was a/2, `(([[A]] <[oo]>))` is a^{1/2}.

## Plain

A square root is "half of" done one box deeper: box the number twice, add a mirrored count of two, and circle twice — the inner circle *is* the halving of the log.

## Derivation

| form | rule | note |
|---|---|---|
| `(([[A]] [(<[oo]>)]))` | [[mult.exponentiation]] | a ^ ½, with ½ = `(<[oo]>)`, [[Q.half]] |
| `(([[A]] <[oo]>))` | [[mult.involution]] | the unit on content `<[oo]>` (real), directly under the inner instance |
| `√A` | name | — |

## Confirms

√a as a^{1/2}, with nothing new adjoined: the mirrored count that made fractions makes roots when applied one level down. It is **not** two-valued: `(([[A]] <[oo]>))` is the principal root, and the other root is its mirror `<(([[A]] <[oo]>))>` — the calculus does not confuse them, which is where James's remark that the calculus is "intrinsically complex" begins to bite ([[alg.root-squared]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the unit step is directly under an instance: depth-1 criterion ([[mult.involution]], Notes) |
| JH, JO | replaced | roots of non-real quaternions: the polar form `([r] ([J_u][t]))` with t halved; two-valued on each slice |
| JP | guarded | the root form `(([[A]] <[oo]>))` halves the three counts of [A] ([[place.reading]]) and is a form at p when the halves are whole — A's count of [p] even and its torsion count even, i.e. A a square mod p at odd p ([[place.lift]]; at 2, A ≡ 1 mod 8 beside an even count of [p]: the radius); the log of a unit always converges once its torsion is split off, so the old worry about the log of a was the wrong one; the root it reads is the principal root — canonical on a principal unit, the generator's choice otherwise (LEGISLATION 31(h)) |

| reading | cell | why |
|---|---|---|
| C | EXACT | the principal square root |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
