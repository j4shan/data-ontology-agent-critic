# Pharma Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices: demand, supply, price. Question-to-column notes stay in `demand/coverage.md`, `supply/coverage.md`, `price/coverage.md`.

| | |
| --- | ---: |
| Datasets | 70 |
| Relationships | 202 |
| Logical identities | 27 |

Snowflake database `PHARMA`, account `pharma.us-east-1`. Node ids use the `sf:pharma` prefix. Qualified names start with `pharma.`

## What the model covers

- Lilly's incretin and diabetes process and Merck's oncology and vaccines processes have their own demand and revenue facts, joined by therapy area and product dimensions that can express both.
- No shared mutually exclusive list contains both companies' reportable-segment names; therapy area, product and indication are separate axes.
- Demand stores patients, prescriptions and doses; supply stores manufacturing and regulatory capacity; price stores sales, gross-to-net and net price without unit quantity.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate column, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`.

A graph build of this directory reports 70 datasets, 202 relationships, 27 logical identities, no unknown fields, and no contradictory edges.
