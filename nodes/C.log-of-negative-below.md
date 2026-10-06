---
id: C.log-of-negative-below
title: The log of a negative, from the other side
type: theorem
level: object
kind: law
rung: C
order: 945
setting: classical
equality: "≐"
domain: negative
law: "[<A>] ≐ [A] <J>"
units: "ln(−a) = ln a − iπ  (a < 0)"
gloss_check: "log(A) - 1j*pi"
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
known_since: "the principal branch's rule for the open upper half-plane and the negative axis; stated here 2026-10-03 (C referee pass: the on-sight rule needs its companion)"
entered: 2026-10-03
guide: need-led
band: "9–12"
uses: [Z.cancellation, C.log-of-negative, Z.inversion]
see_also: [C.log-of-negative, mult.seam-decree, mult.seam-signature]
aliases: ["ln(−a) = ln a − iπ", the other on-sight rule, upper half-plane conversion]
concepts: [phase, logarithm, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[<A>] ≐ [A] <J>` | — | ln(−a) = ln a − iπ, for a < 0 |

The companion of [[C.log-of-negative]]: when A is already negative, its log carries +iπ, and the log of its mirror is reached by taking that half-turn *off*. Together the two laws cover every nonzero complex A — each one exactly where the other fails — and no single law covers both halves: that is the seam.

## Plain

The log of minus a negative number is the log of the number with its half-turn removed, not added. Which rule applies depends on which side of the line you are on — and the page cannot see which side; you have to look.

## Derivation

| form | rule | note |
|---|---|---|
| `[A] <J>` | given | — |
| `[<<A>>] <J>` | [[Z.cancellation]] | `A ≐ <<A>>`, right to left |
| `[<A>] J <J>` | [[C.log-of-negative]] | with A := `<A>`, which is positive when A is negative — inside the law's declared domain |
| `[<A>]` | [[Z.inversion]] | `J <J>` cancels |

## Confirms

ln(−a) = ln a − iπ for negative a: with ln a = ln|a| + iπ on the principal branch, the right side is ln|a|, which is ln(−a) ✓. No unit step is taken here; the law inherits its guard from [[C.log-of-negative]] through the price. It is **not** derivable the way the first law was — `[<A>] → [([A] J)] → [A] J` — because for negative A that content is ln|a| + 2πi, off the strip at depth 0, and the engine refuses it; the route through the mirror of a mirror is the one the decree leaves open. More generally the law is exact for Im Ln A ∈ (0, π] — the open upper half-plane together with the negative real axis — and false by 2πi elsewhere (on the positive reals included), exactly complementary to its companion.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds-mod-Λ | inherits the bare depth-0 unit of [[C.log-of-negative]]: `[<A>] ≃ [A] <J>` with a receipt |
| JH, JO | replaced | as [[C.log-of-negative]]: in ℍ the half-turn removed must be the one in A's own slice |
| JP | holds-mod-Λ | as [[C.log-of-negative]]: J = ω_p/2 at every place, the receipt posted |

| reading | cell | why |
|---|---|---|
| C | PARTIAL | exact for Im Ln A ∈ (0, π]; false by 2πi otherwise |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

The engine samples this law on `domain: negative`, a domain added for it: the first law in the chart whose natural home is the negative reals.
