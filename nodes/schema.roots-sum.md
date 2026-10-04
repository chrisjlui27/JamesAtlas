---
id: schema.roots-sum
title: The n-th roots of unity add to nothing
type: schema
level: object
kind: law
rung: schema
order: 1160
setting: classical
equality: "≐"
domain: positive
law: "Σ{j=1..n: (([J] [o^{2j}] <[o^{n}]>))} ≐ void"
units: "ω + ω² + … + ωⁿ = 0  (n ≥ 2)"
gloss_check: ""
schema_range: "n=2..6"
schema_draw: "n=3"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE-BY-SCHEMA
verified: engine
known_since: "the cyclotomic relation: Gauss 1801 (Disquisitiones, §§ 335–366) for the general theory; the sum of the roots as a Vieta relation is older"
entered: 2026-10-03
guide: need-led
band: "9–12"
uses: [C.phase, schema.roots-of-unity, mult.unit-law, Q.self-division, mult.involution, mult.distribution, mult.inverse-promotion, Z.collection, Z.inversion, schema.cardinality, mult.cardinality, C.period-absorption, mult.black-hole, mult.zero-annihilates]
guarded_by: [mult.seam-decree]
see_also: [C.omega-sum, schema.roots-of-unity, Q.self-division, C.period-absorption]
aliases: [cyclotomic relation, sum of the roots of unity, "1 + ω + … + ω^{n−1} = 0"]
concepts: [root, phase, zero, induction]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `Σ{j=1..n: ω^j} ≐ void`, ω^j = `(([J] [o^{2j}] <[o^{n}]>))` | the n-th roots of unity, juxtaposed, are nothing | 1 + ω + ω² + … + ω^{n−1} = 0 |

The first cyclotomic relation for every n: the n-th roots of unity sum to zero. [[C.omega-sum]] is the case n = 3; the proof is the same — multiply by (ω − 1)/(ω − 1), telescope, and divide nothing — written once as a template over n.

## Plain

Points spaced evenly round a circle pull against each other to nothing. Multiplying the sum by ω − 1 shifts every term one place round; all but the ends cancel, and the ends meet after a whole turn.

## Derivation

