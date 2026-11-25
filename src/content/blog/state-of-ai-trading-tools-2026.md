---
title: "State of AI Trading Tools 2026: Security & Verification"
description: "At the Nov 23 check, 83 of 106 tools were Verified. Nov 11 snapshot: 14 repos idle a year, 25 can trade or move funds, 9 packages don't link back."
date: 2026-11-19
tags: [verification, security, mcp, supply-chain, data-report]
draft: false
---
*Not financial advice. This report describes the maintenance and security-check status of software tools. It is not a recommendation to use, buy, sell or trade anything, and it does not rate any tool as safe or unsafe to invest with.*

> **Key findings**
>
> - At the 23 Nov 2026 check, 83 of the 106 finance AI tools in the TradingAIHub directory were Verified. The findings below, unless dated otherwise, are the 11 Nov 2026 snapshot of 106 tools.
> - As of the 11 Nov 2026 check, 87 of the 106 finance AI tools (82%) were Verified: reachable, with working links and, for repositories, a commit in the last 180 days.
> - As of 11 Nov 2026, 58 of 62 official, vendor-maintained listings (94%) were Verified, compared with 29 of 44 community-maintained listings (66%).
> - As of 11 Nov 2026, 14 of the 80 listings with a readable GitHub repository had gone more than a year without a commit, while 40 had a commit in the previous 30 days.
> - As of 11 Nov 2026, 25 of 106 listings (24%) were flagged as able to place live trades or move funds.
> - As of the 10 Nov 2026 static scan, 79 of 106 listings carried a "no issues found" security-scan note, a point-in-time static check that is not a certification.
> - As of 11 Nov 2026, 9 npm or PyPI package names declared in listed repositories existed on the registry but did not link back to the listed repo, against 29 that did.
> - In the 11 Nov 2026 check, crypto was the least-maintained category, with 8 of 17 listings Verified (47%), against 20 of 22 in market data (91%).

AI assistants now connect to brokers, exchanges, payment processors and market-data feeds through MCP servers, agent skills and APIs. Many of those connectors are a few months old, maintained by one person, or installed with a single `npx` or `pip` command. We run a directory of these tools and re-check every listing each week, so we have a running record of how they are maintained. This report puts that record in one place.

Every number below comes from our own published data and is dated. The detailed tables in this report are the 11 November 2026 snapshot unless a later date is given. At the 23 November 2026 check, 83 of 106 listings were Verified. The [security scan](/security/) page is dated 10 November. The data is free to reuse under CC BY 4.0; see [Developers](/developers/) for the API and MCP server.

## Methodology and limits

**What we count.** The directory listed 106 tools on 11 November 2026: 74 MCP servers, 17 APIs and 15 agent skills, in nine categories. A listing is **official** when the company behind the service maintains it (62 listings) and **community** when anyone else does (44).

**Verification.** Every listing is re-checked each week. Our [method page](/about/) has the full rules. In short:

- **Verified**: the repository is reachable, the homepage and docs respond, any hosted MCP endpoint answers, and (for repositories) there was a commit in the last 180 days.
- **Under review**: the listing is not currently counted as Verified; we re-check every listing weekly.
- **Not currently verified**: no commit for more than 180 days (180 to 365 days, or more than a year), or a repository archived by its owner.

**Package provenance.** When a repository declares an npm or PyPI package, we check that the name exists on the registry and that the registry metadata points back to the listed `owner/repo`. Only packages that link back are counted.

**Security scan.** A static scanner reads package metadata, lockfiles and source text. It never installs or runs third-party code. It looks for install hooks, downloads piped to a shell, exfiltration patterns, typosquat risks and OSV advisories. Details are on the [security scan](/security/) page.

**Capability flags.** We flag a listing as able to place live trades or move funds when it can place real orders or send payments or transfer money. The flags come from each tool's own documentation.

**Limits.**

- **Snapshot date.** At the 23 November 2026 check, 83 of 106 listings were Verified. The detailed tables below remain the 11 November 2026 snapshot of 106 listings (87 Verified), unless a later date is given. Our [November 9 report](/blog/weekly-verification-report-2026-11-09/) covers the check before the 11 November snapshot.
- **Maintenance is not safety.** A recent commit means a project is maintained. It does not mean the code is safe, and an old commit does not mean it is unsafe.
- **The scan's reach.** A "no issues found" note covers only the checks listed above, on the scan date. We do not publish labels for tools that were not clean or not scanned, so the 27 listings without a note are not a group of flagged tools. Some have no public code and some were not scanned.
- **Approval defaults are not recorded.** Our dataset records *whether* a tool can trade or move money. It does not record whether orders need human confirmation by default, so we make no claim about that.
- **Our selection.** We list tools we find and vet, so this is a directory sample, not a census of every finance AI tool.

## Verification status over time

The table shows the status mix at each published check since 29 October 2026, when the first catalog batch took the directory to 104 listings.

| Check | Total | Verified | Under review | Not currently verified |
|---|---|---|---|---|
| 29 Oct 2026 (after batch 1) | 104 | 82 | 2 | 20 |
| 2 Nov 2026 | 104 | 81 | 3 | 20 |
| 9 Nov 2026 | 104 | 81 | 3 | 20 |
| 11 Nov 2026 | 106 | 87 | 0 | 19 |
| 18 Nov 2026 | 106 | 81 | 5 | 20 |
| 23 Nov 2026 | 106 | 83 | 3 | 20 |

Two things stand out. First, the Not currently verified group barely moves. Most of its 19 to 20 listings went quiet long before we started counting. Second, most of the week-to-week movement is in the Under review group.

## By type, and official vs community

