# The Boundary Chart — Specification v1.0

*A step-by-step exposition of mathematics in James boundary arithmetic, from the void to F₁, as a searchable chart of laws; the data model behind a future visual encyclopedia.*

Status: **binding** where it records a decision from `LEGISLATION.md`; **proposed** elsewhere (marked). Written 2026-10-03 for Lui; meant to be picked up cold by a later session.

---

## 0. What this is

The chart is a directed graph of **laws**. Every node is one law of boundary arithmetic — a primitive that licenses forms, an axiom that adds an equation, a definition that abbreviates, a theorem that settles, a decree that legislates, an import that borrows, or a gap that names what cannot yet be written. Every node carries a derivation whose licensing rules are earlier nodes, so the back-links are mechanical, not editorial. The graph has one spine (the trunk from the void to F₁), branches (the extensions), and exactly one marked **re-entry edge** from the last node back to the first: F₁ arithmetic re-reads the natural numbers, so the exposition closes on itself.

Three uses, in order of priority (LEGISLATION 24):

1. **Inventory.** How much of mathematics is already expressible in the three boundaries, at what price, and where the holes are.
2. **The walk.** Lui walks the chart in order; the early nodes confirm, in a notation he already commands, what he knows; the later nodes teach him what he doesn't yet. Every node therefore states, in one plain sentence, the ordinary mathematical fact it is the boundary version of.
3. **Teaching.** Having learned by the walk, teach by the same walk. The K–12 band is visible on every node; the game and the live instruments are later skins over the same files.

The chart is **not** a book. It is the data a book, a game, or an encyclopedia is generated from. Prose lives in nodes and concept files; everything else is computed.

### 0.1 The two ends

- **Start: the void.** The first node is the empty page. The natural numbers are the first rung, not the first node, because a pile cannot be stated without void and `o` (LEGISLATION 1).
- **End: F₁.** One target node, *F₁ arithmetic*, with three roads into it (LEGISLATION 2):
  - **(a) finite sets / sphere spectrum** — `( )` and `[ ]` read as finite sets, `< >` as group completion (Barratt–Priddy–Quillen). *The trunk*, because here the boundaries are themselves the F₁ objects rather than a translation of them.
  - **(b) Borger's λ-rings** — ψ-operations as the whole structure; the nearest relative of the ψ-wall. A planned road: each law on the trunk records whether it has a ψ-reading.
  - **(c) Connes–Consani** — hyperrings, Witt vectors, the arithmetic site; the declared-void pile of the place calculus is the on-ramp. A planned road.
  Roads (b) and (c) are built as *readings* (§4) first and as nodes only where a law is gained. "With an eye to expand the expressibility of the other ways" means: no trunk node is accepted as *settled* until its (b) and (c) reading cells are at least filled with `ABSENT` or `PARTIAL` rather than left blank.
- **The re-entry edge.** `F1.arithmetic → void.page` (one edge, flagged `reentry: true`). It is the chart's largest gap and is drawn differently. The DAG check exempts exactly this edge.

---

## 1. Vocabulary

| term | meaning here |
|---|---|
| **form** | a finite multiset of boundaries, each containing a form; the void is the empty form |
| **boundary** | one of `( )` round/instance, `[ ]` square/abstract, `< >` angle/inverse — plus any later primitive (ordered bracket `[ ; ]`, extrusion brace `{ }`, lens `{n }`) |
| **medium** | the page: juxtaposition is an unordered multiset with the void as unit. Medium facts are laws of type `primitive` with `kind: medium` |
| **law** | one equation `lhs ≐ rhs` between forms (object level), or one statement about the calculus (meta level: freeness, independence, induction) |
| **node** | one law, one file, one id |
| **rung** | a chapter of the walk — usually a number system (`N`, `Z`, `Q`, `C`…), sometimes the arrival of a boundary (`mult` = the square boundary) |
| **setting** | a named set of nodes in force: `classical` (James 1993), `J1`, `JH`, `JO`, `JS`, `JP`, `extrusion`, `field` |
| **reading** | an interpretation of forms: `C` (complex numbers, the default gloss), `finset` (finite sets / F₁), `lambda` (Borger), `CC` (Connes–Consani), `logic` (LoF / EG) |
| **receipt** | in `J1` and later: the Λ-valued record of what a non-strict step dropped |
| **price** | the set of non-derivable ancestors of a node (primitives, axioms, decrees, imports) — computed, never typed |
| **gap** | a node of type `gap`: a concept with no form, or a form with no reading |
| **walk** | the linear order in which the chart is read; a total order refining the dependency DAG. Rung order (LEGISLATION 29): `void N Z mult Q alg C` · `schema` · `J1` · `place` · `H` · `analysis` · `J2` · `logic` `struct` · `F1`; `O`, `S` are a branch |
| **schema** | a node whose law carries a count parameter (`n`, and optionally `k`); the engine instantiates it over a declared range and checks every instance; its derivation is an induction step (LEGISLATION 29) |

Equality symbols, as used across the program: `≐` strict convertibility in the classical calculus; `≡` syntactic (strict) in `J1`; `≃` witnessed (receipt-bearing); `≈` evaluated. Each node declares which is in force (`equality:` field).

---

## 2. The node

### 2.1 One file per node

Path: `nodes/<id>.md`, where `id = <rung>.<slug>`, e.g. `nodes/Z.collection.md`. Ids are stable; slugs are lowercase, hyphenated, never renamed once published (rename = new node + alias). Obsidian-style links `[[Z.collection]]` are the only link syntax, so an Obsidian vault opened on `nodes/` shows the chart as its graph view on day one.

### 2.2 Types

| type | verb | what the node adds | counts toward price |
|---|---|---|---|
| `primitive` | *licenses* | a new way to form a form (a boundary) or a fact of the medium | yes |
| `axiom` | ***adds*** | an equation the calculus did not have | yes |
| `definition` | *reduces* | a name for a form built from existing ones (sugar; no new law of the calculus) | no |
| `theorem` | **settles** | an equation (or meta-statement) the calculus already contained | no |
| `decree` | ***legislates*** | a rule imposed from outside the equational base: an exclusion (`<□>` is not a form), a discipline (J-cancellation only inside an instance, last), a declared-void pile, a guard | yes |
| `import` | borrows | a fact used but not derived (a theorem of ordinary mathematics, a labelling, a count) | yes |
| `gap` | *names* | a concept without a form, or a form without a reading, with a plan | no (it has no derivation) |
| `schema` | **settles** up to the range | a theorem with a count parameter, stated as a template, checked at every value in a declared range and derived by an induction step (§2.7); the passage to all n is the gap | no — but its hypothesis row cites the gap `N.induction`, which is |

Every type is a step of the walk (LEGISLATION 4). The type is the node's colour in every rendering.

A node also has a **level**: `object` (an equation between forms) or `meta` (a statement about the calculus: consistency, freeness, independence, normalization, induction). Meta-level nodes are where the "meta-moves" of LEGISLATION 17 live; they are first-class so the chart can show where the calculus had to be looked at from outside.

