#!/usr/bin/env python3
"""check_progress.py — run the chart's tools/check.py exactly as it is, and say where it has got to.

tools/check.py is silent until it finishes (several minutes for a full run). This wrapper imports it,
wraps a few of its steps so that each announces itself, and then calls its own main() with the same
arguments: what it prints on stdout, what it writes and its exit code are unchanged. The announcements
go to stderr as lines beginning "@@atlas " followed by JSON, which the app reads and does not show.

If the chart's check.py has changed shape and a step is no longer where this expects it, that step is
simply not announced; the check itself always runs.

Usage: python3 check_progress.py <chart folder> [check.py arguments…]
"""
from __future__ import annotations

import json
import os
import runpy
import sys
import time


def emit(**event):
    try:
        sys.stderr.write("@@atlas " + json.dumps(event, ensure_ascii=True) + "\n")
        sys.stderr.flush()
    except Exception:
        pass


def wrap(owner, name, before=None, after=None):
    fn = getattr(owner, name, None)
    if not callable(fn):
        return False

    def wrapped(*a, **k):
        if before:
            try:
                before(*a, **k)
            except Exception:
                pass
        out = fn(*a, **k)
        if after:
            try:
                after(*a, **k)
            except Exception:
                pass
        return out

    setattr(owner, name, wrapped)
    return True


def main():
    if len(sys.argv) < 2:
        print("usage: check_progress.py <chart folder> [check.py arguments…]", file=sys.stderr)
        return 2
    root = os.path.abspath(sys.argv[1])
    argv = sys.argv[2:]
    tools = os.path.join(root, "tools")
    script = os.path.join(tools, "check.py")
    sys.path.insert(0, tools)
    only = None
    if "--only" in argv:
        i = argv.index("--only")
        only = argv[i + 1] if i + 1 < len(argv) else None
    started = time.time()

    try:
        import check  # the chart's engine
    except Exception:
        # it cannot even be imported this way: run it as a script, unannounced
        sys.argv = [script] + argv
        runpy.run_path(script, run_name="__main__")
        return 0

    state = {"done": 0, "total": None, "witnesses": 0, "witness_total": None, "phase": None}

    def phase(name, **extra):
        if state["phase"] != name:
            state["phase"] = name
            emit(event="phase", name=name, seconds=round(time.time() - started, 1), **extra)

    def on_orders(nodes, rep):
        ids = [nid for nid in nodes if not only or nid.startswith(only)]
        state["total"] = len(ids)
        state["witness_total"] = sum(1 for nid in ids if nodes[nid].get("witness"))
        emit(event="start", total=state["total"], witnesses=state["witness_total"], only=only)

    def on_node(node, nodes, rep):
        phase("laws")
        state["done"] += 1
        emit(event="node", id=node.id, done=state["done"], total=state["total"])

    def on_witness(node, rep):
        if not node.get("witness"):
            return
        phase("witnesses")
        state["witnesses"] += 1
        emit(event="witness", id=node.id, done=state["witnesses"], total=state["witness_total"])

    wrap(check, "check_orders", before=on_orders)
    wrap(check, "check_schema", before=on_node)
    wrap(check, "check_witness", before=on_witness)
    wrap(check, "write_j1_ledger", before=lambda *a, **k: phase("j1-ledger"))
    wrap(check, "check_census", before=lambda *a, **k: phase("census"))
    for mod, name, label in (("PLG", "compute", "place-ledger"), ("HLG", "compute", "h-ledger"), ("HLG", "compute_places", "h-place-ledger")):
        owner = getattr(check, mod, None)
        if owner is not None:
            wrap(owner, name, before=lambda *a, _l=label, **k: phase(_l))

    sys.argv = [script] + argv
    code = check.main(argv)
    emit(event="end", code=code, seconds=round(time.time() - started, 1))
    return code


if __name__ == "__main__":
    sys.exit(main())
