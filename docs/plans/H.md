*The plan for rung `H` as sent to Lui on 2026-10-07, before building. As built: ROADMAP §7 and LEGISLATION 32 — three of the planned nodes (the rigidity dichotomy, the half-phase law, the 120° law) were folded into `H.phase-sphere` and `H.polar-form`; `H.hamilton` became eight theorems and a definition; the place conventions of 32(e) were found while building.*

# Rung `H` — the quaternions, read against the places (LEGISLATION 29)

Draft for ROADMAP §7 / SPEC §4.5 / LEGISLATION 32, written 2026-10-06 before the zip (aba3c49) arrived; to be folded into the repo and built, refereed, and recorded as 32 "pending Lui". Ground truth: the JH-Calculus report (Aug 2026, Layer 3 = the ordered abstraction), Book One's rung-four chapters, JS-ARITY-AND-IMPORTS (OC derivable), JP v0.2 (the ladder at p: seal table) and JP v0.3 (3) (the half-shell at p = 2).

## 0. What the rung is for

Three things, in this order:

1. **The first non-commutative wall.** 𝕁₁'s wall `(ω A) ≃ (A)` holds at every place (`place.wall`). At ℍ it holds *per slice* and fails *across slices*: exp(X + Y) = exp X · exp Y iff XY = YX (in-band rigidity, JH-1). The receipt prover must learn this — a receipt gains a *direction*.
2. **The quaternions as the height-one fibre's torsion** (29): η is the half-period J; ν's 24 is the Hurwitz unit group 2T. The rung ends on the 24 and faces `place.local-wall` at k = 1 (M(2) = 24 = 2³·3).
3. **The Hurwitz places.** ℍ = (−1,−1)_ℚ ramifies at exactly 2 and ∞; at every odd p it splits, ℍ ⊗ ℚ_p ≅ M₂(ℚ_p). So "read against the places" has two readings: at 2 the half-shell (v ∈ ½ℤ, π = 1 + i, residue field 𝔽₄, torsion 2T); at odd p matrices, with the norm isotropic — the norm-null zero divisors land on `<□>` (JH-20 meets the page). The 22 `untested` JH cells of rung `place` get filled from these two readings.

## 1. The bill (LEGISLATION 32(a), default)

Rung four's bill is **the semicolon, the seed, and O9** — three additions, nothing else:

| addition | form | note |
|---|---|---|
| the ordered bracket | `[x ; y]` (n ≥ 1 entries) | the log of the *ordered* product; `x·y := ([x ; y])`; splice `[x ; [y ; z]] ≐ [x ; y ; z]`... as list associativity; unit deletion `[x ; o ; z] ≐ [x ; z]`; collapse `[x ; y] ≐ [x][y]` when `comm(x, y) ≐ o` (co-sliced contents recover the classical calculus exactly) |
| the second seed | `J_j`, `(J_j) ≐ <o>`, `J_j ≢ J` | j := `(([J_j] <[oo]>))`; k := `([i ; j])` |
| anticommutation (O9) | `([i ; j]) ≐ <([j ; i])>` | the one non-commutativity axiom; by One-J Rigidity (JH-2) it cannot be derived |

**OC** (ordered cancellation, `[x⃗ ; y ; (<[y]>) ; z⃗] ≐ [x⃗ ; o ; z⃗]`) is a **theorem** on the chart, by JS-ARITY-AND-IMPORTS (Quadratic + Splice via the size-way reciprocal, no Collapse); if the prover cannot license the derivation it drops to a decree and the ROADMAP says so. Central sign and two-sided list distribution are theorems of the reading (structural bookkeeping). Hamilton's relations are theorems: the k² derivation uses central sign twice and *no J-cancellation*.

## 2. The nodes, in walk order (after `place`, orders 1600–1800)

