# Utility Inc price slice

This slice is part of the Utility Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q2 2026 (1) — Duke Energy

For Duke Energy, With additional capital and late-stage load already at the top of the earnings-growth range, could the next update push the growth rate higher?

- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.price.dim_rate_case`: `rate_case_id`, `rate_case_name`, `jurisdiction_id`, `operating_company_id`
- `utility.price.fact_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `distribution_capital_amount`
- `utility.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `utility.price.fact_gas_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `gas_distribution_capital_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (3) — Duke Energy

For Duke Energy, How much of the potential Florida and Indiana large-load capital lands inside the next five-year plan versus the mid-2030s?

- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.price.fact_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `distribution_capital_amount`
- `utility.price.fact_gas_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `gas_distribution_capital_amount`
- `utility.price.fact_generation_capital`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `technology_id`, `generation_capital_amount`
- `utility.price.fact_reliability_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `reliability_capital_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (10) — Duke Energy

For Duke Energy, As near-term tax-credit cash from nuclear and batteries rolls off, does cash flow from new-investment recovery replace it?

- `utility.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `utility.price.fact_rate_base`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `rate_base_amount`, `authorized_return_percent`, `earned_return_percent`
- `utility.price.fact_rate_case_outcome`: `fiscal_quarter_id`, `scenario_id`, `rate_case_id`, `jurisdiction_id`, `operating_company_id`, `authorized_revenue_requirement_amount`, `rate_change_percent`, `authorized_rate_base_amount`
- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.demand.fact_electricity_sales_energy`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `end_use_id`, `operating_company_id`, `jurisdiction_id`, `electricity_sales_quantity`
- `utility.demand.fact_monthly_electricity_sales`: `fiscal_quarter_id`, `scenario_id`, `calendar_month_id`, `rate_class_id`, `operating_company_id`, `monthly_electricity_sales_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (1) — Duke Energy

For Duke Energy, Is a partial settlement possible in the Carolinas rate cases?

- `utility.price.dim_rate_case`: `rate_case_id`, `rate_case_name`, `jurisdiction_id`, `operating_company_id`
- `utility.price.fact_rate_case_outcome`: `fiscal_quarter_id`, `scenario_id`, `rate_case_id`, `jurisdiction_id`, `operating_company_id`, `authorized_revenue_requirement_amount`, `rate_change_percent`, `authorized_rate_base_amount`
- `utility.price.fact_gas_distribution_revenue`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `revenue_type_id`, `gas_distribution_revenue_amount`
- `utility.price.fact_purchased_power_rate`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `purchased_power_rate_amount`
- `utility.price.fact_rate_base`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `rate_base_amount`, `authorized_return_percent`, `earned_return_percent`
- `utility.price.fact_retail_rate`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `retail_rate_per_megawatt_hour`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (4) — Duke Energy

For Duke Energy, Would the company join a utility, hyperscaler, and government structure aimed at nuclear cost-overrun risk?

- `utility.price.fact_fuel_purchased_power_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `fuel_type_id`, `fuel_expense_amount`, `purchased_power_expense_amount`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `operating_expense_amount`
- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `utility.price.dim_rate_case`: `rate_case_id`, `rate_case_name`, `jurisdiction_id`, `operating_company_id`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (6) — Duke Energy

For Duke Energy, Do Carolinas combination savings and tax credits offset the current rate request?

- `utility.price.dim_rate_case`: `rate_case_id`, `rate_case_name`, `jurisdiction_id`, `operating_company_id`
- `utility.price.fact_rate_case_outcome`: `fiscal_quarter_id`, `scenario_id`, `rate_case_id`, `jurisdiction_id`, `operating_company_id`, `authorized_revenue_requirement_amount`, `rate_change_percent`, `authorized_rate_base_amount`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.dim_rate_class`: `rate_class_id`, `rate_class_code`, `rate_class_name`
- `utility.demand.fact_county_customer_count`: `fiscal_quarter_id`, `scenario_id`, `county_id`, `rate_class_id`, `operating_company_id`, `county_customer_quantity`
- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (7) — Duke Energy

For Duke Energy, Are data-center or fuel-cost bills in the legislative session material to load or cost sharing?

- `utility.price.fact_fuel_purchased_power_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `fuel_type_id`, `fuel_expense_amount`, `purchased_power_expense_amount`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `utility.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `operating_expense_amount`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (8) — Duke Energy

For Duke Energy, Has top-of-funnel data-center interest accelerated, and are any regions emerging as larger hubs?

- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `utility.price.dim_rate_case`: `rate_case_id`, `rate_case_name`, `jurisdiction_id`, `operating_company_id`
- `utility.price.dim_revenue_type`: `revenue_type_id`, `revenue_type_code`, `revenue_type_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (9) — Duke Energy

