# Surgical Supply Inc reimbursement and margin

This slice is reimbursement and margin: physician-payment context, operating margin, price realization, tariffs, and guidance. It is the device maker's view of hospital payment and Surgical Supply Inc profit, not a payer remittance warehouse. Procedure volume and the product franchise are owned outside this slice.

Foreign identities are referenced from finance rows and are partial here. Their complete populations are the datasets below, which this slice does not author.

| Identity | Column | Node |
| --- | --- | --- |
| `capital_system_identity` | `capital_system_id` | `sf:surgicalsupply.capital.dim_capital_system` |
| `country_identity` | `country_id` | `sf:surgicalsupply.customer.dim_country` |
| `manufacturing_plant_identity` | `manufacturing_plant_id` | `sf:surgicalsupply.supply.dim_manufacturing_plant` |
| `procedure_family_identity` | `procedure_family_id` | `sf:surgicalsupply.procedure.dim_procedure_family` |
| `product_franchise_identity` | `product_franchise_id` | `sf:surgicalsupply.product.dim_product_franchise` |
| `site_of_care_identity` | `site_of_care_id` | `sf:surgicalsupply.customer.dim_site_of_care` |

## Numbered questions

### Q2 2026 (1) — Underlying demand versus catch-up across capital, vascular, hips, and medical

The organic sales bridge splits underlying demand and catch-up by franchise.

`surgicalsupply.finance.fact_organic_sales_bridge`: `underlying_demand_amount`, `catchup_demand_amount`, `capital_amount`, `procedure_amount`, `product_franchise_id`, `accounting_period_id`.

### Q2 2026 (3) — Margin and earnings path in the second-half outlook

Second-half margin and earnings are stored against the full-year margin rate.

`surgicalsupply.finance.fact_margin_outlook`: `second_half_margin_rate`, `full_year_margin_rate`, `earnings_amount`, `outlook_horizon_code`.

### Q2 2026 (4) — Medicare cut in hip, knee, and shoulder physician payment

The payment change rate is the cut. Procedure volume response and price response show how the industry is moving.

`surgicalsupply.reimbursement.fact_payment_change`: `payment_change_rate`, `payment_change_amount`, `procedure_volume_response`, `price_response_amount`, `industry_response_code`, `procedure_family_id`, `reimbursement_scheme_id`.
`surgicalsupply.procedure.fact_procedure_volume`: `procedure_count`, `growth_rate`, `procedure_family_id`.

### Q2 2026 (7) — Volume, capital conversion, and backlog assumed in the back half

Guidance stores the three back-half assumptions. Open backlog is the capital position those assumptions spend.

`surgicalsupply.finance.fact_guidance`: `volume_growth_assumption_rate`, `capital_conversion_assumption_rate`, `backlog_realization_assumption_amount`, `accounting_period_id`.
`surgicalsupply.commercial.fact_order_backlog`: `open_backlog_amount`, `planned_realization_amount`, `quarter_cadence_code`.
`surgicalsupply.procedure.fact_procedure_volume`: `growth_rate`, `accounting_period_id`.

### Q2 2026 (12) — Revenue recognition, procedure catch-up, capital, and recovery still ahead

The sales bridge separates those three buckets and the recovery that is still ahead.

`surgicalsupply.finance.fact_organic_sales_bridge`: `revenue_recognition_amount`, `catchup_demand_amount`, `capital_amount`, `remaining_recovery_amount`, `accounting_period_id`.

### Q1 2026 (1) — Sales and earnings cadence after reiterating the outlook

Earnings and organic sales are stored by remaining-year cadence, with a flag that the outlook was reiterated despite the disruption.

`surgicalsupply.finance.fact_earnings_outlook`: `earnings_amount`, `organic_sales_amount`, `cadence_code`, `reiterated_despite_disruption_flag`, `cyber_incident_flag`, `accounting_period_id`.
`surgicalsupply.finance.fact_guidance`: `organic_growth_guide_rate`, `full_year_outlook_amount`, `disruption_adjusted_flag`.

### Q1 2026 (2) — Operating margin up about 50 basis points, and input-cost offsets

Guided expansion in basis points sits beside oil and other input inflation and the offset.

`surgicalsupply.finance.fact_input_cost`: `margin_guide_bps`, `input_cost_change_amount`, `offset_amount`, `cost_driver_code`, `cost_element_id`.
`surgicalsupply.finance.fact_margin_outlook`: `margin_expansion_bps`, `full_year_margin_rate`.

### Q4 2025 (1) — Higher starting organic-growth guidance and a 10 percent year

The guide rate is stored with the investor-day market growth and flags for a higher start and a 10 percent year.

`surgicalsupply.finance.fact_guidance`: `organic_growth_guide_rate`, `higher_start_guide_flag`, `ten_percent_year_possible_flag`, `investor_day_market_growth_rate`.

