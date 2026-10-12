# Chemical Inc supply and capacity

Supply and capacity owns plants, stores, acquisitions, growth spend, operating rates, and raw-material cost for Chemical Inc. Agreed input cost and spot input cost are supply facts. They are not the selling-price file and they do not store demand quantity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `country_identity` | `country_id` | `sf:chemical.geography.dim_country` `country_id` |
| `channel_identity` | `channel_id` | `sf:chemical.customer.dim_channel` `channel_id` |
| `business_segment_identity` | `business_segment_id` | `sf:chemical.market.dim_business_segment` `business_segment_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:chemical.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `end_market_identity` | `end_market_id` | `sf:chemical.market.dim_end_market` `end_market_id` |
| `order_pattern_identity` | `order_pattern_id` | `sf:chemical.customer.dim_order_pattern` `order_pattern_id` |
| `labor_factor_identity` | `labor_factor_id` | `sf:chemical.price.dim_labor_factor` `labor_factor_id` |
| `program_identity` | `program_id` | `sf:chemical.program.dim_program` `program_id` |
| `competitor_identity` | `competitor_id` | `sf:chemical.customer.dim_competitor` `competitor_id` |

## Numbered questions

## Sherwin-Williams

### Q1 2026 (2)

For Sherwin-Williams, which inputs pushed the raw-material outlook from low-single-digit to low-to-mid-single-digit, and have VAM and propylene peaked versus spot?

- `chemical.supply.fact_input_cost`: `raw_input_id`, `outlook_band_code`, `fiscal_quarter_id`, `cost_basket_id`, `supplier_id`, `contract_cost_amount`, `inflation_rate`
- `chemical.supply.fact_spot_cost`: `raw_input_id`, `spot_cost_amount`, `peaked_flag`, `fiscal_quarter_id`, `above_contract_flag`
- `chemical.supply.dim_raw_input`: `input_name`, `input_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q1 2026 (10)

For Sherwin-Williams, why is the raw-material exit rate only low-to-mid single digits when outside estimates are much higher?

- `chemical.supply.fact_input_cost`: `inflation_rate`, `above_outside_estimate_flag`, `fiscal_quarter_id`, `raw_input_id`, `cost_basket_id`, `supplier_id`, `contract_cost_amount`
- `chemical.supply.fact_spot_cost`: `fiscal_quarter_id`, `raw_input_id`, `spot_cost_amount`, `peaked_flag`, `above_contract_flag`
- `chemical.geography.dim_country`: `region_id`, `country_name`, `country_code`
- `chemical.supply.dim_raw_input`: `input_name`, `input_code`
- `chemical.supply.dim_cost_basket`: `basket_name`, `basket_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (3)

For Sherwin-Williams, how is the return on growth investment judged across share gains, new stores, and time to steady-state profit?

- `chemical.supply.fact_growth_spend`: `growth_program_id`, `spend_amount`, `share_of_spend_rate`, `fiscal_quarter_id`, `business_segment_id`, `allocation_changed_flag`, `payback_months`
- `chemical.network.dim_growth_program`: `business_segment_id`, `program_name`, `program_code`
- `chemical.supply.fact_store_network`: `store_id`, `net_store_count`, `sales_point_from_new_stores`, `months_to_steady_state`, `fiscal_quarter_id`, `country_id`, `opening_count`
- `chemical.demand.fact_share_position`: `end_market_id`, `share_rate`, `share_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `subsegment_id`, `country_id`
- `chemical.demand.fact_industry_volume`: `end_market_id`, `fiscal_quarter_id`, `subsegment_id`, `country_id`, `industry_volume_quantity`, `industry_change_rate`, `company_versus_industry_rate`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (4)

For Sherwin-Williams, what integration actions are planned at Suvenil?

- `chemical.supply.fact_integration`: `action_name`, `fiscal_quarter_id`, `acquisition_id`, `business_segment_id`, `started_flag`, `versus_base_flag`
- `chemical.network.dim_acquisition`: `business_segment_id`, `acquisition_name`, `acquisition_code`
- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.price.fact_acquisition_margin`: `fiscal_quarter_id`, `acquisition_id`, `business_segment_id`, `drag_rate`, `excluded_margin_rate`, `dilution_rate`, `uses_original_case_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (3)

For Sherwin-Williams, is added SG&A mainly headcount, or does it imply a higher store-count target?

