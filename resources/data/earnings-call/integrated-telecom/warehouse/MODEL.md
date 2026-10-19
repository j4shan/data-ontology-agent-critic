# Carrier Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices: subscribers, network, economics. Question-to-column notes stay in `<slice>/coverage.md` for each slice.

| | |
| --- | ---: |
| Datasets | 76 |
| Relationships | 221 |
| Logical identities | 25 |
| Coverage headings | 56 |
| Numbered questions in the two source sheets | 56 |

Snowflake database `CARRIER`, account `carrier.us-east-1`. Node ids use the `sf:carrier` prefix. Qualified names start with `carrier.`.

## What the model covers

Mobility, fiber broadband, fixed wireless, business wireline, consumer wireline and satellite are separate codes on the service axis. AT&T reportable segments (`mobility`, `business_wireline`, `consumer_wireline`, `corporate_and_other`) live only on `dim_att_reporting_segment`; Verizon segments (`consumer_group`, `business_group`, `corporate_and_other`) live only on `dim_verizon_reporting_segment`. They are never in one mutually exclusive list, and segment subscriber/economics facts exist per axis (`fact_att_segment_subscribers`, `fact_verizon_segment_subscribers`, `fact_att_segment_economics`, `fact_verizon_segment_economics`).

Subscriber quantity (subscribers, movements, churn denominator base, device activations) is in the subscribers slice, network capacity (locations passed, sites, spectrum megahertz, fiber miles, workforce) in network, and dollars/rates in economics. ARPU and churn rates share the exact grain of `fact_subscriber_base`; device subsidy per device shares the grain of `fact_device_upgrades`; fiber ARPU shares the grain of `fact_fiber_penetration_base`, whose supply-side denominator (locations passed) is on `fact_locations_passed`. Enterprise revenue/EBITDA/free cash flow sit only on `fact_enterprise_economics` at fiscal quarter + scenario.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`. A scenario dimension with `reported` and `guide` replaces any guidance horizon on the fiscal quarter. No analyst-conclusion `_flag` columns are stored; classifications live on dimension codes. A quantity fact does not store a price, a price fact does not store unit quantity, and a rate fact's denominator is a measure on its own fact at a joinable grain.

A graph build of this directory reports 76 datasets, 221 relationships, 25 logical identities, 0 unknown fields, and 0 contradictory edges. Validation: `build_snapshot_from_yaml` on `warehouse/yaml` plus `detect_contradictions` on the snapshot edges.
