# Bank Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from 3 subject slices that were written separately. Question-to-column notes stay in `balance/coverage.md`, `credit/coverage.md`, `markets/coverage.md`.

| | |
| --- | ---: |
| Datasets | 74 |
| Relationships | 172 |
| Logical identities | 22 |

Snowflake database `BANK`, account `bank.us-east-1`. Node ids use the `sf:bank` prefix. Qualified names start with `bank.`.

## What the model covers

Every fact grain is the natural combination of fiscal quarter, scenario, and the business keys named in its grain description; a surrogate column is never the grain. The scenario dimension carries `reported` and `guide`, so the same fiscal quarter can be both a reported result and a later guide, and the fiscal-quarter dimension has no `guidance_horizon` column. Demand quantity, supply or capacity, and price or margin stay on separate facts: a quantity fact does not store a price, and a price fact does not store the unit quantity; the denominator a price needs is a quantity measure on its own fact joined by the shared grain keys. No column is an analyst-conclusion flag; operational classifications are dimension codes, and measure descriptions name their unit.

A graph build of this directory reports 74 datasets, 172 relationships, no unknown claims, and no contradictory edges.
