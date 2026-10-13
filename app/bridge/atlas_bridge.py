#!/usr/bin/env python3
"""atlas_bridge.py — the Python side of James Atlas.

One long-lived process per open chart. It imports the chart's own tools (tools/nodes.py,
tools/build.py, tools/forms.py, tools/prover.py, tools/licences.py) so that every card the app
shows is the card build.py draws, and every rewrite the live instrument offers is one the
derivation checker would license.

Protocol: one JSON request per line on stdin — {"id": 1, "method": "chart.summary", "params": {}} —
and one JSON reply per line on stdout — {"id": 1, "result": …} or {"id": 1, "error": {…}}.
Anything the chart's tools print goes to stderr, never to the reply stream.

Standard library only, like the chart. Run: python3 atlas_bridge.py --chart <chart folder>
"""
from __future__ import annotations

import argparse
import html
import io
import json
import os
import random
import re
import sys
import tempfile
import time
import traceback

UNDERSTOOD = ("no", "partial", "yes")
NODE_ID = re.compile(r"^[A-Za-z0-9]+\.[A-Za-z0-9-]+$")
MAX_FORM_CHARS = 600          # the live instrument refuses longer forms: AC matching grows fast
MAX_RESULTS = 80              # rewrites shown per application
REWRITE_LIMIT = 400           # rewrites enumerated per rule before stopping


class BridgeError(Exception):
    def __init__(self, message, kind="error", detail=None):
        super().__init__(message)
        self.kind = kind
        self.detail = detail


