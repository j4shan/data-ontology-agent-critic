# Energy Inc price, cost, and margin

This slice is part of the Energy Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity row does not store a price. A price row does not store the unit quantity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `dim_country_identity` | `country_id` | `energy.geography.dim_country` `country_id` |
| `dim_fiscal_quarter_identity` | `fiscal_quarter_id` | `energy.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `dim_market_identity` | `market_id` | `energy.geography.dim_market` `market_id` |
| `dim_facility_identity` | `facility_id` | `energy.resource.dim_facility` `facility_id` |
| `dim_product_identity` | `product_id` | `energy.customer.dim_product` `product_id` |
| `dim_project_identity` | `project_id` | `energy.resource.dim_project` `project_id` |
| `dim_play_identity` | `play_id` | `energy.resource.dim_play` `play_id` |
| `dim_contract_identity` | `contract_id` | `energy.customer.dim_contract` `contract_id` |
| `dim_technology_identity` | `technology_id` | `energy.resource.dim_technology` `technology_id` |
| `dim_field_identity` | `field_id` | `energy.resource.dim_field` `field_id` |
| `dim_customer_identity` | `customer_id` | `energy.customer.dim_customer` `customer_id` |

## Numbered questions

### Q2 2026 (4) — Chevron

For Chevron, how does Iraq compete for capital on cost of supply and above-ground risk?

- `energy.price.fact_above_ground`: `risk_score`, `competes_flag`, `fiscal_quarter_id`, `country_id`, `hurdle_id`
- `energy.price.fact_cost_of_supply`: `cost_amount`, `rank_code`, `fiscal_quarter_id`, `country_id`, `capital_item_id`
- `energy.price.fact_allocation`: `allocated_amount`, `decision_status_code`, `more_capital_flag`, `fiscal_quarter_id`, `capital_item_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.price.dim_hurdle`: `hurdle_id`, `hurdle_code`, `hurdle_name`
- `energy.price.dim_capital_item`: `capital_item_id`, `item_code`, `item_name`

### Q2 2026 (5) — Chevron

For Chevron, where are the cost savings ahead of schedule, and what was surprising in the efficiency portion?

- `energy.price.fact_cost_savings`: `savings_amount`, `ahead_of_plan_flag`, `efficiency_portion_amount`, `fiscal_quarter_id`, `cost_bucket_id`
- `energy.price.fact_opex_efficiency`: `efficiency_amount`, `surprising_flag`, `fiscal_quarter_id`, `cost_bucket_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`

### Q2 2026 (9) — Chevron

For Chevron, why license the surfactant technology instead of keeping it inside the company?

- `energy.price.fact_license_income`: `license_income_amount`, `kept_exclusive_flag`, `fiscal_quarter_id`, `technology_id`
- `energy.supply.fact_shale_position`: `core_flag`, `learnings_applied_flag`, `paused_growth_flag`, `fiscal_quarter_id`, `play_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`

### Q2 2026 (10) — Chevron

For Chevron, what sets the long-term capital-spending range as Permian spend falls on efficiency but power spending is added?

- `energy.price.fact_permian_capital`: `permian_spend_amount`, `power_spend_amount`, `range_driver_code`, `fiscal_quarter_id`, `capital_item_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.price.dim_capital_item`: `capital_item_id`, `item_code`, `item_name`

### Q2 2026 (11) — Chevron

For Chevron, after the disruption, is there evidence of demand destruction, and where do refining cracks go?

- `energy.price.fact_crack`: `crack_amount`, `direction_code`, `fiscal_quarter_id`, `market_id`, `marker_id`
- `energy.demand.fact_product_demand`: `demand_quantity`, `destruction_flag`, `shortage_flag`, `fiscal_quarter_id`, `product_id`, `market_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.geography.dim_market`: `market_id`, `market_code`, `market_name`, `region_id`
- `energy.price.dim_marker`: `marker_id`, `marker_code`, `marker_name`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`

### Q2 2026 (13) — Chevron

For Chevron, when receivables are repaid, do Venezuela terms shift to the new fiscal framework?

