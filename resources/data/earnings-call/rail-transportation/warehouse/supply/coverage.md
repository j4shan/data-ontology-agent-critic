# Railroad Inc supply slice

This slice is part of the Railroad Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q1 2026 (2) — CSX

For CSX, When is double-stack through the Howard Street Tunnel and the Port of Baltimore fully launched, and how fast does volume load?

- `railroad.demand.fact_port_volume`: `fiscal_quarter_id`, `scenario_id`, `port_id`, `commodity_id`, `coal_grade_id`, `port_carload_quantity`, `port_ton_quantity`
- `railroad.demand.fact_project_volume`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `commodity_id`, `region_id`, `project_carload_quantity`, `ramp_carload_quantity`
- `railroad.supply.dim_infrastructure_project`: `infrastructure_project_id`, `infrastructure_project_name`, `region_id`, `asset_category_id`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_truck_market_volume`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `competitor_id`, `truck_load_quantity`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (4) — CSX

For CSX, How is the network being prepared for the storm relative to the last time weather set the railroad back?

- `railroad.supply.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `train_type_id`, `train_capacity_quantity`, `carload_capacity_quantity`
- `railroad.supply.fact_service_performance`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_dwell_hours`, `car_velocity_miles_per_day`, `trip_plan_compliance_percent`, `average_train_length_cars`
- `railroad.supply.fact_weather_disruption`: `fiscal_quarter_id`, `scenario_id`, `weather_event_type_id`, `division_id`, `disruption_duration_hours`, `delayed_train_quantity`
- `railroad.supply.dim_division`: `division_id`, `division_name`, `region_id`
- `railroad.supply.dim_infrastructure_project`: `infrastructure_project_id`, `infrastructure_project_name`, `region_id`, `asset_category_id`
- `railroad.supply.dim_weather_event_type`: `weather_event_type_id`, `weather_event_type_code`, `weather_event_type_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (5) — CSX

For CSX, What operating changes, under the new approach, get service back to the metrics of a few years ago?

- `railroad.supply.fact_service_performance`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_dwell_hours`, `car_velocity_miles_per_day`, `trip_plan_compliance_percent`, `average_train_length_cars`
- `railroad.supply.dim_division`: `division_id`, `division_name`, `region_id`
- `railroad.supply.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `train_type_id`, `train_capacity_quantity`, `carload_capacity_quantity`
- `railroad.supply.fact_terminal_capacity`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_capacity_quantity`, `terminal_processed_quantity`
- `railroad.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (1) — CSX

For CSX, From a shipper's perspective, what service benefits would a transcontinental railroad provide versus today's interline service?

- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.supply.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `train_type_id`, `train_capacity_quantity`, `carload_capacity_quantity`
- `railroad.supply.fact_service_performance`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_dwell_hours`, `car_velocity_miles_per_day`, `trip_plan_compliance_percent`, `average_train_length_cars`
- `railroad.supply.fact_terminal_capacity`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_capacity_quantity`, `terminal_processed_quantity`
- `railroad.demand.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (2) — CSX

For CSX, How much of the service recovery was weather versus operating changes, and how much further can it go?

- `railroad.supply.fact_service_performance`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_dwell_hours`, `car_velocity_miles_per_day`, `trip_plan_compliance_percent`, `average_train_length_cars`
- `railroad.supply.dim_division`: `division_id`, `division_name`, `region_id`
- `railroad.supply.dim_weather_event_type`: `weather_event_type_id`, `weather_event_type_code`, `weather_event_type_name`
- `railroad.supply.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `train_type_id`, `train_capacity_quantity`, `carload_capacity_quantity`
- `railroad.supply.fact_terminal_capacity`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_capacity_quantity`, `terminal_processed_quantity`
- `railroad.supply.fact_weather_disruption`: `fiscal_quarter_id`, `scenario_id`, `weather_event_type_id`, `division_id`, `disruption_duration_hours`, `delayed_train_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (3) — CSX

For CSX, Is the full-year volume improvement a return of outages or a real acceleration from the second-quarter level?

- `railroad.demand.fact_project_volume`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `commodity_id`, `region_id`, `project_carload_quantity`, `ramp_carload_quantity`
- `railroad.supply.fact_locomotive_efficiency`: `fiscal_quarter_id`, `scenario_id`, `locomotive_type_id`, `division_id`, `gross_ton_miles_per_gallon`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_contracted_volume`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `shipper_id`, `commodity_id`, `contracted_carload_quantity`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_interchange_volume`: `fiscal_quarter_id`, `scenario_id`, `interchange_id`, `service_type_id`, `competitor_id`, `interchanged_carload_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (6) — CSX

For CSX, Is ease of doing business the main gap between single-line service and interline service?

