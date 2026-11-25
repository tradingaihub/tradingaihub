---
title: "Weekly Verification Report, November 9, 2026: One Comeback, One Slip, and a Quiet Week for 104 Finance AI Tools"
description: "The Nov 9, 2026 check: 81 of 104 finance AI tools verified, Valyu MCP back to Verified, Bankless Onchain MCP past the 180-day line, and three package releases."
date: 2026-11-10
tags: [verification, mcp, weekly-report]
tools: [valyu-mcp, bankless-onchain-mcp, norman-finance-mcp]
---
*Not financial advice. This report describes the maintenance status of software tools. It is not a recommendation to use, buy, sell or trade anything.*

Every week, TradingAIHub re-checks every listing in its directory of AI tools for finance and trading: MCP servers, agent skills and data APIs. This report covers the weekly check of **November 9, 2026** and compares it with the previous check on **November 2, 2026**, using the two versions of our public dataset ([tools.json](/tools.json)).

The short version: no tools were added or removed, the number of fully verified tools held steady at 81, and underneath that flat number two tools traded places.

## Status counts, week over week

| Status | Nov 2 check | Nov 9 check | Change |
|---|---|---|---|
| Verified | 81 | 81 | 0 |
| Under review | 3 | 3 | 0 |
| Not currently verified | 20 | 20 | 0 |
| **Total** | **104** | **104** | 0 |

You can see every row on the [latest verification](/verification/) page.

A quick reminder of what the statuses mean, from our [verification method](/about/): **Verified** means the repository is reachable, its links respond, and (for repos) it had a commit in the last 180 days. **Under review** means a listing is not currently counted as Verified; we re-check every listing weekly. **Not currently verified** covers listings with no commit in more than 180 days (180 to 365 days, or more than a year) and repositories archived by their owners.

## What improved: Valyu MCP comes back after a year without commits

The biggest move of the week is [Valyu MCP](/tools/valyu-mcp/), the official MCP server for Valyu's financial deep-research search platform, listed in our [research and filings category](/category/research-filings/).

Last week it was Not currently verified, with more than a year without a commit. This week the check found a new commit to its repository, and it moved straight to **Verified**. In the same check, the license we record for it changed from "unknown" to **MIT**, because we could now read a license from the repository.

That is exactly why we re-check weekly. A tool that looked abandoned last week can be actively maintained this week, and a list that was checked once would still be showing it as idle.

## What slipped: Bankless Onchain MCP crosses the 180-day line

[Bankless Onchain MCP](/tools/bankless-onchain-mcp/), which lets agents query onchain data and ERC-20 token information, moved from **Verified** to **Not currently verified**. Nothing broke. Its last commit is still dated May 5, 2026, and its npm package (`@bankless/onchain-mcp@1.0.6`) is still published. The repository simply crossed our 180-day line, with more than 180 days since its last commit.

A Not currently verified status is not a warning that a tool doesn't work. It is a signal to check the repository's issues and recent activity before you wire it into anything that matters. Other options are listed in our [crypto category](/category/crypto/) and the [crypto MCP servers comparison](/compare/crypto-mcp-servers/).

## A package note: Norman Finance MCP

[Norman Finance MCP](/tools/norman-finance-mcp/) keeps its **Verified** badge, with recent commits and an MIT license. Our package check currently records no npm or PyPI package for it at the repository root. Our package check only counts a package that is named in the repository and links back to it. If you install it from a package manager, confirm the package name against the project's own README. Related tools are in the [accounting category](/category/accounting/) and the [accounting MCP servers comparison](/compare/accounting-mcp-servers/).

## Package releases we picked up this week

Three tools shipped new package versions between the two checks:

- [Financial Modeling Prep MCP (community)](/tools/fmp-mcp-community/): `financial-modeling-prep-mcp-server` 2.8.0 to 2.9.0
- [Alpaca MCP Server](/tools/alpaca-mcp/): `alpaca-mcp-server` 2.4.0 to 2.4.1
- [Lunch Money MCP](/tools/lunchmoney-mcp/): `@akutishevsky/lunchmoney-mcp` 3.0.0 to 4.0.1

The Lunch Money MCP jump is a new major version. Under common semantic-versioning practice a major bump can include breaking changes, so if you depend on it, read the project's release notes before upgrading. These and similar tools are grouped in our [personal finance category](/category/personal-finance/).

## What didn't change

No tool was added or removed this week.

The three repositories archived by their owners are unchanged: Base MCP, Ramp MCP and MCP Trader. They won't get updates.

The three listings that were **Under review** are also unchanged: [OpenBB Platform (MCP)](/tools/openbb/), [Mercury MCP (official)](/tools/mercury-mcp/) and [Firefly III API](/tools/firefly-iii-api/). Under review is not a statement that a tool is down or unsafe.

The 12 listings with more than a year without a commit are the same set as last week. The four tools that were already between 180 and 365 days without a commit last week, MetaTrader 5 MCP, Crypto Indicators MCP, DexScreener Trending MCP and Actual Budget MCP, have had no new commits. Crypto Indicators MCP is the closest to the one-year mark.

## How to use this report

If you are picking an MCP server or agent skill to connect to a brokerage, data feed or accounting system, maintenance status is one input, not the whole decision. A verified badge tells you a project is alive and its links work. It doesn't tell you the tool is secure, accurate or right for your use case. Read the code or docs, test with paper or sandbox accounts first, and keep credentials scoped as tightly as the service allows.

For a ranked view of what's actively maintained, see the [weekly leaderboard](/weekly/). For side-by-side picks, start with the [best stock market MCP servers comparison](/compare/best-stock-market-mcp-servers/) or browse [all tools](/tools/).

*Data sources: TradingAIHub weekly checks of November 2 and November 9, 2026 ([public dataset](/tools.json), [latest verification](/verification/)). Statuses are generated automatically from public repository, package-registry and link checks. Not financial advice.*
