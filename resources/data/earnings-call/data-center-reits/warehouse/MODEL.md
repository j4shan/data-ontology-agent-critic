# Colocation Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

Snowflake database `COLOCATION`, account `colocation.us-west-1`. Node ids use the `sf:` prefix. Qualified names start with `colocation.`.

| | |
| --- | ---: |
| Datasets | 72 |
| Relationships | 189 |
| Logical identities | 29 |
| Questions covered | 84 of 84 |

## What the model covers

- Slice `occupancy` is stored in `yaml/occupancy.yaml` with question mapping in `occupancy/coverage.md`.
- Slice `power` is stored in `yaml/power.yaml` with question mapping in `power/coverage.md`.
- Slice `finance` is stored in `yaml/finance.yaml` with question mapping in `finance/coverage.md`.
- Slice `interconnection` is stored in `yaml/interconnection.yaml` with question mapping in `interconnection/coverage.md`.

Facts are grained by fiscal period, scenario (`reported` or `guide`), and their business keys. Quantity, capacity, and price or rate measures live on separate facts that share the keys needed to join them. Company-wide earnings, cash, and portfolio totals are grained at enterprise or company reporting-segment level and are not repeated on child rows.
