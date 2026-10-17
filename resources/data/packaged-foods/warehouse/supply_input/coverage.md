# Food Inc input supply

Input supply owns plants, origins, hedges, freight, packaging capacity, and commodity cost for Food Inc. Contracted commodity cost and capacity are supply facts. They are not the selling-price file and they do not store consumer demand quantity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `country_identity` | `country_id` | `sf:food.geography.dim_country` `country_id` |
| `category_identity` | `category_id` | `sf:food.category.dim_category` `category_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:food.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `retailer_identity` | `retailer_id` | `sf:food.category.dim_retailer` `retailer_id` |
| `channel_identity` | `channel_id` | `sf:food.category.dim_channel` `channel_id` |
| `brand_identity` | `brand_id` | `sf:food.category.dim_brand` `brand_id` |
| `innovation_item_identity` | `innovation_item_id` | `sf:food.category.dim_innovation_item` `innovation_item_id` |

## Numbered questions

## Mondelez

### Q1 2026 (4)

For Mondelez, after cocoa fell early and then stabilized, how does management assess the cocoa market from here, including the second half?

- `food.supply.fact_commodity_cost`: `contract_cost_amount`, `fiscal_quarter_id`, `commodity_id`, `inflation_rate`, `exit_rate`, `band_code`, `phased_quarter_code`
- `food.supply.fact_spot_path`: `spot_cost_amount`, `fell_then_stabilized_flag`, `second_half_case_code`, `fiscal_quarter_id`, `commodity_id`
- `food.supply.fact_productivity`: `cost_program_id`, `different_from_prior_flag`, `fiscal_quarter_id`, `savings_amount`, `remaining_amount`, `offsets_inflation_flag`, `visible_if_compete_worsens_flag`
- `food.supply.fact_commodity_supply`: `fiscal_quarter_id`, `commodity_id`, `origin_id`, `covered_quantity`, `bought_the_dip_flag`, `locked_flag`, `keeps_rising_case_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (2)

For Mondelez, how does the lower cocoa cost change the guidance range and the room to invest?

- `food.supply.fact_commodity_cost`: `contract_cost_amount`, `fiscal_quarter_id`, `commodity_id`, `inflation_rate`, `exit_rate`, `band_code`, `phased_quarter_code`
- `food.supply.fact_spot_path`: `spot_cost_amount`, `fiscal_quarter_id`, `commodity_id`, `fell_then_stabilized_flag`, `second_half_case_code`
- `food.price.fact_earnings_outlook`: `cocoa_savings_kept_as_flexibility_rate`, `fiscal_quarter_id`, `in_algorithm_flag`, `top_line_same_way_flag`, `refill_enough_flag`, `pulled_forward_flag`
- `food.price.fact_advertising`: `fiscal_quarter_id`, `media_vehicle_id`, `category_id`, `spend_amount`, `versus_normal_rate`, `step_up_rate`, `holds_for_year_flag`
- `food.supply.fact_commodity_supply`: `fiscal_quarter_id`, `commodity_id`, `origin_id`, `covered_quantity`, `bought_the_dip_flag`, `locked_flag`, `keeps_rising_case_flag`
- `food.time.dim_fiscal_quarter`: `guidance_horizon`, `quarter_label`, `quarter_code`

### Q4 2025 (3)

For Mondelez, how does cocoa cost phase through 2026, and how do potential chocolate price investments phase over the year?

