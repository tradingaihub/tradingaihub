#!/usr/bin/env python3
"""Compare the post-verify dataset to git HEAD and decide whether to publish.

Exit 0 if there is a substantive change (status, notes, link failures, package
version, license, tool set, …). Exit 1 if the only differences are volatile
churn: checked_at timestamps, star counts, last-commit dates, or the daily
tick of "No commits for N days" issue text.

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
})
AGE_ISSUE = re.compile(r"No commits for \d+ days")
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


if __name__ == "__main__":
    sys.exit(main())
