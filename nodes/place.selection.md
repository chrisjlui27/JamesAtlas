---
id: place.selection
title: Which fractions of the period are forms at p
type: theorem
level: meta
kind: law
rung: place
order: 1500
setting: JP
equality: "≡"
domain: natural
law: "(([ω] <[o^{n}]>)) is a form at the place p iff n divides p − 1 (n divides 2 at p = 2); so i is a form at p iff p ≡ 1 mod 4 and ζ₃ iff p ≡ 1 mod 3"
units: "μ_n ⊂ ℚ_p ⟺ n | p − 1 (n | 2 at p = 2): the roots of unity of a local field are the Teichmüller torsion"
gloss_check: ""
witness: tools/models/place_selection.py
holds:
  classical: replaced
  J1: replaced
  JH: replaced
  JO: untested
  JP: holds
readings:
  C: ABSENT
  finset: EXACT
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "2026-09-13 (Forms at Every Place, EXACT: 'i is a form at p iff p ≡ 1 mod 4; at p = 5 it is τ(2), digits …31212; ζ iff p ≡ 1 mod 3 — via Cardinality with fractional counts'); Hensel 1908"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [J1.receptacle, place.teichmuller, place.reading]
see_also: [J1.receptacle, C.imaginary-unit, C.cube-root-of-unity, J1.psi-wall, place.teichmuller, place.local-wall]
aliases: [the selection rule, ω/n at p, i at p ≡ 1 mod 4, ζ₃ at p ≡ 1 mod 3, roots of unity at p, d | p − 1]
concepts: [place, root, period, prime]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| `(([ω] <[o^{n}]>))`, the instance of ω/n, is a form at p exactly when n divides p − 1 (n divides 2 at p = 2) | the fractional count of J_p must be whole | μ_n ⊂ ℤ_p^× ⟺ n | p − 1 |

At ∞ every fraction of the period is a form: `(([ω] <[o^{n}]>))` is e^{2πi/n}, and [[J1.receptacle]] says its n-th power is one for every n. At a finite place the period is (p−1)·J_p ([[place.torsion]]), so ω/n is a whole count of J_p — a form — exactly when n divides p − 1, and otherwise it is a fraction of the torsion log that nothing on the page instances. This is the **selection rule** of the place: it chooses, among the receptacle's roots of unity, the ones that exist there. Two instances the chart already has: i = `(([J] <[oo]>))` (half of J, [[C.imaginary-unit]]) is ω/4, a form iff 4 | p − 1; the cube root of unity ([[C.cube-root-of-unity]]) is ω/3, a form iff 3 | p − 1. At p = 5, i is the Teichmüller lift of 2, the doll …31212₅; at p = 3 and 7 there is no i; at p = 7 there is a ζ₃. The ψ-wall ([[J1.psi-wall]]) is this rule read at every place at once ([[place.local-wall]]).

## Plain

A root of unity exists at the place p only if its order divides p − 1. So i lives at 5, 13, 17, …; a cube root of one at 7, 13, 19, …; at 2 and 3 nothing but ±1.

## Derivation

| statement | rule | note |
|---|---|---|
| ω_p/n is the count (p−1)/n of J_p ([[place.teichmuller]]: the torsion log is ω_p/(p−1)); a fractional count of a torsion log is not a form — the reading's selection ([[place.reading]]) — so the fraction is a form iff n divides p − 1 (n | 2 at 2, where the torsion is ±1) | [[place.reading]] | — |
| where it is a form, [[J1.receptacle]] applies at the place: its n-th power is one; so the n-th roots of unity exist at p exactly for n dividing p − 1 | [[J1.receptacle]] | witness: p ≤ 31, n ≤ 12 — the form has a value exactly when n divides p − 1 (2 at 2), its n-th power is then one, and i and ζ₃ appear at exactly the residues 1 mod 4 and 1 mod 3 |

## Confirms

The roots of unity in ℚ_p, and that ℚ_p(i) is a quadratic extension for p ≡ 3 mod 4 — an extension the chart's page does not draw. It is **not** a limitation of the reading's generator: any generator of the torsion gives the same selection. It is **not** the whole story of roots at p: a root of a number that is not one (√2 at 7) is the lift theorem's ([[place.lift]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | replaced | at ∞ every ω/n is a form ([[J1.receptacle]] in the ℂ reading) |
| J1 | replaced | as classical: the receptacle is ℚ/ℤ at ∞, and (ℤ/(p−1)) at p |
| JO | untested | owed |
| JH | replaced | at 2 the roots of unity of the quaternion page are the 24 of [[H.hurwitz-units]] — orders 1, 2, 3, 4, 6 — where the centre selects only ±1; at odd p the centre's selection is as stated and the page selects more |
| JP | holds | witness |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | EXACT | the cyclic group of order p − 1 has a subgroup of order n iff n | p − 1 |
| lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

Rung `Q`'s and `C`'s earlier JP guards said "when n is a unit at p": too weak — 3 is a unit at 5 and ω/3 is still not a form there. Those cells now cite this rule (2026-10-06): a fraction of the period is a form at p iff its denominator divides p − 1.
