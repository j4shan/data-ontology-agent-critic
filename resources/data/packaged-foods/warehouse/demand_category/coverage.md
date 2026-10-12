# Food Inc category demand

Category demand owns categories, brands, channels, and geography for Food Inc. Volume, consumption, share counts, and elasticity are demand facts. They store quantities and rates, not a list price and not a commodity cost.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| — | — | This slice does not borrow an identity. |

## Numbered questions

## Mondelez

### Q1 2026 (1)

For Mondelez, what is driving emerging markets, and where are developed markets improving, including the return to volume-share growth in European chocolate and the March inflection in U.S. biscuits that justified flexibility in the 2026 guide?

- `food.demand.fact_emerging_volume`: `volume_quantity`, `growth_rate`, `fiscal_quarter_id`, `region_id`, `category_id`, `driver_code`
- `food.demand.fact_elasticity`: `fiscal_quarter_id`, `category_id`, `country_id`, `consumer_cohort_id`, `elasticity_rate`, `trade_down_rate`, `fatigue_flag`
- `food.demand.fact_chocolate_volume`: `volume_quantity`, `volume_change_rate`, `share_growth_flag`, `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`
- `food.price.fact_chocolate_margin`: `fiscal_quarter_id`, `category_id`, `region_id`, `profit_rate`, `back_to_pre_period_flag`, `recovery_starts_next_year_flag`, `neutral_after_hedge_flag`
- `food.demand.fact_biscuit_volume`: `volume_quantity`, `volume_change_rate`, `march_inflection_flag`, `fiscal_quarter_id`, `category_id`, `country_id`, `channel_id`
- `food.price.fact_competitor_price`: `fiscal_quarter_id`, `competitor_id`, `category_id`, `competitor_change_rate`, `sharp_cut_flag`, `snack_cut_flag`, `adjacent_only_flag`

### Q1 2026 (7)

For Mondelez, where is the innovation focus now that supply disruption is behind the company, and which consumer insights are shaping it?

- `food.demand.fact_innovation_demand`: `innovation_item_id`, `fiscal_quarter_id`, `category_id`, `brand_id`, `velocity_quantity`, `ahead_of_plan_flag`, `growth_versus_goal_rate`
- `food.category.dim_innovation_item`: `category_id`, `brand_id`, `item_name`, `item_code`, `item_type_code`
- `food.demand.fact_consumer_demand`: `consumer_cohort_id`, `insight_code`, `fiscal_quarter_id`, `category_id`, `confidence_index`, `promo_waiting_faded_flag`, `fragile_flag`
- `food.category.dim_consumer_cohort`: `cohort_name`, `cohort_code`
- `food.price.fact_marketing_response`: `fiscal_quarter_id`, `promotion_id`, `category_id`, `response_rate`, `restored_flag`, `pre_covid_comparable_flag`, `vehicle_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (8)

For Mondelez, can North America improve toward low-single-digit growth this year even if U.S. consumer confidence weakens because of the Middle East conflict?

- `food.demand.fact_developed_volume`: `north_america_growth_rate`, `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `volume_quantity`, `improving_flag`
- `food.demand.fact_organic_result`: `organic_sales_rate`, `fiscal_quarter_id`, `category_id`, `region_id`, `channel_id`, `volume_contributed_flag`, `price_contributed_flag`
- `food.demand.fact_consumer_demand`: `consumer_cohort_id`, `confidence_index`, `fiscal_quarter_id`, `category_id`, `promo_waiting_faded_flag`, `fragile_flag`, `insight_code`
- `food.demand.fact_guidance_volume`: `positive_year_flag`, `fiscal_quarter_id`, `region_id`, `category_id`, `volume_case_rate`, `high_end_flag`, `swing_code`
- `food.geography.dim_region`: `region_name`, `region_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (9)

For Mondelez, what growth and route-to-market changes come from the new North America biscuit supply-chain modernization beyond earlier plant consolidation?

- `food.demand.fact_biscuit_volume`: `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `country_id`, `channel_id`, `volume_quantity`, `march_inflection_flag`
- `food.supply.fact_modernization`: `plant_id`, `fiscal_quarter_id`, `cost_program_id`, `category_id`, `in_place_flag`, `new_program_flag`, `early_target_flag`
- `food.supply.fact_plant_capacity`: `plant_id`, `modernization_flag`, `route_change_flag`, `fiscal_quarter_id`, `cost_program_id`, `category_id`, `capacity_quantity`
- `food.supply.dim_plant`: `plant_name`, `plant_code`, `country_id`, `category_id`
- `food.category.dim_category`: `category_name`, `category_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (1)

For Mondelez, where does the chocolate strategy stand after the drop in cocoa, and how does it play out from here?

- `food.demand.fact_chocolate_volume`: `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`, `volume_quantity`, `share_growth_flag`
- `food.price.fact_chocolate_margin`: `profit_rate`, `neutral_after_hedge_flag`, `fiscal_quarter_id`, `category_id`, `region_id`, `back_to_pre_period_flag`, `recovery_starts_next_year_flag`
- `food.supply.fact_commodity_cost`: `inflation_rate`, `exit_rate`, `fiscal_quarter_id`, `commodity_id`, `contract_cost_amount`, `band_code`, `phased_quarter_code`
- `food.supply.fact_spot_path`: `fiscal_quarter_id`, `commodity_id`, `spot_cost_amount`, `fell_then_stabilized_flag`, `second_half_case_code`
- `food.price.fact_list_price`: `price_action_id`, `list_change_rate`, `share_gain_in_plan_rate`, `usable_after_reset_flag`, `fiscal_quarter_id`, `category_id`, `brand_id`
- `food.price.fact_realized_price`: `price_action_id`, `realized_change_rate`, `landed_rate`, `fiscal_quarter_id`, `category_id`, `country_id`, `region_id`

### Q4 2025 (4)

For Mondelez, is North America weakness cyclical or structural, and what pricing actions follow a large peer cutting snack prices?

- `food.demand.fact_developed_volume`: `volume_quantity`, `north_america_growth_rate`, `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `improving_flag`
- `food.demand.fact_biscuit_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `country_id`, `channel_id`, `march_inflection_flag`
- `food.price.fact_list_price`: `price_action_id`, `peer_raising_flag`, `fiscal_quarter_id`, `category_id`, `brand_id`, `region_id`, `list_change_rate`
- `food.price.fact_realized_price`: `price_action_id`, `fiscal_quarter_id`, `category_id`, `country_id`, `region_id`, `realized_change_rate`, `negotiation_open_flag`
- `food.price.fact_competitor_price`: `competitor_id`, `competitor_change_rate`, `snack_cut_flag`, `fiscal_quarter_id`, `category_id`, `sharp_cut_flag`, `adjacent_only_flag`
- `food.price.fact_price_gap`: `competitor_id`, `fiscal_quarter_id`, `category_id`, `country_id`, `gap_rate`, `closed_flag`, `first_mover_flag`

### Q4 2025 (7)

For Mondelez, what will grow Latin America volumes after a couple of down years, and what volume assumption is in guidance?

- `food.demand.fact_regional_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `improving_flag`
- `food.demand.fact_guidance_volume`: `volume_case_rate`, `positive_year_flag`, `fiscal_quarter_id`, `region_id`, `category_id`, `high_end_flag`, `swing_code`
- `food.price.fact_earnings_outlook`: `fiscal_quarter_id`, `in_algorithm_flag`, `top_line_same_way_flag`, `refill_enough_flag`, `pulled_forward_flag`, `cocoa_savings_kept_as_flexibility_rate`
- `food.geography.dim_region`: `region_name`, `region_code`
- `food.demand.fact_organic_result`: `volume_contributed_flag`, `fiscal_quarter_id`, `category_id`, `region_id`, `channel_id`, `organic_sales_rate`, `price_contributed_flag`
- `food.time.dim_fiscal_quarter`: `guidance_horizon`, `quarter_label`, `quarter_code`

