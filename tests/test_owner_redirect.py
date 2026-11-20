"""Tests for the reviewed repo-transfer allowlist in scripts/verify.py.
A redirect to a different owner is Needs review (unconfirmed) unless the
old-owner/repo → new-owner/repo pair is listed in data/repo-transfers.json.
Network is mocked; these tests make no live calls.
Run: python3 -m unittest tests.test_owner_redirect
"""
import importlib.util, json, os, tempfile, unittest
from unittest import mock

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("verify", os.path.join(ROOT, "scripts", "verify.py"))
V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)

OPENBB_FROM = "https://github.com/OpenBB-finance/OpenBB"
OPENBB_TO = "https://github.com/openbq-org/OpenBB"
OPENBB_ENTRY = {
    "from": "OpenBB-finance/OpenBB",
    "to": "openbq-org/OpenBB",
    "confirmed": "2026-11-20",
    "source": "https://openbb.co/blog/openbb-belongs-to-everyone/",
    "note": "OpenBB wound down; OpenBQ foundation (BrightQuery-funded) stewards the code, per founder's post.",
}

def _g(**extra):
    g = {"reachable": True, "final_url": OPENBB_TO, "archived": False, "stars": 1,
         "license": "Apache-2.0", "last_commit": "2026-11-15T00:00:00Z",
         "cross_org_redirect": OPENBB_TO}
    g.update(extra)
    return g

def _verify(t, g, transfers, age=8):
    """verify() + apply_allowed_transfer, with GitHub mocked and no network."""
    with mock.patch.object(V, "gh_info", return_value=(dict(g), g.get("final_url", "").rsplit("/", 1)[-1] and "x", "y")) as _, \
         mock.patch.object(V, "detect_packages", return_value={}), \
         mock.patch.object(V, "age_days", return_value=age):
        # gh_info return owner/name unused when packages are empty
        owner = "openbq-org" if "openbq" in (g.get("final_url") or "") else "Same"
        name = (g.get("final_url") or "https://github.com/x/y").rstrip("/").split("/")[-1]
        with mock.patch.object(V, "gh_info", return_value=(dict(g), owner, name)):
            v = V.verify(t)
    V.apply_allowed_transfer(t, v, transfers)
    return v


class OwnerRepo(unittest.TestCase):
    def test_url_and_slug(self):
        self.assertEqual(V._owner_repo("https://github.com/OpenBB-finance/OpenBB"), ("openbb-finance", "openbb"))
        self.assertEqual(V._owner_repo("OpenBB-finance/OpenBB"), ("openbb-finance", "openbb"))
        self.assertEqual(V._owner_repo("https://github.com/openbq-org/OpenBB/"), ("openbq-org", "openbb"))

    def test_rejects_junk(self):
        self.assertIsNone(V._owner_repo(""))
        self.assertIsNone(V._owner_repo(None))
        self.assertIsNone(V._owner_repo("not-a-repo"))


class FindTransfer(unittest.TestCase):
    def test_match_is_case_insensitive(self):
        e = V.find_repo_transfer(
            "https://github.com/openbb-finance/openbb",
            "https://github.com/OpenBQ-Org/openbb",
            [OPENBB_ENTRY],
        )
        self.assertIs(e, OPENBB_ENTRY)

    def test_slug_or_url(self):
        self.assertIs(V.find_repo_transfer("OpenBB-finance/OpenBB", "openbq-org/OpenBB", [OPENBB_ENTRY]), OPENBB_ENTRY)

    def test_unknown_pair_is_none(self):
        self.assertIsNone(V.find_repo_transfer(OPENBB_FROM, "https://github.com/evill-org/OpenBB", [OPENBB_ENTRY]))
        self.assertIsNone(V.find_repo_transfer("https://github.com/Other/Repo", OPENBB_TO, [OPENBB_ENTRY]))


class LoadTransfers(unittest.TestCase):
    def test_missing_file_is_empty(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(V.load_repo_transfers(os.path.join(d, "missing.json")), [])

    def test_loads_transfers_key(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "repo-transfers.json")
            with open(path, "w") as f:
                json.dump({"transfers": [OPENBB_ENTRY, {"from": "bad"}]}, f)
            rows = V.load_repo_transfers(path)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["from"], OPENBB_ENTRY["from"])


