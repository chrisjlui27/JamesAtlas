---
id: place.geometric-doll
title: The doll of 1/(1 − p)
type: schema
level: object
kind: law
rung: place
order: 1535
setting: JP
equality: "≃"
domain: natural
law: "Σ{j=0..n-1: ([o^{p}]^{j})} ≃ (<[o <o^{p}>]>)"
units: "1 + p + p² + ⋯ + p^{n−1} ≡ 1/(1 − p) (mod p^n): the geometric series converges at p, and its doll is the re-entry x ≐ o ([p][x]) unfolded n times; at p = 2 it is −1 = …111"
gloss_check: ""
schema_range: "(p,n)=(2,2),(2,3),(3,1),(3,2),(3,3)"
schema_draw: "p=2; n=3"
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
known_since: "2026-09-13 (JP-1: the guarded re-entry x ≐ A ([p][x]) converges; rationals are the re-entrant dolls); 2026-09-19 ('x ≐ o ([oo][x]) converges to <o> at p = 2; at odd p it is neutral; at ∞ it repels'); Hensel 1908"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [J1.counit, Z.inversion, J1.unit, mult.distribution, mult.log-of-one, C.phase-rule, C.phase-under-instance, Z.collection, place.prime-power, Z.void-inverse, place.ostrowski]
see_also: [place.doll, place.negation-is-a-pile, place.division-by-unit, place.completion, Q.reciprocal]
aliases: [the geometric doll, 1/(1−p) at p, "x ≐ o ([p][x])", re-entry, the re-entrant doll, JP-1]
concepts: [place, induction, division, one]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `Σ{j=0..n-1: ([o^{p}]^{j})} ≃ (<[o <o^{p}>]>)` | the sum of the powers of p below the depth is the reciprocal of 1 − p: the doll of a fraction | Σ_{j<n} p^j = (1 − p^n)/(1 − p) ≡ 1/(1 − p) mod p^n |

At ∞ the series 1 + p + p² + ⋯ runs off; at the place p its partial sums *settle*, because each term is a shell deeper than the last and the void pile swallows the tail. Their limit is the fraction 1/(1 − p) — at p = 2, that is −1, the pile of all ones ([[place.negation-is-a-pile]]). The law is a finite sum, stated at a depth; what it unfolds is the chart's first **re-entry**: the doll x = 1 + p·x, unfolded n times, is this sum, and the void pile is what makes the unfolding settle — JP-1, the re-entry convention of the JP ledger: a guarded re-entry (one whose cycle passes through `[p]`) converges, one shell per pass; the re-entry itself, with a shell at every depth, is the gap [[place.completion]]. The derivation is the telescoping product: multiply the sum by 1 − p, every term cancels but the first and the one past the depth, and that one is void ([[place.prime-power]]) — a page step under the square of the log, measured at the squares above it, here one: the square's content goes from 1 − pⁿ to exactly one, its value from a principal part that vanishes at the depth to the period ω_p, and the instance directly outside pays that period (absorbed), with no square above the instance. The law is ≃: the page's equality, and a period absorbed.

## Plain

Add 1, p, p², … up to p^{n−1} on the clock with p^n hours and you land on 1/(1 − p). At p = 2 that is −1: one plus two plus four plus eight… equals minus one.

## Derivation

