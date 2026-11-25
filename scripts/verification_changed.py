#!/usr/bin/env python3
"""Compare the post-verify dataset to git HEAD and decide whether to publish.

Exit codes:
  0  substantive change (status, link results, package version, license, tool
     set, …): publish.
  1  only volatile churn (checked_at timestamps, star counts, last-commit dates,
     rechecked/retry/first_status flags, the daily tick of "No commits for N
     days" text): skip commit and deploy.
  2  the comparison itself failed (crash, malformed JSON): do not publish. The
     workflow fails the run, commits nothing and deploys nothing, so the last
     published state stays live.

Derived files (awesome/, public/og, verification-report.md) are not compared;
they would also move when only checked_at changes. History and changelog are
weekly artifacts and are not used for this decision.
"""
from __future__ import annotations

import json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VOLATILE_KEYS = frozenset({
    "checked_at",
    "stars",
    "collection_stars",
    "last_commit",
    "last_commit_days",
    "rechecked",
    "retry",
    "first_status",
})
AGE_ISSUE = re.compile(r"No commits for \d+ days")
EXIT_PUBLISH, EXIT_SKIP, EXIT_ERROR = 0, 1, 2
PATHS = ("data/tools.json", "data/verification-report.json")


def normalize(obj):
    """Drop volatile fields and stabilize commit-age issue wording."""
    if isinstance(obj, dict):
        return {k: normalize(v) for k, v in obj.items() if k not in VOLATILE_KEYS}
    if isinstance(obj, list):
        return [normalize(x) for x in obj]
    if isinstance(obj, str):
        return AGE_ISSUE.sub("No commits for N days", obj)
    return obj


def substantive_change(old_tools, old_report, new_tools, new_report) -> bool:
    """True when the published dataset would change for a reason other than churn."""
    return normalize({"tools": old_tools, "report": old_report}) != normalize(
        {"tools": new_tools, "report": new_report}
    )


def _load_work(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return json.load(f)


def _load_head(path, ref="HEAD"):
    try:
        raw = subprocess.check_output(
            ["git", "show", f"{ref}:{path}"], cwd=ROOT, stderr=subprocess.DEVNULL
        )
    except subprocess.CalledProcessError:
        return None
    return json.loads(raw.decode("utf-8"))


def main(argv=None):
    try:
        old_tools, old_report = (_load_head(p) for p in PATHS)
        if old_tools is None or old_report is None:
            print("substantive verification change: no HEAD baseline for data files")
            return 0
        new_tools, new_report = (_load_work(p) for p in PATHS)
        if substantive_change(old_tools, old_report, new_tools, new_report):
            print("substantive verification change")
            return 0
        print("no substantive change (checked_at / stars / last_commit only, or identical)")
        return 1
    except Exception as e:           # fail closed: when unsure, keep the last published state
        print(f"verification_changed: cannot compare ({type(e).__name__}: {e}); not publishing")
        return EXIT_ERROR


if __name__ == "__main__":
    sys.exit(main())