- `food.supply.fact_commodity_cost`: `contract_cost_amount`, `fiscal_quarter_id`, `commodity_id`, `inflation_rate`, `exit_rate`, `band_code`, `phased_quarter_code`
- `food.supply.fact_spot_path`: `spot_cost_amount`, `fiscal_quarter_id`, `commodity_id`, `fell_then_stabilized_flag`, `second_half_case_code`
- `food.price.fact_regional_price`: `price_action_id`, `fiscal_quarter_id`, `region_id`, `category_id`, `planned_change_rate`, `flex_risk_flag`, `competitive_response_code`
- `food.price.fact_chocolate_margin`: `recovery_starts_next_year_flag`, `fiscal_quarter_id`, `category_id`, `region_id`, `profit_rate`, `back_to_pre_period_flag`, `neutral_after_hedge_flag`
- `food.supply.dim_commodity`: `commodity_name`, `commodity_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (12)

For Mondelez, how are cocoa-growing investments outside West Africa progressing relative to traditional origins?

- `food.supply.fact_commodity_supply`: `origin_id`, `fiscal_quarter_id`, `commodity_id`, `covered_quantity`, `bought_the_dip_flag`, `locked_flag`, `keeps_rising_case_flag`
- `food.supply.fact_origin_investment`: `origin_id`, `investment_amount`, `ahead_of_traditional_flag`, `fiscal_quarter_id`, `commodity_id`
- `food.supply.dim_origin`: `origin_name`, `origin_code`, `commodity_id`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (2)

For Mondelez, with cocoa largely locked, what drove the fourth-quarter outlook change, and what are the puts and takes for next year's organic sales given planned investment and elasticity?

- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `phased_quarter_code`, `commodity_id`, `contract_cost_amount`, `inflation_rate`, `exit_rate`, `band_code`
- `food.supply.fact_spot_path`: `fiscal_quarter_id`, `commodity_id`, `spot_cost_amount`, `fell_then_stabilized_flag`, `second_half_case_code`
- `food.demand.fact_organic_result`: `fiscal_quarter_id`, `organic_sales_rate`, `price_contributed_flag`, `quarter_phasing_gap_rate`, `category_id`, `region_id`, `channel_id`
- `food.demand.fact_guidance_volume`: `fiscal_quarter_id`, `positive_year_flag`, `region_id`, `category_id`, `volume_case_rate`, `high_end_flag`, `swing_code`
- `food.price.fact_earnings_outlook`: `fiscal_quarter_id`, `cocoa_savings_kept_as_flexibility_rate`, `in_algorithm_flag`, `top_line_same_way_flag`, `refill_enough_flag`, `pulled_forward_flag`
- `food.price.fact_advertising`: `fiscal_quarter_id`, `holds_for_year_flag`, `media_vehicle_id`, `category_id`, `spend_amount`, `versus_normal_rate`, `step_up_rate`

### Q3 2025 (7)

For Mondelez, how does the new multiyear North America supply-chain program differ from earlier productivity programs, and are there early targets?

- `food.supply.fact_modernization`: `cost_program_id`, `new_program_flag`, `early_target_flag`, `fiscal_quarter_id`, `plant_id`, `category_id`, `in_place_flag`
- `food.supply.fact_plant_capacity`: `cost_program_id`, `fiscal_quarter_id`, `plant_id`, `category_id`, `capacity_quantity`, `modernization_flag`, `service_already_in_place_flag`
- `food.supply.fact_productivity`: `cost_program_id`, `different_from_prior_flag`, `fiscal_quarter_id`, `savings_amount`, `remaining_amount`, `offsets_inflation_flag`, `visible_if_compete_worsens_flag`
- `food.price.fact_margin_bridge`: `quarter_code_within_year`, `fiscal_quarter_id`, `category_id`, `effect_rate`, `driver_code`
- `food.supply.dim_cost_program`: `program_name`, `program_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (8)

For Mondelez, how much of this year's SG&A decline is a lasting cost reduction versus spend that returns next year with the planned reinvestment?

- `food.supply.fact_sga`: `cost_program_id`, `spend_amount`, `decline_is_lasting_flag`, `returns_next_year_flag`, `multi_year_continues_flag`, `fiscal_quarter_id`
- `food.price.fact_earnings_outlook`: `top_line_same_way_flag`, `fiscal_quarter_id`, `in_algorithm_flag`, `refill_enough_flag`, `pulled_forward_flag`, `cocoa_savings_kept_as_flexibility_rate`
- `food.price.fact_advertising`: `spend_amount`, `versus_normal_rate`, `holds_for_year_flag`, `fiscal_quarter_id`, `media_vehicle_id`, `category_id`, `step_up_rate`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (10)

For Mondelez, is any 2026 investment being pulled into the fourth quarter, and does the 2026 earnings outlook already refill spend enough that 2027 does not need another reset?

