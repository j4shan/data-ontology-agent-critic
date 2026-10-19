# Automaker Inc price, tariff and profit slice

This slice is part of the Automaker Inc warehouse. Quantity, capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

## General Motors

### Q1 2026 (1)

How large is the revenue-per-vehicle opportunity for software and services on the software-defined platform planned for 2028?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_brand`: `vehicle_brand_id`, `vehicle_brand_code`, `vehicle_brand_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.price.fact_gm_average_wholesale_price`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `average_wholesale_price_amount`
- `automaker.price.fact_gm_incentive_per_vehicle`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_per_vehicle_amount`
- `automaker.price.fact_gm_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `service_revenue_amount`, `revenue_per_paid_subscription_amount`

### Q1 2026 (3)

Are the planned onshoring and software costs already hitting, or are they weighted to the rest of the year?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.dim_revenue_type`: `revenue_type_id`, `revenue_type_code`, `revenue_type_name`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_gm_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `service_revenue_amount`, `revenue_per_paid_subscription_amount`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`

### Q1 2026 (10)

Does the full-size truck changeover hit fourth-quarter volume, or is the volume effect already behind the company?

- `automaker.demand.dim_body_style`: `body_style_id`, `body_style_code`, `body_style_name`
- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.fact_plant_downtime`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `vehicle_nameplate_id`, `downtime_day_quantity`, `planned_downtime_day_quantity`

### Q1 2026 (14)

If commodity inflation carries into 2027, how much cost mitigation can offset it?

- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `automaker.price.dim_credit_type`: `credit_type_id`, `credit_type_code`, `credit_type_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_regulatory_credit_cost`: `fiscal_quarter_id`, `scenario_id`, `credit_type_id`, `credit_purchase_amount`, `avoided_credit_purchase_amount`
- `automaker.price.fact_research_and_development`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `cost_category_id`, `research_and_development_amount`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`

### Q1 2026 (16)

Which commodities are hedged, and are any raw materials already short or at risk if conflict persists?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_state`: `state_id`, `state_name`, `country_id`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_gm_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `service_revenue_amount`, `revenue_per_paid_subscription_amount`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_supplier`: `supplier_id`, `supplier_name`, `country_id`

### Q1 2026 (19)

How much Mexico capacity stays after Orion depends on where USMCA talks land?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `capital_spending_amount`
- `automaker.price.fact_capital_spending_by_nameplate`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `program_capital_spending_amount`
- `automaker.price.fact_tariff_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `tariff_rate_percent`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`

### Q1 2026 (20)

How far along are the China product refresh and restructuring, and is current equity income a finished run rate?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_brand`: `vehicle_brand_id`, `vehicle_brand_code`, `vehicle_brand_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_gm_china_equity_income`: `fiscal_quarter_id`, `scenario_id`, `china_joint_venture_equity_income_amount`
- `automaker.price.fact_tariff_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `tariff_rate_percent`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`

### Q1 2026 (21)

How profitable are China exports versus domestic China sales, and how is that outlet evolving?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_brand`: `vehicle_brand_id`, `vehicle_brand_code`, `vehicle_brand_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_gm_retail_sales_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `retail_vehicle_quantity`
- `automaker.price.dim_incentive_type`: `incentive_type_id`, `incentive_type_code`, `incentive_type_name`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_gm_sales_incentives`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_type_id`, `incentive_amount`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`

### Q4 2025 (2)

With EV programs and battery capacity still sized for a higher volume outlook, how well does that fixed cost fit a nearer-term mix that is richer in ICE?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`
- `automaker.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_research_and_development`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `cost_category_id`, `research_and_development_amount`
- `automaker.supply.dim_battery_chemistry`: `battery_chemistry_id`, `battery_chemistry_code`, `battery_chemistry_name`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.fact_battery_cell_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `battery_chemistry_id`, `annual_cell_capacity_quantity`

### Q4 2025 (3)

