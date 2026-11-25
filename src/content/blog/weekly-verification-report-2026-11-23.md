---
title: "Weekly Verification Report, November 23, 2026: Firefly III API and Razorpay MCP Return to Verified"
description: "Nov 23 re-check: 83 of 106 tools verified, up 2 from the Nov 18 published run. Firefly III API and Razorpay MCP came back. The Nov 16 run never went live."
date: 2026-11-25
draft: true
tags: [verification, mcp, weekly-report]
tools: [firefly-iii-api, razorpay-mcp, fred-api, bls-api, longbridge-skills, solana-agent-kit, ynab-mcp, openbb]
---
*Not financial advice. This report describes the maintenance status of software tools. It is not a recommendation to use, buy, sell or trade anything.*

The scheduled Monday re-check on **November 23, 2026** did go live. It finished at 07:52 Asia/Jerusalem (05:52 UTC). In that published run, every row in the public dataset ([tools.json](/tools.json)) carried a November 23 check date. This report was due on Tuesday, November 24, and is published on November 25.

The comparison baseline is the previous published run on **November 18, 2026**, which finished at 17:35 Asia/Jerusalem (15:35 UTC) and showed **81 Verified** of 106. As we wrote in the [November 16 report](/blog/weekly-verification-report-2026-11-16/), the scheduled Monday run on November 16 never went live: there is still no `data/history/2026-11-16.json` in the public repository. We are not treating that unpublished run as the current side of this week's diff.

In the November 23 published run, **83 of 106** listings were **Verified**, up 2 from November 18. No tools were added or removed. No listing newly broke versus November 18. The two status changes are come-backs: [Firefly III API](/tools/firefly-iii-api/) moved from **Link check pending** to **Verified**, and [Razorpay MCP Server](/tools/razorpay-mcp/) moved from **Check links** to **Verified**. Both badges were **Verified** in that run. The type mix in that run was unchanged: 74 MCP servers, 17 APIs and 15 agent skills.

The 11 November snapshot, which showed 87 Verified of 106, remains useful context. The slips from that snapshot — including [FRED API (St. Louis Fed)](/tools/fred-api/), [BLS Public Data API](/tools/bls-api/), [Longbridge Skills](/tools/longbridge-skills/) and [Solana Agent Kit](/tools/solana-agent-kit/) — happened on the November 18 run, not this one, and those four listings have not changed status since.

## Status counts

| Status | 11 Nov snapshot | 16 Nov re-check (not published) | 18 Nov (previous published run) | 23 Nov (this run) |
|---|---|---|---|---|
| Verified | 87 | 82 | 81 | 83 |
| Aging | 4 | 5 | 5 | 5 |
| Stale | 12 | 12 | 12 | 12 |
| Archived | 3 | 3 | 3 | 3 |
| Link check pending | 0 | 3 | 3 | 2 |
| Check links | 0 | 1 | 2 | 1 |
| **Total** | **106** | **106** | **106** | **106** |

The November 16 totals in that table are the same unpublished run-log figures we already reported. They are not in the repository and cannot be reproduced from a history file. The November 23 published rows are on the [latest verification](/verification/) page.

From our [verification method](/about/): **Verified** means the repository is reachable, its links respond, and (for repos) it had a commit in the last 180 days. **Aging** is 180 to 365 days without a commit; **Stale** is more than a year. **Link check pending** means we could not confirm a homepage or docs link — often because the server answered but refused the checker (HTTP 403). **Check links** means a homepage, docs or endpoint link failed in the check.

## What improved: two come-backs

[Firefly III API](/tools/firefly-iii-api/), in our [personal finance category](/category/personal-finance/), was **Link check pending** on November 18: the checker received HTTP 403 on both the homepage and the API docs. The server answered, but it refused the checker. In the November 23 run, both URLs responded with HTTP 200, the stored issues list is empty, and the listing is **Verified** again. The repository was already reachable in the November 18 record. We are reporting what the checker received in each published run, not a diagnosis of why the earlier responses were 403.

[Razorpay MCP Server](/tools/razorpay-mcp/), in our [payments and banking category](/category/payments-banking/), was in **Check links** on November 18 because the remote MCP endpoint returned a connection error. The homepage itself already responded with HTTP 200 that day. In the November 23 run, a POST to that same endpoint (`https://mcp.razorpay.com/mcp`) received HTTP 401, which our checker treats as reachable for an OAuth-protected MCP server, and the listing moved to **Verified**. The repository had a commit four days before this check. A 401 here means the endpoint answered and asked for authorization. It is not a claim that the server is usable without credentials.

Those two upgrades account for the move from 81 Verified to 83, and for the matching one-step drops in **Link check pending** (3 to 2) and **Check links** (2 to 1).

