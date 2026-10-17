# Airline Inc fleet and supply

Fleet and supply owns aircraft, capacity, fuel availability, maintenance shops, staffing, and unit cost for Airline Inc. Capacity and input cost are supply facts. They are not the fare file and they do not store booked passenger quantity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `city_identity` | `city_id` | `sf:airline.geography.dim_city` `city_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:airline.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `geographic_entity_identity` | `geographic_entity_id` | `sf:airline.geography.dim_geographic_entity` `geographic_entity_id` |
| `hub_identity` | `hub_id` | `sf:airline.geography.dim_hub` `hub_id` |
| `route_identity` | `route_id` | `sf:airline.geography.dim_route` `route_id` |
| `competitor_identity` | `competitor_id` | `sf:airline.customer.dim_competitor` `competitor_id` |
| `cabin_identity` | `cabin_id` | `sf:airline.customer.dim_cabin` `cabin_id` |
| `event_identity` | `event_id` | `sf:airline.customer.dim_event` `event_id` |

## Numbered questions

## Delta Air Lines

### Q1 2026 (6)

For Delta Air Lines, are there constraints on sourcing jet fuel in Asia-Pacific or elsewhere?

- `airline.supply.fact_fuel_supply`: `fuel_region_id`, `constraint_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `available_quantity`, `shortage_flag`, `backup_plan_flag`
- `airline.fleet.dim_fuel_region`: `fuel_region_name`, `fuel_region_code`
- `airline.price.fact_yield_result`: `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `yield_amount`, `yield_change_rate`, `excluding_china_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (7)

For Delta Air Lines, what bounds back-half capacity growth, and is capacity being managed to earnings neutrality?

- `airline.supply.fact_capacity`: `capacity_change_rate`, `back_half_bound_rate`, `earnings_neutral_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `route_id`
- `airline.supply.fact_industry_capacity`: `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `industry_seat_quantity`, `change_rate`, `irrational_return_flag`, `cuts_after_summer_flag`
- `airline.price.fact_earnings_path`: `earnings_amount`, `neutral_to_capacity_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `matches_prior_quarter_flag`, `new_seasonality_flag`, `under_earned_flag`
- `airline.supply.fact_network_plan`: `fiscal_quarter_id`, `geographic_entity_id`, `plan_status_code`, `uses_last_year_weakness_flag`, `even_spread_flag`, `allocation_changed_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (8)

For Delta Air Lines, would a longer fuel shock change the fleet plan, including earlier retirements or exiting an aircraft type?

- `airline.supply.fact_retirement`: `aircraft_type_id`, `retirement_count`, `earlier_flag`, `exit_type_flag`, `few_retirements_flag`, `fiscal_quarter_id`
- `airline.supply.fact_fuel_cost`: `fuel_region_id`, `shock_duration_code`, `fiscal_quarter_id`, `unit_cost_amount`, `high_flag`, `price_to_restore_growth_amount`
- `airline.fleet.dim_aircraft_type`: `type_name`, `type_code`
- `airline.supply.fact_fuel_supply`: `fuel_region_id`, `backup_plan_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `available_quantity`, `shortage_flag`, `constraint_flag`
- `airline.price.fact_fuel_recapture`: `fiscal_quarter_id`, `geographic_entity_id`, `recapture_rate`, `accelerating_flag`, `full_recapture_flag`, `requires_competitor_cuts_flag`, `lag_versus_history_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (14)

For Delta Air Lines, how are lingering pilot-recovery costs fixed before peak summer, when the operation is tighter?

- `airline.supply.fact_labor_cost`: `cost_amount`, `fiscal_quarter_id`, `labor_group_id`, `accrual_in_outlook_flag`, `contract_ratified_flag`, `gap_to_peer_flag`
- `airline.supply.fact_staffing`: `recovery_cost_open_flag`, `operation_tighter_flag`, `fiscal_quarter_id`, `labor_group_id`, `headcount_quantity`, `overstaffed_flag`, `in_balance_flag`
- `airline.supply.fact_cost_opportunity`: `fiscal_quarter_id`, `opportunity_code`, `priority_rank`, `savings_amount`
- `airline.supply.fact_seasonal_capacity`: `peak_share_rate`, `summer_tight_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `more_even_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (4)

For Delta Air Lines, what mix benefit arrives in 2026 and 2027 as new aircraft are delivered?

