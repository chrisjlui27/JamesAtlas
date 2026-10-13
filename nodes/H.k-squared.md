---
id: H.k-squared
title: k squared
type: theorem
level: object
kind: law
rung: H
order: 1695
setting: JH
equality: "≃"
domain: complex
law: "([k ; k]) ≃ <o>"
units: "k·k = (ij)(ij) = i(ji)j = −(ii)(jj) = −1: the central sign twice and splice, with no J-cancellation at all"
gloss_check: ""
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: holds
  JP: holds
readings:
  C: ABSENT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "2026-08 (JH report §4: 'the k² derivation was rebuilt in the repair round to use the central-sign rule twice and no J-cancellation at all — avoiding James's most dangerous rule entirely'); Hamilton 1843"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.central-sign, H.i-squared, H.j-squared, H.ji, H.k, H.splice, H.unit-entry, J1.counit, Z.cancellation]
see_also: [H.k, H.ji, H.central-sign, H.i-squared, H.j-squared, C.james-discipline]
aliases: [k² = −1, "([k ; k]) = <o>", the k² derivation, JH-11]
concepts: [quaternion, ordered-product, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([k ; k]) ≃ <o>` | k times k is minus one | k² = −1 |

The JH report's showpiece: k·k = (ij)(ij) is rewritten as i(ji)j, the inner ji is −k = −(ij) ([[H.ji]]), the sign comes out by [[H.central-sign]], the remaining i·i·j·j is gathered by [[H.splice]] into (ii)(jj), and the two squares are −1 and −1 ([[H.i-squared]], [[H.j-squared]]) whose product, with the sign already outside, is minus one. James's J-cancellation — the crack of the trunk ([[C.james-discipline]]) — is never used: every step of the derivation's own is strict in ℍ, and the two squares it cites are absorbed theorems whose grade the node inherits — absorbed, with k = 0 on the tape: their receipts were paid inside their own instances, and their reuse here moves no period. So the law is ≃, as the squares are, and holds.

## Plain

k times k: write k as ij twice, swap the middle pair at the cost of a sign, and what is left is i times i times j times j, which is (−1)(−1) = 1 — with the sign out front, −1.

## Derivation

| form | rule | note |
|---|---|---|
| `([k ; k])` | given | k beside itself |
| `([([i ; j]) ; ([i ; j])])` | definition | k unfolded twice ([[H.k]]) |
| `([i ; j ; i ; j])` | [[H.splice]] | both products spliced open (twice) |
| `([i ; ([j ; i]) ; j])` | [[H.splice]] | the middle pair gathered, right to left |
| `([i ; <k> ; j])` | [[H.ji]] | ji is −k |
| `<([i ; k ; j])>` | [[H.central-sign]] | the sign comes out — once |
| `<([i ; ([i ; j]) ; j])>` | definition | k unfolded ([[H.k]]) |
| `<([i ; i ; j ; j])>` | [[H.splice]] | spliced open |
| `<([([i ; i]) ; ([j ; j])])>` | [[H.splice]] | the two squares gathered, right to left (twice) |
| `<([<o> ; <o>])>` | [[H.i-squared]] [[H.j-squared]] | i² and j² are minus one |
| `<<<([o ; o])>>>` | [[H.central-sign]] | the two signs come out — twice |
| `<([o ; o])>` | [[Z.cancellation]] | two of the three mirrors cancel |
| `<([o])>` | [[H.unit-entry]] | one times one |
| `<o>` | [[J1.counit]] | the instance of the log of one is one |

## Confirms

k² = −1, and with it ijk = −1: Hamilton's full relation. It is **not** a use of `J J ≐ void`: the derivation never writes two J's side by side, which is the report's point.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | no k |
| JH | holds | every step of its own strict; the squares it cites ([[H.i-squared]] and [[H.j-squared]]) are absorbed theorems, and the node inherits that grade — absorbed, k = 0: the receipts were paid inside their own instances |
| JO | holds | the derivation splices three units, i, j and ij, which generate an associative subalgebra of the octonions (a quaternion subalgebra); splice is valid there |
| JP | holds | at every place |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

~~"k² needs J-cancellation"~~ — the first JH proposal's route; refuted by the repair round (central sign twice).

## Notes

Rows 3 and 9 are two applications each of the one rule, as the derivation checker allows ("Distribution n − 1 times" on the trunk).
