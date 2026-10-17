# Airline Inc price and yield

Price and yield owns fares, bag fees, unit revenue, cabin and geographic margin, fuel recapture, and loyalty economics for Airline Inc. A price row does not store passenger quantity or seat quantity. Fuel gallons and unit cost stay on the supply facts.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `cabin_identity` | `cabin_id` | `sf:airline.customer.dim_cabin` `cabin_id` |
| `loyalty_program_identity` | `loyalty_program_id` | `sf:airline.customer.dim_loyalty_program` `loyalty_program_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:airline.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `geographic_entity_identity` | `geographic_entity_id` | `sf:airline.geography.dim_geographic_entity` `geographic_entity_id` |
| `route_identity` | `route_id` | `sf:airline.geography.dim_route` `route_id` |
| `customer_segment_identity` | `customer_segment_id` | `sf:airline.customer.dim_customer_segment` `customer_segment_id` |
| `hub_identity` | `hub_id` | `sf:airline.geography.dim_hub` `hub_id` |
| `competitor_identity` | `competitor_id` | `sf:airline.customer.dim_competitor` `competitor_id` |
| `partner_identity` | `partner_id` | `sf:airline.customer.dim_partner` `partner_id` |
| `booking_window_identity` | `booking_window_id` | `sf:airline.customer.dim_booking_window` `booking_window_id` |

## Numbered questions

## Delta Air Lines

### Q1 2026 (1)

For Delta Air Lines, does the mid-teens revenue outlook reflect bookings already on the books, or an assumption that higher fares and bag fees accelerate later in the quarter?

- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `unit_revenue_amount`, `unit_revenue_change_rate`, `intra_quarter_change_rate`, `path_to_flat_rate`, `sequential_step_rate`, `geographic_entity_id`
- `airline.price.fact_non_ticket_revenue`: `fiscal_quarter_id`, `revenue_amount`, `growth_rate`, `sustainable_flag`, `maintenance_flag`, `cargo_flag`
- `airline.price.fact_fare`: `fiscal_quarter_id`, `fare_product_id`, `fare_amount`, `fare_change_rate`, `higher_flag`, `domestic_international_gap_rate`, `geographic_entity_id`
- `airline.demand.fact_elasticity_response`: `fiscal_quarter_id`, `response_rate`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `elastic_flag`, `different_from_last_shock_flag`
- `airline.price.fact_ancillary_fee`: `fiscal_quarter_id`, `fee_change_rate`, `in_outlook_flag`, `fee_type_id`, `geographic_entity_id`, `fee_amount`
- `airline.price.dim_fee_type`: `fee_name`, `fee_code`

### Q1 2026 (2)

For Delta Air Lines, how does second-quarter unit revenue differ across the four geographic entities in demand and in the ability to pass through higher costs?

- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `geographic_entity_id`, `unit_revenue_amount`, `unit_revenue_change_rate`, `pass_through_flag`, `intra_quarter_change_rate`, `cabin_id`
- `airline.price.fact_non_ticket_revenue`: `fiscal_quarter_id`, `revenue_amount`, `growth_rate`, `sustainable_flag`, `maintenance_flag`, `cargo_flag`
- `airline.demand.fact_domestic_demand`: `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `passenger_count`, `sequential_improvement_flag`, `best_geography_flag`
- `airline.supply.fact_capacity`: `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `route_id`, `aircraft_type_id`, `seat_quantity`, `capacity_change_rate`
- `airline.price.fact_yield_result`: `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `yield_amount`, `yield_change_rate`, `excluding_china_flag`
- `airline.demand.fact_passenger_flow`: `fiscal_quarter_id`, `geographic_entity_id`, `anti_tourism_effect_flag`, `route_id`, `partner_id`, `event_id`, `flow_passenger_count`

### Q1 2026 (3)

For Delta Air Lines, where has demand been more elastic to higher fares, by geography, customer, or cabin?