### Q4 2025 (2) — Capital and implant pricing and the capital-equipment environment

Price change by type is stored against last year and the capital environment.

`surgicalsupply.finance.fact_price_realization`: `price_type_code`, `price_change_rate`, `prior_year_price_change_rate`, `capital_environment_code`, `product_franchise_id`.
`surgicalsupply.commercial.fact_capital_budget`: `capital_environment_code`, `budget_change_amount`.

### Q4 2025 (6) — Operating-margin expansion path through 2028

The multi-year target rate and the intact flag are the path through 2028, next to current margin.

`surgicalsupply.finance.fact_margin_outlook`: `multiyear_target_rate`, `target_year`, `path_intact_flag`, `operating_margin_rate`, `outlook_horizon_code`.
`surgicalsupply.finance.fact_operating_margin`: `operating_margin_rate`, `accounting_period_id`.

### Q4 2025 (14) — Whether the smaller MedSurg price benefit was temporary

The temporary flag and the dependence flag say whether company price needs MedSurg price to recover.

`surgicalsupply.finance.fact_price_realization`: `price_type_code`, `price_change_rate`, `temporary_flag`, `company_price_dependence_flag`, `assumed_price_rate`, `product_franchise_id`.

### Q4 2025 (19) — Absorbing or reducing this year's tariff cost

Tariff cost, mitigation, and the absorbed flag are the estimate versus the actions.

`surgicalsupply.finance.fact_tariff_cost`: `tariff_cost_amount`, `mitigation_amount`, `absorbed_flag`, `accounting_period_id`.

### Q4 2025 (21) — Price split between MedSurg and orthopedics

Price change by type is the franchise split versus the prior year and the company assumption.

`surgicalsupply.finance.fact_price_realization`: `price_type_code`, `price_change_rate`, `prior_year_price_change_rate`, `assumed_price_rate`, `product_franchise_id`.

### Q2 2025 (3) — Why the tariff estimate came down only modestly

The estimate revision is stored with the manufacturing footprint of the plants that explain it.

`surgicalsupply.finance.fact_tariff_cost`: `estimate_revision_amount`, `tariff_cost_amount`, `manufacturing_footprint_code`, `manufacturing_plant_id`.
`surgicalsupply.supply.dim_manufacturing_plant`: `country_id`, `plant_name`.

### Q2 2025 (16) — Whether the second-half step-down is conservatism or a slowdown

Second-half growth is compared with the first-half run rate, and the step-down reason names which one it is.

`surgicalsupply.finance.fact_guidance`: `second_half_growth_rate`, `first_half_growth_rate`, `step_down_reason_code`, `organic_growth_guide_rate`.

### Q2 2025 (17) — China, tariffs, and the local health-care market

China tariff cost, the under-indexed flag, and the local-market rule effect are one row.

`surgicalsupply.finance.fact_tariff_cost`: `tariff_cost_amount`, `china_under_indexed_flag`, `local_market_rule_effect_amount`, `country_id`.

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `surgicalsupply.calendar.dim_accounting_period` | — |
| `surgicalsupply.calendar.dim_calendar_day` | — |
| `surgicalsupply.finance.dim_currency` | — |
| `surgicalsupply.finance.dim_legal_entity` | — |
| `surgicalsupply.finance.dim_gl_account` | — |
| `surgicalsupply.finance.dim_cost_element` | — |
| `surgicalsupply.finance.fact_journal_line` | — |
| `surgicalsupply.finance.fact_exchange_rate` | — |
| `surgicalsupply.reimbursement.dim_reimbursement_scheme` | — |
| `surgicalsupply.reimbursement.dim_reimbursement_code` | — |
| `surgicalsupply.reimbursement.fact_payment_change` | Q2 2026 (4) |
| `surgicalsupply.finance.dim_tariff_program` | — |
| `surgicalsupply.finance.fact_operating_margin` | Q4 2025 (6) |
| `surgicalsupply.finance.fact_margin_outlook` | Q2 2026 (3), Q1 2026 (2), Q4 2025 (6) |
| `surgicalsupply.finance.fact_margin_bridge` | — |
| `surgicalsupply.finance.fact_earnings_outlook` | Q1 2026 (1) |
| `surgicalsupply.finance.fact_input_cost` | Q1 2026 (2) |
| `surgicalsupply.finance.fact_price_realization` | Q4 2025 (2), Q4 2025 (14), Q4 2025 (21) |
| `surgicalsupply.finance.fact_organic_sales_bridge` | Q2 2026 (1), Q2 2026 (12) |
| `surgicalsupply.finance.fact_tariff_cost` | Q4 2025 (19), Q2 2025 (3), Q2 2025 (17) |
| `surgicalsupply.finance.fact_guidance` | Q2 2026 (7), Q1 2026 (1), Q4 2025 (1), Q2 2025 (16) |