- `energy.supply.fact_venezuela_asset`: `condition_code`, `resource_quantity`, `fiscal_quarter_id`, `country_id`, `asset_id`
- `energy.price.fact_fiscal_terms`: `terms_changed_flag`, `recycle_only_flag`, `forward_only_flag`, `fiscal_quarter_id`, `fiscal_regime_id`, `country_id`
- `energy.price.fact_receivable`: `receivable_amount`, `repaid_flag`, `shifts_framework_flag`, `fiscal_quarter_id`, `fiscal_regime_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_asset`: `asset_id`, `asset_code`, `asset_name`, `country_id`, `play_id`
- `energy.price.dim_fiscal_regime`: `fiscal_regime_id`, `regime_code`, `regime_name`, `country_id`

### Q1 2026 (3) — Chevron

For Chevron, how close are the power contracts with the technology customer to a decision?

- `energy.price.fact_power_return`: `return_rate`, `decision_close_flag`, `fiscal_quarter_id`, `project_id`, `contract_id`
- `energy.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `energy.price.fact_allocation`: `allocated_amount`, `decision_status_code`, `more_capital_flag`, `fiscal_quarter_id`, `capital_item_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_project`: `project_id`, `project_code`, `project_name`, `country_id`, `asset_id`
- `energy.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `product_id`
- `energy.price.dim_capital_item`: `capital_item_id`, `item_code`, `item_name`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`

### Q1 2026 (4) — Chevron

For Chevron, how should recovery of historical Venezuela receivables be weighed against looking only forward?

- `energy.price.fact_receivable`: `receivable_amount`, `repaid_flag`, `shifts_framework_flag`, `fiscal_quarter_id`, `fiscal_regime_id`, `country_id`
- `energy.price.fact_fiscal_terms`: `terms_changed_flag`, `recycle_only_flag`, `forward_only_flag`, `fiscal_quarter_id`, `fiscal_regime_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.price.dim_fiscal_regime`: `fiscal_regime_id`, `regime_code`, `regime_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`

### Q1 2026 (5) — Chevron

For Chevron, where could local product shortages hit, given exposure beyond the regulated refining system?

- `energy.price.fact_refining_margin`: `margin_amount`, `captured_amount`, `quarter_shown_flag`, `fiscal_quarter_id`, `facility_id`, `marker_id`
- `energy.supply.fact_refinery_capacity`: `throughput_quantity`, `can_run_heavy_flag`, `operating_change_flag`, `fiscal_quarter_id`, `facility_id`, `market_id`
- `energy.demand.fact_product_demand`: `demand_quantity`, `destruction_flag`, `shortage_flag`, `fiscal_quarter_id`, `product_id`, `market_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.price.dim_marker`: `marker_id`, `marker_code`, `marker_name`
- `energy.geography.dim_market`: `market_id`, `market_code`, `market_name`, `region_id`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`

### Q1 2026 (9) — Chevron

For Chevron, have lower Bakken costs made it more clearly core, and has buyer interest risen with the oil price?

- `energy.supply.fact_shale_position`: `core_flag`, `learnings_applied_flag`, `paused_growth_flag`, `fiscal_quarter_id`, `play_id`, `country_id`
- `energy.price.fact_operating_cost`: `cost_amount`, `lower_flag`, `clearly_core_flag`, `fiscal_quarter_id`, `play_id`, `cost_bucket_id`
- `energy.price.fact_portfolio_earnings`: `upstream_share_rate`, `downstream_share_rate`, `chemicals_share_rate`, `heavier_acceptable_flag`, `fiscal_quarter_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`

### Q1 2026 (11) — Chevron

For Chevron, which government policies help or hurt during a supply shock?

- `energy.price.fact_refining_margin`: `margin_amount`, `captured_amount`, `quarter_shown_flag`, `fiscal_quarter_id`, `facility_id`, `marker_id`
- `energy.supply.fact_refinery_capacity`: `throughput_quantity`, `can_run_heavy_flag`, `operating_change_flag`, `fiscal_quarter_id`, `facility_id`, `market_id`
- `energy.price.fact_regulation`: `help_amount`, `hurt_amount`, `fiscal_quarter_id`, `market_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.price.dim_marker`: `marker_id`, `marker_code`, `marker_name`
- `energy.geography.dim_market`: `market_id`, `market_code`, `market_name`, `region_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`

### Q4 2025 (4) — Chevron

For Chevron, how much of the remaining cost reduction depends on the organizational changes now a few months old?

- `energy.price.fact_cost_reduction`: `remaining_amount`, `depends_on_organization_flag`, `fiscal_quarter_id`, `cost_bucket_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`

### Q4 2025 (11) — Chevron

For Chevron, what operating or strategic benefits would come from owning more of the chemicals joint venture than the current structure allows?

