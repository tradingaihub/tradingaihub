---
title: "Weekly Verification Report, November 16, 2026: Two New Listings, Four Status Upgrades, and a Monday Re-check That Didn't Go Live"
description: "The Nov 16 re-check did not go live that day. 106 tools and 87 verified as of 11 Nov; the latest published run, 18 Nov, shows 81 verified."
date: 2026-11-17
tags: [verification, mcp, weekly-report]
tools: [sure, coinboss-api, actual-budget-mcp, openbb, mercury-mcp, firefly-iii-api, sec-edgar-api]
---
*Not financial advice. This report describes the maintenance status of software tools. It is not a recommendation to use, buy, sell or trade anything.*

The scheduled Monday re-check on **November 16, 2026** did complete, but those results were **not published**. The site build stopped because a comparison page requires [SEC EDGAR APIs](/tools/sec-edgar-api/) to be verified, and in that run it was not, so the new statuses never went live that day.

This report uses only records we can point to. It compares the weekly run on **November 9, 2026** (finished at 05:50 UTC) with the **November 11, 2026** published snapshot (12:51 UTC), and it reports the **status totals** from the November 16 re-check log. Those Nov 16 totals are not in the site repository (there is no `data/history/2026-11-16.json`), so they cannot be reproduced from the public repo. We are not naming which tools changed in that unpublished run, other than SEC EDGAR APIs, because a per-tool diff was not saved to the repository.

The latest published dataset is now the weekly run of **November 18, 2026**, finished at 17:35 Asia/Jerusalem (15:35 UTC). All 106 rows in the public dataset ([tools.json](/tools.json)) carry that check date: 81 Verified, 5 Aging, 12 Stale, 3 Archived, 3 Link check pending and 2 Check links, as recorded in `data/verification-report.json` and on the [latest verification](/verification/) page.

The status we previously called **Needs review** is now shown on the site as **Link check pending**. The underlying value is unchanged. A separate badge, **Check links**, means a homepage, docs or endpoint link failed in the check.

In the 11 November published snapshot, the directory grew from 104 tools to 106, fully verified listings rose from 81 to 87, and four tools moved up a status. Nothing in that snapshot moved down.

## Status counts

| Status | Nov 9 run | 11 Nov published | 16 Nov re-check (not published) | 18 Nov (latest published) |
|---|---|---|---|---|
| Verified | 81 | 87 | 82 | 81 |
| Aging | 5 | 4 | 5 | 5 |
| Stale | 12 | 12 | 12 | 12 |
| Archived | 3 | 3 | 3 | 3 |
| Link check pending | 3 | 0 | 3 | 3 |
| Check links | 0 | 0 | 1 | 2 |
| **Total** | **104** | **106** | **106** | **106** |

The 11 November published directory had 74 MCP servers, 17 APIs and 15 agent skills, up one MCP server and one API from November 9. Those type counts are unchanged in the 18 November published run. Every current published row is on the [latest verification](/verification/) page.

From our [verification method](/about/): **Verified** means the repository is reachable, its links respond, and (for repos) it had a commit in the last 180 days. **Aging** is 180 to 365 days without a commit; **Stale** is more than a year.

In the 11 November snapshot, most rows still carried a November 9 check date. Only seven listings were re-checked on November 10 or 11: the two new tools, plus Actual Budget MCP, OpenBB Platform, Mercury MCP, Firefly III API and x402. In the 18 November published run, every row carries an 18 November check date.

## What is new: Sure and CoinBoss API

Two listings were added on November 11, both **Verified**. None were removed.

[Sure](/tools/sure/), in our [personal finance category](/category/personal-finance/), is a self-hosted personal finance app: accounts, transactions, budgets and net worth, with a first-party MCP server and REST API. It is a community-maintained fork of Maybe Finance, licensed AGPL-3.0. Our package check did not count an npm package named `sure`, because the name exists on the registry but does not link back to this repository.

[CoinBoss API](/tools/coinboss-api/), in our [crypto category](/category/crypto/), is an official REST API for aggregated crypto derivatives and market data: liquidations, open interest, funding rates, long/short ratios and ETF flows. It is market data only. The listing records it as currently free, including a professional cap of 1,200 requests per minute, with paid plans listed as coming soon.

