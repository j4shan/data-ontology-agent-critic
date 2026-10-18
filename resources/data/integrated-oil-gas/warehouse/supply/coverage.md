# Energy Inc supply and capacity

This slice is part of the Energy Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity row does not store a price. A price row does not store the unit quantity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `dim_country_identity` | `country_id` | `energy.geography.dim_country` `country_id` |
| `dim_market_identity` | `market_id` | `energy.geography.dim_market` `market_id` |
| `dim_fiscal_quarter_identity` | `fiscal_quarter_id` | `energy.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `dim_contract_identity` | `contract_id` | `energy.customer.dim_contract` `contract_id` |
| `dim_customer_identity` | `customer_id` | `energy.customer.dim_customer` `customer_id` |
| `dim_product_identity` | `product_id` | `energy.customer.dim_product` `product_id` |

## Numbered questions

### Q2 2026 (1) — Chevron

For Chevron, what drove the sequential production increase at Tengiz, one of the main volume drivers?

- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.supply.fact_affiliate_volume`: `affiliate_quantity`, `mostly_field_flag`, `fiscal_quarter_id`, `field_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`

### Q2 2026 (2) — Chevron

For Chevron, how large can power be in the mix beyond the first project, and what returns come with later projects?

- `energy.supply.fact_power_capacity`: `capacity_quantity`, `later_project_flag`, `fiscal_quarter_id`, `project_id`, `facility_id`
- `energy.price.fact_portfolio_earnings`: `upstream_share_rate`, `downstream_share_rate`, `chemicals_share_rate`, `heavier_acceptable_flag`, `fiscal_quarter_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_project`: `project_id`, `project_code`, `project_name`, `country_id`, `asset_id`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`

### Q2 2026 (3) — Chevron

For Chevron, with Guyana turning to cash and other portfolio additions, does the Permian growth pause get revisited?

- `energy.supply.fact_shale_position`: `core_flag`, `learnings_applied_flag`, `paused_growth_flag`, `fiscal_quarter_id`, `play_id`, `country_id`
- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.price.fact_free_cash`: `free_cash_amount`, `supports_revisit_flag`, `fiscal_quarter_id`, `play_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`

### Q2 2026 (6) — Chevron

For Chevron, if the export pipeline is closed for a long time, how much of the liquids can move on alternative routes?

- `energy.resource.dim_pipeline`: `pipeline_id`, `pipeline_code`, `pipeline_name`, `country_id`
- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.supply.fact_route_capacity`: `alternate_quantity`, `long_outage_flag`, `fiscal_quarter_id`, `pipeline_id`, `field_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`

### Q2 2026 (7) — Chevron

For Chevron, where do exploration campaigns in Libya, Namibia, and Greece stand?

- `energy.supply.fact_exploration`: `campaign_status_code`, `well_result_code`, `industry_push_flag`, `fiscal_quarter_id`, `country_id`, `play_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`

### Q2 2026 (8) — Chevron

For Chevron, what uncommitted LNG is available to respond to a tight European gas market as Australian plants ramp in the second half?

- `energy.supply.fact_uncommitted_lng`: `uncommitted_quantity`, `available_for_arbitrage_flag`, `fiscal_quarter_id`, `facility_id`, `train_id`
- `energy.demand.fact_lng_demand`: `call_quantity`, `tight_market_flag`, `fiscal_quarter_id`, `market_id`, `product_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.resource.dim_train`: `train_id`, `train_code`, `train_name`, `facility_id`
- `energy.geography.dim_market`: `market_id`, `market_code`, `market_name`, `region_id`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`

### Q2 2026 (12) — Chevron

For Chevron, beyond the contracted power project, is there more value from acreage and wells already in the county?