- `airline.price.fact_yield_result`: `cabin_id`, `customer_segment_id`, `yield_amount`, `yield_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `excluding_china_flag`
- `airline.price.fact_unit_revenue`: `cabin_id`, `fiscal_quarter_id`, `geographic_entity_id`, `route_id`, `unit_revenue_amount`, `unit_revenue_change_rate`, `pass_through_flag`
- `airline.demand.fact_corporate_demand`: `customer_segment_id`, `fiscal_quarter_id`, `geographic_entity_id`, `city_id`, `industry_vertical_id`, `hub_id`, `corporate_passenger_count`
- `airline.geography.dim_geographic_entity`: `region_id`, `entity_name`, `entity_code`
- `airline.demand.fact_elasticity_response`: `cabin_id`, `customer_segment_id`, `elastic_flag`, `different_from_last_shock_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `response_rate`
- `airline.customer.dim_customer_segment`: `segment_name`, `segment_code`

### Q1 2026 (4)

For Delta Air Lines, how are international margins and the premium-versus-main mix inside international expected to evolve?

- `airline.price.fact_geographic_margin`: `margin_rate`, `premium_versus_main_mix_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `contribution_to_long_term_rate`, `in_company_control_flag`
- `airline.demand.fact_international_demand`: `cabin_id`, `premium_mix_rate`, `main_mix_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `route_id`, `passenger_count`
- `airline.demand.fact_cabin_demand`: `cabin_id`, `fiscal_quarter_id`, `geographic_entity_id`, `customer_segment_id`, `passenger_count`, `demand_change_rate`, `holding_if_inelastic_flag`
- `airline.price.fact_cabin_margin`: `cabin_id`, `margin_rate`, `gap_to_premium_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `would_close_if_supply_cut_flag`
- `airline.customer.dim_cabin`: `cabin_name`, `cabin_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (9)

For Delta Air Lines, is Pacific yield, excluding China, improving as long-haul flows avoid the Middle East, including close-in premium?

- `airline.price.fact_yield_result`: `cabin_id`, `yield_amount`, `yield_change_rate`, `excluding_china_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `customer_segment_id`
- `airline.demand.fact_passenger_flow`: `flow_passenger_count`, `fiscal_quarter_id`, `route_id`, `geographic_entity_id`, `partner_id`, `event_id`, `foreign_carrier_flag`
- `airline.demand.fact_cabin_demand`: `cabin_id`, `fiscal_quarter_id`, `geographic_entity_id`, `customer_segment_id`, `passenger_count`, `demand_change_rate`, `holding_if_inelastic_flag`
- `airline.price.fact_cabin_margin`: `cabin_id`, `gap_to_premium_rate`, `would_close_if_supply_cut_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `margin_rate`
- `airline.geography.dim_geographic_entity`: `region_id`, `entity_name`, `entity_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (10)

What is driving maintenance-revenue growth, and how much of Delta's own engine work is done in-house?

- `airline.price.fact_non_ticket_revenue`: `revenue_amount`, `growth_rate`, `maintenance_flag`, `fiscal_quarter_id`, `sustainable_flag`, `cargo_flag`
- `airline.supply.fact_shop_capacity`: `maintenance_shop_id`, `capacity_quantity`, `in_house_share_rate`, `fiscal_quarter_id`, `added_recently_flag`
- `airline.supply.fact_engine_insource`: `maintenance_shop_id`, `in_house_share_rate`, `third_party_growth_rate`, `fiscal_quarter_id`
- `airline.fleet.dim_maintenance_shop`: `shop_name`, `shop_code`, `in_house_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (13)

For Delta Air Lines, does fuel recapture keep accelerating in the back half if fuel stays high?

