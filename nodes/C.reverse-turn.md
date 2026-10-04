---
id: C.reverse-turn
title: One over a turn is the reverse turn
type: theorem
level: object
kind: law
rung: C
order: 1054
setting: classical
equality: "≐"
domain: positive
law: "(<[(([J] [T]))]>) ≐ (([J] [<T>]))"
units: "1 / e^{iπt} = e^{−iπt}  (t > 0)"
gloss_check: "exp(-1j*pi*T)"
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: untested
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "Euler 1748"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [Q.reciprocal, mult.involution, C.phase-rule, C.log-of-negative]
guarded_by: [mult.seam-decree]
see_also: [C.cosine, C.sine, C.cosine-even, C.sine-odd, Q.reciprocal]
aliases: [reverse turn, reciprocal of a turn, "1/e^{iθ} = e^{−iθ}"]
concepts: [phase, inverse]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(<[(([J] [T]))]>) ≐ (([J] [<T>]))` | — | 1/e^{iπt} = e^{−iπt} |

The reciprocal of a turn by t is the turn by −t. The law that makes `(<[X]>)` — the reverse turn used inside the cosine and sine — the same thing as a turn with a mirrored count.

## Plain

Undoing a turn is turning the other way: one over e to the iπt is e to the minus iπt.

## Derivation

| form | rule | note |
|---|---|---|
| `(<[(([J] [T]))]>)` | given | 1 over the turn, [[Q.reciprocal]] |
| `(<([J] [T])>)` | [[mult.involution]] | the unit on `[(([J] [T]))]`, inside an angle directly inside the instance — absorbing through the angle (for t > 1 the content iπt is off the strip: guarded by position) |
| `(([([J] [T])] J))` | [[C.phase-rule]] | `<Y> ≐ ([Y] J)` with Y = `([J] [T])` |
| `(([J] [T] J))` | [[mult.involution]] | the unit on `[([J] [T])]`, directly inside the inner instance — absorbing |
| `(([J] [<T>]))` | [[C.log-of-negative]] | `[T] J ≐ [<T>]`, right to left — t is positive, inside that law's domain |

## Confirms

1/e^{iθ} = e^{−iθ}. The derivation goes through the phase rule and the log of a negative, which is why the domain is positive t: the step `[T] J ≐ [<T>]` is [[C.log-of-negative]] and holds for positive piles. For negative t the companion law [[C.log-of-negative-below]] does the same job, and the statement itself is true for every real t in the ℂ reading. It is **not** the statement that `[X]` and `<[X]>` are negatives of each other for any form X — they are, by [[Z.angle]] — but that the *turns* they produce are a turn and its reverse.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every Λ-step sits directly under an instance: the log-of-negative substitution happens inside `(( … ))` |
| JH, JO | replaced | per slice, as [[C.cosine-even]] |
| JP | untested | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The complex logarithm of a turn, `[(([J] [T]))] ≐ ([J] [T])` for t ∈ (−1, 1] — James's rule 1 in its general form — is not a node: the chart's domain vocabulary (`natural`, `positive`, `negative`, `real`, `complex`) cannot express a bounded real variable, so the engine would sample |t| > 1 and the seam check would rightly refuse the row. Its variable-free instances are writable now, e.g. `[i] ≐ ([J] <[oo]>)`; a `unit-interval` domain, or the induction gap's eventual schema machinery, would admit the law itself.

Guarded by position (Amendment A2): the unit on `[(([J] [T]))]` has content iπt, off the strip for t > 1; it sits inside an angle directly inside the instance — a seam step, admitted by the decree's position clause, so the law carries the decree in its price while its statement is exact in ℂ.