- `airline.supply.fact_fleet_delivery`: `aircraft_type_id`, `fleet_family_id`, `mix_benefit_year_code`, `fiscal_quarter_id`, `manufacturer_id`, `delivery_count`, `ahead_of_plan_flag`
- `airline.price.fact_margin_bridge`: `fiscal_quarter_id`, `geographic_entity_id`, `merchandising_offer_id`, `effect_rate`, `initiative_code`, `long_term_flag`
- `airline.demand.fact_segment_mix`: `fiscal_quarter_id`, `customer_segment_id`, `cabin_id`, `loyalty_program_id`, `mix_rate`, `premium_over_main_flag`, `crossover_year_code`
- `airline.price.fact_unit_revenue`: `unit_revenue_amount`, `unit_revenue_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`, `pass_through_flag`
- `airline.price.fact_non_ticket_revenue`: `revenue_amount`, `fiscal_quarter_id`, `growth_rate`, `sustainable_flag`, `maintenance_flag`, `cargo_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (5)

For Delta Air Lines, how much of the unit-cost efficiency from growing into the workforce, fleet, and airports carries into next year?

- `airline.supply.fact_unit_cost`: `unit_cost_amount`, `carries_into_next_year_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `change_rate`, `ex_fuel_change_rate`, `ex_labor_change_rate`
- `airline.supply.fact_workforce_efficiency`: `efficiency_rate`, `airport_component_flag`, `fleet_component_flag`, `fiscal_quarter_id`, `remaining_runway_rate`
- `airline.supply.fact_staffing`: `recovery_cost_open_flag`, `fiscal_quarter_id`, `labor_group_id`, `headcount_quantity`, `overstaffed_flag`, `in_balance_flag`, `operation_tighter_flag`
- `airline.supply.fact_fleet_delivery`: `fleet_family_id`, `this_year_narrowbody_count`, `mix_benefit_year_code`, `fiscal_quarter_id`, `aircraft_type_id`, `manufacturer_id`, `delivery_count`
- `airline.supply.fact_gauge_plan`: `benefit_year_code`, `unit_cost_effect_rate`, `fiscal_quarter_id`, `aircraft_type_id`, `route_id`, `gauge_change_rate`
- `airline.fleet.dim_airport`: `airport_name`, `airport_code`, `city_id`

### Q3 2025 (12)

For Delta Air Lines, how is Atlantic capacity next year being spread more evenly?

- `airline.supply.fact_capacity`: `capacity_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `route_id`, `aircraft_type_id`, `seat_quantity`
- `airline.supply.fact_seasonal_capacity`: `more_even_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `peak_share_rate`, `summer_tight_flag`
- `airline.price.fact_earnings_path`: `new_seasonality_flag`, `neutral_to_capacity_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `earnings_amount`, `matches_prior_quarter_flag`, `under_earned_flag`
- `airline.geography.dim_geographic_entity`: `region_id`, `entity_name`, `entity_code`
- `airline.supply.fact_industry_capacity`: `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `industry_seat_quantity`, `change_rate`, `irrational_return_flag`, `cuts_after_summer_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (13)

For Delta Air Lines, are heavy-maintenance events higher or lower next year, and what inflation is showing up in maintenance and parts?

- `airline.supply.fact_maintenance_events`: `maintenance_shop_id`, `event_count`, `higher_next_year_flag`, `fiscal_quarter_id`, `real_deferral_flag`, `in_quarter_outlook_flag`
- `airline.supply.fact_parts_cost`: `maintenance_shop_id`, `inflation_rate`, `fiscal_quarter_id`, `cost_amount`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (16)

For Delta Air Lines, how is first-quarter network planning being set given last year's close-in corporate weakness?

- `airline.supply.fact_network_plan`: `fiscal_quarter_id`, `plan_status_code`, `uses_last_year_weakness_flag`, `geographic_entity_id`, `even_spread_flag`, `allocation_changed_flag`
- `airline.demand.fact_close_in_demand`: `fiscal_quarter_id`, `booking_window_id`, `close_in_passenger_count`, `weak_last_year_flag`, `premium_close_in_flag`, `geographic_entity_id`, `cabin_id`
- `airline.demand.fact_corporate_demand`: `fiscal_quarter_id`, `corporate_passenger_count`, `back_to_turn_of_year_flag`, `customer_segment_id`, `geographic_entity_id`, `city_id`, `industry_vertical_id`
- `airline.customer.dim_customer_segment`: `segment_name`, `segment_code`
- `airline.customer.dim_industry_vertical`: `vertical_name`, `vertical_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (21)

For Delta Air Lines, are domestic revenue trends different in hubs than in point-to-point leisure markets where competitor capacity is down?