- `energy.price.fact_jv_economics`: `ownership_constrained_flag`, `strategic_benefit_code`, `fiscal_quarter_id`, `facility_id`
- `energy.supply.fact_base_production`: `base_quantity`, `managed_differently_flag`, `repeatable_flag`, `fiscal_quarter_id`, `play_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`

### Q3 2025 (7) — Chevron

For Chevron, is the beat in affiliate distributions mostly Tengiz?

- `energy.price.fact_affiliate_cash`: `distribution_amount`, `beat_amount`, `mostly_field_flag`, `fiscal_quarter_id`, `field_id`
- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`

### Q1 2026 (1) — Exxon Mobil

For Exxon Mobil, how did April refining margins follow the strong March, and what can the downstream do to balance that market this year?

- `energy.price.fact_refining_margin`: `margin_amount`, `captured_amount`, `quarter_shown_flag`, `fiscal_quarter_id`, `facility_id`, `marker_id`
- `energy.supply.fact_refinery_capacity`: `throughput_quantity`, `can_run_heavy_flag`, `operating_change_flag`, `fiscal_quarter_id`, `facility_id`, `market_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.price.dim_marker`: `marker_id`, `marker_code`, `marker_name`
- `energy.geography.dim_market`: `market_id`, `market_code`, `market_name`, `region_id`

### Q1 2026 (7) — Exxon Mobil

For Exxon Mobil, which parts of the business reverse the short-term timing effects, given the long-term targets span many moving pieces?

- `energy.price.fact_timing_effect`: `timing_amount`, `reverses_flag`, `segment_code`, `fiscal_quarter_id`
- `energy.supply.fact_portfolio_volume`: `upstream_quantity`, `other_quantity`, `fiscal_quarter_id`, `product_id`
- `energy.price.fact_portfolio_earnings`: `upstream_share_rate`, `downstream_share_rate`, `chemicals_share_rate`, `heavier_acceptable_flag`, `fiscal_quarter_id`
- `energy.supply.fact_uncommitted_lng`: `uncommitted_quantity`, `available_for_arbitrage_flag`, `fiscal_quarter_id`, `facility_id`, `train_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.resource.dim_train`: `train_id`, `train_code`, `train_name`, `facility_id`

### Q4 2025 (5) — Exxon Mobil

For Exxon Mobil, how do Papua New Guinea and Mozambique LNG sit on the cost curve versus Gulf Coast LNG, ahead of investment decisions?

- `energy.price.fact_lng_cost`: `cost_amount`, `versus_gulf_amount`, `advantaged_flag`, `fiscal_quarter_id`, `project_id`, `marker_id`
- `energy.supply.fact_security`: `security_status_code`, `early_decision_likely_flag`, `fiscal_quarter_id`, `project_id`, `country_id`
- `energy.price.fact_cost_of_supply`: `cost_amount`, `rank_code`, `fiscal_quarter_id`, `country_id`, `capital_item_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_project`: `project_id`, `project_code`, `project_name`, `country_id`, `asset_id`
- `energy.price.dim_marker`: `marker_id`, `marker_code`, `marker_name`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.price.dim_capital_item`: `capital_item_id`, `item_code`, `item_name`

### Q4 2025 (6) — Exxon Mobil

For Exxon Mobil, how do carbon-capture and battery contributions relate to the lithium business?

- `energy.price.fact_capture_commercial`: `commercial_stage_code`, `challenge_code`, `customer_interest_flag`, `fiscal_quarter_id`, `customer_id`, `contract_id`
- `energy.price.fact_battery_value`: `contribution_amount`, `linked_to_lithium_flag`, `fiscal_quarter_id`, `product_id`
- `energy.price.fact_lithium_price`: `price_amount`, `linked_to_earnings_flag`, `fiscal_quarter_id`, `marker_id`, `product_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `energy.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `product_id`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`
- `energy.price.dim_marker`: `marker_id`, `marker_code`, `marker_name`

### Q4 2025 (7) — Exxon Mobil

For Exxon Mobil, is data-center interest in carbon capture as an emissions offset real, and can it be material?

- `energy.price.fact_capture_commercial`: `commercial_stage_code`, `challenge_code`, `customer_interest_flag`, `fiscal_quarter_id`, `customer_id`, `contract_id`
- `energy.demand.fact_data_center_demand`: `interest_quantity`, `material_flag`, `ordinary_gas_alternative_flag`, `fiscal_quarter_id`, `customer_id`, `product_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `energy.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `product_id`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`

