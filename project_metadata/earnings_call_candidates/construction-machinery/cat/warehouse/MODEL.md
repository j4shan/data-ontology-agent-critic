# Caterpillar warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices that were written separately: dealer inventory and retail demand, the end-market and power-versus-construction mix, and price versus volume versus backlog. Question-to-column notes stay in `dealer/coverage.md`, `mix/coverage.md`, and `commercial/coverage.md`.

| | |
| --- | ---: |
| Datasets | 74 |
| Relationships | 177 |
| Logical identities | 74 |

Snowflake database `CATERPILLAR`, account `caterpillar.us-central-1`. Node ids use the `sf:` prefix. Qualified names start with `caterpillar.`.

## What the model covers

Dealer inventory and retail demand hold the dealer, the sales region, and sales to users apart from factory production. Dealer on-hand units, the inventory swing, and a further destock are not retail demand and not backlog. Deliveries split between end users and rental fleets, with major-project loading counted on its own. Private nonresidential and residential demand can be read with mega-projects and rental restocking excluded. Cat Rental fleet plans compare Cat equipment with alliance products and with national rental fleets.

The mix slice holds Construction Industries, Resource Industries, Power & Energy, and the earlier Energy & Transportation segment name. End markets include data centers, oil and gas, mining, and utilities. Power products include the 10-megawatt reciprocating engine, gas and large reciprocating engines, diesel standby, gas turbines, Solar turbines, and battery storage. Prime, flexible, and backup are applications. The 2030 gigawatt target is separate from a ramp that is either inside that target or additive. Capacity timing, supplier constraints, project content, and the installed-base entry of later deliveries sit on this side.

Price, volume, and backlog are separate facts. Segment volume stores units and no price. Price realization stores a rate and no units. Backlog is unfilled orders, bridged between large power awards and broad-based orders, and it is not dealer stock and not a shipment. Incremental margin, the price/cost bridge, tariffs, manufacturing cost, merchandise programs, and the operating-profit range are the margin side.

A graph build of this directory reports 74 datasets, 177 relationships, no unknown claims, and no contradictory edges.
