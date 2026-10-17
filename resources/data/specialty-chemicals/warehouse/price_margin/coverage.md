# Chemical Inc price and margin

Price and margin owns announced price, realized price, mix, gross margin, segment margin, earnings bridges, and value capture for Chemical Inc. A price or margin row does not store unit volume. Raw-material unit cost stays on the supply cost facts.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `business_segment_identity` | `business_segment_id` | `sf:chemical.market.dim_business_segment` `business_segment_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:chemical.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `end_market_identity` | `end_market_id` | `sf:chemical.market.dim_end_market` `end_market_id` |
| `customer_identity` | `customer_id` | `sf:chemical.customer.dim_customer` `customer_id` |
| `country_identity` | `country_id` | `sf:chemical.geography.dim_country` `country_id` |
| `macro_case_identity` | `macro_case_id` | `sf:chemical.customer.dim_macro_case` `macro_case_id` |
| `acquisition_identity` | `acquisition_id` | `sf:chemical.network.dim_acquisition` `acquisition_id` |
| `program_identity` | `program_id` | `sf:chemical.program.dim_program` `program_id` |
| `raw_input_identity` | `raw_input_id` | `sf:chemical.supply.dim_raw_input` `raw_input_id` |
| `competitor_identity` | `competitor_id` | `sf:chemical.customer.dim_competitor` `competitor_id` |

## Numbered questions

## Sherwin-Williams

### Q1 2026 (1)

For Sherwin-Williams, why is pricing more surgical by customer and end market than in earlier cost-inflation cycles?

- `chemical.price.fact_realized_price`: `end_market_id`, `customer_id`, `surgical_flag`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `price_action_id`
- `chemical.price.fact_announced_price`: `end_market_id`, `sized_to_cost_flag`, `fiscal_quarter_id`, `business_segment_id`, `price_action_id`, `announced_change_rate`, `in_guide_flag`
- `chemical.market.dim_end_market`: `end_market_name`, `end_market_code`, `business_segment_id`
- `chemical.demand.fact_end_market_volume`: `end_market_id`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `demand_driver_id`, `volume_quantity`, `volume_change_rate`
- `chemical.supply.fact_input_cost`: `cost_basket_id`, `contract_cost_amount`, `inflation_rate`, `fiscal_quarter_id`, `raw_input_id`, `supplier_id`, `outlook_band_code`
- `chemical.supply.fact_spot_cost`: `spot_cost_amount`, `fiscal_quarter_id`, `raw_input_id`, `peaked_flag`, `above_contract_flag`

### Q1 2026 (6)

For Sherwin-Williams, is realization on the January price increase ahead of plan, and are those customer conversations finished?

- `chemical.price.fact_announced_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `announced_change_rate`, `in_guide_flag`, `added_after_flag`
- `chemical.price.fact_realized_price`: `customer_id`, `price_action_id`, `ahead_of_plan_flag`, `conversations_finished_flag`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`
- `chemical.customer.dim_customer`: `customer_tier_id`, `customer_name`, `customer_code`, `country_id`, `channel_id`
- `chemical.price.dim_price_action`: `business_segment_id`, `action_name`, `action_code`, `announced_date`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (7)

For Sherwin-Williams, what was first-quarter gross-margin expansion excluding Suvenil, and can gross margin rise in each quarter year over year?

- `chemical.price.fact_gross_margin`: `fiscal_quarter_id`, `gross_margin_rate`, `year_over_year_change_rate`, `flat_demand_margin_rate`, `business_segment_id`, `above_fifty_flag`, `holds_without_recovery_flag`
- `chemical.price.fact_margin_bridge`: `fiscal_quarter_id`, `margin_driver_id`, `persists_next_quarter_flag`, `business_segment_id`, `labor_factor_id`, `effect_rate`, `effect_amount`
- `chemical.supply.fact_integration`: `fiscal_quarter_id`, `acquisition_id`, `business_segment_id`, `action_name`, `started_flag`, `versus_base_flag`
- `chemical.network.dim_acquisition`: `business_segment_id`, `acquisition_name`, `acquisition_code`
- `chemical.price.fact_acquisition_margin`: `fiscal_quarter_id`, `excluded_margin_rate`, `acquisition_id`, `business_segment_id`, `drag_rate`, `dilution_rate`, `uses_original_case_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (9)

For Sherwin-Williams, is the higher price in the guide only the January increase, or pricing added after early March?

