"""Public/internal split in scripts/verify.py: three public statuses, no notes in public files."""
import importlib.util, json, os, tempfile, unittest
from unittest.mock import patch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("verify_public", os.path.join(ROOT, "scripts/verify.py"))
V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)


def tool(status, **kw):
    v = {"checked_at": "2026-11-25", "status": status,
         "checks": [{"check": "homepage alive", "ok": False, "result": "gated", "note": "403: answered but refused our checker"}],
         "issues": ["Could not confirm: homepage 403"], "homepage": {"url": "https://x", "status": 403, "result": "gated"},
         "github": {"reachable": True, "stars": 5, "last_commit": "2026-11-01T00:00:00Z", "cross_org_redirect": "a/b"},
         "last_commit_days": 24}
    v.update(kw.pop("v", {}))
    t = {"id": "x", "name": "X", "type": "mcp", "category": "crypto", "verification": v}
    t.update(kw)
    return t


class PublicStatus(unittest.TestCase):
    def test_mapping(self):
        for internal, pub in [("verified", "verified"), ("unconfirmed", "under_review"), ("warning", "under_review"),
                              ("aging", "not_verified"), ("stale", "not_verified"), ("archived", "not_verified"),
                              ("unreachable", "not_verified"), ("under_review", "under_review"), ("not_verified", "not_verified")]:
            self.assertEqual(V.public_status(tool(internal)), pub, internal)
        self.assertEqual(V.public_status(tool("verified", risk_tier="high")), "not_verified")

    def test_public_tool_strips_notes(self):
        t = tool("unconfirmed", install_note="unmaintained", remote_mcp_url_note="returns 404",
                 v={"manual_check": {"date": "2026-11-11", "note": "free text"}, "manual_override": True,
                    "issues": ["npm name 'foo' exists on the registry but does not link to this repo (not counted)"]})
        p = V.public_tool(t)
        s = json.dumps(p)
        for bad in ("refused", "403", "Could not confirm", "manual", "install_note", "remote_mcp_url_note", "cross_org_redirect", "issues", "note"):
            self.assertNotIn(bad, s, bad)
        self.assertEqual(p["verification"]["status"], "under_review")
        self.assertEqual(p["verification"]["checks"], [{"check": "homepage alive", "ok": False}])
        self.assertEqual(p["verification"]["registry_unlinked"], [{"registry": "npm", "name": "foo"}])

    def test_change_lines_public_labels_only(self):
        prev = {"a": {"name": "A", "status": "aging"}, "b": {"name": "B", "status": "unconfirmed"}, "c": {"name": "C", "status": "verified"}}
        snap = {"a": {"name": "A", "status": "stale"}, "b": {"name": "B", "status": "verified"}, "c": {"name": "C", "status": "warning"}}
        lines = [c["text"] for c in V.change_lines(prev, snap) if c["kind"] == "status"]
        self.assertEqual(sorted(lines), ["B: Under review → Verified", "C: Verified → Under review"])
        self.assertEqual(V.change_lines(None, snap)[0]["text"], "Directory published with 3 tools.")

    def test_write_outputs_keeps_report_md_internal(self):
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(os.path.join(d, "data"))
            internal = os.path.join(d, "internal")
            with patch.object(V, "ROOT", d), patch.object(V, "INTERNAL_DIR", internal):
                V.write_outputs([tool("unconfirmed")])
            self.assertFalse(os.path.exists(os.path.join(d, "data/verification-report.md")))
            self.assertTrue(os.path.exists(os.path.join(internal, "verification-report.md")))
            rep = json.load(open(os.path.join(d, "data/verification-report.json")))
            self.assertEqual(rep["by_status"], {"under_review": 1})
            pub = open(os.path.join(d, "data/tools.json")).read()
            self.assertNotIn("refused", pub); self.assertNotIn("403", pub)


if __name__ == "__main__": unittest.main()
