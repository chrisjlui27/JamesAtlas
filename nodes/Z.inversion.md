---
id: Z.inversion
title: Inversion
type: axiom
level: object
kind: law
rung: Z
order: 210
setting: classical
equality: "≐"
domain: complex
law: "A <A> ≐ void"
units: "a + (−a) = 0"
gloss_check: "0"
holds:
  classical: holds
  J1: guarded
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James), axiom 3 of three"
entered: 2026-10-03
guide: shape-led
band: "1–2"
uses: [Z.angle, void.space, void.page]
see_also: [Z.cancellation, Z.collection, mult.dominion]
aliases: [Inversion, James axiom 3, annihilation, A3, "reflection (Bricken's name)"]
concepts: [negation, zero, inverse]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `A <A> ≐ void` | — | a + (−a) = 0 |

A form and its inverse, standing together, annihilate. Read right-to-left: a pair `A <A>` may be created from nothing. Both directions are used constantly.

## Plain

A pile and its opposite cancel to nothing; and out of nothing you may always conjure a pile together with its opposite.

## Derivation

none — adjoined. The third of James's three axioms, stated in terms of the angle boundary [[Z.angle]], juxtaposition [[void.space]] and the void [[void.page]].

## Confirms

That `(ℤ, +)` is a group: every element has an inverse. Together with the medium ([[void.space]], [[void.page]]) this is the whole group structure. It is **not** the statement that `<>` is void, nor that `<<A>> ≐ A` — those are theorems ([[Z.void-inverse]], [[Z.cancellation]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | axiom |
| J1 | guarded | **stratified** (legislation 2026-08-22): `A<A> ≐ void` in some contexts and `≃ ω` in others; Lui's long-standing observation that `< >` "doesn't play nice with void" — the identity `void<void> ≐ void` is flagged as a hinge |
| JH, JO | holds | verbatim: additive, never obstructed by non-commutativity (JH Exposition Guide, Ch. 15) |
| JP | holds | the axiom audit passes at p = 2, 3, 5, 7, 13, ∞ |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | no inverses; adjoining them *is* group completion — the trunk road's reading of this axiom |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

- ~~`< >` is the uniformizer at a finite place~~ — refuted 2026-09-13: the mirror gives J at every place; the uniformizer at p = 2 is `[oo]` (p-adic-wall thread).

## Notes

Domain `complex` (widened 2026-10-03, C referee pass): rung C instantiates this law at complex content, and under the chart's citation discipline ([[mult.consistency]], Confirms) a law may be cited only inside its declared domain; the law is exact on ℂ×, as the engine confirms. The law's home band and reading are unchanged.

The two directions of this axiom (cancel / create) are the first place the chart's derivations run "backwards"; the Given–Rule tables mark which direction a step uses in the note column.
