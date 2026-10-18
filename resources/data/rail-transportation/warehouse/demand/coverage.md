# Railroad Inc demand, customer, and geography

This slice is part of the Railroad Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity row does not store a price. A price row does not store the unit quantity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `dim_project_identity` | `project_id` | `railroad.network.dim_project` `project_id` |

## Numbered questions

### Q1 2026 (7) — CSX

For CSX, when do the projects already cited reach full carload ramp, and do the remaining projects for the year have a similar impact?

- `railroad.demand.fact_project_volume`: `project_carload_quantity`, `partnership_ramp_quantity`, `win_quantity`, `fiscal_quarter_id`, `project_id`, `commodity_id`, `region_id`
- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_project`: `project_id`, `project_code`, `project_name`, `project_type_id`, `corridor_id`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q1 2026 (10) — CSX

For CSX, how much of the flat volume outlook is project growth offset by macro pressure?

- `railroad.demand.fact_project_volume`: `project_carload_quantity`, `partnership_ramp_quantity`, `win_quantity`, `fiscal_quarter_id`, `project_id`, `commodity_id`, `region_id`
- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.demand.fact_volume_outlook`: `project_offset_quantity`, `macro_drag_quantity`, `outlook_quantity`, `fiscal_quarter_id`, `traffic_type_id`, `region_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_project`: `project_id`, `project_code`, `project_name`, `project_type_id`, `corridor_id`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`

### Q1 2026 (12) — CSX

For CSX, is the revenue outlook more or less optimistic on volume, and how does it split between price and volume given current staffing?

- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.price.fact_price`: `price_change_amount`, `guide_growth_amount`, `price_component_amount`, `net_positive_flag`, `fiscal_quarter_id`, `price_program_id`, `traffic_type_id`
- `railroad.supply.fact_headcount`: `headcount_quantity`, `can_support_volume_flag`, `record_low_flag`, `fiscal_quarter_id`, `resource_pool_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q4 2025 (7) — CSX

For CSX, while the industry combination is under review, what commercial opportunities can be taken in the near term?

- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.demand.fact_intermodal_volume`: `unit_quantity`, `snapback_slower_flag`, `can_accelerate_flag`, `fiscal_quarter_id`, `traffic_type_id`, `port_id`, `channel_id`, `region_id`
- `railroad.demand.fact_competitor_volume`: `competitor_quantity`, `share_shift_flag`, `commercial_risk_flag`, `fiscal_quarter_id`, `competitor_id`, `traffic_type_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q4 2025 (10) — CSX

For CSX, has anything in the business changed the long-term earnings framework once the macro is normal again?

- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.price.fact_price`: `price_change_amount`, `guide_growth_amount`, `price_component_amount`, `net_positive_flag`, `fiscal_quarter_id`, `price_program_id`, `traffic_type_id`
- `railroad.supply.fact_workforce_productivity`: `productivity_index`, `further_gain_flag`, `volume_growth_compatible_flag`, `fiscal_quarter_id`, `resource_pool_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q2 2025 (3) — CSX

For CSX, is the full-year volume improvement a return of outages or a real acceleration from the second-quarter level?

- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.demand.fact_outage_return`: `returned_quantity`, `acceleration_flag`, `fiscal_quarter_id`, `traffic_type_id`, `region_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q2 2025 (7) — CSX

For CSX, why was the intermodal snapback slower than the air pocket, and can volumes accelerate from the quarter-to-date pace?

- `railroad.demand.fact_intermodal_volume`: `unit_quantity`, `snapback_slower_flag`, `can_accelerate_flag`, `fiscal_quarter_id`, `traffic_type_id`, `port_id`, `channel_id`, `region_id`
- `railroad.demand.fact_consumer_demand`: `demand_index`, `air_pocket_flag`, `fiscal_quarter_id`, `traffic_type_id`, `region_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.geography.dim_port`: `port_id`, `port_code`, `port_name`, `metro_id`, `coast_id`
- `railroad.customer.dim_channel`: `channel_id`, `channel_code`, `channel_name`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`

