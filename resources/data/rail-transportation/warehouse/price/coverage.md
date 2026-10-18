# Railroad Inc price, cost, and margin

This slice is part of the Railroad Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity row does not store a price. A price row does not store the unit quantity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `dim_fiscal_quarter_identity` | `fiscal_quarter_id` | `railroad.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `dim_traffic_type_identity` | `traffic_type_id` | `railroad.customer.dim_traffic_type` `traffic_type_id` |
| `dim_commodity_identity` | `commodity_id` | `railroad.customer.dim_commodity` `commodity_id` |
| `dim_contract_identity` | `contract_id` | `railroad.customer.dim_contract` `contract_id` |
| `dim_technology_identity` | `technology_id` | `railroad.network.dim_technology` `technology_id` |
| `dim_initiative_identity` | `initiative_id` | `railroad.network.dim_initiative` `initiative_id` |
| `dim_gateway_identity` | `gateway_id` | `railroad.geography.dim_gateway` `gateway_id` |
| `dim_service_metric_identity` | `service_metric_id` | `railroad.network.dim_service_metric` `service_metric_id` |
| `dim_shipper_identity` | `shipper_id` | `railroad.customer.dim_shipper` `shipper_id` |
| `dim_calendar_day_identity` | `calendar_day_id` | `railroad.geography.dim_calendar_day` `calendar_day_id` |

## Numbered questions

### Q1 2026 (1) — CSX

For CSX, what offsets the operating-ratio hit from higher fuel so the full-year ratio can still be held, with a bias to the high end?

- `railroad.price.fact_operating_ratio`: `operating_ratio`, `full_year_target_ratio`, `high_end_bias_flag`, `fuel_headwind_amount`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.price.fact_fuel_cost`: `fuel_cost_amount`, `diesel_headwind_amount`, `half_versus_half_amount`, `fiscal_quarter_id`, `fuel_grade_id`, `benchmark_id`
- `railroad.supply.fact_workforce_productivity`: `productivity_index`, `further_gain_flag`, `volume_growth_compatible_flag`, `fiscal_quarter_id`, `resource_pool_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `railroad.price.dim_fuel_grade`: `fuel_grade_id`, `grade_code`, `grade_name`
- `railroad.price.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`
- `railroad.network.dim_resource_pool`: `resource_pool_id`, `pool_code`, `pool_name`

### Q1 2026 (3) — CSX

For CSX, is the first-quarter improvement in purchased services and other the run rate, or is there more to take out?

- `railroad.price.fact_purchased_services`: `expense_amount`, `is_run_rate_flag`, `remaining_opportunity_amount`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.price.fact_operating_cost`: `operating_cost_amount`, `improved_with_service_flag`, `intraquarter_improvement_flag`, `fiscal_quarter_id`, `cost_bucket_id`, `calendar_day_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `railroad.geography.dim_calendar_day`: `calendar_day_id`, `calendar_date`, `fiscal_quarter_id`

### Q1 2026 (4) — CSX

For CSX, is the real-estate gain the expected run rate, and does it recur in the back half?

- `railroad.price.fact_real_estate`: `gain_amount`, `run_rate_flag`, `recurs_in_back_half_flag`, `fiscal_quarter_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`

### Q1 2026 (5) — CSX

For CSX, is a higher return on capital mainly asset productivity, mix and price, or cost efficiency?

- `railroad.price.fact_return_on_capital`: `return_rate`, `primary_lever_code`, `fiscal_quarter_id`
- `railroad.supply.fact_asset_productivity`: `productivity_index`, `primary_lever_code`, `fiscal_quarter_id`, `region_id`
- `railroad.price.fact_price`: `price_change_amount`, `guide_growth_amount`, `price_component_amount`, `net_positive_flag`, `fiscal_quarter_id`, `price_program_id`, `traffic_type_id`
- `railroad.price.fact_mix`: `mix_effect_amount`, `negative_mix_flag`, `lifts_growth_flag`, `fiscal_quarter_id`, `traffic_type_id`
- `railroad.price.fact_operating_cost`: `operating_cost_amount`, `improved_with_service_flag`, `intraquarter_improvement_flag`, `fiscal_quarter_id`, `cost_bucket_id`, `calendar_day_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.price.dim_price_program`: `price_program_id`, `program_code`, `program_name`

### Q1 2026 (6) — CSX

For CSX, how long is the lag before a tighter truck spot and contract market shows up in intermodal or merchandise price, and can any of it help in the second half?

- `railroad.price.fact_intermodal_price`: `price_amount`, `talks_status_code`, `loose_truck_flag`, `fiscal_quarter_id`, `price_program_id`, `traffic_type_id`
- `railroad.price.fact_merchandise_price`: `price_amount`, `holding_up_flag`, `fiscal_quarter_id`, `price_program_id`, `contract_id`
- `railroad.price.fact_truck_rate`: `spot_rate_amount`, `contract_rate_amount`, `lag_quarters`, `tightening_flag`, `fiscal_quarter_id`, `benchmark_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_price_program`: `price_program_id`, `program_code`, `program_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_contract`: `contract_id`, `contract_code`, `renewal_year`, `shipper_id`
- `railroad.price.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`

### Q1 2026 (8) — CSX

For CSX, is the sequential coal yield improvement an easing of index headwinds or a mix benefit?

- `railroad.price.fact_coal_yield`: `revenue_per_unit_amount`, `index_headwind_amount`, `mix_benefit_amount`, `sequential_change_amount`, `fiscal_quarter_id`, `benchmark_id`, `commodity_id`
- `railroad.price.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`
- `railroad.price.fact_mix`: `mix_effect_amount`, `negative_mix_flag`, `lifts_growth_flag`, `fiscal_quarter_id`, `traffic_type_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`

### Q1 2026 (11) — CSX

For CSX, what is the size and timing of the cost headwinds, including incentive pay, and which productivity actions are aimed at 2027 rather than this year?

- `railroad.price.fact_incentive_pay`: `incentive_amount`, `shows_in_year_flag`, `aimed_at_next_year_flag`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.supply.fact_workforce_productivity`: `productivity_index`, `further_gain_flag`, `volume_growth_compatible_flag`, `fiscal_quarter_id`, `resource_pool_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `railroad.network.dim_resource_pool`: `resource_pool_id`, `pool_code`, `pool_name`

### Q4 2025 (1) — CSX

For CSX, how should the price-cost spread be thought about, separate from the base operating ratio?

- `railroad.price.fact_price`: `price_change_amount`, `guide_growth_amount`, `price_component_amount`, `net_positive_flag`, `fiscal_quarter_id`, `price_program_id`, `traffic_type_id`
- `railroad.price.fact_operating_cost`: `operating_cost_amount`, `improved_with_service_flag`, `intraquarter_improvement_flag`, `fiscal_quarter_id`, `cost_bucket_id`, `calendar_day_id`
- `railroad.price.fact_operating_ratio`: `operating_ratio`, `full_year_target_ratio`, `high_end_bias_flag`, `fuel_headwind_amount`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_price_program`: `price_program_id`, `program_code`, `program_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `railroad.geography.dim_calendar_day`: `calendar_day_id`, `calendar_date`, `fiscal_quarter_id`

### Q4 2025 (2) — CSX

For CSX, how much of the operating-ratio improvement is items already known to roll off, and what inflation is inside the guide?

- `railroad.price.fact_operating_ratio`: `operating_ratio`, `full_year_target_ratio`, `high_end_bias_flag`, `fuel_headwind_amount`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.price.fact_inflation`: `inflation_amount`, `faster_than_realization_flag`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.price.fact_or_bridge`: `known_rolloff_amount`, `identified_savings_amount`, `other_item_amount`, `inflation_inside_guide_amount`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`

