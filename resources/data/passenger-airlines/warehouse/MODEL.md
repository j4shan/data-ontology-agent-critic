# Airline Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from subject slices that were written separately: network demand, price and yield, fleet and supply. Question-to-column notes for network demand stay in `demand_network/coverage.md`. Question-to-column notes for price and yield stay in `price_yield/coverage.md`. Question-to-column notes for fleet and supply stay in `supply_fleet/coverage.md`.

| | |
| --- | ---: |
| Datasets | 97 |
| Relationships | 213 |
| Logical identities | 97 |

Snowflake database `AIRLINE`, account `airline.us-central-1`. Node ids use the `sf:` prefix. Qualified names start with `airline.`.

## What the model covers

Network demand owns geographic entities, cabins, customers, and bookings for Airline Inc. Passenger counts, share, and booking curves are demand facts. They store quantities and rates, not a fare and not a seat price.

Price and yield owns fares, bag fees, unit revenue, cabin and geographic margin, fuel recapture, and loyalty economics for Airline Inc. A price row does not store passenger quantity or seat quantity. Fuel gallons and unit cost stay on the supply facts.

Fleet and supply owns aircraft, capacity, fuel availability, maintenance shops, staffing, and unit cost for Airline Inc. Capacity and input cost are supply facts. They are not the fare file and they do not store booked passenger quantity.

A graph build of this directory reports 97 datasets, 213 relationships, no unknown claims, and no contradictory edges.
