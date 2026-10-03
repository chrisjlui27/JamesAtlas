---
id: Z.collection
title: Inverse collection
type: theorem
level: object
kind: law
rung: Z
order: 260
setting: classical
equality: "≐"
domain: real
law: "<A> <B> ≐ <A B>"
units: "(−a) + (−b) = −(a + b)"
gloss_check: "-(A + B)"
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
status: NATIVE
verified: engine
known_since: "1993 (James)"
entered: 2026-10-03
guide: shape-led
band: "1–2"
uses: [Z.inversion, void.page, void.space]
see_also: [Z.cancellation, Z.negative-numeral, mult.inverse-promotion]
aliases: [inverse collection, negation of a sum]
concepts: [negation, addition]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `<A> <B> ≐ <A B>` | — | (−a) + (−b) = −(a + b) |

Mirrors collect: two mirrored piles may be gathered into one mirror around both piles, and one mirror around a pile may be split.

## Plain

Minus two and minus three together make minus five — you may put the two mirrors together into one.

## Derivation

| form | rule | note |
|---|---|---|
| `<A> <B>` | given | — |
| `<A> <B> void` | [[void.page]] | — |
| `<A> <B> A B <A B>` | [[Z.inversion]] | create the pair `(A B) <A B>` — the pile `A B` and its mirror |
| `A <A> B <B> <A B>` | medium | regroup, [[void.space]] |
| `<A B>` | [[Z.inversion]] | cancel `A <A>` and `B <B>` |

## Confirms

−(a + b) = −a − b: the angle boundary is a *homomorphism* of the additive layer. In JH this exact law is what makes the braid action additive (JH-7: "additivity *is* inverse collection"). It is **not** inverse promotion — the interaction of mirrors with multiplication — which needs the square boundary ([[mult.inverse-promotion]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | holds | the Inversion cluster survives in every setting |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

With this law, [[Z.negative-numeral]]'s two spellings of −3 — `<ooo>` and `<o><o><o>` — are equivalent.