- `airline.price.fact_fuel_recapture`: `recapture_rate`, `accelerating_flag`, `full_recapture_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `requires_competitor_cuts_flag`, `lag_versus_history_code`
- `airline.supply.fact_fuel_cost`: `fuel_region_id`, `high_flag`, `fiscal_quarter_id`, `unit_cost_amount`, `shock_duration_code`, `price_to_restore_growth_amount`
- `airline.price.fact_fare`: `fare_product_id`, `fare_amount`, `fare_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `higher_flag`
- `airline.demand.fact_elasticity_response`: `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `elastic_flag`, `response_rate`, `different_from_last_shock_flag`
- `airline.supply.fact_capacity`: `capacity_change_rate`, `back_half_bound_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `route_id`, `aircraft_type_id`
- `airline.supply.fact_industry_capacity`: `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `industry_seat_quantity`, `change_rate`, `irrational_return_flag`, `cuts_after_summer_flag`

### Q1 2026 (17)

For Delta Air Lines, how much of demand strength is customers accepting higher fares versus more bookings?

- `airline.price.fact_fare`: `fare_product_id`, `fare_amount`, `fare_change_rate`, `higher_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`
- `airline.demand.fact_elasticity_response`: `customer_segment_id`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `elastic_flag`, `response_rate`, `different_from_last_shock_flag`
- `airline.demand.fact_booking_demand`: `customer_segment_id`, `booking_window_id`, `booking_count`, `versus_january_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`
- `airline.demand.fact_booking_curve`: `booking_window_id`, `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `days_before_departure`, `booked_share_rate`, `close_in_weak_flag`
- `airline.demand.fact_traffic_demand`: `customer_segment_id`, `strength_from_bookings_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `passenger_count`, `traffic_change_rate`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (19)

For Delta Air Lines, how does brand-loyal share in focus cities compare with the coastal hubs?

- `airline.price.fact_cobrand_economics`: `loyalty_program_id`, `fiscal_quarter_id`, `card_program_id`, `partner_id`, `spend_growth_rate`, `sustainable_flag`, `partner_economics_amount`
- `airline.customer.dim_loyalty_program`: `program_name`, `program_code`
- `airline.demand.fact_share_position`: `share_rate`, `loyal_share_rate`, `versus_coastal_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `city_id`
- `airline.geography.dim_city`: `country_id`, `city_name`, `city_code`, `city_role_code`
- `airline.geography.dim_hub`: `city_id`, `hub_name`, `hub_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (1)

For Delta Air Lines, how much of the cash-flow improvement is the booking curve normalizing?

- `airline.price.fact_cash_position`: `cash_flow_amount`, `improvement_from_curve_rate`, `working_capital_amount`, `fiscal_quarter_id`, `geographic_entity_id`
- `airline.demand.fact_booking_curve`: `booking_window_id`, `holiday_curve_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `days_before_departure`, `booked_share_rate`
- `airline.demand.fact_booking_demand`: `booking_window_id`, `booking_count`, `curve_normalized_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`
- `airline.demand.fact_traffic_demand`: `strength_from_bookings_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`, `passenger_count`, `traffic_change_rate`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (3)

For Delta Air Lines, how much of the domestic improvement is unique to higher-income exposure?

- `airline.price.fact_unit_revenue`: `unit_revenue_amount`, `unit_revenue_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`, `pass_through_flag`
- `airline.demand.fact_domestic_demand`: `sequential_improvement_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `passenger_count`, `best_geography_flag`
- `airline.demand.fact_income_demand`: `customer_segment_id`, `higher_income_share_rate`, `unique_to_income_flag`, `fiscal_quarter_id`, `geographic_entity_id`
- `airline.customer.dim_customer_segment`: `segment_name`, `segment_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (7)

For Delta Air Lines, how much premium growth is a change in loyalty-member behavior rather than oil and the consumer backdrop?

- `airline.price.fact_unit_revenue`: `unit_revenue_amount`, `unit_revenue_change_rate`, `intra_quarter_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`
- `airline.demand.fact_segment_mix`: `loyalty_program_id`, `premium_over_main_flag`, `behavior_change_flag`, `fiscal_quarter_id`, `customer_segment_id`, `cabin_id`, `mix_rate`
- `airline.customer.dim_loyalty_program`: `program_name`, `program_code`
- `airline.customer.dim_cabin`: `cabin_name`, `cabin_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (9)

For Delta Air Lines, why would premium overtaking the main cabin slip past next year if 2027 was the prior marker?

- `airline.price.fact_unit_revenue`: `cabin_id`, `unit_revenue_amount`, `unit_revenue_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `route_id`, `pass_through_flag`
- `airline.demand.fact_segment_mix`: `cabin_id`, `premium_over_main_flag`, `crossover_year_code`, `fiscal_quarter_id`, `customer_segment_id`, `loyalty_program_id`, `mix_rate`
- `airline.price.fact_cabin_margin`: `cabin_id`, `gap_to_premium_rate`, `would_close_if_supply_cut_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `margin_rate`
- `airline.customer.dim_cabin`: `cabin_name`, `cabin_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (10)

