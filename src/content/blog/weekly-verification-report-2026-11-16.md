---
title: "Weekly Verification Report, November 2026: Two New Listings and Four Status Upgrades"
description: "Sure and CoinBoss API join the directory and four listings move up to Verified. As of the 11 Nov update: 87 of 106 tools Verified, up from 81 of 104 on 9 Nov."
date: 2026-11-17
tags: [verification, mcp, weekly-report]
tools: [sure, coinboss-api, actual-budget-mcp, openbb, mercury-mcp, firefly-iii-api]
---
*Not financial advice. This report describes the maintenance status of software tools. It is not a recommendation to use, buy, sell or trade anything.*

This report covers what changed in the TradingAIHub directory between the weekly check of **November 9, 2026** and the update of **November 11, 2026**. Two listings were added, four listings moved up to Verified, and nothing moved down. The [latest verification](/verification/) page shows the current data for every listing.

## Status counts

| Status | Nov 9 check | Nov 11 update |
|---|---|---|
| Verified | 81 | 87 |
| Under review | 3 | 0 |
| Not currently verified | 20 | 19 |
| **Total listings** | **104** | **106** |

The 11 November directory had 74 MCP servers, 17 APIs and 15 agent skills, up one MCP server and one API from November 9.

From our [verification method](/about/): **Verified** means the repository is reachable, its links respond, and (for repos) it had a commit in the last 180 days. **Under review** means a listing is not currently counted as Verified; we re-check every listing weekly. **Not currently verified** covers listings with no commit in more than 180 days and repositories archived by their owners.

## What is new: Sure and CoinBoss API

Two listings were added on November 11, both **Verified**. None were removed.

[Sure](/tools/sure/), in our [personal finance category](/category/personal-finance/), is a self-hosted personal finance app: accounts, transactions, budgets and net worth, with a first-party MCP server and REST API. It is a community-maintained fork of Maybe Finance, licensed AGPL-3.0. Our package check did not count an npm package named `sure`, because the name exists on the registry but does not link back to this repository.

[CoinBoss API](/tools/coinboss-api/), in our [crypto category](/category/crypto/), is an official REST API for aggregated crypto derivatives and market data: liquidations, open interest, funding rates, long/short ratios and ETF flows. It is market data only. The listing records it as currently free, with paid plans listed as coming soon.

## What improved

Four listings moved up to **Verified** in the 11 November update.

[Actual Budget MCP](/tools/actual-budget-mcp/), the MCP server for the open-source Actual Budget app, in [personal finance](/category/personal-finance/), is the biggest maintenance move. On November 9 it was Not currently verified, with more than 180 days without a commit. After a new commit to its repository it moved to **Verified**. In the same update, the license we record changed from "unknown" to **MIT**, and the published package `actual-budget-mcp@0.12.0` was counted. See also Valyu MCP in our [November 9 report](/blog/weekly-verification-report-2026-11-09/).

The three listings that were **Under review** on November 9 are all **Verified** in the 11 November update:

- [OpenBB Platform (MCP)](/tools/openbb/), in [research and filings](/category/research-filings/), was marked Verified after a **manual check on November 11**.
- [Mercury MCP (official)](/tools/mercury-mcp/), in [payments and banking](/category/payments-banking/).
- [Firefly III API](/tools/firefly-iii-api/), in [personal finance](/category/personal-finance/).

## What didn't change

The three repositories archived by their owners are unchanged: Base MCP, Ramp MCP and MCP Trader.

The 12 listings with more than a year without a commit are the same set as on November 9. Four listings were between 180 and 365 days without a commit on November 11: Bankless Onchain MCP, MetaTrader 5 MCP, DexScreener Trending MCP and Crypto Indicators MCP. Crypto Indicators MCP is the closest to the one-year mark.

## How to use this report

A Verified badge tells you a project is alive and its links worked in our latest check. It doesn't tell you the tool is secure, accurate or right for your use case. Read the code or docs, test with paper or sandbox accounts first, and keep credentials scoped.

For a ranked view of what's actively maintained, see the [weekly leaderboard](/weekly/). For side-by-side picks, start with the [best AI tools for stock analysis](/compare/best-ai-tools-for-stock-analysis/) page or the [best stock market MCP servers comparison](/compare/best-stock-market-mcp-servers/), or browse [all tools](/tools/). Our [method article](/blog/we-re-check-104-finance-ai-tools-every-week/) explains how we assign the badges.

*Data sources: the TradingAIHub weekly check of November 9, 2026 and the update of November 11, 2026 ([public dataset](/tools.json), [latest verification](/verification/)). Statuses are generated automatically from public repository, package-registry and link checks. Not financial advice.*