class Chart:
    """The chart folder, loaded through its own tools."""

    def __init__(self, root: str):
        self.root = os.path.abspath(root)
        tools = os.path.join(self.root, "tools")
        if not os.path.isfile(os.path.join(tools, "build.py")):
            raise BridgeError(f"{self.root} is not a Boundary Chart folder (no tools/build.py)", "no-chart")
        sys.path.insert(0, tools)
        import forms as F          # noqa: E402  (the chart's own modules)
        import nodes as N          # noqa: E402
        import build as B          # noqa: E402
        import prover as P         # noqa: E402
        import licences as L       # noqa: E402
        self.F, self.N, self.B, self.P, self.L = F, N, B, P, L
        self.css = None
        self.load()

    # ------------------------------------------------------------------ loading

    def load(self):
        """Read the chart. Nothing already loaded is replaced unless the whole read succeeds."""
        B, N = self.B, self.N
        nodes_dir = os.path.join(self.root, "nodes")
        try:
            nodes = N.load_nodes(nodes_dir)
        except Exception as e:
            raise BridgeError("the chart's nodes could not be read:\n" + "\n".join(diagnose_nodes(N, nodes_dir) or [str(e)]), "bad-chart")
        concepts = N.load_concepts(os.path.join(self.root, "concepts"))
        B._J1_LEDGER = None          # the ledgers are re-read: a check run may have rewritten them
        B._PLACE_LEDGER = None
        B._H_LEDGER = None
        try:
            used_by, depth, price = B.compute(nodes)
        except Exception as e:
            raise BridgeError(f"the chart's links could not be followed: {e} — run Check to see which law", "bad-chart")
        # an `order:` that is not a whole number sorts first, as check.py does, so the app still opens and Check names it
        ordered = sorted(nodes.values(), key=lambda n: (n.get("order") if isinstance(n.get("order"), int) else 0, n.id))
        self.nodes, self.concepts = nodes, concepts
        self.used_by, self.depth, self.price = used_by, depth, price
        self.ordered = ordered
        self.cards = {}
        self.rule_cache = {}
        self.rule_env = {}       # a schema instance's parameters, by rule
        self.rule_index = None
        self.loaded_at = time.time()

    def node(self, nid: str):
        nid = str(nid or "")
        if not NODE_ID.match(nid) or nid not in self.nodes:
            raise BridgeError(f"no node {nid!r} in this chart", "no-node")
        return self.nodes[nid]

    # ------------------------------------------------------------------ the walk

    def summary(self):
        B = self.B
        rungs, by_rung = [], {}
        for n in self.ordered:
            r = n.get("rung")
            if r not in by_rung:
                by_rung[r] = []
                rungs.append(r)
            by_rung[r].append(n.id)
        und = {k: 0 for k in UNDERSTOOD}
        types, owed = {}, 0
        out_nodes = []
        for i, n in enumerate(self.ordered):
            u = understood_of(n)
            und[u] = und.get(u, 0) + 1
            types[n.get("type")] = types.get(n.get("type"), 0) + 1
            owed += len(n.get("owed") or [])
            out_nodes.append(self.node_summary(n, i))
        return {
            "root": self.root,
            "nodes": out_nodes,
            "rungs": [{"id": r, "title": B.RUNG_TITLES.get(r, r), "nodes": by_rung[r]} for r in rungs],
            "understood": und,
            "types": types,
            "owed": owed,
            "engineVerified": sum(1 for n in self.nodes.values() if n.get("verified") in ("engine", "numeric", "lean")),
            "css": self.site_css(),
            "loadedAt": self.loaded_at,
        }

    def node_summary(self, n, walk=None):
        if walk is None:
            walk = next(i for i, x in enumerate(self.ordered) if x.id == n.id)
        return {
            "id": n.id,
            "walk": walk,
            "title": str(n.get("title", "")),
            "rung": n.get("rung"),
            "order": n.get("order", 0),
            "type": n.get("type"),
            "level": n.get("level"),
            "kind": n.get("kind"),
            "status": n.get("status"),
            "verified": n.get("verified"),
            "setting": n.get("setting"),
            "band": str(n.get("band", "")),
            "law": str(n.get("law", "")),
            "units": str(n.get("units", "")),
            "plain": str(n.sections.get("Plain", "")),
            "understood": understood_of(n),
            "owed": len(n.get("owed") or []),
            "search": " ".join([n.id, str(n.get("title", "")), " ".join(map(str, n.get("aliases") or [])),
                                " ".join(map(str, n.get("concepts") or [])), str(n.get("units", ""))]).lower(),
        }

    def card(self, nid):
        n = self.node(nid)
        if nid not in self.cards:
            self._classical()
            self.cards[nid] = self.B.render_node(n, self.nodes, self.used_by, self.depth, self.price)
        return {"id": nid, "html": self.cards[nid], "path": n.path, "understood": understood_of(n)}

    def _classical(self):
        """check.set_reading() moves the evaluator to 𝕁₁ or a place; cards and the instrument read in ℂ."""
        self.F.OMEGA = None
        chk = getattr(self.B, "CHK", None)
        if chk is not None and hasattr(chk, "PLACE_READING"):
            chk.PLACE_READING = None

    def graph(self):
        return {"html": self.B.render_dag(self.nodes, self.depth)}

    def lists(self):
        B, md, inline = self.B, self.B.md, self.B.inline
        nodes = self.nodes
        gaps = [n for n in self.ordered if n.get("type") == "gap"]
        gap_html = "".join(
            f'<div class="gapitem"><a class="nl" href="#{n.id}">{n.id}</a> <b>{html.escape(str(n.get("title")))}</b> — {inline(str(n.get("law")), nodes)}</div>'
            for n in gaps)
        owed_html = "".join(
            f'<div class="gapitem"><a class="nl" href="#{n.id}">{n.id}</a> {inline(str(x), nodes)}</div>'
            for n in self.ordered for x in (n.get("owed") or []))
        refuted = [(n, n.sections.get("Refuted readings", "")) for n in self.ordered
                   if not n.sections.get("Refuted readings", "none").strip().lower().startswith("none")]
        ref_html = "".join(f'<div class="refitem"><a class="nl" href="#{n.id}">{n.id}</a>{md(txt, nodes)}</div>' for n, txt in refuted)
        open_forms = ""
        ofp = os.path.join(self.root, "census", "open-forms.md")
        if os.path.exists(ofp):
            with open(ofp, encoding="utf-8") as fh:
                open_forms = md(fh.read().split("\n", 3)[-1], nodes)
        return {
            "gaps": gap_html, "gapCount": len(gaps),
            "owed": owed_html, "owedCount": sum(len(n.get("owed") or []) for n in self.ordered),
            "refuted": ref_html, "refutedCount": len(refuted),
            "concepts": B.render_concepts(nodes, self.concepts),
            "openForms": open_forms,
        }

    def site_css(self):
        """The chart page's own stylesheet, so a card looks the same in the app as on the site."""
        if self.css is None:
            page = None
            site = os.path.join(self.root, "site", "index.html")
            if os.path.exists(site):
                with open(site, encoding="utf-8") as fh:
                    page = fh.read()
            else:
                page = self._render_page()
            m = re.search(r"<style>(.*?)</style>", page or "", re.S)
            self.css = m.group(1) if m else ""
        return self.css

    def _render_page(self):
        """No site/index.html yet: render the page into a temporary file, leaving site/ alone."""
        B = self.B
        fd, tmp = tempfile.mkstemp(suffix=".html")
        os.close(fd)
        old = B.OUT
        try:
            B.OUT = tmp
            B.main()
            with open(tmp, encoding="utf-8") as fh:
                return fh.read()
        except Exception:
            traceback.print_exc(file=sys.stderr)
            return ""
        finally:
            B.OUT = old
            try:
                os.remove(tmp)
            except OSError:
                pass

    # ------------------------------------------------------------------ the tracker

    def set_understood(self, nid, value):
        value = str(value or "").strip().lower()
        if value not in UNDERSTOOD:
            raise BridgeError(f"understood must be one of {', '.join(UNDERSTOOD)}", "bad-value")
        n = self.node(nid)
        write_understood(n.path, value)
        self.load()
        n = self.nodes[nid]
        und = {k: 0 for k in UNDERSTOOD}
        for x in self.nodes.values():
            und[understood_of(x)] += 1
        return {"node": self.node_summary(n), "card": self.card(nid), "understood": und}

    # ------------------------------------------------------------------ the live instrument

    def node_rules(self, n):
        """The rewrite rules a node offers, each with a label naming its instance (a schema's parameter,
        a family's shape) — the rules licences.rules_for gives the derivation checker."""
        F, P, L = self.F, self.P, self.L
        rules = list(L.rules_for(n.id, self.nodes, self.rule_cache))
        if n.get("schema_range"):
            import schema as S   # the chart's own module
            tl, tr, _sym = F.split_law(str(n.get("law", "")))
            labelled = []
            try:
                for env in S.parse_range(n.get("schema_range", "")):
                    r = P.Rule(n.id, F.parse(S.expand(tl, env)), F.parse(S.expand(tr, env)), label=S.describe(env))
                    labelled.append(r)
                    self.rule_env[r] = dict(env)
            except Exception:
                labelled = []
            if labelled:
                keys = {(r.lhs, r.rhs) for r in labelled}
                rules = labelled + [r for r in rules if (r.lhs, r.rhs) not in keys]
        if n.id in ("void.page", "void.space"):
            return []     # the medium: built into the representation (juxtaposition is a multiset with void as unit)
        return rules

    def rules_index(self):
        """Every node, in walk order, with whether the instrument can apply its law."""
        if self.rule_index is None:
            out = []
            for n in self.ordered:
                law = str(n.get("law", ""))
                try:
                    rules = self.node_rules(n)
                except Exception:
                    rules = []
                units = str(n.get("units", ""))
                why = ""
                if not rules:
                    why = ("the medium: juxtaposition is already a multiset with the void as its unit"
                           if n.id in ("void.page", "void.space") else _why_not_rule(law))
                out.append({
                    "id": n.id,
                    "title": str(n.get("title", "")),
                    "rung": n.get("rung"),
                    "type": n.get("type"),
                    "setting": n.get("setting"),
                    "domain": n.get("domain"),
                    "law": law,
                    "units": units,
                    "rules": len(rules),
                    "usable": bool(rules),
                    "conditional": units.startswith("PREMISE"),
                    "schema": bool(n.get("schema_range")),
                    "reading": default_reading(n, self.instance(n)[0]),
                    "why": why,
                })
            self.rule_index = out
        return self.rule_index

    def instance(self, n):
        """For a law written over n (and the place p): the instance its card draws (build.draw_env), when that is in
        the law's range, or else the first in range — as (env, lhs, rhs) with both sides parseable; (None, None, None)
        for an ordinary law or one that will not expand."""
        if not n.get("schema_range"):
            return None, None, None
        import schema as S   # the chart's own module
        F = self.F
        law = str(n.get("law", ""))
        try:
            envs = S.parse_range(n.get("schema_range", ""))
        except Exception:
            envs = []
        drawn = self.B.draw_env(n)
        first = [e for e in envs if all(drawn.get(k) == v for k, v in e.items())]
        for env in first + envs:
            try:
                lhs, rhs, _sym = F.split_law(S.expand(law, env))
                if rhs is None:
                    continue
                F.parse(lhs)
                F.parse(rhs)
                return dict(env), lhs, rhs
            except Exception:
                continue
        return None, None, None

    def law(self, nid):
        n = self.node(nid)
        self._classical()
        lhs, rhs, sym = self.F.split_law(str(n.get("law", "")))
        env, ilhs, irhs = self.instance(n)
        if env is not None:     # a template (A^{n}, o^{p**n}, Σ{…}) is not a form: start from the instance the card draws
            lhs, rhs = ilhs, irhs
        rules = self.node_rules(n)
        one_way = [r.label or f"{self.F.to_string(r.lhs, True) or 'void'} {sym or '≐'} {self.F.to_string(r.rhs, True) or 'void'}"
                   for r in rules if len(r.oriented()) == 1]
        return {"id": n.id, "title": str(n.get("title", "")), "html": self.B.law_block(n, self.nodes),
                "lhs": lhs if rhs is not None else None, "rhs": rhs, "symbol": sym,
                "units": str(n.get("units", "")), "conditional": str(n.get("units", "")).startswith("PREMISE"),
                "setting": n.get("setting"), "domain": n.get("domain"), "reading": default_reading(n, env),
                "instance": self._describe(env),
                "rules": len(rules), "oneWay": bool(one_way) and len(one_way) == len(rules),
                "instances": [r.label for r in rules if r.label][:40] if len(rules) > 1 else []}

    def _describe(self, env):
        if not env:
            return ""
        import schema as S
        try:
            return S.describe(env)
        except Exception:
            return ", ".join(f"{k} = {v}" for k, v in env.items())

    def inspect(self, text, seed=0, reading="C", domain="positive"):
        F = self.F
        form = self._parse(text)
        canonical = F.to_string(form)
        names = sorted(F.variables(form))
        with Reading(self, reading, form) as R:
            env, note = R.env(names, domain, seed)
            value, _raw = R.value(form, env)
            return {
                "ok": True,
                "canonical": canonical,
                "sugar": F.to_string(form, True),
                "svg": self._draw(canonical, "form big"),
                "size": F.size(form),
                "depth": F.depth(form),
                "variables": names,
                "value": value,
                "valueNote": note,
                "reading": R.name,
                "readingLabel": R.label,
            }

    def apply(self, rule_id, text, seed=0, reading=None, domain=None):
        F, P = self.F, self.P
        n = self.node(rule_id)
        form = self._parse(text)
        rules = self.node_rules(n)
        if not rules:
            raise BridgeError(f"{n.id} has no law the instrument can apply: {_why_not_rule(str(n.get('law', '')))}", "no-rule")
        rname = reading or default_reading(n, self.instance(n)[0])
        place_pick = int(rname[1:]) if rname.startswith("p") else None
        if place_pick is not None:
            # read at one place: only the instances written for that place license a step there
            rules = [r for r in rules if self.rule_env.get(r, {}).get("p", place_pick) == place_pick]
            if not rules:
                raise BridgeError(f"{n.id} has no instance at the place {place_pick}: choose another place", "no-rule")
        risky = [r for r in rules if match_cost(r, form, F) > MATCH_BUDGET]
        if risky and len(risky) == len(rules):
            raise BridgeError(
                f"{n.id}'s pattern would have to try more than {MATCH_BUDGET:,} ways of splitting this form's pieces among its "
                f"variables — try it on a smaller form (fewer pieces side by side at one level)", "too-big")
        started = time.time()
        seen, results = set(), []
        truncated = False
        for rule in rules:
            if rule in risky:
                truncated = True
                continue
            found = P.rewrite_all(form, rule, REWRITE_LIMIT)
            if len(found) >= REWRITE_LIMIT:
                truncated = True
            for new, step in found:
                if not step.redex or new == form:     # an empty match, or a step that changes nothing
                    continue
                key = F.to_string(new)
                if key in seen:
                    continue
                seen.add(key)
                results.append((new, step, rule))
            if time.time() - started > 15:
                truncated = True
                break
        results.sort(key=lambda t: (t[1].direction != "→", F.size(t[0]), F.to_string(t[0])))
        shown = results[:MAX_RESULTS]
        sym = F.split_law(str(n.get("law", "")))[2] or "≐"
        dom = domain or n.get("domain") or "positive"
        names = sorted(F.variables(form) | {v for new, _s, _r in shown for v in F.variables(new)})
        rng = random.Random(4242 + int(seed or 0))
        readings = {}      # one reading, sample and starting value per (place, depth) the instances name

        def reading_for(rule):
            env = self.rule_env.get(rule, {})
            key = (rname, env.get("p"), env.get("n")) if "p" in env else (rname, None, None)
            if key not in readings:
                if key[1] is not None:
                    R = Reading(self, f"p{key[1]}", form, depth=key[2])
                else:
                    R = Reading(self, rname, form)
                with R:
                    sample, note = R.env(names, dom, seed)
                    before, before_raw = R.value(form, sample)
                readings[key] = (R, sample, note, before, before_raw)
            return readings[key]

        out = []
        for new, step, rule in shown:
            R, sample, _note, _before, before_raw = reading_for(rule)
            with R:
                canonical = F.to_string(new)
                value, raw = R.value(new, sample)
                kept = R.same(before_raw, raw, sym)
                premise = None
                if n.id in self.J.CONDITIONAL:
                    try:
                        premise = bool(self.J.premise_holds(step, n, rng, self.CHK.H_READING))
                    except Exception:
                        premise = None
            out.append({
                "canonical": canonical,
                "sugar": F.to_string(new, True),
                "svg": self._draw(canonical, "form"),
                "direction": step.direction,
                "where": _path_words(step.path, F),
                "redex": F.to_string(step.redex, True) or "void",
                "into": F.to_string(step.result, True) or "void",
                "env": {k: (F.to_string(v, True) or "void") for k, v in step.env},
                "instance": rule.label if len(rules) > 1 else "",
                "value": value,
                "readingLabel": R.label if R.name != rname or R.depth else "",
                "kept": kept,
                "premise": premise,
            })
        R0, _s0, note0, before0, _b0 = reading_for(shown[0][2]) if shown else (Reading(self, rname, form), None, "", "", None)
        if not shown:
            with R0:
                sample, note0 = R0.env(sorted(F.variables(form)), dom, seed)
                before0, _ = R0.value(form, sample)
        return {
            "rule": n.id,
            "law": str(n.get("law", "")),
            "symbol": sym,
            "conditional": n.id in self.J.CONDITIONAL,
            "units": str(n.get("units", "")),
            "from": F.to_string(form),
            "value": before0,
            "valueNote": note0,
            "reading": R0.name,
            "readingLabel": R0.label,
            "results": out,
            "distinct": len(results),
            "shown": len(out),
            "truncated": truncated,
            "seconds": round(time.time() - started, 3),
        }

    def _draw(self, canonical, cls):
        return self.B.draw_form(canonical, cls) if canonical else '<span class="void" title="the void">void</span>'

    def _parse(self, text):
        F = self.F
        text = str(text if text is not None else "")
        if len(text) > MAX_FORM_CHARS:
            raise BridgeError(f"that form is {len(text)} characters long; the instrument takes up to {MAX_FORM_CHARS}", "too-long")
        try:
            return F.parse(text)
        except Exception as e:
            raise BridgeError(f"not a form: {e}", "parse")

    @property
    def J(self):
        import j1   # the chart's receipt prover: the conditional rules and their premises
        return j1

    @property
    def CHK(self):
        return self.B.CHK


