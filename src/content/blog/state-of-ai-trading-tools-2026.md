---
title: "State of AI Trading Tools 2026: Security & Verification"
description: "106 finance AI tools: 81 verified as of 18 Nov (87 on 11 Nov). As of 11 Nov: 14 repos idle a year, 25 can trade or move funds, 9 packages don't link back."
date: 2026-11-19
tags: [verification, security, mcp, supply-chain, data-report]
draft: false
---
*Not financial advice. This report describes the maintenance and security-check status of software tools. It is not a recommendation to use, buy, sell or trade anything, and it does not rate any tool as safe or unsafe to invest with.*

> **Key findings**
>
> - As of the 18 Nov 2026 published check, 81 of the 106 finance AI tools in the TradingAIHub directory (76%) were Verified. All 106 rows in the 18 Nov dataset carry that check date. The findings below, unless dated otherwise, are the 11 Nov 2026 snapshot.
> - As of the 11 Nov 2026 published check, 87 of the 106 finance AI tools (82%) were Verified: reachable, with working links and, for repositories, a commit in the last 180 days.
> - As of 11 Nov 2026, 58 of 62 official, vendor-maintained listings (94%) were Verified, compared with 29 of 44 community-maintained listings (66%).
> - As of 11 Nov 2026, 14 of the 80 listings with a readable GitHub repository had gone more than a year without a commit, while 40 had a commit in the previous 30 days.
> - As of 11 Nov 2026, 25 of 106 listings (24%) were flagged as able to place live trades or move funds: 16 for live trading, 15 for moving funds, and 6 for both.
> - As of the 10 Nov 2026 static scan, 79 of 106 listings carried a "no issues found" security-scan note, a point-in-time static check that is not a certification.
> - As of 11 Nov 2026, after manual review, 9 npm or PyPI package names declared in listed repositories existed on the registry but did not link back to the listed repo, against 29 that did.
> - In the 11 Nov 2026 check, crypto was the least-maintained category, with 8 of 17 listings Verified (47%), against 20 of 22 in market data (91%).

AI assistants now connect to brokers, exchanges, payment processors and market-data feeds through MCP servers, agent skills and APIs. Many of those connectors are a few months old, maintained by one person, or installed with a single `npx` or `pip` command. We run a directory of these tools and re-check every listing each week, so we have a running record of how they are maintained. This report puts that record in one place.

