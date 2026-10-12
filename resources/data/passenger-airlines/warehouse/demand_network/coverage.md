# Airline Inc network demand

Network demand owns geographic entities, cabins, customers, and bookings for Airline Inc. Passenger counts, share, and booking curves are demand facts. They store quantities and rates, not a fare and not a seat price.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| — | — | This slice does not borrow an identity. |

## Numbered questions

## Delta Air Lines

### Q1 2026 (5)

For Delta Air Lines, where does further segmentation of the premium cabin stand, and what gates a launch?

- `airline.demand.fact_cabin_demand`: `cabin_id`, `customer_segment_id`, `fiscal_quarter_id`, `geographic_entity_id`, `passenger_count`, `demand_change_rate`, `holding_if_inelastic_flag`
- `airline.price.fact_cabin_margin`: `cabin_id`, `gap_to_premium_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `margin_rate`, `would_close_if_supply_cut_flag`
- `airline.customer.dim_cabin`: `cabin_name`, `cabin_code`
- `airline.demand.fact_segment_mix`: `customer_segment_id`, `cabin_id`, `premium_over_main_flag`, `fiscal_quarter_id`, `loyalty_program_id`, `mix_rate`, `crossover_year_code`
- `airline.price.dim_fare_product`: `cabin_id`, `product_name`, `product_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (11)

For Delta Air Lines, as corporate volume returns, can that be served without cutting basic-economy inventory?

- `airline.demand.fact_corporate_demand`: `city_id`, `corporate_passenger_count`, `back_to_turn_of_year_flag`, `fiscal_quarter_id`, `customer_segment_id`, `geographic_entity_id`, `industry_vertical_id`
- `airline.customer.dim_customer_segment`: `segment_name`, `segment_code`
- `airline.demand.fact_basic_economy_demand`: `can_serve_corporate_without_cut_flag`, `fiscal_quarter_id`, `cabin_id`, `customer_segment_id`, `passenger_count`
- `airline.supply.fact_basic_economy_inventory`: `main_cabin_down_rate`, `fiscal_quarter_id`, `cabin_id`, `geographic_entity_id`, `seat_quantity`, `cut_flag`
- `airline.supply.fact_capacity`: `capacity_change_rate`, `back_half_bound_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `route_id`, `aircraft_type_id`
- `airline.supply.fact_industry_capacity`: `change_rate`, `irrational_return_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `industry_seat_quantity`, `cuts_after_summer_flag`

### Q1 2026 (12)

For Delta Air Lines, where is corporate share still short of where it should be, by coast versus the interior?

- `airline.demand.fact_share_position`: `share_rate`, `loyal_share_rate`, `versus_coastal_rate`, `gap_to_target_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`
- `airline.demand.fact_corporate_demand`: `corporate_passenger_count`, `short_of_target_flag`, `fiscal_quarter_id`, `customer_segment_id`, `geographic_entity_id`, `city_id`, `industry_vertical_id`
- `airline.geography.dim_hub`: `city_id`, `hub_name`, `hub_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (15)

For Delta Air Lines, what is different about demand holding up despite higher fares versus last year's macro and geopolitical shock?

- `airline.demand.fact_booking_demand`: `versus_january_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `booking_window_id`, `booking_count`
- `airline.demand.fact_traffic_demand`: `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `passenger_count`, `traffic_change_rate`, `strength_from_bookings_flag`
- `airline.price.fact_fare`: `fare_product_id`, `fare_amount`, `fare_change_rate`, `higher_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`
- `airline.demand.fact_elasticity_response`: `different_from_last_shock_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `elastic_flag`, `response_rate`
- `airline.supply.fact_fuel_cost`: `fuel_region_id`, `high_flag`, `shock_duration_code`, `fiscal_quarter_id`, `unit_cost_amount`, `price_to_restore_growth_amount`
- `airline.supply.fact_fuel_supply`: `fuel_region_id`, `fiscal_quarter_id`, `geographic_entity_id`, `available_quantity`, `shortage_flag`, `constraint_flag`, `backup_plan_flag`

