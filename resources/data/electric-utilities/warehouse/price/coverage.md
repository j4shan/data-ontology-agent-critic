# Utility Inc price, cost, and margin

This slice is part of the Utility Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity row does not store a price. A price row does not store the unit quantity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `dim_state_identity` | `state_id` | `utility.geography.dim_state` `state_id` |
| `dim_customer_identity` | `customer_id` | `utility.customer.dim_customer` `customer_id` |
| `dim_fiscal_quarter_identity` | `fiscal_quarter_id` | `utility.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `dim_project_identity` | `project_id` | `utility.generation.dim_project` `project_id` |
| `dim_contract_identity` | `contract_id` | `utility.customer.dim_contract` `contract_id` |
| `dim_tariff_identity` | `tariff_id` | `utility.customer.dim_tariff` `tariff_id` |
| `dim_technology_identity` | `technology_id` | `utility.generation.dim_technology` `technology_id` |
| `dim_customer_segment_identity` | `customer_segment_id` | `utility.customer.dim_customer_segment` `customer_segment_id` |
| `dim_plant_identity` | `plant_id` | `utility.generation.dim_plant` `plant_id` |

## Numbered questions

### Q2 2026 (1) — Duke Energy

For Duke Energy, with additional capital and late-stage load already at the top of the earnings-growth range, could the next update push the growth rate higher?

- `utility.price.fact_capital_plan`: `capital_amount`, `inside_window_amount`, `later_amount`, `layered_even_flag`, `fiscal_quarter_id`, `capital_program_id`, `project_id`
- `utility.demand.fact_large_load`: `load_quantity`, `top_of_range_flag`, `incremental_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.price.fact_earnings_growth`: `growth_rate`, `above_range_flag`, `high_end_includes_incremental_flag`, `fiscal_quarter_id`, `capital_program_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`

### Q2 2026 (10) — Duke Energy

For Duke Energy, as near-term tax-credit cash from nuclear and batteries rolls off, does cash flow from new-investment recovery replace it?

- `utility.supply.fact_nuclear_path`: `path_code`, `application_status_code`, `beyond_application_flag`, `fiscal_quarter_id`, `technology_id`, `project_id`
- `utility.price.fact_tax_credit`: `credit_amount`, `rolls_off_flag`, `further_monetization_flag`, `flowback_code`, `fiscal_quarter_id`, `cost_bucket_id`
- `utility.price.fact_rate_recovery`: `recovery_amount`, `replaces_credit_flag`, `fiscal_quarter_id`, `capital_program_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`
- `utility.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`

### Q1 2026 (1) — Duke Energy

For Duke Energy, is a partial settlement possible in the Carolinas rate cases?

- `utility.price.fact_rate_case`: `request_amount`, `settlement_possible_flag`, `fully_litigated_flag`, `fiscal_quarter_id`, `rate_case_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.price.dim_rate_case`: `rate_case_id`, `case_code`, `case_name`, `state_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`

### Q1 2026 (3) — Duke Energy

For Duke Energy, are there further tax-credit monetizations that could fund customer bill benefits?

- `utility.price.fact_tax_credit`: `credit_amount`, `rolls_off_flag`, `further_monetization_flag`, `flowback_code`, `fiscal_quarter_id`, `cost_bucket_id`
- `utility.price.fact_bill_credit`: `credit_amount`, `revised_higher_flag`, `cumulative_flag`, `fiscal_quarter_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`

### Q1 2026 (4) — Duke Energy

For Duke Energy, would the company join a utility, hyperscaler, and government structure aimed at nuclear cost-overrun risk?

- `utility.supply.fact_nuclear_choice`: `choice_code`, `long_lead_flag`, `fiscal_quarter_id`, `technology_id`
- `utility.price.fact_hyperscaler_contract`: `long_term_flag`, `standard_toll_flag`, `bears_overrun_flag`, `fiscal_quarter_id`, `contract_id`, `counterparty_id`
- `utility.price.fact_overrun`: `overrun_amount`, `hyperscaler_bears_flag`, `shared_structure_flag`, `fiscal_quarter_id`, `project_id`, `counterparty_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.price.dim_counterparty`: `counterparty_id`, `counterparty_code`, `counterparty_name`, `customer_id`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`

### Q1 2026 (6) — Duke Energy

For Duke Energy, do Carolinas combination savings and tax credits offset the current rate request?

- `utility.price.fact_combination_offset`: `savings_amount`, `offsets_request_flag`, `fiscal_quarter_id`, `rate_case_id`
- `utility.price.fact_tax_credit`: `credit_amount`, `rolls_off_flag`, `further_monetization_flag`, `flowback_code`, `fiscal_quarter_id`, `cost_bucket_id`
- `utility.price.fact_rate_case`: `request_amount`, `settlement_possible_flag`, `fully_litigated_flag`, `fiscal_quarter_id`, `rate_case_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.price.dim_rate_case`: `rate_case_id`, `case_code`, `case_name`, `state_id`
- `utility.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`