- `railroad.demand.fact_interchange_volume`: `fiscal_quarter_id`, `scenario_id`, `interchange_id`, `service_type_id`, `competitor_id`, `interchanged_carload_quantity`
- `railroad.supply.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `train_type_id`, `train_capacity_quantity`, `carload_capacity_quantity`
- `railroad.supply.fact_service_performance`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_dwell_hours`, `car_velocity_miles_per_day`, `trip_plan_compliance_percent`, `average_train_length_cars`
- `railroad.supply.fact_terminal_capacity`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_capacity_quantity`, `terminal_processed_quantity`
- `railroad.demand.dim_coast`: `coast_id`, `coast_code`, `coast_name`
- `railroad.demand.dim_interchange`: `interchange_id`, `interchange_name`, `metro_id`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (9) — CSX

For CSX, What trip-plan compliance is expected next quarter after the weak start and the later carload improvement?

- `railroad.supply.fact_service_performance`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_dwell_hours`, `car_velocity_miles_per_day`, `trip_plan_compliance_percent`, `average_train_length_cars`
- `railroad.supply.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `train_type_id`, `train_capacity_quantity`, `carload_capacity_quantity`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_interchange_volume`: `fiscal_quarter_id`, `scenario_id`, `interchange_id`, `service_type_id`, `competitor_id`, `interchanged_carload_quantity`
- `railroad.demand.fact_project_volume`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `commodity_id`, `region_id`, `project_carload_quantity`, `ramp_carload_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (4) — CSX

For CSX, How do headcount and cost trend from here, including compensation per employee?

- `railroad.price.fact_labor_expense`: `fiscal_quarter_id`, `scenario_id`, `workforce_group_id`, `cost_bucket_id`, `labor_expense_amount`, `compensation_per_employee`
- `railroad.supply.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `workforce_group_id`, `division_id`, `employee_quantity`, `trainee_quantity`
- `railroad.supply.fact_locomotive_efficiency`: `fiscal_quarter_id`, `scenario_id`, `locomotive_type_id`, `division_id`, `gross_ton_miles_per_gallon`
- `railroad.supply.fact_service_performance`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_dwell_hours`, `car_velocity_miles_per_day`, `trip_plan_compliance_percent`, `average_train_length_cars`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.fact_fuel`: `fiscal_quarter_id`, `scenario_id`, `fuel_type_id`, `service_type_id`, `fuel_gallon_quantity`, `fuel_expense_amount`, `fuel_price_per_gallon`, `fuel_surcharge_revenue_amount`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (10) — CSX

For CSX, How stable is export coal demand, and how should service be read against the erosion customers still see?

- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.dim_coal_grade`: `coal_grade_id`, `coal_grade_code`, `coal_grade_name`
- `railroad.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `railroad.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `railroad.demand.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_segment_id`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`

### Q3 2024 (13) — CSX

For CSX, Is the competitor's service disruption showing up as contract opportunity or risk?

- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_contracted_volume`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `shipper_id`, `commodity_id`, `contracted_carload_quantity`
- `railroad.demand.fact_interchange_volume`: `fiscal_quarter_id`, `scenario_id`, `interchange_id`, `service_type_id`, `competitor_id`, `interchanged_carload_quantity`
- `railroad.demand.fact_truck_market_volume`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `competitor_id`, `truck_load_quantity`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.fact_truck_rate`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `competitor_id`, `truck_spot_rate_per_load`, `truck_contract_rate_per_load`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (2) — Union Pacific

For Union Pacific, How much spare capacity does the network have, and what volume growth can it take without adding resources if end markets turn?

