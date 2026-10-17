# Food Inc price and margin

Price and margin owns list price, realized price, price gaps, mix, gross margin, advertising, and profit for Food Inc. A price or margin row does not store case quantity. Cocoa, wheat, and fuel unit costs stay on the supply cost facts.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `region_identity` | `region_id` | `sf:food.geography.dim_region` `region_id` |
| `category_identity` | `category_id` | `sf:food.category.dim_category` `category_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:food.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `brand_identity` | `brand_id` | `sf:food.category.dim_brand` `brand_id` |
| `country_identity` | `country_id` | `sf:food.geography.dim_country` `country_id` |
| `competitor_identity` | `competitor_id` | `sf:food.category.dim_competitor` `competitor_id` |
| `channel_identity` | `channel_id` | `sf:food.category.dim_channel` `channel_id` |

## Numbered questions

## Mondelez

### Q1 2026 (2)

For Mondelez, which European geographies still have pricing negotiations open heading into the second quarter?

- `food.price.fact_realized_price`: `fiscal_quarter_id`, `negotiation_open_flag`, `category_id`, `country_id`, `region_id`, `price_action_id`, `realized_change_rate`
- `food.demand.fact_chocolate_volume`: `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `share_growth_flag`
- `food.price.dim_price_action`: `open_flag`, `region_id`, `category_id`, `action_name`, `action_code`
- `food.geography.dim_region`: `region_name`, `region_code`
- `food.geography.dim_country`: `region_id`, `country_name`, `country_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (3)

For Mondelez, how has the European competitive environment evolved with cocoa volatility, and how is that expected to look for the rest of the year?

- `food.price.fact_realized_price`: `price_action_id`, `fiscal_quarter_id`, `category_id`, `country_id`, `region_id`, `realized_change_rate`, `negotiation_open_flag`
- `food.demand.fact_chocolate_volume`: `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `share_growth_flag`
- `food.price.fact_competitor_price`: `competitor_id`, `competitor_change_rate`, `fiscal_quarter_id`, `category_id`, `sharp_cut_flag`, `snack_cut_flag`, `adjacent_only_flag`
- `food.price.fact_price_gap`: `competitor_id`, `fiscal_quarter_id`, `category_id`, `country_id`, `gap_rate`, `closed_flag`, `first_mover_flag`
- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `commodity_id`, `contract_cost_amount`, `inflation_rate`, `exit_rate`, `band_code`, `phased_quarter_code`
- `food.supply.fact_spot_path`: `fiscal_quarter_id`, `commodity_id`, `spot_cost_amount`, `fell_then_stabilized_flag`, `second_half_case_code`

### Q1 2026 (5)

For Mondelez, what price elasticity and trade-down is showing up by European market, given a fragile consumer but only a small organic-sales decline?

- `food.price.fact_realized_price`: `price_action_id`, `flat_while_cost_down_flag`, `fiscal_quarter_id`, `category_id`, `country_id`, `region_id`, `realized_change_rate`
- `food.demand.fact_chocolate_volume`: `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `share_growth_flag`
- `food.demand.fact_elasticity`: `consumer_cohort_id`, `elasticity_rate`, `trade_down_rate`, `small_sales_decline_flag`, `fiscal_quarter_id`, `category_id`, `country_id`
- `food.demand.fact_organic_result`: `organic_sales_rate`, `price_contributed_flag`, `fiscal_quarter_id`, `category_id`, `region_id`, `channel_id`, `volume_contributed_flag`
- `food.demand.fact_consumer_demand`: `consumer_cohort_id`, `fragile_flag`, `fiscal_quarter_id`, `category_id`, `confidence_index`, `promo_waiting_faded_flag`, `insight_code`
- `food.category.dim_consumer_cohort`: `cohort_name`, `cohort_code`

### Q1 2026 (6)

For Mondelez, how should gross margin progress after the quarter's inventory-phasing effect was smaller than feared?

- `food.price.fact_gross_margin`: `fiscal_quarter_id`, `gross_margin_rate`, `inventory_phasing_drag_rate`, `smaller_than_feared_flag`, `category_id`, `flat_if_ranges_match_inflation_flag`, `mid_thirties_reachable_flag`
- `food.price.fact_margin_bridge`: `fiscal_quarter_id`, `effect_rate`, `quarter_code_within_year`, `category_id`, `driver_code`
- `food.supply.fact_inventory_position`: `fiscal_quarter_id`, `inventory_quantity`, `phasing_drag_smaller_flag`, `commodity_id`, `acquisition_id`, `extra_month_flag`
- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `phased_quarter_code`, `commodity_id`, `contract_cost_amount`, `inflation_rate`, `exit_rate`, `band_code`
- `food.supply.dim_commodity`: `commodity_name`, `commodity_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (5)

