#!/usr/bin/env python3
"""build.py — nodes/*.md → site/index.html (SPEC §12–13).

Renders every law with its forms drawn as nested boundaries, the chart as a clickable
layered DAG, computed price and used-by, the walk with its progress, the concept index,
the gap list with plans, the refuted list, and the small-form census.
No dependencies beyond Python 3.  Run: python3 tools/build.py
"""
from __future__ import annotations
import html
import os
import re
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import forms as F
import check as CHK  # noqa: E402
import schema as SCH  # noqa: E402
import nodes as N  # noqa: E402
import census as C  # noqa: E402

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "site", "index.html")

BASE_IDS = {"void.page", "void.space", "N.round", "Z.angle", "mult.square", "mult.involution", "mult.distribution", "Z.inversion", "J1.counit"}
PRICED_TYPES = {"primitive", "axiom", "decree", "import", "gap"}
RUNG_TITLES = {
    "void": "The page", "N": "ℕ — piles", "Z": "ℤ — the angle boundary", "mult": "× — the square boundary",
    "Q": "ℚ — division and fractional counts", "alg": "Radicals and the base", "C": "ℂ and J", "schema": "Schemas — one law for every n", "J1": "𝕁₁ — the receipt", "H": "ℍ — the ordered square", "O": "𝕆 (JO)", "S": "𝕊 (JS)", "J2": "𝕁₂ — the moduli of lattices",
    "analysis": "Analysis", "place": "Places — the same wall at p", "logic": "Logic", "struct": "Structure", "F1": "F₁", "field": "The Field",
}

# ----------------------------------------------------------------------------- form drawing

H0, PAD, GAP, FS = 16.0, 5.0, 5.0, 12.0


def _layout(form):
    if not form:
        return {"w": 0.0, "h": H0, "kids": []}
    kids = [_layout_child(ch) for ch in form]
    w = sum(k["w"] for k in kids) + GAP * (len(kids) - 1)
    h = max(k["h"] for k in kids)
    return {"w": w, "h": h, "kids": kids}


SEP = 9.0   # the gap either side of the divider between the entries of an ordered square


def _layout_child(ch):
    if ch[0] == F.VAR:
        return {"kind": "v", "name": ch[1], "w": FS * 0.75 * len(ch[1]) + 2, "h": FS + 2}
    if ch[0] == F.CONST:
        name = F.CONSTANTS.get(ch[1], ch[1])
        return {"kind": "v", "name": name, "w": FS * 0.75 * len(name) + 2, "h": FS + 2, "const": True}
    if ch[0] == F.ORDERED:
        ents = [_layout(e) for e in ch[1]]
        for e in ents:
            if e["w"] == 0:
                e["w"] = H0 * 0.6   # an empty entry still takes a slot
        w = sum(e["w"] for e in ents) + SEP * (len(ents) - 1) + 2 * PAD
        h = max(e["h"] for e in ents) + 2 * PAD
        return {"kind": F.ORDERED, "entries": ents, "w": w, "h": h, "inner": {"w": w}}
    inner = _layout(ch[1])
    if inner["w"] == 0:
        w = h = H0
        if ch[0] == F.ANGLE:
            w = H0 * 1.25
    else:
        h = inner["h"] + 2 * PAD
        w = inner["w"] + 2 * PAD
        if ch[0] == F.ANGLE:
            w += 2 * (h / 3.0)
    return {"kind": ch[0], "inner": inner, "w": w, "h": h}


def _draw(lay, x, y, out):
    cx = x
    for k in lay["kids"]:
        ky = y + (lay["h"] - k["h"]) / 2
        _draw_child(k, cx, ky, out)
        cx += k["w"] + GAP


def _draw_child(k, x, y, out):
    w, h = k["w"], k["h"]
    if k["kind"] == "v":
        cls = "fv fc" if k.get("const") else "fv"
        out.append(f'<text class="{cls}" x="{x + w/2:.1f}" y="{y + h/2 + FS*0.36:.1f}" text-anchor="middle">{html.escape(k["name"])}</text>')
        return
    if k["kind"] == F.ORDERED:
        # an ordered square: a rectangle whose entries are separated by thin dividers (the semicolons)
        out.append(f'<rect class="b-s b-q" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}"/>')
        cx = x + PAD
        for n, e in enumerate(k["entries"]):
            if n:
                sx = cx - SEP / 2
                out.append(f'<line class="b-sep" x1="{sx:.1f}" y1="{y + 2:.1f}" x2="{sx:.1f}" y2="{y + h - 2:.1f}"/>')
            if e["kids"]:
                _draw(e, cx, y + PAD + (h - 2 * PAD - e["h"]) / 2, out)
            cx += e["w"] + SEP
        return
    if k["kind"] == F.ROUND:
        out.append(f'<rect class="b-r" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{h/2:.1f}" ry="{h/2:.1f}"/>')
        ix = x + PAD
    elif k["kind"] == F.SQUARE:
        out.append(f'<rect class="b-s" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}"/>')
        ix = x + PAD
    else:
        d = h / 3.0 if k["inner"]["w"] else w / 2.5
        pts = f"{x:.1f},{y + h/2:.1f} {x + d:.1f},{y:.1f} {x + w - d:.1f},{y:.1f} {x + w:.1f},{y + h/2:.1f} {x + w - d:.1f},{y + h:.1f} {x + d:.1f},{y + h:.1f}"
        out.append(f'<polygon class="b-a" points="{pts}"/>')
        ix = x + d + PAD
    if k["inner"]["w"]:
        _draw(k["inner"], ix, y + PAD, out)


def draw_form(s: str, cls: str = "form") -> str:
    """SVG for a canonical string; falls back to text for standard-notation names."""
    try:
        form = F.parse(s)
    except Exception:
        return f'<span class="name">{html.escape(s)}</span>'
    lay = _layout(form)
    if lay["w"] == 0:
        return '<span class="void" title="the void">void</span>'
    out = []
    _draw(lay, 1.5, 1.5, out)
    w, h = lay["w"] + 3, lay["h"] + 3
    return (f'<svg class="{cls}" width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.1f} {h:.1f}" '
            f'role="img" aria-label="{html.escape(F.to_string(form, True))}">{"".join(out)}</svg>')


# ----------------------------------------------------------------------------- markdown (small subset)

def link_title(nodes, nid):
    return nodes[nid].get("title", nid) if nid in nodes else nid


def inline(text: str, nodes) -> str:
    codes = []

    def stash(m):
        codes.append(m.group(1))
        return f"\x00{len(codes)-1}\x00"

    t = re.sub(r"`([^`]*)`", stash, text)
    t = html.escape(t, quote=False)
    t = re.sub(r"\[\[([A-Za-z0-9]+\.[A-Za-z0-9-]+)\]\]", lambda m: f'<a class="nl" href="#{m.group(1)}" title="{html.escape(link_title(nodes, m.group(1)))}">{m.group(1)}</a>', t)
    t = re.sub(r"~~(.+?)~~", r"<s>\1</s>", t)
    t = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{html.escape(codes[int(m.group(1))])}</code>", t)
    return t


