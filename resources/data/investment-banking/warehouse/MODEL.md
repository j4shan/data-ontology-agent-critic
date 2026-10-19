# Broker Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices: demand, supply, price. Question-to-column notes stay in `demand/coverage.md`, `supply/coverage.md`, `price/coverage.md`.

| | |
| --- | ---: |
| Datasets | 79 |
| Relationships | 191 |
| Logical identities | 36 |

Snowflake database `BROKER`, account `broker.us-east-1`. Node ids use the `sf:broker` prefix. Qualified names start with `broker.`

## What the model covers

- Investment banking, markets, and wealth are different processes, modeled as separate advisory, trading, financing and wealth facts rather than one revenue fact.
- Reporting units are Broker Inc business processes. Neither company's reportable-segment names are placed in a shared mutually exclusive code list.
- Balance-sheet capacity, risk-weighted assets and leverage exposure sit on supply facts; revenue, margin and return sit on price facts; deal, issuance and client activity counts sit on demand facts.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate column, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`.

A graph build of this directory reports 79 datasets, 191 relationships, 36 logical identities, no unknown fields, and no contradictory edges.