Will tight inventory discipline continue, and is it a reason cash generation is running ahead of expectations?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_captive_finance_contracts`: `fiscal_quarter_id`, `scenario_id`, `borrower_credit_tier_id`, `country_id`, `finance_contract_quantity`, `financed_vehicle_quantity`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`

### Q4 2025 (4)

How much does an industrial-bank approval lower GM Financial's cost of capital?

- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_captive_finance_contracts`: `fiscal_quarter_id`, `scenario_id`, `borrower_credit_tier_id`, `country_id`, `finance_contract_quantity`, `financed_vehicle_quantity`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`
- `automaker.price.dim_general_motors_segment`: `general_motors_segment_id`, `general_motors_segment_code`, `general_motors_segment_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_gm_finance_book_result`: `fiscal_quarter_id`, `scenario_id`, `borrower_credit_tier_id`, `country_id`, `finance_revenue_amount`, `credit_loss_amount`, `loan_receivable_amount`, `credit_loss_percent`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`

### Q4 2025 (6)

Of the onshoring and software spending, how much is temporary startup cost versus ongoing software expense?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_gm_incentive_per_vehicle`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_per_vehicle_amount`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`

### Q4 2025 (7)

If the South Korea tariff moved back toward 25%, what would that do to the gross tariff assumption that used a lower rate?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_capital_spending_by_nameplate`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `program_capital_spending_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_tariff_cost`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `component_id`, `gross_tariff_amount`, `tariff_offset_amount`, `net_tariff_amount`
- `automaker.price.fact_tariff_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `tariff_rate_percent`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`
- `automaker.supply.dim_sourcing_mode`: `sourcing_mode_id`, `sourcing_mode_code`, `sourcing_mode_name`

### Q4 2025 (13)

Why is this year's pricing assumption more constructive than last year's expectation of a decline?

- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_capital_spending_by_nameplate`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `program_capital_spending_amount`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`

### Q4 2025 (14)

Beyond lower EV losses, is there more mix benefit from a richer ICE mix under looser emissions rules or from rebuilding very lean inventories?

- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_state`: `state_id`, `state_name`, `country_id`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.price.dim_credit_type`: `credit_type_id`, `credit_type_code`, `credit_type_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_capital_spending_by_nameplate`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `program_capital_spending_amount`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_regulatory_credit_cost`: `fiscal_quarter_id`, `scenario_id`, `credit_type_id`, `credit_purchase_amount`, `avoided_credit_purchase_amount`

### Q4 2025 (15)

What drives the expected warranty benefit, how much of the V8-engine issue is already reserved, and why is the benefit still credible after the investigation reopened?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_gm_incentive_per_vehicle`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_per_vehicle_amount`
- `automaker.price.fact_warranty_expense`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `component_id`, `warranty_expense_amount`, `warranty_reserve_amount`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.fact_warranty_claims`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `component_id`, `warranty_claim_quantity`

### Q4 2025 (16)

Why is the expected savings from no longer buying emissions credits smaller than the roughly annual amount previously spent?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_brand`: `vehicle_brand_id`, `vehicle_brand_code`, `vehicle_brand_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.price.dim_credit_type`: `credit_type_id`, `credit_type_code`, `credit_type_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_gm_average_wholesale_price`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `average_wholesale_price_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_regulatory_credit_cost`: `fiscal_quarter_id`, `scenario_id`, `credit_type_id`, `credit_purchase_amount`, `avoided_credit_purchase_amount`

### Q4 2025 (17)

What drives the large step-up in Super Cruise revenue, and is Super Cruise the main digital-services driver or are other OnStar areas growing too?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_gm_service_subscriptions`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `paid_subscription_quantity`, `eligible_vehicle_quantity`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.price.fact_gm_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `service_revenue_amount`, `revenue_per_paid_subscription_amount`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`

### Q4 2025 (18)

If the China market softens after last year's stimulus, what lets GM hold China profit about flat?

- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.price.dim_general_motors_segment`: `general_motors_segment_id`, `general_motors_segment_code`, `general_motors_segment_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_gm_average_wholesale_price`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `average_wholesale_price_amount`
- `automaker.price.fact_gm_china_equity_income`: `fiscal_quarter_id`, `scenario_id`, `china_joint_venture_equity_income_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_gm_incentive_per_vehicle`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_per_vehicle_amount`

### Q3 2025 (1)

Does the lower gross tariff from the MSRP offset reflect more parts coverage, including engines, and how does that offset work?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_tariff_cost`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `component_id`, `gross_tariff_amount`, `tariff_offset_amount`, `net_tariff_amount`
- `automaker.price.fact_tariff_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `tariff_rate_percent`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`

### Q3 2025 (4)

With price looking maxed out, how much runway is left in cost and footprint tariff mitigation into 2026, and is any Korea-tariff relief excluded from this year's guide?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.price.dim_credit_type`: `credit_type_id`, `credit_type_code`, `credit_type_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_regulatory_credit_cost`: `fiscal_quarter_id`, `scenario_id`, `credit_type_id`, `credit_purchase_amount`, `avoided_credit_purchase_amount`
- `automaker.price.fact_tariff_cost`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `component_id`, `gross_tariff_amount`, `tariff_offset_amount`, `net_tariff_amount`
- `automaker.price.fact_tariff_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `tariff_rate_percent`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`

### Q3 2025 (6)

Does moving faster make GM less capital intensive in calmer markets, and is that best seen in cash flow or capex relative to revenue?

- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_captive_finance_contracts`: `fiscal_quarter_id`, `scenario_id`, `borrower_credit_tier_id`, `country_id`, `finance_contract_quantity`, `financed_vehicle_quantity`
- `automaker.demand.fact_gm_retail_sales_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `retail_vehicle_quantity`
- `automaker.price.dim_incentive_type`: `incentive_type_id`, `incentive_type_code`, `incentive_type_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_gm_finance_book_result`: `fiscal_quarter_id`, `scenario_id`, `borrower_credit_tier_id`, `country_id`, `finance_revenue_amount`, `credit_loss_amount`, `loan_receivable_amount`, `credit_loss_percent`

### Q3 2025 (7)

What has to happen for North America margins to return to 8% to 10%, and is that feasible without a large tariff reduction?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_brand`: `vehicle_brand_id`, `vehicle_brand_code`, `vehicle_brand_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_capital_spending_by_nameplate`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `program_capital_spending_amount`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`

### Q3 2025 (9)

How are prime GM Financial borrowers at above-average transaction prices performing versus subprime, and what would a weaker U.S. job market do to the portfolio?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.price.dim_general_motors_segment`: `general_motors_segment_id`, `general_motors_segment_code`, `general_motors_segment_name`
- `automaker.price.fact_gm_average_wholesale_price`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `average_wholesale_price_amount`
- `automaker.price.fact_gm_finance_book_result`: `fiscal_quarter_id`, `scenario_id`, `borrower_credit_tier_id`, `country_id`, `finance_revenue_amount`, `credit_loss_amount`, `loan_receivable_amount`, `credit_loss_percent`
- `automaker.price.fact_gm_segment_result`: `fiscal_quarter_id`, `scenario_id`, `general_motors_segment_id`, `segment_revenue_amount`, `segment_operating_income_amount`
- `automaker.supply.dim_sourcing_mode`: `sourcing_mode_id`, `sourcing_mode_code`, `sourcing_mode_name`

### Q3 2025 (10)

Is a stronger 2026 still excluding both unfinished Korea-tariff relief and the elimination of greenhouse-gas or fuel-economy credit purchases?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.price.dim_credit_type`: `credit_type_id`, `credit_type_code`, `credit_type_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_regulatory_credit_cost`: `fiscal_quarter_id`, `scenario_id`, `credit_type_id`, `credit_purchase_amount`, `avoided_credit_purchase_amount`
- `automaker.price.fact_tariff_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `tariff_rate_percent`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`

### Q3 2025 (12)