### Q2 2025 (10) — CSX

For CSX, where does second-half volume have to come from, including peak season, to get the full year back to growth?

- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.demand.fact_peak_volume`: `peak_quantity`, `required_for_growth_flag`, `fiscal_quarter_id`, `peak_season_id`, `traffic_type_id`
- `railroad.demand.fact_consumer_demand`: `demand_index`, `air_pocket_flag`, `fiscal_quarter_id`, `traffic_type_id`, `region_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q2 2025 (13) — CSX

For CSX, have customer conversations on railroad-specific projects increased or paused because of tariffs, and how large is the partnership ramp?

- `railroad.demand.fact_project_volume`: `project_carload_quantity`, `partnership_ramp_quantity`, `win_quantity`, `fiscal_quarter_id`, `project_id`, `commodity_id`, `region_id`
- `railroad.demand.fact_trade_risk`: `volume_at_risk_quantity`, `trade_pause_flag`, `fiscal_quarter_id`, `project_id`, `commodity_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_project`: `project_id`, `project_code`, `project_name`, `project_type_id`, `corridor_id`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`

### Q3 2024 (3) — CSX

For CSX, after fuel, coal, hurricane, and softer autos and metals, why is revenue down and the operating margin lower?

- `railroad.price.fact_fuel_cost`: `fuel_cost_amount`, `diesel_headwind_amount`, `half_versus_half_amount`, `fiscal_quarter_id`, `fuel_grade_id`, `benchmark_id`
- `railroad.demand.fact_coal_volume`: `coal_quantity`, `response_lag_quarters`, `fiscal_quarter_id`, `commodity_id`, `region_id`
- `railroad.network.dim_weather_event`: `weather_event_id`, `event_code`, `event_name`, `fiscal_quarter_id`
- `railroad.demand.fact_auto_move`: `auto_quantity`, `softer_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`
- `railroad.demand.fact_metals_move`: `move_quantity`, `domestic_positive_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`
- `railroad.price.fact_operating_margin`: `margin_rate`, `expansion_condition_code`, `lower_flag`, `fiscal_quarter_id`, `traffic_type_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_fuel_grade`: `fuel_grade_id`, `grade_code`, `grade_name`

### Q3 2024 (5) — CSX

For CSX, how sensitive are the multi-year industrial projects to the economic cycle?

- `railroad.demand.fact_cycle_sensitivity`: `cycle_sensitive_flag`, `project_quantity`, `fiscal_quarter_id`, `project_id`, `region_id`
- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_project`: `project_id`, `project_code`, `project_name`, `project_type_id`, `corridor_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q3 2024 (7) — CSX

For CSX, what categories did truck-to-rail wins fall into, and how is merchandise pricing holding up?

- `railroad.demand.fact_truck_conversion`: `converted_quantity`, `win_category_code`, `still_on_highway_flag`, `fiscal_quarter_id`, `traffic_type_id`, `channel_id`, `region_id`
- `railroad.price.fact_merchandise_price`: `price_amount`, `holding_up_flag`, `fiscal_quarter_id`, `price_program_id`, `contract_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_channel`: `channel_id`, `channel_code`, `channel_name`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.price.dim_price_program`: `price_program_id`, `program_code`, `program_name`
- `railroad.customer.dim_contract`: `contract_id`, `contract_code`, `renewal_year`, `shipper_id`

### Q3 2024 (8) — CSX

For CSX, is the modest domestic-intermodal uptick enough to move intermodal yield, relative to international?