- `railroad.supply.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `train_type_id`, `train_capacity_quantity`, `carload_capacity_quantity`
- `railroad.supply.dim_division`: `division_id`, `division_name`, `region_id`
- `railroad.supply.dim_infrastructure_project`: `infrastructure_project_id`, `infrastructure_project_name`, `region_id`, `asset_category_id`
- `railroad.supply.fact_infrastructure_project_progress`: `fiscal_quarter_id`, `scenario_id`, `infrastructure_project_id`, `asset_category_id`, `project_completion_percent`, `capacity_added_carload_quantity`
- `railroad.supply.fact_locomotive_efficiency`: `fiscal_quarter_id`, `scenario_id`, `locomotive_type_id`, `division_id`, `gross_ton_miles_per_gallon`
- `railroad.supply.fact_terminal_capacity`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_capacity_quantity`, `terminal_processed_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (5) — Union Pacific

For Union Pacific, How important is volume growth, alongside current service, to showing the network can absorb a larger system?

- `railroad.supply.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `train_type_id`, `train_capacity_quantity`, `carload_capacity_quantity`
- `railroad.supply.fact_terminal_capacity`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_capacity_quantity`, `terminal_processed_quantity`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_interchange_volume`: `fiscal_quarter_id`, `scenario_id`, `interchange_id`, `service_type_id`, `competitor_id`, `interchanged_carload_quantity`
- `railroad.demand.fact_seasonal_volume`: `fiscal_quarter_id`, `scenario_id`, `peak_season_id`, `service_type_id`, `commodity_id`, `seasonal_carload_quantity`, `seasonal_revenue_ton_mile_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (6) — Union Pacific

For Union Pacific, Is record workforce productivity and the low headcount the new normal, or can it improve further while revenue grows?

- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.supply.dim_workforce_group`: `workforce_group_id`, `workforce_group_code`, `workforce_group_name`
- `railroad.supply.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `workforce_group_id`, `division_id`, `employee_quantity`, `trainee_quantity`
- `railroad.demand.fact_seasonal_volume`: `fiscal_quarter_id`, `scenario_id`, `peak_season_id`, `service_type_id`, `commodity_id`, `seasonal_carload_quantity`, `seasonal_revenue_ton_mile_quantity`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.supply.dim_productivity_initiative`: `productivity_initiative_id`, `productivity_initiative_name`, `division_id`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (9) — Union Pacific

For Union Pacific, Does network performance support a stronger pricing conversation?

- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.supply.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `train_type_id`, `train_capacity_quantity`, `carload_capacity_quantity`
- `railroad.supply.fact_service_performance`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_dwell_hours`, `car_velocity_miles_per_day`, `trip_plan_compliance_percent`, `average_train_length_cars`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.price.dim_price_program`: `price_program_id`, `price_program_code`, `price_program_name`
- `railroad.price.fact_accessorial_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `price_program_id`, `accessorial_revenue_amount`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (6) — Union Pacific

For Union Pacific, Is the intermodal change versus the other western railroad a share shift, looking at originated volume?

- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_interchange_volume`: `fiscal_quarter_id`, `scenario_id`, `interchange_id`, `service_type_id`, `competitor_id`, `interchanged_carload_quantity`
- `railroad.demand.fact_truck_market_volume`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `competitor_id`, `truck_load_quantity`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.supply.fact_locomotive_efficiency`: `fiscal_quarter_id`, `scenario_id`, `locomotive_type_id`, `division_id`, `gross_ton_miles_per_gallon`
- `railroad.demand.dim_commercial_channel`: `commercial_channel_id`, `commercial_channel_code`, `commercial_channel_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (7) — Union Pacific

For Union Pacific, How confident is the transfer of current service practices to a combined network, and how long would that take?

- `railroad.supply.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `train_type_id`, `train_capacity_quantity`, `carload_capacity_quantity`
- `railroad.supply.dim_division`: `division_id`, `division_name`, `region_id`
- `railroad.supply.dim_infrastructure_project`: `infrastructure_project_id`, `infrastructure_project_name`, `region_id`, `asset_category_id`
- `railroad.supply.fact_service_performance`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_dwell_hours`, `car_velocity_miles_per_day`, `trip_plan_compliance_percent`, `average_train_length_cars`
- `railroad.supply.fact_terminal_capacity`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_capacity_quantity`, `terminal_processed_quantity`
- `railroad.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (9) — Union Pacific

For Union Pacific, Is pricing in the coming contracting season better than this year, and does the service product support that?

- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.dim_price_program`: `price_program_id`, `price_program_code`, `price_program_name`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_contracted_volume`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `shipper_id`, `commodity_id`, `contracted_carload_quantity`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_seasonal_volume`: `fiscal_quarter_id`, `scenario_id`, `peak_season_id`, `service_type_id`, `commodity_id`, `seasonal_carload_quantity`, `seasonal_revenue_ton_mile_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (1) — Union Pacific

For Union Pacific, What cost puts and takes show up from the second quarter into the third, with the network running as well as it has?

- `railroad.supply.dim_division`: `division_id`, `division_name`, `region_id`
- `railroad.supply.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `train_type_id`, `train_capacity_quantity`, `carload_capacity_quantity`
- `railroad.supply.fact_service_performance`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_dwell_hours`, `car_velocity_miles_per_day`, `trip_plan_compliance_percent`, `average_train_length_cars`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (2) — Union Pacific

For Union Pacific, After the locomotive-refresh agreement ends, what is the condition of the fleet and is more refresh needed?