### Q1 2026 (7) — Duke Energy

For Duke Energy, are data-center or fuel-cost bills in the legislative session material to load or cost sharing?

- `utility.demand.fact_data_center_load`: `load_quantity`, `funnel_accelerated_flag`, `in_sales_range_flag`, `joint_announcement_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.price.fact_fuel_sharing`: `sharing_amount`, `material_flag`, `fiscal_quarter_id`, `state_id`, `cost_bucket_id`
- `utility.price.fact_legislation`: `material_flag`, `affects_recovery_flag`, `fiscal_quarter_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `utility.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`

### Q1 2026 (9) — Duke Energy

For Duke Energy, when do the latest tax-credit monetization benefits flow back to customers?

- `utility.price.fact_tax_credit`: `credit_amount`, `rolls_off_flag`, `further_monetization_flag`, `flowback_code`, `fiscal_quarter_id`, `cost_bucket_id`
- `utility.price.fact_customer_rate`: `rate_amount`, `political_reception_code`, `larger_credit_chance_flag`, `fiscal_quarter_id`, `state_id`, `tariff_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_tariff`: `tariff_id`, `tariff_code`, `tariff_name`, `state_id`

### Q4 2025 (1) — Duke Energy

For Duke Energy, what storm costs are still open, and are they already in the earnings midpoint?

- `utility.price.fact_storm_cost`: `storm_amount`, `still_open_flag`, `in_midpoint_flag`, `fiscal_quarter_id`, `cost_bucket_id`
- `utility.price.fact_earnings_growth`: `growth_rate`, `above_range_flag`, `high_end_includes_incremental_flag`, `fiscal_quarter_id`, `capital_program_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`

### Q4 2025 (2) — Duke Energy

For Duke Energy, does the Carolinas case, with the combination and affordability focus, need to be fully litigated or can it settle?

- `utility.price.fact_rate_case`: `request_amount`, `settlement_possible_flag`, `fully_litigated_flag`, `fiscal_quarter_id`, `rate_case_id`, `state_id`
- `utility.price.fact_combination_offset`: `savings_amount`, `offsets_request_flag`, `fiscal_quarter_id`, `rate_case_id`
- `utility.price.fact_affordability`: `pressure_flag`, `offset_amount`, `fiscal_quarter_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.price.dim_rate_case`: `rate_case_id`, `case_code`, `case_name`, `state_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`

### Q4 2025 (4) — Duke Energy

For Duke Energy, what explains the gap between rate-base growth and earnings growth, and can that gap narrow in the Carolinas?

- `utility.price.fact_rate_base`: `rate_base_growth_rate`, `gap_to_earnings_rate`, `fiscal_quarter_id`, `state_id`
- `utility.price.fact_earnings_growth`: `growth_rate`, `above_range_flag`, `high_end_includes_incremental_flag`, `fiscal_quarter_id`, `capital_program_id`
- `utility.demand.fact_state_load`: `load_quantity`, `softer_flag`, `still_finalizing_flag`, `fiscal_quarter_id`, `state_id`, `load_class_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`
- `utility.customer.dim_load_class`: `load_class_id`, `class_code`, `class_name`

### Q4 2025 (5) — Duke Energy

For Duke Energy, what earned returns and other conditions are required to deliver the top half of the growth range from 2028?

- `utility.price.fact_earned_return`: `earned_return_rate`, `required_for_top_half_flag`, `fiscal_quarter_id`, `rate_case_id`
- `utility.price.fact_earnings_growth`: `growth_rate`, `above_range_flag`, `high_end_includes_incremental_flag`, `fiscal_quarter_id`, `capital_program_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.price.dim_rate_case`: `rate_case_id`, `case_code`, `case_name`, `state_id`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`

### Q4 2025 (8) — Duke Energy

For Duke Energy, are data-center approvals being structured so residential customers are kept whole?