- `energy.supply.fact_power_capacity`: `capacity_quantity`, `later_project_flag`, `fiscal_quarter_id`, `project_id`, `facility_id`
- `energy.supply.fact_acreage`: `acreage_quantity`, `well_quantity`, `fiscal_quarter_id`, `play_id`, `well_type_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_project`: `project_id`, `project_code`, `project_name`, `country_id`, `asset_id`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.resource.dim_well_type`: `well_type_id`, `well_type_code`, `well_type_name`

### Q2 2026 (14) — Chevron

For Chevron, what is the latest view on further investment in Vaca Muerta?

- `energy.supply.fact_argentina_ramp`: `ramp_quantity`, `gate_code`, `comparable_to_peer_flag`, `fiscal_quarter_id`, `play_id`, `country_id`
- `energy.price.fact_allocation`: `allocated_amount`, `decision_status_code`, `more_capital_flag`, `fiscal_quarter_id`, `capital_item_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.price.dim_capital_item`: `capital_item_id`, `item_code`, `item_name`

### Q1 2026 (1) — Chevron

For Chevron, what margin is being captured in refining and from waterborne crudes after the merger, and how did the first quarter show that?

- `energy.price.fact_refining_margin`: `margin_amount`, `captured_amount`, `quarter_shown_flag`, `fiscal_quarter_id`, `facility_id`, `marker_id`
- `energy.supply.fact_waterborne`: `available_quantity`, `in_slate_flag`, `fiscal_quarter_id`, `product_id`, `facility_id`
- `energy.supply.fact_acquired_volume`: `acquired_quantity`, `at_high_end_flag`, `fiscal_quarter_id`, `play_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.price.dim_marker`: `marker_id`, `marker_code`, `marker_name`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`

### Q1 2026 (2) — Chevron

For Chevron, have Venezuela fiscal terms changed enough to do more than recycle cash and pay down the legacy balance?

- `energy.supply.fact_venezuela_asset`: `condition_code`, `resource_quantity`, `fiscal_quarter_id`, `country_id`, `asset_id`
- `energy.price.fact_fiscal_terms`: `terms_changed_flag`, `recycle_only_flag`, `forward_only_flag`, `fiscal_quarter_id`, `fiscal_regime_id`, `country_id`
- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_asset`: `asset_id`, `asset_code`, `asset_name`, `country_id`, `play_id`
- `energy.price.dim_fiscal_regime`: `fiscal_regime_id`, `regime_code`, `regime_name`, `country_id`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`

### Q1 2026 (6) — Chevron

For Chevron, what is driving Tengiz above nameplate, and what debottlenecking remains?

- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.supply.fact_capacity`: `nameplate_quantity`, `remaining_quantity`, `at_capacity_flag`, `fiscal_quarter_id`, `field_id`, `facility_id`
- `energy.supply.fact_debottleneck`: `remaining_quantity`, `underway_flag`, `fiscal_quarter_id`, `field_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`

### Q1 2026 (7) — Chevron

For Chevron, how much LNG is uncommitted and available for arbitrage in a tighter market?

- `energy.supply.fact_lng_train`: `trains_down_quantity`, `concentrated_flag`, `fiscal_quarter_id`, `train_id`, `country_id`, `facility_id`
- `energy.supply.fact_uncommitted_lng`: `uncommitted_quantity`, `available_for_arbitrage_flag`, `fiscal_quarter_id`, `facility_id`, `train_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_train`: `train_id`, `train_code`, `train_name`, `facility_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`

### Q1 2026 (8) — Chevron

For Chevron, can a U.S.-heavy chemicals system capture a polyethylene price move while naphtha crackers elsewhere are short of feedstock?

- `energy.supply.fact_chemical_capacity`: `capacity_quantity`, `us_heavy_flag`, `feedstock_advantage_flag`, `fiscal_quarter_id`, `facility_id`, `country_id`
- `energy.demand.fact_polyethylene_demand`: `demand_quantity`, `captured_move_flag`, `fiscal_quarter_id`, `product_id`, `country_id`
- `energy.demand.fact_chemical_demand`: `demand_quantity`, `feedstock_short_flag`, `green_shoot_flag`, `fiscal_quarter_id`, `product_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`

### Q1 2026 (10) — Chevron

For Chevron, how are the operated and non-operated Eastern Mediterranean gas assets being prioritized given the nearby conflict?

- `energy.supply.fact_gas_priority`: `priority_code`, `operatorship_code`, `conflict_flag`, `fiscal_quarter_id`, `asset_id`, `operator_role_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_asset`: `asset_id`, `asset_code`, `asset_name`, `country_id`, `play_id`
- `energy.resource.dim_operator_role`: `operator_role_id`, `role_code`, `role_name`

### Q1 2026 (12) — Chevron

For Chevron, has the exploration order changed in order to get oil to market faster?

- `energy.supply.fact_exploration`: `campaign_status_code`, `well_result_code`, `industry_push_flag`, `fiscal_quarter_id`, `country_id`, `play_id`
- `energy.supply.fact_new_country`: `queue_changed_flag`, `accelerated_flag`, `fiscal_quarter_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`

### Q1 2026 (13) — Chevron

For Chevron, have California refineries used shipping rules or other operating changes to keep the market supplied?

- `energy.supply.fact_refinery_capacity`: `throughput_quantity`, `can_run_heavy_flag`, `operating_change_flag`, `fiscal_quarter_id`, `facility_id`, `market_id`
- `energy.demand.fact_import_demand`: `import_quantity`, `needed_flag`, `fiscal_quarter_id`, `product_id`, `market_id`
- `energy.supply.fact_inventory`: `inventory_quantity`, `drawn_flag`, `fiscal_quarter_id`, `market_id`, `product_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.geography.dim_market`: `market_id`, `market_code`, `market_name`, `region_id`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`

