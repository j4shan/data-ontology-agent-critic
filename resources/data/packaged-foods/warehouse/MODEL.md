# Food Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from subject slices that were written separately: category demand, price and margin, input supply. Question-to-column notes for category demand stay in `demand_category/coverage.md`. Question-to-column notes for price and margin stay in `price_margin/coverage.md`. Question-to-column notes for input supply stay in `supply_input/coverage.md`.

| | |
| --- | ---: |
| Datasets | 94 |
| Relationships | 235 |
| Logical identities | 94 |

Snowflake database `FOOD`, account `food.us-east-1`. Node ids use the `sf:` prefix. Qualified names start with `food.`.

## What the model covers

Category demand owns categories, brands, channels, and geography for Food Inc. Volume, consumption, share counts, and elasticity are demand facts. They store quantities and rates, not a list price and not a commodity cost.

Price and margin owns list price, realized price, price gaps, mix, gross margin, advertising, and profit for Food Inc. A price or margin row does not store case quantity. Cocoa, wheat, and fuel unit costs stay on the supply cost facts.

Input supply owns plants, origins, hedges, freight, packaging capacity, and commodity cost for Food Inc. Contracted commodity cost and capacity are supply facts. They are not the selling-price file and they do not store consumer demand quantity.

A graph build of this directory reports 94 datasets, 235 relationships, no unknown claims, and no contradictory edges.
