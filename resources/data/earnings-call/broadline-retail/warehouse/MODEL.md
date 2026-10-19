# Broadline Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices: marketplace, operations, economics. Question-to-column notes stay in `<slice>/coverage.md` for each slice.

| | |
| --- | ---: |
| Datasets | 74 |
| Relationships | 205 |
| Logical identities | 24 |
| Coverage headings | 53 |
| Numbered questions in the two source sheets | 53 |

Snowflake database `BROADLINE`, account `broadline.us-west-1`. Node ids use the `sf:broadline` prefix. Qualified names start with `broadline.`.

## What the model covers

Amazon and eBay processes are never merged. Amazon activities (online/physical stores, third-party seller services, subscriptions, advertising, AWS) are on `dim_amazon_business_activity` with `fact_amazon_unit_sales` and `fact_amazon_activity_sales`; Amazon reportable segments are only on `dim_amazon_reporting_segment`. eBay activities (core marketplace, promoted listings, managed payments, classifieds, vertical marketplace) are on the separate `dim_ebay_business_activity` with its own `fact_ebay_transaction_volume`, `fact_ebay_gmv`, `fact_ebay_revenue` and `fact_ebay_take_rate` — eBay is not modelled as an Amazon first-party store. A generic `dim_process_type` (first-party sale, third-party marketplace, payment processing, advertising, cloud, logistics, subscription) is additionally carried on marketplace/payment facts, and each process also has its own fact.

Order/unit/usage quantity is in marketplace, fulfillment/logistics/store/cloud capacity in operations, and sales/GMV/take-rate/cloud/advertising/payment/margin dollars in economics. The eBay take rate names `fact_ebay_gmv` as its denominator; selling-price and cloud-margin rates name their quantity/revenue denominator facts.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`. A scenario dimension with `reported` and `guide` replaces any guidance horizon on the fiscal quarter. No analyst-conclusion `_flag` columns are stored; classifications live on dimension codes. A quantity fact does not store a price, a price fact does not store unit quantity, and a rate fact's denominator is a measure on its own fact at a joinable grain.

A graph build of this directory reports 74 datasets, 205 relationships, 24 logical identities, 0 unknown fields, and 0 contradictory edges. Validation: `build_snapshot_from_yaml` on `warehouse/yaml` plus `detect_contradictions` on the snapshot edges.
