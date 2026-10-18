# Utility Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices: demand, supply, and price. Question-to-column notes stay in `demand/coverage.md`, `supply/coverage.md`, `price/coverage.md`.

| | |
| --- | ---: |
| Datasets | 71 |
| Relationships | 201 |
| Logical identities | 26 |

Snowflake database `UTILITY`, account `utility.us-east-1`. Node ids use the `sf:utility` prefix. Qualified names start with `utility.`.

## What the model covers

Demand owns the customer, the geography, the calendar, and the quantity facts. Those rows store demand quantity, not a price and not a capacity rating.

Supply owns the capacity, the network or the asset base, and the operating constraints. A capacity row stores how much can be produced, moved, or built. It does not store the price of that unit.

Price owns yields, rates, margins, cost, and capital dollars. A price row does not store the unit quantity. The denominator a price needs (revenue ton-miles, megawatt-hours, barrels) is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate column, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`.

## Structural changes in this rebuild

- Replaced the mixed load-class list with rate class (residential, commercial, industrial, wholesale), end use (data center is an end use), and a separate large-load pipeline-stage dimension.
- Separated megawatt-hours of electricity sales, megawatts of peak and pipeline load, and customer counts into different facts. Weather stores heating and cooling degree days.
- A generating station is a place and technology (combined cycle, nuclear, and others) is a dimension of the station. Generation output in megawatt-hours, capacity in megawatts, and capacity factor in percent are separate measures on separate facts.
- Rate base is dollars by operating company and jurisdiction with authorized and earned return in percent, so regulatory lag can be computed from the two returns; it is not only a growth rate on a rate-case list.
- Transmission capital, distribution capital, generation capital, and gas distribution capital have separate facts, and fuel and purchased-power expense dollars have a fact by operating company and cost category.
- Gas local distribution throughput in therms and gas customers are separate from generation fuel consumption in million British thermal units by station and fuel type. A scenario dimension with `reported` and `guide` replaces any guidance column on the fiscal-quarter dimension.

A graph build of this directory reports 71 datasets, 201 relationships, 26 logical identities, no unknown fields, and no contradictory edges.
