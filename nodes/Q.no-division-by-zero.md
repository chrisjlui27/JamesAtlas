---
id: Q.no-division-by-zero
title: There is no form for dividing by zero
type: theorem
level: meta
kind: law
rung: Q
order: 650
setting: classical
equality: ≐
domain: positive
law: "([A] <[void]>) is not a form"
units: a ÷ 0 is undefined
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
  logic: ABSENT
status: NATIVE-BY-DECREE
verified: hand
known_since: 1993 (James)
entered: 2026-10-03
guide: need-led
band: 3–5
uses: [Q.division, mult.black-hole, mult.hole-exclusion]
see_also: [Q.zero-divided, Q.reciprocal]
aliases: [division by zero, a/0]
concepts: [zero, division, infinity]
understood: "yes"
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A] <[void]>)` | — | a ÷ 0 — not admissible |

## Plain

You cannot divide by zero, and the page shows why: the shape you would have to draw contains the one mark the calculus refuses.

## Derivation

| statement | rule | note |
|---|---|---|
| `([A] <[void]>)` is the shape of A ÷ 0 | [[Q.division]] | — |
| its subform `<[void]>` is `<□>`, the mirror of the black hole | [[mult.black-hole]] | — |
| `<□>` is excluded, up to ≐, so the shape is not an admissible form and no derivation may contain it | [[mult.hole-exclusion]] | the decree, not a theorem of the axioms |

## Confirms

That "undefined" is the right word, not "infinite": the calculus does not assign a/0 a value it then refuses to use; it has no inscription for it at all. The same decree bans inverting a singular matrix in JH (JH-20) and is what keeps the calculus from collapsing ([[mult.consistency]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | holds | the exclusion is kept in every extension |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Status NATIVE-BY-DECREE because the law is a consequence of a decree; verification `hand` because a meta statement has no witness script — the engine's `Excluded` exception on evaluation is the mechanized version, but it is not stated as a rule the checker reports on.