For Mondelez, with chocolate pricing expected flat while cocoa is down, is the net price-cost relationship in the guide roughly neutral after hedges and inventory accounting, or still a benefit?

- `food.price.fact_regional_price`: `price_action_id`, `fiscal_quarter_id`, `region_id`, `category_id`, `planned_change_rate`, `flex_risk_flag`, `competitive_response_code`
- `food.price.fact_chocolate_margin`: `neutral_after_hedge_flag`, `still_a_benefit_flag`, `fiscal_quarter_id`, `category_id`, `region_id`, `profit_rate`, `back_to_pre_period_flag`
- `food.supply.fact_commodity_cost`: `contract_cost_amount`, `fiscal_quarter_id`, `commodity_id`, `inflation_rate`, `exit_rate`, `band_code`, `phased_quarter_code`
- `food.supply.fact_spot_path`: `spot_cost_amount`, `fiscal_quarter_id`, `commodity_id`, `fell_then_stabilized_flag`, `second_half_case_code`
- `food.supply.fact_hedge_coverage`: `hedge_book_id`, `with_fuel_case_rate`, `fiscal_quarter_id`, `commodity_id`, `coverage_rate`, `unhedged_assumption_rate`, `without_fuel_case_rate`
- `food.supply.dim_hedge_book`: `commodity_id`, `book_name`, `book_code`

### Q4 2025 (6)

For Mondelez, how large is the 2026 advertising step-up versus a normal level?

