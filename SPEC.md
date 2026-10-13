# The Boundary Chart — Specification v2.1

*A step-by-step exposition of mathematics in James boundary arithmetic, from the void to F₁, as a searchable chart of laws; the data model, the engine and the process behind a future visual encyclopedia.*

Status: **binding** — every rule here records a decision from `LEGISLATION.md` (0–33, all decided as of 2026-10-13; the forks taken and the deferrals are listed in §14) or a default that stands unless Lui objects. Version 2.1, 2026-10-13: v2.0 consolidated v1.0 (2026-10-03) and the increments of rungs `schema`, `J1`, `place` and `H` — the rules stated once, in force, with the history of how they were reached in `README.md` (Status), `ROADMAP.md` (§5–§7) and `LEGISLATION.md`; v2.1 records Lui's confirmation of every pending decision and the actions it folded in. Written for Lui; meant to be picked up cold by a later session, and to be brought into a project as its reference. How it is iterated: §11.4.

---

## 0. What this is

The chart is a directed graph of **laws**. Every node is one law of boundary arithmetic — a primitive that licenses forms, an axiom that adds an equation, a definition that abbreviates, a theorem that settles, a schema that settles up to a range, a decree that legislates, an import that borrows, or a gap that names what cannot yet be written. Every node carries a derivation whose licensing rules are earlier nodes, so the back-links are mechanical, not editorial. The graph has one spine (the trunk from the void to F₁), branches (the extensions), and exactly one marked **re-entry edge** from the last node back to the first: F₁ arithmetic re-reads the natural numbers, so the exposition closes on itself.

Three uses, in order of priority (LEGISLATION 24):

1. **Inventory.** How much of mathematics is already expressible in the three boundaries, at what price, and where the holes are.
2. **The walk.** Lui walks the chart in order; the early nodes confirm, in a notation he already commands, what he knows; the later nodes teach him what he doesn't yet. Every node therefore states, in one plain sentence, the ordinary mathematical fact it is the boundary version of.
3. **Teaching.** Having learned by the walk, teach by the same walk. The K–12 band is visible on every node; the game and the live instruments are later skins over the same files.

The chart is **not** a book. It is the data a book, a game, or an encyclopedia is generated from. Prose lives in nodes and concept files; everything else is computed.

### 0.1 The two ends

- **Start: the void.** The first node is the empty page. The natural numbers are the first rung, not the first node, because a pile cannot be stated without void and `o` (LEGISLATION 1).
- **End: F₁.** One target node, *F₁ arithmetic*, with three roads into it (LEGISLATION 2): **(a) finite sets / sphere spectrum** — `( )` and `[ ]` read as finite sets, `< >` as group completion (Barratt–Priddy–Quillen); the trunk, because here the boundaries are themselves the F₁ objects rather than a translation of them. **(b) Borger's λ-rings** — ψ-operations as the whole structure; the nearest relative of the ψ-wall. **(c) Connes–Consani** — hyperrings, Witt vectors, the arithmetic site; the declared-void pile of the place calculus is the on-ramp. Roads (b) and (c) are built as *readings* (§6) first and as nodes only where a law is gained; no trunk node is accepted as *settled* until its (b) and (c) reading cells are at least `ABSENT` or `PARTIAL` rather than blank.
- **The re-entry edge.** `F1.arithmetic → void.page` (one edge, flagged `reentry: true`). It is the chart's largest gap and is drawn differently. The DAG check exempts exactly this edge.

### 0.2 Three target pictures

The chart has the shape all three need; the rungs make it native (ROADMAP §1). **Motivic:** a node is a form, its `readings` row is its row of realizations, and a law that holds in every reading is the stable part. **F₁ (finset / BPQ):** the additive fragment is EXACT in finite sets today; the inverse boundary is where the sphere spectrum enters, and J's finset analogy (η) matches the 𝕁₁ J (2J = ω), so the F₁ road passes through `J1`. **A sheaf of formal groups over the Berkovich spectrum of ℤ:** the places are the base (rung `place`), the wall `(ω A) ≃ (A)` at a place is a formal group of height one with the ψ-wall as its torsion, and the stack of lattices (rung `J2`) is the moduli of formal groups with its height stratification.

---

## 1. Vocabulary

| term | meaning here |
|---|---|
| **form** | a finite multiset of boundaries, each containing a form; the void is the empty form |
| **boundary** | `( )` round/instance, `[ ]` square/abstract, `< >` angle/inverse — and, from rung `H`, the **ordered square** `[ ; ]`; later primitives still to come: the extrusion brace `{ }`, the lens `{n }` |
| **medium** | the page: juxtaposition is an unordered multiset with the void as unit. Medium facts are laws of type `primitive` with `kind: medium` |
| **law** | one equation between forms (object level), or one statement about the calculus (meta level: freeness, independence, induction, a theorem of a reading) |
| **node** | one law, one file, one id |
| **rung** | a chapter of the walk — usually a number system (`N`, `Z`, `Q`, `C`, `H`), sometimes the arrival of a boundary (`mult`) or of a piece of machinery (`schema`, `J1`, `place`) |
| **setting** | a named set of nodes in force: `classical`, `J1`, `JP`, `JH`, `JO`, `JS`, `extrusion`, `field` (§5) |
| **reading** | an interpretation of forms, as a model: `C` (the default gloss), `finset`, `lambda`, `CC`, `logic` (§6); and, for the engine, the readings it computes with — ℂ, 𝕁₁, the page at p, ℍ at ∞, ℍ at p |
| **receipt** | in `J1` and later: the Λ-valued record of what a non-strict step dropped; at a place a count of the place's period; in ℍ a lattice element with a *direction* |
| **tape** | the graded record of a derivation's non-strict steps (§7.3); a node's grade is its worst step |
| **ledger** | a computed table comparing every law's hand cells with what a reading computes (§7.4); written by the engine, never edited |
| **witness** | a script in `tools/models/` that checks a meta-level claim by computation; exits 0 iff the claim holds |
| **price** | the set of non-derivable ancestors of a node (primitives, axioms, decrees, imports, gaps) and the guards along the way — computed, never typed (§4.3) |
| **gap** | a node of type `gap`: a concept with no form, or a form with no reading, with a plan (§9) |
| **owed** | a named, dated obligation the chart has not met — a derivation, a reading, a cell — recorded on the node where it falls due (`owed:`, §9.2) and collected into one list |
| **walk** | the linear order in which the chart is read; a total order (`order`) refining the dependency DAG. Rung order (LEGISLATION 29): `void N Z mult Q alg C` · `schema` · `J1` · `place` · `H` · `analysis` · `J2` · `logic` `struct` · `F1`; `O`, `S` are a branch |
| **schema** | a node whose law carries a count parameter (`n`, and optionally `k` or the place `p`); the engine instantiates it over a declared range and checks every instance; its derivation is an induction step (§3.7) |
| **page** | the finite place p read to depth n: the residues mod pⁿ, declared by the void pile `o^{p**n} ≃ void` (§6.3) |
| **ordered square** | `[x₁ ; … ; xₙ]`, rung `H`: a square whose contents are a sequence of forms, read as the log of their ordered product; one entry is the ordinary square; `[A ; B]` and `[B ; A]` are different forms where `[A][B]` and `[B][A]` are one (§6.4) |
| **constant** | a form of a setting with no expansion into the three boundaries: `Jj`, the second seed of rung `H`, is one (`i`, `j`, `k` are sugar). A constant has a value in the readings that know it and none elsewhere |
| **conditional law** | a law whose `units:` field opens with `PREMISE …`: the equation holds where the premise does, and the reading checks the premise at every use (§7.2) |
| **slice** | in ℍ, a copy of ℂ: C_u = ℝ + ℝu for a pure unit u. The **plane** is the slice of the pinned J, C_i = ℂ ⊂ ℍ, where the trunk's laws hold verbatim (§6.4) |
| **seam** | where the unit step `[(A)] ≐ A` is false by a displacement no period measures: the point θ = π of ℂ, the angle-π sphere of ℍ but the pinned ray, and on a quaternion page a positive-measure set (§6.4, §7.3) |

