"""Tests for daily-verify helpers: snapshot gating and substantive-change detection.
New file (does not edit tests/test_verify.py). Run via npm run test:verify."""
import importlib.util, os, sys, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

V = _load("verify_daily", "scripts/verify.py")
C = _load("verification_changed", "scripts/verification_changed.py")


def _tool(status="verified", checked_at="2026-11-18", **extra):
    ver = {
        "checked_at": checked_at,
        "status": status,
        "issues": extra.pop("issues", []),
        "checks": extra.pop("checks", [{"check": "repo reachable", "ok": True}]),
        "github": extra.pop("github", {"reachable": True, "stars": 10, "last_commit": "2026-11-01T00:00:00Z", "license": "MIT"}),
    }
    ver.update(extra.pop("verification", {}))
    t = {"id": extra.pop("id", "demo"), "name": extra.pop("name", "Demo"), "verification": ver}
    t.update(extra)
    return t


def _report(checked_at="2026-11-18T15:35:02+00:00", **kw):
    r = {"checked_at": checked_at, "total": 1, "by_status": {"verified": 1}, "issues": [], "with_package": 0}
    r.update(kw)
    return r


class SnapshotGate(unittest.TestCase):
    def test_unset_defaults_to_write(self):
        self.assertTrue(V.should_write_snapshot({}))
        self.assertTrue(V.should_write_snapshot({"OTHER": "1"}))
        self.assertTrue(V.should_write_snapshot({"VERIFY_SNAPSHOT": ""}))
        self.assertTrue(V.should_write_snapshot({"VERIFY_SNAPSHOT": "  "}))

    def test_truthy_writes(self):
        for v in ("1", "true", "TRUE", "yes", "on", " Yes "):
            self.assertTrue(V.should_write_snapshot({"VERIFY_SNAPSHOT": v}), v)

    def test_falsy_skips(self):
        for v in ("0", "false", "FALSE", "no", "off", " 0 "):
            self.assertFalse(V.should_write_snapshot({"VERIFY_SNAPSHOT": v}), v)


class SubstantiveChange(unittest.TestCase):
    def _same(self, old_t, new_t, old_r=None, new_r=None, expect=False):
        old_r = old_r or _report()
        new_r = new_r or _report()
        got = C.substantive_change([old_t], old_r, [new_t], new_r)
        self.assertEqual(got, expect)

    def test_identical_is_not_a_change(self):
        t = _tool()
        self._same(t, t, expect=False)

    def test_checked_at_only_is_not_a_change(self):
        self._same(_tool(checked_at="2026-11-18"), _tool(checked_at="2026-11-20"), expect=False)
        old_r, new_r = _report(), _report(checked_at="2026-11-20T03:00:00+00:00")
        self._same(_tool(), _tool(checked_at="2026-11-20"), old_r, new_r, expect=False)

    def test_stars_and_last_commit_only_are_not_a_change(self):
        old = _tool(github={"reachable": True, "stars": 10, "last_commit": "2026-11-01T00:00:00Z", "license": "MIT"})
        new = _tool(github={"reachable": True, "stars": 12, "last_commit": "2026-11-19T00:00:00Z", "license": "MIT"})
        self._same(old, new, expect=False)

    def test_commit_age_issue_tick_is_not_a_change(self):
        old = _tool(status="aging", issues=["No commits for 200 days"])
        new = _tool(status="aging", issues=["No commits for 201 days"])
        self._same(old, new, expect=False)

    def test_status_change_is_a_change(self):
        self._same(_tool(status="verified"), _tool(status="warning", issues=["homepage failed"]), expect=True)

    def test_new_failure_is_a_change(self):
        old = _tool(status="verified")
        new = _tool(status="warning", issues=["A homepage/docs/endpoint link failed: homepage 404: not found (dead link)"])
        self._same(old, new, expect=True)

    def test_version_change_is_a_change(self):
        old = _tool(npm={"name": "demo", "version": "1.0.0"})
        new = _tool(npm={"name": "demo", "version": "1.1.0"})
        self._same(old, new, expect=True)

    def test_license_change_is_a_change(self):
        old = _tool(github={"reachable": True, "stars": 10, "last_commit": "2026-11-01T00:00:00Z", "license": "MIT"})
        new = _tool(github={"reachable": True, "stars": 10, "last_commit": "2026-11-01T00:00:00Z", "license": "Apache-2.0"})
        self._same(old, new, expect=True)

    def test_new_tool_is_a_change(self):
        self.assertTrue(C.substantive_change(
            [_tool(id="a")], _report(total=1),
            [_tool(id="a"), _tool(id="b", name="B")], _report(total=2, by_status={"verified": 2}),
        ))

    def test_cross_org_redirect_note_is_a_change(self):
        old = _tool()
        new = _tool(issues=["Repository redirects to another owner (https://github.com/other/x); stored link not updated"],
                    github={"reachable": True, "stars": 10, "last_commit": "2026-11-01T00:00:00Z", "license": "MIT",
                            "cross_org_redirect": "https://github.com/other/x"})
        self._same(old, new, expect=True)

    def test_aging_to_stale_is_a_change_even_if_age_text_normalized(self):
        old = _tool(status="aging", issues=["No commits for 365 days"])
        new = _tool(status="stale", issues=["No commits for 366 days"])
        self._same(old, new, expect=True)


if __name__ == "__main__":
    unittest.main()
