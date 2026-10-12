# Device Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices that were written separately: demand and device family, memory and silicon supply, and price versus services attach. Question-to-column notes stay in `demand/coverage.md`, `supply/coverage.md`, and `price/coverage.md`.

| | |
| --- | ---: |
| Datasets | 78 |
| Relationships | 180 |
| Logical identities | 78 |

Snowflake database `DEVICE`, account `device.us-west-1`. Node ids use the `sf:` prefix. Qualified names start with `device.`.

## What the model covers

Demand and device family own the iPhone, Mac, iPad, and Wearables families, their generations and SKUs, channel, country, region, and calendar day. Sell-through, device demand, the installed base, the upgrade program, buyer mix, unmet demand, and regional outlook are demand facts. They store quantities and rates, not a unit price and not a shipment quantity.

Memory and silicon supply owns purchased commodities, suppliers, sourcing mode, and silicon sources. A silicon source is a commercial option Device Inc can buy from. The slice does not describe a wafer fab. Coverage, agreements, component cost, shortages, production, tariffs, shipments, and channel inventory are supply facts. Agreed component cost stays on the agreement. It is not the device price file.

Price versus services attach owns the price file, the price decision, product margin, and the margin bridge. Memory, NAND, mix, currency, Services mix, and custom silicon are separate effects on that bridge. Services growth, Services margin, ad inventory, partner payments, and service attachment are their own facts. A service attachment may name a shipment or an installed-base snapshot. Its attached quantity is not the shipment quantity.

A graph build of this directory reports 78 datasets, 180 relationships, no unknown claims, and no contradictory edges.