- `food.price.fact_advertising`: `versus_normal_rate`, `step_up_rate`, `fiscal_quarter_id`, `media_vehicle_id`, `category_id`, `spend_amount`, `holds_for_year_flag`
- `food.price.dim_media_vehicle`: `vehicle_name`, `vehicle_code`
- `food.price.fact_earnings_outlook`: `fiscal_quarter_id`, `in_algorithm_flag`, `top_line_same_way_flag`, `refill_enough_flag`, `pulled_forward_flag`, `cocoa_savings_kept_as_flexibility_rate`
- `food.price.fact_price_investment`: `fiscal_quarter_id`, `category_id`, `brand_id`, `price_action_id`, `invested_share_rate`, `untreated_share_rate`, `lapped_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (9)

For Mondelez, going into 2027, are media, compensation, and channel investments largely lapped so leverage comes from mix, lower cocoa, and overhead, or do multiyear investments continue?

- `food.price.fact_advertising`: `media_vehicle_id`, `holds_for_year_flag`, `fiscal_quarter_id`, `category_id`, `spend_amount`, `versus_normal_rate`, `step_up_rate`
- `food.supply.fact_sga`: `returns_next_year_flag`, `multi_year_continues_flag`, `fiscal_quarter_id`, `cost_program_id`, `spend_amount`, `decline_is_lasting_flag`
- `food.demand.fact_channel_volume`: `channel_id`, `fiscal_quarter_id`, `category_id`, `retailer_id`, `volume_quantity`, `volume_change_rate`, `material_driver_flag`
- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `commodity_id`, `contract_cost_amount`, `inflation_rate`, `exit_rate`, `band_code`, `phased_quarter_code`
- `food.supply.fact_spot_path`: `fiscal_quarter_id`, `commodity_id`, `spot_cost_amount`, `fell_then_stabilized_flag`, `second_half_case_code`
- `food.price.fact_gross_margin`: `gross_margin_rate`, `fiscal_quarter_id`, `category_id`, `inventory_phasing_drag_rate`, `smaller_than_feared_flag`, `flat_if_ranges_match_inflation_flag`, `mid_thirties_reachable_flag`

### Q3 2025 (1)

For Mondelez, how is European pricing landing into year-end and next year, including price-gap management in specific markets?

- `food.price.fact_realized_price`: `price_action_id`, `fiscal_quarter_id`, `category_id`, `country_id`, `region_id`, `realized_change_rate`, `negotiation_open_flag`
- `food.demand.fact_chocolate_volume`: `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `share_growth_flag`
- `food.price.fact_list_price`: `price_action_id`, `fiscal_quarter_id`, `category_id`, `brand_id`, `region_id`, `list_change_rate`, `held_flat_flag`
- `food.price.fact_price_gap`: `fiscal_quarter_id`, `category_id`, `country_id`, `competitor_id`, `gap_rate`, `closed_flag`, `first_mover_flag`
- `food.category.dim_competitor`: `competitor_name`, `competitor_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (9)

For Mondelez, is emphasizing value while protecting the profit pool the right North America approach over the next six to twelve months, or do price investment and profit protection have to be traded off?

- `food.price.fact_regional_price`: `price_action_id`, `fiscal_quarter_id`, `region_id`, `category_id`, `planned_change_rate`, `flex_risk_flag`, `competitive_response_code`
- `food.price.fact_profit_pool`: `profit_amount`, `protect_pool_flag`, `fiscal_quarter_id`, `category_id`, `channel_id`, `tradeoff_required_flag`, `growth_realistic_flag`
- `food.demand.fact_category_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`, `category_pounds_quantity`
- `food.demand.fact_regional_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `improving_flag`
- `food.price.fact_operating_profit`: `profit_change_rate`, `fiscal_quarter_id`, `inflation_offset_flag`, `high_end_reachable_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

## General Mills

### Q1 FY2027 (8)

For General Mills, how do gross-margin puts and takes work through the year as input-cost inflation, which accelerated late last year, is set against productivity and a rising mix benefit?

- `food.price.fact_gross_margin`: `gross_margin_rate`, `inventory_phasing_drag_rate`, `flat_if_ranges_match_inflation_flag`, `fiscal_quarter_id`, `category_id`, `smaller_than_feared_flag`, `mid_thirties_reachable_flag`
- `food.price.fact_margin_bridge`: `effect_rate`, `quarter_code_within_year`, `fiscal_quarter_id`, `category_id`, `driver_code`
- `food.supply.fact_inflation_path`: `quarter_inflation_rate`, `rest_of_year_rate`, `exit_rate`, `fiscal_quarter_id`, `similar_three_quarters_flag`, `fourth_quarter_step_up_flag`, `net_includes_refund_flag`
- `food.supply.fact_input_inflation_case`: `assumed_rate`, `hedged_share_rate`, `fiscal_quarter_id`, `commodity_id`, `hedge_book_id`, `fuel_in_range_flag`
- `food.supply.fact_productivity`: `cost_program_id`, `offsets_inflation_flag`, `fiscal_quarter_id`, `savings_amount`, `remaining_amount`, `visible_if_compete_worsens_flag`, `different_from_prior_flag`
- `food.price.fact_price_mix`: `price_mix_rate`, `mix_pressure_rate`, `fiscal_quarter_id`, `category_id`, `competitor_id`, `positive_flag`, `competitor_followed_flag`

### Q1 FY2027 (9)

For General Mills, have pricing plans changed from the start of the year after better foodservice and pet pricing, in the current inflation backdrop?

- `food.price.fact_list_price`: `price_action_id`, `list_change_rate`, `held_flat_flag`, `share_gain_in_plan_rate`, `usable_after_reset_flag`, `fiscal_quarter_id`, `category_id`
- `food.price.fact_realized_price`: `price_action_id`, `realized_change_rate`, `flat_while_cost_down_flag`, `fiscal_quarter_id`, `category_id`, `country_id`, `region_id`
- `food.demand.fact_foodservice_volume`: `fiscal_quarter_id`, `channel_id`, `category_id`, `volume_quantity`, `flour_volume_quantity`, `persists_flag`, `says_about_channel_flag`
- `food.price.fact_flour_price`: `better_than_plan_flag`, `fiscal_quarter_id`, `channel_id`, `category_id`, `pass_through_rate`, `indexed_flag`
- `food.demand.fact_pet_volume`: `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `brand_id`, `consumer_cohort_id`, `volume_quantity`, `cyclical_visit_flag`
- `food.supply.fact_retailer_inventory`: `fiscal_quarter_id`, `retailer_id`, `category_id`, `channel_id`, `acquisition_id`, `inventory_quantity`, `expected_reduction_quantity`