For Delta Air Lines, what did Atlantic unit revenue do through the quarter, and what is required to get back to flat?

- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `unit_revenue_amount`, `unit_revenue_change_rate`, `pass_through_flag`, `intra_quarter_change_rate`, `path_to_flat_rate`, `geographic_entity_id`
- `airline.geography.dim_geographic_entity`: `region_id`, `entity_name`, `entity_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (14)

For Delta Air Lines, is a fourth quarter matching third-quarter earnings a new seasonality, or did the third quarter under-earn?

- `airline.price.fact_earnings_path`: `fiscal_quarter_id`, `earnings_amount`, `matches_prior_quarter_flag`, `new_seasonality_flag`, `under_earned_flag`, `geographic_entity_id`, `neutral_to_capacity_flag`
- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `unit_revenue_amount`, `unit_revenue_change_rate`, `intra_quarter_change_rate`, `geographic_entity_id`, `cabin_id`, `route_id`
- `airline.price.fact_non_ticket_revenue`: `fiscal_quarter_id`, `revenue_amount`, `growth_rate`, `sustainable_flag`, `maintenance_flag`, `cargo_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (15)

For Delta Air Lines, is maintenance and cargo revenue strength sustainable into the fourth quarter?

- `airline.price.fact_non_ticket_revenue`: `fiscal_quarter_id`, `revenue_amount`, `sustainable_flag`, `maintenance_flag`, `cargo_flag`, `growth_rate`
- `airline.supply.fact_shop_capacity`: `fiscal_quarter_id`, `maintenance_shop_id`, `capacity_quantity`, `in_house_share_rate`, `added_recently_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (18)

For Delta Air Lines, what margin improvement into next year is in the company's control?

- `airline.price.fact_geographic_margin`: `margin_rate`, `in_company_control_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `contribution_to_long_term_rate`, `premium_versus_main_mix_rate`
- `airline.price.fact_cabin_margin`: `margin_rate`, `fiscal_quarter_id`, `cabin_id`, `geographic_entity_id`, `gap_to_premium_rate`, `would_close_if_supply_cut_flag`
- `airline.price.fact_unit_revenue`: `unit_revenue_amount`, `unit_revenue_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`, `pass_through_flag`
- `airline.price.fact_non_ticket_revenue`: `revenue_amount`, `fiscal_quarter_id`, `growth_rate`, `sustainable_flag`, `maintenance_flag`, `cargo_flag`
- `airline.supply.fact_unit_cost`: `unit_cost_amount`, `carries_into_next_year_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `change_rate`, `ex_fuel_change_rate`, `ex_labor_change_rate`
- `airline.supply.fact_workforce_efficiency`: `fiscal_quarter_id`, `efficiency_rate`, `remaining_runway_rate`, `airport_component_flag`, `fleet_component_flag`

### Q3 2025 (19)

For Delta Air Lines, how sustainable is co-brand spend growth?

- `airline.price.fact_cobrand_economics`: `loyalty_program_id`, `spend_growth_rate`, `sustainable_flag`, `fiscal_quarter_id`, `card_program_id`, `partner_id`, `partner_economics_amount`
- `airline.price.dim_card_program`: `loyalty_program_id`, `card_name`, `card_code`, `rules_change_flag`
- `airline.customer.dim_loyalty_program`: `program_name`, `program_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2024 (2)

For Delta Air Lines, how is SkyMiles monetized through the new partnerships?