### Q4 2025 (1) — Chevron

For Chevron, how do Tengiz volumes in the year ahead reflect the maintenance schedule, the power-distribution issue, and debottlenecking?

- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.supply.fact_maintenance`: `downtime_days`, `on_schedule_flag`, `fiscal_quarter_id`, `field_id`, `facility_id`
- `energy.supply.fact_power_distribution`: `constrained_flag`, `issue_open_flag`, `fiscal_quarter_id`, `field_id`
- `energy.supply.fact_capacity`: `nameplate_quantity`, `remaining_quantity`, `at_capacity_flag`, `fiscal_quarter_id`, `field_id`, `facility_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`

### Q4 2025 (2) — Chevron

For Chevron, what condition are the Venezuela assets in, and how large could the resource be in the portfolio?

- `energy.supply.fact_venezuela_asset`: `condition_code`, `resource_quantity`, `fiscal_quarter_id`, `country_id`, `asset_id`
- `energy.supply.fact_reserves`: `resource_quantity`, `condition_code`, `fiscal_quarter_id`, `country_id`, `asset_id`
- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_asset`: `asset_id`, `asset_code`, `asset_name`, `country_id`, `play_id`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`

### Q4 2025 (3) — Chevron

For Chevron, how do Kazakhstan's planned compensation cuts interact with Tengiz maintenance?

- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.supply.fact_kazakhstan_limit`: `cut_quantity`, `overlaps_maintenance_flag`, `fiscal_quarter_id`, `field_id`, `country_id`
- `energy.supply.fact_maintenance`: `downtime_days`, `on_schedule_flag`, `fiscal_quarter_id`, `field_id`, `facility_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`

### Q4 2025 (5) — Chevron

For Chevron, now that Permian well productivity is showing up in capital efficiency, what does that momentum mean for a short-cycle asset?

- `energy.supply.fact_well_productivity`: `productivity_index`, `short_cycle_flag`, `fiscal_quarter_id`, `play_id`, `well_type_id`
- `energy.price.fact_capital_efficiency`: `capital_per_unit_amount`, `improving_flag`, `fiscal_quarter_id`, `play_id`, `capital_item_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.resource.dim_well_type`: `well_type_id`, `well_type_code`, `well_type_name`
- `energy.price.dim_capital_item`: `capital_item_id`, `item_code`, `item_name`

### Q4 2025 (6) — Chevron

For Chevron, how do Libya and Iraq compare with peers' interest, and is a smaller LNG portfolio a different long-term view?

