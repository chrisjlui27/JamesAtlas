---
id: place.wall
title: The same wall at every place
type: theorem
level: meta
kind: law
rung: place
order: 1520
setting: JP
equality: "≃"
domain: complex
law: "(ω A) ≃ (A) with ω := [()] at every place v, ω_v the period of v: 2πi at ∞, (p−1)·J_p at an odd p, 2·J_2 at 2 — the same law, the same shape, the same tape"
units: "e^{ω_v} = 1 at every v; the wall absorbs the period of the place; J J ≃ ω_v and (ω_v) ≡ () at every v"
gloss_check: ""
witness: tools/models/place_wall.py
holds:
  classical: replaced
  J1: holds
  JH: guarded
  JO: untested
  JP: holds
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: EXACT
status: NATIVE
verified: engine
known_since: "2026-09-13 (Forms at Every Place: 'the wall (ωA) ≐ (A) has the SAME shape at every place; the place sets three data'); Part II Ch. 9 (Place: Axiom 4, Wall)"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [J1.period-form, J1.absorption, J1.half-period, J1.classical-floor, place.reading, place.torsion, place.radius, place.selection]
see_also: [J1.absorption, J1.closure, J1.half-period, J1.classical-floor, place.torsion, place.local-wall]
aliases: [the same wall at every place, Axiom 4 (Wall), ω_v, the period of the place, the wall parameterized by a place]
concepts: [place, period, receipt]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| the wall `(ω A) ≃ (A)` holds at every place, with ω = `[()]` reading the place's own period; its derivation is the same one absorbed step at every place, and the trunk's tapes keep their grades there | — | the kernel of exp is 2πiℤ at ∞ and (p−1)J_pℤ at p: one law, parameterized |

This is the theorem the rung exists to state. The enriched calculus 𝕁₁ was built at ∞: the log of one kept as the period form ω ([[J1.period-form]]), the instance absorbing it ([[J1.absorption]]), the half-period `J J ≃ ω` ([[J1.half-period]]). Read at a finite place — the log of exactly one reading the period of the place ([[place.reading]]), the torsion log J_p for J ([[place.torsion]]) — *none of it changes*: `[()]` is ω_p, `(ω_p) ≡ ()` is the counit at one, `(ω_p A) ≃ (A)` is one absorbed receipt, `J J ≃ ω_p` posts the same receipt, and the receipt prover re-grades every J1 derivation (the twelve of the rung's twenty-one nodes that have one) at p = 2, 3, 5, 7, 13 and finds the grade it earned at ∞ (`census/place-ledger.md`; the witness compares the two ledgers). The place sets three data — which fractions of the period are forms ([[place.selection]]), the irreducible `[p]` ([[place.prime-log]]), the radius of the instance ([[place.radius]]) — and the three are one datum, the void pile ([[place.void-pile]]). The wall is not among them. It is the same wall.

## Plain

The rule that a whole turn disappears inside a circle is not a fact about the complex numbers. It is a fact about circles and boxes, and it holds at every prime with that prime's own whole turn.

## Derivation

| statement | rule | note |
|---|---|---|
| **The period at v.** `[()]` reads the generator of the kernel of the instance at v: 2πi at ∞, (p−1)·J_p at odd p, 2·J_2 at 2 — the reading's one convention ([[place.reading]], LEGISLATION 30b at every place) | [[J1.period-form]] | witness part (1): `(ω) ≡ ()` and ω ≠ void at every tested place |
| **The wall.** `(ω A) ≃ (A)`: the derivation of [[J1.absorption]] — the unit at void content, directly inside the instance, absorbed — licenses at every place; the receipt is ω_v | [[J1.absorption]] | witness part (2): `(ω A) ≃ (A)` for random A on the radius at every tested place; the place ledger: J1.absorption `holds` at p = 2, 3, 5, 7, 13 with an absorbed tape |
| **The half-period.** `J J ≃ ω_v`: J = ω_v/2 ([[place.torsion]]), so `J J` and ω_v are the same element of the log space at every place; the derivation of [[J1.half-period]] posts there what it posts at ∞ | [[J1.half-period]] | witness part (3); the place ledger: holds-mod-Λ at every p |
| **The trunk.** Every derivation the receipt prover grades at ∞ is re-graded at each place with the place's receipts (`census/place-ledger.md`): the tapes are the same by position — strict stays strict, absorbed absorbed, posted posted (`alg.log-law`, `alg.log-of-power` post at depth 0 at p exactly as at ∞, and hold mod Λ_p for the same reason); what the places change is content, not position — the laws of the base e are replaced ([[place.radius]]), the roots selected ([[place.selection]]), and the few under-square imports whose content is formless at p (the base e, a root the place refuses) become absent there | [[J1.classical-floor]] | witness part (4): each J1 derivation's cell at every place equals its cell at ∞, read from the two ledgers |

## Confirms

Chapter 9 of the JP ledger, Axiom 4 (Wall), and the 2026-09-13 finding that "the wall has the same shape at every place": *verified here by the same prover running at the places*. The two closures of Chapter 9 — the void pile on the page, the period inside the instance — sit on opposite sides of Involution: one is declared on the additive layer at depth 0, the other is absorbed at depth 1. It is **not** the adelic page: one engine runs at one place at a time; the product formula that binds the places is [[place.local-wall]]'s, for the ψ-wall, and the full adelic form is owed (ROADMAP: `J2`).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | replaced | the classical calculus has no wall: it erases the period ([[mult.log-of-one]]) and the crack follows |
| J1 | holds | the wall at ∞ is [[J1.absorption]] |
| JO | untested | the Hurwitz wall at a place: owed to rung `H` |
| JH | guarded | the same tape per slice: at the places the torsion logs carry a direction too, and a receipt is paid only by an instance whose content lies in its slice ([[H.slice-wall]]) |
| JP | holds | witness, and the place ledger |

| reading | cell | why |
|---|---|---|
| C | EXACT | at ∞ |
| logic | EXACT | the measured unit of the ¬¬-monad is the same monad at every place (𝕁 v3.1) |
| finset | untested | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The witness reads the J1 rung's three laws at p = 2 … 31 and reports each place's period; the ledger does the rest. What differs between the places is written down one node at a time on this rung — and it is all *downstream* of the void pile.