- `airline.supply.fact_hub_capacity`: `fiscal_quarter_id`, `hub_id`, `constraint_type_id`, `airport_id`, `seat_quantity`, `rebuild_complete_flag`, `profit_versus_plan_rate`
- `airline.price.fact_system_margin`: `fiscal_quarter_id`, `hub_id`, `geographic_entity_id`, `margin_rate`, `run_for_system_flag`, `annual_improvement_rate`, `from_price_rate`
- `airline.demand.fact_leisure_demand`: `city_id`, `leisure_passenger_count`, `point_to_point_flag`, `domestic_trend_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `customer_segment_id`
- `airline.demand.fact_hub_demand`: `city_id`, `hub_versus_leisure_gap_rate`, `fiscal_quarter_id`, `hub_id`, `geographic_entity_id`, `passenger_count`, `non_hub_dilutive_flag`
- `airline.supply.fact_industry_capacity`: `competitor_id`, `fiscal_quarter_id`, `geographic_entity_id`, `industry_seat_quantity`, `change_rate`, `irrational_return_flag`, `cuts_after_summer_flag`
- `airline.supply.fact_competitor_schedule`: `competitor_id`, `city_id`, `competitor_seat_quantity`, `changes_domestic_view_flag`, `fiscal_quarter_id`, `hub_id`, `unprofitable_flag`

### Q4 2024 (5)

For Delta Air Lines, how quickly can higher fuel be recaptured compared with the historical lag?

- `airline.supply.fact_fuel_cost`: `fuel_region_id`, `high_flag`, `fiscal_quarter_id`, `unit_cost_amount`, `shock_duration_code`, `price_to_restore_growth_amount`
- `airline.supply.fact_fuel_supply`: `fuel_region_id`, `fiscal_quarter_id`, `geographic_entity_id`, `available_quantity`, `shortage_flag`, `constraint_flag`, `backup_plan_flag`
- `airline.price.fact_fare`: `fare_product_id`, `fare_amount`, `fare_change_rate`, `higher_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`
- `airline.demand.fact_elasticity_response`: `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `elastic_flag`, `response_rate`, `different_from_last_shock_flag`
- `airline.price.fact_yield_result`: `yield_amount`, `yield_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `excluding_china_flag`
- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`, `unit_revenue_amount`, `unit_revenue_change_rate`, `pass_through_flag`

### Q3 2024 (2)

For Delta Air Lines, how is domestic capacity being set as lower-cost airlines cut capacity?

- `airline.supply.fact_capacity`: `capacity_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `route_id`, `aircraft_type_id`, `seat_quantity`
- `airline.supply.fact_industry_capacity`: `competitor_id`, `fiscal_quarter_id`, `geographic_entity_id`, `industry_seat_quantity`, `change_rate`, `irrational_return_flag`, `cuts_after_summer_flag`
- `airline.customer.dim_competitor`: `competitor_name`, `competitor_code`
- `airline.geography.dim_geographic_entity`: `region_id`, `entity_name`, `entity_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2024 (3)

For Delta Air Lines, are the benefits of tighter industry capacity front-loaded for the airline that is not cutting?

- `airline.supply.fact_industry_capacity`: `industry_seat_quantity`, `front_loaded_benefit_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `change_rate`, `irrational_return_flag`
- `airline.price.fact_fuel_recapture`: `fiscal_quarter_id`, `geographic_entity_id`, `recapture_rate`, `accelerating_flag`, `full_recapture_flag`, `requires_competitor_cuts_flag`, `lag_versus_history_code`
- `airline.price.fact_yield_result`: `yield_amount`, `yield_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `excluding_china_flag`
- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`, `unit_revenue_amount`, `unit_revenue_change_rate`, `pass_through_flag`
- `airline.price.fact_revenue_premium`: `fiscal_quarter_id`, `competitor_id`, `geographic_entity_id`, `premium_rate`, `depth_available_rate`, `competitor_product_change_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

## United Airlines

### Q1 2026 (2)

For United Airlines, if fuel stays high for a long time, how does that change which hubs are run for system profit, including versus competitors?

- `airline.supply.fact_fuel_cost`: `fuel_region_id`, `unit_cost_amount`, `high_flag`, `fiscal_quarter_id`, `shock_duration_code`, `price_to_restore_growth_amount`
- `airline.supply.fact_fuel_supply`: `fuel_region_id`, `fiscal_quarter_id`, `geographic_entity_id`, `available_quantity`, `shortage_flag`, `constraint_flag`, `backup_plan_flag`
- `airline.supply.fact_hub_capacity`: `profit_versus_plan_rate`, `fiscal_quarter_id`, `hub_id`, `constraint_type_id`, `airport_id`, `seat_quantity`, `rebuild_complete_flag`
- `airline.price.fact_system_margin`: `margin_rate`, `run_for_system_flag`, `fiscal_quarter_id`, `hub_id`, `geographic_entity_id`, `annual_improvement_rate`, `from_price_rate`
- `airline.geography.dim_hub`: `city_id`, `hub_name`, `hub_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (4)

For United Airlines, what visibility is there on jet-fuel shortages in Asia or Europe, and what is the backup plan?

- `airline.supply.fact_fuel_supply`: `fuel_region_id`, `shortage_flag`, `backup_plan_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `available_quantity`, `constraint_flag`
- `airline.fleet.dim_fuel_region`: `fuel_region_name`, `fuel_region_code`
- `airline.demand.fact_passenger_flow`: `fiscal_quarter_id`, `route_id`, `geographic_entity_id`, `partner_id`, `event_id`, `flow_passenger_count`, `foreign_carrier_flag`
- `airline.geography.dim_region`: `region_name`, `region_code`
- `airline.price.fact_partnership_margin`: `europe_hub_fit_flag`, `fiscal_quarter_id`, `partner_id`, `geographic_entity_id`, `margin_rate`, `longer_term_change_rate`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (7)

