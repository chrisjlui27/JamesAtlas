"""nodes.py — load node files (front matter + sections) for check.py and build.py.

Front matter is a small YAML subset: `key: value`, quoted strings, inline lists `[a, b]`,
booleans, integers, and one level of nested maps written as indented `key: value` lines.
Body sections are introduced by `## ` headings.  Derivation tables are Markdown pipe tables.
"""
from __future__ import annotations
import os
import re
from dataclasses import dataclass, field

LINK = re.compile(r"\[\[([A-Za-z0-9]+\.[A-Za-z0-9-]+)\]\]")

TYPES = {"primitive", "axiom", "definition", "theorem", "decree", "import", "gap", "schema"}
LEVELS = {"object", "meta"}
STATUS = {"NATIVE", "NATIVE-BY-DECREE", "NATIVE-BY-SCHEMA", "IMPORTED", "ANALOGY", "CONJECTURE", "REFUTED", "ABSENT"}
VERIFIED = ["none", "hand", "engine", "numeric", "lean"]
GUIDE = {"shape-led", "need-led"}
HOLDS = {"holds", "holds-mod-Λ", "guarded", "replaced", "fails", "untested"}
READING_CELLS = {"EXACT", "PARTIAL", "ANALOGY", "ABSENT", "CONVERSE", "untested"}
EQUALITIES = {"≐", "≡", "≃", "≈"}
DOMAINS = {"natural", "positive", "negative", "real", "complex", "unit", "slice"}   # unit: a unit of the place (rung `place`; at ∞, a nonzero real); slice: co-sliced quaternions (rung `H`; in ℂ, complex)
SECTIONS = ["Law", "Plain", "Derivation", "Confirms", "Settings and readings", "Refuted readings", "Notes", "Plan"]
RUNGS = ["void", "N", "Z", "mult", "Q", "alg", "C", "schema", "J1", "place", "H", "analysis", "J2", "logic", "struct", "F1", "O", "S", "field"]


@dataclass
class Node:
    id: str
    path: str
    meta: dict
    sections: dict
    body: str
    derivations: list = field(default_factory=list)   # list of tables; each table is a list of (form, rules_text, note)

    def get(self, k, default=None):
        return self.meta.get(k, default)


def _scalar(v: str):
    v = v.strip()
    if v == "":
        return ""
    if v.startswith('"') and v.endswith('"') and len(v) >= 2:
        return v[1:-1]
    if v.startswith("'") and v.endswith("'") and len(v) >= 2:
        return v[1:-1]
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        if not inner:
            return []
        return [_scalar(x) for x in _split_commas(inner)]
    if v in ("true", "True"):
        return True
    if v in ("false", "False"):
        return False
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    return v


def _split_commas(s: str):
    out, cur, depth, quote = [], "", 0, None
    for ch in s:
        if quote:
            cur += ch
            if ch == quote:
                quote = None
            continue
        if ch in "\"'" and not cur.strip():
            quote = ch  # a quote opens an item only at its start: James's, Euler's stay plain text
            cur += ch
        elif ch == "[":
            depth += 1
            cur += ch
        elif ch == "]":
            depth -= 1
            cur += ch
        elif ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    return out


def parse_front_matter(text: str):
    if not text.startswith("---"):
        raise ValueError("missing front matter")
    end = text.find("\n---", 3)
    if end < 0:
        raise ValueError("unterminated front matter")
    fm = text[3:end].strip("\n")
    body = text[end + 4:]
    meta = {}
    lines = fm.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue
        if line.startswith(" "):
            raise ValueError(f"unexpected indentation: {line!r}")
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.split(" #")[0] if not val.strip().startswith('"') else val
        if val.strip() == "" and i + 1 < len(lines) and lines[i + 1].startswith(" "):
            sub = {}
            i += 1
            while i < len(lines) and lines[i].startswith(" "):
                sl = lines[i].strip()
                if sl and not sl.startswith("#"):
                    k2, _, v2 = sl.partition(":")
                    sub[k2.strip()] = _scalar(v2.split(" #")[0])
                i += 1
            meta[key] = sub
            continue
        meta[key] = _scalar(val)
        i += 1
    return meta, body


def parse_sections(body: str) -> dict:
    sections = {}
    current = "_preamble"
    buf = []
    for line in body.split("\n"):
        m = re.match(r"^##\s+(.*?)\s*$", line)
        if m:
            sections[current] = "\n".join(buf).strip()
            current = m.group(1)
            buf = []
        else:
            buf.append(line)
    sections[current] = "\n".join(buf).strip()
    return sections


def parse_tables(text: str):
    """Return a list of tables; each table a list of rows (list of cells)."""
    tables, cur = [], []
    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                continue  # separator
            cur.append(cells)
        else:
            if cur:
                tables.append(cur)
                cur = []
    if cur:
        tables.append(cur)
    return tables


def derivation_tables(node: "Node"):
    text = node.sections.get("Derivation", "")
    out = []
    for t in parse_tables(text):
        if not t:
            continue
        header = [c.lower() for c in t[0]]
        rows = t[1:] if header and header[0] in ("form", "statement") else t
        table = []
        for r in rows:
            form = r[0] if len(r) > 0 else ""
            rules = r[1] if len(r) > 1 else ""
            note = r[2] if len(r) > 2 else ""
            table.append((form.strip("`").strip(), rules, note))
        out.append(table)
    return out


def cited_ids(node: "Node") -> set:
    ids = set()
    for table in node.derivations:
        for _, rules, _ in table:
            ids |= set(LINK.findall(rules))
    return ids


def load_nodes(nodes_dir: str) -> dict:
    nodes = {}
    for fn in sorted(os.listdir(nodes_dir)):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(nodes_dir, fn)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        meta, body = parse_front_matter(text)
        node = Node(id=meta.get("id", fn[:-3]), path=path, meta=meta, sections=parse_sections(body), body=body)
        node.derivations = derivation_tables(node)
        nodes[node.id] = node
    return nodes


def load_concepts(concepts_dir: str) -> dict:
    out = {}
    if not os.path.isdir(concepts_dir):
        return out
    for fn in sorted(os.listdir(concepts_dir)):
        if fn.endswith(".md"):
            with open(os.path.join(concepts_dir, fn), encoding="utf-8") as f:
                text = f.read()
            try:
                meta, body = parse_front_matter(text)
            except ValueError:
                meta, body = {}, text
            out[fn[:-3]] = {"meta": meta, "body": body.strip()}
    return out
