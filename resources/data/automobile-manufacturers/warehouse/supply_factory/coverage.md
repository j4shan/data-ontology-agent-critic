# Automaker Inc factory and component supply slice

This slice is part of the Automaker Inc warehouse. Quantity, capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

## General Motors

### Q1 2026 (6)

Should investors expect more factory downtime as the next full-size pickup launches?

- `automaker.demand.dim_body_style`: `body_style_id`, `body_style_code`, `body_style_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.price.fact_gm_average_wholesale_price`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `average_wholesale_price_amount`
- `automaker.price.fact_gm_wholesale_revenue`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_revenue_amount`
- `automaker.supply.dim_battery_chemistry`: `battery_chemistry_id`, `battery_chemistry_code`, `battery_chemistry_name`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.fact_plant_downtime`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `vehicle_nameplate_id`, `downtime_day_quantity`, `planned_downtime_day_quantity`

### Q4 2025 (8)

What approvals are required to take Super Cruise abroad, and what functionality, including point-to-point, should customers see next?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.demand.fact_gm_service_subscriptions`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `paid_subscription_quantity`, `eligible_vehicle_quantity`
- `automaker.price.fact_gm_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `vehicle_nameplate_id`, `service_revenue_amount`, `revenue_per_paid_subscription_amount`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`
- `automaker.supply.dim_sourcing_mode`: `sourcing_mode_id`, `sourcing_mode_code`, `sourcing_mode_name`
- `automaker.supply.fact_regulatory_approvals`: `fiscal_quarter_id`, `scenario_id`, `regulation_type_id`, `country_id`, `required_approval_quantity`, `obtained_approval_quantity`

### Q4 2025 (9)

How much of this year's memory-chip supply and price is already locked?

- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.dim_supplier`: `supplier_id`, `supplier_name`, `country_id`
- `automaker.supply.fact_component_cover`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `supplier_id`, `cover_week_quantity`, `alternate_source_week_quantity`
- `automaker.supply.fact_vehicle_assembly_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `annual_vehicle_capacity_quantity`

### Q4 2025 (10)

How much downtime is in the full-size pickup launch guide, and do volume and price-mix effects land this year or in 2027?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_state`: `state_id`, `state_name`, `country_id`
- `automaker.demand.dim_trim_level`: `trim_level_id`, `trim_level_code`, `trim_level_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_gm_wholesale_quantity`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `wholesale_vehicle_quantity`
- `automaker.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`, `automotive_cash_flow_amount`
- `automaker.price.fact_gm_incentive_per_vehicle`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `incentive_per_vehicle_amount`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.fact_plant_downtime`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `vehicle_nameplate_id`, `downtime_day_quantity`, `planned_downtime_day_quantity`

### Q3 2025 (8)

How many weeks of aluminum, semiconductors, and rare earths do GM and suppliers hold, and how quickly can alternate supply be brought up?

- `automaker.demand.dim_borrower_credit_tier`: `borrower_credit_tier_id`, `borrower_credit_tier_code`, `borrower_credit_tier_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_captive_finance_contracts`: `fiscal_quarter_id`, `scenario_id`, `borrower_credit_tier_id`, `country_id`, `finance_contract_quantity`, `financed_vehicle_quantity`
- `automaker.demand.fact_dealer_inventory_days`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `dealer_supply_days`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_component_level`: `component_level_id`, `component_level_code`, `component_level_name`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.dim_plant_function`: `plant_function_id`, `plant_function_code`, `plant_function_name`
- `automaker.supply.dim_supplier`: `supplier_id`, `supplier_name`, `country_id`
- `automaker.supply.fact_component_cover`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `supplier_id`, `cover_week_quantity`, `alternate_source_week_quantity`
- `automaker.supply.fact_vehicle_assembly_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `annual_vehicle_capacity_quantity`

## Tesla

### Q2 2026 (6)

