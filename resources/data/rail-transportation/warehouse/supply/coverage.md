# Railroad Inc supply and capacity

This slice is part of the Railroad Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity row does not store a price. A price row does not store the unit quantity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `dim_corridor_identity` | `corridor_id` | `railroad.geography.dim_corridor` `corridor_id` |
| `dim_fiscal_quarter_identity` | `fiscal_quarter_id` | `railroad.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `dim_metro_identity` | `metro_id` | `railroad.geography.dim_metro` `metro_id` |
| `dim_region_identity` | `region_id` | `railroad.geography.dim_region` `region_id` |
| `dim_calendar_day_identity` | `calendar_day_id` | `railroad.geography.dim_calendar_day` `calendar_day_id` |
| `dim_port_identity` | `port_id` | `railroad.geography.dim_port` `port_id` |
| `dim_gateway_identity` | `gateway_id` | `railroad.geography.dim_gateway` `gateway_id` |
| `dim_channel_identity` | `channel_id` | `railroad.customer.dim_channel` `channel_id` |
| `dim_shipper_identity` | `shipper_id` | `railroad.customer.dim_shipper` `shipper_id` |

## Numbered questions

### Q1 2026 (2) — CSX

For CSX, when is double-stack through the Howard Street Tunnel and the Port of Baltimore fully launched, and how fast does volume load?

- `railroad.network.dim_project`: `project_id`, `project_code`, `project_name`, `project_type_id`, `corridor_id`
- `railroad.geography.dim_port`: `port_id`, `port_code`, `port_name`, `metro_id`, `coast_id`
- `railroad.supply.fact_project_ramp`: `months_to_full`, `fully_launched_flag`, `similar_impact_flag`, `fiscal_quarter_id`, `project_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`

### Q1 2026 (7) — CSX

For CSX, when do the projects already cited reach full carload ramp, and do the remaining projects for the year have a similar impact?

- `railroad.supply.fact_project_ramp`: `months_to_full`, `fully_launched_flag`, `similar_impact_flag`, `fiscal_quarter_id`, `project_id`
- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_project`: `project_id`, `project_code`, `project_name`, `project_type_id`, `corridor_id`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q1 2026 (9) — CSX

For CSX, besides the bridges that enable double-stack and the Chicago flow changes, what else this year improves productivity and margins?

- `railroad.supply.fact_project_ramp`: `months_to_full`, `fully_launched_flag`, `similar_impact_flag`, `fiscal_quarter_id`, `project_id`
- `railroad.supply.fact_chicago_constraint`: `constraint_flag`, `remaining_pain_flag`, `fiscal_quarter_id`, `metro_id`, `yard_id`
- `railroad.supply.fact_workforce_productivity`: `productivity_index`, `further_gain_flag`, `volume_growth_compatible_flag`, `fiscal_quarter_id`, `resource_pool_id`
- `railroad.price.fact_operating_margin`: `margin_rate`, `expansion_condition_code`, `lower_flag`, `fiscal_quarter_id`, `traffic_type_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_project`: `project_id`, `project_code`, `project_name`, `project_type_id`, `corridor_id`
- `railroad.geography.dim_metro`: `metro_id`, `metro_code`, `metro_name`, `state_id`
- `railroad.network.dim_yard`: `yard_id`, `yard_code`, `yard_name`, `metro_id`

### Q4 2025 (4) — CSX

For CSX, how is the network being prepared for the storm relative to the last time weather set the railroad back?

- `railroad.supply.fact_weather_disruption`: `delay_hours`, `recovery_days`, `fiscal_quarter_id`, `weather_event_id`, `region_id`
- `railroad.supply.fact_service_recovery`: `weather_share_rate`, `operating_change_share_rate`, `further_recovery_flag`, `fiscal_quarter_id`, `weather_event_id`, `region_id`
- `railroad.supply.fact_service_level`: `service_index`, `prior_best_gap`, `commercial_support_flag`, `fiscal_quarter_id`, `service_metric_id`, `calendar_day_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_weather_event`: `weather_event_id`, `event_code`, `event_name`, `fiscal_quarter_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.network.dim_service_metric`: `service_metric_id`, `metric_code`, `metric_name`
- `railroad.geography.dim_calendar_day`: `calendar_day_id`, `calendar_date`, `fiscal_quarter_id`

### Q4 2025 (5) — CSX

For CSX, what operating changes, under the new approach, get service back to the metrics of a few years ago?