- `chemical.price.fact_realized_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `customer_id`, `country_id`, `realized_change_rate`
- `chemical.price.fact_announced_price`: `price_action_id`, `in_guide_flag`, `added_after_flag`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `announced_change_rate`
- `chemical.price.fact_price_guide`: `price_action_id`, `guided_price_change_rate`, `january_only_flag`, `net_price_tailwind_rate`, `fiscal_quarter_id`, `business_segment_id`, `macro_case_id`
- `chemical.price.dim_price_action`: `business_segment_id`, `action_name`, `action_code`, `announced_date`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (2)

For Sherwin-Williams, what labor, raw-basket, and titanium-dioxide utilization assumptions sit inside the gross-margin guide?

- `chemical.price.fact_gross_margin`: `gross_margin_rate`, `flat_demand_margin_rate`, `fiscal_quarter_id`, `business_segment_id`, `year_over_year_change_rate`, `above_fifty_flag`, `holds_without_recovery_flag`
- `chemical.price.fact_margin_bridge`: `margin_driver_id`, `labor_factor_id`, `fiscal_quarter_id`, `business_segment_id`, `effect_rate`, `effect_amount`, `persists_next_quarter_flag`
- `chemical.supply.fact_manufacturing_cost`: `labor_factor_id`, `in_guide_flag`, `labor_component_amount`, `fiscal_quarter_id`, `plant_id`, `business_segment_id`, `cost_amount`
- `chemical.price.dim_labor_factor`: `factor_name`, `factor_code`
- `chemical.supply.fact_input_cost`: `cost_basket_id`, `fiscal_quarter_id`, `raw_input_id`, `supplier_id`, `contract_cost_amount`, `inflation_rate`, `outlook_band_code`
- `chemical.supply.dim_raw_input`: `input_name`, `input_code`

### Q4 2025 (3)

For Sherwin-Williams, why would fourth-quarter price-mix plus the January increase not produce a larger first-quarter price-mix?

- `chemical.price.fact_price_mix`: `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `margin_driver_id`, `mix_effect_rate`, `unfavorable_flag`, `packaging_mix_flag`
- `chemical.price.fact_realized_price`: `fiscal_quarter_id`, `price_action_id`, `business_segment_id`, `end_market_id`, `customer_id`, `country_id`, `realized_change_rate`
- `chemical.price.fact_announced_price`: `fiscal_quarter_id`, `price_action_id`, `business_segment_id`, `end_market_id`, `announced_change_rate`, `in_guide_flag`, `added_after_flag`
- `chemical.price.dim_price_action`: `business_segment_id`, `action_name`, `action_code`, `announced_date`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (11)

For Sherwin-Williams, is low-single-digit realization on the 7% increase a near-term rate or the full run rate over the next few quarters?

- `chemical.price.fact_realized_price`: `fiscal_quarter_id`, `price_action_id`, `realized_change_rate`, `versus_announced_rate`, `run_rate_flag`, `business_segment_id`, `end_market_id`
- `chemical.price.fact_announced_price`: `fiscal_quarter_id`, `price_action_id`, `announced_change_rate`, `business_segment_id`, `end_market_id`, `in_guide_flag`, `added_after_flag`
- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `volume_change_rate`, `sales_change_rate`, `business_segment_id`, `country_id`, `volume_quantity`, `organic_volume_quantity`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.supply.fact_store_network`: `fiscal_quarter_id`, `store_id`, `net_store_count`, `sales_point_from_new_stores`, `country_id`, `opening_count`, `closure_count`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (14)

For Sherwin-Williams, what net price tailwind is expected in 2026 versus trend pricing without a sharp cyclical recovery?

- `chemical.price.fact_net_price`: `net_price_change_rate`, `trend_price_change_rate`, `tailwind_rate`, `fiscal_quarter_id`, `business_segment_id`
- `chemical.price.fact_price_guide`: `price_action_id`, `guided_price_change_rate`, `net_price_tailwind_rate`, `fiscal_quarter_id`, `business_segment_id`, `macro_case_id`, `january_only_flag`
- `chemical.demand.fact_end_market_volume`: `demand_driver_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `volume_quantity`, `volume_change_rate`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (10)

For Sherwin-Williams, can gross margin hold at or above 50% without a material volume recovery?