- `airline.price.fact_cobrand_economics`: `partner_id`, `partner_economics_amount`, `fiscal_quarter_id`, `card_program_id`, `loyalty_program_id`, `spend_growth_rate`, `sustainable_flag`
- `airline.customer.dim_loyalty_program`: `program_name`, `program_code`
- `airline.customer.dim_partner`: `partner_name`, `partner_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2024 (3)

For Delta Air Lines, with difficult comparisons, including last year's competitor grounding, should unit revenue accelerate into the spring?

- `airline.price.fact_unit_revenue`: `unit_revenue_amount`, `unit_revenue_change_rate`, `intra_quarter_change_rate`, `path_to_flat_rate`, `sequential_step_rate`, `fiscal_quarter_id`, `geographic_entity_id`
- `airline.price.fact_non_ticket_revenue`: `revenue_amount`, `growth_rate`, `fiscal_quarter_id`, `sustainable_flag`, `maintenance_flag`, `cargo_flag`
- `airline.supply.fact_industry_capacity`: `competitor_id`, `change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `industry_seat_quantity`, `irrational_return_flag`, `cuts_after_summer_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2024 (5)

For Delta Air Lines, how deep can the revenue premium versus domestic leisure carriers go as those carriers change product and network?

- `airline.price.fact_revenue_premium`: `premium_rate`, `competitor_product_change_flag`, `fiscal_quarter_id`, `competitor_id`, `geographic_entity_id`, `depth_available_rate`
- `airline.customer.dim_competitor`: `competitor_name`, `competitor_code`
- `airline.price.dim_fare_product`: `product_name`, `product_code`, `cabin_id`
- `airline.supply.fact_procurement_cost`: `product_investment_amount`, `fiscal_quarter_id`, `cost_amount`, `savings_follow_through_flag`, `keeping_unit_cost_in_check_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

## United Airlines

### Q1 2026 (9)

For United Airlines, what longer-term margin uplift is expected from merchandising, fleet, and loyalty, including newer narrow-bodies on those routes?

- `airline.price.fact_margin_bridge`: `merchandising_offer_id`, `long_term_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `effect_rate`, `initiative_code`
- `airline.price.dim_merchandising_offer`: `offer_name`, `offer_code`
- `airline.supply.fact_fleet_delivery`: `fleet_family_id`, `fiscal_quarter_id`, `aircraft_type_id`, `manufacturer_id`, `delivery_count`, `ahead_of_plan_flag`, `this_year_narrowbody_count`
- `airline.supply.fact_gauge_plan`: `route_id`, `unit_cost_effect_rate`, `fiscal_quarter_id`, `aircraft_type_id`, `gauge_change_rate`, `benefit_year_code`
- `airline.price.fact_cobrand_economics`: `loyalty_program_id`, `fiscal_quarter_id`, `card_program_id`, `partner_id`, `spend_growth_rate`, `sustainable_flag`, `partner_economics_amount`
- `airline.customer.dim_loyalty_program`: `program_name`, `program_code`

### Q1 2026 (10)

For United Airlines, what supports full fuel-cost recapture, and does it require other carriers to cut capacity?

- `airline.price.fact_fuel_recapture`: `recapture_rate`, `full_recapture_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `accelerating_flag`, `requires_competitor_cuts_flag`, `lag_versus_history_code`
- `airline.supply.fact_fuel_cost`: `fuel_region_id`, `unit_cost_amount`, `fiscal_quarter_id`, `high_flag`, `shock_duration_code`, `price_to_restore_growth_amount`
- `airline.supply.fact_industry_capacity`: `industry_seat_quantity`, `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `change_rate`, `irrational_return_flag`, `cuts_after_summer_flag`
- `airline.price.fact_fare`: `fiscal_quarter_id`, `fare_product_id`, `geographic_entity_id`, `cabin_id`, `fare_amount`, `fare_change_rate`, `higher_flag`
- `airline.supply.fact_capacity`: `capacity_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `route_id`, `aircraft_type_id`, `seat_quantity`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (2)

For United Airlines, if card-program rules change, what can be done around the loyalty economics over the next couple of years?

- `airline.price.fact_cobrand_economics`: `card_program_id`, `loyalty_program_id`, `partner_economics_amount`, `rules_response_code`, `fiscal_quarter_id`, `partner_id`, `spend_growth_rate`
- `airline.price.dim_card_program`: `loyalty_program_id`, `card_name`, `card_code`, `rules_change_flag`
- `airline.customer.dim_loyalty_program`: `program_name`, `program_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (3)

For United Airlines, what near-term program enhancements are possible on top of the existing card agreements?

- `airline.price.fact_cobrand_economics`: `card_program_id`, `loyalty_program_id`, `partner_id`, `partner_economics_amount`, `enhancement_without_renegotiation_flag`, `fiscal_quarter_id`, `spend_growth_rate`
- `airline.customer.dim_loyalty_program`: `program_name`, `program_code`
- `airline.customer.dim_partner`: `partner_name`, `partner_code`
- `airline.price.dim_card_program`: `loyalty_program_id`, `card_name`, `card_code`, `rules_change_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (6)