| node | type | law (chart notation) | at ∞ | at 2 | at odd p |
|---|---|---|---|---|---|
| `H.no-go` | theorem (meta, witness) | `[x][y] ≡ [y][x]` as forms ⇒ a sound reading of `([x][y])` is commutative: breadth is capped at ℂ (JH-1, the Slice theorem) | EXACT | EXACT | EXACT |
| `H.ordered-bracket` | primitive | `[x ; y]` is a form; `[x ; y] ≢ [y ; x]`; splice; unit deletion | holds | holds | holds |
| `H.collapse` | theorem | `comm(x, y) ≐ o ⇒ [x ; y] ≃ [x][y]` — the classical calculus is the co-sliced fragment (JH-4) | holds | holds | holds |
| `H.seed` | decree | `(J_j) ≐ <o>`, `J_j ≢ J`; `j := (([J_j] <[oo]>))` | holds (πj) | holds (j ∈ 1 + πO) | holds (a matrix with square −1) |
| `H.anticommutation` | axiom (O9) | `([i ; j]) ≐ <([j ; i])>` | holds | holds | holds |
| `H.k` | definition | `k := ([i ; j])`; `k k ≐ <o>` | holds | holds: `k ≐ o π ζ` exactly (the quaternionic doll, one shell) | holds |
| `H.hamilton` | theorem | `i² ≐ j² ≐ k² ≐ <o>`, `ij ≐ k`, `ji ≐ <k>`, `jk ≐ i`, `ki ≐ j`, and the cyclic negatives | holds | holds | holds |
| `H.central-sign` | theorem | `([x ; <y> ; z]) ≐ <([x ; y ; z])>` | holds | holds | holds |
| `H.list-distribution` | theorem | `([x ; y z]) ≐ ([x ; y]) ([x ; z])` and on the left — *two-sided*: what dies in ℍ is exp-splitting, not distributivity | holds | holds | holds |
| `H.ordered-cancellation` | theorem (OC) | `[x⃗ ; y ; (<[y]>) ; z⃗] ≐ [x⃗ ; o ; z⃗]` | holds | holds | guarded (y a non-zero-divisor) |
| `H.conjugate` | definition | `q̄ := a <b i> <c j> <d k>` for `q = a (b i) (c j) (d k)` (tuple notation in the lede) | holds | holds | holds (the adjugate) |
| `H.norm` | theorem | `([q ; q̄]) ≐ ([q̄ ; q]) ≐ N`, N real: `a² + b² + c² + d²` | holds | holds | holds (the determinant) |
| `H.inverse` | theorem | `q⁻¹ ≐ ([<[N]>] [q̄])`, two-sided; `N ≐ void ⇒ <□>` excluded (JH-20) | holds | holds | **guarded**: N isotropic — `(o (i_C i))`-type zero divisors; the norm-null species |
| `H.four-squares` | theorem | `N([p ; q]) ≐ ([N_p][N_q])` — Euler 1748; the import that prices Hurwitz's seal later | holds | holds | holds |
| `H.phase-sphere` | theorem | `(J_u) ≐ <o>` for every pure unit u: −1 has a 2-sphere of logs | holds | holds (the conjugacy class of i in 1 + πO) | holds (a quadric) |
| `H.seam-guard` | decree | `[(A)] → A` fires only when `L(exp V(A)) = V(A)`: in ℂ the seam is the point θ = π (the `mult.seam-decree` content clause), in ℍ the whole angle-π sphere but one ray (JH-3) | the decree | the decree | the decree |
| `H.slice-wall` | theorem | `(ω_u A) ≃ (A)` for A in the slice of u — absorbed; **absent across slices** (in-band rigidity). The first non-commutative wall: the receipt has a direction | holds per slice | holds per slice (half-shells) | holds per slice |
| `H.rigidity-dichotomy` | theorem | `<A> ≐ ([A] J_u)` for every u when A is real positive; only u = ±v off the reals (JH-12) | holds | holds | holds |
| `H.polar-form` | theorem | `q ≐ ([r] ([J_u][t]))` = r·e^{tπu}; S³ = the suspension of the phase sphere (JH-17) | holds | replaced by `H.ramified-place`'s polar form | replaced (Cartan/Iwasawa) |
| `H.half-phase` | theorem | `([((J_u/2)) ; ((J_v/2))]) ≐ (u × v)` for u ⟂ v: ij = k from James's own i (JH-18) | holds | holds | holds |
| `H.120-law` | theorem | `J_u J_v ≐ J_{u+v}` when \|u + v\| = 1 — two juxtaposed phases are a third (JH-15) | holds | untested | untested |
| `H.ramification` | import | (−1,−1)_ℚ ramifies at exactly {2, ∞} (Hilbert symbol); at odd p it splits — the Hurwitz places | — | ramified | split |
| `H.split-place` | theorem (reading) | at odd p, i ↦ and j ↦ 2×2 matrices with a² + b² ≡ −1 mod pⁿ; every H law holds as a matrix law; the norm is the determinant and is isotropic | — | — | the reading |
| `H.ramified-place` | theorem (reading) | at 2: `π := o i` (1 + i), `v(π) = ½`, `([π ; π]) ≐ ([oo][i])`; v ∈ ½ℤ; residue field 𝔽₄ = {0, o, ζ, ζ²} with ζ the Hurwitz unit of order 3; the radius of the instance is the half-shell v ≥ 3/2; i, j principal, μ₃ the Teichmüller part (roles inverted vs rung 2) — JP v0.3 (3) | — | the reading | — |
| `H.hurwitz-units` | theorem | the 24 units ±1, ±i, ±j, ±k, (±1 ±i ±j ±k)/2; orders {1, 2, 3, 4, 6}; 2T = μ₃ ⋉ Q₈; the de-collapse of the 16-valued world (JH-19) in the Notes | holds | holds: the torsion of the unique maximal order | holds (a subgroup of GL₂) |
| `H.twenty-four` | ANALOGY | \|2T\| = 24 = 8·3 beside M(2) = 24 = 2³·3 (`place.local-wall`, k = 1): the orders match factor by factor (Q₈ ↔ e₂(1) = 3, μ₃ ↔ e₃(1) = 1) but not place by place — μ₃ lives at 2 (𝔽₄) in ℍ and at 3 in the ψ-wall. Kept ANALOGY until a form equates them (LEGISLATION 19) | — | — | — |
| `H.octonion-gap` | gap | the next doubling needs non-associative depth; composition is associative; owed to the `O` branch (JH OP-3) | — | — | — |

