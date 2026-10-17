# Chemical Inc end market demand

End market demand owns segments, end markets, customers, channels, and geography for Chemical Inc. Volume, orders, share, traffic, retention, and outlook are demand facts. They store quantities and rates, not a selling price and not a raw-material cost.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `acquisition_identity` | `acquisition_id` | `sf:chemical.network.dim_acquisition` `acquisition_id` |

## Numbered questions

## Sherwin-Williams

### Q1 2026 (3)

For Sherwin-Williams, how are growth spend and net store openings and closures being set while share gains continue?

- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.supply.fact_store_network`: `store_id`, `opening_count`, `closure_count`, `net_store_count`, `sales_point_from_new_stores`, `fiscal_quarter_id`, `country_id`
- `chemical.supply.fact_headcount`: `implies_more_stores_flag`, `fiscal_quarter_id`, `headcount_role_id`, `business_segment_id`, `headcount_quantity`, `addition_quantity`
- `chemical.supply.fact_growth_spend`: `growth_program_id`, `spend_amount`, `share_of_spend_rate`, `fiscal_quarter_id`, `business_segment_id`, `allocation_changed_flag`, `payback_months`
- `chemical.network.dim_growth_program`: `business_segment_id`, `program_name`, `program_code`

### Q1 2026 (4)

For Sherwin-Williams, is the volume-guide swing from growth to a low-single-digit decline a rest-of-year market view, and what offsets keep earnings intact?

- `chemical.demand.fact_end_market_volume`: `end_market_id`, `demand_driver_id`, `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `country_id`
- `chemical.demand.fact_segment_volume`: `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `sales_change_rate`
- `chemical.price.fact_earnings_bridge`: `earnings_change_rate`, `offset_amount`, `intact_flag`, `fiscal_quarter_id`, `business_segment_id`, `margin_driver_id`, `price_led_flag`
- `chemical.price.fact_acquisition_margin`: `fiscal_quarter_id`, `acquisition_id`, `business_segment_id`, `drag_rate`, `excluded_margin_rate`, `dilution_rate`, `uses_original_case_flag`
- `chemical.demand.fact_industry_volume`: `end_market_id`, `industry_volume_quantity`, `fiscal_quarter_id`, `subsegment_id`, `country_id`, `industry_change_rate`, `company_versus_industry_rate`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (5)

For Sherwin-Williams, what is driving the margin improvement in Consumer Brands?

- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.price.fact_gross_margin`: `gross_margin_rate`, `flat_demand_margin_rate`, `fiscal_quarter_id`, `business_segment_id`, `year_over_year_change_rate`, `above_fifty_flag`, `holds_without_recovery_flag`
- `chemical.price.fact_segment_margin`: `margin_driver_id`, `operating_margin_rate`, `margin_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `target_rate`, `quarter_dip_flag`
- `chemical.price.fact_acquisition_margin`: `excluded_margin_rate`, `fiscal_quarter_id`, `acquisition_id`, `business_segment_id`, `drag_rate`, `dilution_rate`, `uses_original_case_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (8)

For Sherwin-Williams, will residential repaint stay solid, and will refinish, general industrial, and coil strength continue?

- `chemical.demand.fact_end_market_volume`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `demand_driver_id`, `volume_quantity`, `volume_change_rate`
- `chemical.demand.fact_repaint_cycle`: `solid_demand_flag`, `fiscal_quarter_id`, `end_market_id`, `country_id`, `cycle_years`, `delayed_flag`, `labor_available_flag`
- `chemical.demand.fact_share_position`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `subsegment_id`, `country_id`, `competitor_id`, `share_rate`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (11)

For Sherwin-Williams, how much of packaging outgrowth is the regulatory conversion, and does growth move back toward the industry after that catalyst is lapped?

- `chemical.demand.fact_packaging_conversion`: `conversion_quantity`, `remaining_conversion_quantity`, `outgrowth_rate`, `lapped_flag`, `fiscal_quarter_id`, `end_market_id`, `country_id`
- `chemical.demand.fact_end_market_volume`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `demand_driver_id`, `volume_quantity`, `volume_change_rate`
- `chemical.demand.fact_industry_volume`: `industry_volume_quantity`, `industry_change_rate`, `company_versus_industry_rate`, `fiscal_quarter_id`, `end_market_id`, `subsegment_id`, `country_id`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (12)

For Sherwin-Williams, is the lower Performance Coatings volume guide from current order weakness or March pull-forward, and where is U.S. industrial demand expanding?

- `chemical.demand.fact_segment_volume`: `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `sales_change_rate`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.demand.fact_order_book`: `order_pattern_id`, `order_quantity`, `pull_forward_flag`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `customer_id`
- `chemical.demand.fact_volume_outlook`: `guided_volume_change_rate`, `prior_volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `macro_case_id`, `market_decline_flag`
- `chemical.demand.fact_end_market_volume`: `demand_driver_id`, `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`

### Q1 2026 (13)

For Sherwin-Williams, are Performance Coatings customers locking production schedules or shifting to short-cycle orders?

- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.demand.fact_order_book`: `customer_id`, `order_pattern_id`, `order_quantity`, `short_cycle_flag`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`
- `chemical.customer.dim_order_pattern`: `pattern_name`, `pattern_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (14)

For Sherwin-Williams, are customers prebuying ahead of inflationary price increases?

- `chemical.demand.fact_prebuy`: `customer_id`, `prebuy_quantity`, `prebuy_flag`, `inventory_weeks`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`
- `chemical.demand.fact_distributor_inventory`: `inventory_quantity`, `fiscal_quarter_id`, `business_segment_id`, `channel_id`, `country_id`, `reduction_quantity`, `underlying_volume_change_rate`
- `chemical.price.fact_announced_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `announced_change_rate`, `in_guide_flag`, `added_after_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (15)

For Sherwin-Williams, if U.S. architectural demand stays weak through the decade, how does strategy change, and is Paint Stores tracking a low-single-digit sales decline?

- `chemical.demand.fact_end_market_volume`: `demand_driver_id`, `volume_change_rate`, `run_rate_quantity`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.demand.fact_segment_volume`: `volume_change_rate`, `sales_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `organic_volume_quantity`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.demand.fact_volume_outlook`: `guided_volume_change_rate`, `prior_volume_change_rate`, `market_decline_flag`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `macro_case_id`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (16)

For Sherwin-Williams, what is distinctive in refinish and EMEA decorative share gains, and is price part of it?

- `chemical.demand.fact_end_market_volume`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `demand_driver_id`, `volume_quantity`, `volume_change_rate`
- `chemical.demand.fact_share_position`: `share_rate`, `share_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `subsegment_id`, `country_id`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.price.fact_realized_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `customer_id`, `country_id`, `realized_change_rate`
- `chemical.price.fact_announced_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `announced_change_rate`, `in_guide_flag`, `added_after_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (1)

For Sherwin-Williams, what drove Performance Coatings margin outperformance beyond a mix shift toward packaging and auto refinish?

- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.demand.fact_packaging_conversion`: `fiscal_quarter_id`, `end_market_id`, `country_id`, `conversion_quantity`, `remaining_conversion_quantity`, `outgrowth_rate`, `lapped_flag`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.demand.fact_end_market_volume`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `demand_driver_id`, `volume_quantity`, `volume_change_rate`
- `chemical.price.fact_price_mix`: `margin_driver_id`, `packaging_mix_flag`, `refinish_mix_flag`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `mix_effect_rate`

### Q4 2025 (4)

For Sherwin-Williams, how is severe winter weather changing current demand, and could it pull first-quarter results below last year?

- `chemical.demand.fact_weather_demand`: `fiscal_quarter_id`, `weather_regime_id`, `demand_change_rate`, `below_last_year_flag`, `end_market_id`, `country_id`, `affected_quantity`
- `chemical.customer.dim_weather_regime`: `regime_name`, `regime_code`
- `chemical.demand.fact_end_market_volume`: `fiscal_quarter_id`, `demand_driver_id`, `business_segment_id`, `end_market_id`, `country_id`, `volume_quantity`, `volume_change_rate`
- `chemical.demand.fact_volume_outlook`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `macro_case_id`, `guided_volume_change_rate`, `prior_volume_change_rate`, `market_decline_flag`
- `chemical.demand.fact_customer_confidence`: `fiscal_quarter_id`, `end_market_id`, `business_segment_id`, `country_id`, `confidence_index`, `changed_flag`, `cautious_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (5)