Is GM pursuing a robotaxi, or personal Level 4 first, how profitable is Super Cruise, and what autonomy milestones are set for 2026?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_gm_service_subscriptions`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `paid_subscription_quantity`, `eligible_vehicle_quantity`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_gm_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `service_revenue_amount`, `revenue_per_paid_subscription_amount`

### Q3 2025 (13)

By how much do the recent EV asset write-downs and capacity shifts lower structural EV cost?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.price.dim_incentive_type`: `incentive_type_id`, `incentive_type_code`, `incentive_type_name`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_gm_sales_incentives`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_type_id`, `incentive_amount`
- `automaker.price.fact_tariff_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `tariff_rate_percent`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`

### Q3 2025 (14)

Does lower EV capital spending reduce company-wide capex, or is that money needed elsewhere?

- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `capital_spending_amount`
- `automaker.price.fact_capital_spending_by_nameplate`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `program_capital_spending_amount`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`

### Q3 2025 (15)

Why is wholesale average price up much more than the smaller pricing contribution in the earnings walk?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.price.dim_incentive_type`: `incentive_type_id`, `incentive_type_code`, `incentive_type_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_gm_average_wholesale_price`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `average_wholesale_price_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_gm_incentive_per_vehicle`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_per_vehicle_amount`

### Q3 2025 (16)

How much of the earnings walk from lower EV losses is simply lower EV incentives, with a smaller effect on ICE?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.price.dim_incentive_type`: `incentive_type_id`, `incentive_type_code`, `incentive_type_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_capital_spending_by_nameplate`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `program_capital_spending_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_gm_incentive_per_vehicle`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_per_vehicle_amount`
- `automaker.price.fact_gm_sales_incentives`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_type_id`, `incentive_amount`

### Q3 2025 (17)

Is the Hyundai development partnership for South America the way GM competes with Chinese automakers abroad, and is GM pushing international markets again?

- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_gm_retail_sales_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `retail_vehicle_quantity`
- `automaker.price.dim_general_motors_segment`: `general_motors_segment_id`, `general_motors_segment_code`, `general_motors_segment_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_gm_incentive_per_vehicle`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_per_vehicle_amount`

### Q3 2025 (18)

What 2026 tariff rates on Mexico and Canada are assumed in the outlook?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.price.dim_incentive_type`: `incentive_type_id`, `incentive_type_code`, `incentive_type_name`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_gm_sales_incentives`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_type_id`, `incentive_amount`
- `automaker.price.fact_tariff_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `tariff_rate_percent`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_component_level`: `component_level_id`, `component_level_code`, `component_level_name`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`

### Q2 2025 (1)

As purchase credits end and rules change, how broad should the EV lineup stay, and do profitable price points move higher?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_state`: `state_id`, `state_name`, `country_id`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.price.dim_incentive_type`: `incentive_type_id`, `incentive_type_code`, `incentive_type_name`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_gm_average_wholesale_price`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `average_wholesale_price_amount`
- `automaker.price.fact_gm_sales_incentives`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_type_id`, `incentive_amount`
- `automaker.price.fact_gm_wholesale_revenue`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_revenue_amount`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`

### Q2 2025 (2)

Is there a clear path to profit on the affordable EV?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.price.dim_incentive_type`: `incentive_type_id`, `incentive_type_code`, `incentive_type_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_capital_spending_by_nameplate`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `program_capital_spending_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_gm_incentive_per_vehicle`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_per_vehicle_amount`
- `automaker.price.fact_gm_sales_incentives`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_type_id`, `incentive_amount`

### Q2 2025 (3)

How do the new U.S. manufacturing investments change net tariff cost beyond this year?

- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_gm_cost_of_capital`: `fiscal_quarter_id`, `scenario_id`, `lending_institution_type_id`, `cost_of_capital_percent`
- `automaker.price.fact_tariff_cost`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `component_id`, `gross_tariff_amount`, `tariff_offset_amount`, `net_tariff_amount`
- `automaker.price.fact_tariff_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `tariff_rate_percent`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`

### Q2 2025 (6)

What in GM's EV design, scale, or supplier setup supports a profit if a larger Western EV maker is still loss-making once credits and retail are set aside?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_gm_retail_sales_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `retail_vehicle_quantity`
- `automaker.price.dim_incentive_type`: `incentive_type_id`, `incentive_type_code`, `incentive_type_name`
- `automaker.price.dim_lending_institution_type`: `lending_institution_type_id`, `lending_institution_type_code`, `lending_institution_type_name`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_gm_sales_incentives`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_type_id`, `incentive_amount`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`