- `chemical.price.fact_gross_margin`: `gross_margin_rate`, `year_over_year_change_rate`, `above_fifty_flag`, `flat_demand_margin_rate`, `holds_without_recovery_flag`, `fiscal_quarter_id`, `business_segment_id`
- `chemical.price.fact_margin_bridge`: `margin_driver_id`, `fiscal_quarter_id`, `business_segment_id`, `labor_factor_id`, `effect_rate`, `effect_amount`, `persists_next_quarter_flag`
- `chemical.demand.fact_end_market_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `demand_driver_id`
- `chemical.demand.fact_segment_volume`: `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `sales_change_rate`
- `chemical.price.fact_acquisition_margin`: `excluded_margin_rate`, `fiscal_quarter_id`, `acquisition_id`, `business_segment_id`, `drag_rate`, `dilution_rate`, `uses_original_case_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (12)

For Sherwin-Williams, is a roughly 30% incremental margin on low-single-digit store volume a useful benchmark for other segments when demand improves?

- `chemical.price.fact_incremental_margin`: `business_segment_id`, `incremental_margin_rate`, `benchmark_rate`, `useful_for_other_segments_flag`, `stronger_than_peer_segment_flag`, `fiscal_quarter_id`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.demand.fact_segment_volume`: `business_segment_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `fiscal_quarter_id`, `country_id`, `sales_change_rate`
- `chemical.supply.fact_store_network`: `store_id`, `net_store_count`, `sales_point_from_new_stores`, `fiscal_quarter_id`, `country_id`, `opening_count`, `closure_count`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (5)

For Sherwin-Williams, how much of the gross-margin pressure was architectural volume, and what would the rate have been if volume were flat or up?

- `chemical.price.fact_gross_margin`: `gross_margin_rate`, `year_over_year_change_rate`, `flat_demand_margin_rate`, `fiscal_quarter_id`, `business_segment_id`, `above_fifty_flag`, `holds_without_recovery_flag`
- `chemical.price.fact_margin_bridge`: `margin_driver_id`, `effect_rate`, `fiscal_quarter_id`, `business_segment_id`, `labor_factor_id`, `effect_amount`, `persists_next_quarter_flag`
- `chemical.demand.fact_end_market_volume`: `volume_quantity`, `volume_change_rate`, `run_rate_quantity`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`
- `chemical.price.fact_operating_leverage`: `flat_demand_margin_rate`, `hurt_rate`, `fiscal_quarter_id`, `business_segment_id`, `leverage_basis_points`, `split_even_flag`
- `chemical.price.fact_acquisition_margin`: `drag_rate`, `excluded_margin_rate`, `dilution_rate`, `fiscal_quarter_id`, `acquisition_id`, `business_segment_id`, `uses_original_case_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (9)

For Sherwin-Williams, what role does price play in pursuing share and volume across end markets?

- `chemical.price.fact_realized_price`: `end_market_id`, `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `customer_id`, `country_id`, `realized_change_rate`
- `chemical.price.fact_announced_price`: `end_market_id`, `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `announced_change_rate`, `in_guide_flag`, `added_after_flag`
- `chemical.demand.fact_end_market_volume`: `end_market_id`, `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `demand_driver_id`
- `chemical.demand.fact_segment_volume`: `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `sales_change_rate`
- `chemical.market.dim_end_market`: `end_market_name`, `end_market_code`, `business_segment_id`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

## Ecolab

### Q1 2026 (1)

For Ecolab, why is gross margin expected to stabilize in the second half, and how does the energy surcharge fit that path?

- `chemical.price.fact_gross_margin`: `gross_margin_rate`, `flat_demand_margin_rate`, `fiscal_quarter_id`, `business_segment_id`, `year_over_year_change_rate`, `above_fifty_flag`, `holds_without_recovery_flag`
- `chemical.price.fact_margin_bridge`: `margin_driver_id`, `fiscal_quarter_id`, `business_segment_id`, `labor_factor_id`, `effect_rate`, `effect_amount`, `persists_next_quarter_flag`
- `chemical.price.fact_surcharge_realization`: `surcharge_id`, `half_code`, `fiscal_quarter_id`, `customer_id`, `business_segment_id`, `realized_rate`, `approached_customer_rate`
- `chemical.price.dim_surcharge`: `surcharge_name`, `surcharge_code`
- `chemical.supply.fact_input_cost`: `half_code`, `fiscal_quarter_id`, `raw_input_id`, `cost_basket_id`, `supplier_id`, `contract_cost_amount`, `inflation_rate`
- `chemical.supply.fact_spot_cost`: `fiscal_quarter_id`, `raw_input_id`, `spot_cost_amount`, `peaked_flag`, `above_contract_flag`

### Q1 2026 (6)

For Ecolab, what puts and takes sit between current margins and the 2027 targets in Institutional and other markets?

- `chemical.price.fact_segment_margin`: `margin_driver_id`, `operating_margin_rate`, `margin_change_rate`, `target_rate`, `fiscal_quarter_id`, `business_segment_id`, `quarter_dip_flag`
- `chemical.price.fact_margin_target`: `current_margin_rate`, `target_margin_rate`, `fiscal_quarter_id`, `business_segment_id`, `gap_rate`, `holds_in_low_demand_flag`, `straight_line_flag`
- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.demand.fact_customer_traffic`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `traffic_index`, `weak_traffic_flag`, `visit_quantity`
- `chemical.supply.fact_input_cost`: `fiscal_quarter_id`, `raw_input_id`, `cost_basket_id`, `supplier_id`, `contract_cost_amount`, `inflation_rate`, `outlook_band_code`
- `chemical.supply.fact_spot_cost`: `fiscal_quarter_id`, `raw_input_id`, `spot_cost_amount`, `peaked_flag`, `above_contract_flag`

