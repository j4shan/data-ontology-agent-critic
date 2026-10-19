# Energy Inc supply slice

This slice is part of the Energy Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q2 2026 (6) — Chevron

For Chevron, If the export pipeline is closed for a long time, how much of the liquids can move on alternative routes?

- `energy.supply.fact_pipeline_throughput`: `fiscal_quarter_id`, `scenario_id`, `pipeline_id`, `hydrocarbon_id`, `pipeline_throughput_quantity`
- `energy.demand.fact_export_volume`: `fiscal_quarter_id`, `scenario_id`, `trade_route_id`, `hydrocarbon_id`, `market_id`, `export_quantity`
- `energy.supply.dim_field`: `field_id`, `field_name`, `country_id`
- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.supply.dim_operator_affiliate`: `operator_affiliate_id`, `operator_affiliate_name`, `country_id`
- `energy.supply.dim_pipeline`: `pipeline_id`, `pipeline_name`, `region_id`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (8) — Chevron

For Chevron, What uncommitted LNG is available to respond to a tight European gas market as Australian plants ramp in the second half?

- `energy.demand.fact_lng_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `lng_cargo_quantity`, `lng_demand_quantity`
- `energy.supply.dim_lng_terminal`: `lng_terminal_id`, `lng_terminal_name`, `country_id`
- `energy.price.fact_lng_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `lng_price_amount`
- `energy.price.fact_trading_optimization`: `fiscal_quarter_id`, `scenario_id`, `trading_desk_id`, `market_id`, `calendar_month_id`, `trading_income_amount`, `optimization_income_amount`
- `energy.supply.dim_field`: `field_id`, `field_name`, `country_id`
- `energy.supply.fact_affiliate_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `operator_affiliate_id`, `hydrocarbon_id`, `asset_id`, `country_id`, `affiliate_gross_production_quantity`, `affiliate_net_production_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (12) — Chevron

For Chevron, Beyond the contracted power project, is there more value from acreage and wells already in the county?

- `energy.supply.dim_power_plant`: `power_plant_id`, `power_plant_name`, `country_id`
- `energy.supply.fact_power_generation`: `fiscal_quarter_id`, `scenario_id`, `power_plant_id`, `power_generation_quantity`
- `energy.supply.dim_asset`: `asset_id`, `asset_name`, `country_id`, `field_id`
- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.supply.dim_play`: `play_id`, `play_name`, `region_id`
- `energy.supply.dim_project`: `project_id`, `project_name`, `asset_id`, `field_id`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (6) — Chevron

For Chevron, What is driving Tengiz above nameplate, and what debottlenecking remains?

- `energy.supply.fact_basin_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `basin_id`, `hydrocarbon_id`, `play_id`, `basin_capacity_quantity`
- `energy.supply.fact_chemical_capacity`: `fiscal_quarter_id`, `scenario_id`, `chemical_plant_id`, `chemical_product_id`, `chemical_capacity_quantity`
- `energy.supply.fact_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `asset_id`, `hydrocarbon_id`, `production_capacity_quantity`
- `energy.supply.dim_facility_type`: `facility_type_id`, `facility_type_code`, `facility_type_name`
- `energy.supply.dim_field`: `field_id`, `field_name`, `country_id`
- `energy.supply.dim_operator_affiliate`: `operator_affiliate_id`, `operator_affiliate_name`, `country_id`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (1) — Chevron

For Chevron, How do Tengiz volumes in the year ahead reflect the maintenance schedule, the power-distribution issue, and debottlenecking?

- `energy.supply.dim_facility_type`: `facility_type_id`, `facility_type_code`, `facility_type_name`
- `energy.supply.dim_field`: `field_id`, `field_name`, `country_id`
- `energy.supply.dim_operator_affiliate`: `operator_affiliate_id`, `operator_affiliate_name`, `country_id`
- `energy.supply.dim_power_plant`: `power_plant_id`, `power_plant_name`, `country_id`
- `energy.supply.fact_basin_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `basin_id`, `hydrocarbon_id`, `play_id`, `basin_capacity_quantity`
- `energy.supply.fact_chemical_capacity`: `fiscal_quarter_id`, `scenario_id`, `chemical_plant_id`, `chemical_product_id`, `chemical_capacity_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (7) — Chevron

For Chevron, Can heavy Venezuela barrels be run on the Gulf Coast and elsewhere, alongside a competitor closing California capacity?

- `energy.supply.fact_basin_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `basin_id`, `hydrocarbon_id`, `play_id`, `basin_capacity_quantity`
- `energy.supply.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `country_id`, `facility_capacity_quantity`
- `energy.supply.fact_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `asset_id`, `hydrocarbon_id`, `production_capacity_quantity`
- `energy.supply.fact_refinery_capacity`: `fiscal_quarter_id`, `scenario_id`, `refinery_id`, `refinery_capacity_quantity`
- `energy.supply.fact_affiliate_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `operator_affiliate_id`, `hydrocarbon_id`, `asset_id`, `country_id`, `affiliate_gross_production_quantity`, `affiliate_net_production_quantity`
- `energy.supply.fact_monthly_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `calendar_month_id`, `hydrocarbon_id`, `field_id`, `asset_id`, `monthly_gross_production_quantity`, `monthly_net_production_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (4) — Chevron

