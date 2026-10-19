# Device Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

Snowflake database `DEVICE`, account `device.us-west-1`. Node ids use the `sf:` prefix. Qualified names start with `device.`.

| | |
| --- | ---: |
| Datasets | 74 |
| Relationships | 181 |
| Logical identities | 30 |
| Questions covered | 89 of 89 |

## What the model covers

- Slice `demand` is stored in `yaml/demand.yaml` with question mapping in `demand/coverage.md`.
- Slice `supply` is stored in `yaml/supply.yaml` with question mapping in `supply/coverage.md`.
- Slice `price` is stored in `yaml/price.yaml` with question mapping in `price/coverage.md`.

Facts are grained by fiscal period, scenario (`reported` or `guide`), and their business keys. Quantity, capacity, and price or rate measures live on separate facts that share the keys needed to join them. Company-wide earnings, cash, and portfolio totals are grained at enterprise or company reporting-segment level and are not repeated on child rows.
