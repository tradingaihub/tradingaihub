"""#67 fail-closed behaviour: a compare crash must not publish.
verification_changed.py exits 0 (publish), 1 (skip) or 2 (error, no commit/deploy),
and the workflow publishes only on exit 0. New file; existing tests are not edited."""
import contextlib, importlib.util, io, json, os, re, unittest
from unittest.mock import patch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("verification_changed_fc", os.path.join(ROOT, "scripts/verification_changed.py"))
C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)


def run():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = C.main()
    return rc, buf.getvalue()


class CompareErrorsDoNotPublish(unittest.TestCase):
    def test_malformed_worktree_json(self):
        with patch.object(C, "_load_head", return_value=[]), \
             patch.object(C, "_load_work", side_effect=json.JSONDecodeError("x", "{", 0)):
            rc, out = run()
        self.assertEqual(rc, 2); self.assertIn("not publishing", out)

    def test_malformed_head_blob(self):
        with patch.object(C.subprocess, "check_output", return_value=b"{not json"):
            rc, out = run()
        self.assertEqual(rc, 2); self.assertIn("JSONDecodeError", out)

    def test_comparison_error(self):
        with patch.object(C, "_load_head", return_value=[]), patch.object(C, "_load_work", return_value=[]), \
             patch.object(C, "substantive_change", side_effect=TypeError("boom")):
            rc, _ = run()
        self.assertEqual(rc, 2)

    def test_change_and_no_change_codes(self):
        with patch.object(C, "_load_head", return_value=[]), patch.object(C, "_load_work", return_value=[]):
            with patch.object(C, "substantive_change", return_value=True):
                self.assertEqual(run()[0], 0)
            with patch.object(C, "substantive_change", return_value=False):
                self.assertEqual(run()[0], 1)


class WorkflowPublishesOnlyOnZero(unittest.TestCase):
    def setUp(self):
        self.wf = open(os.path.join(ROOT, ".github/workflows/weekly.yml"), encoding="utf-8").read()

    def test_publish_only_on_exit_zero(self):
        self.assertRegex(self.wf, r'if \[ "\$rc" = 0 \]; then\s+echo "[^"]*"\s+publish=1')
        self.assertNotIn("also publishes", self.wf)

    def test_other_codes_fail_without_commit_or_deploy(self):
        m = re.search(r'else\n(.*?)\n\s+fi', self.wf.split('elif [ "$rc" = 1 ]')[1], re.S)
        branch = m.group(1)
        self.assertIn("SHOULD_DEPLOY=false", branch)
        self.assertIn("exit 1", branch)
        self.assertNotIn("publish=1", branch)
        self.assertNotIn("git commit", branch)

    def test_deploy_gated_on_should_deploy(self):
        for step in ("Deploy to Cloudflare Pages", "IndexNow"):
            block = self.wf.split(f"name: {step}")[1].split("\n      - name:")[0]
            self.assertIn("env.SHOULD_DEPLOY == 'true'", block)


if __name__ == "__main__": unittest.main()