def md(text: str, nodes, draw_first_col=False) -> str:
    out, para, table, ul = [], [], [], []

    def flush_para():
        if para:
            out.append(f"<p>{inline(' '.join(para), nodes)}</p>")
            para.clear()

    def flush_ul():
        if ul:
            out.append("<ul>" + "".join(f"<li>{inline(x, nodes)}</li>" for x in ul) + "</ul>")
            ul.clear()

    def flush_table():
        if not table:
            return
        rows = [r for r in table if not all(re.fullmatch(r":?-{2,}:?", c) for c in r)]
        if not rows:
            table.clear()
            return
        head, body = rows[0], rows[1:]
        h = "".join(f"<th>{inline(c, nodes)}</th>" for c in head)
        draw_here = draw_first_col and bool(head) and head[0].strip().lower() == "form"  # statement tables are prose
        b = []
        for r in body:
            cells = []
            for i, c in enumerate(r):
                if draw_here and i == 0:
                    raw = c.strip().strip("`").strip()
                    cells.append(f'<td class="fcell"><div class="draw">{draw_form(raw, "form sm")}</div><code>{html.escape(raw)}</code></td>')
                else:
                    cells.append(f"<td>{inline(c, nodes)}</td>")
            b.append("<tr>" + "".join(cells) + "</tr>")
        # a derivation table keeps its rule and note columns on screen however wide a drawn form is: fixed layout,
        # the drawing scrolls inside its own cell at legible size, the code string wraps
        colgroup = '<colgroup><col class="c-form"><col class="c-rule"><col class="c-note"></colgroup>' if draw_here and len(head) >= 3 else ""
        cls = ' class="deriv"' if draw_here else ""
        out.append(f'<div class="tw"><table{cls}>{colgroup}<thead><tr>{h}</tr></thead><tbody>{"".join(b)}</tbody></table></div>')
        table.clear()

    for line in text.split("\n"):
        s = line.rstrip()
        if s.strip().startswith("|"):
            flush_para(); flush_ul()
            table.append([c.strip() for c in s.strip().strip("|").split("|")])
            continue
        flush_table()
        if s.strip().startswith("- "):
            flush_para()
            ul.append(s.strip()[2:])
            continue
        flush_ul()
        if not s.strip():
            flush_para()
            continue
        para.append(s.strip())
    flush_para(); flush_ul(); flush_table()
    return "\n".join(out)


# ----------------------------------------------------------------------------- graph computations

def compute(nodes):
    used_by = {nid: [] for nid in nodes}
    for n in nodes.values():
        for u in n.get("uses", []) or []:
            if u in used_by:
                used_by[u].append(n.id)
    depth, price = {}, {}

    def dep(nid, seen=()):
        if nid in depth:
            return depth[nid]
        if nid in seen:
            return 0
        us = [u for u in (nodes[nid].get("uses", []) or []) if u in nodes]
        d = 0 if not us else 1 + max(dep(u, seen + (nid,)) for u in us)
        depth[nid] = d
        return d

    def anc(nid, seen=()):
        if nid in price:
            return price[nid]
        acc = set()
        for g in nodes[nid].get("guarded_by", []) or []:
            if g in nodes:
                acc.add(g)
        for u in nodes[nid].get("uses", []) or []:
            if u in nodes and u not in seen:
                if nodes[u].get("type") in PRICED_TYPES:
                    acc.add(u)
                acc |= anc(u, seen + (nid,))
        price[nid] = acc
        return acc

    for nid in nodes:
        dep(nid); anc(nid)
    # the price of a 𝕁₁ law is stated in 𝕁₁'s own axioms (SPEC §4.3): Involution is the split pair — the counit, and
    # the unit when the tape has a receipt — and the seam decree is not in force there (replaced by receipts)
    ledger = j1_ledger()
    pledger = place_ledger()
    for nid, n in nodes.items():
        if n.get("setting") not in ("J1", "JP"):
            continue
        p = set(price[nid])
        if "mult.involution" in p:
            p.discard("mult.involution")
            p.add("J1.counit")
            tape = ledger.get(nid, ("", ""))[1] if n.get("setting") == "J1" else pledger.get("rung", {}).get(nid, ("", "", ""))[2]
            if any(w in tape for w in ("absorbed", "posted", "import", "pole")):
                p.add("J1.unit")  # the tape took a unit step (with a receipt, or on the pole): the unit is in the price
        p.discard("mult.seam-decree")
        price[nid] = p
    return used_by, depth, price


# ----------------------------------------------------------------------------- rendering

def badge(cls, text, title=""):
    return f'<span class="bd {cls}" title="{html.escape(title)}">{html.escape(str(text))}</span>'


def chips(d: dict, kind: str) -> str:
    if not d:
        return ""
    cells = []
    for k, v in d.items():
        cells.append(f'<span class="chip c-{kind}-{re.sub(r"[^a-zA-Z]", "", str(v)).lower()}" title="{html.escape(k)}: {html.escape(str(v))}"><b>{html.escape(k)}</b> {html.escape(str(v))}</span>')
    return "".join(cells)


def draw_env(node):
    spec = str(node.get("schema_draw", "n=3; k=1"))
    env = {}
    for c in spec.split(";"):
        if "=" in c:
            k, v = c.split("=", 1)
            env[k.strip()] = int(v.strip())
    return env


_J1_LEDGER = None


def j1_ledger():
    """census/j1-ledger.md as {node id: (computed cell, tape text)} — written by check.py."""
    global _J1_LEDGER
    if _J1_LEDGER is None:
        _J1_LEDGER = {}
        path = os.path.join(ROOT, "census", "j1-ledger.md")
        if os.path.exists(path):
            for line in open(path, encoding="utf-8"):
                if line.startswith("| `"):
                    cells = [c.strip() for c in line.strip().strip("|").split("|")]
                    if len(cells) >= 4:
                        _J1_LEDGER[cells[0].strip("`")] = (cells[1], cells[3])
    return _J1_LEDGER


_PLACE_LEDGER = None


def place_ledger():
    """census/place-ledger.md as {"trunk": {node id: (per-place cells, computed JP, hand JP)},
    "rung": {node id: (place, computed JP, tape)}} — written by check.py."""
    global _PLACE_LEDGER
    if _PLACE_LEDGER is None:
        _PLACE_LEDGER = {"trunk": {}, "rung": {}, "places": []}
        path = os.path.join(ROOT, "census", "place-ledger.md")
        if os.path.exists(path):
            section = "trunk"
            for line in open(path, encoding="utf-8"):
                if line.startswith("## Rung"):
                    section = "rung"
                if line.startswith("| node |") and section == "trunk":
                    _PLACE_LEDGER["places"] = [c.strip() for c in line.strip().strip("|").split("|")][1:-2]
                if line.startswith("| `"):
                    cells = [c.strip() for c in line.strip().strip("|").split("|")]
                    nid = cells[0].strip("`")
                    if section == "trunk" and len(cells) >= 8:
                        _PLACE_LEDGER["trunk"][nid] = (cells[1:6], cells[6], cells[7])
                    elif section == "rung" and len(cells) >= 5:
                        _PLACE_LEDGER["rung"][nid] = (cells[1], cells[2], cells[4])
    return _PLACE_LEDGER


_H_LEDGER = None


def h_ledger():
    """census/h-ledger.md as {"trunk": {node id: (on its domain, on generic ℍ, tape, computed JH, hand JH)},
    "rung": {node id: (computed JH, hand JH, tape)}} and census/h-place-ledger.md as {"h": {node id: (per-place
    cells, computed JP, hand JP)}, "place": {node id: (centre, generic, computed JH, hand JH)}, "places": [...]} —
    both written by check.py (SPEC §7.4)."""
    global _H_LEDGER
    if _H_LEDGER is None:
        _H_LEDGER = {"trunk": {}, "rung": {}, "h": {}, "place": {}, "places": []}
        path = os.path.join(ROOT, "census", "h-ledger.md")
        if os.path.exists(path):
            section = "trunk"
            for line in open(path, encoding="utf-8"):
                if line.startswith("## Rung"):
                    section = "rung"
                if line.startswith("| `"):
                    cells = [c.strip() for c in line.strip().strip("|").split("|")]
                    nid = cells[0].strip("`")
                    if section == "trunk" and len(cells) >= 6:
                        _H_LEDGER["trunk"][nid] = (cells[1], cells[2], cells[3], cells[4], cells[5])
                    elif section == "rung" and len(cells) >= 4:
                        _H_LEDGER["rung"][nid] = (cells[1], cells[2], cells[3])
        path = os.path.join(ROOT, "census", "h-place-ledger.md")
        if os.path.exists(path):
            section = "h"
            for line in open(path, encoding="utf-8"):
                if line.startswith("**Rung place in"):
                    section = "place"
                if line.startswith("| node |") and section == "h":
                    _H_LEDGER["places"] = [c.strip() for c in line.strip().strip("|").split("|")][1:-2]
                if line.startswith("| `"):
                    cells = [c.strip() for c in line.strip().strip("|").split("|")]
                    nid = cells[0].strip("`")
                    if section == "h" and len(cells) >= 8:
                        _H_LEDGER["h"][nid] = (cells[1:6], cells[6], cells[7])
                    elif section == "place" and len(cells) >= 5:
                        _H_LEDGER["place"][nid] = (cells[1], cells[2], cells[3], cells[4])
    return _H_LEDGER


