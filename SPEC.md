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
| **walk** | the linear order in which the chart is read; a total order refining the dependency DAG |

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

Every type is a step of the walk (LEGISLATION 4). The type is the node's colour in every rendering.

A node also has a **level**: `object` (an equation between forms) or `meta` (a statement about the calculus: consistency, freeness, independence, normalization, induction). Meta-level nodes are where the "meta-moves" of LEGISLATION 17 live; they are first-class so the chart can show where the calculus had to be looked at from outside.

### 2.3 Front matter (required unless marked optional)

```yaml
---
id: Z.collection
title: Inverse collection
type: theorem                 # primitive | axiom | definition | theorem | decree | import | gap
level: object                 # object | meta
kind: law                     # primitive: boundary | medium ; decree: exclusion | discipline | declaration | guard ; theorem/axiom: law | schema ; gap: concept | form
rung: Z
order: 230                    # walk order; integers with gaps of 10 so nodes can be inserted
setting: classical            # the setting the law is stated in
equality: "≐"                 # ≐ | ≡ | ≃ | ≈
domain: real                  # variables range over: natural | positive | real | complex (for the shadow check)
law: "<A><B> ≐ <A B>"         # canonical string; for definitions "name := form"; for gaps a one-line statement of what is missing
units: "−a + −b = −(a + b)"   # the law in standard notation (the ℂ reading)
gloss_check: "-A + -B == -(A+B)"   # optional: a Python expression the checker evaluates against the form's value
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
status: NATIVE                # NATIVE | NATIVE-BY-DECREE | IMPORTED | ANALOGY | CONJECTURE | REFUTED | ABSENT
verified: engine              # none | hand | engine | numeric | lean
known_since: "1993 (James); the arithmetic fact is ancient"
entered: 2026-10-03
guide: shape-led              # shape-led | need-led
band: "1–2"                   # K–12 band: K | 1–2 | 3–5 | 6–8 | 9–12 | beyond
uses: [Z.inversion, void.space]   # mechanical: must equal the set of rules cited in the derivation
see_also: [M.inverse-promotion]   # curated
aliases: []                   # ids in the existing ledgers (JO-n, JS-n, JP-n, JH-n, Field) and other names
concepts: [negation, addition]
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
   Allowed rules: `given`, `[[id]]` (one or more), `medium` (rearrangement in space — must also cite `[[void.space]]` once in the table), `substitution` (replacing a variable by a form), `congruence` (applying the same operation to both sides), `definition` (unfolding a definition — cite it). Axioms and primitives write `none — adjoined`. Gaps write `none — gap`. Meta theorems give the proof in prose and name the witness (a model, an invariant, a computation in `tools/`).
   The checker evaluates every consecutive pair of forms on random values and fails the node if any step is not an equality in the declared sense.
4. **Confirms** — the standard-notation fact (with its usual name) that this law *is*, and what it is **not** (where a naive reading overreaches). This is the "in-house confirmation" line for the walk.
5. **Settings and readings** — the two tables from the front matter, with one-line justifications for any cell that is not `holds`/`EXACT`.
6. **Refuted readings** — ~~struck through~~ readings or derivations once believed and since refuted, each with the date and the refuting witness (LEGISLATION 15). `none` is a legal entry.
7. **Notes** — anything else: Bricken's variant (attributed by volume), history, the thread that owns it.
8. **Plan** — gaps only (§6.3).

Price and used-by are **not** written in the file; the generator computes and renders them.

### 2.5 Canonical strings

- Boundaries: `( )`, `[ ]`, `< >`. Later primitives: `[ ; ]` ordered bracket (JH), `{ }` brace (extrusion), `{n }` lens (JP). Whitespace is ignored.
- Sugar accepted by the parser and expanded before checking: `o` = `()`, `□` = `[]`, `J` = `[<o>]`, `void` = the empty form. Numerals `n` are **not** sugar in canonical strings (write the pile) except inside `[[...]]` prose.
- Variables: single capital letters `A`–`Z`, optionally followed by a digit. A law with variables is a **schema**; the checker instantiates it.
- Repetition schemas ("n copies") are written with an explicit small instance in the table and the general statement in `law:` using `^n` superscript notation only in `units:`, never in a canonical string.

### 2.6 Rendering conventions (generator)

Canonical strings are drawn as nested boundaries: round → rounded capsule, square → rectangle, angle → hexagon with pointed sides. Beside the drawing: the ASCII string, the units form, the standard form. Type = colour; status = badge; verified = badge; band = small tag. Refuted content is struck through. House typographic notation in prose: *italic* for a reduction (an emptying), ***bold-italic*** for an emergent operation, **bold** for a settled one, ~~strikethrough~~ for wrong, "scare-quotes" to hold a term at arm's length.

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
| `classical` | three boundaries, Involution, Distribution, Inversion, James's J-discipline | James 1993; Book One Part I–II |
| `J1` | + weakened unit `[(A)] ≐ A mod Λ`, period axiom `(ω) ≐ ()`, A5′ absorption, L0 linearity, receipts | james-algebra notes v3.1 |
| `JH` | + ordered bracket `[ ; ]`, seed `J_j`, O9, OC, seam guard on Involution-down | JH Exposition Guide |
| `JO` | + tree nesting, priced receipts, alternator | Book One Part IV |
| `JS` | + fourth doubling, octave grade | JS-algebra-sedenionic |
| `JP` | + void pile (place), depth, lens, re-entry convention | Part II: Calculus of Number at a Place |
| `extrusion` | + brace `{ }`, gauge principle G0 | 𝕁 v3.2 |
| `field` | + ι or κ adjunction, boost seed | The Field, Vol. I |

Every law carries a `holds` cell for each setting: `holds` · `holds-mod-Λ` · `guarded` (holds under a named guard) · `replaced` (a more general law restricts back to it) · `fails` · `untested`. The three-way dominion check (classical holds / spectral fails / J1 deferred) is the template.

### 4.2 Readings

A **reading** is a model. The default gloss is `C`. The F₁ roads enter as readings first: `finset` (trunk road), `lambda` (Borger), `CC` (Connes–Consani); `logic` covers LoF/Existential-Graphs. Cells: `EXACT` · `PARTIAL` · `ANALOGY` · `ABSENT` · `CONVERSE` · `untested` — the five-word verdict vocabulary from the page-logic ledger, plus `untested`.

Readings are how the moduli-stack idea (LEGISLATION 17) enters the chart without a new primitive: a form is one thing; its readings are the points of its moduli; a law that holds in every reading is the stable part, and a law that holds in only one is the chart's way of saying where a reading is doing work the calculus is not.

### 4.3 Bricken (LEGISLATION 9)

James 1993 is the ground truth for `classical`. Bricken's constructs (`[[ ]]` as complex infinity, unit-ensemble presentations, parallel forms) enter as **attributed notes** inside the node they vary, tagged by volume (*Iconic Arithmetic* I/II/III), and become nodes only where they add a law James does not have.

---

## 5. Status, verification, dates, price

### 5.1 Status (one enum for the whole program; LEGISLATION 12)

| status | meaning |
|---|---|
| `NATIVE` | derived inside the setting from its own axioms; or a primitive/axiom of the base three |
| `NATIVE-BY-DECREE` | holds because a decree was issued (exclusion, discipline, declared-void pile, guard) |
| `IMPORTED` | used, not derived; the import is named and dated |
| `ANALOGY` | a correspondence asserted but not an equation of forms (e.g. 24 ↔ ν) |
| `CONJECTURE` | stated, unrefuted, undemonstrated |
| `REFUTED` | shown false; kept, struck through, attached to the law it was mistaken for |
| `ABSENT` | the concept has no form (gaps) |

Mapping from the old ledgers (recorded in `aliases`/`notes`, never silently): EXACT→`NATIVE` (with reading EXACT); PARTIAL→`NATIVE` with a `PARTIAL` reading cell or `IMPORTED`; IMPORTED→`IMPORTED`; emerged→`NATIVE`; CONJECTURE/REFUTED unchanged; ANALOGY/ABSENT/CONVERSE live in reading cells.

### 5.2 Verification tier

`none` → `hand` (a written derivation) → `engine` (the derivation's every step shadow-checked by `tools/check.py`, or a meta claim checked by a script in `tools/`) → `numeric` (high-precision numerical identity beyond the shadow check — e.g. the receipt prover) → `lean` (a Lean declaration; node id = declaration name — later scoped expansion, LEGISLATION 20).

**"Exact" is withheld until `engine`** (LEGISLATION 21): a node whose `verified` is `none` or `hand` renders with a hollow badge whatever its status says.

### 5.3 Two dates

`known_since` — when the mathematics was known (James 1993; "ancient"; Sagle 1961; "this chart, 2026" when nothing earlier is located — and then a literature check is a standing obligation). `entered` — when it entered the program.

### 5.4 Price (computed; LEGISLATION 11)

`price(n)` = the set of ancestors of `n` along `uses` whose type is `primitive`, `axiom`, `decree`, or `import`, partitioned into:

- **base**: the three boundaries, the medium, and James's three axioms;
- **extra**: everything else — further primitives, axioms, decrees, imports.

Rendered as "what it costs to write X": *i* costs nothing extra (fractional cardinality is a theorem schema); ℍ costs an ordered bracket + O9 + OC; ℤ_p costs the void-pile decree. The concept index shows the cheapest price among a concept's forms.

---

## 6. Gaps

### 6.1 Two kinds (LEGISLATION 13)

- `kind: concept` — a mathematical concept with no form (induction, order, a heap, a metric at ∞, weight).
- `kind: form` — a form the calculus can write that nobody has read (`[[ ]]` until Bricken; `[[<>]]`; most of the size-3 census).

### 6.2 The census

`tools/census.py` enumerates every form up to a size bound (v1: ≤ 3 boundaries, no variables), canonicalizes, evaluates in the `C` reading (with `□` as the black hole, `<□>` as excluded, `[□]` as undefined), and classifies each form as `numeral` · `reduces` (its value is already achieved by a smaller form) · `new` (a value no smaller form has) · `hole` · `excluded` · `undefined`. Every `new` or `undefined` form must be assigned to a node or listed in `census/open-forms.md`. Raising the bound is a standing task; the census is re-run by the checker.

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

`void` → `N` → `Z` → `mult` → `Q` → `alg` → `C` → `J1` → `H` → `O` → `S` → `analysis` → `place` → `logic` → `struct` → `F1` (→ re-entry to `void`). `field` is a side chapter. The additive-first order (ℤ before the square boundary) follows the Iconic Mathematics scope and sequence and is the walk's own ordering principle: each stage adds an idea, not necessarily a boundary; the inverse boundary gains multiplicative powers only when it meets the square.

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

- **Engine is the core** (LEGISLATION 20): every object-level law and derivation step is shadow-checked in `tools/check.py`; meta-level claims are checked by a named script in `tools/`; where the receipt prover or `jadic.js` applies, their results are cited as `numeric`.
- **Propose → refute → repair** per rung (LEGISLATION 21): a rung's nodes are drafted, an independent referee pass (a fresh agent that has not seen the drafting) attacks derivations and status claims, repairs are made, and only then are nodes marked `engine`. Nodes are written to be picked up cold.
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

1. **Fresh uniform walk** of the trunk to ℂ: rungs `void`, `N`, `Z`, `mult`, `Q`, `alg`, `C`, in that order, each rung refereed before the next. Estimated: 30 (pilot, done) + ~45.
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
- `domain` for the shadow check defaults to `positive` in rungs through `alg` and `complex` from `C` on; nodes may narrow or widen it.
