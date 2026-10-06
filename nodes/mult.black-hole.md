---
id: mult.black-hole
title: The black hole
type: definition
level: object
kind: law
rung: mult
order: 390
setting: classical
equality: "≐"
domain: complex
law: "□ := []"
units: "□ = ln 0 = −∞"
gloss_check: "BH"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "1993 (James)"
entered: 2026-10-03
guide: shape-led
band: beyond
uses: [mult.square, void.page]
see_also: [mult.hole-instance, mult.dominion, mult.hole-exclusion]
aliases: [□, "[ ]", empty square, log zero, minus infinity, black hole]
concepts: [zero, infinity, logarithm]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[]` | `□` | ln 0 = −∞ |

The empty square boundary — the abstract of the void — is a form the calculus can write and ℂ cannot value: the logarithm of zero. James calls it the black hole and writes it □. It is the second of the three empty boundaries to be something ([[N.unit]] is the first; `<>` is nothing, [[Z.void-inverse]]).

## Plain

Ask "what would I have to circle to get nothing?" — there is no answer, and the empty box is the name of that no-answer.

## Derivation

| form | rule | note |
|---|---|---|
| `[]` | [[mult.square]] | the square boundary around the void, [[void.page]] |
| `□` | definition | James's name |

## Confirms

That −∞ is a legitimate point of the *additive* layer: the calculus's log space is ℂ ∪ {−∞}, the way the extended reals absorb the log of zero. It is **not** "infinity" in the sense of 1/0 — that would be `(<□>)`, built on the excluded form `<□>` ([[mult.hole-exclusion]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | the same definition, the same three laws, the same two exclusions ([[J1.pole]]: "not a change of law"); what changes is the reading of the empty square from outside — □ is the **pole**, read by polarity (LEGISLATION 30f): inside an instance it is ✠, concession — `(A □) ≡ void` strictly; outside it is Ω, the log of nothing, already the whole coset −∞ + Λ (ln 0 has every branch: "pole = Λ"), so a unit step on pole-valued content has no winding to record and is strict — Dominion is ≡ |
| JH, JO | holds | the black hole "knows about singular matrices" (JH-20) |
| JP | holds | at a place □ sits at the end of the rung-count axis: −∞ at ∞, +∞·[p] at p — a consequence of the rung's size, not a choice (p-adic-wall) |

| reading | cell | why |
|---|---|---|
| C | EXACT | as a point of the extended log space |
| finset | ABSENT | — |
| logic | untested | — |
| lambda, CC | untested | — |

## Refuted readings

- ~~□ is +∞~~ — Lui confirmed 2026-09-13 that □ is log 0 = −∞ when the engine labelled its valuation +∞; the sign depends on which axis (value or valuation) is meant.

## Notes

Domain `complex` (widened 2026-10-03, C referee pass): rung C instantiates this law at complex content, and a law may be cited only inside its declared domain ([[mult.consistency]], Confirms); the law is exact on ℂ ∪ {□}. The home band and reading are unchanged.

`[[]]` — the square of the black hole — is James's other undefined form ([[mult.hole-exclusion]]); Bricken (Iconic Arithmetic) reads it as complex infinity. The census lists every form containing it as undefined.
