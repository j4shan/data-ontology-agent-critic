# Automaker Inc demand and vehicle slice

This slice is part of the Automaker Inc warehouse. Quantity, capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

## General Motors

### Q1 2026 (2)

Is industry discounting in line with the plan from 90 days ago, and would competitor price increases give GM room to recover higher costs?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_dealer_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_inventory_vehicle_quantity`
- `automaker.demand.fact_gm_retail_sales_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `retail_vehicle_quantity`
- `automaker.price.dim_general_motors_segment`: `general_motors_segment_id`, `general_motors_segment_code`, `general_motors_segment_name`
- `automaker.price.fact_gm_incentive_per_vehicle`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_per_vehicle_amount`

### Q1 2026 (4)

Among demand, vehicle mix, and input costs, which could still move this year's outlook the most?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_brand`: `vehicle_brand_id`, `vehicle_brand_code`, `vehicle_brand_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_captive_finance_contracts`: `fiscal_quarter_id`, `scenario_id`, `borrower_credit_tier_id`, `country_id`, `finance_contract_quantity`, `financed_vehicle_quantity`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`

### Q1 2026 (5)

How long does the updated guidance assume elevated commodity costs last in the second half?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_tariff_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `tariff_rate_percent`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`

### Q1 2026 (7)

Is paid Super Cruise demand concentrated in Cadillac, or is it showing up more broadly across the portfolio?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_gm_service_subscriptions`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `paid_subscription_quantity`, `eligible_vehicle_quantity`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.price.fact_gm_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `service_revenue_amount`, `revenue_per_paid_subscription_amount`

### Q1 2026 (8)

How should the higher GM Financial dividend be read inside adjusted automotive free cash flow?

- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_captive_finance_contracts`: `fiscal_quarter_id`, `scenario_id`, `borrower_credit_tier_id`, `country_id`, `finance_contract_quantity`, `financed_vehicle_quantity`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.price.dim_general_motors_segment`: `general_motors_segment_id`, `general_motors_segment_code`, `general_motors_segment_name`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_gm_finance_book_result`: `fiscal_quarter_id`, `scenario_id`, `borrower_credit_tier_id`, `country_id`, `finance_revenue_amount`, `credit_loss_amount`, `loan_receivable_amount`, `credit_loss_percent`

### Q1 2026 (9)

How should international volume and profit track versus the first quarter, and does the usual pattern of stronger second and third quarters still hold?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`
- `automaker.price.dim_credit_type`: `credit_type_id`, `credit_type_code`, `credit_type_name`
- `automaker.price.dim_general_motors_segment`: `general_motors_segment_id`, `general_motors_segment_code`, `general_motors_segment_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_gm_average_wholesale_price`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `average_wholesale_price_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`

### Q1 2026 (11)

When do digital-services margins look like other software businesses, and how does that cost-to-revenue path evolve over two to three years?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_gm_service_subscriptions`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `paid_subscription_quantity`, `eligible_vehicle_quantity`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `automaker.price.dim_revenue_type`: `revenue_type_id`, `revenue_type_code`, `revenue_type_name`
- `automaker.price.fact_gm_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `service_revenue_amount`, `revenue_per_paid_subscription_amount`

### Q1 2026 (12)

What limits putting digital subscriptions on the large installed base that does not subscribe today, including hardware?

- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.price.fact_gm_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `service_revenue_amount`, `revenue_per_paid_subscription_amount`

### Q1 2026 (13)

What limits expanding Super Cruise road coverage: regulation or GM's own risk appetite?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_state`: `state_id`, `state_name`, `country_id`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_captive_finance_contracts`: `fiscal_quarter_id`, `scenario_id`, `borrower_credit_tier_id`, `country_id`, `finance_contract_quantity`, `financed_vehicle_quantity`
- `automaker.demand.fact_gm_service_subscriptions`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `paid_subscription_quantity`, `eligible_vehicle_quantity`
- `automaker.price.fact_gm_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `service_revenue_amount`, `revenue_per_paid_subscription_amount`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`
- `automaker.supply.fact_regulatory_approvals`: `fiscal_quarter_id`, `scenario_id`, `regulation_type_id`, `country_id`, `required_approval_quantity`, `obtained_approval_quantity`

### Q1 2026 (15)

In the more profitable slices of full-size pickups, is GM holding share, or are competitor gains concentrated in less profitable slices?

- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_gm_retail_sales_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `retail_vehicle_quantity`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_gm_incentive_per_vehicle`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_per_vehicle_amount`

### Q1 2026 (17)

How does wholesale volume cadence change with the truck refresh, and can depleted truck inventory be rebuilt?

- `automaker.demand.dim_body_style`: `body_style_id`, `body_style_code`, `body_style_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`
- `automaker.price.dim_incentive_type`: `incentive_type_id`, `incentive_type_code`, `incentive_type_name`
- `automaker.price.fact_gm_average_wholesale_price`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `average_wholesale_price_amount`
- `automaker.price.fact_gm_incentive_per_vehicle`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_per_vehicle_amount`