- `railroad.supply.dim_locomotive_type`: `locomotive_type_id`, `locomotive_type_code`, `locomotive_type_name`
- `railroad.supply.dim_asset_category`: `asset_category_id`, `asset_category_code`, `asset_category_name`
- `railroad.supply.dim_maintenance_type`: `maintenance_type_id`, `maintenance_type_code`, `maintenance_type_name`
- `railroad.supply.fact_locomotive_efficiency`: `fiscal_quarter_id`, `scenario_id`, `locomotive_type_id`, `division_id`, `gross_ton_miles_per_gallon`
- `railroad.supply.fact_locomotive_resource`: `fiscal_quarter_id`, `scenario_id`, `locomotive_type_id`, `division_id`, `locomotive_unit_quantity`, `available_locomotive_quantity`
- `railroad.supply.fact_maintenance_activity`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `asset_category_id`, `division_id`, `maintenance_unit_quantity`, `inspected_unit_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (4) — Union Pacific

For Union Pacific, Is there progress toward smaller crews or more automation under the current regulatory backdrop?

- `railroad.supply.dim_crew_district`: `crew_district_id`, `crew_district_name`, `division_id`
- `railroad.supply.fact_crew_resource`: `fiscal_quarter_id`, `scenario_id`, `crew_district_id`, `workforce_group_id`, `crew_quantity`, `crew_employee_quantity`
- `railroad.supply.dim_division`: `division_id`, `division_name`, `region_id`
- `railroad.supply.fact_infrastructure_project_progress`: `fiscal_quarter_id`, `scenario_id`, `infrastructure_project_id`, `asset_category_id`, `project_completion_percent`, `capacity_added_carload_quantity`
- `railroad.supply.fact_service_performance`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_dwell_hours`, `car_velocity_miles_per_day`, `trip_plan_compliance_percent`, `average_train_length_cars`
- `railroad.demand.fact_contracted_volume`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `shipper_id`, `commodity_id`, `contracted_carload_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (7) — Union Pacific

For Union Pacific, Are intermodal marketing companies or the railroad's own transload services the better path to more domestic intermodal, including the new seven-day product?

- `railroad.demand.dim_commercial_channel`: `commercial_channel_id`, `commercial_channel_code`, `commercial_channel_name`
- `railroad.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.supply.dim_train_type`: `train_type_id`, `train_type_code`, `train_type_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (8) — Union Pacific

For Union Pacific, Where does Chicago interchange still constrain shippers?

- `railroad.supply.fact_service_performance`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_dwell_hours`, `car_velocity_miles_per_day`, `trip_plan_compliance_percent`, `average_train_length_cars`
- `railroad.demand.dim_interchange`: `interchange_id`, `interchange_name`, `metro_id`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_interchange_volume`: `fiscal_quarter_id`, `scenario_id`, `interchange_id`, `service_type_id`, `competitor_id`, `interchanged_carload_quantity`
- `railroad.supply.dim_crew_district`: `crew_district_id`, `crew_district_name`, `division_id`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (9) — Union Pacific

For Union Pacific, How much U.S.-bound traffic through Canadian ports could be repatriated, and is port capacity the bottleneck?

- `railroad.demand.fact_port_volume`: `fiscal_quarter_id`, `scenario_id`, `port_id`, `commodity_id`, `coal_grade_id`, `port_carload_quantity`, `port_ton_quantity`
- `railroad.supply.fact_infrastructure_project_progress`: `fiscal_quarter_id`, `scenario_id`, `infrastructure_project_id`, `asset_category_id`, `project_completion_percent`, `capacity_added_carload_quantity`
- `railroad.supply.fact_locomotive_efficiency`: `fiscal_quarter_id`, `scenario_id`, `locomotive_type_id`, `division_id`, `gross_ton_miles_per_gallon`
- `railroad.supply.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `train_type_id`, `train_capacity_quantity`, `carload_capacity_quantity`
- `railroad.supply.fact_terminal_capacity`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_capacity_quantity`, `terminal_processed_quantity`
- `railroad.demand.dim_coast`: `coast_id`, `coast_code`, `coast_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (11) — Union Pacific

For Union Pacific, What structural limits of the network still keep freight on the highway despite strong service?

- `railroad.demand.fact_truck_market_volume`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `competitor_id`, `truck_load_quantity`
- `railroad.supply.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `train_type_id`, `train_capacity_quantity`, `carload_capacity_quantity`
- `railroad.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (12) — Union Pacific

For Union Pacific, How much of the interest in a transcontinental service is coming from shippers who want trucks off the road?

- `railroad.demand.fact_truck_market_volume`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `competitor_id`, `truck_load_quantity`
- `railroad.supply.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `train_type_id`, `train_capacity_quantity`, `carload_capacity_quantity`
- `railroad.supply.fact_service_performance`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_dwell_hours`, `car_velocity_miles_per_day`, `trip_plan_compliance_percent`, `average_train_length_cars`
- `railroad.supply.fact_terminal_capacity`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_capacity_quantity`, `terminal_processed_quantity`
- `railroad.demand.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `railroad.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