### Q1 FY2027 (11)

For General Mills, how much was marketing up year over year this quarter, and does that rate hold for the rest of the year?

- `food.price.fact_advertising`: `fiscal_quarter_id`, `spend_amount`, `versus_normal_rate`, `step_up_rate`, `holds_for_year_flag`, `media_vehicle_id`, `category_id`
- `food.price.dim_media_vehicle`: `vehicle_name`, `vehicle_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 FY2027 (13)

For General Mills, beyond cereal entry prices and larger formats, where else has price-pack architecture changed, and have results matched North America Retail cereal?

- `food.price.fact_architecture_result`: `price_pack_id`, `result_rate`, `matched_cereal_flag`, `fiscal_quarter_id`, `category_id`, `promotion_id`, `everyday_versus_high_low_code`
- `food.price.dim_price_pack`: `pack_name`, `pack_code`, `category_id`
- `food.demand.fact_cereal_volume`: `matched_other_categories_flag`, `fiscal_quarter_id`, `category_id`, `brand_id`, `volume_quantity`, `acceleration_still_ahead_flag`
- `food.demand.fact_consumption`: `consumption_change_rate`, `fiscal_quarter_id`, `category_id`, `channel_id`, `brand_id`, `consumption_quantity`, `healthier_than_shipments_flag`
- `food.demand.fact_volume_share`: `share_change_rate`, `fiscal_quarter_id`, `category_id`, `brand_id`, `region_id`, `country_id`, `volume_share_rate`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 FY2027 (17)

If peers raise list prices while General Mills holds them, how much market-share gain is in the plan as consumers shift?

- `food.price.fact_list_price`: `price_action_id`, `list_change_rate`, `peer_raising_flag`, `share_gain_in_plan_rate`, `fiscal_quarter_id`, `category_id`, `brand_id`
- `food.demand.fact_share_destination`: `competitor_id`, `private_label_share_rate`, `insurgent_share_rate`, `fiscal_quarter_id`, `category_id`, `channel_id`, `not_mainly_private_label_flag`
- `food.demand.fact_volume_share`: `volume_share_rate`, `share_change_rate`, `fiscal_quarter_id`, `category_id`, `brand_id`, `region_id`, `country_id`
- `food.price.fact_competitor_price`: `competitor_id`, `competitor_change_rate`, `fiscal_quarter_id`, `category_id`, `sharp_cut_flag`, `snack_cut_flag`, `adjacent_only_flag`
- `food.price.fact_price_gap`: `competitor_id`, `fiscal_quarter_id`, `category_id`, `country_id`, `gap_rate`, `closed_flag`, `first_mover_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 FY2026 (1)

For General Mills, what was learned from last year's price investments that supports pivoting fiscal 2027 spend toward better-for-you innovation and renovation, and how confident is management that the shift delivers?

- `food.price.fact_list_price`: `fiscal_quarter_id`, `price_action_id`, `category_id`, `brand_id`, `region_id`, `list_change_rate`, `held_flat_flag`
- `food.price.fact_realized_price`: `fiscal_quarter_id`, `price_action_id`, `category_id`, `country_id`, `region_id`, `realized_change_rate`, `negotiation_open_flag`
- `food.demand.fact_innovation_demand`: `fiscal_quarter_id`, `innovation_item_id`, `category_id`, `brand_id`, `velocity_quantity`, `ahead_of_plan_flag`, `growth_versus_goal_rate`
- `food.category.dim_innovation_item`: `category_id`, `brand_id`, `item_name`, `item_code`, `item_type_code`
- `food.demand.fact_consumer_demand`: `fiscal_quarter_id`, `consumer_cohort_id`, `category_id`, `confidence_index`, `promo_waiting_faded_flag`, `fragile_flag`, `insight_code`
- `food.category.dim_consumer_cohort`: `cohort_name`, `cohort_code`

