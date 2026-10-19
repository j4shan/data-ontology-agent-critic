# Wafer Tool Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices: demand, supply, price. Question-to-column notes stay in `demand/coverage.md`, `supply/coverage.md`, `price/coverage.md`.

| | |
| --- | ---: |
| Datasets | 74 |
| Relationships | 190 |
| Logical identities | 31 |

Snowflake database `WAFER_TOOL`, account `wafertool.us-west-1`. Node ids use the `sf:wafertool` prefix. Qualified names start with `wafertool.`

## What the model covers

- Deposition, etch, inspection and service are different tool processes, modeled with separate process, deposition-type and etch-type dimensions and separate shipment facts.
- Both installed-base service and new systems are modeled: installed base, service capacity and spares on supply facts; systems and service revenue on separate price facts.
- This is wafer-fab equipment. No chip-design, GPU or Device Inc hardware concepts are used.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate column, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`.

A graph build of this directory reports 74 datasets, 190 relationships, 31 logical identities, no unknown fields, and no contradictory edges.
