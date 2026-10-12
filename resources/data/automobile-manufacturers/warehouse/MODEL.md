# Automaker Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from 3 subject slices that were written separately: demand and vehicle, factory and component supply, price, tariff, and profit. Question-to-column notes stay in `demand_vehicle/coverage.md`, `supply_factory/coverage.md`, `price_profit/coverage.md`.

| | |
| --- | ---: |
| Datasets | 113 |
| Relationships | 303 |
| Logical identities | 113 |

Snowflake database `AUTOMAKER`, account `automaker.us-central-1`. Node ids use the `sf:` prefix. Qualified names start with `automaker.`.

## What the model covers

Demand and vehicle own Automaker Inc families, cities, and the quantities that move: deliveries, robotaxi fleet, autonomous miles, and storage deployments. Optimus, Cybercab, the Semi, full-size pickups, Super Cruise, and energy storage are product families in this catalog. A delivery row does not store a price.

Factory and component supply own plants, supplier commitments, memory and metal cover, downtime, and capacity. Weeks on hand are supply. They are not a price.

Price, tariff, and profit own incentives, tariffs, capital spending, service revenue, and margins. Capital spending is a money amount. It is not a unit of capacity.

A graph build of this directory reports 113 datasets, 303 relationships, no unknown claims, and no contradictory edges.