### Q2 2025 (7)

If the Korea tariff status quo lasts, do better local economics justify keeping current Korea production and capacity?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `automaker.price.fact_tariff_cost`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `component_id`, `gross_tariff_amount`, `tariff_offset_amount`, `net_tariff_amount`
- `automaker.price.fact_tariff_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `tariff_rate_percent`
- `automaker.supply.dim_battery_chemistry`: `battery_chemistry_id`, `battery_chemistry_code`, `battery_chemistry_name`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`
- `automaker.supply.fact_battery_cell_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `battery_chemistry_id`, `annual_cell_capacity_quantity`
- `automaker.supply.fact_vehicle_assembly_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `annual_vehicle_capacity_quantity`

### Q2 2025 (8)

Given a better-than-feared China result and a tougher Europe, should GM concentrate more on the U.S. than on those two markets?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.price.dim_incentive_type`: `incentive_type_id`, `incentive_type_code`, `incentive_type_name`
- `automaker.price.fact_gm_incentive_per_vehicle`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_per_vehicle_amount`
- `automaker.price.fact_gm_sales_incentives`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_type_id`, `incentive_amount`
- `automaker.price.fact_gm_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `service_revenue_amount`, `revenue_per_paid_subscription_amount`

## Tesla

### Q2 2026 (1)

Are outside suppliers putting capital into U.S. manufacturing for Optimus, or does Tesla still have to build most of that supply chain itself to ramp faster?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_energy_product`: `energy_product_id`, `energy_product_code`, `energy_product_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_tesla_customer_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `delivered_vehicle_quantity`
- `automaker.price.fact_supplier_commitment_amount`: `fiscal_quarter_id`, `scenario_id`, `supplier_id`, `country_id`, `supplier_commitment_amount`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`
- `automaker.supply.dim_robot_product`: `robot_product_id`, `robot_product_code`, `robot_product_name`
- `automaker.supply.dim_sourcing_mode`: `sourcing_mode_id`, `sourcing_mode_code`, `sourcing_mode_name`
- `automaker.supply.dim_supplier`: `supplier_id`, `supplier_name`, `country_id`
- `automaker.supply.fact_energy_product_production`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `energy_product_id`, `produced_storage_energy_quantity`, `produced_unit_quantity`
- `automaker.supply.fact_robot_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `robot_product_id`, `plant_id`, `annual_robot_capacity_quantity`, `produced_robot_quantity`

### Q2 2026 (2)

What state-level sensor rules would Tesla need, or want to avoid, before it expands the robotaxi rollout?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_energy_product`: `energy_product_id`, `energy_product_code`, `energy_product_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_launch_stage`: `launch_stage_id`, `launch_stage_code`, `launch_stage_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_state`: `state_id`, `state_name`, `country_id`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_robotaxi_fleet`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `vehicle_nameplate_id`, `launch_stage_id`, `robotaxi_vehicle_quantity`, `served_city_quantity`
- `automaker.demand.fact_robotaxi_miles`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `autonomy_capability_id`, `autonomous_mile_quantity`, `safety_intervention_quantity`
- `automaker.price.fact_robotaxi_cost_per_mile`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `cost_per_mile_amount`
- `automaker.price.fact_robotaxi_operating_cost`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `robotaxi_operating_cost_amount`

### Q2 2026 (7)

Could Cybercabs with Starlink act as mobile hotspots, not only as connected vehicles for passengers?

- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_energy_use_case`: `energy_use_case_id`, `energy_use_case_code`, `energy_use_case_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_launch_stage`: `launch_stage_id`, `launch_stage_code`, `launch_stage_name`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.demand.fact_robotaxi_fleet`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `vehicle_nameplate_id`, `launch_stage_id`, `robotaxi_vehicle_quantity`, `served_city_quantity`
- `automaker.demand.fact_tesla_customer_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `delivered_vehicle_quantity`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`

### Q2 2026 (8)

When does Tesla expect unsupervised driving on the Semi, given the truck-driver shortage?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_body_style`: `body_style_id`, `body_style_code`, `body_style_name`
- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_energy_product`: `energy_product_id`, `energy_product_code`, `energy_product_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.price.fact_energy_revenue`: `fiscal_quarter_id`, `scenario_id`, `energy_product_id`, `country_id`, `energy_revenue_amount`, `revenue_per_megawatt_hour_amount`
- `automaker.price.fact_robotaxi_cost_per_mile`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `cost_per_mile_amount`
- `automaker.price.fact_robotaxi_operating_cost`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `robotaxi_operating_cost_amount`
- `automaker.price.fact_tesla_software_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `recognized_software_revenue_amount`, `deferred_software_revenue_amount`, `revenue_per_paid_subscription_amount`

### Q2 2026 (12)

Is capital spending currently limited by how fast Tesla can spend without waste, and is that pace what unlocks constrained supply?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_energy_product`: `energy_product_id`, `energy_product_code`, `energy_product_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_brand`: `vehicle_brand_id`, `vehicle_brand_code`, `vehicle_brand_name`
- `automaker.demand.fact_charging_network_quantity`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `charging_connector_quantity`, `charging_session_quantity`
- `automaker.price.fact_supplier_commitment_amount`: `fiscal_quarter_id`, `scenario_id`, `supplier_id`, `country_id`, `supplier_commitment_amount`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.dim_robot_product`: `robot_product_id`, `robot_product_code`, `robot_product_name`
- `automaker.supply.dim_supplier`: `supplier_id`, `supplier_name`, `country_id`
- `automaker.supply.fact_energy_product_production`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `energy_product_id`, `produced_storage_energy_quantity`, `produced_unit_quantity`
- `automaker.supply.fact_robot_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `robot_product_id`, `plant_id`, `annual_robot_capacity_quantity`, `produced_robot_quantity`

### Q4 2025 (2)

Is the higher capital-spending level a 2026 spike or a multi-year run rate?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `capital_spending_amount`
- `automaker.price.fact_capital_spending_by_nameplate`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `program_capital_spending_amount`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_supplier_commitment_amount`: `fiscal_quarter_id`, `scenario_id`, `supplier_id`, `country_id`, `supplier_commitment_amount`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.dim_supplier`: `supplier_id`, `supplier_name`, `country_id`

### Q4 2025 (3)

Are memory shortages constraining near-term production, and would Tesla cut features the way it did during earlier chip shortages?

- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_energy_product`: `energy_product_id`, `energy_product_code`, `energy_product_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_energy_revenue`: `fiscal_quarter_id`, `scenario_id`, `energy_product_id`, `country_id`, `energy_revenue_amount`, `revenue_per_megawatt_hour_amount`
- `automaker.price.fact_tesla_average_selling_price`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `average_selling_price_amount`, `price_change_percent`
- `automaker.price.fact_tesla_software_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `recognized_software_revenue_amount`, `deferred_software_revenue_amount`, `revenue_per_paid_subscription_amount`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_robot_product`: `robot_product_id`, `robot_product_code`, `robot_product_name`

### Q4 2025 (5)

How do battery, memory, and purpose-built hardware programs share R&D, and what advantage does that create across end markets?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_research_and_development`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `cost_category_id`, `research_and_development_amount`
- `automaker.supply.dim_battery_chemistry`: `battery_chemistry_id`, `battery_chemistry_code`, `battery_chemistry_name`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.dim_plant_function`: `plant_function_id`, `plant_function_code`, `plant_function_name`
- `automaker.supply.fact_battery_cell_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `battery_chemistry_id`, `annual_cell_capacity_quantity`
- `automaker.supply.fact_battery_production`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `battery_chemistry_id`, `produced_energy_quantity`