For Duke Energy, When do the latest tax-credit monetization benefits flow back to customers?

- `utility.demand.fact_county_customer_count`: `fiscal_quarter_id`, `scenario_id`, `county_id`, `rate_class_id`, `operating_company_id`, `county_customer_quantity`
- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.demand.fact_gas_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `gas_customer_quantity`
- `utility.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (1) — Duke Energy

For Duke Energy, What storm costs are still open, and are they already in the earnings midpoint?

- `utility.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `utility.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `utility.price.fact_fuel_purchased_power_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `fuel_type_id`, `fuel_expense_amount`, `purchased_power_expense_amount`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `operating_expense_amount`
- `utility.price.fact_segment_earnings`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `earnings_amount`, `revenue_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (2) — Duke Energy

For Duke Energy, Does the Carolinas case, with the combination and affordability focus, need to be fully litigated or can it settle?

- `utility.price.dim_rate_case`: `rate_case_id`, `rate_case_name`, `jurisdiction_id`, `operating_company_id`
- `utility.price.fact_rate_case_outcome`: `fiscal_quarter_id`, `scenario_id`, `rate_case_id`, `jurisdiction_id`, `operating_company_id`, `authorized_revenue_requirement_amount`, `rate_change_percent`, `authorized_rate_base_amount`
- `utility.price.fact_gas_distribution_revenue`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `revenue_type_id`, `gas_distribution_revenue_amount`
- `utility.price.fact_purchased_power_rate`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `purchased_power_rate_amount`
- `utility.price.fact_rate_base`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `rate_base_amount`, `authorized_return_percent`, `earned_return_percent`
- `utility.price.fact_retail_rate`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `retail_rate_per_megawatt_hour`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (3) — Duke Energy

For Duke Energy, How confident is the company in rolling incremental data-center opportunities into the capital plan?

- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.price.fact_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `distribution_capital_amount`
- `utility.price.fact_gas_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `gas_distribution_capital_amount`
- `utility.price.fact_reliability_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `reliability_capital_amount`
- `utility.price.fact_total_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `capital_spending_amount`
- `utility.price.fact_transmission_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `transmission_capital_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (4) — Duke Energy

For Duke Energy, What explains the gap between rate-base growth and earnings growth, and can that gap narrow in the Carolinas?

- `utility.price.fact_rate_base`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `rate_base_amount`, `authorized_return_percent`, `earned_return_percent`
- `utility.price.fact_rate_case_outcome`: `fiscal_quarter_id`, `scenario_id`, `rate_case_id`, `jurisdiction_id`, `operating_company_id`, `authorized_revenue_requirement_amount`, `rate_change_percent`, `authorized_rate_base_amount`
- `utility.price.dim_rate_case`: `rate_case_id`, `rate_case_name`, `jurisdiction_id`, `operating_company_id`
- `utility.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `utility.price.fact_gas_distribution_revenue`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `revenue_type_id`, `gas_distribution_revenue_amount`
- `utility.price.fact_purchased_power_rate`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `purchased_power_rate_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (5) — Duke Energy

For Duke Energy, What earned returns and other conditions are required to deliver the top half of the growth range from 2028?

- `utility.price.fact_rate_base`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `rate_base_amount`, `authorized_return_percent`, `earned_return_percent`
- `utility.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `utility.price.fact_segment_earnings`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `earnings_amount`, `revenue_amount`
- `utility.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `utility.price.dim_rate_case`: `rate_case_id`, `rate_case_name`, `jurisdiction_id`, `operating_company_id`
- `utility.price.dim_revenue_type`: `revenue_type_id`, `revenue_type_code`, `revenue_type_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (7) — Duke Energy

For Duke Energy, What is the timing and capital for gas, nuclear, and hydro uprate opportunities?

- `utility.price.fact_gas_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `gas_distribution_capital_amount`
- `utility.price.fact_generation_capital`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `technology_id`, `generation_capital_amount`
- `utility.supply.fact_interconnection_queue`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `queued_capacity_quantity`, `interconnection_request_quantity`
- `utility.supply.fact_planned_capacity`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `planned_capacity_quantity`
- `utility.supply.fact_storage_capacity`: `fiscal_quarter_id`, `scenario_id`, `storage_type_id`, `operating_company_id`, `technology_id`, `storage_power_capacity_quantity`
- `utility.price.fact_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `distribution_capital_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (8) — Duke Energy

