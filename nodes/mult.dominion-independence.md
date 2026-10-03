---
id: mult.dominion-independence
title: Dominion is independent of Involution and Distribution
type: theorem
level: meta
kind: law
rung: mult
order: 430
setting: classical
equality: "≐"
domain: positive
law: "□ A ≐ □ is not derivable from Involution + Distribution; it is derivable once Inversion is adjoined"
units: "a semiring need not have an absorbing zero; a ring must"
witness: tools/models/dominion_models.py
holds:
  classical: holds
  J1: untested
  JH: untested
  JO: untested
  JP: holds
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "semiring theory, for the shape of the fact (an absorbing zero is an axiom of semirings because it is independent of the others); the James-specific witness with the exp/log bijection: this chart, 2026-10-03"
entered: 2026-10-03
guide: need-led
band: beyond
uses: [mult.involution, mult.distribution, Z.inversion, mult.dominion, mult.zero-annihilates, mult.hole-instance, void.space]
see_also: [N.freeness, mult.hole-instance]
aliases: [dominion independence, the 3-element model]
concepts: [consistency, infinity]
understood: partial
understood_note: "I follow the model; I want to see it drawn"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| no derivation of `□ A ≐ □` uses only [[mult.involution]] and [[mult.distribution]] | — | there is a model of {Involution, Distribution} in which □ ≠ void and □ does not absorb |

## Plain

Without the mirror, the page cannot prove that the bottomless pit swallows everything; here is a tiny toy world where it doesn't.

## Derivation

| statement | rule | note |
|---|---|---|
| A model of the medium plus Involution and Distribution is a commutative monoid (M, +, 0) — the multiset syntax forces commutativity and associativity — with a bijection e : M → M (the round boundary), l = e⁻¹ (the square), satisfying e(a + l(b + c)) = e(a + l b) + e(a + l c) for all a, b, c; the angle boundary may be interpreted by any map, since no axiom of this fragment constrains it | [[void.space]] [[mult.involution]] [[mult.distribution]] | any equational derivation is sound in any such total algebra |
| Take M = {0, 1, 2} with 0 the unit, 1 + 1 = 1, 1 + 2 = 1, 2 + 2 = 2; e(0) = 2, e(1) = 1, e(2) = 0 | — | the witness; `tools/models/dominion_models.py` checks all 27 instances of Distribution |
| In this model □ = l(0) = 2 ≠ 0 = void, and `(□)` = e(2) = 0 = void as [[mult.hole-instance]] requires — but □ + 1 = 2 + 1 = 1 ≠ 2, so `□ A ≐ □` fails at A = 1 | — | hence [[mult.dominion]] is not derivable from the two axioms |
| M is not a group (1 has no inverse), so [[Z.inversion]] has no interpretation here — consistent with the derivation of [[mult.zero-annihilates]] and [[mult.dominion]] through Inversion | — | the other two axioms do not suffice; with Inversion (by those nodes) they do |

The script also reports the census of *labelled* structures (not isomorphism classes): of all commutative monoids of order ≤ 4 with a bijection satisfying Distribution, Dominion fails in 1 of 2 (order 2), 4 of 8 (order 3), 42 of 78 (order 4); those counts include degenerate models with □ = void, and only the chosen witness insists on □ ≠ void. `(□) ≐ void` holds in every model, as it must — it is Involution at 0 ([[mult.hole-instance]]).

## Confirms

That James's three axioms are not redundant *for this theorem*: the additive-inverse axiom is what makes zero absorbing, exactly as in algebra at large — absorption (0·a = 0) must be *postulated* in a semiring because it does not follow from distributivity and the monoid laws, and is *derived* in a ring. The witness model is itself such a structure: a commutative pre-semiring with unit e(0) = 2 in which 0·1 = 1. The shape of the fact is textbook; what this node adds is the James-specific witness, with the exp/log bijection in place, showing where in the chart the cost falls.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | a meta-theorem about the classical axioms |
| J1 | untested | the J1 axiom set differs (weakened unit, period axiom); the independence question must be re-posed |
| JH, JO | untested | Involution is guarded and Distribution replaced there; the question must be re-posed in the same way |
| JP | holds | keeps the classical axioms; the derivation stands |

| reading | cell | why |
|---|---|---|
| C | EXACT | a statement about derivability, witnessed by a finite model; "Dominion is not derivable from Involution + Distribution" means: over the multiset medium, with the angle boundary unconstrained |
| others | untested | — |

## Refuted readings

none

## Notes

Method note for the chart: this is the template for every *independence* node — a finite model found by brute force, stored under `tools/models/`, cited as `witness:` in the front matter, and re-run by the checker.
