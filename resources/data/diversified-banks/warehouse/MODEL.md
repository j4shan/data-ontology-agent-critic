# Bank Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices that were written separately: balance sheet and deposits, credit and loans, markets, capital, and expense. Question-to-column notes stay in `balance/coverage.md`, `credit/coverage.md`, `markets/coverage.md`.

| | |
| --- | ---: |
| Datasets | 114 |
| Relationships | 261 |
| Logical identities | 114 |

Snowflake database `BANK`, account `bank.us-east-1`. Node ids use the `sf:` prefix. Qualified names start with `bank.`.

## What the model covers

Balance sheet and deposits own geography, the client, the deposit product, and the rate path. Deposit balances, new accounts, spend, and stablecoin outflows are quantities. Deposit rates, betas, offered smart-cash rates, and the rate threshold are prices. Net interest income is an income result and does not store the deposit quantity or the deposit rate. Net interest margin does not store the earning-asset quantity.

Credit and loans own the loan product, the card program, and credit outcomes. Loan balances, card balances, pipelines, and maturity walls are quantities. Spreads, card yields, advance rates, and card fees are prices. A loss rate does not store the loan balance.

Markets, capital, and expense own desks, fee lines, capital constraints, and spending. Markets balance-sheet allocation, headcount, and lower-margin capacity are quantities. A premium-card annual fee and an open-banking fee are prices. Markets revenue does not store the allocated balance. AI spend is kept apart from the AI outcome.

A graph build of this directory reports 114 datasets, 261 relationships, no unknown claims, and no contradictory edges.
