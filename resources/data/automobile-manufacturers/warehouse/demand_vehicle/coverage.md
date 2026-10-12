# Automaker Inc demand and vehicle

This slice owns vehicle families, cities, channels, and delivery, fleet, and mile quantities for Automaker Inc. A demand row does not store a price and does not store plant capacity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `component_identity` | `component_id` | `sf:automaker.supply.dim_component` `component_id` |
| `component_identity` | `component_id` | `sf:automaker.supply.dim_component` `component_id` |
| `regulation_identity` | `regulation_id` | `sf:automaker.supply.dim_regulation` `regulation_id` |
| `component_identity` | `component_id` | `sf:automaker.supply.dim_component` `component_id` |
| `component_identity` | `component_id` | `sf:automaker.supply.dim_component` `component_id` |
| `regulation_identity` | `regulation_id` | `sf:automaker.supply.dim_regulation` `regulation_id` |
| `component_identity` | `component_id` | `sf:automaker.supply.dim_component` `component_id` |

## Numbered questions

## Tesla

### Q2 2026 (2)

What state-level sensor rules would Tesla need, or want to avoid, before it expands the robotaxi rollout?

- `automaker.geography.dim_state`: `country_id`, `state_code`, `state_name`
- `automaker.supply.dim_regulation`: `country_id`, `regulation_code`, `regulation_name`
- `automaker.supply.fact_approval_gate`: `fiscal_quarter_id`, `regulation_id`, `vehicle_program_id`, `state_id`, `avoid_flag`, `approval_required_flag`
- `automaker.product.dim_vehicle_family`: `vehicle_family_code`, `vehicle_family_name`

### Q2 2026 (3)

Which safety or reliability milestones would cause Tesla to speed up robotaxi fleet growth and new-market launches?

- `automaker.demand.fact_safety_gate`: `fiscal_quarter_id`, `city_id`, `vehicle_program_id`, `speeds_growth_flag`, `milestone_met_flag`
- `automaker.demand.fact_fleet`: `fiscal_quarter_id`, `city_id`, `vehicle_program_id`, `channel_id`, `fleet_count`, `small_fleet_flag`
- `automaker.product.dim_vehicle_family`: `vehicle_family_code`, `vehicle_family_name`

### Q2 2026 (4)

Would Tesla use rideshare partners to raise robotaxi utilization, or keep the service vertically integrated?

- `automaker.demand.fact_utilization`: `fiscal_quarter_id`, `channel_id`, `city_id`, `vehicle_program_id`, `partner_used_flag`, `utilization_rate`
- `automaker.channel.dim_channel`: `channel_code`, `channel_name`
- `automaker.product.dim_vehicle_family`: `vehicle_family_code`, `vehicle_family_name`

### Q2 2026 (5)

Why is Tesla adding cities while the robotaxi vehicle count still looks small, and what blocks a much larger fleet in one major city?

- `automaker.demand.fact_fleet`: `fiscal_quarter_id`, `city_id`, `vehicle_program_id`, `channel_id`, `small_fleet_flag`, `city_count`
- `automaker.demand.fact_miles`: `fiscal_quarter_id`, `city_id`, `autonomy_stack_id`, `vehicle_program_id`, `intervention_count`, `mile_count`
- `automaker.product.dim_vehicle_family`: `vehicle_family_code`, `vehicle_family_name`
- `automaker.demand.fact_utilization`: `fiscal_quarter_id`, `channel_id`, `city_id`, `vehicle_program_id`, `utilization_rate`, `partner_used_flag`

### Q2 2026 (7)

Could Cybercabs with Starlink act as mobile hotspots, not only as connected vehicles for passengers?

- `automaker.demand.fact_connectivity_use`: `fiscal_quarter_id`, `vehicle_program_id`, `component_id`, `hotspot_flag`, `passenger_only_flag`
- `automaker.product.dim_vehicle_family`: `vehicle_family_code`, `vehicle_family_name`

### Q2 2026 (8)

When does Tesla expect unsupervised driving on the Semi, given the truck-driver shortage?