For Sherwin-Williams, has packaging recovered past the prior correction, and how much industry conversion is left?

- `chemical.demand.fact_packaging_conversion`: `conversion_quantity`, `remaining_conversion_quantity`, `fiscal_quarter_id`, `end_market_id`, `country_id`, `outgrowth_rate`, `lapped_flag`
- `chemical.demand.fact_end_market_volume`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `demand_driver_id`, `volume_quantity`, `volume_change_rate`
- `chemical.demand.fact_industry_volume`: `industry_volume_quantity`, `industry_change_rate`, `company_versus_industry_rate`, `fiscal_quarter_id`, `end_market_id`, `subsegment_id`, `country_id`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (6)

For Sherwin-Williams, if the emphasis shifts from price to volume, why would competitors not match and erase the share gain?

- `chemical.demand.fact_end_market_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `demand_driver_id`
- `chemical.demand.fact_segment_volume`: `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `sales_change_rate`
- `chemical.price.fact_realized_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `customer_id`, `country_id`, `realized_change_rate`
- `chemical.price.fact_announced_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `announced_change_rate`, `in_guide_flag`, `added_after_flag`
- `chemical.price.fact_competitor_price`: `competitor_id`, `competitor_change_rate`, `can_match_flag`, `price_part_of_share_flag`, `company_uses_price_for_share_flag`, `fiscal_quarter_id`, `business_segment_id`
- `chemical.customer.dim_competitor`: `competitor_name`, `competitor_code`

### Q4 2025 (7)

For Sherwin-Williams, were residential repaint volumes flat or down if price rose faster than sales?

- `chemical.demand.fact_end_market_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `demand_driver_id`
- `chemical.demand.fact_repaint_cycle`: `fiscal_quarter_id`, `end_market_id`, `country_id`, `cycle_years`, `delayed_flag`, `labor_available_flag`, `solid_demand_flag`
- `chemical.price.fact_realized_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `customer_id`, `country_id`, `realized_change_rate`
- `chemical.price.fact_announced_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `announced_change_rate`, `in_guide_flag`, `added_after_flag`
- `chemical.demand.fact_segment_volume`: `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `country_id`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (8)

For Sherwin-Williams, how does Consumer Brands bridge from fourth-quarter growth that included Suvenil to the first-quarter and full-year outlook?

- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.supply.fact_integration`: `fiscal_quarter_id`, `acquisition_id`, `business_segment_id`, `action_name`, `started_flag`, `versus_base_flag`
- `chemical.network.dim_acquisition`: `business_segment_id`, `acquisition_name`, `acquisition_code`
- `chemical.price.fact_acquisition_margin`: `fiscal_quarter_id`, `acquisition_id`, `business_segment_id`, `drag_rate`, `excluded_margin_rate`, `dilution_rate`, `uses_original_case_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (9)

For Sherwin-Williams, does flat Paint Stores guidance imply share gain if the market is down and new stores add about a point of sales?

- `chemical.demand.fact_segment_volume`: `sales_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.demand.fact_end_market_volume`: `end_market_id`, `demand_driver_id`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`
- `chemical.demand.fact_industry_volume`: `end_market_id`, `fiscal_quarter_id`, `subsegment_id`, `country_id`, `industry_volume_quantity`, `industry_change_rate`, `company_versus_industry_rate`
- `chemical.supply.fact_store_network`: `store_id`, `net_store_count`, `sales_point_from_new_stores`, `fiscal_quarter_id`, `country_id`, `opening_count`, `closure_count`
- `chemical.supply.fact_growth_spend`: `share_of_spend_rate`, `fiscal_quarter_id`, `growth_program_id`, `business_segment_id`, `spend_amount`, `allocation_changed_flag`, `payback_months`

### Q4 2025 (10)

For Sherwin-Williams, what is delaying the five-to-seven-year repaint cycle after demand was pulled into 2021, including contractor labor?

- `chemical.demand.fact_end_market_volume`: `demand_driver_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `volume_quantity`, `volume_change_rate`
- `chemical.demand.fact_repaint_cycle`: `cycle_years`, `labor_available_flag`, `solid_demand_flag`, `fiscal_quarter_id`, `end_market_id`, `country_id`, `delayed_flag`
- `chemical.supply.fact_headcount`: `fiscal_quarter_id`, `headcount_role_id`, `business_segment_id`, `headcount_quantity`, `addition_quantity`, `implies_more_stores_flag`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (12)

For Sherwin-Williams, how does a coatings merger change the opportunity set in industrial-facing businesses?

- `chemical.demand.fact_segment_volume`: `business_segment_id`, `volume_change_rate`, `sales_change_rate`, `fiscal_quarter_id`, `country_id`, `volume_quantity`, `organic_volume_quantity`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.demand.fact_competitive_disruption`: `business_segment_id`, `opportunity_share_rate`, `disruption_flag`, `fiscal_quarter_id`, `subsegment_id`, `end_market_id`, `competitor_id`
- `chemical.customer.dim_competitor`: `competitor_name`, `competitor_code`
- `chemical.demand.fact_order_book`: `business_segment_id`, `fiscal_quarter_id`, `end_market_id`, `customer_id`, `order_pattern_id`, `order_quantity`, `duration_weeks`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (13)

For Sherwin-Williams, what volume and price-mix are showing in DIY in the fourth quarter and in the 2026 outlook?

- `chemical.demand.fact_end_market_volume`: `fiscal_quarter_id`, `volume_quantity`, `volume_change_rate`, `business_segment_id`, `end_market_id`, `country_id`, `demand_driver_id`
- `chemical.price.fact_price_mix`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `margin_driver_id`, `mix_effect_rate`, `unfavorable_flag`, `packaging_mix_flag`
- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `business_segment_id`, `country_id`, `sales_change_rate`
- `chemical.price.fact_realized_price`: `fiscal_quarter_id`, `price_action_id`, `business_segment_id`, `end_market_id`, `customer_id`, `country_id`, `realized_change_rate`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (1)

For Sherwin-Williams, how was the 7% Paint Stores price increase sized against raw materials and other costs?

- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.price.fact_realized_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `customer_id`, `country_id`, `realized_change_rate`
- `chemical.price.fact_announced_price`: `price_action_id`, `sized_to_cost_flag`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `announced_change_rate`, `in_guide_flag`
- `chemical.supply.fact_input_cost`: `cost_basket_id`, `contract_cost_amount`, `fiscal_quarter_id`, `raw_input_id`, `supplier_id`, `inflation_rate`, `outlook_band_code`
- `chemical.supply.fact_spot_cost`: `spot_cost_amount`, `fiscal_quarter_id`, `raw_input_id`, `peaked_flag`, `above_contract_flag`

### Q3 2025 (2)

For Sherwin-Williams, how far do mortgage rates need to fall before they catalyze Paint Stores demand?

- `chemical.demand.fact_mortgage_demand`: `rate_gap_to_threshold`, `demand_response_flag`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `threshold_crossed_flag`
- `chemical.demand.fact_segment_volume`: `volume_change_rate`, `sales_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `organic_volume_quantity`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.supply.fact_store_network`: `store_id`, `net_store_count`, `sales_point_from_new_stores`, `fiscal_quarter_id`, `country_id`, `opening_count`, `closure_count`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (5)

For Sherwin-Williams, is the more cautious tone on the second half of next year from specific demand signals or from current-trend conservatism?

- `chemical.demand.fact_volume_outlook`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `macro_case_id`, `guided_volume_change_rate`, `prior_volume_change_rate`, `market_decline_flag`
- `chemical.customer.dim_macro_case`: `case_name`, `case_code`
- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.supply.fact_store_network`: `store_id`, `net_store_count`, `sales_point_from_new_stores`, `fiscal_quarter_id`, `country_id`, `opening_count`, `closure_count`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (6)

