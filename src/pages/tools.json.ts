import { tools, publicStatus } from "../lib/data";
import { untagUrl } from "../lib/aff";
// Public data export: EODHD and TrendSpider vendor URLs are exported plain (no via=/_go=); the site's own links carry the affiliate param.
const plain = (u?: string) => untagUrl(untagUrl(u, "eodhd"), "trendspider");
export const GET = () => new Response(JSON.stringify(tools.map((t) => ({
  id: t.id, name: t.name, type: t.type, category: t.category, description: t.description,
  repo: t.repo, homepage: plain(t.homepage),
  pricing: t.pricing ? { ...t.pricing, source: plain(t.pricing.source) } : t.pricing,
  license: t.license, status: publicStatus(t),
  risk_tier: t.risk_tier === "high" ? "high" : "standard",
  checked_at: t.verification.checked_at,
}))), { headers: { "content-type": "application/json" } });