### Q4 FY2026 (2)

For General Mills, has the mid-year shift toward waiting for promotions faded?

- `food.price.fact_marketing_response`: `promotion_id`, `fiscal_quarter_id`, `category_id`, `response_rate`, `restored_flag`, `pre_covid_comparable_flag`, `vehicle_code`
- `food.price.dim_promotion`: `promotion_name`, `promotion_code`
- `food.demand.fact_consumer_demand`: `consumer_cohort_id`, `promo_waiting_faded_flag`, `fiscal_quarter_id`, `category_id`, `confidence_index`, `fragile_flag`, `insight_code`
- `food.category.dim_consumer_cohort`: `cohort_name`, `cohort_code`
- `food.demand.fact_category_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`, `category_pounds_quantity`
- `food.demand.fact_regional_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `improving_flag`

### Q4 FY2026 (8)

What dollar category growth is expected, and does the guide assume General Mills grows in line with the category by year-end as dollar share improves?

- `food.price.fact_value_share`: `category_id`, `value_share_rate`, `dollar_share_rate`, `gap_to_volume_share_rate`, `in_line_with_category_flag`, `fiscal_quarter_id`, `channel_id`
- `food.demand.fact_scanner_demand`: `category_id`, `category_dollar_growth_rate`, `fiscal_quarter_id`, `region_id`, `scanner_change_rate`, `softer_flag`
- `food.demand.fact_category_volume`: `category_id`, `category_pounds_quantity`, `fiscal_quarter_id`, `region_id`, `country_id`, `volume_quantity`, `volume_change_rate`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 FY2026 (10)

For General Mills, ignoring the extra week, are gross margins roughly flat in fiscal 2027 if the sales and profit ranges match the inflation rate?

- `food.price.fact_gross_margin`: `fiscal_quarter_id`, `gross_margin_rate`, `inventory_phasing_drag_rate`, `flat_if_ranges_match_inflation_flag`, `category_id`, `smaller_than_feared_flag`, `mid_thirties_reachable_flag`
- `food.price.fact_margin_bridge`: `fiscal_quarter_id`, `effect_rate`, `category_id`, `driver_code`, `quarter_code_within_year`
- `food.supply.fact_inflation_path`: `fiscal_quarter_id`, `quarter_inflation_rate`, `rest_of_year_rate`, `exit_rate`, `similar_three_quarters_flag`, `fourth_quarter_step_up_flag`, `net_includes_refund_flag`
- `food.supply.fact_input_inflation_case`: `fiscal_quarter_id`, `assumed_rate`, `hedged_share_rate`, `fuel_in_range_flag`, `commodity_id`, `hedge_book_id`
- `food.price.fact_operating_profit`: `fiscal_quarter_id`, `profit_change_rate`, `inflation_offset_flag`, `high_end_reachable_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 FY2026 (2)

What have competitors done in key categories after General Mills' price investments, given category price/mix stayed positive?

- `food.price.fact_price_mix`: `category_id`, `competitor_id`, `price_mix_rate`, `positive_flag`, `competitor_followed_flag`, `fiscal_quarter_id`, `mix_pressure_rate`
- `food.demand.fact_volume_share`: `category_id`, `negative_category_count`, `fiscal_quarter_id`, `brand_id`, `region_id`, `country_id`, `volume_share_rate`
- `food.price.fact_competitor_price`: `competitor_id`, `category_id`, `competitor_change_rate`, `fiscal_quarter_id`, `sharp_cut_flag`, `snack_cut_flag`, `adjacent_only_flag`
- `food.price.fact_price_gap`: `category_id`, `competitor_id`, `fiscal_quarter_id`, `country_id`, `gap_rate`, `closed_flag`, `first_mover_flag`
- `food.demand.fact_category_volume`: `category_id`, `category_pounds_quantity`, `fiscal_quarter_id`, `region_id`, `country_id`, `volume_quantity`, `volume_change_rate`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 FY2026 (6)

