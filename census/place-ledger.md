# The chart at every place — computed by the place reading (tools/place.py) and the receipt prover (tools/j1.py)

Each law read at p = 2, 3, 5, 7, 13 (page depth = working precision 2: 34, 3: 22, 5: 16, 7: 12, 13: 10 shells): the law's status at the generic points of the place (exact · mod-Λ · guarded · none · fails; ·exc when it fails at a lattice point, a variable exactly one, where the log reads ω_p; a sample outside the radius of the instance is retried on the radius and, if still outside, counts as formless; a sample past the working precision is dropped) and the grade of its derivation re-graded there (strict · absorbed · posted · import · absent), with the JP cell they imply beside the hand-written one. Written by `tools/check.py`; do not edit. The place rung's own nodes are graded at their own place and listed last.

| node | p = 2 | p = 3 | p = 5 | p = 7 | p = 13 | computed JP | hand JP |
|---|---|---|---|---|---|---|---|
| `void.page` | exact | exact | exact | exact | exact | holds | holds |
| `void.space` | exact | exact | exact | exact | exact | holds | holds |
| `N.round` | exact | exact | exact | exact | exact | holds | holds |
| `N.unit` | exact | exact | exact | exact | exact | holds | holds |
| `N.numeral` | exact | exact | exact | exact | exact | holds | holds |
| `N.addition` | exact | exact | exact | exact | exact | holds | holds |
| `N.add-comm` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `N.zero` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `N.successor` | exact | exact | exact | exact | exact | holds | holds |
| `Z.angle` | exact | exact | exact | exact | exact | holds | holds |
| `Z.inversion` | exact | exact | exact | exact | exact | holds | holds |
| `Z.void-inverse` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `Z.negative-numeral` | exact | exact | exact | exact | exact | holds | holds |
| `Z.subtraction` | exact | exact | exact | exact | exact | holds | holds |
| `Z.cancellation` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `Z.collection` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `Z.normal-form` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `mult.square` | exact | exact | exact | exact | exact | holds | holds |
| `mult.involution` | exact | exact | exact | exact | exact | holds | holds |
| `mult.distribution` | exact | exact | exact | exact | exact | holds | holds |
| `mult.multiplication` | exact | exact | exact | exact | exact | holds | holds |
| `mult.log-of-one` | mod-Λ · posted | mod-Λ · posted | mod-Λ · posted | mod-Λ · posted | mod-Λ · posted | holds-mod-Λ | holds-mod-Λ |
| `mult.unit-law` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `mult.product-of-numerals` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `mult.cardinality` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `mult.exponentiation` | exact | exact | exact | exact | exact | holds | holds |
| `mult.square-is-product` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `mult.black-hole` | exact | exact | exact | exact | exact | holds | holds |
| `mult.hole-instance` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `mult.zero-annihilates` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `mult.dominion` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `mult.inverse-promotion` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `mult.product-of-negatives` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `Q.division` | guarded | guarded | guarded | guarded | guarded | guarded | guarded |
| `Q.self-division` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `Q.division-by-one` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `Q.reciprocal` | guarded | guarded | guarded | guarded | exact | guarded | guarded |
| `Q.one-over-a` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `Q.reciprocal-law` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `Q.double-reciprocal` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `Q.division-as-product` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `Q.fraction` | exact | none | exact | exact | exact | guarded | guarded |
| `Q.half` | none | exact | exact | exact | exact | guarded | guarded |
| `Q.halves` | none · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | guarded | guarded |
| `Q.fractional-cardinality` | guarded · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | guarded | guarded |
| `Q.cancel-common-factor` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `Q.quotient-of-numerals` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `Q.add-fractions` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `Q.multiply-fractions` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `Q.flip` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `Q.divide-by-fraction` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `Q.reciprocal-of-product` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `Q.negative-fraction` | guarded · strict | guarded · strict | guarded · strict | guarded · strict | guarded · strict | guarded | guarded |
| `Q.reciprocal-of-negative` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `Q.negative-denominator` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `Q.negatives-cancel` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `Q.rational` | exact | none | exact | exact | exact | guarded | guarded |
| `Q.zero-divided` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `Q.normal-form` | none · absorbed | none · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | guarded | guarded |
| `alg.base` | none | none | none | none | none | replaced | replaced |
| `alg.log-of-base` | none · posted | none · posted | none · posted | none · posted | none · posted | replaced | replaced |
| `alg.exp-law` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `alg.power-of-base` | none · absent | none · absent | none · absent | none · absent | none · absent | replaced | replaced |
| `alg.log-law` | exact · posted | exact · posted | exact · posted | exact · posted | exact · posted | holds-mod-Λ | holds-mod-Λ |
| `alg.exp-of-pile` | none · absorbed | none · absorbed | none · absorbed | none · absorbed | none · absorbed | replaced | replaced |
| `alg.product-of-powers` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `alg.first-power` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `alg.zeroth-power` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `alg.one-to-power` | guarded · absent | fails · absent | fails · absent | fails · absent | fails · absent | fails | replaced |
| `alg.log-of-power` | exact · posted | exact · posted | exact · posted | guarded · posted | exact · posted | guarded | guarded |
| `alg.negative-exponent` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `alg.power-of-power` | exact · import | guarded · import | guarded · import | guarded · import | guarded · import | guarded | guarded |
| `alg.root` | guarded | guarded | guarded | guarded | guarded | guarded | guarded |
| `alg.root-squared` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `alg.root-of-product` | guarded ·exc · import | guarded ·exc · import | guarded ·exc · import | guarded ·exc · import | guarded ·exc · import | guarded | guarded |
| `alg.root-of-quotient` | guarded ·exc · import | guarded ·exc · import | guarded ·exc · import | guarded ·exc · import | guarded ·exc · import | guarded | guarded |
| `alg.sqrt4` | exact · import | fails · absent | exact · import | exact · import | exact · import | fails | fails |
| `alg.sqrt2` | none | none | none | exact | none | guarded | guarded |
| `alg.nth-root` | guarded | guarded | guarded | guarded | guarded | guarded | guarded |
| `alg.rational-exponent` | none · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `C.phase` | exact | exact | exact | exact | exact | holds | holds |
| `C.phase-value` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `C.euler-identity` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `C.phase-rule` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `C.phase-independence` | exact · posted | exact · posted | exact · posted | exact · posted | exact · posted | holds-mod-Λ | holds-mod-Λ |
| `C.log-of-negative` | exact · posted | exact · posted | exact · posted | exact · posted | exact · posted | holds-mod-Λ | holds-mod-Λ |
| `C.log-of-negative-below` | exact · posted | exact · posted | exact · posted | exact · posted | exact · posted | holds-mod-Λ | holds-mod-Λ |
| `C.phase-under-instance` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `C.double-phase` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `C.period-absorption` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `C.phase-sign` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `C.imaginary-unit` | none | none | exact | none | exact | guarded | guarded |
| `C.i-squared` | none · absorbed | none · absorbed | exact · absorbed | none · absorbed | exact · absorbed | guarded | guarded |
| `C.pi` | none | none | none | none | none | replaced | replaced |
| `C.i-to-the-i` | none · absent | none · absent | none · import | none · absent | none · import | replaced | replaced |
| `C.root-of-negative` | none · import | none · import | guarded ·exc · import | none · import | guarded ·exc · import | guarded | guarded |
| `C.cube-root-of-negation` | none · absorbed | none · absorbed | none · absorbed | exact · absorbed | exact · absorbed | guarded | guarded |
| `C.cube-root-of-unity` | none · absorbed | none · absorbed | none · absorbed | exact · absorbed | exact · absorbed | guarded | guarded |
| `C.omega-sum` | none · absorbed | none · absorbed | none · absorbed | exact · absorbed | exact · absorbed | guarded | guarded |
| `C.complex-number` | none | none | exact | none | exact | guarded | guarded |
| `C.polar-form` | guarded | guarded | exact | guarded | guarded | guarded | guarded |
| `C.turn-of-sum` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `C.polar-product` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `C.reverse-turn` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `C.minus-one-power` | guarded | guarded | guarded | guarded | guarded | guarded | guarded |
| `C.conjugate` | none | none | exact | none | exact | guarded | guarded |
| `C.complex-product` | none · absorbed | none · absorbed | exact · absorbed | none · absorbed | exact · absorbed | guarded | guarded |
| `C.modulus-squared` | none · absorbed | none · absorbed | exact · absorbed | none · absorbed | exact · absorbed | guarded | guarded |
| `C.modulus` | guarded | guarded | guarded | exact | guarded | guarded | guarded |
| `C.cosine` | guarded | guarded | guarded | guarded | guarded | guarded | guarded |
| `C.complex-quotient` | none · absorbed | none · absorbed | exact · absorbed | none · absorbed | guarded · absorbed | guarded | guarded |
| `C.sine` | none | none | guarded | none | guarded | guarded | guarded |
| `C.cosine-even` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `C.sine-odd` | none · absorbed | none · absorbed | guarded · absorbed | none · absorbed | guarded · absorbed | guarded | guarded |
| `C.euler-formula` | none · absorbed | none · absorbed | guarded · absorbed | none · absorbed | guarded · absorbed | guarded | guarded |
| `C.conjugate-of-turn` | none · absorbed | none · absorbed | guarded · absorbed | none · absorbed | guarded · absorbed | guarded | guarded |
| `C.pythagorean` | none · absorbed | none · absorbed | guarded · absorbed | none · absorbed | guarded · absorbed | guarded | guarded |
| `C.modulus-of-polar` | none · import | none · import | exact ·exc · import | none · import | guarded ·exc · import | guarded | guarded |
| `C.cosine-addition` | none · absorbed | none · absorbed | guarded · absorbed | none · absorbed | guarded · absorbed | guarded | guarded |
| `C.sine-addition` | none · absorbed | none · absorbed | guarded · absorbed | none · absorbed | guarded · absorbed | guarded | guarded |
| `C.de-moivre` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `C.quadratic-formula` | none · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `schema.cardinality` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `schema.power` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `schema.period-multiple` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `schema.roots-of-unity` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `schema.roots-of-negation` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `schema.de-moivre` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `schema.roots-sum` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `J1.period-form` | exact | exact | exact | exact | exact | holds | holds |
| `J1.counit` | exact | exact | exact | exact | exact | holds | holds |
| `J1.unit` | exact | exact | exact | exact | exact | holds | holds |
| `J1.closure` | exact · strict | exact · strict | exact · strict | exact · strict | exact · strict | holds | holds |
| `J1.absorption` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `J1.absorption-mirror` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `J1.half-period` | exact · posted | exact · posted | exact · posted | exact · posted | exact · posted | holds-mod-Λ | holds-mod-Λ |
| `J1.j-cancellation` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |
| `J1.multiple-value` | exact · posted | exact · posted | exact · posted | exact · posted | exact · posted | holds-mod-Λ | holds-mod-Λ |
| `J1.receptacle` | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded · absorbed | guarded | guarded |
| `J1.phase-independence` | exact · posted | exact · posted | exact · posted | exact · posted | exact · posted | holds-mod-Λ | holds-mod-Λ |
| `J1.seam-theorem` | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | exact · absorbed | holds | holds |