### Q1 2026 (18)

After Orion and remaining Mexico capacity come online, where can GM sell more high-value pickups and SUVs: upper trim, lower trim, or outside North America?

- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_captive_finance_contracts`: `fiscal_quarter_id`, `scenario_id`, `borrower_credit_tier_id`, `country_id`, `finance_contract_quantity`, `financed_vehicle_quantity`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_dealer_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_inventory_vehicle_quantity`
- `automaker.demand.fact_gm_retail_sales_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `retail_vehicle_quantity`
- `automaker.price.dim_general_motors_segment`: `general_motors_segment_id`, `general_motors_segment_code`, `general_motors_segment_name`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`

### Q4 2025 (1)

What supports a flat-to-up pricing assumption in a demand-constrained market with a share-seeking competitor, and how much is ICE mix rather than other factors?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_dealer_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_inventory_vehicle_quantity`
- `automaker.demand.fact_gm_retail_sales_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `retail_vehicle_quantity`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`

### Q4 2025 (5)

How is the hybrid, plug-in, and extended-range portfolio evolving, is it inside the stated capital-spending range, and will those vehicles use the next architecture around 2028?

- `automaker.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_dealer_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_inventory_vehicle_quantity`
- `automaker.demand.fact_gm_retail_sales_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `retail_vehicle_quantity`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`

### Q4 2025 (11)

How much of this year's EV volume decline can convert into incremental ICE demand, and how does that change inventory and wholesale planning?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_dealer_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_inventory_vehicle_quantity`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`
- `automaker.price.dim_incentive_type`: `incentive_type_id`, `incentive_type_code`, `incentive_type_name`
- `automaker.price.fact_gm_sales_incentives`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_type_id`, `incentive_amount`

### Q4 2025 (12)

If the quantified puts and takes in guidance roughly net out, what actually lifts earnings, given ICE volume described as flat to slightly up?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.price.dim_incentive_type`: `incentive_type_id`, `incentive_type_code`, `incentive_type_name`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`

### Q3 2025 (2)

How does GM see 2026 demand given consumer and credit worries, and how does a competitor's added pickup product change the competitive setup?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_body_style`: `body_style_id`, `body_style_code`, `body_style_name`
- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_captive_finance_contracts`: `fiscal_quarter_id`, `scenario_id`, `borrower_credit_tier_id`, `country_id`, `finance_contract_quantity`, `financed_vehicle_quantity`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_dealer_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_inventory_vehicle_quantity`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`

### Q3 2025 (3)

Over the next few years, do easier emissions rules create incremental full-size pickup and SUV volume, or does Orion capacity mostly offset tariffs?

- `automaker.demand.dim_body_style`: `body_style_id`, `body_style_code`, `body_style_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_state`: `state_id`, `state_name`, `country_id`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.fact_plant_downtime`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `vehicle_nameplate_id`, `downtime_day_quantity`, `planned_downtime_day_quantity`

### Q3 2025 (5)