### 2.3 Front matter (required unless marked optional)

```yaml
---
id: Z.collection
title: Inverse collection
type: theorem                 # primitive | axiom | definition | theorem | decree | import | gap | schema
level: object                 # object | meta
kind: law                     # primitive: boundary | medium ; decree: exclusion | discipline | declaration | guard ; theorem/axiom/definition: law | instance (one value of a family over n) ; gap: concept | form
rung: Z
order: 230                    # walk order; integers with gaps of 10 so nodes can be inserted
setting: classical            # the setting the law is stated in
equality: "≐"                 # ≐ | ≡ | ≃ | ≈
domain: real                  # variables range over: natural | positive | real | complex (for the shadow check)
law: "<A><B> ≐ <A B>"         # canonical string; for definitions "name := form"; for gaps a one-line statement of what is missing
units: "−a + −b = −(a + b)"   # the law in standard notation (the ℂ reading)
gloss_check: "-A + -B == -(A+B)"   # optional: a Python expression the checker evaluates against the form's value
schema_range: "n=2..8"        # schema nodes only: the instances the engine checks ("n=1..6; k=1..n" for two parameters)
schema_draw: "n=3"            # schema nodes only, optional: the instance the card draws (default n=3; k=1)
holds:                        # settings table: holds | holds-mod-Λ | guarded | replaced | fails | untested
  classical: holds
  J1: holds
  JH: holds
readings:                     # readings table: EXACT | PARTIAL | ANALOGY | ABSENT | CONVERSE | untested
  C: EXACT
  finset: ABSENT              # no negatives in finite sets — group completion is exactly what <> adds
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE                # NATIVE | NATIVE-BY-SCHEMA | NATIVE-BY-DECREE | IMPORTED | ANALOGY | CONJECTURE | REFUTED | ABSENT
verified: engine              # none | hand | engine | numeric | lean
known_since: "1993 (James); the arithmetic fact is ancient"
entered: 2026-10-03
guide: shape-led              # shape-led | need-led
band: "1–2"                   # K–12 band: K | 1–2 | 3–5 | 6–8 | 9–12 | beyond
uses: [Z.inversion, void.space]   # mechanical: must equal the set of rules cited in the derivation
see_also: [M.inverse-promotion]   # curated
aliases: []                   # ids in the existing ledgers (JO-n, JS-n, JP-n, JH-n, Field) and other names
concepts: [negation, addition]
guarded_by: []                # mechanical: [mult.seam-decree] iff the derivation relies on a clause of the decree — by content (a unit step at a non-absorbing position) or by position (an absorbing seam step); §5.4. Feeds the price
understood: no                # personal tracker: no | partial | yes
understood_note: ""           # optional
reentry: false                # true only on the one re-entry edge's source node
---
```

Field rules:

- `uses` is **mechanical**: the checker computes the set of `[[id]]` cited in the Derivation section and fails the node if `uses` differs. Hand-chosen relevance goes in `see_also`.
- `holds` is per **setting**; `readings` is per **reading**. Both are small tables, not branches (LEGISLATION 8). A setting that doesn't exist yet in the chart is still a legal column (`untested`).
- `status` describes the law's standing in the program; `verified` describes how it was checked; `known_since` is the mathematics' date; `entered` is the program's date (LEGISLATION 12). Four separate things.
- `band` is the K–12 band from the Iconic Mathematics scope and sequence (additive-first order: void → instance → inverse (additive) → abstract → inverse+abstract → J → functional), or `beyond`. Visible in v1, unfilled where unsure (LEGISLATION 25).
- `understood` is Lui's, is never used in verification, and is rendered as a progress bar over the walk.

### 2.4 Body sections (in this order; `##` headings; a section may say `none`)

