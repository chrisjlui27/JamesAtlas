"""One-off author's script for rung Q (2026-10-03). Emits nodes/Q.*.md; the emitted files are the source of truth.
Kept under tools/gen/ as a record of how the rung was drafted; it is not part of the build."""
import os, textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TODAY = "2026-10-03"

COMMON_READINGS = {"lambda": "untested", "CC": "untested", "logic": "ABSENT"}


def fm(d):
    lines = ["---"]
    for k in ["id", "title", "type", "level", "kind", "rung", "order", "setting", "equality", "domain", "law", "units",
              "gloss_check", "witness", "holds", "readings", "status", "verified", "known_since", "entered", "guide", "band",
              "uses", "see_also", "aliases", "concepts", "understood", "understood_note", "reentry"]:
        if k not in d:
            continue
        v = d[k]
        if isinstance(v, dict):
            lines.append(f"{k}:")
            for kk, vv in v.items():
                lines.append(f"  {kk}: {vv}")
        elif isinstance(v, list):
            items = []
            for x in v:
                x = str(x)
                items.append(f'"{x}"' if any(c in x for c in ",:#'") else x)
            lines.append(f"{k}: [{', '.join(items)}]")
        elif isinstance(v, bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        elif isinstance(v, int):
            lines.append(f"{k}: {v}")
        else:
            s = str(v)
            if any(c in s for c in ":#'\"<>[]{}") or s != s.strip() or s in ("yes", "no"):
                s = '"' + s.replace('"', '\\"') + '"'
            lines.append(f"{k}: {s}")
    lines.append("---")
    return "\n".join(lines)


def node(**d):
    body = d.pop("body")
    d.setdefault("setting", "classical")
    d.setdefault("equality", "≐")
    d.setdefault("rung", "Q")
    d.setdefault("entered", TODAY)
    d.setdefault("understood", "no")
    d.setdefault("understood_note", "")
    d.setdefault("reentry", False)
    d.setdefault("see_also", [])
    readings = {"C": "EXACT", "finset": "ABSENT"}
    readings.update(d.pop("readings_over", {}))
    readings.update(COMMON_READINGS)
    readings.update(d.pop("readings_fix", {}))
    d["readings"] = readings
    holds = {"classical": "holds", "J1": "holds", "JH": "holds", "JO": "holds", "JP": "holds"}
    holds.update(d.pop("holds_over", {}))
    d["holds"] = holds
    text = fm(d) + "\n\n" + textwrap.dedent(body).strip() + "\n"
    path = os.path.join(ROOT, "nodes", d["id"] + ".md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", path)


J1_DOWN = "the Involution-down step `[(X)] ≐ X` is mod Λ in J1; both sides of the law sit inside an instance, which absorbs the period (A5′), so the law holds exactly"

node(
    id="Q.division", title="Division is the instance of a difference of abstracts", type="definition", level="object", kind="law",
    order=500, domain="positive", law="A ÷ B := ([A] <[B]>)", units="a ÷ b = e^{ln a − ln b}", gloss_check="A / B",
    holds_over={"JH": "replaced", "JO": "replaced", "JP": "guarded"}, readings_over={}, status="NATIVE", verified="engine",
    known_since="1993 (James); division is ancient", guide="shape-led", band="3–5",
    uses=["N.round", "mult.square", "Z.angle", "void.space"], see_also=["mult.multiplication", "Q.reciprocal", "Q.division-as-product"],
    aliases=["quotient", "÷", "fraction bar"], concepts=["division"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([A] <[B]>)` | — | a ÷ b |
    | `([oooooo] <[oo]>)` | — | 6 ÷ 2 |

    To divide, abstract both, mirror the divisor's abstract, put them together, take the instance. Division is multiplication with one abstract mirrored — subtraction one level deeper, exactly as multiplication was addition one level deeper.

    ## Plain

    Dividing is the times recipe with the second box turned to its mirror.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `([A] <[B]>)` | [[N.round]] | the instance of the abstract of A ([[mult.square]]) beside the mirror ([[Z.angle]]) of the abstract of B, in one space ([[void.space]]) |
    | `A ÷ B` | name | — |

    ## Confirms

    a ÷ b = e^{ln a − ln b}: the slide-rule's subtraction. There is no new symbol and no new axiom; division is a shape. It is **not** yet shown that `6 ÷ 2` is a pile — that follows from [[Q.cancel-common-factor]] with the numerator written as `([ooo][oo])` — and it is **not** commutative in ℍ, where JH needs two quotients, `x·y⁻¹` and `y⁻¹·x`, and the ordered bracket.

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical | holds | — |
    | J1 | holds | the form is the same; its laws below hold exactly thanks to A5′ |
    | JH, JO | replaced | two quotients in a non-commutative algebra; `x⁻¹ ≐ (<[x]>)` survives, the single `÷` does not |
    | JP | guarded | at a finite place one cannot divide by the prime ([[Q.reciprocal]]); the form exists for unit divisors |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | finite sets have no quotients; see [[Q.half]] for the groupoid-cardinality analogy |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    The Iconic Mathematics scope puts division at grades 3–5 as "the inverse boundary meets the abstract boundary": the angle boundary, additive since grade 1, gains its multiplicative power here.
    """,
)

node(
    id="Q.reciprocal", title="The reciprocal is the mirror of the abstract", type="definition", level="object", kind="law",
    order=510, domain="positive", law="1/A := (<[A]>)", units="1/a = e^{−ln a}", gloss_check="1 / A",
    holds_over={"JP": "guarded"}, readings_over={"finset": "ANALOGY"}, status="NATIVE", verified="engine",
    known_since="1993 (James); reciprocals are ancient", guide="shape-led", band="6–8",
    uses=["N.round", "Z.angle", "mult.square"], see_also=["Q.one-over-a", "Q.reciprocal-law", "Q.half", "mult.hole-exclusion"],
    aliases=["multiplicative inverse", "1/x", "x⁻¹", "(<[x]>)"], concepts=["division", "inverse"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `(<[A]>)` | — | 1/a |

    The angle boundary threaded between the other two: mirror the abstract, take the instance. Placed directly, `<A>` was −a; placed between, it is 1/a. One boundary, two inverses, the depth deciding which.

    ## Plain

    One over a number is the number's box, mirrored, then circled.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `(<[A]>)` | [[N.round]] | the instance of the mirror ([[Z.angle]]) of the abstract ([[mult.square]]) of A |
    | `1/A` | name | — |

    ## Confirms

    x⁻¹ = e^{−ln x}; that `1 ÷ A` reduces to this form is the theorem [[Q.one-over-a]]. In JH this exact form is kept — "with x⁻¹ ≐ (<[x]>)" — where the right-inverse law is the axiom OC and the left-inverse law is a theorem ([[Q.reciprocal-law]]). What this is **not**: a form for 1/0. With A the void, `[A]` is □ and `<□>` is excluded ([[mult.hole-exclusion]]); the reciprocal of zero is not undefined-by-convention, it is unwritable ([[Q.no-division-by-zero]]).

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical | holds | — |
    | J1 | holds | the form is the same; note that `[o] ≐ void`, used by [[Q.one-over-a]], becomes `[o] → ω` in J1 — a Λ-step absorbed by the instance |
    | JH, JO | holds | `x⁻¹ ≐ (<[x]>)` is the inverse used throughout the JH guide |
    | JP | guarded | at a finite place the prime has no inverse (Part II, Ch. 10: No-inverse-of-the-prime); reciprocals exist for units only |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ANALOGY | Baez–Dolan groupoid cardinality gives 1/n to a one-object groupoid with n automorphisms — a reading in which fractional counts are counts of symmetry; an analogy here, a candidate law at the `struct` rung |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.reciprocal-law", title="A number times its reciprocal is one", type="theorem", level="object", kind="law",
    order=520, domain="positive", law="([A] [(<[A]>)]) ≐ o", units="a · (1/a) = 1", gloss_check="1",
    holds_over={"JP": "guarded"}, status="NATIVE", verified="engine",
    known_since="1993 (James); the fact is ancient", guide="shape-led", band="6–8",
    uses=["mult.multiplication", "Q.reciprocal", "mult.involution", "Z.inversion", "N.unit"], see_also=["Z.inversion", "mult.unit-law"],
    aliases=["multiplicative inverse law", "x · x⁻¹ = 1"], concepts=["division", "inverse", "one"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([A] [(<[A]>)]) ≐ o` | — | a · (1/a) = 1 |

    ## Plain

    A number times one-over-itself is one — because, under the box, "times the reciprocal" is just "plus the opposite", and opposites cancel.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `([A] [(<[A]>)])` | [[mult.multiplication]] | A × (1/A), [[Q.reciprocal]] |
    | `([A] <[A]>)` | [[mult.involution]] | `[(X)] ≐ X` with X = `<[A]>` — Involution-down; X is real |
    | `(void)` | [[Z.inversion]] | `[A] <[A]>` cancels |
    | `o` | [[N.unit]] | the empty round boundary is the unit |

    ## Confirms

    The multiplicative-inverse law of a field, derived from the additive one: the multiplicative group of ℚ⁺ is the additive group of its logarithms, and Inversion serves both. It is the cleanest instance of the chart's refrain that every multiplicative law is an additive law one level deeper.

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical | holds | — |
    | J1 | holds | the Involution-down step sits at depth 1 under the instance: the depth-1 criterion ([[mult.involution]], Notes) |
    | JH, JO | holds | `x · x⁻¹ ≐ o` is the Cancellation axiom OC there (right inverse); the left inverse `x⁻¹ · x ≐ o` is a three-line theorem — an axiom, because the ordered product no longer reduces to a sum of abstracts |
    | JP | guarded | for units at the place |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    Price comparison worth seeing in the chart: here this law is a theorem of Involution + Inversion; in JH it must be *posited* (axiom OC) because Splice and the ordered bracket cut the route through the sum of abstracts. The same fact, two prices, one setting apart.
    """,
)

node(
    id="Q.division-as-product", title="Dividing is multiplying by the reciprocal", type="theorem", level="object", kind="law",
    order=530, domain="positive", law="([A] [(<[B]>)]) ≐ ([A] <[B]>)", units="a · (1/b) = a ÷ b", gloss_check="A / B",
    holds_over={"JH": "replaced", "JO": "replaced", "JP": "guarded"}, status="NATIVE", verified="engine",
    known_since="1993 (James); the rule is ancient", guide="shape-led", band="6–8",
    uses=["mult.multiplication", "Q.reciprocal", "mult.involution", "Q.division"], see_also=["Q.multiply-fractions"],
    aliases=["invert and multiply", "a/b = a · b⁻¹"], concepts=["division", "multiplication"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([A] [(<[B]>)]) ≐ ([A] <[B]>)` | — | a · (1/b) = a ÷ b |

    ## Plain

    Dividing by a number is the same as multiplying by one over it — the boxed reciprocal unboxes to a mirrored box.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `([A] [(<[B]>)])` | [[mult.multiplication]] | A × (1/B), [[Q.reciprocal]] |
    | `([A] <[B]>)` | [[mult.involution]] | `[(X)] ≐ X` with X = `<[B]>`; the result is A ÷ B by [[Q.division]] |

    ## Confirms

    "Invert and multiply", as one Involution. The schoolroom rule for dividing by a fraction is this law followed by [[Q.flip]] and [[Q.multiply-fractions]] — see [[Q.divide-by-fraction]].

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical | holds | — |
    | J1 | holds | the Involution-down step sits at depth 1 under the instance — the depth-1 criterion ([[mult.involution]], Notes) |
    | JH, JO | replaced | `x · y⁻¹` and `y⁻¹ · x` differ; the ordered bracket carries both |
    | JP | guarded | for unit divisors |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.fraction", title="Fractions are quotients of piles", type="definition", level="object", kind="schema",
    order=540, domain="natural", law="([oo] <[ooo]>) := 2/3", units="m/n = ([o^m] <[o^n]>)", gloss_check="2/3",
    holds_over={"JP": "guarded"}, readings_over={"finset": "ANALOGY"}, status="NATIVE", verified="engine",
    known_since="1993 (James); fractions are Egyptian", guide="shape-led", band="3–5",
    uses=["Q.division", "N.numeral"], see_also=["Q.half", "Q.cancel-common-factor", "Q.rational"],
    aliases=["m/n", "numerator and denominator"], concepts=["fraction", "division"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([oo] <[ooo]>)` | — | 2/3 |

    A fraction is a pile divided by a pile: the numerator's abstract and the mirrored abstract of the denominator, under one instance.

    ## Plain

    Two-thirds is the pile of two, boxed, next to the mirrored box of the pile of three, all circled.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `([oo] <[ooo]>)` | [[Q.division]] | 2 ÷ 3, with the piles of [[N.numeral]] |
    | `2/3` | name | — |

    ## Confirms

    The positive rationals as inscriptions. Equality of fractions is **not** visible yet — `([oo]<[oooo]>)` and `([o]<[oo]>)` are different inscriptions of ½ — and becomes a theorem at [[Q.cancel-common-factor]]; the choice of a canonical one is the gap [[Q.lowest-terms]].

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical, J1, JH, JO | holds | real content |
    | JP | guarded | a fraction is a form at p only when its denominator is a unit at p; `([o]<[oo]>)` is not a 2-adic integer |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ANALOGY | m · (1/n) as the cardinality of an action groupoid (m points, a ℤ/n acting freely) — the Baez–Dolan reading of [[Q.half]], extended |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.half", title="One half", type="definition", level="object", kind="law",
    order=550, domain="natural", law="½ := (<[oo]>)", units="½ = e^{−ln 2}", gloss_check="0.5",
    holds_over={"JP": "guarded"}, readings_over={"finset": "ANALOGY"}, status="NATIVE", verified="engine",
    known_since="1993 (James); ½ is ancient", guide="shape-led", band="3–5",
    uses=["Q.reciprocal", "N.numeral"], see_also=["Q.halves", "Q.fractional-cardinality"],
    aliases=["1/2", "one half", "(<[oo]>)"], concepts=["fraction"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `(<[oo]>)` | — | ½ |

    The first fraction: the reciprocal of two. It is the count that will later halve J and so produce i — `i ≐ (([J] <[oo]>))` is e^{iπ/2} — which is why the chart gives ½ its own node.

    ## Plain

    A half is one over two: the pile of two, boxed, mirrored, circled.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `(<[oo]>)` | [[Q.reciprocal]] | 1/A with A the pile of two, [[N.numeral]] |
    | `½` | name | — |

    ## Confirms

    ½ as e^{−ln 2}. What it is **not**: a new kind of number. A fractional *count* is the same cardinality mechanism as `([A][oo])`, with the count mirrored; nothing is added to the calculus to admit fractions.

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical, J1, JH, JO | holds | — |
    | JP | guarded | at p = 2 the form is not an integer at the place; at odd p it is a unit |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ANALOGY | the one-object groupoid with a ℤ/2 of automorphisms has Baez–Dolan cardinality ½: fractional counts as counts of symmetry — the reading under which `< >` on a count becomes a quotient by a group action |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.halves", title="Two halves make one", type="theorem", level="object", kind="law",
    order=560, domain="natural", law="(<[oo]>) (<[oo]>) ≐ o", units="½ + ½ = 1", gloss_check="1",
    holds_over={"JP": "guarded"}, status="NATIVE", verified="engine",
    known_since="1993 (James); the fact is ancient", guide="shape-led", band="3–5",
    uses=["Q.half", "mult.cardinality", "mult.involution", "Z.inversion", "N.unit"], see_also=["Q.fractional-cardinality"],
    aliases=["½ + ½ = 1"], concepts=["fraction", "addition"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `(<[oo]>) (<[oo]>) ≐ o` | — | ½ + ½ = 1 |

    ## Plain

    Two halves side by side are one whole — the two copies collect into a count of two, which cancels the mirrored two.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `(<[oo]>) (<[oo]>)` | given | two halves, [[Q.half]] |
    | `([(<[oo]>)] [oo])` | [[mult.cardinality]] | two copies of X are X with count 2 |
    | `(<[oo]> [oo])` | [[mult.involution]] | `[(X)] ≐ X` |
    | `(void)` | [[Z.inversion]] | `<[oo]> [oo]` cancels |
    | `o` | [[N.unit]] | — |

    ## Confirms

    The first arithmetic of fractions, and the mechanism behind all of it: *repetition becomes a count, and a count cancels its mirror*. Every "n copies of 1/n make 1" is this derivation with `oo` replaced by the pile of n.

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical, J1, JH, JO | holds | in J1 the Involution-down step sits at depth 1 under the instance (depth-1 criterion, [[mult.involution]] Notes) |
    | JP | guarded | needs ½ to be a form at the place (odd p) |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.fractional-cardinality", title="Fractional cardinality — half of a form, twice, is the form", type="theorem", level="object", kind="schema",
    order=570, domain="positive", law="([A] <[oo]>) ([A] <[oo]>) ≐ A", units="a/2 + a/2 = a ; in general n copies of ([A]<[o^n]>) ≐ A", gloss_check="A",
    holds_over={"JP": "guarded"}, status="NATIVE", verified="engine",
    known_since="1993 (James) for the mechanism; 'fractional cardinality' is the name Book One uses; the arithmetic is ancient", guide="shape-led", band="3–5",
    uses=["Q.division", "mult.cardinality", "mult.involution", "Z.inversion"], see_also=["Q.halves", "mult.cardinality"],
    aliases=["fractional cardinality", "a/n", "mirrored count"], concepts=["fraction", "division", "counting"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([A] <[oo]>) ([A] <[oo]>) ≐ A` | — | a/2 + a/2 = a |

    Cardinality with a mirrored count: `([A] <[o^n]>)` is "A with count 1/n", and n copies of it collect back to A. This is James's fractional cardinality, the mechanism that will give roots one level down (`(([[A]] <[oo]>))` = √a at rung `alg`) and, when the form is J, the roots of −1 — `(([J] <[o^n]>))` is e^{iπ/n}, a 2n-th root of unity.

    ## Plain

    Half of something, twice, is the thing — and "half of" is just "with a mirrored count of two".

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `([A] <[oo]>) ([A] <[oo]>)` | given | two copies of A ÷ 2, [[Q.division]] |
    | `([([A] <[oo]>)] [oo])` | [[mult.cardinality]] | two copies are one copy with count 2 |
    | `([A] <[oo]> [oo])` | [[mult.involution]] | `[(X)] ≐ X` |
    | `([A])` | [[Z.inversion]] | `<[oo]> [oo]` cancels |
    | `A` | [[mult.involution]] | `([A]) ≐ A` |

    ## Confirms

    That counts need not be piles: a mirrored pile is a count too, and the same two theorems (Cardinality, Inversion) govern it. Nothing is added to admit fractions of arbitrary forms; the "for every n" is the usual schema ([[N.induction]]).

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical, J1, JH, JO | holds | in J1 the Involution-down step sits at depth 1 under the instance (depth-1 criterion, [[mult.involution]] Notes) |
    | JP | guarded | `([A]<[o^n]>)` is a form at p iff n is a unit at p (Division-by-unit, Part II Ch. 10); the separate selection `d | p−1` (and `d | 2` at p = 2) concerns fractional counts of ω — which roots of unity exist at p — and belongs to rung C |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | the ψ-road: `ψ^r` is a cardinality-power; fractional counts are where the (b) road and the chart's trunk first share a form |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.cancel-common-factor", title="Equivalent fractions — a common factor cancels", type="theorem", level="object", kind="law",
    order=580, domain="positive", law="([([A] [C])] <[([B] [C])]>) ≐ ([A] <[B]>)", units="(ac)/(bc) = a/b", gloss_check="A / B",
    holds_over={"JH": "replaced", "JO": "replaced", "JP": "guarded"}, status="NATIVE", verified="engine",
    known_since="1993 (James); the fact is Euclid VII", guide="shape-led", band="3–5",
    uses=["Q.division", "mult.multiplication", "mult.involution", "Z.collection", "Z.inversion", "void.space"], see_also=["Q.lowest-terms", "Q.fraction", "Q.quotient-of-numerals"],
    aliases=["equivalent fractions", "reducing a fraction", "cancelling"], concepts=["fraction", "division"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([([A] [C])] <[([B] [C])]>) ≐ ([A] <[B]>)` | — | (a·c) ÷ (b·c) = a ÷ b |

    ## Plain

    A factor shared by the top and bottom of a fraction disappears: under the box it is a plus and a minus of the same thing.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `([([A] [C])] <[([B] [C])]>)` | given | (a·c) ÷ (b·c): [[Q.division]] of two products, [[mult.multiplication]] |
    | `([A] [C] <[([B] [C])]>)` | [[mult.involution]] | `[(X)] ≐ X` on the numerator |
    | `([A] [C] <[B] [C]>)` | [[mult.involution]] | the same on the denominator |
    | `([A] [C] <[B]> <[C]>)` | [[Z.collection]] | split the mirror; regroup by [[void.space]] |
    | `([A] <[B]>)` | [[Z.inversion]] | `[C] <[C]>` cancels |

    ## Confirms

    Equivalent fractions. With it, and with [[Q.division-by-one]], `6 ÷ 2 ≐ 3` becomes the theorem [[Q.quotient-of-numerals]]. The schoolroom "cancel the common factor" is literally Inversion on the abstracts. What it does **not** give is a *canonical* reduced form — see [[Q.lowest-terms]].

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical | holds | — |
    | J1 | holds | the Involution-down steps sit at depth 1 under the instance (depth-1 criterion, [[mult.involution]] Notes) |
    | JH, JO | replaced | a common factor cancels only where it meets its own inverse — the right factor of `x·y⁻¹`, the left factor of `y⁻¹·x`; on the other side it conjugates instead |
    | JP | guarded | cancelling a factor that is the prime involves `<[p]>`, which is not a form at p |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.add-fractions", title="Adding fractions", type="theorem", level="object", kind="law",
    order=590, domain="positive", law="([A] <[B]>) ([C] <[D]>) ≐ ([([A] [D]) ([C] [B])] <[B]> <[D]>)", units="a/b + c/d = (ad + cb)/(bd)", gloss_check="A/B + C/D",
    holds_over={"JH": "replaced", "JO": "replaced", "JP": "guarded"}, status="NATIVE", verified="engine",
    known_since="1993 (James); the rule is ancient", guide="need-led", band="3–5",
    uses=["Q.division", "mult.multiplication", "mult.distribution", "mult.involution", "Z.inversion", "void.space"], see_also=["Q.multiply-fractions", "Q.cancel-common-factor", "Q.negative-fraction"],
    aliases=["common denominator", "a/b + c/d"], concepts=["fraction", "addition"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([A] <[B]>) ([C] <[D]>) ≐ ([([A] [D]) ([C] [B])] <[B]> <[D]>)` | — | a/b + c/d = (ad + cb)/(bd) |

    The denominator bd is written `<[B]> <[D]>`, which is `<[([B][D])]>` by Involution and collection (an equality of bare abstracts: exact classically, mod Λ in J1); the chart keeps the split form because that is the shape Distribution produces.

    ## Plain

    To add two fractions you bring them to a common bottom — and on the page that is one use of Distribution, read backwards: two circles sharing the same mirrored boxes collect into one.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `([([A] [D]) ([C] [B])] <[B]> <[D]>)` | given | (ad + cb) ÷ (bd): [[Q.division]] with the products of [[mult.multiplication]] |
    | `([([A] [D])] <[B]> <[D]>) ([([C] [B])] <[B]> <[D]>)` | [[mult.distribution]] | `(X [Y Z]) ≐ (X [Y]) (X [Z])` with X = `<[B]> <[D]>` |
    | `([A] [D] <[B]> <[D]>) ([C] [B] <[B]> <[D]>)` | [[mult.involution]] | `[(Y)] ≐ Y`, in each factor |
    | `([A] <[B]>) ([C] <[D]>)` | [[Z.inversion]] | `[D] <[D]>` cancels in the first, `[B] <[B]>` in the second; regroup by [[void.space]] |

    ## Confirms

    The common-denominator rule, derived in the direction that explains it: start from the single fraction and *distribute*. The "cross-multiplication" the rule is usually taught as is the Involution rows. Tagged *need-led*: the forms do not ask for a common denominator; the wish to see a sum of fractions as one fraction does. Subtraction of fractions is this law with [[Q.negative-fraction]].

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical | holds | — |
    | J1 | holds | the Involution-down steps sit at depth 1 under their instances (depth-1 criterion, [[mult.involution]] Notes) |
    | JH, JO | replaced | Distribution is replaced by its two-sided list form; the sum of two quotients needs sides |
    | JP | guarded | for unit denominators |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.multiply-fractions", title="Multiplying fractions", type="theorem", level="object", kind="law",
    order=600, domain="positive", law="([([A] <[B]>)] [([C] <[D]>)]) ≐ ([([A] [C])] <[([B] [D])]>)", units="(a/b)(c/d) = (ac)/(bd)", gloss_check="(A*C)/(B*D)",
    holds_over={"JH": "replaced", "JO": "replaced", "JP": "guarded"}, status="NATIVE", verified="engine",
    known_since="1993 (James); the rule is ancient", guide="shape-led", band="6–8",
    uses=["mult.multiplication", "Q.division", "mult.involution", "Z.collection", "void.space"], see_also=["Q.division-as-product", "Q.reciprocal-of-product", "Q.divide-by-fraction"],
    aliases=["(a/b)(c/d)", "multiply across"], concepts=["fraction", "multiplication"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([([A] <[B]>)] [([C] <[D]>)]) ≐ ([([A] [C])] <[([B] [D])]>)` | — | (a/b)(c/d) = (ac)/(bd) |

    ## Plain

    Multiply tops together and bottoms together — because under the box everything is a sum, and the mirrors gather.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `([([A] <[B]>)] [([C] <[D]>)])` | given | (a/b) × (c/d): [[mult.multiplication]] of two quotients, [[Q.division]] |
    | `([A] <[B]> [C] <[D]>)` | [[mult.involution]] | `[(X)] ≐ X`, twice |
    | `([A] [C] <[B] [D]>)` | [[Z.collection]] | gather the mirrors; regroup by [[void.space]] |
    | `([([A] [C])] <[([B] [D])]>)` | [[mult.involution]] | the unit `X ≐ [(X)]`, twice, right to left — writing the numerator and denominator as products again |

    ## Confirms

    "Multiply across". Dividing by a fraction is [[Q.divide-by-fraction]]. The whole fraction arithmetic of grades 3–8 is a handful of theorems of Involution, Distribution, Inversion and their two corollaries (collection, cardinality).

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical | holds | — |
    | J1 | holds | the unit steps (both directions) sit at depth 1 under the instance (depth-1 criterion, [[mult.involution]] Notes) |
    | JH, JO | replaced | order of factors matters; the ordered bracket's Splice carries the product |
    | JP | guarded | for unit denominators |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.reciprocal-of-product", title="The reciprocal of a product is the product of reciprocals", type="theorem", level="object", kind="law",
    order=610, domain="positive", law="(<[([A] [B])]>) ≐ (<[A]> <[B]>)", units="1/(ab) = (1/a)(1/b)", gloss_check="1/(A*B)",
    holds_over={"JH": "replaced", "JO": "replaced", "JP": "guarded"}, status="NATIVE", verified="engine",
    known_since="1993 (James); the fact is ancient", guide="shape-led", band="6–8",
    uses=["Q.reciprocal", "mult.multiplication", "mult.involution", "Z.collection"], see_also=["Z.collection", "Q.multiply-fractions"],
    aliases=["1/(ab)", "reciprocal of a product"], concepts=["division", "inverse"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `(<[([A] [B])]>) ≐ (<[A]> <[B]>)` | — | 1/(ab) = (1/a)(1/b) |

    The right-hand side is the product `([(<[A]>)] [(<[B]>)])` with its two Involutions already taken: inverse collection ([[Z.collection]]), one level deeper, becomes the law of reciprocals.

    ## Plain

    One over a product is the product of the one-overs — the mirror splits over the two boxes.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `(<[([A] [B])]>)` | given | 1/(ab): [[Q.reciprocal]] of a product, [[mult.multiplication]] |
    | `(<[A] [B]>)` | [[mult.involution]] | `[(X)] ≐ X` |
    | `(<[A]> <[B]>)` | [[Z.collection]] | split the mirror |

    ## Confirms

    (ab)⁻¹ = a⁻¹b⁻¹ — true here because breadth commutes. In ℍ the same law reads (xy)⁻¹ = y⁻¹x⁻¹ and *reverses the order*: JH's Reversal rule. The chart records that as `replaced`: the law survives with its factors reversed, which the unordered page cannot express — the commutative case restricts back.

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical | holds | — |
    | J1 | holds | depth-1 criterion ([[mult.involution]], Notes) |
    | JH, JO | replaced | by Reversal, `<[x₁;…;xₙ]> ≐ [(<[xₙ]>);…;(<[x₁]>)]` — the order flips; this law is its commutative case |
    | JP | guarded | for units |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.negative-fraction", title="A sign on top is a sign in front", type="theorem", level="object", kind="law",
    order=620, domain="positive", law="([<A>] <[B]>) ≐ <([A] <[B]>)>", units="(−a)/b = −(a/b)", gloss_check="-A/B",
    holds_over={"JP": "guarded"}, status="NATIVE", verified="engine",
    known_since="1993 (James); the sign rule is ancient", guide="shape-led", band="6–8",
    uses=["Q.division", "mult.inverse-promotion"], see_also=["Q.negative-denominator", "Q.reciprocal-of-negative", "mult.product-of-negatives", "Q.rational"],
    aliases=["(−a)/b = −(a/b)", "sign of a fraction"], concepts=["fraction", "negation"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([<A>] <[B]>) ≐ <([A] <[B]>)>` | — | (−a)/b = −(a/b) |

    The sign on the *bottom*, a/(−b) = −(a/b), is **not** the same promotion: it needs the reciprocal of a negative, which costs a trip through the seam ([[Q.reciprocal-of-negative]], [[Q.negative-denominator]]).

    ## Plain

    A minus on the top of a fraction is the same as a minus in front of it.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `([<A>] <[B]>)` | given | (−a) ÷ b, [[Q.division]] |
    | `<([A] <[B]>)>` | [[mult.inverse-promotion]] | `<(X [Y])> ≐ (X [<Y>])` with X = `<[B]>` and Y = A, used right to left |

    ## Confirms

    The sign rule for fractions as one instance of inverse promotion — no unit step at all, so it is exact on all of ℂ× even though `[<A>]` is `ln a + iπ`; the engine samples positive a and b, where the mirror is the only sign.

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical, JH, JO | holds | the Inversion cluster |
    | J1 | holds | per the survival ledger (promotion unchanged); the chart's own derivation of [[mult.inverse-promotion]] routes through zero-annihilates, whose J1 cell is untested |
    | JP | guarded | the denominator must be a unit at p |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | exact on all of ℂ×, not only on the sampled positive domain |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    - ~~a/(−b) = −(a/b) follows "by the same promotion with the roles exchanged"~~ — the first draft (2026-10-03) claimed this in prose; the referee pass the same day showed no instantiation of inverse promotion matches `([A] <[<B>]>)`. The bottom-sign law is [[Q.negative-denominator]] and needs [[Q.reciprocal-of-negative]].

    ## Notes

    —
    """,
)

node(
    id="Q.rational", title="The rational numbers", type="definition", level="object", kind="schema",
    order=630, domain="natural", law="<([oo] <[ooo]>)> := −2/3", units="ℚ = { ([o^m] <[o^n]>) with n ≥ 1, their mirrors, and the void }", gloss_check="-2/3",
    holds_over={"JP": "guarded"}, status="NATIVE", verified="engine",
    known_since="1993 (James)", guide="shape-led", band="6–8",
    uses=["Z.angle", "Q.fraction", "void.page"], see_also=["Z.normal-form", "Q.lowest-terms", "Q.cross-multiplication", "N.order"],
    aliases=["ℚ", "rational number", "signed fraction"], concepts=["fraction", "integer", "negation", "normal-form"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `<([oo] <[ooo]>)>` | — | −2/3 |

    A rational number is a fraction of piles, the mirror of one, or the void. The class is closed under the arithmetic of this rung: a juxtaposition of instances, mirrored or not, whose contents are juxtapositions of `[pile]` and `<[pile]>`, reduces to one of these — a normal-form theorem owed as `Q.normal-form` (see Notes).

    ## Plain

    The rationals are the fractions, their mirror images, and zero.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `<([oo] <[ooo]>)>` | [[Z.angle]] | the mirror of a fraction, [[Q.fraction]]; the void is [[void.page]] |
    | `−2/3` | name | — |

    ## Confirms

    ℚ as a set of inscriptions. Two things are **not** given: that two inscriptions name the same rational ([[Q.cancel-common-factor]] decides it instance by instance; a canonical form is [[Q.lowest-terms]]), and the order and density of ℚ ([[N.order]]). The field laws are all above this node — as axioms (Inversion, Distribution), medium facts (commutativity, identity), theorems (the rest), and one meta node (0 ≠ 1, [[mult.consistency]]).

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical, J1, JH, JO | holds | — |
    | JP | guarded | fractions with unit denominators are integers at the place — the re-entrant "dolls" (periodic expansions) of the p-adic-wall thread, whose completion is ℤ_p; fractions with the prime in the denominator are not forms at p at all (No-inverse-of-the-prime) |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    - ~~every form in which each pile occurs only as `[pile]` or `<[pile]>` directly under an instance is rational~~ — refuted 2026-10-03 (second referee pass): `(([oo]))` = e² fits that description. The class must be stated as juxtapositions of (mirrored) instances of such contents.

    ## Notes

    The normal-form theorem for this class — derivable from [[Q.add-fractions]], [[Q.negative-fraction]], [[mult.product-of-numerals]], [[Z.normal-form]], [[Q.zero-divided]] for a void numerator, and the degenerate shapes [[Q.division-by-one]] and [[Q.one-over-a]] — is not yet written as a node; `Q.normal-form` is owed.
    """,
)

node(
    id="Q.zero-divided", title="Zero divided by a nonzero number is zero", type="theorem", level="object", kind="law",
    order=640, domain="positive", law="(□ <[A]>) ≐ void", units="0 ÷ a = 0", gloss_check="0",
    holds_over={"J1": "untested"}, status="NATIVE", verified="engine",
    known_since="1993 (James); the fact is ancient", guide="shape-led", band="3–5",
    uses=["Q.division", "mult.black-hole", "mult.dominion", "mult.hole-instance"], see_also=["Q.no-division-by-zero"],
    aliases=["0/a = 0"], concepts=["zero", "division"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `(□ <[A]>) ≐ void` | — | 0 ÷ a = 0 |

    ## Plain

    Nothing shared among any number of people (at least one) is nothing each: the bottomless pit swallows the divisor and the circled pit is zero.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `(□ <[A]>)` | given | 0 ÷ A: the abstract of the void is □, [[mult.black-hole]], in the shape of [[Q.division]] |
    | `(□)` | [[mult.dominion]] | □ swallows `<[A]>` |
    | `void` | [[mult.hole-instance]] | the instance of the hole is nothing |

    ## Confirms

    0/a = 0 as a two-step consequence of the black hole's two laws. Its mirror image, a/0, is not a theorem but an exclusion ([[Q.no-division-by-zero]]) — the chart shows the asymmetry as the asymmetry between Dominion (a law) and the undefined form (a decree).

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical | holds | — |
    | J1 | untested | inherits the open status of □ in J1 |
    | JH, JO, JP | holds | — |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.no-division-by-zero", title="There is no form for dividing by zero", type="theorem", level="meta", kind="law",
    order=650, domain="positive", law="([A] <[void]>) is not a form", units="a ÷ 0 is undefined",
    holds_over={}, status="NATIVE-BY-DECREE", verified="hand",
    known_since="1993 (James)", guide="need-led", band="3–5",
    uses=["Q.division", "mult.black-hole", "mult.hole-exclusion"], see_also=["Q.zero-divided", "Q.reciprocal"],
    aliases=["division by zero", "a/0"], concepts=["zero", "division", "infinity"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([A] <[void]>)` | — | a ÷ 0 — not admissible |

    ## Plain

    You cannot divide by zero, and the page shows why: the shape you would have to draw contains the one mark the calculus refuses.

    ## Derivation

    | statement | rule | note |
    |---|---|---|
    | `([A] <[void]>)` is the shape of A ÷ 0 | [[Q.division]] | — |
    | its subform `<[void]>` is `<□>`, the mirror of the black hole | [[mult.black-hole]] | — |
    | `<□>` is excluded, up to ≐, so the shape is not an admissible form and no derivation may contain it | [[mult.hole-exclusion]] | the decree, not a theorem of the axioms |

    ## Confirms

    That "undefined" is the right word, not "infinite": the calculus does not assign a/0 a value it then refuses to use; it has no inscription for it at all. The same decree bans inverting a singular matrix in JH (JH-20) and is what keeps the calculus from collapsing ([[mult.consistency]]).

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | all | holds | the exclusion is kept in every extension |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    Status NATIVE-BY-DECREE because the law is a consequence of a decree; verification `hand` because a meta statement has no witness script — the engine's `Excluded` exception on evaluation is the mechanized version, but it is not stated as a rule the checker reports on.
    """,
)

node(
    id="Q.lowest-terms", title="Lowest terms — a canonical fraction", type="gap", level="meta", kind="concept",
    order=660, domain="natural", law="GAP — 'the reduced form of a fraction' is not an equation: deciding it needs a greatest common divisor, which is an iteration",
    units="gcd(m, n) ; m/n in lowest terms",
    holds_over={"classical": "fails", "J1": "fails", "JH": "fails", "JO": "fails", "JP": "fails"},
    readings_fix={"C": "ABSENT", "finset": "PARTIAL"}, status="ABSENT", verified="hand",
    known_since="Euclid VII (the algorithm); the gap named here 2026-10-03", guide="need-led", band="3–5",
    uses=[], see_also=["Q.cancel-common-factor", "Q.cross-multiplication", "Z.normal-form", "N.order", "N.induction"],
    aliases=["reduced fraction", "gcd", "Euclid's algorithm", "canonical form of a rational"], concepts=["fraction", "normal-form"], understood="partial",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | none | — | m/n with gcd(m, n) = 1 |

    [[Q.cancel-common-factor]] proves that two fractions with a common factor are ≐; it does not say *which* fraction is the canonical one, nor how to find the common factor. Both are the job of Euclid's algorithm, and an algorithm is an iteration — "repeat until the remainder is void" — which no single equation states. The integers had a normal form by a terminating rewrite ([[Z.normal-form]]); the rationals do not, yet.

    ## Plain

    The page can show that 2/4 and 1/2 are equal; it cannot by itself say that 1/2 is the "real" name, because finding the shared factor takes a repeated step the page has no form for.

    ## Derivation

    none — gap.

    ## Confirms

    That for the rationals a *canonical* name needs factoring, not a local rewrite: given two fraction forms, ≐ is decidable by [[Q.cross-multiplication]] (compare two piles), but a reduced representative needs the greatest common divisor, which no single cancellation finds. The gap is the same shape as [[N.induction]] — a "repeat" the equational calculus cannot say — and it is the first place the chart meets the re-entry idea from the place calculus (a guarded iteration that converges).

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | all | fails | no setting has an iteration construct; JP's guarded re-entry (JP-1) is the nearest thing and is not in the classical setting |

    | reading | cell | why |
    |---|---|---|
    | C | ABSENT | — |
    | finset | PARTIAL | in finite sets a fraction m/n is a class of pairs; the canonical representative is a choice, and the groupoid-cardinality reading ([[Q.half]]) suggests the class, not the representative, is the object |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —

    ## Plan

    | field | content |
    |---|---|
    | candidate form(s) | none as an equation. Candidate *meta-form*: Euclid as a guarded re-entry on piles — `x ≐ remainder(y, x)` iterated — in the style of the place calculus's JP-1 convention, where a re-entry with a shrinking guard converges |
    | law(s) to add, and type | a `definition` at the meta level (the reduced form := the result of repeated [[Q.cancel-common-factor]] until no common pile divides both), or a `decree` (choose the representative with the smallest denominator pile) |
    | nativity criterion | the procedure may use only cancel-common-factor, the normal form of piles, and a termination argument on pile size — no external gcd |
    | refutation test | two fraction forms equal in ℂ whose cancellation sequences reach different "irreducible" forms (impossible if gcd is well-defined; the test bites on the termination argument) |
    | meta-move? | yes: iteration / re-entry. The gap is a statement about a *process* on forms, not about a form; it is the first appearance of the fixed-point idea Lui favours for constructive computation |
    | owner thread | p-adic-wall (re-entry, JP-1); boundary-lean-game |
    | rank | meta-definition (iterated cancellation) < decree (smallest denominator) < new primitive (an iteration boundary — not proposed) |
    """,
)

# ----------------------------------------------------------------------------- laws added after the referee pass (2026-10-03)

SEAM = ("Involution-down at the **seam**: the content is negative, so in the ℂ reading the two abstracts differ by the period 2πi; "
        "as forms of the classical calculus they are equal, and the enclosing instance absorbs the period — the J1 receipt in miniature")

node(
    id="Q.self-division", title="A number divided by itself is one", type="theorem", level="object", kind="law",
    order=502, domain="positive", law="([A] <[A]>) ≐ o", units="a ÷ a = 1", gloss_check="1",
    holds_over={"JP": "guarded"}, status="NATIVE", verified="engine",
    known_since="1993 (James); the fact is ancient", guide="shape-led", band="3–5",
    uses=["Q.division", "Z.inversion", "N.unit"], see_also=["Q.reciprocal-law", "Q.division-by-one"],
    aliases=["a/a = 1"], concepts=["division", "one"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([A] <[A]>) ≐ o` | — | a ÷ a = 1 |

    ## Plain

    Anything divided by itself is one: under the box, a thing and its mirror cancel, and the circle around nothing is one.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `([A] <[A]>)` | given | a ÷ a, [[Q.division]] |
    | `(void)` | [[Z.inversion]] | `[A] <[A]>` cancels |
    | `o` | [[N.unit]] | — |

    ## Confirms

    The most basic fact of division, as one Inversion. It is **not** `0 ÷ 0`: with A the void the form contains `<□>` and is excluded ([[Q.no-division-by-zero]]).

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical, J1, JH, JO | holds | Inversion only; it survives verbatim in JH (the inverse cluster) |
    | JP | guarded | for units |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.division-by-one", title="Dividing by one changes nothing", type="theorem", level="object", kind="law",
    order=504, domain="positive", law="([A] <[o]>) ≐ A", units="a ÷ 1 = a", gloss_check="A",
    holds_over={}, status="NATIVE", verified="engine",
    known_since="1993 (James); the fact is ancient", guide="shape-led", band="3–5",
    uses=["Q.division", "mult.unit-law", "Z.void-inverse", "void.page", "mult.involution"], see_also=["Q.self-division", "mult.unit-law"],
    aliases=["a/1 = a"], concepts=["division", "one"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([A] <[o]>) ≐ A` | — | a ÷ 1 = a |

    ## Plain

    Dividing by one does nothing, because the box around one is empty and the mirror of nothing is nothing.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `([A] <[o]>)` | given | a ÷ 1, [[Q.division]] |
    | `([A] <>)` | [[mult.unit-law]] | `[o] ≐ void` |
    | `([A] void)` | [[Z.void-inverse]] | `<> ≐ void` |
    | `([A])` | [[void.page]] | — |
    | `A` | [[mult.involution]] | `([A]) ≐ A` |

    ## Confirms

    a/1 = a, and a small reunion: two of the three empty boundaries appear — `()` as the divisor and `<>` on the way — and the third, `[]`, must not: `[o]` is `[()]`, which is void, not the black hole, and `<[]>` would be the excluded form.

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical, JH, JO, JP | holds | — |
    | J1 | holds | the `[o] → ω` step sits under an angle under the instance: depth-1 criterion ([[mult.involution]], Notes) |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.one-over-a", title="One divided by a number is its reciprocal", type="theorem", level="object", kind="law",
    order=512, domain="positive", law="([o] <[A]>) ≐ (<[A]>)", units="1 ÷ a = 1/a", gloss_check="1/A",
    holds_over={"JP": "guarded"}, status="NATIVE", verified="engine",
    known_since="1993 (James); the fact is ancient", guide="shape-led", band="6–8",
    uses=["Q.division", "Q.reciprocal", "mult.unit-law", "void.page"], see_also=["Q.reciprocal"],
    aliases=["1 ÷ a"], concepts=["division", "inverse"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([o] <[A]>) ≐ (<[A]>)` | — | 1 ÷ a = 1/a |

    ## Plain

    One divided by a number is one over that number — the box around one vanishes and leaves the reciprocal's shape.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `([o] <[A]>)` | given | 1 ÷ A, [[Q.division]] |
    | `(void <[A]>)` | [[mult.unit-law]] | `[o] ≐ void` |
    | `(<[A]>)` | [[void.page]] | the reciprocal, [[Q.reciprocal]] |

    ## Confirms

    That [[Q.reciprocal]] is the special case of [[Q.division]] it ought to be. In J1 the step `[o] ≐ void` becomes `[o] → ω`, a Λ-step the instance absorbs.

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical, JH, JO | holds | — |
    | J1 | holds | the `[o] ≐ void` step sits at depth 1 under the instance (depth-1 criterion, [[mult.involution]] Notes) |
    | JP | guarded | for units |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.double-reciprocal", title="The reciprocal of the reciprocal", type="theorem", level="object", kind="law",
    order=524, domain="positive", law="(<[(<[A]>)]>) ≐ A", units="1/(1/a) = a", gloss_check="A",
    holds_over={"JP": "guarded"}, status="NATIVE", verified="engine",
    known_since="1993 (James); the fact is ancient", guide="shape-led", band="6–8",
    uses=["Q.reciprocal", "mult.involution", "Z.cancellation"], see_also=["Z.cancellation", "Q.flip"],
    aliases=["1/(1/a) = a"], concepts=["inverse", "division"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `(<[(<[A]>)]>) ≐ A` | — | 1/(1/a) = a |

    Inverse cancellation ([[Z.cancellation]]) one level deeper: the multiplicative inverse is an involution because the additive one is.

    ## Plain

    One over one-over-a-number is the number again: unbox the inner circle and the two mirrors cancel.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `(<[(<[A]>)]>)` | given | the reciprocal of 1/A, [[Q.reciprocal]] |
    | `(<<[A]>>)` | [[mult.involution]] | `[(X)] ≐ X` with X = `<[A]>` |
    | `([A])` | [[Z.cancellation]] | two mirrors cancel |
    | `A` | [[mult.involution]] | `([A]) ≐ A` |

    ## Confirms

    (a⁻¹)⁻¹ = a. In JH it is the lemma inside the "left inverse needs three lines" argument (x⁻¹x = x⁻¹(x⁻¹)⁻¹ = 1), with the Involution-down guarded off the seam.

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical, JH, JO | holds | — |
    | J1 | holds | depth-1 criterion ([[mult.involution]], Notes) |
    | JP | guarded | for units |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.quotient-of-numerals", title="A quotient of piles that divides evenly is a pile", type="theorem", level="object", kind="schema",
    order=585, domain="natural", law="([oooooo] <[oo]>) ≐ ooo", units="6 ÷ 2 = 3 ; in general ([o^{mn}] <[o^n]>) ≐ o^m", gloss_check="3",
    holds_over={"JP": "guarded"}, status="NATIVE", verified="engine",
    known_since="1993 (James); the fact is ancient", guide="shape-led", band="3–5",
    uses=["Q.division", "mult.product-of-numerals", "mult.involution", "Z.inversion", "N.numeral"], see_also=["Q.cancel-common-factor", "mult.product-of-numerals"],
    aliases=["6 ÷ 2 = 3", "exact division"], concepts=["division", "natural-number"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([oooooo] <[oo]>) ≐ ooo` | — | 6 ÷ 2 = 3 |

    The defined division agrees with the schoolroom's on numerals that divide evenly: write the dividend as a product and cancel. This is the law that makes [[Q.division]] *division* and not merely a shape — the counterpart of [[mult.product-of-numerals]].

    ## Plain

    Six divided by two really is three: six is three-times-two, and the two cancels against its mirror.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `([oooooo] <[oo]>)` | given | 6 ÷ 2, [[Q.division]] with the piles of [[N.numeral]] |
    | `([([ooo] [oo])] <[oo]>)` | [[mult.product-of-numerals]] | 6 is 3 × 2, right to left |
    | `([ooo] [oo] <[oo]>)` | [[mult.involution]] | `[(X)] ≐ X` |
    | `([ooo])` | [[Z.inversion]] | `[oo] <[oo]>` cancels |
    | `ooo` | [[mult.involution]] | `([A]) ≐ A` |

    ## Confirms

    Exact division of naturals. What happens when the division is *not* exact — `7 ÷ 2` — is a fraction, [[Q.fraction]], and the calculus does not prefer the mixed-number spelling `ooo (<[oo]>)` over it: the two inscriptions are convertible (≐) by Distribution with the context `<[oo]>`, this law, and the unit law.

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical, J1, JH, JO | holds | real content; the Involution-down step is on the strip |
    | JP | guarded | `<[oo]>` is not a form at p = 2; the law holds where the divisor is a unit |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.flip", title="The reciprocal of a fraction is the fraction flipped", type="theorem", level="object", kind="law",
    order=602, domain="positive", law="(<[([C] <[D]>)]>) ≐ ([D] <[C]>)", units="1/(c/d) = d/c", gloss_check="D/C",
    holds_over={"JP": "guarded"}, status="NATIVE", verified="engine",
    known_since="1993 (James); the fact is ancient", guide="shape-led", band="6–8",
    uses=["Q.reciprocal", "Q.division", "mult.involution", "Z.collection", "Z.cancellation"], see_also=["Q.divide-by-fraction", "Q.double-reciprocal"],
    aliases=["flip the fraction", "1/(c/d) = d/c"], concepts=["fraction", "inverse"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `(<[([C] <[D]>)]>) ≐ ([D] <[C]>)` | — | 1/(c/d) = d/c |

    ## Plain

    One over a fraction is the fraction upside down: the outer mirror splits over top and bottom, and the bottom's two mirrors cancel.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `(<[([C] <[D]>)]>)` | given | the reciprocal ([[Q.reciprocal]]) of c/d ([[Q.division]]) |
    | `(<[C] <[D]>>)` | [[mult.involution]] | `[(X)] ≐ X` |
    | `(<[C]> <<[D]>>)` | [[Z.collection]] | split the mirror |
    | `(<[C]> [D])` | [[Z.cancellation]] | two mirrors cancel on D |

    The result is `([D] <[C]>)`, which is d ÷ c by [[Q.division]].

    ## Confirms

    "Flip it": the rule behind dividing by a fraction ([[Q.divide-by-fraction]]). It is inverse collection and cancellation, one level deeper, exactly as [[Q.reciprocal-of-product]] was collection one level deeper.

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical | holds | — |
    | J1 | holds | depth-1 criterion ([[mult.involution]], Notes) |
    | JH, JO | holds | the law survives per quotient type by Reversal, `(xy⁻¹)⁻¹ = yx⁻¹`; the collection step inside the bracket does not transfer verbatim |
    | JP | guarded | for units |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.divide-by-fraction", title="Dividing by a fraction", type="theorem", level="object", kind="law",
    order=604, domain="positive", law="([([A] <[B]>)] <[([C] <[D]>)]>) ≐ ([([A] [D])] <[([B] [C])]>)", units="(a/b) ÷ (c/d) = (ad)/(bc)", gloss_check="(A*D)/(B*C)",
    holds_over={"JH": "replaced", "JO": "replaced", "JP": "guarded"}, status="NATIVE", verified="engine",
    known_since="1993 (James); the rule is ancient", guide="shape-led", band="6–8",
    uses=["Q.division", "mult.involution", "Z.collection", "Z.cancellation", "void.space"], see_also=["Q.flip", "Q.multiply-fractions", "Q.division-as-product"],
    aliases=["invert and multiply", "(a/b) ÷ (c/d)"], concepts=["fraction", "division"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([([A] <[B]>)] <[([C] <[D]>)]>) ≐ ([([A] [D])] <[([B] [C])]>)` | — | (a/b) ÷ (c/d) = (ad)/(bc) |

    ## Plain

    To divide by a fraction, flip it and multiply — on the page, the divisor's mirror splits over its top and bottom and the bottom's mirrors cancel, leaving top and bottom exchanged.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `([([A] <[B]>)] <[([C] <[D]>)]>)` | given | (a/b) ÷ (c/d), [[Q.division]] |
    | `([A] <[B]> <[C] <[D]>>)` | [[mult.involution]] | `[(X)] ≐ X`, twice |
    | `([A] <[B]> <[C]> <<[D]>>)` | [[Z.collection]] | split the divisor's mirror |
    | `([A] [D] <[B]> <[C]>)` | [[Z.cancellation]] | `<<[D]>> ≐ [D]`; regroup by [[void.space]] |
    | `([A] [D] <[B] [C]>)` | [[Z.collection]] | gather the two remaining mirrors |
    | `([([A] [D])] <[([B] [C])]>)` | [[mult.involution]] | the unit `X ≐ [(X)]`, twice, right to left |

    ## Confirms

    "Keep, change, flip" as three moves of the Inversion cluster and a regroup, under two Involutions. It is [[Q.flip]] followed by [[Q.multiply-fractions]], written out in one table.

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical | holds | — |
    | J1 | holds | depth-1 criterion ([[mult.involution]], Notes) |
    | JH, JO | replaced | order of factors matters |
    | JP | guarded | for unit denominators |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.reciprocal-of-negative", title="The reciprocal of a negative is the negative of the reciprocal", type="theorem", level="object", kind="law",
    order=622, domain="positive", law="(<[<A>]>) ≐ <(<[A]>)>", units="1/(−a) = −(1/a)", gloss_check="-1/A",
    holds_over={"JP": "guarded"}, status="NATIVE-BY-DECREE", verified="engine",
    known_since="1993 (James); the fact is ancient; the seam-crossing noted here 2026-10-03", guide="need-led", band="6–8",
    uses=["Q.reciprocal", "mult.multiplication", "mult.product-of-negatives", "Q.reciprocal-law", "mult.involution", "Z.inversion", "N.unit", "mult.unit-law", "void.space", "mult.seam-decree"],
    see_also=["Q.negative-denominator", "Q.negative-fraction", "mult.involution"],
    aliases=["1/(−a) = −(1/a)", "sign of a reciprocal"], concepts=["inverse", "negation"], understood="partial",
    understood_note="the seam steps are the part I want to watch at rung C",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `(<[<A>]>) ≐ <(<[A]>)>` | — | 1/(−a) = −(1/a) |

    The first law of the chart whose derivation crosses the **seam**: `[<A>]`, the abstract of a negative, is ln a + iπ in the ℂ reading, and the unit `[(X)] ≐ X` applied to content carrying it is exact only up to the period 2πi. Three such steps occur below; each sits in an absorbing position, so the seam decree ([[mult.seam-decree]]) admits it and the enclosing instance cancels the period. No seam-free classical derivation is known; James's own route is through the phase rule `[<A>] ≐ [A] J` at rung C, which relocates the one unavoidable crossing to a J-cancellation inside the instance — exactly where his discipline permits it.

    ## Plain

    One over minus-a is minus one-over-a. The page can show it, but only by passing through the place where "the log of a negative" lives — which is where the imaginary numbers are about to come from.

    ## Derivation

    First, `<(<[A]>)>` is an inverse of `<A>`:

    | form | rule | note |
    |---|---|---|
    | `([<A>] [<(<[A]>)>])` | given | (−a) × (−(1/a)), [[mult.multiplication]] |
    | `([A] [(<[A]>)])` | [[mult.product-of-negatives]] | two mirrors cancel across the product |
    | `o` | [[Q.reciprocal-law]] | a × (1/a) = 1 |

    Second, `(<[<A>]>)` is an inverse of `<A>`:

    | form | rule | note |
    |---|---|---|
    | `([<A>] [(<[<A>]>)])` | given | (−a) × (1/(−a)), [[Q.reciprocal]] |
    | `([<A>] <[<A>]>)` | [[mult.involution]] | `[(X)] ≐ X` with X = `<[<A>]>` — phased content, absorbing position: admitted by [[mult.seam-decree]] (seam step 1) |
    | `(void)` | [[Z.inversion]] | `[<A>] <[<A>]>` cancels |
    | `o` | [[N.unit]] | — |

    Inverses are unique:

    | form | rule | note |
    |---|---|---|
    | `(<[<A>]>)` | given | X, the left-hand side |
    | `([(<[<A>]>)] [o])` | [[mult.unit-law]] | X × 1, right to left |
    | `([(<[<A>]>)] [([<A>] [<(<[A]>)>])])` | lemma | 1 ≐ (−a) × (−(1/a)), the first table right to left |
    | `([(<[<A>]>)] [<A>] [<(<[A]>)>])` | [[mult.involution]] | `[(Z)] ≐ Z` on the inner product — Z = `[<A>] [<(<[A]>)>]` has value 2πi, so this is seam step 2, absorbing position; regroup by [[void.space]] |
    | `([([(<[<A>]>)] [<A>])] [<(<[A]>)>])` | [[mult.involution]] | `Z ≐ [(Z)]` on `[X][<A>]` (value 2πi), right to left — seam step 3, absorbing position |
    | `([o] [<(<[A]>)>])` | lemma | X × (−a) ≐ 1, the second table |
    | `<(<[A]>)>` | [[mult.unit-law]] | 1 × Y = Y |

    ## Confirms

    (−a)⁻¹ = −a⁻¹, by uniqueness of inverses, as in any field. What the chart adds is the *price*: three of the steps are the unit on content off the principal strip, admitted only by the seam decree — so the law is NATIVE-BY-DECREE, the first sign law to cost a decree. In J1 the same three steps post receipts of ±2πi, and the law holds exactly by the depth-1 criterion; these are the first ℚ laws whose receipts do not vanish. The engine passes every row because it evaluates whole rows: the periods cancel inside the instance.

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical | holds | under the seam decree, which admits the three marked steps |
    | J1 | holds | exact by the depth-1 criterion ([[mult.involution]], Notes); the three receipts are ±2πi — the first ℚ law whose receipts do not vanish |
    | JH, JO | holds | the Inversion cluster plus guarded Involution; the semantic seam guard JH-3 blocks the three marked steps and the route is through the left-inverse theorem |
    | JP | guarded | for units |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | the law is exact on ℂ×; the three seam steps are exact only mod 2πi |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    The three seam steps, in the ℂ reading: (1) `[(<[<A>]>)]` has value −ln a + iπ while `<[<A>]>` has value −ln a − iπ; (2) `[(Z)]` with Z = `[<A>][<(<[A]>)>]` has value 0 while Z has value 2πi; (3) `[X][<A>]` sums to 2πi while `[([X][<A>])]` is 0. Each difference is the period. Tagged *need-led*: nothing in the shape of the forms asks for this law; the sign rules of fractions ([[Q.negative-denominator]]) do, and the shape answers by pointing at the seam.
    """,
)

node(
    id="Q.negative-denominator", title="A sign on the bottom is a sign in front", type="theorem", level="object", kind="law",
    order=624, domain="positive", law="([A] <[<B>]>) ≐ <([A] <[B]>)>", units="a/(−b) = −(a/b)", gloss_check="-A/B",
    holds_over={"JP": "guarded"}, status="NATIVE-BY-DECREE", verified="engine",
    known_since="1993 (James); the sign rule is ancient", guide="shape-led", band="6–8",
    uses=["Q.division", "mult.involution", "Q.reciprocal-of-negative", "mult.inverse-promotion", "mult.seam-decree"], see_also=["Q.negative-fraction", "Q.negatives-cancel"],
    aliases=["a/(−b) = −(a/b)"], concepts=["fraction", "negation"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([A] <[<B>]>) ≐ <([A] <[B]>)>` | — | a/(−b) = −(a/b) |

    ## Plain

    A minus on the bottom of a fraction is the same as a minus in front — but, unlike the minus on top, the page needs the reciprocal of a negative to show it.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `([A] <[<B>]>)` | given | a ÷ (−b), [[Q.division]] |
    | `([A] [(<[<B>]>)])` | [[mult.involution]] | `X ≐ [(X)]` with X = `<[<B>]>`, right to left — a seam step in an absorbing position, admitted by [[mult.seam-decree]] |
    | `([A] [<(<[B]>)>])` | [[Q.reciprocal-of-negative]] | 1/(−b) = −(1/b) |
    | `<([A] [(<[B]>)])>` | [[mult.inverse-promotion]] | `(X [<Y>]) ≐ <(X [Y])>` with X = `[A]`, Y = `(<[B]>)`, used right to left |
    | `<([A] <[B]>)>` | [[mult.involution]] | `[(Y)] ≐ Y` with Y = `<[B]>`, on the strip |

    ## Confirms

    The second sign rule for fractions. Its asymmetry with [[Q.negative-fraction]] is real: a sign on top moves out by inverse promotion alone (NATIVE); a sign on the bottom must first be turned into a sign on a reciprocal, and that crosses the seam (NATIVE-BY-DECREE). With both, [[Q.negatives-cancel]] follows.

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical | holds | under the seam decree |
    | J1 | holds | exact by the depth-1 criterion; inherits the receipts of [[Q.reciprocal-of-negative]] and posts one more at its own seam step |
    | JH, JO | holds | guarded Involution; the route is through the left-inverse theorem |
    | JP | guarded | for units |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | exact on ℂ× |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.negatives-cancel", title="Two signs on a fraction cancel", type="theorem", level="object", kind="law",
    order=626, domain="positive", law="([<A>] <[<B>]>) ≐ ([A] <[B]>)", units="(−a)/(−b) = a/b", gloss_check="A/B",
    holds_over={"JP": "guarded"}, status="NATIVE-BY-DECREE", verified="engine",
    known_since="1993 (James); the sign rule is ancient", guide="shape-led", band="6–8",
    uses=["Q.division", "Q.negative-fraction", "Q.negative-denominator", "Z.cancellation"], see_also=["mult.product-of-negatives"],
    aliases=["(−a)/(−b) = a/b"], concepts=["fraction", "negation"], understood="yes",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([<A>] <[<B>]>) ≐ ([A] <[B]>)` | — | (−a)/(−b) = a/b |

    ## Plain

    A minus on top and a minus on the bottom cancel each other — each moves out front, and two minuses in front are none.

    ## Derivation

    | form | rule | note |
    |---|---|---|
    | `([<A>] <[<B>]>)` | given | (−a) ÷ (−b), [[Q.division]] |
    | `<([A] <[<B>]>)>` | [[Q.negative-fraction]] | the top sign moves out, with B := `<B>` |
    | `<<([A] <[B]>)>>` | [[Q.negative-denominator]] | the bottom sign moves out |
    | `([A] <[B]>)` | [[Z.cancellation]] | two mirrors cancel |

    ## Confirms

    The quotient counterpart of [[mult.product-of-negatives]], and the end of the sign rules: with this, every signed fraction is a fraction or the mirror of one ([[Q.rational]]).

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical | holds | under the seam decree, through [[Q.negative-denominator]] |
    | J1 | holds | exact; no Λ-step of its own, inherits the receipts of [[Q.negative-denominator]] |
    | JH, JO | holds | — |
    | JP | guarded | for units |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | exact on ℂ× |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    —
    """,
)

node(
    id="Q.cross-multiplication", title="Two fractions are equal when their cross products are", type="theorem", level="meta", kind="law",
    order=655, domain="positive", law="([A] <[B]>) ≐ ([C] <[D]>)  iff  ([A] [D]) ≐ ([C] [B])", units="a/b = c/d ⟺ ad = cb",
    holds_over={"JH": "replaced", "JO": "replaced", "JP": "guarded"}, status="NATIVE-BY-DECREE", verified="hand",
    known_since="Euclid VII (proportion); the fact is ancient", guide="need-led", band="3–5",
    uses=["Q.division", "mult.multiplication", "mult.involution", "Z.inversion", "Q.cancel-common-factor", "mult.product-of-numerals", "mult.consistency"], see_also=["Q.lowest-terms", "Z.normal-form", "N.freeness"],
    aliases=["cross-multiply", "proportion", "a/b = c/d iff ad = bc"], concepts=["fraction", "normal-form"], understood="partial",
    body="""
    ## Law

    | form | units | standard |
    |---|---|---|
    | `([A] <[B]>) ≐ ([C] <[D]>)` iff `([A] [D]) ≐ ([C] [B])` | — | a/b = c/d ⟺ ad = cb |

    An *iff* is two implications, and an implication between equations is not itself an equation: this is a meta-level law, stated about the calculus. Each direction is a derivation schema.

    ## Plain

    Two fractions are the same number exactly when top-times-other-bottom matches on both sides — the page can run either direction, but "exactly when" is a sentence about the page, not a form on it.

    ## Derivation

    | statement | rule | note |
    |---|---|---|
    | (⇒) Suppose `([A] <[B]>) ≐ ([C] <[D]>)`. Multiply both sides by `([B] [D])`: on the left, `([([A]<[B]>)] [([B][D])]) ≐ ([A] <[B]> [B] [D]) ≐ ([A] [D])` — two unit steps and one Inversion; on the right, likewise `([C] <[D]> [B] [D]) ≐ ([C] [B])` | [[mult.multiplication]] [[mult.involution]] [[Z.inversion]] | congruence: equals multiplied by equals are equal; the unit steps are on real content |
    | (⇐) Suppose `([A] [D]) ≐ ([C] [B])`. Divide both sides by `([B] [D])`: on the left, `([([A][D])] <[([B][D])]>) ≐ ([A] <[B]>)` by [[Q.cancel-common-factor]] with the common factor D; on the right, the same with the common factor B gives `([C] <[D]>)` | [[Q.division]] | congruence again |
    | On numerals each side of `([A][D]) ≐ ([C][B])` is a pile by [[mult.product-of-numerals]], and two piles are ≐ iff they have the same count — in the full calculus by [[mult.consistency]]; so equality of fractions of numerals is decidable | — | the fact the lowest-terms gap relies on; it inherits consistency's price |

    ## Confirms

    Euclid's criterion for proportion, and the decidability of equality in ℚ. The chart keeps it meta because its content is an *iff*; each direction's instances are engine-checkable, and the object-level laws it leans on are. It is **not** a canonical form: it decides equality without choosing a representative.

    ## Settings and readings

    | setting | holds | why |
    |---|---|---|
    | classical | holds | — |
    | J1 | holds | the two directions use only laws that hold in J1 |
    | JH, JO | replaced | with two quotients there are two criteria |
    | JP | guarded | for unit denominators |

    | reading | cell | why |
    |---|---|---|
    | C | EXACT | — |
    | finset | ABSENT | — |
    | logic | ABSENT | — |
    | lambda, CC | untested | — |

    ## Refuted readings

    none

    ## Notes

    Verification is `hand`: a meta statement with no witness script. The obligation is a script that instantiates both directions on random numerals and runs the engine on each — the shape of every future "iff" node's witness.
    """,
)
