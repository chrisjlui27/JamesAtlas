# Legislation

The binding design decisions for the Boundary Chart, numbered as in the design questions of 2026-10-03. "Default" means Lui accepted the proposed default; his own words are quoted where he gave them. A later session changes a decision only by adding a dated amendment below it, never by editing the line.

**0. Continuity.** This chart framing supersedes the 2026-10-02 "game" framing. The game becomes a later skin over the same files (§12 of SPEC).

**1. Start.** At the void; the natural numbers are the first rung. A pile cannot be stated without void and `o`.

**2. The F₁ end.** One target node with three roads in: (a) finite sets / sphere spectrum as the trunk; (b) Borger λ-rings and (c) Connes–Consani as planned roads. Lui: "Uncertain. Default as the path with an eye to expand the expressibility of the other ways." Implementation: (b) and (c) are readings on every trunk node before they are nodes; no trunk node is settled with blank (b)/(c) cells.

**3. Loop.** Yes: a DAG with exactly one marked re-entry edge, `F1.arithmetic → void.page`, carrying the chart's largest gap.

**4. Node types.** Primitive, Axiom, Definition, Theorem, Decree, Import, Gap — all seven are steps; type is colour and price. Most steps will be theorems.

**5. Granularity.** One law per node. Concepts are a second index pointing at the laws that express them.

**6. Back-links.** Mechanical: exactly the rules cited in the Given–Rule derivation; checkable by the engine. Curated relevance is a separate `see_also` field.

**7. Display.** Raw forms beside named units beside standard notation; the equality in force is recorded on every node.

**8. Settings.** An attribute (a per-setting `holds` table), not a branch. An extension is itself a node; a setting is a named set of nodes.

**9. Bricken.** James 1993 is the ground truth for the classical setting. Bricken's constructs enter as attributed notes tagged by volume, and as nodes only where they add a law.

**10. Notation.** Canonical strings in `( ) [ ] < >` for machines; rendering shows `o` / `□` / mirror or drawn boundaries.

**11. Price.** Computed from the links, never hand-entered: the non-derivable ancestors (primitives, axioms, decrees, imports), split into the base three-and-three and the extras.

**12. Status.** One enum: NATIVE, NATIVE-BY-DECREE, IMPORTED, ANALOGY, CONJECTURE, REFUTED, ABSENT. Separate verification tier (none / hand / engine / numeric / lean). Separate `known_since` (the mathematics) and `entered` (the program).

**13. Two kinds of gap.** Concept-without-form and form-without-reading. A mechanical census of all small forms is part of the chart.

**14. Gap plans.** Fields: candidate form; law(s) to add and their type; nativity criterion; refutation test; owner thread. A new primitive is allowed but ranks last.

**15. Refuted readings.** Kept, struck through, attached to the law they were mistaken for; collected into one searchable list.

**16. Scope for v1.** A (number and algebra) and B (analysis) in full; D (structure) as far as the F₁ road needs; C (logic) as one strand; E (The Field) as pointers.

**17. Induction.** A named gap, the first the reader meets. Lui: "Meta-moves may wind up being necessary. The moduli-stack is a sort of meta-primitive idea that decomposes into 'readings' in the calculus is my sort of understanding. Start with the named gap." Implementation: a `level: meta` on nodes; `readings` as a first-class table; gap plans carry a `meta-move?` field.

**18. Order.** Dependency order is the spine; rungs (number systems) are the chapters; every node carries a shape-led / need-led tag.

**19. Trunk.** The 𝕁₁ road is the trunk; the adelic page is the second road into F₁; the division-algebra branch rejoins at 24, marked ANALOGY.

**20. Verification.** Lui: "I was originally just wanting to remove the Lean portion. I think we can have (c) as the core option, with (b) as a later scoped expansion to make everything legible in that setting." So: the rewrite engine, fixture corpus, `jadic.js` and the receipt prover carry verification now; Lean is a later scoped expansion over the classical trunk, with node ids chosen to become declaration names without renaming.

**21. Process.** Propose → refute → repair with an independent referee, per rung; nodes written to be picked up cold; "Exact" withheld until engine-verified.