### Q4 2025 (8)

For Mondelez, in which regions should the 2026 volume trajectory change show up, and are North America channel strategies a material driver?

- `food.demand.fact_category_volume`: `region_id`, `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `country_id`, `category_pounds_quantity`
- `food.demand.fact_regional_volume`: `region_id`, `volume_quantity`, `volume_change_rate`, `driver_flag`, `fiscal_quarter_id`, `country_id`, `category_id`
- `food.demand.fact_brazil_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `country_id`, `category_id`, `exit_flag`, `strategic_fit_flag`
- `food.geography.dim_country`: `region_id`, `country_name`, `country_code`
- `food.demand.fact_channel_volume`: `channel_id`, `volume_quantity`, `volume_change_rate`, `material_driver_flag`, `fiscal_quarter_id`, `category_id`, `retailer_id`
- `food.category.dim_channel`: `channel_name`, `channel_code`

### Q4 2025 (10)

For Mondelez, is there a path for European chocolate profit back to pre-2025 levels, and does that recovery start in 2027 as prices come down?

- `food.demand.fact_chocolate_volume`: `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `share_growth_flag`
- `food.price.fact_chocolate_margin`: `profit_rate`, `back_to_pre_period_flag`, `recovery_starts_next_year_flag`, `fiscal_quarter_id`, `category_id`, `region_id`, `neutral_after_hedge_flag`
- `food.price.fact_profit_pool`: `profit_amount`, `fiscal_quarter_id`, `category_id`, `channel_id`, `protect_pool_flag`, `tradeoff_required_flag`, `growth_realistic_flag`
- `food.price.fact_list_price`: `price_action_id`, `fiscal_quarter_id`, `category_id`, `brand_id`, `region_id`, `list_change_rate`, `held_flat_flag`
- `food.price.fact_realized_price`: `price_action_id`, `flat_while_cost_down_flag`, `fiscal_quarter_id`, `category_id`, `country_id`, `region_id`, `realized_change_rate`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (11)

For Mondelez, which in-year milestones, such as retailer-brand pricing and the company's own elasticity, will show whether the chocolate plan is working?

- `food.demand.fact_retailer_brand_demand`: `retailer_brand_volume_quantity`, `pricing_landed_flag`, `fiscal_quarter_id`, `competitor_id`, `category_id`, `country_id`
- `food.price.fact_price_gap`: `fiscal_quarter_id`, `category_id`, `country_id`, `competitor_id`, `gap_rate`, `closed_flag`, `first_mover_flag`
- `food.demand.fact_elasticity`: `elasticity_rate`, `fiscal_quarter_id`, `category_id`, `country_id`, `consumer_cohort_id`, `trade_down_rate`, `fatigue_flag`
- `food.demand.fact_organic_result`: `price_contributed_flag`, `fiscal_quarter_id`, `category_id`, `region_id`, `channel_id`, `organic_sales_rate`, `volume_contributed_flag`
- `food.demand.fact_chocolate_volume`: `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `share_growth_flag`
- `food.price.fact_chocolate_margin`: `recovery_starts_next_year_flag`, `fiscal_quarter_id`, `category_id`, `region_id`, `profit_rate`, `back_to_pre_period_flag`, `neutral_after_hedge_flag`

### Q3 2025 (3)

For Mondelez, what is the path for the U.S. business back to growth?

- `food.demand.fact_developed_volume`: `volume_quantity`, `north_america_growth_rate`, `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `improving_flag`
- `food.demand.fact_biscuit_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `country_id`, `channel_id`, `march_inflection_flag`
- `food.demand.fact_organic_result`: `organic_sales_rate`, `volume_contributed_flag`, `fiscal_quarter_id`, `category_id`, `region_id`, `channel_id`, `price_contributed_flag`
- `food.demand.fact_guidance_volume`: `volume_case_rate`, `fiscal_quarter_id`, `region_id`, `category_id`, `high_end_flag`, `positive_year_flag`, `swing_code`
- `food.demand.fact_regional_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `improving_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (4)

For Mondelez, if next year's earnings can be described relative to the algorithm, should the top line be thought of the same way?

