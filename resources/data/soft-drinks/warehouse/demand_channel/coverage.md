# Beverage Inc demand and channel

This slice owns brands, packs, channels, countries, and unit-case demand for Beverage Inc. A demand row stores quantity or a demand index. It does not store a price and it does not store plant capacity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `bottler_identity` | `bottler_id` | `sf:beverage.supply.dim_bottler` `bottler_id` |
| `bottler_identity` | `bottler_id` | `sf:beverage.supply.dim_bottler` `bottler_id` |
| `bottler_identity` | `bottler_id` | `sf:beverage.supply.dim_bottler` `bottler_id` |
| `bottler_identity` | `bottler_id` | `sf:beverage.supply.dim_bottler` `bottler_id` |
| `bottler_identity` | `bottler_id` | `sf:beverage.supply.dim_bottler` `bottler_id` |
| `bottler_identity` | `bottler_id` | `sf:beverage.supply.dim_bottler` `bottler_id` |
| `bottler_identity` | `bottler_id` | `sf:beverage.supply.dim_bottler` `bottler_id` |

## Numbered questions

## Coca-Cola

### Q1 2026 (1)

How should volume and price/mix split for the rest of 2026 in North America and Asia after a strong unit-case quarter and two softer price/mix quarters?

- `beverage.demand.fact_unit_case`: `fiscal_quarter_id`, `region_id`, `country_id`, `brand_id`, `channel_id`, `volume_growth_rate`
- `beverage.geography.dim_region`: `region_code`, `region_name`
- `beverage.price.fact_price_mix`: `fiscal_quarter_id`, `region_id`, `country_id`, `brand_id`, `affordability_share`, `price_mix_rate`
- `beverage.price.fact_price_bridge`: `fiscal_quarter_id`, `region_id`, `brand_id`, `channel_id`, `contribution_rate`, `distribution_remaining_flag`

### Q1 2026 (4)

How will the European Coke Zero relaunch sit alongside Diet Coke so the system does not starve one no-sugar trademark of attention?

- `beverage.demand.fact_trademark_attention`: `fiscal_quarter_id`, `trademark_id`, `country_id`, `bottler_id`, `attention_share`, `starved_flag`
- `beverage.product.dim_trademark`: `brand_id`, `trademark_code`, `trademark_name`
- `beverage.supply.fact_bottler_capacity`: `fiscal_quarter_id`, `bottler_id`, `country_id`, `brand_id`, `execution_slot_count`, `higher_cost_ready_flag`
- `beverage.supply.dim_bottler`: `country_id`, `bottler_code`, `bottler_name`

### Q1 2026 (7)

What is driving the strong China and India results, and how sustainable is that APAC performance through the year?

- `beverage.demand.fact_country_volume`: `fiscal_quarter_id`, `country_id`, `region_id`, `brand_id`, `sustainable_flag`, `rebound_timing_code`
- `beverage.geography.dim_country`: `region_id`, `country_code`, `country_name`
- `beverage.demand.fact_consumer_group`: `fiscal_quarter_id`, `consumer_segment_id`, `country_id`, `brand_id`, `comparison_help_flag`, `prior_disruption_flag`

### Q1 2026 (9)

Is the U.S. foodservice approach changing to participate in newer away-from-home formats such as drive-thru beverage chains?

- `beverage.channel.dim_channel`: `channel_code`, `channel_name`
- `beverage.demand.fact_channel_volume`: `fiscal_quarter_id`, `channel_id`, `country_id`, `brand_id`, `customer_id`, `newer_format_flag`
- `beverage.customer.dim_customer`: `channel_id`, `customer_code`, `customer_name`

### Q4 2025 (2)

How are worsening consumer conditions assumed to trend through 2026 relative to the milder backdrop described a few months earlier?

- `beverage.demand.fact_consumer_demand`: `fiscal_quarter_id`, `region_id`, `country_id`, `calendar_day_id`, `demand_index`, `improved_flag`
- `beverage.price.fact_organic_outlook`: `fiscal_quarter_id`, `region_id`, `country_id`, `organic_growth_rate`, `conservative_flag`, `volume_contribution_rate`
- `beverage.demand.fact_country_volume`: `fiscal_quarter_id`, `country_id`, `region_id`, `brand_id`, `unit_case_quantity`, `rebound_timing_code`
- `beverage.demand.fact_division_volume`: `fiscal_quarter_id`, `category_id`, `region_id`, `brand_id`, `consumer_backdrop_flag`, `unit_case_quantity`

