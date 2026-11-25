"""Additional daily-verify tests for volatile flags and VERIFY_SNAPSHOT.
New file (does not edit tests/test_daily_verify.py or other existing tests)."""
from __future__ import annotations

import os
import tempfile
import unittest
from unittest.mock import patch

import importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


V = _load("verify_daily_failsafe", "scripts/verify.py")
C = _load("verification_changed_failsafe", "scripts/verification_changed.py")


def _tool(status="verified", checked_at="2026-11-18", **extra):
    ver = {
        "checked_at": checked_at,
        "status": status,
        "issues": extra.pop("issues", []),
        "checks": extra.pop("checks", [{"check": "repo reachable", "ok": True}]),
        "github": extra.pop(
            "github",
            {
                "reachable": True,
                "stars": 10,
                "last_commit": "2026-11-01T00:00:00Z",
                "license": "MIT",
            },
        ),
    }
    ver.update(extra.pop("verification", {}))
    t = {"id": extra.pop("id", "demo"), "name": extra.pop("name", "Demo"), "verification": ver}
    t.update(extra)
    return t


def _report(checked_at="2026-11-18T15:35:02+00:00", **kw):
    r = {"checked_at": checked_at, "total": 1, "by_status": {"verified": 1}, "issues": [], "with_package": 0}
    r.update(kw)
    return r


class VolatileFlags(unittest.TestCase):
    def test_rechecked_retry_first_status_are_ignored(self):
        old = _tool(verification={"rechecked": True, "retry": 1, "first_status": "warning"})
        new = _tool(verification={"rechecked": None, "retry": 2, "first_status": "verified"})
        self.assertFalse(C.substantive_change([old], _report(), [new], _report()))

    def test_status_still_counts_when_volatile_flags_also_flip(self):
        old = _tool(status="verified", verification={"rechecked": True, "retry": 1, "first_status": "verified"})
        new = _tool(
            status="warning",
            issues=["homepage failed"],
            verification={"rechecked": None, "retry": 2, "first_status": "warning"},
        )
        self.assertTrue(C.substantive_change([old], _report(), [new], _report()))


class WriteHistorySnapshot(unittest.TestCase):
    def test_verify_snapshot_0_writes_no_history(self):
        with tempfile.TemporaryDirectory() as td:
            hist = os.path.join(td, "data", "history")
            os.makedirs(hist)
            changelog = os.path.join(td, "data", "changelog.json")
            prior = os.path.join(hist, "2026-11-18.json")
            with open(prior, "w", encoding="utf-8") as f:
                f.write("{}")
            with open(changelog, "w", encoding="utf-8") as f:
                f.write("[]")
            before_hist = sorted(os.listdir(hist))
            with open(changelog, encoding="utf-8") as f:
                before_ch = f.read()
            tools = [
                {
                    "id": "demo",
                    "name": "Demo",
                    "verification": {"status": "verified", "github": {"stars": 1}},
                }
            ]
            with patch.object(V, "ROOT", td), patch.dict(os.environ, {"VERIFY_SNAPSHOT": "0"}):
                V.write_history(tools)
            self.assertEqual(sorted(os.listdir(hist)), before_hist)
            with open(changelog, encoding="utf-8") as f:
                self.assertEqual(f.read(), before_ch)
            with open(prior, encoding="utf-8") as f:
                self.assertEqual(f.read(), "{}")


if __name__ == "__main__":
    unittest.main()