- `food.demand.fact_organic_result`: `organic_sales_rate`, `versus_algorithm_flag`, `fiscal_quarter_id`, `category_id`, `region_id`, `channel_id`, `volume_contributed_flag`
- `food.demand.fact_guidance_volume`: `positive_year_flag`, `fiscal_quarter_id`, `region_id`, `category_id`, `volume_case_rate`, `high_end_flag`, `swing_code`
- `food.price.fact_earnings_outlook`: `in_algorithm_flag`, `top_line_same_way_flag`, `fiscal_quarter_id`, `refill_enough_flag`, `pulled_forward_flag`, `cocoa_savings_kept_as_flexibility_rate`
- `food.demand.fact_regional_volume`: `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `volume_quantity`, `volume_change_rate`, `improving_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (5)

For Mondelez, in emerging markets, where is elasticity showing fatigue or price-gap problems versus behaving as expected?

- `food.demand.fact_emerging_volume`: `volume_quantity`, `fiscal_quarter_id`, `region_id`, `category_id`, `growth_rate`, `driver_code`
- `food.demand.fact_elasticity`: `elasticity_rate`, `fatigue_flag`, `fiscal_quarter_id`, `category_id`, `country_id`, `consumer_cohort_id`, `trade_down_rate`
- `food.demand.fact_organic_result`: `volume_contributed_flag`, `price_contributed_flag`, `versus_algorithm_flag`, `fiscal_quarter_id`, `category_id`, `region_id`, `channel_id`
- `food.demand.fact_category_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`, `category_pounds_quantity`
- `food.demand.fact_regional_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `improving_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (6)

For Mondelez, is the implied fourth-quarter organic-sales step-up mostly Europe, and what is expected in North America given softer recent scanner data?

- `food.demand.fact_organic_result`: `fiscal_quarter_id`, `organic_sales_rate`, `quarter_phasing_gap_rate`, `category_id`, `region_id`, `channel_id`, `volume_contributed_flag`
- `food.demand.fact_regional_volume`: `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `volume_quantity`, `volume_change_rate`, `improving_flag`
- `food.geography.dim_region`: `region_name`, `region_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (1)

For Mondelez, what second-half puts and takes, including a weaker U.S., leave full-year guidance unchanged after a strong first half?

- `food.demand.fact_developed_volume`: `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `volume_quantity`, `improving_flag`, `north_america_growth_rate`
- `food.demand.fact_guidance_volume`: `positive_year_flag`, `fiscal_quarter_id`, `region_id`, `category_id`, `volume_case_rate`, `high_end_flag`, `swing_code`
- `food.price.fact_earnings_outlook`: `fiscal_quarter_id`, `in_algorithm_flag`, `top_line_same_way_flag`, `refill_enough_flag`, `pulled_forward_flag`, `cocoa_savings_kept_as_flexibility_rate`
- `food.demand.fact_organic_result`: `organic_sales_rate`, `fiscal_quarter_id`, `category_id`, `region_id`, `channel_id`, `volume_contributed_flag`, `price_contributed_flag`
- `food.demand.fact_regional_volume`: `volume_change_rate`, `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `volume_quantity`, `improving_flag`
- `food.time.dim_fiscal_quarter`: `guidance_horizon`, `quarter_label`, `quarter_code`

### Q2 2025 (3)

For Mondelez, if U.S. biscuit category volume stays down while prices rise and the consumer is under pressure, how much U.S. pricing is planned and where could that flex the wrong way?

- `food.demand.fact_biscuit_volume`: `category_id`, `volume_quantity`, `volume_change_rate`, `category_down_flag`, `fiscal_quarter_id`, `country_id`, `channel_id`
- `food.price.fact_competitor_price`: `category_id`, `fiscal_quarter_id`, `competitor_id`, `competitor_change_rate`, `sharp_cut_flag`, `snack_cut_flag`, `adjacent_only_flag`
- `food.demand.fact_category_volume`: `category_id`, `volume_quantity`, `volume_change_rate`, `category_pounds_quantity`, `fiscal_quarter_id`, `region_id`, `country_id`
- `food.category.dim_category`: `category_name`, `category_code`
- `food.price.fact_list_price`: `category_id`, `price_action_id`, `share_gain_in_plan_rate`, `fiscal_quarter_id`, `brand_id`, `region_id`, `list_change_rate`
- `food.price.fact_realized_price`: `category_id`, `price_action_id`, `flat_while_cost_down_flag`, `fiscal_quarter_id`, `country_id`, `region_id`, `realized_change_rate`

### Q2 2025 (4)

For Mondelez, how is GLP-1 use, including expected pill forms, affecting indulgent snacking, and could North America volume stay under pressure?

- `food.demand.fact_glp_demand`: `affected_volume_change_rate`, `pill_form_flag`, `fiscal_quarter_id`, `category_id`, `consumer_cohort_id`, `region_id`, `longer_than_value_seeking_flag`
- `food.category.dim_consumer_cohort`: `cohort_name`, `cohort_code`
- `food.demand.fact_developed_volume`: `volume_quantity`, `north_america_growth_rate`, `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `improving_flag`
- `food.demand.fact_biscuit_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `country_id`, `channel_id`, `march_inflection_flag`
- `food.category.dim_category`: `category_name`, `category_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

## General Mills

### Q1 FY2027 (1)

For General Mills, should North America Retail improve further from the minus 2% retail consumption in the quarter, or stabilize around that rate?

- `food.demand.fact_consumption`: `fiscal_quarter_id`, `consumption_quantity`, `consumption_change_rate`, `stabilize_flag`, `category_id`, `channel_id`, `brand_id`
- `food.demand.fact_volume_share`: `fiscal_quarter_id`, `volume_share_rate`, `share_change_rate`, `category_id`, `brand_id`, `region_id`, `country_id`
- `food.supply.fact_retailer_inventory`: `fiscal_quarter_id`, `refill_quarter_flag`, `retailer_id`, `category_id`, `channel_id`, `acquisition_id`, `inventory_quantity`
- `food.category.dim_channel`: `channel_name`, `channel_code`
- `food.demand.fact_share_destination`: `fiscal_quarter_id`, `private_label_share_rate`, `insurgent_share_rate`, `category_id`, `competitor_id`, `channel_id`, `not_mainly_private_label_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 FY2027 (2)