For Sherwin-Williams, what are contractor backlogs and visibility over the next three to six months, and which Paint Stores submarkets sound confident versus cautious?

- `chemical.demand.fact_contractor_backlog`: `backlog_weeks`, `visibility_months`, `confident_location_count`, `cautious_location_count`, `fiscal_quarter_id`, `business_segment_id`, `subsegment_id`
- `chemical.market.dim_subsegment`: `end_market_id`, `business_segment_id`, `subsegment_name`, `subsegment_code`, `confidence_code`
- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (7)

For Sherwin-Williams, where are U.S. industry gallons down by architectural subsegment?

- `chemical.demand.fact_industry_volume`: `subsegment_id`, `industry_volume_quantity`, `industry_change_rate`, `company_versus_industry_rate`, `gallon_change_rate`, `fiscal_quarter_id`, `end_market_id`
- `chemical.market.dim_subsegment`: `business_segment_id`, `subsegment_name`, `subsegment_code`, `end_market_id`, `confidence_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (8)

For Sherwin-Williams, why is Performance Coatings showing negative operating leverage on positive sales, and do the same mix and cost dynamics persist in the fourth quarter?

- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `sales_change_rate`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.price.fact_price_mix`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `margin_driver_id`, `mix_effect_rate`, `unfavorable_flag`, `packaging_mix_flag`
- `chemical.price.fact_margin_bridge`: `fiscal_quarter_id`, `persists_next_quarter_flag`, `negative_leverage_flag`, `business_segment_id`, `margin_driver_id`, `labor_factor_id`, `effect_rate`
- `chemical.price.fact_operating_leverage`: `fiscal_quarter_id`, `leverage_basis_points`, `business_segment_id`, `flat_demand_margin_rate`, `hurt_rate`, `split_even_flag`
- `chemical.price.fact_segment_margin`: `fiscal_quarter_id`, `operating_margin_rate`, `quarter_dip_flag`, `business_segment_id`, `margin_driver_id`, `margin_change_rate`, `target_rate`

### Q3 2025 (9)

For Sherwin-Williams, how does a roughly flat second-half Paint Stores volume compare with a first-half organic decline in a lower-for-longer market?

- `chemical.demand.fact_segment_volume`: `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `sales_change_rate`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.demand.fact_end_market_volume`: `end_market_id`, `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `demand_driver_id`
- `chemical.supply.fact_store_network`: `store_id`, `net_store_count`, `sales_point_from_new_stores`, `fiscal_quarter_id`, `country_id`, `opening_count`, `closure_count`
- `chemical.demand.fact_volume_outlook`: `end_market_id`, `guided_volume_change_rate`, `prior_volume_change_rate`, `market_decline_flag`, `fiscal_quarter_id`, `business_segment_id`, `macro_case_id`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (11)

For Sherwin-Williams, how much does weak volume hurt the gross-margin rate, and what volume growth yields about 100 basis points of leverage?

- `chemical.demand.fact_end_market_volume`: `volume_quantity`, `volume_change_rate`, `run_rate_quantity`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`
- `chemical.demand.fact_segment_volume`: `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `country_id`
- `chemical.price.fact_gross_margin`: `gross_margin_rate`, `year_over_year_change_rate`, `flat_demand_margin_rate`, `fiscal_quarter_id`, `business_segment_id`, `above_fifty_flag`, `holds_without_recovery_flag`
- `chemical.price.fact_margin_bridge`: `margin_driver_id`, `effect_rate`, `negative_leverage_flag`, `fiscal_quarter_id`, `business_segment_id`, `labor_factor_id`, `effect_amount`
- `chemical.demand.fact_volume_outlook`: `guided_volume_change_rate`, `prior_volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `macro_case_id`, `market_decline_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (13)

For Sherwin-Williams, does pushing share gains in another soft year pull forward gains that would normally arrive in a recovery?

- `chemical.demand.fact_share_position`: `end_market_id`, `share_rate`, `share_change_rate`, `soft_year_pull_forward_flag`, `fiscal_quarter_id`, `business_segment_id`, `subsegment_id`
- `chemical.demand.fact_industry_volume`: `end_market_id`, `fiscal_quarter_id`, `subsegment_id`, `country_id`, `industry_volume_quantity`, `industry_change_rate`, `company_versus_industry_rate`
- `chemical.demand.fact_volume_outlook`: `end_market_id`, `market_decline_flag`, `fiscal_quarter_id`, `business_segment_id`, `macro_case_id`, `guided_volume_change_rate`, `prior_volume_change_rate`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (14)

For Sherwin-Williams, did non-residential Paint Stores businesses accelerate because delayed price rolled through or because those markets' demand accelerated?

- `chemical.demand.fact_contractor_backlog`: `business_segment_id`, `subsegment_id`, `fiscal_quarter_id`, `country_id`, `backlog_weeks`, `visibility_months`, `confident_location_count`
- `chemical.market.dim_subsegment`: `business_segment_id`, `end_market_id`, `subsegment_name`, `subsegment_code`, `confidence_code`
- `chemical.price.fact_realized_price`: `business_segment_id`, `end_market_id`, `price_action_id`, `realized_change_rate`, `versus_announced_rate`, `run_rate_flag`, `fiscal_quarter_id`
- `chemical.price.fact_announced_price`: `business_segment_id`, `end_market_id`, `price_action_id`, `announced_change_rate`, `fiscal_quarter_id`, `in_guide_flag`, `added_after_flag`
- `chemical.demand.fact_end_market_volume`: `business_segment_id`, `end_market_id`, `demand_driver_id`, `volume_change_rate`, `run_rate_quantity`, `fiscal_quarter_id`, `country_id`
- `chemical.demand.fact_volume_outlook`: `business_segment_id`, `end_market_id`, `guided_volume_change_rate`, `prior_volume_change_rate`, `market_decline_flag`, `fiscal_quarter_id`, `macro_case_id`

### Q2 2025 (1)

For Sherwin-Williams, what supports caution that demand could deteriorate in the back half, and where would that show up?

- `chemical.demand.fact_end_market_volume`: `end_market_id`, `demand_driver_id`, `volume_change_rate`, `run_rate_quantity`, `fiscal_quarter_id`, `business_segment_id`, `country_id`
- `chemical.demand.fact_volume_outlook`: `end_market_id`, `guided_volume_change_rate`, `prior_volume_change_rate`, `market_decline_flag`, `fiscal_quarter_id`, `business_segment_id`, `macro_case_id`
- `chemical.market.dim_end_market`: `end_market_name`, `end_market_code`, `business_segment_id`
- `chemical.demand.fact_customer_confidence`: `end_market_id`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `confidence_index`, `changed_flag`, `cautious_flag`
- `chemical.price.fact_realized_price`: `end_market_id`, `realized_change_rate`, `versus_announced_rate`, `run_rate_flag`, `fiscal_quarter_id`, `business_segment_id`, `customer_id`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (2)

For Sherwin-Williams, in which of the six Paint Stores subsegments would incremental competitive disruption yield the most share over the next year?

- `chemical.demand.fact_contractor_backlog`: `business_segment_id`, `subsegment_id`, `fiscal_quarter_id`, `country_id`, `backlog_weeks`, `visibility_months`, `confident_location_count`
- `chemical.market.dim_subsegment`: `business_segment_id`, `end_market_id`, `subsegment_name`, `subsegment_code`, `confidence_code`
- `chemical.demand.fact_share_position`: `business_segment_id`, `end_market_id`, `subsegment_id`, `share_rate`, `share_change_rate`, `soft_year_pull_forward_flag`, `fiscal_quarter_id`
- `chemical.demand.fact_industry_volume`: `end_market_id`, `subsegment_id`, `fiscal_quarter_id`, `country_id`, `industry_volume_quantity`, `industry_change_rate`, `company_versus_industry_rate`
- `chemical.demand.fact_segment_volume`: `business_segment_id`, `fiscal_quarter_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (6)

