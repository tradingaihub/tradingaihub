// Static "Verified on TradingAIHub" / "Listed on TradingAIHub" SVG badges.
// Generated at build from verification status (and risk_tier, when present).
// Weekly-verify rebuilds refresh the SVGs; a tool that loses verification keeps
// the same /badge/<id>.svg URL and switches to the Listed artwork, so embeds
// don't 404.
import { SITE } from "../config";

export const BADGE_W = 180;
export const BADGE_H = 40;

export type BadgeKind = "verified" | "listed";
export type BadgeTheme = "light" | "dark";

export function isBadgeVerified(t: { verification?: { status?: string }; risk_tier?: string } | null | undefined): boolean {
  return !!t && t.verification?.status === "verified" && t.risk_tier !== "high";
}

export function badgeKindOf(t?: { verification?: { status?: string }; risk_tier?: string } | null): BadgeKind {
  return isBadgeVerified(t) ? "verified" : "listed";
}

export function badgeLabel(kind: BadgeKind): string {
  return kind === "verified" ? "Verified on TradingAIHub" : "Listed on TradingAIHub";
}

export function badgeSnippets(id: string, kind: BadgeKind) {
  const label = badgeLabel(kind);
  const page = `${SITE.url}/tools/${id}/?utm_source=badge`;
  const src = `${SITE.url}/badge/${id}.svg`;
  const darkSrc = `${SITE.url}/badge/${id}-dark.svg`;
  const html = `<a href="${page}"><img src="${src}" alt="${label}" width="${BADGE_W}" height="${BADGE_H}"></a>`;
  const md = `[![${label}](${src})](${page})`;
  return { html, md, src, darkSrc, page, label };
}

const THEME: Record<BadgeTheme, Record<BadgeKind, { bg: string; stroke: string; title: string; name: string; icon: string; iconFg: string }>> = {
  light: {
    verified: { bg: "#f0fdf4", stroke: "#86efac", title: "#166534", name: "#0f172a", icon: "#15803d", iconFg: "#ffffff" },
    listed: { bg: "#f8fafc", stroke: "#d9e0ea", title: "#4b5a70", name: "#0f172a", icon: "#64748b", iconFg: "#ffffff" },
  },
  dark: {
    verified: { bg: "#052e16", stroke: "#14532d", title: "#86efac", name: "#f1f5f9", icon: "#22c55e", iconFg: "#052e16" },
    listed: { bg: "#121826", stroke: "#243049", title: "#9aa7bd", name: "#e8edf6", icon: "#64748b", iconFg: "#f1f5f9" },
  },
};

function icon(kind: BadgeKind, c: { icon: string; iconFg: string }): string {
  if (kind === "verified") {
    return `<circle cx="20" cy="20" r="12" fill="${c.icon}"/><path d="M14.5 20.2l3.6 3.6 7.4-8" fill="none" stroke="${c.iconFg}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>`;
  }
  return `<circle cx="20" cy="20" r="12" fill="${c.icon}"/><path d="M15 16.5h10M15 20h10M15 23.5h7" fill="none" stroke="${c.iconFg}" stroke-width="1.8" stroke-linecap="round"/>`;
}

export function badgeSvg(kind: BadgeKind, theme: BadgeTheme = "light"): string {
  const c = THEME[theme][kind];
  const label = badgeLabel(kind);
  const kicker = kind === "verified" ? "Verified on" : "Listed on";
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${BADGE_W}" height="${BADGE_H}" viewBox="0 0 ${BADGE_W} ${BADGE_H}" role="img" aria-label="${label}"><title>${label}</title><rect x="0.5" y="0.5" width="${BADGE_W - 1}" height="${BADGE_H - 1}" rx="8" fill="${c.bg}" stroke="${c.stroke}" stroke-width="1"/>${icon(kind, c)}<g font-family="Verdana, DejaVu Sans, Liberation Sans, sans-serif"><text x="38" y="16" font-size="10" fill="${c.title}">${kicker}</text><text x="38" y="31" font-size="12" font-weight="700" fill="${c.name}">TradingAIHub</text></g></svg>`;
}
