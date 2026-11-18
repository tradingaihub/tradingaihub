---
title: "MCP Supply-Chain Report, November 2026: 9 Packages We Couldn't Link Back to the Listed Repo"
description: "Of 106 tools in the Nov 11, 2026 published check, 29 packages link back to the listed repo and 9 packages we couldn't link back."
date: 2026-11-18
tags: [supply-chain, mcp, verification]
tools: [actual-budget-mcp, base-mcp, binance-mcp, bitcoin-mcp, ccxt-mcp, financial-datasets-mcp, finbrain-mcp, options-trading-skills, ramp-mcp, square-mcp, sure]
---
*Not financial advice. This report describes package-registry metadata for software tools. It is not a recommendation to use, buy, sell or trade anything.*

This is our first monthly MCP supply-chain report. Each week we check whether the npm or PyPI package named in a listed repository actually links back to that repository. Installing with `npx` or `pip` pulls whatever is published under that name, which is not always the code in the repository you just read.

The counts come from the published verification run on **November 11, 2026**, at 14:51 Asia/Jerusalem (12:51 UTC), in the site repository files `data/tools.json` and `data/verification-report.json`. The public export at [/tools.json](/tools.json) (CC BY 4.0) covers all 106 listings but does not yet include package-provenance fields, so the link-back results are taken from those verification records. We compare that run with November 2, 2026 (07:46 Asia/Jerusalem), the first weekly check after the directory reached 104 tools.

A brief we wrote earlier used the shorthand “10 of 104.” After manual review of the November 11 records, the number of **packages we couldn't link back to the listed repo** is **9**, and the directory now has **106** tools. The set is not the same as on November 2.

## At a glance

| | November 2, 2026 | November 11, 2026 (published) | Change |
|---|---|---|---|
| Package links back to the listed repo | 28 | 29* | +1 |
| Packages we couldn't link back to the listed repo | 10 | 9* | −1 |
| Repository, no package detected at repo root | 41 | 42 | +1 |
| No public repository (hosted APIs and similar) | 25 | 26 | +1 |
| Tools checked | 104 | 106 | +2 |

“Links back” means the name declared in the repository’s root `package.json` or `pyproject.toml` exists on npm or PyPI, and the registry metadata contains the listed `owner/repo`. Only those 29 packages are counted. A mismatch, or a missing package, never changes a tool’s maintenance badge on the [verification](/verification/) page.

## What changed

Two listings were added on November 11: [Sure](/tools/sure/), in [personal finance](/category/personal-finance/), and [CoinBoss API](/tools/coinboss-api/), a market-data API with no public repository.

The automated mismatch total stayed at 10 because one listing left the list and another joined it. Through November 9, the npm package `actual-budget-mcp` did not link back to the repository we listed for [Actual Budget MCP](/tools/actual-budget-mcp/), so we did not count it. In the published November 10–11 records the listed repository URL was updated, `actual-budget-mcp@0.12.0` is stored with `links_back: true`, and it is counted as linking back. [Sure](/tools/sure/) is the new row: the November 11 check found an npm package named `sure` that does not link to the repository we list.

Between November 2 and November 9 we also stopped detecting a published package at the repository root for Norman Finance MCP, so the counted total fell from 28 to 27 before Actual Budget MCP brought it back to 28. That change is not a mismatch: the later records say no package was detected at the repo root. No other listing entered or left the “couldn’t link back” set in this period.

## Current list: packages we couldn't link back to the listed repo

This is the full set after manual review of the November 11 published records. On November 18, 2026 we looked up the same package names on the public npm and PyPI registries to describe the metadata, not as a new directory-wide run. A mismatch is not an accusation. It can be a fork, a rename, a separate wrapper, missing metadata, or a name that already belonged to another project.

