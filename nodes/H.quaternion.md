---
id: H.quaternion
title: A quaternion is a pile beside three scaled units
type: definition
level: object
kind: law
rung: H
order: 1720
setting: JH
equality: "≐"
domain: real
law: "A + Bi + Cj + Dk := A ([B ; i]) ([C ; j]) ([D ; k])"
units: "a + bi + cj + dk — a real part beside three real counts of i, j, k; the tuple (a, b, c, d) in the prose"
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
known_since: "Hamilton 1843 (the quaternion as a quadruple of reals, 'a + bi + cj + dk'); 1993 (James, ℂ as a + bi); this rung, 2026-10-07"
entered: 2026-10-07
guide: shape-led
band: "beyond"
uses: [C.imaginary-unit, H.collapse, H.j, H.k, H.ordered-product, N.addition]
see_also: [C.complex-number, H.conjugate, H.norm, H.polar-form, H.ordered-bracket]
aliases: [quaternion, a + bi + cj + dk, the four parts, rectangular form of a quaternion, scalar and vector part]
concepts: [quaternion, addition, ordered-product]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `A ([B ; i]) ([C ; j]) ([D ; k])` | `A (B·i) (C·j) (D·k)` | a + bi + cj + dk |

The rung's number. A real part `A` beside three parts, each a real count of one of the units i ([[C.imaginary-unit]]), j ([[H.j]]) and k ([[H.k]]); the count is the ordered product `([B ; i])` ([[H.ordered-product]]), which for a real `B` is also the old product `([B][i])` — the two are one by [[H.collapse]], a real log commuting with every log — and the ordered spelling is chosen because it is the one the later derivations open with splice. The pure part `([B ; i]) ([C ; j]) ([D ; k])` is written V in the prose and the quaternion `A V`; its conjugate is [[H.conjugate]], its norm [[H.norm]]. As at rung `C` ([[C.complex-number]]) nothing is adjoined: the spelling names the points of ℍ the forms reach, countably many, and "two quaternions are equal iff their four parts are" is a fact of the ℍ reading (SPEC §4.5), not a law of forms.

## Plain

A quaternion is an ordinary number next to some amount of i, some amount of j and some amount of k. The three amounts are products like any other; what is new is the units themselves.

## Derivation

| form | rule | note |
|---|---|---|
| `A ([B ; i]) ([C ; j]) ([D ; k])` | [[N.addition]] | a juxtaposed with the three counts b·i ([[C.imaginary-unit]]), c·j ([[H.j]]), d·k ([[H.k]]) — each an ordered product [[H.ordered-product]] of a real with a unit, and for a real count also the old product, by [[H.collapse]] |
| `A + Bi + Cj + Dk` | name | — |

## Confirms

ℍ = ℝ + ℝi + ℝj + ℝk, Hamilton's quadruple, with addition the juxtaposition of the page and multiplication the ordered square: the product of two such spellings is again one, by two-sided distribution ([[H.list-distribution]]) and the table of [[H.k]]…[[H.ik]] — [[H.pure-square]] and [[H.norm]] carry that computation out. It is **not** a canonical spelling: the same quaternion has many forms (the polar one, [[H.polar-form]]), and the forms do not know they are quadruples.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | no j, k: the spelling restricts to [[C.complex-number]] when C and D are void |
| JH | holds | the definition |
| JO | holds | the first four of an octonion's eight parts: the quaternions are a subalgebra |
| JP | holds | the quaternions of the page: at 2 the Hurwitz order allows the four parts to be all half-integers as well ([[H.hurwitz-units]]); at odd p the same spelling names a matrix ([[H.split-place]]) |

| reading | cell | why |
|---|---|---|
| C | ABSENT | j and k have no value in ℂ |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The domain is `real`: the four parts are sampled as nonzero reals, as at [[C.complex-number]] — a void part would make its square the black hole, and `(□ ; i)`-shaped counts are the hole rules' business, not multiplication's. In prose the chart writes q = (a, b, c, d) or q = a + v with v = bi + cj + dk the pure (vector) part; on the page it is always `A ([B ; i]) ([C ; j]) ([D ; k])`.