READINGS = {
    "C": "ℂ — the classical reading",
    "J1": "𝕁₁ — ℂ with ω = [()] read as 2πi",
    "H": "ℍ — the quaternions",
    "p2": "the place 2", "p3": "the place 3", "p5": "the place 5", "p7": "the place 7", "p13": "the place 13",
}


def default_reading(n, env=None) -> str:
    """The reading a law is read in by the engine (check.set_reading): its setting's, and for a law written over the
    place p, the place of the instance it starts from."""
    setting = n.get("setting")
    if setting == "J1":
        return "J1"
    if setting == "JH":
        return "H"
    if setting == "JP":
        p = (env or {}).get("p", n.get("place"))
        if p is not None and f"p{p}" in READINGS:
            return f"p{p}"
    return "C"


class Reading:
    """A reading to value forms in — the engine's own (forms.py's ℂ, 𝕁₁'s ℂ, quat.py's ℍ, place.py's pages) —
    set for the duration of a `with` block and reset to ℂ afterwards, as check.set_reading does per node."""

    def __init__(self, chart, name, form=None, depth=None):
        self.chart = chart
        self.depth = depth
        F = chart.F
        name = name if name in READINGS else "C"
        if name == "C" and form is not None and (F.constants(form) or _has_ordered(form, F)):
            name = "H"     # Jj and the ordered square have values only in ℍ
        self.name, self.label = name, READINGS[name] + (f", to depth {depth}" if depth else "")
        self.R = None

    def __enter__(self):
        ch = self.chart
        ch._classical()
        if self.name == "J1":
            import math
            ch.F.OMEGA = 2j * math.pi
        elif self.name == "H":
            self.R = ch.CHK.H_READING
        elif self.name.startswith("p"):
            import place as PL
            self.R = PL.Reading(PL.Place(int(self.name[1:]), depth=int(self.depth) if self.depth else None))
        return self

    def __exit__(self, *exc):
        self.chart._classical()
        return False

    def env(self, names, domain, seed):
        F = self.chart.F
        if not names:
            return {}, ""
        rng = random.Random(1000 + int(seed or 0))
        domain = domain if domain in self.chart.N.DOMAINS else "positive"
        try:
            env = self.R.random_env(names, domain, rng) if self.R else F.random_env(names, domain, rng)
        except Exception:
            env = F.random_env(names, "positive", rng) if not self.R else {}
        return env, "at " + ", ".join(f"{k} = {self.fmt(v)}" for k, v in sorted(env.items()))

    def fmt(self, v):
        try:
            if self.R:
                return self.R.fmt(v)
            if isinstance(v, complex):
                big = max(1.0, abs(v))
                v = complex(0.0 if abs(v.real) < 1e-12 * big else v.real, 0.0 if abs(v.imag) < 1e-12 * big else v.imag)
            return self.chart.F.fmt(v)
        except Exception:
            return str(v)

    def value(self, form, env):
        """(text, raw value or None)."""
        try:
            v = self.R.evaluate(form, env) if self.R else self.chart.F.evaluate(form, env)
        except Exception as e:
            return f"no value — {str(e) or type(e).__name__}", None
        return self.fmt(v), v

    def same(self, a, b, sym):
        if a is None or b is None:
            return None
        try:
            return bool(self.R.equal(a, b, sym) if self.R else self.chart.F.equal(a, b, sym))
        except Exception:
            return None