For Chevron, How prospective is Namibia after the early wells and a larger campaign?

- `energy.supply.fact_well_activity`: `fiscal_quarter_id`, `scenario_id`, `play_id`, `field_id`, `well_type_id`, `rig_type_id`, `well_quantity`, `rig_quantity`
- `energy.supply.dim_well_type`: `well_type_id`, `well_type_code`, `well_type_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.supply.dim_asset`: `asset_id`, `asset_name`, `country_id`, `field_id`
- `energy.supply.dim_basin`: `basin_id`, `basin_name`, `region_id`
- `energy.supply.dim_chemical_plant`: `chemical_plant_id`, `chemical_plant_name`, `country_id`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (8) — Chevron

For Chevron, Is Tengiz essentially at capacity even with a fourth-quarter turnaround?

- `energy.supply.dim_facility_type`: `facility_type_id`, `facility_type_code`, `facility_type_name`
- `energy.supply.dim_field`: `field_id`, `field_name`, `country_id`
- `energy.supply.dim_operator_affiliate`: `operator_affiliate_id`, `operator_affiliate_name`, `country_id`
- `energy.supply.fact_basin_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `basin_id`, `hydrocarbon_id`, `play_id`, `basin_capacity_quantity`
- `energy.supply.fact_chemical_capacity`: `fiscal_quarter_id`, `scenario_id`, `chemical_plant_id`, `chemical_product_id`, `chemical_capacity_quantity`
- `energy.supply.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `country_id`, `facility_capacity_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (11) — Chevron

For Chevron, What is different about Permian operations versus smaller peers that are dropping rigs and completion crews?

- `energy.supply.fact_well_activity`: `fiscal_quarter_id`, `scenario_id`, `play_id`, `field_id`, `well_type_id`, `rig_type_id`, `well_quantity`, `rig_quantity`
- `energy.supply.fact_affiliate_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `operator_affiliate_id`, `hydrocarbon_id`, `asset_id`, `country_id`, `affiliate_gross_production_quantity`, `affiliate_net_production_quantity`
- `energy.supply.fact_basin_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `basin_id`, `hydrocarbon_id`, `play_id`, `basin_capacity_quantity`
- `energy.supply.fact_chemical_capacity`: `fiscal_quarter_id`, `scenario_id`, `chemical_plant_id`, `chemical_product_id`, `chemical_capacity_quantity`
- `energy.supply.fact_chemical_production`: `fiscal_quarter_id`, `scenario_id`, `chemical_plant_id`, `chemical_product_id`, `chemical_production_quantity`
- `energy.supply.fact_lng_production`: `fiscal_quarter_id`, `scenario_id`, `lng_terminal_id`, `lng_production_quantity`, `lng_cargo_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (6) — Exxon Mobil

For Exxon Mobil, Is the organization at its limit given the number of projects underway?

- `energy.supply.dim_asset`: `asset_id`, `asset_name`, `country_id`, `field_id`
- `energy.supply.dim_facility_type`: `facility_type_id`, `facility_type_code`, `facility_type_name`
- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.supply.dim_play`: `play_id`, `play_name`, `region_id`
- `energy.supply.dim_project`: `project_id`, `project_name`, `asset_id`, `field_id`
- `energy.supply.fact_basin_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `basin_id`, `hydrocarbon_id`, `play_id`, `basin_capacity_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (9) — Exxon Mobil

For Exxon Mobil, Where is the proppant improving recovery the most, including gassier zones?

- `energy.supply.dim_facility_type`: `facility_type_id`, `facility_type_code`, `facility_type_name`
- `energy.supply.dim_well_type`: `well_type_id`, `well_type_code`, `well_type_name`
- `energy.supply.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `country_id`, `facility_capacity_quantity`
- `energy.supply.fact_well_activity`: `fiscal_quarter_id`, `scenario_id`, `play_id`, `field_id`, `well_type_id`, `rig_type_id`, `well_quantity`, `rig_quantity`
- `energy.supply.dim_field`: `field_id`, `field_name`, `country_id`
- `energy.supply.dim_lng_terminal`: `lng_terminal_id`, `lng_terminal_name`, `country_id`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (7) — Exxon Mobil

For Exxon Mobil, What returns, certainty, and local conditions are required to move Papua New Guinea and Mozambique LNG forward?

- `energy.supply.dim_asset`: `asset_id`, `asset_name`, `country_id`, `field_id`
- `energy.supply.dim_lng_terminal`: `lng_terminal_id`, `lng_terminal_name`, `country_id`
- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.supply.dim_play`: `play_id`, `play_name`, `region_id`
- `energy.supply.dim_project`: `project_id`, `project_name`, `asset_id`, `field_id`
- `energy.supply.dim_well_type`: `well_type_id`, `well_type_code`, `well_type_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