For Sherwin-Williams, is industry volume weakness expected to spill into early 2026, and which Paint Stores verticals would improve first?

- `chemical.demand.fact_industry_volume`: `industry_volume_quantity`, `industry_change_rate`, `company_versus_industry_rate`, `fiscal_quarter_id`, `end_market_id`, `subsegment_id`, `country_id`
- `chemical.demand.fact_share_position`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `subsegment_id`, `country_id`, `competitor_id`, `share_rate`
- `chemical.demand.fact_segment_volume`: `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `sales_change_rate`
- `chemical.market.dim_subsegment`: `business_segment_id`, `end_market_id`, `subsegment_name`, `subsegment_code`, `confidence_code`
- `chemical.demand.fact_volume_outlook`: `guided_volume_change_rate`, `prior_volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `macro_case_id`, `market_decline_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (7)

For Sherwin-Williams, how do Paint Stores volume declines compare with industry volumes in the quarter and for the full year?

- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `business_segment_id`, `country_id`, `sales_change_rate`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.demand.fact_industry_volume`: `fiscal_quarter_id`, `end_market_id`, `industry_volume_quantity`, `industry_change_rate`, `company_versus_industry_rate`, `subsegment_id`, `country_id`
- `chemical.demand.fact_share_position`: `fiscal_quarter_id`, `end_market_id`, `share_rate`, `share_change_rate`, `soft_year_pull_forward_flag`, `business_segment_id`, `subsegment_id`
- `chemical.supply.fact_store_network`: `fiscal_quarter_id`, `store_id`, `net_store_count`, `sales_point_from_new_stores`, `country_id`, `opening_count`, `closure_count`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (8)

For Sherwin-Williams, will new commercial and new residential hold current levels in the second half or fall with completions?

- `chemical.demand.fact_completion_demand`: `completion_quantity`, `half_code`, `fiscal_quarter_id`, `end_market_id`, `country_id`, `demand_quantity`, `holding_flag`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (13)

For Sherwin-Williams, what unfavorable mix drove Performance Coatings price, and was there a mix drag in Consumer Brands as well?

- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.price.fact_price_mix`: `unfavorable_flag`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `margin_driver_id`, `mix_effect_rate`, `packaging_mix_flag`
- `chemical.price.fact_margin_bridge`: `fiscal_quarter_id`, `business_segment_id`, `margin_driver_id`, `labor_factor_id`, `effect_rate`, `effect_amount`, `persists_next_quarter_flag`
- `chemical.demand.fact_order_book`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `customer_id`, `order_pattern_id`, `order_quantity`, `duration_weeks`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

## Ecolab

### Q1 2026 (2)

For Ecolab, does the guide assume stable demand with modest improvement, or a more cautious customer posture from energy costs and geopolitics?

- `chemical.demand.fact_end_market_volume`: `demand_driver_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `volume_quantity`, `volume_change_rate`
- `chemical.demand.fact_volume_outlook`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `macro_case_id`, `guided_volume_change_rate`, `prior_volume_change_rate`, `market_decline_flag`
- `chemical.supply.fact_delivered_cost`: `delivered_cost_amount`, `cost_change_rate`, `fiscal_quarter_id`, `raw_input_id`, `business_segment_id`, `tariff_component_amount`, `second_half_direction_code`
- `chemical.supply.dim_raw_input`: `input_name`, `input_code`
- `chemical.demand.fact_customer_confidence`: `confidence_index`, `cautious_flag`, `fiscal_quarter_id`, `end_market_id`, `business_segment_id`, `country_id`, `changed_flag`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`

### Q1 2026 (3)

For Ecolab, how is Ovivo tracking versus plan, and what cross-sell exists with core high-tech offerings and with CoolIT?

- `chemical.demand.fact_acquired_volume`: `versus_plan_rate`, `fiscal_quarter_id`, `acquisition_id`, `business_segment_id`, `acquired_quantity`, `in_run_rate_flag`
- `chemical.network.dim_acquisition`: `business_segment_id`, `acquisition_name`, `acquisition_code`
- `chemical.demand.fact_platform_volume`: `fiscal_quarter_id`, `program_id`, `business_segment_id`, `volume_quantity`, `growth_rate`, `above_thirty_percent_flag`, `dilution_uses_current_rate_flag`
- `chemical.supply.fact_capability`: `fiscal_quarter_id`, `product_platform_id`, `program_id`, `equipped_flag`, `bolt_on_required_flag`, `competitor_emphasizes_chemistry_flag`
- `chemical.demand.fact_water_volume`: `high_single_digit_decline_flag`, `fiscal_quarter_id`, `business_segment_id`, `vertical_id`, `end_market_id`, `country_id`, `volume_quantity`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`

### Q1 2026 (4)

How much faster is One Ecolab growing than the core, and what would accelerate it further?

