---
id: C.quadratic-formula
title: The quadratic formula — James's factorization
type: theorem
level: object
kind: law
rung: C
order: 1089
setting: classical
equality: "≐"
domain: real
law: "([A] ([[X]] [oo])) ([B] [X]) C ≐ ([A] [X ([B] <[A] [oo]>) (([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))] [X ([B] <[A] [oo]>) <(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))>])"
units: "a x² + b x + c = a (x + d + f)(x + d − f), d = b/2a, f = √(d² − c/a)"
gloss_check: "A*X*X + B*X + C"
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: untested
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "Brahmagupta 628 and al-Khwārizmī c. 820 for the solutions; the factorization in forms: James 1993, Appendix B.5 pp. 76–79"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [mult.multiplication, Q.division, alg.root, mult.distribution, mult.inverse-promotion, Z.inversion, mult.involution, Q.fractional-cardinality, Z.collection, Z.cancellation, mult.cardinality]
guarded_by: [mult.seam-decree]
see_also: [Q.division, alg.root, C.root-of-negative, mult.multiplication, Q.no-division-by-zero]
aliases: [quadratic formula, completing the square, "ax² + bx + c"]
concepts: [root, multiplication, complex-number]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A] ([[X]] [oo])) ([B] [X]) C ≐ ([A] [X d f] [X d <f>])` | with d = `([B] <[A] [oo]>)`, e = `([C] <[A]>)`, f = `(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))` | a x² + b x + c = a (x − s₁)(x − s₂), s₁,₂ = (−b ∓ √(b² − 4ac)) / 2a |

James's finale: the quadratic, factored into its two roots on the page. The two solutions are the two factors — `<d f>` and `<d <f>>` in his notation (p. 78) — and no sign choice is made: f is the principal root form, and its mirror is the other root. The thesis derives this under the hypothesis "= void" by completing the square; the chart states it as the identity the hypothesis is applied to.

## Plain

Any quadratic is a times (x minus one root) times (x minus the other). The roots are minus half the middle coefficient, give or take a square root — and "give or take" is one mirror on the page.

## Derivation

| form | rule | note |
|---|---|---|
| `([A] [X ([B] <[A] [oo]>) (([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))] [X ([B] <[A] [oo]>) <(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))>])` | given | a (x + d + f)(x + d − f), with d = b ÷ 2a, e = c ÷ a and f = √(d² − e) — James's s₁ = `<d f>`, s₂ = `<d <f>>` (p. 78); [[mult.multiplication]], [[Q.division]], [[alg.root]] |
| `([A] [X ([B] <[A] [oo]>) (([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))] [X ([B] <[A] [oo]>)]) ([A] [X ([B] <[A] [oo]>) (([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))] [<(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))>])` | [[mult.distribution]] | distribute over the second factor, x + d and <f> |
| `([A] [X ([B] <[A] [oo]>)] [X ([B] <[A] [oo]>)]) ([A] [(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))] [X ([B] <[A] [oo]>)]) ([A] [X ([B] <[A] [oo]>)] [<(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))>]) ([A] [(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))] [<(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))>])` | [[mult.distribution]] | and over the first, x + d and f, in each: four terms |
| `([A] [X ([B] <[A] [oo]>)] [X ([B] <[A] [oo]>)]) ([A] [(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))] [X ([B] <[A] [oo]>)]) <([A] [X ([B] <[A] [oo]>)] [(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))])> <([A] [(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))] [(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))])>` | [[mult.inverse-promotion]] | the two mirrors come out |
| `([A] [X ([B] <[A] [oo]>)] [X ([B] <[A] [oo]>)]) <([A] [(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))] [(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))])>` | [[Z.inversion]] | the cross terms cancel: (x + d)² − f² |
| `([A] [X] [X ([B] <[A] [oo]>)]) ([A] [([B] <[A] [oo]>)] [X ([B] <[A] [oo]>)]) <([A] [(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))] [(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))])>` | [[mult.distribution]] | expand the square, first factor |
| `([A] [X] [X]) ([A] [X] [([B] <[A] [oo]>)]) ([A] [([B] <[A] [oo]>)] [X]) ([A] [([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([A] [(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))] [(([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))])>` | [[mult.distribution]] | and second: x² + 2dx + d² |
| `([A] [X] [X]) ([A] [X] [([B] <[A] [oo]>)]) ([A] [X] [([B] <[A] [oo]>)]) ([A] [([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([A] ([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>) ([[([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>]] <[oo]>))>` | [[mult.involution]] | the unit on each `[f]` — f is an instance — directly inside the mirrored instance: absorbing through the angle |
| `([A] [X] [X]) ([A] [X] [([B] <[A] [oo]>)]) ([A] [X] [([B] <[A] [oo]>)]) ([A] [([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([A] [([([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([C] <[A]>)>])>` | [[Q.fractional-cardinality]] | two halves of the log of d² − e make the log: f² = d² − e, the root squared |
| `([A] [X] [X]) ([A] [X] [([B] <[A] [oo]>)]) ([A] [X] [([B] <[A] [oo]>)]) ([A] [([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([A] [([([B] <[A] [oo]>)] [([B] <[A] [oo]>)])]) ([A] [<([C] <[A]>)>])>` | [[mult.distribution]] | distribute a over d² and <e> |
| `([A] [X] [X]) ([A] [X] [([B] <[A] [oo]>)]) ([A] [X] [([B] <[A] [oo]>)]) ([A] [([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([A] [([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([A] [([C] <[A]>)])>>` | [[mult.involution]] [[mult.inverse-promotion]] | the unit on `[([d][d])]`, absorbing; the mirror of e comes out |
| `([A] [X] [X]) ([A] [X] [([B] <[A] [oo]>)]) ([A] [X] [([B] <[A] [oo]>)]) ([A] [([B] <[A] [oo]>)] [([B] <[A] [oo]>)]) <([A] [([B] <[A] [oo]>)] [([B] <[A] [oo]>)])> ([A] [([C] <[A]>)])` | [[Z.collection]] [[Z.cancellation]] | the outer mirror distributes, right to left; the double mirror on a·e cancels |
| `([A] [X] [X]) ([A] [X] [([B] <[A] [oo]>)]) ([A] [X] [([B] <[A] [oo]>)]) ([A] [([C] <[A]>)])` | [[Z.inversion]] | a·d² and its mirror cancel |
| `([A] [X] [X]) ([A] [X] [([B] <[A] [oo]>)]) ([A] [X] [([B] <[A] [oo]>)]) ([A] [C] <[A]>)` | [[mult.involution]] | the unit on `[e]` = `[([C] <[A]>)]`, directly inside the instance — absorbing |
| `([A] [X] [X]) ([A] [X] [([B] <[A] [oo]>)]) ([A] [X] [([B] <[A] [oo]>)]) C` | [[Z.inversion]] [[mult.involution]] | `[A] <[A]>` cancels and the counit `([C]) ≐ C`: a·e is c |
| `([A] [X] [X]) ([([A] [X] [([B] <[A] [oo]>)])] [oo]) C` | [[mult.cardinality]] | two copies of a·d·x become the count 2 |
| `([A] [X] [X]) ([A] [X] [([B] <[A] [oo]>)] [oo]) C` | [[mult.involution]] | the unit, directly inside the instance — absorbing |
| `([A] [X] [X]) ([A] [X] [B] <[A] [oo]> [oo]) C` | [[mult.involution]] | the unit on `[d]` = `[([B] <[A] [oo]>)]` — absorbing (for a and b of opposite sign the content is off the strip: a seam step) |
| `([A] [X] [X]) ([A] [X] [B] <[A]> <[oo]> [oo]) C` | [[Z.collection]] | right to left: the mirror of the pile is the pile of mirrors |
| `([A] [X] [X]) ([X] [B]) C` | [[Z.inversion]] | `[A] <[A]>` and `[oo] <[oo]>` cancel: 2a·d·x is b·x |
| `([A] ([[X]] [oo])) ([B] [X]) C` | [[mult.cardinality]] | `[X] [X] ≐ ([[X]] [oo])`: a x² + b x + c, in James's spelling (p. 79) |

## Confirms

The quadratic formula as a factorization identity, exact for every complex x and every a ≠ 0 — expanded here from the factored side, the way one checks the formula, which is the reverse of James's completing-the-square derivation (pp. 76–79: introduce 1/a from the void, work d and e in, flatten, complete the square, make a difference of squares, separate the factors). Where the textbook writes ±, the page writes f and `<f>`, two forms the calculus keeps apart; the two "solutions" are the equation `([A] [X d f] [X d <f>]) ≐ void` read with [[Q.no-division-by-zero]]'s companion — a product is void only if a factor is — which is a reading-level fact, not a law of the forms. It is **not** an algorithm for roots (James: "an *informed* calculation", p. 75) and **not** restricted to a positive discriminant: for d² − e < 0 the form f is a quarter-turn times a real root ([[C.root-of-negative]]), and the identity holds unchanged.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | every unit step directly under an instance, through an angle at most |
| JH, JO | replaced | quadratics over ℍ have infinitely many roots when the discriminant is negative (every unit imaginary direction gives one); the factorization is slice-local |
| JP | untested | the p-adic quadratic formula needs √ at p, i.e. the wall criterion for f |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

Guarded by position (Amendment A2): the units on `[f]`, `[d]`, `[e]` and `[([d][d])]` have content off the strip for some signs of a, b, c (e.g. `[d]` → ln b − ln a − ln 2 has imaginary part −π when b > 0 > a); all sit directly inside instances, through an angle at most. The engine samples a, b, c, x as nonzero reals; at d² = e exactly the form f passes through the hole and the law is still true but outside the sampled domain.