For United Airlines, does cutting about five points of capacity create maintenance-cost leverage, or does maintenance stay lumpy?

- `airline.supply.fact_maintenance_cost`: `maintenance_shop_id`, `cost_amount`, `leverage_from_cut_flag`, `lumpy_flag`, `fiscal_quarter_id`, `labor_group_id`, `inflation_rate`
- `airline.supply.fact_capacity`: `capacity_change_rate`, `cut_points`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `route_id`, `aircraft_type_id`
- `airline.supply.fact_industry_capacity`: `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `industry_seat_quantity`, `change_rate`, `irrational_return_flag`, `cuts_after_summer_flag`
- `airline.supply.fact_network_plan`: `fiscal_quarter_id`, `geographic_entity_id`, `plan_status_code`, `uses_last_year_weakness_flag`, `even_spread_flag`, `allocation_changed_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (8)

For United Airlines, what fuel price would be required to put mid-single-digit capacity growth back in the second half, and how much irrational capacity could return?

- `airline.supply.fact_capacity`: `capacity_change_rate`, `back_half_bound_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `route_id`, `aircraft_type_id`
- `airline.supply.fact_industry_capacity`: `industry_seat_quantity`, `irrational_return_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `change_rate`, `cuts_after_summer_flag`
- `airline.supply.fact_fuel_cost`: `fuel_region_id`, `unit_cost_amount`, `price_to_restore_growth_amount`, `fiscal_quarter_id`, `high_flag`, `shock_duration_code`
- `airline.supply.fact_fuel_supply`: `fuel_region_id`, `fiscal_quarter_id`, `geographic_entity_id`, `available_quantity`, `shortage_flag`, `constraint_flag`, `backup_plan_flag`
- `airline.price.fact_fuel_recapture`: `fiscal_quarter_id`, `geographic_entity_id`, `recapture_rate`, `accelerating_flag`, `full_recapture_flag`, `requires_competitor_cuts_flag`, `lag_versus_history_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (4)

For United Airlines, what is keeping unit cost in check despite product investment, and what efficiencies remain for next year?

- `airline.supply.fact_unit_cost`: `unit_cost_amount`, `carries_into_next_year_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `change_rate`, `ex_fuel_change_rate`, `ex_labor_change_rate`
- `airline.supply.fact_workforce_efficiency`: `fiscal_quarter_id`, `efficiency_rate`, `remaining_runway_rate`, `airport_component_flag`, `fleet_component_flag`
- `airline.supply.fact_procurement_cost`: `cost_amount`, `product_investment_amount`, `keeping_unit_cost_in_check_flag`, `fiscal_quarter_id`, `savings_follow_through_flag`
- `airline.supply.fact_gauge_plan`: `benefit_year_code`, `unit_cost_effect_rate`, `fiscal_quarter_id`, `aircraft_type_id`, `route_id`, `gauge_change_rate`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (5)

For United Airlines, with a large narrow-body and wide-body delivery plan and few retirements, what guardrails limit capacity growth, and where in the network?

- `airline.supply.fact_fleet_delivery`: `aircraft_type_id`, `delivery_count`, `ahead_of_plan_flag`, `fiscal_quarter_id`, `manufacturer_id`, `fleet_family_id`, `this_year_narrowbody_count`
- `airline.supply.fact_retirement`: `aircraft_type_id`, `retirement_count`, `few_retirements_flag`, `fiscal_quarter_id`, `earlier_flag`, `exit_type_flag`
- `airline.fleet.dim_aircraft_type`: `type_name`, `type_code`
- `airline.supply.fact_capacity`: `aircraft_type_id`, `capacity_change_rate`, `guardrail_code`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `route_id`
- `airline.supply.fact_industry_capacity`: `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `industry_seat_quantity`, `change_rate`, `irrational_return_flag`, `cuts_after_summer_flag`
- `airline.supply.fact_network_plan`: `plan_status_code`, `fiscal_quarter_id`, `geographic_entity_id`, `uses_last_year_weakness_flag`, `even_spread_flag`, `allocation_changed_flag`

### Q4 2025 (7)

For United Airlines, which cost opportunities matter most next year: operation, procurement, or follow-through on this year's savings?

- `airline.supply.fact_unit_cost`: `unit_cost_amount`, `carries_into_next_year_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `change_rate`, `ex_fuel_change_rate`, `ex_labor_change_rate`
- `airline.supply.fact_workforce_efficiency`: `fiscal_quarter_id`, `efficiency_rate`, `remaining_runway_rate`, `airport_component_flag`, `fleet_component_flag`
- `airline.supply.fact_staffing`: `recovery_cost_open_flag`, `operation_tighter_flag`, `fiscal_quarter_id`, `labor_group_id`, `headcount_quantity`, `overstaffed_flag`, `in_balance_flag`
- `airline.supply.fact_cost_opportunity`: `savings_amount`, `fiscal_quarter_id`, `opportunity_code`, `priority_rank`
- `airline.supply.fact_procurement_cost`: `cost_amount`, `savings_follow_through_flag`, `keeping_unit_cost_in_check_flag`, `fiscal_quarter_id`, `product_investment_amount`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (10)