Every number below comes from our own published data and is dated. The public dataset at [/tools.json](/tools.json) and the [latest verification run](/verification/) now reflect the 18 November 2026 weekly run. The detailed tables in this report are the 11 November 2026 snapshot, taken from the 11 November records in our public [site repository](https://github.com/tradingaihub/tradingaihub) and its git history, unless a later date is given. The [security scan](/security/) page is dated 10 November. The data is free to reuse under CC BY 4.0; see [Developers](/developers/) for the API and MCP server.

## Methodology and limits

**What we count.** The directory listed 106 tools on 11 November 2026: 74 MCP servers, 17 APIs and 15 agent skills, in nine categories. A listing is **official** when the company behind the service maintains it (62 listings) and **community** when anyone else does (44).

**Verification.** Every Monday at 05:00 UTC a script checks each listing. Our [method page](/about/) has the full rules. In short:

- **Verified**: the repository is reachable, the homepage and docs respond, any hosted MCP endpoint answers, and (for repositories) there was a commit in the last 180 days.
- **Aging**: 180 to 365 days without a commit. **Stale**: more than 365 days.
- **Archived**: the repository is marked archived on GitHub.
- **Link check pending** (stored as `unconfirmed`): a link could not be confirmed automatically and is waiting for a re-check.

**Package provenance.** When a repository declares an npm or PyPI package in its root `package.json` or `pyproject.toml`, we check that the name exists on the registry and that the registry metadata points back to the listed `owner/repo`. Only packages that link back are counted.

**Security scan.** A static scanner reads package metadata, lockfiles and source text. It never installs or runs third-party code. It looks for install hooks, downloads piped to a shell, exfiltration patterns, typosquat risks and OSV advisories. Details are on the [security scan](/security/) page.

**Capability flags.** We flag a listing `live_trading` when it can place real orders and `moves_funds` when it can send payments or transfer money. The flags come from each tool's own documentation.

**Limits.**

- **Snapshot date.** The latest *published* data is from 18 November 2026, finished at 17:35 Asia/Jerusalem (15:35 UTC). All 106 rows in the 18 November dataset (`data/history/2026-11-18.json`) carry that check date: 81 Verified, 5 Aging, 12 Stale, 3 Archived, 3 Link check pending and 2 Check links. The detailed tables below remain the 11 November 2026 snapshot (87 Verified; most rows in that snapshot still carried a 9 November check date), unless a later date is given. The 16 November re-check finished, but its results were not published because of a build failure. We report only its status totals, taken from a run log that is not in the repository (there is no `data/history/2026-11-16.json`). Our [November 9 report](/blog/weekly-verification-report-2026-11-09/) covers the run before the 11 November snapshot.
- **Maintenance is not safety.** A recent commit means a project is maintained. It does not mean the code is safe, and an old commit does not mean it is unsafe.
- **The scan's reach.** A "no issues found" note covers only the checks listed above, on the scan date. We do not publish labels for tools that were not clean or not scanned, so the 27 listings without a note are not a group of flagged tools. Some have no public code, some were not scanned, and some had incomplete scans.
- **Approval defaults are not recorded.** Our dataset records *whether* a tool can trade or move money. It does not record whether orders need human confirmation by default, so we make no claim about that.
- **Our selection.** We list tools we find and vet, so this is a directory sample, not a census of every finance AI tool.

## Verification status over time

The directory launched on 29 October 2026 with 75 listings, 56 of them Verified. The first catalog batch the same day took it to 104. The table shows every published state since then, from the git history of `data/tools.json`, plus the unpublished 16 November totals (from a run log that is not in the repository) and the 18 November published run.

| Run | Total | Verified | Aging | Stale | Archived | Link check pending | Check links |
|---|---|---|---|---|---|---|---|
| 29 Oct 2026 (after batch 1) | 104 | 82 | 4 | 13 | 3 | 2 | 0 |
| 2 Nov 2026 | 104 | 81 | 4 | 13 | 3 | 3 | 0 |
| 9 Nov 2026 | 104 | 81 | 5 | 12 | 3 | 3 | 0 |
| 11 Nov 2026 | 106 | 87 | 4 | 12 | 3 | 0 | 0 |
| 16 Nov 2026 (run log, not published) | 106 | 82 | 5 | 12 | 3 | 3 | 1 |
| 18 Nov 2026 (latest published) | 106 | 81 | 5 | 12 | 3 | 3 | 2 |

Two things stand out. First, the stale and archived group barely moves. Of the 15 to 16 listings in it each week, most went quiet long before we started counting. Second, most of the week-to-week movement is in **Link check pending** and **Check links**, which reflect how a link responded to our checker on the day. On 11 November we changed the checker to send browser-like headers and to count an MCP sign-in response (HTTP 401/403) as reachable. Two listings moved to Verified after that change, and a third after a manual check. This was a change in how we check, not a change in the tools. In the 18 November published run, six listings left Verified: three moved to Link check pending, two to Check links, and one to Aging.

## By type, and official vs community

| Group | Listings | Verified | Not verified | Security-scan note (10 Nov) | Live trading or moves funds |
|---|---|---|---|---|---|
| MCP servers | 74 | 58 (78%) | 16 | 52 | 21 |
| APIs | 17 | 17 (100%) | 0 | 16 | 0 |
| Agent skills | 15 | 12 (80%) | 3 | 11 | 4 |
| Official (vendor) | 62 | 58 (94%) | 4 | 49 | 18 |
| Community | 44 | 29 (66%) | 15 | 30 | 7 |
| **All** | **106** | **87 (82%)** | **19** | **79** | **25** |

Every API listing is official and hosted. Only one of the 17 has a public repository, so the commit-age rules rarely apply to them, and all 17 were Verified. MCP servers are where the maintenance gap shows: 16 of the 19 listings that are not Verified are MCP servers.

The official/community split is the clearest pattern in the data. Of the 15 community listings that are not Verified, 11 are **Stale**, 3 are **Aging** and 1 is **Archived**. On the official side, 2 of the 4 that are not Verified are archived repositories. Official status is no guarantee either way: a vendor can archive a project, and many community servers are actively maintained. There is more on this split in [official vs community finance MCP servers](/blog/official-vs-community-finance-mcp-servers/).

## By category

| Category | Listings | Verified | Official | Can trade or move funds |
|---|---|---|---|---|
| Market data | 22 | 20 | 15 | 0 |
| Crypto | 17 | 8 | 9 | 6 |
| Trading & brokers | 11 | 9 | 7 | 9 |
| Quant & backtesting | 11 | 9 | 3 | 2 |
| Research & filings | 10 | 9 | 3 | 0 |
| Payments & banking | 10 | 9 | 10 | 8 |
| Accounting | 9 | 8 | 7 | 0 |
| Macro | 8 | 8 | 6 | 0 |
| Personal finance | 8 | 7 | 2 | 0 |

[Crypto](/category/crypto/) accounts for 9 of the 19 listings that are not Verified: 7 Stale or Aging community MCP servers, plus one Aging and one Archived official server. It is also the category where trading and money-moving capabilities overlap most: 6 of its 17 listings carry a capability flag, often both. [Market data](/category/market-data/) is the opposite: mostly official, mostly hosted, read-only, and 20 of 22 Verified. [Payments & banking](/category/payments-banking/) is all official, and 8 of its 10 listings can move funds.

## License distribution

As of 11 November 2026, 72 of 106 listings use an OSI-approved open-source license: MIT (54), Apache-2.0 (13), AGPL-3.0 (4) and MIT-0 (1). 26 are proprietary or governed by the provider's terms of service: 16 of the 17 APIs and 10 MCP servers, usually hosted endpoints. For 8 listings (5 MCP servers and 3 skills), we could not find a license in the repository and record it as **unknown**. Without a license, the default is that the code is not licensed for reuse, so builders who plan to fork or redistribute one of those should ask the maintainer first.

## Maintenance freshness

We read the date of the latest commit for the 80 listings with a GitHub repository the checker could read. The other 26 are hosted services with no public repository. Ages are counted to 11 November 2026.

| Last commit age | MCP servers | Skills | APIs | All |
|---|---|---|---|---|
| 0–30 days | 30 | 9 | 1 | 40 |
| 31–90 days | 14 | 1 | 0 | 15 |
| 91–180 days | 3 | 2 | 0 | 5 |
| 181–365 days | 6 | 0 | 0 | 6 |
| More than 365 days | 11 | 3 | 0 | 14 |
| **Total with repo data** | **64** | **15** | **1** | **80** |

Half the repositories (40 of 80) had a commit within a month, so this ecosystem moves fast. But 20 of 80 (25%) had nothing in over 180 days, and 14 had nothing in over a year. Three repositories are archived on GitHub. Their listings stay in the directory, so anyone who finds them through an old blog post or README can see that status.

## Packages and provenance

Installing an MCP server with `npx some-name` or `pip install some-name` pulls whatever is published under that name. That is not always the code in the repository you just read. In the 11 November data, after manual review, 29 listed repositories declared a package that links back to them. For 9 more, the declared name existed on npm or PyPI, but the registry entry did not point to the listed repository. Usually that means someone else holds the name, or the project publishes under a different one. It is not, by itself, evidence of anything harmful, and we do not treat it as such.

Our companion piece, the first monthly [MCP Supply-Chain Report](/blog/mcp-supply-chain-report-1/) (November 2026), covers all 9 in detail.

## Security scan results

The [static scan](/security/) on 10 November 2026 (scanner commit `bce7a11`, rules version 6) gave 79 of 106 listings a "no issues found" note: 52 MCP servers, 16 APIs and 11 skills. Seventy of those 79 are also Verified. That leaves 9 listings with a clean scan result but a maintenance status of Stale, Aging or Archived. That's a reminder that the two checks answer different questions.

Separately, one listing has carried a public **"Not safe, pending clarification"** note since 11 November 2026. The note describes what we observed in the code: a wallet address and signed swap orders sent over unencrypted HTTP to an undocumented server. We have asked the developer about it. The note is a description of observed behavior pending an answer, not a finding of intent.

## Trading and money-moving tools

As of 11 November 2026, 25 listings carry a capability flag: 21 MCP servers and 4 skills. 16 can place live trades, 15 can move funds, and 6 can do both. 18 of the 25 are official. 22 are Verified, and 15 have a "no issues found" scan note.

In [Trading & brokers](/category/trading-brokers/), 9 of 11 listings are flagged for live trading. The other two are a paper-trading server and a market-data and portfolio skill pack. Hosted endpoints show a clear auth pattern. Of the 15 listings with a remote MCP endpoint, 12 required sign-in when our checker called them. 11 of those advertised OAuth protected-resource metadata, and the other one asked for authentication without it. The remaining 3 answered an unauthenticated `initialize` request.

What our data does not show is the permission model inside each tool: whether it defaults to read-only, whether orders need confirmation, or how API keys are scoped. We covered what brokers themselves publish about this in [brokers opening accounts to AI agents](/blog/brokers-ai-agents-mcp-permissions/). For the tools that place orders, compare our [best AI tools for options trading](/compare/best-ai-tools-for-options-trading/) page.

## What builders and users should check

**Before you connect a tool:**

1. **Check the last commit date and status.** A Stale or Archived listing may not get fixes for an API change or a security issue. Check the [verification page](/verification/) or the [weekly leaderboard](/weekly/).
2. **Match the package to the repo.** Before running `npx` or `pip install`, open the package's registry page and confirm its repository link is the repo you read. If not, install from the repository's own instructions.
3. **Check the capability.** If a tool can place orders or move money, start with a paper or sandbox account, use API keys with the narrowest scope the provider offers, and check whether orders need confirmation.
4. **Prefer a known license.** An "unknown" license limits what you can legally fork or ship.
5. **Treat scan notes as one input.** A "no issues found" note is static and dated. Read the code yourself, especially for tools that touch money.

**If you maintain a tool:**

- Add `repository` metadata to your npm or PyPI package that points to the canonical repo.
- Put a license file in the repository root.
- Document default permissions plainly: read-only or trading, confirmation on or off, and the key scopes required.
- If a project is finished or replaced, archive it and say where users should go. You can update your listing through [submit a tool](/submit/).

## How to cite

Suggested citation:

> TradingAIHub Editorial. "State of AI Trading Tools 2026: Security & Verification." TradingAIHub, 19 November 2026. https://tradingaihub.com/blog/state-of-ai-trading-tools-2026/

The data is licensed under **CC BY 4.0**. Credit "TradingAIHub, https://tradingaihub.com" and note any changes. The dataset is at [/tools.json](/tools.json), a summary table of the figures in this report is at [/data/state-2026-summary.csv](/data/state-2026-summary.csv), and the API and MCP server are documented on [Developers](/developers/). Please cite figures with their date ("as of 11 Nov 2026" or "as of 18 Nov 2026"), because the data changes every week. The detailed tables in this report remain the 11 November snapshot unless marked otherwise. We plan to update this report as new runs are published. Corrections are welcome at hello@tradingaihub.com.