- `automaker.demand.fact_autonomy_timing`: `fiscal_quarter_id`, `vehicle_program_id`, `autonomy_stack_id`, `priority_versus_volume_flag`, `unsupervised_flag`
- `automaker.product.dim_vehicle_family`: `vehicle_family_code`, `vehicle_family_name`

### Q2 2026 (11)

Is Tesla still planning hardware upgrades so older camera-equipped cars can run newer Full Self-Driving software?

- `automaker.demand.fact_hardware_upgrade`: `fiscal_quarter_id`, `component_id`, `software_release_id`, `vehicle_family_id`, `compute_gap_flag`, `upgrade_planned_flag`
- `automaker.software.dim_software_release`: `autonomy_stack_id`, `software_release_code`, `software_release_name`
- `automaker.demand.fact_installed_base`: `fiscal_quarter_id`, `vehicle_family_id`, `country_id`, `component_id`, `camera_equipped_quantity`, `installed_quantity`

### Q2 2026 (14)

How much current storage demand is data-center power smoothing versus utility peak shaving and grid balancing?

- `automaker.demand.fact_storage_demand`: `fiscal_quarter_id`, `use_case_id`, `country_id`, `vehicle_family_id`, `deployment_quantity`, `use_case_share`
- `automaker.product.dim_use_case`: `vehicle_family_id`, `use_case_code`, `use_case_name`

### Q4 2025 (3)

Are memory shortages constraining near-term production, and would Tesla cut features the way it did during earlier chip shortages?

- `automaker.demand.fact_feature_cut`: `fiscal_quarter_id`, `component_id`, `vehicle_family_id`, `same_playbook_flag`, `cut_flag`
- `automaker.supply.fact_production`: `fiscal_quarter_id`, `plant_id`, `vehicle_program_id`, `component_id`, `constrained_flag`, `production_quantity`
- `automaker.supply.fact_memory_cover`: `fiscal_quarter_id`, `component_id`, `supplier_id`, `coverage_months`, `shortage_flag`
- `automaker.supply.dim_component`: `component_code`, `component_name`

### Q4 2025 (4)

What keeps Optimus ahead of the new humanoid startups, especially from China, and how will the product differ?

- `automaker.demand.fact_competitive_design`: `fiscal_quarter_id`, `vehicle_program_id`, `country_id`, `difference_code`, `ahead_flag`
- `automaker.geography.dim_country`: `region_id`, `country_code`, `country_name`
- `automaker.product.dim_vehicle_family`: `vehicle_family_code`, `vehicle_family_name`

### Q3 2025 (2)

Which AI applications sit inside Tesla's core work, and which markets should stay outside it?

- `automaker.demand.fact_product_scope`: `fiscal_quarter_id`, `vehicle_family_id`, `use_case_id`, `in_scope_flag`, `outside_market_flag`
- `automaker.product.dim_vehicle_family`: `vehicle_family_code`, `vehicle_family_name`

### Q3 2025 (3)

If the safety driver can leave the Austin robotaxi at year-end, is the Bay Area limit regulation or local learning, and do new cities start with an attendant?

- `automaker.demand.fact_city_staffing`: `fiscal_quarter_id`, `city_id`, `regulation_id`, `autonomy_stack_id`, `limit_code`, `driver_removed_flag`
- `automaker.geography.dim_city`: `country_id`, `city_code`, `city_name`
- `automaker.demand.fact_coverage_limit`: `fiscal_quarter_id`, `service_id`, `regulation_id`, `country_id`, `limit_code`, `expanded_flag`
- `automaker.product.dim_vehicle_family`: `vehicle_family_code`, `vehicle_family_name`

### Q3 2025 (4)

Are consumer Full Self-Driving builds on a different path from the robotaxi stack, and are new releases aimed at fewer interventions or at added functions such as parking and comfort?

- `automaker.demand.fact_software_path`: `fiscal_quarter_id`, `software_release_id`, `autonomy_stack_id`, `release_aim_code`, `separate_path_flag`
- `automaker.software.dim_autonomy_stack`: `autonomy_stack_code`, `autonomy_stack_name`
- `automaker.software.dim_software_release`: `autonomy_stack_id`, `software_release_code`, `software_release_name`
- `automaker.product.dim_vehicle_family`: `vehicle_family_code`, `vehicle_family_name`