- `railroad.demand.fact_intermodal_volume`: `unit_quantity`, `snapback_slower_flag`, `can_accelerate_flag`, `fiscal_quarter_id`, `traffic_type_id`, `port_id`, `channel_id`, `region_id`
- `railroad.price.fact_yield`: `yield_amount`, `core_yield_amount`, `fuel_excluded_flag`, `fiscal_quarter_id`, `traffic_type_id`, `benchmark_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.geography.dim_port`: `port_id`, `port_code`, `port_name`, `metro_id`, `coast_id`
- `railroad.customer.dim_channel`: `channel_id`, `channel_code`, `channel_name`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.price.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`

### Q3 2024 (9) — CSX

For CSX, how much volume was diverted ahead of the East Coast labor risk, and is it returning?

- `railroad.geography.dim_port`: `port_id`, `port_code`, `port_name`, `metro_id`, `coast_id`
- `railroad.demand.fact_diverted_volume`: `diverted_quantity`, `returning_flag`, `labor_risk_flag`, `fiscal_quarter_id`, `port_id`, `coast_id`, `traffic_type_id`
- `railroad.demand.fact_intermodal_volume`: `unit_quantity`, `snapback_slower_flag`, `can_accelerate_flag`, `fiscal_quarter_id`, `traffic_type_id`, `port_id`, `channel_id`, `region_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.geography.dim_coast`: `coast_id`, `coast_code`, `coast_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_channel`: `channel_id`, `channel_code`, `channel_name`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`

### Q3 2024 (10) — CSX

For CSX, how stable is export coal demand, and how should service be read against the erosion customers still see?

- `railroad.demand.fact_export_coal`: `export_quantity`, `demand_stability_code`, `service_read_code`, `fiscal_quarter_id`, `commodity_id`, `port_id`
- `railroad.supply.fact_service_level`: `service_index`, `prior_best_gap`, `commercial_support_flag`, `fiscal_quarter_id`, `service_metric_id`, `calendar_day_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_port`: `port_id`, `port_code`, `port_name`, `metro_id`, `coast_id`
- `railroad.network.dim_service_metric`: `service_metric_id`, `metric_code`, `metric_name`
- `railroad.geography.dim_calendar_day`: `calendar_day_id`, `calendar_date`, `fiscal_quarter_id`

### Q3 2024 (12) — CSX

For CSX, if freight that moved to the West Coast ahead of the port strike switches back, what happens to intermodal yields?

- `railroad.price.fact_intermodal_price`: `price_amount`, `talks_status_code`, `loose_truck_flag`, `fiscal_quarter_id`, `price_program_id`, `traffic_type_id`
- `railroad.geography.dim_port`: `port_id`, `port_code`, `port_name`, `metro_id`, `coast_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_price_program`: `price_program_id`, `program_code`, `program_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`

### Q3 2024 (13) — CSX

For CSX, is the competitor's service disruption showing up as contract opportunity or risk?

- `railroad.customer.dim_contract`: `contract_id`, `contract_code`, `renewal_year`, `shipper_id`
- `railroad.supply.fact_service_level`: `service_index`, `prior_best_gap`, `commercial_support_flag`, `fiscal_quarter_id`, `service_metric_id`, `calendar_day_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_service_metric`: `service_metric_id`, `metric_code`, `metric_name`
- `railroad.geography.dim_calendar_day`: `calendar_day_id`, `calendar_date`, `fiscal_quarter_id`

### Q1 2026 (3) — Union Pacific

For Union Pacific, how much carload growth is the business-development pipeline expected to add?

- `railroad.demand.fact_project_volume`: `project_carload_quantity`, `partnership_ramp_quantity`, `win_quantity`, `fiscal_quarter_id`, `project_id`, `commodity_id`, `region_id`
- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_project`: `project_id`, `project_code`, `project_name`, `project_type_id`, `corridor_id`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q4 2025 (2) — Union Pacific

For Union Pacific, how variable is the gross traffic gain from the combination relative to the cost of handling that traffic?

- `railroad.demand.fact_incremental_traffic`: `added_quantity`, `fiscal_quarter_id`, `traffic_type_id`, `region_id`
- `railroad.price.fact_handling_cost`: `handling_cost_amount`, `variable_with_traffic_flag`, `fiscal_quarter_id`, `traffic_type_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`

### Q4 2025 (4) — Union Pacific

For Union Pacific, how are customers reacting to the competitive proposal now that they have seen it?

- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`
- `railroad.price.fact_switching`: `access_change_code`, `rule_relation_code`, `customer_reaction_code`, `fiscal_quarter_id`, `gateway_id`, `shipper_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.geography.dim_gateway`: `gateway_id`, `gateway_code`, `gateway_name`, `metro_id`

