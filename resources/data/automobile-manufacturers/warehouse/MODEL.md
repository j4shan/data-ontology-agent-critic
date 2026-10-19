# Automaker Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from 3 subject slices: demand and vehicle, factory and component supply, price, tariff and profit. Question-to-column notes stay in `demand_vehicle/coverage.md`, `supply_factory/coverage.md`, `price_profit/coverage.md`.

| | |
| --- | ---: |
| Datasets | 93 |
| Relationships | 234 |
| Logical identities | 36 |

Snowflake database `AUTOMAKER`, account `automaker.us-central-1`. Node ids use the `sf:` prefix. Qualified names start with `automaker.`.

## What the model covers

Demand and vehicle own General Motors dealer wholesale and retail quantities, Tesla direct customer deliveries, dealer and company inventory, installed vehicles, subscriptions, robotaxi fleet and miles, energy storage in megawatt-hours, and captive finance contracts. Factory and component supply own production, assembly and battery capacity, downtime, component cover in weeks, sourcing, and approvals. Price, tariff, and profit own wholesale and direct vehicle revenue and per-vehicle prices, incentives, segment and enterprise results, finance-book results, software revenue keyed by subscription, tariff dollars and rates, capital spending, warranty, and regulatory credits; energy storage is priced per megawatt-hour from deployments at shared product and country keys.

A vehicle family is a nameplate; Optimus robots, the robotaxi service, and energy storage have their own dimensions and facts. General Motors wholesales to dealers and has a captive finance book classified by borrower credit tier, while Tesla delivers to customers and does not use that dealer wholesale process. Company cash flow is grained at enterprise level only and is not keyed by a borrower credit tier.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate column, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`. No column stores a conclusion marker. A scenario dimension with `reported` and `guide` replaces any guidance column on the fiscal-quarter dimension, so one quarter can be both a reported result and a later guide.

A graph build of this directory reports 93 datasets, 234 relationships, 36 logical identities, no unknown fields, and no contradictory edges.
