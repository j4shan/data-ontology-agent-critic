# Chip Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices: demand, supply, price. Question-to-column notes stay in `demand/coverage.md`, `supply/coverage.md`, `price/coverage.md`.

| | |
| --- | ---: |
| Datasets | 71 |
| Relationships | 176 |
| Logical identities | 27 |

Snowflake database `CHIP`, account `chip.us-west-1`. Node ids use the `sf:chip` prefix. Qualified names start with `chip.`

## What the model covers

- Chip Inc is a semiconductor model. It does not extend a hardware-device warehouse and uses no device, server or PC concepts from another industry model.
- Custom ASICs, networking and infrastructure software are modeled by product family and software product, separate from GPU accelerators and data-center systems.
- End market and workload are bridge facts, so one product can serve more than one market or workload. Neither company's segment names are placed in a shared list.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate column, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`.

A graph build of this directory reports 71 datasets, 176 relationships, 27 logical identities, no unknown fields, and no contradictory edges.
