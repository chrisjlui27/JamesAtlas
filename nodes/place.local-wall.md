---
id: place.local-wall
title: The wall is the product of its local factors
type: theorem
level: meta
kind: law
rung: place
order: 1570
setting: JP
equality: "≡"
domain: natural
law: "M(2k) = ∏_p p^{e_p(k)}, with e_p(k) the largest e such that λ(p^e) divides 2k — the ψ-wall at level k is decided one place at a time"
units: "e_p(k) = 1 + v_p(k) for odd p with (p−1) | 2k, else 0; e_2(k) = 3 + v_2(k); the product is the denominator of B_{2k}/4k"
gloss_check: ""
witness: tools/models/place_local_wall.py
holds:
  classical: replaced
  J1: holds
  JH: untested
  JO: untested
  JP: holds
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "2026-09-15 (JP v0.4: the fixed-point count on ℤ/p^n is p^{min(v_p(R−1), n)}, locking in at n = e_p(k); ∏_p p^{e_p} = M(2k) for k = 1 … 8); von Staudt–Clausen 1840, Adams 1965"
entered: 2026-10-06
guide: need-led
band: "beyond"
uses: [J1.psi-wall, J1.wall-census, place.selection, place.teichmuller]
see_also: [J1.psi-wall, J1.wall-census, J1.von-staudt-clausen, place.selection, place.wall]
aliases: [the local wall, e_p(k), the adelic page, the product formula for the wall, M(2k) = ∏ p^{e_p}]
concepts: [place, period, induction, prime]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| the count of the ψ-wall at level k is a product over the finite places: at each p the largest power p^e whose Carmichael value λ(p^e) divides 2k, and nothing at ∞ | — | 24 = 2³·3, 240 = 2⁴·3·5, 504 = 2³·3²·7, 480 = 2⁵·3·5, 264 = 2³·3·11, 65520 = 2⁴·3²·5·7·13 |

The ψ-wall ([[J1.psi-wall]]) selects the fractions ω/n well formed at level k by one condition on the whole of n: λ(n) | 2k, with λ Carmichael's function; the census ([[J1.wall-census]]) counts 24, 240, 504. Read at the places, the condition splits: λ(n) is the least common multiple of the λ(p^e) over the prime powers in n, so n passes the wall iff each of its prime-power parts does, and the largest n that passes is the product of the largest prime powers that do. The wall is **local**: at each place p it is a number e_p(k), the depth at which the fixed points of the re-entry x ≐ ([R][x]) with R = r^{2k} lock in (JP v0.4) — and e_p(k) = 1 + v_p(k) when the torsion of the place, p − 1, divides 2k ([[place.selection]]: the (p−1)-th roots of unity are the forms at p that ψ^r can see), 0 when it does not; at 2, where the torsion is ±1 and the principal units start at 5, it is 3 + v_2(k). The product over the places is M(2k) — and nothing is contributed at ∞, which has no generator and no lock-in. This is the *adelic page* of the JP ledger: one re-entry counted on every place's clock.

## Plain

The number 24 is 8 times 3 because the wall at level 1 is 8 at the place 2 and 3 at the place 3, and nothing anywhere else. Every wall number is built this way, one prime at a time.

## Derivation

| statement | rule | note |
|---|---|---|
| **The wall splits.** λ(n) | 2k iff λ(p^e) | 2k for every p^e ∥ n, since λ(n) = lcm of the λ(p^e); so the largest n with λ(n) | 2k is the product over p of the largest p^e with λ(p^e) | 2k | [[J1.psi-wall]] | Carmichael's function is a least common multiple over the prime powers |
| **The local count.** λ(p^e) = (p−1)p^{e−1} for odd p, so λ(p^e) | 2k iff (p−1) | 2k and e − 1 ≤ v_p(k): e_p = 1 + v_p(k) when (p−1) | 2k, else 0. At 2: λ(2) = 1, λ(4) = 2, λ(2^e) = 2^{e−2} for e ≥ 3, so e_2 = 3 + v_2(k) | [[place.selection]] | the torsion at p is the (p−1)-th roots of unity ([[place.teichmuller]]); its order must divide 2k for ψ^r to fix ω/p^e |
| **The product.** ∏_p p^{e_p(k)} = M(2k) = 24, 240, 504, 480, 264, 65520, 24, 16320 for k = 1 … 8 | [[J1.wall-census]] | witness: computed locally, compared with the census |

## Confirms

Von Staudt–Clausen's theorem read locally: a prime p divides the denominator of B_{2k} iff (p−1) | 2k, with the exact power given by Adams — the e_p(k) above; the "universal 24" of the J-tower (every im-J order is divisible by 8·3, because (2−1)... the place 2 contributes 2³ at every level and the place 3 contributes 3 at every level, since 2 | 2k always). It is **not** a derivation of the labelling M(2k) = |im J|, which stays the rung's import ([[J1.von-staudt-clausen]]). It is **not** the adelic form on one page: the places are read one at a time.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | replaced | the classical calculus has no wall |
| J1 | holds | the wall at ∞ is the whole product, seen as one condition on n |
| JH, JO | untested | — |
| JP | holds | witness |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset, lambda, CC, logic | untested | the λ-ring reading should see e_p as the order of ψ^p's fixed points; owed |

## Refuted readings

none

## Notes

The JP ledger's trace-formula test (Lui's spec of 2026-09-14: sum v(1 − F′) over guarded re-entries, "discard if not") held with its aggregation corrected — the wall is the *minimum* over generators, the count of common fixed points, not a sum. What remains open there is ∞'s share: the realized weights 2k.
