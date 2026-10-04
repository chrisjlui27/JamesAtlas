---
id: C.phase-unique
title: J is the only survivor among the forms that use each boundary once
type: theorem
level: meta
kind: law
rung: C
order: 905
setting: classical
equality: "≐"
domain: positive
law: "of the sixteen forms that use each of the three boundaries exactly once, eight are void, four are the black hole, three are excluded, and only [<()>] is a new form"
units: "the six nestings: ([<>]) = 0, [(<>)] = 0, <([])> = 0, <[()]> = 0, (<[]>) excluded, [<()>] = iπ; the ten juxtaposed shapes are void, □ or excluded"
witness: tools/models/phase_unique.py
holds:
  classical: holds
  J1: fails
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James, Ch. 6 §6.2, p. 44: J 'uses all three boundaries exactly once. All other legal configurations of three different boundaries reduce to void'; the sixth, (<[]>), undefined)"
entered: 2026-10-03
guide: shape-led
band: beyond
uses: [C.phase, Z.void-inverse, mult.hole-instance, mult.unit-law, mult.hole-exclusion, mult.dominion, mult.consistency]
see_also: [C.phase]
aliases: [uniqueness of J, the six nestings]
concepts: [phase, census]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[<()>]` alone survives among the sixteen one-of-each-boundary forms — the six nestings `([<>])`, `[(<>)]`, `<([])>`, `<[()]>`, `(<[]>)`, `[<()>]` and the ten shapes with juxtaposition | — | J is found, not imposed |

## Plain

Use each kind of boundary once: there are sixteen ways to arrange them. Fifteen fall into nothing, into the bottomless pit, or are forbidden; one stands, and it is the log of minus one.

## Derivation

| statement | rule | note |
|---|---|---|
| `([<>])`: the mirror of nothing is nothing, so this is `([])`, the instance of the hole, which is void | [[Z.void-inverse]] [[mult.hole-instance]] | — |
| `[(<>)]`: `(<>)` is `()`, whose abstract is void | [[Z.void-inverse]] [[mult.unit-law]] | — |
| `<([])>`: the mirror of `([]) ≐ void` is void | [[mult.hole-instance]] [[Z.void-inverse]] | — |
| `<[()]>`: the mirror of `[o] ≐ void` is void | [[mult.unit-law]] [[Z.void-inverse]] | — |
| `(<[]>)` contains `<□>` and is excluded | [[mult.hole-exclusion]] | — |
| the ten shapes with juxtaposition: two (`() <[]>`, `<() []>`) contain `<□>` and are excluded; four (`() [] <>`, `() [<>]`, `(<>) []`, `<()> []`) are the black hole, each a unit or a nothing beside the hole; four (`(<> [])`, `([]) <>`, `<> [()]`, `[() <>]`) are void | [[mult.hole-exclusion]] [[mult.dominion]] [[mult.hole-instance]] [[mult.unit-law]] [[Z.void-inverse]] | `□ A ≐ □` swallows the unit; `(□) ≐ void` and `[o] ≐ void` empty the rest |
| `[<()>]` is J, value iπ, reducible to nothing by any admissible derivation | [[C.phase]] [[mult.consistency]] | a sound reading sends it to iπ ≠ 0, so no admissible derivation empties it; the witness `tools/models/phase_unique.py` enumerates all sixteen |

## Confirms

James's observation that J is *found* by the calculus rather than posited — his "unique stable configuration that uses each of the three boundaries exactly once" — the syntactic fact that motivates the whole phase story. It is **not** a proof that J is irreducible in the sense of a normal form on its own: that it cannot be emptied is borrowed from the consistency theorem ([[mult.consistency]]), and this node is the census of one shape.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | fails | in J1 `[()]` is ω, not void ([[mult.unit-law]]), and `<> ≐ void` is only guarded ([[Z.void-inverse]]): the nestings that reduce through `[()]` — `[(<>)]`, `<[()]>`, `<> [()]` — are ±ω there, so J = ω/2 is one of several survivors; the census of this shape is different in the enriched calculus, which is the group/torsor split in miniature |
| JH, JO | holds | the hole rules, the unit law and `<> ≐ void` survive verbatim (JH rule cards), and the seam guard admits the unit at void content |
| JP | holds | the unit law and the hole rules hold at every tested place |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| logic | ABSENT | — |
| others | untested | — |

## Refuted readings

none

## Notes

—