## What still isn't confirmed

Nothing newly broke versus November 18. Three listings that left the verified set on that earlier run are still not confirmed:

- [FRED API (St. Louis Fed)](/tools/fred-api/), in our [macro category](/category/macro/), remains **Check links**. The checker recorded a read timeout on the homepage and docs, which share the same URL, in both the November 18 and November 23 runs.
- [BLS Public Data API](/tools/bls-api/), also in [macro](/category/macro/), remains **Link check pending**. The homepage and docs both returned HTTP 403: the server answered but refused the checker, in both published runs.
- [Longbridge Skills](/tools/longbridge-skills/), in our [trading and brokers category](/category/trading-brokers/), remains **Link check pending**. The homepage returned HTTP 403 in both runs. The repository itself had a commit 14 days before the November 23 check, so the open issue is the homepage check, not repository age.

[Solana Agent Kit](/tools/solana-agent-kit/), in our [crypto category](/category/crypto/), remains **Aging**. That move happened on November 18, when the listing left **Verified**. As of the November 23 check it had gone 192 days without a commit, up from 187 days in the November 18 record.

## What is new

No listings were added or removed between November 18 and November 23. In the November 23 run the directory was still 106 tools, the same set as in the 11 November snapshot, when [Sure](/tools/sure/) and [CoinBoss API](/tools/coinboss-api/) were added.

One published package version changed. [YNAB MCP Server (community)](/tools/ynab-mcp/), in [personal finance](/category/personal-finance/), remains **Verified** and now records `ynab-mcp-server@0.10.0` (it was 0.9.0 in the November 18 history file). The package record links back to the listed repository. The number of listings with a counted package was unchanged at 28.

## Catalog notes that did not change a badge

[OpenBB Platform (MCP)](/tools/openbb/), in [research and filings](/category/research-filings/), is still **Verified**. The November 23 record includes a catalog note, dated November 20, that the repository has been transferred from `OpenBB-finance/OpenBB` to `openbq-org/OpenBB`, citing [OpenBB's own post](https://openbb.co/blog/openbb-belongs-to-everyone/). The stored repository link on the listing has not been updated yet. This is the same redirect situation we flagged in the [November 16 report](/blog/weekly-verification-report-2026-11-16/); the new note records a confirmed transfer date. A manual-check label from November 11 remains on the record.

## What didn't change

The three **archived** repositories are unchanged: [Base MCP](/tools/base-mcp/), [Ramp MCP](/tools/ramp-mcp/) and [MCP Trader](/tools/mcp-trader/).

The 12 **stale** entries are the same set as on November 18, ranging from the Invoice Organizer skill (401 days without a commit, as of this check) to Claude Investor (970 days). Day counts have been refreshed because every row was re-checked on November 23.

The five **Aging** tools are also the same set as on November 18, with refreshed day counts: Solana Agent Kit (192 days), Bankless Onchain MCP (201 days), MetaTrader 5 MCP (239 days), DexScreener Trending MCP (314 days) and Crypto Indicators MCP (352 days). In the 11 November snapshot the Aging set had four tools; Solana Agent Kit joined it on November 18.

[SEC EDGAR APIs](/tools/sec-edgar-api/) and [Mercury MCP (official)](/tools/mercury-mcp/), which featured in earlier reports this month, remain **Verified**.

## How to use this report

A verified badge tells you a project is alive and its links worked in our last published check. It doesn't tell you the tool is secure, accurate or right for your use case. Read the code or docs, test with paper or sandbox accounts first, and keep credentials scoped.

For a ranked view of what's actively maintained, see the [weekly leaderboard](/weekly/). For a side-by-side starting point, try the [best AI tools for stock analysis](/compare/best-ai-tools-for-stock-analysis/) page, or browse [all tools](/tools/). Our [method article](/blog/we-re-check-104-finance-ai-tools-every-week/) explains how we assign the badges. The next scheduled weekly run is Monday, November 30, 2026.

*Data sources: published weekly run of November 18, 2026, 15:35 UTC (`data/history/2026-11-18.json`, commit `c4fb507`); published weekly run of November 23, 2026, 05:52 UTC (`data/history/2026-11-23.json`, `data/verification-report.json` checked_at 2026-11-23T05:52:54+00:00, commit `737e22a`); 11 November 2026 snapshot (`data/history/2026-11-11.json`) and unpublished November 16 totals from our previous report, included only as context; the November 23 public dataset ([tools.json](/tools.json) as published in that run, all 106 rows `checked_at` 2026-11-23) and the [latest verification](/verification/) page as of that run. Statuses are generated automatically from public repository, package-registry and link checks. Not financial advice.*