For Duke Energy, Are data-center approvals being structured so residential customers are kept whole?

- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `utility.price.fact_shareholder_distributions`: `fiscal_quarter_id`, `scenario_id`, `dividend_amount`, `buyback_amount`, `dividend_per_share_amount`
- `utility.demand.fact_county_customer_count`: `fiscal_quarter_id`, `scenario_id`, `county_id`, `rate_class_id`, `operating_company_id`, `county_customer_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (10) — Duke Energy

For Duke Energy, How much data-center load is already inside the enterprise and Carolinas sales-growth ranges, and how would more signed agreements change those ranges?

- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `utility.price.fact_rate_case_outcome`: `fiscal_quarter_id`, `scenario_id`, `rate_case_id`, `jurisdiction_id`, `operating_company_id`, `authorized_revenue_requirement_amount`, `rate_change_percent`, `authorized_rate_base_amount`
- `utility.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (11) — Duke Energy

For Duke Energy, Would a North Carolina large-load tariff reach back to agreements already signed?

- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `utility.price.fact_segment_earnings`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `earnings_amount`, `revenue_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.fact_electricity_sales_energy`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `end_use_id`, `operating_company_id`, `jurisdiction_id`, `electricity_sales_quantity`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (1) — Duke Energy

For Duke Energy, Is the incremental capital expected to layer in evenly across the planning period?

- `utility.price.fact_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `distribution_capital_amount`
- `utility.price.fact_gas_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `gas_distribution_capital_amount`
- `utility.price.fact_generation_capital`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `technology_id`, `generation_capital_amount`
- `utility.price.fact_reliability_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `reliability_capital_amount`
- `utility.price.fact_total_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `capital_spending_amount`
- `utility.price.fact_transmission_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `transmission_capital_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (2) — Duke Energy

For Duke Energy, What projects make up the incremental capital opportunity of roughly $10 billion?

- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.price.fact_generation_capital`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `technology_id`, `generation_capital_amount`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.supply.dim_generation_unit`: `generation_unit_id`, `generation_unit_name`, `generating_station_id`
- `utility.price.fact_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `distribution_capital_amount`
- `utility.price.fact_gas_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `gas_distribution_capital_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (4) — Duke Energy

For Duke Energy, Does the high end of the earnings-growth range already reflect incremental capital, including the confidence in hitting that high end from 2028?

- `utility.price.fact_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `distribution_capital_amount`
- `utility.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `utility.price.fact_gas_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `gas_distribution_capital_amount`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.price.fact_generation_capital`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `technology_id`, `generation_capital_amount`
- `utility.price.fact_rate_base`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `rate_base_amount`, `authorized_return_percent`, `earned_return_percent`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (5) — Duke Energy

For Duke Energy, What balance-sheet conditions would allow the lower end of the equity share used to fund capital upside?

- `utility.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `utility.demand.fact_electricity_sales_energy`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `end_use_id`, `operating_company_id`, `jurisdiction_id`, `electricity_sales_quantity`
- `utility.price.fact_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `distribution_capital_amount`
- `utility.price.fact_gas_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `gas_distribution_capital_amount`
- `utility.price.fact_generation_capital`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `technology_id`, `generation_capital_amount`
- `utility.price.fact_reliability_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `reliability_capital_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (1) — Southern Company

For Southern Company, How does better visibility on contracted megawatts and the 2028 load ramp change how far regulatory plans can be extended?

- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.price.fact_rate_case_outcome`: `fiscal_quarter_id`, `scenario_id`, `rate_case_id`, `jurisdiction_id`, `operating_company_id`, `authorized_revenue_requirement_amount`, `rate_change_percent`, `authorized_rate_base_amount`
- `utility.price.fact_transmission_revenue`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `revenue_type_id`, `transmission_revenue_amount`
- `utility.demand.fact_electricity_sales_energy`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `end_use_id`, `operating_company_id`, `jurisdiction_id`, `electricity_sales_quantity`
- `utility.supply.fact_substation_capacity`: `fiscal_quarter_id`, `scenario_id`, `substation_id`, `operating_company_id`, `substation_capacity_quantity`, `substation_peak_load_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (5) — Southern Company