For United Airlines, does a competitor adding unprofitable Chicago flying change the view that domestic is the best geography next year?

- `airline.supply.fact_competitor_schedule`: `competitor_id`, `city_id`, `competitor_seat_quantity`, `unprofitable_flag`, `changes_domestic_view_flag`, `fiscal_quarter_id`, `hub_id`
- `airline.demand.fact_share_position`: `city_id`, `competitor_id`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `customer_segment_id`, `share_rate`
- `airline.price.fact_unit_revenue`: `unit_revenue_amount`, `unit_revenue_change_rate`, `intra_quarter_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`
- `airline.demand.fact_domestic_demand`: `best_geography_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `passenger_count`, `sequential_improvement_flag`
- `airline.supply.fact_industry_capacity`: `competitor_id`, `change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `industry_seat_quantity`, `irrational_return_flag`, `cuts_after_summer_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (12)

For United Airlines, excluding labor, is this year's unit-cost performance the right benchmark for next year?

- `airline.supply.fact_unit_cost`: `unit_cost_amount`, `ex_labor_change_rate`, `carries_into_next_year_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `change_rate`, `ex_fuel_change_rate`
- `airline.supply.fact_workforce_efficiency`: `fiscal_quarter_id`, `efficiency_rate`, `remaining_runway_rate`, `airport_component_flag`, `fleet_component_flag`
- `airline.supply.fact_labor_cost`: `labor_group_id`, `cost_amount`, `fiscal_quarter_id`, `accrual_in_outlook_flag`, `contract_ratified_flag`, `gap_to_peer_flag`
- `airline.supply.fact_gauge_plan`: `benefit_year_code`, `unit_cost_effect_rate`, `fiscal_quarter_id`, `aircraft_type_id`, `route_id`, `gauge_change_rate`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (14)

For United Airlines, how does capacity discipline persist as aircraft deliveries ramp?

- `airline.supply.fact_industry_capacity`: `industry_seat_quantity`, `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `change_rate`, `irrational_return_flag`, `cuts_after_summer_flag`
- `airline.price.fact_fuel_recapture`: `fiscal_quarter_id`, `geographic_entity_id`, `recapture_rate`, `accelerating_flag`, `full_recapture_flag`, `requires_competitor_cuts_flag`, `lag_versus_history_code`
- `airline.supply.fact_fleet_delivery`: `aircraft_type_id`, `fiscal_quarter_id`, `manufacturer_id`, `fleet_family_id`, `delivery_count`, `ahead_of_plan_flag`, `this_year_narrowbody_count`
- `airline.supply.fact_retirement`: `aircraft_type_id`, `fiscal_quarter_id`, `retirement_count`, `earlier_flag`, `exit_type_flag`, `few_retirements_flag`
- `airline.supply.fact_capacity`: `aircraft_type_id`, `capacity_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `route_id`, `seat_quantity`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (2)

For United Airlines, after maintenance shifts and the flight-attendant agreement, is fourth-quarter unit cost still near the second-quarter reference?

- `airline.supply.fact_unit_cost`: `fiscal_quarter_id`, `unit_cost_amount`, `ex_labor_change_rate`, `near_reference_quarter_flag`, `geographic_entity_id`, `change_rate`, `ex_fuel_change_rate`
- `airline.supply.fact_workforce_efficiency`: `fiscal_quarter_id`, `efficiency_rate`, `remaining_runway_rate`, `airport_component_flag`, `fleet_component_flag`
- `airline.supply.fact_maintenance_cost`: `fiscal_quarter_id`, `maintenance_shop_id`, `labor_group_id`, `cost_amount`, `leverage_from_cut_flag`, `lumpy_flag`, `inflation_rate`
- `airline.supply.fact_maintenance_events`: `fiscal_quarter_id`, `maintenance_shop_id`, `in_quarter_outlook_flag`, `event_count`, `higher_next_year_flag`, `real_deferral_flag`
- `airline.supply.fact_labor_cost`: `fiscal_quarter_id`, `labor_group_id`, `cost_amount`, `contract_ratified_flag`, `accrual_in_outlook_flag`, `gap_to_peer_flag`
- `airline.fleet.dim_labor_group`: `group_name`, `group_code`