- `food.supply.fact_sga`: `fiscal_quarter_id`, `spend_amount`, `cost_program_id`, `decline_is_lasting_flag`, `returns_next_year_flag`, `multi_year_continues_flag`
- `food.price.fact_earnings_outlook`: `fiscal_quarter_id`, `refill_enough_flag`, `pulled_forward_flag`, `in_algorithm_flag`, `top_line_same_way_flag`, `cocoa_savings_kept_as_flexibility_rate`
- `food.price.fact_advertising`: `fiscal_quarter_id`, `spend_amount`, `media_vehicle_id`, `category_id`, `versus_normal_rate`, `step_up_rate`, `holds_for_year_flag`
- `food.price.fact_operating_profit`: `fiscal_quarter_id`, `profit_change_rate`, `inflation_offset_flag`, `high_end_reachable_flag`
- `food.price.fact_price_investment`: `fiscal_quarter_id`, `category_id`, `brand_id`, `price_action_id`, `invested_share_rate`, `untreated_share_rate`, `lapped_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (2)

For Mondelez, after buying the recent cocoa dip, is more pricing or revenue-growth management still needed in the back half under the higher-cocoa scenario?

- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `commodity_id`, `contract_cost_amount`, `inflation_rate`, `exit_rate`, `band_code`, `phased_quarter_code`
- `food.supply.fact_spot_path`: `second_half_case_code`, `fiscal_quarter_id`, `commodity_id`, `spot_cost_amount`, `fell_then_stabilized_flag`
- `food.price.fact_list_price`: `price_action_id`, `usable_after_reset_flag`, `fiscal_quarter_id`, `category_id`, `brand_id`, `region_id`, `list_change_rate`
- `food.price.fact_realized_price`: `price_action_id`, `fiscal_quarter_id`, `category_id`, `country_id`, `region_id`, `realized_change_rate`, `negotiation_open_flag`
- `food.price.fact_revenue_management`: `price_action_id`, `action_still_needed_flag`, `higher_cost_scenario_flag`, `back_half_flag`, `fiscal_quarter_id`, `category_id`
- `food.supply.fact_commodity_supply`: `fiscal_quarter_id`, `commodity_id`, `origin_id`, `covered_quantity`, `bought_the_dip_flag`, `locked_flag`, `keeps_rising_case_flag`

## General Mills

### Q1 FY2027 (3)

For General Mills, where did inflation land in the first quarter, how does it pace for the rest of the year, and what exit rate sits inside the high end of the 4% to 5% range?

- `food.supply.fact_inflation_path`: `fiscal_quarter_id`, `quarter_inflation_rate`, `rest_of_year_rate`, `exit_rate`, `fourth_quarter_step_up_flag`, `similar_three_quarters_flag`, `net_includes_refund_flag`
- `food.supply.fact_input_inflation_case`: `fiscal_quarter_id`, `assumed_rate`, `hedged_share_rate`, `fuel_in_range_flag`, `commodity_id`, `hedge_book_id`
- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `contract_cost_amount`, `inflation_rate`, `exit_rate`, `phased_quarter_code`, `commodity_id`, `band_code`
- `food.price.fact_margin_bridge`: `fiscal_quarter_id`, `effect_rate`, `quarter_code_within_year`, `category_id`, `driver_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 FY2027 (10)

For General Mills, if inflation is similar in the first three fiscal quarters and steps up in the fourth, can the company stay ahead of sticky inflation in later years, and is price a usable lever after the recent value reset?