| form | rule | note |
|---|---|---|
| `Σ{j=0..n-1: ([o^{p}]^{j})}` | given | 1 + p + ⋯ + p^{n−1}, each power as j copies of `[p]` instanced; at every place ([[place.ostrowski]]) |
| `([Σ{j=0..n-1: ([o^{p}]^{j})}])` | [[J1.counit]] | the counit, right to left: the sum wrapped |
| `([Σ{j=0..n-1: ([o^{p}]^{j})}] [o <o^{p}>] <[o <o^{p}>]>)` | [[Z.inversion]] | the log of 1 − p and its mirror created inside: multiply and divide by 1 − p |
| `([([Σ{j=0..n-1: ([o^{p}]^{j})}] [o <o^{p}>])] <[o <o^{p}>]>)` | [[J1.unit]] | the product gathered under one abstract, directly inside the instance: absorbed |
| `([([Σ{j=0..n-1: ([o^{p}]^{j})}] [o]) ([Σ{j=0..n-1: ([o^{p}]^{j})}] [<o^{p}>])] <[o <o^{p}>]>)` | [[mult.distribution]] | the sum times (1 − p) is the sum times 1 beside the sum times −p |
| `([Σ{j=0..n-1: ([o^{p}]^{j})} ([Σ{j=0..n-1: ([o^{p}]^{j})}] [<o^{p}>])] <[o <o^{p}>]>)` | [[mult.log-of-one]] [[J1.counit]] | times one is itself: the log of one erased, the counit |
| `([Σ{j=0..n-1: ([o^{p}]^{j})} ([Σ{j=0..n-1: ([o^{p}]^{j})}] [([o^{p}] J)])] <[o <o^{p}>]>)` | [[C.phase-rule]] | −p is the instance of log p beside J: the Phase rule, right to left |
| `([Σ{j=0..n-1: ([o^{p}]^{j})} ([Σ{j=0..n-1: ([o^{p}]^{j})}] [o^{p}] J)] <[o <o^{p}>]>)` | [[J1.unit]] | the unit inside the instance: absorbed |
| `([Σ{j=0..n-1: ([o^{p}]^{j})} <([Σ{j=0..n-1: ([o^{p}]^{j})}] [o^{p}])>] <[o <o^{p}>]>)` | [[C.phase-under-instance]] | J under the instance is a sign: minus the product with p |
| `([Σ{j=0..n-1: ([o^{p}]^{j})} <Σ{j=0..n-1: ([([o^{p}]^{j})] [o^{p}])}>] <[o <o^{p}>]>)` | [[mult.distribution]] | the product distributed over the sum, one instance per term |
| `([Σ{j=0..n-1: ([o^{p}]^{j})} <Σ{j=0..n-1: ([o^{p}]^{j+1})}>] <[o <o^{p}>]>)` | [[J1.unit]] [[mult.log-of-one]] | each `[([p]^{j})]` opened: the unit inside the instance, absorbed — p^j · p is p^{j+1}; the j = 0 term is the log of one |
| `([Σ{j=0..n-1: ([o^{p}]^{j})} Σ{j=0..n-1: <([o^{p}]^{j+1})>}] <[o <o^{p}>]>)` | [[Z.collection]] | the mirror distributed over the sum |
| `([o <([o^{p}]^{n})>] <[o <o^{p}>]>)` | [[Z.inversion]] | the telescope: every p^j with 0 < j < n meets its mirror; one and minus p^n remain |
| `([o <>] <[o <o^{p}>]>)` | [[place.prime-power]] | pⁿ is the void pile at depth n: a page step under the square, measured at the square above it — its value changes by the period, which the instance directly outside absorbs |
| `([o] <[o <o^{p}>]>)` | [[Z.void-inverse]] | the mirror of nothing is nothing |
| `(<[o <o^{p}>]>)` | [[mult.log-of-one]] | the log of one erased, inside the instance: 1/(1 − p) |

## Confirms

The convergence of the geometric series in ℚ_p and the doll of a rational number: the rationals are exactly the eventually periodic dolls, the re-entrant ones (JP ledger, EXACT), and this is the simplest, with every digit 1. It is **not** the limit itself: the law is at depth n, and the infinite doll is the compatible tower of these, the gap [[place.completion]]. It is **not** a convergence at ∞: there the same unfolding repels (1, 3, 7, 15, …), and at an odd prime other than p the form `o ([oo][x])` is *neutral* — 2 is a unit there and nothing shrinks. The place supplies the guard.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | fails | the series diverges at ∞; 1 + 2 + 4 + 8 is not −1 there |
| J1 | fails | as classical |
| JH, JO | untested | owed |
| JP | holds | absorbed receipts at p = 2, 3 and depths 1 … 3 (the unit inside the instance; the page step measured at its square) — a page law, ≃ |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | EXACT | the sum in ℤ/p^n |
| lambda, CC, logic | untested | — |

## Refuted readings

~~"every p-adic number is a re-entry"~~ — refuted 2026-09-19: finite re-entry systems are countable; completion must enter as a rule ([[place.completion]]).

## Notes

The schema runs at p = 3 to depths 1 … 3 and at p = 2 to depths 2, 3 (at depth 3 the sum has three terms and the telescope two cancellations); the derivation is the same at every p and n, and the prover licenses each instance row by row. At p = 2, depth 1, the law is true (the one-term sum, 1 ≡ −1 mod 2) but not by this derivation: 1 − p is −1 there, not a principal unit, and the page step at the square `[o <(oo)>]` → `[o]` changes the square's value by half a period, J₂, which no instance absorbs — the prover grades it absent, and the instance is left out of the range. The guard — "`[p]` shrinks" — is semantic: it is the void pile acting through [[place.prime-power]], not a rule of its own (the JP ledger's load-bearing gap, paid here by the void pile and its discipline, LEGISLATION 31(g)).
