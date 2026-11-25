// High-risk tools must never appear as "verified" on public surfaces.
import { readFileSync, existsSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import assert from "node:assert/strict";
import test from "node:test";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const tools = JSON.parse(readFileSync(join(root, "data/tools.json"), "utf8"));
const high = tools.filter((t) => t.risk_tier === "high" || t.category === "high-risk-crypto");
const publicStatus = (t) =>
  t.risk_tier === "high" || t.category === "high-risk-crypto" ? "high_risk" : t.verification.status;

test("there is at least one high-risk tool", () => {
  assert.ok(high.length >= 1);
  assert.ok(high.some((t) => t.id === "copy-top"));
});

test("the verification report does not count high-risk tools as verified", () => {
  const rep = JSON.parse(readFileSync(join(root, "data/verification-report.json"), "utf8"));
  const md = readFileSync(join(root, "data/verification-report.md"), "utf8");
  const expectedVerified = tools.filter((t) => publicStatus(t) === "verified").length;
  assert.equal(rep.by_status.verified, expectedVerified);
  assert.equal(rep.by_status.high_risk, high.length);
  assert.equal(rep.total, tools.length);
  for (const t of high) {
    assert.match(md, new RegExp(`\\| ${t.id} \\| high_risk \\|`));
    assert.doesNotMatch(md, new RegExp(`\\| ${t.id} \\| verified \\|`));
    assert.notEqual(t.verification.status, "high_risk", "internal verifier status stays raw");
  }
});

test("source derives one public status (high_risk) for high-risk tools", () => {
  const data = readFileSync(join(root, "src/lib/data.ts"), "utf8");
  assert.match(data, /export const publicStatus/);
  assert.match(data, /high_risk/);
  const api = readFileSync(join(root, "src/lib/publicApi.ts"), "utf8");
  assert.match(api, /status: publicStatus\(t\)/);
  assert.match(api, /status_label: STATUS\[publicStatus\(t\)\]/);
  const exportFile = readFileSync(join(root, "src/pages/tools.json.ts"), "utf8");
  assert.match(exportFile, /status: publicStatus\(t\)/);
  assert.match(exportFile, /risk_tier:/);
  const ver = readFileSync(join(root, "src/pages/[...lang]/verification.astro"), "utf8");
  assert.match(ver, /Status status=\{publicStatus\(x\)\}/);
  assert.match(ver, /TitleText text=\{x\.name\} bdi/);
  const llms = readFileSync(join(root, "src/lib/llms.ts"), "utf8");
  assert.match(llms, /STATUS\[publicStatus\(x\)\]/);
  const mcp = readFileSync(join(root, "functions/_lib/mcp.js"), "utf8");
  assert.match(mcp, /risk_tier: t\.risk_tier/);
  const awesome = readFileSync(join(root, "scripts/awesome.py"), "utf8");
  assert.match(awesome, /public_status\(t\)/);
  assert.match(awesome, /"high_risk": "⚠️"/);
});

test("awesome README marks high-risk tools with the warning, not verified", () => {
  const md = readFileSync(join(root, "awesome/README.md"), "utf8");
  assert.match(md, /⚠️ \[copy\.top\]/);
  assert.doesNotMatch(md, /✅ \[copy\.top\]/);
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
    assert.equal(r.status, "high_risk", `/tools.json ${t0.id}`);
    assert.equal(r.risk_tier, "high", `/tools.json ${t0.id} risk_tier`);
    const a = apiRows.find((x) => x.slug === t0.id);
    assert.ok(a, `missing ${t0.id} in /api/v1/tools`);
    assert.equal(a.status, "high_risk");
    assert.equal(a.status_label, "High risk");
    assert.equal(a.verified, false);
    assert.equal(a.risk_tier, "high");
  }
  assert.equal(apiRows.filter((x) => x.status === "verified" && x.risk_tier === "high").length, 0);
  assert.equal(apiRows.filter((x) => x.status === "verified").every((x) => x.risk_tier !== "high"), true);
  if (llmsFull) {
    const txt = readFileSync(llmsFull, "utf8");
    assert.match(txt, /Status: High risk/);
    // The "not eligible" line must not be followed by Status: Verified for copy.top
    assert.doesNotMatch(txt, /Not eligible for the Verified badge\.\n  - [^\n]*Status: Verified/);
  }
  if (verHtml) {
    const html = readFileSync(verHtml, "utf8");
    assert.match(html, /High risk/);
    // copy.top row should not show a Verified chip in isolation; summary must not say 101 if home is 100
    // At least: the copy-top link is present and a High risk badge exists on the page.
    assert.match(html, /\/tools\/copy-top\//);
  }
});