- `chemical.demand.fact_program_coverage`: `coverage_rate`, `next_cohort_sales_driver_flag`, `fiscal_quarter_id`, `program_id`, `cohort_id`, `customer_id`, `covered_customer_count`
- `chemical.demand.fact_organic_growth`: `organic_growth_rate`, `faster_than_core_flag`, `fiscal_quarter_id`, `business_segment_id`, `program_id`, `country_id`, `volume_contributed_flag`
- `chemical.demand.fact_growth_mix`: `engine_mix_rate`, `core_mix_rate`, `core_growth_rate`, `engine_growth_rate`, `fiscal_quarter_id`, `business_segment_id`, `program_id`
- `chemical.program.dim_program`: `program_name`, `program_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (5)

For Ecolab, is Life Sciences organic strength the expected step-change, and how does growth change when new capacity comes online?

- `chemical.demand.fact_segment_volume`: `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`
- `chemical.supply.fact_capacity_addition`: `capacity_asset_id`, `capacity_quantity`, `online_flag`, `more_to_come_flag`, `fiscal_quarter_id`, `business_segment_id`, `contributing_flag`
- `chemical.supply.fact_capex_contribution`: `capacity_asset_id`, `fiscal_quarter_id`, `business_segment_id`, `capex_amount`, `still_to_contribute_flag`, `in_run_rate_flag`
- `chemical.price.fact_segment_margin`: `margin_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `margin_driver_id`, `operating_margin_rate`, `target_rate`, `quarter_dip_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (7)

For Ecolab, how do Ovivo, March raw-material inflation, and softer Heavy and Paper sales combine in Global Water margins?

- `chemical.demand.fact_water_volume`: `fiscal_quarter_id`, `business_segment_id`, `vertical_id`, `end_market_id`, `country_id`, `volume_quantity`, `volume_change_rate`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.demand.fact_acquired_volume`: `fiscal_quarter_id`, `acquisition_id`, `business_segment_id`, `acquired_quantity`, `versus_plan_rate`, `in_run_rate_flag`
- `chemical.network.dim_acquisition`: `business_segment_id`, `acquisition_name`, `acquisition_code`
- `chemical.demand.fact_site_activity`: `fiscal_quarter_id`, `end_market_id`, `country_id`, `site_status_id`, `open_site_count`, `closed_site_count`, `closures_stopped_flag`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`

### Q1 2026 (8)

For Ecolab, is Specialty growth inside Institutional and Specialty coming from digital and productivity tools rather than chemical volume, given weak foot traffic?

- `chemical.demand.fact_segment_volume`: `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `sales_change_rate`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.supply.fact_digital_install`: `product_platform_id`, `productivity_flag`, `fiscal_quarter_id`, `program_id`, `installed_quantity`
- `chemical.network.dim_product_platform`: `platform_name`, `platform_code`
- `chemical.demand.fact_end_market_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `demand_driver_id`
- `chemical.demand.fact_customer_traffic`: `traffic_index`, `weak_traffic_flag`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `visit_quantity`

### Q1 2026 (9)

For Ecolab, are Paper and basic industries turning because growth is improving or because mill closures have stopped?

- `chemical.demand.fact_site_activity`: `site_status_id`, `open_site_count`, `closed_site_count`, `closures_stopped_flag`, `fiscal_quarter_id`, `end_market_id`, `country_id`
- `chemical.demand.fact_water_volume`: `fiscal_quarter_id`, `business_segment_id`, `vertical_id`, `end_market_id`, `country_id`, `volume_quantity`, `volume_change_rate`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.customer.dim_site_status`: `status_name`, `status_code`
- `chemical.demand.fact_end_market_volume`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `demand_driver_id`, `volume_quantity`, `volume_change_rate`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (10)

For Ecolab, how fast is CoolIT growing above 30%, and do data-center competitors emphasize water-treatment chemistry or equipment?

- `chemical.demand.fact_platform_volume`: `above_thirty_percent_flag`, `fiscal_quarter_id`, `program_id`, `business_segment_id`, `volume_quantity`, `growth_rate`, `dilution_uses_current_rate_flag`
- `chemical.supply.fact_capability`: `competitor_emphasizes_chemistry_flag`, `fiscal_quarter_id`, `product_platform_id`, `program_id`, `equipped_flag`, `bolt_on_required_flag`
- `chemical.supply.fact_acquisition_cost`: `competitor_id`, `fiscal_quarter_id`, `business_segment_id`, `cost_amount`, `stepped_up_flag`, `competitive_pressure_flag`
- `chemical.customer.dim_competitor`: `competitor_name`, `competitor_code`
- `chemical.program.dim_program`: `program_name`, `program_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (11)

For Ecolab, is CoolIT dilution based on the original 30% growth case or on the much faster current sales rate?

- `chemical.demand.fact_platform_volume`: `growth_rate`, `dilution_uses_current_rate_flag`, `fiscal_quarter_id`, `program_id`, `business_segment_id`, `volume_quantity`, `above_thirty_percent_flag`
- `chemical.supply.fact_capability`: `fiscal_quarter_id`, `product_platform_id`, `program_id`, `equipped_flag`, `bolt_on_required_flag`, `competitor_emphasizes_chemistry_flag`
- `chemical.demand.fact_organic_growth`: `organic_growth_rate`, `faster_than_core_flag`, `fiscal_quarter_id`, `business_segment_id`, `program_id`, `country_id`, `volume_contributed_flag`
- `chemical.price.fact_earnings_bridge`: `earnings_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `margin_driver_id`, `offset_amount`, `intact_flag`, `price_led_flag`
- `chemical.price.fact_acquisition_margin`: `drag_rate`, `excluded_margin_rate`, `dilution_rate`, `uses_original_case_flag`, `fiscal_quarter_id`, `acquisition_id`, `business_segment_id`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (12)

For Ecolab, what share of pest locations is on the new connected traps?

- `chemical.demand.fact_location_coverage`: `covered_location_count`, `base_location_count`, `fiscal_quarter_id`, `program_id`, `country_id`, `coverage_rate`, `expected_coverage_rate`
- `chemical.program.dim_program`: `program_name`, `program_code`
- `chemical.supply.fact_acquisition_cost`: `fiscal_quarter_id`, `business_segment_id`, `competitor_id`, `cost_amount`, `stepped_up_flag`, `competitive_pressure_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (15)

For Ecolab, has the Middle East conflict changed customer confidence in any end market?

- `chemical.market.dim_end_market`: `end_market_name`, `end_market_code`, `business_segment_id`
- `chemical.demand.fact_end_market_volume`: `end_market_id`, `volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `demand_driver_id`, `volume_quantity`
- `chemical.demand.fact_customer_confidence`: `end_market_id`, `confidence_index`, `changed_flag`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `cautious_flag`
- `chemical.price.fact_realized_price`: `end_market_id`, `customer_id`, `realized_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `price_action_id`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (17)

For Ecolab, will transportation and green energy remain the main drivers of Light Water?

- `chemical.demand.fact_water_volume`: `driver_vertical_flag`, `fiscal_quarter_id`, `business_segment_id`, `vertical_id`, `end_market_id`, `country_id`, `volume_quantity`
- `chemical.market.dim_vertical`: `vertical_name`, `vertical_code`
- `chemical.demand.fact_end_market_volume`: `demand_driver_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `volume_quantity`, `volume_change_rate`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (1)

For Ecolab, how do paper, basic industries, and institutional inventory headwinds fade through the year against momentum in other businesses?

- `chemical.demand.fact_site_activity`: `volume_change_rate`, `fiscal_quarter_id`, `end_market_id`, `country_id`, `site_status_id`, `open_site_count`, `closed_site_count`
- `chemical.demand.fact_water_volume`: `business_segment_id`, `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `vertical_id`, `end_market_id`, `country_id`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.demand.fact_segment_volume`: `business_segment_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `fiscal_quarter_id`, `country_id`, `sales_change_rate`
- `chemical.demand.fact_customer_traffic`: `business_segment_id`, `fiscal_quarter_id`, `country_id`, `traffic_index`, `weak_traffic_flag`, `visit_quantity`
- `chemical.demand.fact_end_market_volume`: `business_segment_id`, `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `end_market_id`, `country_id`, `demand_driver_id`

### Q4 2025 (2)

For Ecolab, what growth rate and roadblocks apply to global high tech across water, semiconductors, and data centers after Ovivo?

- `chemical.demand.fact_water_volume`: `volume_change_rate`, `high_single_digit_decline_flag`, `fiscal_quarter_id`, `business_segment_id`, `vertical_id`, `end_market_id`, `country_id`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.market.dim_vertical`: `vertical_name`, `vertical_code`
- `chemical.demand.fact_platform_volume`: `growth_rate`, `dilution_uses_current_rate_flag`, `fiscal_quarter_id`, `program_id`, `business_segment_id`, `volume_quantity`, `above_thirty_percent_flag`
- `chemical.demand.fact_acquired_volume`: `versus_plan_rate`, `in_run_rate_flag`, `fiscal_quarter_id`, `acquisition_id`, `business_segment_id`, `acquired_quantity`
- `chemical.network.dim_acquisition`: `business_segment_id`, `acquisition_name`, `acquisition_code`