For United Airlines, was most of the shutdown hit domestic revenue, so is the sequential improvement mostly domestic?

- `airline.price.fact_unit_revenue`: `unit_revenue_amount`, `unit_revenue_change_rate`, `sequential_step_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`
- `airline.demand.fact_domestic_demand`: `sequential_improvement_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `passenger_count`, `best_geography_flag`
- `airline.demand.fact_international_demand`: `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`, `passenger_count`, `premium_mix_rate`, `main_mix_rate`
- `airline.supply.fact_shutdown_case`: `domestic_share_of_hit_rate`, `fiscal_quarter_id`, `event_id`, `geographic_entity_id`, `case_code`, `in_outlook_flag`
- `airline.customer.dim_event`: `event_name`, `event_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (8)

For United Airlines, are recent international routes still opening at a margin premium to their geography, and how long does that last?

- `airline.price.fact_route_margin`: `route_id`, `margin_rate`, `premium_to_geography_flag`, `premium_lasts_quarters`, `fiscal_quarter_id`, `geographic_entity_id`
- `airline.supply.fact_fleet_delivery`: `international_entry_quarters`, `fiscal_quarter_id`, `aircraft_type_id`, `manufacturer_id`, `fleet_family_id`, `delivery_count`, `ahead_of_plan_flag`
- `airline.price.fact_geographic_margin`: `margin_rate`, `contribution_to_long_term_rate`, `premium_versus_main_mix_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `in_company_control_flag`
- `airline.price.fact_cabin_margin`: `margin_rate`, `gap_to_premium_rate`, `fiscal_quarter_id`, `cabin_id`, `geographic_entity_id`, `would_close_if_supply_cut_flag`
- `airline.geography.dim_route`: `route_name`, `route_code`, `international_flag`, `long_haul_flag`, `geographic_entity_id`, `hub_id`, `new_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (11)

For United Airlines, how should price and cost deliver about a point of annual margin improvement given the comparison?

- `airline.price.fact_price_action`: `fiscal_quarter_id`, `geographic_entity_id`, `fare_product_id`, `increase_rate`, `domestic_flag`, `international_flag`, `different_flag`
- `airline.price.fact_fare`: `fiscal_quarter_id`, `fare_product_id`, `geographic_entity_id`, `cabin_id`, `fare_amount`, `fare_change_rate`, `higher_flag`
- `airline.supply.fact_unit_cost`: `unit_cost_amount`, `fiscal_quarter_id`, `geographic_entity_id`, `change_rate`, `ex_fuel_change_rate`, `ex_labor_change_rate`, `carries_into_next_year_flag`
- `airline.supply.fact_workforce_efficiency`: `fiscal_quarter_id`, `efficiency_rate`, `remaining_runway_rate`, `airport_component_flag`, `fleet_component_flag`
- `airline.price.fact_geographic_margin`: `margin_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `contribution_to_long_term_rate`, `premium_versus_main_mix_rate`, `in_company_control_flag`
- `airline.price.fact_cabin_margin`: `margin_rate`, `fiscal_quarter_id`, `cabin_id`, `geographic_entity_id`, `gap_to_premium_rate`, `would_close_if_supply_cut_flag`

### Q3 2025 (3)

For United Airlines, how widespread is premium leisure yield exceeding some corporate yields, and is that a lasting change?

- `airline.price.fact_yield_result`: `yield_amount`, `yield_change_rate`, `leisure_above_corporate_flag`, `lasting_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`
- `airline.customer.dim_cabin`: `cabin_name`, `cabin_code`
- `airline.customer.dim_customer_segment`: `segment_name`, `segment_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (5)

For United Airlines, does the smaller seasonal drop in air-traffic liability reflect pricing, or a longer booking curve?

