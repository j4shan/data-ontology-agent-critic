# Truck Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices that were written separately: dealer inventory and retail demand, end markets, plants, and product mix, and price, volume, and backlog. Question-to-column notes stay in `dealer/coverage.md`, `mix/coverage.md`, and `commercial/coverage.md`.

| | |
| --- | ---: |
| Datasets | 65 |
| Relationships | 147 |
| Logical identities | 65 |

Snowflake database `TRUCK`, account `truck.us-central-1`. Node ids use the `sf:` prefix. Qualified names start with `truck.`.

## What the model covers

Dealer inventory and retail demand hold the dealer, the sales region, and retail deliveries apart from factory build slots. Dealer on-hand units, stock orders ahead of the emissions change, and industry truck inventory are not backlog and not a price. The U.S. and Canada retail range, regional outlooks, used-truck values, fleet capacity, fleet age, and the reason a customer buys (prebuy, replacement, fleet growth, or an ordinary need) sit on this side.

The mix slice holds Kenworth, Peterbilt, and DAF, over-the-road and vocational end markets, and the current diesel, low-NOx, and electric powertrains. Plants include Denton and Chillicothe. Local-for-local production, the Europe order book, China electric demand, the emissions timetable, supplier cadence, and the inputs that can block a ramp (steel, aluminum, memory chips, parts) are kept here. Peer build location is a comparison, not a second OEM catalog.

Price, volume, and backlog are separate facts. Truck price stores a rate and no units. Order intake and regional deliveries store units and no price. Backlog is unfilled orders, not dealer stock. Slot deferral records a move from one delivery year to another without a second period key. Gross margin, profit per truck, the tariff bridge, the rebate, and the per-truck surcharge stay on the commercial side, with parts results and financial-services lease and rental demand beside them.

A graph build of this directory reports 65 datasets, 147 relationships, no unknown claims, and no contradictory edges.