For General Mills, versus a year ago, in how many North America Retail categories are volume and share still negative, and what is the fix in the remaining problem categories?

- `food.demand.fact_consumption`: `fiscal_quarter_id`, `category_id`, `channel_id`, `brand_id`, `consumption_quantity`, `consumption_change_rate`, `healthier_than_shipments_flag`
- `food.demand.fact_volume_share`: `volume_share_rate`, `share_change_rate`, `negative_category_count`, `fiscal_quarter_id`, `category_id`, `brand_id`, `region_id`
- `food.demand.fact_category_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`, `category_pounds_quantity`
- `food.demand.fact_regional_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `improving_flag`
- `food.demand.fact_share_destination`: `private_label_share_rate`, `insurgent_share_rate`, `fiscal_quarter_id`, `category_id`, `competitor_id`, `channel_id`, `not_mainly_private_label_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 FY2027 (4)

For General Mills, how much of the low-single-digit pet headwind is caution versus the first quarter simply having a smaller retailer-inventory hit than expected, aside from the extra month of Whitebridge?

- `food.demand.fact_pet_volume`: `fiscal_quarter_id`, `category_id`, `brand_id`, `consumer_cohort_id`, `volume_quantity`, `volume_change_rate`, `cyclical_visit_flag`
- `food.supply.fact_retailer_inventory`: `fiscal_quarter_id`, `retailer_id`, `inventory_quantity`, `expected_reduction_quantity`, `smaller_than_expected_flag`, `refill_quarter_flag`, `category_id`
- `food.category.dim_retailer`: `retailer_name`, `retailer_code`, `channel_id`
- `food.supply.fact_acquisition_timing`: `fiscal_quarter_id`, `extra_month_count`, `in_quarter_flag`, `acquisition_id`
- `food.price.fact_pet_price`: `fiscal_quarter_id`, `brand_id`, `category_id`, `planned_change_rate`, `strategy_code`, `change_possible_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 FY2027 (5)

For General Mills, how incremental was Love Made Fresh in dog food, and is the high-single-digit dog-food decline mostly Wilderness or other lines?

- `food.demand.fact_pet_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `brand_id`, `consumer_cohort_id`, `cyclical_visit_flag`
- `food.category.dim_category`: `category_name`, `category_code`
- `food.demand.fact_brand_volume`: `volume_quantity`, `volume_change_rate`, `incremental_flag`, `fiscal_quarter_id`, `brand_id`, `category_id`, `channel_id`
- `food.demand.fact_innovation_demand`: `fiscal_quarter_id`, `innovation_item_id`, `category_id`, `brand_id`, `velocity_quantity`, `ahead_of_plan_flag`, `growth_versus_goal_rate`
- `food.price.fact_pet_price`: `fiscal_quarter_id`, `brand_id`, `category_id`, `planned_change_rate`, `strategy_code`, `change_possible_flag`
- `food.demand.fact_category_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`, `category_pounds_quantity`

### Q1 FY2027 (6)

For General Mills, how is the small wet-dog-food business performing?

- `food.demand.fact_pet_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `brand_id`, `consumer_cohort_id`, `cyclical_visit_flag`
- `food.category.dim_category`: `category_name`, `category_code`
- `food.demand.fact_category_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`, `category_pounds_quantity`
- `food.demand.fact_regional_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `improving_flag`
- `food.demand.fact_brand_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `brand_id`, `category_id`, `channel_id`, `incremental_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 FY2027 (7)

For General Mills, which innovation and renovation is tracking ahead of plan, what that says about the consumer, and what cereal acceleration is still to come?

- `food.demand.fact_innovation_demand`: `innovation_item_id`, `ahead_of_plan_flag`, `fiscal_quarter_id`, `category_id`, `brand_id`, `velocity_quantity`, `growth_versus_goal_rate`
- `food.category.dim_innovation_item`: `category_id`, `brand_id`, `item_name`, `item_code`, `item_type_code`
- `food.demand.fact_cereal_volume`: `acceleration_still_ahead_flag`, `fiscal_quarter_id`, `category_id`, `brand_id`, `volume_quantity`, `matched_other_categories_flag`
- `food.price.fact_architecture_result`: `matched_cereal_flag`, `fiscal_quarter_id`, `price_pack_id`, `category_id`, `promotion_id`, `result_rate`, `everyday_versus_high_low_code`
- `food.demand.fact_consumer_demand`: `consumer_cohort_id`, `fiscal_quarter_id`, `category_id`, `confidence_index`, `promo_waiting_faded_flag`, `fragile_flag`, `insight_code`
- `food.category.dim_consumer_cohort`: `cohort_name`, `cohort_code`

### Q1 FY2027 (15)

For General Mills, as shoppers use AI-generated lists at Instacart and Kroger, how does the company stay selected when the decision happens off the physical shelf?

