---
id: H.seed
title: The second seed
type: decree
level: object
kind: declaration
rung: H
order: 1660
setting: JH
equality: "≐"
domain: complex
law: "(Jj) ≐ <o>"
units: "e^{J_j} = −1 with J_j ≢ J: a second logarithm of minus one, J_j = πj, adjoined as a constant — the seed of the second imaginary unit"
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
status: NATIVE-BY-DECREE
verified: engine
known_since: "2026-08 (JH report, Layer 3: 'one new constant J_j (a second phase seed, (J_j) ≐ <o>)'); the direction of j is Hamilton 1843"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [C.phase, C.phase-value, Z.angle]
see_also: [C.phase, C.phase-value, C.phase-unique, H.j, H.anticommutation, H.phase-sphere, H.seam-guard]
aliases: [J_j, the second phase seed, Jj, second seed, a second log of −1, the Clifford seed]
concepts: [quaternion, phase, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(Jj) ≐ <o>`, with `Jj` a new constant and `Jj ≢ J` | the instance of the second seed is minus one, and the seed is not J | e^{πj} = −1, πj ≠ πi |

James found J = `[<o>]` ([[C.phase]]) as the one stable three-boundary form ([[C.phase-unique]]), and `(J) ≐ <o>` ([[C.phase-value]]) says it is a log of −1. In ℂ there is one such log up to sign; in ℍ there is a 2-sphere of them ([[H.phase-sphere]]), and the calculus can name a second only by adjoining it: `Jj`, a constant with no boundaries, declared to be a log of minus one — `(Jj) ≐ <o>` — and declared different from J. Nothing in the three boundaries produces it (One-J Rigidity, JH-2: a James-style calculus with unguarded involution tolerates exactly one J up to sign), so it is a decree, and priced. Its half is j ([[H.j]]); with i and O9 ([[H.anticommutation]]) it generates the quaternions. The road to Clifford algebras runs through this node: n pairwise-anticommuting seeds J_{e₁}, …, J_{eₙ} give Cl₀,ₙ(ℝ), with n = 2 the quaternions (JH OP-4) — a mixed signature would need a +1-square seed `(K) ≐ o` with K ≢ void, which no stable three-boundary configuration supplies.

## Plain

Minus one has one logarithm in the complex numbers (up to sign) and a whole sphere of them in the quaternions. The chart names a second one and calls it J_j; its half is the unit j.

## Derivation

none — adjoined: a declaration that a second log of minus one exists, built on [[C.phase]] (the first), [[C.phase-value]] (what a log of minus one satisfies) and [[Z.angle]] (minus one itself). The engine reads `Jj` as πj (`tools/quat.py`) and checks the declared equation.

## Confirms

That ℍ contains a second square root of −1 anticommuting with the first — but only once O9 is adjoined: the seed alone says the direction is new, not that it is orthogonal. It is **not** derivable from `[<o>]`: `[(Jj)]` is `[<o>]` = J, not `Jj` — the unit step on the seed is false, and that is the sphere seam ([[H.seam-guard]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | one J; `Jj` has no value in ℂ |
| JH | holds | the declaration of the setting |
| JO | holds | the octonions add a third seed J_l anticommuting with both |
| JP | holds | at every place: the log of −1 in the direction j, with (Jj) = −1 on the page (`tools/quatplace.py`) |

| reading | cell | why |
|---|---|---|
| C | ABSENT | ℂ has one slice: no second direction |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

~~"a second phase constant can be adjoined with Involution unguarded"~~ — refuted in the JH audit (JH-2): three steps then prove (−1)(−1) ≐ e^{π(u₀+v)}, a non-real unit; the seam guard is load-bearing from the second seed on.

## Notes

Canonical strings write the constant as `Jj`; cards draw it as J_j. In the ℍ reading its value is πj, the J-pinning convention for the second seed (LEGISLATION 32(a)).