def tape_html(nid: str) -> str:
    """The 𝕁₁ tape of a derivation, as the receipt prover computed it (LEGISLATION 30c), the law at the places
    (the place ledger, rung `place`), and the law in ℍ (the ℍ ledger and the quaternion place ledger, rung `H`)."""
    out = ""
    entry = j1_ledger().get(nid)
    if entry:
        cell, tape = entry
        out += f'<div class="kv"><span class="k">𝕁₁ tape</span><span class="v tape">{inline_tape(tape)}</span></div>'
    pl = place_ledger()
    if nid in pl["trunk"]:
        cells, computed, hand = pl["trunk"][nid]
        places = pl["places"] or [f"p = {q}" for q in (2, 3, 5, 7, 13)]
        items = " · ".join(f"<b>{html.escape(pq)}</b> {html.escape(c)}" for pq, c in zip(places, cells))
        out += f'<div class="kv"><span class="k">at the places</span><span class="v tape">{items} — JP <b>{html.escape(computed)}</b></span></div>'
    elif nid in pl["rung"]:
        place, computed, tape = pl["rung"][nid]
        out += f'<div class="kv"><span class="k">tape at {html.escape(place)}</span><span class="v tape">{inline_tape(tape)}</span></div>'
    hl = h_ledger()
    if nid in hl["trunk"]:
        dom, gen, tape, computed, hand = hl["trunk"][nid]
        t = f'; tape {inline_tape(tape)}' if tape and tape != "—" else ""
        out += f'<div class="kv"><span class="k">in ℍ</span><span class="v tape">on its domain <b>{html.escape(dom)}</b> · on generic ℍ <b>{html.escape(gen)}</b>{t} — JH <b>{html.escape(computed)}</b></span></div>'
    elif nid in hl["rung"]:
        computed, hand, tape = hl["rung"][nid]
        out += f'<div class="kv"><span class="k">tape in ℍ</span><span class="v tape">{inline_tape(tape)}</span></div>'
    if nid in hl["h"]:
        cells, computed, hand = hl["h"][nid]
        places = hl["places"] or [f"p = {q}" for q in (2, 3, 5, 7, 13)]
        items = " · ".join(f"<b>{html.escape(pq)}</b> {html.escape(c)}" for pq, c in zip(places, cells))
        out += f'<div class="kv"><span class="k">at the places</span><span class="v tape">{items} — JP <b>{html.escape(computed)}</b></span></div>'
    elif nid in hl["place"]:
        centre, gen, computed, hand = hl["place"][nid]
        out += f'<div class="kv"><span class="k">in ℍ at its place</span><span class="v tape">on the centre <b>{html.escape(centre)}</b> · on generic quaternions of the page <b>{html.escape(gen)}</b> — JH <b>{html.escape(computed)}</b></span></div>'
    return out


def inline_tape(tape: str) -> str:
    out = html.escape(tape, quote=False)
    out = re.sub(r"`([^`]*)`", r"<code>\1</code>", out)
    out = out.replace("absorbed [absorbing]", "<b>absorbed</b>").replace("posted [depth-0]", "<b>posted</b>").replace("import [under-square]", "<b>import</b>").replace("absent [under-square]", "<b>false</b>")
    out = out.replace("strict [pole]", "<b>strict</b> [pole]").replace("; except ", "; <b>except</b> ")
    out = re.sub(r"page \[([^\]]*)\]", r"<b>page</b> [\1]", out)
    out = out.replace("formless [under-square]", "<b>formless</b> [under-square]")
    out = re.sub(r"(absorbed|posted|import|absent) \[page step under a square, measured at the square: ([^\]]*)\]", r"<b>\1</b> [page step, measured at the square above it: \2]", out)
    out = re.sub(r"absorbed \[inherited ([^\]]*)\]", r"<b>absorbed</b> [inherited \1]", out)
    out = out.replace("absent [cross-slice]", "<b>absent</b> [cross-slice]").replace("absent [premise]", "<b>absent</b> [premise]").replace("absorbed [seam]", "<b>absorbed</b> [seam]")
    return out


def law_block(node, nodes):
    law = str(node.get("law", ""))
    units = str(node.get("units", ""))
    if node.get("schema_range"):   # a schema, or a decree/import written over the place and the depth (rung `place`)
        env = draw_env(node)
        try:
            inst = SCH.expand(law, env)
        except ValueError:
            inst = law
        tmpl = law
        law = inst
        l, r, sym = F.split_law(law)
        r = r or ""
        drawing = f'{draw_form(l)}<span class="eq">{sym}</span>{draw_form(r)}' if r else f'<span class="lawtext">{html.escape(law)}</span>'
        return (f'<div class="law schema"><div class="drawing">{drawing}</div>'
                f'<div class="lawrow"><code class="canon">{html.escape(tmpl)}</code>'
                f'<span class="units">{html.escape(units)}</span></div>'
                f'<div class="lawrow"><span class="sugar">drawn at {html.escape(SCH.describe(env))}; checked for {html.escape(str(node.get("schema_range", "")))}</span></div></div>')
    if node.get("type") == "gap" or law.startswith("DISCIPLINE") or node.get("kind") in ("discipline", "declaration", "guard") or node.get("level") == "meta":
        cls = "law gap" if node.get("type") == "gap" else "law decree"
        return f'<div class="{cls}"><div class="lawtext">{inline(law, nodes)}</div><div class="units">{html.escape(units)}</div></div>'
    if F.split_law(law)[1] is not None:
        l, r, sym = F.split_law(law)
        drawing = f'{draw_form(l)}<span class="eq">{sym}</span>{draw_form(r)}'
    elif ":=" in law:
        l, r = [x.strip() for x in law.split(":=", 1)]
        left = draw_form(l)
        right = draw_form(r)
        drawing = f'{left}<span class="eq">:=</span>{right}'
    elif " is a form" in law:
        drawing = f'{draw_form(law.split(" is a form")[0].strip())}<span class="eq small">is a form</span>'
    elif "is not a form" in law:
        parts = [p.strip() for p in law.split(";") if p.strip()]
        drawing = "".join(f'<span class="excl">{draw_form(p.split(" is not")[0].strip())}</span><span class="eq small">is not a form</span>' for p in parts)
    else:
        drawing = f'<span class="lawtext">{inline(law, nodes)}</span>'
    sugar = law
    try:
        if F.split_law(law)[1] is not None:
            l, r, sym = F.split_law(law)
            sugar = f" {sym} ".join(F.to_string(F.parse(x), True, omega=node.get("setting") in ("J1", "JP")) for x in (l, r))
    except Exception:
        pass
    return (f'<div class="law"><div class="drawing">{drawing}</div>'
            f'<div class="lawrow"><code class="canon">{html.escape(law)}</code>'
            f'{"" if sugar == law else f"<code class=sugar>{html.escape(sugar)}</code>"}'
            f'<span class="units">{html.escape(units)}</span></div></div>')