- `chemical.supply.fact_sga`: `mostly_headcount_flag`, `fiscal_quarter_id`, `business_segment_id`, `spend_amount`, `leverage_flag`, `step_up_flag`
- `chemical.price.fact_margin_target`: `target_margin_rate`, `fiscal_quarter_id`, `business_segment_id`, `current_margin_rate`, `gap_rate`, `holds_in_low_demand_flag`, `straight_line_flag`
- `chemical.supply.fact_headcount`: `headcount_role_id`, `headcount_quantity`, `fiscal_quarter_id`, `business_segment_id`, `addition_quantity`, `implies_more_stores_flag`
- `chemical.network.dim_headcount_role`: `role_name`, `role_code`
- `chemical.supply.fact_store_network`: `store_id`, `opening_count`, `closure_count`, `net_store_count`, `fiscal_quarter_id`, `country_id`, `sales_point_from_new_stores`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (4)

For Sherwin-Williams, has competitor disruption changed how growth spend is split between Paint Stores and Consumer Brands?

- `chemical.supply.fact_growth_spend`: `growth_program_id`, `spend_amount`, `share_of_spend_rate`, `allocation_changed_flag`, `fiscal_quarter_id`, `business_segment_id`, `payback_months`
- `chemical.network.dim_growth_program`: `business_segment_id`, `program_name`, `program_code`
- `chemical.demand.fact_segment_volume`: `volume_change_rate`, `sales_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `organic_volume_quantity`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.supply.fact_store_network`: `store_id`, `net_store_count`, `sales_point_from_new_stores`, `fiscal_quarter_id`, `country_id`, `opening_count`, `closure_count`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (10)

For Sherwin-Williams, where do the doubled restructuring savings come from, and do they accelerate in the back half?

- `chemical.supply.fact_restructuring_savings`: `cost_action_id`, `savings_amount`, `doubled_flag`, `fiscal_quarter_id`, `business_segment_id`, `accelerates_flag`, `source_code`
- `chemical.network.dim_cost_action`: `action_name`, `action_code`
- `chemical.supply.fact_input_cost`: `cost_basket_id`, `contract_cost_amount`, `inflation_rate`, `half_code`, `fiscal_quarter_id`, `raw_input_id`, `supplier_id`
- `chemical.supply.fact_delivered_cost`: `delivered_cost_amount`, `cost_change_rate`, `second_half_direction_code`, `fiscal_quarter_id`, `raw_input_id`, `business_segment_id`, `tariff_component_amount`
- `chemical.supply.fact_manufacturing_cost`: `cost_amount`, `fiscal_quarter_id`, `labor_factor_id`, `plant_id`, `business_segment_id`, `in_guide_flag`, `labor_component_amount`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (11)

For Sherwin-Williams, with volumes below plan, is the margin pain from lower operating rates split evenly between manufacturing and Paint Stores?

- `chemical.supply.fact_operating_rate`: `operating_rate`, `below_plan_flag`, `manufacturing_share_of_pain_rate`, `stores_share_of_pain_rate`, `fiscal_quarter_id`, `plant_id`, `business_segment_id`
- `chemical.network.dim_plant`: `country_id`, `plant_name`, `plant_code`
- `chemical.supply.fact_manufacturing_cost`: `fiscal_quarter_id`, `labor_factor_id`, `plant_id`, `business_segment_id`, `cost_amount`, `in_guide_flag`, `labor_component_amount`
- `chemical.demand.fact_segment_volume`: `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`, `fiscal_quarter_id`, `business_segment_id`, `country_id`
- `chemical.market.dim_business_segment`: `segment_name`, `segment_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (12)

For Sherwin-Williams, which raw-material baskets drive expected second-half deflation?

- `chemical.supply.fact_input_cost`: `cost_basket_id`, `half_code`, `fiscal_quarter_id`, `raw_input_id`, `supplier_id`, `contract_cost_amount`, `inflation_rate`
- `chemical.supply.fact_spot_cost`: `fiscal_quarter_id`, `raw_input_id`, `spot_cost_amount`, `peaked_flag`, `above_contract_flag`
- `chemical.supply.dim_raw_input`: `input_name`, `input_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (14)

For Sherwin-Williams, what supply-chain inefficiencies became a larger headwind in the quarter?