For General Mills, if organic sales stabilize in fiscal 2027, can gross margin return to the mid-30s rather than the low-30s?

- `food.price.fact_gross_margin`: `fiscal_quarter_id`, `gross_margin_rate`, `smaller_than_feared_flag`, `category_id`, `inventory_phasing_drag_rate`, `flat_if_ranges_match_inflation_flag`, `mid_thirties_reachable_flag`
- `food.price.fact_margin_bridge`: `fiscal_quarter_id`, `category_id`, `effect_rate`, `driver_code`, `quarter_code_within_year`
- `food.demand.fact_organic_result`: `fiscal_quarter_id`, `organic_sales_rate`, `category_id`, `region_id`, `channel_id`, `volume_contributed_flag`, `price_contributed_flag`
- `food.demand.fact_guidance_volume`: `fiscal_quarter_id`, `region_id`, `category_id`, `volume_case_rate`, `high_end_flag`, `positive_year_flag`, `swing_code`
- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `commodity_id`, `contract_cost_amount`, `inflation_rate`, `exit_rate`, `band_code`, `phased_quarter_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 FY2026 (1)

After a large peer cut prices sharply, will other competitors have to follow, and does General Mills still have a first-mover advantage on closing price gaps?

- `food.price.fact_price_gap`: `competitor_id`, `first_mover_flag`, `followers_must_move_flag`, `fiscal_quarter_id`, `category_id`, `country_id`, `gap_rate`
- `food.category.dim_competitor`: `competitor_name`, `competitor_code`
- `food.price.fact_competitor_price`: `competitor_id`, `competitor_change_rate`, `sharp_cut_flag`, `fiscal_quarter_id`, `category_id`, `snack_cut_flag`, `adjacent_only_flag`
- `food.demand.fact_consumption`: `fiscal_quarter_id`, `category_id`, `channel_id`, `brand_id`, `consumption_quantity`, `consumption_change_rate`, `healthier_than_shipments_flag`
- `food.demand.fact_volume_share`: `fiscal_quarter_id`, `category_id`, `brand_id`, `region_id`, `country_id`, `volume_share_rate`, `share_change_rate`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 FY2026 (5)

For General Mills, are larger promotions needed because shoppers are waiting for deals, and how does everyday-low-price compare with high-low in this environment versus past downturns?

- `food.price.fact_marketing_response`: `promotion_id`, `fiscal_quarter_id`, `category_id`, `response_rate`, `restored_flag`, `pre_covid_comparable_flag`, `vehicle_code`
- `food.price.dim_promotion`: `promotion_name`, `promotion_code`
- `food.price.fact_architecture_result`: `price_pack_id`, `promotion_id`, `everyday_versus_high_low_code`, `deeper_promo_needed_flag`, `fiscal_quarter_id`, `category_id`, `result_rate`
- `food.price.dim_price_pack`: `category_id`, `pack_name`, `pack_code`
- `food.demand.fact_consumer_demand`: `consumer_cohort_id`, `promo_waiting_faded_flag`, `fiscal_quarter_id`, `category_id`, `confidence_index`, `fragile_flag`, `insight_code`
- `food.category.dim_consumer_cohort`: `cohort_name`, `cohort_code`

### Q2 FY2026 (8)

For General Mills, how much holistic margin management benefit is still to come, and how does it phase between the third and fourth quarters?

- `food.price.fact_gross_margin`: `fiscal_quarter_id`, `gross_margin_rate`, `category_id`, `inventory_phasing_drag_rate`, `smaller_than_feared_flag`, `flat_if_ranges_match_inflation_flag`, `mid_thirties_reachable_flag`
- `food.price.fact_margin_bridge`: `fiscal_quarter_id`, `quarter_code_within_year`, `category_id`, `effect_rate`, `driver_code`
- `food.supply.fact_productivity`: `fiscal_quarter_id`, `cost_program_id`, `savings_amount`, `remaining_amount`, `offsets_inflation_flag`, `visible_if_compete_worsens_flag`, `different_from_prior_flag`
- `food.supply.fact_holistic_margin`: `fiscal_quarter_id`, `third_quarter_share_rate`, `fourth_quarter_share_rate`, `cost_program_id`, `remaining_savings_amount`
- `food.supply.dim_cost_program`: `program_name`, `program_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 FY2026 (11)