### Q4 2025 (5)

How will incremental fairlife capacity early in the year flow through brand growth over 2026?

- `beverage.demand.fact_brand_volume`: `fiscal_quarter_id`, `brand_id`, `country_id`, `product_line_id`, `unit_case_quantity`, `line_managed_separately_flag`
- `beverage.supply.fact_plant_capacity`: `fiscal_quarter_id`, `plant_id`, `brand_id`, `country_id`, `capacity_quantity`, `replicable_abroad_flag`
- `beverage.geography.dim_region`: `region_code`, `region_name`
- `beverage.supply.dim_plant`: `country_id`, `bottler_id`, `plant_code`, `plant_name`

### Q4 2025 (6)

What sales uplift is expected from World Cup activation in the summer?

- `beverage.demand.fact_event_volume`: `fiscal_quarter_id`, `event_id`, `region_id`, `brand_id`, `category_id`, `versus_past_event_code`
- `beverage.demand.dim_event`: `event_code`, `event_name`
- `beverage.geography.dim_region`: `region_code`, `region_name`
- `beverage.demand.fact_country_volume`: `fiscal_quarter_id`, `country_id`, `region_id`, `brand_id`, `rebound_timing_code`, `sustainable_flag`

### Q4 2025 (7)

Could the comparison with last year's temporary Hispanic-consumer disruption in North America help the first part of 2026?

- `beverage.demand.fact_consumer_group`: `fiscal_quarter_id`, `consumer_segment_id`, `country_id`, `brand_id`, `comparison_help_flag`, `prior_disruption_flag`
- `beverage.geography.dim_region`: `region_code`, `region_name`
- `beverage.product.dim_consumer_segment`: `consumer_segment_code`, `consumer_segment_name`

### Q4 2025 (9)

How do U.S. SNAP changes affect demand, and did the first read on the Mexican tax make the 2026 organic-sales outlook more conservative?

- `beverage.demand.fact_program_volume`: `fiscal_quarter_id`, `country_id`, `consumer_segment_id`, `brand_id`, `demand_effect_code`, `exposed_quantity`
- `beverage.price.fact_organic_outlook`: `fiscal_quarter_id`, `region_id`, `country_id`, `conservative_flag`, `organic_growth_rate`, `volume_contribution_rate`
- `beverage.price.fact_excise`: `fiscal_quarter_id`, `country_id`, `outlook_more_conservative_flag`, `first_read_code`, `tax_rate`
- `beverage.geography.dim_country`: `region_id`, `country_code`, `country_name`

### Q4 2025 (12)

Where does the new chief executive see the largest innovation opportunities, and how are those executed against a weaker global consumer?

- `beverage.demand.fact_innovation`: `fiscal_quarter_id`, `brand_id`, `category_id`, `country_id`, `weaker_consumer_fit_flag`, `opportunity_code`
- `beverage.demand.fact_consumer_demand`: `fiscal_quarter_id`, `region_id`, `country_id`, `calendar_day_id`, `demand_index`, `tougher_flag`
- `beverage.demand.fact_innovation_volume`: `fiscal_quarter_id`, `brand_id`, `category_id`, `country_id`, `innovation_quantity`, `pipeline_ready_flag`
- `beverage.demand.fact_glp1_demand`: `fiscal_quarter_id`, `consumer_segment_id`, `category_id`, `brand_id`, `explains_slowdown_flag`, `strategy_changed_flag`

### Q4 2025 (13)

Should marketing and innovation step up in India as refranchising proceeds, and how far have B2B digital and analytics gone for store-level execution before the bottler takes demand fulfillment?

- `beverage.demand.fact_refranchising`: `fiscal_quarter_id`, `country_id`, `bottler_id`, `marketing_steps_up_flag`, `remaining_share`
- `beverage.demand.fact_digital_execution`: `fiscal_quarter_id`, `country_id`, `bottler_id`, `customer_id`, `in_place_flag`, `coverage_share`
- `beverage.price.fact_price_action`: `fiscal_quarter_id`, `brand_id`, `customer_id`, `region_id`, `pack_id`, `in_place_share`
- `beverage.supply.dim_bottler`: `country_id`, `bottler_code`, `bottler_name`

