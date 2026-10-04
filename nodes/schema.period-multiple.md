---
id: schema.period-multiple
title: Any number of whole turns inside an instance is nothing
type: schema
level: object
kind: law
rung: schema
order: 1120
setting: classical
equality: "≐"
domain: complex
law: "(A J^{2n}) ≐ (A)"
units: "e^{a + 2πin} = e^a"
gloss_check: ""
schema_range: "n=1..6"
schema_draw: "n=2"
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
status: NATIVE-BY-SCHEMA
verified: engine
known_since: "1993 (James, Ch. 6 §6.3 p. 46: 'ambiguous cardinality, void = JJ = JJJJ = …' — true inside an instance, which is this schema)"
entered: 2026-10-03
guide: need-led
band: "9–12"
uses: [C.period-absorption, N.induction, void.space]
see_also: [C.period-absorption, C.double-phase, schema.roots-of-unity]
aliases: [period multiple, "e^{2πin} = 1"]
concepts: [phase, period, induction]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(A J^{2n}) ≐ (A)` | 2n copies of J inside an instance are forgotten | e^{a + 2πin} = e^a |

[[C.period-absorption]] for every number of turns: the instance forgets any multiple of the period. It is the law the roots of unity need to come back to one.

## Plain

Inside a circle, one whole turn is nothing — so any number of whole turns is nothing. Peel them off two J at a time.

## Derivation

| form (n = 1) | rule | note |
|---|---|---|
| `(A J J)` | given | one whole turn inside the instance |
| `(A)` | [[C.period-absorption]] | — |

| form | rule | note |
|---|---|---|
| `(A J^{2n})` | given | n whole turns inside the instance |
| `(A J^{2n-2} J J)` | medium | one pair set apart — the same multiset ([[void.space]]) |
| `(A J^{2n-2})` | [[C.period-absorption]] | with A := `A J^{2n−2}`: one pair cancels |
| `(A)` | hypothesis | the schema at n − 1 ([[N.induction]]) |

## Confirms

e^{a + 2πin} = e^a for every n ≥ 1 (the negative multiples need one Inversion more, `<J J>` beside `J J`, and are not stated here): the kernel of the exponential is all of 2πiℤ, not just its generator — which in J1 is A5′ for the whole lattice Λ = ℤω (the chart's `(λ A) ≐ (A)`). James's "ambiguous cardinality" `void = JJ = JJJJ = …` (p. 46) is exactly this schema *with the instance removed*, which is the crack; with the instance kept it is a theorem. It is **not** a statement about odd counts of J: an odd number of J inside an instance is a sign ([[C.phase-under-instance]], [[schema.roots-of-negation]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | A5′: exp kills the whole kernel Λ — this schema *is* that axiom, read classically |
| JH, JO | guarded | slice-local, as [[C.period-absorption]] |
| JP | holds | `(ω_v A) ≐ (A)` at every place, iterated |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Checked for n = 1 … 6 (the base n = 1 is [[C.period-absorption]] itself); the card draws n = 3. No unit step occurs, so the schema is not guarded.
