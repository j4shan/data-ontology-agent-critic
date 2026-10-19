# Railroad Inc demand slice

This slice is part of the Railroad Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q1 2026 (7) — CSX

For CSX, When do the projects already cited reach full carload ramp, and do the remaining projects for the year have a similar impact?

- `railroad.demand.fact_project_volume`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `commodity_id`, `region_id`, `project_carload_quantity`, `ramp_carload_quantity`
- `railroad.demand.dim_project`: `project_id`, `project_name`, `region_id`, `commodity_id`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_contracted_volume`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `shipper_id`, `commodity_id`, `contracted_carload_quantity`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_interchange_volume`: `fiscal_quarter_id`, `scenario_id`, `interchange_id`, `service_type_id`, `competitor_id`, `interchanged_carload_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (7) — CSX

For CSX, While the industry combination is under review, what commercial opportunities can be taken in the near term?

- `railroad.demand.dim_commercial_channel`: `commercial_channel_id`, `commercial_channel_code`, `commercial_channel_name`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.demand.dim_intermodal_trade`: `intermodal_trade_id`, `intermodal_trade_code`, `intermodal_trade_name`
- `railroad.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (11) — CSX

For CSX, How large is the double-stack opportunity, and how fast does it ramp after bids for the second quarter?

- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.dim_commercial_channel`: `commercial_channel_id`, `commercial_channel_code`, `commercial_channel_name`
- `railroad.demand.dim_intermodal_trade`: `intermodal_trade_id`, `intermodal_trade_code`, `intermodal_trade_name`
- `railroad.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_project_volume`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `commodity_id`, `region_id`, `project_carload_quantity`, `ramp_carload_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (10) — CSX

For CSX, Where does second-half volume have to come from, including peak season, to get the full year back to growth?

- `railroad.demand.fact_seasonal_volume`: `fiscal_quarter_id`, `scenario_id`, `peak_season_id`, `service_type_id`, `commodity_id`, `seasonal_carload_quantity`, `seasonal_revenue_ton_mile_quantity`
- `railroad.demand.dim_peak_season`: `peak_season_id`, `peak_season_code`, `peak_season_name`, `fiscal_quarter_id`
- `railroad.demand.dim_interchange`: `interchange_id`, `interchange_name`, `metro_id`
- `railroad.demand.dim_metro`: `metro_id`, `metro_code`, `metro_name`, `state_id`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_contracted_volume`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `shipper_id`, `commodity_id`, `contracted_carload_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (5) — CSX

For CSX, How sensitive are the multi-year industrial projects to the economic cycle?

- `railroad.demand.fact_project_volume`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `commodity_id`, `region_id`, `project_carload_quantity`, `ramp_carload_quantity`
- `railroad.demand.dim_project`: `project_id`, `project_name`, `region_id`, `commodity_id`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_contracted_volume`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `shipper_id`, `commodity_id`, `contracted_carload_quantity`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_interchange_volume`: `fiscal_quarter_id`, `scenario_id`, `interchange_id`, `service_type_id`, `competitor_id`, `interchanged_carload_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (9) — CSX

For CSX, How much volume was diverted ahead of the East Coast labor risk, and is it returning?

- `railroad.demand.dim_coast`: `coast_id`, `coast_code`, `coast_name`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.demand.dim_commercial_channel`: `commercial_channel_id`, `commercial_channel_code`, `commercial_channel_name`
- `railroad.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (3) — Union Pacific

For Union Pacific, How much carload growth is the business-development pipeline expected to add?

- `railroad.demand.fact_project_volume`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `commodity_id`, `region_id`, `project_carload_quantity`, `ramp_carload_quantity`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_contracted_volume`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `shipper_id`, `commodity_id`, `contracted_carload_quantity`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_interchange_volume`: `fiscal_quarter_id`, `scenario_id`, `interchange_id`, `service_type_id`, `competitor_id`, `interchanged_carload_quantity`
- `railroad.demand.fact_port_volume`: `fiscal_quarter_id`, `scenario_id`, `port_id`, `commodity_id`, `coal_grade_id`, `port_carload_quantity`, `port_ton_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (4) — Union Pacific

For Union Pacific, What customer feedback has committed gateway pricing produced?

- `railroad.demand.dim_metro`: `metro_id`, `metro_code`, `metro_name`, `state_id`
- `railroad.demand.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_segment_id`
- `railroad.price.dim_price_program`: `price_program_id`, `price_program_code`, `price_program_name`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `railroad.demand.dim_coal_grade`: `coal_grade_id`, `coal_grade_code`, `coal_grade_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (7) — Union Pacific

For Union Pacific, Does the commitment to protect union jobs slow the productivity gains?

- `railroad.price.fact_labor_expense`: `fiscal_quarter_id`, `scenario_id`, `workforce_group_id`, `cost_bucket_id`, `labor_expense_amount`, `compensation_per_employee`
- `railroad.price.fact_other_income`: `fiscal_quarter_id`, `scenario_id`, `income_type_id`, `other_income_amount`, `real_estate_gain_amount`
- `railroad.price.fact_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `productivity_initiative_id`, `cost_bucket_id`, `productivity_savings_amount`
- `railroad.supply.dim_productivity_initiative`: `productivity_initiative_id`, `productivity_initiative_name`, `division_id`
- `railroad.supply.dim_workforce_group`: `workforce_group_id`, `workforce_group_code`, `workforce_group_name`
- `railroad.supply.fact_crew_resource`: `fiscal_quarter_id`, `scenario_id`, `crew_district_id`, `workforce_group_id`, `crew_quantity`, `crew_employee_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (3) — Union Pacific

