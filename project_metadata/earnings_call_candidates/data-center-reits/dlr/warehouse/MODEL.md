# Digital Realty warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices that were written separately: land-bank power, lease commencement and occupancy, and interconnection and customer mix. Question-to-column notes stay in `land/coverage.md`, `lease/coverage.md`, and `interconnection/coverage.md`.

| | |
| --- | ---: |
| Datasets | 62 |
| Relationships | 139 |
| Logical identities | 62 |

Snowflake database `DIGITAL_REALTY`, account `digitalrealty.us-east-1`. Node ids use the `sf:` prefix. Qualified names start with `digitalrealty.`.

## What the model covers

Land-bank power keeps secured gigawatts apart from the quarter that power becomes available. Campuses, halls, land parcels, and development projects are different populations. Constraints, cost per megawatt, developable capacity, industry supply, and labor coverage are facts. Behind-the-meter power is not grid power. The hyperscale fund is a funding channel, with operating and development ownership stored as separate positions.

Lease commencement and occupancy keep the lease, the booking, the commencement, and the quarterly occupancy snapshot apart. Megawatt band is its own dimension, so 0 to 1 megawatt, above 1 megawatt, and 5 to 15 megawatt blocks can be compared. Renewal spreads, expirations, and the forward renewal book are different facts. Cash NOI keeps energy off the other expense lines. Calendar year, quarter, and day are complete in this slice.

Interconnection and customer mix own the metro, the region, the customer, and the customer vertical. A market entry can be an interconnection site rather than a hyperscale build. Interconnection flow from small-block leasing is not the booking. Large-block mix and latency demand say which vertical wants which kind of market.

A graph build of this directory reports 62 datasets, 139 relationships, no unknown claims, and no contradictory edges.
