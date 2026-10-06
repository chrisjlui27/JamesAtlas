---
id: place.prime-power
title: The instance of n copies of the prime's log is void
type: schema
level: object
kind: law
rung: place
order: 1525
setting: JP
equality: "≃"
domain: natural
law: "([o^{p}]^{n}) ≃ void"
units: "exp(n·log p) = p^n ≡ 0 at depth n: the void pile reached from the log side, as an instance — n·[p] itself is a finite log, not the pole"
gloss_check: ""
schema_range: "p=2,3,5,7; n=1..3"
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
  logic: untested
status: NATIVE-BY-SCHEMA
verified: engine
known_since: "2026-09-13 (the position of □ on the rung-count axis: −∞ at ∞, +∞·[p] at p); restated 2026-10-06 after the place referee pass — the count n·[p] is not the pole but a finite log whose instance is the void pile"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [place.void-pile, J1.unit, schema.cardinality, J1.counit, place.ostrowski]
see_also: [place.void-pile, place.prime-log, place.two-ends, mult.black-hole, J1.pole, place.geometric-doll]
aliases: [the prime power is void, "([p]^n) ≃ void", p^n as an instance, the void pile from the log side, the rung-count axis]
concepts: [place, pole, zero, logarithm]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([o^{p}]^{n}) ≃ void` | n copies of the log of the prime, instanced, are the pile of pⁿ marks — the void pile at depth n | exp(n log p) = p^n ≡ 0 in ℤ/p^n |

At ∞ the black hole is −∞, the log of 0, unreachable by any finite sum of logs ([[mult.black-hole]]). At a finite place the void *is* reached by a finite count — but as an **instance**: exp of n copies of `[p]` is pⁿ, and pⁿ is the void pile ([[place.void-pile]]). The log n·[p] itself is a finite element of the log space, not the pole: the page's equality is mod pⁿ and does not pass through a square — `[o^{p**n}]` is n·[p], `[void]` is □, and the two are not equal. So the pole at a finite place is the *limit* end of the count of `[p]` ([[place.two-ends]]), which no finite count reaches; what a finite count reaches is the void pile, and only through an instance. The rung's first draft stated `[p]^{n} ≐ □` — n·[p] *is* the pole at depth n; the referee's chain `ooooo → ([ooooo]) → ([ooooo][ooooo]<[ooooo]>) → (□ <[ooooo]>) → (□) → void` at p = 5, depth 2 (counit, Inversion, the pole law, Dominion, the hole instance: five licensed rows) showed that it proves `o^{5} ≐ void` at depth 2 and collapses the page, and it was withdrawn (LEGISLATION 31(g)). Dominion still holds — □ is still the log of nothing — but nothing finite is the pole.

## Plain

Take e to the power of n copies of log p and you get p to the n: on the clock with pⁿ hours, that is midnight. The logarithm itself is not the black hole; only its exponential is nothing.

## Derivation

| form | rule | note |
|---|---|---|
| `([o^{p}]^{n})` | given | n copies of the log of the prime, instanced; at every place ([[place.ostrowski]]) |
| `o^{p**n}` | [[schema.cardinality]] [[J1.unit]] [[J1.counit]] | the pile of pⁿ marks: at n = 1 the counit; at n ≥ 2, two of the logs gathered under one abstract (the unit, absorbed inside the instance) and cardinality at count p, as often as needed |
| `void` | [[place.void-pile]] | the pile is void at depth n: a page step at depth 0 |

## Confirms

That the log space at a finite place is ℤ_p ⊕ ℤ[p] ⊕ ℤJ_p *with no finite pole*: every finite count of `[p]` is a legitimate log, and the valuation axis is a line with the pole beyond its upper end. The three laws of [[mult.black-hole]] and the two exclusions hold at the pole of the place as at ∞'s (the ledger: `mult.hole-exclusion` holds everywhere). It is **not** the other end: the negative counts of `[p]` are not the pole but legitimate logs whose instances the page refuses ([[place.no-inverse-of-the-prime]], [[place.two-ends]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | fails | at ∞ no finite count of logs instances to nothing: pⁿ is pⁿ |
| J1 | fails | as classical |
| JH, JO | untested | owed |
| JP | holds | the gathering steps inside the instance are absorbed; the void pile at depth 0 is a page step — p = 2, 3, 5, 7, depths 1 … 3 |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | EXACT | pⁿ = 0 in the finite ring |
| lambda, CC, logic | untested | — |

## Refuted readings

~~"`[o^{p}]^{n} ≐ □`: n copies of `[p]` are the pole at depth n"~~ — refuted 2026-10-06 (the place referee pass): with the void pile usable under a square the law derives `o^{5} ≐ void` at p = 5, depth 2, and makes juxtaposition non-associative in the reading (−[p] + [p] + [p] grouped two ways). The pole is the limit end; the finite count is this law.

## Notes

The schema's cardinality steps use [[schema.cardinality]] at count p, whose range runs to 12, so the law is checked at p = 2, 3, 5, 7 (13 would need a cardinality instance the chart does not have). The tape: absorbed (the unit inside the instance, gathering the logs) and the page step at depth 0; the law is ≃, the page's equality.
