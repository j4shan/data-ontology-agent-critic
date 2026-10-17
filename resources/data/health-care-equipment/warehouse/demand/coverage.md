# Surgical Supply Inc procedure volume and hospital demand

This slice is procedure volume and hospital demand: hospitals, geography, procedure families, site of care, market share, coverage, and competitive events around procedures. Capital systems, franchises, backlog, supply, and margin are owned outside this slice.

Foreign identities are referenced from demand rows and are partial here. Their complete populations are the datasets below, which this slice does not author.

| Identity | Column | Node |
| --- | --- | --- |
| `accounting_period_identity` | `accounting_period_id` | `sf:surgicalsupply.calendar.dim_accounting_period` |
| `accounting_period_identity` | `source_accounting_period_id` | `sf:surgicalsupply.calendar.dim_accounting_period` |
| `product_franchise_identity` | `product_franchise_id` | `sf:surgicalsupply.product.dim_product_franchise` |

## Numbered questions

### Q2 2026 (5) — U.S. hip and knee results and share shifts

Lighter U.S. hip and knee results are a share shift when Surgical Supply Inc growth lags market growth for those families.

`surgicalsupply.market.fact_market_share`: `stryker_growth_rate`, `market_growth_rate`, `share_shift_flag`, `procedure_family_id`, `country_id`, `product_franchise_id`.

### Q2 2026 (9) — Peripheral vascular reacceleration after supply clears

Procedures that cannot be delayed stay in procedure volume as deferred or lost cases. Supply recovery is the shortage row.

`surgicalsupply.procedure.fact_procedure_volume`: `deferred_case_count`, `lost_case_count`, `procedure_family_id`, `accounting_period_id`.
`surgicalsupply.supply.fact_supply_shortage`: `shortage_scope_code`, `procedures_cannot_delay_flag`, `recovery_expected_flag`, `procedure_deferral_count`, `procedure_loss_count`, `expected_clear_accounting_period_id`.

### Q1 2026 (3) — Competitive change in orthopedics

Rival restructuring, a possible spin, and sales-force moves are competitive events beside share.

`surgicalsupply.market.fact_competitive_event`: `event_code`, `share_effect_rate`, `ordering_pattern_code`, `product_franchise_id`, `country_id`.
`surgicalsupply.market.fact_market_share`: `stryker_growth_rate`, `share_shift_flag`, `procedure_family_id`.

### Q1 2026 (7) — Orthopedics reacceleration outside the United States

International orthopedic growth is compared with peer growth in the same procedure families.

`surgicalsupply.market.fact_market_share`: `stryker_growth_rate`, `peer_growth_rate`, `market_growth_rate`, `country_id`, `procedure_family_id`.
`surgicalsupply.market.fact_growth_geography`: `growth_rate`, `driver_code`, `country_id`.

### Q1 2026 (15) — Mako shoulder ramp and shoulder market health

Early placement demand sits next to shoulder market growth and market health. Placements themselves are on the capital slice.

`surgicalsupply.procedure.fact_procedure_market`: `market_growth_rate`, `stryker_growth_rate`, `market_health_code`, `early_placement_demand_count`, `procedure_family_id`.
`surgicalsupply.capital.fact_capital_placement`: `placement_count`, `application_code`, `capital_system_id`.

### Q1 2026 (16) — Customer relationships after the cyber incident

Each hospital response says whether the relationship held and whether guidance assumes a lasting loss.

`surgicalsupply.market.fact_customer_response`: `relationship_held_flag`, `lasting_loss_assumed_flag`, `guidance_loss_amount`, `capital_order_response_code`, `hospital_id`.

### Q4 2025 (4) — Rival vascular acquisition and a possible orthopedic spin

Portfolio moves are competitive events with a share effect on the exposed franchise.

`surgicalsupply.market.fact_competitive_event`: `event_code`, `share_effect_rate`, `product_franchise_id`, `procedure_family_id`.

### Q4 2025 (5) — Exchange coverage and patient volumes

Coverage changes are tied to expected procedure demand and the count of affected procedures.

`surgicalsupply.market.fact_exchange_coverage`: `coverage_change_code`, `expected_procedure_demand`, `affected_procedure_count`, `procedure_family_id`, `country_id`.

### Q4 2025 (12) — Share of hips, knees, and shoulders in surgery centers

Site-of-care mix holds the share of each family performed in an ambulatory surgery center.

`surgicalsupply.procedure.fact_site_of_care_mix`: `procedure_share_rate`, `procedure_count`, `procedure_family_id`, `site_of_care_id`, `country_id`.

