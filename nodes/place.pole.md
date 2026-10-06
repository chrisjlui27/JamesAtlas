---
id: place.pole
title: The pole is a finite count of the prime's log
type: schema
level: object
kind: law
rung: place
order: 1525
setting: JP
equality: "≃"
domain: natural
law: "[o^{p}]^{n} ≐ □"
units: "n·[p] = log p^n = log 0 at depth n: the black hole is reached by n copies of [p] — +∞·[p] at the place, where it is −∞ at ∞"
gloss_check: ""
schema_range: "p=2,3,5; n=1..3"
schema_draw: "p=3; n=2"
holds:
  classical: fails
  J1: fails
  JH: untested
  JO: untested
  JP: holds
readings:
  C: ABSENT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: PARTIAL
status: NATIVE-BY-SCHEMA
verified: engine
known_since: "2026-09-13 (the position of □ on the rung-count axis: −∞ at ∞, +∞·[p] at p, finite N·[p] in ℤ/p^N — 'a consequence of the rung's size, not a free choice')"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [mult.black-hole, place.void-pile, J1.unit, schema.cardinality, J1.counit]
see_also: [mult.black-hole, J1.pole, place.prime-log, place.two-ends, place.no-inverse-of-the-prime]
aliases: [the pole at p, "□ = N·[p]", the rung-count axis, "+∞·[p]", the void pile's log]
concepts: [place, pole, zero, logarithm]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[o^{p}]^{n} ≐ □` | n copies of the log of the prime are the black hole at depth n: the log of the void pile | log(p^n) = log 0 in ℤ/p^n |

At ∞ the black hole is −∞, the log of 0, unreachable by any finite sum of logs ([[mult.black-hole]]). At a finite place it is reachable, and by a *count*: n copies of `[p]` are the log of p^n, and p^n is void at depth n ([[place.void-pile]]) — so n·[p] is `[void]`, which is □. The pole sits at the top of the count of `[p]`, at +n, where at ∞ it sits at −∞ on the real line: Lui's question of 2026-09-13 — whether □ is +∞ or −∞ — answered by the place: *it is where the rung's size puts it*, and |p|_p < 1 where |e| > 1. Dominion `□ A ≐ □` then says that any log with n or more copies of `[p]` is the pole, whatever else it carries: that is the wrap of the finite page, and the reading's rule ([[place.reading]]).

## Plain

Take the logarithm of p, n times over, and you have the logarithm of nothing: on the clock with p^n hours, p^n is midnight, and midnight has no logarithm but the black hole.

## Derivation

| form | rule | note |
|---|---|---|
| `[o^{p}]^{n}` | given | n copies of the log of the prime |
| `[([o^{p}]^{n})]` | [[J1.unit]] | the unit, right to left, on pole-valued content: strict (LEGISLATION 30f — the pole has no winding) |
| `[o^{p**n}]` | [[schema.cardinality]] [[J1.unit]] [[J1.counit]] | n copies of `[p]` instanced is the pile of pⁿ marks: at n = 1 the counit; at n ≥ 2, two of the logs gathered under one abstract (the unit, absorbed inside the instance) and cardinality at count p, as often as needed |
| `[]` | [[place.void-pile]] | the pile is void at depth n: the empty square |
| `□` | definition | [[mult.black-hole]] |

## Confirms

That the extended log space at a finite place is ℤ_p ⊕ ℤ[p] ⊕ ℤJ_p with the pole at `[p]`-count n — the "rung-count axis" of the JP ledger. The three laws of [[mult.black-hole]] and the two exclusions hold at the pole of the place as at ∞'s (the ledger: `mult.hole-exclusion` holds everywhere). It is **not** the other end: the negative counts of `[p]` are not the pole but the forms the page excludes ([[place.no-inverse-of-the-prime]], [[place.two-ends]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | fails | at ∞ no finite count of logs is the pole |
| J1 | fails | as classical: n·ln p is a number |
| JH, JO | untested | owed |
| JP | holds | the unit on pole-valued content is strict (30f); the gathering steps inside the instance are absorbed — p = 2, 3, 5, depths 1 … 3 |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | EXACT | log of 0 in the finite ring |
| logic | PARTIAL | the daimon reached by a finite count: the page logic's Ω at a finite place; owed |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The receipt prover grades the first step strict by the pole exemption of LEGISLATION 30(f): the content n·[p] is pole-valued at depth n on every sample. The schema's cardinality steps use [[schema.cardinality]] at count p, so the range stops at p = 5 here (the cardinality schema runs to n = 12).
