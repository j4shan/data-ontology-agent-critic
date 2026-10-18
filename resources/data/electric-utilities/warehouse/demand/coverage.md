# Utility Inc demand slice

This slice is part of the Utility Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q2 2026 (2) — Duke Energy

For Duke Energy, Given affordability pressure in Indiana, would a generation-company structure be used to serve large load?

- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.dim_service_territory`: `service_territory_id`, `service_territory_name`, `operating_company_id`, `state_id`
- `utility.demand.dim_weather_zone`: `weather_zone_id`, `weather_zone_name`, `state_id`
- `utility.demand.fact_gas_throughput`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `gas_throughput_quantity`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (4) — Duke Energy

For Duke Energy, What bottlenecks are appearing while 5 gigawatts are already under construction, and what should be watched on the next gas build?

- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.supply.fact_generation_fuel_consumption`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `fuel_type_id`, `generation_fuel_quantity`
- `utility.demand.fact_gas_throughput`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `gas_throughput_quantity`
- `utility.supply.dim_fuel_type`: `fuel_type_id`, `fuel_type_code`, `fuel_type_name`
- `utility.supply.dim_generation_unit`: `generation_unit_id`, `generation_unit_name`, `generating_station_id`
- `utility.supply.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (5) — Duke Energy

For Duke Energy, How does the new-nuclear effort come together beyond the near-term application work?

- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `utility.demand.dim_county`: `county_id`, `county_name`, `state_id`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (6) — Duke Energy

For Duke Energy, How many gigawatts of the high-confidence load pipeline sit in Indiana and Florida versus the Carolinas?

- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.supply.fact_substation_capacity`: `fiscal_quarter_id`, `scenario_id`, `substation_id`, `operating_company_id`, `substation_capacity_quantity`, `substation_peak_load_quantity`
- `utility.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `utility.demand.dim_county`: `county_id`, `county_name`, `state_id`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (9) — Duke Energy

For Duke Energy, Is the nuclear preference large-scale reactors or small modular reactors, and is the company in a long-lead procurement?

- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.supply.dim_generating_station`: `generating_station_id`, `generating_station_name`, `technology_id`, `operating_company_id`, `state_id`
- `utility.supply.fact_interconnection_queue`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `queued_capacity_quantity`, `interconnection_request_quantity`
- `utility.supply.fact_planned_capacity`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `planned_capacity_quantity`
- `utility.supply.fact_renewable_generation`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `renewable_generation_quantity`
- `utility.supply.fact_storage_capacity`: `fiscal_quarter_id`, `scenario_id`, `storage_type_id`, `operating_company_id`, `technology_id`, `storage_power_capacity_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (2) — Duke Energy

For Duke Energy, Where does the South Carolina large-load tariff docket stand, and could it catalyze more load?

- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.supply.fact_substation_capacity`: `fiscal_quarter_id`, `scenario_id`, `substation_id`, `operating_company_id`, `substation_capacity_quantity`, `substation_peak_load_quantity`
- `utility.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `utility.demand.dim_county`: `county_id`, `county_name`, `state_id`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (5) — Duke Energy

For Duke Energy, How could the energy-services agreement pipeline beyond the signed set expand the capital plan over time?

- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.fact_electricity_sales_energy`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `end_use_id`, `operating_company_id`, `jurisdiction_id`, `electricity_sales_quantity`
- `utility.demand.fact_monthly_electricity_sales`: `fiscal_quarter_id`, `scenario_id`, `calendar_month_id`, `rate_class_id`, `operating_company_id`, `monthly_electricity_sales_quantity`
- `utility.price.fact_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `distribution_capital_amount`
- `utility.price.fact_gas_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `gas_distribution_capital_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (10) — Duke Energy

For Duke Energy, When do the energy-services projects not yet under construction start, and do local moratoriums threaten them?

- `utility.demand.fact_gas_throughput`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `gas_throughput_quantity`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.supply.fact_renewable_generation`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `renewable_generation_quantity`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.dim_rate_class`: `rate_class_id`, `rate_class_code`, `rate_class_name`
- `utility.demand.fact_electricity_sales_energy`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `end_use_id`, `operating_company_id`, `jurisdiction_id`, `electricity_sales_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (9) — Duke Energy

For Duke Energy, Is flexible interconnection being used to speed data-center connections, and would customers accept it?

- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.fact_county_customer_count`: `fiscal_quarter_id`, `scenario_id`, `county_id`, `rate_class_id`, `operating_company_id`, `county_customer_quantity`
- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.demand.fact_gas_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `gas_customer_quantity`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.dim_meter_type`: `meter_type_id`, `meter_type_code`, `meter_type_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (7) — Southern Company

For Southern Company, Did generation RFPs through 2032 already include the latest load-pipeline progress, and is there room for further upside if more of the pipeline converts?

- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.fact_gas_throughput`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `gas_throughput_quantity`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.price.fact_generation_capital`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `technology_id`, `generation_capital_amount`
- `utility.supply.dim_generation_unit`: `generation_unit_id`, `generation_unit_name`, `generating_station_id`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (8) — Southern Company

For Southern Company, Does every incremental large load in Alabama require incremental generation, given signed contracts and an oversubscribed request?

- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.supply.fact_interconnection_queue`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `queued_capacity_quantity`, `interconnection_request_quantity`
- `utility.demand.fact_gas_throughput`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `gas_throughput_quantity`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.price.fact_generation_capital`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `technology_id`, `generation_capital_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (9) — Southern Company

For Southern Company, How is the OpenAI demand-response commitment being factored into the broader project pipeline?

- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `utility.demand.dim_county`: `county_id`, `county_name`, `state_id`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (10) — Southern Company

For Southern Company, How do Georgia tariffs handle credit risk for data-center customers that are not strongly investment grade?

- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.fact_county_customer_count`: `fiscal_quarter_id`, `scenario_id`, `county_id`, `rate_class_id`, `operating_company_id`, `county_customer_quantity`
- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.demand.fact_gas_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `gas_customer_quantity`
- `utility.demand.fact_gas_throughput`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `gas_throughput_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (14) — Southern Company

For Southern Company, How are Southern Power upgrade and brownfield conversations trending with current and new counterparties?

- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.price.fact_fuel_purchased_power_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `fuel_type_id`, `fuel_expense_amount`, `purchased_power_expense_amount`
- `utility.price.fact_purchased_power_rate`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `purchased_power_rate_amount`
- `utility.supply.fact_storage_capacity`: `fiscal_quarter_id`, `scenario_id`, `storage_type_id`, `operating_company_id`, `technology_id`, `storage_power_capacity_quantity`
- `utility.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`

### Q1 2026 (2) — Southern Company

For Southern Company, Have renegotiations started on Southern Power tolls that are rolling off, including with hyperscalers?

- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.price.fact_fuel_purchased_power_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `fuel_type_id`, `fuel_expense_amount`, `purchased_power_expense_amount`
- `utility.price.fact_purchased_power_rate`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `purchased_power_rate_amount`
- `utility.supply.fact_storage_capacity`: `fiscal_quarter_id`, `scenario_id`, `storage_type_id`, `operating_company_id`, `technology_id`, `storage_power_capacity_quantity`
- `utility.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `utility.demand.dim_county`: `county_id`, `county_name`, `state_id`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (3) — Southern Company

For Southern Company, Is large-load visibility ahead of the plan that supported the regulatory stay-outs?

- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.dim_jurisdiction`: `jurisdiction_id`, `jurisdiction_name`
- `utility.price.fact_rate_base`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `jurisdiction_id`, `rate_base_amount`, `authorized_return_percent`, `earned_return_percent`
- `utility.supply.fact_substation_capacity`: `fiscal_quarter_id`, `scenario_id`, `substation_id`, `operating_company_id`, `substation_capacity_quantity`, `substation_peak_load_quantity`
- `utility.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (4) — Southern Company

For Southern Company, Could cumulative bill credits be revised higher as contracted large load rises?

- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.supply.fact_substation_capacity`: `fiscal_quarter_id`, `scenario_id`, `substation_id`, `operating_company_id`, `substation_capacity_quantity`, `substation_peak_load_quantity`
- `utility.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `utility.demand.dim_county`: `county_id`, `county_name`, `state_id`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (5) — Southern Company

For Southern Company, Why does the Georgia large-load report look softer while other states, including Alabama, keep finalizing contracts?

- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.dim_county`: `county_id`, `county_name`, `state_id`
- `utility.demand.dim_jurisdiction`: `jurisdiction_id`, `jurisdiction_name`
- `utility.demand.dim_service_territory`: `service_territory_id`, `service_territory_name`, `operating_company_id`, `state_id`
- `utility.demand.dim_state`: `state_id`, `state_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (6) — Southern Company

For Southern Company, What is the timing and remaining size of gas-fleet upgrades at Southern Power?

- `utility.supply.fact_storage_capacity`: `fiscal_quarter_id`, `scenario_id`, `storage_type_id`, `operating_company_id`, `technology_id`, `storage_power_capacity_quantity`
- `utility.supply.fact_transmission_system`: `fiscal_quarter_id`, `scenario_id`, `transmission_asset_id`, `operating_company_id`, `transfer_capacity_quantity`, `circuit_mile_quantity`
- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_electricity_sales_energy`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `end_use_id`, `operating_company_id`, `jurisdiction_id`, `electricity_sales_quantity`
- `utility.demand.fact_gas_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `gas_customer_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (8) — Southern Company

