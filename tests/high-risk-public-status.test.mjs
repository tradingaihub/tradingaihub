// High-risk tools must never appear as "verified" on public surfaces.
import { readFileSync, existsSync, readdirSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import assert from "node:assert/strict";
import test from "node:test";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const tools = JSON.parse(readFileSync(join(root, "data/tools.json"), "utf8"));
const high = tools.filter((t) => t.risk_tier === "high" || t.category === "high-risk-crypto");
const PUBLIC = new Set(["verified", "under_review", "not_verified"]);
const isHigh = (t) => t.risk_tier === "high" || t.category === "high-risk-crypto";
const publicStatus = (t) => (isHigh(t) ? "not_verified" : t.verification.status);

test("there is at least one high-risk tool", () => {
  assert.ok(high.length >= 1);
  assert.ok(high.some((t) => t.id === "copy-top"));
});

test("the verification report does not count high-risk tools as verified", () => {
  assert.ok(!existsSync(join(root, "data/verification-report.md")), "verification-report.md must not be committed");
  const rep = JSON.parse(readFileSync(join(root, "data/verification-report.json"), "utf8"));
  const expectedVerified = tools.filter((t) => publicStatus(t) === "verified").length;
  assert.equal(rep.by_status.verified, expectedVerified);
  assert.equal(rep.by_status.verified, tools.filter((t) => t.verification.status === "verified" && !isHigh(t)).length);
  assert.ok(!("high_risk" in rep.by_status));
  assert.deepEqual(Object.keys(rep.by_status).sort(), [...PUBLIC].sort());
  assert.equal(rep.total, tools.length);
  for (const t of high) {
    assert.equal(t.verification.status, "not_verified", t.id);
    assert.notEqual(t.verification.status, "verified", t.id);
  }
});

test("source derives not_verified (never verified) for high-risk tools", () => {
  const data = readFileSync(join(root, "src/lib/data.ts"), "utf8");
  assert.match(data, /export const publicStatus/);
  assert.match(data, /isHighRisk\(t\) \? "not_verified"/);
  assert.doesNotMatch(data, /high_risk: \{ label/);
  const api = readFileSync(join(root, "src/lib/publicApi.ts"), "utf8");
  assert.match(api, /status: publicStatus\(t\)/);
  assert.match(api, /status_label: STATUS\[publicStatus\(t\)\]/);
  const exportFile = readFileSync(join(root, "src/pages/tools.json.ts"), "utf8");
  assert.match(exportFile, /status: publicStatus\(t\)/);
  assert.match(exportFile, /risk_tier:/);
  const ver = readFileSync(join(root, "src/pages/[...lang]/verification.astro"), "utf8");
  assert.match(ver, /Status status=\{publicStatus\(x\)\}/);
  const toolsPage = readFileSync(join(root, "src/pages/[...lang]/tools/[id].astro"), "utf8");
  assert.match(toolsPage, /!highRisk && <Status status=\{publicStatus\(tool\)\}/);
  assert.match(toolsPage, /<RiskBanner /);
  const llms = readFileSync(join(root, "src/lib/llms.ts"), "utf8");
  assert.match(llms, /STATUS\[publicStatus\(x\)\]/);
  const mcp = readFileSync(join(root, "functions/_lib/mcp.js"), "utf8");
  assert.match(mcp, /risk_tier: t\.risk_tier/);
  assert.match(mcp, /status: t\.status/);
  const awesome = readFileSync(join(root, "scripts/awesome.py"), "utf8");
  assert.match(awesome, /public_status\(t\)/);
  assert.match(awesome, /"high_risk": "⚠️"/);
  assert.doesNotMatch(awesome, /"high_risk": "✅"/);
});

test("awesome README marks high-risk tools with the warning, not verified", () => {
  const md = readFileSync(join(root, "awesome/README.md"), "utf8");
  assert.match(md, /⚠️ \[copy\.top\]/);
  assert.doesNotMatch(md, /✅ \[copy\.top\]/);
  assert.doesNotMatch(md, /🟡 \[copy\.top\]/);
});

function loadDist() {
  const toolsJson = ["dist/tools.json", "dist/tools.json/index.html"].find((p) => existsSync(join(root, p)));
  const apiJson = ["dist/api/v1/tools.json", "dist/api/v1/tools.json/index.html"].find((p) => existsSync(join(root, p)));
  const llmsFull = existsSync(join(root, "dist/llms-full.txt")) ? join(root, "dist/llms-full.txt") : null;
  const verHtml = existsSync(join(root, "dist/verification/index.html")) ? join(root, "dist/verification/index.html") : null;
  return { toolsJson, apiJson, llmsFull, verHtml };
}

test("built public surfaces never call a high-risk tool verified", function (t) {
  const { toolsJson, apiJson, llmsFull, verHtml } = loadDist();
  if (!toolsJson || !apiJson) {
    t.skip("dist not built yet");
    return;
  }
  const pub = JSON.parse(readFileSync(join(root, toolsJson), "utf8"));
  const rows = Array.isArray(pub) ? pub : pub.tools;
  const api = JSON.parse(readFileSync(join(root, apiJson), "utf8"));
  const apiRows = api.tools || api;
  for (const t0 of high) {
    const r = rows.find((x) => x.id === t0.id || x.slug === t0.id);
    assert.ok(r, `missing ${t0.id} in /tools.json`);
    assert.equal(r.status, "not_verified", `/tools.json ${t0.id}`);
    assert.notEqual(r.status, "verified", `/tools.json ${t0.id}`);
    assert.equal(r.risk_tier, "high", `/tools.json ${t0.id} risk_tier`);
    const a = apiRows.find((x) => x.slug === t0.id);
    assert.ok(a, `missing ${t0.id} in /api/v1/tools`);
    assert.equal(a.status, "not_verified");
    assert.equal(a.status_label, "Not currently verified");
    assert.notEqual(a.status_label, "Verified");
    assert.equal(a.verified, false);
    assert.equal(a.risk_tier, "high");
    const page = join(root, "dist/tools", t0.id, "index.html");
    assert.ok(existsSync(page), page);
    const html = readFileSync(page, "utf8");
    assert.match(html, /class="risk-banner"/);
    assert.doesNotMatch(html, /class="badge good"/);
    assert.doesNotMatch(html, /✓ Verified/);
    assert.ok(!html.includes(`/badge/${t0.id}`), `${t0.id} tool page must not link a status badge`);
  }
  assert.equal(apiRows.filter((x) => x.status === "verified" && x.risk_tier === "high").length, 0);
  assert.equal(apiRows.filter((x) => x.verified === true && x.risk_tier === "high").length, 0);
  assert.equal(rows.filter((x) => x.status === "verified" && x.risk_tier === "high").length, 0);
  if (llmsFull) {
    const txt = readFileSync(llmsFull, "utf8");
    assert.match(txt, /Not eligible for the Verified badge/);
    assert.match(txt, /Status: Not currently verified/);
    assert.doesNotMatch(txt, /copy\.top[\s\S]{0,800}Status: Verified/);
  }
  if (verHtml) {
    const html = readFileSync(verHtml, "utf8");
    assert.match(html, /\/tools\/copy-top\//);
    const row = html.split("/tools/copy-top/")[1].split("</tr>")[0];
    assert.match(row, /Not currently verified/);
    assert.doesNotMatch(row, /✓ Verified/);
    assert.doesNotMatch(row, /badge good/);
  }
});
