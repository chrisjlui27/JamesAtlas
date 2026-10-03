---
id: N.freeness
title: Distinct piles are distinct
type: theorem
level: meta
kind: law
rung: N
order: 170
setting: classical
equality: "≐"
domain: natural
law: "o…o (m) ≐ o…o (n)  iff  m = n"
units: "S(m) = S(n) ⇒ m = n ;  S(n) ≠ 0"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: untested
readings:
  C: EXACT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "Peano 1889 (the axioms); 1993 (soundness of the calculus in ℂ is James's Chapter 5)"
entered: 2026-10-03
guide: need-led
band: beyond
uses: [N.numeral, void.space, void.page]
see_also: [N.induction, N.successor]
aliases: [Peano 3 and 4, injectivity of successor, no collapse]
concepts: [natural-number, consistency]
understood: partial
understood_note: "the fragment argument is clear; the full-calculus argument rests on the ℂ model"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `oo ≐ ooo` is **not** derivable | — | 2 ≠ 3 |

Two piles are equivalent in the calculus exactly when they have the same count. In particular no pile is equivalent to the void.

## Plain

Different numbers of circles are different numbers; the calculus never confuses two with three.

## Derivation

| statement | rule | note |
|---|---|---|
| In the fragment {void, `o`, juxtaposition} there is no rewrite rule at all, so ≐ is identity of multisets | [[void.space]] [[N.numeral]] | the rung-N calculus has no axioms yet |
| two piles of units are the same multiset iff they have the same count | medium | — |
| hence `o^m ≐ o^n` iff m = n, and no pile is ≐ void | [[void.page]] | Peano 3 and 4 |
| In the *full* classical calculus the same holds because every axiom preserves the ℂ value, and distinct counts have distinct values | — | soundness in ℂ: an **import** at the meta level (the existence of a model) |

## Confirms

Peano's third and fourth axioms (S injective; 0 not a successor). The fragment proof is trivial and native. The full-calculus statement — that nothing added later (Involution, Distribution, Inversion, J) ever collapses two piles — is *consistency relative to ℂ*: a meta-theorem proven by a model, not by a derivation. The chart records that as the one import at this rung and keeps it visible: the shadow checker in `tools/check.py` is this model, mechanized.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1, JH, JO | holds | each has a sound model (ℂ; ℂ with Λ; ℍ per slice; 𝕆) |
| JP | untested | at a finite place of depth N the pile p^N is **declared void** — the place calculus deliberately collapses piles; freeness there is a statement about residues |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | EXACT | cardinality is an isomorphism invariant |
| logic | ABSENT | Calling |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The JP cell is the first place the chart shows the place calculus doing something *to* ℕ rather than *with* it: the void pile `p^N ≐ void` is a decree that breaks this theorem on purpose. That is a feature of the chart, not a bug of either calculus.
