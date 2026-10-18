# Social Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices that were written separately: audience and usage, monetization and price, compute, models, and capacity. Question-to-column notes stay in `audience/coverage.md`, `monetization/coverage.md`, `infrastructure/coverage.md`.

| | |
| --- | ---: |
| Datasets | 105 |
| Relationships | 218 |
| Logical identities | 105 |

Snowflake database `SOCIAL`, account `social.us-west-1`. Node ids use the `sf:` prefix. Qualified names start with `social.`.

## What the model covers

Audience and usage own surfaces, queries, sessions, and the installed audience. Query counts, clicks, and users are quantities. They do not store a price per click.

Monetization and price own ad products, subscriptions, and cloud deals. Ad price and cloud margin are prices. Ad revenue and cloud revenue do not store the click quantity or the backlog quantity. A search bridge stores separate volume and price effects, not the unit quantity and the unit price together.

Compute, models, and capacity own pools, silicon, labs, and capital plans. Compute capacity, backlog, and glasses units are quantities. Supply-chain inflation and talent cost are prices or costs. Capital spending does not store the capacity quantity. Capacity bought from others is a different fact from capacity sold.

A graph build of this directory reports 105 datasets, 218 relationships, no unknown claims, and no contradictory edges.