### Q2 2025 (1)

What specifically is being pivoted in second-half plans even though organic sales and profit were strong, and does the environment feel tougher?

- `beverage.demand.fact_plan_pivot`: `fiscal_quarter_id`, `region_id`, `category_id`, `tougher_flag`, `emphasis_code`, `pivot_flag`
- `beverage.price.fact_organic_outlook`: `fiscal_quarter_id`, `region_id`, `country_id`, `organic_growth_rate`, `conservative_flag`, `price_contribution_rate`
- `beverage.demand.fact_country_volume`: `fiscal_quarter_id`, `country_id`, `region_id`, `brand_id`, `rebound_timing_code`, `sustainable_flag`
- `beverage.demand.fact_consumer_demand`: `fiscal_quarter_id`, `region_id`, `country_id`, `calendar_day_id`, `tougher_flag`, `demand_index`

### Q2 2025 (4)

How quickly should Mexico and India rebound after the plan changes made for the second half?

- `beverage.demand.fact_country_volume`: `fiscal_quarter_id`, `country_id`, `region_id`, `brand_id`, `rebound_timing_code`, `sustainable_flag`
- `beverage.geography.dim_country`: `region_id`, `country_code`, `country_name`
- `beverage.price.fact_deal_timing`: `fiscal_quarter_id`, `region_id`, `second_half_flag`, `margin_effect_rate`

### Q2 2025 (6)

Where is consumer strength or weakness showing up globally beyond weather and geopolitics, and did June softness continue into July?

- `beverage.demand.fact_consumer_demand`: `fiscal_quarter_id`, `region_id`, `country_id`, `calendar_day_id`, `demand_index`, `improved_flag`
- `beverage.time.dim_calendar_day`: `fiscal_quarter_id`, `month_code`, `calendar_date`, `calendar_day_code`, `calendar_day_name`

### Q2 2025 (7)

How do consumer preferences for cane and fiber shape innovation, and how is Simply Pop performing against competitors launching prebiotic drinks under a core trademark?

- `beverage.demand.fact_competitor_set`: `fiscal_quarter_id`, `brand_id`, `category_id`, `country_id`, `same_occasion_flag`, `ahead_flag`
- `beverage.demand.fact_innovation`: `fiscal_quarter_id`, `brand_id`, `category_id`, `country_id`, `opportunity_code`, `weaker_consumer_fit_flag`
- `beverage.product.dim_brand`: `category_id`, `brand_code`, `brand_name`
- `beverage.product.dim_category`: `category_code`, `category_name`

### Q2 2025 (8)

How is the European consumer holding up versus other developed markets, given EMEA is expected to drive unit cases in the second half?

- `beverage.demand.fact_country_volume`: `fiscal_quarter_id`, `country_id`, `region_id`, `brand_id`, `rebound_timing_code`, `unit_case_quantity`
- `beverage.demand.fact_unit_case`: `fiscal_quarter_id`, `region_id`, `country_id`, `brand_id`, `channel_id`, `unit_case_quantity`
- `beverage.geography.dim_region`: `region_code`, `region_name`
- `beverage.demand.fact_consumer_group`: `fiscal_quarter_id`, `consumer_segment_id`, `country_id`, `brand_id`, `unit_case_quantity`, `comparison_help_flag`

### Q2 2025 (9)

With most refranchising done, how is the capability to create demand and recruit consumers actually intensifying?

- `beverage.demand.fact_demand_creation`: `fiscal_quarter_id`, `bottler_id`, `country_id`, `brand_id`, `retained_flag`, `recruiting_flag`
- `beverage.demand.fact_refranchising`: `fiscal_quarter_id`, `country_id`, `bottler_id`, `marketing_steps_up_flag`, `remaining_share`
- `beverage.supply.dim_bottler`: `country_id`, `bottler_code`, `bottler_name`
- `beverage.price.fact_bottler_incentive`: `fiscal_quarter_id`, `bottler_id`, `incentive_amount`, `insight_loop_flag`

### Q2 2025 (10)

How confident is management that concentrate volume turns positive in the second half after transitory hits and a tough comparison, and is the fourth-quarter concentrate comparison especially difficult?

