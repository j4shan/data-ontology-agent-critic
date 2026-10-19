# Energy Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices: demand, supply, and price. Question-to-column notes stay in `demand/coverage.md`, `supply/coverage.md`, `price/coverage.md`.

| | |
| --- | ---: |
| Datasets | 78 |
| Relationships | 206 |
| Logical identities | 33 |

Snowflake database `ENERGY`, account `energy.us-central-1`. Node ids use the `sf:energy` prefix. Qualified names start with `energy.`.

## What the model covers

Demand owns the customer, the geography, the calendar, and the quantity facts. Those rows store demand quantity, not a price and not a capacity rating.

Supply owns the capacity, the network or the asset base, and the operating constraints. A capacity row stores how much can be produced, moved, or built. It does not store the price of that unit.

Price owns yields, rates, margins, cost, and capital dollars. A price row does not store the unit quantity. The denominator a price needs (revenue ton-miles, megawatt-hours, barrels) is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate column, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`.

## Structural changes in this rebuild

- Replaced the mixed product list with separate upstream hydrocarbon (crude, natural gas, NGL), refined product, and chemical product dimensions.
- Production quantity is by hydrocarbon, field, play, asset, and country, with gross operated and net entitlement as separate measures. Field, play, asset (block or concession), project, and operator affiliate are separate dimensions, so Tengiz is a field, TCO is an operator affiliate, and a named offshore block is an asset rather than a play or project.
- Refinery throughput and utilization are by refinery; LNG production and capacity are by LNG terminal; chemical production and capacity are by chemical plant and chemical product. Those facility types are not one fact.
- Realized price stores realized, benchmark, and differential (realized minus benchmark) amounts and no production quantity; the production-quantity fact supplies the denominator by the shared grain keys.
- Segment earnings are dollar amounts by segment. Shareholder distributions and capital spending by project have their own facts, and free cash flow is corporate (fiscal quarter and scenario only), not keyed by play.
- Trading and supply optimization income has a fact by trading desk, market, and calendar month. A calendar-month dimension inside the fiscal quarter supports month-to-month comparisons. A scenario dimension with `reported` and `guide` replaces any guidance column on the fiscal-quarter dimension.

A graph build of this directory reports 78 datasets, 206 relationships, 33 logical identities, no unknown fields, and no contradictory edges.
