---
id: alg.log-law
title: The logarithm of a product
type: theorem
level: object
kind: law
rung: alg
order: 720
setting: classical
equality: ≐
domain: positive
law: "[([A] [B])] ≐ [A] [B]"
units: ln(ab) = ln a + ln b
gloss_check: log(A) + log(B)
holds:
  classical: holds
  J1: holds-mod-Λ
  JH: replaced
  JO: replaced
  JP: holds
readings:
  C: PARTIAL
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: 1993 (James); Napier 1614
entered: 2026-10-03
guide: shape-led
band: 9–12
uses: [mult.multiplication, mult.involution]
guarded_by: [mult.seam-decree]
see_also: [alg.exp-law, Z.collection]
aliases: [ln(ab) = ln a + ln b, the slide rule]
concepts: [logarithm, multiplication, addition]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[([A] [B])] ≐ [A] [B]` | — | ln(ab) = ln a + ln b |

## Plain

The box of a product is the two boxes side by side — the slide rule's whole secret, in one unit step.

## Derivation

| form | rule | note |
|---|---|---|
| `[([A] [B])]` | given | ln(a × b), [[mult.multiplication]] |
| `[A] [B]` | [[mult.involution]] | the unit `[(X)] ≐ X` with X = `[A] [B]` — at depth 0, admitted because the content is real for positive a, b (the seam decree) |

## Confirms

The one law of this rung whose two sides are bare abstracts: it is exactly the unit, applied where nothing absorbs. So its fate tracks the unit's: in J1 it holds only mod Λ, and for negative a, b in ℂ it fails by 2πi — ln((−1)(−1)) = 0 ≠ 2 ln(−1). The exponential law ([[alg.exp-law]]) is the same step wrapped in an instance, and holds everywhere. The pair is the chart's cleanest exhibit of what the seam decree protects.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | on positive content, by the seam decree |
| J1 | holds-mod-Λ | the sides are bare abstracts; nothing absorbs the receipt |
| JH, JO | replaced | `[x ; y]` is the log of the *ordered* product; there is no sum of logs for non-commuting x, y |
| JP | holds | — |

| reading | cell | why |
|---|---|---|
| C | PARTIAL | exact for positive reals (more generally when the arguments' principal arguments do not add past π); false by 2πi otherwise |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
