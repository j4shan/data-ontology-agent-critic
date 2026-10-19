# Burger Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

Snowflake database `BURGER`, account `burger.us-east-1`. Node ids use the `sf:` prefix. Qualified names start with `burger.`.

| | |
| --- | ---: |
| Datasets | 82 |
| Relationships | 216 |
| Logical identities | 34 |
| Questions covered | 92 of 92 |

## What the model covers

- Slice `guest` is stored in `yaml/guest.yaml` with question mapping in `guest/coverage.md`.
- Slice `system` is stored in `yaml/system.yaml` with question mapping in `system/coverage.md`.
- Slice `finance` is stored in `yaml/finance.yaml` with question mapping in `finance/coverage.md`.

Facts are grained by fiscal period, scenario (`reported` or `guide`), and their business keys. Quantity, capacity, and price or rate measures live on separate facts that share the keys needed to join them. Company-wide earnings, cash, and portfolio totals are grained at enterprise or company reporting-segment level and are not repeated on child rows.