### Q4 2025 (3) — CSX

For CSX, how does low-single-digit revenue growth split between volume and yield, and what longer-term operating ratio is realistic?

- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.price.fact_yield`: `yield_amount`, `core_yield_amount`, `fuel_excluded_flag`, `fiscal_quarter_id`, `traffic_type_id`, `benchmark_id`
- `railroad.price.fact_operating_ratio`: `operating_ratio`, `full_year_target_ratio`, `high_end_bias_flag`, `fuel_headwind_amount`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q4 2025 (8) — CSX

For CSX, what is driving coal revenue per unit, and what is assumed in the revenue outlook?

- `railroad.price.fact_coal_yield`: `revenue_per_unit_amount`, `index_headwind_amount`, `mix_benefit_amount`, `sequential_change_amount`, `fiscal_quarter_id`, `benchmark_id`, `commodity_id`
- `railroad.demand.fact_coal_volume`: `coal_quantity`, `response_lag_quarters`, `fiscal_quarter_id`, `commodity_id`, `region_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`

### Q4 2025 (9) — CSX

For CSX, how long do natural-gas prices have to stay high before coal or other volumes respond?

- `railroad.price.fact_gas_price`: `gas_price_amount`, `weeks_above_threshold`, `fiscal_quarter_id`, `benchmark_id`
- `railroad.demand.fact_coal_volume`: `coal_quantity`, `response_lag_quarters`, `fiscal_quarter_id`, `commodity_id`, `region_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`

### Q4 2025 (12) — CSX

For CSX, does low-single-digit revenue growth imply negative mix if price is in the usual range and volume grows?

- `railroad.price.fact_price`: `price_change_amount`, `guide_growth_amount`, `price_component_amount`, `net_positive_flag`, `fiscal_quarter_id`, `price_program_id`, `traffic_type_id`
- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.price.fact_mix`: `mix_effect_amount`, `negative_mix_flag`, `lifts_growth_flag`, `fiscal_quarter_id`, `traffic_type_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_price_program`: `price_program_id`, `program_code`, `program_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`

