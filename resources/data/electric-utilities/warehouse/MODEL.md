# Utility Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices that were written separately: demand, supply, and price. Question-to-column notes stay in `demand/coverage.md`, `supply/coverage.md`, `price/coverage.md`.

| | |
| --- | ---: |
| Datasets | 90 |
| Relationships | 204 |
| Logical identities | 90 |

Snowflake database `UTILITY`, account `utility.us-east-1`. Node ids use the `sf:utility` prefix. Qualified names start with `utility.`.

## What the model covers

Demand owns the customer, the geography, the calendar, and the quantity facts. Those rows store demand quantity, not a price and not a capacity rating.

Supply owns the capacity, the network or the asset base, and the operating constraints. A capacity row stores how much can be produced, moved, or built. It does not store the price of that unit.

Price owns yields, rates, margins, cost, and capital dollars. A price row does not store the unit quantity. Agreed cost stays on the cost fact. It is not copied onto the demand fact.

A graph build of this directory reports 90 datasets, 204 relationships, no unknown claims, and no contradictory edges.