- `utility.demand.fact_data_center_load`: `load_quantity`, `funnel_accelerated_flag`, `in_sales_range_flag`, `joint_announcement_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.price.fact_residential_protection`: `kept_whole_flag`, `bill_impact_amount`, `fiscal_quarter_id`, `state_id`, `customer_segment_id`
- `utility.price.fact_customer_rate`: `rate_amount`, `political_reception_code`, `larger_credit_chance_flag`, `fiscal_quarter_id`, `state_id`, `tariff_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `utility.customer.dim_customer_segment`: `customer_segment_id`, `segment_code`, `segment_name`
- `utility.customer.dim_tariff`: `tariff_id`, `tariff_code`, `tariff_name`, `state_id`

### Q4 2025 (11) — Duke Energy

For Duke Energy, would a North Carolina large-load tariff reach back to agreements already signed?

- `utility.price.fact_tariff_terms`: `credit_terms_code`, `reaches_back_flag`, `docket_status_code`, `fiscal_quarter_id`, `tariff_id`, `customer_id`
- `utility.demand.fact_contracted_load`: `contracted_quantity`, `still_finalizing_flag`, `fiscal_quarter_id`, `contract_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.customer.dim_tariff`: `tariff_id`, `tariff_code`, `tariff_name`, `state_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`

### Q3 2025 (1) — Duke Energy

For Duke Energy, is the incremental capital expected to layer in evenly across the planning period?

- `utility.price.fact_capital_plan`: `capital_amount`, `inside_window_amount`, `later_amount`, `layered_even_flag`, `fiscal_quarter_id`, `capital_program_id`, `project_id`
- `utility.supply.fact_schedule`: `in_service_year`, `milestone_code`, `remaining_flag`, `fiscal_quarter_id`, `project_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`

### Q3 2025 (2) — Duke Energy

For Duke Energy, what projects make up the incremental capital opportunity of roughly $10 billion?

- `utility.price.fact_capital_plan`: `capital_amount`, `inside_window_amount`, `later_amount`, `layered_even_flag`, `fiscal_quarter_id`, `capital_program_id`, `project_id`
- `utility.supply.fact_generation_capacity`: `capacity_quantity`, `incremental_required_flag`, `company_owned_flag`, `fiscal_quarter_id`, `technology_id`, `state_id`, `plant_id`
- `utility.demand.fact_large_load`: `load_quantity`, `top_of_range_flag`, `incremental_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`

### Q3 2025 (4) — Duke Energy

For Duke Energy, does the high end of the earnings-growth range already reflect incremental capital, including the confidence in hitting that high end from 2028?

- `utility.price.fact_earnings_growth`: `growth_rate`, `above_range_flag`, `high_end_includes_incremental_flag`, `fiscal_quarter_id`, `capital_program_id`
- `utility.price.fact_capital_plan`: `capital_amount`, `inside_window_amount`, `later_amount`, `layered_even_flag`, `fiscal_quarter_id`, `capital_program_id`, `project_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`

### Q3 2025 (5) — Duke Energy

For Duke Energy, what balance-sheet conditions would allow the lower end of the equity share used to fund capital upside?

- `utility.price.fact_funding_mix`: `equity_share_rate`, `lower_end_allowed_flag`, `balance_sheet_ok_flag`, `fiscal_quarter_id`, `capital_program_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`

### Q2 2026 (5) — Southern Company

For Southern Company, are hyperscalers willing to take cost-overrun risk above budget on new large reactors?

- `utility.supply.fact_nuclear_choice`: `choice_code`, `long_lead_flag`, `fiscal_quarter_id`, `technology_id`
- `utility.price.fact_hyperscaler_contract`: `long_term_flag`, `standard_toll_flag`, `bears_overrun_flag`, `fiscal_quarter_id`, `contract_id`, `counterparty_id`
- `utility.price.fact_overrun`: `overrun_amount`, `hyperscaler_bears_flag`, `shared_structure_flag`, `fiscal_quarter_id`, `project_id`, `counterparty_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.price.dim_counterparty`: `counterparty_id`, `counterparty_code`, `counterparty_name`, `customer_id`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`

### Q2 2026 (10) — Southern Company

For Southern Company, how do Georgia tariffs handle credit risk for data-center customers that are not strongly investment grade?

- `utility.demand.fact_state_load`: `load_quantity`, `softer_flag`, `still_finalizing_flag`, `fiscal_quarter_id`, `state_id`, `load_class_id`
- `utility.price.fact_tariff_terms`: `credit_terms_code`, `reaches_back_flag`, `docket_status_code`, `fiscal_quarter_id`, `tariff_id`, `customer_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_load_class`: `load_class_id`, `class_code`, `class_name`
- `utility.customer.dim_tariff`: `tariff_id`, `tariff_code`, `tariff_name`, `state_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`

### Q2 2026 (13) — Southern Company

For Southern Company, how do Georgia and Alabama turn this load growth into rates, including the chance of a larger rate credit in Georgia?

- `utility.price.fact_customer_rate`: `rate_amount`, `political_reception_code`, `larger_credit_chance_flag`, `fiscal_quarter_id`, `state_id`, `tariff_id`
- `utility.demand.fact_large_load`: `load_quantity`, `top_of_range_flag`, `incremental_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_tariff`: `tariff_id`, `tariff_code`, `tariff_name`, `state_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`