### Q3 2025 (1)

If vehicle output is to rise as fast as possible, does that mean filling the existing roughly 3 million-unit capacity, on what timeline, and would that favor volume over near-term profit?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_brand`: `vehicle_brand_id`, `vehicle_brand_code`, `vehicle_brand_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_tesla_customer_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `delivered_vehicle_quantity`
- `automaker.price.fact_capital_spending_by_nameplate`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `program_capital_spending_amount`
- `automaker.price.fact_tesla_average_selling_price`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `average_selling_price_amount`, `price_change_percent`
- `automaker.price.fact_tesla_vehicle_revenue`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `vehicle_revenue_amount`

### Q3 2025 (3)

If the safety driver can leave the Austin robotaxi at year-end, is the Bay Area limit regulation or local learning, and do new cities start with an attendant?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_launch_stage`: `launch_stage_id`, `launch_stage_code`, `launch_stage_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_state`: `state_id`, `state_name`, `country_id`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_robotaxi_fleet`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `vehicle_nameplate_id`, `launch_stage_id`, `robotaxi_vehicle_quantity`, `served_city_quantity`
- `automaker.demand.fact_robotaxi_miles`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `autonomy_capability_id`, `autonomous_mile_quantity`, `safety_intervention_quantity`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`

### Q3 2025 (4)

Are consumer Full Self-Driving builds on a different path from the robotaxi stack, and are new releases aimed at fewer interventions or at added functions such as parking and comfort?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_energy_product`: `energy_product_id`, `energy_product_code`, `energy_product_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_launch_stage`: `launch_stage_id`, `launch_stage_code`, `launch_stage_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.price.fact_energy_revenue`: `fiscal_quarter_id`, `scenario_id`, `energy_product_id`, `country_id`, `energy_revenue_amount`, `revenue_per_megawatt_hour_amount`
- `automaker.price.fact_robotaxi_cost_per_mile`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `cost_per_mile_amount`
- `automaker.price.fact_robotaxi_operating_cost`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `robotaxi_operating_cost_amount`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`

### Q2 2025 (2)

Now that the service is live, what milestones bring robotaxi cost per mile down toward the previously discussed range?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_launch_stage`: `launch_stage_id`, `launch_stage_code`, `launch_stage_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_robotaxi_fleet`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `vehicle_nameplate_id`, `launch_stage_id`, `robotaxi_vehicle_quantity`, `served_city_quantity`
- `automaker.demand.fact_robotaxi_miles`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `autonomy_capability_id`, `autonomous_mile_quantity`, `safety_intervention_quantity`
- `automaker.price.fact_robotaxi_cost_per_mile`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `cost_per_mile_amount`
- `automaker.price.fact_robotaxi_operating_cost`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `robotaxi_operating_cost_amount`

### Q2 2025 (4)

What costs rise as the robotaxi business scales, and can automotive cash flow fund them?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_tesla_average_selling_price`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `average_selling_price_amount`, `price_change_percent`
- `automaker.price.fact_tesla_vehicle_revenue`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `vehicle_revenue_amount`

### Q2 2025 (5)

What are current Full Self-Driving subscription trends, take rates, and revenue after the consumer trials?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_energy_product`: `energy_product_id`, `energy_product_code`, `energy_product_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.demand.fact_tesla_software_subscriptions`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `paid_subscription_quantity`, `trial_vehicle_quantity`, `eligible_vehicle_quantity`
- `automaker.price.dim_revenue_type`: `revenue_type_id`, `revenue_type_code`, `revenue_type_name`
- `automaker.price.fact_energy_revenue`: `fiscal_quarter_id`, `scenario_id`, `energy_product_id`, `country_id`, `energy_revenue_amount`, `revenue_per_megawatt_hour_amount`
- `automaker.price.fact_tesla_software_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `recognized_software_revenue_amount`, `deferred_software_revenue_amount`, `revenue_per_paid_subscription_amount`
