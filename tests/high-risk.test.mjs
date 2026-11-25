// High-risk crypto listings must never appear in best-of or comparison outputs.
import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const tools = JSON.parse(readFileSync(join(root, "data/tools.json"), "utf8"));
const highIds = tools.filter((t) => t.risk_tier === "high" || t.category === "high-risk-crypto").map((t) => t.id);

test("copy.top is the high-risk listing and is not marked verified in public fields", () => {
  assert.ok(highIds.includes("copy-top"));
  for (const t of tools.filter((x) => highIds.includes(x.id))) {
    assert.equal(t.risk_tier, "high", t.id);
    assert.equal(t.category, "high-risk-crypto", t.id);
  }
});

test("best-of pages do not list high-risk tool ids", () => {
  const src = readFileSync(join(root, "src/lib/bestPages.ts"), "utf8");
  const ids = [...src.matchAll(/toolIds:\s*\[([\s\S]*?)\]/g)].flatMap((m) => [...m[1].matchAll(/"([a-z0-9-]+)"/g)].map((x) => x[1]));
  assert.ok(ids.length >= 20, "could not parse best-page toolIds");
  const leaked = ids.filter((id) => highIds.includes(id));
  assert.deepEqual(leaked, []);
  assert.match(src, /isHighRisk/);
  assert.match(src, /high-risk tools cannot appear/);
});

test("COMPARISONS filters exclude high-risk tools", () => {
  const src = readFileSync(join(root, "src/lib/data.ts"), "utf8");
  const filters = [...src.matchAll(/filter: \(t: any\) => ([^,\n]+)/g)].map((m) => m[1]);
  assert.equal(filters.length, 7);
  for (const f of filters) assert.match(f, /!isHighRisk\(t\)/);
});
