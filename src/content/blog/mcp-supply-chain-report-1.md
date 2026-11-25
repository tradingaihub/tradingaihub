---
title: "MCP Supply-Chain Report, November 2026: 9 Packages We Couldn't Link Back to the Listed Repo"
description: "On our verification page, 30 listings have a package that links back to the listed repo and 9 list a package name we couldn't link back."
date: 2026-11-18
tags: [supply-chain, mcp, verification]
tools: [base-mcp, binance-mcp, bitcoin-mcp, ccxt-mcp, financial-datasets-mcp, finbrain-mcp, options-trading-skills, ramp-mcp, square-mcp, sure]
---
*Not financial advice. This report describes package-registry metadata for software tools. It is not a recommendation to use, buy, sell or trade anything.*

This is our first monthly MCP supply-chain report. Each week we check whether the npm or PyPI package named in a listed repository actually links back to that repository. Installing with `npx` or `pip` pulls whatever is published under that name, which is not always the code in the repository you just read.

The figures in this report come from our [latest verification](/verification/) page and the public API export at [/api/v1/tools.json](https://tradingaihub.com/api/v1/tools.json) (CC BY 4.0). There, **30 listings** have a counted package that links back to the listed repo, and **9 listings** have a package name on npm or PyPI that we couldn't link back to the listed repo. In the November 11, 2026 published check of 106 tools, the counts were 29 and 9.

“Links back” means the package named in the repository exists on npm or PyPI and the registry metadata contains the listed `owner/repo`. Only those packages are counted. A mismatch, or a missing package, never changes a tool's maintenance status on the [verification](/verification/) page.

## Current list: packages we couldn't link back to the listed repo

This is the full set shown on the verification page as of November 25, 2026. A mismatch is not an accusation. It can be a fork, a rename, a separate wrapper, missing metadata, or a name that already belonged to another project.

| Tool | Registry | Package name | Listed repo | Maintenance status |
|---|---|---|---|---|
| [Sure](/tools/sure/) | npm | `sure` | `we-promise/sure` | Verified |
| [Binance MCP (community)](/tools/binance-mcp/) | npm | `binance-mcp` | `TermiX-official/binance-mcp` | Not currently verified |
| [Base MCP](/tools/base-mcp/) | npm | `base-mcp` | `base/base-mcp-legacy` | Not currently verified (repository archived by its owner) |
| [Square MCP Server](/tools/square-mcp/) | npm | `square-mcp-server` | `square/square-mcp-server` | Verified |
| [Financial Datasets MCP](/tools/financial-datasets-mcp/) | PyPI | `mcp-server` | `financial-datasets/mcp-server` | Not currently verified |
| [CCXT MCP](/tools/ccxt-mcp/) | PyPI | `mcp-server-ccxt` | `Nayshins/mcp-server-ccxt` | Not currently verified |
| [Ramp MCP](/tools/ramp-mcp/) | PyPI | `ramp-mcp` | `ramp-public/ramp_mcp` | Not currently verified (repository archived by its owner) |
| [FinBrain MCP](/tools/finbrain-mcp/) | PyPI | `finbrain-mcp` | `ahmetsbilgin/finbrain-mcp` | Verified |
| [Trading Skills for options traders (community)](/tools/options-trading-skills/) | PyPI | `trading-skills` | `staskh/trading_skills` | Verified |

On the verification page each of these nine listings carries the same note: the registry name exists but does not link to the listed repository, so the package is not counted. Separately, [Bitcoin & Lightning MCP](/tools/bitcoin-mcp/) carries a note that its npm package is currently unmaintained and that you should install from source.

## Methodology and limits

For each listing with a public repository, we read the package declared in the repository and look it up on npm or PyPI. We then test whether the registry metadata links to the listed `owner/repo`. If the links match, we store the name and latest version and count the package. If a package with that name exists but does not link back, we record that it “exists on the registry but does not link to this repo (not counted).” If no package is declared in the repository, or the name is not on the registry, we record that no package was detected.

We do not check who controls the registry account, the published files, or install scripts. “Links back” means the metadata matched, not that the code was audited. Packages declared only in a subdirectory will not be detected. If you maintain one of the tools above, add the repository URL to the package metadata, publish a new version, or [submit a correction](/submit/).

Before running `npx` or `pip install` from a README, compare the package's repository link with the repo you read. If the metadata has no repository link, or points somewhere else, install from the repository's own instructions. See also the [latest verification](/verification/), the [weekly leaderboard](/weekly/), and our [method article](/blog/we-re-check-104-finance-ai-tools-every-week/). We plan to publish this report monthly.

*Data sources: the TradingAIHub public dataset ([tools.json](/tools.json), [API export](https://tradingaihub.com/api/v1/tools.json)) and the [latest verification](/verification/) page as of November 25, 2026. Directory data is offered under CC BY 4.0 with attribution to TradingAIHub. Not financial advice.*
