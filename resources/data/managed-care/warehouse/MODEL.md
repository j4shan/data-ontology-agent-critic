# Health Plan Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from 3 subject slices that were written separately: membership and channel, medical cost and provider capacity, price, bid, and margin. Question-to-column notes stay in `membership_channel/coverage.md`, `medical_provider/coverage.md`, `price_benefit/coverage.md`.

| | |
| --- | ---: |
| Datasets | 116 |
| Relationships | 297 |
| Logical identities | 116 |

Snowflake database `HEALTH_PLAN`, account `healthplan.us-east-1`. Node ids use the `sf:` prefix. Qualified names start with `healthplan.`.

## What the model covers

Membership and channel own the Health Plan Inc books, states, employers, and life counts. Medicare Advantage, Medicaid, commercial, exchange, and pharmacy lives are quantities. They do not store a premium or a margin.

Medical cost and provider capacity own utilization, surgical volume, dispute counts, coding volume, and panel capacity. A panel slot is capacity. It is not a price and not a membership count.

Price, bid, and margin own trend rates, rate notices, bids, investment, and book margins. A margin row may name a book or a business unit. It does not store the life count.

A graph build of this directory reports 116 datasets, 297 relationships, no unknown claims, and no contradictory edges.
