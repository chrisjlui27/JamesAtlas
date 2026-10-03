---
id: alg.non-radical
title: Algebraic numbers that radicals cannot reach
type: gap
level: meta
kind: concept
rung: alg
order: 830
setting: classical
equality: ≐
domain: positive
law: "GAP — no radical form reaches the real root of x⁵ − x − 1 (Abel–Ruffini); whether any form at all does is open: the forms' values are Chow's exp–log numbers, and 'no non-radical algebraic number is an exp–log number' is Chow's conjecture, a theorem only under Schanuel's conjecture (Chow 1999)"
units: "not every algebraic number is a radical expression; whether one can be an exp–log number is open"
holds:
  classical: fails
  J1: fails
  JH: fails
  JO: fails
  JP: fails
readings:
  C: ABSENT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: ABSENT
verified: hand
known_since: "Ruffini 1799, Abel 1824, Galois 1831 (published 1846) for radicals; Chow 1999 for exp–log numbers and the conjecture (Lin 1983 for the related Liouvillian result); for the chart, the exp–log thread 2026-10-01 (Lehmer's number is not a radical); the gap named 2026-10-03 and corrected the same day by the alg referee pass"
entered: 2026-10-03
guide: need-led
band: beyond
uses: []
see_also: [alg.nth-root, Q.lowest-terms, alg.irrationality]
aliases: [Abel–Ruffini, unsolvable quintic, non-radical algebraic, "Lehmer's number"]
concepts: [root, gap]
understood: partial
understood_note: 
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| none | — | the real root 1.1673… of x⁵ − x − 1 (Galois group S₅) is algebraic and not expressible by radicals; whether it is an exp–log number is open |

The values of the forms are exactly the closure of 0 under +, −, exp and the principal log — Chow's field **E** of *exp–log numbers* (`(([[oo]] [[oo]]))` = e^{(ln 2)²} is one; the radical towers are a small part). Every radical is a form, by one mechanism (fractional counts). By Abel–Ruffini most roots of quintics are not radicals; whether such a root can nevertheless be an exp–log number — reached by some form that is not a radical tower — is **open**: Chow proves it cannot *if* Schanuel's conjecture holds (his Theorem 2, stated for his quintic 2x⁵ − 10x + 5 as Conjecture 2; the Galois argument transfers to any S₅ quintic, as he remarks), and leaves the unconditional question open. His field E is defined with the principal branch of log — the chart's branch. So the gap has two layers: no *radical* form reaches the root (a theorem), and no *form at all* reaches it (conjectural). Lui's exp–log thread met the first layer directly: ~~"Lehmer's number is a radical form"~~ was wrong, because the Galois group of its trace polynomial is S₅, so the group is not solvable.

## Plain

The page can write any number you can reach with roots. Some solutions of simple equations lie beyond every stack of roots; whether the page's other shapes — logs of logs, exponentials of sums — reach them is unsettled.

## Derivation

none — gap.

## Confirms

That James's remark "the calculus covers the integers, the rationals, and the algebraic irrationals" is proven only for *the radical irrationals*; the stronger reading is *refuted* if Schanuel's conjecture holds (Chow 1999, Theorem 2) and survives only if Schanuel fails. A root-*finding* construction — an iteration that converges — would reach every real algebraic number regardless; that is the same shape as the gaps at [[Q.lowest-terms]] (Euclid) and [[N.induction]]: a process on forms, not a form.

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | fails | no setting adds a root-finding construction; JP's guarded re-entry (Hensel/Newton as re-entries) is the nearest thing and lives at a finite place |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

- ~~Lehmer's number is a radical form~~ — refuted 2026-10-01 in the exp–log thread: the Galois group of its degree-5 trace polynomial is S₅, so the Galois group of the degree-10 Lehmer polynomial is not solvable. (The first record here said "is a form" and "Galois group S₅" of the Lehmer polynomial itself; both corrected 2026-10-03 — the group of the degree-10 polynomial lies in C₂ ≀ S₅ and is larger than S₅.)
- ~~the real root of x⁵ − x − 1 is not ≐ any form~~ — overclaimed 2026-10-03 and corrected the same day: Abel–Ruffini excludes radical forms only; the exp–log case is Chow's conjecture.

## Notes

x⁵ − x − 1 is the standard example: irreducible over ℚ, discriminant 2869 = 19·151, Galois group S₅, one real root. Chow, "What is a closed-form number?", Amer. Math. Monthly 106 (1999).

## Plan

| field | content |
|---|---|
| candidate form(s) | a guarded *re-entry* (the JP-1 convention): `x ≐ F(x)` iterated with a contracting guard — Newton's step written natively, which the p-adic thread already does at finite places with depths 1, 2, 4, 8, 16, 32; at ∞ the guard ("the step shrinks") is semantic, which is the load-bearing gap the JP thread already named |
| law(s) to add, and type | a `decree` (the re-entry convention: a form defined by a guarded fixed-point equation is admissible) — or a `primitive` (a fixed-point / re-entry boundary, Spencer-Brown's re-entry made arithmetical), ranked last |
| nativity criterion | the guard must be checkable on forms (a syntactic contraction criterion), not only in the reading; at finite places the JP thread has this (the prime shrinks); at ∞ it does not |
| refutation test | a re-entry that satisfies the syntactic guard and fails to converge in the ℂ reading, or converges to the wrong root |
| meta-move? | yes: iteration; the fixed-point operator Lui favours for constructive computation in every setting |
| owner thread | p-adic-wall (JP-1, guarded re-entry); james-algebra (exp–log completeness, Lehmer) |
| rank | decree (re-entry convention) < primitive (re-entry boundary) |