- `beverage.demand.fact_concentrate_shipment`: `fiscal_quarter_id`, `country_id`, `bottler_id`, `brand_id`, `tough_comparison_flag`, `turns_positive_flag`
- `beverage.demand.fact_country_volume`: `fiscal_quarter_id`, `country_id`, `region_id`, `brand_id`, `rebound_timing_code`, `sustainable_flag`

### Q4 2024 (3)

How does 5% to 6% organic sales growth compare with industry growth and the industry exit rate?

- `beverage.demand.fact_industry_volume`: `fiscal_quarter_id`, `category_id`, `region_id`, `company_gap_rate`, `exit_rate`, `industry_growth_rate`
- `beverage.price.fact_organic_outlook`: `fiscal_quarter_id`, `region_id`, `country_id`, `organic_growth_rate`, `volume_contribution_rate`, `conservative_flag`
- `beverage.demand.fact_category_health`: `fiscal_quarter_id`, `category_id`, `region_id`, `category_growth_rate`, `better_footing_flag`, `extrapolate_flag`
- `beverage.demand.fact_country_volume`: `fiscal_quarter_id`, `country_id`, `region_id`, `brand_id`, `rebound_timing_code`, `sustainable_flag`

### Q4 2024 (6)

What share of the U.S. portfolio could be touched by potential regulatory change, and how fast can the portfolio be adapted?

- `beverage.demand.fact_regulatory_exposure`: `fiscal_quarter_id`, `brand_id`, `country_id`, `adapt_months`, `exposed_share`
- `beverage.demand.fact_pack_mix`: `fiscal_quarter_id`, `pack_id`, `brand_id`, `region_id`, `category_id`, `pack_share`

### Q4 2024 (7)

Has GLP-1 use changed consumption, and has that changed innovation strategy?

- `beverage.demand.fact_glp1_demand`: `fiscal_quarter_id`, `consumer_segment_id`, `category_id`, `brand_id`, `exposed_quantity`, `strategy_changed_flag`
- `beverage.demand.fact_innovation`: `fiscal_quarter_id`, `brand_id`, `category_id`, `country_id`, `in_market_flag`, `opportunity_code`

### Q4 2024 (8)

Is Walmart's modern-soda shelf a fad or a lasting consumer shift, and how does Coca-Cola plan to compete there relative to something like fairlife?

- `beverage.demand.fact_shelf_set`: `fiscal_quarter_id`, `customer_id`, `brand_id`, `category_id`, `repeat_flag`, `fad_flag`
- `beverage.product.dim_brand`: `category_id`, `brand_code`, `brand_name`
- `beverage.demand.fact_repeat`: `fiscal_quarter_id`, `brand_id`, `customer_id`, `consumer_repeat_flag`, `repeat_rate`
- `beverage.customer.dim_customer`: `channel_id`, `customer_code`, `customer_name`

### Q4 2024 (13)

How does Asia Pacific price/mix, down despite some pricing, reconcile with share gains in South Korea and Japan and share losses in Indonesia and Bangladesh?

- `beverage.demand.fact_country_share`: `fiscal_quarter_id`, `country_id`, `brand_id`, `gaining_flag`, `share_change_rate`
- `beverage.geography.dim_country`: `region_id`, `country_code`, `country_name`
- `beverage.geography.dim_region`: `region_code`, `region_name`
- `beverage.demand.fact_value_share`: `fiscal_quarter_id`, `brand_id`, `region_id`, `category_id`, `declining_flag`, `value_share_rate`

## PepsiCo

### Q2 2026 (1)

Has U.S. consumer behavior improved as fuel and other inflation eased, and does that still support the high end of the organic-sales range in the back half?

- `beverage.demand.fact_consumer_demand`: `fiscal_quarter_id`, `region_id`, `country_id`, `calendar_day_id`, `improved_flag`, `demand_index`
- `beverage.price.fact_organic_outlook`: `fiscal_quarter_id`, `region_id`, `country_id`, `organic_growth_rate`, `conservative_flag`, `price_contribution_rate`
- `beverage.demand.fact_country_volume`: `fiscal_quarter_id`, `country_id`, `region_id`, `brand_id`, `rebound_timing_code`, `unit_case_quantity`

### Q2 2026 (2)

Were weaker-than-hoped Frito-Lay North America and PepsiCo Beverages North America volumes a shortfall in the new initiatives or the consumer backdrop?