- `chemical.supply.fact_supply_disruption`: `fiscal_quarter_id`, `supply_issue_id`, `headwind_amount`, `larger_than_prior_flag`, `business_segment_id`, `inefficiency_flag`
- `chemical.network.dim_supply_issue`: `issue_name`, `issue_code`
- `chemical.supply.fact_input_cost`: `fiscal_quarter_id`, `cost_basket_id`, `contract_cost_amount`, `raw_input_id`, `supplier_id`, `inflation_rate`, `outlook_band_code`
- `chemical.supply.fact_delivered_cost`: `fiscal_quarter_id`, `delivered_cost_amount`, `cost_change_rate`, `raw_input_id`, `business_segment_id`, `tariff_component_amount`, `second_half_direction_code`
- `chemical.supply.fact_manufacturing_cost`: `fiscal_quarter_id`, `cost_amount`, `labor_factor_id`, `plant_id`, `business_segment_id`, `in_guide_flag`, `labor_component_amount`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

## Ecolab

### Q1 2026 (16)

For Ecolab, why is raw inflation described as high-single-digit in the second quarter without a further increase later in the year?

- `chemical.supply.fact_input_cost`: `fiscal_quarter_id`, `cost_basket_id`, `contract_cost_amount`, `inflation_rate`, `raw_input_id`, `supplier_id`, `outlook_band_code`
- `chemical.supply.fact_spot_cost`: `fiscal_quarter_id`, `spot_cost_amount`, `raw_input_id`, `peaked_flag`, `above_contract_flag`
- `chemical.price.fact_price_cost_gap`: `fiscal_quarter_id`, `cost_ahead_flag`, `second_quarter_only_flag`, `business_segment_id`, `raw_input_id`, `spread_rate`
- `chemical.supply.dim_raw_input`: `input_name`, `input_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q3 2025 (14)

For Ecolab, is the company equipped for direct-to-chip cooling, or are more bolt-on deals required?

- `chemical.supply.fact_capability`: `equipped_flag`, `bolt_on_required_flag`, `fiscal_quarter_id`, `product_platform_id`, `program_id`, `competitor_emphasizes_chemistry_flag`
- `chemical.demand.fact_platform_volume`: `fiscal_quarter_id`, `program_id`, `business_segment_id`, `volume_quantity`, `growth_rate`, `above_thirty_percent_flag`, `dilution_uses_current_rate_flag`
- `chemical.market.dim_end_market`: `business_segment_id`, `end_market_name`, `end_market_code`
- `chemical.network.dim_acquisition`: `business_segment_id`, `acquisition_name`, `acquisition_code`
- `chemical.supply.fact_integration`: `fiscal_quarter_id`, `acquisition_id`, `business_segment_id`, `action_name`, `started_flag`, `versus_base_flag`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (4)

For Ecolab, how is delivered product cost trending into the second half given tariffs and mixed raw materials?

- `chemical.supply.fact_delivered_cost`: `delivered_cost_amount`, `cost_change_rate`, `tariff_component_amount`, `second_half_direction_code`, `fiscal_quarter_id`, `raw_input_id`, `business_segment_id`
- `chemical.supply.fact_input_cost`: `cost_basket_id`, `contract_cost_amount`, `half_code`, `fiscal_quarter_id`, `raw_input_id`, `supplier_id`, `inflation_rate`
- `chemical.price.fact_surcharge_realization`: `half_code`, `fiscal_quarter_id`, `surcharge_id`, `customer_id`, `business_segment_id`, `realized_rate`, `approached_customer_rate`
- `chemical.supply.fact_spot_cost`: `spot_cost_amount`, `fiscal_quarter_id`, `raw_input_id`, `peaked_flag`, `above_contract_flag`
- `chemical.supply.dim_raw_input`: `input_name`, `input_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`

### Q2 2025 (10)

For Ecolab, do returns and paybacks on the three priority growth areas differ from traditional institutional investments?

- `chemical.supply.fact_investment_return`: `growth_program_id`, `payback_months`, `return_rate`, `differs_from_historical_flag`, `fiscal_quarter_id`, `business_segment_id`
- `chemical.supply.fact_growth_spend`: `growth_program_id`, `payback_months`, `fiscal_quarter_id`, `business_segment_id`, `spend_amount`, `share_of_spend_rate`, `allocation_changed_flag`
- `chemical.demand.fact_segment_volume`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `volume_quantity`, `volume_change_rate`, `organic_volume_quantity`, `sales_change_rate`
- `chemical.demand.fact_customer_traffic`: `fiscal_quarter_id`, `business_segment_id`, `country_id`, `traffic_index`, `weak_traffic_flag`, `visit_quantity`
- `chemical.network.dim_growth_program`: `business_segment_id`, `program_name`, `program_code`
- `chemical.time.dim_fiscal_quarter`: `quarter_label`, `quarter_code`, `guidance_horizon`