House typographic notation in prose (and in the type verbs of §3.2): *italic* for a reduction (an emptying), ***bold-italic*** for an emergent operation, **bold** for a settled one, ~~strikethrough~~ for wrong, "scare-quotes" to hold a term at arm's length.

---

## 2. Equalities and cells

### 2.1 The four equalities

`≐` strict convertibility in the classical calculus; `≡` strict (syntactic) in 𝕁₁ and later settings; `≃` witnessed — the two sides agree mod the period, and a receipt records what was dropped; `≈` evaluated. Every node declares which is in force (`equality:`), and in the graded settings (`J1`, `JP`, `JH`) **the symbol is the one the tape earns** (§7.3): ≡ for a strict tape, ≃ for an absorbed or posted one; the `law:` string carries the same symbol. A classical node writes ≐.

### 2.2 The `holds` cells (per setting)

| cell | meaning |
|---|---|
| `holds` | the law holds in the setting as stated: its tape there is strict, page or absorbed, and its law reads exact on its domain |
| `holds-mod-Λ` | the law holds mod the setting's period: its tape posts a receipt at depth 0, or its law reads mod-Λ |
| `guarded` | the law holds under a named guard: where its forms have a value (some sample is formless), off the seam, or by a legislative guard; or its tape imports (a receipt void only by content) |
| `replaced` | a more general law of the setting restricts back to it; the cell names that law. Legal where the law fails or is formless there |
| `fails` | the law is false in the setting, or its derivation is absent there with a non-void receipt |
| `untested` | not yet examined — legal only where no ledger computes the cell |

**The ACCEPT rule.** Where a ledger computes a cell, the hand cell may say *more* and never less: hand `holds` needs computed `holds`; `holds-mod-Λ` needs `holds-mod-Λ`; `guarded` accepts `holds`, `holds-mod-Λ`, `guarded`; `replaced` accepts anything; `fails` needs `fails`; `untested` is illegal. The engine fails the node otherwise.

### 2.3 The `readings` cells (per reading)

`EXACT` · `PARTIAL` · `ANALOGY` · `ABSENT` · `CONVERSE` · `untested` — the five-word verdict vocabulary of the page-logic ledger, plus `untested`.

### 2.4 The ledger words and the tape grades

A ledger reads a *law* at the generic points of a domain and says `exact` (as stated on every judged sample) · `mod-Λ` (only mod the period) · `guarded` (holds where its forms have a value; some sample is formless) · `none` (no sample has a value) · `seam` (the two sides differ by a seam displacement on some sample) · `fails`. A tape grades a *step*: `strict` · `page` (at a place only) · `absorbed` · `posted` · `import` · `absent`, with its position class — `absorbing`, `depth-0`, `under-square`, `inherited`, `pole`, `seam`, `cross-slice`, `premise`, `formless`. A law no sample can judge is not a law that holds: an equality is certified by samples, never by their absence.

---

## 3. The node

### 3.1 One file per node

Path: `nodes/<id>.md`, where `id = <rung>.<slug>`. Ids are stable; slugs are lowercase, hyphenated, never renamed once published (rename = new node + alias). Obsidian-style links `[[Z.collection]]` are the only link syntax.

### 3.2 Types, levels, kinds

| type | verb | what the node adds | priced |
|---|---|---|---|
| `primitive` | *licenses* | a new way to form a form (a boundary) or a fact of the medium | yes |
| `axiom` | ***adds*** | an equation the calculus did not have | yes |
| `definition` | *reduces* | a name for a form built from existing ones (sugar; no new law) | no |
| `theorem` | **settles** | an equation (or meta-statement) the calculus already contained | no |
| `schema` | **settles** up to the range | a theorem with a count parameter, stated as a template, checked at every value in a declared range and derived by an induction step; the passage to all n is the gap | no — but its hypothesis row cites `N.induction`, which is |
| `decree` | ***legislates*** | a rule imposed from outside the equational base: an exclusion, a discipline, a declaration (a declared-void pile), a guard | yes |
| `import` | borrows | a fact used but not derived (a theorem of ordinary mathematics, a reading, a count) | yes |
| `gap` | *names* | a concept without a form, or a form without a reading, with a plan | yes (so a schema's price shows the induction gap) |

Every type is a step of the walk (LEGISLATION 4); the type is the node's colour in every rendering. **Level:** `object` (an equation between forms) or `meta` (a statement about the calculus or about a reading); meta nodes are where the meta-moves of LEGISLATION 17 live, and a meta node is at most `hand`-verified without a `witness:`. **Kind:** primitive `boundary | medium`; decree `exclusion | discipline | declaration | guard`; theorem/axiom/definition/import `law | instance` (one value of a family over n) | `declaration` (a definition or import stated in prose); gap `concept | form`.

### 3.3 Front matter

```yaml
---
id: Z.collection
title: Inverse collection
type: theorem                 # primitive | axiom | definition | theorem | schema | decree | import | gap
level: object                 # object | meta
kind: law                     # §3.2
rung: Z
order: 230                    # walk order; integers spaced by 10
setting: classical            # the setting the law is stated in: classical | J1 | JP | JH | …
equality: "≐"                 # ≐ | ≡ | ≃ | ≈ (§2.1)
domain: real                  # natural | positive | negative | real | unit | complex | slice (§3.6)
law: "<A><B> ≐ <A B>"         # canonical string; definitions "name := form"; gaps/decrees/imports a one-line statement (GAP — / DISCIPLINE — / DECLARATION — / IMPORT — prefixes mark prose laws)
units: "−a + −b = −(a + b)"   # the law in standard notation; a conditional law's opens with "PREMISE …"
gloss_check: "-A + -B == -(A+B)"   # optional: a Python expression the checker evaluates against the form's value in ℂ
schema_range: "n=2..8"        # schema nodes, and decrees/imports written over the place: the instances the engine checks (§3.7)
schema_draw: "n=3"            # schema nodes, optional: the instance the card draws
witness: tools/models/x.py    # meta nodes: the script that checks the claim; exits 0 iff it holds
forms: []                     # optional: canonical forms this node reads, for the census (§7.6)
holds:                        # per setting (§2.2); every setting of §5 is a legal column
  classical: holds
  J1: holds
  JH: holds
  JO: untested
  JP: holds
readings:                     # per reading (§2.3)
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: untested
status: NATIVE                # §8.1
verified: engine              # none | hand | engine | numeric | lean (§8.2)
known_since: "1993 (James); the arithmetic fact is ancient"
entered: 2026-10-03
guide: shape-led              # shape-led | need-led
band: "1–2"                   # K–12 band: K | 1–2 | 3–5 | 6–8 | 9–12 | beyond
uses: [Z.inversion, void.space]   # mechanical: must equal the set of [[ids]] cited in the Derivation section
see_also: [mult.inverse-promotion]   # curated
aliases: []                   # ids in the existing ledgers (JO-n, JS-n, JP-n, JH-n, Field) and other names
concepts: [negation, addition]
guarded_by: []                # mechanical: [mult.seam-decree] iff the derivation relies on a clause of the decree (§4.3)
owed: ["2026-10-07: what is owed, in a line"]   # optional: dated obligations this node carries (§9.2); rendered and collected
understood: no                # Lui's tracker: no | partial | yes
understood_note: ""
reentry: false                # true only on the one re-entry edge's source node
---
```

Field rules: `uses` is **mechanical** (the checker computes the citations and fails the node if `uses` differs; hand-chosen relevance goes in `see_also`); `holds` is per setting and `readings` per reading — tables, not branches (LEGISLATION 8); `status`, `verified`, `known_since`, `entered` are four separate things (LEGISLATION 12); `band` follows the Iconic Mathematics scope and sequence and is unfilled (`beyond`) where unsure; `understood` is Lui's, never used in verification, rendered as a progress bar over the walk.

### 3.4 Body sections (in this order; `##` headings; a section may say `none`)

1. **Law** — the law three ways, side by side: raw form · named units · standard notation; the generator draws the forms from the canonical string. Then the lede: what the law is, in prose, with its back-links.
2. **Plain** — one sentence (at most 45 words) a ninth-grader could read, stating the ordinary fact this is the boundary version of. Required on every node (LEGISLATION 24).
3. **Derivation** — a Given–Rule table `| form | rule | note |` in Book One's style, every row a canonical form. Rules: `given` (opens a table — a chain cannot restart; start a new table or a lemma), `[[id]]` (one or more; a law linked in the note cell counts as cited), `medium` (rearrangement in space; cite `[[void.space]]` once in the table), `substitution`, `congruence`, `definition` (unfolding a definition — the row is an identity once the sugar is expanded), `name` (a row that merely names the previous form in standard notation; not a form, not checked), `lemma` (an equation proved by an earlier table of the same node), `hypothesis` (schema nodes only: the schema's own law at a smaller parameter; the note cites `[[N.induction]]`). Axioms, primitives, decrees and imports write `none — adjoined` and cite in prose the nodes their statement is built from — those citations are their `uses`. Gaps write `none — gap`. Meta-level nodes use a `| statement | rule | note |` table: prose steps, each citing the laws it leans on, with `witness part (k)` naming what the script checks. What the engine checks of a derivation: §7.1–7.3.
4. **Confirms** — the standard-notation fact (with its usual name) that this law *is*, and what it is **not** (where a naive reading overreaches). The "in-house confirmation" line for the walk.
5. **Settings and readings** — the two tables from the front matter, with one-line justifications for any cell that is not `holds`/`EXACT`; the body tables must agree with the front matter (checked).
6. **Refuted readings** — ~~struck through~~ readings or derivations once believed and since refuted, each with the date and the refuting witness (LEGISLATION 15). `none` is legal.
7. **Notes** — anything else: Bricken's variant (attributed by volume), history, the thread that owns it, what is owed.
8. **Plan** — gaps only (§9.1).