For Southern Company, Where do turbine and labor supply stand, and when is the next all-source request needed as more large-load contracts are signed?

- `utility.supply.fact_interconnection_queue`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `queued_capacity_quantity`, `interconnection_request_quantity`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.supply.dim_generation_unit`: `generation_unit_id`, `generation_unit_name`, `generating_station_id`
- `utility.supply.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (4) — Southern Company

For Southern Company, What is the timing of Southeast gas supply and the pipeline expansion needed to serve it?

- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.supply.dim_fuel_type`: `fuel_type_id`, `fuel_type_code`, `fuel_type_name`
- `utility.supply.fact_generation_fuel_consumption`: `fiscal_quarter_id`, `scenario_id`, `generating_station_id`, `fuel_type_id`, `generation_fuel_quantity`
- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_gas_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `gas_customer_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (6) — Southern Company

For Southern Company, Is there still room to add more large load by 2029, and which years would the next requests for generation cover?

- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.supply.fact_interconnection_queue`: `fiscal_quarter_id`, `scenario_id`, `technology_id`, `operating_company_id`, `queued_capacity_quantity`, `interconnection_request_quantity`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.fact_gas_throughput`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `gas_throughput_quantity`
- `utility.price.fact_gas_supply_expense`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `cost_category_id`, `gas_supply_expense_amount`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (8) — Southern Company

For Southern Company, What is the difference between contracted and committed large load, and how many gigawatts are in advanced negotiation?

- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.supply.fact_substation_capacity`: `fiscal_quarter_id`, `scenario_id`, `substation_id`, `operating_company_id`, `substation_capacity_quantity`, `substation_peak_load_quantity`
- `utility.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `utility.demand.dim_county`: `county_id`, `county_name`, `state_id`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (5) — Southern Company

For Southern Company, Where do new-nuclear discussions stand after the resource plan's upgrade cases?

- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `utility.demand.fact_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `customer_segment_id`, `customer_quantity`, `new_customer_quantity`
- `utility.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `utility.demand.dim_county`: `county_id`, `county_name`, `state_id`
- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`

### Q2 2025 (6) — Southern Company

For Southern Company, Is the large-load update expected to come in above the prior pipeline figure?

- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.supply.fact_substation_capacity`: `fiscal_quarter_id`, `scenario_id`, `substation_id`, `operating_company_id`, `substation_capacity_quantity`, `substation_peak_load_quantity`
- `utility.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `utility.demand.dim_county`: `county_id`, `county_name`, `state_id`
- `utility.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (9) — Southern Company

For Southern Company, What gating items remain on a FERC gas-pipeline expansion?

- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.fact_gas_customer_count`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `gas_customer_quantity`
- `utility.demand.fact_gas_throughput`: `fiscal_quarter_id`, `scenario_id`, `rate_class_id`, `operating_company_id`, `jurisdiction_id`, `gas_throughput_quantity`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.price.fact_gas_distribution_capital`: `fiscal_quarter_id`, `scenario_id`, `operating_company_id`, `asset_category_id`, `gas_distribution_capital_amount`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (11) — Southern Company

For Southern Company, Why are fewer data-center announcements being made jointly with the company in Georgia and Mississippi than at some other utilities?

- `utility.demand.dim_end_use`: `end_use_id`, `end_use_code`, `end_use_name`
- `utility.demand.fact_large_load_pipeline`: `fiscal_quarter_id`, `scenario_id`, `pipeline_stage_id`, `end_use_id`, `operating_company_id`, `service_territory_id`, `pipeline_load_quantity`, `contracted_load_quantity`
- `utility.supply.fact_substation_capacity`: `fiscal_quarter_id`, `scenario_id`, `substation_id`, `operating_company_id`, `substation_capacity_quantity`, `substation_peak_load_quantity`
- `utility.demand.dim_operating_company`: `operating_company_id`, `operating_company_code`, `operating_company_name`
- `utility.demand.dim_pipeline_stage`: `pipeline_stage_id`, `pipeline_stage_code`, `pipeline_stage_name`
- `utility.demand.dim_service_territory`: `service_territory_id`, `service_territory_name`, `operating_company_id`, `state_id`
- `utility.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `utility.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