def render_node(node, nodes, used_by, depth, price):
    m = node.meta
    nid = node.id
    t = m.get("type")
    base = sorted(p for p in price[nid] if p in BASE_IDS)
    extra = sorted(p for p in price[nid] if p not in BASE_IDS)
    meta_tags = []
    if m.get("level") == "meta":
        meta_tags.append(badge("lvl", "meta", "a statement about the calculus"))
    meta_tags.append(badge("guide", m.get("guide", ""), "shape-led: the forms asked for it · need-led: mathematics pushed for it"))
    meta_tags.append(badge("band", f"band {m.get('band')}", "K–12 band from the Iconic Mathematics scope and sequence"))
    if m.get("kind") not in ("law",):
        meta_tags.append(badge("kind", m.get("kind", "")))
    und = str(m.get("understood", "no")).lower()
    und_mark = {"yes": "●", "partial": "◐", "no": "○"}.get(und, "○")
    secs = node.sections
    uses_links = " ".join(f'<a class="nl" href="#{u}">{u}</a>' for u in (m.get("uses") or []))
    used_links = " ".join(f'<a class="nl" href="#{u}">{u}</a>' for u in used_by[nid])
    see_links = " ".join(f'<a class="nl dashed" href="#{u}">{u}</a>' for u in (m.get("see_also") or []))
    rel = sorted(CHK.seam_reliance(node)) if m.get("guarded_by") else []
    guard_links = " ".join(f'<a class="nl" href="#{u}">{u}</a>' for u in (m.get("guarded_by") or []))
    if rel:
        guard_links += f' <span class="clause">by {" and ".join(rel)}</span>'
    price_html = ""
    if t in ("theorem", "definition", "gap"):
        pb = ", ".join(f'<a class="nl" href="#{p}">{p}</a>' for p in base) or "—"
        pe = ", ".join(f'<a class="nl" href="#{p}">{p}</a>' for p in extra) or "none"
        price_html = f'<div class="kv"><span class="k">price</span><span class="v">base: {pb}<br>extra: <b>{pe}</b></span></div>'
    refuted = secs.get("Refuted readings", "none").strip()
    refuted_html = "" if refuted.lower().startswith("none") else f'<h4>Refuted readings</h4><div class="refuted">{md(refuted, nodes)}</div>'
    plan_html = f'<h4>Plan</h4>{md(secs["Plan"], nodes)}' if "Plan" in secs else ""
    notes = secs.get("Notes", "").strip()
    notes_html = "" if notes in ("", "—") else f'<h4>Notes</h4>{md(notes, nodes)}'
    verified = m.get("verified", "none")
    status = m.get("status", "")
    hollow = " hollow" if verified in ("none", "hand") and t in ("theorem", "definition") else ""
    return f'''
<article class="node t-{t}" id="{nid}" data-search="{html.escape(nid + ' ' + str(m.get('title','')) + ' ' + ' '.join(map(str, m.get('aliases') or [])) + ' ' + ' '.join(map(str, m.get('concepts') or [])))}">
  <header>
    <div class="idrow"><a class="id" href="#{nid}">{nid}</a>{badge("type t-" + str(t), t)}{badge("status s-" + status.lower().replace("-", "") + hollow, status, "status (SPEC §8.1)" + ("; hollow: Exact withheld until engine-verified" if hollow else ""))}{badge("ver v-" + verified, verified, "verification tier")}{"".join(meta_tags)}<span class="und" title="understood: {und}">{und_mark}</span></div>
    <h3>{html.escape(str(m.get("title", "")))}</h3>
  </header>
  {law_block(node, nodes)}
  <p class="plain">{inline(secs.get("Plain", ""), nodes)}</p>
  <div class="settings">{chips(m.get("holds") or {}, "h")}<span class="sep"></span>{chips(m.get("readings") or {}, "r")}</div>
  <details class="deriv" open>
    <summary>Derivation</summary>
    {md(SCH.expand_derivation(secs.get("Derivation", ""), draw_env(node), keep_fixed="all", captions=True) if m.get("schema_range") else secs.get("Derivation", ""), nodes, draw_first_col=True)}
  </details>
  <details class="more">
    <summary>Confirms · settings · notes</summary>
    <h4>Confirms</h4>{md(secs.get("Confirms", ""), nodes)}
    <h4>Settings and readings</h4>{md(secs.get("Settings and readings", ""), nodes)}
    {refuted_html}{notes_html}{plan_html}
  </details>
  <footer>
    <div class="kv"><span class="k">uses</span><span class="v">{uses_links or "—"}</span></div>
    <div class="kv"><span class="k">used by</span><span class="v">{used_links or "—"}</span></div>
    {f'<div class="kv"><span class="k">guarded by</span><span class="v">{guard_links}</span></div>' if guard_links else ""}
    {f'<div class="kv"><span class="k">owed</span><span class="v owed">{"<br>".join(inline(str(x), nodes) for x in (m.get("owed") or []))}</span></div>' if m.get("owed") else ""}
    {tape_html(nid)}
    {f'<div class="kv"><span class="k">see also</span><span class="v">{see_links}</span></div>' if see_links else ""}
    {price_html}
    <div class="kv"><span class="k">depth</span><span class="v">{depth[nid]}</span><span class="k">known since</span><span class="v">{html.escape(str(m.get("known_since","")))}</span><span class="k">entered</span><span class="v">{html.escape(str(m.get("entered","")))}</span><span class="k">equality</span><span class="v">{html.escape(str(m.get("equality","")))}</span></div>
    <div class="kv"><span class="k">aliases</span><span class="v">{html.escape(", ".join(map(str, m.get("aliases") or [])) or "—")}</span><span class="k">concepts</span><span class="v">{" ".join(f'<a class="cl" href="#concept-{c}">{html.escape(c)}</a>' for c in (m.get("concepts") or []))}</span></div>
  </footer>
</article>'''


def render_dag(nodes, depth):
    """Layered DAG: columns by depth; rows grouped by rung then walk order."""
    rung_order = {r: i for i, r in enumerate(N.RUNGS)}
    cols = {}
    for n in nodes.values():
        cols.setdefault(depth[n.id], []).append(n)
    for c in cols.values():
        c.sort(key=lambda n: (rung_order.get(n.get("rung"), 99), n.get("order", 0)))
    colw, rowh, bw, bh = 196, 42, 170, 30
    maxrows = max(len(c) for c in cols.values())
    W = colw * (max(cols) + 1) + 30
    Hh = rowh * maxrows + 40
    pos = {}
    for d, col in cols.items():
        for i, n in enumerate(col):
            pos[n.id] = (20 + d * colw, 20 + i * rowh)
    edges, boxes = [], []
    for n in nodes.values():
        x2, y2 = pos[n.id]
        for u in n.get("uses", []) or []:
            if u not in pos:
                continue
            x1, y1 = pos[u]
            sx, sy = x1 + bw, y1 + bh / 2
            tx, ty = x2, y2 + bh / 2
            cx = (sx + tx) / 2
            cls = "edge reentry" if n.get("reentry") else "edge"
            edges.append(f'<path class="{cls}" data-from="{u}" data-to="{n.id}" d="M{sx:.0f},{sy:.0f} C{cx:.0f},{sy:.0f} {cx:.0f},{ty:.0f} {tx:.0f},{ty:.0f}"/>')
    for n in nodes.values():
        x, y = pos[n.id]
        title = str(n.get("title", ""))
        short = title if len(title) <= 24 else title[:23] + "…"
        boxes.append(f'<a href="#{n.id}" class="gn t-{n.get("type")}" data-id="{n.id}"><rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="4"/>'
                     f'<text x="{x+7}" y="{y+12}" class="gid">{html.escape(n.id)}</text><text x="{x+7}" y="{y+24}" class="gt">{html.escape(short)}</text><title>{html.escape(n.id + " — " + title)}</title></a>')
    labels = "".join(f'<text class="glab" x="{20 + d*colw}" y="12">depth {d}</text>' for d in cols)
    return (f'<div class="dagwrap" id="dagwrap"><svg id="dag" viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}">'
            f'<g id="dagg">{labels}{"".join(edges)}{"".join(boxes)}</g></svg></div>')