### Q4 2025 (3)

For Ecolab, why were pest incremental margins much stronger than Life Sciences incremental margins?

- `chemical.demand.fact_location_coverage`: `fiscal_quarter_id`, `program_id`, `country_id`, `covered_location_count`, `base_location_count`, `coverage_rate`, `expected_coverage_rate`
- `chemical.program.dim_program`: `program_name`, `program_code`
- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.supply.fact_capacity_addition`: `fiscal_quarter_id`, `capacity_asset_id`, `business_segment_id`, `capacity_quantity`, `online_flag`, `contributing_flag`, `more_to_come_flag`
- `chemical.price.fact_incremental_margin`: `incremental_margin_rate`, `stronger_than_peer_segment_flag`, `fiscal_quarter_id`, `business_segment_id`, `benchmark_rate`, `useful_for_other_segments_flag`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`

### Q4 2025 (4)

For Ecolab, why are light and heavy water diverging, with food and beverage improving and paper still a drag?

- `chemical.demand.fact_water_volume`: `fiscal_quarter_id`, `business_segment_id`, `vertical_id`, `end_market_id`, `country_id`, `volume_quantity`, `volume_change_rate`
- `chemical.market.dim_vertical`: `vertical_name`, `vertical_code`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.demand.fact_site_activity`: `fiscal_quarter_id`, `end_market_id`, `country_id`, `site_status_id`, `open_site_count`, `closed_site_count`, `closures_stopped_flag`
- `chemical.demand.fact_end_market_volume`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `demand_driver_id`, `volume_quantity`, `volume_change_rate`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (5)

For Ecolab, after normalizing for distributor inventory reductions, are underlying volumes actually rising?

- `chemical.demand.fact_segment_volume`: `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `sales_change_rate`
- `chemical.demand.fact_customer_traffic`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `traffic_index`, `weak_traffic_flag`, `visit_quantity`
- `chemical.demand.fact_distributor_inventory`: `inventory_quantity`, `reduction_quantity`, `underlying_volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `channel_id`, `country_id`
- `chemical.demand.fact_organic_growth`: `volume_contributed_flag`, `fiscal_quarter_id`, `business_segment_id`, `program_id`, `country_id`, `organic_growth_rate`, `price_contributed_flag`
- `chemical.demand.fact_end_market_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `demand_driver_id`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (6)

What feedback is coming from the first One Ecolab customers, and when does the rollout to the next cohort become a sales driver?

- `chemical.demand.fact_program_coverage`: `cohort_id`, `customer_id`, `covered_customer_count`, `targeted_customer_count`, `next_cohort_sales_driver_flag`, `fiscal_quarter_id`, `program_id`
- `chemical.demand.fact_organic_growth`: `fiscal_quarter_id`, `business_segment_id`, `program_id`, `country_id`, `organic_growth_rate`, `volume_contributed_flag`, `price_contributed_flag`
- `chemical.customer.dim_customer`: `customer_tier_id`, `customer_name`, `customer_code`, `country_id`, `channel_id`
- `chemical.program.dim_program`: `program_name`, `program_code`
- `chemical.customer.dim_cohort`: `cohort_name`, `cohort_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (7)

For Ecolab, where is IQ Suite penetration today versus the level expected in two to three years?

- `chemical.demand.fact_location_coverage`: `expected_coverage_rate`, `fiscal_quarter_id`, `program_id`, `country_id`, `covered_location_count`, `base_location_count`, `coverage_rate`
- `chemical.program.dim_program`: `program_name`, `program_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (8)

For Ecolab, what would push results to the high or low end of the 2026 guide?

- `chemical.demand.fact_guidance_case`: `demand_driver_id`, `high_end_flag`, `swing_rate`, `fiscal_quarter_id`, `business_segment_id`, `macro_case_id`, `low_end_flag`
- `chemical.customer.dim_macro_case`: `case_name`, `case_code`
- `chemical.demand.fact_end_market_volume`: `demand_driver_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `volume_quantity`, `volume_change_rate`
- `chemical.demand.fact_volume_outlook`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `macro_case_id`, `guided_volume_change_rate`, `prior_volume_change_rate`, `market_decline_flag`
- `chemical.price.fact_realized_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `customer_id`, `country_id`, `realized_change_rate`
- `chemical.price.fact_announced_price`: `price_action_id`, `in_guide_flag`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `announced_change_rate`, `added_after_flag`

### Q4 2025 (10)

For Ecolab, is specialty growth from earlier capacity investments now in the run rate, or is more still to come?

- `chemical.demand.fact_segment_volume`: `volume_change_rate`, `sales_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `organic_volume_quantity`
- `chemical.supply.fact_capacity_addition`: `capacity_asset_id`, `capacity_quantity`, `more_to_come_flag`, `fiscal_quarter_id`, `business_segment_id`, `online_flag`, `contributing_flag`
- `chemical.supply.fact_capex_contribution`: `capacity_asset_id`, `capex_amount`, `still_to_contribute_flag`, `in_run_rate_flag`, `fiscal_quarter_id`, `business_segment_id`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (11)

For Ecolab, is the expected acceleration in organic sales from basic industries stabilizing, or from faster growth in the higher-growth platforms as well?

- `chemical.demand.fact_organic_growth`: `organic_growth_rate`, `faster_than_core_flag`, `fiscal_quarter_id`, `business_segment_id`, `program_id`, `country_id`, `volume_contributed_flag`
- `chemical.demand.fact_growth_mix`: `core_growth_rate`, `engine_growth_rate`, `fiscal_quarter_id`, `business_segment_id`, `program_id`, `engine_mix_rate`, `core_mix_rate`
- `chemical.demand.fact_site_activity`: `fiscal_quarter_id`, `end_market_id`, `country_id`, `site_status_id`, `open_site_count`, `closed_site_count`, `closures_stopped_flag`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.demand.fact_end_market_volume`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `demand_driver_id`, `volume_quantity`, `volume_change_rate`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (12)

For Ecolab, is the Life Sciences margin setback from the capability build a multi-quarter drag or a one-quarter dip?

- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.supply.fact_capacity_addition`: `fiscal_quarter_id`, `capacity_asset_id`, `capacity_quantity`, `business_segment_id`, `online_flag`, `contributing_flag`, `more_to_come_flag`
- `chemical.price.fact_gross_margin`: `fiscal_quarter_id`, `gross_margin_rate`, `flat_demand_margin_rate`, `business_segment_id`, `year_over_year_change_rate`, `above_fifty_flag`, `holds_without_recovery_flag`
- `chemical.price.fact_segment_margin`: `fiscal_quarter_id`, `margin_driver_id`, `operating_margin_rate`, `margin_change_rate`, `quarter_dip_flag`, `business_segment_id`, `target_rate`
- `chemical.price.fact_margin_bridge`: `fiscal_quarter_id`, `margin_driver_id`, `persists_next_quarter_flag`, `business_segment_id`, `labor_factor_id`, `effect_rate`, `effect_amount`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (13)

For Ecolab, how is customer retention trending in Institutional and Specialty?

- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.demand.fact_customer_traffic`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `traffic_index`, `weak_traffic_flag`, `visit_quantity`
- `chemical.supply.fact_capacity_addition`: `fiscal_quarter_id`, `capacity_asset_id`, `business_segment_id`, `capacity_quantity`, `online_flag`, `contributing_flag`, `more_to_come_flag`
- `chemical.demand.fact_customer_retention`: `retained_customer_count`, `base_customer_count`, `retention_rate`, `fiscal_quarter_id`, `business_segment_id`, `country_id`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (1)

