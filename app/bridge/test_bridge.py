"""Tests for atlas_bridge.py, on a scratch copy of the chart (the real one is never written).

Run from app/:  python3 -m unittest discover -s bridge -p "test_*.py" -v
The chart is the folder above app/, or ATLAS_TEST_CHART.
"""
from __future__ import annotations

import io
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import atlas_bridge as AB  # noqa: E402

CHART = os.path.abspath(os.environ.get("ATLAS_TEST_CHART") or os.path.join(HERE, "..", ".."))


def copy_chart():
    dest = tempfile.mkdtemp(prefix="atlas-test-")
    for sub in ("nodes", "tools", "census", "concepts", "site"):
        src = os.path.join(CHART, sub)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(dest, sub), ignore=shutil.ignore_patterns("__pycache__"))
    return dest


class WriteUnderstood(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp(prefix="atlas-und-")

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def write(self, name, data: bytes):
        p = os.path.join(self.dir, name)
        with open(p, "wb") as fh:
            fh.write(data)
        return p

    def read(self, p):
        with open(p, "rb") as fh:
            return fh.read()

    def test_keeps_double_quotes(self):
        p = self.write("a.md", b'---\nid: a\nunderstood: "no"\nunderstood_note: ""\n---\n\n## Law\n')
        AB.write_understood(p, "partial")
        self.assertEqual(self.read(p), b'---\nid: a\nunderstood: "partial"\nunderstood_note: ""\n---\n\n## Law\n')

    def test_keeps_bare_values(self):
        p = self.write("b.md", b'---\nid: b\nunderstood: yes\nunderstood_note: ""\n---\nbody\n')
        AB.write_understood(p, "no")
        self.assertEqual(self.read(p), b'---\nid: b\nunderstood: no\nunderstood_note: ""\n---\nbody\n')

    def test_keeps_crlf(self):
        p = self.write("c.md", b'---\r\nid: c\r\nunderstood: "no"\r\nunderstood_note: ""\r\n---\r\nbody\r\n')
        AB.write_understood(p, "yes")
        self.assertEqual(self.read(p), b'---\r\nid: c\r\nunderstood: "yes"\r\nunderstood_note: ""\r\n---\r\nbody\r\n')

    def test_body_line_untouched(self):
        p = self.write("d.md", b'---\nid: d\nunderstood: "no"\n---\nunderstood: no \xe2\x80\x94 a line in the body\n')
        AB.write_understood(p, "yes")
        self.assertEqual(self.read(p), b'---\nid: d\nunderstood: "yes"\n---\nunderstood: no \xe2\x80\x94 a line in the body\n')

    def test_inserts_when_missing(self):
        p = self.write("e.md", b'---\nid: e\ntitle: x\n---\nbody\n')
        AB.write_understood(p, "partial")
        self.assertEqual(self.read(p), b'---\nid: e\ntitle: x\nunderstood: "partial"\n---\nbody\n')

    def test_inserts_when_missing_crlf(self):
        p = self.write("f.md", b'---\r\nid: f\r\n---\r\nbody\r\n')
        AB.write_understood(p, "yes")
        self.assertEqual(self.read(p), b'---\r\nid: f\r\nunderstood: "yes"\r\n---\r\nbody\r\n')

    def test_bom_refused(self):
        p = self.write("g.md", b'\xef\xbb\xbf---\nid: g\nunderstood: no\n---\n')
        with self.assertRaises(AB.BridgeError):
            AB.write_understood(p, "yes")
        self.assertEqual(self.read(p), b'\xef\xbb\xbf---\nid: g\nunderstood: no\n---\n')

    def test_no_temp_files_left(self):
        p = self.write("h.md", b'---\nid: h\nunderstood: no\n---\n')
        AB.write_understood(p, "yes")
        self.assertEqual(sorted(os.listdir(self.dir)), ["h.md"])


class ChartTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = copy_chart()
        cls.chart = AB.Chart(cls.root)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.root, ignore_errors=True)

    def test_summary_is_the_walk(self):
        s = self.chart.summary()
        orders = [n["order"] for n in s["nodes"]]
        self.assertEqual(orders, sorted(orders))
        self.assertEqual(sum(s["understood"].values()), len(s["nodes"]))
        self.assertEqual(sum(len(r["nodes"]) for r in s["rungs"]), len(s["nodes"]))
        self.assertIn("article.node", s["css"])
        json.dumps(s)   # everything the window gets is JSON

    def test_card_is_build_py_card(self):
        c = self.chart.card("Z.collection")
        self.assertIn('id="Z.collection"', c["html"])
        self.assertIn("<svg", c["html"])

    def test_unknown_node(self):
        with self.assertRaises(AB.BridgeError):
            self.chart.card("Z.nothing-here")
        with self.assertRaises(AB.BridgeError):
            self.chart.card("../../etc/passwd")

    def test_set_understood_round_trip(self):
        nid = "N.unit"
        before = self.chart.nodes[nid].get("understood")
        r = self.chart.set_understood(nid, "partial")
        self.assertEqual(r["node"]["understood"], "partial")
        self.assertEqual(self.chart.nodes[nid].get("understood"), "partial")
        self.chart.set_understood(nid, before if before in AB.UNDERSTOOD else "no")
        with self.assertRaises(AB.BridgeError):
            self.chart.set_understood(nid, "maybe")

    def test_lists_and_graph(self):
        l = self.chart.lists()
        self.assertGreater(l["gapCount"], 0)
        self.assertIn("gapitem", l["gaps"])
        self.assertIn('<svg id="dag"', self.chart.graph()["html"])

    def test_rules_index(self):
        rules = {r["id"]: r for r in self.chart.rules_index()}
        self.assertTrue(rules["Z.collection"]["usable"])
        self.assertFalse(rules["void.space"]["usable"])          # the medium is the representation
        self.assertFalse(rules["N.induction"]["usable"])         # a gap
        self.assertEqual(rules["J1.unit"]["reading"], "J1")
        self.assertEqual(rules["H.commutation"]["reading"], "H")

    def test_inspect(self):
        r = self.chart.inspect("(([[([A] [A]) ([B] [B])]] <[oo]>))")
        self.assertEqual(r["variables"], ["A", "B"])
        self.assertIn("<svg", r["svg"])
        self.assertEqual(self.chart.inspect("(o)")["value"], "2.71828")
        self.assertEqual(self.chart.inspect("[i ; j]")["reading"], "H")   # the ordered square has its value in ℍ
        with self.assertRaises(AB.BridgeError) as cm:
            self.chart.inspect("(A [B")
        self.assertEqual(cm.exception.kind, "parse")
        with self.assertRaises(AB.BridgeError):
            self.chart.inspect("o" * (AB.MAX_FORM_CHARS + 1))

    def test_apply_collection(self):
        r = self.chart.apply("Z.collection", "<o> <o o> <A>")
        self.assertGreaterEqual(r["distinct"], 2)
        forms = {x["canonical"] for x in r["results"]}
        self.assertEqual(len(forms), len(r["results"]))              # no duplicates
        self.assertNotIn(r["from"], forms)                           # no step that changes nothing
        self.assertTrue(all(x["kept"] for x in r["results"]))        # ≐ keeps the value in ℂ

    def test_apply_unit_in_j1(self):
        r = self.chart.apply("J1.unit", "[(J J)]")
        self.assertEqual(r["reading"], "J1")
        self.assertTrue(any(x["sugar"] == "J J" for x in r["results"]))

    def test_conditional_premise(self):
        r = self.chart.apply("H.commutation", "[i ; j]")
        self.assertTrue(r["conditional"])
        self.assertTrue(any(x["premise"] is False for x in r["results"]))

    def test_place_instances_read_at_their_own_place(self):
        r = self.chart.apply("place.void-pile", "o o o o A", reading="p2")
        self.assertTrue(r["results"])
        self.assertTrue(all("p = 2" in x["instance"] for x in r["results"]))
        self.assertTrue(all(x["kept"] for x in r["results"]))

    def test_no_rule(self):
        with self.assertRaises(AB.BridgeError) as cm:
            self.chart.apply("N.induction", "o")
        self.assertEqual(cm.exception.kind, "no-rule")

    def test_match_cost_guard(self):
        F, P = self.chart.F, self.chart.P
        wide = F.parse(" ".join("ABCDEFGHIKLM"))
        three = P.Rule("t", F.parse("A B C"), F.parse("(A B C)"))
        self.assertGreater(AB.match_cost(three, wide, F), AB.MATCH_BUDGET)
        one = P.Rule("t", F.parse("<A>"), F.parse("A"))
        self.assertEqual(AB.match_cost(one, wide, F), 0)

    def test_evaluator_left_classical(self):
        self.chart.apply("J1.unit", "[(J J)]")
        self.assertIsNone(self.chart.F.OMEGA)     # a 𝕁₁ reading never leaks into the next card