- `beverage.demand.fact_division_volume`: `fiscal_quarter_id`, `category_id`, `region_id`, `brand_id`, `consumer_backdrop_flag`, `initiative_shortfall_flag`
- `beverage.geography.dim_region`: `region_code`, `region_name`
- `beverage.product.dim_brand`: `category_id`, `brand_code`, `brand_name`

### Q2 2026 (4)

Will price rollbacks spread beyond the largest U.S. customer, and have those reinvestments already shown up as better volume in convenience and away-from-home?

- `beverage.demand.fact_channel_volume`: `fiscal_quarter_id`, `channel_id`, `country_id`, `brand_id`, `customer_id`, `newer_format_flag`
- `beverage.customer.dim_customer`: `channel_id`, `customer_code`, `customer_name`
- `beverage.price.fact_price_action`: `fiscal_quarter_id`, `brand_id`, `customer_id`, `region_id`, `pack_id`, `rollback_spread_flag`
- `beverage.channel.dim_channel`: `channel_code`, `channel_name`

### Q2 2026 (6)

How do category growth and consumer health differ across international regions, and should second-quarter international growth be extrapolated for the rest of the year?

- `beverage.demand.fact_category_health`: `fiscal_quarter_id`, `category_id`, `region_id`, `category_growth_rate`, `better_footing_flag`, `extrapolate_flag`
- `beverage.demand.fact_industry_volume`: `fiscal_quarter_id`, `category_id`, `region_id`, `exit_rate`, `industry_growth_rate`, `company_gap_rate`
- `beverage.price.fact_cost_structure`: `fiscal_quarter_id`, `region_id`, `offset_by_international_flag`, `cost_amount`
- `beverage.demand.fact_country_volume`: `fiscal_quarter_id`, `country_id`, `region_id`, `brand_id`, `sustainable_flag`, `rebound_timing_code`

### Q2 2026 (7)

Are affordability, package, and innovation actions already in market and now a matter of scaling, or are further catalysts still ahead?

- `beverage.demand.fact_initiative_stage`: `fiscal_quarter_id`, `brand_id`, `region_id`, `pack_id`, `catalyst_still_ahead_flag`, `in_market_flag`
- `beverage.demand.fact_innovation`: `fiscal_quarter_id`, `brand_id`, `category_id`, `country_id`, `in_market_flag`, `opportunity_code`

### Q1 2026 (2)

Is international demand still solid, or is there macro risk after the conflict?

- `beverage.demand.fact_country_volume`: `fiscal_quarter_id`, `country_id`, `region_id`, `brand_id`, `rebound_timing_code`, `sustainable_flag`
- `beverage.price.fact_spend_mix`: `fiscal_quarter_id`, `region_id`, `above_growth_flag`, `spend_amount`

### Q1 2026 (3)

How sustainable is the Frito-Lay North America volume inflection after possible ship-ahead of shelf resets and winter storms, and what are repeat rates on the refill orders?

- `beverage.demand.fact_shipment_timing`: `fiscal_quarter_id`, `brand_id`, `region_id`, `customer_id`, `inflection_durable_flag`, `storm_quantity`
- `beverage.demand.fact_repeat`: `fiscal_quarter_id`, `brand_id`, `customer_id`, `consumer_repeat_flag`, `repeat_rate`
- `beverage.geography.dim_region`: `region_code`, `region_name`
- `beverage.product.dim_brand`: `category_id`, `brand_code`, `brand_name`

### Q1 2026 (5)

How much of PepsiCo Beverages North America volume pressure is smaller packs and price-pack architecture, and should volume declines moderate through the year?

- `beverage.product.dim_pack`: `brand_id`, `pack_code`, `pack_name`
- `beverage.demand.fact_pack_mix`: `fiscal_quarter_id`, `pack_id`, `brand_id`, `region_id`, `category_id`, `pack_share`
- `beverage.demand.fact_volume_bridge`: `fiscal_quarter_id`, `category_id`, `pack_id`, `region_id`, `pack_contribution_share`, `category_contribution_share`
- `beverage.geography.dim_region`: `region_code`, `region_name`

### Q1 2026 (6)

How should innovation versus distribution gains in Frito-Lay North America compare in the second quarter versus the first, as protein and better-for-you items ship?

