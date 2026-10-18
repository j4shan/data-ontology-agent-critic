# Railroad Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices that were written separately: demand, supply, and price. Question-to-column notes stay in `demand/coverage.md`, `supply/coverage.md`, `price/coverage.md`.

| | |
| --- | ---: |
| Datasets | 119 |
| Relationships | 245 |
| Logical identities | 119 |

Snowflake database `RAILROAD`, account `railroad.us-central-1`. Node ids use the `sf:railroad` prefix. Qualified names start with `railroad.`.

## What the model covers

Demand owns the customer, the geography, the calendar, and the quantity facts. Those rows store units, loads, or barrels, not a price and not a capacity rating.

Supply owns the capacity, the network or the asset base, and the operating constraints. A capacity row stores how much can be produced, moved, or built. It does not store the price of that unit.

Price owns yields, rates, margins, cost, and capital dollars. A price row does not store the unit quantity. Agreed cost stays on the cost fact. It is not copied onto the demand fact.

A graph build of this directory reports 119 datasets, 245 relationships, no unknown claims, and no contradictory edges.
