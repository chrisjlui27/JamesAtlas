---
id: C.conjugate
title: The conjugate mirrors the imaginary part
type: definition
level: object
kind: law
rung: C
order: 1056
setting: classical
equality: "≐"
domain: real
law: "conj(A + iB) := A <([B] [(([J] <[oo]>))])>"
units: "a − bi"
gloss_check: "A - B*1j"
holds:
  classical: holds
  J1: holds
  JH: replaced
  JO: replaced
  JP: guarded
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "Bombelli 1572 for the pairing; the name 'conjugate' Cauchy 1821"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [Z.subtraction, C.complex-number, C.imaginary-unit, mult.multiplication]
see_also: [C.complex-number, C.modulus-squared, C.conjugate-of-turn]
aliases: [conjugate, "a − bi", z̄]
concepts: [complex-number, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `A <([B] [(([J] <[oo]>))])>` | `A <([B] [i])>` | a − bi |

The rectangular spelling with the imaginary part mirrored. Conjugation is not an operation the calculus can apply to an arbitrary form — a variable has no "imaginary part" to mirror — it is a second spelling that goes with the first.

## Plain

The conjugate of a complex number is the same number with its up-and-down part flipped. On the page that is one mirror, placed around the i-term.

## Derivation

| form | rule | note |
|---|---|---|
| `A <([B] [(([J] <[oo]>))])>` | [[Z.subtraction]] | a minus b × i: the complex number of [[C.complex-number]] with its imaginary part mirrored ([[C.imaginary-unit]], [[mult.multiplication]]) |
| `conj(A + iB)` | name | — |

## Confirms

a − bi. What it is **not**: a function of forms. There is no boundary that conjugates, and `conj(X)` for a variable X is not a form; the conjugate exists for a number *written as* a + bi, and the theorem that the polar spelling has a conjugate too — the reverse turn — is [[C.conjugate-of-turn]]. That z z̄ is real is [[C.modulus-squared]].

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical | holds | — |
| J1 | holds | a spelling; no Λ-step |
| JH, JO | replaced | the quaternionic conjugate mirrors three imaginary parts, and reverses products: `conj(xy) = conj(y) conj(x)` |
| JP | guarded | as [[C.imaginary-unit]] |

| reading | cell | why |
|---|---|---|
| C | EXACT | — |
| finset | ABSENT | — |
| logic | ABSENT | — |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

—
