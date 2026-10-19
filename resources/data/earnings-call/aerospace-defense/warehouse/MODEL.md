# Defense Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices: demand, supply, and price. Question-to-column notes stay in `demand/coverage.md`, `supply/coverage.md`, `price/coverage.md`.

| | |
| --- | ---: |
| Datasets | 78 |
| Relationships | 197 |
| Logical identities | 27 |

Snowflake database `DEFENSE`, account `defense.us-east-1`. Node ids use the `sf:defense` prefix. Qualified names start with `defense.`.

## What the model covers

Demand owns quantity facts. Those rows store demand quantity, not a price and not a capacity rating.

Supply owns capacity, installed base, workforce and operating capacity facts. A capacity row stores how much can be produced, moved, served or supported. It does not store the price of that unit.

Price owns revenue, yields or rates, margins, cost and cash dollars. A price row does not store the unit quantity. The denominator a price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate column, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`.

## Two-company design

Lockheed Martin programs (F-35, PAC-3, THAAD, helicopters, classified programs) use `dim_lmt_program` and Lockheed segment facts; RTX franchises (Pratt engines, Collins, Raytheon) use `dim_rtx_franchise` and RTX segment facts. The two companies' reportable-segment names live in separate `dim_lmt_segment` and `dim_rtx_segment` code lists. Each operating process (production, sustainment, shop visits, aftermarket, missile ramp, supplier capacity) has its own fact or service-stream dimension.

A scenario dimension with `reported` and `guide` replaces any guidance horizon on the fiscal-quarter dimension. Enterprise totals (revenue, operating income, cash flow, margin) are grained at the reporting unit or the reporting segment, not repeated on child program, product, park, content or transaction rows.

A graph build of this directory reports 78 datasets, 197 relationships, 27 logical identities, no unknown fields, and no contradictory edges. Coverage contains 74 headings, one for every numbered question in the two source question sheets.