### Q4 2025 (13) — CSX

For CSX, is operating-ratio improvement spread through the year or weighted to the front or back?

- `railroad.price.fact_operating_ratio`: `operating_ratio`, `full_year_target_ratio`, `high_end_bias_flag`, `fuel_headwind_amount`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.price.fact_or_cadence`: `weight_code`, `front_weighted_flag`, `fiscal_quarter_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`

### Q4 2025 (14) — CSX

For CSX, of the guided operating-ratio improvement, how much is the identified cost savings versus other items?

- `railroad.price.fact_cost_savings`: `savings_amount`, `workforce_bucket_amount`, `other_bucket_amount`, `fiscal_quarter_id`, `cost_bucket_id`, `initiative_id`
- `railroad.price.fact_operating_ratio`: `operating_ratio`, `full_year_target_ratio`, `high_end_bias_flag`, `fuel_headwind_amount`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `railroad.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`

### Q2 2025 (4) — CSX

For CSX, did costs improve as operating metrics improved through the quarter after a weak April?

- `railroad.price.fact_operating_cost`: `operating_cost_amount`, `improved_with_service_flag`, `intraquarter_improvement_flag`, `fiscal_quarter_id`, `cost_bucket_id`, `calendar_day_id`
- `railroad.supply.fact_service_level`: `service_index`, `prior_best_gap`, `commercial_support_flag`, `fiscal_quarter_id`, `service_metric_id`, `calendar_day_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `railroad.geography.dim_calendar_day`: `calendar_day_id`, `calendar_date`, `fiscal_quarter_id`
- `railroad.network.dim_service_metric`: `service_metric_id`, `metric_code`, `metric_name`

### Q2 2025 (5) — CSX

For CSX, what is the sequential outlook for coal revenue per unit, and how much smaller are the benchmark and diesel headwinds in the second half versus the first?

- `railroad.price.fact_coal_yield`: `revenue_per_unit_amount`, `index_headwind_amount`, `mix_benefit_amount`, `sequential_change_amount`, `fiscal_quarter_id`, `benchmark_id`, `commodity_id`
- `railroad.price.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`
- `railroad.price.fact_fuel_cost`: `fuel_cost_amount`, `diesel_headwind_amount`, `half_versus_half_amount`, `fiscal_quarter_id`, `fuel_grade_id`, `benchmark_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.price.dim_fuel_grade`: `fuel_grade_id`, `grade_code`, `grade_name`

### Q2 2025 (8) — CSX

For CSX, was there an upside surprise late in the quarter inside the other-revenue run rate?

- `railroad.price.fact_other_revenue`: `other_revenue_amount`, `upside_surprise_flag`, `run_rate_amount`, `fiscal_quarter_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`

### Q2 2025 (11) — CSX

For CSX, does the stated cost of inconvenience capture the whole service penalty?

