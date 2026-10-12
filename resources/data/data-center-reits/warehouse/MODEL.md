# Colocation Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices that were written separately: occupancy and bookings, power and development capacity, and interconnection. Question-to-column notes stay in `occupancy/coverage.md`, `power/coverage.md`, and `interconnection/coverage.md`.

| | |
| --- | ---: |
| Datasets | 67 |
| Relationships | 162 |
| Logical identities | 67 |

Snowflake database `COLOCATION`, account `colocation.us-west-1`. Node ids use the `sf:` prefix. Qualified names start with `colocation.`.

## What the model covers

Occupancy and bookings keep a booking, a pre-lease, and a quarterly occupancy snapshot as different facts. A lease is the contract. Deal size, workload, churn driver, and price realization are their own datasets. Revenue splits recurring from nonrecurring, including xScale fees. Renewal spreads feed a multi-year bridge. Regional growth and profit sit on the quarter. Calendar year, quarter, and day are complete in this slice.

Power and development own the campus, the IBX, the land site, and the development project. Planned megawatts, power actually available, and the developable pool are different measures. Industry supply is not Colocation Inc's own additions. Cooling deployments, edge constraints, and capital per megawatt for a workload are facts, not notes on the project. A lower-demand case says whether the capital plan can still be deployed.

Interconnection owns the metro, the region, the customer, and the customer vertical. A cross-connect is not a lease line. Net adds, price, attach rate, on-ramp nodes, and interconnection revenue are separate facts. Total company revenue stays on the occupancy revenue fact. Customer vertical is the mix that bookings and cross-connects share.

A graph build of this directory reports 67 datasets, 162 relationships, no unknown claims, and no contradictory edges.
