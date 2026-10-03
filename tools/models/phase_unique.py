"""Witness for C.phase-unique — every form that uses each of the three boundaries exactly once (16 forms: the six
nestings, the three 'one around two', the six 'one around one beside the third', and the three side by side).
Evaluates all of them in the ℂ reading and exits 0 iff [<()>] is the only one that is neither void, nor the black
hole, nor excluded/undefined — James's 'unique stable configuration that uses each of the three boundaries exactly
once'. This is a census of one shape, not a proof of irreducibility (that is mult.consistency's job).
"""
import os, sys, math, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import forms as F

K = {"r": ("(", ")"), "s": ("[", "]"), "a": ("<", ">")}
def wrap(k, inner=""):
    return K[k][0] + inner + K[k][1]

shapes = set()
for a, b, c in itertools.permutations("rsa"):
    shapes.add(wrap(a, wrap(b, wrap(c))))            # nesting a(b(c))
    shapes.add(wrap(a, wrap(b) + " " + wrap(c)))      # a(b c)
    shapes.add(wrap(a, wrap(b)) + " " + wrap(c))      # a(b) c
shapes.add("() [] <>")
forms = sorted({F.to_string(F.parse(s)) for s in shapes})
assert len(forms) == 16, forms

void, hole, excluded, survivors, report = [], [], [], [], []
for s in forms:
    f = F.parse(s)
    try:
        v = F.evaluate(f)
    except F.Excluded:
        excluded.append(s); report.append(f"{s:12} excluded (<□>)"); continue
    except F.Undefined:
        excluded.append(s); report.append(f"{s:12} undefined ([□])"); continue
    if v is F.BH:
        hole.append(s); report.append(f"{s:12} = □"); continue
    report.append(f"{s:12} = {F.fmt(v)}")
    (void if abs(v) < 1e-12 else survivors).append(s)

fails = []
if survivors != ["[<()>]"]:
    fails.append(f"expected [<()>] as the only survivor, got {survivors}")
if not F.equal(F.evaluate(F.parse("[<()>]")), 1j * math.pi):
    fails.append("[<()>] is not iπ")
if (len(void), len(hole), len(excluded)) != (8, 4, 3):
    fails.append(f"expected 8 void, 4 black hole, 3 excluded among the sixteen; got {len(void)}, {len(hole)}, {len(excluded)}")
six = ["([<>])", "[(<>)]", "<([])>", "<[()]>", "(<[]>)", "[<()>]"]
six_void = [s for s in six if F.to_string(F.parse(s)) in void]
if len(six_void) != 4 or F.to_string(F.parse("(<[]>)")) not in excluded:
    fails.append(f"the six nestings: expected four void and (<[]>) excluded; void = {six_void}")
print("\n".join(report))
print(f"{len(forms)} forms: {len(void)} void, {len(hole)} black hole, {len(excluded)} excluded/undefined, {len(survivors)} survivor(s)")
if fails:
    print("FAIL"); print("\n".join(fails)); sys.exit(1)
print("OK: J = [<()>] = iπ is the only survivor")
