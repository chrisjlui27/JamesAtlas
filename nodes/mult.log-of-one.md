---
id: mult.log-of-one
title: The log of one is nothing
type: theorem
level: object
kind: law
rung: mult
order: 335
setting: classical
equality: "≐"
domain: natural
law: "[o] ≐ void"
units: "ln 1 = 0"
gloss_check: ""
holds:
  classical: holds
  J1: holds-mod-Λ
  JH: holds-mod-Λ
  JO: holds
  JP: holds-mod-Λ
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "1993 (James, Ch. 4 §4.3, p. 26: 'An element multiplied by the unit reduces to itself by involution, ([a][()]) = ([a]) = a' — the first step is this law); ln 1 = 0 is Napier's (1614)"
entered: 2026-10-04
guide: shape-led
band: "3–5"
uses: [N.unit, mult.involution]
see_also: [mult.unit-law, mult.involution, N.unit, C.period-absorption]
aliases: ["[o] = void", ln 1 = 0, log of one, "[()] ≐ void", the unit at void]
concepts: [one, logarithm, void]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[o] ≐ void` | the abstract of one is nothing | ln 1 = 0 |

The square around the empty round is nothing at all: `[()]` is the unit half of Involution — `[(A)] ≐ A` — at A = void. It is the smallest law on the chart with a square in it, and the one the whole enriched calculus turns on.

## Plain

Take the log of 1 and you get 0. On the page: a box around an empty circle is the same as nothing.

## Derivation

| form | rule | note |
|---|---|---|
| `[o]` | given | the abstract of one, `o` = `()` ([[N.unit]]) |
| `[()]` | definition | unfold the abbreviation |
| `void` | [[mult.involution]] | the unit `[(A)] ≐ A` at A = void: the abstract of the instance of nothing is nothing |

## Confirms

ln 1 = 0 — the log of the multiplicative unit is the additive unit. Every use of "`[o] ≐ void`" on the chart (the unit law `([A][o]) ≐ A`, every removal of a count of one, every `[o] → void` inside a power) is this law and nothing else, so it is a node of its own rather than a line in [[mult.unit-law]]. It is **not** a free fact: it is one unit step, at void content — and in `J1` that step is exactly the one that is weakened. There `[()]` is not void but the period form ω, and `[()] ≃ void` holds only with the receipt ω: this law is the classical shadow of the lattice. (The engine's seam check exempts the unit at void content from the decree because the classical reading makes it exact, ln 1 = 0 — SPEC §4.3; it is not a theorem of the hole rules, and the 𝕁₁ reading, in which the log of exactly one is ω, keeps every hole rule and falsifies it.)

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds-mod-Λ | `[()]` is ω, the generator of Λ, not void: the law holds mod Λ with receipt ω and fails strictly — the first law to change in 𝕁₁ |
| JO | holds | the log of the unit is void in every slice |
| JH | holds-mod-Λ | as in 𝕁₁: `[(void)] → void` posts the receipt ω, now the pinned 2πi (census/h-ledger.md) |
| JP | holds-mod-Λ | `[o]` reads ω_p = (p−1)·J_p at a finite place, the generator of the kernel of the instance there ([[place.torsion]], [[place.reading]]): the law holds mod Λ_p with receipt ω_p, exactly as in 𝕁₁ — the place ledger |

| reading | cell | why |
|---|---|---|
| C | EXACT | ln 1 = 0 |
| finset | untested | the abstract of a one-element set — whether `[ ]` has a finset reading at all is open from [[mult.square]] on |
| logic | untested | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Split out of [[mult.unit-law]] on 2026-10-04 when the derivation checker (`tools/prover.py`) showed sixteen rows citing the unit law for a step the unit law does not state. One law per node (LEGISLATION 4).
