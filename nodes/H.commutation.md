---
id: H.commutation
title: Commuting entries exchange
type: axiom
level: object
kind: law
rung: H
order: 1630
setting: JH
equality: "≐"
domain: slice
law: "[P ; Q] ≐ [Q ; P]"
units: "PREMISE P·Q ≐ Q·P — log(PQ) = log(QP) when the values commute: a conditional law, its premise checked by the reading at each use; adjacent entries of any list; the law's domain is the slice"
gloss_check: ""
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
status: NATIVE
verified: engine
known_since: "this chart, 2026-10-07 (the value-level half of the JH report's conditional collapse rule, needed to move a central scalar past j when the scalar is negative)"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [H.ordered-bracket, H.ordered-product, void.space]
see_also: [void.space, H.collapse, H.norm, H.inverse]
aliases: [ordered commutation, central elements commute in a list, conditional exchange, "comm(x,y) ≐ o"]
concepts: [ordered-product, multiplication]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `[P ; Q] ≐ [Q ; P]` **when the values commute** (P·Q ≐ Q·P); the family exchanges any two adjacent entries of a list of up to five | log(PQ) = log(QP) | a conditional rule: its premise is a fact about the values |

The premise is not a form, so the `law:` field carries the equation and the `units:` field the premise, and the law's domain is `slice` — the engine shadow-checks the equation on co-sliced entries, where the premise holds, and checks the premise itself at every use of the rule.

The medium exchanges juxtaposed forms for free ([[void.space]]); the ordered square does not, and that is its point. But two entries whose *values* commute may be exchanged, because then PQ and QP are one quaternion and their logs are one log ([[H.ordered-product]]). The rule is **conditional**, and the chart's first: the engine checks the premise at every use — the entries matched as P and Q are evaluated at the generic points of the node's domain, and a step whose entries do not commute is refused (`tools/j1.py`, `premise_holds`; `absent [premise]` on the tape). The typical use is a central scalar moving past a unit: `[B ; i ; C ; j]` → `[B ; C ; i ; j]` ([[H.norm]]). The premise is weaker than the collapse's ([[H.collapse]]): −1 and j commute as values though their pinned logs do not, so `[<o> ; j] ≐ [j ; <o>]` while `[<o> ; j]` does not collapse to `[<o>][j]`.

## Plain

In the ordered row you may swap two neighbours only if they commute — a real number and anything, two powers of the same unit. The engine checks that they do before it lets you.

## Derivation

none — adjoined, as a conditional rule of the ordered square ([[H.ordered-bracket]]) about its instances ([[H.ordered-product]]): a theorem of the reading (PQ = QP ⟹ log PQ = log QP), stated as a rule because the calculus has no other way to use a commutation. The medium's [[void.space]] is its unconditional ancestor.

## Confirms

That the centre of ℍ is ℝ, and that each slice C_u is commutative: inside a slice the ordered square may be permuted. It is **not** derivable from the collapse: the collapse needs the logs to commute, which fails for a negative real beside j.

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | replaced | [[void.space]]: everything commutes |
| JH | holds | an axiom of the setting, conditional |
| JO | holds | in the octonions too, commuting elements have equal products in either order |
| JP | holds | at every place, with the premise checked on the page's quaternions |

| reading | cell | why |
|---|---|---|
| C | EXACT | the premise always holds in ℂ |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

Conditional rules are new to the chart (SPEC §4.5, LEGISLATION 32): the premise is not a form, so it is checked by the reading at the use site, as the seam decree's by-content clause is — and recorded on the tape when it fails. The premise function (`tools/quat.py`, `premise("commute")`) evaluates the two entries and tests their commutator.