What mix of lower overhead and lower EV sales is assumed in smaller EV losses, and do vehicles that struggle to cover variable profit still need to be sold without a regulatory requirement?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_gm_retail_sales_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `retail_vehicle_quantity`
- `automaker.price.dim_incentive_type`: `incentive_type_id`, `incentive_type_code`, `incentive_type_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_capital_spending_by_nameplate`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `program_capital_spending_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_gm_sales_incentives`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_type_id`, `incentive_amount`

### Q3 2025 (11)

Do Chinese automakers eventually sell in the United States, and how would that entry evolve?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_dealer_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_inventory_vehicle_quantity`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.price.dim_incentive_type`: `incentive_type_id`, `incentive_type_code`, `incentive_type_name`
- `automaker.price.fact_tariff_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `tariff_rate_percent`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`

### Q2 2025 (4)

What would put second-half earnings at the low end versus the high end of the wide range?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_body_style`: `body_style_id`, `body_style_code`, `body_style_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_gm_average_wholesale_price`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `average_wholesale_price_amount`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`

### Q2 2025 (5)

About where could U.S. dealer inventory finish the year after share gains and a seasonal wholesale decline?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_body_style`: `body_style_id`, `body_style_code`, `body_style_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_dealer_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_inventory_vehicle_quantity`
- `automaker.demand.fact_gm_retail_sales_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `retail_vehicle_quantity`
- `automaker.price.dim_incentive_type`: `incentive_type_id`, `incentive_type_code`, `incentive_type_name`
- `automaker.price.fact_gm_sales_incentives`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_type_id`, `incentive_amount`

## Tesla

### Q2 2026 (3)

Which safety or reliability milestones would cause Tesla to speed up robotaxi fleet growth and new-market launches?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_energy_product`: `energy_product_id`, `energy_product_code`, `energy_product_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_launch_stage`: `launch_stage_id`, `launch_stage_code`, `launch_stage_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_brand`: `vehicle_brand_id`, `vehicle_brand_code`, `vehicle_brand_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_robotaxi_fleet`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `vehicle_nameplate_id`, `launch_stage_id`, `robotaxi_vehicle_quantity`, `served_city_quantity`
- `automaker.demand.fact_robotaxi_miles`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `autonomy_capability_id`, `autonomous_mile_quantity`, `safety_intervention_quantity`
- `automaker.demand.fact_tesla_customer_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `delivered_vehicle_quantity`
- `automaker.price.fact_robotaxi_fare_revenue`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `fare_revenue_amount`

### Q2 2026 (4)

Would Tesla use rideshare partners to raise robotaxi utilization, or keep the service vertically integrated?

- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_energy_product`: `energy_product_id`, `energy_product_code`, `energy_product_name`
- `automaker.demand.dim_energy_use_case`: `energy_use_case_id`, `energy_use_case_code`, `energy_use_case_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_launch_stage`: `launch_stage_id`, `launch_stage_code`, `launch_stage_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_robotaxi_fleet`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `vehicle_nameplate_id`, `launch_stage_id`, `robotaxi_vehicle_quantity`, `served_city_quantity`
- `automaker.price.fact_robotaxi_cost_per_mile`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `cost_per_mile_amount`
- `automaker.price.fact_robotaxi_operating_cost`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `robotaxi_operating_cost_amount`
- `automaker.price.fact_tesla_software_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `recognized_software_revenue_amount`, `deferred_software_revenue_amount`, `revenue_per_paid_subscription_amount`

### Q2 2026 (5)

