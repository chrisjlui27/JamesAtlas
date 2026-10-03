---
id: mult.hole-exclusion
title: The two undefined forms
type: decree
level: meta
kind: exclusion
rung: mult
order: 440
setting: classical
equality: "≐"
domain: positive
law: "<□> is not a form; [□] is not a form"
units: "1/0 (as the exponent of (<□>)) and ln(−∞) are undefined"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE-BY-DECREE
verified: hand
known_since: "1993 (James: both forms undefined); JO-25 in Book One restates the refusal of <□>; the collapse argument that shows the decree is load-bearing: referee pass 2026-10-03"
entered: 2026-10-03
guide: need-led
band: "6–8"
uses: [Z.angle, mult.square, mult.black-hole]
see_also: [mult.dominion, mult.consistency, Z.void-inverse]
aliases: ["<□>", "[□]", "[[ ]]", division by zero, James's undefined forms, JO-25, admissibility]
concepts: [infinity, inverse, consistency]
understood: yes
understood_note: ""
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `<□>` | — | +∞ in the log layer; `(<□>)` would be 1/0 |
| `[□]` | — | ln(−∞): no value |

James leaves exactly two forms undefined: the angle boundary around the black hole and the square boundary around it. The decree is read **up to ≐**: a form that reduces to □ may be neither mirrored nor abstracted, and no row of a derivation may contain such a subform. Of the nine combinations of two empty boundaries, these are the two that are refused; `<>`, `[()]`, `(<>)`, `<<>>`, `[<>]` are nothing, `(())`, `([])` and `<()>` are something.

## Plain

You may not mirror the bottomless pit, and you may not ask what you would have to circle to get it. Both questions have no answer, and the page refuses them rather than answering wrongly.

## Derivation

none — adjoined, as a decree about the two forms built from [[Z.angle]], [[mult.square]] and [[mult.black-hole]]. The calculus does not derive the exclusion; it legislates it, and the legislation is load-bearing. If `<□>` were admitted, Dominion and Inversion would give `A ≐ A □ <□> ≐ □ <□> ≐ void` for every `A`. If `[□]` were admitted, write `W` for `(o [□])`: Dominion inside the square gives `(o [□]) ≐ (o [□ C])`, Distribution gives `(o [□ C]) ≐ (o [□]) (o [C])`, so `W ≐ W X` with `X` = `(o [C])`; adjoining `<W>` and cancelling gives `X ≐ void`, i.e. `(o [C]) ≐ void` for every `C`, and with `C` = `(<o>)` the unit itself is void. Either admission makes every form equal to every other.

## Confirms

Division by zero as *the* exclusion of arithmetic, and ln(−∞) beside it. The JH extension found the same decree bans a third thing: inverting a singular matrix (JH-20: a biquaternion with norm form void demands `<□>`). What the decree protects is the consistency of the whole calculus ([[mult.consistency]]): the engine enforces it by raising `Excluded` and `Undefined` whenever a derivation row evaluates to one of the two forms, which is the up-to-value version of the rule.

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | holds | kept in every extension; JO-25 restates the refusal of `<□>` |

| reading | cell | why |
|---|---|---|
| C | EXACT | 1/0 and ln(−∞) |
| finset | ABSENT | — |
| logic | untested | — |
| lambda, CC | untested | — |

## Refuted readings

- ~~`[□]` is merely an *open* form, unread but admissible~~ — refuted 2026-10-03 (referee pass): admitting it collapses the calculus by the derivation above. It is excluded, and Bricken's reading of `[[ ]]` as complex infinity is a reading of an excluded form, not a law.
- ~~the decree bans only the literal string `<□>`~~ — refuted the same day: any form ≐ □ (e.g. `[J J]` once J-cancellation is available at rung C) would bypass a literal ban; the decree is up to ≐.

## Notes

Lui's open question (p-adic-wall thread) whether `[ ]` can be split into ±∞ and what that does to `<[ ]>` is a *plan* against this decree; it is recorded there, not here, until it produces a form.