- `food.demand.fact_digital_selection`: `selected_rate`, `retail_media_flag`, `fiscal_quarter_id`, `retailer_id`, `category_id`, `in_store_activation_flag`
- `food.category.dim_retailer`: `channel_id`, `retailer_name`, `retailer_code`
- `food.price.dim_media_vehicle`: `vehicle_name`, `vehicle_code`
- `food.demand.fact_consumer_demand`: `consumer_cohort_id`, `fiscal_quarter_id`, `category_id`, `confidence_index`, `promo_waiting_faded_flag`, `fragile_flag`, `insight_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 FY2027 (16)

For General Mills, in pet, how much of the pressure is cyclical household and vet-visit softness versus the structural aging of large dogs where the margin sits?

- `food.demand.fact_pet_volume`: `consumer_cohort_id`, `cyclical_visit_flag`, `large_dog_structural_flag`, `fiscal_quarter_id`, `category_id`, `brand_id`, `volume_quantity`
- `food.supply.fact_retailer_inventory`: `fiscal_quarter_id`, `retailer_id`, `category_id`, `channel_id`, `acquisition_id`, `inventory_quantity`, `expected_reduction_quantity`
- `food.demand.fact_consumer_demand`: `consumer_cohort_id`, `fiscal_quarter_id`, `category_id`, `confidence_index`, `promo_waiting_faded_flag`, `fragile_flag`, `insight_code`
- `food.category.dim_consumer_cohort`: `cohort_name`, `cohort_code`
- `food.price.fact_gross_margin`: `gross_margin_rate`, `fiscal_quarter_id`, `category_id`, `inventory_phasing_drag_rate`, `smaller_than_feared_flag`, `flat_if_ranges_match_inflation_flag`, `mid_thirties_reachable_flag`
- `food.price.fact_margin_bridge`: `fiscal_quarter_id`, `category_id`, `effect_rate`, `driver_code`, `quarter_code_within_year`

### Q4 FY2026 (3)

For General Mills, is category growth still below long-term trends for cyclical reasons?

- `food.demand.fact_category_volume`: `category_id`, `category_pounds_quantity`, `below_trend_flag`, `cyclical_flag`, `fiscal_quarter_id`, `region_id`, `country_id`
- `food.demand.fact_scanner_demand`: `category_id`, `category_dollar_growth_rate`, `fiscal_quarter_id`, `region_id`, `scanner_change_rate`, `softer_flag`
- `food.demand.fact_consumer_demand`: `consumer_cohort_id`, `category_id`, `fiscal_quarter_id`, `confidence_index`, `promo_waiting_faded_flag`, `fragile_flag`, `insight_code`
- `food.category.dim_consumer_cohort`: `cohort_name`, `cohort_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 FY2026 (4)

For General Mills, how far below the full-year organic-sales guide should the first quarter start, and how does growth phase after that?

- `food.demand.fact_organic_result`: `fiscal_quarter_id`, `organic_sales_rate`, `quarter_phasing_gap_rate`, `category_id`, `region_id`, `channel_id`, `volume_contributed_flag`
- `food.demand.fact_guidance_volume`: `fiscal_quarter_id`, `positive_year_flag`, `region_id`, `category_id`, `volume_case_rate`, `high_end_flag`, `swing_code`
- `food.demand.fact_regional_volume`: `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `volume_quantity`, `volume_change_rate`, `improving_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 FY2026 (5)

For General Mills, what should be expected for volume share and value share?

- `food.demand.fact_volume_share`: `volume_share_rate`, `share_change_rate`, `fiscal_quarter_id`, `category_id`, `brand_id`, `region_id`, `country_id`
- `food.price.fact_value_share`: `value_share_rate`, `dollar_share_rate`, `gap_to_volume_share_rate`, `fiscal_quarter_id`, `category_id`, `channel_id`, `narrowing_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 FY2026 (6)

For General Mills, if North America Retail dollar-share losses are not mainly private label, how much has gone to smaller insurgent brands, and how does the remarkability work take it back?

- `food.demand.fact_consumption`: `brand_id`, `fiscal_quarter_id`, `category_id`, `channel_id`, `consumption_quantity`, `consumption_change_rate`, `healthier_than_shipments_flag`
- `food.demand.fact_volume_share`: `brand_id`, `volume_share_rate`, `share_change_rate`, `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`
- `food.price.fact_value_share`: `value_share_rate`, `dollar_share_rate`, `gap_to_volume_share_rate`, `fiscal_quarter_id`, `category_id`, `channel_id`, `narrowing_flag`
- `food.demand.fact_scanner_demand`: `category_dollar_growth_rate`, `fiscal_quarter_id`, `category_id`, `region_id`, `scanner_change_rate`, `softer_flag`
- `food.demand.fact_share_destination`: `private_label_share_rate`, `insurgent_share_rate`, `not_mainly_private_label_flag`, `remarkability_recovers_flag`, `fiscal_quarter_id`, `category_id`, `competitor_id`
- `food.category.dim_competitor`: `competitor_name`, `competitor_code`

### Q4 FY2026 (9)

For General Mills, how do at-home spending trends differ by income cohort, and where does improvement come from in fiscal 2027?

- `food.demand.fact_cohort_demand`: `fiscal_quarter_id`, `consumer_cohort_id`, `trade_down_from_restaurants_flag`, `improvement_source_flag`, `category_id`, `demand_quantity`, `trade_up_to_small_brands_flag`
- `food.category.dim_consumer_cohort`: `cohort_name`, `cohort_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 FY2026 (12)

For General Mills, what has to happen to reach the high end of the organic-sales range and positive growth for the year?

- `food.demand.fact_organic_result`: `organic_sales_rate`, `fiscal_quarter_id`, `category_id`, `region_id`, `channel_id`, `volume_contributed_flag`, `price_contributed_flag`
- `food.demand.fact_guidance_volume`: `high_end_flag`, `positive_year_flag`, `fiscal_quarter_id`, `region_id`, `category_id`, `volume_case_rate`, `swing_code`
- `food.demand.fact_regional_volume`: `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `volume_quantity`, `volume_change_rate`, `improving_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 FY2026 (13)

For General Mills, is there visibility that pet retailer-inventory swings will smooth out, given consumption has been healthier than reported results?

- `food.demand.fact_pet_volume`: `fiscal_quarter_id`, `category_id`, `brand_id`, `consumer_cohort_id`, `volume_quantity`, `volume_change_rate`, `cyclical_visit_flag`
- `food.supply.fact_retailer_inventory`: `retailer_id`, `inventory_quantity`, `smaller_than_expected_flag`, `fiscal_quarter_id`, `category_id`, `channel_id`, `acquisition_id`
- `food.category.dim_retailer`: `retailer_name`, `retailer_code`, `channel_id`
- `food.demand.fact_consumption`: `consumption_quantity`, `consumption_change_rate`, `healthier_than_shipments_flag`, `fiscal_quarter_id`, `category_id`, `channel_id`, `brand_id`
- `food.price.fact_pet_price`: `fiscal_quarter_id`, `brand_id`, `category_id`, `planned_change_rate`, `strategy_code`, `change_possible_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 FY2026 (1)

For General Mills, once this year's price investments and remarkability work are lapped, can volume grow in fiscal 2027 even if category growth stays below its long-term rate?

- `food.demand.fact_category_volume`: `fiscal_quarter_id`, `category_id`, `volume_quantity`, `volume_change_rate`, `category_pounds_quantity`, `below_trend_flag`, `region_id`
- `food.demand.fact_regional_volume`: `fiscal_quarter_id`, `category_id`, `volume_quantity`, `volume_change_rate`, `region_id`, `country_id`, `improving_flag`
- `food.price.fact_list_price`: `fiscal_quarter_id`, `category_id`, `price_action_id`, `list_change_rate`, `share_gain_in_plan_rate`, `brand_id`, `region_id`
- `food.price.fact_realized_price`: `fiscal_quarter_id`, `category_id`, `price_action_id`, `realized_change_rate`, `landed_rate`, `country_id`, `region_id`
- `food.demand.fact_scanner_demand`: `fiscal_quarter_id`, `category_id`, `scanner_change_rate`, `category_dollar_growth_rate`, `region_id`, `softer_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 FY2026 (3)