### Q1 2026 (13)

For Ecolab, is value capture rising as a percentage of the portfolio, and is it higher in the newer businesses?

- `chemical.price.fact_realized_price`: `business_segment_id`, `fiscal_quarter_id`, `end_market_id`, `customer_id`, `country_id`, `price_action_id`, `realized_change_rate`
- `chemical.price.fact_announced_price`: `business_segment_id`, `fiscal_quarter_id`, `end_market_id`, `price_action_id`, `announced_change_rate`, `in_guide_flag`, `added_after_flag`
- `chemical.price.fact_value_capture`: `business_segment_id`, `value_metric_id`, `rising_flag`, `higher_in_newer_flag`, `value_case_clear_flag`, `fiscal_quarter_id`, `program_id`
- `chemical.price.dim_value_metric`: `metric_name`, `metric_code`
- `chemical.demand.fact_growth_mix`: `business_segment_id`, `fiscal_quarter_id`, `program_id`, `engine_mix_rate`, `core_mix_rate`, `core_growth_rate`, `engine_growth_rate`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (14)

For Ecolab, what share of customers targeted for the energy surcharge have already been approached?

- `chemical.price.fact_surcharge_realization`: `surcharge_id`, `customer_id`, `approached_customer_rate`, `fiscal_quarter_id`, `business_segment_id`, `realized_rate`, `competitor_support_flag`
- `chemical.price.dim_surcharge`: `surcharge_name`, `surcharge_code`
- `chemical.customer.dim_customer`: `customer_tier_id`, `customer_name`, `customer_code`, `country_id`, `channel_id`
- `chemical.price.fact_gross_margin`: `fiscal_quarter_id`, `business_segment_id`, `gross_margin_rate`, `year_over_year_change_rate`, `above_fifty_flag`, `flat_demand_margin_rate`, `holds_without_recovery_flag`
- `chemical.demand.fact_program_coverage`: `customer_id`, `covered_customer_count`, `targeted_customer_count`, `fiscal_quarter_id`, `program_id`, `cohort_id`, `coverage_rate`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q4 2025 (9)

For Ecolab, does the 2025 tariff surcharge create a larger price contribution in the first half of 2026 than in the second half?

- `chemical.price.fact_realized_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `customer_id`, `country_id`, `realized_change_rate`
- `chemical.price.fact_announced_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `announced_change_rate`, `in_guide_flag`, `added_after_flag`
- `chemical.price.fact_surcharge_realization`: `surcharge_id`, `half_code`, `fiscal_quarter_id`, `customer_id`, `business_segment_id`, `realized_rate`, `approached_customer_rate`
- `chemical.price.dim_surcharge`: `surcharge_name`, `surcharge_code`
- `chemical.price.fact_price_guide`: `price_action_id`, `guided_price_change_rate`, `net_price_tailwind_rate`, `half_code`, `fiscal_quarter_id`, `business_segment_id`, `macro_case_id`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (3)

For Ecolab, excluding the tariff surcharge, is underlying price getting easier because the value case is clearer, or harder because of price fatigue?

- `chemical.price.fact_realized_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `customer_id`, `country_id`, `realized_change_rate`
- `chemical.price.fact_announced_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `announced_change_rate`, `in_guide_flag`, `added_after_flag`
- `chemical.price.fact_surcharge_realization`: `surcharge_id`, `fiscal_quarter_id`, `customer_id`, `business_segment_id`, `realized_rate`, `approached_customer_rate`, `competitor_support_flag`
- `chemical.price.dim_surcharge`: `surcharge_name`, `surcharge_code`
- `chemical.price.fact_value_capture`: `value_metric_id`, `fatigue_flag`, `value_case_clear_flag`, `fiscal_quarter_id`, `business_segment_id`, `program_id`, `captured_rate`
- `chemical.price.dim_value_metric`: `metric_name`, `metric_code`

### Q3 2025 (8)

For Ecolab, how much of the price surcharge was realized, and does roughly 3% pricing persist for the next few quarters?