- `railroad.supply.fact_service_level`: `service_index`, `prior_best_gap`, `commercial_support_flag`, `fiscal_quarter_id`, `service_metric_id`, `calendar_day_id`
- `railroad.supply.fact_operating_plan`: `plan_code`, `targets_prior_best_flag`, `fiscal_quarter_id`, `service_metric_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_service_metric`: `service_metric_id`, `metric_code`, `metric_name`
- `railroad.geography.dim_calendar_day`: `calendar_day_id`, `calendar_date`, `fiscal_quarter_id`

### Q4 2025 (6) — CSX

For CSX, what dollar buckets and headcount targets sit inside the savings programs?

- `railroad.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `railroad.supply.fact_headcount`: `headcount_quantity`, `can_support_volume_flag`, `record_low_flag`, `fiscal_quarter_id`, `resource_pool_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_resource_pool`: `resource_pool_id`, `pool_code`, `pool_name`

### Q4 2025 (11) — CSX

For CSX, how large is the double-stack opportunity, and how fast does it ramp after bids for the second quarter?

- `railroad.supply.fact_project_ramp`: `months_to_full`, `fully_launched_flag`, `similar_impact_flag`, `fiscal_quarter_id`, `project_id`
- `railroad.demand.fact_bid_volume`: `bid_quantity`, `second_quarter_bid_flag`, `fiscal_quarter_id`, `project_id`, `traffic_type_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_project`: `project_id`, `project_code`, `project_name`, `project_type_id`, `corridor_id`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`

### Q2 2025 (1) — CSX

For CSX, from a shipper's perspective, what service benefits would a transcontinental railroad provide versus today's interline service?

- `railroad.supply.fact_single_line`: `ease_gap_score`, `shipper_benefit_code`, `fiscal_quarter_id`, `channel_id`, `shipper_id`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_channel`: `channel_id`, `channel_code`, `channel_name`

### Q2 2025 (2) — CSX

For CSX, how much of the service recovery was weather versus operating changes, and how much further can it go?

- `railroad.supply.fact_service_level`: `service_index`, `prior_best_gap`, `commercial_support_flag`, `fiscal_quarter_id`, `service_metric_id`, `calendar_day_id`
- `railroad.supply.fact_weather_disruption`: `delay_hours`, `recovery_days`, `fiscal_quarter_id`, `weather_event_id`, `region_id`
- `railroad.supply.fact_operating_plan`: `plan_code`, `targets_prior_best_flag`, `fiscal_quarter_id`, `service_metric_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_service_metric`: `service_metric_id`, `metric_code`, `metric_name`
- `railroad.geography.dim_calendar_day`: `calendar_day_id`, `calendar_date`, `fiscal_quarter_id`
- `railroad.network.dim_weather_event`: `weather_event_id`, `event_code`, `event_name`, `fiscal_quarter_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`

### Q2 2025 (6) — CSX

For CSX, is ease of doing business the main gap between single-line service and interline service?

- `railroad.supply.fact_single_line`: `ease_gap_score`, `shipper_benefit_code`, `fiscal_quarter_id`, `channel_id`, `shipper_id`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_channel`: `channel_id`, `channel_code`, `channel_name`

### Q2 2025 (9) — CSX

For CSX, what trip-plan compliance is expected next quarter after the weak start and the later carload improvement?