## What improved in the 11 November published data

[Actual Budget MCP](/tools/actual-budget-mcp/), the MCP server for the open-source Actual Budget app, also in [personal finance](/category/personal-finance/), is the biggest maintenance move. On November 9 it was **Aging**, with a last commit dated March 23, 2026 (230 days) and no counted package. The November 10 check found a commit dated November 4, 2026 (five days before that check) and moved it to **Verified**. In the same update, the license we record changed from "unknown" to **MIT**, and the checker counted the published package `actual-budget-mcp@0.12.0`. See also Valyu MCP in our [November 9 report](/blog/weekly-verification-report-2026-11-09/).

The three listings that were in **Link check pending** on November 9 are all **Verified** in the 11 November published snapshot:

- [OpenBB Platform (MCP)](/tools/openbb/), in [research and filings](/category/research-filings/), was marked verified after a **manual check on November 11**. The stored repository link still redirects to another owner (`openbq-org/OpenBB`) and has not been updated yet. The redirect note remains on the record.
- [Mercury MCP (official)](/tools/mercury-mcp/) and [Firefly III API](/tools/firefly-iii-api/) also moved to verified on November 11, after a change to our checker that day: it now sends browser-like request headers, and it treats some MCP sign-in responses as reachable. The badge change reflects how we check, not that those services were down last week and back this week. In the 18 November published run, [Firefly III API](/tools/firefly-iii-api/) is **Link check pending** (unconfirmed) again: the checker received HTTP 403 on the homepage and docs.

Published package counts rose from 27 to 28, the extra row being Actual Budget MCP. No other package versions changed between the November 9 and November 11 report tables.

## What the unpublished November 16 re-check showed

The November 16 totals, from a run log that was not committed to the repository, are in the table above. Verified listings would have fallen from 87 to 82, matching the rise in **Link check pending** (back to 3), **Aging** (to 5) and **Check links** (to 1). Those Nov 16 results were never published, so the public dataset stayed at the 11 November snapshot until the next weekly run. [SEC EDGAR APIs](/tools/sec-edgar-api/) was the listing that blocked that deploy; it is Verified again in the 18 November published run. That listing is a pick on our [best AI tools for stock analysis](/compare/best-ai-tools-for-stock-analysis/) page, which is why the unpublished run could not go live.

Because the Nov 16 dataset and per-tool report were not committed, we cannot list the other four listings that left the verified set that day, or say which three were in Link check pending. The 18 November run has since published (81 Verified of 106). The next scheduled run is Monday, November 23, 2026 at 05:00 UTC.

## What didn't change in the 11 November published data

The three **archived** repositories are unchanged: Base MCP, Ramp MCP and MCP Trader.

The 12 **stale** entries are the same set as on November 9, ranging from the Invoice Organizer skill (387 days without a commit, as of that check) to Claude Investor (956 days). The four **Aging** tools in the November 11 published data are Bankless Onchain MCP (187 days), MetaTrader 5 MCP (225 days), DexScreener Trending MCP (300 days) and Crypto Indicators MCP (338 days). In that snapshot those four still had a November 9 check date, so the day counts had not been refreshed.

No listing in the 11 November published snapshot became unreachable or failed a link check between November 9 and November 11.

## How to use this report

A verified badge tells you a project is alive and its links worked in our last published check. It doesn't tell you the tool is secure, accurate or right for your use case. Read the code or docs, test with paper or sandbox accounts first, and keep credentials scoped.

For a ranked view of what's actively maintained, see the [weekly leaderboard](/weekly/). For a side-by-side starting point, try the [best AI tools for stock analysis](/compare/best-ai-tools-for-stock-analysis/) page, or browse [all tools](/tools/). Our [method article](/blog/we-re-check-104-finance-ai-tools-every-week/) explains how we assign the badges.

*Data sources: weekly run of November 9, 2026; published verification report of November 11, 2026, 12:51 UTC (snapshot in `data/history/2026-11-11.json`); status totals from the unpublished November 16, 2026 re-check log, which is not in the repository; latest published run of November 18, 2026, 15:35 UTC ([public dataset](/tools.json), `data/verification-report.json`, [latest run](/verification/)). Statuses are generated automatically from public repository, package-registry and link checks. Not financial advice.*