Then the back-fill: the 22 JH cells of rung `place` (void pile at 2: `π^{2n} ≐ void` on O/2ⁿO, depth in half-shells; prime-log: `[π]` has count ½; no-inverse-of-the-prime: π has none; Fermat on (O/πⁿ)^×; the doll with digits in 𝔽₄; selection: which roots exist in 2T; the wall: the same tape, per slice) and `split` at odd p.

## 3. Engine

- `tools/forms.py`: parse `[x ; y ; …]` as an ORDERED square (a fourth node kind); unordered squares unchanged.
- `tools/quat.py`: the ℍ reading at ∞ — juxtaposition addition, `( )` exp (entire), `[ ]` principal log with the sphere seam (θ = π: direction ambiguous → `Seam` error unless guarded), `< >` negation, `[x ; y]` log of the ordered product; constants J = πi (J-pinning: u₀ = i), J_j = πj; receipts in Λ_ℍ = {2πk·u}: `k(a, b)` returns (k, u) or None.
- `tools/j1.py`: a receipt carries a direction; `absorbed` directly inside an instance **only when the content is co-sliced with the receipt's direction** (cross product of imaginary parts void on every sample); otherwise `absent` — that *is* `H.slice-wall`, graded.
- `tools/placeh.py`: D₂ at p = 2 (valuation in ½ℤ, uniformizer 1 + i, O/πⁿ, exp/log on v ≥ 3/2, 2T as the torsion) and M₂(ℤ/pⁿ) at odd p (i, j from a² + b² ≡ −1); the ledger reads every H law at 2 and at 3, 5, 7, 13.
- `tools/check.py`: `setting: JH` nodes read in `quat`; the place ledger gains a JH column per place; the JP cell vocabulary gains `split`.

## 4. Decisions recorded as LEGISLATION 32, pending Lui (defaults)

(a) **The bill**: semicolon + J_j + O9 as the rung's three additions; OC a theorem (decree if the derivation won't license). (b) **The ordered bracket is a fourth boundary on the chart**, introduced here as the ordered *abstraction*; whether the same `[x ; y]` is also the lens of `place.completion` is left open (the completion stays a gap). (c) **Receipts carry a direction**; absorption is slice-conditional; a cross-slice absorption is `absent`. That is the first non-commutative wall, and it is what the No-Go theorem looks like on a tape. (d) **The seam decree generalizes**: a new `H.seam-guard` citing `mult.seam-decree`, with the content clause "L(exp V(A)) = V(A)" (the sphere seam), rather than editing the trunk's decree. (e) **The ledger reads H at 2 and at the odd places**, and `split` is a JP/JH cell value: the law holds in M₂ with the norm-null divisors guarded. (f) **24 stays an ANALOGY** between `H.hurwitz-units` and `place.local-wall` — the chart records the factor-by-factor match and the place mismatch, and does not equate them. (g) **The 120° law and phase interference** enter as theorems at ∞ with their place cells `untested`: the sphere of phases has no finite-place analogue the chart can yet read.

## 5. What the rung does not do

The octonions (`O`, a branch; the fork `(kl)² ≐ o` vs `<o>`), Clifford algebras from n seeds (JH OP-4 — the Clifford road is noted in `H.seed`'s Notes), the adelic page (`J2`), the metric (`analysis`). Emergent order (JH OP-5) is the rung's named gap beside `H.octonion-gap`: the ordered device is imported, not found as J was.