### Q4 2025 (6) — Union Pacific

For Union Pacific, what volume and price are in the outlook, and how are customers absorbing new contracts in a soft demand environment?

- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.price.fact_price`: `price_change_amount`, `guide_growth_amount`, `price_component_amount`, `net_positive_flag`, `fiscal_quarter_id`, `price_program_id`, `traffic_type_id`
- `railroad.customer.dim_contract`: `contract_id`, `contract_code`, `renewal_year`, `shipper_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q4 2025 (7) — Union Pacific

For Union Pacific, is there a risk that volume shifts to another eastern railroad while approval is pending?

- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.demand.fact_intermodal_volume`: `unit_quantity`, `snapback_slower_flag`, `can_accelerate_flag`, `fiscal_quarter_id`, `traffic_type_id`, `port_id`, `channel_id`, `region_id`
- `railroad.demand.fact_eastern_shift`: `at_risk_quantity`, `review_pending_flag`, `fiscal_quarter_id`, `competitor_id`, `traffic_type_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q3 2025 (1) — Union Pacific

For Union Pacific, how is shipper support progressing, beyond the labor agreement already reached?

- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`
- `railroad.supply.fact_union_jobs`: `protection_flag`, `slows_productivity_flag`, `fiscal_quarter_id`, `resource_pool_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_resource_pool`: `resource_pool_id`, `pool_code`, `pool_name`

### Q3 2025 (3) — Union Pacific

For Union Pacific, does closer collaboration among competitors create a commercial risk during the review?

- `railroad.demand.fact_competitor_volume`: `competitor_quantity`, `share_shift_flag`, `commercial_risk_flag`, `fiscal_quarter_id`, `competitor_id`, `traffic_type_id`
- `railroad.demand.fact_intermodal_volume`: `unit_quantity`, `snapback_slower_flag`, `can_accelerate_flag`, `fiscal_quarter_id`, `traffic_type_id`, `port_id`, `channel_id`, `region_id`
- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`, `region_id`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.geography.dim_port`: `port_id`, `port_code`, `port_name`, `metro_id`, `coast_id`
- `railroad.customer.dim_channel`: `channel_id`, `channel_code`, `channel_name`

### Q3 2025 (6) — Union Pacific

For Union Pacific, is the intermodal change versus the other western railroad a share shift, looking at originated volume?

- `railroad.demand.fact_intermodal_volume`: `unit_quantity`, `snapback_slower_flag`, `can_accelerate_flag`, `fiscal_quarter_id`, `traffic_type_id`, `port_id`, `channel_id`, `region_id`
- `railroad.demand.fact_originated_volume`: `originated_quantity`, `share_shift_flag`, `fiscal_quarter_id`, `traffic_type_id`, `competitor_id`, `region_id`
- `railroad.customer.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`, `region_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.geography.dim_port`: `port_id`, `port_code`, `port_name`, `metro_id`, `coast_id`
- `railroad.customer.dim_channel`: `channel_id`, `channel_code`, `channel_name`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`

### Q3 2025 (10) — Union Pacific

For Union Pacific, what macro deterioration, including housing, would change the volume outlook?

- `railroad.demand.fact_housing_volume`: `housing_sensitive_quantity`, `outlook_change_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`
- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.demand.fact_volume_outlook`: `project_offset_quantity`, `macro_drag_quantity`, `outlook_quantity`, `fiscal_quarter_id`, `traffic_type_id`, `region_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q3 2025 (11) — Union Pacific