For General Mills, how is this year's innovation tracking against the 25% growth goal, and what should seasonal events and early fiscal 2027 commentary imply?

- `food.demand.fact_innovation_demand`: `fiscal_quarter_id`, `innovation_item_id`, `growth_versus_goal_rate`, `category_id`, `brand_id`, `velocity_quantity`, `ahead_of_plan_flag`
- `food.category.dim_innovation_item`: `category_id`, `brand_id`, `item_name`, `item_code`, `item_type_code`
- `food.demand.fact_seasonal_demand`: `fiscal_quarter_id`, `innovation_item_id`, `seasonal_quantity`, `occasion_id`, `on_slate_flag`
- `food.price.fact_marketing_response`: `fiscal_quarter_id`, `promotion_id`, `category_id`, `response_rate`, `restored_flag`, `pre_covid_comparable_flag`, `vehicle_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 FY2026 (4)

For General Mills, how large is the recent Love Made Fresh acceleration, how much more distribution is available, and how is on-shelf availability tracking?

- `food.demand.fact_brand_volume`: `fiscal_quarter_id`, `brand_id`, `category_id`, `channel_id`, `volume_quantity`, `volume_change_rate`, `incremental_flag`
- `food.demand.fact_innovation_demand`: `distribution_remaining_rate`, `fiscal_quarter_id`, `innovation_item_id`, `category_id`, `brand_id`, `velocity_quantity`, `ahead_of_plan_flag`
- `food.supply.fact_distribution_doors`: `on_shelf_rate`, `more_doors_next_flag`, `fiscal_quarter_id`, `brand_id`, `innovation_item_id`, `channel_id`, `door_count`
- `food.supply.fact_availability`: `fiscal_quarter_id`, `category_id`, `plant_id`, `in_stock_rate`, `disruption_behind_flag`
- `food.category.dim_brand`: `category_id`, `brand_name`, `brand_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 FY2026 (5)

For General Mills, versus the pre-COVID period, when a similar innovation rate, restored promotion, and marketing spend stabilized organic sales, what response is each of those spends getting now?

- `food.demand.fact_innovation_demand`: `innovation_item_id`, `growth_versus_goal_rate`, `distribution_remaining_rate`, `fiscal_quarter_id`, `category_id`, `brand_id`, `velocity_quantity`
- `food.category.dim_innovation_item`: `category_id`, `brand_id`, `item_name`, `item_code`, `item_type_code`
- `food.price.fact_marketing_response`: `promotion_id`, `response_rate`, `restored_flag`, `pre_covid_comparable_flag`, `fiscal_quarter_id`, `category_id`, `vehicle_code`
- `food.price.dim_promotion`: `promotion_name`, `promotion_code`
- `food.price.fact_advertising`: `spend_amount`, `versus_normal_rate`, `step_up_rate`, `fiscal_quarter_id`, `media_vehicle_id`, `category_id`, `holds_for_year_flag`
- `food.demand.fact_organic_result`: `organic_sales_rate`, `versus_algorithm_flag`, `quarter_phasing_gap_rate`, `fiscal_quarter_id`, `category_id`, `region_id`, `channel_id`

### Q3 FY2026 (8)

For General Mills, is positive organic revenue growth in the fourth quarter still reachable for the total company, North America Retail, or both, or has the language moved to only improved trends?

- `food.demand.fact_organic_result`: `fiscal_quarter_id`, `organic_sales_rate`, `quarter_phasing_gap_rate`, `category_id`, `region_id`, `channel_id`, `volume_contributed_flag`
- `food.demand.fact_guidance_volume`: `fiscal_quarter_id`, `positive_year_flag`, `region_id`, `category_id`, `volume_case_rate`, `high_end_flag`, `swing_code`
- `food.demand.fact_consumption`: `fiscal_quarter_id`, `category_id`, `channel_id`, `brand_id`, `consumption_quantity`, `consumption_change_rate`, `healthier_than_shipments_flag`
- `food.demand.fact_volume_share`: `fiscal_quarter_id`, `returned_to_growth_flag`, `category_id`, `brand_id`, `region_id`, `country_id`, `volume_share_rate`
- `food.demand.fact_regional_volume`: `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `volume_quantity`, `volume_change_rate`, `improving_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 FY2026 (9)

For General Mills, is foodservice weakness in bakery flour volumes likely to persist, and what does it say about that channel?

- `food.demand.fact_foodservice_volume`: `channel_id`, `volume_quantity`, `flour_volume_quantity`, `says_about_channel_flag`, `fiscal_quarter_id`, `category_id`, `persists_flag`
- `food.price.fact_flour_price`: `channel_id`, `fiscal_quarter_id`, `category_id`, `pass_through_rate`, `indexed_flag`, `better_than_plan_flag`
- `food.category.dim_category`: `category_name`, `category_code`
- `food.demand.fact_category_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`, `category_pounds_quantity`
- `food.demand.fact_regional_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `improving_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 FY2026 (10)

For General Mills, after hitting the cooler-distribution goal for Love Made Fresh, is the next step more doors or higher turns in doors already won?