### Q2 2025 (1)

How many robotaxis are operating, how many autonomous miles and safety-critical interventions have they logged, and what targets should follow?

- `automaker.demand.fact_fleet`: `fiscal_quarter_id`, `city_id`, `vehicle_program_id`, `channel_id`, `fleet_count`, `small_fleet_flag`
- `automaker.demand.fact_miles`: `fiscal_quarter_id`, `city_id`, `autonomy_stack_id`, `vehicle_program_id`, `intervention_count`, `mile_count`
- `automaker.product.dim_vehicle_family`: `vehicle_family_code`, `vehicle_family_name`
- `automaker.demand.fact_safety_gate`: `fiscal_quarter_id`, `city_id`, `vehicle_program_id`, `speeds_growth_flag`, `milestone_met_flag`

### Q2 2025 (3)

What has to happen, and on what timeline, before customer-owned vehicles can join the robotaxi network?

- `automaker.demand.fact_network_entry`: `fiscal_quarter_id`, `vehicle_family_id`, `software_release_id`, `eligible_flag`, `timing_code`
- `automaker.product.dim_vehicle_family`: `vehicle_family_code`, `vehicle_family_name`

### Q2 2025 (5)

What are current Full Self-Driving subscription trends, take rates, and revenue after the consumer trials?

- `automaker.demand.fact_fsd_attach`: `fiscal_quarter_id`, `software_release_id`, `vehicle_family_id`, `country_id`, `take_rate`, `trial_conversion_rate`
- `automaker.price.fact_fsd_revenue`: `fiscal_quarter_id`, `software_release_id`, `service_id`, `revenue_amount`
- `automaker.demand.fact_subscription_demand`: `fiscal_quarter_id`, `service_id`, `trim_id`, `vehicle_family_id`, `paid_subscription_count`, `take_rate`
- `automaker.software.dim_software_release`: `autonomy_stack_id`, `software_release_code`, `software_release_name`

## General Motors

### Q1 2026 (7)

Is paid Super Cruise demand concentrated in Cadillac, or is it showing up more broadly across the portfolio?

- `automaker.demand.fact_subscription_demand`: `fiscal_quarter_id`, `service_id`, `trim_id`, `vehicle_family_id`, `concentrated_in_luxury_flag`, `paid_subscription_count`
- `automaker.software.dim_service`: `vehicle_family_id`, `service_code`, `service_name`
- `automaker.price.fact_service_revenue`: `fiscal_quarter_id`, `service_id`, `vehicle_program_id`, `revenue_per_vehicle_amount`, `main_driver_flag`, `revenue_amount`

### Q1 2026 (9)

How should international volume and profit track versus the first quarter, and does the usual pattern of stronger second and third quarters still hold?

- `automaker.demand.fact_regional_volume`: `fiscal_quarter_id`, `region_id`, `country_id`, `vehicle_family_id`, `seasonal_pattern_flag`, `delivery_quantity`
- `automaker.price.fact_regional_profit`: `fiscal_quarter_id`, `region_id`, `country_id`, `flat_flag`, `profit_amount`, `finished_run_rate_flag`
- `automaker.demand.fact_delivery`: `fiscal_quarter_id`, `vehicle_family_id`, `powertrain_id`, `country_id`, `region_id`, `cadence_code`
- `automaker.geography.dim_region`: `region_code`, `region_name`

### Q1 2026 (12)

What limits putting digital subscriptions on the large installed base that does not subscribe today, including hardware?

- `automaker.demand.fact_subscription_limit`: `fiscal_quarter_id`, `service_id`, `component_id`, `vehicle_family_id`, `hardware_limit_flag`, `other_limit_code`
- `automaker.demand.fact_installed_base`: `fiscal_quarter_id`, `vehicle_family_id`, `country_id`, `component_id`, `installed_quantity`, `unsubscribed_quantity`
- `automaker.software.dim_service`: `vehicle_family_id`, `service_code`, `service_name`

### Q1 2026 (13)

What limits expanding Super Cruise road coverage: regulation or GM's own risk appetite?