## Rung `place`

| node | place | computed JP | hand JP | tape |
|---|---|---|---|---|
| `place.residue` | p = 2, 3, 5 | holds | holds | holds: page [depth-0] on `o o` (the page's equality, mod p^n: not through a square); page [depth-0] on `o o o o` (the page's equality, mod p^n: not through a square); page [depth-0] on `o o o` (the page's equality, mod p^n: not through a square); page [depth-0] on `o o o o o o o o o` (the page's equality, mod p^n: not through a square); page [depth-0] on `o o o o o` (the page's equality, mod p^n: not through a square); page [depth-0] on `o o o o o o o o o o o o o o o o o o o o o o o o o` (the page's equality, mod p^n: not through a square) |
| `place.negation-is-a-pile` | p = 2, 3, 5 | holds | holds | holds: page [depth-0] on `void` (the page's equality, mod p^n: not through a square) |
| `place.division-by-unit` | p = 2, 3, 5, 7 | holds | holds | holds: absorbed [absorbing] on `void` (k = -1); absorbed [page step, measured at the squares above it: the outermost changed square posts, directly inside an instance] on `o` (k = 1); absorbed [absorbing] on `([o o] [[U]])` (k = -1,0); absorbed [absorbing] on `([o o o o o o] [[U]])` (k = -3,0); absorbed [absorbing] on `([o o o o] [[U]])` (k = -3,-2,-1,0); absorbed [absorbing] on `([o o o o o o o o o o o o o o o o o o o o] [[U]])` (k = -15,-10,-5,0); absorbed [absorbing] on `([o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o] [[U]])` (k = -35,-28,-21,-14,-7,0) |
| `place.doll` | p = 2, 3, 5 | holds | holds | holds: absorbed [inherited schema.cardinality] on `o o` (k = 0); absorbed [inherited schema.cardinality] on `o o o o` (k = 0); absorbed [inherited schema.cardinality] on `o o o o o o` (k = 0); absorbed [inherited schema.cardinality] on `o o o` (k = 0); absorbed [inherited schema.cardinality] on `o o o o o o o o o` (k = 0); absorbed [inherited schema.cardinality] on `o o o o o` (k = 0); absorbed [inherited schema.cardinality] on `o o o o o o o o o o` (k = 0); absorbed [inherited schema.cardinality] on `o o o o o o o o o o o o o o o` (k = 0) |
| `place.teichmuller` | p = 3, 5, 7 | holds | holds | holds: absorbed [inherited schema.power] on `(([o o o] [[((<[o o]> [[o]]))]]))` (k = 0); absorbed [absorbing] on `(<[o o]> [[o]])` (k = 0); absorbed [inherited schema.cardinality] on `(<[o o]> [[o]]) (<[o o]> [[o]]) (<[o o]> [[o]])` (k = 0); absorbed [absorbing] on `<[o o]> [[o]]` (k = ?); absorbed [absorbing] on `void` (k = 1); absorbed [absorbing] on `((<[o o]> [[o]]) [o])` (k = 1); absorbed [inherited schema.power] on `(([o o o o o] [[((<[o o o o]> [[o]]))]]))` (k = 0); absorbed [absorbing] on `(<[o o o o]> [[o]])` (k = 0); absorbed [inherited schema.cardinality] on `(<[o o o o]> [[o]]) (<[o o o o]> [[o]]) (<[o o o o]> [[o]]) (<[o o o o]> [[o]]) (<[o o o o]> [[o]])` (k = 0); absorbed [absorbing] on `<[o o o o]> [[o]]` (k = ?); absorbed [absorbing] on `((<[o o o o]> [[o]]) [o])` (k = 1); absorbed [inherited schema.power] on `(([o o o o o o o] [[((<[o o o o o o]> [[o]]))]]))` (k = 0); absorbed [absorbing] on `(<[o o o o o o]> [[o]])` (k = 0); absorbed [inherited schema.cardinality] on `(<[o o o o o o]> [[o]]) (<[o o o o o o]> [[o]]) (<[o o o o o o]> [[o]]) (<[o o o o o o]> [[o]]) (<[o o o o o o]> [[o]]) (<[o o o o o o]> [[o]]) (<[o o o o o o]> [[o]])` (k = 0); absorbed [absorbing] on `<[o o o o o o]> [[o]]` (k = ?); absorbed [absorbing] on `((<[o o o o o o]> [[o]]) [o])` (k = 1) |
| `place.prime-power` | p = 2, 3, 5, 7 | holds | holds | holds: page [depth-0] on `o o` (the page's equality, mod p^n: not through a square); absorbed [inherited schema.cardinality] on `([o o] [o o])` (k = 0); page [depth-0] on `o o o o` (the page's equality, mod p^n: not through a square); absorbed [absorbing] on `[o o] [o o]` (k = 0); absorbed [inherited schema.cardinality] on `([o o o o] [o o])` (k = 0); page [depth-0] on `o o o o o o o o` (the page's equality, mod p^n: not through a square); page [depth-0] on `o o o` (the page's equality, mod p^n: not through a square); absorbed [inherited schema.cardinality] on `([o o o] [o o o])` (k = 0); page [depth-0] on `o o o o o o o o o` (the page's equality, mod p^n: not through a square); absorbed [absorbing] on `[o o o] [o o o]` (k = 0); absorbed [inherited schema.cardinality] on `([o o o o o o o o o] [o o o])` (k = 0); page [depth-0] on `o o o o o o o o o o o o o o o o o o o o o o o o o o o` (the page's equality, mod p^n: not through a square); page [depth-0] on `o o o o o` (the page's equality, mod p^n: not through a square); absorbed [inherited schema.cardinality] on `([o o o o o] [o o o o o])` (k = 0); page [depth-0] on `o o o o o o o o o o o o o o o o o o o o o o o o o` (the page's equality, mod p^n: not through a square); absorbed [absorbing] on `[o o o o o] [o o o o o]` (k = 0); absorbed [inherited schema.cardinality] on `([o o o o o o o o o o o o o o o o o o o o o o o o o] [o o o o o])` (k = 0); page [depth-0] on `o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o` (the page's equality, mod p^n: not through a square); page [depth-0] on `o o o o o o o` (the page's equality, mod p^n: not through a square); absorbed [inherited schema.cardinality] on `([o o o o o o o] [o o o o o o o])` (k = 0); page [depth-0] on `o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o` (the page's equality, mod p^n: not through a square); absorbed [absorbing] on `[o o o o o o o] [o o o o o o o]` (k = 0); absorbed [inherited schema.cardinality] on `([o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o] [o o o o o o o])` (k = 0); page [depth-0] on `o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o` (the page's equality, mod p^n: not through a square) |
| `place.geometric-doll` | p = 2, 3 | holds | holds | holds: absorbed [absorbing] on `[o ([o o])] [o <o o>]` (k = 1); absorbed [absorbing] on `void` (k = 1); absorbed [inherited C.phase-rule] on `<o o>` (k = 0); absorbed [absorbing] on `[o o] J` (k = 0); absorbed [inherited C.phase-under-instance] on `([o o] [o ([o o])] J)` (k = 0); absorbed [absorbing] on `[o o]` (k = 0); absorbed [absorbing] on `void` (k = 1); absorbed [page step, measured at the squares above it: the outermost changed square posts, directly inside an instance] on `([o o] [o o])` (k = -1); absorbed [absorbing] on `[o ([o o] [o o]) ([o o])] [o <o o>]` (k = 1); absorbed [inherited C.phase-under-instance] on `([o o] [o ([o o] [o o]) ([o o])] J)` (k = 0); absorbed [absorbing] on `[o o] [o o]` (k = 0); absorbed [page step, measured at the squares above it: the outermost changed square posts, directly inside an instance] on `([o o] [o o] [o o])` (k = -1); absorbed [absorbing] on `[o <o o o>] [o]` (k = 1); absorbed [inherited C.phase-rule] on `<o o o>` (k = 0); absorbed [absorbing] on `[o o o] J` (k = 0); absorbed [inherited C.phase-under-instance] on `([o o o] [o] J)` (k = 0); absorbed [page step, measured at the squares above it: the outermost changed square posts, directly inside an instance] on `([o o o])` (k = -1); absorbed [absorbing] on `[o ([o o o])] [o <o o o>]` (k = 0); absorbed [inherited C.phase-under-instance] on `([o o o] [o ([o o o])] J)` (k = 0); absorbed [absorbing] on `[o o o]` (k = 0); absorbed [page step, measured at the squares above it: the outermost changed square posts, directly inside an instance] on `([o o o] [o o o])` (k = -1); absorbed [absorbing] on `[o ([o o o] [o o o]) ([o o o])] [o <o o o>]` (k = 0); absorbed [inherited C.phase-under-instance] on `([o o o] [o ([o o o] [o o o]) ([o o o])] J)` (k = 0); absorbed [absorbing] on `[o o o] [o o o]` (k = 0); absorbed [page step, measured at the squares above it: the outermost changed square posts, directly inside an instance] on `([o o o] [o o o] [o o o])` (k = -1) |