- `beverage.demand.fact_innovation_volume`: `fiscal_quarter_id`, `brand_id`, `category_id`, `country_id`, `innovation_quantity`, `pipeline_ready_flag`
- `beverage.demand.fact_distribution`: `fiscal_quarter_id`, `brand_id`, `customer_id`, `country_id`, `versus_innovation_code`, `placement_count`
- `beverage.geography.dim_region`: `region_code`, `region_name`
- `beverage.product.dim_category`: `category_code`, `category_name`

### Q1 2026 (9)

Is the expected sequential improvement in Frito-Lay North America broad-based, or should organic sales keep rising from the 1% just reported, and what guardrails apply for the rest of the year?

- `beverage.demand.fact_division_path`: `fiscal_quarter_id`, `category_id`, `region_id`, `broad_based_flag`, `guardrail_code`
- `beverage.geography.dim_region`: `region_code`, `region_name`
- `beverage.price.fact_organic_outlook`: `fiscal_quarter_id`, `region_id`, `country_id`, `organic_growth_rate`, `conservative_flag`, `price_contribution_rate`
- `beverage.product.dim_brand`: `category_id`, `brand_code`, `brand_name`

### Q1 2026 (12)

Who is driving the increase in consumption occasions, and are those occasions different from the core user?

- `beverage.demand.fact_occasion`: `fiscal_quarter_id`, `consumer_segment_id`, `category_id`, `brand_id`, `new_user_flag`, `lost_to_cheaper_food_flag`
- `beverage.product.dim_consumer_segment`: `consumer_segment_code`, `consumer_segment_name`

### Q1 2026 (14)

What does World Cup activation look like for Frito-Lay versus past events, and is any uplift in the outlook?

- `beverage.demand.fact_event_volume`: `fiscal_quarter_id`, `event_id`, `region_id`, `brand_id`, `category_id`, `in_outlook_flag`
- `beverage.demand.dim_event`: `event_code`, `event_name`
- `beverage.product.dim_brand`: `category_id`, `brand_code`, `brand_name`

### Q3 2025 (1)

How much of the food and beverage volume pressure is the shift to smaller packs versus soft category trends or share loss, and can the innovation pipeline turn volume?

- `beverage.demand.fact_volume_bridge`: `fiscal_quarter_id`, `category_id`, `pack_id`, `region_id`, `pack_contribution_share`, `category_contribution_share`
- `beverage.product.dim_pack`: `brand_id`, `pack_code`, `pack_name`
- `beverage.demand.fact_pack_mix`: `fiscal_quarter_id`, `pack_id`, `brand_id`, `region_id`, `category_id`, `pack_share`
- `beverage.demand.fact_innovation`: `fiscal_quarter_id`, `brand_id`, `category_id`, `country_id`, `in_market_flag`, `opportunity_code`

### Q3 2025 (2)

Which of innovation, functional products, portfolio reshaping, and price-pack architecture matter most for accelerating 2026 revenue, and is the long-term growth algorithm visible inside 2026?

- `beverage.demand.fact_growth_lever`: `fiscal_quarter_id`, `category_id`, `brand_id`, `leading_lever_code`, `visible_in_year_flag`
- `beverage.demand.fact_pack_mix`: `fiscal_quarter_id`, `pack_id`, `brand_id`, `region_id`, `category_id`, `decline_moderates_flag`
- `beverage.product.dim_pack`: `brand_id`, `pack_code`, `pack_name`

### Q3 2025 (4)

How healthy is the consumer in Latin America, Asia Pacific, and India after a weather-hit quarter and a better September, and what supports the expected acceleration?

- `beverage.geography.dim_region`: `region_code`, `region_name`
- `beverage.geography.dim_country`: `region_id`, `country_code`, `country_name`
- `beverage.demand.fact_consumer_demand`: `fiscal_quarter_id`, `region_id`, `country_id`, `calendar_day_id`, `demand_index`, `improved_flag`
- `beverage.demand.fact_country_volume`: `fiscal_quarter_id`, `country_id`, `region_id`, `brand_id`, `rebound_timing_code`, `sustainable_flag`

### Q3 2025 (5)

What is driving better U.S. Pepsi brand momentum and share, messaging or more marketing, and does optimizing marketing ROI mean lower spend?