- `energy.supply.fact_exploration`: `campaign_status_code`, `well_result_code`, `industry_push_flag`, `fiscal_quarter_id`, `country_id`, `play_id`
- `energy.price.fact_above_ground`: `risk_score`, `competes_flag`, `fiscal_quarter_id`, `country_id`, `hurdle_id`
- `energy.supply.fact_lng_train`: `trains_down_quantity`, `concentrated_flag`, `fiscal_quarter_id`, `train_id`, `country_id`, `facility_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.price.dim_hurdle`: `hurdle_id`, `hurdle_code`, `hurdle_name`
- `energy.resource.dim_train`: `train_id`, `train_code`, `train_name`, `facility_id`

### Q4 2025 (7) — Chevron

For Chevron, can heavy Venezuela barrels be run on the Gulf Coast and elsewhere, alongside a competitor closing California capacity?

- `energy.price.fact_refining_margin`: `margin_amount`, `captured_amount`, `quarter_shown_flag`, `fiscal_quarter_id`, `facility_id`, `marker_id`
- `energy.supply.fact_heavy_intake`: `intake_quantity`, `backs_out_other_flag`, `fiscal_quarter_id`, `facility_id`, `product_id`
- `energy.supply.fact_refinery_capacity`: `throughput_quantity`, `can_run_heavy_flag`, `operating_change_flag`, `fiscal_quarter_id`, `facility_id`, `market_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.price.dim_marker`: `marker_id`, `marker_code`, `marker_name`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`
- `energy.geography.dim_market`: `market_id`, `market_code`, `market_name`, `region_id`

### Q4 2025 (8) — Chevron

For Chevron, are early surfactant results outside the Permian, in the DJ or Bakken, similar?

- `energy.supply.fact_surfactant_trial`: `similar_result_flag`, `trial_status_code`, `fiscal_quarter_id`, `play_id`, `technology_id`
- `energy.supply.fact_shale_position`: `core_flag`, `learnings_applied_flag`, `paused_growth_flag`, `fiscal_quarter_id`, `play_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.resource.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`

### Q4 2025 (9) — Chevron

For Chevron, how is the Bakken performing versus expectations after a couple of quarters of cross-learning?

- `energy.supply.fact_shale_position`: `core_flag`, `learnings_applied_flag`, `paused_growth_flag`, `fiscal_quarter_id`, `play_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`

### Q4 2025 (10) — Chevron

For Chevron, how much Venezuela heavy can U.S. refineries take without backing out Canadian heavy or changing the heavy-light spread?

- `energy.supply.fact_heavy_intake`: `intake_quantity`, `backs_out_other_flag`, `fiscal_quarter_id`, `facility_id`, `product_id`
- `energy.supply.fact_refinery_capacity`: `throughput_quantity`, `can_run_heavy_flag`, `operating_change_flag`, `fiscal_quarter_id`, `facility_id`, `market_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`
- `energy.geography.dim_market`: `market_id`, `market_code`, `market_name`, `region_id`

### Q3 2025 (1) — Chevron

For Chevron, what drove the Permian result, including any difference between operated and non-operated acreage?

- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.supply.fact_operated_split`: `operated_quantity`, `nonoperated_quantity`, `fiscal_quarter_id`, `play_id`, `operator_role_id`
- `energy.price.fact_capital_efficiency`: `capital_per_unit_amount`, `improving_flag`, `fiscal_quarter_id`, `play_id`, `capital_item_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_operator_role`: `operator_role_id`, `role_code`, `role_name`

### Q3 2025 (2) — Chevron

For Chevron, is the Bakken core, and does it compete as part of a broader Rockies position?

- `energy.supply.fact_shale_position`: `core_flag`, `learnings_applied_flag`, `paused_growth_flag`, `fiscal_quarter_id`, `play_id`, `country_id`
- `energy.price.fact_allocation`: `allocated_amount`, `decision_status_code`, `more_capital_flag`, `fiscal_quarter_id`, `capital_item_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.price.dim_capital_item`: `capital_item_id`, `item_code`, `item_name`

### Q3 2025 (3) — Chevron

For Chevron, what drove the acquired production to the high end of expectations?

