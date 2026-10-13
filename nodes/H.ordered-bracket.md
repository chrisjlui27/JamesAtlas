---
id: H.ordered-bracket
title: The ordered square
type: primitive
level: object
kind: boundary
rung: H
order: 1605
setting: JH
equality: "≐"
domain: complex
law: "[A ; B] is a form"
units: "log(A·B): the log of the ORDERED product; [x₁ ; … ; xₙ] with n ≥ 1 entries, [x] the ordinary square; [A ; B] and [B ; A] are different forms"
gloss_check: ""
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: holds
  JP: guarded
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "2026-08 (the JH-Calculus report, Layer 3: 'one new constructor: the ordered list [x₁ ; … ; xₙ], interpreted as the log of the ordered Hamilton product'); Book One, rung four"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [N.round, mult.square, void.space]
see_also: [mult.square, mult.multiplication, H.ordered-product, H.splice, H.unit-entry, H.list-distribution, H.collapse, H.no-go]
aliases: [the ordered bracket, the semicolon, "[x ; y]", ordered abstraction, Layer 3, the ordered list, ordered depth]
concepts: [quaternion, ordered-product, multiplication]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[A ; B]` is a form | the log of the ordered product A·B; with one entry, `[A]`, the square of rung `mult` | log(AB), for AB the Hamilton product |

The fourth boundary of the chart. The square `[A]` ([[mult.square]]) holds one multiset; the **ordered square** holds a *sequence* of them, separated by semicolons, and reads as the log of their ordered product. One entry is the ordinary square — `[A]` is `[A]` — so nothing is lost; two entries are what the classical calculus cannot write, the product in one order rather than the other: `[A ; B]` and `[B ; A]` are different forms, as `[A][B]` and `[B][A]` are not ([[H.no-go]]). The instance `([A ; B])` ([[N.round]]) is then the product A·B itself ([[H.ordered-product]]). What the ordered square costs, the rung's bill, is the bookkeeping that makes it the log of a product: splice ([[H.splice]]), the unit entry ([[H.unit-entry]]), two-sided distribution ([[H.list-distribution]]), the exchange of commuting entries ([[H.commutation]]) and the collapse of co-sliced ones to the old square ([[H.collapse]]); the medium ([[void.space]]) is unchanged — inside each entry juxtaposition is as unordered as ever. The order is *imported*, not found as J was found (JH OP-5: no tagging trick within the three boundaries can produce it); that is the rung's honest price, and [[H.octonion-gap]] records where the question goes next.

## Plain

A box whose contents are written in a row with semicolons between: "first this, then that". The old box didn't care about order; this one does, and that is exactly what multiplying quaternions needs.

## Derivation

none — adjoined: a new boundary, with [[mult.square]] its one-entry case, its instance by [[N.round]], and the medium [[void.space]] inside every entry. The engine parses it (`tools/forms.py`: `;` inside a square), rewrites inside its entries (`tools/prover.py`), reads it in ℍ (`tools/quat.py`) and at the places (`tools/quatplace.py`).

## Confirms

The log of a product in a non-commutative algebra — log(AB) — kept as a form of its own because it is no longer log A + log B. It is **not** a new kind of number: its instance is a quaternion like any other; and **not** the lens of [[place.completion]], though the 2026-09-19 note suggested one notation might serve both — that question is left open (LEGISLATION 32(b)).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | the classical square: one entry; `[A ; B]` reads as `[A][B]` there (ℂ commutes), [[H.collapse]] |
| JH | holds | the primitive of the setting |
| JO | holds | the octonions keep the ordered square and lose splice ([[H.octonion-gap]]) |
| JP | guarded | read at every place by `tools/quatplace.py` as the log of the ordered product of the page, where that log exists: the reading's log reaches the units of the page whose torsion and principal parts commute, and at odd p those whose reduction has order prime to p — on the rest the law is formless (owed, [[H.split-place]] and [[H.ramified-place]], Notes) (census/h-place-ledger.md) |

| reading | cell | why |
|---|---|---|
| C | EXACT | log(xy), which in ℂ is log x + log y mod Λ |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

~~"a tag on the square can carry the order: `[A]ₗ [B]ᵣ`"~~ — refuted in the JH audit (OP-5): depth tags collapse under Involution and decorated atoms die by unordered space; the order must be a constructor.

## Notes

The semicolon in canonical strings: `[A ; B ; C]`; whitespace is ignored; an empty entry is the void (whose product is 0: [[H.zero-entry]]). Cards draw the ordered square as a rectangle with dashed dividers.