MATCH_BUDGET = 300_000


def _has_ordered(form, F) -> bool:
    for ch in form:
        if F.is_leaf(ch):
            continue
        if ch[0] == F.ORDERED:
            return True
        if _has_ordered(ch[1], F):
            return True
    return False


def _widest(form, F) -> int:
    """The most pieces side by side at any one level of the form (an ordered square's entries counted apart)."""
    best = len(form)
    for ch in form:
        if F.is_leaf(ch):
            continue
        subs = ch[1] if ch[0] == F.ORDERED else (ch[1],)
        for sub in subs:
            best = max(best, _widest(sub, F))
    return best


def _free_names(pattern, F, top=True):
    """The largest number of distinct variables side by side at one level of a pattern (plus the context the
    rewriter adds at the level it matches at): `A A` splits a multiset two ways, not three."""
    here = len({ch[1] for ch in pattern if ch[0] == F.VAR}) + (1 if top else 0)
    best = here
    for ch in pattern:
        if F.is_leaf(ch):
            continue
        subs = ch[1] if ch[0] == F.ORDERED else (ch[1],)
        for sub in subs:
            best = max(best, _free_names(sub, F, top=False))
    return best


def match_cost(rule, form, F) -> int:
    """How many splits the matcher may build before its first answer: with k free names at a level and m pieces
    there, it materializes k^m candidates (prover._match_vars), capped at 14 pieces where it stops splitting."""
    m = min(_widest(form, F), 14)
    worst = 0
    for _d, frm, _to in rule.oriented():
        k = _free_names(frm, F)
        if k >= 2:
            worst = max(worst, k ** m)
    return worst