For Union Pacific, what is driving the business wins in the fourth-quarter outlook, and can that pipeline grow volume next year despite trade uncertainty?

- `railroad.demand.fact_project_volume`: `project_carload_quantity`, `partnership_ramp_quantity`, `win_quantity`, `fiscal_quarter_id`, `project_id`, `commodity_id`, `region_id`
- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.demand.fact_trade_risk`: `volume_at_risk_quantity`, `trade_pause_flag`, `fiscal_quarter_id`, `project_id`, `commodity_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_project`: `project_id`, `project_code`, `project_name`, `project_type_id`, `corridor_id`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`

### Q2 2025 (5) — Union Pacific

For Union Pacific, how large is the watershed traffic the industry could still access?

- `railroad.demand.fact_watershed`: `addressable_quantity`, `already_railed_quantity`, `fiscal_quarter_id`, `region_id`, `traffic_type_id`
- `railroad.demand.fact_truck_conversion`: `converted_quantity`, `win_category_code`, `still_on_highway_flag`, `fiscal_quarter_id`, `traffic_type_id`, `channel_id`, `region_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_channel`: `channel_id`, `channel_code`, `channel_name`

### Q2 2025 (7) — Union Pacific

For Union Pacific, are intermodal marketing companies or the railroad's own transload services the better path to more domestic intermodal, including the new seven-day product?

- `railroad.demand.fact_intermodal_volume`: `unit_quantity`, `snapback_slower_flag`, `can_accelerate_flag`, `fiscal_quarter_id`, `traffic_type_id`, `port_id`, `channel_id`, `region_id`
- `railroad.customer.dim_channel`: `channel_id`, `channel_code`, `channel_name`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.geography.dim_port`: `port_id`, `port_code`, `port_name`, `metro_id`, `coast_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`

### Q2 2025 (9) — Union Pacific

For Union Pacific, how much U.S.-bound traffic through Canadian ports could be repatriated, and is port capacity the bottleneck?

- `railroad.geography.dim_port`: `port_id`, `port_code`, `port_name`, `metro_id`, `coast_id`
- `railroad.demand.fact_repatriation`: `addressable_quantity`, `through_canadian_port_flag`, `fiscal_quarter_id`, `port_id`, `traffic_type_id`
- `railroad.supply.fact_port_capacity`: `capacity_quantity`, `bottleneck_flag`, `fiscal_quarter_id`, `port_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`

### Q2 2025 (10) — Union Pacific

For Union Pacific, on grain, is export the negative from tariffs while domestic metals and other moves are a positive?

- `railroad.demand.fact_grain_export`: `export_quantity`, `trade_pressure_flag`, `fiscal_quarter_id`, `commodity_id`, `port_id`
- `railroad.demand.fact_metals_move`: `move_quantity`, `domestic_positive_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`
- `railroad.demand.fact_trade_risk`: `volume_at_risk_quantity`, `trade_pause_flag`, `fiscal_quarter_id`, `project_id`, `commodity_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_port`: `port_id`, `port_code`, `port_name`, `metro_id`, `coast_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.network.dim_project`: `project_id`, `project_code`, `project_name`, `project_type_id`, `corridor_id`

### Q2 2025 (12) — Union Pacific

For Union Pacific, how much of the interest in a transcontinental service is coming from shippers who want trucks off the road?

- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`
- `railroad.supply.fact_single_line`: `ease_gap_score`, `shipper_benefit_code`, `fiscal_quarter_id`, `channel_id`, `shipper_id`
- `railroad.demand.fact_truck_conversion`: `converted_quantity`, `win_category_code`, `still_on_highway_flag`, `fiscal_quarter_id`, `traffic_type_id`, `channel_id`, `region_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_channel`: `channel_id`, `channel_code`, `channel_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
