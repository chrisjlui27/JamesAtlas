---
id: place.residue
title: Piles that agree mod p^n are one pile
type: schema
level: object
kind: law
rung: place
order: 1410
setting: JP
equality: "≃"
domain: natural
law: "o^{p**n + k} ≃ o^{k}"
units: "m ≡ k (mod p^n) ⟹ the piles are equal at depth n: a pile is its residue"
gloss_check: ""
schema_range: "p=2,3,5; n=1..2; k=1..3"
schema_draw: "p=3; n=1; k=2"
holds:
  classical: fails
  J1: fails
  JH: holds
  JO: untested
  JP: holds
readings:
  C: ABSENT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE-BY-SCHEMA
verified: engine
known_since: "2026-09-13 (Forms at Every Place: at depth N the number p^{N−1}… the observation wall); as residue classes, Gauss 1801"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [place.void-pile, void.space, place.ostrowski]
see_also: [N.freeness, Z.normal-form, place.void-pile, place.negation-is-a-pile]
aliases: [residues, a pile is its residue, freeness fails at p, mod p^n]
concepts: [place, zero, induction]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `o^{p**n + k} ≃ o^{k}` | a pile of p^n + k marks is a pile of k marks at depth n: the void pile is subtracted | m ≡ k mod p^n |

What [[N.freeness]] forbids at ∞ — two different piles equal — is the first theorem at a finite place: a pile is its residue. The derivation is two steps, and the second is the void pile, at depth 0: a **page step** (the page's equality, ≃ — it does not pass through a square: `[o^{p**n + k}]` and `[o^{k}]` differ when k is not a unit, by as many shells as p divides k, and at p = 2, depth 1 even for a unit k — `[ooo]` is J₂ where `[o]` is the period, the torsion invisible mod 2 and visible in the log; [[place.void-pile]]).

## Plain

On a clock with p^n hours, p^n + k o'clock is k o'clock.

## Derivation

| form | rule | note |
|---|---|---|
| `o^{p**n + k}` | given | p^n + k marks; at every place ([[place.ostrowski]]) |
| `o^{p**n} o^{k}` | medium | the pile regrouped: p^n marks beside k marks — the same form, [[void.space]] |
| `o^{k}` | [[place.void-pile]] | the p^n marks are void at depth n: a page step at depth 0 |

## Confirms

The residue classes mod p^n, and that the chart's piles wrap: the normal form of [[Z.normal-form]] becomes a residue at a finite place (its JP cell). It is **not** a statement about which residue a pile *is*: that is the doll, [[place.doll]], the base-p digits.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | fails | [[N.freeness]]: at ∞ distinct piles are distinct |
| J1 | fails | as classical |
| JO | untested | owed to rung `H` |
| JH | holds | on the quaternion page: at 2 the residue field is 𝔽₄ and at odd p the matrices mod p ([[H.ramified-place]], [[H.split-place]]); exact on the centre and on generic quaternions of the page (census/h-place-ledger.md) |
| JP | holds | a page step at depth 0 at every instance (p = 2, 3, 5; depths 1, 2; k = 1 … 3): the page's equality, ≃ |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | EXACT | a set of p^n elements with addition wrapping |
| lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The regrouping row is the identity row of [[void.space]]: a pile of p^n + k marks *is* the juxtaposition of p^n marks and k marks. The one step of content is the void pile.