- `railroad.supply.fact_trip_plan`: `compliance_rate`, `next_quarter_expected_rate`, `weak_start_flag`, `fiscal_quarter_id`, `service_metric_id`, `region_id`
- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_service_metric`: `service_metric_id`, `metric_code`, `metric_name`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q3 2024 (4) — CSX

For CSX, how do headcount and cost trend from here, including compensation per employee?

- `railroad.supply.fact_headcount`: `headcount_quantity`, `can_support_volume_flag`, `record_low_flag`, `fiscal_quarter_id`, `resource_pool_id`
- `railroad.price.fact_compensation`: `compensation_per_employee_amount`, `wage_inflation_amount`, `technology_offset_amount`, `fiscal_quarter_id`, `cost_bucket_id`, `technology_id`
- `railroad.supply.fact_service_level`: `service_index`, `prior_best_gap`, `commercial_support_flag`, `fiscal_quarter_id`, `service_metric_id`, `calendar_day_id`
- `railroad.supply.fact_asset_productivity`: `productivity_index`, `primary_lever_code`, `fiscal_quarter_id`, `region_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_resource_pool`: `resource_pool_id`, `pool_code`, `pool_name`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `railroad.network.dim_technology`: `technology_id`, `technology_code`, `technology_name`

### Q1 2026 (2) — Union Pacific

For Union Pacific, how much spare capacity does the network have, and what volume growth can it take without adding resources if end markets turn?

- `railroad.supply.fact_network_capacity`: `capacity_quantity`, `absorbable_growth_quantity`, `fiscal_quarter_id`, `region_id`, `corridor_id`
- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.supply.fact_spare_capacity`: `spare_quantity`, `utilization_index`, `volume_without_new_resources_quantity`, `fiscal_quarter_id`, `resource_pool_id`, `region_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.geography.dim_corridor`: `corridor_id`, `corridor_code`, `corridor_name`, `region_id`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`

### Q1 2026 (5) — Union Pacific

For Union Pacific, how important is volume growth, alongside current service, to showing the network can absorb a larger system?

- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.supply.fact_service_level`: `service_index`, `prior_best_gap`, `commercial_support_flag`, `fiscal_quarter_id`, `service_metric_id`, `calendar_day_id`
- `railroad.supply.fact_network_capacity`: `capacity_quantity`, `absorbable_growth_quantity`, `fiscal_quarter_id`, `region_id`, `corridor_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q1 2026 (6) — Union Pacific

For Union Pacific, is record workforce productivity and the low headcount the new normal, or can it improve further while revenue grows?

- `railroad.supply.fact_headcount`: `headcount_quantity`, `can_support_volume_flag`, `record_low_flag`, `fiscal_quarter_id`, `resource_pool_id`
- `railroad.supply.fact_workforce_productivity`: `productivity_index`, `further_gain_flag`, `volume_growth_compatible_flag`, `fiscal_quarter_id`, `resource_pool_id`
- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_resource_pool`: `resource_pool_id`, `pool_code`, `pool_name`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`

### Q1 2026 (7) — Union Pacific

For Union Pacific, does the commitment to protect union jobs slow the productivity gains?

- `railroad.supply.fact_union_jobs`: `protection_flag`, `slows_productivity_flag`, `fiscal_quarter_id`, `resource_pool_id`
- `railroad.supply.fact_workforce_productivity`: `productivity_index`, `further_gain_flag`, `volume_growth_compatible_flag`, `fiscal_quarter_id`, `resource_pool_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_resource_pool`: `resource_pool_id`, `pool_code`, `pool_name`

### Q1 2026 (8) — Union Pacific

For Union Pacific, given current utilization, service, and inflation, what do incremental margins look like if volume turns up?

- `railroad.supply.fact_spare_capacity`: `spare_quantity`, `utilization_index`, `volume_without_new_resources_quantity`, `fiscal_quarter_id`, `resource_pool_id`, `region_id`
- `railroad.supply.fact_service_level`: `service_index`, `prior_best_gap`, `commercial_support_flag`, `fiscal_quarter_id`, `service_metric_id`, `calendar_day_id`
- `railroad.price.fact_incremental_margin`: `incremental_margin_rate`, `leverage_rate`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.price.fact_inflation`: `inflation_amount`, `faster_than_realization_flag`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_resource_pool`: `resource_pool_id`, `pool_code`, `pool_name`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.network.dim_service_metric`: `service_metric_id`, `metric_code`, `metric_name`

### Q4 2025 (5) — Union Pacific

For Union Pacific, with record train length and velocity, why wouldn't the operating ratio improve by more?

- `railroad.price.fact_operating_ratio`: `operating_ratio`, `full_year_target_ratio`, `high_end_bias_flag`, `fuel_headwind_amount`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.supply.fact_train_length`: `length_feet`, `record_flag`, `fiscal_quarter_id`, `service_metric_id`, `region_id`
- `railroad.supply.fact_velocity`: `velocity_mph`, `record_flag`, `fiscal_quarter_id`, `service_metric_id`, `region_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `railroad.network.dim_service_metric`: `service_metric_id`, `metric_code`, `metric_name`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`

### Q4 2025 (9) — Union Pacific

For Union Pacific, does network performance support a stronger pricing conversation?

- `railroad.supply.fact_service_level`: `service_index`, `prior_best_gap`, `commercial_support_flag`, `fiscal_quarter_id`, `service_metric_id`, `calendar_day_id`
- `railroad.price.fact_price`: `price_change_amount`, `guide_growth_amount`, `price_component_amount`, `net_positive_flag`, `fiscal_quarter_id`, `price_program_id`, `traffic_type_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_service_metric`: `service_metric_id`, `metric_code`, `metric_name`
- `railroad.geography.dim_calendar_day`: `calendar_day_id`, `calendar_date`, `fiscal_quarter_id`
- `railroad.price.dim_price_program`: `price_program_id`, `program_code`, `program_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`

### Q4 2025 (10) — Union Pacific

For Union Pacific, does the compensation-per-employee increase include items that productivity, process, and technology are expected to offset?

- `railroad.price.fact_compensation`: `compensation_per_employee_amount`, `wage_inflation_amount`, `technology_offset_amount`, `fiscal_quarter_id`, `cost_bucket_id`, `technology_id`
- `railroad.supply.fact_workforce_productivity`: `productivity_index`, `further_gain_flag`, `volume_growth_compatible_flag`, `fiscal_quarter_id`, `resource_pool_id`
- `railroad.network.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `railroad.network.dim_resource_pool`: `resource_pool_id`, `pool_code`, `pool_name`