### Q1 2026 (16)

Is premium corporate strength a market trend or the result of Delta merchandising with corporate clients?

- `airline.demand.fact_corporate_demand`: `corporate_passenger_count`, `fiscal_quarter_id`, `customer_segment_id`, `geographic_entity_id`, `city_id`, `industry_vertical_id`, `hub_id`
- `airline.customer.dim_customer_segment`: `segment_name`, `segment_code`
- `airline.demand.fact_segment_mix`: `mix_rate`, `premium_over_main_flag`, `fiscal_quarter_id`, `customer_segment_id`, `cabin_id`, `loyalty_program_id`, `crossover_year_code`
- `airline.price.dim_merchandising_offer`: `offer_name`, `offer_code`
- `airline.price.fact_margin_bridge`: `merchandising_offer_id`, `effect_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `initiative_code`, `long_term_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (18)

For Delta Air Lines, where do international share opportunities sit as fuel rises, and were domestic and international price increases different?

- `airline.demand.fact_share_position`: `share_rate`, `loyal_share_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `city_id`, `competitor_id`
- `airline.demand.fact_passenger_flow`: `fiscal_quarter_id`, `route_id`, `geographic_entity_id`, `partner_id`, `event_id`, `flow_passenger_count`, `foreign_carrier_flag`
- `airline.price.fact_price_action`: `increase_rate`, `domestic_flag`, `international_flag`, `different_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `fare_product_id`
- `airline.price.fact_fare`: `domestic_international_gap_rate`, `fiscal_quarter_id`, `fare_product_id`, `geographic_entity_id`, `cabin_id`, `fare_amount`, `fare_change_rate`
- `airline.supply.fact_fuel_cost`: `fuel_region_id`, `unit_cost_amount`, `price_to_restore_growth_amount`, `fiscal_quarter_id`, `high_flag`, `shock_duration_code`
- `airline.supply.fact_fuel_supply`: `fuel_region_id`, `fiscal_quarter_id`, `geographic_entity_id`, `available_quantity`, `shortage_flag`, `constraint_flag`, `backup_plan_flag`

### Q3 2025 (2)

For Delta Air Lines, is corporate travel fully recovered once the prior-year disruption comparison is excluded?

- `airline.demand.fact_corporate_demand`: `corporate_passenger_count`, `recovered_flag`, `back_to_turn_of_year_flag`, `fiscal_quarter_id`, `customer_segment_id`, `geographic_entity_id`, `city_id`
- `airline.customer.dim_customer_segment`: `segment_name`, `segment_code`
- `airline.customer.dim_industry_vertical`: `vertical_name`, `vertical_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (6)

For Delta Air Lines, by how much are domestic main-cabin seats down, and how does that relate to main cabin turning positive?

- `airline.demand.fact_cabin_demand`: `cabin_id`, `positive_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `customer_segment_id`, `passenger_count`, `demand_change_rate`
- `airline.supply.fact_basic_economy_inventory`: `cabin_id`, `seat_quantity`, `main_cabin_down_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `cut_flag`
- `airline.supply.fact_capacity`: `seat_quantity`, `capacity_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `route_id`, `aircraft_type_id`
- `airline.supply.fact_industry_capacity`: `industry_seat_quantity`, `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `change_rate`, `irrational_return_flag`, `cuts_after_summer_flag`
- `airline.price.fact_unit_revenue`: `cabin_id`, `unit_revenue_amount`, `unit_revenue_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `route_id`, `pass_through_flag`
- `airline.price.fact_non_ticket_revenue`: `revenue_amount`, `fiscal_quarter_id`, `growth_rate`, `sustainable_flag`, `maintenance_flag`, `cargo_flag`

### Q3 2025 (8)

For Delta Air Lines, what share of premium revenue is corporate?