| Group | Listings | Verified | Not currently verified | Security-scan note (10 Nov) | Live trading or moves funds |
|---|---|---|---|---|---|
| MCP servers | 74 | 58 (78%) | 16 | 52 | 21 |
| APIs | 17 | 17 (100%) | 0 | 16 | 0 |
| Agent skills | 15 | 12 (80%) | 3 | 11 | 4 |
| Official (vendor) | 62 | 58 (94%) | 4 | 49 | 18 |
| Community | 44 | 29 (66%) | 15 | 30 | 7 |
| **All** | **106** | **87 (82%)** | **19** | **79** | **25** |

Every API listing is official and hosted. Only one of the 17 has a public repository, so the commit-age rules rarely apply to them, and all 17 were Verified. MCP servers are where the maintenance gap shows: 16 of the 19 listings that are not Verified are MCP servers.

The official/community split is the clearest pattern in the data. Of the 15 community listings that are not Verified, 11 have gone more than a year without a commit, 3 have gone 180 to 365 days and 1 has a repository archived by its owner. On the official side, 2 of the 4 that are not Verified have repositories archived by their owners. Official status is no guarantee either way: a vendor can retire a project, and many community servers are actively maintained. There is more on this split in [official vs community finance MCP servers](/blog/official-vs-community-finance-mcp-servers/).

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

[Crypto](/category/crypto/) accounts for 9 of the 19 listings that are not Verified. It is also the category where trading and money-moving capabilities are most common: 6 of its 17 listings carry a capability flag. [Market data](/category/market-data/) is the opposite: mostly official, mostly hosted, none flagged for trading or moving funds, and 20 of 22 Verified. [Payments & banking](/category/payments-banking/) is all official, and 8 of its 10 listings can move funds.

## License distribution

As of 11 November 2026, 72 of 106 listings use an OSI-approved open-source license: MIT (54), Apache-2.0 (13), AGPL-3.0 (4) and MIT-0 (1). 26 are proprietary or governed by the provider's terms of service: 16 of the 17 APIs and 10 MCP servers. For 8 listings (5 MCP servers and 3 skills), we could not find a license in the repository and record it as **unknown**. Without a license, the default is that the code is not licensed for reuse, so builders who plan to fork or redistribute one of those should ask the maintainer first.

## Maintenance freshness

We read the date of the latest commit for the 80 listings with a GitHub repository we could read. The other 26 are hosted services with no public repository. Ages are counted to 11 November 2026.

| Last commit age | MCP servers | Skills | APIs | All |
|---|---|---|---|---|
| 0–30 days | 30 | 9 | 1 | 40 |
| 31–90 days | 14 | 1 | 0 | 15 |
| 91–180 days | 3 | 2 | 0 | 5 |
| 181–365 days | 6 | 0 | 0 | 6 |
| More than 365 days | 11 | 3 | 0 | 14 |
| **Total with repo data** | **64** | **15** | **1** | **80** |

Half the repositories (40 of 80) had a commit within a month, so this ecosystem moves fast. But 20 of 80 (25%) had nothing in over 180 days, and 14 had nothing in over a year. Three repositories have been archived by their owners. Their listings stay in the directory, so anyone who finds them through an old blog post or README can see that status.

## Packages and provenance

Installing an MCP server with `npx some-name` or `pip install some-name` pulls whatever is published under that name. That is not always the code in the repository you just read. In the 11 November data, 29 listed repositories declared a package that links back to them. For 9 more, the declared name existed on npm or PyPI, but the registry entry did not point to the listed repository. Usually that means someone else holds the name, or the project publishes under a different one. It is not, by itself, evidence of anything harmful, and we do not treat it as such.

Our companion piece, the first monthly [MCP Supply-Chain Report](/blog/mcp-supply-chain-report-1/) (November 2026), covers all 9 in detail.

## Security scan results

The [static scan](/security/) on 10 November 2026 gave 79 of 106 listings a "no issues found" note: 52 MCP servers, 16 APIs and 11 skills.

Separately, one listing has carried a public "Not safe" note since 11 November 2026. The note describes what we observed in the code: a wallet address and signed swap orders sent over unencrypted HTTP to an undocumented server. The note is a description of observed behavior, not a finding of intent.

## Trading and money-moving tools

As of 11 November 2026, 25 listings carry a capability flag: 21 MCP servers and 4 skills. 18 of the 25 are official.

In [Trading & brokers](/category/trading-brokers/), 9 of 11 listings are flagged for live trading. The other two are a paper-trading server and a market-data and portfolio skill pack.

What our data does not show is the permission model inside each tool: whether it defaults to read-only, whether orders need confirmation, or how API keys are scoped. We covered what brokers themselves publish about this in [brokers opening accounts to AI agents](/blog/brokers-ai-agents-mcp-permissions/). For the tools that place orders, compare our [best AI tools for options trading](/compare/best-ai-tools-for-options-trading/) page.

## What builders and users should check

**Before you connect a tool:**

1. **Check the last commit date and status.** A listing with no recent commits, or with an archived repository, may not get fixes for an API change or a security issue. Check the [verification page](/verification/) or the [weekly leaderboard](/weekly/).
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

The data is licensed under **CC BY 4.0**. Credit "TradingAIHub, https://tradingaihub.com" and note any changes. The dataset is at [/tools.json](/tools.json), and the API and MCP server are documented on [Developers](/developers/). Please cite figures with their date ("as of 11 Nov 2026" or "as of 23 Nov 2026"), because the data changes every week. The detailed tables in this report remain the 11 November snapshot unless marked otherwise. Corrections are welcome at hello@tradingaihub.com.
