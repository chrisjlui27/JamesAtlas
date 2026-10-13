---
id: H.pure-square
title: A pure quaternion squares to minus its norm
type: theorem
level: object
kind: law
rung: H
order: 1730
setting: JH
equality: "≃"
domain: real
law: "([([B ; i]) ([C ; j]) ([D ; k]) ; ([B ; i]) ([C ; j]) ([D ; k])]) ≃ <([B] [B]) ([C] [C]) ([D] [D])>"
units: "v² = −(b² + c² + d²) for v = bi + cj + dk: the square of a pure quaternion is a non-positive real; the six cross terms cancel in three anticommuting pairs"
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
status: NATIVE
verified: engine
known_since: "Hamilton 1843 (the square of a 'pure imaginary' quaternion is negative); this rung, 2026-10-07"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.central-sign, H.collapse, H.commutation, H.i-squared, H.ik, H.j-squared, H.ji, H.jk, H.k, H.k-squared, H.ki, H.kj, H.list-distribution, H.quaternion, H.splice, H.unit-entry, J1.counit, Z.collection, Z.inversion]
see_also: [H.norm, H.phase-sphere, C.i-squared, H.anticommutation]
aliases: [v² = −|v|², the square of a pure quaternion, pure quaternions square to negative reals]
concepts: [quaternion, ordered-product, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `([([B ; i]) ([C ; j]) ([D ; k]) ; ([B ; i]) ([C ; j]) ([D ; k])]) ≃ <([B] [B]) ([C] [C]) ([D] [D])>` | V·V ≃ −(b² + c² + d²) | v² = −\|v\|² |

The pure part of [[H.quaternion]] multiplied by itself in order. Two-sided distribution ([[H.list-distribution]]) opens the product into nine terms; the three diagonal ones are `(b·i)(b·i)` and its kin, each a real square times a unit squared ([[H.i-squared]], [[H.j-squared]], [[H.k-squared]]) — minus a square; the six cross terms come in three pairs `(b·i)(c·j)` and `(c·j)(b·i)`, which Hamilton's table turns into `bc·k` and `−bc·k` ([[H.k]], [[H.ji]]; likewise [[H.jk]]/[[H.kj]] and [[H.ki]]/[[H.ik]]) and Inversion cancels. Eighty rows, every one a shape rule; the only steps not strict are the three collapses `<([B ; B])> → <([B][B])>` — a real count beside itself, co-sliced with everything — which the receipt prover absorbs inside the instance. The 2-sphere of pure units u (b² + c² + d² = 1) therefore all satisfy u·u ≐ <o>: that is [[H.phase-sphere]].

## Plain

Square a quaternion with no ordinary part and you get an ordinary number, and a negative one: the i, j, k cross terms kill each other off in pairs because ij = −ji, and what remains is −(b² + c² + d²).

## Derivation

| form | rule | note |
|---|---|---|
| `([([B ; i]) ([C ; j]) ([D ; k]) ; ([B ; i]) ([C ; j]) ([D ; k])])` | given | the pure part V = b·i + c·j + d·k of [[H.quaternion]], squared in order |
| `([([B ; i]) ([C ; j]) ([D ; k]) ; ([B ; i])]) ([([B ; i]) ([C ; j]) ([D ; k]) ; ([C ; j]) ([D ; k])])` | [[H.list-distribution]] | the second entry split: V·(b·i) beside V·(c·j + d·k) |
| `([([B ; i]) ([C ; j]) ([D ; k]) ; ([B ; i])]) ([([B ; i]) ([C ; j]) ([D ; k]) ; ([C ; j])]) ([([B ; i]) ([C ; j]) ([D ; k]) ; ([D ; k])])` | [[H.list-distribution]] | — and again: three products |
| `([([B ; i]) ; ([B ; i])]) ([([C ; j]) ([D ; k]) ; ([B ; i])]) ([([B ; i]) ([C ; j]) ([D ; k]) ; ([C ; j])]) ([([B ; i]) ([C ; j]) ([D ; k]) ; ([D ; k])])` | [[H.list-distribution]] | the first entry of V·b·i split, on the left |
| `([([B ; i]) ; ([B ; i])]) ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ([C ; j]) ([D ; k]) ; ([C ; j])]) ([([B ; i]) ([C ; j]) ([D ; k]) ; ([D ; k])])` | [[H.list-distribution]] | — and again |
| `([([B ; i]) ; ([B ; i])]) ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; j]) ([D ; k]) ; ([C ; j])]) ([([B ; i]) ([C ; j]) ([D ; k]) ; ([D ; k])])` | [[H.list-distribution]] | the first entry of V·c·j split, on the left |
| `([([B ; i]) ; ([B ; i])]) ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; j]) ; ([C ; j])]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ([C ; j]) ([D ; k]) ; ([D ; k])])` | [[H.list-distribution]] | — and again |
| `([([B ; i]) ; ([B ; i])]) ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; j]) ; ([C ; j])]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ([D ; k]) ; ([D ; k])])` | [[H.list-distribution]] | the first entry of V·d·k split, on the left |
| `([([B ; i]) ; ([B ; i])]) ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; j]) ; ([C ; j])]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.list-distribution]] | — and again: nine products in all |
| `([B ; i ; ([B ; i])]) ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; j]) ; ([C ; j])]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.splice]] | the diagonal term (b·i)²: its first entry spliced open |
| `([B ; i ; B ; i]) ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; j]) ; ([C ; j])]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.splice]] | — and its second |
| `([B ; B ; i ; i]) ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; j]) ; ([C ; j])]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.commutation]] | the real count B commutes with i: exchanged |
| `([([B ; B]) ; i ; i]) ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; j]) ; ([C ; j])]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.splice]] | the two counts gathered |
| `([([B ; B]) ; ([i ; i])]) ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; j]) ; ([C ; j])]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.splice]] | the two units gathered |
| `([([B ; B]) ; <o>]) ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; j]) ; ([C ; j])]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.i-squared]] | i² is minus one |
| `<([([B ; B]) ; o])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; j]) ; ([C ; j])]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.central-sign]] | the sign out |
| `<([([B ; B])])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; j]) ; ([C ; j])]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.unit-entry]] | times one |
| `<([B ; B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; j]) ; ([C ; j])]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[J1.counit]] | —  |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; j]) ; ([C ; j])]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.collapse]] | two copies of the real B: co-sliced, the ordered square collapses to the square — absorbed inside the instance |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([C ; j ; ([C ; j])]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.splice]] | the diagonal term (c·j)²: its first entry spliced open |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([C ; j ; C ; j]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.splice]] | — and its second |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([C ; C ; j ; j]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.commutation]] | the real count C commutes with j: exchanged |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; C]) ; j ; j]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.splice]] | the two counts gathered |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; C]) ; ([j ; j])]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.splice]] | the two units gathered |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) ([([C ; C]) ; <o>]) ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.j-squared]] | j² is minus one |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) <([([C ; C]) ; o])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.central-sign]] | the sign out |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) <([([C ; C])])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.unit-entry]] | times one |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) <([C ; C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[J1.counit]] | —  |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; k]) ; ([D ; k])])` | [[H.collapse]] | two copies of the real C: co-sliced, the ordered square collapses to the square — absorbed inside the instance |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([D ; k ; ([D ; k])])` | [[H.splice]] | the diagonal term (d·k)²: its first entry spliced open |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([D ; k ; D ; k])` | [[H.splice]] | — and its second |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([D ; D ; k ; k])` | [[H.commutation]] | the real count D commutes with k: exchanged |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; D]) ; k ; k])` | [[H.splice]] | the two counts gathered |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; D]) ; ([k ; k])])` | [[H.splice]] | the two units gathered |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) ([([D ; D]) ; <o>])` | [[H.k-squared]] | k² is minus one |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([([D ; D]) ; o])>` | [[H.central-sign]] | the sign out |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([([D ; D])])>` | [[H.unit-entry]] | times one |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([D ; D])>` | [[J1.counit]] | —  |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([([B ; i]) ; ([C ; j])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([D] [D])>` | [[H.collapse]] | two copies of the real D: co-sliced, the ordered square collapses to the square — absorbed inside the instance |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([B ; i ; ([C ; j])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([D] [D])>` | [[H.splice]] | the cross term (b·i)(c·j): first entry spliced open |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([B ; i ; C ; j]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([D] [D])>` | [[H.splice]] | — and the second |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([B ; C ; i ; j]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([D] [D])>` | [[H.commutation]] | the real count C commutes with i: exchanged |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([B ; C ; ([i ; j])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([D] [D])>` | [[H.splice]] | the two units gathered |
| `<([B] [B])> ([([C ; j]) ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([B ; C ; k]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([D] [D])>` | definition | ij is k ([[H.k]]) |
| `<([B] [B])> ([C ; j ; ([B ; i])]) ([([D ; k]) ; ([B ; i])]) ([B ; C ; k]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([D] [D])>` | [[H.splice]] | the cross term (c·j)(b·i): first entry spliced open |
| `<([B] [B])> ([C ; j ; B ; i]) ([([D ; k]) ; ([B ; i])]) ([B ; C ; k]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([D] [D])>` | [[H.splice]] | — and the second |
| `<([B] [B])> ([C ; B ; j ; i]) ([([D ; k]) ; ([B ; i])]) ([B ; C ; k]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([D] [D])>` | [[H.commutation]] | the real count B commutes with j: exchanged |
| `<([B] [B])> ([C ; B ; ([j ; i])]) ([([D ; k]) ; ([B ; i])]) ([B ; C ; k]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([D] [D])>` | [[H.splice]] | the two units gathered |
| `<([B] [B])> ([C ; B ; <k>]) ([([D ; k]) ; ([B ; i])]) ([B ; C ; k]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([D] [D])>` | [[H.ji]] | ji is minus k |
| `<([B] [B])> <([C ; B ; k])> ([([D ; k]) ; ([B ; i])]) ([B ; C ; k]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([D] [D])>` | [[H.central-sign]] | the sign out |
| `<([B] [B])> <([B ; C ; k])> ([([D ; k]) ; ([B ; i])]) ([B ; C ; k]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([D] [D])>` | [[H.commutation]] | the real counts C, B exchanged: now the mirror image of the other cross term |
| `<([B] [B])> ([([D ; k]) ; ([B ; i])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([([C ; j]) ; ([D ; k])]) <([D] [D])>` | [[Z.inversion]] | the pair (b·i)(c·j) + (c·j)(b·i) cancels: anticommutation made visible |
| `<([B] [B])> ([([D ; k]) ; ([B ; i])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([C ; j ; ([D ; k])]) <([D] [D])>` | [[H.splice]] | the cross term (c·j)(d·k): first entry spliced open |
| `<([B] [B])> ([([D ; k]) ; ([B ; i])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([C ; j ; D ; k]) <([D] [D])>` | [[H.splice]] | — and the second |
| `<([B] [B])> ([([D ; k]) ; ([B ; i])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([C ; D ; j ; k]) <([D] [D])>` | [[H.commutation]] | the real count D commutes with j: exchanged |
| `<([B] [B])> ([([D ; k]) ; ([B ; i])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([C ; D ; ([j ; k])]) <([D] [D])>` | [[H.splice]] | the two units gathered |
| `<([B] [B])> ([([D ; k]) ; ([B ; i])]) <([C] [C])> ([([D ; k]) ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([C ; D ; i]) <([D] [D])>` | [[H.jk]] | jk is i |
| `<([B] [B])> ([([D ; k]) ; ([B ; i])]) <([C] [C])> ([D ; k ; ([C ; j])]) ([([B ; i]) ; ([D ; k])]) ([C ; D ; i]) <([D] [D])>` | [[H.splice]] | the cross term (d·k)(c·j): first entry spliced open |
| `<([B] [B])> ([([D ; k]) ; ([B ; i])]) <([C] [C])> ([D ; k ; C ; j]) ([([B ; i]) ; ([D ; k])]) ([C ; D ; i]) <([D] [D])>` | [[H.splice]] | — and the second |
| `<([B] [B])> ([([D ; k]) ; ([B ; i])]) <([C] [C])> ([D ; C ; k ; j]) ([([B ; i]) ; ([D ; k])]) ([C ; D ; i]) <([D] [D])>` | [[H.commutation]] | the real count C commutes with k: exchanged |
| `<([B] [B])> ([([D ; k]) ; ([B ; i])]) <([C] [C])> ([D ; C ; ([k ; j])]) ([([B ; i]) ; ([D ; k])]) ([C ; D ; i]) <([D] [D])>` | [[H.splice]] | the two units gathered |
| `<([B] [B])> ([([D ; k]) ; ([B ; i])]) <([C] [C])> ([D ; C ; <i>]) ([([B ; i]) ; ([D ; k])]) ([C ; D ; i]) <([D] [D])>` | [[H.kj]] | kj is minus i |
| `<([B] [B])> ([([D ; k]) ; ([B ; i])]) <([C] [C])> <([D ; C ; i])> ([([B ; i]) ; ([D ; k])]) ([C ; D ; i]) <([D] [D])>` | [[H.central-sign]] | the sign out |
| `<([B] [B])> ([([D ; k]) ; ([B ; i])]) <([C] [C])> <([C ; D ; i])> ([([B ; i]) ; ([D ; k])]) ([C ; D ; i]) <([D] [D])>` | [[H.commutation]] | the real counts D, C exchanged: now the mirror image of the other cross term |
| `<([B] [B])> ([([D ; k]) ; ([B ; i])]) <([C] [C])> ([([B ; i]) ; ([D ; k])]) <([D] [D])>` | [[Z.inversion]] | the pair (c·j)(d·k) + (d·k)(c·j) cancels: anticommutation made visible |
| `<([B] [B])> ([D ; k ; ([B ; i])]) <([C] [C])> ([([B ; i]) ; ([D ; k])]) <([D] [D])>` | [[H.splice]] | the cross term (d·k)(b·i): first entry spliced open |
| `<([B] [B])> ([D ; k ; B ; i]) <([C] [C])> ([([B ; i]) ; ([D ; k])]) <([D] [D])>` | [[H.splice]] | — and the second |
| `<([B] [B])> ([D ; B ; k ; i]) <([C] [C])> ([([B ; i]) ; ([D ; k])]) <([D] [D])>` | [[H.commutation]] | the real count B commutes with k: exchanged |
| `<([B] [B])> ([D ; B ; ([k ; i])]) <([C] [C])> ([([B ; i]) ; ([D ; k])]) <([D] [D])>` | [[H.splice]] | the two units gathered |
| `<([B] [B])> ([D ; B ; j]) <([C] [C])> ([([B ; i]) ; ([D ; k])]) <([D] [D])>` | [[H.ki]] | ki is j |
| `<([B] [B])> ([D ; B ; j]) <([C] [C])> ([B ; i ; ([D ; k])]) <([D] [D])>` | [[H.splice]] | the cross term (b·i)(d·k): first entry spliced open |
| `<([B] [B])> ([D ; B ; j]) <([C] [C])> ([B ; i ; D ; k]) <([D] [D])>` | [[H.splice]] | — and the second |
| `<([B] [B])> ([D ; B ; j]) <([C] [C])> ([B ; D ; i ; k]) <([D] [D])>` | [[H.commutation]] | the real count D commutes with i: exchanged |
| `<([B] [B])> ([D ; B ; j]) <([C] [C])> ([B ; D ; ([i ; k])]) <([D] [D])>` | [[H.splice]] | the two units gathered |
| `<([B] [B])> ([D ; B ; j]) <([C] [C])> ([B ; D ; <j>]) <([D] [D])>` | [[H.ik]] | ik is minus j |
| `<([B] [B])> ([D ; B ; j]) <([C] [C])> <([B ; D ; j])> <([D] [D])>` | [[H.central-sign]] | the sign out |
| `<([B] [B])> ([D ; B ; j]) <([C] [C])> <([D ; B ; j])> <([D] [D])>` | [[H.commutation]] | the real counts B, D exchanged: now the mirror image of the other cross term |
| `<([B] [B])> <([C] [C])> <([D] [D])>` | [[Z.inversion]] | the pair (d·k)(b·i) + (b·i)(d·k) cancels: anticommutation made visible |
| `<([B] [B]) ([C] [C])> <([D] [D])>` | [[Z.collection]] | the three negatives collected |
| `<([B] [B]) ([C] [C]) ([D] [D])>` | [[Z.collection]] | — minus the sum of the three squares |

## Confirms

That the pure quaternions are the "square roots of negative reals" of ℍ, as i is the square root of −1 in ℂ ([[C.i-squared]]) — and there are a sphere's worth of them of each modulus. It is **not** a statement about mixed quaternions: with a real part a ≠ 0 the square `(a + v)² = a² − |v|² + 2a·v` is not real, and [[H.norm]] pairs a + v with a − v instead.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | one unit: `([([B ; i]) ; ([B ; i])]) ≃ <([B][B])>` is [[C.i-squared]] scaled |
| JH | holds | three absorbed collapses, every other step strict (the tape, census/h-ledger.md) |
| JO | holds | the same expansion for a pure octonion: distinct units anticommute and each squares to −1, and no step needs associativity across more than a quaternion subalgebra |
| JP | holds | at 2 and at odd p the law is the same congruence on the page (census/h-place-ledger.md); at odd p the right side can be ≡ 0 for a nonzero V — the isotropic norm of [[H.split-place]] — and then `[V ; V]` is formless, a zero divisor's log |

| reading | cell | why |
|---|---|---|
| C | ABSENT | j and k have no value in ℂ |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The table is generated (tools: the rung's emitter) and licensed row by row by the prover; it is long because the chart refuses to write "by distributivity and the multiplication table" as one step. The three pair cancellations are the three uses of anticommutation ([[H.anticommutation]], through [[H.ji]], [[H.kj]], [[H.ik]]) — the page shows exactly where O9 is spent.