- `airline.demand.fact_cabin_demand`: `cabin_id`, `demand_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `customer_segment_id`, `passenger_count`, `holding_if_inelastic_flag`
- `airline.price.fact_cabin_margin`: `cabin_id`, `margin_rate`, `gap_to_premium_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `would_close_if_supply_cut_flag`
- `airline.demand.fact_corporate_demand`: `corporate_passenger_count`, `fiscal_quarter_id`, `customer_segment_id`, `geographic_entity_id`, `city_id`, `industry_vertical_id`, `hub_id`
- `airline.customer.dim_customer_segment`: `segment_name`, `segment_code`
- `airline.customer.dim_cabin`: `cabin_name`, `cabin_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (11)

For Delta Air Lines, why is Austin, a non-hub, no longer dilutive the way non-hub flying used to be?

- `airline.demand.fact_hub_demand`: `non_hub_dilutive_flag`, `fiscal_quarter_id`, `hub_id`, `city_id`, `geographic_entity_id`, `passenger_count`, `hub_versus_leisure_gap_rate`
- `airline.geography.dim_city`: `country_id`, `city_name`, `city_code`, `city_role_code`
- `airline.price.fact_unit_revenue`: `unit_revenue_amount`, `unit_revenue_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`, `pass_through_flag`
- `airline.price.fact_non_ticket_revenue`: `revenue_amount`, `fiscal_quarter_id`, `growth_rate`, `sustainable_flag`, `maintenance_flag`, `cargo_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (17)

For Delta Air Lines, does shoulder-season Transatlantic strength still hold without last year's currency tailwind?

- `airline.demand.fact_shoulder_demand`: `holding_without_currency_flag`, `season_code`, `fiscal_quarter_id`, `geographic_entity_id`, `booking_window_id`, `passenger_count`
- `airline.price.dim_currency`: `currency_name`, `currency_code`
- `airline.demand.fact_international_demand`: `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`, `passenger_count`, `premium_mix_rate`, `main_mix_rate`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (20)

Is the main-cabin improvement more flying or Delta taking share as industry capacity comes out?

- `airline.demand.fact_cabin_demand`: `cabin_id`, `fiscal_quarter_id`, `geographic_entity_id`, `customer_segment_id`, `passenger_count`, `demand_change_rate`, `holding_if_inelastic_flag`
- `airline.price.fact_cabin_margin`: `cabin_id`, `fiscal_quarter_id`, `geographic_entity_id`, `margin_rate`, `gap_to_premium_rate`, `would_close_if_supply_cut_flag`
- `airline.supply.fact_industry_capacity`: `industry_seat_quantity`, `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `change_rate`, `irrational_return_flag`, `cuts_after_summer_flag`
- `airline.price.fact_fuel_recapture`: `fiscal_quarter_id`, `geographic_entity_id`, `recapture_rate`, `accelerating_flag`, `full_recapture_flag`, `requires_competitor_cuts_flag`, `lag_versus_history_code`
- `airline.demand.fact_share_position`: `city_id`, `share_rate`, `loyal_share_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `competitor_id`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2024 (1)

For Delta Air Lines, which geographic entity improved the most versus the initial fourth-quarter expectation, and how does that change 2025 capacity allocation?

