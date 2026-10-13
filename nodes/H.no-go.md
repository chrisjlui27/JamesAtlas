---
id: H.no-go
title: Breadth is capped at ℂ
type: theorem
level: meta
kind: law
rung: H
order: 1600
setting: JH
equality: "≡"
domain: complex
law: "[A][B] and [B][A] are one form, so a reading in which ([A][B]) is the product A·B is commutative wherever it is sound; pairwise-commuting quaternions lie in one slice ℝ + ℝu — the classical calculus is intrinsically at most complex (JH-1, the Slice theorem)"
units: "exp(log A + log B) = A·B forces AB = BA; commuting quaternions have parallel pure parts; in-band rigidity: exp(X+Y) = exp X · exp Y iff XY = YX for X, Y with |Im| < π"
gloss_check: ""
witness: tools/models/h_no_go.py
holds:
  classical: holds
  J1: holds
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
known_since: "2026-08 (the JH-Calculus report, JH-1/JH-5: 'relocating non-commutativity from spatial breadth into ordered depth'); the algebra is Hamilton 1843"
entered: 2026-10-07
guide: need-led
band: "beyond"
uses: [mult.c-reading, mult.multiplication, void.space]
see_also: [mult.multiplication, void.space, H.ordered-bracket, H.collapse, H.slice-wall, H.seam-guard]
aliases: [JH-1, the No-Go theorem, the Slice theorem, breadth is commutative, JH-5, the Depth Principle]
concepts: [quaternion, multiplication, ordered-product]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| statement | units | standard |
|---|---|---|
| the forms `[A][B]` and `[B][A]` are the same form of the medium; so any reading sound for the multiplication encoding `([A][B]) = A·B` on a set of values makes that product commutative, and a set of pairwise-commuting quaternions lies in one slice C_u = ℝ + ℝu ≅ ℂ | — | the classical James algebra reaches ℂ and no further: the Slice theorem |

The chart's product is `([A][B])` ([[mult.multiplication]]): the instance of two logs *beside each other*. Beside is unordered ([[void.space]]): `[A][B]` and `[B][A]` are one form, so whatever the reading, the product it encodes commutes. In ℍ that is fatal for the encoding — `exp(log A + log B)` is not A·B for generic quaternions (the witness: on 60 of 60 samples), and is for co-sliced ones — and the reason is a theorem of ℍ: pq − qp = 2 P × Q, so pairwise-commuting quaternions have parallel pure parts, and parallelism globalizes to one slice. Three independent proofs survive the JH audit: the symmetry of the form (above); branch-robustness — in-band rigidity, exp(X + Y) = exp X · exp Y iff XY = YX for X, Y in the principal band |Im| < π, which is where James's J-discipline keeps the logs, so no branch trickery evades it (and the bound is sharp: X = 4πu, Y = 3πv with u ⟂ v gives a coincidence out of band); and J-pinning — the one form `[<o>]` takes one value L(−1) = πu₀, and the sole freedom u₀ ↦ −u₀ is James's sign pathology. **The Depth Principle (JH-5)** follows: breadth carries only the abelian group (ℍ, +); nesting — containment, composition — is intrinsically ordered and can carry the Hamilton product. So a non-commutative multiplication *must* be located in depth, and the rest of the rung is the ordered square that does it.

## Plain

Two boxes side by side are the same picture whichever is on the left, so "a times b" written that way can never tell ab from ba. The quaternions need to tell them apart; a box whose inside has an order will.

## Derivation

| statement | rule | note |
|---|---|---|
| **Symmetry.** `[A][B]` and `[B][A]` are one form: juxtaposition is unordered | [[void.space]] | witness part (a): the two parse to one canonical form |
| **The encoding.** `([A][B])` reads as exp(log A + log B) ([[mult.c-reading]] moved to ℍ, SPEC §4.5); it equals A·B on co-sliced contents and not on generic ones | [[mult.multiplication]] | witness part (b): 60/60 generic samples fail, 60/60 co-sliced samples agree up to the seam's sign |
| **Commuting ⟹ co-sliced.** pq − qp = 2 P × Q for the pure parts P, Q; so pairwise commutation forces parallel pure parts, and a pairwise-commuting set lies in one slice | — | witness part (c) |
| **In-band rigidity.** For X, Y in the band, exp(X + Y) = exp X · exp Y iff [X, Y] = 0; sharp: out of band X = 4πi, Y = 3πj gives −1 = −1 with [X, Y] ≠ 0 | — | witness part (d): the branch discipline is what makes the theorem exact |

## Confirms

Hamilton's own discovery, read as a theorem about a notation: a commutative notation cannot write his product. It is **not** a limitation of boundaries as such — the ordered square [[H.ordered-bracket]] writes the product one rung on — and **not** a statement about the real slices: within any C_u the whole classical calculus applies verbatim with J → J_u ([[H.collapse]], the Slice Principle).

## Settings and readings

| setting | holds | why |
|---|---|---|
| classical, J1 | holds | a theorem about those settings: their product is commutative |
| JH | holds | the reason the setting has an ordered square |
| JO | holds | a fortiori: the octonions are not even associative, and composition is |
| JP | holds | at a finite place too: `([A][B])` is formless or false for non-commuting quaternions of the page ([[H.split-place]]) |

| reading | cell | why |
|---|---|---|
| C | EXACT | in ℂ everything commutes and the encoding is exact — the theorem's conclusion |
| finset, lambda, CC, logic | untested | — |

## Refuted readings

none

## Notes

The JH report's three proofs (A symmetry, B branch-robustness, C J-pinning) are the four witness parts; the report's "200,000 random trials with an exact cross-product obstruction" is here 60 samples and the exact theorem pq − qp = 2P×Q. The corollary One-J Rigidity (JH-2) — a second phase constant with unguarded involution proves (−1)(−1) ≐ e^{π(u₀+v)} — is the seam guard's business, [[H.seam-guard]].
