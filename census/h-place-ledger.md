# Rung H at the places, and rung place in ℍ — computed by the quaternion reading at a place (tools/quatplace.py)

**Rung H at the places.** Each law of rung `H` read at p = 2, 3, 5, 7, 13 in the quaternion reading — the Hurwitz order at 2 (ramified: half-shells, the uniformizer 1 + i, the residue field 𝔽₄, the 24 units), the quaternions over ℤ/pⁿ at an odd p (split: the norm isotropic) — on the law's own domain (exact · mod-Λ · guarded · none · fails), and the JP cell these imply beside the hand-written one. Written by `tools/check.py`; do not edit.

| node | p = 2 | p = 3 | p = 5 | p = 7 | p = 13 | computed JP | hand JP |
|---|---|---|---|---|---|---|---|
| `H.ordered-bracket` | guarded | guarded | guarded | guarded | guarded | guarded | guarded |
| `H.ordered-product` | guarded | guarded | guarded | guarded | guarded | guarded | guarded |
| `H.splice` | none | guarded | guarded | guarded | guarded | guarded | guarded |
| `H.unit-entry` | none | guarded | guarded | guarded | guarded | guarded | guarded |
| `H.list-distribution` | none | guarded | guarded | guarded | guarded | guarded | guarded |
| `H.commutation` | exact | exact | exact | exact | exact | holds | holds |
| `H.collapse` | seam | seam | seam | seam | seam | guarded | guarded |
| `H.zero-entry` | exact | exact | exact | exact | exact | holds | holds |
| `H.central-sign` | none | guarded | guarded | guarded | guarded | guarded | guarded |
| `H.ordered-cancellation` | guarded | guarded | guarded | guarded | guarded | guarded | guarded |
| `H.reversal` | none | seam | seam | seam | seam | guarded | guarded |
| `H.j` | exact | exact | exact | exact | exact | holds | holds |
| `H.anticommutation` | exact | exact | exact | exact | exact | holds | holds |
| `H.k` | exact | exact | exact | exact | exact | holds | holds |
| `H.i-squared` | exact | exact | exact | exact | exact | holds | holds |
| `H.j-squared` | exact | exact | exact | exact | exact | holds | holds |
| `H.ji` | exact | exact | exact | exact | exact | holds | holds |
| `H.k-squared` | exact | exact | exact | exact | exact | holds | holds |
| `H.jk` | exact | exact | exact | exact | exact | holds | holds |
| `H.ki` | exact | exact | exact | exact | exact | holds | holds |
| `H.kj` | exact | exact | exact | exact | exact | holds | holds |
| `H.ik` | exact | exact | exact | exact | exact | holds | holds |
| `H.quaternion` | exact | exact | exact | exact | exact | holds | holds |
| `H.conjugate` | exact | exact | exact | exact | exact | holds | holds |
| `H.pure-square` | exact | exact | exact | exact | exact | holds | holds |
| `H.norm` | exact | exact | exact | exact | exact | holds | holds |
| `H.inverse` | none | guarded | exact | exact | guarded | guarded | guarded |

**Rung place in ℍ.** Each law of rung `place` read at its own place in the quaternion reading: on its domain (the centre — the page's own numbers) and on generic quaternions of the page; the JH cell these imply (holds on generic quaternions; guarded when only on the centre) beside the hand-written one.

| node | on the centre | on generic ℍ_p | computed JH | hand JH |
|---|---|---|---|---|
| `place.residue` | exact | exact | holds | holds |
| `place.negation-is-a-pile` | exact | exact | holds | holds |
| `place.fermat` | exact | fails | guarded | guarded |
| `place.division-by-unit` | exact | fails | guarded | guarded |
| `place.doll` | exact | exact | holds | holds |
| `place.teichmuller` | exact | exact | holds | holds |
| `place.prime-power` | exact | exact | holds | holds |
| `place.geometric-doll` | exact | exact | holds | holds |