- `energy.supply.fact_acquired_volume`: `acquired_quantity`, `at_high_end_flag`, `fiscal_quarter_id`, `play_id`, `country_id`
- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.supply.fact_shale_position`: `core_flag`, `learnings_applied_flag`, `paused_growth_flag`, `fiscal_quarter_id`, `play_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`

### Q3 2025 (4) — Chevron

For Chevron, how prospective is Namibia after the early wells and a larger campaign?

- `energy.supply.fact_exploration`: `campaign_status_code`, `well_result_code`, `industry_push_flag`, `fiscal_quarter_id`, `country_id`, `play_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`

### Q3 2025 (5) — Chevron

For Chevron, has the way the base business is managed changed, and is that repeatable?

- `energy.supply.fact_base_production`: `base_quantity`, `managed_differently_flag`, `repeatable_flag`, `fiscal_quarter_id`, `play_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`

### Q3 2025 (6) — Chevron

For Chevron, is the heavier upstream mix acceptable, or should downstream and chemicals be larger over time?

- `energy.supply.fact_portfolio_volume`: `upstream_quantity`, `other_quantity`, `fiscal_quarter_id`, `product_id`
- `energy.price.fact_portfolio_earnings`: `upstream_share_rate`, `downstream_share_rate`, `chemicals_share_rate`, `heavier_acceptable_flag`, `fiscal_quarter_id`
- `energy.supply.fact_chemical_capacity`: `capacity_quantity`, `us_heavy_flag`, `feedstock_advantage_flag`, `fiscal_quarter_id`, `facility_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`

### Q3 2025 (8) — Chevron

For Chevron, is Tengiz essentially at capacity even with a fourth-quarter turnaround?

- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.supply.fact_capacity`: `nameplate_quantity`, `remaining_quantity`, `at_capacity_flag`, `fiscal_quarter_id`, `field_id`, `facility_id`
- `energy.supply.fact_turnaround`: `turnaround_days`, `still_at_capacity_flag`, `fiscal_quarter_id`, `field_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`

### Q3 2025 (9) — Chevron

For Chevron, what is the state of the Permian if shale has to make room for other supply next year?

- `energy.supply.fact_shale_position`: `core_flag`, `learnings_applied_flag`, `paused_growth_flag`, `fiscal_quarter_id`, `play_id`, `country_id`
- `energy.supply.fact_operated_split`: `operated_quantity`, `nonoperated_quantity`, `fiscal_quarter_id`, `play_id`, `operator_role_id`
- `energy.supply.fact_royalty`: `royalty_quantity`, `fiscal_quarter_id`, `play_id`, `well_type_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_operator_role`: `operator_role_id`, `role_code`, `role_name`
- `energy.resource.dim_well_type`: `well_type_id`, `well_type_code`, `well_type_name`

### Q3 2025 (10) — Chevron

For Chevron, what could Argentina production become over two or three years, and what gates it, given acreage comparable to the DJ?

- `energy.supply.fact_argentina_ramp`: `ramp_quantity`, `gate_code`, `comparable_to_peer_flag`, `fiscal_quarter_id`, `play_id`, `country_id`
- `energy.supply.fact_surfactant_trial`: `similar_result_flag`, `trial_status_code`, `fiscal_quarter_id`, `play_id`, `technology_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_technology`: `technology_id`, `technology_code`, `technology_name`

### Q3 2025 (11) — Chevron

For Chevron, what is different about Permian operations versus smaller peers that are dropping rigs and completion crews?

- `energy.supply.fact_shale_position`: `core_flag`, `learnings_applied_flag`, `paused_growth_flag`, `fiscal_quarter_id`, `play_id`, `country_id`
- `energy.supply.fact_rigs`: `rig_quantity`, `peers_dropping_flag`, `fiscal_quarter_id`, `play_id`
- `energy.supply.fact_completion_crews`: `crew_quantity`, `peers_dropping_flag`, `fiscal_quarter_id`, `play_id`
- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`

### Q1 2026 (2) — Exxon Mobil

Does a higher price and the need for U.S. barrels change Permian activity, for the industry or for Exxon?

- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.supply.fact_activity`: `activity_index`, `changed_flag`, `fiscal_quarter_id`, `play_id`
- `energy.price.fact_oil_price`: `price_amount`, `higher_flag`, `fiscal_quarter_id`, `marker_id`, `play_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.price.dim_marker`: `marker_id`, `marker_code`, `marker_name`