For Ecolab, how are data-center share gains being won and measured, and how does Ovivo change that position?

- `chemical.demand.fact_platform_volume`: `fiscal_quarter_id`, `program_id`, `business_segment_id`, `volume_quantity`, `growth_rate`, `above_thirty_percent_flag`, `dilution_uses_current_rate_flag`
- `chemical.market.dim_end_market`: `end_market_name`, `end_market_code`, `business_segment_id`
- `chemical.demand.fact_share_position`: `end_market_id`, `share_rate`, `share_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `subsegment_id`, `country_id`
- `chemical.demand.fact_industry_volume`: `end_market_id`, `industry_change_rate`, `gallon_change_rate`, `fiscal_quarter_id`, `subsegment_id`, `country_id`, `industry_volume_quantity`
- `chemical.demand.fact_acquired_volume`: `fiscal_quarter_id`, `acquisition_id`, `business_segment_id`, `acquired_quantity`, `versus_plan_rate`, `in_run_rate_flag`
- `chemical.network.dim_acquisition`: `business_segment_id`, `acquisition_name`, `acquisition_code`

### Q3 2025 (2)

For Ecolab, how do resource shifts, innovation, and share gains offset end-market weakness as basic industries and paper return toward growth?

- `chemical.demand.fact_site_activity`: `end_market_id`, `fiscal_quarter_id`, `country_id`, `site_status_id`, `open_site_count`, `closed_site_count`, `closures_stopped_flag`
- `chemical.market.dim_end_market`: `end_market_name`, `end_market_code`, `business_segment_id`
- `chemical.demand.fact_water_volume`: `end_market_id`, `fiscal_quarter_id`, `business_segment_id`, `vertical_id`, `country_id`, `volume_quantity`, `volume_change_rate`
- `chemical.demand.fact_share_position`: `end_market_id`, `share_rate`, `share_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `subsegment_id`, `country_id`
- `chemical.demand.fact_competitive_disruption`: `end_market_id`, `opportunity_share_rate`, `fiscal_quarter_id`, `business_segment_id`, `subsegment_id`, `competitor_id`, `disruption_flag`
- `chemical.supply.fact_innovation_pipeline`: `end_market_id`, `offsets_weakness_flag`, `share_gain_flag`, `fiscal_quarter_id`, `business_segment_id`, `project_count`

### Q3 2025 (4)

For Ecolab, how is the water top line flowing through segment margin, split across the businesses inside water?

- `chemical.demand.fact_water_volume`: `business_segment_id`, `fiscal_quarter_id`, `vertical_id`, `end_market_id`, `country_id`, `volume_quantity`, `volume_change_rate`
- `chemical.price.fact_segment_margin`: `business_segment_id`, `margin_driver_id`, `operating_margin_rate`, `margin_change_rate`, `fiscal_quarter_id`, `target_rate`, `quarter_dip_flag`
- `chemical.price.fact_gross_margin`: `business_segment_id`, `gross_margin_rate`, `flat_demand_margin_rate`, `fiscal_quarter_id`, `year_over_year_change_rate`, `above_fifty_flag`, `holds_without_recovery_flag`
- `chemical.price.fact_price_mix`: `business_segment_id`, `margin_driver_id`, `fiscal_quarter_id`, `end_market_id`, `mix_effect_rate`, `unfavorable_flag`, `packaging_mix_flag`
- `chemical.price.fact_margin_bridge`: `business_segment_id`, `margin_driver_id`, `fiscal_quarter_id`, `labor_factor_id`, `effect_rate`, `effect_amount`, `persists_next_quarter_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (5)

Where will One Ecolab stand with the top customers by year-end, and how far does the rollout extend next year?

- `chemical.demand.fact_program_coverage`: `customer_id`, `covered_customer_count`, `targeted_customer_count`, `next_cohort_sales_driver_flag`, `fiscal_quarter_id`, `program_id`, `cohort_id`
- `chemical.demand.fact_organic_growth`: `fiscal_quarter_id`, `business_segment_id`, `program_id`, `country_id`, `organic_growth_rate`, `volume_contributed_flag`, `price_contributed_flag`
- `chemical.customer.dim_customer`: `customer_tier_id`, `customer_name`, `customer_code`, `country_id`, `channel_id`
- `chemical.program.dim_program`: `program_name`, `program_code`
- `chemical.customer.dim_cohort`: `cohort_name`, `cohort_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (6)

For Ecolab, as pest and Life Sciences lap growth investments, is SG&A leverage a straight line to the 2027 targets or another step-up in spend?

- `chemical.demand.fact_location_coverage`: `fiscal_quarter_id`, `program_id`, `country_id`, `covered_location_count`, `base_location_count`, `coverage_rate`, `expected_coverage_rate`
- `chemical.program.dim_program`: `program_name`, `program_code`
- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.supply.fact_capacity_addition`: `fiscal_quarter_id`, `capacity_asset_id`, `business_segment_id`, `capacity_quantity`, `online_flag`, `contributing_flag`, `more_to_come_flag`
- `chemical.supply.fact_sga`: `spend_amount`, `leverage_flag`, `step_up_flag`, `fiscal_quarter_id`, `business_segment_id`, `mostly_headcount_flag`
- `chemical.price.fact_margin_target`: `target_margin_rate`, `straight_line_flag`, `fiscal_quarter_id`, `business_segment_id`, `current_margin_rate`, `gap_rate`, `holds_in_low_demand_flag`

### Q3 2025 (7)

For Ecolab, how long before the faster growth engines are large enough to lift the 85% core that is growing more slowly?

- `chemical.demand.fact_growth_mix`: `engine_mix_rate`, `core_mix_rate`, `core_growth_rate`, `engine_growth_rate`, `large_enough_flag`, `fiscal_quarter_id`, `business_segment_id`
- `chemical.program.dim_program`: `program_name`, `program_code`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.price.fact_price_mix`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `margin_driver_id`, `mix_effect_rate`, `unfavorable_flag`, `packaging_mix_flag`
- `chemical.price.fact_margin_bridge`: `fiscal_quarter_id`, `business_segment_id`, `margin_driver_id`, `labor_factor_id`, `effect_rate`, `effect_amount`, `persists_next_quarter_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (9)

For Ecolab, did water volume grow, and was basic industries and paper volume down at a high-single-digit rate?

- `chemical.demand.fact_water_volume`: `volume_quantity`, `volume_change_rate`, `high_single_digit_decline_flag`, `fiscal_quarter_id`, `business_segment_id`, `vertical_id`, `end_market_id`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.demand.fact_site_activity`: `volume_change_rate`, `fiscal_quarter_id`, `end_market_id`, `country_id`, `site_status_id`, `open_site_count`, `closed_site_count`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.demand.fact_end_market_volume`: `volume_quantity`, `volume_change_rate`, `run_rate_quantity`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (10)

How much did One Ecolab cross-sell contribute to organic growth?

- `chemical.demand.fact_program_coverage`: `fiscal_quarter_id`, `program_id`, `cohort_id`, `customer_id`, `covered_customer_count`, `targeted_customer_count`, `coverage_rate`
- `chemical.demand.fact_organic_growth`: `organic_growth_rate`, `fiscal_quarter_id`, `business_segment_id`, `program_id`, `country_id`, `volume_contributed_flag`, `price_contributed_flag`
- `chemical.demand.fact_cross_sell`: `cross_sell_quantity`, `fiscal_quarter_id`, `program_id`, `business_segment_id`, `customer_id`, `contribution_rate`, `with_core_flag`
- `chemical.program.dim_program`: `program_name`, `program_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (11)