Beyond removing the steering wheel and pedals, what federal approvals still gate a Cybercab production ramp?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_body_style`: `body_style_id`, `body_style_code`, `body_style_name`
- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_launch_stage`: `launch_stage_id`, `launch_stage_code`, `launch_stage_name`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.demand.fact_robotaxi_fleet`: `fiscal_quarter_id`, `scenario_id`, `city_id`, `vehicle_nameplate_id`, `launch_stage_id`, `robotaxi_vehicle_quantity`, `served_city_quantity`
- `automaker.price.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `commodity_cost_amount`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`
- `automaker.supply.fact_regulatory_approvals`: `fiscal_quarter_id`, `scenario_id`, `regulation_type_id`, `country_id`, `required_approval_quantity`, `obtained_approval_quantity`

### Q2 2026 (9)

For Optimus processors, controllers, and actuators, how much will Tesla buy, design for outside fabs, or make itself?

- `automaker.demand.dim_city`: `city_id`, `city_name`, `country_id`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_energy_product`: `energy_product_id`, `energy_product_code`, `energy_product_name`
- `automaker.demand.dim_energy_use_case`: `energy_use_case_id`, `energy_use_case_code`, `energy_use_case_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_charging_network_quantity`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `charging_connector_quantity`, `charging_session_quantity`
- `automaker.demand.fact_energy_storage_backlog`: `fiscal_quarter_id`, `scenario_id`, `energy_product_id`, `country_id`, `backlog_energy_quantity`, `ordered_energy_quantity`
- `automaker.supply.dim_component`: `component_id`, `component_code`, `component_name`, `component_level_id`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.dim_robot_product`: `robot_product_id`, `robot_product_code`, `robot_product_name`
- `automaker.supply.dim_sourcing_mode`: `sourcing_mode_id`, `sourcing_mode_code`, `sourcing_mode_name`
- `automaker.supply.fact_component_sourcing_quantity`: `fiscal_quarter_id`, `scenario_id`, `component_id`, `sourcing_mode_id`, `vehicle_nameplate_id`, `component_quantity`
- `automaker.supply.fact_robot_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `robot_product_id`, `plant_id`, `annual_robot_capacity_quantity`, `produced_robot_quantity`

### Q4 2025 (1)

Which products and technologies account for most of the step-up in capital spending above $20 billion?

- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_energy_product`: `energy_product_id`, `energy_product_code`, `energy_product_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_powertrain`: `powertrain_id`, `powertrain_code`, `powertrain_name`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.dim_vehicle_nameplate`: `vehicle_nameplate_id`, `vehicle_nameplate_code`, `vehicle_nameplate_name`, `vehicle_brand_id`, `body_style_id`
- `automaker.demand.fact_installed_vehicle_base`: `fiscal_quarter_id`, `scenario_id`, `vehicle_nameplate_id`, `country_id`, `powertrain_id`, `installed_vehicle_quantity`, `software_equipped_vehicle_quantity`
- `automaker.price.fact_supplier_commitment_amount`: `fiscal_quarter_id`, `scenario_id`, `supplier_id`, `country_id`, `supplier_commitment_amount`
- `automaker.price.fact_tariff_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `regulation_type_id`, `tariff_rate_percent`
- `automaker.supply.dim_component_level`: `component_level_id`, `component_level_code`, `component_level_name`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.dim_regulation_type`: `regulation_type_id`, `regulation_type_code`, `regulation_type_name`
- `automaker.supply.dim_robot_product`: `robot_product_id`, `robot_product_code`, `robot_product_name`
- `automaker.supply.dim_supplier`: `supplier_id`, `supplier_name`, `country_id`
- `automaker.supply.fact_energy_product_production`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `energy_product_id`, `produced_storage_energy_quantity`, `produced_unit_quantity`

### Q4 2025 (4)

What keeps Optimus ahead of the new humanoid startups, especially from China, and how will the product differ?

- `automaker.demand.dim_autonomy_capability`: `autonomy_capability_id`, `autonomy_capability_code`, `autonomy_capability_name`
- `automaker.demand.dim_body_style`: `body_style_id`, `body_style_code`, `body_style_name`
- `automaker.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `automaker.demand.dim_energy_product`: `energy_product_id`, `energy_product_code`, `energy_product_name`
- `automaker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `automaker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `automaker.demand.fact_energy_storage_backlog`: `fiscal_quarter_id`, `scenario_id`, `energy_product_id`, `country_id`, `backlog_energy_quantity`, `ordered_energy_quantity`
- `automaker.price.fact_energy_revenue`: `fiscal_quarter_id`, `scenario_id`, `energy_product_id`, `country_id`, `energy_revenue_amount`, `revenue_per_megawatt_hour_amount`
- `automaker.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `automaker.supply.dim_robot_product`: `robot_product_id`, `robot_product_code`, `robot_product_name`
- `automaker.supply.fact_energy_product_production`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `energy_product_id`, `produced_storage_energy_quantity`, `produced_unit_quantity`
- `automaker.supply.fact_robot_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `robot_product_id`, `plant_id`, `annual_robot_capacity_quantity`, `produced_robot_quantity`