| form | rule | note |
|---|---|---|
| `Σ{j=1..n: (([J] [o^{2j}] <[o^{n}]>))}` | given | the sum of the n-th roots of unity ω, ω², …, ωⁿ, each a fractional count of J ([[C.phase]], [[schema.roots-of-unity]]) |
| `([Σ{j=1..n: (([J] [o^{2j}] <[o^{n}]>))}] [o])` | [[mult.unit-law]] | `A ≐ ([A] [o])`, right to left |
| `([Σ{j=1..n: (([J] [o^{2j}] <[o^{n}]>))}] [([(([J] [oo] <[o^{n}]>)) <o>] <[(([J] [oo] <[o^{n}]>)) <o>]>)])` | [[Q.self-division]] | `o ≐ ([B] <[B]>)` with B = ω − 1, which is not void for n ≥ 2 — right to left, inside the square |
| `([Σ{j=1..n: (([J] [o^{2j}] <[o^{n}]>))}] [(([J] [oo] <[o^{n}]>)) <o>] <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[mult.involution]] | the unit, directly inside the instance — absorbing (and its content is void) |
| `([([Σ{j=1..n: (([J] [o^{2j}] <[o^{n}]>))}] [(([J] [oo] <[o^{n}]>)) <o>])] <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[mult.involution]] | the unit right to left on `[S] [ω − 1]` — absorbing; the content is the hole, since S is void |
| `([([Σ{j=1..n: (([J] [o^{2j}] <[o^{n}]>))}] [(([J] [oo] <[o^{n}]>))]) ([Σ{j=1..n: (([J] [o^{2j}] <[o^{n}]>))}] [<o>])] <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[mult.distribution]] | distribute S over `ω <o>` |
| `([([Σ{j=1..n: (([J] [o^{2j}] <[o^{n}]>))}] [(([J] [oo] <[o^{n}]>))]) <([Σ{j=1..n: (([J] [o^{2j}] <[o^{n}]>))}] [o])>] <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[mult.inverse-promotion]] | — |
| `([([Σ{j=1..n: (([J] [o^{2j}] <[o^{n}]>))}] [(([J] [oo] <[o^{n}]>))]) <Σ{j=1..n: (([J] [o^{2j}] <[o^{n}]>))}>] <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[mult.unit-law]] | `([S] [o]) ≐ S` |
| `([Σ{j=1..n: ([(([J] [o^{2j}] <[o^{n}]>))] [(([J] [oo] <[o^{n}]>))])} <Σ{j=1..n: (([J] [o^{2j}] <[o^{n}]>))}>] <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[mult.distribution]] | distribute ω over the n summands of S — Distribution n − 1 times |
| `([Σ{j=1..n: (([J] [o^{2j}] <[o^{n}]>) ([J] [oo] <[o^{n}]>))} <Σ{j=1..n: (([J] [o^{2j}] <[o^{n}]>))}>] <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[mult.involution]] | the unit on each abstract, directly inside its instance — absorbing (2n applications) |
| `([Σ{j=2..n+1: (([J] [o^{2j}] <[o^{n}]>))} <Σ{j=1..n: (([J] [o^{2j}] <[o^{n}]>))}>] <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[mult.distribution]] | in each product, collect the two counts over the shared `[J] <[n]>`, right to left: ω^j · ω is ω^{j+1} — the sum is re-indexed |
| `([Σ{j=2..n+1: (([J] [o^{2j}] <[o^{n}]>))} Σ{j=1..n: <(([J] [o^{2j}] <[o^{n}]>))>}] <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[Z.collection]] | the mirror of the sum is the sum of the mirrors, right to left (n − 1 applications) |
| `([(([J] [o^{2n+2}] <[o^{n}]>)) <(([J] [oo] <[o^{n}]>))>] <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[Z.inversion]] | ω² … ωⁿ cancel against their mirrors (n − 1 pairs): what is left is ω^{n+1} − ω |
| `([(([J] [o^{2n}] <[o^{n}]>) ([J] [oo] <[o^{n}]>)) <(([J] [oo] <[o^{n}]>))>] <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[mult.distribution]] | ω^{n+1} = ωⁿ · ω: distribute the counts 2n and 2 over the shared `[J] <[n]>` |
| `([(([J] [([o^{n}] [oo])] <[o^{n}]>) ([J] [oo] <[o^{n}]>)) <(([J] [oo] <[o^{n}]>))>] <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[schema.cardinality]] | the pile 2n is two copies of the pile n: `o^{n} o^{n} ≐ ([o^{n}] [oo])` |
| `([(([J] [o^{n}] [oo] <[o^{n}]>) ([J] [oo] <[o^{n}]>)) <(([J] [oo] <[o^{n}]>))>] <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[mult.involution]] | the unit, directly inside its instance — absorbing (content real) |
| `([(([J] [oo]) ([J] [oo] <[o^{n}]>)) <(([J] [oo] <[o^{n}]>))>] <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[Z.inversion]] | the count n and its mirror cancel: ωⁿ is `(J J)` |
| `([(J J ([J] [oo] <[o^{n}]>)) <(([J] [oo] <[o^{n}]>))>] <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[mult.cardinality]] | right to left: `([J] [oo]) ≐ J J` |
| `([(([J] [oo] <[o^{n}]>)) <(([J] [oo] <[o^{n}]>))>] <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[C.period-absorption]] | the whole turn inside the instance is forgotten: ω^{n+1} is ω |
| `(□ <[(([J] [oo] <[o^{n}]>)) <o>]>)` | [[Z.inversion]] | ω and its mirror cancel; the abstract of nothing is the black hole ([[mult.black-hole]]) |
| `void` | [[mult.zero-annihilates]] | `(□ C) ≐ void`: nothing divided by ω − 1 is nothing |

## Confirms

Σ ω^j = 0 for n ≥ 2, the sum of all n-th roots of unity, proved by telescoping: (ω − 1)·Σ_{j=1}^{n} ω^j = ω^{n+1} − ω = 0 since ω^{n+1} = ω by a whole turn ([[C.period-absorption]]), and dividing nothing by ω − 1 ≠ 0 is nothing. The rows with Σ are templates: "Distribution n − 1 times", "Inversion, n − 1 pairs"; the engine instantiates them for n = 2 … 6 and checks each. It is **not** a statement about the *proper* n-th roots alone (the primitive ones sum to the Möbius value μ(n)), and it is **not** Gauss's theory of periods — only its first identity. Every row has the value 0, so, as for [[C.omega-sum]], the engine certifies 0 = 0 and the seam check; the licensing is the referee's.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step directly under an instance, through an angle at most |
| JH, JO | holds | per slice |
| JP | guarded | as [[schema.roots-of-unity]], and ω − 1 must be a unit at p |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Guarded by position (Amendment A2): the units on the abstracts of ω^j and ω have content 2jπi/n, off the strip for 2j > n; they sit directly inside instances. Checked for n = 2 … 6; the card draws n = 3.
