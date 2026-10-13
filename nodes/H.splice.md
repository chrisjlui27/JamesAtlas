---
id: H.splice
title: Splice
type: axiom
level: object
kind: law
rung: H
order: 1615
setting: JH
equality: "≐"
domain: complex
law: "[A ; ([B ; C])] ≐ [A ; B ; C]"
units: "log(A·(B·C)) = log(A·B·C): associativity of the product, as list concatenation; at any position, for lists of any length"
gloss_check: ""
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: fails
  JP: guarded
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "2026-08 (JH report, Layer 3: splice/unit-deletion as associativity)"
entered: 2026-10-07
guide: shape-led
band: "beyond"
uses: [H.ordered-bracket, H.ordered-product]
see_also: [H.ordered-bracket, H.unit-entry, H.list-distribution, H.octonion-gap]
aliases: [splice, list associativity, flattening, "[x ; (y·z)] = [x ; y ; z]"]
concepts: [ordered-product, multiplication]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[A ; ([B ; C])] ≐ [A ; B ; C]` | an entry that is an ordered product is spliced into the list | log(A(BC)) = log(ABC) — associativity |

An entry of an ordered square that is itself the instance of an ordered square is *spliced* in: `[A ; ([B ; C])]` is `[A ; B ; C]`. Read in ℍ, the entry `([B ; C])` is the product B·C ([[H.ordered-product]]), and log(A·(B·C)) = log(A·B·C) because the product is associative. The law is a family over the position of the spliced entry and the lengths of the lists (SPEC §4.5): the engine instantiates it for lists of up to five entries. A one-entry splice — `[([B ; C])] ≐ [B ; C]` — is not in the family: it is the unit `[(X)] ≃ X` of [[J1.unit]], with its receipt.

## Plain

"a times (b times c)" is "a times b times c": the parentheses inside the ordered box can be dropped. That is associativity, which the quaternions keep and the octonions lose.

## Derivation

none — adjoined, as a rule of the ordered square ([[H.ordered-bracket]]) about its instances ([[H.ordered-product]]). Checked in ℍ at every instantiation.

## Confirms

Associativity of the Hamilton product, as a syntactic law: concatenation of lists. It is **not** valid one rung on: the octonions are not associative, splice fails there, and the JO setting needs tree-shaped nesting ([[H.octonion-gap]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | the square has one entry; the content is `[A] [B] [C]` and associativity is the medium's |
| JH | holds | an axiom of the setting |
| JO | fails | the octonions are not associative: `[a ; (b·c)]` and `[(a·b) ; c]` differ (JH OP-3) |
| JP | guarded | the product on the page is associative at every place, and the law is exact wherever its ordered squares have a value; formless where the page's log is owed ([[H.ordered-bracket]]; census/h-place-ledger.md) |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The family (`tools/licences.py`, `_family_splice`): outer lists of 2 … 4 entries, spliced lists of 2 or 3, every position. The JH report's notation `[x⃗ ; (y⃗) ; z⃗]` is the family written with vector entries.
