---
id: place.torsion
title: The torsion log J_p
type: definition
level: meta
kind: declaration
rung: place
order: 1495
setting: JP
equality: "≡"
domain: natural
law: "J_p := [T], T a generating Teichmüller element: J := [<o>] ≐ ω_p/2 at every place"
units: "J_p = log of a generator of μ_{p−1}, formal (the p-adic log of a root of unity is 0); ω_p = (p−1)·J_p; J = (p−1)/2 · J_p = ω_p/2; at p = 2 the torsion of ℤ_2^× is ±1 (not a Teichmüller lift: μ_1 is trivial there), J_2 = [<o>] and ω_2 = 2·J_2"
gloss_check: ""
witness: tools/models/place_torsion.py
holds:
  classical: replaced
  J1: replaced
  JH: untested
  JO: untested
  JP: holds
readings:
  C: ABSENT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE-BY-DECREE
verified: engine
known_since: "2026-09-13 (Forms at Every Place: 'J = [<o>] ≐ ω_v/2 at every place'; 'J stops being a number — a pure phase'); the Teichmüller character, 1937"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [C.phase, J1.period-form, place.teichmuller, place.reading, place.void-pile]
see_also: [C.phase, J1.half-period, J1.period-form, place.teichmuller, place.selection, place.wall]
aliases: [J_p, the torsion log, the log of a root of unity, J = ω_v/2, the phase at a place]
concepts: [place, phase, period, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| J_p := `[T]` for T the Teichmüller generator (the instance of ω_p/(p−1)) at an odd place; the log of any root of unity at p is a whole count of J_p; `J = [<o>]` is (p−1)/2 of them — half the period — at every odd place. At 2 the torsion of the units is ±1 alone, which is no Teichmüller lift (μ_1 is trivial there): T = −1 by convention, J_2 = `[<o>]` itself and ω_2 = 2·J_2 | — | log on μ_{p−1} is 0 in ℚ_p; the reading keeps the count instead |

At ∞, J = `[<o>]` is a number, iπ. At a finite place it is not: the p-adic logarithm of −1 is 0 (2·log(−1) = log 1 = 0 and ℚ_p has no 2-torsion), and exp never reaches −1 from the radius. If the reading evaluated J it would *empty* it, and `(J)` would read `o` instead of `<o>` — the Phase value law ([[C.phase-value]]) would fail. So J survives at p only **formally**, as the count of a torsion log: the reading's third count ([[place.reading]]). The torsion log itself, J_p, is the log of the generator τ of the roots of unity at p ([[place.teichmuller]]); −1 is τ^{(p−1)/2}, so J = ω_p/2 at every place — the half-period, exactly as at ∞ ([[J1.half-period]]), and `J J ≃ ω` holds at p as it does there (the place ledger). At p = 2 the torsion is ±1 alone, J_2 = J, and ω_2 = `J J`.

## Plain

Minus one has no logarithm at a finite place — but it still needs one, or (J) would stop being −1. So the place keeps J as a count: half a turn, with the whole turn being the period of the place.

## Derivation

| statement | rule | note |
|---|---|---|
| **J_p := `[T]`**, T the generating Teichmüller element — the instance of ω_p/(p−1), fixed by the p-th power ([[place.teichmuller]]); ω_p = `[()]` is (p−1) of it ([[J1.period-form]] at the place) | [[place.teichmuller]] | the reading's third count ([[place.reading]]): a formal count, since the p-adic log of a root of unity is void — on the page the void pile declares ([[place.void-pile]]), the decree this definition rests on |
| **J = ω_p/2.** `<o>` = −1 is T^{(p−1)/2}, so `[<o>]` ([[C.phase]]) is (p−1)/2 copies of J_p: half the period, at every odd place; at 2, J_2 = `[<o>]` and ω_2 = J J | [[C.phase]] | witness: τ at p = 3, 5, 7, 13 to depth n; τ^{p−1} ≐ o, τ^{(p−1)/2} ≐ <o>; `[<o>]` reads (p−1)/2·J_p; `[τ]` reads J_p with a void number part; `(J) ≐ <o>` and `<A> ≐ ([A] J)` hold at every place |

## Confirms

The Teichmüller character and the splitting ℤ_p^× = μ_{p−1} × (1 + pℤ_p) read as the two counts of a log; that Book One's Phase rule `<A> ≐ ([A] J)` holds at every place with the place's J; that the log space at p is ℤ_p ⊕ ℤ[p] ⊕ ℤJ_p (JP ledger). It is **not** the claim that J_p is a number: the p-adic log of every root of unity is 0, and J_p is a count the reading refuses to evaluate — which is also why `([J][J])`, −π² at ∞, has no value at p (weight 2, [[place.reading]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | replaced | J = iπ, a number ([[C.phase]]) |
| J1 | replaced | J = ω/2 as a number, iπ = 2πi/2: the same statement with ∞'s period |
| JH, JO | untested | the JH seed J_j at a place; owed |
| JP | holds | witness |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | EXACT | the generator of the cyclic group μ_{p−1} |
| lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

"J ↔ −1 beside ψ ↔ 5" at p = 2 is the 'secretly 2-adic' split of the K(1) thesis (2026-09-13): ℤ_2^× = ⟨−1⟩ × ⟨5⟩, torsion and principal units — the reading's third and first counts at p = 2. The generator T at each place is the reading's convention (the least primitive root; LEGISLATION 31(h)): which root of unity is "the" generator is not a fact of the place, and only the count of J_p modulo p − 1 is.
