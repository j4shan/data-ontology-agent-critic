# App Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices: adoption, delivery, economics. Question-to-column notes stay in `<slice>/coverage.md` for each slice.

| | |
| --- | ---: |
| Datasets | 73 |
| Relationships | 209 |
| Logical identities | 22 |
| Coverage headings | 43 |
| Numbered questions in the two source sheets | 43 |

Snowflake database `APP`, account `app.us-west-1`. Node ids use the `sf:app` prefix. Qualified names start with `app.`.

## What the model covers

Salesforce and Oracle are modelled as different businesses. Salesforce core clouds (Sales, Service, Slack, Marketing, Commerce, MuleSoft, Tableau) are on `dim_salesforce_cloud`; Agentforce, Data Cloud, headless CRM, the Claude-based offer and Informatica are on the separate `dim_agentforce_product`, with seat quantity on `fact_subscription_seats` and token/work-unit quantity on `fact_agentforce_usage`. Oracle database, OCI cloud infrastructure, applications, license/support, hardware and services are on `dim_oracle_business` / `dim_oracle_product` / `dim_oracle_cloud_venue`, with their own usage, pipeline, booking, revenue and RPO facts. Neither vendor's products are codes on the other's axis.

Seat/usage/adoption/pipeline quantity is in adoption (the dataset floor of 70 is met with 73 datasets despite only 43 questions), data-center/cloud-region/sales/partner/sovereign capacity in delivery, and revenue/ARR/RPO-CRPO/margin/pricing/capex dollars in economics. Revenue per work unit shares the grain of `fact_agentforce_usage`; account value shares the grain of `fact_installed_base`; database and Slack revenue share the grains of their usage facts. Enterprise totals sit only on `fact_enterprise_economics`.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`. A scenario dimension with `reported` and `guide` replaces any guidance horizon on the fiscal quarter. No analyst-conclusion `_flag` columns are stored; classifications live on dimension codes. A quantity fact does not store a price, a price fact does not store unit quantity, and a rate fact's denominator is a measure on its own fact at a joinable grain.

A graph build of this directory reports 73 datasets, 209 relationships, 22 logical identities, 0 unknown fields, and 0 contradictory edges. Validation: `build_snapshot_from_yaml` on `warehouse/yaml` plus `detect_contradictions` on the snapshot edges.
