"""schema.py — template expansion for schema nodes (SPEC §2.7, LEGISLATION 29).

A schema law is written with count parameters:
    X^{e}            e juxtaposed copies of X, where X is ONE token: a variable (A, B2), o, J, □, or a bracketed
                     group ( … ) [ … ] < … >; e an expression in the parameters n, k, j (n-1, 2k, 2k+1, …)
    Σ{j=a..b: F}     the juxtaposition of F for j = a..b, with ^{…j…} counts inside F
Instances are plain canonical strings, which the engine checks like any object law.

Only canonical cells are expanded — the law and the form column of a derivation table; rule and note cells
are prose and are kept as written (SPEC §2.7). Every malformed template raises ValueError, which the engine
reports as a failure of the node rather than a crash.

No dependencies beyond the standard library.
"""
from __future__ import annotations
import re

_EXPR_OK = re.compile(r"^[0-9nkj+\-*/ ()]+$")


def eval_expr(expr: str, env: dict) -> int:
    expr = expr.strip()
    if not expr or not _EXPR_OK.match(expr):
        raise ValueError(f"bad schema expression {expr!r} (digits, n, k, j and + - * / only)")
    expr = re.sub(r"(\d)\s*([nkj])", r"\1*\2", expr)  # 2k, 3n → 2*k, 3*n
    expr = re.sub(r"([nkj])\s+([nkj0-9])", r"\1*\2", expr)  # n k → n*k
    try:
        v = eval(expr, {"__builtins__": {}}, dict(env))  # noqa: S307 — digits, n, k, j and arithmetic only
    except NameError as ex:
        raise ValueError(f"schema expression {expr!r} uses a parameter that is not bound at {env}: {ex}") from None
    except (SyntaxError, TypeError, ZeroDivisionError) as ex:
        raise ValueError(f"schema expression {expr!r} does not evaluate: {ex}") from None
    if not isinstance(v, (int, float)) or int(v) != v:
        raise ValueError(f"schema expression {expr!r} is not an integer at {env}")
    if v < 0:
        raise ValueError(f"schema expression {expr!r} is negative ({int(v)}) at {env}")
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


_SUM = re.compile(r"Σ\s*\{\s*(\w)\s*=\s*([^.:{}]+?)\s*\.\.\s*([^:{}]+?)\s*:")
_POW = re.compile(r"\^\{([^{}]*)\}")


def _base_token(s: str, j: int, template: str):
    """The one token ending at s[j] that a following ^{…} repeats: returns its start index."""
    if j < 0:
        raise ValueError(f"^ with nothing before it in {template!r}")
    c = s[j]
    if c in ")]>":
        return _matching_open(s, j)
    if c == "}":
        raise ValueError(f"chained powers X^{{a}}^{{b}} are not allowed in {template!r}; write one count")
    if c in "oJ□":
        # a bare o/J/□ — but `oo^{n}` is ambiguous (the chart writes piles as oo), so refuse a run
        if j >= 1 and (s[j - 1].isalnum() or s[j - 1] == "□"):
            raise ValueError(f"{s[max(0, j-3):j+1]!r}^{{…}} in {template!r}: the base of ^ must be one token — write o^{{2n}}, (o o)^{{n}} or a bracketed group")
        return j
    if c.isdigit() and j >= 1 and s[j - 1].isalpha() and s[j - 1].isupper():
        if j >= 2 and (s[j - 2].isalnum() or s[j - 2] == "□"):
            raise ValueError(f"{s[max(0, j-3):j+1]!r}^{{…}} in {template!r}: the base of ^ must be one token")
        return j - 1  # variable with a digit, e.g. A2
    if c.isalpha() and c.isupper():
        if j >= 1 and (s[j - 1].isalnum() or s[j - 1] == "□"):
            raise ValueError(f"{s[max(0, j-3):j+1]!r}^{{…}} in {template!r}: the base of ^ must be one token")
        return j
    raise ValueError(f"{c!r} cannot carry a count in {template!r}: the base of ^ is a variable, o, J, □ or a bracketed group")


def expand(template: str, env: dict) -> str:
    """Expand one template string at the given parameter values."""
    s = template
    # 1. sums Σ{j=a..b: F} — outermost first; the body is expanded recursively with j bound
    while True:
        m = _SUM.search(s)
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
        if b < a - 1:
            raise ValueError(f"Σ bounds reversed ({var} = {a}..{b}) in {template!r}")
        parts = []
        for v in range(a, b + 1):
            e2 = dict(env)
            e2[var] = v
            parts.append(expand(body, e2))
        s = s[:start] + " " + " ".join(p for p in parts if p) + " " + s[i:]
    if "Σ" in s:
        raise ValueError(f"malformed Σ in {template!r}: write Σ{{j=a..b: F}}")
    # 2. repetitions X^{e}
    while True:
        found = list(_POW.finditer(s))
        if not found:
            break
        m = found[-1]  # rightmost first, so a chained X^{a}^{b} is seen as such and (X^{a})^{b} nests correctly
        count = eval_expr(m.group(1), env)
        j = m.start() - 1
        while j >= 0 and s[j] == " ":
            j -= 1
        xstart = _base_token(s, j, template)
        x = s[xstart:j + 1]
        sep = "" if x == "o" else " "  # the chart writes piles as oo, ooo; everything else spaced
        rep = sep.join([x] * count) if count > 0 else ""
        s = s[:xstart] + " " + rep + " " + s[m.end():]
    if "^" in s:
        raise ValueError(f"stray ^ in {template!r}: counts are written X^{{e}}")
    # 3. tidy
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"([(\[<]) ", r"\1", s)
    s = re.sub(r" ([)\]>])", r"\1", s)
    return s


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
    if not envs:
        raise ValueError(f"schema_range {spec!r} is empty")
    return envs