### Q4 2025 (11) — Union Pacific

For Union Pacific, what volume or cost impact should be expected from the winter storm?

- `railroad.supply.fact_weather_disruption`: `delay_hours`, `recovery_days`, `fiscal_quarter_id`, `weather_event_id`, `region_id`
- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_weather_event`: `weather_event_id`, `event_code`, `event_name`, `fiscal_quarter_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q3 2025 (4) — Union Pacific

For Union Pacific, with productivity challenged and the outlook showing more negatives than positives, how quickly can resources held for new business be adjusted?

- `railroad.supply.fact_resource_flex`: `days_to_adjust`, `resources_held_flag`, `fiscal_quarter_id`, `resource_pool_id`
- `railroad.supply.fact_headcount`: `headcount_quantity`, `can_support_volume_flag`, `record_low_flag`, `fiscal_quarter_id`, `resource_pool_id`
- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_resource_pool`: `resource_pool_id`, `pool_code`, `pool_name`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`

### Q3 2025 (7) — Union Pacific

For Union Pacific, how confident is the transfer of current service practices to a combined network, and how long would that take?

- `railroad.supply.fact_service_level`: `service_index`, `prior_best_gap`, `commercial_support_flag`, `fiscal_quarter_id`, `service_metric_id`, `calendar_day_id`
- `railroad.supply.fact_integration`: `months_to_transfer`, `confidence_code`, `fiscal_quarter_id`, `region_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_service_metric`: `service_metric_id`, `metric_code`, `metric_name`
- `railroad.geography.dim_calendar_day`: `calendar_day_id`, `calendar_date`, `fiscal_quarter_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`

### Q2 2025 (2) — Union Pacific

For Union Pacific, after the locomotive-refresh agreement ends, what is the condition of the fleet and is more refresh needed?

- `railroad.supply.fact_locomotive_fleet`: `unit_quantity`, `condition_code`, `refresh_needed_flag`, `fiscal_quarter_id`, `locomotive_class_id`
- `railroad.supply.fact_maintenance`: `program_ending_flag`, `refresh_complete_flag`, `fiscal_quarter_id`, `locomotive_class_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_locomotive_class`: `locomotive_class_id`, `class_code`, `class_name`

### Q2 2025 (4) — Union Pacific

For Union Pacific, is there progress toward smaller crews or more automation under the current regulatory backdrop?

- `railroad.supply.fact_crew_automation`: `crew_size_quantity`, `automation_progress_flag`, `regulatory_permission_flag`, `fiscal_quarter_id`, `crew_practice_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_crew_practice`: `crew_practice_id`, `practice_code`, `practice_name`

### Q2 2025 (8) — Union Pacific

For Union Pacific, where does Chicago interchange still constrain shippers?

- `railroad.supply.fact_chicago_constraint`: `constraint_flag`, `remaining_pain_flag`, `fiscal_quarter_id`, `metro_id`, `yard_id`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`
- `railroad.supply.fact_service_level`: `service_index`, `prior_best_gap`, `commercial_support_flag`, `fiscal_quarter_id`, `service_metric_id`, `calendar_day_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.geography.dim_metro`: `metro_id`, `metro_code`, `metro_name`, `state_id`
- `railroad.network.dim_yard`: `yard_id`, `yard_code`, `yard_name`, `metro_id`
- `railroad.network.dim_service_metric`: `service_metric_id`, `metric_code`, `metric_name`
- `railroad.geography.dim_calendar_day`: `calendar_day_id`, `calendar_date`, `fiscal_quarter_id`

### Q2 2025 (11) — Union Pacific

For Union Pacific, what structural limits of the network still keep freight on the highway despite strong service?

- `railroad.supply.fact_network_capacity`: `capacity_quantity`, `absorbable_growth_quantity`, `fiscal_quarter_id`, `region_id`, `corridor_id`
- `railroad.demand.fact_truck_conversion`: `converted_quantity`, `win_category_code`, `still_on_highway_flag`, `fiscal_quarter_id`, `traffic_type_id`, `channel_id`, `region_id`
- `railroad.supply.fact_service_level`: `service_index`, `prior_best_gap`, `commercial_support_flag`, `fiscal_quarter_id`, `service_metric_id`, `calendar_day_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.geography.dim_corridor`: `corridor_id`, `corridor_code`, `corridor_name`, `region_id`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_channel`: `channel_id`, `channel_code`, `channel_name`
