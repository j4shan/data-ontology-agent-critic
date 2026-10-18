# Utility Inc supply slice

This slice is part of the Utility Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q2 2026 (7) — Duke Energy

For Duke Energy, Is gas supply being secured for the next plants alongside the additional turbines, and could fuel supply constrain the build?

- `utility.supply.fact_generation_fuel_consumption`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `fuel_type_id`, `generation_fuel_quantity`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.supply.dim_fuel_type`: `fuel_type_id`, `fuel_type_code`, `fuel_type_name`
- `utility.supply.dim_generation_unit`: `generation_unit_id`, `generation_unit_name`, `generating_station_id`
- `utility.supply.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.supply.fact_generation_output`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `generation_output_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (8) — Duke Energy

For Duke Energy, Where does a possible sale of the Cayuga coal plant stand relative to Indiana's goals?

- `utility.supply.dim_generating_station`: `generating_station_id`, `generating_station_name`, `technology_id`, `operating_company_id`, `state_id`
- `utility.supply.dim_generation_unit`: `generation_unit_id`, `generation_unit_name`, `generating_station_id`
- `utility.supply.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.supply.fact_generation_fuel_consumption`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `fuel_type_id`, `generation_fuel_quantity`
- `utility.supply.fact_generation_output`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `generation_output_quantity`
- `utility.supply.fact_generation_unit_capacity`: `fiscal_quarter_id`, `scenario_id`, `generation_unit_id`, `generating_station_id`, `unit_capacity_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (3) — Duke Energy

For Duke Energy, Are there further tax-credit monetizations that could fund customer bill benefits?

- `utility.supply.fact_capacity_factor`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `capacity_factor_percent`, `availability_percent`, `outage_duration_hours`
- `utility.supply.fact_generating_capacity`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `nameplate_capacity_quantity`, `available_capacity_quantity`
- `utility.supply.fact_generation_unit_capacity`: `fiscal_quarter_id`, `scenario_id`, `generation_unit_id`, `generating_station_id`, `unit_capacity_quantity`
- `utility.supply.fact_interconnection_queue`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `queued_capacity_quantity`, `interconnection_request_quantity`
- `utility.supply.fact_planned_capacity`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `planned_capacity_quantity`
- `utility.supply.fact_reliability_performance`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `service_territory_id`, `outage_duration_minutes`, `outage_quantity`, `customer_interruption_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (6) — Duke Energy

For Duke Energy, What still has to be cleared before firm construction contracts can be signed for the gas plants in the plan?

- `utility.supply.fact_generation_fuel_consumption`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `fuel_type_id`, `generation_fuel_quantity`
- `utility.demand.fact_gas_throughput`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `gas_throughput_quantity`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.supply.dim_fuel_type`: `fuel_type_id`, `fuel_type_code`, `fuel_type_name`
- `utility.supply.dim_generation_unit`: `generation_unit_id`, `generation_unit_name`, `generating_station_id`
- `utility.supply.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (3) — Duke Energy

For Duke Energy, If more natural-gas pipeline capacity reaches the Southeast, would the Carolinas resource plan shift further toward gas?

- `utility.supply.dim_fuel_type`: `fuel_type_id`, `fuel_type_code`, `fuel_type_name`
- `utility.supply.fact_capacity_factor`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `capacity_factor_percent`, `availability_percent`, `outage_duration_hours`
- `utility.supply.fact_generating_capacity`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `nameplate_capacity_quantity`, `available_capacity_quantity`
- `utility.supply.fact_generation_fuel_consumption`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `fuel_type_id`, `generation_fuel_quantity`
- `utility.supply.fact_generation_unit_capacity`: `fiscal_quarter_id`, `scenario_id`, `generation_unit_id`, `generating_station_id`, `unit_capacity_quantity`
- `utility.supply.fact_interconnection_queue`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `queued_capacity_quantity`, `interconnection_request_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (2) — Southern Company

For Southern Company, Are the 3 gigawatts still being finalized inside the 2030 window, and what milestones remain?

- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.supply.fact_substation_capacity`: `fiscal_quarter_id`, `scenario_id`, `substation_id`, `operating_company_id`, `substation_capacity_quantity`, `substation_peak_load_quantity`
- `utility.supply.dim_fuel_type`: `fuel_type_id`, `fuel_type_code`, `fuel_type_name`
- `utility.supply.dim_generation_unit`: `generation_unit_id`, `generation_unit_name`, `generating_station_id`
- `utility.supply.fact_capacity_factor`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `capacity_factor_percent`, `availability_percent`, `outage_duration_hours`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (3) — Southern Company

For Southern Company, As Southern Power tolling agreements roll off, can that capacity be repurposed for hyperscalers, and does it sit inside the existing pipeline?

- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.supply.fact_storage_capacity`: `fiscal_quarter_id`, `scenario_id`, `storage_type_id`, `operating_company_id`, `technology_id`, `storage_power_capacity_quantity`
- `utility.supply.fact_substation_capacity`: `fiscal_quarter_id`, `scenario_id`, `substation_id`, `operating_company_id`, `substation_capacity_quantity`, `substation_peak_load_quantity`
- `utility.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `utility.demand.fact_electricity_sales_energy`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `end_use_id`, `operating_company_id`, `jurisdiction_id`, `electricity_sales_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (4) — Southern Company

For Southern Company, Would those hyperscaler deals be long-term energy and capacity contracts rather than standard tolls?

- `utility.supply.fact_storage_capacity`: `fiscal_quarter_id`, `scenario_id`, `storage_type_id`, `operating_company_id`, `technology_id`, `storage_power_capacity_quantity`
- `utility.demand.fact_electricity_sales_energy`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `end_use_id`, `operating_company_id`, `jurisdiction_id`, `electricity_sales_quantity`
- `utility.supply.dim_storage_type`: `storage_type_id`, `storage_type_code`, `storage_type_name`
- `utility.supply.fact_capacity_factor`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `capacity_factor_percent`, `availability_percent`, `outage_duration_hours`
- `utility.supply.fact_generating_capacity`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `nameplate_capacity_quantity`, `available_capacity_quantity`
- `utility.supply.fact_generation_output`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `generation_output_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (6) — Southern Company