### Q1 2026 (3) — Exxon Mobil

For Exxon Mobil, how does force majeure on the Qatar trains interact with the remaining contract length, and does the contract get extended?

- `energy.supply.fact_force_majeure`: `in_force_flag`, `term_covers_repair_flag`, `fiscal_quarter_id`, `train_id`, `contract_id`
- `energy.price.fact_lng_contract`: `years_remaining`, `extension_likely_flag`, `contracting_changed_flag`, `fiscal_quarter_id`, `contract_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_train`: `train_id`, `train_code`, `train_name`, `facility_id`
- `energy.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `product_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`

### Q1 2026 (4) — Exxon Mobil

For Exxon Mobil, does the concentration of the LNG portfolio in Qatar change the portfolio strategy versus a more diversified upstream?

- `energy.supply.fact_lng_train`: `trains_down_quantity`, `concentrated_flag`, `fiscal_quarter_id`, `train_id`, `country_id`, `facility_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_train`: `train_id`, `train_code`, `train_name`, `facility_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`

### Q1 2026 (5) — Exxon Mobil

For Exxon Mobil, can heavy-oil technology bring Canada, including Aspen, back faster given short supply?

- `energy.supply.fact_heavy_oil`: `capacity_quantity`, `restart_faster_flag`, `fiscal_quarter_id`, `asset_id`, `technology_id`, `country_id`
- `energy.supply.fact_shale_toolkit`: `extends_beyond_shale_flag`, `resource_type_code`, `fiscal_quarter_id`, `technology_id`, `play_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_asset`: `asset_id`, `asset_code`, `asset_name`, `country_id`, `play_id`
- `energy.resource.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`

### Q1 2026 (6) — Exxon Mobil

For Exxon Mobil, is cold-box lead time the main reason damaged Qatar trains take three to five years to return?

- `energy.supply.fact_lead_time`: `lead_time_years`, `is_critical_path_flag`, `fiscal_quarter_id`, `train_id`, `facility_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_train`: `train_id`, `train_code`, `train_name`, `facility_id`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`

### Q4 2025 (1) — Exxon Mobil

For Exxon Mobil, what happens to Guyana growth as the Stabroek license expiration approaches?

- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.supply.fact_license_term`: `years_remaining`, `growth_continues_flag`, `fiscal_quarter_id`, `asset_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_asset`: `asset_id`, `asset_code`, `asset_name`, `country_id`, `play_id`

### Q4 2025 (2) — Exxon Mobil

For Exxon Mobil, with Permian exit and full-year rates both around the same level, is there upside in the intra-year cadence?

- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`

### Q4 2025 (3) — Exxon Mobil

For Exxon Mobil, do assets added beyond the 2030s still have to look like Guyana, the Permian, and LNG?

- `energy.supply.fact_portfolio_volume`: `upstream_quantity`, `other_quantity`, `fiscal_quarter_id`, `product_id`
- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.supply.fact_shale_position`: `core_flag`, `learnings_applied_flag`, `paused_growth_flag`, `fiscal_quarter_id`, `play_id`, `country_id`
- `energy.supply.fact_uncommitted_lng`: `uncommitted_quantity`, `available_for_arbitrage_flag`, `fiscal_quarter_id`, `facility_id`, `train_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`

### Q4 2025 (4) — Exxon Mobil

For Exxon Mobil, how far does the Permian technology toolkit scale beyond U.S. shale?

- `energy.supply.fact_shale_toolkit`: `extends_beyond_shale_flag`, `resource_type_code`, `fiscal_quarter_id`, `technology_id`, `play_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`

### Q4 2025 (8) — Exxon Mobil

For Exxon Mobil, what base decline should be assumed for the upstream, and what mid-cycle return is expected in refining and chemicals?

- `energy.supply.fact_decline`: `decline_rate`, `assumption_rate`, `fiscal_quarter_id`, `play_id`
- `energy.price.fact_refining_margin`: `margin_amount`, `captured_amount`, `quarter_shown_flag`, `fiscal_quarter_id`, `facility_id`, `marker_id`
- `energy.supply.fact_chemical_capacity`: `capacity_quantity`, `us_heavy_flag`, `feedstock_advantage_flag`, `fiscal_quarter_id`, `facility_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.price.dim_marker`: `marker_id`, `marker_code`, `marker_name`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`

