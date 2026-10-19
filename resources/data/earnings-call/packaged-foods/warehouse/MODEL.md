# Food Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from 3 subject slices that were written separately. Question-to-column notes stay in `demand_category/coverage.md`, `price_margin/coverage.md`, `supply_input/coverage.md`.

| | |
| --- | ---: |
| Datasets | 81 |
| Relationships | 206 |
| Logical identities | 30 |

Snowflake database `FOOD`, account `food.us-east-1`. Node ids use the `sf:` prefix. Qualified names start with `food.`.

## What the model covers

General Mills and Mondelez each have their own reporting-segment dimension and brand dimension, and North America Retail appears only as a General Mills reporting segment, not as a channel. Realized price per pound or per kilogram shares brand and region keys with the matching brand-volume fact, and cocoa and wheat are carried as quantity at risk in tonnes beside cost per tonne. Every fact grain is the natural combination of fiscal period, scenario, and the business keys named in its grain description; a surrogate column is never the grain. The scenario dimension carries `reported` and `guide`, so the same fiscal period can be both a reported result and a later guide. No column is an analyst-conclusion flag; operational classifications are dimension codes, and measure descriptions name their unit.

A graph build of this directory reports 81 datasets, 206 relationships, no unknown claims, and no contradictory edges.