| Tool | Registry | Package | Listed repo | What we observed | In our records since |
|---|---|---|---|---|---|
| [Sure](/tools/sure/) | npm | `sure` | `we-promise/sure` | Metadata points to a different GitHub repository (`github.com/jntn/sure`). The package describes itself as a shell confirmation utility, not a personal-finance app. | November 11, 2026 |
| [Binance MCP (community)](/tools/binance-mcp/) | npm | `binance-mcp` | `TermiX-official/binance-mcp` | No repository link in the metadata. | October 29, 2026 |
| [Bitcoin & Lightning MCP](/tools/bitcoin-mcp/) | npm | `bitcoin-mcp` | `AbdelStark/bitcoin-mcp` | No repository link in the metadata. Our listing already notes to install from source. | October 29, 2026 |
| [Square MCP Server](/tools/square-mcp/) | npm | `square-mcp-server` | `square/square-mcp-server` | No repository link in the metadata. | November 2, 2026 |
| [Financial Datasets MCP](/tools/financial-datasets-mcp/) | PyPI | `mcp-server` | `financial-datasets/mcp-server` | A package with this generic name exists. No repository link in the metadata. | October 29, 2026 |
| [CCXT MCP](/tools/ccxt-mcp/) | PyPI | `mcp-server-ccxt` | `Nayshins/mcp-server-ccxt` | No repository link in the metadata. | October 29, 2026 |
| [Ramp MCP](/tools/ramp-mcp/) | PyPI | `ramp-mcp` | `ramp-public/ramp_mcp` | No repository link in the metadata. | October 29, 2026 |
| [FinBrain MCP](/tools/finbrain-mcp/) | PyPI | `finbrain-mcp` | `ahmetsbilgin/finbrain-mcp` | No repository link in the metadata. | October 29, 2026 |
| [Trading Skills for options traders (community)](/tools/options-trading-skills/) | PyPI | `trading-skills` | `staskh/trading_skills` | No repository link in the metadata. | November 2, 2026 |

Correction note: the automated 11 Nov 2026 run counted 10. On manual review, the npm package `base-mcp` declares github.com/base/base-mcp, which redirects (HTTP 301) to the listed base-mcp-legacy repository, so we count it as linked. Our checker now follows repository redirects. The November 11 figures marked * above include this review.

One of the nine has metadata that points at a different repository (Sure). The other eight have a registry entry and no repository link in the fields we check, so we cannot confirm the package belongs to the listed repo. “Since” is the first weekly snapshot in our history that already records the mismatch, not the first day the package existed.

## Methodology and limits

The check is in `scripts/verify.py` and runs with the rest of our [weekly verification](/verification/). For each listing with a public repository we read `package.json` at the repo root (skipping packages marked private) and `pyproject.toml`, take the declared name, and look it up on npm or PyPI. We then test whether the metadata contains the listed `owner/repo`: for npm, the `repository`, `homepage` and `bugs` fields; for PyPI, `project_urls`, `home_page` and `download_url`. If the links match, we store the name, version, publish date and registry URL, and count the package. If a package with that name exists but does not link back, we record that it “exists on the registry but does not link to this repo (not counted).” If no candidate is declared at the repo root, or the name is not on the registry, we record that no package was detected.

We do not check who controls the registry account, the published files, or install scripts. “Links back” means the metadata matched, not that the code was audited. Packages declared only in a subdirectory, or under a name missing from the root manifest, will not be detected. The November 16, 2026 weekly re-check was not published, so it is not used here. If you maintain one of the tools above, add the repository URL to the package metadata, publish a new version, or [submit a correction](/submit/).

Before running `npx` or `pip install` from a README, compare the package’s repository link with the repo you read. If the metadata has no repository link, or points somewhere else, install from the repository’s own instructions. See also the [latest verification run](/verification/), the [weekly leaderboard](/weekly/), and our [method article](/blog/we-re-check-104-finance-ai-tools-every-week/). We plan to publish this report monthly from the last published run of the month.

*Data sources: published verification records in the TradingAIHub site repository (`data/tools.json`, `data/verification-report.json`, and `data/history/`), from the runs of November 2, 2026, 07:46 Asia/Jerusalem; November 9, 2026, 07:50 Asia/Jerusalem; and November 11, 2026, 14:51 Asia/Jerusalem. Observation details in the mismatch table were checked against public npm and PyPI metadata on November 18, 2026. Directory data is offered under CC BY 4.0 with attribution to TradingAIHub. Not financial advice.*
