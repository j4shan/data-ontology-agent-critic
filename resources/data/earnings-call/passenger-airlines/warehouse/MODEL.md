# Airline Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from 3 subject slices that were written separately. Question-to-column notes stay in `demand_network/coverage.md`, `price_yield/coverage.md`, `supply_fleet/coverage.md`.

| | |
| --- | ---: |
| Datasets | 78 |
| Relationships | 182 |
| Logical identities | 31 |

Snowflake database `AIRLINE`, account `airline.us-central-1`. Node ids use the `sf:` prefix. Qualified names start with `airline.`.

## What the model covers

Capacity is available seat-miles, traffic is revenue passenger-miles, and yield and unit cost use those denominators through shared geographic, cabin, and traveler keys. A route carries an origin airport and a destination airport. Cargo and maintenance are revenue and traffic measures, SkyMiles and MileagePlus stay in separate facts, and enterprise earnings are grained at enterprise level, not at a hub. Every fact grain is the natural combination of fiscal period, scenario, and the business keys named in its grain description; a surrogate column is never the grain. The scenario dimension carries `reported` and `guide`, so the same fiscal period can be both a reported result and a later guide. No column is an analyst-conclusion flag; operational classifications are dimension codes, and measure descriptions name their unit.

A graph build of this directory reports 78 datasets, 182 relationships, no unknown claims, and no contradictory edges.
