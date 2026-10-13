---
id: H.seam-guard
title: The sphere seam
type: decree
level: meta
kind: guard
rung: H
order: 1755
setting: JH
equality: "≐"
domain: complex
law: "GUARD — in ℍ the unit step `[(A)] → A` fires only where L(exp V(A)) = V(A): on the band |Im A| < π and on the pinned ray Im A = π·i; on the rest of the angle-π sphere, Im A = π·u with u ≠ i, it is refused, because the one log the reading gives −r is ln r + πi (J-pinning, LEGISLATION 31)"
units: "log(exp(πu)) = πi ≠ πu for a pure unit u ≠ i; unguarded, with a second seed J_v = πv, the step would prove (−1)(−1) ≐ e^{π(i+v)}, a non-real unit — One-J Rigidity (JH-2)"
gloss_check: ""
witness: tools/models/h_seam_guard.py
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE-BY-DECREE
verified: engine
known_since: "2026-08 (the JH-Calculus report, JH-3: 'Involution-down is valid off the seam; on the seam only the pinned ray survives'; JH-2: One-J Rigidity); the trunk's seam decree 2026-10-03; J-pinning in ℍ: LEGISLATION 31, 2026-10-06"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.phase-sphere, H.seed, J1.unit, mult.involution, mult.seam-decree]
see_also: [mult.seam-signature, J1.half-period, J1.seam-theorem, H.slice-wall, H.no-go, H.anticommutation]
aliases: [JH-3, the Involution-Seam theorem, the sphere seam, One-J Rigidity, JH-2, J-pinning, the pinned ray]
concepts: [consistency, logarithm, negation, quaternion]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[(A)] → A` admitted iff L(exp V(A)) = V(A): V(A) in the band, or on the pinned ray ln r + πi | — | log e^z = z fails on the seam by a *direction*, not only by a multiple of 2π |

The trunk's seam decree ([[mult.seam-decree]]) says where the unit direction of Involution ([[mult.involution]]) may fire: on the principal strip, or in an absorbing position. In ℂ the seam is one point of the circle, θ = π, and the strip's edge is where the step is "off by 2πi". In ℍ the seam is a **2-sphere**: every pure unit u gives a log πu of −1 ([[H.phase-sphere]]), the reading's log returns the one it has pinned — L(−r) = ln r + πi, the direction of James's own J ([[H.seed]] names the second seed; the pinning is LEGISLATION 31) — and so `[(A)]` with V(A) = ln r + πu, u ≠ i, is not A: it is A rotated to the pinned ray. Off the seam, in the open band |Im A| < π, the step is exact. The decree is the same content clause as the trunk's, "L(exp V(A)) = V(A)", read in ℍ (SPEC §6.4): no new rule, a new seam. What it guards against is One-J Rigidity (JH-2): a second phase constant J_v = πv with the step unguarded proves `<o> <o>`, which is `(J_i) (J_v)`, is `(J_i J_v)` is e^{π(i+v)}, a non-real unit, so (−1)(−1) ≐ a non-real — the collapse. In 𝕁₁ the step is priced, not refused ([[J1.unit]]): the receipt prover computes V(A) − L(exp V(A)) and asks whether an instance pays it; on the seam the difference π(u − i) is no lattice element and no instance pays, so the step is `absent` — the engine's reading of this decree.

## Plain

The box may undo the circle except right on the seam, and in the quaternions the seam is not a point but a whole sphere's worth of directions; only the one direction the calculus chose for its own J gets through.

## Derivation

none — adjoined, as the ℍ reading of [[mult.seam-decree]], stated in terms of [[mult.involution]], the receipt of [[J1.unit]] and the sphere of [[H.phase-sphere]], whose second named point is the seed [[H.seed]].

| statement | rule | note |
|---|---|---|
| L(exp(πu)) = πi ≠ πu for u ≠ i | — | witness part (1): 40 random pure units |
| unguarded, J_v a second seed: (−1)(−1) ≐ e^{π(i + v)} ≠ 1 | — | witness part (2): the blow-up, computed |
| the guard holds exactly on the band plus the pinned ray; the receipt of a step across the seam is no lattice element, and the prover grades that step `absent` at depth 0 and `absorbed [seam]` directly inside an instance | [[J1.unit]] | witness parts (3), (4), (5) |

## Confirms

James's J-discipline a third time ([[C.james-discipline]] on the trunk, [[mult.seam-decree]] at rung `mult`, this at `H`): the crack is the same crack, and in ℍ it is wider. It is **not** a restriction on the counit `([A]) ≐ A`, which is exact in every direction, nor on absorbed positions — a seam step directly inside an instance is paid by that instance if the content is co-sliced with the receipt ([[H.slice-wall]]); across slices even an instance does not pay, which is the second guard the rung adds.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | replaced | the seam is the point θ = π: [[mult.seam-decree]] |
| J1 | replaced | the step is priced by a receipt, not refused: [[J1.unit]] |
| JH | holds | the decree |
| JO | holds | the seam is a 6-sphere of directions; the pinned ray is the same |
| JP | holds | at 2 the negative principal units are pinned to the direction i (tools/quatplace.py, LEGISLATION 31); at odd p J_p is central and the seam has no directions to choose |

| reading | cell | why |
|---|---|---|
| C | EXACT | the guard restricted to the slice of i is the trunk's |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

JH-3's statement is for the involution-down direction; the up direction `A → [(A)]` is guarded by the same clause (as the trunk's decree learned from its referee pass), and the prover grades both. The witness's last part is the engine's own behaviour: it feeds the prover the seam step `[(Jj)] → Jj` and checks the grade — `absent` at depth 0, `absorbed [seam]` directly inside an instance.