class Protocol(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = copy_chart()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.root, ignore_errors=True)

    def run_lines(self, *reqs):
        inp = io.StringIO("".join(json.dumps(r) + "\n" for r in reqs))
        out = io.StringIO()
        saved = sys.stdout
        try:
            AB.serve(self.root, inp, out)
        finally:
            sys.stdout = saved
        return [json.loads(l) for l in out.getvalue().splitlines()]

    def test_replies_in_order_and_ascii(self):
        replies = self.run_lines({"id": 1, "method": "ping"}, {"id": 2, "method": "nope"},
                                 {"id": 3, "method": "instrument.inspect", "params": {"form": "(("}})
        self.assertEqual([r["id"] for r in replies], [1, 2, 3])
        self.assertTrue(replies[0]["result"]["ok"])
        self.assertEqual(replies[1]["error"]["kind"], "unknown")
        self.assertEqual(replies[2]["error"]["kind"], "parse")

    def test_bad_json_line(self):
        inp = io.StringIO("not json\n" + json.dumps({"id": 7, "method": "ping"}) + "\n")
        out = io.StringIO()
        saved = sys.stdout
        try:
            AB.serve(self.root, inp, out)
        finally:
            sys.stdout = saved
        lines = out.getvalue().splitlines()
        self.assertEqual(len(lines), 2)
        self.assertTrue(all(l.isascii() for l in lines))
        self.assertEqual(json.loads(lines[1])["id"], 7)

    def test_unreadable_node_is_named(self):
        root = copy_chart()
        try:
            p = os.path.join(root, "nodes", "N.unit.md")
            with open(p, "rb") as fh:
                data = fh.read()
            with open(p, "wb") as fh:
                fh.write(b"\xef\xbb\xbf" + data)
            with self.assertRaises(AB.BridgeError) as cm:
                AB.Chart(root)
            self.assertIn("N.unit.md", str(cm.exception))
            self.assertIn("byte-order mark", str(cm.exception))
        finally:
            shutil.rmtree(root, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