For Southern Company, What is new on FERC pipeline investment timing as incremental requests could point to more gas plants?

- `utility.supply.fact_generation_fuel_consumption`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `fuel_type_id`, `generation_fuel_quantity`
- `utility.supply.fact_interconnection_queue`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `queued_capacity_quantity`, `interconnection_request_quantity`
- `utility.demand.fact_gas_throughput`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `gas_throughput_quantity`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.supply.dim_fuel_type`: `fuel_type_id`, `fuel_type_code`, `fuel_type_name`
- `utility.supply.dim_generation_unit`: `generation_unit_id`, `generation_unit_name`, `generating_station_id`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (7) — Southern Company

For Southern Company, When does the Georgia all-source process give visibility into company-owned resources and capital, and could some capacity be needed before 2032?

- `utility.supply.fact_interconnection_queue`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `queued_capacity_quantity`, `interconnection_request_quantity`
- `utility.supply.fact_storage_capacity`: `fiscal_quarter_id`, `scenario_id`, `storage_type_id`, `operating_company_id`, `technology_id`, `storage_power_capacity_quantity`
- `utility.demand.dim_service_territory`: `service_territory_id`, `service_territory_name`, `operating_company_id`, `state_id`
- `utility.demand.fact_electricity_sales_energy`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `end_use_id`, `operating_company_id`, `jurisdiction_id`, `electricity_sales_quantity`
- `utility.demand.fact_gas_throughput`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `gas_throughput_quantity`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (9) — Southern Company

For Southern Company, How much Southern Power capacity is contracted today, including the upgrade megawatts?

- `utility.supply.fact_storage_capacity`: `fiscal_quarter_id`, `scenario_id`, `storage_type_id`, `operating_company_id`, `technology_id`, `storage_power_capacity_quantity`
- `utility.supply.fact_generating_capacity`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `nameplate_capacity_quantity`, `available_capacity_quantity`
- `utility.supply.fact_generation_unit_capacity`: `fiscal_quarter_id`, `scenario_id`, `generation_unit_id`, `generating_station_id`, `unit_capacity_quantity`
- `utility.supply.fact_interconnection_queue`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `queued_capacity_quantity`, `interconnection_request_quantity`
- `utility.supply.fact_planned_capacity`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `planned_capacity_quantity`
- `utility.supply.fact_substation_capacity`: `fiscal_quarter_id`, `scenario_id`, `substation_id`, `operating_company_id`, `substation_capacity_quantity`, `substation_peak_load_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (5) — Southern Company

For Southern Company, How much of the later-decade large-load figure is the same projects ramping versus new projects?

- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.supply.fact_substation_capacity`: `fiscal_quarter_id`, `scenario_id`, `substation_id`, `operating_company_id`, `substation_capacity_quantity`, `substation_peak_load_quantity`
- `utility.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`

### Q3 2025 (7) — Southern Company

For Southern Company, Are customers now willing to pay fully loaded economics for contract-based gas plants at Southern Power?

- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.demand.fact_gas_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `gas_customer_quantity`
- `utility.demand.fact_gas_throughput`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `gas_throughput_quantity`
- `utility.supply.dim_fuel_type`: `fuel_type_id`, `fuel_type_code`, `fuel_type_name`
- `utility.supply.dim_generating_station`: `generating_station_id`, `generating_station_name`, `technology_id`, `operating_company_id`, `state_id`
- `utility.supply.fact_generation_fuel_consumption`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `fuel_type_id`, `generation_fuel_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (2) — Southern Company

For Southern Company, Where do turbine procurement and gas supply stand for combined-cycle units aimed at 2029 and 2030?

- `utility.supply.fact_generation_fuel_consumption`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `fuel_type_id`, `generation_fuel_quantity`
- `utility.supply.dim_fuel_type`: `fuel_type_id`, `fuel_type_code`, `fuel_type_name`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.supply.dim_generation_unit`: `generation_unit_id`, `generation_unit_name`, `generating_station_id`
- `utility.supply.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.supply.fact_distribution_system`: `fiscal_quarter_id`, `scenario_id`, `distribution_asset_id`, `operating_company_id`, `distribution_circuit_mile_quantity`, `distribution_asset_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (7) — Southern Company

For Southern Company, How confident is delivery of purchased combined-cycle capacity as early as 2028 given equipment and construction timing?

- `utility.supply.dim_fuel_type`: `fuel_type_id`, `fuel_type_code`, `fuel_type_name`
- `utility.supply.fact_capacity_factor`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `capacity_factor_percent`, `availability_percent`, `outage_duration_hours`
- `utility.supply.fact_generating_capacity`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `nameplate_capacity_quantity`, `available_capacity_quantity`
- `utility.supply.fact_generation_unit_capacity`: `fiscal_quarter_id`, `scenario_id`, `generation_unit_id`, `generating_station_id`, `unit_capacity_quantity`
- `utility.supply.fact_interconnection_queue`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `queued_capacity_quantity`, `interconnection_request_quantity`
- `utility.supply.fact_planned_capacity`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `planned_capacity_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
