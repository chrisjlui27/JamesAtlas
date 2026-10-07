---
id: place.void-pile
title: A place is a pile declared void
type: decree
level: object
kind: declaration
rung: place
order: 1402
setting: JP
equality: "≃"
domain: natural
law: "o^{p**n} ≃ void"
units: "p^n ≡ 0: the page at the finite place p, to depth n, is ℤ/p^n — a pile of p^n marks is nothing there; at ∞ no pile is void"
gloss_check: ""
schema_range: "p=2,3,5,7,13; n=1..3"
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
status: NATIVE-BY-DECREE
verified: engine
known_since: "2026-09-13 (Forms at Every Place: the place is a pile declared void — p^N marks ≐ void; the three place-data are one datum); as ℤ/p^N, Gauss 1801"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [N.numeral, void.page, place.ostrowski]
see_also: [N.freeness, Z.normal-form, J1.period-form, place.ostrowski, place.reading, place.residue, place.prime-power]
aliases: [the void pile, the page at p, ℤ/p^n, depth, Axiom 5 (Depth), p^N ≐ void]
concepts: [place, zero, one, induction]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `o^{p**n} ≃ void` | at the place p, to depth n, a pile of p^n marks is the void — the page's own law, declared, not derived | p^n ≡ 0 (mod p^n): the ring ℤ/p^n |

A **place** is where a pile is void. The chart so far has lived at one place, ∞, where no pile is ever void ([[N.freeness]]: distinct piles are distinct) and the only thing declared void is a lattice inside an instance (the wall, [[J1.absorption]]). A finite place is the other possibility: a pile of p^n marks is declared void on the page itself — the void pile. Everything the place calculus has — the irreducible log of the prime, the radius of the instance, the selection of which fractions of the period are forms — is downstream of this one declaration, through the reading that reads the page ([[place.reading]]): *the three place-data are one datum, the void pile* (JP ledger, 2026-09-13). The depth n is the page's resolution; at depth n every number is a residue, a doll of n shells ([[place.doll]]), and the instance of n copies of the prime's log is this void pile ([[place.prime-power]]).

**The discipline of the page** (LEGISLATION 31(g), pending Lui). The equality this decree declares is the page's: two forms are equal at depth n when their values agree mod pⁿ. It passes through juxtaposition, angles and instances — exp(p^n) ≡ 1 — but **not through a square**: `[o^{p**n}]` is n copies of `[p]`, a finite log, and `[void]` is the pole; the log of a non-unit loses as many shells as its count of `[p]`. So a law of the page — this one, and every law derived from it by the page's equality alone: [[place.residue]], [[place.negation-is-a-pile]], [[place.fermat]], [[place.division-by-unit]], [[place.prime-power]], [[place.geometric-doll]] — is written with ≃, and the receipt prover grades a page step by position: `page` with no square anywhere above it (an instance only page-equalizes a page difference — it does not pay it, as it pays a period — so a square above an instance still reads the difference, as the period at the point where a content is exactly one); with a square above it, measured at every square above — an import where no square's value changes, absorbed or posted where some change by a period (the outermost changed square posts the receipt; the instance directly outside it pays it, or it stays on the tape at depth 0), absent otherwise (SPEC §5.5). Without the discipline the page collapses: with the void pile a rewrite rule under a square, `o^{5} ≐ void` is derivable at p = 5, depth 2 (the referee's chain, 2026-10-06), and the first draft's `[p]^{n} ≐ □` was withdrawn for the same reason.

The ∞ place and the finite places are one schema — *a subgroup of the additive layer declared void at a depth*: (ℤω, 1) is the enriched ∞ (the lattice void inside one instance: the wall), (ℤω, 0) the classical crack (the lattice void on the page: `J J ≐ void`), (p^n·o, 0) the finite place (a pile void on the page).

## Plain

Count to p^n and you are back at nothing: that is what it means to be at the place p, to depth n. At ∞ you never come back; at a finite place the page is a clock face with p^n hours.

## Derivation

none — declared. The pile of pⁿ marks ([[N.numeral]]) is declared the void ([[void.page]]) on the page at p to depth n. The decree is written over the place and the depth, and the engine reads each instance at its own place — p = 2, 3, 5, 7, 13 and n = 1 … 3 — checking that the pile reads 0 there; a law over the place p rests on the import that lists the places ([[place.ostrowski]]), as a schema over n rests on the induction gap. It is the first law of the chart that is *false at ∞* and *true at p*; the place is the parameter that decides.

## Confirms

ℤ/p^n as a page: the arithmetic of residues, the clock. It is **not** ℤ_p: the whole p-adic integer is the compatible tower of pages at every depth, which the chart's finite page does not contain ([[place.completion]]). It is **not** a new boundary: no fourth boundary is drawn; a pile is declared void, as James's own exclusions declare a form absent.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | fails | no pile is void at ∞ ([[N.freeness]]): the law is the place's, and ∞ is not a finite place |
| J1 | fails | as classical: 𝕁₁ at ∞ keeps every pile |
| JH, JO | untested | the Hurwitz places (rung `H`) have their own void piles — the primes where the quaternions ramify; owed |
| JP | holds | the declaration of the setting, at p = 2, 3, 5, 7, 13 and depths 1 … 3 (the engine reads each instance at its own place); a page law — ≃, not under a square |

| reading | cell | why |
|---|---|---|
| C | ABSENT | ℂ has no void pile |
| finset | EXACT | a finite set of p^n elements with the pile wrapping: ℤ/p^n |
| lambda, CC, logic | untested | — |

## Refuted readings

~~"([p]^∞ [Z]) ≡ void is a new p-adic axiom"~~ — refuted 2026-09-13: it is the black hole, `(□) ≐ void`, which the chart already has ([[mult.hole-instance]]); the void pile is the only new declaration.

## Notes

A decree written over the place and the depth, so that the engine checks it at every instance (the pile of p^n marks reads 0 at depth n): the only declared-void pile on the chart (SPEC §2.1 lists "a declared-void pile" among the decrees), and the one that enters the price of every law of the rung. The depth is a parameter of the page, not a form on it; the lens that reads a form to n shells as a form of its own is the JP ledger's, and is the gap [[place.completion]].