# ----------------------------------------------------------------------------- helpers

def understood_of(n) -> str:
    u = str(n.get("understood", "no")).strip().lower()
    return u if u in UNDERSTOOD else "no"


_FM_LINE = re.compile(r"^understood:[^\r\n]*", re.M)


def write_understood(path: str, value: str):
    """Rewrite the one `understood:` line of a node's front matter in place — nothing else in the
    file changes, line endings included — and replace the file atomically."""
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8")
    if not text.startswith("---"):
        raise BridgeError(f"{os.path.basename(path)} has no front matter", "bad-file")
    end = text.find("\n---", 3)
    if end < 0:
        raise BridgeError(f"{os.path.basename(path)} has unterminated front matter", "bad-file")
    fm, rest = text[:end], text[end:]
    m = _FM_LINE.search(fm)
    if m:
        # keep the line's own style: Lui writes `understood: yes` by hand, the chart's files `understood: "no"`
        old = m.group(0)[len("understood:"):].strip()
        quoted = old[:1] in ("'", '"')
        q = old[0] if quoted else ""
        fm = fm[:m.start()] + f"understood: {q}{value}{q}" + fm[m.end():]
    else:
        eol = "\r\n" if "\r\n" in fm else "\n"
        fm = fm.rstrip("\r\n") + eol + f'understood: "{value}"' + ("\r" if eol == "\r\n" else "")
    data = (fm + rest).encode("utf-8")
    if data == raw:
        return
    d = os.path.dirname(path)
    fd, tmp = tempfile.mkstemp(prefix=".understood-", dir=d)
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
        try:
            os.chmod(tmp, os.stat(path).st_mode & 0o777)
        except OSError:
            pass
        os.replace(tmp, path)
    except Exception:
        try:
            os.remove(tmp)
        except OSError:
            pass
        raise


