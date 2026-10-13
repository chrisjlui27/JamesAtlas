---
id: place.ostrowski
title: The places of ℚ are the primes and ∞
type: import
level: meta
kind: declaration
rung: place
order: 1400
setting: JP
equality: "≡"
domain: natural
law: "IMPORT — every nontrivial absolute value on ℚ is equivalent to |·|_∞ or to one |·|_p (Ostrowski 1916): the chart's places are exactly the pages this rung draws, and no other"
units: "the Berkovich spectrum of ℤ: the trivial point at the centre, an archimedean branch, and one branch for each prime — each branch the powers |·|^ε of one absolute value"
gloss_check: ""
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: untested
  JP: holds
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: PARTIAL
  logic: untested
status: IMPORTED
verified: hand
known_since: "Ostrowski 1916; on the chart the ROADMAP (2026-10-03): 'the Berkovich spectrum of ℤ is the space of places; the chart cannot say \"at every place\" natively without a metric rung'"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [mult.c-reading, N.numeral]
see_also: [place.void-pile, place.wall, place.local-wall, J1.von-staudt-clausen, mult.c-reading]
aliases: [Ostrowski's theorem, the places of ℚ, the Berkovich base, all the pages there are]
concepts: [place, prime]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| the pages of this rung — one for each prime, declared by its void pile — together with ∞ are *all* the places of ℚ: there are no others | — | Ostrowski's theorem |

The rung that follows draws a page for each prime p ([[place.void-pile]]) and reads it ([[place.reading]]); the wall is the same on every one ([[place.wall]]) and the ψ-wall's count is a product over them ([[place.local-wall]]). What the chart cannot say natively is that these are *all* the places: that every way of measuring size on ℚ — every absolute value — is ∞'s ([[mult.c-reading]]) or one prime's. That is Ostrowski's theorem, and it needs the notion of an absolute value, which is the metric rung's (`analysis`: the Berkovich space *is* the set of seminorms). The rung imports it first, as rung `J1` imports von Staudt–Clausen ([[J1.von-staudt-clausen]]): named, priced as an import, and the one statement on this rung the engine cannot check. It is the price of the rung's meta-move — *at every place* — as [[N.induction]]'s gap is the price of *for every n*: every schema over the place p on this rung rests on it.

## Plain

There are exactly two kinds of place to do arithmetic: the usual one, and one for each prime. Nothing else. That fact has a name and a proof, and the chart borrows both.

## Derivation

none — an import, adjoined before the pages: it names the places the reading at ∞ ([[mult.c-reading]]) does not see — one for each prime, each the pile of that many marks ([[N.numeral]]) declared void. The proof is the classification of absolute values by whether |n| ≤ 1 for all integers n (non-archimedean: then |·| is some |·|_p) or not (archimedean: then |·| is a power of |·|_∞).

## Confirms

The completeness of the rung's list of pages. It is **not** the product formula ∏_v |x|_v = 1, which also waits for the metric rung and binds the places together; nor the adelic page.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | holds | the ∞ place is one of the two kinds |
| JO | untested | the places of a quaternion algebra over ℚ are those of ℚ where it ramifies; owed to rung `H` |
| JH | holds | the places of ℚ are the places of the centre of ℍ, and ℍ adds none: it ramifies at two of them and splits at the rest ([[H.ramification]]) |
| JP | holds | the import that closes the list |

| reading | cell | why |
|---|---|---|
| C | EXACT | ∞ |
| CC | PARTIAL | the points of the Berkovich spectrum of ℤ as the arithmetic site's places: a branch per prime, one archimedean branch, the trivial point at the centre; the reading in detail is owed |
| finset, lambda, logic | untested | — |

## Refuted readings

none

## Notes

The trivial absolute value — the centre of the Berkovich spectrum, from which one branch runs out to each prime and one to ∞, and where F₁ sits in every published road — is the place of rung `F1` (ROADMAP §4). Ostrowski names the places; it does not license the passage from the five primes the engine reads at to all of them — that passage is the import's price, as the passage from a schema's range to all n is the induction gap's.