- `food.demand.fact_brand_volume`: `fiscal_quarter_id`, `brand_id`, `category_id`, `channel_id`, `volume_quantity`, `volume_change_rate`, `incremental_flag`
- `food.demand.fact_innovation_demand`: `velocity_quantity`, `growth_versus_goal_rate`, `distribution_remaining_rate`, `turns_before_doors_flag`, `fiscal_quarter_id`, `innovation_item_id`, `category_id`
- `food.supply.fact_distribution_doors`: `door_count`, `cooler_goal_hit_flag`, `more_doors_next_flag`, `fiscal_quarter_id`, `brand_id`, `innovation_item_id`, `channel_id`
- `food.category.dim_brand`: `category_id`, `brand_name`, `brand_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 FY2026 (11)

Are salty-snack price cuts and innovation only adjacent to General Mills, or are they taking share from its brands, and what returns snacks to growth after a high-single-digit decline?

- `food.demand.fact_snack_volume`: `brand_id`, `competitor_id`, `high_single_digit_decline_flag`, `stable_ex_brand_flag`, `competitor_taking_share_flag`, `fiscal_quarter_id`, `category_id`
- `food.price.fact_competitor_price`: `competitor_id`, `competitor_change_rate`, `snack_cut_flag`, `adjacent_only_flag`, `fiscal_quarter_id`, `category_id`, `sharp_cut_flag`
- `food.price.fact_price_gap`: `competitor_id`, `fiscal_quarter_id`, `category_id`, `country_id`, `gap_rate`, `closed_flag`, `first_mover_flag`
- `food.price.fact_list_price`: `brand_id`, `price_action_id`, `share_gain_in_plan_rate`, `usable_after_reset_flag`, `fiscal_quarter_id`, `category_id`, `region_id`
- `food.price.fact_realized_price`: `price_action_id`, `fiscal_quarter_id`, `category_id`, `country_id`, `region_id`, `realized_change_rate`, `negotiation_open_flag`
- `food.demand.fact_innovation_demand`: `innovation_item_id`, `brand_id`, `growth_versus_goal_rate`, `turns_before_doors_flag`, `fiscal_quarter_id`, `category_id`, `velocity_quantity`

### Q3 FY2026 (12)

For General Mills, excluding Totino's, is the snacks business stable?

- `food.demand.fact_snack_volume`: `stable_ex_brand_flag`, `fiscal_quarter_id`, `category_id`, `brand_id`, `competitor_id`, `volume_quantity`, `volume_change_rate`
- `food.price.fact_competitor_price`: `snack_cut_flag`, `fiscal_quarter_id`, `competitor_id`, `category_id`, `competitor_change_rate`, `sharp_cut_flag`, `adjacent_only_flag`
- `food.category.dim_brand`: `category_id`, `brand_name`, `brand_code`
- `food.price.fact_price_investment`: `fiscal_quarter_id`, `category_id`, `brand_id`, `price_action_id`, `invested_share_rate`, `untreated_share_rate`, `lapped_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 FY2026 (14)

For General Mills, what swing factors could push fourth-quarter results toward either end of a wide implied range while the full-year guide is held?

- `food.demand.fact_organic_result`: `fiscal_quarter_id`, `organic_sales_rate`, `quarter_phasing_gap_rate`, `category_id`, `region_id`, `channel_id`, `volume_contributed_flag`
- `food.demand.fact_guidance_volume`: `fiscal_quarter_id`, `positive_year_flag`, `swing_code`, `region_id`, `category_id`, `volume_case_rate`, `high_end_flag`
- `food.price.fact_profit_pool`: `fiscal_quarter_id`, `profit_amount`, `category_id`, `channel_id`, `protect_pool_flag`, `tradeoff_required_flag`, `growth_realistic_flag`
- `food.price.fact_operating_profit`: `fiscal_quarter_id`, `profit_change_rate`, `inflation_offset_flag`, `high_end_reachable_flag`
- `food.demand.fact_regional_volume`: `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `volume_quantity`, `volume_change_rate`, `improving_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 FY2026 (16)

For General Mills, what drove the decision to exit Brazil?

- `food.demand.fact_brazil_volume`: `exit_flag`, `fiscal_quarter_id`, `country_id`, `category_id`, `volume_quantity`, `volume_change_rate`, `strategic_fit_flag`
- `food.geography.dim_country`: `region_id`, `country_name`, `country_code`
- `food.demand.fact_regional_volume`: `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `volume_quantity`, `volume_change_rate`, `improving_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 FY2026 (2)

For General Mills, how fast should the gap between improving volume share and value share narrow in the third and fourth quarters as last year's prices are lapped, where should that stand entering fiscal 2027, and how does a higher cost of volume affect price/mix?

- `food.demand.fact_volume_share`: `fiscal_quarter_id`, `volume_share_rate`, `share_change_rate`, `category_id`, `brand_id`, `region_id`, `country_id`
- `food.price.fact_value_share`: `fiscal_quarter_id`, `value_share_rate`, `dollar_share_rate`, `gap_to_volume_share_rate`, `category_id`, `channel_id`, `narrowing_flag`
- `food.price.fact_price_mix`: `fiscal_quarter_id`, `price_mix_rate`, `category_id`, `competitor_id`, `positive_flag`, `competitor_followed_flag`, `mix_pressure_rate`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 FY2026 (3)

For General Mills, how is consumer behavior in the broader dog-feeding category, which has been weaker than hoped, even as core pet improves?