- `beverage.demand.fact_brand_trend`: `fiscal_quarter_id`, `brand_id`, `country_id`, `message_driven_flag`, `volume_growth_rate`
- `beverage.price.fact_marketing_spend`: `fiscal_quarter_id`, `region_id`, `brand_id`, `lower_spend_flag`, `spend_amount`, `timing_code`
- `beverage.demand.fact_value_share`: `fiscal_quarter_id`, `brand_id`, `region_id`, `category_id`, `declining_flag`, `value_share_rate`
- `beverage.product.dim_brand`: `category_id`, `brand_code`, `brand_name`

### Q3 2025 (6)

Was Frito-Lay North America's return to growth in the last month mostly an easier comparison, or innovation and everyday execution, on the way to flat fourth-quarter organic sales?

- `beverage.demand.fact_comparison_base`: `fiscal_quarter_id`, `category_id`, `region_id`, `easier_comparison_flag`, `execution_flag`
- `beverage.price.fact_organic_outlook`: `fiscal_quarter_id`, `region_id`, `country_id`, `organic_growth_rate`, `conservative_flag`, `price_contribution_rate`
- `beverage.geography.dim_region`: `region_code`, `region_name`
- `beverage.product.dim_brand`: `category_id`, `brand_code`, `brand_name`

### Q3 2025 (7)

How large a headwind is SKU rationalization on organic growth?

- `beverage.demand.fact_sku_count`: `fiscal_quarter_id`, `brand_id`, `category_id`, `region_id`, `discontinued_sku_count`, `remaining_sku_count`
- `beverage.price.fact_organic_outlook`: `fiscal_quarter_id`, `region_id`, `country_id`, `organic_growth_rate`, `conservative_flag`, `price_contribution_rate`
- `beverage.demand.fact_division_path`: `fiscal_quarter_id`, `category_id`, `region_id`, `broad_based_flag`, `guardrail_code`

### Q3 2025 (9)

Where has volume turned positive in the last four weeks, and is that company-wide or only where service levels recovered?

- `beverage.demand.fact_recent_volume`: `fiscal_quarter_id`, `region_id`, `country_id`, `calendar_day_id`, `four_week_quantity`, `positive_flag`
- `beverage.supply.fact_service_level`: `fiscal_quarter_id`, `country_id`, `brand_id`, `customer_id`, `recovered_flag`, `fill_rate`

### Q3 2025 (10)

Why address beverage protein with in-house brands such as Muscle Milk and Propel rather than buying or partnering, as in energy and prebiotic?

- `beverage.demand.fact_make_or_partner`: `fiscal_quarter_id`, `brand_id`, `category_id`, `different_from_adjacent_flag`, `route_code`
- `beverage.product.dim_brand`: `category_id`, `brand_code`, `brand_name`
- `beverage.product.dim_category`: `category_code`, `category_name`

### Q3 2025 (12)

In the U.S., how much of the slowdown is structural healthier eating versus cyclical value-seeking, and how does that compare with international markets?

- `beverage.demand.fact_preference_shift`: `fiscal_quarter_id`, `region_id`, `category_id`, `consumer_segment_id`, `driver_code`, `international_same_flag`
- `beverage.demand.fact_consumer_demand`: `fiscal_quarter_id`, `region_id`, `country_id`, `calendar_day_id`, `demand_index`, `improved_flag`
- `beverage.product.dim_consumer_segment`: `consumer_segment_code`, `consumer_segment_name`

### Q4 2024 (2)

How is Frito-Lay and the beverage business being managed differently in 2025 than in the second half of last year, given a muted North America top line?

- `beverage.demand.fact_plan_pivot`: `fiscal_quarter_id`, `region_id`, `category_id`, `emphasis_code`, `pivot_flag`, `tougher_flag`
- `beverage.geography.dim_region`: `region_code`, `region_name`
- `beverage.product.dim_brand`: `category_id`, `brand_code`, `brand_name`
- `beverage.demand.fact_division_volume`: `fiscal_quarter_id`, `category_id`, `region_id`, `brand_id`, `consumer_backdrop_flag`, `initiative_shortfall_flag`

### Q4 2024 (3)

How did Mexico perform in the fourth quarter in the same subdued consumer environment?

- `beverage.demand.fact_country_volume`: `fiscal_quarter_id`, `country_id`, `region_id`, `brand_id`, `rebound_timing_code`, `sustainable_flag`
- `beverage.geography.dim_region`: `region_code`, `region_name`
- `beverage.geography.dim_country`: `region_id`, `country_code`, `country_name`
- `beverage.demand.fact_division_volume`: `fiscal_quarter_id`, `category_id`, `region_id`, `brand_id`, `consumer_backdrop_flag`, `initiative_shortfall_flag`