- `chemical.price.fact_surcharge_realization`: `fiscal_quarter_id`, `surcharge_id`, `realized_rate`, `customer_id`, `business_segment_id`, `approached_customer_rate`, `competitor_support_flag`
- `chemical.price.dim_surcharge`: `surcharge_name`, `surcharge_code`
- `chemical.price.fact_realized_price`: `fiscal_quarter_id`, `price_action_id`, `realized_change_rate`, `business_segment_id`, `end_market_id`, `customer_id`, `country_id`
- `chemical.price.fact_announced_price`: `fiscal_quarter_id`, `price_action_id`, `business_segment_id`, `end_market_id`, `announced_change_rate`, `in_guide_flag`, `added_after_flag`
- `chemical.price.fact_price_guide`: `fiscal_quarter_id`, `price_action_id`, `guided_price_change_rate`, `net_price_tailwind_rate`, `business_segment_id`, `macro_case_id`, `january_only_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (13)

For Ecolab, can low-to-mid-teens earnings growth still be reached with little volume growth, as in the prior price-led case?

- `chemical.price.fact_earnings_bridge`: `earnings_change_rate`, `price_led_flag`, `low_to_mid_teens_reachable_flag`, `fiscal_quarter_id`, `business_segment_id`, `margin_driver_id`, `offset_amount`
- `chemical.price.fact_acquisition_margin`: `uses_original_case_flag`, `fiscal_quarter_id`, `acquisition_id`, `business_segment_id`, `drag_rate`, `excluded_margin_rate`, `dilution_rate`
- `chemical.demand.fact_end_market_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `demand_driver_id`
- `chemical.demand.fact_segment_volume`: `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `sales_change_rate`
- `chemical.price.fact_realized_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `customer_id`, `country_id`, `realized_change_rate`
- `chemical.price.fact_announced_price`: `price_action_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `announced_change_rate`, `in_guide_flag`, `added_after_flag`

### Q2 2025 (2)

For Ecolab, why did pricing land near 2% rather than a higher rate, and what pricing is expected in the second half?

- `chemical.price.fact_realized_price`: `realized_change_rate`, `versus_announced_rate`, `run_rate_flag`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `customer_id`
- `chemical.price.fact_announced_price`: `announced_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `price_action_id`, `in_guide_flag`, `added_after_flag`
- `chemical.demand.fact_end_market_volume`: `volume_quantity`, `volume_change_rate`, `run_rate_quantity`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`
- `chemical.demand.fact_segment_volume`: `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `country_id`
- `chemical.price.fact_price_guide`: `guided_price_change_rate`, `net_price_tailwind_rate`, `half_code`, `fiscal_quarter_id`, `business_segment_id`, `price_action_id`, `macro_case_id`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (5)

For Ecolab, is about half of the announced U.S. surcharge still expected to be realized, and are competitors supporting it?

- `chemical.price.fact_surcharge_realization`: `surcharge_id`, `realized_rate`, `competitor_support_flag`, `half_code`, `fiscal_quarter_id`, `customer_id`, `business_segment_id`
- `chemical.price.dim_surcharge`: `surcharge_name`, `surcharge_code`
- `chemical.price.fact_competitor_price`: `competitor_id`, `competitor_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `can_match_flag`, `price_part_of_share_flag`
- `chemical.customer.dim_competitor`: `competitor_name`, `competitor_code`
- `chemical.demand.fact_share_position`: `competitor_id`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `subsegment_id`, `country_id`, `share_rate`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (7)

For Ecolab, does confidence in the operating-margin target hold if volume stays near 1% inside roughly 3% organic growth?

- `chemical.price.fact_segment_margin`: `margin_driver_id`, `operating_margin_rate`, `margin_change_rate`, `target_rate`, `fiscal_quarter_id`, `business_segment_id`, `quarter_dip_flag`
- `chemical.price.fact_margin_target`: `current_margin_rate`, `target_margin_rate`, `fiscal_quarter_id`, `business_segment_id`, `gap_rate`, `holds_in_low_demand_flag`, `straight_line_flag`
- `chemical.demand.fact_end_market_volume`: `volume_quantity`, `volume_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `end_market_id`, `country_id`, `demand_driver_id`
- `chemical.demand.fact_segment_volume`: `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `sales_change_rate`
- `chemical.demand.fact_organic_growth`: `organic_growth_rate`, `volume_contributed_flag`, `fiscal_quarter_id`, `business_segment_id`, `program_id`, `country_id`, `price_contributed_flag`
- `chemical.demand.fact_cross_sell`: `fiscal_quarter_id`, `program_id`, `business_segment_id`, `customer_id`, `cross_sell_quantity`, `contribution_rate`, `with_core_flag`