- `railroad.price.fact_inconvenience_cost`: `inconvenience_amount`, `captures_full_penalty_flag`, `fiscal_quarter_id`, `service_metric_id`
- `railroad.price.fact_operating_cost`: `operating_cost_amount`, `improved_with_service_flag`, `intraquarter_improvement_flag`, `fiscal_quarter_id`, `cost_bucket_id`, `calendar_day_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.network.dim_service_metric`: `service_metric_id`, `metric_code`, `metric_name`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `railroad.geography.dim_calendar_day`: `calendar_day_id`, `calendar_date`, `fiscal_quarter_id`

### Q2 2025 (12) — CSX

For CSX, can better service produce positive net price in the back half after mix and fuel absorbed price this quarter?

- `railroad.price.fact_price`: `price_change_amount`, `guide_growth_amount`, `price_component_amount`, `net_positive_flag`, `fiscal_quarter_id`, `price_program_id`, `traffic_type_id`
- `railroad.supply.fact_service_level`: `service_index`, `prior_best_gap`, `commercial_support_flag`, `fiscal_quarter_id`, `service_metric_id`, `calendar_day_id`
- `railroad.price.fact_mix`: `mix_effect_amount`, `negative_mix_flag`, `lifts_growth_flag`, `fiscal_quarter_id`, `traffic_type_id`
- `railroad.price.fact_fuel_cost`: `fuel_cost_amount`, `diesel_headwind_amount`, `half_versus_half_amount`, `fiscal_quarter_id`, `fuel_grade_id`, `benchmark_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_price_program`: `price_program_id`, `program_code`, `program_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.network.dim_service_metric`: `service_metric_id`, `metric_code`, `metric_name`

### Q3 2024 (1) — CSX

For CSX, how does price get back to a positive spread versus cost next year after labor inflation is already set?

- `railroad.price.fact_price`: `price_change_amount`, `guide_growth_amount`, `price_component_amount`, `net_positive_flag`, `fiscal_quarter_id`, `price_program_id`, `traffic_type_id`
- `railroad.price.fact_compensation`: `compensation_per_employee_amount`, `wage_inflation_amount`, `technology_offset_amount`, `fiscal_quarter_id`, `cost_bucket_id`, `technology_id`
- `railroad.customer.dim_contract`: `contract_id`, `contract_code`, `renewal_year`, `shipper_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_price_program`: `price_program_id`, `program_code`, `program_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `railroad.network.dim_technology`: `technology_id`, `technology_code`, `technology_name`

### Q3 2024 (2) — CSX

For CSX, how are next-year intermodal price talks progressing in a loose truck market, and can mix lift revenue growth above the low single digits?

- `railroad.price.fact_intermodal_price`: `price_amount`, `talks_status_code`, `loose_truck_flag`, `fiscal_quarter_id`, `price_program_id`, `traffic_type_id`
- `railroad.price.fact_truck_rate`: `spot_rate_amount`, `contract_rate_amount`, `lag_quarters`, `tightening_flag`, `fiscal_quarter_id`, `benchmark_id`
- `railroad.price.fact_mix`: `mix_effect_amount`, `negative_mix_flag`, `lifts_growth_flag`, `fiscal_quarter_id`, `traffic_type_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_price_program`: `price_program_id`, `program_code`, `program_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.price.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`

### Q3 2024 (6) — CSX

For CSX, with little margin progress likely this year, what would have to change for margin to expand in the current environment?

- `railroad.price.fact_operating_margin`: `margin_rate`, `expansion_condition_code`, `lower_flag`, `fiscal_quarter_id`, `traffic_type_id`
- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.price.fact_operating_cost`: `operating_cost_amount`, `improved_with_service_flag`, `intraquarter_improvement_flag`, `fiscal_quarter_id`, `cost_bucket_id`, `calendar_day_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q3 2024 (11) — CSX

For CSX, is better chemical pricing a healthy market or a quality mix shift?

- `railroad.demand.fact_chemical_volume`: `chemical_quantity`, `fiscal_quarter_id`, `commodity_id`, `region_id`
- `railroad.price.fact_price`: `price_change_amount`, `guide_growth_amount`, `price_component_amount`, `net_positive_flag`, `fiscal_quarter_id`, `price_program_id`, `traffic_type_id`
- `railroad.price.fact_mix`: `mix_effect_amount`, `negative_mix_flag`, `lifts_growth_flag`, `fiscal_quarter_id`, `traffic_type_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.price.dim_price_program`: `price_program_id`, `program_code`, `program_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`

### Q1 2026 (1) — Union Pacific

For Union Pacific, can operating-ratio improvement continue if fuel and fuel-surcharge lag are a headwind, and where is incremental productivity showing up?

- `railroad.price.fact_operating_ratio`: `operating_ratio`, `full_year_target_ratio`, `high_end_bias_flag`, `fuel_headwind_amount`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.price.fact_fuel_cost`: `fuel_cost_amount`, `diesel_headwind_amount`, `half_versus_half_amount`, `fiscal_quarter_id`, `fuel_grade_id`, `benchmark_id`
- `railroad.price.fact_fuel_surcharge`: `lag_amount`, `headwind_flag`, `fiscal_quarter_id`, `fuel_grade_id`
- `railroad.supply.fact_workforce_productivity`: `productivity_index`, `further_gain_flag`, `volume_growth_compatible_flag`, `fiscal_quarter_id`, `resource_pool_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `railroad.price.dim_fuel_grade`: `fuel_grade_id`, `grade_code`, `grade_name`
- `railroad.price.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`

### Q1 2026 (4) — Union Pacific

For Union Pacific, what customer feedback has committed gateway pricing produced?

- `railroad.price.fact_gateway_price`: `gateway_price_amount`, `feedback_code`, `competition_claim_flag`, `fiscal_quarter_id`, `gateway_id`, `price_program_id`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.geography.dim_gateway`: `gateway_id`, `gateway_code`, `gateway_name`, `metro_id`
- `railroad.price.dim_price_program`: `price_program_id`, `program_code`, `program_name`