### Q3 2025 (6)

For United Airlines, why grow so much in Latin America in the quarter if unit revenue did not support it?

- `airline.supply.fact_capacity`: `fiscal_quarter_id`, `capacity_change_rate`, `geographic_entity_id`, `hub_id`, `route_id`, `aircraft_type_id`, `seat_quantity`
- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `unit_revenue_amount`, `unit_revenue_change_rate`, `intra_quarter_change_rate`, `geographic_entity_id`, `cabin_id`, `route_id`
- `airline.price.fact_non_ticket_revenue`: `fiscal_quarter_id`, `revenue_amount`, `growth_rate`, `sustainable_flag`, `maintenance_flag`, `cargo_flag`
- `airline.price.fact_geographic_margin`: `fiscal_quarter_id`, `margin_rate`, `geographic_entity_id`, `contribution_to_long_term_rate`, `premium_versus_main_mix_rate`, `in_company_control_flag`
- `airline.price.fact_cabin_margin`: `fiscal_quarter_id`, `margin_rate`, `cabin_id`, `geographic_entity_id`, `gap_to_premium_rate`, `would_close_if_supply_cut_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (8)

For United Airlines, if unit cost rises a few percent a year, what revenue drivers produce about a point of annual margin expansion?

- `airline.supply.fact_unit_cost`: `unit_cost_amount`, `carries_into_next_year_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `change_rate`, `ex_fuel_change_rate`, `ex_labor_change_rate`
- `airline.supply.fact_workforce_efficiency`: `fiscal_quarter_id`, `efficiency_rate`, `remaining_runway_rate`, `airport_component_flag`, `fleet_component_flag`
- `airline.price.fact_unit_revenue`: `unit_revenue_amount`, `unit_revenue_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`, `pass_through_flag`
- `airline.price.fact_non_ticket_revenue`: `revenue_amount`, `fiscal_quarter_id`, `growth_rate`, `sustainable_flag`, `maintenance_flag`, `cargo_flag`
- `airline.price.fact_geographic_margin`: `margin_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `contribution_to_long_term_rate`, `premium_versus_main_mix_rate`, `in_company_control_flag`
- `airline.price.fact_cabin_margin`: `margin_rate`, `fiscal_quarter_id`, `cabin_id`, `geographic_entity_id`, `gap_to_premium_rate`, `would_close_if_supply_cut_flag`

### Q3 2025 (10)

For United Airlines, is the maintenance expense that moved a real deferral, and is a flight-attendant accrual in the fourth-quarter outlook?

- `airline.supply.fact_maintenance_cost`: `fiscal_quarter_id`, `maintenance_shop_id`, `labor_group_id`, `cost_amount`, `leverage_from_cut_flag`, `lumpy_flag`, `inflation_rate`
- `airline.supply.fact_maintenance_events`: `fiscal_quarter_id`, `maintenance_shop_id`, `real_deferral_flag`, `in_quarter_outlook_flag`, `event_count`, `higher_next_year_flag`
- `airline.supply.fact_labor_cost`: `fiscal_quarter_id`, `labor_group_id`, `accrual_in_outlook_flag`, `cost_amount`, `contract_ratified_flag`, `gap_to_peer_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (11)

For United Airlines, where does the mid-continent hub rebuild stand?

- `airline.supply.fact_hub_capacity`: `rebuild_complete_flag`, `fiscal_quarter_id`, `hub_id`, `constraint_type_id`, `airport_id`, `seat_quantity`, `profit_versus_plan_rate`
- `airline.geography.dim_hub`: `city_id`, `hub_name`, `hub_code`
- `airline.supply.fact_capacity`: `capacity_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `route_id`, `aircraft_type_id`, `seat_quantity`
- `airline.supply.fact_industry_capacity`: `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `industry_seat_quantity`, `change_rate`, `irrational_return_flag`, `cuts_after_summer_flag`
- `airline.price.fact_geographic_margin`: `margin_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `contribution_to_long_term_rate`, `premium_versus_main_mix_rate`, `in_company_control_flag`
- `airline.price.fact_cabin_margin`: `margin_rate`, `fiscal_quarter_id`, `cabin_id`, `geographic_entity_id`, `gap_to_premium_rate`, `would_close_if_supply_cut_flag`

### Q3 2025 (12)

For United Airlines, what factors decide whether another wide-body type is still too expensive to add?

- `airline.supply.fact_widebody_case`: `aircraft_type_id`, `too_expensive_flag`, `cost_versus_existing_rate`, `fiscal_quarter_id`
- `airline.fleet.dim_aircraft_type`: `type_name`, `type_code`
- `airline.supply.fact_unit_cost`: `unit_cost_amount`, `fiscal_quarter_id`, `geographic_entity_id`, `change_rate`, `ex_fuel_change_rate`, `ex_labor_change_rate`, `carries_into_next_year_flag`
- `airline.supply.fact_workforce_efficiency`: `fleet_component_flag`, `fiscal_quarter_id`, `efficiency_rate`, `remaining_runway_rate`, `airport_component_flag`
- `airline.supply.fact_gauge_plan`: `aircraft_type_id`, `unit_cost_effect_rate`, `fiscal_quarter_id`, `route_id`, `gauge_change_rate`, `benefit_year_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (13)