- `food.supply.fact_inflation_path`: `fiscal_quarter_id`, `quarter_inflation_rate`, `rest_of_year_rate`, `similar_three_quarters_flag`, `fourth_quarter_step_up_flag`, `exit_rate`, `net_includes_refund_flag`
- `food.supply.fact_input_inflation_case`: `fiscal_quarter_id`, `hedge_book_id`, `commodity_id`, `assumed_rate`, `hedged_share_rate`, `fuel_in_range_flag`
- `food.supply.fact_hedge_coverage`: `fiscal_quarter_id`, `hedge_book_id`, `commodity_id`, `coverage_rate`, `unhedged_assumption_rate`, `with_fuel_case_rate`, `without_fuel_case_rate`
- `food.supply.dim_hedge_book`: `commodity_id`, `book_name`, `book_code`
- `food.price.fact_list_price`: `fiscal_quarter_id`, `price_action_id`, `held_flat_flag`, `usable_after_reset_flag`, `category_id`, `brand_id`, `region_id`
- `food.price.fact_realized_price`: `fiscal_quarter_id`, `price_action_id`, `flat_while_cost_down_flag`, `category_id`, `country_id`, `region_id`, `realized_change_rate`

### Q1 FY2027 (12)

For General Mills, what flexibility does the new partner packaging facility add, what other transformation work is underway, and when do the benefits show up?

- `food.supply.fact_packaging_capacity`: `packaging_site_id`, `capacity_asset_id`, `capacity_quantity`, `partner_flag`, `flexibility_flag`, `fiscal_quarter_id`
- `food.supply.dim_packaging_site`: `partner_flag`, `site_name`, `site_code`
- `food.supply.fact_transformation`: `cost_program_id`, `capacity_asset_id`, `benefit_year_code`, `flexibility_added_flag`, `fiscal_quarter_id`, `project_count`
- `food.supply.fact_commodity_cost`: `contract_cost_amount`, `fiscal_quarter_id`, `commodity_id`, `inflation_rate`, `exit_rate`, `band_code`, `phased_quarter_code`
- `food.supply.fact_productivity`: `cost_program_id`, `fiscal_quarter_id`, `savings_amount`, `remaining_amount`, `offsets_inflation_flag`, `visible_if_compete_worsens_flag`, `different_from_prior_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 FY2027 (14)

For General Mills, how exposed is the company to higher wheat costs, how covered is it if wheat keeps rising, and how much flour pass-through lifts foodservice?

- `food.supply.fact_commodity_supply`: `covered_quantity`, `keeps_rising_case_flag`, `fiscal_quarter_id`, `commodity_id`, `origin_id`, `bought_the_dip_flag`, `locked_flag`
- `food.supply.fact_hedge_coverage`: `hedge_book_id`, `fiscal_quarter_id`, `commodity_id`, `coverage_rate`, `unhedged_assumption_rate`, `with_fuel_case_rate`, `without_fuel_case_rate`
- `food.supply.dim_hedge_book`: `commodity_id`, `book_name`, `book_code`
- `food.price.fact_flour_price`: `pass_through_rate`, `fiscal_quarter_id`, `channel_id`, `category_id`, `indexed_flag`, `better_than_plan_flag`
- `food.demand.fact_foodservice_volume`: `flour_volume_quantity`, `fiscal_quarter_id`, `channel_id`, `category_id`, `volume_quantity`, `persists_flag`, `says_about_channel_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 FY2026 (7)

For General Mills, how were fuel and other inflation assumptions set inside the 4% to 5% range, and how much is hedged versus assumed?