- `airline.demand.fact_domestic_demand`: `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `passenger_count`, `sequential_improvement_flag`, `best_geography_flag`
- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `geographic_entity_id`, `unit_revenue_change_rate`, `intra_quarter_change_rate`, `cabin_id`, `route_id`, `unit_revenue_amount`
- `airline.supply.fact_capacity`: `fiscal_quarter_id`, `geographic_entity_id`, `capacity_change_rate`, `hub_id`, `route_id`, `aircraft_type_id`, `seat_quantity`
- `airline.price.fact_yield_result`: `fiscal_quarter_id`, `geographic_entity_id`, `yield_change_rate`, `cabin_id`, `customer_segment_id`, `yield_amount`, `excluding_china_flag`
- `airline.demand.fact_passenger_flow`: `fiscal_quarter_id`, `geographic_entity_id`, `anti_tourism_effect_flag`, `route_id`, `partner_id`, `event_id`, `flow_passenger_count`
- `airline.geography.dim_geographic_entity`: `entity_name`, `entity_code`, `region_id`

### Q4 2024 (4)

For Delta Air Lines, how do business and leisure, and older versus younger travelers, differ right now?

- `airline.demand.fact_cohort_demand`: `age_cohort_id`, `business_flag`, `fiscal_quarter_id`, `customer_segment_id`, `passenger_count`
- `airline.demand.fact_corporate_demand`: `fiscal_quarter_id`, `customer_segment_id`, `geographic_entity_id`, `city_id`, `industry_vertical_id`, `hub_id`, `corporate_passenger_count`
- `airline.demand.fact_leisure_demand`: `leisure_passenger_count`, `fiscal_quarter_id`, `geographic_entity_id`, `city_id`, `customer_segment_id`, `point_to_point_flag`, `domestic_trend_rate`
- `airline.customer.dim_customer_segment`: `segment_name`, `segment_code`
- `airline.customer.dim_age_cohort`: `cohort_name`, `cohort_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2024 (1)

For Delta Air Lines, how is the election period being separated from the underlying domestic and short-haul Latin demand trend?

- `airline.demand.fact_domestic_demand`: `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `passenger_count`, `sequential_improvement_flag`, `best_geography_flag`
- `airline.demand.fact_event_demand`: `separated_from_trend_flag`, `fiscal_quarter_id`, `event_id`, `geographic_entity_id`, `event_passenger_count`, `in_guide_flag`, `tailwind_size_code`
- `airline.geography.dim_geographic_entity`: `region_id`, `entity_name`, `entity_code`
- `airline.customer.dim_event`: `event_name`, `event_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2024 (4)

For Delta Air Lines, what corporate recovery is expected next year?

- `airline.demand.fact_corporate_demand`: `corporate_passenger_count`, `back_to_turn_of_year_flag`, `fiscal_quarter_id`, `customer_segment_id`, `geographic_entity_id`, `city_id`, `industry_vertical_id`
- `airline.customer.dim_customer_segment`: `segment_name`, `segment_code`
- `airline.customer.dim_industry_vertical`: `vertical_name`, `vertical_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

## United Airlines

### Q1 2026 (1)

Could a larger brand that captures passengers now flying foreign competitors include a United hub in Europe, and how do Star Alliance partners fit?

- `airline.demand.fact_share_position`: `competitor_id`, `share_rate`, `loyal_share_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `city_id`
- `airline.demand.fact_passenger_flow`: `partner_id`, `flow_passenger_count`, `foreign_carrier_flag`, `fiscal_quarter_id`, `route_id`, `geographic_entity_id`, `event_id`
- `airline.price.fact_partnership_margin`: `partner_id`, `europe_hub_fit_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `margin_rate`, `longer_term_change_rate`
- `airline.geography.dim_hub`: `city_id`, `hub_name`, `hub_code`
- `airline.customer.dim_partner`: `partner_name`, `partner_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (3)

For United Airlines, in a high-fare scenario, how would premium and business traffic hold up if demand is usually inelastic?