For United Airlines, are Airbus and Boeing deliveries now ahead of the original plan?

- `airline.supply.fact_fleet_delivery`: `aircraft_type_id`, `ahead_of_plan_flag`, `fiscal_quarter_id`, `manufacturer_id`, `fleet_family_id`, `delivery_count`, `this_year_narrowbody_count`
- `airline.supply.fact_retirement`: `aircraft_type_id`, `fiscal_quarter_id`, `retirement_count`, `earlier_flag`, `exit_type_flag`, `few_retirements_flag`
- `airline.fleet.dim_manufacturer`: `manufacturer_name`, `manufacturer_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (14)

For United Airlines, what range of outcomes from a government shutdown is already in the quarter's outlook?

- `airline.supply.fact_shutdown_case`: `fiscal_quarter_id`, `in_outlook_flag`, `event_id`, `geographic_entity_id`, `case_code`, `domestic_share_of_hit_rate`
- `airline.customer.dim_event`: `event_name`, `event_code`
- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `unit_revenue_amount`, `unit_revenue_change_rate`, `intra_quarter_change_rate`, `geographic_entity_id`, `cabin_id`, `route_id`
- `airline.price.fact_non_ticket_revenue`: `fiscal_quarter_id`, `revenue_amount`, `growth_rate`, `sustainable_flag`, `maintenance_flag`, `cargo_flag`
- `airline.price.fact_outlook_case`: `fiscal_quarter_id`, `geographic_entity_id`, `case_code`, `changed_flag`, `driver_code`, `upside_cabin_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (15)

For United Airlines, as more low-end capacity exits, how does the shorter booking window at discount carriers affect brand-loyal demand?

- `airline.supply.fact_industry_capacity`: `low_end_exit_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `industry_seat_quantity`, `change_rate`, `irrational_return_flag`
- `airline.demand.fact_booking_curve`: `booking_window_id`, `shorter_at_discounters_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `days_before_departure`, `booked_share_rate`
- `airline.customer.dim_booking_window`: `window_name`, `window_code`
- `airline.demand.fact_share_position`: `city_id`, `loyal_share_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `competitor_id`, `customer_segment_id`
- `airline.customer.dim_competitor`: `competitor_name`, `competitor_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (1)

For United Airlines, how should unit cost excluding fuel trend after a low-single-digit increase, including the distribution-expense item?

- `airline.supply.fact_unit_cost`: `unit_cost_amount`, `ex_fuel_change_rate`, `distribution_item_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `change_rate`, `ex_labor_change_rate`
- `airline.supply.fact_workforce_efficiency`: `fiscal_quarter_id`, `efficiency_rate`, `remaining_runway_rate`, `airport_component_flag`, `fleet_component_flag`
- `airline.supply.fact_procurement_cost`: `cost_amount`, `keeping_unit_cost_in_check_flag`, `fiscal_quarter_id`, `savings_follow_through_flag`, `product_investment_amount`
- `airline.supply.fact_gauge_plan`: `unit_cost_effect_rate`, `fiscal_quarter_id`, `aircraft_type_id`, `route_id`, `gauge_change_rate`, `benefit_year_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (5)

What would let United close the remaining gap with the competitor that has a different labor, hub, maintenance, and loyalty setup?

- `airline.supply.fact_labor_cost`: `labor_group_id`, `fiscal_quarter_id`, `cost_amount`, `accrual_in_outlook_flag`, `contract_ratified_flag`, `gap_to_peer_flag`
- `airline.fleet.dim_labor_group`: `group_name`, `group_code`
- `airline.supply.fact_hub_capacity`: `fiscal_quarter_id`, `hub_id`, `constraint_type_id`, `airport_id`, `seat_quantity`, `rebuild_complete_flag`, `profit_versus_plan_rate`
- `airline.price.fact_system_margin`: `margin_rate`, `fiscal_quarter_id`, `hub_id`, `geographic_entity_id`, `run_for_system_flag`, `annual_improvement_rate`, `from_price_rate`
- `airline.supply.fact_maintenance_cost`: `maintenance_shop_id`, `labor_group_id`, `fiscal_quarter_id`, `cost_amount`, `leverage_from_cut_flag`, `lumpy_flag`, `inflation_rate`
- `airline.supply.fact_maintenance_events`: `maintenance_shop_id`, `fiscal_quarter_id`, `event_count`, `higher_next_year_flag`, `real_deferral_flag`, `in_quarter_outlook_flag`

