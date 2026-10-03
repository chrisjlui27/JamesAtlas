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
law: "in the fragment {void, o, space}: o…o (m) ≐ o…o (n) iff m = n"
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
witness: tools/models/freeness_check.py
known_since: "Peano 1889 (the axioms); the fragment argument is immediate"
entered: 2026-10-03
guide: need-led
band: beyond
uses: [N.numeral, void.space, void.page]
see_also: [N.induction, N.successor, mult.consistency]
aliases: [Peano 3 and 4, injectivity of successor, no collapse]
concepts: [natural-number, consistency]
understood: yes
understood_note: "the fragment argument is clear; what happens once the axioms arrive is mult.consistency"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `oo ≐ ooo` is **not** derivable in the fragment | — | 2 ≠ 3 |

In the fragment of the calculus that has only the void, the unit and space — the rung-N calculus — two piles are equivalent exactly when they have the same count, and no pile is equivalent to the void.

## Plain

Different numbers of circles are different numbers: with nothing but circles on the page, there is no rule that could turn two into three.

## Derivation

| statement | rule | note |
|---|---|---|
| In the fragment {void, `o`, juxtaposition} there is no rewrite rule at all, so ≐ is identity of multisets | [[void.space]] [[N.numeral]] | the rung-N calculus has no axioms yet |
| two piles of units are the same multiset iff they have the same count | medium | — |
| hence `o^m ≐ o^n` iff m = n, and no pile is ≐ void | [[void.page]] | Peano 3 and 4 |

## Confirms

Peano's third and fourth axioms (S injective; 0 not a successor) — for the fragment, trivially and natively. Whether they *survive* once Involution, Distribution and Inversion arrive is a different theorem, with a different price: the consistency of the whole calculus, which the chart states at [[mult.consistency]] and which rests on a decree and an import. This node deliberately claims only what the fragment proves.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1, JH, JO | holds | the fragment is the same in every setting |
| JP | untested | at a finite place of depth N the pile p^N is **declared void** — the place calculus deliberately collapses piles; freeness there is a statement about residues |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | EXACT | cardinality is an isomorphism invariant |
| logic | ABSENT | Calling |
| lambda, CC | untested | — |

## Refuted readings

- ~~"nothing added later ever collapses two piles" follows from soundness in ℂ~~ — the first draft (2026-10-03) made this claim here with an `engine` badge; the referee pass the same day showed the unrestricted laws *do* collapse the calculus unless the undefined forms are excluded, and that nothing in the engine checks a meta claim. Moved to [[mult.consistency]], with its decree and import made explicit.

## Notes

The witness `tools/models/freeness_check.py` enumerates piles up to twelve units and confirms their canonical forms are pairwise distinct — all that a fragment with no rewrite rules can be asked to show.

The JP cell is the first place the chart shows the place calculus doing something *to* ℕ rather than *with* it: the void pile `p^N ≐ void` is a decree that breaks this theorem on purpose. That is a feature of the chart, not a bug of either calculus.