1. **Law** — the law displayed three ways, side by side: raw form · named units (`o`, `□`, `J`, `ω`, `i`) · standard notation. The generator draws the forms from the canonical string; the file holds the strings.
2. **Plain** — one sentence a ninth-grader could read, stating the ordinary fact this is the boundary version of. Required on every node (LEGISLATION 24).
3. **Derivation** — a Given–Rule table in Book One's style:

   ```
   | form | rule | note |
   |---|---|---|
   | <A><B> | given | |
   | <A><B> A B <A B> | [[Z.inversion]] | create the pair (A B)<A B> |
   | <A B> | [[Z.inversion]] | cancel A<A> and B<B> |
   ```
   Allowed rules: `given`, `[[id]]` (one or more), `medium` (rearrangement in space — must also cite `[[void.space]]` once in the table), `substitution` (replacing a variable by a form), `congruence` (applying the same operation to both sides), `definition` (unfolding a definition — cite it), `name` (a row that merely names the previous form in standard notation, e.g. `A × B`; not a form, not checked), `lemma` (an equation proved by an earlier table of the same node, used right to left), `hypothesis` (schema nodes only: the schema's own law at a smaller parameter — the note cites `[[N.induction]]`; §2.7). Axioms, primitives, decrees and imports write `none — adjoined` and cite in prose the nodes their statement is built from — those citations are their `uses`. Gaps write `none — gap`. Meta-level nodes use a `| statement | rule | note |` table instead: prose steps, each citing the laws it leans on, plus a `witness:` script in the front matter where a computation carries the proof.
   The engine evaluates every consecutive pair of forms on random values and fails the node if any step is not an equality in the declared sense; for an object-level theorem it also requires the tables to start at one side of the law and end at the other, as forms. Since 2026-10-04 it also checks that **the cited rule licenses the step**: the derivation checker (`tools/prover.py`, run by `check.py`) rewrites the previous form by the cited laws — each law as a rewrite in either orientation, at any position, variables matching sub-multisets — and must reach the next form in at most fourteen applications (one row may say "the counit, twice" or "Distribution n − 1 times"); a numerically true step with the wrong rule fails. Laws linked in the note cell count as cited. `given` may only open a table — a chain cannot restart — and the endpoint check asks that *one* table run from one side of the law to the other, as forms (a lemma table proves an equation a later table uses and contributes no endpoint). What the engine still does not check: that a note *describes* the step correctly, that the derivation is the intended one, or anything about the prose — that remains the referee's job (§10).
4. **Confirms** — the standard-notation fact (with its usual name) that this law *is*, and what it is **not** (where a naive reading overreaches). This is the "in-house confirmation" line for the walk.
5. **Settings and readings** — the two tables from the front matter, with one-line justifications for any cell that is not `holds`/`EXACT`.
6. **Refuted readings** — ~~struck through~~ readings or derivations once believed and since refuted, each with the date and the refuting witness (LEGISLATION 15). `none` is a legal entry.
7. **Notes** — anything else: Bricken's variant (attributed by volume), history, the thread that owns it.
8. **Plan** — gaps only (§6.3).

Price and used-by are **not** written in the file; the generator computes and renders them.

### 2.5 Canonical strings

- Boundaries: `( )`, `[ ]`, `< >`. Later primitives: `[ ; ]` ordered bracket (JH), `{ }` brace (extrusion), `{n }` lens (JP). Whitespace is ignored.
- Sugar accepted by the parser and expanded before checking: `o` = `()`, `□` = `[]`, `J` = `[<o>]`, `ω` = `[()]` (the period form, rung `J1`; the cube root of unity that rung `C`'s prose also calls ω is never written as a canonical string, so the two do not collide), `void` = the empty form. Numerals `n` are **not** sugar in canonical strings (write the pile) except inside `[[...]]` prose.
- Variables: single capital letters `A`–`Z`, optionally followed by a digit. The checker instantiates them on random values of the node's domain (the shadow check). A node whose law is one value of a family over n (`A A ≐ ([A][oo])`, the pile `ooo`) is marked `kind: instance`; the family itself, when the chart states it, is a `schema` node (§2.7).
- Repetition over a count ("n copies") is a `schema` node (§2.7), whose canonical strings are templates in `X^{e}` / `Σ{…}` notation; an object law writes its small instance out in full (`A A`, `J J`), never a superscript.

### 2.6 Rendering conventions (generator)

Canonical strings are drawn as nested boundaries: round → rounded capsule, square → rectangle, angle → hexagon with pointed sides. Beside the drawing: the ASCII string, the units form, the standard form. Type = colour; status = badge; verified = badge; band = small tag. Refuted content is struck through. House typographic notation in prose: *italic* for a reduction (an emptying), ***bold-italic*** for an emergent operation, **bold** for a settled one, ~~strikethrough~~ for wrong, "scare-quotes" to hold a term at arm's length.

---

### 2.7 Schema nodes (LEGISLATION 29)

A `type: schema` node states a law for every value of a count parameter. The law and the derivation rows are **templates**:

- `X^{e}` — e juxtaposed copies of X, where X is a variable, `o`, `J`, `□`, or a bracketed group, and e is an expression in the parameters (`n`, `k`, `n-1`, `2k`, `2k+1`, `n+1`); `o^{n}` is the pile n.
- `Σ{j=a..b: F}` — the juxtaposition of F for j = a, …, b, with counts `^{…j…}` inside F (an empty range, b = a − 1, is void).
- `schema_range:` in the front matter, e.g. `n=2..8` or `n=2..7; k=1..n-1`, gives the instances the engine checks. A derivation table whose header reads `| form (n = 1) | rule | note |` (any parameter, any value) is a **base case**; the other tables are the **step**. An instance at a base value consists of the base table alone; an instance at any other value consists of the step tables alone — so a `hypothesis` row always points at a value already checked, and the range may not start below the base.
- The step may cite the schema itself at a smaller parameter with the rule `hypothesis`, and that row cites `[[N.induction]]` in its note, which puts the gap in `uses` and so in the price. A schema with a `hypothesis` row must have a base case at the minimum of its range; a schema without one (one that reduces to earlier schemas, as the roots of unity reduce to cardinality) needs no base.
- What the engine checks, per instance: the law shadow, every consecutive pair of rows as an equality in ℂ, the seam decree on every row (with `guarded_by` the union over instances), and the endpoints — the first row is the instantiated law's left side and the last its right side *as forms*, not merely in value. For a `hypothesis` row it checks, syntactically, that the row is obtained from the previous one by one application, in either direction, of the schema's own law at a smaller parameter in range (any smaller one — strong induction — with the variables kept as written, so a hypothesis applied under a substitution is a `substitution` row first and a `hypothesis` row after). What it does **not** check: that any other cited rule licenses its step (the referee's job, as everywhere), and the passage to all n — that is the gap, and it is priced. So a schema is verified *up to the range* and no further; that is what `NATIVE-BY-SCHEMA` records. Cards draw one instance (n = 3 by default, `schema_draw:`) and show the template beneath it; each derivation table is captioned with the values it is drawn at.
- Only canonical cells are expanded: the `law:` string and the form column of a derivation table. Rule and note cells and the prose of the section are kept as written, so a note may say `a^{n−1}` or ω^{n+1} without being a template. A row whose instance coincides with the row before it (the pile n *is* the pile n − 1 beside a unit) is legal and says so in its note.
- **Schemas over the place (rung `place`; proposed, pending LEGISLATION 31).** The parameter `p` is the place: `o^{p}` is the prime as a pile, `[o^{p}]` its log, and the range is an explicit list, `p=2,3,5,7,13`, which may be joined with a depth, `p=2,3; n=1..3`, or given as tuples where the depths differ by place, `(p,n)=(2,2),(2,3),(3,1),(3,2),(3,3)`. Expressions may use `**` (`o^{p**n}`, `o^{(p-1)*p**(n-1)}`). The engine reads each instance *at its own place* (SPEC §4.4), to the depth n when the range has one. The price of the meta-move "at every place" is the import [[place.ostrowski]]: **every** node whose range binds p cites it in `uses` — a schema over p as a schema over n cites [[N.induction]] (resting on another schema does not stand in for it) — and the import names the places without licensing the passage from the five the engine reads at to all of them, exactly as the induction gap is the price of the passage from a range to all n. A `decree` may be written over p and n too (the void pile, `o^{p**n} ≃ void`): its declared equation is then checked at every instance, and it acts as a rule at each, but it has no derivation and earns no tape; an `import` may be too (Fermat–Euler), checked at every instance of its range and priced as an import.

---

## 3. Links

- **Back-links** (`uses`) are exactly the rules cited in the derivation. They are the chart's edges. A node may cite a node of a later rung only if that node's `order` is smaller — the walk order, not the rung, is what the DAG check enforces, so cross-rung dependencies (Dominion needs Inversion) are legal and visible.
- **Used-by** is computed.
- **See-also** is curated and drawn dashed.
- **Aliases** map ledger ids (JO-12, JS-39, JP-1, JH-3, Field prohibitions) onto nodes so the existing work is reachable by its old names (LEGISLATION 25).
- **Concepts** form the second index: `concepts/<slug>.md` holds a one-paragraph plain description; the generator lists under each concept every node that names it. "Square root" resolves to its concept page, which resolves to the forms and the laws (LEGISLATION 5).

---

## 4. Settings and readings

### 4.1 Settings are attributes, not branches (LEGISLATION 8)

A **setting** is a named set of nodes in force. A calculus extension is itself a node (a new axiom or primitive), and the setting is the set that includes it:

| setting | = classical ∪ … | source |
|---|---|---|
| `classical` | three boundaries, Involution, Distribution, Inversion, and two decrees: the undefined forms (`<□>`, `[□]`) and the seam discipline (of which James's J-discipline is a special case — `C.james-discipline`; stated in the ℂ reading because no syntactic signature exists — `mult.seam-signature`) | James 1993; Book One Part I–II; `mult.hole-exclusion`, `mult.seam-decree` |
| `J1` | Involution split: the counit `([A]) ≡ A` strict (`J1.counit`), the unit `[(A)] ≃ A` witnessed by a receipt (`J1.unit`); the period form ω := `[()]` kept rather than erased; the period `(ω) ≡ ()` and absorption `(ω A) ≃ (A)` are theorems (strict; absorbed); L0 linearity (`J1.linearity`, decree); the pole read by polarity (`J1.pole`, decree); the ψ-wall (`J1.psi-wall`, decree) with von Staudt–Clausen as its one import. Three equalities: ≡ strict, ≃ witnessed, ≈ evaluated (LEGISLATION 30) | Number at Height One (2026-07-21), 𝕁 v3.1 Linearity (2026-08-09), the page-logic legislation (2026-08-22), LEGISLATION 30 |
| `JH` | + ordered bracket `[ ; ]`, seed `J_j`, O9, OC, seam guard on Involution-down | JH Exposition Guide |
| `JO` | + tree nesting, priced receipts, alternator | Book One Part IV |
| `JS` | + fourth doubling, octave grade | JS-algebra-sedenionic |
| `JP` | the enriched calculus read at a finite place: the void pile `o^{p**n} ≃ void` declares the page (`place.void-pile`, a decree over p and n), the reading at p (`place.reading`: the log space ℤ_p ⊕ ℚ[p] ⊕ ℚJ_p, the radius of the instance, the selection of the fractions of the period, no reciprocal of the prime, the log of exactly one as the place's period ω_p), and the discipline of the page — the page's equality does not pass through a square, so a law of the page is ≃ and a page step is graded by position (§5.5); the lens and the completion are the rung's gap. *Proposed, pending LEGISLATION 31* | Part II: Calculus of Number at a Place; rung `place` (2026-10-06) |
| `extrusion` | + brace `{ }`, gauge principle G0 | 𝕁 v3.2 |
| `field` | + ι or κ adjunction, boost seed | The Field, Vol. I |

Every law carries a `holds` cell for each setting: `holds` · `holds-mod-Λ` · `guarded` (holds under a named guard) · `replaced` (a more general law restricts back to it) · `fails` · `untested`. The three-way dominion check (classical holds / spectral fails / J1 deferred) is the template.

### 4.2 Readings

A **reading** is a model. The default gloss is `C`. The F₁ roads enter as readings first: `finset` (trunk road), `lambda` (Borger), `CC` (Connes–Consani); `logic` covers LoF/Existential-Graphs. Cells: `EXACT` · `PARTIAL` · `ANALOGY` · `ABSENT` · `CONVERSE` · `untested` — the five-word verdict vocabulary from the page-logic ledger, plus `untested`.

Readings are how the moduli-stack idea (LEGISLATION 17) enters the chart without a new primitive: a form is one thing; its readings are the points of its moduli; a law that holds in every reading is the stable part, and a law that holds in only one is the chart's way of saying where a reading is doing work the calculus is not.

### 4.3 Bricken (LEGISLATION 9)

James 1993 is the ground truth for `classical` (the thesis is in `references/james-1993-calculus-of-number.pdf`; its page numbers are cited in `known_since` and Notes). Bricken's constructs (`[[ ]]` as complex infinity, unit-ensemble presentations, parallel forms) enter as **attributed notes** inside the node they vary, tagged by volume (*Iconic Arithmetic* I/II/III), and become nodes only where they add a law James does not have.

### 4.4 The place ledger (computed; rung `place`; proposed, pending LEGISLATION 31)

The chart reads every law at the finite places p = 2, 3, 5, 7, 13 (`tools/place.py`, `tools/placeledger.py`) and writes `census/place-ledger.md`. The reading at p is the 𝕁₁ reading moved to a finite place: a value is a number part (a residue of the page, mod p^n — the void pile), a count of the prime's log `[p]` and a count of the torsion log J_p; `[ ]` splits a number into the three and `( )` reassembles them where it can — the number part on the radius p·ℤ_p (4ℤ_2), the counts whole. Five conventions (`place.reading`): the log of *exactly one* reads the place's period ω_p = (p−1)·J_p (2·J_2 at 2), every other log principal (LEGISLATION 30b at p); a fraction of a torsion count is taken in 0 … p−2 (0, 1 at 2) — the *principal root* of the place, canonical on the principal units and a convention elsewhere; the generator of the torsion is the Teichmüller lift of the least primitive root (−1 at 2), a convention like the choice of 2πi over −2πi; a formal element's log is a formal symbol that a count scales, and the product of two formal elements has no value (weight 2); counts scale formal elements only when exact. Counts are carried exactly beside the residues. **Depth and precision.** The page's depth n is what equality is mod; the engine's working precision N ≥ n is what the arithmetic is carried to (the ledger reads at the default N, where the two coincide; the rung's own schemas read at their depth n with N above it), and "exactly one" is decided at N — so a 1-unit ≡ 1 mod p^n but not mod p^N has the log of a 1-unit, not the period. The equality at depth n is coarser than at N and the values are the same, so a law exact at N is exact at every smaller depth, and a receipt void at N is void there: the ledger at N is the strongest statement, and the referee's depth-1…3 runs (2026-10-06, after the repair) find no law that holds at N and fails at a smaller depth.

**The discipline of the page (LEGISLATION 31(g)).** The page's equality — agreement mod p^n — passes through juxtaposition, angles and instances, not through a square: `[o^{p**n}]` is n·[p], `[void]` is the pole, and the log of a non-unit loses as many shells as its count of `[p]`. The laws of the page — the void pile and what follows from it by the page's equality alone (residues, minus one as a pile, Fermat–Euler, division by a unit, the prime power, the geometric doll) — are written ≃, and the receipt prover grades a page step by position (§5.5): `page` at depth 0 or inside an instance; under a square it is measured at the first square above it. Without the discipline the page collapses (`o^{5} ≐ void` at p = 5, depth 2, by the void pile under the exponent's square). The pole is the limit end of the count of `[p]` — no finite count is it; the instance of n·[p] is the void pile at depth n (`place.prime-power`, `place.two-ends`).

**The domains at a place.** `natural` — a small count; `positive` — a principal unit, now and then times p or p², and a fifth of the time a *fraction* of principal units (so that a count that is not whole is sampled: the laws that hold for integer turns only are told apart) — the place's image of the positive reals, the sector where the log is single-valued and the receipts are void; `negative` — minus a principal unit; `real` — either; `unit` — any unit of the page; `complex` and the rest — any residue, with the natural share of multiples of p. The radius is the *standing proviso* of every instance at a finite place: a sample whose instance content falls outside it is retried on the radius (every variable times p, 4 at 2), and if it is still outside, the form has no value at p for that sample — it counts as formless, exactly as a sample that is not a form for a *selection* reason does (a fraction of the period that is not a form at p, the reciprocal of the prime, weight 2; at 2 a unit ≡ 5 mod 8 has no root, and the root form's content is outside the radius there). A sample past the engine's working precision is dropped unjudged — a limit of the engine, not of the place. The exceptional points are probed by domain as at ∞ — a variable exactly one, and minus one for a negative or real variable — on the lattice point itself (no retry), and a failure there is marked `·exc`, as the tape names the exceptional points at ∞.

**Per place** the ledger records the law — `exact` (as stated on every generic sample), `mod-Λ` (a strict law holding only mod ω_p), `guarded` (holds where its forms exist; some sample is not a form), `none` (no sample is a form), `fails` — and the derivation's **tape**: the licensed path found at ∞ re-graded with the place's receipts (strict, absorbed, posted, import, absent), so that "the same wall at every place" is checked by the same prover; a step whose content is formless at p is `absent` there with receipt `?` (the step is not false at p — it has no value there — and the cell reads `fails` only when the law itself is a form somewhere). **The JP cell** these imply: `replaced` when the law is a form at no tested place (the hand cell names the place law that takes over — the radius, the void pile); `fails` when it fails somewhere it is a form, or its tape is absent; `guarded` when some instance somewhere is not a form, or the tape imports; else the tape's grade — strict, page or absorbed `holds`, posted `holds-mod-Λ` — or, for a node without a derivation, from the law alone. The hand cell may say more (`guarded` over `holds`, `replaced` over `fails`), never less, and `untested` is no longer legal where the ledger computes. The nodes of rung `place` are graded at their own place as they are checked, like 𝕁₁'s at ∞: the equality symbol and the JP cell follow the tape, and the rung's tapes are kept for the nodes after them (a page law cited under a square is measured there). A trunk theorem cited by a node of the rung is priced at its grade at ∞ (its grade at the place is computed afterwards, by the ledger). A path re-graded at p is the path found cheapest at ∞; a cheaper one may exist at p, so a tape at p can be too pessimistic, never too generous. `tools/check.py --only place.` grades the cited trunk theorems first, so that its tapes agree with the full run's.

---

## 5. Status, verification, dates, price

### 5.1 Status (one enum for the whole program; LEGISLATION 12)

| status | meaning |
|---|---|
| `NATIVE` | derived inside the setting from its own axioms; or a primitive/axiom of the base three |
| `NATIVE-BY-SCHEMA` | holds for every value of a count parameter by an induction the calculus cannot do natively: each instance in the declared range is engine-checked (base case at the base, step at every other value, the hypothesis row verified to be the law at a smaller parameter); the passage to all n is not checked, and the induction gap `N.induction` is in the price |
| `NATIVE-BY-DECREE` | the *statement* holds because a decree was issued — exclusions (`a/0 is not a form`), the decrees themselves, and the meta theorems about the decree-governed calculus (consistency; James's rules sitting inside the decree). A node whose *derivation* merely passes through a guarded unit step stays `NATIVE` and declares `guarded_by` (§5.4, Amendment A2) |
| `IMPORTED` | used, not derived; the import is named and dated |
| `ANALOGY` | a correspondence asserted but not an equation of forms (e.g. 24 ↔ ν) |
| `CONJECTURE` | stated, unrefuted, undemonstrated |
| `REFUTED` | shown false; kept, struck through, attached to the law it was mistaken for |
| `ABSENT` | the concept has no form (gaps) |

Mapping from the old ledgers (recorded in `aliases`/`notes`, never silently): EXACT→`NATIVE` (with reading EXACT); PARTIAL→`NATIVE` with a `PARTIAL` reading cell or `IMPORTED`; IMPORTED→`IMPORTED`; emerged→`NATIVE`; CONJECTURE/REFUTED unchanged; ANALOGY/ABSENT/CONVERSE live in reading cells.

### 5.2 Verification tier

`none` → `hand` (a written derivation, or a meta argument with no script) → `engine` (every derivation step shadow-checked in the ℂ reading by `tools/check.py`, every step licensed by the rule it cites (`tools/prover.py`), and the tables shown to connect the law's two sides as forms; or a meta claim checked by a named `witness:` script in `tools/models/`) → `numeric` (high-precision numerical identity beyond the shadow check) → `lean` (a Lean declaration; node id = declaration name — later scoped expansion, LEGISLATION 20). A meta-level node without a witness script is at most `hand`, whatever its author believes.

**"Exact" is withheld until `engine`** (LEGISLATION 21): a node whose `verified` is `none` or `hand` renders with a hollow badge whatever its status says.

### 5.3 Two dates

`known_since` — when the mathematics was known (James 1993; "ancient"; Sagle 1961; "this chart, 2026" when nothing earlier is located — and then a literature check is a standing obligation). `entered` — when it entered the program.

### 5.4 Price (computed; LEGISLATION 11)

`price(n)` = the set of ancestors of `n` along `uses` whose type is `primitive`, `axiom`, `decree`, `import`, or `gap` (a schema cites the induction gap in its hypothesis row, so induction is priced), together with every `guarded_by` along the way (so a guard declared by an ancestor is inherited by price, never by re-declaring the field), partitioned into:

- **base**: the three boundaries, the medium, and James's three axioms;
- **extra**: everything else — further primitives, axioms, decrees, imports.

Rendered as "what it costs to write X": *i* costs nothing extra (fractional cardinality is a theorem schema); ℍ costs an ordered bracket + O9 + OC; ℤ_p costs the void-pile decree. The concept index shows the cheapest price among a concept's forms.

**`guarded_by` (Amendment A2).** A node declares `guarded_by: [mult.seam-decree]` exactly when its derivation *relies* on a clause of the seam decree, and the checker computes this from the derivation and enforces it both ways:

- **by content** — a unit step `[(X)] ↔ X` at a non-absorbing position: it is admitted only because X stays on the principal strip over the whole domain, which the ℂ reading certifies (e.g. `alg.log-law`, `C.log-of-negative`);
- **by position** — a unit step in an absorbing position whose content leaves the strip for some value of the domain (a *seam step*: the local equation `[(X)] ≐ X` is false there, and only the enclosing instance saves it — e.g. `Q.reciprocal-of-negative`, `C.period-absorption`);
- **free** — a unit step that is absorbing *and* on the strip relies on neither clause (the equation is true and the position is safe), as does any derivation with no unit step; and a unit step on **void or hole content** — `[(void)] ≐ void` (which is `[o] ≐ void`, `mult.log-of-one`) and `[(□)] ≐ □` (`mult.hole-instance` with `mult.black-hole`) — is exempt: the second is a theorem of the hole rules wherever it stands, and the first is exact in the classical reading (ln 1 = 0), which is the reading the decree is stated in. Without this clause the decree would enter the price of nearly every node through `[o] ≐ void`. (The exemption is classical: in 𝕁₁ the log of one is the receipt ω itself — §5.5 — which is why it is a node of its own.)

The card shows which clause. Status is unaffected: a guarded theorem is `NATIVE`. (The earlier convention, which made seam-step laws `NATIVE-BY-DECREE` and left absorbing seam steps unpriced, labelled exact identities of ℂ — `e^{a+2πi} = e^a` — "by decree" while leaving the half-true `ln(−a) = ln a + iπ` NATIVE; the C referee pass found four rung-C laws priced as if the decree did not exist, and the rule was changed.) One correction to the clause above, found by the receipt prover (§5.5): `[o] ≐ void` is not free in 𝕁₁ — it is the receipt ω — so it is a node of its own, `mult.log-of-one`; the classical exemption stands for the classical setting.

### 5.5 The 𝕁₁ tape (computed; LEGISLATION 30)

For every derivation, `check.py` asks the derivation checker (§2.4) for the cheapest licensed path in 𝕁₁ — strict steps only, then absorbed, then posted, then anything — and grades each step by the rule it used and the position it used it at (`tools/j1.py`):

- **strict** — the counit `([A]) ≡ A`, Distribution, Inversion, the medium, the hole rules; a theorem whose own tape is empty; and a unit step on *pole-valued* content (the pole has no winding to record: LEGISLATION 30f, refined 2026-10-06 — this is why Dominion is ≡);
- **absorbed** — the unit `[(A)] ↔ A`, absorption `(ω A) ↔ (A)`, or a theorem with posted receipts, applied *directly inside an instance, through angles at most*: the instance pays the receipt on the spot; value-exact; the receipt is recorded on the tape as paid. A theorem whose own receipts were all absorbed is also **absorbed** when reused, at any position: its reuse replays the paid moves, and a law that uses it is ≃, never ≡ (LEGISLATION 30a: absorption is a witnessed move);
- **posted** — a unit step, or a posted theorem, at depth 0 (through angles and juxtaposition only): the receipt stays on the tape; the two forms agree mod Λ;
- **import** — a unit step, or a posted theorem, under a square before any instance, whose receipt is void at the *generic* points of the node's domain. ≃ is not a congruence through `[ ]` (a lattice offset inside a log is not a lattice offset of the log), so the step is sound only by that fact of the reading — the classical decree's by-content clause — which 𝕁₁ cannot see. The reading has *exceptional points*: where a content is exactly one its log reads ω, and the receipt there can be non-void. The prover probes them (each variable at 1, −1, ½, 2, i within the domain, the others at 2 and at random, and all variables equal to one probe) and names on the tape, for up to three receipt values found at the probes, one point each (`except k = −1 at A=1, B=1`); the exceptional set is a locus, not a list — the law stays `guarded`, with the points stated — there the classical law is false in 𝕁₁'s reading;
- **fails** — the same with a receipt that is not void (the step is false in 𝕁₁), or a rule 𝕁₁ does not have.

A node's grade is its worst step; the `J1` cell it implies: strict or absorbed → `holds`; posted → `holds-mod-Λ`; import → `guarded`; fails → `fails`. The checker compares the computed cell with the hand-written one and fails the node on disagreement, allowing the hand cell to say *more* (a `guarded` by legislation over a computed `holds`, as for Inversion's stratification; a `replaced` that names what takes a failed law's place); `untested` is no longer a legal J1 cell for a graded derivation. For a node in `setting: J1` the equality symbol must be the one the tape earns — ≡ for strict, ≃ for absorbed or posted — and its own J1 cell must match. The result is `census/j1-ledger.md`, written by `check.py` and rendered on each card as its **𝕁₁ tape**.

**The reading and the receipt values.** Receipts are read in the 𝕁₁ reading (LEGISLATION 30b, amended 2026-10-06): the log of *exactly one* is the chosen lift ω = 2πi, every other log is principal. This is compositional — a square's value depends only on the value inside it — so the strict rules stay exact inside any context, which the literal convention ("the form `[()]` reads as 2πi") did not give (`[(o <o>)] → [()]` is Inversion, strict, and jumped 0 → 2πi under it). Consequences: `[()]`, `[(ω)]` and `[(J J)]` all read 2πi; `[(J J)] → J J` has receipt 0 and the crack's non-void receipt sits at the log of one, `[()] → void`, which is where the classical calculus actually erases the turn (`mult.log-of-one`). The **receipt of a step** is the lattice element the step forgets: value before minus value after, in units of ω, sampled over the node's domain; for a step between two instances the contents are compared (an absorbed period is invisible at the instance level and is exactly what the receipt records). A receipt is `?` when a sampled difference is not a lattice element, or a reused theorem's sides reach the pole (none on the current ledger); a unit step on pole-valued content is not `?` but `strict [pole]`. The tape records the position class and the sampled receipt values of every non-strict step; a step inherited from a theorem's own tape is marked `inherited`, naming the theorem (its k counts the periods the theorem's own derivation moved at content level, all paid where it is absorbed); a strict unit step on pole-valued content is marked `pole`, with no receipt.

**The tape at a place.** The receipt prover takes a reading as a parameter (`tools/j1.py`, `Reading`): the same grading runs at a finite place with that place's period, and the place ledger (§4.4) re-grades every licensed path there. One grade exists only at a place, between strict and absorbed — **page**: a step by a law of the page (the void pile and the laws derived from it by the page's equality alone; `PAGE_RULES` in `tools/j1.py`, and any theorem whose own tape carries a page step) applied at depth 0, through angles and juxtaposition, or inside an instance. The two forms agree mod p^n, which *is* the page's equality, but that equality is not a congruence through a square (§4.4), so a page step under a square is **measured at the first square above it** (`page_under_square`; the prover records that square's content before and after on the step): where the square's value does not change at the generic points of the domain, the step is an `import` (sound by content, as a unit step under a square is); where it changes by a lattice element, the square posts that receipt and *the square's own position* grades the step — `absorbed` directly inside an instance, `posted` at depth 0; otherwise `absent`. The exceptional points are probed as at ∞. A page law is ≃ (its JP cell `holds`), and page, like absorption, is never promoted to ≡ by reuse. The same measurement would be sound for a unit step under a square at ∞ (a square whose value changes by kω, directly inside an instance, is absorbed there); it is not applied to the trunk, whose tapes stand as graded, and is recorded as a proposal (LEGISLATION 31(g)).

**What the tape does not do.** Receipts are *sampled*: 24 random points of the node's domain and the probe points above; a value the sampler never hits can hide a non-void receipt, and a tape's `k = 0` is evidence, not proof. The search for the cheapest path is heuristic (a focus-guided beam, §2.4): a strict path the search misses can make a grade *worse* than the truth, never better — the author's remedy is to split the row. A lemma table is graded as it closes and priced at that grade in every later table's search (`on_table`), so a later row prefers a strict path to an absorbed lemma when one exists; the lemma's own rows are not searched again at the use site. Two directions are searched separately and never joined, so a row needing a creation step and a reduction step at once may be refused though each licenses alone. The position rule is pessimistic at a counit pair: a square that is the only child of an instance is transparent to a receipt below it, and the rule still refuses. The tape is a multiset: exchange is free, duplicates from a schema's instances are merged, and a reused theorem contributes one entry whatever its tape held — the exchange half of L0 (ordered vs unordered tape, Q2 of the page-logic draft) is not represented. The derivation checker licenses a step; it does not read the note.

What this settled on the trunk (2026-10-04): of 93 derivations, 78 agreed with the hand cells as written; eight that said `holds-mod-Λ` for a unit step under a square were wrong and are `guarded` (the by-content guard survives into 𝕁₁ as an import: `alg.power-of-base`, `alg.power-of-power`, `alg.root-of-product`, `alg.root-of-quotient`, `alg.sqrt4`, `C.i-to-the-i`, `C.root-of-negative`, `C.modulus-of-polar`); the nine cells waiting on □ were filled from the grades and LEGISLATION 30(f) — Dominion strict, by the pole exemption; `alg.one-to-power` fails in 𝕁₁ exactly where the prover points (the log of one under a square, receipt ω) and is `replaced` by the receptacle. LEGISLATION 28's forecast is corrected accordingly: a *by position* guard dissolves into an absorbed receipt; a *by content* guard at depth 0 becomes a posted receipt (holds mod Λ); a *by content* guard under a square stays a guard — the receipt check the reading performs.

---

## 6. Gaps

### 6.1 Two kinds (LEGISLATION 13)

- `kind: concept` — a mathematical concept with no form (induction, order, a heap, a metric at ∞, weight).
- `kind: form` — a form the calculus can write that nobody has read yet (the size-3 constants `(o)`, `((o))`, `[o o]` before their rungs are laid). Forms containing `[□]` or `<□>` are not gaps: James leaves both undefined and the chart excludes them by decree, because admitting either collapses the calculus (`mult.hole-exclusion`).

### 6.2 The census

`tools/census.py` enumerates every form up to a size bound (v1: ≤ 3 boundaries, no variables), canonicalizes, evaluates in the `C` reading (with `□` as the black hole), and classifies each form as `numeral` · `reduces` (its value is already achieved by a smaller form) · `new` (a value no smaller form has) · `hole` · `excluded` (contains `<□>`) · `undefined` (contains `[□]`). Every `new` form must be assigned to a node or listed in `census/open-forms.md`; `excluded` and `undefined` forms are assigned to the exclusion decree. Raising the bound is a standing task; the census is re-run by the checker.

### 6.3 Gap plans (LEGISLATION 14)

Every gap node's **Plan** section has exactly these fields:

| field | content |
|---|---|
| candidate form(s) | the form(s) proposed, or "none — a rule schema" |
| law(s) to add, and type | what would have to be adjoined (`axiom`, `decree`, `primitive`, `import`) |
| nativity criterion | the test the addition must pass to count as native (stated in terms of forms and ≐ only) |
| refutation test | the concrete computation or model that would kill it |
| meta-move? | whether the plan requires looking at the calculus from outside (a schema, a model, a moduli of readings) — and if so, which |
| owner thread | the existing project file that owns it |
| rank | by cost: reading < definition < theorem < decree < axiom < new primitive (new primitives rank last) |

### 6.4 Induction and order (LEGISLATION 17)

The first honest gaps the reader meets, both at rung N: an equational calculus does not express "by induction on a pile", and `m < n` is not a form. Both are `gap` nodes with plans; both are **meta-level**; both are expected to be resolved by meta-moves (a schema rule; the finite-set reading in which induction is the universal property of the free monoid on `o`; the Lean tier where `Nat.rec` lives natively). The chart records them as gaps rather than smoothing them over.

---

## 7. Refuted readings (LEGISLATION 15)

Refutations are kept, never deleted. Attached to the node they were mistaken for, struck through, with date and witness. The generator collects them into one searchable list. The Field's error log, the JH adversarial ledger, and the JS refuter's catches are the first backfill.

---

## 8. Scope and the trunk

### 8.1 Tiers (LEGISLATION 16)

| tier | content | v1 |
|---|---|---|
| **A** number and algebra | void → ℕ → ℤ → the square boundary → ℚ → algebraic (fractional cardinality) → J, ℂ → 𝕁₁ → ℍ (JH) → 𝕆 (JO) → 𝕊 (JS) | full |
| **B** analysis | exp–log completeness (the receipt prover), shift and derivative, metric and order, places and p-adics (JP), the adelic page | full |
| **C** logic | LoF Boolean, Existential Graphs, polarized/affine readings | one strand |
| **D** structure | `() ⊣ []`, ω/Λ, im J, Bott, moduli, the F₁ road | as far as the F₁ road needs |
| **E** The Field | ι/κ census, E and B as one form | pointers only |

### 8.2 Rungs (chapters), in walk order

`void` → `N` → `Z` → `mult` → `Q` → `alg` → `C` → `schema` → `J1` → `place` → `H` → `analysis` → `J2` → `logic` → `struct` → `F1` (→ re-entry to `void`), with `O` and `S` a branch off `H` (LEGISLATION 29). `field` is a side chapter. Built through `place` (2026-10-06): the finite places as pages, read by `tools/place.py`, with the trunk's JP cells computed (§4.4). The additive-first order (ℤ before the square boundary) follows the Iconic Mathematics scope and sequence and is the walk's own ordering principle: each stage adds an idea, not necessarily a boundary; the inverse boundary gains multiplicative powers only when it meets the square.

### 8.3 Trunk and roads (LEGISLATION 19)

The **𝕁₁ road** is the trunk: ℕ → ℤ → ℚ → algebraic → ℂ → 𝕁₁ → finite sets / sphere spectrum → F₁. The **adelic page** (JP) is the second road into F₁ (Connes–Consani lives there). The **division-algebra branch** (JH/JO/JS) rejoins at 24, marked `ANALOGY` until a form equates them. **Analysis** and **The Field** are branches.

---

## 9. Order (LEGISLATION 18)

- Dependency order is the spine (the `uses` DAG).
- Rungs are the chapters.
- `order` is the walk: a total order refining the DAG. Integers spaced by 10.
- `guide: shape-led | need-led` on every node records whether the step followed the shape of the forms or was pushed by what mathematics needed. The ratio per rung is rendered — it is itself a finding.

---

## 10. Verification and process

- **Engine is the core** (LEGISLATION 20): every object-level law and derivation step is shadow-checked in `tools/check.py`; meta-level claims are checked by a named script in `tools/models/`; where the receipt prover or `jadic.js` applies, their results are cited as `numeric`. The engine enforces the undefined-form decree by exception: a row that mirrors or abstracts a form whose value is □ fails. It samples variables only in the node's declared `domain`, so a law that is unsound outside that domain (Involution-down off the principal strip) is not caught by it — the node must say so in its reading cells.
- **Propose → refute → repair** per rung (LEGISLATION 21): a rung's nodes are drafted, an independent referee pass (a fresh agent that has not seen the drafting) attacks derivations and status claims — above all whether each cited rule *licenses* its step, which the engine cannot see — repairs are made, and only then are nodes marked `engine`. Nodes are written to be picked up cold. The pilot's referee pass (2026-10-03) found two mis-licensed steps and one collapse of the unrestricted theory; all three are recorded in the nodes' Refuted readings.
- **Lean later** (LEGISLATION 20): a scoped expansion in which node ids become Lean declaration names for the classical trunk; `#print axioms` then computes price automatically and doc-gen produces the hyperlinked chart. Not in v1; the id scheme is chosen so this is a renaming-free step.

---

## 11. Repository and tooling (LEGISLATION 22)

```
boundary-chart/
  SPEC.md               this file
  LEGISLATION.md        the binding decisions, by number
  README.md             how to add a node, run the checker, build the site
  nodes/<id>.md         one law per file
  concepts/<slug>.md    one paragraph per concept (optional per concept)
  census/               generated: size-le-3.md, open-forms.md
  tools/
    forms.py            parser · canonicalizer · ℂ evaluator (black hole, exclusion) · random instantiation
    nodes.py            front-matter + section parser shared by check and build
    check.py            schema · DAG · uses-consistency · shadow check of every derivation step and law · census freshness
    census.py           the small-form census
    build.py            nodes → site/index.html (drawn forms, clickable chart, price, used-by, concept index, gaps, refuted list, walk progress)
    models/             witnesses for meta theorems (e.g. dominion_models.py)
  site/index.html       generated; the pilot chart, publishable as an artifact
  docs/                 narrative material that is not a law (the F₁ roads memo, backfill maps)
```

Zero dependencies beyond Python 3. `python3 tools/check.py` must exit 0 before any node is marked `engine`. `python3 tools/build.py` regenerates the site. The repo is the source of truth; the published artifact is a build product.

---

## 12. The visual encyclopedia

- **v1 (now):** (a) every form drawn as nested boundaries from its canonical string; (b) the chart as a zoomable, clickable DAG layered by rung, with the re-entry edge drawn as a loop; the concept index; the gap list with plans; the refuted list; the walk with its progress bar.
- **v2:** (c) a live instrument per law — apply-this-law on an editable form — reusing the rewrite calculator and `jadic.js`, scoped node by node.
- **Game skin (deferred):** prerequisites = `uses`; "unlocked" = status `NATIVE` with a derivation; the player is at a node and must reach the next by rewriting. All of this is derivable from the files; nothing is stored for it now.

---

## 13. Seeding and backfill (LEGISLATION 25)

1. **Fresh uniform walk** of the trunk to ℂ: rungs `void`, `N`, `Z`, `mult`, `Q`, `alg`, `C`, in that order, each rung refereed before the next. Estimated: 30 (pilot) + ~45; actual, 2026-10-03: 138 laws through `C`, every rung refereed twice and `C` five times, the last against the thesis text. 2026-10-04: rung `schema` — seven laws over every n (145 laws), the induction gap priced on each. 2026-10-04, later: the derivation checker and the receipt prover (§2.4, §5.5), `mult.log-of-one` split out (146), and rung `J1` — twenty-one nodes (167 laws): the split Involution, the period form, closure and absorption as theorems, L0, the half-period, James's Theorems 1 and 2 re-read, the receptacle, the depth-one criterion, the strata of annihilation as a gap, the pole, soundness and the classical floor with witnesses, the ψ-wall with its census and import. 2026-10-06: rung `place` — twenty-two nodes (189 laws): the places imported (Ostrowski), the void pile as a decree over p and n, the reading at p as an import with its engine (`tools/place.py`), residues, minus one as a pile, the irreducible `[p]`, no reciprocal of the prime, Fermat–Euler imported, division by a unit, the doll and the geometric doll, the radius, the Teichmüller element, the torsion log, the selection rule, the polar form, the same wall at every place, the prime power, the two ends, Hensel's lift, the local wall, and completion as the gap — with the trunk's JP cells computed by the place ledger (§4.4) and the discipline of the page (§5.5; LEGISLATION 31(g)) found by the rung's referee pass. The walk continues: `H`, `analysis`, `J2`, `logic`, `struct`, `F1`.
2. **Backfill the branches** from the existing ledgers, keeping the old ids as aliases: `JH-1…22` (Exposition Guide App. C), `JO-1…34`, `JS-1…41`, `JP-1…` (Shell Calculus, settlements, adelic page), the exp–log ledger with its known-since column, the motivic rule card, The Field's results and prohibitions.
3. **Place the F₁ node** and the three roads as readings on the trunk; fill `finset` cells on every trunk node.
4. **Census** to size 4; assign or list.
5. **Referee** each rung; promote to `engine`.
6. **Generate** the site; publish; walk.

---

## 14. Decided by default — revisit if wrong

- Rung `mult` (the square boundary) sits after `Z`, not inside `N`, per the additive-first curriculum. The dependency DAG is unaffected either way.
- Medium facts (void transparency, unordered juxtaposition) are `primitive` nodes with `kind: medium`, so commutativity is visibly *free* rather than an axiom.
- Meta-level nodes count as laws and may be theorems (a finite model is a proof).
- `domain` for the shadow check defaults to `positive` in rungs through `alg` and `complex` from `C` on; nodes may narrow or widen it. The engine snaps values that are real up to rounding onto the real axis before taking a log, so the branch cut is not decided by floating-point noise.
- **Decided under referee pressure, 2026-10-03, pending Lui's confirmation:** the seam discipline is a decree of the classical setting from rung `mult` on (`mult.seam-decree`), because `J J = [<o>][<o>]` can be written there and one unguarded unit step — in either orientation — proves `J J ≐ void`, from which the ℚ sign laws collapse the calculus. A **seam step** is a unit step whose content leaves the principal strip for some value in the node's domain; a law whose derivation uses one declares `guarded_by` (by position; Amendment A2 — until the C referee pass such laws were NATIVE-BY-DECREE, and absorbing seam steps went unpriced). The decree is stated in the ℂ reading, because `[[[oo]]]` carries iπ with no mirror anywhere and no shape-based signature is exact (`mult.seam-signature`); the alternative (defer the sign laws to rung C, or to J1 with `≃`) was rejected as the less honest inventory. Laws whose unit steps are admitted by content at non-absorbing positions, or by position on off-strip content, declare `guarded_by: [mult.seam-decree]` — a mechanical field the checker enforces in both directions — and carry the guard in their price (§5.4).
- The two undefined forms, `<□>` and `[□]`, are one decree node (`mult.hole-exclusion`), read up to ≐; the ℂ reading is an `import` node so that consistency has a computable price.
- Rule names follow James 1993 / Book One (Involution, Distribution, Inversion); Bricken's names (inversion, arrangement, reflection; involution for `<<A>> ≐ A`) are carried as aliases, to be verified against the sources.
