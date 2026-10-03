---
id: alg.zero-to-power
title: Zero to a power has no form
type: theorem
level: meta
kind: law
rung: alg
order: 746
setting: classical
equality: "≐"
domain: positive
law: "(([[void]] [B])) is not a form"
units: "0ᵇ is not written; neither is 0⁰"
holds:
  classical: holds
  J1: untested
  JH: holds
  JO: holds
  JP: holds
readings:
  C: PARTIAL
  finset: PARTIAL
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE-BY-DECREE
verified: hand
known_since: "1993 (James); the gap in the schoolroom convention is old"
entered: 2026-10-03
guide: need-led
band: "6–8"
uses: [mult.exponentiation, mult.black-hole, mult.hole-exclusion]
see_also: [alg.zeroth-power, Q.no-division-by-zero]
aliases: ["0^b", "0^0"]
concepts: [exponentiation, zero, infinity]
understood: "yes"
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(([[void]] [B]))` | — | 0ᵇ — not admissible |

## Plain

Zero to a power is not something the page can write: the double box around nothing is the box around the pit, one of the two shapes the page refuses.

## Derivation

| statement | rule | note |
|---|---|---|
| `(([[void]] [B]))` is the shape of 0^B | [[mult.exponentiation]] | — |
| its subform `[[void]]` is `[□]`, the square of the black hole | [[mult.black-hole]] | — |
| `[□]` is excluded, so the shape is not an admissible form, for every B — including B = void (0⁰) and B = o (0¹) | [[mult.hole-exclusion]] | the decree |

## Confirms

That 0ᵇ sits with 1/0 among the unwritable things, which is honest about 0⁰ (the schoolroom's "convention 1" and analysis's "indeterminate" are both outside the forms) but overshoots for 0¹ = 0 and 0² = 0, which arithmetic does assign. Those are reachable by another shape: `0 · 0` is `(□ □)` ≐ void by [[mult.zero-annihilates]]. The power *form* and the product *form* part ways at zero — a fact about forms, not about numbers.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, JH, JO, JP | holds | the exclusion is kept everywhere |
| J1 | untested | depends on the status of □ in J1 |

| reading | cell | why |
|---|---|---|
| C | PARTIAL | ℂ assigns 0ᵇ = 0 for b > 0 and leaves 0⁰ and negative b undefined; the form refuses all of them |
| finset | PARTIAL | ∅^B is empty for nonempty B and a point for B = ∅ — finite sets *do* assign 0⁰ = 1; the form cannot say so |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Verification `hand`: a meta statement whose mechanized form is the engine's `Undefined` exception on `[□]`.