def diagnose_nodes(N, nodes_dir):
    """Which node files the chart's loader cannot read, and why — one line each."""
    problems = []
    for fn in sorted(os.listdir(nodes_dir)):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(nodes_dir, fn)
        try:
            with open(path, "rb") as fh:
                raw = fh.read()
            if raw.startswith(b"\xef\xbb\xbf"):
                problems.append(f"{fn}: starts with a byte-order mark — save it as UTF-8 without BOM")
                continue
            N.parse_front_matter(raw.decode("utf-8"))
        except UnicodeDecodeError:
            problems.append(f"{fn}: not UTF-8 text")
        except Exception as e:
            problems.append(f"{fn}: {e}")
    return problems


def _why_not_rule(law: str) -> str:
    for prefix, why in (("GAP", "a gap names what cannot be written yet"), ("DISCIPLINE", "a discipline, not an equation"),
                        ("DECLARATION", "a declaration, not an equation"), ("IMPORT", "an import, stated in prose")):
        if law.startswith(prefix):
            return why
    if ":=" in law:
        return "a definition: it names a form rather than rewriting one"
    if not any(s in law for s in ("≐", "≡", "≃")):
        return "not an equation between forms"
    return "its sides are not forms the parser reads"


def _path_words(path, F):
    names = {F.ROUND: "instance ( )", F.SQUARE: "square [ ]", F.ANGLE: "angle < >", F.ORDERED: "ordered square [ ; ]"}
    if not path:
        return "on the page"
    return " › ".join(names.get(k, str(k)) for k in path)


