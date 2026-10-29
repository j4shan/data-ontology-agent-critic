# Halyard Securities

Halyard Securities is a fictional US retail brokerage. Self-directed and broker-serviced customers trade listed equities through web, mobile, API, and branch channels. The firm routes orders to exchanges and wholesalers, settles trades T+1, lends on margin, sweeps idle cash to program banks, lends fully paid shares, and reports to FINRA, the SEC, the IRS, and the Consolidated Audit Trail. An integration pipeline loads the operational data and purchased marketing data into a Snowflake warehouse every night, and analytic marts in that warehouse serve finance, sales, compliance, and execution-quality reporting.

The catalog `securities-brokerage` is a schema version 4 intermediary for the actor's graph builder. It has 114 datasets, 893 columns, 51 logical entities, and 296 entity definitions. The actor derives 1,578 relationships from those definitions.

## Why this domain

The goal was a business domain with sophisticated operational and analytic data warehouses whose schema has already been used for benchmarking. The candidates considered were:

| Candidate | Benchmark use | Shape | Decision |
| --- | --- | --- | --- |
| Retail brokerage: [TPC-E](https://www.tpc.org/tpce/) operational schema and the [TPC-DI](https://www.tpc.org/tpcdi/) warehouse loaded from it | TPC OLTP and data-integration benchmarks; TPC-DI is also a [DW-Bench](https://arxiv.org/html/2604.18964) dataset | 33 normalized OLTP tables, a 20-table snowflake-style warehouse with Type 2 history, and its source files | **Chosen** |
| Retail decision support: [TPC-DS](https://www.tpc.org/tpcds/) | TPC and DW-Bench | 24-table star schema with no operational layer | Overlaps `retail-grocery` |
| Manufacturing and sales: AdventureWorks and AdventureWorksDW | DW-Bench | 102 tables across OLTP and DW | Overlaps `manufacturing-discrete` and `commerce-marketplace` |
| Wholesale distribution: [Wide World Importers](https://learn.microsoft.com/en-us/sql/samples/wide-world-importers-dw-database-catalog) OLTP and DW | Microsoft reference sample | Normalized OLTP plus an 8-dimension, 6-fact star | Thin warehouse |
| Observational health: OMOP CDM | DW-Bench | 37 tables | Overlaps `healthcare-payer` |
| Financial crime: [LDBC FinBench](https://ldbcouncil.org/post/announcing-the-official-release-of-ldbc-financial-benchmark/) | LDBC graph benchmark | Property graph | Not a relational warehouse |
| Enterprise text-to-SQL: [BEAVER](https://arxiv.org/html/2409.02038) | Text-to-SQL benchmark | Private warehouses averaging 101.5 tables | Schemas are not public |

The brokerage pair is the only candidate where one benchmark defines the operational system and another defines the warehouse loaded from it. That makes cross-layer relationships, surrogate keys, history, and load lag first-class rather than invented. It is also a domain with many identities that recur across subject areas: customers, accounts, securities, trades, orders, and dates. No current assessment domain covers capital markets.

## Layers

| Layer | Accessor | Node prefix | Schemas | Datasets |
| --- | --- | --- | --- | ---: |
| Operational | `accessor.sql-database.v1`, PostgreSQL `brokerage` on `oltp.halyard.internal` | `sql-database:` | `reference`, `market`, `customer`, `trading`, `oms`, `risk`, `cashier`, `compliance`, `firm`, `service`, `tax` | 66 |
| Landing | `accessor.s3.v1`, bucket `halyard-di-landing` | `s3:` | `landing` | 11 |
| Warehouse | `accessor.snowflake.v1`, database `SECURITIES_BROKERAGE` on account `halyard.us-east-1` | `snowflake:` | `dw`, `mart` | 37 |

Qualified names are `securities-brokerage.<schema>.<dataset>`. Node IDs follow the actor rule `<accessor-family>:<qualified name>`.

## Subject areas

| Schema | Source | Datasets |
| --- | --- | --- |
| `reference` | TPC-E fixed tables, plus `customer_tier` | Zip codes, addresses, status types, tax rates, trade types, charges, commission schedule, exchanges, sectors, industries |
| `market` | TPC-E market tables, plus extensions | Companies, competitors, securities, daily market, last trade, financials, news; extensions: security identifiers (CUSIP, ISIN, FIGI, SEDOL), corporate actions, account entitlements |
| `customer` | TPC-E | Customers, customer tax rates, accounts, account permissions, watch lists, brokers |
| `trading` | TPC-E | Trades, trade history, pending trade requests, settlement, cash ledger, tax lots, lot history, position summary |
| `oms` | Extension | Customer orders, order events, routes, venue executions with NBBO at receipt, execution venues by MIC, exchange calendar |
| `risk` | Extension | Margin accounts, margin calls, daily account risk, cash sweep balances, fully paid securities loans |
| `cashier` | Extension | Bank links, ACH and wire transfers, ACATS transfers and their asset lines |
| `compliance` | Extension | KYC reviews, AML alerts and cases, trade surveillance alerts, FINRA 4530 complaints, CAT events |
| `firm`, `service`, `tax` | Extension | Branches, employees and managers, registrations; statements, digital sessions, service contacts; lot-level realized gains, 1099 forms |
| `landing` | TPC-DI source files | CustomerMgmt XML, HR, FINWIRE company, security, and financial records, and the DailyMarket, Trade, CashTransaction, HoldingHistory, WatchHistory, and Prospect feeds |
| `dw` | TPC-DI warehouse | Date, time, customer, account, broker, company, security, and trade dimensions; cash balance, holdings, market history, and watch facts; prospect, financial, and reference copies; DImessages and Audit |
| `mart` | Extension | Account daily snapshot, daily revenue, margin exposure, customer month, broker month, Rule 605 execution quality, Rule 606 routing, net new assets, digital engagement, surveillance, AML, complaints, corporate action impact |

## Modeling notes

Relationships are not written by hand. Each entity definition states whether its key is `unique`, `total`, and `conforms`, and whether the dataset holds the `complete` population. The actor derives one relationship for every two definitions of the same logical entity. The claims follow the benchmark rules where the benchmarks state them, for example:

- Every customer has at least one account, one watch list, and two tax rates, and every trade has a status history. Those foreign keys are `complete`, so the derived match from the parent side is `always`.
- Every trade is booked from an order, but an order has no trade until its first fill: `customer_order.ord_t_id` is `complete`, `unique`, and not `total`.
- Warehouse dimensions carry a durable natural key and a version surrogate key as separate logical entities, such as `customer_identity` and `customer_version_identity`. The natural key is `partial` because the warehouse loads nightly. Facts join on the surrogate key, and the customer and broker marts join on the durable key.
- `position_identity` is the composite key of account and security. It is complete on `holding_summary` and on the tax lots, and partial on entitlements and securities loans. `account_day_identity` is the composite key of account version and date across the account-day marts.
- Several datasets realize one entity in more than one role: competitor pairs, an employee and their manager, the opening and the changing trade of a lot, the security and the successor in a merger, and the trade, 52-week high, and 52-week low dates in market history. The actor reports 255 such groups where one key reaches several columns of the same dataset.
- FINWIRE security and financial records name the issuer in a field that holds either a CIK or a company name. That realization's `conforms` claim is `unknown`.
- `di_messages` and `audit` have no entity definitions. They relate to the rest of the warehouse only through `batch_id`, as in TPC-DI, so they are isolated nodes.

TPC-DI's prescribed source formats are kept. Each landing feed has its own S3 prefix. The three FINWIRE record types share one prefix because they share files.

## Imperfect knowledge

`build_catalog.py` applies a seeded forget pass after it builds the full catalog. With seed `20261029`, it removes 5 percent of the non-empty descriptive fields: 81 of 1,620. Eligible fields are dataset descriptions and synonyms, grain descriptions, column descriptions, value descriptions, and synonyms, entity-definition descriptions, and logical-entity descriptions and synonyms. Names, keys, accessors, grains, and entity claims are never removed, so the derived relationship graph is the same with or without the pass.

| Field | Removed |
| --- | ---: |
| Column description | 44 |
| Column value description | 18 |
| Dataset description | 7 |
| Dataset synonyms | 3 |
| Entity-definition description | 4 |
| Grain description | 4 |
| Logical-entity description | 1 |

`forget-log.yaml` records every removed value with its file and location. It is the answer key for scoring what an agent recovers. It is not builder input.

## Files

| Path | Contents |
| --- | --- |
| `directory-manifest.yaml` | Schema version 4 directory manifest. |
| `yaml/` | One logical-entities file and one node file per layer and schema. It contains only `.yaml` files. |
| `forget-log.yaml` | Seed, rate, counts, and every forgotten value. |
| `catalog_source.py` | Authoring source: logical entities and every dataset, column, key, and claim. |
| `build_catalog.py` | Generator and forget pass. |
| `questions.md` | Role-based analytical questions for the benchmark. |

Regenerate from this directory with `python3 build_catalog.py`. The output is deterministic. To check it against the actor, load `yaml/` with the actor's `build_snapshot_from_yaml` from a separate environment. Critic code never imports the actor.

## Sources

- TPC Benchmark E Standard Specification, version 1.14.0, [tpc.org](https://www.tpc.org/tpc_documents_current_versions/pdf/tpc-e_v1.14.0.pdf).
- M. Poess et al., "TPC-DI: The First Industry Benchmark for Data Integration," PVLDB 7(13), 2014, [vldb.org](http://www.vldb.org/pvldb/vol7/p1367-poess.pdf).
- [TPC-DI benchmark overview](https://benchbox.dev/docs/benchmarks/tpc-di.html), for the warehouse table inventory and Type 2 dimensions.
- SEC Rules 605 and 606, FINRA Rules 4210 (margin) and 4530 (complaints), and the CAT NMS Plan, for the extension marts and compliance datasets.

The company, people, hosts, and accounts are fictional.
