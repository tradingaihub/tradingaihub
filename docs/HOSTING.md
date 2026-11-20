# Hosting & deploy

## Cloudflare Pages
```bash
npm run weekly            # verify → awesome list → OG images → astro build (dist/)
npx wrangler pages deploy dist --project-name=tradingaihub --branch=main
```
Production: https://tradingaihub.com (Cloudflare Pages + Pages Functions in `functions/`). Brand settings live in `src/config.ts` and `wrangler.toml`.
Cloudflare Pages free plan: static requests/bandwidth are free; 500 builds/month; 20k files per deploy.

## Daily automation
`.github/workflows/weekly.yml` (workflow name `weekly-verify`, daily at 03:00 UTC) runs verify → awesome → og → build. It commits `data/`, `awesome/` and `public/og` and deploys only when the published dataset actually changed, or on the Monday weekly snapshot (history + changelog for `/weekly/` and the Tuesday blog report). Timestamp-only churn such as `checked_at` does not trigger a mid-week deploy. It needs Cloudflare deploy credentials configured as repository secrets.

## Services
| Purpose | Service |
|---|---|
| Hosting, DNS, registrar | Cloudflare |
| Awesome list mirror | GitHub `awesome-finance-ai-tools` (generated from `awesome/README.md`) |
| Submissions | GitHub Issue Form + https://tradingaihub.com/submit/ |
| Contact | hello@tradingaihub.com (Cloudflare Email Routing) |
| Analytics | Cookie-free Cloudflare Web Analytics |
| Payments | Polar (merchant of record) |

## Monetization principles
- Sponsored placements and affiliate links are always labelled; listings stay ranked by verification, not by payment.
- Affiliate programs in use or considered: TradingView Partner Program, EODHD, Financial Modeling Prep, TrendSpider.
- "Not investment advice" disclaimer (incl. Israel's Investment Advice Law 5755-1995) is on every page. Vendor data is never redistributed.
