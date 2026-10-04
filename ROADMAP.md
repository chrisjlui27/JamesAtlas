# Roadmap — from the classical algebra to the F₁ picture

*Written 2026-10-03, after rung `C` was closed against the thesis. This is the chart's own view of the path; the decisions in it are proposals until Lui confirms them (LEGISLATION).*

## 0. Where the chart stands

138 laws, rungs `void` → `C`, 907 engine checks, five referee passes on `C`, every citation checked against James 1993 (now in `references/`). The classical James algebra — three boundaries, three axioms, two decrees — is on the chart with its two cracks located: `[□]` admitted collapses it (pilot pass), and the last row of James's own proof of phase independence (p. 44) is the unit step the seam decree adjudicates. Six named gaps: induction, order, lowest terms, a native seam signature, irrationality of √2, non-radical algebraic numbers.

## 1. The three target pictures, in the chart's terms

The chart already has the shape all three targets need; what is missing is the rungs that make the shape *native*.

| target | what it is, in the chart | what is missing |
|---|---|---|
| **motivic** | a node is a form; its `readings` row (ℂ, finset, λ, CC, logic …) is its row of *realizations*; a law that holds in every reading is the stable part. The form is the motive, the readings are its realizations, and the "comparison boundary B between pages" (motivic thread, 2026-10-03) is the comparison isomorphism between realizations | the readings are columns filled by hand; nothing on the page *is* a reading. The rung that makes a reading a form is `struct` (a page as a form) and `logic` (the internal language in which "for every reading" can be said) |
| **F₁ (finset / BPQ road)** | `( )` and `[ ]` as finite sets, `< >` as group completion; the additive fragment `void`–`N` is EXACT in finset today, and the inverse boundary is where the sphere spectrum enters | the `finset` cells are mostly `ABSENT`/`untested` past `N`; J's finset analogy (η) matches the *J1* J (2J = ω), not the classical one — so the F₁ road passes through `J1`, not around it |
| **sheaf of formal groups over the (classifying topos of the) Berkovich space** | the Berkovich spectrum of ℤ is the space of places; the chart's `JP` setting is "the same wall `(ω A) ≐ (A)` at every place", with the place a pile declared void. The wall at a place is a formal group of height one (Λ = the period lattice of exp = Ĝ_m at ∞; the ψ-wall selecting ω/n is its torsion, the im-J arithmetic). The *stack* of lattices — level 2, "a syntax fibered over the moduli stack of its own lattices" — is the moduli of formal groups with its height stratification. The sheaf is the chart itself once the base (places) and the fibre (the lattice per place) are rungs rather than columns | a `place` rung before the branches; a `J1` rung that makes Λ native (closing `mult.seam-signature`); a `J2`/moduli rung that does not yet exist in `RUNGS`; and the schema machinery (induction) without which μ_n for all n — the torsion of the formal group — cannot be stated |

So: **yes, the target adjusts the order**, in three ways. The places move before the division algebras; the moduli rung is inserted; and the induction gap stops being a gap left for later and becomes the first thing to build, because every one of the three pictures needs schemas over n.

## 2. Proposed rung order (revision of SPEC §1 / §13)

Current: `void N Z mult Q alg C | J1 H O S | analysis place logic struct F1`.

Proposed:

```
void N Z mult Q alg C          the trunk (done)
schema                          induction / schemas over n as meta-moves (gap → machinery)
J1                              the enriched wall at ∞: Λ native, the decree becomes a theorem
place                           the same wall at p; the void pile; the Berkovich base (JP)
analysis                        metrics at ∞ and p (Ostrowski), differentiation (James Table 7.1)
J2 (moduli)                     the stack of lattices; readings as points of the base
logic, struct                   the page as a form; the internal language; the comparison boundary B
F1                              the fibre over the trivial place; the finset reading made native
H, O, S                         the Hurwitz road (JH/JO/JS), backfilled from the book as a branch
```

Why each move:

- **`schema` first.** The thesis itself proves cardinality by induction (p. 27). General n-th roots of unity, general De Moivre, the ψ-wall (`n | r^{2k} − 1`), M(2k) = 24, 240, 504, μ_n ⊂ Ĝ_m — all are statements *over n*. The chart can hold each n as a node today (it does, for n = 2, 3) and nothing more. Proposal (LEGISLATION 17 said "start with the named gap; meta-moves may wind up being necessary"): a node type `schema` whose law carries a parameter `n`, verified by finite instantiation (the engine instantiates n = 1…8 and shadow-checks each) plus a prose induction step in James's style; `status: NATIVE-BY-SCHEMA` so the price shows the meta-move. This is the smallest machinery that unlocks the torsion of the formal group.
- **`J1` before everything else.** It is where the chart's biggest import is paid off: the seam decree is stated in the ℂ reading because no syntactic signature of "off the strip" exists (`mult.seam-signature`). In J1 the condition becomes "the receipt is void" — Λ is a native object, the unit is weakened to `[(A)] ≃ A mod Λ`, `(ω) ≐ o` is forced by confluence, A5′ absorbs the kernel, `J J ≐ ω` heals the crack identically at every place (JP result). The `holds-mod-Λ` and `≃` cells already on every trunk node are the ledger J1 will settle. Deliverables: the J1 axioms as nodes; `mult.seam-signature` closed (`guarded_by` the import becomes `guarded_by` a lattice law); the depth-1 criterion as a theorem; the J1 cells of rung `C` (eleven are `untested`) filled.
- **`place` before `H O S`.** The Berkovich picture needs the base before the fibres. JP already exists as a ledger (`Part-II-A-Calculus-of-Number-at-a-Place.md`, chapters 9–15 continuing the thesis numbering) and as the "Forms at Every Place" engine; the chart's job is to make its axioms nodes — the wall as Axiom 4, depth as Axiom 5, the lens axioms — and to show that `(ω A) ≐ (A)` has the same shape at ∞ and p. The quaternions and octonions are a different road (Hurwitz, the ordered bracket), orthogonal to places; they lose nothing by coming later and would clutter the base if they came first.
- **`analysis` next, not last.** The Berkovich space *is* the set of seminorms; Ostrowski's theorem is its classification; the chart cannot say "at every place" natively without a metric rung. James's own future work (Ch. 7, Table 7.1, boundary differentiation) belongs here, and the trunk's analysis-owing nodes (modulus and the triangle inequality, `((o))`, `[o o]`) land here.
- **`J2` inserted.** The level-2 question — what forces a Λ₂ the way the multiplicative-identity theorem forced A5′ — is the program's stall. The chart should hold it as a rung with gap nodes and witnesses (the additive route closed, Λ + Λ = Λ; the monodromy route computing Λ₂ = ℤ/2; the multiplicative route an import with a stated nativeness criterion) rather than pretend it is a rung of laws. Its pedagogical content for the walk: the readings columns are the fibres of a moduli; this is where that becomes a statement rather than a table.
- **`logic`, `struct` before `F1`.** The classifying topos is the internal language; "a sheaf over the base" is said in it. The polarized-linear-logic dictionary and the two-cell presentation (receipts as 2-cells) are the material; the comparison boundary B of the motivic thread is the first new primitive the chart will have proposed since the three boundaries, and it should be *forced* by a theorem the way A5′ was, or it is an import.
- **`F1` last, as the fibre over the trivial place.** On the Berkovich spectrum of ℤ the trivial absolute value is the centre; F₁ sits there in every published road. The finset road is the default (LEGISLATION 2); Borger's λ-rings (ψ as Frobenius lifts — the chart already has ψ as cardinality-power) and Connes–Consani are readings to fill alongside.

## 3. What does not change

One law per node; every derivation engine-checked; referees before acceptance; the price computed, never asserted; readings filled honestly (`untested` is a legal cell, a confident wrong cell is not); the thesis as ground truth for `classical` and the ledgers (JH, JO, JS, JP, 𝕁 v3.x) as ground truth for the branches, each cited by page or rule number.

## 4. The next three steps, concretely

1. **Confirm A1 and A2**, and the rung order above (or amend it). Nothing below starts on an unconfirmed order.
2. **`schema`**: design the node type (law with parameter, finite instantiation in the engine, prose induction step), convert `mult.cardinality`, `C.cube-root-of-unity`/`C.cube-root-of-negation`, `C.de-moivre` to instances of schemas, and write the first schema-only law: the n-th roots of unity `(([J] [2k] <[n]>))` with their multiplication as addition of counts mod 2.
3. **`J1`**: the axioms as nodes; the seam decree re-derived as a theorem with Λ native; `mult.seam-signature` closed; the C-rung J1 cells settled; the receipts rendered on the cards (the `≃` equality the data model already carries).

Still owed on the trunk, to be picked up as the rungs above reach them: conj(zw), |zw|, the equality of James's π with the chart's as rows (C); the base boundary `{A} ≐ ([b][A])`, number formats and place-value carry (James A.3, B.1 — `N`/`mult`); the complex log of a turn with a bounded variable (a `unit-interval` domain or the schema machinery); an independent J1 derivation of the phase rule; a cheaper branch-reading import than ℂ for the decree (moot once J1 lands).