- `airline.price.fact_traffic_liability`: `liability_amount`, `seasonal_drop_rate`, `from_pricing_flag`, `from_longer_curve_flag`, `fiscal_quarter_id`
- `airline.demand.fact_booking_curve`: `booking_window_id`, `holiday_curve_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `competitor_id`, `days_before_departure`, `booked_share_rate`
- `airline.price.fact_fare`: `fiscal_quarter_id`, `fare_product_id`, `geographic_entity_id`, `cabin_id`, `fare_amount`, `fare_change_rate`, `higher_flag`
- `airline.demand.fact_booking_demand`: `booking_window_id`, `booking_count`, `curve_normalized_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `customer_segment_id`
- `airline.price.fact_price_action`: `fiscal_quarter_id`, `geographic_entity_id`, `fare_product_id`, `increase_rate`, `domestic_flag`, `international_flag`, `different_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (7)

For United Airlines, how does fourth-quarter unit revenue sequence between domestic and international, including the holiday booking curve?

- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `unit_revenue_amount`, `unit_revenue_change_rate`, `intra_quarter_change_rate`, `geographic_entity_id`, `cabin_id`, `route_id`
- `airline.demand.fact_domestic_demand`: `fiscal_quarter_id`, `geographic_entity_id`, `hub_id`, `passenger_count`, `sequential_improvement_flag`, `best_geography_flag`
- `airline.demand.fact_international_demand`: `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`, `passenger_count`, `premium_mix_rate`, `main_mix_rate`
- `airline.demand.fact_booking_curve`: `fiscal_quarter_id`, `booking_window_id`, `holiday_curve_flag`, `geographic_entity_id`, `competitor_id`, `days_before_departure`, `booked_share_rate`
- `airline.price.fact_traffic_liability`: `fiscal_quarter_id`, `from_longer_curve_flag`, `liability_amount`, `seasonal_drop_rate`, `from_pricing_flag`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (4)

For United Airlines, which levers, including the main cabin, could make the fourth-quarter unit-revenue step better than the conservative case?

- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `cabin_id`, `unit_revenue_amount`, `unit_revenue_change_rate`, `intra_quarter_change_rate`, `sequential_step_rate`, `geographic_entity_id`
- `airline.price.fact_non_ticket_revenue`: `fiscal_quarter_id`, `revenue_amount`, `growth_rate`, `sustainable_flag`, `maintenance_flag`, `cargo_flag`
- `airline.demand.fact_cabin_demand`: `fiscal_quarter_id`, `cabin_id`, `geographic_entity_id`, `customer_segment_id`, `passenger_count`, `demand_change_rate`, `holding_if_inelastic_flag`
- `airline.price.fact_cabin_margin`: `fiscal_quarter_id`, `cabin_id`, `geographic_entity_id`, `margin_rate`, `gap_to_premium_rate`, `would_close_if_supply_cut_flag`
- `airline.customer.dim_cabin`: `cabin_name`, `cabin_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (9)

For United Airlines, how does the partner arrangement change the longer-term margin view?

- `airline.price.fact_partnership_margin`: `partner_id`, `margin_rate`, `longer_term_change_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `europe_hub_fit_flag`
- `airline.customer.dim_partner`: `partner_name`, `partner_code`
- `airline.price.fact_geographic_margin`: `margin_rate`, `contribution_to_long_term_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `premium_versus_main_mix_rate`, `in_company_control_flag`
- `airline.price.fact_cabin_margin`: `margin_rate`, `fiscal_quarter_id`, `cabin_id`, `geographic_entity_id`, `gap_to_premium_rate`, `would_close_if_supply_cut_flag`
- `airline.price.fact_margin_bridge`: `long_term_flag`, `fiscal_quarter_id`, `geographic_entity_id`, `merchandising_offer_id`, `effect_rate`, `initiative_code`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (11)

For United Airlines, which geography contributes most to the longer-term margin expansion?

- `airline.price.fact_geographic_margin`: `margin_rate`, `contribution_to_long_term_rate`, `fiscal_quarter_id`, `geographic_entity_id`, `premium_versus_main_mix_rate`, `in_company_control_flag`
- `airline.geography.dim_geographic_entity`: `region_id`, `entity_name`, `entity_code`
- `airline.demand.fact_international_demand`: `fiscal_quarter_id`, `geographic_entity_id`, `cabin_id`, `route_id`, `passenger_count`, `premium_mix_rate`, `main_mix_rate`
- `airline.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`
