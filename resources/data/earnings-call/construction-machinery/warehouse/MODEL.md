# Machinery Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from 3 subject slices that were written separately. Question-to-column notes stay in `dealer/coverage.md`, `mix/coverage.md`, `commercial/coverage.md`.

| | |
| --- | ---: |
| Datasets | 91 |
| Relationships | 252 |
| Logical identities | 35 |

Snowflake database `MACHINERY`, account `machinery.us-central-1`. Node ids use the `sf:` prefix. Qualified names start with `machinery.`.

## What the model covers

Dealer stock is inventory on its own quantity fact, not a retail channel. Caterpillar machine and power processes and PACCAR truck, parts, and finance processes use separate facts and separate reporting-segment dimensions. Quantity, capacity, and price or margin are separate facts joined by fiscal period, scenario, and the business keys. Every fact grain is the natural combination of fiscal period, scenario, and the business keys named in its grain description; a surrogate column is never the grain. The scenario dimension carries `reported` and `guide`, so the same fiscal period can be both a reported result and a later guide. No column is an analyst-conclusion flag; operational classifications are dimension codes, and measure descriptions name their unit.

A graph build of this directory reports 91 datasets, 252 relationships, no unknown claims, and no contradictory edges.
