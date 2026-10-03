---
id: Z.cancellation
title: Inverse cancellation
type: theorem
level: object
kind: law
rung: Z
order: 250
setting: classical
equality: "≐"
domain: real
law: "<<A>> ≐ A"
units: "−(−a) = a"
gloss_check: "A"
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
  logic: ANALOGY
status: NATIVE
verified: engine
known_since: "1993 (James)"
entered: 2026-10-03
guide: shape-led
band: "6–8"
uses: [Z.inversion, void.page, void.space]
see_also: [Z.collection, mult.product-of-negatives]
aliases: [double negation, inverse cancellation, "<<A>> = A", "involution (Bricken's name)"]
concepts: [negation]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `<<A>> ≐ A` | — | −(−a) = a |

## Plain

The opposite of the opposite is the thing itself.

## Derivation

| form | rule | note |
|---|---|---|
| `<<A>>` | given | — |
| `<<A>> void` | [[void.page]] | — |
| `<<A>> A <A>` | [[Z.inversion]] | create the pair `A <A>` from the void |
| `A <A> <<A>>` | medium | regroup in space, [[void.space]] |
| `A` | [[Z.inversion]] | cancel `<A> <<A>>` — the pair `X <X>` with X = `<A>` |

## Confirms

−(−a) = a, derived rather than stipulated: the angle boundary is an *involution* because inverses in a group are unique. In JH the same single theorem makes every Q₈ relation a theorem (Ch. 10: "every Q₈ relation is now a theorem of a single classical axiom, `<<A>> ≐ A`") — the quaternion group's sign bookkeeping is this node, applied slotwise.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | survival ledger: inverse collection/cancellation/promotion unchanged |
| JH, JO | holds | verbatim; load-bearing for Q₈ and the braid relations (JH-6, JH-7) |
| JP | holds | — |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ANALOGY | LoF's Reflexion, `((a)) = a`, has the same shape on a different boundary; the chart keeps them apart |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Band 6–8 because the curriculum teaches "negative of a negative" with integer multiplication; the law itself needs only grade-1 forms.
