import { tools } from "../../lib/data";
import { badgeKindOf, badgeSvg, type BadgeKind, type BadgeTheme } from "../../lib/badge";

export function getStaticPaths() {
  const paths: { params: { id: string }; props: { kind: BadgeKind; theme: BadgeTheme } }[] = [
    { params: { id: "verified" }, props: { kind: "verified", theme: "light" } },
    { params: { id: "verified-dark" }, props: { kind: "verified", theme: "dark" } },
  ];
  for (const t of tools) {
    const kind = badgeKindOf(t);
    paths.push({ params: { id: t.id }, props: { kind, theme: "light" } });
    paths.push({ params: { id: `${t.id}-dark` }, props: { kind, theme: "dark" } });
  }
  return paths;
}

export function GET({ props }: { props: { kind: BadgeKind; theme: BadgeTheme } }) {
  return new Response(badgeSvg(props.kind, props.theme), {
    headers: { "Content-Type": "image/svg+xml; charset=utf-8", "Cache-Control": "public, max-age=86400" },
  });
}
