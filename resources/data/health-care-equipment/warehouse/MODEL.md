# Surgical Supply Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

Snowflake database `SURGICAL_SUPPLY`, account `surgicalsupply.us-east-1`. Node ids use the `sf:` prefix. Qualified names start with `surgicalsupply.`.

| | |
| --- | ---: |
| Datasets | 74 |
| Relationships | 192 |
| Logical identities | 33 |
| Questions covered | 105 of 105 |

## What the model covers

- Slice `demand` is stored in `yaml/demand.yaml` with question mapping in `demand/coverage.md`.
- Slice `capital` is stored in `yaml/capital.yaml` with question mapping in `capital/coverage.md`.
- Slice `finance` is stored in `yaml/finance.yaml` with question mapping in `finance/coverage.md`.

Facts are grained by fiscal period, scenario (`reported` or `guide`), and their business keys. Quantity, capacity, and price or rate measures live on separate facts that share the keys needed to join them. Company-wide earnings, cash, and portfolio totals are grained at enterprise or company reporting-segment level and are not repeated on child rows.