Why is Tesla adding cities while the robotaxi vehicle count still looks small, and what blocks a much larger fleet in one major city?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_launch_stage`: `launch_stage_id`, `launch_stage_code`, `launch_stage_name`
- `automaker.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_brand`: `vehicle_brand_id`, `vehicle_brand_code`, `vehicle_brand_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_robotaxi_fleet`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `vehicle_nameplate_id`, `launch_stage_id`, `robotaxi_vehicle_quantity`, `served_city_quantity`
- `automaker.demand.fact_robotaxi_miles`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `autonomy_capability_id`, `autonomous_mile_quantity`, `safety_intervention_quantity`
- `automaker.price.fact_robotaxi_cost_per_mile`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `cost_per_mile_amount`
- `automaker.price.fact_robotaxi_fare_revenue`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `fare_revenue_amount`

### Q2 2026 (10)

When does Optimus 4 production start relative to the much larger volume target versus Optimus 3?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.demand.fact_tesla_customer_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `delivered_vehicle_quantity`
- `automaker.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`
- `automaker.supply.dim_robot_product`: `robot_product_id`, `robot_product_code`, `robot_product_name`
- `automaker.supply.dim_sourcing_mode`: `sourcing_mode_id`, `sourcing_mode_code`, `sourcing_mode_name`
- `automaker.supply.fact_regulatory_approvals`: `fiscal_quarter_id`, `scenario_id`, `regulation_type_id`, `country_id`, `required_approval_quantity`, `obtained_approval_quantity`
- `automaker.supply.fact_robot_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `robot_product_id`, `plant_id`, `annual_robot_capacity_quantity`, `produced_robot_quantity`

### Q2 2026 (11)

Is Tesla still planning hardware upgrades so older camera-equipped cars can run newer Full Self-Driving software?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_vehicle_brand`: `vehicle_brand_id`, `vehicle_brand_code`, `vehicle_brand_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_charging_network_quantity`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `charging_connector_quantity`, `charging_session_quantity`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.demand.fact_tesla_software_subscriptions`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `paid_subscription_quantity`, `trial_vehicle_quantity`, `eligible_vehicle_quantity`
- `automaker.price.fact_tesla_software_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `recognized_software_revenue_amount`, `deferred_software_revenue_amount`, `revenue_per_paid_subscription_amount`

### Q2 2026 (13)

How long will energy-storage deployments stay supply-constrained?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_energy_product`: `energy_product_id`, `energy_product_code`, `energy_product_name`
- `automaker.demand.dim_energy_use_case`: `energy_use_case_id`, `energy_use_case_code`, `energy_use_case_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.fact_energy_storage_backlog`: `fiscal_quarter_id`, `scenario_id`, `energy_product_id`, `country_id`, `backlog_energy_quantity`, `ordered_energy_quantity`
- `automaker.demand.fact_energy_storage_deployments`: `fiscal_quarter_id`, `scenario_id`, `energy_product_id`, `energy_use_case_id`, `country_id`, `deployed_energy_quantity`, `deployed_unit_quantity`
- `automaker.price.dim_revenue_type`: `revenue_type_id`, `revenue_type_code`, `revenue_type_name`
- `automaker.price.fact_energy_revenue`: `fiscal_quarter_id`, `scenario_id`, `energy_product_id`, `country_id`, `energy_revenue_amount`, `revenue_per_megawatt_hour_amount`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.dim_robot_product`: `robot_product_id`, `robot_product_code`, `robot_product_name`
- `automaker.supply.fact_energy_product_production`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `energy_product_id`, `produced_storage_energy_quantity`, `produced_unit_quantity`

### Q2 2026 (14)

How much current storage demand is data-center power smoothing versus utility peak shaving and grid balancing?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_energy_product`: `energy_product_id`, `energy_product_code`, `energy_product_name`
- `automaker.demand.dim_energy_use_case`: `energy_use_case_id`, `energy_use_case_code`, `energy_use_case_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_brand`: `vehicle_brand_id`, `vehicle_brand_code`, `vehicle_brand_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_charging_network_quantity`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `charging_connector_quantity`, `charging_session_quantity`
- `automaker.demand.fact_energy_storage_backlog`: `fiscal_quarter_id`, `scenario_id`, `energy_product_id`, `country_id`, `backlog_energy_quantity`, `ordered_energy_quantity`
- `automaker.demand.fact_energy_storage_deployments`: `fiscal_quarter_id`, `scenario_id`, `energy_product_id`, `energy_use_case_id`, `country_id`, `deployed_energy_quantity`, `deployed_unit_quantity`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`

### Q3 2025 (2)

Which AI applications sit inside Tesla's core work, and which markets should stay outside it?

- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_energy_product`: `energy_product_id`, `energy_product_code`, `energy_product_name`
- `automaker.demand.dim_energy_use_case`: `energy_use_case_id`, `energy_use_case_code`, `energy_use_case_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_launch_stage`: `launch_stage_id`, `launch_stage_code`, `launch_stage_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_brand`: `vehicle_brand_id`, `vehicle_brand_code`, `vehicle_brand_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_charging_network_quantity`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `charging_connector_quantity`, `charging_session_quantity`
- `automaker.demand.fact_energy_storage_backlog`: `fiscal_quarter_id`, `scenario_id`, `energy_product_id`, `country_id`, `backlog_energy_quantity`, `ordered_energy_quantity`
- `automaker.demand.fact_energy_storage_deployments`: `fiscal_quarter_id`, `scenario_id`, `energy_product_id`, `energy_use_case_id`, `country_id`, `deployed_energy_quantity`, `deployed_unit_quantity`
- `automaker.demand.fact_robotaxi_fleet`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `vehicle_nameplate_id`, `launch_stage_id`, `robotaxi_vehicle_quantity`, `served_city_quantity`
- `automaker.price.dim_tesla_business_activity`: `tesla_business_activity_id`, `tesla_business_activity_code`, `tesla_business_activity_name`