For Southern Company, Are hyperscalers willing to take cost-overrun risk above budget on new large reactors?

- `utility.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `utility.price.fact_fuel_purchased_power_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `fuel_type_id`, `fuel_expense_amount`, `purchased_power_expense_amount`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `operating_expense_amount`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (11) — Southern Company

For Southern Company, Has the customer-rate benefit of data centers changed the political reception in Georgia?

- `utility.price.fact_rate_base`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `rate_base_amount`, `authorized_return_percent`, `earned_return_percent`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.dim_rate_class`: `rate_class_id`, `rate_class_code`, `rate_class_name`
- `utility.demand.fact_county_customer_count`: `fiscal_quarter_id`, `scenario_id`, `county_id`, `rate_class_id`, `operating_company_id`, `county_customer_quantity`
- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (12) — Southern Company

For Southern Company, Is the gigawatt of demand response a first for a data center, and have the customer savings been quantified?

- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.dim_meter_type`: `meter_type_id`, `meter_type_code`, `meter_type_name`
- `utility.demand.dim_rate_class`: `rate_class_id`, `rate_class_code`, `rate_class_name`
- `utility.demand.fact_county_customer_count`: `fiscal_quarter_id`, `scenario_id`, `county_id`, `rate_class_id`, `operating_company_id`, `county_customer_quantity`
- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (13) — Southern Company

For Southern Company, How do Georgia and Alabama turn this load growth into rates, including the chance of a larger rate credit in Georgia?

- `utility.price.dim_rate_case`: `rate_case_id`, `rate_case_name`, `jurisdiction_id`, `operating_company_id`
- `utility.price.fact_rate_case_outcome`: `fiscal_quarter_id`, `scenario_id`, `rate_case_id`, `jurisdiction_id`, `operating_company_id`, `authorized_revenue_requirement_amount`, `rate_change_percent`, `authorized_rate_base_amount`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.price.fact_gas_distribution_revenue`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `revenue_type_id`, `gas_distribution_revenue_amount`
- `utility.price.fact_purchased_power_rate`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `purchased_power_rate_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (15) — Southern Company

For Southern Company, What has the recent data-center ramp taught about sales trends?

- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `utility.price.fact_segment_earnings`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `earnings_amount`, `revenue_amount`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (1) — Southern Company

For Southern Company, Would the company join a utility and hyperscaler structure in which hyperscalers take cost inflation above budget on new reactors?

- `utility.price.fact_fuel_purchased_power_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `fuel_type_id`, `fuel_expense_amount`, `purchased_power_expense_amount`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `operating_expense_amount`
- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `utility.price.dim_rate_case`: `rate_case_id`, `rate_case_name`, `jurisdiction_id`, `operating_company_id`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (10) — Southern Company

For Southern Company, Would a new build also depend on contracting the plant before it is completed, given upgrade costs that approach new-build costs?

- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.demand.fact_gas_throughput`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `gas_throughput_quantity`
- `utility.supply.fact_generation_fuel_consumption`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `fuel_type_id`, `generation_fuel_quantity`
- `utility.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `utility.price.dim_rate_case`: `rate_case_id`, `rate_case_name`, `jurisdiction_id`, `operating_company_id`
- `utility.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (1) — Southern Company

For Southern Company, How are Georgia customers receiving the new large-load tariff, and how does the minimum bill protect cost recovery?

- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_county_customer_count`: `fiscal_quarter_id`, `scenario_id`, `county_id`, `rate_class_id`, `operating_company_id`, `county_customer_quantity`
- `utility.demand.fact_gas_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `gas_customer_quantity`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (2) — Southern Company

For Southern Company, How could upcoming commission elections affect generation certifications in Georgia?

- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.price.fact_generation_capital`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `technology_id`, `generation_capital_amount`
- `utility.demand.dim_jurisdiction`: `jurisdiction_id`, `jurisdiction_name`
- `utility.demand.fact_gas_throughput`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `gas_throughput_quantity`
- `utility.supply.dim_generation_unit`: `generation_unit_id`, `generation_unit_name`, `generating_station_id`
- `utility.supply.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (3) — Southern Company

