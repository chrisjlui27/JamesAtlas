"""schema.py — template expansion for schema nodes (SPEC §2.7, LEGISLATION 29).

A schema law is written with count parameters:
    X^{e}            e juxtaposed copies of X (X a variable, o, J, □, or a bracketed group); e an expression in n, k
    Σ{k=a..b: F}     the juxtaposition of F for k = a..b, with {k}-expressions inside F
Instances are plain canonical strings, which the engine checks like any object law.

No dependencies beyond the standard library.
"""
from __future__ import annotations
import re

_EXPR_OK = re.compile(r"^[0-9nkj+\-*/ ()]+$")


def eval_expr(expr: str, env: dict) -> int:
    expr = expr.strip()
    if not _EXPR_OK.match(expr):
        raise ValueError(f"bad schema expression {expr!r}")
    expr = re.sub(r"(\d)([nkj])", r"\1*\2", expr)  # 2k, 3n → 2*k, 3*n
    v = eval(expr, {"__builtins__": {}}, dict(env))  # noqa: S307 — digits, n, k and arithmetic only
    if int(v) != v:
        raise ValueError(f"schema expression {expr!r} is not an integer at {env}")
    return int(v)


def _matching_open(s: str, j: int) -> int:
    closer = s[j]
    opener = {")": "(", "]": "[", ">": "<", "}": "{"}[closer]
    depth = 0
    i = j
    while i >= 0:
        if s[i] == closer:
            depth += 1
        elif s[i] == opener:
            depth -= 1
            if depth == 0:
                return i
        i -= 1
    raise ValueError(f"unbalanced {closer!r} in {s!r}")


def expand(template: str, env: dict) -> str:
    """Expand one template string at the given parameter values."""
    s = template
    # 1. sums Σ{k=a..b: F} — innermost first by repeated search
    while True:
        m = re.search(r"Σ\{(\w)=([^.:{}]+)\.\.([^:{}]+):", s)
        if not m:
            break
        start, i, depth = m.start(), m.end(), 1
        while i < len(s) and depth:
            if s[i] == "{":
                depth += 1
            elif s[i] == "}":
                depth -= 1
            i += 1
        if depth:
            raise ValueError(f"unclosed Σ in {template!r}")
        body = s[m.end():i - 1]
        var, a, b = m.group(1), eval_expr(m.group(2), env), eval_expr(m.group(3), env)
        parts = []
        for v in range(a, b + 1):
            e2 = dict(env)
            e2[var] = v
            parts.append(expand(body, e2))
        s = s[:start] + " ".join(p for p in parts if p) + s[i:]
    # 2. repetitions X^{e}
    while True:
        m = re.search(r"\^\{([^{}]*)\}", s)
        if not m:
            break
        count = eval_expr(m.group(1), env)
        j = m.start() - 1
        if j < 0:
            raise ValueError(f"^ with nothing before it in {template!r}")
        if s[j] in ")]>":
            xstart = _matching_open(s, j)
        else:
            i = j
            while i >= 0 and (s[i].isalnum() or s[i] == "□"):
                i -= 1
            xstart = i + 1
        x = s[xstart:j + 1]
        if not x:
            raise ValueError(f"^ with nothing before it in {template!r}")
        rep = " ".join([x] * count) if count > 0 else ""
        s = s[:xstart] + rep + s[m.end():]
    # 3. bare {e} counts (used inside Σ bodies for numerals written as o^{k} — nothing left to do) and tidy
    return re.sub(r"\s+", " ", s).strip()


def parse_range(spec: str):
    """'n=2..8' or 'n=2..7; k=1..n-1' -> list of {n:..., k:...} environments."""
    clauses = [c.strip() for c in str(spec).split(";") if c.strip()]
    envs = [{}]
    for c in clauses:
        m = re.match(r"^(\w)\s*=\s*([^.]+)\.\.(.+)$", c)
        if not m:
            raise ValueError(f"bad schema_range clause {c!r}")
        var, a, b = m.group(1), m.group(2), m.group(3)
        new = []
        for env in envs:
            lo, hi = eval_expr(a, env), eval_expr(b, env)
            for v in range(lo, hi + 1):
                e2 = dict(env)
                e2[var] = v
                new.append(e2)
        envs = new
    return envs


_FIXED = re.compile(r"^\|\s*form\s*\((\w)\s*=\s*(\d+)\)\s*\|", re.I)


def expand_derivation(text: str, env: dict, keep_fixed: str = "match", captions: bool = False) -> str:
    """Expand a Derivation section. Tables whose header is `| form (n = 1) | ... |` are base cases:
    with keep_fixed='match' they are kept (expanded at their own value) only when env matches, with
    'all' they are always kept at their own value, with 'none' they are dropped. With captions=True
    (the card) each table is preceded by a line saying what it is and at which values it is drawn."""
    out, cur_env, in_table, drop = [], dict(env), False, False
    has_base = any(_FIXED.match(l.strip()) for l in text.split("\n"))
    for line in text.split("\n"):
        stripped = line.strip()
        m = _FIXED.match(stripped)
        if m:
            var, val = m.group(1), int(m.group(2))
            in_table = True
            if keep_fixed == "none" or (keep_fixed == "match" and env.get(var) != val):
                drop = True
                continue
            cur_env = dict(env)
            cur_env[var] = val
            drop = False
            if captions:
                out.append(f"*Base case, {var} = {val}.*")
            out.append(re.sub(r"\(\w\s*=\s*\d+\)", "", line, count=1).replace("| form  |", "| form |"))
            continue
        if stripped.startswith("|"):
            if not in_table:
                in_table, cur_env, drop = True, dict(env), False
                if captions:
                    out.append(f"*{'Induction step' if has_base else 'The derivation'}, drawn at {describe(env)}; the engine checks it at every value in the range.*")
            if drop:
                continue
            out.append(expand_row(line, cur_env))
            continue
        in_table, drop, cur_env = False, False, dict(env)
        out.append(line)  # prose keeps its template notation (a^{n−1} in a note is not a form)
    return "\n".join(out)


def expand_row(line: str, env: dict) -> str:
    """Expand only the form cell (the first cell) of a derivation-table row; rule and note cells are
    prose and may mention n − 1, ω^{n+1} and the like, which are not schema expressions."""
    cells = line.split("|")
    if len(cells) < 3:
        return line
    cells[1] = " " + expand(cells[1], env) + " "
    return "|".join(cells)


def describe(env: dict) -> str:
    return ", ".join(f"{k} = {v}" for k, v in sorted(env.items()))


if __name__ == "__main__":
    tests = [
        ("A^{n} ≐ ([A] [o^{n}])", {"n": 3}),
        ("([(([J] [o^{2k}] <[o^{n}]>))]^{n}) ≐ o", {"n": 3, "k": 1}),
        ("Σ{k=1..n: (([J] [o^{2k}] <[o^{n}]>))} ≐ void", {"n": 3}),
        ("(A J^{2n}) ≐ (A)", {"n": 2}),
        ("A^{n-1} A", {"n": 4}),
    ]
    for t, e in tests:
        print(f"{t!r:55} @ {e} -> {expand(t, e)}")
    print(parse_range("n=2..4; k=1..n-1"))
