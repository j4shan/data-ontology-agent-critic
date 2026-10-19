# Hardware Store Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices: customers, operations, economics. Question-to-column notes stay in `<slice>/coverage.md` for each slice.

| | |
| --- | ---: |
| Datasets | 71 |
| Relationships | 208 |
| Logical identities | 23 |
| Coverage headings | 54 |
| Numbered questions in the two source sheets | 54 |

Snowflake database `HARDWARE_STORE`, account `hardwarestore.us-east-1`. Node ids use the `sf:hardwarestore` prefix. Qualified names start with `hardwarestore.`.

## What the model covers

Pro and DIY are the two codes on `dim_customer_type` and are used consistently on transaction, project, pro-order and sales facts, so a Pro row is never conflated with a DIY row. Ticket and transaction count stay distinct: `fact_sales_transactions` (customers) stores `transaction_count` and `unit_quantity` only, and `fact_average_ticket_rate` (economics) stores dollars per transaction at the identical grain (fiscal quarter, scenario, customer type, department, sales channel), naming that fact as its denominator.

Transaction/traffic quantity is in customers, store/distribution/inventory/workforce capacity in operations, and sales, ticket, comparable-sales, margin, cost and capex dollars in economics. Enterprise revenue/earnings/free cash flow sit only on `fact_enterprise_economics` at fiscal quarter + scenario.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`. A scenario dimension with `reported` and `guide` replaces any guidance horizon on the fiscal quarter. No analyst-conclusion `_flag` columns are stored; classifications live on dimension codes. A quantity fact does not store a price, a price fact does not store unit quantity, and a rate fact's denominator is a measure on its own fact at a joinable grain.

A graph build of this directory reports 71 datasets, 208 relationships, 23 logical identities, 0 unknown fields, and 0 contradictory edges. Validation: `build_snapshot_from_yaml` on `warehouse/yaml` plus `detect_contradictions` on the snapshot edges.