For Ecolab, what underlying food-and-beverage market dynamics sit under the best organic growth in several quarters?

- `chemical.demand.fact_water_volume`: `fiscal_quarter_id`, `end_market_id`, `business_segment_id`, `vertical_id`, `country_id`, `volume_quantity`, `volume_change_rate`
- `chemical.market.dim_end_market`: `end_market_name`, `end_market_code`, `business_segment_id`
- `chemical.demand.fact_organic_growth`: `fiscal_quarter_id`, `organic_growth_rate`, `business_segment_id`, `program_id`, `country_id`, `volume_contributed_flag`, `price_contributed_flag`
- `chemical.demand.fact_cross_sell`: `fiscal_quarter_id`, `program_id`, `business_segment_id`, `customer_id`, `cross_sell_quantity`, `contribution_rate`, `with_core_flag`
- `chemical.price.fact_realized_price`: `fiscal_quarter_id`, `end_market_id`, `business_segment_id`, `customer_id`, `country_id`, `price_action_id`, `realized_change_rate`
- `chemical.price.fact_announced_price`: `fiscal_quarter_id`, `end_market_id`, `business_segment_id`, `price_action_id`, `announced_change_rate`, `in_guide_flag`, `added_after_flag`

### Q3 2025 (12)

For Ecolab, have pest customer-acquisition costs or competition from major players stepped up?

- `chemical.demand.fact_location_coverage`: `fiscal_quarter_id`, `program_id`, `country_id`, `covered_location_count`, `base_location_count`, `coverage_rate`, `expected_coverage_rate`
- `chemical.program.dim_program`: `program_name`, `program_code`
- `chemical.supply.fact_acquisition_cost`: `cost_amount`, `stepped_up_flag`, `fiscal_quarter_id`, `business_segment_id`, `competitor_id`, `competitive_pressure_flag`
- `chemical.customer.dim_competitor`: `competitor_name`, `competitor_code`
- `chemical.supply.fact_capability`: `fiscal_quarter_id`, `product_platform_id`, `program_id`, `equipped_flag`, `bolt_on_required_flag`, `competitor_emphasizes_chemistry_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (1)

For Ecolab, what puts and takes kept the second-half outlook from moving up after an in-line quarter?

- `chemical.demand.fact_guidance_case`: `fiscal_quarter_id`, `demand_driver_id`, `business_segment_id`, `macro_case_id`, `high_end_flag`, `low_end_flag`, `swing_rate`
- `chemical.demand.fact_volume_outlook`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `macro_case_id`, `guided_volume_change_rate`, `prior_volume_change_rate`, `market_decline_flag`
- `chemical.price.fact_price_guide`: `fiscal_quarter_id`, `half_code`, `business_segment_id`, `price_action_id`, `macro_case_id`, `guided_price_change_rate`, `january_only_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (3)

For Ecolab, how are pest-intelligence rollouts coming together, and what are the puts and takes for pest growth?

- `chemical.demand.fact_location_coverage`: `fiscal_quarter_id`, `program_id`, `country_id`, `covered_location_count`, `base_location_count`, `coverage_rate`, `expected_coverage_rate`
- `chemical.program.dim_program`: `program_name`, `program_code`
- `chemical.supply.fact_acquisition_cost`: `fiscal_quarter_id`, `business_segment_id`, `competitor_id`, `cost_amount`, `stepped_up_flag`, `competitive_pressure_flag`
- `chemical.demand.fact_organic_growth`: `organic_growth_rate`, `fiscal_quarter_id`, `business_segment_id`, `program_id`, `country_id`, `volume_contributed_flag`, `price_contributed_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (6)

For Ecolab, what is pulling Institutional and Life Sciences margins up despite a sluggish macro and growth spend?

- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.demand.fact_customer_traffic`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `traffic_index`, `weak_traffic_flag`, `visit_quantity`
- `chemical.supply.fact_capacity_addition`: `fiscal_quarter_id`, `capacity_asset_id`, `business_segment_id`, `capacity_quantity`, `online_flag`, `contributing_flag`, `more_to_come_flag`
- `chemical.price.fact_gross_margin`: `gross_margin_rate`, `flat_demand_margin_rate`, `fiscal_quarter_id`, `business_segment_id`, `year_over_year_change_rate`, `above_fifty_flag`, `holds_without_recovery_flag`
- `chemical.price.fact_segment_margin`: `margin_driver_id`, `operating_margin_rate`, `margin_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `target_rate`, `quarter_dip_flag`
- `chemical.supply.fact_growth_spend`: `growth_program_id`, `spend_amount`, `share_of_spend_rate`, `fiscal_quarter_id`, `business_segment_id`, `allocation_changed_flag`, `payback_months`

### Q2 2025 (8)

For Ecolab, is the second-half challenge getting better price in water, including paper and heavy industry where volume is contracting?

- `chemical.demand.fact_water_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `vertical_id`, `end_market_id`, `country_id`
- `chemical.price.fact_segment_margin`: `fiscal_quarter_id`, `business_segment_id`, `margin_driver_id`, `operating_margin_rate`, `margin_change_rate`, `target_rate`, `quarter_dip_flag`
- `chemical.demand.fact_site_activity`: `volume_change_rate`, `fiscal_quarter_id`, `end_market_id`, `country_id`, `site_status_id`, `open_site_count`, `closed_site_count`
- `chemical.market.dim_vertical`: `vertical_name`, `vertical_code`
- `chemical.price.fact_realized_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `customer_id`, `country_id`, `realized_change_rate`
- `chemical.price.fact_announced_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `announced_change_rate`, `in_guide_flag`, `added_after_flag`

### Q2 2025 (9)

For Ecolab, what is driving the expected sequential drop in Life Sciences margin from nearly 20% back toward the mid-teens?

- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.supply.fact_capacity_addition`: `fiscal_quarter_id`, `capacity_asset_id`, `business_segment_id`, `capacity_quantity`, `online_flag`, `contributing_flag`, `more_to_come_flag`
- `chemical.price.fact_gross_margin`: `gross_margin_rate`, `flat_demand_margin_rate`, `fiscal_quarter_id`, `business_segment_id`, `year_over_year_change_rate`, `above_fifty_flag`, `holds_without_recovery_flag`
- `chemical.price.fact_segment_margin`: `margin_driver_id`, `operating_margin_rate`, `margin_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `target_rate`, `quarter_dip_flag`
- `chemical.price.fact_margin_bridge`: `margin_driver_id`, `fiscal_quarter_id`, `business_segment_id`, `labor_factor_id`, `effect_rate`, `effect_amount`, `persists_next_quarter_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (11)

For Ecolab, does weakness in basic industries require portfolio, resource, or productivity actions, or is the current approach enough?

- `chemical.demand.fact_site_activity`: `fiscal_quarter_id`, `end_market_id`, `country_id`, `site_status_id`, `open_site_count`, `closed_site_count`, `closures_stopped_flag`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.demand.fact_growth_mix`: `large_enough_flag`, `fiscal_quarter_id`, `business_segment_id`, `program_id`, `engine_mix_rate`, `core_mix_rate`, `core_growth_rate`
- `chemical.supply.fact_resource_shift`: `cost_action_id`, `portfolio_action_flag`, `current_approach_enough_flag`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `shift_underway_flag`
- `chemical.supply.fact_restructuring_savings`: `cost_action_id`, `source_code`, `fiscal_quarter_id`, `business_segment_id`, `savings_amount`, `doubled_flag`, `accelerates_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`
