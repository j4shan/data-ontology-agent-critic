# Surgical Robot Inc procedure volume

This slice is procedure volume: hospitals, countries, procedure categories, and the case counts Surgical Robot Inc uses to read adoption. The da Vinci installed base and margin are owned outside this slice. Procedure volume here is not a claim and not a payer remittance.

Foreign identities are referenced from procedure rows and are partial here. Their complete populations are the datasets below, which this slice does not author.

| Identity | Column | Node |
| --- | --- | --- |
| `accounting_period_identity` | `accounting_period_id` | `sf:surgicalrobot.calendar.dim_accounting_period` |
| `system_generation_identity` | `system_generation_id` | `sf:surgicalrobot.system.dim_system_generation` |

## Numbered questions

### Q1 2026 (6) — International instruments growing faster than procedures

Instrument growth is compared with procedure growth, with flags for a one-time or country-specific gap.

`surgicalrobot.procedure.fact_instrument_procedure_gap`: `instrument_growth_rate`, `procedure_growth_rate`, `one_time_flag`, `country_specific_flag`, `country_id`, `accounting_period_id`.

### Q4 2025 (2) — Ambulatory surgery center opportunity and what unlocks it

Focused procedures that are moving, and the unlock still required, are on the surgery-center procedure fact. Placements show whether systems are following.

`surgicalrobot.procedure.fact_asc_procedure`: `moving_flag`, `focused_procedure_flag`, `unlock_code`, `procedure_count`, `procedure_category_id`, `site_of_care_id`.
`surgicalrobot.system.fact_system_placement`: `placement_count`, `site_of_care_id`, `system_generation_id`.

### Q4 2025 (3) — How early the procedure opportunity still is

Penetration of the current base versus the addressable opportunity, including new disease states, is the early-opportunity read.

`surgicalrobot.procedure.fact_procedure_opportunity`: `current_procedure_count`, `addressable_procedure_count`, `penetration_rate`, `early_opportunity_flag`, `disease_state_id`, `procedure_category_id`.

### Q4 2025 (5) — Hospital purchasing, Medicaid, exchange subsidies, and pull-forward

Procedure timing and coverage policy record the late-2025 pull-forward. Capital conversations record the purchasing side.

`surgicalrobot.procedure.fact_procedure_timing`: `pull_forward_count`, `timing_driver_code`, `accounting_period_id`.
`surgicalrobot.market.fact_coverage_policy`: `policy_code`, `procedure_effect_count`, `placement_effect_count`.
`surgicalrobot.commercial.fact_capital_conversation`: `purchasing_behavior_code`, `budget_risk_code`, `placement_plan_count`.

### Q3 2025 (1) — Procedure growth in the United States versus outside

Growth rates and a sustainability flag are stored separately for the United States and international procedures.

`surgicalrobot.procedure.fact_procedure_growth`: `growth_rate`, `prior_period_growth_rate`, `geography_code`, `sustainable_flag`, `driver_code`, `country_id`.

### Q3 2025 (4) — Cardiac care gaps the newer platforms address

The gap between the current standard of care and the robotic use case is stored on the newer generation.

`surgicalrobot.procedure.fact_cardiac_gap`: `standard_of_care_code`, `robotic_use_case`, `gap_code`, `system_generation_id`, `procedure_category_id`.

### Q3 2025 (7) — How long bariatric volume drags procedure growth

Bariatric growth, the drag rate, and whether the drag is still expected are one trend.

`surgicalrobot.procedure.fact_bariatric_trend`: `bariatric_growth_rate`, `total_procedure_growth_rate`, `drag_rate`, `drag_remaining_flag`, `accounting_period_id`.

### Q3 2025 (8) — How constrained and competitive the China outlook is

China procedure growth is compared with the global rate, with constraint and competitive intensity.

`surgicalrobot.market.fact_china_outlook`: `procedure_growth_rate`, `global_procedure_growth_rate`, `constraint_code`, `competitive_intensity_code`, `country_id`, `competitor_id`.

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `surgicalrobot.customer.dim_country` | — |
| `surgicalrobot.customer.dim_region` | — |
| `surgicalrobot.customer.dim_hospital` | — |
| `surgicalrobot.customer.dim_site_of_care` | — |
| `surgicalrobot.customer.dim_hospital_site` | — |
| `surgicalrobot.procedure.dim_procedure_category` | — |
| `surgicalrobot.procedure.dim_disease_state` | — |
| `surgicalrobot.procedure.dim_procedure` | — |
| `surgicalrobot.procedure.fact_procedure_volume` | — |
| `surgicalrobot.procedure.fact_procedure_growth` | Q3 2025 (1) |
| `surgicalrobot.procedure.fact_procedure_opportunity` | Q4 2025 (3) |
| `surgicalrobot.procedure.fact_bariatric_trend` | Q3 2025 (7) |
| `surgicalrobot.procedure.fact_procedure_timing` | Q4 2025 (5) |
| `surgicalrobot.procedure.fact_asc_procedure` | Q4 2025 (2) |
| `surgicalrobot.procedure.fact_instrument_procedure_gap` | Q1 2026 (6) |
| `surgicalrobot.procedure.fact_cardiac_gap` | Q3 2025 (4) |
| `surgicalrobot.market.dim_competitor` | — |
| `surgicalrobot.market.fact_coverage_policy` | Q4 2025 (5) |
| `surgicalrobot.market.fact_china_outlook` | Q3 2025 (8) |