### Q2 2025 (7)

For United Airlines, why do industry capacity cuts keep showing up after peak summer rather than earlier?

- `airline.supply.fact_industry_capacity`: `industry_seat_quantity`, `cuts_after_summer_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `change_rate`, `irrational_return_flag`
- `airline.price.fact_fuel_recapture`: `requires_competitor_cuts_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `recapture_rate`, `accelerating_flag`, `full_recapture_flag`, `lag_versus_history_code`
- `airline.price.fact_earnings_path`: `new_seasonality_flag`, `neutral_to_capacity_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `earnings_amount`, `matches_prior_quarter_flag`, `under_earned_flag`
- `airline.supply.fact_seasonal_capacity`: `peak_share_rate`, `summer_tight_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `more_even_flag`
- `airline.supply.fact_capacity`: `capacity_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `route_id`, `aircraft_type_id`, `seat_quantity`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (10)

For United Airlines, what cadence of gauge benefit is expected over the next two years?

- `airline.supply.fact_gauge_plan`: `aircraft_type_id`, `gauge_change_rate`, `benefit_year_code`, `unit_cost_effect_rate`, `fiscal_quarter_id`, `route_id`
- `airline.fleet.dim_aircraft_type`: `type_name`, `type_code`
- `airline.price.fact_unit_revenue`: `unit_revenue_amount`, `unit_revenue_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`, `pass_through_flag`
- `airline.price.fact_non_ticket_revenue`: `revenue_amount`, `fiscal_quarter_id`, `growth_rate`, `sustainable_flag`, `maintenance_flag`, `cargo_flag`
- `airline.supply.fact_unit_cost`: `unit_cost_amount`, `carries_into_next_year_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `change_rate`, `ex_fuel_change_rate`, `ex_labor_change_rate`
- `airline.supply.fact_workforce_efficiency`: `fiscal_quarter_id`, `efficiency_rate`, `remaining_runway_rate`, `airport_component_flag`, `fleet_component_flag`

### Q2 2025 (12)

For United Airlines, are pilots now in balance with deliveries, or still overstaffed?

- `airline.supply.fact_pilot_balance`: `aircraft_type_id`, `pilot_count`, `in_balance_flag`, `overstaffed_flag`, `fiscal_quarter_id`, `labor_group_id`
- `airline.supply.fact_fleet_delivery`: `aircraft_type_id`, `fiscal_quarter_id`, `manufacturer_id`, `fleet_family_id`, `delivery_count`, `ahead_of_plan_flag`, `this_year_narrowbody_count`
- `airline.supply.fact_retirement`: `aircraft_type_id`, `fiscal_quarter_id`, `retirement_count`, `earlier_flag`, `exit_type_flag`, `few_retirements_flag`
- `airline.fleet.dim_manufacturer`: `manufacturer_name`, `manufacturer_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (13)

For United Airlines, what is being debated about returning Newark to a less restricted operating level after the cap?

- `airline.supply.fact_hub_capacity`: `less_restricted_under_debate_flag`, `fiscal_quarter_id`, `hub_id`, `constraint_type_id`, `airport_id`, `seat_quantity`, `rebuild_complete_flag`
- `airline.geography.dim_city`: `city_name`, `city_code`, `city_role_code`, `country_id`
- `airline.fleet.dim_constraint_type`: `constraint_name`, `constraint_code`
- `airline.fleet.dim_airport`: `city_id`, `airport_name`, `airport_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (14)

For United Airlines, how many long-range narrow-bodies arrive this year, and how soon do they fly internationally?

- `airline.supply.fact_fleet_delivery`: `fleet_family_id`, `this_year_narrowbody_count`, `international_entry_quarters`, `mix_benefit_year_code`, `fiscal_quarter_id`, `aircraft_type_id`, `manufacturer_id`
- `airline.fleet.dim_aircraft_type`: `type_name`, `type_code`
- `airline.price.fact_route_margin`: `route_id`, `fiscal_quarter_id`, `geographic_entity_id`, `margin_rate`, `premium_to_geography_flag`, `premium_lasts_quarters`
- `airline.geography.dim_route`: `route_name`, `route_code`, `international_flag`, `long_haul_flag`, `geographic_entity_id`, `hub_id`, `new_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`