For Union Pacific, How does a looser switching rule change the view of access and competition?

- `railroad.demand.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `railroad.demand.dim_contract_type`: `contract_type_id`, `contract_type_code`, `contract_type_name`
- `railroad.demand.dim_interchange`: `interchange_id`, `interchange_name`, `metro_id`
- `railroad.demand.dim_lane`: `lane_id`, `lane_name`, `origin_metro_name`, `destination_metro_name`, `interchange_id`
- `railroad.demand.dim_project`: `project_id`, `project_name`, `region_id`, `commodity_id`
- `railroad.demand.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_segment_id`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (4) — Union Pacific

For Union Pacific, How are customers reacting to the competitive proposal now that they have seen it?

- `railroad.demand.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_segment_id`
- `railroad.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `railroad.demand.dim_coal_grade`: `coal_grade_id`, `coal_grade_code`, `coal_grade_name`
- `railroad.demand.dim_coast`: `coast_id`, `coast_code`, `coast_name`
- `railroad.demand.dim_commercial_channel`: `commercial_channel_id`, `commercial_channel_code`, `commercial_channel_name`
- `railroad.demand.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (7) — Union Pacific

For Union Pacific, Is there a risk that volume shifts to another eastern railroad while approval is pending?

- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_interchange_volume`: `fiscal_quarter_id`, `scenario_id`, `interchange_id`, `service_type_id`, `competitor_id`, `interchanged_carload_quantity`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.demand.dim_coast`: `coast_id`, `coast_code`, `coast_name`
- `railroad.demand.dim_commercial_channel`: `commercial_channel_id`, `commercial_channel_code`, `commercial_channel_name`
- `railroad.demand.dim_interchange`: `interchange_id`, `interchange_name`, `metro_id`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (8) — Union Pacific

For Union Pacific, How does the open-access gateway offer relate to the proposed change in reciprocal-switching rules?

- `railroad.demand.dim_metro`: `metro_id`, `metro_code`, `metro_name`, `state_id`
- `railroad.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `railroad.demand.dim_coal_grade`: `coal_grade_id`, `coal_grade_code`, `coal_grade_name`
- `railroad.demand.dim_coast`: `coast_id`, `coast_code`, `coast_name`
- `railroad.demand.dim_commercial_channel`: `commercial_channel_id`, `commercial_channel_code`, `commercial_channel_name`
- `railroad.demand.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (11) — Union Pacific

For Union Pacific, What volume or cost impact should be expected from the winter storm?

- `railroad.demand.fact_project_volume`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `commodity_id`, `region_id`, `project_carload_quantity`, `ramp_carload_quantity`
- `railroad.supply.dim_weather_event_type`: `weather_event_type_id`, `weather_event_type_code`, `weather_event_type_name`
- `railroad.supply.fact_weather_disruption`: `fiscal_quarter_id`, `scenario_id`, `weather_event_type_id`, `division_id`, `disruption_duration_hours`, `delayed_train_quantity`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_contracted_volume`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `shipper_id`, `commodity_id`, `contracted_carload_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`

### Q3 2025 (1) — Union Pacific

For Union Pacific, How is shipper support progressing, beyond the labor agreement already reached?

- `railroad.demand.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_segment_id`
- `railroad.demand.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `railroad.demand.dim_contract_type`: `contract_type_id`, `contract_type_code`, `contract_type_name`
- `railroad.demand.dim_project`: `project_id`, `project_name`, `region_id`, `commodity_id`
- `railroad.demand.dim_shipper_segment`: `shipper_segment_id`, `shipper_segment_code`, `shipper_segment_name`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (5) — Union Pacific

For Union Pacific, How large is the watershed traffic the industry could still access?

- `railroad.demand.fact_truck_market_volume`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `competitor_id`, `truck_load_quantity`
- `railroad.supply.fact_equipment_resource`: `fiscal_quarter_id`, `scenario_id`, `equipment_type_id`, `division_id`, `equipment_unit_quantity`, `available_equipment_quantity`
- `railroad.demand.dim_coast`: `coast_id`, `coast_code`, `coast_name`
- `railroad.demand.dim_commercial_channel`: `commercial_channel_id`, `commercial_channel_code`, `commercial_channel_name`
- `railroad.demand.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `railroad.demand.dim_handling_type`: `handling_type_id`, `handling_type_code`, `handling_type_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (10) — Union Pacific

For Union Pacific, On grain, is export the negative from tariffs while domestic metals and other moves are a positive?

- `railroad.price.fact_accessorial_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `price_program_id`, `accessorial_revenue_amount`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_other_income`: `fiscal_quarter_id`, `scenario_id`, `income_type_id`, `other_income_amount`, `real_estate_gain_amount`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.demand.dim_coast`: `coast_id`, `coast_code`, `coast_name`
- `railroad.demand.dim_commercial_channel`: `commercial_channel_id`, `commercial_channel_code`, `commercial_channel_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
