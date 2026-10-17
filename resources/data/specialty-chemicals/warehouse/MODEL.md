# Chemical Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from subject slices that were written separately: end market demand, price and margin, supply and capacity. Question-to-column notes for end market demand stay in `end_market/coverage.md`. Question-to-column notes for price and margin stay in `price_margin/coverage.md`. Question-to-column notes for supply and capacity stay in `supply_capacity/coverage.md`.

| | |
| --- | ---: |
| Datasets | 103 |
| Relationships | 247 |
| Logical identities | 103 |

Snowflake database `CHEMICAL`, account `chemical.us-east-1`. Node ids use the `sf:` prefix. Qualified names start with `chemical.`.

## What the model covers

End market demand owns segments, end markets, customers, channels, and geography for Chemical Inc. Volume, orders, share, traffic, retention, and outlook are demand facts. They store quantities and rates, not a selling price and not a raw-material cost.

Price and margin owns announced price, realized price, mix, gross margin, segment margin, earnings bridges, and value capture for Chemical Inc. A price or margin row does not store unit volume. Raw-material unit cost stays on the supply cost facts.

Supply and capacity owns plants, stores, acquisitions, growth spend, operating rates, and raw-material cost for Chemical Inc. Agreed input cost and spot input cost are supply facts. They are not the selling-price file and they do not store demand quantity.

A graph build of this directory reports 103 datasets, 247 relationships, no unknown claims, and no contradictory edges.
