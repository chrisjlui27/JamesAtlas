---
id: H.inverse
title: Every nonzero quaternion has a two-sided inverse
type: theorem
level: object
kind: law
rung: H
order: 1740
setting: JH
equality: "≃"
domain: real
law: "([A ([B ; i]) ([C ; j]) ([D ; k]) ; (<[([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])]> [A <([B ; i])> <([C ; j])> <([D ; k])>])]) ≃ o"
units: "q · (q̄/N(q)) = 1 = (q̄/N(q)) · q: ℍ is a division algebra; N = 0 only for q = 0, where the inverse is the excluded <□> (JH-20)"
gloss_check: ""
holds:
  classical: replaced
  J1: replaced
  JH: holds
  JO: holds
  JP: guarded
readings:
  C: ABSENT
  finset: untested
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE
verified: engine
known_since: "Hamilton 1843 (q⁻¹ = Kq/(Tq)²: 'the reciprocal of a quaternion'); Frobenius 1878 (ℍ is one of the three associative real division algebras); this rung, 2026-10-07"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.collapse, H.commutation, H.conjugate, H.norm, H.ordered-cancellation, H.splice, J1.counit, J1.unit, Q.reciprocal]
see_also: [Q.reciprocal-law, Q.no-division-by-zero, C.complex-quotient, H.split-place, H.hurwitz-units, mult.hole-exclusion]
aliases: [q⁻¹ = q̄/N, the quaternion inverse, division of quaternions, ℍ is a division algebra, the inverse quaternion]
concepts: [quaternion, reciprocal, division]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([A ([B ; i]) ([C ; j]) ([D ; k]) ; (<[([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])]> [A <([B ; i])> <([C ; j])> <([D ; k])>])]) ≃ o` | q · (q̄/N) ≃ 1 | q⁻¹ = q̄ / N(q) |

The conjugate divided by the norm is the inverse, on the right (the first table) and on the left (the second). The division is the page's own: `(<[N]> [q̄])` is the instance of the log of q̄ beside the negated log of N ([[Q.reciprocal]]) — the old, unordered product, which is legitimate here because N is real and real logs commute with every log ([[H.collapse]]). The derivation then lines the three factors up in one ordered square, moves the real `1/N` to the front ([[H.commutation]]), gathers `q ; q̄` into N ([[H.norm]]) and cancels `1/N ; N` by ordered cancellation ([[H.ordered-cancellation]]) — the one rung-H rule that cancels a reciprocal in depth. The receipt prover absorbs the two non-strict steps (the unit on the real `<[N]>`, receipt void, and the collapse) inside the instance. Hence ℍ is a **division algebra**: every q ≠ 0 divides, and the only quaternion without an inverse is 0, whose "inverse" `(<[void]>)` is `(<□>)`, excluded by decree ([[mult.hole-exclusion]], [[Q.no-division-by-zero]]) — JH-20's zero divisors do not exist at ∞. At an odd place they do ([[H.split-place]]): the norm is isotropic there, nonzero quaternions of the page have N ≡ 0, and for those `[N]` is formless — the law is guarded by N ≢ 0 (mod p), and the ledger says so.

## Plain

To divide by a quaternion, multiply by its flipped twin and divide by the ordinary number that twin produces. Only zero has no inverse — except at an odd prime, where some non-zero quaternions multiply to zero and cannot be divided by.

## Derivation

| form | rule | note |
|---|---|---|
| `([A ([B ; i]) ([C ; j]) ([D ; k]) ; (<[([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])]> [A <([B ; i])> <([C ; j])> <([D ; k])>])])` | given | q times q̄/N: the conjugate ([[H.conjugate]]) scaled by the reciprocal of the norm ([[Q.reciprocal]]) |
| `([A ([B ; i]) ([C ; j]) ([D ; k]) ; ([(<[([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])]>)] [A <([B ; i])> <([C ; j])> <([D ; k])>])])` | [[J1.unit]] | the reciprocal's log written as the log of its instance — receipt void: `<[N]>` is real |
| `([A ([B ; i]) ([C ; j]) ([D ; k]) ; ([(<[([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])]>) ; A <([B ; i])> <([C ; j])> <([D ; k])>])])` | [[H.collapse]] | two logs that commute (one is real): the square is the ordered square |
| `([A ([B ; i]) ([C ; j]) ([D ; k]) ; (<[([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])]>) ; A <([B ; i])> <([C ; j])> <([D ; k])>])` | [[H.splice]] | spliced open: q, then 1/N, then q̄ |
| `([(<[([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])]>) ; A ([B ; i]) ([C ; j]) ([D ; k]) ; A <([B ; i])> <([C ; j])> <([D ; k])>])` | [[H.commutation]] | 1/N is real: it commutes past q |
| `([(<[([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])]>) ; ([A ([B ; i]) ([C ; j]) ([D ; k]) ; A <([B ; i])> <([C ; j])> <([D ; k])>])])` | [[H.splice]] | q and q̄ gathered |
| `([(<[([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])]>) ; ([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])])` | [[H.norm]] | q·q̄ is N |
| `([o])` | [[H.ordered-cancellation]] | 1/N then N: the pair cancels to one |
| `o` | [[J1.counit]] | —  |

The other side:

| form | rule | note |
|---|---|---|
| `([(<[([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])]> [A <([B ; i])> <([C ; j])> <([D ; k])>]) ; A ([B ; i]) ([C ; j]) ([D ; k])])` | given | q̄/N times q |
| `([([(<[([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])]>)] [A <([B ; i])> <([C ; j])> <([D ; k])>]) ; A ([B ; i]) ([C ; j]) ([D ; k])])` | [[J1.unit]] | the reciprocal's log as the log of its instance |
| `([([(<[([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])]>) ; A <([B ; i])> <([C ; j])> <([D ; k])>]) ; A ([B ; i]) ([C ; j]) ([D ; k])])` | [[H.collapse]] | commuting logs: the square is the ordered square |
| `([(<[([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])]>) ; A <([B ; i])> <([C ; j])> <([D ; k])> ; A ([B ; i]) ([C ; j]) ([D ; k])])` | [[H.splice]] | spliced open |
| `([(<[([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])]>) ; ([A <([B ; i])> <([C ; j])> <([D ; k])> ; A ([B ; i]) ([C ; j]) ([D ; k])])])` | [[H.splice]] | q̄ and q gathered |
| `([(<[([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])]>) ; ([A] [A]) ([B] [B]) ([C] [C]) ([D] [D])])` | [[H.norm]] | q̄·q is N — the second table of [[H.norm]] |
| `([o])` | [[H.ordered-cancellation]] | 1/N then N cancels to one |
| `o` | [[J1.counit]] | —  |

## Confirms

Hamilton's q⁻¹ = Kq/(Tq)², and Frobenius's theorem in the only direction the chart can state: ℍ *is* a division algebra; that ℝ, ℂ, ℍ are the only finite-dimensional associative ones is a theorem about readings, not forms. The two-sidedness is the point of the second table — in a non-commutative algebra a right inverse need not be a left inverse, and here it is because the norm is two-sided ([[H.norm]]). It is **not** a new reciprocal: `(<[q]>)`, the reciprocal form of rung `Q`, is exp(−log q) = q⁻¹ in the reading, and `([q ; (<[q]>)]) ≃ o` is already ordered cancellation ([[H.ordered-cancellation]]); what this law adds is the *closed form* q̄/N, which needs no log of a quaternion — only the real log `[N]` — and which is what the places can read where logs are scarce ([[H.split-place]]).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | [[C.complex-quotient]]: z⁻¹ = z̄ / \|z\|² |
| JH | holds | two absorbed steps per table, the rest strict (census/h-ledger.md) |
| JO | holds | the octonions are a division algebra too (the norm is anisotropic over ℝ), by the same q̄/N — with the alternative laws standing in for splice |
| JP | guarded | at 2 the quaternions of the page divide (a division algebra: [[H.ramified-place]]), but the reading's log reaches few of them and the law is formless on every sample there (`none`: owed, [[H.ramified-place]], Notes); at odd p the norm is isotropic and the law holds only where N ≢ 0 mod p and the logs exist — a nonzero zero divisor has no reciprocal and no log (census/h-place-ledger.md) |

| reading | cell | why |
|---|---|---|
| C | ABSENT | j and k have no value in ℂ |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The unit step `<[N]> → [(<[N]>)]` is a 𝕁₁ step ([[J1.unit]]) with a void receipt — `<[N]>` is real, so exp then log returns it exactly — graded absorbed by position rather than strict because the prover grades every unit step in 𝕁₁ by its receipt; the tape records it. The zero divisors at odd p are the page's reading of JH-20 (the norm-null species): at ∞ the species is empty, and the chart's `<□>` exclusion is all the guard needed.
