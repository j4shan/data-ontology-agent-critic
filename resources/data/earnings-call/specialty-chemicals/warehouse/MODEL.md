# Chemical Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from 3 subject slices that were written separately. Question-to-column notes stay in `end_market/coverage.md`, `price_margin/coverage.md`, `supply_capacity/coverage.md`.

| | |
| --- | ---: |
| Datasets | 82 |
| Relationships | 213 |
| Logical identities | 30 |

Snowflake database `CHEMICAL`, account `chemical.us-east-1`. Node ids use the `sf:` prefix. Qualified names start with `chemical.`.

## What the model covers

Sherwin-Williams coatings are measured in gallons through company stores and plants, with its own reporting-segment dimension. Ecolab is measured as site service in visits, customer sites, and technician hours, with its own reporting-segment dimension, and is not modeled as a paint-plant operating rate. Quantity and price or margin are separate facts joined by fiscal quarter, scenario, and the business keys. Every fact grain is the natural combination of fiscal period, scenario, and the business keys named in its grain description; a surrogate column is never the grain. The scenario dimension carries `reported` and `guide`, so the same fiscal period can be both a reported result and a later guide. No column is an analyst-conclusion flag; operational classifications are dimension codes, and measure descriptions name their unit.

A graph build of this directory reports 82 datasets, 213 relationships, no unknown claims, and no contradictory edges.