- `airline.demand.fact_cabin_demand`: `demand_change_rate`, `holding_if_inelastic_flag`, `fiscal_quarter_id`, `cabin_id`, `geographic_entity_id`, `customer_segment_id`, `passenger_count`
- `airline.demand.fact_elasticity_response`: `elastic_flag`, `different_from_last_shock_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `response_rate`
- `airline.demand.fact_corporate_demand`: `fiscal_quarter_id`, `customer_segment_id`, `geographic_entity_id`, `city_id`, `industry_vertical_id`, `hub_id`, `corporate_passenger_count`
- `airline.price.fact_fare`: `fare_product_id`, `fare_amount`, `fare_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `higher_flag`
- `airline.customer.dim_cabin`: `cabin_name`, `cabin_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (5)

For United Airlines, is there a structural share opportunity on the Atlantic or longer haul while Middle East carriers are disrupted, or will they be aggressive when they return?

- `airline.demand.fact_share_position`: `share_rate`, `loyal_share_rate`, `opportunity_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `city_id`
- `airline.demand.fact_passenger_flow`: `foreign_carrier_flag`, `anti_tourism_effect_flag`, `fiscal_quarter_id`, `route_id`, `geographic_entity_id`, `partner_id`, `event_id`
- `airline.customer.dim_competitor`: `competitor_name`, `competitor_code`
- `airline.geography.dim_geographic_entity`: `region_id`, `entity_name`, `entity_code`
- `airline.geography.dim_route`: `long_haul_flag`, `geographic_entity_id`, `hub_id`, `route_name`, `route_code`, `international_flag`, `new_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (6)

For United Airlines, how is brand-loyal share at Chicago O'Hare holding up versus the competitor under a proposed summer operations cap?

- `airline.demand.fact_share_position`: `city_id`, `competitor_id`, `share_rate`, `loyal_share_rate`, `versus_coastal_rate`, `fiscal_quarter_id`, `geographic_entity_id`
- `airline.supply.fact_competitor_schedule`: `competitor_id`, `city_id`, `competitor_seat_quantity`, `cap_proposed_flag`, `fiscal_quarter_id`, `hub_id`, `unprofitable_flag`
- `airline.geography.dim_hub`: `city_id`, `hub_name`, `hub_code`
- `airline.supply.fact_hub_capacity`: `profit_versus_plan_rate`, `less_restricted_under_debate_flag`, `fiscal_quarter_id`, `hub_id`, `constraint_type_id`, `airport_id`, `seat_quantity`
- `airline.geography.dim_city`: `city_name`, `city_code`, `city_role_code`, `country_id`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (1)

For United Airlines, what would turn the main cabin positive, and is a specific rate of change assumed?

- `airline.demand.fact_cabin_demand`: `cabin_id`, `demand_change_rate`, `positive_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `customer_segment_id`, `passenger_count`
- `airline.price.fact_cabin_margin`: `cabin_id`, `margin_rate`, `gap_to_premium_rate`, `would_close_if_supply_cut_flag`, `fiscal_quarter_id`, `geographic_entity_id`
- `airline.price.fact_yield_result`: `cabin_id`, `yield_amount`, `yield_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `customer_segment_id`, `excluding_china_flag`
- `airline.price.fact_unit_revenue`: `cabin_id`, `unit_revenue_amount`, `unit_revenue_change_rate`, `intra_quarter_change_rate`, `path_to_flat_rate`, `sequential_step_rate`, `fiscal_quarter_id`
- `airline.demand.fact_booking_demand`: `cabin_id`, `fiscal_quarter_id`, `geographic_entity_id`, `customer_segment_id`, `booking_window_id`, `booking_count`, `on_books_flag`
- `airline.demand.fact_traffic_demand`: `cabin_id`, `traffic_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `customer_segment_id`, `passenger_count`, `strength_from_bookings_flag`

### Q4 2025 (9)

For United Airlines, if industry revenue was flat versus the economy, what does that imply for broader industry growth?

