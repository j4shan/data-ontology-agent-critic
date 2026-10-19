# Beverage Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from 3 subject slices: demand and channel, bottler and commodity supply, price, mix and margin. Question-to-column notes stay in `demand_channel/coverage.md`, `supply_bottler/coverage.md`, `price_margin/coverage.md`.

| | |
| --- | ---: |
| Datasets | 82 |
| Relationships | 226 |
| Logical identities | 33 |

Snowflake database `BEVERAGE`, account `beverage.us-east-1`. Node ids use the `sf:` prefix. Qualified names start with `beverage.`.

## What the model covers

Demand and channel own Coca-Cola unit cases, PepsiCo finished-beverage unit cases, PepsiCo snack pounds, and PepsiCo food pounds as separate quantity facts. Bottler and commodity supply own concentrate, bottling, dairy, and snack capacity, commodity cover duration, order fulfillment, and packaging quantities. Price, mix, and margin own net revenue, revenue per unit case for beverages and per pound for snacks and foods, division results, input cost, currency, tax, and marketing dollars; price mix uses unit cases and net revenue at the same trademark, brand, country, and channel keys.

Coca-Cola concentrate shipments and refranchising and PepsiCo finished beverages, Frito-Lay snacks, and Quaker foods are separate processes with separate trademarks, brands, and reporting divisions. Snack volume is in pounds, not beverage unit cases, and Coke trademarks and Frito-Lay are not in one brand list.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate column, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`. No column stores a conclusion marker. A scenario dimension with `reported` and `guide` replaces any guidance column on the fiscal-quarter dimension, so one quarter can be both a reported result and a later guide.

A graph build of this directory reports 82 datasets, 226 relationships, 33 logical identities, no unknown fields, and no contradictory edges.