### Q3 2025 (1) — Exxon Mobil

For Exxon Mobil, is capital spending below the range this year mostly captured deflation?

- `energy.price.fact_capital_spend`: `spend_amount`, `below_range_flag`, `in_range_flag`, `fiscal_quarter_id`, `capital_item_id`
- `energy.price.fact_deflation`: `deflation_amount`, `explains_underspend_flag`, `fiscal_quarter_id`, `cost_bucket_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.price.dim_capital_item`: `capital_item_id`, `item_code`, `item_name`
- `energy.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`

### Q3 2025 (5) — Exxon Mobil

For Exxon Mobil, do capital efficiency and the balance sheet support a step-up in acquisitions?

- `energy.price.fact_capital_efficiency`: `capital_per_unit_amount`, `improving_flag`, `fiscal_quarter_id`, `play_id`, `capital_item_id`
- `energy.price.fact_acquisition`: `step_up_supported_flag`, `organic_need_amount`, `fiscal_quarter_id`, `capital_item_id`, `hurdle_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.price.dim_capital_item`: `capital_item_id`, `item_code`, `item_name`
- `energy.price.dim_hurdle`: `hurdle_id`, `hurdle_code`, `hurdle_name`

### Q4 2024 (5) — Exxon Mobil

For Exxon Mobil, is capital spending the main risk to the return target, given the projects organization?

- `energy.price.fact_capital_spend`: `spend_amount`, `below_range_flag`, `in_range_flag`, `fiscal_quarter_id`, `capital_item_id`
- `energy.price.fact_return_target`: `return_rate`, `spending_is_main_risk_flag`, `fiscal_quarter_id`, `hurdle_id`, `capital_item_id`
- `energy.supply.fact_project_load`: `active_project_count`, `can_add_more_flag`, `fiscal_quarter_id`, `project_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.price.dim_capital_item`: `capital_item_id`, `item_code`, `item_name`
- `energy.price.dim_hurdle`: `hurdle_id`, `hurdle_code`, `hurdle_name`
- `energy.resource.dim_project`: `project_id`, `project_code`, `project_name`, `country_id`, `asset_id`

### Q4 2024 (7) — Exxon Mobil

For Exxon Mobil, what returns, certainty, and local conditions are required to move Papua New Guinea and Mozambique LNG forward?

- `energy.price.fact_lng_cost`: `cost_amount`, `versus_gulf_amount`, `advantaged_flag`, `fiscal_quarter_id`, `project_id`, `marker_id`
- `energy.supply.fact_security`: `security_status_code`, `early_decision_likely_flag`, `fiscal_quarter_id`, `project_id`, `country_id`
- `energy.price.fact_allocation`: `allocated_amount`, `decision_status_code`, `more_capital_flag`, `fiscal_quarter_id`, `capital_item_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_project`: `project_id`, `project_code`, `project_name`, `country_id`, `asset_id`
- `energy.price.dim_marker`: `marker_id`, `marker_code`, `marker_name`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.price.dim_capital_item`: `capital_item_id`, `item_code`, `item_name`

### Q4 2024 (8) — Exxon Mobil

For Exxon Mobil, what commodity and margin levels are assumed in the cash-flow growth plan tied to higher U.S. production?

- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.price.fact_cash_flow`: `cash_flow_amount`, `plan_amount`, `fiscal_quarter_id`, `marker_id`
- `energy.price.fact_oil_price`: `price_amount`, `higher_flag`, `fiscal_quarter_id`, `marker_id`, `play_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.price.dim_marker`: `marker_id`, `marker_code`, `marker_name`

### Q4 2024 (10) — Exxon Mobil

For Exxon Mobil, how has the commercial side of carbon capture evolved, and what challenges remain?

- `energy.price.fact_capture_commercial`: `commercial_stage_code`, `challenge_code`, `customer_interest_flag`, `fiscal_quarter_id`, `customer_id`, `contract_id`
- `energy.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `product_id`

### Q4 2024 (11) — Exxon Mobil

For Exxon Mobil, are there regional or product green shoots in chemicals, and do new complexes change the margin position?

- `energy.price.fact_chemical_margin`: `margin_amount`, `versus_average_amount`, `green_shoot_flag`, `fiscal_quarter_id`, `facility_id`, `product_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`