For General Mills, what share of the portfolio has had price investment, and if the cost-to-compete environment worsens, what savings are visible to respond?

- `food.price.fact_list_price`: `price_action_id`, `share_gain_in_plan_rate`, `fiscal_quarter_id`, `category_id`, `brand_id`, `region_id`, `list_change_rate`
- `food.price.fact_realized_price`: `price_action_id`, `flat_while_cost_down_flag`, `fiscal_quarter_id`, `category_id`, `country_id`, `region_id`, `realized_change_rate`
- `food.price.fact_price_investment`: `price_action_id`, `invested_share_rate`, `untreated_share_rate`, `fiscal_quarter_id`, `category_id`, `brand_id`, `lapped_flag`
- `food.category.dim_category`: `category_name`, `category_code`
- `food.supply.fact_productivity`: `cost_program_id`, `savings_amount`, `visible_if_compete_worsens_flag`, `fiscal_quarter_id`, `remaining_amount`, `offsets_inflation_flag`, `different_from_prior_flag`
- `food.price.fact_margin_bridge`: `fiscal_quarter_id`, `category_id`, `effect_rate`, `driver_code`, `quarter_code_within_year`

### Q2 FY2026 (12)

For General Mills, what is the current Wilderness strategy, and what changes are possible?

- `food.price.fact_pet_price`: `planned_change_rate`, `strategy_code`, `change_possible_flag`, `fiscal_quarter_id`, `brand_id`, `category_id`
- `food.demand.fact_brand_volume`: `volume_change_rate`, `fiscal_quarter_id`, `brand_id`, `category_id`, `channel_id`, `volume_quantity`, `incremental_flag`
- `food.demand.fact_pet_volume`: `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `brand_id`, `consumer_cohort_id`, `volume_quantity`, `cyclical_visit_flag`
- `food.supply.fact_retailer_inventory`: `fiscal_quarter_id`, `retailer_id`, `category_id`, `channel_id`, `acquisition_id`, `inventory_quantity`, `expected_reduction_quantity`
- `food.price.fact_list_price`: `price_action_id`, `list_change_rate`, `share_gain_in_plan_rate`, `fiscal_quarter_id`, `category_id`, `brand_id`, `region_id`
- `food.price.fact_realized_price`: `price_action_id`, `realized_change_rate`, `landed_rate`, `fiscal_quarter_id`, `category_id`, `country_id`, `region_id`

### Q2 FY2026 (14)

For General Mills, in the portion of the portfolio where price adjustments and remarkability are still missing the high hit rate, is there a common thread beyond Totino's?

- `food.price.fact_list_price`: `price_action_id`, `list_change_rate`, `share_gain_in_plan_rate`, `fiscal_quarter_id`, `category_id`, `brand_id`, `region_id`
- `food.price.fact_realized_price`: `price_action_id`, `realized_change_rate`, `landed_rate`, `fiscal_quarter_id`, `category_id`, `country_id`, `region_id`
- `food.demand.fact_share_destination`: `private_label_share_rate`, `insurgent_share_rate`, `remarkability_recovers_flag`, `fiscal_quarter_id`, `category_id`, `competitor_id`, `channel_id`
- `food.price.fact_price_investment`: `price_action_id`, `invested_share_rate`, `untreated_share_rate`, `hit_rate`, `common_thread_flag`, `fiscal_quarter_id`, `category_id`
- `food.demand.fact_snack_volume`: `volume_change_rate`, `high_single_digit_decline_flag`, `fiscal_quarter_id`, `category_id`, `brand_id`, `competitor_id`, `volume_quantity`
- `food.category.dim_brand`: `category_id`, `brand_name`, `brand_code`
