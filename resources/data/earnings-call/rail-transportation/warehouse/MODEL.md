# Railroad Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices: demand, supply, and price. Question-to-column notes stay in `demand/coverage.md`, `supply/coverage.md`, `price/coverage.md`.

| | |
| --- | ---: |
| Datasets | 78 |
| Relationships | 197 |
| Logical identities | 39 |

Snowflake database `RAILROAD`, account `railroad.us-central-1`. Node ids use the `sf:railroad` prefix. Qualified names start with `railroad.`.

## What the model covers

Demand owns the customer, the geography, the calendar, and the quantity facts. Those rows store demand quantity, not a price and not a capacity rating.

Supply owns the capacity, the network or the asset base, and the operating constraints. A capacity row stores how much can be produced, moved, or built. It does not store the price of that unit.

Price owns yields, rates, margins, cost, and capital dollars. A price row does not store the unit quantity. The denominator a price needs (revenue ton-miles, megawatt-hours, barrels) is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate column, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`.

## Structural changes in this rebuild

- Split the old traffic-type list into service type (carload, intermodal), commodity (coal, grain, chemicals, autos, metals, other merchandise), coal grade (metallurgical, thermal), and intermodal trade (domestic, international) dimensions.
- Split the old channel list into commercial channel (direct, intermodal marketing company), routing (single-line, interline), and handling type (direct load, transload, unit train, manifest).
- Replaced surrogate-grain volume facts with one freight-volume fact at the natural grain of fiscal quarter, scenario, service, commodity, coal grade, intermodal trade, commercial channel, routing, handling, lane, and shipper, storing carloads, tons, revenue ton-miles, and gross ton-miles. Freight revenue and the yield-rate fact (dollars per revenue ton-mile, length of haul in miles) share the revenue grain and store no carload quantity.
- Made operating ratio enterprise-level (fiscal quarter and scenario only); expense dollars sit on an operating-expense fact by cost bucket.
- Fuel stores gallons, dollars, dollars per gallon, and surcharge dollars; locomotive efficiency stores gross ton-miles per gallon with gross ton-miles supplied by the freight-volume fact.
- Service performance stores terminal dwell in hours, car velocity in miles per day, trip-plan compliance in percent, and train length in cars per train, with no generic index or conclusion flags. Lane carries origin and destination metro names and an interchange key, and volume is stated by lane on the freight-volume fact.
- Capital spending, locomotive units, and crew resources are separate facts. A scenario dimension with `reported` and `guide` replaces `guidance_horizon` on the fiscal-quarter dimension.

A graph build of this directory reports 78 datasets, 197 relationships, 39 logical identities, no unknown fields, and no contradictory edges.
