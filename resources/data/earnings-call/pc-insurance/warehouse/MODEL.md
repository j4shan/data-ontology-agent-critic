# Insurance Inc warehouse catalog

Loadable intermediary schema version 3. The builder input is `directory-manifest.yaml` beside `yaml/`.

The catalog was assembled from three subject slices: exposure, underwriting, economics. Question-to-column notes stay in `<slice>/coverage.md` for each slice.

| | |
| --- | ---: |
| Datasets | 71 |
| Relationships | 207 |
| Logical identities | 23 |
| Coverage headings | 44 |
| Numbered questions in the two source sheets | 44 |

Snowflake database `INSURANCE`, account `insurance.us-east-1`. Node ids use the `sf:insurance` prefix. Qualified names start with `insurance.`.

## What the model covers

Chubb and Progressive books are kept apart where they differ. Chubb reportable segments (North America commercial P&C, North America personal, overseas general, global reinsurance, life) live only on `dim_chubb_reporting_segment`, with commercial account size (`large_account`, `middle_market`, `small_commercial`) on its own axis for Chubb's commercial/specialty and large-account book. Progressive-style personal products (personal auto, commercial auto, motorcycle, recreational vehicle, home property, renters, umbrella) live only on `dim_progressive_product`. The two companies' product/segment names are never in one mutually exclusive list; a generic `dim_line_of_business` serves only the combined owner book.

Policy/exposure/claim quantity is in exposure, underwriting/agency/claims/digital capacity in underwriting, and premium/loss/reserve/investment/ratio dollars in economics. The loss ratio is joinable: `fact_loss_and_premium` stores earned premium and incurred loss at line + region, and `fact_loss_ratio_rate` at the same grain stores the percent; combined/expense ratios use the same earned-premium grain. Average premium per policy shares the grain of `fact_progressive_policies_in_force`. Enterprise income/book value sit only on `fact_enterprise_economics`.

Every fact grain is the natural combination of fiscal quarter, scenario, and its business keys, stated in `grain.description`. A surrogate, where present, is not the grain. The dimension that owns an identity uses `entity_universe: complete`; a fact or dimension that references it uses `entity_universe: partial`. A scenario dimension with `reported` and `guide` replaces any guidance horizon on the fiscal quarter. No analyst-conclusion `_flag` columns are stored; classifications live on dimension codes. A quantity fact does not store a price, a price fact does not store unit quantity, and a rate fact's denominator is a measure on its own fact at a joinable grain.

A graph build of this directory reports 71 datasets, 207 relationships, 23 logical identities, 0 unknown fields, and 0 contradictory edges. Validation: `build_snapshot_from_yaml` on `warehouse/yaml` plus `detect_contradictions` on the snapshot edges.