### Q4 2024 (4)

For Frito-Lay, which matters more: price running ahead of the wallet, a shift toward healthier choices, or snacks losing meal occasions to cheaper food?

- `beverage.demand.fact_snack_driver`: `fiscal_quarter_id`, `category_id`, `consumer_segment_id`, `leading_driver_code`, `confidence_code`
- `beverage.demand.fact_occasion`: `fiscal_quarter_id`, `consumer_segment_id`, `category_id`, `brand_id`, `lost_to_cheaper_food_flag`, `new_user_flag`
- `beverage.product.dim_consumer_segment`: `consumer_segment_code`, `consumer_segment_name`
- `beverage.product.dim_brand`: `category_id`, `brand_code`, `brand_name`

### Q4 2024 (6)

What is different in recent salty-snack trends that supports confidence the category is on better footing after earlier upturns reversed?

- `beverage.demand.fact_category_health`: `fiscal_quarter_id`, `category_id`, `region_id`, `better_footing_flag`, `category_growth_rate`, `extrapolate_flag`
- `beverage.demand.fact_comparison_base`: `fiscal_quarter_id`, `category_id`, `region_id`, `easier_comparison_flag`, `execution_flag`
- `beverage.demand.fact_industry_volume`: `fiscal_quarter_id`, `category_id`, `region_id`, `exit_rate`, `industry_growth_rate`, `company_gap_rate`

### Q4 2024 (8)

Has the view of the energy-drink category or PepsiCo's platform changed, and what execution or partner actions are planned to grow that part of the portfolio?

- `beverage.demand.fact_energy_platform`: `fiscal_quarter_id`, `category_id`, `brand_id`, `bottler_id`, `view_changed_flag`, `partner_action_flag`
- `beverage.supply.fact_service_level`: `fiscal_quarter_id`, `country_id`, `brand_id`, `customer_id`, `recovered_flag`, `fill_rate`
- `beverage.product.dim_category`: `category_code`, `category_name`
- `beverage.demand.fact_distribution`: `fiscal_quarter_id`, `brand_id`, `customer_id`, `country_id`, `versus_innovation_code`, `placement_count`

### Q4 2024 (10)

How incremental is the latest beverage partnership, and how is the Mountain Dew franchise expected to perform?

- `beverage.demand.fact_partnership_volume`: `fiscal_quarter_id`, `brand_id`, `country_id`, `bottler_id`, `incremental_flag`, `incremental_quantity`
- `beverage.demand.fact_brand_volume`: `fiscal_quarter_id`, `brand_id`, `country_id`, `product_line_id`, `line_managed_separately_flag`, `unit_case_quantity`
- `beverage.demand.fact_brand_trend`: `fiscal_quarter_id`, `brand_id`, `country_id`, `volume_growth_rate`, `message_driven_flag`
- `beverage.product.dim_brand`: `category_id`, `brand_code`, `brand_name`

### Q4 2024 (11)

Does rising GLP-1 use explain the salty-snack slowdown as outside studies suggest, or does that overstate the impact?

- `beverage.demand.fact_glp1_demand`: `fiscal_quarter_id`, `consumer_segment_id`, `category_id`, `brand_id`, `explains_slowdown_flag`, `exposed_quantity`
- `beverage.demand.fact_category_health`: `fiscal_quarter_id`, `category_id`, `region_id`, `better_footing_flag`, `category_growth_rate`, `extrapolate_flag`

### Q4 2024 (12)

How aggressive does PepsiCo want to be in protein drinks given that segment's growth?

- `beverage.demand.fact_protein_push`: `fiscal_quarter_id`, `category_id`, `brand_id`, `push_code`, `participation_share`
- `beverage.demand.fact_industry_volume`: `fiscal_quarter_id`, `category_id`, `region_id`, `exit_rate`, `industry_growth_rate`, `company_gap_rate`
- `beverage.demand.fact_category_health`: `fiscal_quarter_id`, `category_id`, `region_id`, `category_growth_rate`, `better_footing_flag`, `extrapolate_flag`
- `beverage.product.dim_category`: `category_code`, `category_name`