- `automaker.demand.fact_coverage_limit`: `fiscal_quarter_id`, `service_id`, `regulation_id`, `country_id`, `limit_code`, `expanded_flag`
- `automaker.software.dim_service`: `vehicle_family_id`, `service_code`, `service_name`

### Q1 2026 (15)

In the more profitable slices of full-size pickups, is GM holding share, or are competitor gains concentrated in less profitable slices?

- `automaker.demand.fact_trim_share`: `fiscal_quarter_id`, `trim_id`, `vehicle_family_id`, `country_id`, `holding_flag`, `share_rate`
- `automaker.product.dim_trim`: `vehicle_family_id`, `trim_code`, `trim_name`

### Q4 2025 (11)

How much of this year's EV volume decline can convert into incremental ICE demand, and how does that change inventory and wholesale planning?

- `automaker.demand.fact_powertrain_mix`: `fiscal_quarter_id`, `powertrain_id`, `vehicle_family_id`, `country_id`, `converted_quantity`, `delivery_quantity`
- `automaker.product.dim_powertrain`: `powertrain_code`, `powertrain_name`
- `automaker.price.fact_emissions_volume`: `fiscal_quarter_id`, `regulation_id`, `vehicle_family_id`, `creates_volume_flag`, `offsets_trade_flag`

### Q3 2025 (2)

How does GM see 2026 demand given consumer and credit worries, and how does a competitor's added pickup product change the competitive setup?

- `automaker.demand.fact_consumer_demand`: `fiscal_quarter_id`, `country_id`, `vehicle_family_id`, `competitor_product_flag`, `credit_worry_flag`, `demand_index`
- `automaker.demand.fact_autonomy_timing`: `fiscal_quarter_id`, `vehicle_program_id`, `autonomy_stack_id`, `priority_versus_volume_flag`, `unsupervised_flag`

### Q3 2025 (11)

Do Chinese automakers eventually sell in the United States, and how would that entry evolve?

- `automaker.demand.fact_competitor_entry`: `fiscal_quarter_id`, `country_id`, `vehicle_family_id`, `entry_flag`, `path_code`
- `automaker.geography.dim_country`: `region_id`, `country_code`, `country_name`

### Q3 2025 (17)

Is the Hyundai development partnership for South America the way GM competes with Chinese automakers abroad, and is GM pushing international markets again?

- `automaker.demand.fact_partnership`: `fiscal_quarter_id`, `country_id`, `region_id`, `vehicle_family_id`, `pushing_again_flag`, `partnership_flag`
- `automaker.geography.dim_region`: `region_code`, `region_name`
- `automaker.demand.fact_competitor_entry`: `fiscal_quarter_id`, `country_id`, `vehicle_family_id`, `entry_flag`, `path_code`

### Q2 2025 (1)

As purchase credits end and rules change, how broad should the EV lineup stay, and do profitable price points move higher?

- `automaker.demand.fact_lineup`: `fiscal_quarter_id`, `powertrain_id`, `vehicle_program_id`, `breadth_code`, `point_moved_up_flag`
- `automaker.price.fact_price_action`: `fiscal_quarter_id`, `vehicle_family_id`, `country_id`, `powertrain_id`, `credit_end_flag`, `price_change_rate`
- `automaker.price.fact_ev_loss`: `fiscal_quarter_id`, `powertrain_id`, `still_sold_flag`, `loss_amount`, `overhead_share`, `volume_share`
- `automaker.product.dim_powertrain`: `powertrain_code`, `powertrain_name`

### Q2 2025 (8)

Given a better-than-feared China result and a tougher Europe, should GM concentrate more on the U.S. than on those two markets?

- `automaker.demand.fact_geo_focus`: `fiscal_quarter_id`, `country_id`, `region_id`, `focus_code`, `china_better_flag`
- `automaker.geography.dim_country`: `region_id`, `country_code`, `country_name`
- `automaker.geography.dim_region`: `region_code`, `region_name`
- `automaker.price.fact_regional_profit`: `fiscal_quarter_id`, `region_id`, `country_id`, `flat_flag`, `profit_amount`, `finished_run_rate_flag`