# ----------------------------------------------------------------------------- the loop

def handle(chart: Chart, method: str, params: dict):
    if method == "ping":
        return {"ok": True, "root": chart.root}
    if method == "chart.summary":
        return chart.summary()
    if method == "chart.card":
        return chart.card(params.get("id"))
    if method == "chart.graph":
        return chart.graph()
    if method == "chart.lists":
        return chart.lists()
    if method == "chart.reload":
        chart.css = None
        chart.load()
        return chart.summary()
    if method == "chart.setUnderstood":
        return chart.set_understood(params.get("id"), params.get("value"))
    if method == "instrument.rules":
        return {"rules": chart.rules_index()}
    if method == "instrument.law":
        return chart.law(params.get("id"))
    if method == "instrument.inspect":
        return chart.inspect(params.get("form", ""), params.get("seed", 0), params.get("reading", "C"), params.get("domain", "positive"))
    if method == "instrument.apply":
        return chart.apply(params.get("rule"), params.get("form", ""), params.get("seed", 0), params.get("reading"), params.get("domain"))
    raise BridgeError(f"unknown method {method!r}", "unknown")


def serve(chart_root: str, inp=None, out=None):
    inp = inp or io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")
    out = out or io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n", write_through=True)
    sys.stdout = sys.stderr   # whatever the chart's tools print must not reach the reply stream

    def reply(obj):
        out.write(json.dumps(obj, ensure_ascii=True) + "\n")
        out.flush()

    chart, load_error = None, None
    try:
        chart = Chart(chart_root)
    except Exception as e:
        load_error = e
        traceback.print_exc(file=sys.stderr)

    for line in inp:
        line = line.strip()
        if not line:
            continue
        rid = None
        try:
            try:
                req = json.loads(line)
            except ValueError:
                raise BridgeError("a request that is not JSON", "bad-request")
            if not isinstance(req, dict):
                raise BridgeError("a request must be a JSON object", "bad-request")
            rid = req.get("id")
            if chart is None:
                raise BridgeError(f"the chart could not be loaded: {load_error}", "no-chart")
            result = handle(chart, str(req.get("method", "")), req.get("params") or {})
            reply({"id": rid, "result": result})
        except BridgeError as e:
            reply({"id": rid, "error": {"message": str(e), "kind": e.kind, "detail": e.detail}})
        except Exception as e:
            traceback.print_exc(file=sys.stderr)
            reply({"id": rid, "error": {"message": f"{type(e).__name__}: {e}", "kind": "internal"}})


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--chart", required=True, help="the Boundary Chart folder (holds nodes/ and tools/)")
    args = ap.parse_args(argv)
    serve(args.chart)


if __name__ == "__main__":
    main()
