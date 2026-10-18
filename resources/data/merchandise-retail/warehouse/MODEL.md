# Merchandise Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices that were written separately: member and traffic, merchandise price and mix, network, fuel, and capacity. Question-to-column notes stay in `member/coverage.md`, `merchandise/coverage.md`, `network/coverage.md`.

| | |
| --- | ---: |
| Datasets | 109 |
| Relationships | 297 |
| Logical identities | 109 |

Snowflake database `MERCHANDISE`, account `merchandise.us-east-1`. Node ids use the `sf:` prefix. Qualified names start with `merchandise.`.

## What the model covers

Member and traffic own the banner, the member, the cohort, and trip quantity. Member counts, sign-ups, households, and trips are quantities. They do not store a shelf price. Renewal is a rate and does not store the member count.

Merchandise price and mix own items, departments, and price actions. Unit volume is a quantity. Shelf price, vendor cost, fuel price per gallon, and inflation rates are prices. A price-investment dollar amount does not store the unit quantity.

Network, fuel, and capacity own sites, openings, gallons, and ad inventory. Warehouse potential and fast-delivery coverage are capacity. Fuel gallons are a quantity and fuel profit per gallon is a margin. Retail-media revenue does not store the ad-inventory quantity.

A graph build of this directory reports 109 datasets, 297 relationships, no unknown claims, and no contradictory edges.
