---
id: N.induction
title: Induction on a pile
type: gap
level: meta
kind: concept
rung: N
order: 180
setting: classical
equality: "≐"
domain: natural
law: "GAP — 'a law that holds of void and is preserved by adjoining o holds of every pile' is not a form and not an equation"
units: "P(0) ∧ (∀n. P(n) ⇒ P(n+1)) ⇒ ∀n. P(n)"
holds:
  classical: fails
  J1: fails
  JH: fails
  JO: fails
  JP: fails
readings:
  C: ABSENT
  finset: PARTIAL
  lambda: untested
  CC: untested
  logic: ABSENT
status: ABSENT
verified: hand
known_since: "Peano 1889 (the schema); Lawvere 1964 (the universal property, in the ETCS paper); the gap named here 2026-10-03"
entered: 2026-10-03
guide: need-led
band: beyond
uses: []
see_also: [N.freeness, N.successor, N.add-comm]
aliases: [Peano 5, induction schema, Nat.rec]
concepts: [induction, natural-number]
understood: partial
understood_note: "I see why an equational calculus can't say it; the finset route is the one I want to understand"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| none | — | P(0) and P(n) ⇒ P(n+1) give P(n) for all n |

An equational calculus states equalities between forms. "For every pile" is a quantifier over forms, and "a property that is preserved by `A ↦ A o`" is a statement about statements. Neither is a form. Yet without induction ℕ is not ℕ: commutativity ([[N.add-comm]]) came free from the medium, but the general theorems of arithmetic (every pile is even or odd; the division algorithm; cardinality for *every* n at [[mult.cardinality]]) are schemas whose "for every n" the calculus cannot itself assert.

## Plain

The calculus can show something for 2, for 3, for 4 — one pile at a time — but it has no way to say "and so on, forever."

## Derivation

none — gap.

## Confirms

That James's calculus is an *equational* theory of forms, not a *logic*: it has no quantifiers, no implication, no variables ranging over properties. Every "for all n" in the chart is a meta-statement the reader supplies: a `kind: instance` node states one value of such a family, and a `schema` node (rung `schema`, SPEC §3.7) states the family as a template, checked by the engine at every value in a declared range and closed by a `hypothesis` row that cites this gap — so from rung `schema` on the gap is *priced* (it appears in the price of every schema and of everything built on one) rather than merely named. That is the Plan's option (i), the schema as an admissible rule of the chart's proof language, taken in its weakest form: the engine checks the base case and that the hypothesis row is the law at a smaller parameter; the passage to all n it cannot check, and does not claim to. The two ends of the chart both need this gap closed: the Lean expansion (where `Nat.rec` is native) and the F₁ end (where ℕ must be recognized as the *free* commutative monoid on `o`).

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | fails | no setting of the program has quantifiers; the extrusion calculus's receipts and the ludics frame gesture at a logic layer but do not supply a schema |

| reading | cell | why |
|---|---|---|
| C | ABSENT | — |
| finset | PARTIAL | in the finite-set reading, induction is the *universal property* of ℕ as the initial algebra / free monoid on one generator (Lawvere's natural numbers object): a statement about the medium, not an equation — but a statement with a form-level shadow (freeness, [[N.freeness]]) |
| logic | ABSENT | LoF has no numbers to induct over |
| lambda, CC | untested | — |

## Refuted readings

none

## Notes

This is the first honest gap the reader meets (LEGISLATION 17). It is deliberately not smoothed over. Since 2026-10-04 it is cited by [[schema.cardinality]], [[schema.power]] and [[schema.period-multiple]] and inherited by every schema built on them (LEGISLATION 29): a gap in the price, not a gap in the chart's knowledge of where it stands.

## Plan

| field | content |
|---|---|
| candidate form(s) | none — a rule schema, not a form. Candidate *meta-form*: a judgement `A ⊢ B` over forms with a rule "from `P(void)` and `P(A) ⊢ P(A o)` infer `P(A)` for all piles `A`" |
| law(s) to add, and type | (i) a `decree` at the meta level: the induction schema as an admissible rule of the chart's proof language (not of the calculus); (ii) alternatively an `import` — Lawvere's universal property, with the finite-set reading carrying it; (iii) the Lean expansion, where it is `Nat.rec` and costs nothing |
| nativity criterion | the schema must be stated using only forms, juxtaposition, and ≐ — "holds of void" and "holds of `A o` whenever it holds of `A`" are already statable; only the closing "for every pile" is not. Native iff the closing step can be read as a property of the *medium* (piles are free) rather than an added rule |
| refutation test | exhibit a property P of piles, statable as an equation schema, true of every numeral, and not derivable from the schema — i.e. a non-standard model of the chart's piles satisfying the schema |
| meta-move? | yes: the moduli of readings. Induction is the statement that the stack of piles is generated by one point. In the finset reading that is the universal property; in the ℂ reading it is invisible. The chart treats induction as *the first law that lives only in a reading*, which is the shape Lui expects meta-moves to take |
| owner thread | boundary-lean-game; james-algebra (the F₁ / BPQ reading) |
| rank | import (finset universal property) < meta-decree (schema) < new primitive (a quantifier boundary — not proposed) |