def render_concepts(nodes, concepts):
    index = {}
    for n in nodes.values():
        for c in n.get("concepts") or []:
            index.setdefault(c, []).append(n)
    out = []
    for c in sorted(index):
        ns = sorted(index[c], key=lambda n: n.get("order", 0))
        desc = concepts.get(c, {}).get("body", "")
        links = " ".join(f'<a class="nl" href="#{n.id}">{n.id}</a>' for n in ns)
        out.append(f'<div class="concept" id="concept-{c}"><h4>{html.escape(c)}</h4>{f"<p>{inline(desc, nodes)}</p>" if desc else ""}<div class="links">{links}</div></div>')
    return "".join(out)


def render_census(rows, nodes):
    counts = {}
    for r in rows:
        counts[r[2]] = counts.get(r[2], 0) + 1
    summary = " · ".join(f"{k} <b>{v}</b>" for k, v in sorted(counts.items()))
    trs = []
    for n, f, cls, v, a in rows:
        val = "—" if v is None else F.fmt(v)
        link = f'<a class="nl" href="#{a}">{a}</a>' if a else ""
        trs.append(f'<tr class="cz-{cls}"><td>{n}</td><td class="fcell">{draw_form(F.to_string(f), "form sm")}<code>{html.escape(F.to_string(f, True))}</code></td><td>{cls}</td><td>{html.escape(val)}</td><td>{link}</td></tr>')
    return summary, "".join(trs)