- `airline.demand.fact_industry_context`: `industry_growth_rate`, `versus_gdp_rate`, `flat_versus_economy_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `above_pre_pandemic_flag`
- `airline.price.fact_unit_revenue`: `unit_revenue_amount`, `unit_revenue_change_rate`, `path_to_flat_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`
- `airline.supply.fact_capacity`: `capacity_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `route_id`, `aircraft_type_id`, `seat_quantity`
- `airline.supply.fact_industry_capacity`: `industry_seat_quantity`, `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `change_rate`, `irrational_return_flag`, `cuts_after_summer_flag`
- `airline.supply.fact_network_plan`: `even_spread_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `plan_status_code`, `uses_last_year_weakness_flag`, `allocation_changed_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (13)

For United Airlines, is a World Cup demand tailwind in the outlook, and how large could it be?

- `airline.demand.fact_booking_demand`: `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `booking_window_id`, `booking_count`, `on_books_flag`
- `airline.demand.fact_traffic_demand`: `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `passenger_count`, `traffic_change_rate`, `strength_from_bookings_flag`
- `airline.demand.fact_event_demand`: `event_id`, `event_passenger_count`, `tailwind_size_code`, `fiscal_quarter_id`, `geographic_entity_id`, `in_guide_flag`, `separated_from_trend_flag`
- `airline.customer.dim_event`: `event_name`, `event_code`
- `airline.supply.fact_capacity`: `capacity_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `route_id`, `aircraft_type_id`, `seat_quantity`
- `airline.supply.fact_industry_capacity`: `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `industry_seat_quantity`, `change_rate`, `irrational_return_flag`, `cuts_after_summer_flag`

### Q3 2025 (1)

For United Airlines, if main-cabin supply were cut in a step, would main-cabin margins close the gap with premium?

- `airline.demand.fact_cabin_demand`: `cabin_id`, `fiscal_quarter_id`, `geographic_entity_id`, `customer_segment_id`, `passenger_count`, `demand_change_rate`, `holding_if_inelastic_flag`
- `airline.price.fact_cabin_margin`: `cabin_id`, `margin_rate`, `gap_to_premium_rate`, `would_close_if_supply_cut_flag`, `fiscal_quarter_id`, `geographic_entity_id`
- `airline.supply.fact_industry_capacity`: `industry_seat_quantity`, `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `change_rate`, `irrational_return_flag`, `cuts_after_summer_flag`
- `airline.price.fact_fuel_recapture`: `fiscal_quarter_id`, `geographic_entity_id`, `recapture_rate`, `accelerating_flag`, `full_recapture_flag`, `requires_competitor_cuts_flag`, `lag_versus_history_code`
- `airline.price.fact_geographic_margin`: `margin_rate`, `premium_versus_main_mix_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `contribution_to_long_term_rate`, `in_company_control_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (4)

For United Airlines, can the industry revenue relationship to the economy exceed the pre-pandemic pattern?

- `airline.demand.fact_industry_context`: `industry_growth_rate`, `above_pre_pandemic_flag`, `flat_versus_economy_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `versus_gdp_rate`
- `airline.price.fact_unit_revenue`: `unit_revenue_amount`, `unit_revenue_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`, `pass_through_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (9)

For United Airlines, how much of a head start do fourth-quarter bookings and advanced yields have, including the Atlantic?

- `airline.demand.fact_booking_demand`: `fiscal_quarter_id`, `booking_window_id`, `booking_count`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `on_books_flag`
- `airline.demand.fact_booking_curve`: `fiscal_quarter_id`, `booking_window_id`, `geographic_entity_id`, `competitor_id`, `days_before_departure`, `booked_share_rate`, `close_in_weak_flag`
- `airline.price.fact_advanced_yield`: `fiscal_quarter_id`, `booking_window_id`, `advanced_yield_amount`, `head_start_rate`, `atlantic_flag`, `geographic_entity_id`
- `airline.customer.dim_booking_window`: `window_name`, `window_code`
- `airline.demand.fact_shoulder_demand`: `fiscal_quarter_id`, `booking_window_id`, `geographic_entity_id`, `passenger_count`, `holding_without_currency_flag`, `season_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (2)

For United Airlines, is demand back to the January level after the Newark recovery, or only on the way?

- `airline.demand.fact_booking_demand`: `booking_window_id`, `booking_count`, `versus_january_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`
- `airline.demand.fact_traffic_demand`: `strength_from_bookings_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `passenger_count`, `traffic_change_rate`
- `airline.demand.fact_disruption_demand`: `fiscal_quarter_id`, `city_id`, `event_id`, `geographic_entity_id`, `passenger_count`, `recovered_flag`, `system_share_of_improvement_rate`
- `airline.supply.fact_hub_capacity`: `fiscal_quarter_id`, `hub_id`, `constraint_type_id`, `airport_id`, `seat_quantity`, `rebuild_complete_flag`, `profit_versus_plan_rate`
- `airline.demand.fact_booking_curve`: `booking_window_id`, `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `days_before_departure`, `booked_share_rate`, `close_in_weak_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (3)