### Q3 2025 (2) — Exxon Mobil

For Exxon Mobil, how much of the Permian beat and higher full-year guide is the advanced proppant versus spacing or development changes?

- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.supply.fact_proppant`: `recovery_uplift_quantity`, `gassy_zone_flag`, `fiscal_quarter_id`, `play_id`, `technology_id`
- `energy.supply.fact_spacing`: `spacing_share_rate`, `changed_flag`, `fiscal_quarter_id`, `play_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_technology`: `technology_id`, `technology_code`, `technology_name`

### Q3 2025 (3) — Exxon Mobil

For Exxon Mobil, how does the long-term gas and LNG demand outlook change organic or inorganic priorities?

- `energy.supply.fact_gas_resource`: `resource_quantity`, `gassy_flag`, `fiscal_quarter_id`, `play_id`, `product_id`
- `energy.supply.fact_uncommitted_lng`: `uncommitted_quantity`, `available_for_arbitrage_flag`, `fiscal_quarter_id`, `facility_id`, `train_id`
- `energy.price.fact_portfolio_earnings`: `upstream_share_rate`, `downstream_share_rate`, `chemicals_share_rate`, `heavier_acceptable_flag`, `fiscal_quarter_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.resource.dim_train`: `train_id`, `train_code`, `train_name`, `facility_id`

### Q3 2025 (4) — Exxon Mobil

For Exxon Mobil, was the graphite acquisition facilities, technology, or both, and how tightly does it tie to refining and chemicals?

- `energy.supply.fact_graphite`: `facilities_flag`, `technology_flag`, `tie_to_refining_flag`, `fiscal_quarter_id`, `technology_id`, `facility_id`
- `energy.price.fact_refining_margin`: `margin_amount`, `captured_amount`, `quarter_shown_flag`, `fiscal_quarter_id`, `facility_id`, `marker_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.price.dim_marker`: `marker_id`, `marker_code`, `marker_name`

### Q3 2025 (6) — Exxon Mobil

For Exxon Mobil, is the organization at its limit given the number of projects underway?

- `energy.supply.fact_project_load`: `active_project_count`, `can_add_more_flag`, `fiscal_quarter_id`, `project_id`
- `energy.supply.fact_org_capacity`: `at_limit_flag`, `active_project_count`, `fiscal_quarter_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_project`: `project_id`, `project_code`, `project_name`, `country_id`, `asset_id`

### Q3 2025 (7) — Exxon Mobil

For Exxon Mobil, where does Mozambique stand on security, and is an early investment decision still likely?

- `energy.supply.fact_security`: `security_status_code`, `early_decision_likely_flag`, `fiscal_quarter_id`, `project_id`, `country_id`
- `energy.price.fact_allocation`: `allocated_amount`, `decision_status_code`, `more_capital_flag`, `fiscal_quarter_id`, `capital_item_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_project`: `project_id`, `project_code`, `project_name`, `country_id`, `asset_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.price.dim_capital_item`: `capital_item_id`, `item_code`, `item_name`

### Q3 2025 (8) — Exxon Mobil

For Exxon Mobil, what exploration opportunities are in the next one to two years, and has the approach changed?

- `energy.supply.fact_exploration`: `campaign_status_code`, `well_result_code`, `industry_push_flag`, `fiscal_quarter_id`, `country_id`, `play_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`

### Q3 2025 (9) — Exxon Mobil

For Exxon Mobil, where is the proppant improving recovery the most, including gassier zones?

- `energy.supply.fact_proppant`: `recovery_uplift_quantity`, `gassy_zone_flag`, `fiscal_quarter_id`, `play_id`, `technology_id`
- `energy.supply.fact_gas_resource`: `resource_quantity`, `gassy_flag`, `fiscal_quarter_id`, `play_id`, `product_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.resource.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`

### Q3 2025 (10) — Exxon Mobil

For Exxon Mobil, what is driving the broader industry push back into exploration?

- `energy.supply.fact_exploration`: `campaign_status_code`, `well_result_code`, `industry_push_flag`, `fiscal_quarter_id`, `country_id`, `play_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`

### Q4 2024 (1) — Exxon Mobil

For Exxon Mobil, what Guyana milestones matter this year, and how is the asset tracking?

- `energy.supply.fact_production`: `production_quantity`, `above_nameplate_flag`, `sequential_increase_flag`, `fiscal_quarter_id`, `field_id`, `play_id`, `country_id`
- `energy.supply.fact_startup`: `milestone_code`, `on_plan_flag`, `months_to_start`, `fiscal_quarter_id`, `project_id`, `asset_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_field`: `field_id`, `field_code`, `field_name`, `play_id`, `country_id`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_project`: `project_id`, `project_code`, `project_name`, `country_id`, `asset_id`
- `energy.resource.dim_asset`: `asset_id`, `asset_code`, `asset_name`, `country_id`, `play_id`