**22. Source of truth.** One Markdown file per node in a repository. Lui: "if I have to set up something for this to be workable, let's set it up." A git repository (`boundary-chart`) with a checker and a generator; Obsidian-compatible links.

**23. Visual.** v1: forms drawn from canonical strings, and the chart as a zoomable DAG. v2: a live instrument per law, scoped node by node. The game, if it survives, is a skin.

**24. Audience.** Lui: "Mainly me. Essentially, the goal is to see how much of this exists AND to use it to walk the line and educate myself on the concepts I don't understand yet in the language I have already in my command, the earlier nodes confirming this understanding for me in house. Secondly, if I can use it to teach myself to understand, then I could use it to teach someone else to understand." Implementation: a required one-sentence Plain statement and a Confirms section on every node; a personal `understood` tracker rendered as walk progress; K–12 band visible.

**25. Seeding.** A fresh uniform walk for the trunk to ℂ, then backfill of the branches from the existing ledgers with their ids kept as aliases; the graded K–12 band visible on every node.

**26. Pilot.** Spec plus a pilot of the first rungs so the schema meets real forms before the trunk is walked. The pilot delivered 2026-10-03 covers `void`, `N`, `Z`, and the opening of `mult`.

---

**Amendment A1 (2026-10-03, proposed by the session, pending Lui's confirmation).** The classical setting carries two decrees from rung `mult` on: the undefined forms (`<□>` and `[□]` excluded, up to ≐) and the seam discipline (a unit step `[(X)] ≐ X`, in either orientation, only on content inside the principal strip or in an absorbing position). Both were forced by referee passes that collapsed the unrestricted theory with laws already on the chart. The seam discipline is stated in the ℂ reading — an import inside the classical setting — because no syntactic signature of off-strip content exists (`mult.seam-signature`). If Lui prefers James's own formulation (name J first, then state the J-discipline at rung C), the decree node moves to rung C and the sign laws that cross the seam move with it.

**Amendment A2 (2026-10-03, proposed by the session after the rung-C referee pass, pending Lui's confirmation).** `NATIVE-BY-DECREE` is reserved for statements that hold because a decree was issued (exclusions, the decrees, the meta theorems about the decree-governed calculus). A node whose derivation passes through a unit step that the seam decree adjudicates stays `NATIVE` and declares `guarded_by: [mult.seam-decree]`, which the checker computes from the derivation: *by content* when the step is at a non-absorbing position (the ℂ reading certifies the content is on the strip), *by position* when the step is absorbing but its content leaves the strip for some value of the domain (a seam step). An absorbing on-strip step is free, and so is a unit step on void or hole content (`[(void)] ≐ void`, `[(□)] ≐ □` are theorems of the hole rules, not instances of the decree). Price inherits guards through `uses`, so descendants are not re-tagged. Reason: the previous convention priced identical steps differently in rungs Q and C (the referee's BLOCKER), left absorbing seam steps unpriced, and called exact identities of ℂ "by decree". Reversing this amendment means restoring `NATIVE-BY-DECREE` on `Q.reciprocal-of-negative`, `Q.negative-denominator`, `Q.negatives-cancel` and the four rung-C laws now guarded by position, and narrowing `check_guarded_by` to the content clause.

**Note (2026-10-03).** The thesis — J. M. James, *A Calculus of Number Based on Spatial Forms*, M.S. thesis, University of Washington, 1993 — is in `references/` and is the ground truth for the `classical` setting. Its chapter plan is: 3 Boundary Mathematics; 4 Instance and Abstract (two-boundary calculus, N, cardinality, dominion); 5 Inverse (three-boundary calculus, Z, Q, division by zero, negative and fractional cardinality); 6 Phase (J, phase independence, J cancellation, multiple value and the two constraints, exp/log, e, π, trigonometry); 7 Future work (incl. boundary differentiation, Table 7.1); Appendix A conversion and formulas; Appendix B examples (base multiplication with carry, √9, fractions, (a+b)(a−b), the quadratic formula). Earlier citations to "Chapter 4/5" for the phase material were wrong and have been corrected to Chapter 6 with page numbers.
