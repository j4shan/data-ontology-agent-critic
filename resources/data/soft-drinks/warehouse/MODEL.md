# Beverage Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from 3 subject slices that were written separately: demand and channel, bottler and commodity supply, price, mix, and margin. Question-to-column notes stay in `demand_channel/coverage.md`, `supply_bottler/coverage.md`, `price_margin/coverage.md`.

| | |
| --- | ---: |
| Datasets | 105 |
| Relationships | 312 |
| Logical identities | 105 |

Snowflake database `BEVERAGE`, account `beverage.us-east-1`. Node ids use the `sf:` prefix. Qualified names start with `beverage.`.

## What the model covers

Demand and channel own Beverage Inc brands, packs, countries, and unit cases. Coca-Cola, Coke Zero, Diet Coke, fairlife, Pepsi, Mountain Dew, and Frito-Lay are brands in this catalog. A unit-case row does not store a price.

Bottler and commodity supply own plants, bottler execution slots, locked commodity cover, and service fill. Cover is capacity. It is not the commodity price.

Price, mix, and margin own price/mix, organic sales growth, regional margin, currency, and input cost. Those rows do not store unit cases.

A graph build of this directory reports 105 datasets, 312 relationships, no unknown claims, and no contradictory edges.