- `food.supply.fact_input_inflation_case`: `hedge_book_id`, `assumed_rate`, `hedged_share_rate`, `fuel_in_range_flag`, `fiscal_quarter_id`, `commodity_id`
- `food.supply.fact_hedge_coverage`: `hedge_book_id`, `unhedged_assumption_rate`, `with_fuel_case_rate`, `without_fuel_case_rate`, `fiscal_quarter_id`, `commodity_id`, `coverage_rate`
- `food.supply.fact_inflation_path`: `quarter_inflation_rate`, `fiscal_quarter_id`, `rest_of_year_rate`, `exit_rate`, `similar_three_quarters_flag`, `fourth_quarter_step_up_flag`, `net_includes_refund_flag`
- `food.supply.dim_hedge_book`: `commodity_id`, `book_name`, `book_code`
- `food.supply.dim_commodity`: `commodity_name`, `commodity_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 FY2026 (11)

For General Mills, does the 4% to 5% net inflation figure include tariff refunds, and when would those refunds land?

- `food.supply.fact_inflation_path`: `quarter_inflation_rate`, `net_includes_refund_flag`, `fiscal_quarter_id`, `rest_of_year_rate`, `exit_rate`, `similar_three_quarters_flag`, `fourth_quarter_step_up_flag`
- `food.supply.fact_input_inflation_case`: `fiscal_quarter_id`, `commodity_id`, `hedge_book_id`, `assumed_rate`, `hedged_share_rate`, `fuel_in_range_flag`
- `food.price.fact_tariff_price`: `refund_timing_code`, `fiscal_quarter_id`, `included_in_net_flag`
- `food.price.fact_margin_bridge`: `fiscal_quarter_id`, `category_id`, `effect_rate`, `driver_code`, `quarter_code_within_year`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 FY2026 (7)

For General Mills, what does fiscal 2027 inflation look like with and without elevated fuel and oil-derivative costs, and how hard do savings have to work to offset it?

- `food.supply.fact_inflation_path`: `fiscal_quarter_id`, `quarter_inflation_rate`, `rest_of_year_rate`, `exit_rate`, `similar_three_quarters_flag`, `fourth_quarter_step_up_flag`, `net_includes_refund_flag`
- `food.supply.fact_input_inflation_case`: `fiscal_quarter_id`, `fuel_in_range_flag`, `commodity_id`, `hedge_book_id`, `assumed_rate`, `hedged_share_rate`
- `food.supply.fact_hedge_coverage`: `fiscal_quarter_id`, `with_fuel_case_rate`, `without_fuel_case_rate`, `savings_required_rate`, `hedge_book_id`, `commodity_id`, `coverage_rate`
- `food.supply.fact_productivity`: `fiscal_quarter_id`, `cost_program_id`, `savings_amount`, `offsets_inflation_flag`, `remaining_amount`, `visible_if_compete_worsens_flag`, `different_from_prior_flag`
- `food.price.fact_margin_bridge`: `fiscal_quarter_id`, `category_id`, `effect_rate`, `driver_code`, `quarter_code_within_year`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 FY2026 (13)

For General Mills, which parts of North America Retail and pet were hit by retailer inventory adjustments, and how does each reverse in the fourth quarter?

- `food.supply.fact_retailer_inventory`: `fiscal_quarter_id`, `retailer_id`, `inventory_quantity`, `refill_quarter_flag`, `category_id`, `channel_id`, `acquisition_id`
- `food.category.dim_retailer`: `retailer_name`, `retailer_code`, `channel_id`
- `food.demand.fact_consumption`: `fiscal_quarter_id`, `category_id`, `channel_id`, `brand_id`, `consumption_quantity`, `consumption_change_rate`, `healthier_than_shipments_flag`
- `food.demand.fact_volume_share`: `fiscal_quarter_id`, `category_id`, `brand_id`, `region_id`, `country_id`, `volume_share_rate`, `share_change_rate`
- `food.demand.fact_pet_volume`: `fiscal_quarter_id`, `category_id`, `brand_id`, `consumer_cohort_id`, `volume_quantity`, `volume_change_rate`, `cyclical_visit_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 FY2026 (15)

For General Mills, beyond diesel, is driver tightness or other freight a headwind for next year's inflation?

- `food.supply.fact_freight_cost`: `freight_lane_id`, `driver_tight_flag`, `beyond_diesel_flag`, `in_next_year_outlook_flag`, `fiscal_quarter_id`, `cost_amount`
- `food.supply.dim_freight_lane`: `lane_name`, `lane_code`
- `food.supply.fact_inflation_path`: `quarter_inflation_rate`, `rest_of_year_rate`, `fiscal_quarter_id`, `exit_rate`, `similar_three_quarters_flag`, `fourth_quarter_step_up_flag`, `net_includes_refund_flag`
- `food.supply.fact_input_inflation_case`: `fiscal_quarter_id`, `commodity_id`, `hedge_book_id`, `assumed_rate`, `hedged_share_rate`, `fuel_in_range_flag`
- `food.price.fact_margin_bridge`: `driver_code`, `quarter_code_within_year`, `fiscal_quarter_id`, `category_id`, `effect_rate`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`