_FIXED = re.compile(r"^\|\s*form\s*\((\w)\s*=\s*(\d+)\)\s*\|", re.I)


def base_values(text: str) -> dict:
    """The base-case tables of a Derivation section: {var: sorted values} from headers `| form (n = 1) | …`."""
    out = {}
    for line in text.split("\n"):
        m = _FIXED.match(line.strip())
        if m:
            out.setdefault(m.group(1), set()).add(int(m.group(2)))
    return {k: sorted(v) for k, v in out.items()}


def induction_variable(text: str, env: dict):
    """The parameter the base cases are stated in (None when the schema has no base-case table)."""
    b = base_values(text)
    if not b:
        return None
    if len(b) > 1:
        raise ValueError(f"base cases in more than one parameter: {sorted(b)}")
    var = next(iter(b))
    if var not in env:
        raise ValueError(f"base case in {var}, which schema_range does not bind")
    return var


def expand_derivation(text: str, env: dict, keep_fixed: str = "match", captions: bool = False) -> str:
    """Expand a Derivation section. Tables whose header is `| form (n = 1) | ... |` are base cases.

    keep_fixed='match' (the engine's instance): at a base value only the base-case table(s) at that value are kept
    and the step tables are dropped; at any other value the base tables are dropped and the step tables kept
    (so a `hypothesis` row always refers to a value at or above the base). 'all' keeps every table, the base
    ones at their own value (the card); 'none' drops the base tables. With captions=True each table is preceded
    by a line saying what it is and at which values it is drawn."""
    bases = base_values(text)
    var = induction_variable(text, env) if keep_fixed == "match" else (next(iter(bases)) if bases else None)
    at_base = bool(bases) and var is not None and env.get(var) in bases[var]
    if keep_fixed == "match" and bases and env.get(var) is not None and env[var] < min(bases[var]):
        raise ValueError(f"schema_range reaches {var} = {env[var]}, below the base case {var} = {min(bases[var])}")
    out, cur_env, in_table, drop = [], dict(env), False, False
    for line in text.split("\n"):
        stripped = line.strip()
        m = _FIXED.match(stripped)
        if m:
            bvar, val = m.group(1), int(m.group(2))
            in_table = True
            if keep_fixed == "none" or (keep_fixed == "match" and env.get(bvar) != val):
                drop = True
                continue
            cur_env = dict(env)
            cur_env[bvar] = val
            drop = False
            if captions:
                out.append(f"*Base case, {bvar} = {val}.*")
            out.append(re.sub(r"\(\w\s*=\s*\d+\)", "", line, count=1).replace("| form  |", "| form |"))
            continue
        if stripped.startswith("|"):
            if not in_table:
                in_table, cur_env = True, dict(env)
                drop = keep_fixed == "match" and at_base  # a step table is not an instance at the base value
                if captions and not drop:
                    out.append(f"*Induction step, drawn at {describe(env)}; the engine checks it at every value in the range above the base.*" if bases
                               else f"*The derivation, drawn at {describe(env)}; the engine checks it at every value in the range.*")
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
        ("Σ{ j = 1 .. n : (A [o^{j}]) }", {"n": 2}),
        ("(A J^{2n}) ≐ (A)", {"n": 2}),
        ("A^{n-1} A", {"n": 4}),
        ("A^{n-1} A", {"n": 1}),
        ("(A2^{n})", {"n": 2}),
        ("(o o)^{n}", {"n": 2}),
        ("(A^{n})^{2}", {"n": 2}),
    ]
    for t, e in tests:
        print(f"{t!r:55} @ {e} -> {expand(t, e)!r}")
    for bad in ["[oo^{n}]", "A^{n}^{2}", "A^{k}", "A^{n k}", "A^{()}", "A^{n-3}", "JJ^{2}", "2^{n}", "Σ{j=1..n (A)}"]:
        try:
            print(f"{bad!r:20} -> {expand(bad, {'n': 1})!r}  (should have failed)")
        except ValueError as ex:
            print(f"{bad!r:20} -> ValueError: {ex}")
    print(parse_range("n=2..4; k=1..n-1"))