### Q4 2024 (2) — Exxon Mobil

For Exxon Mobil, how would North American tariffs hit Canadian upstream and downstream versus U.S. downstream?

- `energy.supply.fact_heavy_oil`: `capacity_quantity`, `restart_faster_flag`, `fiscal_quarter_id`, `asset_id`, `technology_id`, `country_id`
- `energy.supply.fact_refinery_capacity`: `throughput_quantity`, `can_run_heavy_flag`, `operating_change_flag`, `fiscal_quarter_id`, `facility_id`, `market_id`
- `energy.price.fact_tariff_exposure`: `upstream_exposure_amount`, `downstream_exposure_amount`, `us_downstream_amount`, `fiscal_quarter_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_asset`: `asset_id`, `asset_code`, `asset_name`, `country_id`, `play_id`
- `energy.resource.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`

### Q4 2024 (4) — Exxon Mobil

For Exxon Mobil, what is the timing of the near-term start-ups beyond Guyana that contribute the earnings queued up?

- `energy.supply.fact_startup`: `milestone_code`, `on_plan_flag`, `months_to_start`, `fiscal_quarter_id`, `project_id`, `asset_id`
- `energy.price.fact_earnings`: `earnings_amount`, `startup_contribution_amount`, `fiscal_quarter_id`, `project_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_project`: `project_id`, `project_code`, `project_name`, `country_id`, `asset_id`
- `energy.resource.dim_asset`: `asset_id`, `asset_code`, `asset_name`, `country_id`, `play_id`

### Q4 2024 (6) — Exxon Mobil

For Exxon Mobil, how does LNG contracting change as permit constraints ease, and is the medium-term market oversupplied?

- `energy.price.fact_lng_contract`: `years_remaining`, `extension_likely_flag`, `contracting_changed_flag`, `fiscal_quarter_id`, `contract_id`, `country_id`
- `energy.supply.fact_third_party_lng`: `supply_quantity`, `oversupplied_flag`, `fiscal_quarter_id`, `contract_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `product_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`

### Q4 2024 (9) — Exxon Mobil

For Exxon Mobil, why is the Gulf of Mexico a small deepwater position relative to Angola and Guyana?

- `energy.supply.fact_deepwater`: `position_quantity`, `small_versus_peers_flag`, `fiscal_quarter_id`, `play_id`, `country_id`
- `energy.price.fact_cost_of_supply`: `cost_amount`, `rank_code`, `fiscal_quarter_id`, `country_id`, `capital_item_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.resource.dim_play`: `play_id`, `play_code`, `play_name`, `country_id`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.price.dim_capital_item`: `capital_item_id`, `item_code`, `item_name`
