# Payments Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices: demand, supply, and price. Question-to-column notes stay in `demand/coverage.md`, `supply/coverage.md`, `price/coverage.md`.

| | |
| --- | ---: |
| Datasets | 74 |
| Relationships | 202 |
| Logical identities | 25 |

Snowflake database `PAYMENTS`, account `payments.us-east-1`. Node ids use the `sf:payments` prefix. Qualified names start with `payments.`.

## What the model covers

Demand owns quantity facts. Those rows store demand quantity, not a price and not a capacity rating.

Supply owns capacity, installed base, workforce and operating capacity facts. A capacity row stores how much can be produced, moved, served or supported. It does not store the price of that unit.

Price owns revenue, yields or rates, margins, cost and cash dollars. A price row does not store the unit quantity. The denominator a price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate column, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`.

## Two-company design

Credit versus debit is `dim_card_type`, domestic versus cross-border is `dim_cross_border_type` with corridor, value-added services are `dim_value_added_service`, and client incentives are separate price facts. Every generic volume, capacity and revenue fact carries `dim_reporting_unit` (Mastercard, Visa) so a row can be traced to the business that produced it; neither company's segment names are mixed into a shared code list.

A scenario dimension with `reported` and `guide` replaces any guidance horizon on the fiscal-quarter dimension. Enterprise totals (revenue, operating income, cash flow, margin) are grained at the reporting unit or the reporting segment, not repeated on child program, product, park, content or transaction rows.

A graph build of this directory reports 74 datasets, 202 relationships, 25 logical identities, no unknown fields, and no contradictory edges. Coverage contains 71 headings, one for every numbered question in the two source question sheets.