Price and used-by are **not** written in the file; the generator computes and renders them.

### 3.5 Canonical strings

- Boundaries: `( )`, `[ ]`, `< >`; from rung `H`, `[x ; y ; …]` — the ordered square, entries separated by `;`, each entry a form (its own multiset), the sequence ordered. Whitespace is ignored. Later primitives: `{ }` brace (extrusion), `{n }` lens (JP).
- Sugar, expanded by the parser and folded back by the printer: `o` = `()`, `□` = `[]`, `J` = `[<o>]`, `ω` = `[()]` (the period form; the cube root of unity that rung `C`'s prose also calls ω is never a canonical string), `void` = the empty form; from rung `H`: `i` = `(([J] <[oo]>))`, `j` = `(([Jj] <[oo]>))`, `k` = `([i ; j])`; and `Jj`, the second seed, a **constant** (§1). Numerals are **not** sugar in canonical strings (write the pile) except inside `[[...]]` prose.
- Variables: single capital letters `A`–`Z`, optionally followed by a digit; the checker instantiates them on random values of the node's domain. A node whose law is one value of a family over n (`A A ≐ ([A][oo])`) is `kind: instance`; the family itself is a `schema` node (§3.7). Repetition over a count is a schema; an object law writes its small instance out in full, never a superscript.
- A conditional law (§1) writes the bare equation in `law:` and its premise in `units:` (`PREMISE P·Q ≐ Q·P — …`); its domain is `slice`.

### 3.6 Domains

The domain says where the shadow check samples a node's variables, per reading (§6): `natural` — a small count; `positive` — a positive real (at a place: a principal unit, now and then times p, and a fifth of the time a fraction of principal units); `negative`; `real` — either, nonzero; `unit` — a unit of the place (at ∞ a nonzero real); `complex` — any complex number (at a place any residue; in ℍ a generic quaternion); `slice` — in ℍ, co-sliced quaternions (in ℂ, any complex number); `plane` — internal to the ℍ ledger, ℂ ⊂ ℍ. Defaults: `positive` through `alg`, `complex` from `C` on; a node may narrow or widen it, and a law unsound outside its domain says so in its reading cells. The engine snaps values that are real up to rounding onto the real axis before taking a log.

### 3.7 Schema nodes (LEGISLATION 29)

A `type: schema` node states a law for every value of a count parameter; the law and the derivation rows are **templates**: `X^{e}` — e juxtaposed copies of X (X a variable, `o`, `J`, `□`, or a bracketed group; e an expression in the parameters: `n`, `k`, `n-1`, `2k`, `2k+1`, `n+1`; `o^{n}` is the pile n); `Σ{j=a..b: F}` — the juxtaposition of F for j = a … b (an empty range is void). `schema_range:` gives the instances the engine checks (`n=2..8`; `n=2..7; k=1..n-1`). A derivation table whose header reads `| form (n = 1) | rule | note |` is a **base case**; the other tables are the **step**; an instance at the base value is the base table alone, at any other value the step tables alone — so a `hypothesis` row always points at a value already checked, and the range may not start below the base. The step may cite the schema itself at a smaller parameter with the rule `hypothesis`, whose note cites `[[N.induction]]` — the gap enters `uses` and the price. What the engine checks per instance: the law shadow, every row pair as an equality, the seam decree, the endpoints as forms, and for a `hypothesis` row that it is one application of the schema's own law at a smaller parameter in range (strong induction; variables kept as written). What it does not check: the passage to all n — that is the gap, priced; `NATIVE-BY-SCHEMA` records exactly this. Only the `law:` string and the form column are expanded; rule and note cells are kept as written. Cards draw one instance (`schema_draw:`, default n = 3).

**Over the place.** The parameter `p` is the place: `o^{p}` is the prime as a pile, `[o^{p}]` its log; the range is an explicit list, `p=2,3,5,7,13`, joined with a depth (`p=2,3; n=1..3`) or given as tuples where the depths differ (`(p,n)=(2,2),(3,1),…`); expressions may use `**`. Each instance is read *at its own place* to its depth. **Every** node whose range binds p cites `[[place.ostrowski]]` in `uses` — the import names the places and does not license the passage from the five tested to all of them, exactly as the induction gap prices the passage from a range to all n. A `decree` may be written over p and n (the void pile): checked at every instance, a rule at each, no derivation, no tape; an `import` may be too (Fermat–Euler), checked at every instance and priced as an import.

### 3.8 Meta nodes and witnesses

A meta node's Derivation is a statement table; its `witness:` script in `tools/models/` checks what the statements claim, exits 0 iff all hold, and prints one line per part; the node's rows name the parts. The checker runs every witness. A meta claim a witness computes is `verified: engine`; without a witness it is at most `hand`, and "Exact" is withheld (§8.2). A witness computes what the node cites — a row that names "witness part (k)" refers to a check the script actually makes.

### 3.9 Rendering

Canonical strings are drawn as nested boundaries: round → capsule, square → rectangle, angle → hexagon, the ordered square → a rectangle with dashed dividers between its entries, a constant → an italic letter. Beside the drawing: the ASCII string, the units form, the standard form. Type = colour; status = badge; verified = badge; band = tag; refuted content struck through. Each card shows its 𝕁₁ tape, its law at the places, its law in ℍ and its tape in ℍ, from the ledgers (§7.4).

---

## 4. Links, order and price

### 4.1 Links

**Back-links** (`uses`) are exactly the rules cited in the Derivation; they are the chart's edges. **Used-by** is computed. **See-also** is curated, drawn dashed. **Aliases** map ledger ids (JH-3, JO-12, JS-39, JP-1, Field prohibitions) onto nodes so the existing work is reachable by its old names (LEGISLATION 25). **Concepts** form the second index: `concepts/<slug>.md` holds a one-paragraph plain description; the generator lists under each concept every node that names it (LEGISLATION 5).

### 4.2 Order (LEGISLATION 18)

Dependency order is the spine (the `uses` DAG); rungs are the chapters; `order` is the walk, a total order refining the DAG, integers spaced by 10. A node may cite a node of a later rung only if that node's `order` is smaller — the walk order, not the rung, is what the DAG check enforces. `guide: shape-led | need-led` on every node records whether the step followed the shape of the forms or was pushed by what mathematics needed; the ratio per rung is rendered — it is itself a finding.

### 4.3 Price (LEGISLATION 11)

`price(n)` = the ancestors of n along `uses` whose type is `primitive`, `axiom`, `decree`, `import` or `gap`, together with every `guarded_by` along the way (a guard declared by an ancestor is inherited by price, never re-declared), partitioned into **base** (the three boundaries, the medium, James's three axioms) and **extra** (everything else). Rendered as "what it costs to write X". The concept index shows the cheapest price among a concept's forms.

**`guarded_by`** (LEGISLATION 28). A node declares `guarded_by: [mult.seam-decree]` exactly when its derivation relies on a clause of the seam decree, and the checker computes this from the derivation and enforces it both ways: **by content** — a unit step `[(X)] ↔ X` at a non-absorbing position, admitted because X stays on the principal strip over the whole domain, which the ℂ reading certifies; **by position** — a unit step in an absorbing position whose content leaves the strip for some value of the domain (a seam step, saved by the enclosing instance); **free** — an absorbing on-strip unit step, any derivation with no unit step, and a unit step on void or hole content (`mult.log-of-one`, `mult.hole-instance`). The clause is shown on the card; status is unaffected (a guarded theorem is `NATIVE`). In 𝕁₁ the guards dissolve into receipts (§7.3): by position → absorbed; by content at depth 0 → posted; by content under a square → an import, still a guard.

---

## 5. Settings (LEGISLATION 8)

A **setting** is a named set of nodes in force. An extension is itself a node (a new axiom, primitive or decree), and the setting is the set that includes it — an attribute of every law (its `holds` cell), not a branch of the chart.

| setting | = classical ∪ … | source |
|---|---|---|
| `classical` | three boundaries, Involution, Distribution, Inversion, and two decrees: the undefined forms (`<□>`, `[□]` excluded: `mult.hole-exclusion`) and the seam discipline (`mult.seam-decree`, stated in the ℂ reading because no syntactic signature exists — `mult.seam-signature`; James's J-discipline is its special case, `C.james-discipline`). The ℂ import is provisional until `J1` (LEGISLATION 27) | James 1993; Book One I–II |
| `J1` | Involution split: the counit `([A]) ≡ A` strict (`J1.counit`), the unit `[(A)] ≃ A` witnessed by a receipt (`J1.unit`); the period form ω := `[()]` kept rather than erased; closure `(ω) ≡ ()` and absorption `(ω A) ≃ (A)` theorems; L0 linearity, the pole read by polarity, the ψ-wall as decrees; von Staudt–Clausen the one import. Three equalities ≡, ≃, ≈ | Number at Height One; 𝕁 v3.1; LEGISLATION 30 |
| `JP` | the enriched calculus read at a finite place: the void pile `o^{p**n} ≃ void` declares the page (`place.void-pile`, a decree over p and n); the reading at p (`place.reading`, an import); the discipline of the page — the page's equality does not pass through a square, so a law of the page is ≃ and a page step is graded by position; the lens and the completion are the rung's gap (LEGISLATION 31) | Part II: Calculus of Number at a Place; rung `place` |
| `JH` | the ordered square `[ ; ]` (`H.ordered-bracket`, a fourth boundary) with splice, the unit entry and two-sided distribution as axioms and two conditional axioms — the exchange of commuting entries (`H.commutation`) and the collapse of co-sliced entries to the classical square (`H.collapse`, witnessed); the second seed `Jj`, `(Jj) ≐ <o>` (`H.seed`, decree); anticommutation O9 (`H.anticommutation`, the one non-commutativity axiom); ordered cancellation a theorem; the seam guard `H.seam-guard`; receipts with a direction (`H.slice-wall`) (LEGISLATION 32) | the JH-Calculus report; rung `H` |
| `JO` | + tree-shaped nesting, the alternative laws, a third seed: the rung's gap (`H.octonion-gap`), not yet laid | Book One Part IV |
| `JS` | + the fourth doubling, the octave grade | JS-algebra-sedenionic |
| `extrusion` | + brace `{ }`, gauge principle G0 | 𝕁 v3.2 |
| `field` | + ι or κ adjunction, boost seed | The Field, Vol. I |

Every law carries a `holds` cell for every setting (§2.2). A setting that is not yet built is still a legal column, `untested`, until a ledger computes it.

---

## 6. Readings

A **reading** is a model. The default gloss is `C`; the F₁ roads enter as readings first (`finset`, `lambda`, `CC`); `logic` covers LoF / Existential Graphs (§2.3 for the cells). Readings are how the moduli-stack idea (LEGISLATION 17) enters without a new primitive: a form is one thing, its readings are the points of its moduli. James 1993 is the ground truth for `classical`; Bricken's constructs enter as attributed notes tagged by volume and as nodes only where they add a law (LEGISLATION 9).

The engine computes with five readings, each a `Reading` object with one interface (§6.5): ℂ (classical), 𝕁₁ (§6.1), the page at a finite place (§6.2–6.3), ℍ at ∞ (§6.4) and ℍ at a finite place (§6.4). Each is the 𝕁₁ reading moved to its place and algebra.

### 6.1 The 𝕁₁ reading (LEGISLATION 30(b′))

Values are complex numbers. The log of *exactly one* is the chosen lift ω = 2πi; every other log is principal. This is compositional — a square's value depends only on the value inside it — so the strict rules are exact in every context; `[()]`, `[(ω)]`, `[(J J)]` all read 2πi, and the crack's non-void receipt sits at the log of one, `[()] → void` (`mult.log-of-one`). The **receipt of a step** is the lattice element it forgets: value before minus value after, in units of ω, sampled over the node's domain (for a step between two instances the contents are compared). The reading has **exceptional points** — where a content is exactly one its log reads ω — probed at each variable's lattice values (1, −1, ½, 2, i within the domain) and named on the tape.

### 6.2 The reading at a finite place (LEGISLATION 31)

A value is a number part (a residue of the page, mod pⁿ), a count of the prime's log `[p]`, and a count of the torsion log J_p; `[ ]` splits a number into the three and `( )` reassembles them where it can — the number part on the radius p·ℤ_p (4ℤ₂), the counts whole. Five conventions (`place.reading`): the log of *exactly one* reads the place's period ω_p = (p−1)·J_p (2·J₂ at 2), every other log principal; a fraction of a torsion count is taken in 0 … p−2 (0, 1 at 2) — the *principal root* of the place, canonical on the principal units and a convention elsewhere; the generator of the torsion is the Teichmüller lift of the least primitive root (−1 at 2) — a convention like 2πi over −2πi; a formal element's log is a formal symbol that a count scales, and the product of two formal elements has no value (weight 2); counts scale formal elements only when exact.

**Depth and precision.** The page's depth n is what equality is mod; the engine's working precision N is the depth plus a margin of as many shells again (`default_depth(p)`: 17 at 2, 11 at 3, 8 at 5, 6 at 7, 5 at 13), so that a log that loses shells is still read to the depth; a value that has lost more than the margin cannot be judged (`BeyondPrecision`: the sample is dropped, never judged). "Exactly one" is decided at N. A law exact at N is exact at every smaller depth. **The radius** is the standing proviso of every instance: a sample whose instance content falls outside it is retried on the radius (every variable times p, 4 at 2) and, if still outside, is formless for that sample — as is a sample that is not a form for a selection reason (a fraction of the period that is not a form at p, the reciprocal of the prime, weight 2). The exceptional points are probed by domain as at ∞ (a variable exactly one, its negative for a real variable, the void pile pⁿ) and a failure there is marked `·exc`.

### 6.3 The discipline of the page (LEGISLATION 31(g))

The page's equality — agreement mod pⁿ — passes through juxtaposition, angles and instances, **not through a square**: `[o^{p**n}]` is n·[p], `[void]` is the pole, the log of a non-unit loses as many shells as its count of `[p]`. The laws of the page — the void pile and what follows from it by the page's equality alone (residues, minus one as a pile, Fermat–Euler, division by a unit, the prime power, the geometric doll; `PAGE_RULES`) — are ≃, never ≡, and a page step is graded by position (§7.3). The pole is the limit end of the count of `[p]` — no finite count is it; the instance of n·[p] is the void pile at depth n (`place.prime-power`, `place.two-ends`).

### 6.4 The ℍ reading, at ∞ and at the places (LEGISLATION 32)

**Breadth is commutative.** `[A][B]` and `[B][A]` are one form, so any reading in which `([A][B])` is a product makes it commute; in ℍ that encoding is A·B only for co-sliced contents (`H.no-go`, the Slice theorem). A non-commutative product lives in *depth*: the ordered square reads as the log of the ordered product, `([A ; B])` is A·B. A law of the ordered square written with vector entries is a **family** of rules, one per shape of the list; the engine instantiates each family for lists of up to five entries (`tools/licences.py`, `FAMILIES`); the node's derivation proves the shape its law states.

**At ∞** (`tools/quat.py`). A value is a quaternion; `[ ]` is the principal log L(q) = ln|q| + θu, θ ∈ [0, π], with **J-pinning**: L(−r) = ln r + πi, so that the one form `[<o>]` has one value, and the log of exactly one is the pinned ω = 2πi; an ordered square is the log of the ordered product of its entries' values; `Jj` reads πj. The period lattice is Λ_ℍ = {2πk·u}: a receipt carries a direction, and `equal(≃)` tests whether a difference is a lattice element in *any* direction — so ≃ in ℍ is not a congruence through an instance (A ≃ A Jj Jj while `(A)` and `(A Jj Jj)` differ for A off the slice of j); what keeps the tapes sound is the value check of every absorbed step at its paying instance (§7.3). The domains: the real ones are central; `complex` is a generic quaternion; `slice` is co-sliced; `plane` is ℂ ⊂ ℍ. The Slice Principle (JH-4) — on a slice the classical calculus holds with J → J_u — is a substitution the forms do not make: J and ω are pinned to i, so a trunk law that mentions them holds verbatim on the **plane** and is carried to the other slices by the symmetry of ℍ, not by the forms. A **seam displacement** is a difference that is no lattice element though the instances agree (πu against πi): measure zero at ∞.

**Conditional laws.** `H.commutation` (`[P ; Q] ≐ [Q ; P]` when the *values* commute) and `H.collapse` (`[P ; Q] ≃ [P] [Q]` when the *logs* commute). The reading checks the premise at every use on the entries matched as P and Q (`CONDITIONAL`, `premise_holds`); a step whose premise fails, or whose premise no sample could test, is `absent [premise]`. The two premises differ by the pinning: −1 and j commute as values, their pinned logs do not, so `[<o> ; j]` exchanges and does not collapse. The collapse is also witnessed (`WITNESSED_H`): it posts a receipt by position exactly as the unit does.

**At a finite place** (`tools/quatplace.py`). Hamilton's quaternions ramify at exactly 2 and ∞ and split at every odd p (`H.ramification`). At an **odd p** the quaternions of the page are 2×2 matrices over ℤ/pⁿ: Hamilton's relations hold, the norm is the determinant and is isotropic — a nonzero quaternion with norm ≡ 0 is a zero divisor with no reciprocal and no log (the norm-null species, JH-20, refused by name). At **2** the page is the Hurwitz order O (all-integer or all-half-odd parts) mod a power of π = 1 + i: v(π) = ½, the valuation v(q) = v₂(N(q))/2 runs in half-shells over the whole algebra, the residue field O/πO is 𝔽₄, the radius of the instance is v ≥ 3/2, and the 24 Hurwitz units — the torsion of the *global* order — are the torsion the reading names; the local order O₂ has infinitely many more (the conjugates of i, j, ζ), which the reading does not read. A value is a number part, a count of the prime's log (`[π]` at 2, in halves), and a **torsion part**: (direction, count) pairs over the Hurwitz units, antipodal directions one direction with a signed count, the pinned −1 at (i, 1), the central Teichmüller log J_p at odd p, and a *carrier* for any other unit of finite order prime to p (its Teichmüller lift, whole counts only). The log of a unit: strip the prime's power (on the left at 2, q = πᵐ·unit, as the instance rebuilds it), then a torsion factor t with the rest t⁻¹·unit principal — and **t must commute with the rest**, so that the log is a sum of two logs whose negation is the log of the inverse; a unit whose torsion and principal parts do not commute, or whose reduction has order divisible by p, has no log — *owed*, and named in the refusal (at 2 nearly every unit of O₂; the rung's structural laws read `none` there and `guarded` at odd p, the laws whose variables are central `exact` everywhere). The log is read at the working precision, so on the quaternion page the digits past the depth decide the *existence* of a log, not only its value. Since π is not central, a central number acquires a torsion part from its spelling (2 = π²·(−i)), so `[oo][oo]` and `[oooo]` agree mod the period at 2, not exactly. The `slice` domain at a place is co-sliced by construction. The **seam** has positive measure on a page (a product of co-sliced units is a negative principal unit as often as not, its log pinned to i while the sum of the logs lies in the slice): the ledger's verdict `seam`, a guard.

### 6.5 The `Reading` interface

Every reading the engine computes with provides: `evaluate(form, env)`; `random_env(names, domain, rng)` and `probes(names, domain, rng)` by the domains of §3.6; `equal(a, b, equality)` for ≐/≡ and for ≃ (mod the reading's periods); `seam(a, b)` (not equal mod the periods, instances agree); `k(a, b)` — the receipt in units of the period, `None` when the difference is no lattice element; `direction(a, b)` where receipts have one; `premise(name, env, domain, rng)` for conditional rules; `is_pole`, `fmt`, `skip_errors` (what counts as formless), and `noncommutative` where absorbed steps must be value-checked. A new setting arrives with its reading (§11.3).

---

## 7. The engine

### 7.1 The shadow check

Every object-level law parses and is sampled on random values of its domain in the node's setting's reading; a definition's `gloss_check` is compared with the form's value; every consecutive pair of rows of every derivation table is an equality in the declared sense on random instantiations; for an object-level theorem or schema, *one* table runs from one side of the law to the other **as forms**. Samples on which a form has no value (formless, past the precision, overflow) are skipped — and a law no sample can judge **fails** (§2.4). Exceptional points are probed as §6 says. The seam decree is checked on every row of a classical node (`guarded_by`, §4.3). In 𝕁₁, at the places and in ℍ, the decree is not in force: receipts replace it.

### 7.2 The derivation checker (`tools/prover.py`, `tools/licences.py`)

Every row must be *obtained from the previous one by the rule it cites*: each cited law is a rewrite in either orientation at any position (associative-commutative matching over the multiset of boundaries; inside the entries of an ordered square, never across entry boundaries), and the next form must be reached in at most fourteen applications. A numerically true step with the wrong rule fails. Rules: a node's `law:` (and its `EXTRA_RULES`, laws the node proves in a second table — the two-sided norm); a schema's instances at the citing node's own place and depth; a family's shapes (`FAMILIES`); `lemma` rules from the node's earlier tables; a `hypothesis` rule at a smaller parameter. The identity rules (`definition`, `substitution`, `congruence`, `medium`, `name`) license a row that is the same form once sugar is expanded. The search is a focus-guided beam from both ends, never joined: a strict path the search misses can make a grade *worse* than the truth, never better — the author's remedy is to split the row. What the checker does not do: read the note, judge whether the derivation is the intended one, or anything about the prose — the referee's job (§11.2).

### 7.3 The receipt prover (`tools/j1.py`)

For every derivation the engine asks for the cheapest licensed path — strict steps only, then absorbed, then posted, then anything — and grades each step by the rule and the position:

- **strict** — the counit, Distribution, Inversion, the medium, the hole rules, the strict rules of the ordered square (splice, the unit entry, list distribution, anticommutation, the seed, the definitions, commutation); a theorem whose own tape is empty; a unit step on *pole-valued* content (no winding to record: Dominion is ≡).
- **page** (at a place only) — a step by a law of the page with no square anywhere above it. A page step with a square above it is **measured at every square above it**: an import where no square's value changes at the generic points, absorbed or posted where some change by one period (the outermost changed square posts the receipt, and the instance directly outside it pays it — an import when a further square lies above that instance; posted at depth 0), absent otherwise. A page theorem reused keeps its standing as a floor; page, like absorption, is never promoted to ≡ by reuse.
- **absorbed** — the unit `[(A)] ↔ A`, absorption `(ω A) ↔ (A)`, the collapse, or a theorem with posted receipts, applied *directly inside an instance, through angles at most*: the instance pays the receipt; value-exact. A theorem whose receipts were all absorbed is absorbed when reused, at any position, and a law that uses it is ≃.
- **posted** — a unit step, a collapse, or a posted theorem at depth 0: the receipt stays on the tape; the two forms agree mod Λ.
- **import** — a unit step or a posted theorem under a square before any instance, whose receipt is void at the generic points of the domain (≃ is not a congruence through `[ ]`; the step is sound by a fact of the reading the calculus cannot see). The exceptional points are probed and named; the law stays `guarded`. The measurement at every square above (the page rule) is the criterion stated for both ∞ and p; at ∞ it coincides with this receipt check on the eight trunk laws it would touch (the experiment of 2026-10-13, LEGISLATION 31(g)), so the engine keeps the receipt check as its ∞ case.
- **absent** — a receipt that is not void where it must be; a rule the setting does not have; a conditional rule whose premise fails (`premise`); in ℍ a cross-slice absorption or a seam displacement at depth 0.

**In ℍ.** Receipts carry a direction. Every absorbed step is **checked by value** at its paying instance — the innermost instance above the redex, through angles, for a primitive witnessed rule and for a unit-shaped step of a theorem; the two sides themselves for a theorem reused on another shape — and is `absent [cross-slice]` when the instance no longer agrees (the first non-commutative wall, `H.slice-wall`). A receipt that is no lattice element is the seam: `absent` at depth 0, paid and recorded `seam` directly inside an agreeing instance (`H.seam-guard`). The trunk's derivations are re-graded on the plane, and a trunk theorem reused in rung `H` is value-checked on the citing node's own contents.

A node's grade is its worst step; the cell it implies: strict, page or absorbed → `holds`; posted → `holds-mod-Λ`; import → `guarded`; absent → `fails` (or `guarded` when every absent step is formless). In `J1`, `JP` and `JH` the node's equality symbol and its own cell must be what the tape earns. **What the tape does not do:** receipts are sampled (24 random points plus the probes), so `k = 0` is evidence, not proof; the tape is a multiset (exchange is free); a path re-graded in another reading is the path found cheapest at ∞, so it can be too pessimistic, never too generous.

### 7.4 The ledgers (written by the engine; `census/`)

| ledger | file | reads | computes |
|---|---|---|---|
| 𝕁₁ | `j1-ledger.md` | every derivation of the chart at ∞ in the 𝕁₁ reading | the J1 cell of every node; the tape on each card |
| place | `place-ledger.md` | every trunk law at p = 2, 3, 5, 7, 13 on the domain dictionary of §3.6, every licensed path re-graded there | the JP cell of every trunk node; rung `place`'s nodes graded at their own place as they are checked |
| ℍ | `h-ledger.md` | every trunk law in ℍ on its domain and on generic quaternions, every licensed path re-graded on the plane | the JH cell of every trunk node; rung `H`'s nodes graded in ℍ as they are checked |
| quaternion place | `h-place-ledger.md` | every law of rung `H` at the five places in the quaternion reading; every law of rung `place` in that reading at its own place, on the centre and on generic quaternions of the page | the JP cells of rung `H`; the JH cells of rung `place` |

Cell logic, common to all: `replaced` when the law is formless at every tested point; `fails` when it fails somewhere it is a form, or its tape is absent with a non-void receipt; `guarded` when some sample is formless, the law is on the seam, or the tape imports; `holds-mod-Λ` when the tape posts or the law holds mod Λ; else `holds`. The hand cell is compared under the ACCEPT rule (§2.2). Declarations and meta theorems are not computed by a ledger; their cells are read by hand from the witnesses and say so. `tools/check.py --only <prefix>` grades the cited closure first, so that its tapes agree with the full run's; the full run writes the ledgers.

### 7.5 Witnesses

`tools/models/*.py`, one per meta node (§3.8); `h_common.py`-style helpers may be shared. A witness that reads an engine output (the 𝕁₁ ledger, `J1.classical-floor`) runs after the ledgers are written.

### 7.6 The census

`tools/census.py` enumerates every form up to a size bound (≤ 3 boundaries, no variables), canonicalizes, evaluates in the `C` reading, and classifies each form as `numeral` · `reduces` · `new` · `hole` · `excluded` (contains `<□>`) · `undefined` (contains `[□]`). Every `new` form must be assigned to a node or listed in `census/open-forms.md`; `excluded` and `undefined` forms are assigned to the exclusion decree. Ownership: a node's explicit `forms:` or a definition's/primitive's law sides and an axiom's or decree's left-hand side, earliest `order` first; then the numeral patterns; then a theorem's left-hand side — never any right-hand side. Raising the bound is a standing task; the census is re-run by the checker.

### 7.7 What the engine checks, in one list

Required fields and enums, id = filename, unique order, required sections, Plain ≤ 45 words (warned); every link resolves; `uses` = the citations; the DAG by order; the body's settings/readings tables agree with the front matter; the law shadow and gloss; every derivation row parses, cites allowed rules, is an equality, is licensed; `given` opens tables only; endpoints as forms; hypothesis rows; the seam decree and `guarded_by` both ways on classical nodes; the tapes, the equality symbol and the cells in the graded settings; every witness exits 0; `verified` below `engine` on a theorem (warned: Exact withheld); the census fresh and assigned; the four ledgers, with the ACCEPT rule. Exit 0 iff no failures.

---

## 8. Status, verification, dates

### 8.1 Status (LEGISLATION 12)

| status | meaning |
|---|---|
| `NATIVE` | derived inside the setting from its own axioms; or a primitive/axiom of the base three; a guarded theorem stays `NATIVE` |
| `NATIVE-BY-SCHEMA` | holds for every value of a count parameter by an induction the calculus cannot do natively: each instance in range engine-checked, the passage to all n priced as the gap |
| `NATIVE-BY-DECREE` | the *statement* holds because a decree was issued — exclusions, the decrees themselves, the meta theorems about the decree-governed calculus |
| `IMPORTED` | used, not derived; the import named and dated |
| `ANALOGY` | a correspondence asserted but not an equation of forms (24 ↔ M(2)) |
| `CONJECTURE` | stated, unrefuted, undemonstrated |
| `REFUTED` | shown false; kept, struck through, attached to the law it was mistaken for |
| `ABSENT` | the concept has no form (gaps) |

### 8.2 Verification tier (LEGISLATION 20, 21)

`none` → `hand` (a written derivation or meta argument with no script) → `engine` (every step shadow-checked and licensed, the tables connecting the law's sides as forms; or a meta claim checked by a named witness) → `numeric` (a high-precision identity beyond the shadow check) → `lean` (a Lean declaration, node id = declaration name; a later scoped expansion over the classical trunk). **"Exact" is withheld until `engine`**: a node whose `verified` is below it renders with a hollow badge whatever its status says.

### 8.3 Two dates

`known_since` — when the mathematics was known (James 1993; "ancient"; Hamilton 1843; "this chart, 2026-10-07" when nothing earlier is located — and then a literature check is a standing obligation). `entered` — when it entered the program.

---

## 9. Gaps, owed, refuted

### 9.1 Gaps (LEGISLATION 13, 14)

Two kinds: `kind: concept` — a mathematical concept with no form (induction, order, a metric at ∞, weight); `kind: form` — a form the calculus can write that nobody has read yet. Forms containing `[□]` or `<□>` are not gaps: both are excluded by decree. Every gap node's **Plan** has exactly these fields: candidate form(s); law(s) to add, and type; nativity criterion (stated in forms and ≐ only); refutation test; meta-move? (whether the plan needs the calculus looked at from outside, and which); owner thread; rank (reading < definition < theorem < decree < axiom < new primitive). The first gaps the reader meets, `N.induction` and `N.order`, are meta-level and resolved by meta-moves (the schema machinery prices the first).

### 9.2 Owed (LEGISLATION 33(d))

An obligation the chart has not met — a derivation it cites by witness, a reading it refuses by name, a cell read by hand — is recorded on the node where it falls due, in its `owed:` list: short strings of the form `YYYY-MM-DD: what is owed` (checked), rendered on the card and collected by the generator into one list beside the gaps. The node's prose may say *owed* as well, and a reading that declines names the owed case in its refusal; ROADMAP's "what the rung does not do" summarizes. A referee's MINOR finding that is not repaired becomes an owed item. An owed item is closed by removing it when the obligation is met — with a line in the node's Notes or Refuted readings saying what met it.

### 9.3 Refuted readings (LEGISLATION 15)

Refutations are kept, never deleted: attached to the node they were mistaken for, struck through, with date and witness; the generator collects them into one searchable list. A refuted reading of a rule's premise, a derivation, or a cell stays on the node that carried it.

---

## 10. Scope

### 10.1 Tiers (LEGISLATION 16)

**A** number and algebra (void → ℕ → ℤ → the square → ℚ → algebraic → J, ℂ → 𝕁₁ → ℍ → 𝕆 → 𝕊) in full; **B** analysis (exp–log completeness, shift and derivative, metric and order, places and p-adics, the adelic page) in full; **C** logic (LoF, Existential Graphs, polarized readings) as one strand; **D** structure (`() ⊣ []`, ω/Λ, im J, Bott, moduli, the F₁ road) as far as the F₁ road needs; **E** The Field as pointers.

### 10.2 Rungs, in walk order (LEGISLATION 29)

`void` → `N` → `Z` → `mult` → `Q` → `alg` → `C` → `schema` → `J1` → `place` → `H` → `analysis` → `J2` → `logic` → `struct` → `F1` (→ re-entry to `void`), with `O` and `S` a branch off `H`; `field` a side chapter. Built through `H` (233 laws, 2026-10-13); next `analysis` (LEGISLATION 33(e)). The additive-first order follows the Iconic Mathematics scope and sequence: each stage adds an idea, not necessarily a boundary. Why the order (ROADMAP §2): `schema` first because every target needs statements over n; `J1` before everything else because it pays off the chart's biggest import; `place` before `H` and `H` directly after it so the first non-commutative wall is read against the places; `analysis` next because "at every place" needs a metric; `J2` as a rung of gaps and witnesses for the level-2 question; `logic`, `struct` before `F1`; `F1` last, as the fibre over the trivial place.

### 10.3 Trunk and roads (LEGISLATION 19)

The 𝕁₁ road is the trunk: ℕ → ℤ → ℚ → algebraic → ℂ → 𝕁₁ → finite sets / sphere spectrum → F₁. The adelic page (JP) is the second road into F₁. The division-algebra branch (JH/JO/JS) rejoins at 24, marked `ANALOGY` until a form equates them (`H.twenty-four`). Analysis and The Field are branches.

### 10.4 What does not change

One law per node; every derivation engine-checked and licensed; referees before acceptance; the price computed, never asserted; readings and settings filled honestly (`untested` is a legal cell where nothing computes it; a confident wrong cell is not); the thesis as ground truth for `classical` and the ledgers (JH, JO, JS, JP, 𝕁 v3.x) for the branches, each cited by page or rule number.

---

## 11. Process

### 11.1 Adding a law

Copy the nearest node file; give it the next free `order` in its rung and an id that matches the filename; write the `law:` in canonical strings and the `units:` in standard notation; write the Given–Rule derivation citing the licensing node on every row; set `uses` to exactly the ids cited in the Derivation; fill the `holds` and `readings` tables (`untested` where no ledger computes the cell); run `tools/check.py` — a theorem becomes `verified: engine` only when it passes; run `tools/build.py` and look at the card. A law over every n is a `schema` (§3.7); a meta claim gets a witness (§3.8).

### 11.2 Adding a rung — the rung protocol (LEGISLATION 33(b))

A rung lands in this order, each step a gate for the next:

1. **Plan.** A short plan, sent to Lui before building: the node list with types and the expected cells per setting, the engine and ledger work, the decisions it proposes (as a draft LEGISLATION item with defaults), what it leaves owed. Kept as `docs/plans/<rung>.md`.
2. **Nodes and engine.** Nodes written as above; the engine extended where the rung's setting needs a reading, a rule family, a grade or a ledger (§11.3); witnesses for every meta node.
3. **Full check, zero failures.** `tools/check.py` exits 0; the ledgers are written; `untested` is gone wherever a ledger computes.
4. **Referee pass.** An independent agent that has not seen the drafting attacks derivations, cells, engine soundness, the mathematics and the documents, and reports findings as BLOCKER (a false law, a collapse of the calculus, an unsound grade) / MAJOR (a wrong claim, a wrong cell, an unsound path the chart does not yet take) / MINOR (a wrong sentence, a stale number, a weak witness). Blockers and majors are repaired before the commit; minors are repaired or become owed. The report is kept as `docs/referee/<rung>.md`, and the repairs are recorded in the nodes' Refuted readings where they refute something. A rung that adds a boundary gets two independent passes.
5. **Documents.** The SPEC's increment (new rules only, stated in force), the LEGISLATION item (pending), ROADMAP's "as built" section and "next", README's Status entry (latest first), the generator's lede for the rung.
6. **Release.** Check (0 failures) → build → commit with the session's attribution → republish the artifact → zip the repository and send it. Lui pushes to GitHub from his own Claude Code, confirms or amends the LEGISLATION item, and flips `understood` as he walks.

### 11.3 Adding a setting (LEGISLATION 33(c))

A new setting comes with: its nodes (the extension as axioms, primitives, decrees and the theorems they settle); a **reading** implementing §6.5, as the 𝕁₁ reading moved to its place and algebra; a **ledger** that reads every object-level law of the trunk in it and re-grades every licensed path there, and reads the earlier settings' rungs in it where that is meaningful (as `H` read `place`); the ACCEPT rule applied to its column, so that its cells are computed, not typed; its grades on the cards; witnesses for the meta theorems that state what the reading is. The trunk's cells in the new column are filled from the ledger, each `replaced` cell naming the law of the new setting that takes over.

### 11.4 Iterating this specification (LEGISLATION 33(a))

The SPEC is versioned: a rung lands with an increment (v2.1, v2.2, …) that adds the rules its setting needs, stated once and in force, and never a narrative of how they were found — history goes to README's Status, ROADMAP's "as built" sections and LEGISLATION's amendments. A decision changes only in LEGISLATION, by a dated amendment under its number; the SPEC then restates the rule. The version in force is named at the top; the register in §14 lists what is pending. Lui brings the current SPEC into his project when a rung is to be added, and the session that adds it returns the next increment.

### 11.5 Roles

The session proposes, builds, referees and repairs; it never pushes. Lui confirms or amends decisions, pushes, and walks the chart. A pending decision is implemented as the proposal so the chart is never blocked on it, and reversed if he decides otherwise.

---

## 12. Repository and tooling (LEGISLATION 22)

```
boundary-chart/
  SPEC.md               this file
  LEGISLATION.md        the binding decisions, by number, with their status
  ROADMAP.md            the path to the three targets; each rung as planned and as built
  README.md             how to add a node, run the checker, build the site; the status by date
  references/           James 1993, the ground truth for the classical setting
  nodes/<id>.md         one law per file
  concepts/<slug>.md    one paragraph per concept (optional per concept)
  census/               generated: size-le-3.md, open-forms.md (hand-kept), j1-ledger.md, place-ledger.md, h-ledger.md, h-place-ledger.md
  docs/plans/, docs/referee/   a rung's plan and referee report (from rung H on)
  tools/
    forms.py            parser · canonicalizer · ℂ evaluator · random instantiation (the ordered square, the constants)
    nodes.py            front-matter + section parser shared by check and build
    schema.py           templates and ranges (§3.7)
    prover.py           the rewrite engine behind the derivation checker
    licences.py         licensing of every row by the rules it cites; rule families; extra rules
    j1.py               the receipt prover: grades, positions, receipts, premises
    place.py            the reading at a finite place      placeledger.py   the place ledger
    quat.py             the ℍ reading at ∞                 quatplace.py     the quaternion reading at a place
    hledger.py          the ℍ ledger and the quaternion place ledger
    check.py            the engine (§7.7)                  build.py         nodes → site/index.html
    census.py           the small-form census              models/          witnesses for meta theorems
  site/index.html       generated; publishable as an artifact
```

Zero dependencies beyond Python 3. `python3 tools/check.py` (flags: `--only <prefix>`, `--seed`, `--trials`, `--no-census`, `--no-licences`, `--no-places`) must exit 0 before any node is marked `engine`; `python3 tools/build.py` regenerates the site; `python3 tools/census.py` regenerates the census. The repository is the source of truth; the published artifact is a build product; the zip is how it travels to Lui.

---

## 13. The visual encyclopedia (LEGISLATION 23)

**v1 (built):** every form drawn from its canonical string; the chart as a zoomable, clickable DAG layered by rung with the re-entry edge drawn as a loop; the concept index; the gap list with plans; the refuted list; the walk with its progress bar; each card's tapes and ledger lines. **v2:** a live instrument per law — apply-this-law on an editable form — reusing the rewrite calculator, scoped node by node. **Game skin (deferred):** prerequisites = `uses`; "unlocked" = `NATIVE` with a derivation; the player is at a node and must reach the next by rewriting. All derivable from the files; nothing is stored for it now.

---

## 14. Decisions

The register is `LEGISLATION.md`; this section says what stands, which forks were taken, and what is deferred.

**In force (decided):** 0–29 (2026-10-03/04); the amendments to 30, and 31, 32, 33 — confirmed 2026-10-13 (Lui: "Fold all recommended actions into the spec, noting deferrals and forked paths taken"), each as recommended on the ballot of that day. **Defaults** (stand unless Lui objects): rung `mult` after `Z`; medium facts as `primitive`/`medium`; meta nodes count as laws; the domain defaults of §3.6; the two undefined forms as one decree and the ℂ reading as an import; rule names after James 1993 / Book One with Bricken's as aliases.

**Forked paths taken, and deferrals** (the alternative each was weighed against is in LEGISLATION's item):

| item | the path taken | deferred or noted |
|---|---|---|
| 30(b′) | the compositional 𝕁₁ reading (§6.1): the log of exactly one is ω; five trunk laws stay `guarded` at their exceptional points | — |
| 30(f′), (d′), (a′), (c′) | the pole exemption; annihilation as a gap; reuse of an absorbed theorem is ≃; the heuristic search accepted as pessimistic | — |
| 31(a) | a place is a pile declared void; the lens not drawn | whether `[x ; y]` of rung `H` is the lens of `place.completion` — settled at `analysis` or `J2` (owed on `place.completion`) |
| 31(b)–(f), (h) | the 𝕁₁ reading at p; Ostrowski as the price; the trunk's JP cells computed; the wall a theorem of the reading; the generator of the torsion by table | 31(f) is discharged by 32(e) |
| 31(g) | the discipline of the page, with measurement at every square above | the offer (the same measurement for unit steps under a square at ∞) was *run as an experiment* on 2026-10-13: the eight trunk laws it would touch stay `import` — no square above changes — so the measurement is the rule stated for ∞ and p alike (§7.3) and no cell changed; the engine keeps the receipt check as its ∞ case |
| 32(a)–(d), (f) | the bill; the collapse's premise on the logs; directional receipts and the seam payment; the seam guard as its own node; 24 as `ANALOGY` | — |
| 32(e) | the prime on the left at 2; a torsion factor must commute with its principal rest; the seam as a ledger verdict | the extension that reads non-commuting torsion factors (negation by conjugation) is owed on `H.split-place` and `H.ramified-place` |
| 32(g) | **split**: one law per node (LEGISLATION 5) — `H.rigidity-dichotomy`, `H.half-phase`, `H.120-law`, `H.interference` are their own nodes with their own witnesses (44 nodes on the rung) | the sphere of phases at a finite place is owed on `H.phase-sphere` |
| 32(h) | the octonions as the rung's gap | an octonion reading of rung `H` at ∞ (splice failing), computing the JO cells before any boundary is designed — when the `O` branch's turn comes (owed on `H.octonion-gap`) |
| 33(a)–(c) | the spec versioned (§11.4); the rung protocol with severities as gates, two passes for a rung that adds a boundary (§11.2); a setting comes with a reading and a ledger (§11.3) | — |
| 33(d) | owed items as the `owed:` field (§9.2) — implemented: checked, rendered, collected; seventeen nodes carry one, nineteen items in all | — |
| 33(e) | the next rung is `analysis`; then `J2`; the `O` branch deferred | the `finset` back-fill of the trunk (LEGISLATION 2) is reading work that may run alongside `analysis` |

## Appendix A — Changelog of this specification

- **v1.0 (2026-10-03).** The data model, the node format, links, settings and readings, status, price, gaps, scope, verification, the build plan; the pilot of `void`, `N`, `Z`, the opening of `mult`; then the trunk to `C` with five referee passes.
- **v1.1 (2026-10-04).** The `schema` type (§3.7); the derivation checker (§7.2); rung `J1` and the receipt prover (§7.3), LEGISLATION 30.
- **v1.2 (2026-10-06).** Rung `place`: the reading at a finite place, the place ledger, the discipline of the page (§6.2–6.3), LEGISLATION 31.
- **v1.3 (2026-10-07).** Rung `H`: the ordered square, conditional laws and rule families, the ℍ reading at ∞ and at the places, the ℍ ledgers, the referee's repairs (§6.4), LEGISLATION 32.
- **Section map, v1 → v2.** §1 vocabulary → §1; equalities (end of §1) → §2.1; §2.1–2.6 the node → §3.1–3.6 (§2.3 front matter → §3.3; §2.4 body → §3.4; §2.5 canonical strings → §3.5; §2.6 rendering → §3.9); §2.7 schemas → §3.7; §3 links → §4.1; §4.1 settings → §5; §4.2–4.3 readings, Bricken → §6; §4.4 the place ledger → §6.2–6.3 (the reading) and §7.4 (the ledger); §4.5 the ℍ reading → §6.4 and §7.4; §5.1 status → §8.1; §5.2 verification → §8.2; §5.3 dates → §8.3; §5.4 price → §4.3; §5.5 the tape → §7.3; §6.1–6.3 gaps → §9.1; §6.2 census → §7.6; §7 refuted → §9.3; §8 scope → §10; §9 order → §4.2; §10 process → §11; §11 repository → §12; §12 visual → §13; §13 seeding → README (Status); §14 defaults → §14. A bare "§x.y" in a node's prose written before 2026-10-13 is a v1 number.
- **v2.1 (2026-10-13, later).** Every pending decision confirmed as recommended (LEGISLATION 30′, 31, 32, 33); the forks and deferrals recorded in §14; the `owed:` field implemented (§9.2, §3.3); rung `H`'s folded laws split into their own nodes (§14, 32(g)); the 31(g) experiment run and its result stated (§7.3); two referee passes for a rung that adds a boundary (§11.2).
- **v2.0 (2026-10-13).** Consolidation: the rules stated once, in force; the cell vocabulary and the ACCEPT rule in one place (§2); the engine's checks in one list (§7.7); the `Reading` interface (§6.5); the process — the rung protocol, adding a setting, iterating the spec, roles (§11); the decisions register (§14). Proposes LEGISLATION 33. The history that v1 carried inline now lives in README (Status), ROADMAP (§5–§7) and LEGISLATION.