For Southern Company, What operational, regulatory, or signed data-center milestones would make a 2027 rebase more definite?

- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `utility.price.fact_rate_base`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `rate_base_amount`, `authorized_return_percent`, `earned_return_percent`
- `utility.price.fact_segment_earnings`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `earnings_amount`, `revenue_amount`
- `utility.demand.dim_jurisdiction`: `jurisdiction_id`, `jurisdiction_name`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (9) — Southern Company

For Southern Company, In which year is the targeted sales-growth rate expected to be reached?

- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.fact_electricity_sales_energy`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `end_use_id`, `operating_company_id`, `jurisdiction_id`, `electricity_sales_quantity`
- `utility.demand.fact_monthly_electricity_sales`: `fiscal_quarter_id`, `scenario_id`, `calendar_month_id`, `rate_class_id`, `operating_company_id`, `monthly_electricity_sales_quantity`
- `utility.price.dim_rate_case`: `rate_case_id`, `rate_case_name`, `jurisdiction_id`, `operating_company_id`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (10) — Southern Company

For Southern Company, Is the average large-load project a few hundred megawatts, and are the later-stage projects greenfield or brownfield?

- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.supply.fact_transmission_system`: `fiscal_quarter_id`, `scenario_id`, `transmission_asset_id`, `operating_company_id`, `transfer_capacity_quantity`, `circuit_mile_quantity`
- `utility.price.fact_transmission_revenue`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `revenue_type_id`, `transmission_revenue_amount`
- `utility.demand.fact_meter_count`: `fiscal_quarter_id`, `scenario_id`, `meter_type_id`, `rate_class_id`, `operating_company_id`, `meter_quantity`
- `utility.supply.fact_distribution_system`: `fiscal_quarter_id`, `scenario_id`, `distribution_asset_id`, `operating_company_id`, `distribution_circuit_mile_quantity`, `distribution_asset_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (1) — Southern Company

For Southern Company, Does the higher rate-base growth path change the 2027 rebase or the long-term growth view?

- `utility.price.fact_rate_case_outcome`: `fiscal_quarter_id`, `scenario_id`, `rate_case_id`, `jurisdiction_id`, `operating_company_id`, `authorized_revenue_requirement_amount`, `rate_change_percent`, `authorized_rate_base_amount`
- `utility.price.fact_rate_base`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `rate_base_amount`, `authorized_return_percent`, `earned_return_percent`
- `utility.price.dim_rate_case`: `rate_case_id`, `rate_case_name`, `jurisdiction_id`, `operating_company_id`
- `utility.price.fact_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `distribution_capital_amount`
- `utility.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `utility.price.fact_gas_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `gas_distribution_capital_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (3) — Southern Company

For Southern Company, Is the rebase still aimed at the top of the long-term growth range?

- `utility.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `utility.price.fact_segment_earnings`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `earnings_amount`, `revenue_amount`
- `utility.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `utility.price.dim_rate_case`: `rate_case_id`, `rate_case_name`, `jurisdiction_id`, `operating_company_id`
- `utility.price.dim_revenue_type`: `revenue_type_id`, `revenue_type_code`, `revenue_type_name`
- `utility.price.fact_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `distribution_capital_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (4) — Southern Company

For Southern Company, How do Southern Power returns on the added capital compare with the regulated business?

- `utility.price.dim_revenue_type`: `revenue_type_id`, `revenue_type_code`, `revenue_type_name`
- `utility.price.fact_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `distribution_capital_amount`
- `utility.price.fact_fuel_purchased_power_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `fuel_type_id`, `fuel_expense_amount`, `purchased_power_expense_amount`
- `utility.price.fact_gas_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `gas_distribution_capital_amount`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.price.fact_generation_capital`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `technology_id`, `generation_capital_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (8) — Southern Company

For Southern Company, After completing the resource-plan process, how durable is the demand outlook over the next few years?

- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `utility.demand.dim_county`: `county_id`, `county_name`, `state_id`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (10) — Southern Company

For Southern Company, What generation-cost inflation is being assumed for future combined cycles and peakers?

- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `utility.price.fact_fuel_purchased_power_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `fuel_type_id`, `fuel_expense_amount`, `purchased_power_expense_amount`
- `utility.price.fact_generation_capital`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `technology_id`, `generation_capital_amount`
- `utility.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `operating_expense_amount`
- `utility.demand.fact_gas_throughput`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `gas_throughput_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