### Q1 2026 (1) — Southern Company

For Southern Company, would the company join a utility and hyperscaler structure in which hyperscalers take cost inflation above budget on new reactors?

- `utility.supply.fact_nuclear_choice`: `choice_code`, `long_lead_flag`, `fiscal_quarter_id`, `technology_id`
- `utility.price.fact_hyperscaler_contract`: `long_term_flag`, `standard_toll_flag`, `bears_overrun_flag`, `fiscal_quarter_id`, `contract_id`, `counterparty_id`
- `utility.price.fact_overrun`: `overrun_amount`, `hyperscaler_bears_flag`, `shared_structure_flag`, `fiscal_quarter_id`, `project_id`, `counterparty_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.price.dim_counterparty`: `counterparty_id`, `counterparty_code`, `counterparty_name`, `customer_id`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`

### Q1 2026 (4) — Southern Company

For Southern Company, could cumulative bill credits be revised higher as contracted large load rises?

- `utility.price.fact_bill_credit`: `credit_amount`, `revised_higher_flag`, `cumulative_flag`, `fiscal_quarter_id`, `state_id`
- `utility.demand.fact_large_load`: `load_quantity`, `top_of_range_flag`, `incremental_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`

### Q1 2026 (10) — Southern Company

For Southern Company, would a new build also depend on contracting the plant before it is completed, given upgrade costs that approach new-build costs?

- `utility.supply.fact_new_build`: `capacity_quantity`, `needs_offtake_flag`, `needed_sooner_flag`, `fiscal_quarter_id`, `technology_id`, `project_id`
- `utility.price.fact_contract_price`: `offered_price_amount`, `covers_return_flag`, `customers_willing_flag`, `fiscal_quarter_id`, `contract_id`, `counterparty_id`
- `utility.price.fact_cost_inflation`: `inflation_amount`, `cost_per_kw_amount`, `assumed_flag`, `fiscal_quarter_id`, `technology_id`, `cost_bucket_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.price.dim_counterparty`: `counterparty_id`, `counterparty_code`, `counterparty_name`, `customer_id`

### Q3 2025 (1) — Southern Company

For Southern Company, how are Georgia customers receiving the new large-load tariff, and how does the minimum bill protect cost recovery?

- `utility.price.fact_tariff_terms`: `credit_terms_code`, `reaches_back_flag`, `docket_status_code`, `fiscal_quarter_id`, `tariff_id`, `customer_id`
- `utility.price.fact_minimum_bill`: `minimum_bill_amount`, `protects_recovery_flag`, `reception_code`, `fiscal_quarter_id`, `tariff_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.customer.dim_tariff`: `tariff_id`, `tariff_code`, `tariff_name`, `state_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`

### Q2 2025 (1) — Southern Company

For Southern Company, does the higher rate-base growth path change the 2027 rebase or the long-term growth view?

- `utility.price.fact_rate_base`: `rate_base_growth_rate`, `gap_to_earnings_rate`, `fiscal_quarter_id`, `state_id`
- `utility.price.fact_earnings_growth`: `growth_rate`, `above_range_flag`, `high_end_includes_incremental_flag`, `fiscal_quarter_id`, `capital_program_id`
- `utility.price.fact_rebase`: `rebase_year_code`, `aimed_at_top_flag`, `more_definite_flag`, `fiscal_quarter_id`, `capital_program_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`

### Q2 2025 (3) — Southern Company

For Southern Company, is the rebase still aimed at the top of the long-term growth range?

- `utility.price.fact_earnings_growth`: `growth_rate`, `above_range_flag`, `high_end_includes_incremental_flag`, `fiscal_quarter_id`, `capital_program_id`
- `utility.price.fact_rebase`: `rebase_year_code`, `aimed_at_top_flag`, `more_definite_flag`, `fiscal_quarter_id`, `capital_program_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`

### Q2 2025 (4) — Southern Company

How do Southern Power returns on the added capital compare with the regulated business?

- `utility.supply.fact_wholesale_fleet`: `contracted_quantity`, `upgrade_included_flag`, `fiscal_quarter_id`, `plant_id`, `contract_id`
- `utility.price.fact_regulated_return`: `regulated_return_rate`, `wholesale_gap_rate`, `fiscal_quarter_id`, `capital_program_id`
- `utility.price.fact_capital_plan`: `capital_amount`, `inside_window_amount`, `later_amount`, `layered_even_flag`, `fiscal_quarter_id`, `capital_program_id`, `project_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_plant`: `plant_id`, `plant_code`, `plant_name`, `state_id`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`