class RedirectRule(unittest.TestCase):
    def test_different_owner_not_allowlisted_is_needs_review(self):
        t = {"id": "x", "type": "mcp", "repo": OPENBB_FROM}
        v = _verify(t, _g(), transfers=[])
        self.assertEqual(v["status"], "unconfirmed")
        self.assertTrue(any("redirects to another owner" in i and "openbq-org" in i for i in v["issues"]), v["issues"])
        self.assertFalse(any("transfer confirmed" in i for i in v["issues"]))

    def test_allowlisted_is_verified_with_confirmed_note(self):
        t = {"id": "openbb", "type": "mcp", "repo": OPENBB_FROM}
        v = _verify(t, _g(), transfers=[OPENBB_ENTRY])
        self.assertEqual(v["status"], "verified")
        self.assertTrue(v.get("transfer_confirmed"))
        notes = [i for i in v["issues"] if "transfer confirmed" in i]
        self.assertEqual(len(notes), 1, v["issues"])
        self.assertIn("2026-11-20", notes[0])
        self.assertIn("https://openbb.co/blog/openbb-belongs-to-everyone/", notes[0])
        self.assertIn("OpenBB-finance/OpenBB", notes[0])
        self.assertIn("openbq-org/OpenBB", notes[0])
        self.assertFalse(any("redirects to another owner" in i for i in v["issues"]))

    def test_allowlisted_match_is_case_insensitive(self):
        t = {"id": "openbb", "type": "mcp", "repo": "https://github.com/openbb-finance/openbb"}
        g = _g(final_url="https://github.com/OpenBQ-Org/OpenBB",
               cross_org_redirect="https://github.com/OpenBQ-Org/OpenBB")
        v = _verify(t, g, transfers=[OPENBB_ENTRY])
        self.assertEqual(v["status"], "verified")
        self.assertTrue(any("transfer confirmed" in i for i in v["issues"]))

    def test_same_owner_rename_stays_verified_without_redirect_note(self):
        t = {"id": "ren", "type": "mcp", "repo": "https://github.com/Same/old"}
        g = {"reachable": True, "final_url": "https://github.com/Same/new", "archived": False,
             "stars": 1, "license": "MIT", "last_commit": "2026-11-15T00:00:00Z"}
        v = _verify(t, g, transfers=[])
        self.assertEqual(v["status"], "verified")
        self.assertEqual(v["issues"], [])
        self.assertFalse(g.get("cross_org_redirect"))

    def test_same_owner_different_case_is_not_cross_org(self):
        """Owner comparison in gh_info is case-insensitive; no cross_org_redirect is set."""
        # Drive gh_info itself with a mocked API payload — no network.
        api = {"html_url": "https://github.com/OpenBB-finance/OpenBB", "stargazers_count": 1,
               "archived": False, "pushed_at": "2026-11-15T00:00:00Z",
               "owner": {"login": "openbb-finance"}, "name": "OpenBB", "license": {"spdx_id": "Apache-2.0"}}
        with mock.patch.object(V, "api", return_value=api):
            g, owner, name = V.gh_info("https://github.com/OpenBB-finance/OpenBB")
        self.assertNotIn("cross_org_redirect", g)
        self.assertEqual((owner.lower(), name.lower()), ("openbb-finance", "openbb"))

    def test_allowlisted_aging_stays_aging(self):
        t = {"id": "openbb", "type": "mcp", "repo": OPENBB_FROM}
        v = _verify(t, _g(), transfers=[OPENBB_ENTRY], age=200)
        self.assertEqual(v["status"], "aging")
        self.assertTrue(any("transfer confirmed" in i for i in v["issues"]))
        self.assertFalse(any("redirects to another owner" in i for i in v["issues"]))

    def test_does_not_rewrite_stored_link(self):
        t = {"id": "openbb", "type": "mcp", "repo": OPENBB_FROM}
        v = _verify(t, _g(), transfers=[OPENBB_ENTRY])
        self.assertEqual(t["repo"], OPENBB_FROM)
        self.assertEqual(v["status"], "verified")


class ManualCheckDoesNotBypass(unittest.TestCase):
    def test_manual_check_does_not_verify_non_allowlisted_redirect(self):
        # Pair is not in data/repo-transfers.json (OpenBB is); a manual check must not
        # promote a typo-squat-looking redirect to Verified.
        t = {"id": "x", "type": "mcp", "repo": "https://github.com/Honest/tool",
             "manual_check": {"method": "manual", "date": V.NOW.date().isoformat()}}
        g = _g(final_url="https://github.com/evill-org/tool",
               cross_org_redirect="https://github.com/evill-org/tool")
        v = _verify(t, g, transfers=[])
        self.assertEqual(v["status"], "unconfirmed")
        self.assertFalse(v.get("manual_override"))
        self.assertTrue(any("redirects to another owner" in i and "evill-org" in i for i in v["issues"]))


class MainHonoursAllowlist(unittest.TestCase):
    """main() --dry-run with a temp ROOT: allowlisted OpenBB stays verified; stored repo kept."""

    def test_main_allowlisted_stays_verified_and_link_kept(self):
        g = _g()
        seed = [{"id": "openbb", "name": "OpenBB", "type": "mcp", "repo": OPENBB_FROM}]
        def gh(url, collection=False):
            return dict(g), "openbq-org", "OpenBB"
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(os.path.join(d, "data"))
            with open(os.path.join(d, "data", "seed.json"), "w") as f: json.dump(seed, f)
            with open(os.path.join(d, "data", "tools.json"), "w") as f: json.dump([], f)
            with open(os.path.join(d, "data", "repo-transfers.json"), "w") as f:
                json.dump({"transfers": [OPENBB_ENTRY]}, f)
            out_json = os.path.join(d, "dry.json")
            with mock.patch.object(V, "ROOT", d), mock.patch.object(V.sys, "argv", ["verify.py", "--dry-run"]), \
                 mock.patch.dict(os.environ, {"VERIFY_DRY_JSON": out_json}), \
                 mock.patch.object(V, "gh_info", side_effect=gh), \
                 mock.patch.object(V, "detect_packages", return_value={}), \
                 mock.patch.object(V, "age_days", return_value=5), \
                 mock.patch("sys.stdout"), mock.patch("sys.stderr"):
                V.main()
            with open(out_json) as f:
                out = {x["id"]: x for x in json.load(f)}
        self.assertEqual(out["openbb"]["repo"], OPENBB_FROM)
        v = out["openbb"]["verification"]
        self.assertEqual(v["status"], "verified")
        self.assertTrue(any("transfer confirmed" in i for i in v["issues"]))
        self.assertFalse(any("redirects to another owner" in i for i in v["issues"]))


if __name__ == "__main__":
    unittest.main()