### Q4 2025 (1) — Union Pacific

For Union Pacific, if price is not the margin driver in 2026, how does faster inflation get covered?

- `railroad.price.fact_price`: `price_change_amount`, `guide_growth_amount`, `price_component_amount`, `net_positive_flag`, `fiscal_quarter_id`, `price_program_id`, `traffic_type_id`
- `railroad.price.fact_inflation`: `inflation_amount`, `faster_than_realization_flag`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.price.fact_operating_margin`: `margin_rate`, `expansion_condition_code`, `lower_flag`, `fiscal_quarter_id`, `traffic_type_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_price_program`: `price_program_id`, `program_code`, `program_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`

### Q4 2025 (3) — Union Pacific

For Union Pacific, how does a looser switching rule change the view of access and competition?

- `railroad.price.fact_switching`: `access_change_code`, `rule_relation_code`, `customer_reaction_code`, `fiscal_quarter_id`, `gateway_id`, `shipper_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.geography.dim_gateway`: `gateway_id`, `gateway_code`, `gateway_name`, `metro_id`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q4 2025 (8) — Union Pacific

For Union Pacific, how does the open-access gateway offer relate to the proposed change in reciprocal-switching rules?

- `railroad.price.fact_switching`: `access_change_code`, `rule_relation_code`, `customer_reaction_code`, `fiscal_quarter_id`, `gateway_id`, `shipper_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.geography.dim_gateway`: `gateway_id`, `gateway_code`, `gateway_name`, `metro_id`
- `railroad.customer.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_code`, `shipper_segment_id`

### Q3 2025 (2) — Union Pacific

For Union Pacific, what are the fourth-quarter operating-ratio puts and takes if volume is down mid-single digits?

- `railroad.price.fact_operating_ratio`: `operating_ratio`, `full_year_target_ratio`, `high_end_bias_flag`, `fuel_headwind_amount`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.demand.fact_volume`: `carload_quantity`, `merchandise_quantity`, `outlook_flat_flag`, `fiscal_quarter_id`, `commodity_id`, `region_id`, `traffic_type_id`, `shipper_id`
- `railroad.price.fact_mix`: `mix_effect_amount`, `negative_mix_flag`, `lifts_growth_flag`, `fiscal_quarter_id`, `traffic_type_id`
- `railroad.price.fact_equipment_settlement`: `settlement_amount`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`

### Q3 2025 (5) — Union Pacific

For Union Pacific, what mix sits inside the yield increase excluding fuel?

- `railroad.price.fact_yield`: `yield_amount`, `core_yield_amount`, `fuel_excluded_flag`, `fiscal_quarter_id`, `traffic_type_id`, `benchmark_id`
- `railroad.price.fact_mix`: `mix_effect_amount`, `negative_mix_flag`, `lifts_growth_flag`, `fiscal_quarter_id`, `traffic_type_id`
- `railroad.price.fact_fuel_cost`: `fuel_cost_amount`, `diesel_headwind_amount`, `half_versus_half_amount`, `fiscal_quarter_id`, `fuel_grade_id`, `benchmark_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.price.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`
- `railroad.price.dim_fuel_grade`: `fuel_grade_id`, `grade_code`, `grade_name`

### Q3 2025 (8) — Union Pacific

For Union Pacific, if the truckload market inflects, how fast can domestic intermodal yields move, and what is the lag?

- `railroad.price.fact_domestic_intermodal_yield`: `yield_amount`, `domestic_uptick_sufficient_flag`, `lag_quarters`, `fiscal_quarter_id`, `traffic_type_id`, `benchmark_id`
- `railroad.price.fact_truck_rate`: `spot_rate_amount`, `contract_rate_amount`, `lag_quarters`, `tightening_flag`, `fiscal_quarter_id`, `benchmark_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.price.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`

### Q3 2025 (9) — Union Pacific

For Union Pacific, is pricing in the coming contracting season better than this year, and does the service product support that?

- `railroad.price.fact_price`: `price_change_amount`, `guide_growth_amount`, `price_component_amount`, `net_positive_flag`, `fiscal_quarter_id`, `price_program_id`, `traffic_type_id`
- `railroad.supply.fact_service_level`: `service_index`, `prior_best_gap`, `commercial_support_flag`, `fiscal_quarter_id`, `service_metric_id`, `calendar_day_id`
- `railroad.customer.dim_contract`: `contract_id`, `contract_code`, `renewal_year`, `shipper_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_price_program`: `price_program_id`, `program_code`, `program_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.network.dim_service_metric`: `service_metric_id`, `metric_code`, `metric_name`
- `railroad.geography.dim_calendar_day`: `calendar_day_id`, `calendar_date`, `fiscal_quarter_id`

### Q2 2025 (1) — Union Pacific

For Union Pacific, what cost puts and takes show up from the second quarter into the third, with the network running as well as it has?

- `railroad.price.fact_operating_cost`: `operating_cost_amount`, `improved_with_service_flag`, `intraquarter_improvement_flag`, `fiscal_quarter_id`, `cost_bucket_id`, `calendar_day_id`
- `railroad.supply.fact_service_level`: `service_index`, `prior_best_gap`, `commercial_support_flag`, `fiscal_quarter_id`, `service_metric_id`, `calendar_day_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `railroad.geography.dim_calendar_day`: `calendar_day_id`, `calendar_date`, `fiscal_quarter_id`
- `railroad.network.dim_service_metric`: `service_metric_id`, `metric_code`, `metric_name`