def main():
    nodes = N.load_nodes(os.path.join(ROOT, "nodes"))
    concepts = N.load_concepts(os.path.join(ROOT, "concepts"))
    used_by, depth, price = compute(nodes)
    ordered = sorted(nodes.values(), key=lambda n: n.get("order", 0))
    rungs = []
    for n in ordered:
        if not rungs or rungs[-1] != n.get("rung"):
            rungs.append(n.get("rung"))
    rows, unassigned = C.run(write=False)
    census_summary, census_rows = render_census(rows, nodes)
    open_forms = ""
    ofp = os.path.join(ROOT, "census", "open-forms.md")
    if os.path.exists(ofp):
        with open(ofp, encoding="utf-8") as fh:
            open_forms = md(fh.read().split("\n", 3)[-1], nodes)

    counts = {}
    for n in nodes.values():
        counts[n.get("type")] = counts.get(n.get("type"), 0) + 1
    und = {"yes": 0, "partial": 0, "no": 0}
    for n in nodes.values():
        und[str(n.get("understood", "no")).lower()] = und.get(str(n.get("understood", "no")).lower(), 0) + 1
    gaps = [n for n in ordered if n.get("type") == "gap"]
    refuted = [(n, n.sections.get("Refuted readings", "")) for n in ordered if not n.sections.get("Refuted readings", "none").strip().lower().startswith("none")]
    engine = sum(1 for n in nodes.values() if n.get("verified") in ("engine", "numeric", "lean"))
    steps = sum(len(t) - 1 for n in nodes.values() for t in N.parse_tables(n.sections.get("Derivation", "")) if t and t[0][0].lower() == "form")
    shape_led = sum(1 for n in nodes.values() if n.get("guide") == "shape-led")

    chapters = []
    for r in rungs:
        ns = [n for n in ordered if n.get("rung") == r]
        sl = sum(1 for n in ns if n.get("guide") == "shape-led")
        chapters.append(f'<section class="rung" id="rung-{r}"><h2><span class="rid">{html.escape(r)}</span> {html.escape(RUNG_TITLES.get(r, r))}<span class="rmeta">{len(ns)} laws · {sl} shape-led · {len(ns)-sl} need-led</span></h2>'
                        + "".join(render_node(n, nodes, used_by, depth, price) for n in ns) + "</section>")

    gap_html = "".join(f'<div class="gapitem"><a class="nl" href="#{n.id}">{n.id}</a> <b>{html.escape(str(n.get("title")))}</b> — {inline(str(n.get("law")), nodes)}</div>' for n in gaps)
    owed_items = [(n, x) for n in ordered for x in (n.get("owed") or [])]
    owed_html = "".join(f'<div class="gapitem"><a class="nl" href="#{n.id}">{n.id}</a> {inline(str(x), nodes)}</div>' for n, x in owed_items)
    ref_html = "".join(f'<div class="refitem"><a class="nl" href="#{n.id}">{n.id}</a>{md(txt, nodes)}</div>' for n, txt in refuted)
    toc = "".join(f'<a href="#rung-{r}">{html.escape(r)}</a>' for r in rungs)

    page = f'''<title>Boundary Chart</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Serif:ital,wght@0,500;0,600;1,400&display=swap">
<style>
/* layout: a ledger — one column of chapters, each law a card with the forms drawn first; a search bar and a layered graph up top */
:root {{
  --bg:#f6f7f5; --bg2:#ffffff; --bg3:#eceeea; --fg:#1f2421; --fg2:#5a635e; --line:#d6dad4; --accent:#1f5f8b;
  --round:#2a6f97; --square:#b07a1a; --angle:#b23a48;
  --t-primitive:#4c6a92; --t-axiom:#b23a48; --t-definition:#2e8b8b; --t-theorem:#3e7d3a; --t-decree:#b07a1a; --t-import:#7a5ca8; --t-gap:#7d7f7a; --t-schema:#2f6f9f;
  --ok:#3e7d3a; --warn:#b07a1a; --bad:#b23a48; --mute:#8a8f8a;
  --serif:"IBM Plex Serif", Georgia, "Times New Roman", serif; --sans:"IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif; --mono:"IBM Plex Mono", ui-monospace, Menlo, Consolas, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg:#181b19; --bg2:#202421; --bg3:#2a2f2b; --fg:#e6e9e4; --fg2:#a6ada7; --line:#3a403b; --accent:#7fb3d5;
  --round:#7fb3d5; --square:#d9a84a; --angle:#e07a86;
  --t-primitive:#8fa8cc; --t-axiom:#e07a86; --t-definition:#6fc1c1; --t-theorem:#7fbf78; --t-decree:#d9a84a; --t-import:#b39ddb; --t-gap:#9a9e98; --t-schema:#6ea8d8;
  --ok:#7fbf78; --warn:#d9a84a; --bad:#e07a86; --mute:#767b76; color-scheme: dark }} }}
:root[data-theme="dark"] {{
  --bg:#181b19; --bg2:#202421; --bg3:#2a2f2b; --fg:#e6e9e4; --fg2:#a6ada7; --line:#3a403b; --accent:#7fb3d5;
  --round:#7fb3d5; --square:#d9a84a; --angle:#e07a86;
  --t-primitive:#8fa8cc; --t-axiom:#e07a86; --t-definition:#6fc1c1; --t-theorem:#7fbf78; --t-decree:#d9a84a; --t-import:#b39ddb; --t-gap:#9a9e98; --t-schema:#6ea8d8;
  --ok:#7fbf78; --warn:#d9a84a; --bad:#e07a86; --mute:#767b76; color-scheme: dark }}
body {{ background:var(--bg); color:var(--fg); font-family:var(--sans); font-size:15px; line-height:1.5; margin:0; }}
.wrap {{ max-width:1040px; margin:0 auto; padding-block:20px 60px; padding-inline:16px; }}
h1 {{ font-family:var(--serif); font-weight:600; font-size:2rem; margin:0; letter-spacing:-0.01em; text-wrap:balance; }}
h2 {{ font-family:var(--serif); font-weight:600; font-size:1.45rem; margin:48px 0 14px; padding-top:18px; border-top:2px solid var(--line); display:flex; gap:10px; align-items:baseline; flex-wrap:wrap; }}
h2 .rid {{ font-family:var(--mono); font-size:0.95rem; color:var(--fg2); font-weight:500; }}
h2 .rmeta {{ margin-left:auto; font-family:var(--sans); font-size:0.78rem; color:var(--fg2); font-weight:400; }}
h3 {{ font-family:var(--serif); font-weight:500; font-size:1.2rem; margin:4px 0 8px; text-wrap:balance; }}
h4 {{ font-size:0.72rem; text-transform:uppercase; letter-spacing:0.08em; color:var(--fg2); margin:16px 0 6px; font-weight:600; }}
p {{ margin:6px 0; max-width:72ch; }}
code {{ font-family:var(--mono); font-size:0.86em; background:var(--bg3); padding:1px 4px; border-radius:3px; }}
a {{ color:var(--accent); }}
.lede {{ color:var(--fg2); max-width:72ch; margin:8px 0 0; }}
.stats {{ display:flex; gap:18px 26px; flex-wrap:wrap; margin:18px 0 8px; font-variant-numeric:tabular-nums; }}
.stat b {{ display:block; font-family:var(--serif); font-size:1.5rem; font-weight:600; line-height:1.1; }}
.stat span {{ font-size:0.75rem; color:var(--fg2); text-transform:uppercase; letter-spacing:0.06em; }}
.progress {{ height:8px; background:var(--bg3); border-radius:4px; overflow:hidden; display:flex; max-width:420px; margin:6px 0 2px; }}
.progress i {{ display:block; height:100%; }}
.legend {{ display:flex; gap:6px 14px; flex-wrap:wrap; font-size:0.78rem; color:var(--fg2); margin:14px 0; align-items:center; }}
.legend .sw {{ display:inline-block; width:10px; height:10px; border-radius:2px; margin-right:5px; vertical-align:-1px; }}
.toolbar {{ display:flex; gap:10px; flex-wrap:wrap; align-items:center; margin:16px 0; position:sticky; top:env(safe-area-inset-top, 0px); background:var(--bg); padding:8px 0; z-index:5; border-bottom:1px solid var(--line); }}
.toolbar input {{ flex:1 1 220px; min-width:0; font:inherit; padding:7px 10px; border:1px solid var(--line); border-radius:6px; background:var(--bg2); color:var(--fg); }}
.toolbar input:focus {{ outline:2px solid var(--accent); outline-offset:1px; }}
.toc {{ display:flex; gap:6px; flex-wrap:wrap; }}
.toc a {{ font-family:var(--mono); font-size:0.78rem; text-decoration:none; padding:4px 8px; border:1px solid var(--line); border-radius:4px; color:var(--fg2); background:var(--bg2); }}
.toc a:hover {{ color:var(--fg); border-color:var(--accent); }}
.dagwrap {{ overflow:auto; border:1px solid var(--line); border-radius:6px; background:var(--bg2); max-height:520px; cursor:grab; }}
.dagwrap:active {{ cursor:grabbing; }}
#dag {{ display:block; font-family:var(--mono); }}
#dag .edge {{ fill:none; stroke:var(--line); stroke-width:1.2; }}
#dag .edge.hl {{ stroke:var(--accent); stroke-width:2; }}
#dag .edge.reentry {{ stroke:var(--bad); stroke-dasharray:4 3; }}
#dag .gn rect {{ fill:var(--bg2); stroke-width:1.6; }}
#dag .gn.t-gap rect {{ stroke-dasharray:4 3; }}
#dag .gn:hover rect {{ fill:var(--bg3); }}
#dag .gn text {{ fill:var(--fg); }}
#dag .gid {{ font-size:10px; font-weight:500; }}
#dag .gt {{ font-size:9.5px; fill:var(--fg2) !important; font-family:var(--sans); }}
#dag .glab {{ font-size:9px; fill:var(--fg2); text-transform:uppercase; letter-spacing:0.08em; }}
#dag .t-primitive rect {{ stroke:var(--t-primitive); }} #dag .t-axiom rect {{ stroke:var(--t-axiom); }} #dag .t-definition rect {{ stroke:var(--t-definition); }}
#dag .t-theorem rect {{ stroke:var(--t-theorem); }} #dag .t-decree rect {{ stroke:var(--t-decree); }} #dag .t-import rect {{ stroke:var(--t-import); }} #dag .t-gap rect {{ stroke:var(--t-gap); }} #dag .t-schema rect {{ stroke:var(--t-schema); stroke-width:2.5; }}
.hint {{ font-size:0.75rem; color:var(--fg2); margin:6px 0 0; }}
article.node {{ background:var(--bg2); border:1px solid var(--line); border-left:4px solid var(--mute); border-radius:6px; padding:14px 16px 10px; margin:12px 0; scroll-margin-top:70px; }}
article.node.hidden-by-search {{ display:none; }}
.t-primitive {{ border-left-color:var(--t-primitive) !important; }} .t-axiom {{ border-left-color:var(--t-axiom) !important; }} .t-definition {{ border-left-color:var(--t-definition) !important; }}
.t-theorem {{ border-left-color:var(--t-theorem) !important; }} .t-decree {{ border-left-color:var(--t-decree) !important; }} .t-import {{ border-left-color:var(--t-import) !important; }} .t-gap {{ border-left-color:var(--t-gap) !important; border-left-style:dashed; }}
.idrow {{ display:flex; gap:6px; flex-wrap:wrap; align-items:center; font-size:0.74rem; }}
.id {{ font-family:var(--mono); font-weight:500; text-decoration:none; color:var(--fg2); }}
.bd {{ display:inline-block; padding:1px 7px; border-radius:10px; border:1px solid var(--line); color:var(--fg2); line-height:1.4; white-space:nowrap; }}
.bd.type {{ color:#fff; border-color:transparent; font-weight:500; }}
.bd.type.t-primitive {{ background:var(--t-primitive); }} .bd.type.t-axiom {{ background:var(--t-axiom); }} .bd.type.t-definition {{ background:var(--t-definition); }} .bd.type.t-theorem {{ background:var(--t-theorem); }} .bd.type.t-decree {{ background:var(--t-decree); }} .bd.type.t-import {{ background:var(--t-import); }} .bd.type.t-gap {{ background:var(--t-gap); }} .bd.type.t-schema {{ background:var(--t-schema); }}
.bd.status {{ font-weight:500; }}
.bd.s-native, .bd.s-nativebydecree, .bd.s-nativebyschema {{ color:var(--ok); border-color:var(--ok); }}
.bd.s-nativebyschema {{ border-style:double; }}
.bd.s-imported, .bd.s-analogy, .bd.s-conjecture {{ color:var(--warn); border-color:var(--warn); }}
.bd.s-refuted {{ color:var(--bad); border-color:var(--bad); text-decoration:line-through; }}
.bd.s-absent {{ color:var(--mute); border-style:dashed; }}
.bd.hollow {{ background:transparent; border-style:dotted; }}
.bd.v-engine, .bd.v-numeric, .bd.v-lean {{ background:var(--bg3); }}
.bd.v-none, .bd.v-hand {{ border-style:dotted; }}
.und {{ margin-left:auto; font-size:0.95rem; color:var(--fg2); }}
.law {{ display:flex; flex-direction:column; gap:8px; padding:10px 12px; background:var(--bg3); border-radius:6px; margin:8px 0; overflow-x:auto; }}
.law .drawing {{ display:flex; align-items:center; gap:10px; flex-wrap:wrap; min-height:28px; }}
.law .eq {{ font-family:var(--serif); font-size:1.3rem; color:var(--fg2); }}
.law .eq.small {{ font-size:0.9rem; font-family:var(--sans); }}
.law .excl {{ position:relative; display:inline-flex; }}
.law .excl::after {{ content:""; position:absolute; left:-4px; right:-4px; top:50%; border-top:2px solid var(--bad); transform:rotate(-20deg); }}
.lawrow {{ display:flex; gap:12px; flex-wrap:wrap; align-items:baseline; font-size:0.85rem; }}
.lawrow code {{ background:transparent; padding:0; }}
.lawrow .sugar {{ color:var(--fg2); }}
.lawrow .units {{ color:var(--fg2); font-family:var(--serif); font-style:italic; }}
.law.gap {{ border:1px dashed var(--t-gap); background:transparent; }}
.law.decree {{ border:1px solid var(--t-decree); }}
.law.schema {{ border:3px double var(--accent); }}
.law .lawtext {{ font-size:0.95rem; }}
svg.form {{ overflow:visible; vertical-align:middle; flex:none; }}
.law .drawing svg.form {{ max-width:100%; height:auto; }}
svg.form .b-r {{ fill:none; stroke:var(--round); stroke-width:1.6; }}
svg.form .b-s {{ fill:none; stroke:var(--square); stroke-width:1.6; }}
svg.form .b-sep {{ stroke:var(--square); stroke-width:1; stroke-dasharray:2 2; }}
svg.form .fc {{ font-style:italic; }}
svg.form .b-a {{ fill:none; stroke:var(--angle); stroke-width:1.6; stroke-linejoin:round; }}
svg.form .fv {{ font-family:var(--serif); font-style:italic; font-size:12px; fill:var(--fg); }}
svg.form.sm {{ transform:scale(0.85); transform-origin:left center; }}
.void {{ font-family:var(--serif); font-style:italic; color:var(--fg2); border:1px dotted var(--line); padding:0 6px; border-radius:3px; }}
.name {{ font-family:var(--serif); font-style:italic; }}
.plain {{ font-family:var(--serif); font-size:1.05rem; line-height:1.5; margin:8px 0 10px; }}
.settings {{ display:flex; gap:4px; flex-wrap:wrap; align-items:center; margin:4px 0 8px; }}
.settings .sep {{ width:10px; }}
.chip {{ font-size:0.68rem; padding:1px 6px; border-radius:3px; background:var(--bg3); color:var(--fg2); white-space:nowrap; }}
.chip b {{ font-weight:500; color:var(--fg); margin-right:3px; }}
.chip.c-h-holds, .chip.c-r-exact {{ box-shadow:inset 0 -2px 0 var(--ok); }}
.chip.c-h-holdsmod, .chip.c-h-guarded, .chip.c-h-replaced, .chip.c-r-partial, .chip.c-r-analogy, .chip.c-r-converse {{ box-shadow:inset 0 -2px 0 var(--warn); }}
.chip.c-h-fails, .chip.c-r-absent {{ box-shadow:inset 0 -2px 0 var(--bad); }}
.chip.c-h-untested, .chip.c-r-untested {{ opacity:0.65; }}
.clause {{ font-size:0.78rem; color:var(--fg2); font-style:italic; margin-left:4px; }}
details {{ margin:8px 0; }}
summary {{ cursor:pointer; font-size:0.72rem; text-transform:uppercase; letter-spacing:0.08em; color:var(--fg2); font-weight:600; }}
summary:focus-visible {{ outline:2px solid var(--accent); }}
.tw {{ overflow-x:auto; margin:6px 0; }}
table {{ border-collapse:collapse; font-size:0.86rem; width:100%; }}
th, td {{ text-align:left; vertical-align:top; padding:5px 8px; border-bottom:1px solid var(--line); }}
th {{ font-size:0.7rem; text-transform:uppercase; letter-spacing:0.06em; color:var(--fg2); font-weight:600; }}
table.deriv {{ table-layout:fixed; }}
table.deriv col.c-form {{ width:46%; }} table.deriv col.c-rule {{ width:22%; }} table.deriv col.c-note {{ width:32%; }}
td.fcell {{ white-space:normal; }}
td.fcell .draw {{ overflow-x:auto; max-width:100%; padding-bottom:4px; }}
td.fcell code {{ white-space:pre-wrap; word-break:break-all; }}
td.fcell code {{ display:block; margin-top:2px; font-size:0.74rem; background:transparent; padding:0; color:var(--fg2); }}
.deriv table td:nth-child(2) {{ white-space:normal; overflow-wrap:anywhere; }}
.nl {{ font-family:var(--mono); font-size:0.84em; text-decoration:none; border-bottom:1px solid var(--line); }}
.nl:hover {{ border-bottom-color:var(--accent); }}
.nl.dashed {{ border-bottom-style:dashed; }}
.cl {{ font-size:0.84em; text-decoration:none; border-bottom:1px dotted var(--line); margin-right:6px; }}
.v.tape {{ font-size:0.76rem; color:var(--mute); }} .v.tape b {{ color:var(--fg); font-weight:600; }} .v.owed {{ font-size:0.8rem; color:var(--warn); }}
article footer {{ margin-top:10px; padding-top:8px; border-top:1px dashed var(--line); font-size:0.8rem; display:flex; flex-direction:column; gap:4px; }}
.kv {{ display:flex; gap:10px; flex-wrap:wrap; align-items:baseline; }}
.kv .k {{ font-size:0.68rem; text-transform:uppercase; letter-spacing:0.06em; color:var(--fg2); min-width:60px; }}
.kv .v {{ color:var(--fg); min-width:0; }}
.refuted {{ border-left:3px solid var(--bad); padding-left:10px; }}
.concepts {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(220px, 1fr)); gap:10px; }}
.concept {{ background:var(--bg2); border:1px solid var(--line); border-radius:6px; padding:10px 12px; min-width:0; }}
.concept h4 {{ margin:0 0 6px; }}
.concept .links {{ display:flex; gap:6px; flex-wrap:wrap; }}
.gapitem, .refitem {{ padding:8px 0; border-bottom:1px solid var(--line); }}
.census td:nth-child(2) {{ white-space:nowrap; }}
.cz-new td:nth-child(3) {{ color:var(--ok); font-weight:500; }} .cz-undefined td:nth-child(3), .cz-excluded td:nth-child(3) {{ color:var(--bad); }}
.foot {{ margin-top:40px; color:var(--fg2); font-size:0.8rem; border-top:1px solid var(--line); padding-top:12px; }}
@media (max-width: 600px) {{ h2 .rmeta {{ margin-left:0; }} .kv .k {{ min-width:0; }} }}
@media (prefers-reduced-motion: reduce) {{ * {{ scroll-behavior:auto !important; transition:none !important; }} }}
</style>
<div class="wrap">
<header>
  <h1>The Boundary Chart</h1>
  <p class="lede">Mathematics in James boundary arithmetic, one law per step, from the void toward F₁. Every law is drawn, glossed, derived from the laws before it, and checked by the engine. Built so far: rungs <code>void</code>, <code>N</code>, <code>Z</code>, <code>mult</code>, <code>Q</code>, <code>alg</code> and <code>C</code> — the classical James algebra of the 1993 thesis (Chapters 4–6 and Appendix B, checked against the text) with the standard complex-number toolkit — <code>schema</code>, the laws over every n (cardinality, powers, the n-th roots of unity, De Moivre) stated once as templates, checked at every n in a range, and priced with the induction gap they lean on; and <code>J1</code>, the enriched calculus 𝕁₁ — Involution split into a strict counit and a witnessed unit, the log of one kept as the period form ω rather than erased, every step graded by the receipt it posts (strict, absorbed, posted) by the receipt prover, James's two theorems of Chapter 6 re-read as true mod Λ, and the ψ-wall counting 24, 240, 504; and <code>place</code>, the finite places — a place is a pile declared void, the page at p read in its log space (a number part, a count of the prime's log, a count of the torsion log), the same wall <code>(ω A) ≃ (A)</code> with the place's own period, every trunk law read at p = 2, 3, 5, 7, 13 and every derivation re-graded there, Fermat and Hensel and the doll of 1/(1 − p) as laws, and the ψ-wall split into its local factors.</p>
  <div class="stats">
    <div class="stat"><b>{len(nodes)}</b><span>laws</span></div>
    <div class="stat"><b>{counts.get("theorem",0)}</b><span>theorems</span></div>
    <div class="stat"><b>{counts.get("axiom",0)} + {counts.get("primitive",0)}</b><span>axioms + primitives</span></div>
    <div class="stat"><b>{counts.get("decree",0)}</b><span>decrees</span></div>
    <div class="stat"><b>{counts.get("gap",0)}</b><span>gaps</span></div>
    <div class="stat"><b>{len(owed_items)}</b><span>owed</span></div>
    <div class="stat"><b>{steps}</b><span>derivation steps checked</span></div>
    <div class="stat"><b>{engine}/{len(nodes)}</b><span>engine-verified</span></div>
    <div class="stat"><b>{shape_led}/{len(nodes)}</b><span>shape-led</span></div>
  </div>
  <div class="stat"><span>the walk — understood</span>
    <div class="progress" title="● {und.get('yes',0)} understood · ◐ {und.get('partial',0)} partial · ○ {und.get('no',0)} not yet">
      <i style="width:{100*und.get('yes',0)/max(1,len(nodes)):.0f}%;background:var(--ok)"></i><i style="width:{100*und.get('partial',0)/max(1,len(nodes)):.0f}%;background:var(--warn)"></i>
    </div>
    <span>● {und.get('yes',0)} · ◐ {und.get('partial',0)} · ○ {und.get('no',0)}</span>
  </div>
  <div class="legend">
    <span><i class="sw" style="background:var(--t-primitive)"></i>primitive</span><span><i class="sw" style="background:var(--t-axiom)"></i>axiom</span><span><i class="sw" style="background:var(--t-definition)"></i>definition</span><span><i class="sw" style="background:var(--t-theorem)"></i>theorem</span><span><i class="sw" style="background:var(--t-decree)"></i>decree</span><span><i class="sw" style="background:var(--t-import)"></i>import</span><span><i class="sw" style="background:var(--t-gap);opacity:.6"></i>gap</span><span><i class="sw" style="background:var(--t-schema)"></i>schema</span>
    <span style="margin-left:10px"><i class="sw" style="background:var(--round);border-radius:6px"></i>( ) round</span><span><i class="sw" style="background:var(--square);border-radius:0"></i>[ ] square</span><span><i class="sw" style="background:var(--angle);transform:rotate(45deg)"></i>&lt; &gt; angle</span>
  </div>
</header>
<div class="toolbar">
  <input id="q" type="search" placeholder="search laws, aliases, concepts — e.g. negation, Dominion, JH-20" aria-label="search the chart">
  <nav class="toc">{toc}<a href="#concepts">concepts</a><a href="#gaps">gaps</a><a href="#owed">owed</a><a href="#refuted">refuted</a><a href="#census">census</a></nav>
</div>
<section id="chart">
  <h2>The chart<span class="rmeta">columns = derivation depth · click a law to jump · hover to light its edges · drag to pan</span></h2>
  {render_dag(nodes, depth)}
  <p class="hint">Edges run from a law to the laws derived from it. Dashed boxes are gaps; heavy boxes are schemas (one law for every n). The one re-entry edge (F₁ → void) is not yet in the pilot.</p>
</section>
{"".join(chapters)}
<section id="concepts"><h2>Concept index<span class="rmeta">a concept resolves to the laws that express it</span></h2><div class="concepts">{render_concepts(nodes, concepts)}</div></section>
<section id="gaps"><h2>Gaps<span class="rmeta">concepts without a form; each carries a plan</span></h2>{gap_html}</section>
<section id="owed"><h2>Owed<span class="rmeta">obligations the chart has not met — a derivation, a reading, a cell — recorded where they fall due (LEGISLATION 33(d))</span></h2>{owed_html or "<p>none</p>"}</section>
<section id="refuted"><h2>Refuted readings<span class="rmeta">kept, struck through, attached to the law they were mistaken for</span></h2>{ref_html or "<p>none yet</p>"}</section>
<section id="census"><h2>Census of small forms<span class="rmeta">every form with at most three boundaries</span></h2>
  <p>{census_summary} · {len(rows)} forms. A form is <b>new</b> when no smaller form has its value; <b>reduces</b> when one does; <b>undefined</b> when it contains <code>[□]</code>; <b>excluded</b> when it contains <code>&lt;□&gt;</code>.</p>
  <h4>Open forms</h4>{open_forms}
  <details><summary>All {len(rows)} forms</summary><div class="tw census"><table><thead><tr><th>size</th><th>form</th><th>class</th><th>value</th><th>read by</th></tr></thead><tbody>{census_rows}</tbody></table></div></details>
</section>
<div class="foot">Generated {date.today().isoformat()} by <code>tools/build.py</code> from <code>nodes/*.md</code>; verified by <code>tools/check.py</code>. Decisions in <code>LEGISLATION.md</code>; model in <code>SPEC.md</code>.</div>
</div>
<script>
(function(){{
  var q=document.getElementById('q');
  if(q){{ q.addEventListener('input',function(){{
    var v=q.value.trim().toLowerCase();
    document.querySelectorAll('article.node').forEach(function(a){{
      var hit=!v || (a.getAttribute('data-search')+' '+a.textContent).toLowerCase().indexOf(v)>=0;
      a.classList.toggle('hidden-by-search',!hit);
    }});
  }}); }}
  var wrap=document.getElementById('dagwrap'); var dragging=false, sx=0, sy=0, sl=0, st=0;
  if(wrap){{
    wrap.addEventListener('mousedown',function(e){{ dragging=true; sx=e.clientX; sy=e.clientY; sl=wrap.scrollLeft; st=wrap.scrollTop; }});
    window.addEventListener('mousemove',function(e){{ if(!dragging) return; wrap.scrollLeft=sl-(e.clientX-sx); wrap.scrollTop=st-(e.clientY-sy); }});
    window.addEventListener('mouseup',function(){{ dragging=false; }});
    var edges=document.querySelectorAll('#dag .edge');
    document.querySelectorAll('#dag .gn').forEach(function(g){{
      var id=g.getAttribute('data-id');
      g.addEventListener('mouseenter',function(){{ edges.forEach(function(e){{ if(e.getAttribute('data-from')===id||e.getAttribute('data-to')===id) e.classList.add('hl'); }}); }});
      g.addEventListener('mouseleave',function(){{ edges.forEach(function(e){{ e.classList.remove('hl'); }}); }});
      g.addEventListener('click',function(){{ var t=document.getElementById(id); if(t){{ t.querySelector('details.deriv').open=true; }} }});
    }});
  }}
}})();
</script>
'''
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(page)
    print(f"wrote {OUT} ({os.path.getsize(OUT)//1024} KB): {len(nodes)} nodes, {len(rungs)} rungs")


if __name__ == "__main__":
    main()
