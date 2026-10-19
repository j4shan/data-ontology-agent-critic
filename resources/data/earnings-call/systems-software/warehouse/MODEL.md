# Platform Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices: demand, supply, and price. Question-to-column notes stay in `demand/coverage.md`, `supply/coverage.md`, `price/coverage.md`.

| | |
| --- | ---: |
| Datasets | 76 |
| Relationships | 192 |
| Logical identities | 26 |

Snowflake database `PLATFORM`, account `platform.us-west-1`. Node ids use the `sf:platform` prefix. Qualified names start with `platform.`.

## What the model covers

Demand owns quantity facts. Those rows store demand quantity, not a price and not a capacity rating.

Supply owns capacity, installed base, workforce and operating capacity facts. A capacity row stores how much can be produced, moved, served or supported. It does not store the price of that unit.

Price owns revenue, yields or rates, margins, cost and cash dollars. A price row does not store the unit quantity. The denominator a price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate column, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`.

## Two-company design

Microsoft Azure consumption, Microsoft 365 Copilot seats, gaming and segment facts use Microsoft product and segment dimensions; ServiceNow workflow subscriptions, Now Assist, Control Tower and autonomous-workforce rows use `dim_now_product`. Subscription quantity, cloud capacity, and price or margin stay on separate facts, and reporting unit traces generic rows to Microsoft or ServiceNow.

A scenario dimension with `reported` and `guide` replaces any guidance horizon on the fiscal-quarter dimension. Enterprise totals (revenue, operating income, cash flow, margin) are grained at the reporting unit or the reporting segment, not repeated on child program, product, park, content or transaction rows.

A graph build of this directory reports 76 datasets, 192 relationships, 26 logical identities, no unknown fields, and no contradictory edges. Coverage contains 69 headings, one for every numbered question in the two source question sheets.
