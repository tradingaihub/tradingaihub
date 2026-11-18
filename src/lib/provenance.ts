// Package provenance helpers shared by the badge, the tool page, /audit/, llms and /tools.json.
// Source of truth: data/tools.json -> verification.provenance (written by scripts/verify.py). Raw URLs only (no affiliate tags).
import raw from "../../data/tools.json";
export type ProvState = "verified" | "mismatch" | "unlinked" | "none";
export const PROV_STATES: ProvState[] = ["verified", "mismatch", "unlinked", "none"];
export const REGISTRY_LABEL: Record<string, string> = { npm: "npm", pypi: "PyPI" };
const rawById: Record<string, any> = Object.fromEntries((raw as any[]).map((t) => [t.id, t]));
const NONE = { state: "none" as ProvState, registry: null, package: null, package_url: null, version: null, declared_repo: null };
export const provOf = (id: string): { state: ProvState; registry: string | null; package: string | null; package_url: string | null; version: string | null; declared_repo: string | null; checked_at?: string } =>
  rawById[id]?.verification?.provenance ?? NONE;
/** Public export shape (tools.json, /api/v1): no maintainer names. */
export const provExport = (id: string) => { const p = provOf(id); return { state: p.state, registry: p.registry, package: p.package, package_url: p.package_url, declared_repo: p.declared_repo }; };
export const provCounts = () => {
  const c: Record<ProvState, number> = { verified: 0, mismatch: 0, unlinked: 0, none: 0 };
  for (const t of raw as any[]) c[(t.verification?.provenance?.state ?? "none") as ProvState]++;
  return c;
};
export const shortRepo = (u: string | null | undefined) => (u || "").replace(/^https:\/\/github\.com\//, "").replace(/\/tree\/.*$/, "");

// Weekly tools.json still records the older "name exists but does not link" issue and a failed
// "package published" / "no package at repo root" check even when the newer provenance pass
// verified the same package (e.g. after following a GitHub rename redirect). Prefer provenance.
const STALE_LINK_ISSUE = /exists on the registry but does not link to this repo/;
const STALE_ROOT_NOTE = /no package at repo root/i;

export function visibleIssues(v: { provenance?: { state?: string }; issues?: string[] } | null | undefined): string[] {
  const issues = Array.isArray(v?.issues) ? v!.issues! : [];
  if (v?.provenance?.state !== "verified") return issues;
  return issues.filter((i) => !STALE_LINK_ISSUE.test(i));
}

export function visibleChecks(v: { provenance?: { state?: string }; checks?: any[] } | null | undefined): any[] {
  const checks = Array.isArray(v?.checks) ? v!.checks! : [];
  if (v?.provenance?.state !== "verified") return checks;
  return checks.filter((c) => !(c?.check === "package published" && !c?.ok && STALE_ROOT_NOTE.test(String(c?.note || ""))));
}