### Q2 2025 (3) — Union Pacific

For Union Pacific, how much further can the operating ratio move from the level already reached?

- `railroad.price.fact_operating_ratio`: `operating_ratio`, `full_year_target_ratio`, `high_end_bias_flag`, `fuel_headwind_amount`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`

### Q2 2025 (6) — Union Pacific

For Union Pacific, what second-half operating ratio and price/mix are expected, and how sustainable is coal strength beyond the contract win?

- `railroad.price.fact_operating_ratio`: `operating_ratio`, `full_year_target_ratio`, `high_end_bias_flag`, `fuel_headwind_amount`, `fiscal_quarter_id`, `cost_bucket_id`
- `railroad.price.fact_mix`: `mix_effect_amount`, `negative_mix_flag`, `lifts_growth_flag`, `fiscal_quarter_id`, `traffic_type_id`
- `railroad.demand.fact_coal_volume`: `coal_quantity`, `response_lag_quarters`, `fiscal_quarter_id`, `commodity_id`, `region_id`
- `railroad.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
- `railroad.customer.dim_traffic_type`: `traffic_type_id`, `traffic_type_code`, `traffic_type_name`
- `railroad.customer.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`, `traffic_type_id`
- `railroad.geography.dim_region`: `region_id`, `region_code`, `region_name`