### Q4 2025 (13) — U.S. versus international growth drivers

The growth geography row separates U.S. and international drivers.

`surgicalsupply.market.fact_growth_geography`: `growth_rate`, `driver_code`, `country_id`, `region_id`, `product_franchise_id`.

### Q4 2025 (16) — Procedures leaving the inpatient-only list

Endoscopy and other families record an inpatient-only exit as a site-of-care shift and a share change.

`surgicalsupply.procedure.fact_site_of_care_mix`: `category_shift_code`, `share_change_rate`, `procedure_share_rate`, `procedure_family_id`, `site_of_care_id`.

### Q2 2025 (2) — Surgery-center construction beyond orthopedics

Buildout counts centers and flags categories such as ablation moving outpatient.

`surgicalsupply.market.fact_asc_buildout`: `center_construction_count`, `beyond_orthopedics_flag`, `procedure_category_code`, `procedure_family_id`, `site_of_care_id`.

### Q2 2025 (7) — U.S. endoscopy acceleration versus the prior quarter

U.S. endoscopy growth is the current rate against the prior quarter, with a driver for mix reclassification.

`surgicalsupply.market.fact_growth_geography`: `growth_rate`, `prior_period_growth_rate`, `driver_code`, `country_id`, `product_franchise_id`, `procedure_family_id`.

### Q2 2025 (9) — Knee growth and the harder comparison

Knee growth is stored with the prior-period rate and a flag when the comparison is harder.

`surgicalsupply.procedure.fact_procedure_market`: `stryker_growth_rate`, `market_growth_rate`, `comparison_difficulty_flag`, `procedure_family_id`.
`surgicalsupply.procedure.fact_procedure_volume`: `growth_rate`, `prior_period_growth_rate`, `procedure_family_id`.

### Q2 2025 (15) — Shoulder procedures moving into surgery centers

Volume by site of care is balanced against the price realized in the surgery center.

`surgicalsupply.procedure.fact_site_of_care_mix`: `procedure_count`, `procedure_share_rate`, `procedure_family_id`, `site_of_care_id`.
`surgicalsupply.finance.fact_price_realization`: `asc_price_amount`, `volume_balance_amount`, `price_change_rate`, `procedure_family_id`, `site_of_care_id`.

### Q2 2025 (20) — Competitor hip launches and robotic penetration

Hip growth and the share of procedures done on a robot sit beside the rival hip-launch event.

`surgicalsupply.procedure.fact_procedure_volume`: `growth_rate`, `robotic_penetration_rate`, `robotic_case_count`, `procedure_family_id`.
`surgicalsupply.market.fact_competitive_event`: `event_code`, `share_effect_rate`, `procedure_family_id`.

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `surgicalsupply.customer.dim_country` | — |
| `surgicalsupply.customer.dim_region` | — |
| `surgicalsupply.customer.dim_health_system` | — |
| `surgicalsupply.customer.dim_site_of_care` | — |
| `surgicalsupply.customer.dim_hospital` | — |
| `surgicalsupply.customer.dim_hospital_site` | — |
| `surgicalsupply.procedure.dim_procedure_family` | — |
| `surgicalsupply.procedure.dim_procedure` | — |
| `surgicalsupply.procedure.fact_procedure_volume` | Q2 2026 (9), Q2 2025 (9), Q2 2025 (20) |
| `surgicalsupply.procedure.fact_procedure_catchup` | — |
| `surgicalsupply.procedure.fact_site_of_care_mix` | Q4 2025 (12), Q4 2025 (16), Q2 2025 (15) |
| `surgicalsupply.procedure.fact_procedure_market` | Q1 2026 (15), Q2 2025 (9) |
| `surgicalsupply.market.dim_competitor` | — |
| `surgicalsupply.market.fact_market_share` | Q2 2026 (5), Q1 2026 (3), Q1 2026 (7) |
| `surgicalsupply.market.fact_competitive_event` | Q1 2026 (3), Q4 2025 (4), Q2 2025 (20) |
| `surgicalsupply.market.fact_exchange_coverage` | Q4 2025 (5) |
| `surgicalsupply.market.fact_hospital_demand` | — |
| `surgicalsupply.market.fact_customer_response` | Q1 2026 (16) |
| `surgicalsupply.market.fact_asc_buildout` | Q2 2025 (2) |
| `surgicalsupply.market.fact_growth_geography` | Q1 2026 (7), Q4 2025 (13), Q2 2025 (7) |
