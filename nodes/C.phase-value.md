---
id: C.phase-value
title: The instance of J is minus one
type: theorem
level: object
kind: law
rung: C
order: 910
setting: classical
equality: "≐"
domain: positive
law: "(J) ≐ <o>"
units: "e^{iπ} = −1"
gloss_check: "-1"
holds:
  classical: holds
  J1: holds
  JH: holds
  JO: holds
  JP: holds
readings:
  C: EXACT
  finset: ABSENT
  lambda: untested
  CC: untested
  logic: ABSENT
status: NATIVE
verified: engine
known_since: "1993 (James); Euler 1748"
entered: 2026-10-03
guide: shape-led
band: "9–12"
uses: [C.phase, mult.involution]
see_also: [C.euler-identity, C.phase-rule]
aliases: [phase value, "e^{iπ} = −1"]
concepts: [phase, negation]
understood: "no"
understood_note: "not yet walked — the tracker is Lui's to flip"
reentry: false
---

## Law

| form | units | standard |
|---|---|---|
| `(J) ≐ <o>` | — | e^{iπ} = −1 |

## Plain

Circle the log of minus one and you get minus one back — the famous identity is one counit.

## Derivation

| form | rule | note |
|---|---|---|
| `(J)` | given | [[C.phase]] |
| `([<o>])` | definition | unfold J |
| `<o>` | [[mult.involution]] | the counit `([X]) ≐ X` — never restricted |

## Confirms

e^{iπ} = −1 as the counit at −1: the "most beautiful equation" is, on the page, the statement that circling undoes boxing. It is **not** the other direction: `[(J)] ≐ J` would be the unit on content iπ (on the edge of the strip, admitted), but `[(J J)] ≐ J J` is the refused step.

## Settings and readings

| setting | holds | why |
|---|---|---|
| all | holds | the counit survives in every setting |

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