- `food.demand.fact_pet_volume`: `category_id`, `consumer_cohort_id`, `category_weaker_flag`, `fiscal_quarter_id`, `brand_id`, `volume_quantity`, `volume_change_rate`
- `food.demand.fact_category_volume`: `category_id`, `category_pounds_quantity`, `fiscal_quarter_id`, `region_id`, `country_id`, `volume_quantity`, `volume_change_rate`
- `food.supply.fact_retailer_inventory`: `category_id`, `smaller_than_expected_flag`, `fiscal_quarter_id`, `retailer_id`, `channel_id`, `acquisition_id`, `inventory_quantity`
- `food.demand.fact_consumer_demand`: `consumer_cohort_id`, `category_id`, `fiscal_quarter_id`, `confidence_index`, `promo_waiting_faded_flag`, `fragile_flag`, `insight_code`
- `food.category.dim_consumer_cohort`: `cohort_name`, `cohort_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 FY2026 (4)

For General Mills, can volumes stay positive after the company laps its own price cuts?

- `food.demand.fact_category_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `category_id`, `region_id`, `country_id`, `category_pounds_quantity`
- `food.demand.fact_regional_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `improving_flag`
- `food.price.fact_list_price`: `price_action_id`, `usable_after_reset_flag`, `fiscal_quarter_id`, `category_id`, `brand_id`, `region_id`, `list_change_rate`
- `food.price.fact_realized_price`: `price_action_id`, `fiscal_quarter_id`, `category_id`, `country_id`, `region_id`, `realized_change_rate`, `negotiation_open_flag`
- `food.demand.fact_organic_result`: `volume_contributed_flag`, `price_contributed_flag`, `fiscal_quarter_id`, `category_id`, `region_id`, `channel_id`, `organic_sales_rate`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 FY2026 (6)

For General Mills, beyond the first-quarter international timing benefit that was due to unwind, were there incremental timing tailwinds or headwinds in the second quarter?

- `food.demand.fact_timing_shift`: `fiscal_quarter_id`, `unwind_points`, `incremental_timing_flag`, `region_id`, `shifted_quantity`
- `food.demand.fact_regional_volume`: `fiscal_quarter_id`, `region_id`, `country_id`, `category_id`, `volume_quantity`, `volume_change_rate`, `improving_flag`
- `food.supply.fact_acquisition_timing`: `fiscal_quarter_id`, `in_quarter_flag`, `acquisition_id`, `extra_month_count`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 FY2026 (7)

For General Mills, is Love Made Fresh helping the Blue Buffalo base business, or are the two still separate?

- `food.demand.fact_brand_volume`: `volume_change_rate`, `base_separate_flag`, `fiscal_quarter_id`, `brand_id`, `category_id`, `channel_id`, `volume_quantity`
- `food.demand.fact_innovation_demand`: `growth_versus_goal_rate`, `distribution_remaining_rate`, `fiscal_quarter_id`, `innovation_item_id`, `category_id`, `brand_id`, `velocity_quantity`
- `food.category.dim_brand`: `category_id`, `brand_name`, `brand_code`
- `food.supply.fact_distribution_doors`: `on_shelf_rate`, `fiscal_quarter_id`, `brand_id`, `innovation_item_id`, `channel_id`, `door_count`, `cooler_goal_hit_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 FY2026 (9)

For General Mills, how is the higher cost of volume, expected to pressure third-quarter margins, embedded in the reaffirmed full-year outlook?

- `food.demand.fact_category_volume`: `fiscal_quarter_id`, `volume_quantity`, `volume_change_rate`, `category_id`, `region_id`, `country_id`, `category_pounds_quantity`
- `food.demand.fact_regional_volume`: `fiscal_quarter_id`, `volume_quantity`, `volume_change_rate`, `region_id`, `country_id`, `category_id`, `improving_flag`
- `food.price.fact_gross_margin`: `fiscal_quarter_id`, `gross_margin_rate`, `category_id`, `inventory_phasing_drag_rate`, `smaller_than_feared_flag`, `flat_if_ranges_match_inflation_flag`, `mid_thirties_reachable_flag`
- `food.price.fact_margin_bridge`: `fiscal_quarter_id`, `quarter_code_within_year`, `category_id`, `effect_rate`, `driver_code`
- `food.demand.fact_guidance_volume`: `fiscal_quarter_id`, `volume_case_rate`, `high_end_flag`, `positive_year_flag`, `region_id`, `category_id`, `swing_code`
- `food.price.fact_earnings_outlook`: `fiscal_quarter_id`, `in_algorithm_flag`, `top_line_same_way_flag`, `refill_enough_flag`, `pulled_forward_flag`, `cocoa_savings_kept_as_flexibility_rate`

### Q2 FY2026 (10)

For General Mills, have category pounds, which were lagging the full-year view because of a few categories, improved in the quarter?

- `food.demand.fact_category_volume`: `fiscal_quarter_id`, `category_id`, `volume_quantity`, `volume_change_rate`, `category_pounds_quantity`, `region_id`, `country_id`
- `food.category.dim_category`: `category_name`, `category_code`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 FY2026 (13)

For General Mills, which North America Retail and pet consumption measures would indicate that profit growth is realistic in fiscal 2027 after the volume-recovery year?

- `food.demand.fact_consumption`: `fiscal_quarter_id`, `consumption_quantity`, `consumption_change_rate`, `category_id`, `channel_id`, `brand_id`, `healthier_than_shipments_flag`
- `food.category.dim_channel`: `channel_name`, `channel_code`
- `food.demand.fact_pet_volume`: `fiscal_quarter_id`, `volume_quantity`, `volume_change_rate`, `category_id`, `brand_id`, `consumer_cohort_id`, `cyclical_visit_flag`
- `food.price.fact_profit_pool`: `fiscal_quarter_id`, `profit_amount`, `growth_realistic_flag`, `category_id`, `channel_id`, `protect_pool_flag`, `tradeoff_required_flag`
- `food.price.fact_operating_profit`: `fiscal_quarter_id`, `profit_change_rate`, `inflation_offset_flag`, `high_end_reachable_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 FY2026 (15)

For General Mills, which unmeasured channels are taking pet share from traditional channels?

- `food.demand.fact_pet_volume`: `fiscal_quarter_id`, `category_id`, `brand_id`, `consumer_cohort_id`, `volume_quantity`, `volume_change_rate`, `cyclical_visit_flag`
- `food.supply.fact_retailer_inventory`: `channel_id`, `fiscal_quarter_id`, `retailer_id`, `category_id`, `acquisition_id`, `inventory_quantity`, `expected_reduction_quantity`
- `food.demand.fact_channel_volume`: `channel_id`, `unmeasured_gain_flag`, `fiscal_quarter_id`, `category_id`, `retailer_id`, `volume_quantity`, `volume_change_rate`
- `food.category.dim_channel`: `channel_name`, `channel_code`
- `food.price.fact_pet_price`: `fiscal_quarter_id`, `brand_id`, `category_id`, `planned_change_rate`, `strategy_code`, `change_possible_flag`
- `food.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`
