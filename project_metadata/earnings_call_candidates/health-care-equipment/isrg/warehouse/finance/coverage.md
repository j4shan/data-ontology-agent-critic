# Intuitive Surgical margin, tariffs, and innovation revenue

This slice is margin, tariffs, and innovation revenue: gross margin, the bridge, generation contribution margin, tariff headwind, and revenue from new products. Payment rates are the device maker's view of surgery-center economics, not a payer remittance warehouse. Procedures and the installed base are owned outside this slice.

Foreign identities are referenced from finance rows and are partial here. Their complete populations are the datasets below, which this slice does not author.

| Identity | Column | Node |
| --- | --- | --- |
| `country_identity` | `country_id` | `sf:intuitive.customer.dim_country` |
| `procedure_category_identity` | `procedure_category_id` | `sf:intuitive.procedure.dim_procedure_category` |
| `site_of_care_identity` | `site_of_care_id` | `sf:intuitive.customer.dim_site_of_care` |
| `system_generation_identity` | `system_generation_id` | `sf:intuitive.system.dim_system_generation` |

## Numbered questions

### Q1 2026 (2) — Gross-margin outlook, tariffs, and da Vinci 5 versus Xi

Non-tariff cost support and the tariff headwind sit beside da Vinci 5 contribution margin versus Xi.

`intuitive.finance.fact_guidance`: `gross_margin_guide_rate`, `non_tariff_cost_support_amount`.
`intuitive.finance.fact_tariff_cost`: `tariff_cost_amount`, `headwind_change_amount`, `prior_headwind_amount`.
`intuitive.finance.fact_margin_bridge`: `other_effect_amount`, `tariff_effect_amount`, `cost_element_id`.
`intuitive.finance.fact_generation_margin`: `contribution_margin_rate`, `compared_contribution_margin_rate`, `system_generation_id`, `compared_system_generation_id`, `mix_share_rate`.

### Q1 2026 (3) — Innovation revenue versus procedure growth

Innovation revenue growth is compared with procedure growth in the same quarter.

`intuitive.finance.fact_innovation_revenue`: `innovation_revenue_amount`, `revenue_growth_rate`, `procedure_growth_rate`, `faster_than_procedures_flag`, `accounting_period_id`.
`intuitive.procedure.fact_procedure_volume`: `procedure_count`, `growth_rate`, `accounting_period_id`.

### Q3 2025 (6) — Gross-margin puts and takes into the next year

Fourth-quarter margin is the starting point, and puts and takes are the bridge into the next year.

`intuitive.finance.fact_margin_outlook`: `fourth_quarter_margin_rate`, `starting_margin_rate`, `put_amount`, `take_amount`, `outlook_margin_rate`.
`intuitive.finance.fact_margin_bridge`: `mix_effect_amount`, `product_cost_effect_amount`, `accounting_period_id`.

### Q3 2025 (10) — Surgery-center economics of capital, payment, instruments, and sterilization

Capital cost, Medicare and commercial rates, instrument cost, and sterilization cost are the placement economics.

`intuitive.finance.fact_asc_economics`: `capital_cost_amount`, `medicare_rate_amount`, `commercial_rate_amount`, `instrument_cost_amount`, `sterilization_cost_amount`, `system_generation_id`, `site_of_care_id`, `reimbursement_scheme_id`.
`intuitive.finance.fact_payment_rate`: `payment_rate_amount`, `reimbursement_scheme_id`, `procedure_category_id`, `site_of_care_id`.

### Q2 2025 (1) — Gross-margin upside from the new facility and what is sustainable

Facility uplift is split into one-time and sustainable, next to quarterly gross margin.

`intuitive.finance.fact_facility_margin`: `margin_uplift_amount`, `one_time_flag`, `sustainable_flag`, `manufacturing_facility_id`.
`intuitive.finance.fact_gross_margin`: `gross_margin_rate`, `one_time_flag`, `accounting_period_id`.
`intuitive.finance.dim_manufacturing_facility`: `new_facility_flag`, `facility_name`.

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `intuitive.calendar.dim_accounting_period` | — |
| `intuitive.calendar.dim_calendar_day` | — |
| `intuitive.finance.dim_currency` | — |
| `intuitive.finance.dim_legal_entity` | — |
| `intuitive.finance.dim_gl_account` | — |
| `intuitive.finance.dim_cost_element` | — |
| `intuitive.finance.dim_manufacturing_facility` | Q2 2025 (1) |
| `intuitive.finance.dim_reimbursement_scheme` | — |
| `intuitive.finance.dim_tariff_program` | — |
| `intuitive.finance.fact_journal_line` | — |
| `intuitive.finance.fact_exchange_rate` | — |
| `intuitive.finance.fact_gross_margin` | Q2 2025 (1) |
| `intuitive.finance.fact_margin_bridge` | Q1 2026 (2), Q3 2025 (6) |
| `intuitive.finance.fact_margin_outlook` | Q3 2025 (6) |
| `intuitive.finance.fact_generation_margin` | Q1 2026 (2) |
| `intuitive.finance.fact_tariff_cost` | Q1 2026 (2) |
| `intuitive.finance.fact_innovation_revenue` | Q1 2026 (3) |
| `intuitive.finance.fact_asc_economics` | Q3 2025 (10) |
| `intuitive.finance.fact_facility_margin` | Q2 2025 (1) |
| `intuitive.finance.fact_guidance` | Q1 2026 (2) |
| `intuitive.finance.fact_payment_rate` | Q3 2025 (10) |
