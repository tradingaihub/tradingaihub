---
title: "Weekly Verification Report, November 16, 2026: Two New Listings, Four Status Upgrades, and a Monday Re-check That Didn't Go Live"
description: "The Nov 16 re-check is not in the public dataset. Since the Nov 9 run, the directory grew to 106 tools and 87 verified, with Sure, CoinBoss and four upgrades."
date: 2026-11-17
tags: [verification, mcp, weekly-report]
tools: [sure, coinboss-api, actual-budget-mcp, openbb, mercury-mcp, firefly-iii-api, sec-edgar-api]
---
*Not financial advice. This report describes the maintenance status of software tools. It is not a recommendation to use, buy, sell or trade anything.*

The scheduled Monday re-check on **November 16, 2026** did complete, but those results are **not** in our public dataset ([tools.json](/tools.json)). The site build stopped because a comparison page requires [SEC EDGAR APIs](/tools/sec-edgar-api/) to be verified, and in that run it was not, so the new statuses were never published.

This report uses only records we can point to. It compares the weekly run on **November 9, 2026** (finished at 05:50 UTC) with the latest live data, from a check dated **November 11, 2026** at 12:51 UTC, and it reports the **status totals** from the November 16 re-check log. We are not naming which tools changed in that unpublished run, other than SEC EDGAR APIs, because a per-tool diff was not saved to the repository.

The status we previously called **Needs review** is now shown on the site as **Link check pending**. The underlying value is unchanged. A separate badge, **Check links**, means a homepage, docs or endpoint link failed in the check.

In the published data, the directory grew from 104 tools to 106, fully verified listings rose from 81 to 87, and four tools moved up a status. Nothing in the published dataset moved down.

## Status counts

| Status | Nov 9 run | Latest published (Nov 11) | Nov 16 re-check (not published) |
|---|---|---|---|
| Verified | 81 | 87 | 82 |
| Aging | 5 | 4 | 5 |
| Stale | 12 | 12 | 12 |
| Archived | 3 | 3 | 3 |
| Link check pending | 3 | 0 | 3 |
| Check links | 0 | 0 | 1 |
| **Total** | **104** | **106** | **106** |

The published directory has 74 MCP servers, 17 APIs and 15 agent skills, up one MCP server and one API from November 9. Every published row is on the [latest verification](/verification/) page.

From our [verification method](/about/): **Verified** means the repository is reachable, its links respond, and (for repos) it had a commit in the last 180 days. **Aging** is 180 to 365 days without a commit; **Stale** is more than a year.

Most published rows still carry a November 9 check date. Only seven listings were re-checked on November 10 or 11: the two new tools, plus Actual Budget MCP, OpenBB Platform, Mercury MCP, Firefly III API and x402.

## What is new: Sure and CoinBoss API

Two listings were added on November 11, both **Verified**. None were removed.

[Sure](/tools/sure/), in our [personal finance category](/category/personal-finance/), is a self-hosted personal finance app: accounts, transactions, budgets and net worth, with a first-party MCP server and REST API. It is a community-maintained fork of Maybe Finance, licensed AGPL-3.0. Our package check did not count an npm package named `sure`, because the name exists on the registry but does not link back to this repository.

[CoinBoss API](/tools/coinboss-api/), in our [crypto category](/category/crypto/), is an official REST API for aggregated crypto derivatives and market data: liquidations, open interest, funding rates, long/short ratios and ETF flows. It is market data only. The listing records it as currently free, including a professional cap of 1,200 requests per minute, with paid plans listed as coming soon.

## What improved in the published data

[Actual Budget MCP](/tools/actual-budget-mcp/), the MCP server for the open-source Actual Budget app, also in [personal finance](/category/personal-finance/), is the biggest maintenance move. On November 9 it was **Aging**, with a last commit dated March 23, 2026 (230 days) and no counted package. The November 10 check found a commit dated November 4, 2026 (five days before that check) and moved it to **Verified**. In the same update, the license we record changed from "unknown" to **MIT**, and the checker counted the published package `actual-budget-mcp@0.12.0`. See also Valyu MCP in our [November 9 report](/blog/weekly-verification-report-2026-11-09/).

The three listings that were in **Link check pending** on November 9 are all **Verified** in the published dataset:

- [OpenBB Platform (MCP)](/tools/openbb/), in [research and filings](/category/research-filings/), was marked verified after a **manual check on November 11**. The stored repository link still redirects to another owner (`openbq-org/OpenBB`) and has not been updated yet. The redirect note remains on the record.
- [Mercury MCP (official)](/tools/mercury-mcp/) and [Firefly III API](/tools/firefly-iii-api/) also moved to verified on November 11, after a change to our checker that day: it now sends browser-like request headers, and it treats some MCP sign-in responses as reachable. The badge change reflects how we check, not that those services were down last week and back this week.

Published package counts rose from 27 to 28, the extra row being Actual Budget MCP. No other package versions changed between the November 9 and November 11 report tables.

## What the unpublished November 16 re-check showed

The November 16 totals, from the run log, are in the table above. Verified listings would have fallen from 87 to 82, matching the rise in **Link check pending** (back to 3), **Aging** (to 5) and **Check links** (to 1). The public dataset was left unchanged, so [SEC EDGAR APIs](/tools/sec-edgar-api/) still appears as verified. That listing is a pick on our [best AI tools for stock analysis](/compare/best-ai-tools-for-stock-analysis/) page, which is why the unpublished run could not go live.

Because the new dataset and per-tool report were not committed, we cannot list the other four listings that left the verified set, or say which three are in Link check pending. The next scheduled run is Monday, November 23, 2026 at 05:00 UTC. If that run publishes, the next report will use it as the current side of the diff.

## What didn't change in the published data

The three **archived** repositories are unchanged: Base MCP, Ramp MCP and MCP Trader.

The 12 **stale** entries are the same set as on November 9, ranging from the Invoice Organizer skill (387 days without a commit, as of that check) to Claude Investor (956 days). The four **Aging** tools in the November 11 published data are Bankless Onchain MCP (187 days), MetaTrader 5 MCP (225 days), DexScreener Trending MCP (300 days) and Crypto Indicators MCP (338 days). Those four still have a November 9 check date, so the day counts have not been refreshed.

No published listing became unreachable or failed a link check in that span.

## How to use this report

A verified badge tells you a project is alive and its links worked in our last published check. It doesn't tell you the tool is secure, accurate or right for your use case. Read the code or docs, test with paper or sandbox accounts first, and keep credentials scoped.

For a ranked view of what's actively maintained, see the [weekly leaderboard](/weekly/). For a side-by-side starting point, try the [best AI tools for stock analysis](/compare/best-ai-tools-for-stock-analysis/) page, or browse [all tools](/tools/). Our [method article](/blog/we-re-check-104-finance-ai-tools-every-week/) explains how we assign the badges.

*Data sources: weekly run of November 9, 2026; published verification report of November 11, 2026, 12:51 UTC ([public dataset](/tools.json), [latest run](/verification/)); status totals from the unpublished November 16, 2026 re-check log. Statuses are generated automatically from public repository, package-registry and link checks. Not financial advice.*