For United Airlines, what changed from the stable case to the lower second-half outlook?

- `airline.demand.fact_booking_demand`: `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `booking_window_id`, `booking_count`, `on_books_flag`
- `airline.demand.fact_traffic_demand`: `traffic_change_rate`, `strength_from_bookings_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `passenger_count`
- `airline.price.fact_outlook_case`: `case_code`, `changed_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `driver_code`, `upside_cabin_code`
- `airline.supply.fact_shutdown_case`: `case_code`, `in_outlook_flag`, `fiscal_quarter_id`, `event_id`, `geographic_entity_id`, `domestic_share_of_hit_rate`
- `airline.demand.fact_disruption_demand`: `fiscal_quarter_id`, `city_id`, `event_id`, `geographic_entity_id`, `passenger_count`, `recovered_flag`, `system_share_of_improvement_rate`
- `airline.supply.fact_hub_capacity`: `fiscal_quarter_id`, `hub_id`, `constraint_type_id`, `airport_id`, `seat_quantity`, `rebuild_complete_flag`, `profit_versus_plan_rate`

### Q2 2025 (6)

For United Airlines, which geographies or industries are driving the summer corporate acceleration, and are bookings back to the prior turn-of-year level?

- `airline.demand.fact_corporate_demand`: `industry_vertical_id`, `corporate_passenger_count`, `acceleration_flag`, `back_to_turn_of_year_flag`, `fiscal_quarter_id`, `customer_segment_id`, `geographic_entity_id`
- `airline.customer.dim_customer_segment`: `segment_name`, `segment_code`
- `airline.geography.dim_geographic_entity`: `region_id`, `entity_name`, `entity_code`
- `airline.customer.dim_industry_vertical`: `vertical_name`, `vertical_code`
- `airline.geography.dim_city`: `country_id`, `city_name`, `city_code`, `city_role_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (8)

For United Airlines, how much of the booking improvement is Newark versus the broader system, and is the fourth-quarter unit-revenue gain domestic or international?

- `airline.demand.fact_disruption_demand`: `fiscal_quarter_id`, `system_share_of_improvement_rate`, `city_id`, `event_id`, `geographic_entity_id`, `passenger_count`, `recovered_flag`
- `airline.supply.fact_hub_capacity`: `fiscal_quarter_id`, `profit_versus_plan_rate`, `hub_id`, `constraint_type_id`, `airport_id`, `seat_quantity`, `rebuild_complete_flag`
- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `unit_revenue_amount`, `unit_revenue_change_rate`, `intra_quarter_change_rate`, `geographic_entity_id`, `cabin_id`, `route_id`
- `airline.demand.fact_domestic_demand`: `fiscal_quarter_id`, `sequential_improvement_flag`, `geographic_entity_id`, `hub_id`, `passenger_count`, `best_geography_flag`
- `airline.demand.fact_international_demand`: `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`, `passenger_count`, `premium_mix_rate`, `main_mix_rate`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (15)

For United Airlines, is anti-tourism in some European cities changing passenger flows?

- `airline.demand.fact_passenger_flow`: `flow_passenger_count`, `anti_tourism_effect_flag`, `fiscal_quarter_id`, `route_id`, `geographic_entity_id`, `partner_id`, `event_id`
- `airline.customer.dim_event`: `event_name`, `event_code`
- `airline.customer.dim_partner`: `partner_name`, `partner_code`
- `airline.geography.dim_region`: `region_name`, `region_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`
