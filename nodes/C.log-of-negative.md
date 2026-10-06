---
id: C.log-of-negative
title: The log of a negative is the log plus J
type: theorem
level: object
kind: law
rung: C
order: 940
setting: classical
equality: "≐"
domain: positive
law: "[<A>] ≐ [A] J"
units: "ln(−a) = ln a + iπ  (a > 0)"
gloss_check: "log(A) + 1j*pi"
holds:
  classical: holds
  J1: holds-mod-Λ
  JH: replaced
  JO: replaced
  JP: holds-mod-Λ
readings:
  C: PARTIAL
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James, Ch. 6 p. 45: 'the inverse jumping outside of the abstract boundary', [<A>] = [A] J; and §6.3 p. 47, constraint 1: convert inverse boundaries to Js on sight); its failure for negative A: alg referee pass 2026-10-03"
entered: 2026-10-03
guide: need-led
band: "9–12"
uses: [C.phase-rule, mult.involution]
guarded_by: [mult.seam-decree]
see_also: [C.phase-rule, C.log-of-negative-below, C.james-discipline, mult.seam-signature]
aliases: [on-sight conversion, "ln(−a) = ln a + iπ", James's first disciplinary rule]
concepts: [phase, logarithm, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[<A>] ≐ [A] J` | — | ln(−a) = ln a + iπ, for a > 0 |

The phase rule under a square. James's first disciplinary rule says to apply it *on sight*; the chart records exactly when that is admissible: for content whose log has imaginary part in (−π, 0] — positive reals, and the lower half-plane — and not otherwise.

## Plain

The log of minus a number is the log of the number plus a half-turn — true for the numbers you meet first, and a trap for the others.

## Derivation

| form | rule | note |
|---|---|---|
| `[<A>]` | given | — |
| `[([A] J)]` | [[C.phase-rule]] | `<A> ≐ ([A] J)` under the square |
| `[A] J` | [[mult.involution]] | the unit at depth 0, content ln a + iπ: imaginary part exactly π, the closed edge of the strip — admitted by the seam decree on its content (guarded by content) |

## Confirms

ln(−a) = ln a + iπ for positive a, which is the principal branch's choice. It is **not** a law for all A: at A = `<o>` the content is 2πi and the step is a refused seam step (which is how `J J ≐ void` would otherwise be derived); at A = `[[oo]]`, a negative real with no mirror, the left side is −1.0037 and the right −1.0037 + 2πi. So James's "on sight" is sound only on sight of a positive pile, and the chart's `domain: positive` is where the engine samples it.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | under the seam decree, for content on the strip |
| J1 | holds-mod-Λ | a bare unit step at depth 0: the receipt is not absorbed — `[<A>] ≃ [A] J` with receipt, which is J1's phase-independence statement |
| JH, JO | replaced | unsound in ℍ as stated: the log of −w is the log of w plus π·(the direction of w's own slice), not plus the fixed J (JH's O6 warning); the central sign `< >` is the portable carrier |
| JP | holds-mod-Λ | `[<A>] ≃ [A] J` with J = ω_p/2 at every place; posted, as at 𝕁₁ (the place ledger) |

| reading | cell | why |
|---|---|---|
| C | PARTIAL | exact for Im Ln A ∈ (−π, 0]; false by 2πi otherwise |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

- ~~`[<A>] ≐ [A] J` holds for every form A (the on-sight rule as a law)~~ — refuted 2026-10-03 (alg referee pass) at A = `[[oo]]`; recorded at [[mult.seam-decree]] and [[C.james-discipline]].

## Notes

Status: NATIVE with `guarded_by` (by content), like [[alg.log-law]] — the unit step is at depth 0, where nothing absorbs, and is admitted because its content stays on the strip over the whole declared domain (imaginary part exactly π for positive A). Had the domain admitted content that leaves the strip, the engine would have refused the row outright: at depth 0 there is no position to save it. The chart's statement is therefore *narrower* than James's "on sight": the rule is sound on sight of a positive pile, and the engine samples it there. The other half-plane has its own law, [[C.log-of-negative-below]].