### Q2 2025 (1)

How many robotaxis are operating, how many autonomous miles and safety-critical interventions have they logged, and what targets should follow?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.fact_robotaxi_miles`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `autonomy_capability_id`, `autonomous_mile_quantity`, `safety_intervention_quantity`
- `automaker.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `automaker.price.fact_robotaxi_cost_per_mile`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `cost_per_mile_amount`
- `automaker.price.fact_robotaxi_fare_revenue`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `fare_revenue_amount`
- `automaker.price.fact_robotaxi_operating_cost`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `robotaxi_operating_cost_amount`

### Q2 2025 (3)

What has to happen, and on what timeline, before customer-owned vehicles can join the robotaxi network?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_launch_stage`: `launch_stage_id`, `launch_stage_code`, `launch_stage_name`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.demand.fact_robotaxi_fleet`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `vehicle_nameplate_id`, `launch_stage_id`, `robotaxi_vehicle_quantity`, `served_city_quantity`
- `automaker.demand.fact_tesla_customer_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `delivered_vehicle_quantity`
- `automaker.demand.fact_vehicle_orders`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `customer_type_id`, `ordered_vehicle_quantity`
- `automaker.supply.dim_robot_product`: `robot_product_id`, `robot_product_code`, `robot_product_name`

### Q2 2025 (6)

Will Tesla cut vehicle prices to hold volume as U.S. purchase credits end, or keep cuts smaller than cost reductions because free cash flow is tighter?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_energy_product`: `energy_product_id`, `energy_product_code`, `energy_product_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_brand`: `vehicle_brand_id`, `vehicle_brand_code`, `vehicle_brand_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_robotaxi_miles`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `autonomy_capability_id`, `autonomous_mile_quantity`, `safety_intervention_quantity`
- `automaker.demand.fact_tesla_customer_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `delivered_vehicle_quantity`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_tesla_average_selling_price`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `average_selling_price_amount`, `price_change_percent`

### Q2 2025 (7)

Which cost reductions from the prior plan, such as less silicon carbide and no rare earths in the motor, are actually in the lower-cost vehicle that ramps later?

- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.price.dim_credit_type`: `credit_type_id`, `credit_type_code`, `credit_type_name`
- `automaker.price.fact_regulatory_credit_cost`: `fiscal_quarter_id`, `scenario_id`, `credit_type_id`, `credit_purchase_amount`, `avoided_credit_purchase_amount`
- `automaker.price.fact_tariff_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `tariff_rate_percent`
- `automaker.price.fact_tesla_average_selling_price`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `average_selling_price_amount`, `price_change_percent`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`
- `automaker.supply.dim_robot_product`: `robot_product_id`, `robot_product_code`, `robot_product_name`
