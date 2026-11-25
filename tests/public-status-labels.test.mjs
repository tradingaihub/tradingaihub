// Public outputs use only the three public statuses and carry no checker notes.
import { readFileSync, existsSync, readdirSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import assert from "node:assert/strict";
import test from "node:test";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const read = (p) => readFileSync(join(root, p), "utf8");
const PUBLIC = new Set(["verified", "under_review", "not_verified"]);
const PRIVATE_KEYS = ["issues", "note", "manual_check", "manual_override", "install_note", "remote_mcp_url_note", "cross_org_redirect", "last_commit_days"];

test("data/tools.json: public statuses only, no notes or HTTP codes", () => {
  const tools = JSON.parse(read("data/tools.json"));
  for (const t of tools) {
    assert.ok(PUBLIC.has(t.verification.status), `${t.id}: ${t.verification.status}`);
    const s = JSON.stringify(t.verification);
    for (const k of PRIVATE_KEYS) assert.ok(!s.includes(`"${k}"`), `${t.id} has ${k}`);
    for (const k of ["install_note", "remote_mcp_url_note", "manual_check"]) assert.ok(!(k in t), `${t.id} has ${k}`);
    for (const k of ["homepage", "docs", "remote_mcp"]) assert.ok(!(k in t.verification), `${t.id} verification.${k}`);
    for (const c of t.verification.checks) assert.deepEqual(Object.keys(c).sort(), ["check", "ok"], t.id);
    if (t.risk_tier === "high" || t.category === "high-risk-crypto") assert.equal(t.verification.status, "not_verified", t.id);
  }
});

test("verification report, history and changelog use public statuses only", () => {
  assert.ok(!existsSync(join(root, "data/verification-report.md")), "verification-report.md must not be committed");
  const rep = JSON.parse(read("data/verification-report.json"));
  assert.deepEqual(Object.keys(rep).sort(), ["by_status", "checked_at", "total", "with_package"]);
  for (const k of Object.keys(rep.by_status)) assert.ok(PUBLIC.has(k), k);
  for (const f of readdirSync(join(root, "data/history"))) {
    for (const s of Object.values(JSON.parse(read(`data/history/${f}`)))) assert.ok(PUBLIC.has(s.status), `${f}: ${s.status}`);
  }
  const labels = /^(Verified|Under review|Not currently verified)$/;
  for (const w of JSON.parse(read("data/changelog.json"))) {
    for (const k of Object.keys(w.counts)) assert.ok(PUBLIC.has(k), `${w.date}: ${k}`);
    for (const c of w.changes) {
      if (c.kind === "status") {
        assert.notEqual(c.from, c.to, `${w.date} ${c.id}`);
        const [, arrow] = c.text.split(/: (?=[^:]*$)/);
        for (const x of arrow.split(" → ")) assert.match(x, labels, c.text);
      }
      assert.doesNotMatch(c.text, /unconfirmed|warning|aging|stale|archived|unreachable|First verification run/i, c.text);
    }
  }
});

test("public CSV uses public statuses and a neutral source", () => {
  const csv = read("public/data/state-2026-summary.csv");
  assert.doesNotMatch(csv, /aging|stale|archived|link_check_pending|check_links|run log|not published|git history|data\//i);
  for (const line of csv.trim().split("\n").slice(1)) assert.match(line, /,TradingAIHub verification data$/, line);
});

test("i18n: three status labels in every locale, old keys removed", () => {
  const dir = join(root, "src/i18n");
  const files = readdirSync(dir).filter((f) => f.endsWith(".json"));
  assert.equal(files.length, 13);
  for (const f of files) {
    const d = JSON.parse(readFileSync(join(dir, f), "utf8"));
    assert.deepEqual(Object.keys(d.status), ["verified", "under_review", "not_verified"], f);
    for (const k of ["aging", "stale", "archived", "warning", "unconfirmed", "unreachable", "manual"]) assert.ok(!(k in d.xp), `${f} xp.${k}`);
    assert.ok(!("manualCheck" in d.tool) && !("autoCheck" in d.tool), f);
    assert.ok(!("love" in d.weekly) && !("loveNote" in d.weekly), f);
    assert.match(d.tool.lastChecked, /\{date\}/, f);
    assert.match(d.ver.registryUnlinked, /\{name\}/, f);
  }
});

function* walk(dir) {
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    const p = join(dir, e.name);
    if (e.isDirectory()) yield* walk(p); else yield p;
  }
}

test("built site: no internal status wording outside blog articles", (t) => {
  const dist = join(root, "dist");
  if (!existsSync(join(dist, "verification/index.html"))) return t.skip("dist not built");
  const bad = /Link check pending|refused our checker|Needs maintainer love|Manually checked on|Automated check on|unconfirmed →|ReadTimeout|Could not confirm|checker error|checker timed out/i;
  const hits = [];
  for (const p of walk(dist)) {
    if (!/\.(html|json|txt|xml|svg|csv)$/.test(p)) continue;
    if (/\/blog\/(?!index\.html|page\/|tag\/|rss\.xml)/.test(p.slice(dist.length))) continue; // articles are edited separately
    const s = readFileSync(p, "utf8");
    const m = s.match(bad);
    if (m) hits.push(`${p.slice(dist.length)}: ${m[0]}`);
  }
  assert.deepEqual(hits.slice(0, 20), []);
});

test("badge SVGs show one of the three public labels", (t) => {
  const dir = join(root, "dist/badge");
  if (!existsSync(dir)) return t.skip("dist not built");
  for (const f of readdirSync(dir)) {
    const s = readFileSync(join(dir, f), "utf8");
    assert.match(s, /<title>TradingAIHub: (✓ Verified|Under review|Not currently verified) \d{4}-\d{2}-\d{2}<\/title>/, f);
  }
});
