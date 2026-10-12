# Automaker Inc factory and component supply

This slice owns plants, suppliers, component cover, and production capacity for Automaker Inc. A capacity row does not store a vehicle price. Deliveries stay in demand_vehicle.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `country_identity` | `country_id` | `sf:automaker.geography.dim_country` `country_id` |
| `country_identity` | `country_id` | `sf:automaker.geography.dim_country` `country_id` |
| `country_identity` | `country_id` | `sf:automaker.geography.dim_country` `country_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `vehicle_family_identity` | `vehicle_family_id` | `sf:automaker.product.dim_vehicle_family` `vehicle_family_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `vehicle_program_identity` | `vehicle_program_id` | `sf:automaker.product.dim_vehicle_program` `vehicle_program_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `vehicle_program_identity` | `vehicle_program_id` | `sf:automaker.product.dim_vehicle_program` `vehicle_program_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `vehicle_program_identity` | `vehicle_program_id` | `sf:automaker.product.dim_vehicle_program` `vehicle_program_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `vehicle_program_identity` | `vehicle_program_id` | `sf:automaker.product.dim_vehicle_program` `vehicle_program_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `vehicle_family_identity` | `vehicle_family_id` | `sf:automaker.product.dim_vehicle_family` `vehicle_family_id` |
| `country_identity` | `country_id` | `sf:automaker.geography.dim_country` `country_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `vehicle_family_identity` | `vehicle_family_id` | `sf:automaker.product.dim_vehicle_family` `vehicle_family_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `vehicle_program_identity` | `vehicle_program_id` | `sf:automaker.product.dim_vehicle_program` `vehicle_program_id` |
| `country_identity` | `country_id` | `sf:automaker.geography.dim_country` `country_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `vehicle_program_identity` | `vehicle_program_id` | `sf:automaker.product.dim_vehicle_program` `vehicle_program_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `vehicle_program_identity` | `vehicle_program_id` | `sf:automaker.product.dim_vehicle_program` `vehicle_program_id` |
| `country_identity` | `country_id` | `sf:automaker.geography.dim_country` `country_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `vehicle_program_identity` | `vehicle_program_id` | `sf:automaker.product.dim_vehicle_program` `vehicle_program_id` |
| `state_identity` | `state_id` | `sf:automaker.geography.dim_state` `state_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `service_identity` | `service_id` | `sf:automaker.software.dim_service` `service_id` |
| `country_identity` | `country_id` | `sf:automaker.geography.dim_country` `country_id` |
| `software_release_identity` | `software_release_id` | `sf:automaker.software.dim_software_release` `software_release_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `country_identity` | `country_id` | `sf:automaker.geography.dim_country` `country_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `trim_identity` | `trim_id` | `sf:automaker.product.dim_trim` `trim_id` |
| `region_identity` | `region_id` | `sf:automaker.geography.dim_region` `region_id` |
| `vehicle_family_identity` | `vehicle_family_id` | `sf:automaker.product.dim_vehicle_family` `vehicle_family_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `powertrain_identity` | `powertrain_id` | `sf:automaker.product.dim_powertrain` `powertrain_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `vehicle_program_identity` | `vehicle_program_id` | `sf:automaker.product.dim_vehicle_program` `vehicle_program_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:automaker.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `vehicle_family_identity` | `vehicle_family_id` | `sf:automaker.product.dim_vehicle_family` `vehicle_family_id` |

## Numbered questions

## Tesla

### Q2 2026 (1)

Are outside suppliers putting capital into U.S. manufacturing for Optimus, or does Tesla still have to build most of that supply chain itself to ramp faster?

- `automaker.supply.fact_inhouse_capacity`: `fiscal_quarter_id`, `vehicle_program_id`, `plant_id`, `country_id`, `inhouse_capacity_quantity`, `self_build_flag`
- `automaker.price.fact_supplier_investment`: `fiscal_quarter_id`, `supplier_id`, `country_id`, `vehicle_program_id`, `investment_amount`, `committed_flag`
- `automaker.supply.fact_supplier_commitment`: `fiscal_quarter_id`, `supplier_id`, `vehicle_program_id`, `country_id`, `us_manufacturing_flag`, `committed_flag`
- `automaker.supply.dim_supplier`: `country_id`, `supplier_code`, `supplier_name`

### Q2 2026 (6)

Beyond removing the steering wheel and pedals, what federal approvals still gate a Cybercab production ramp?

- `automaker.supply.fact_approval_gate`: `fiscal_quarter_id`, `regulation_id`, `vehicle_program_id`, `state_id`, `blocks_ramp_flag`, `approval_required_flag`
- `automaker.supply.dim_regulation`: `country_id`, `regulation_code`, `regulation_name`
- `automaker.supply.fact_production`: `fiscal_quarter_id`, `plant_id`, `vehicle_program_id`, `component_id`, `constrained_flag`, `production_quantity`
- `automaker.supply.fact_plant_capacity`: `fiscal_quarter_id`, `plant_id`, `vehicle_family_id`, `capacity_quantity`, `fill_timeline_code`

### Q2 2026 (9)

For Optimus processors, controllers, and actuators, how much will Tesla buy, design for outside fabs, or make itself?

- `automaker.supply.fact_sourcing_mode`: `fiscal_quarter_id`, `component_id`, `vehicle_program_id`, `supplier_id`, `mode_code`, `generation_code`
- `automaker.supply.fact_generation_capacity`: `fiscal_quarter_id`, `vehicle_program_id`, `plant_id`, `step_up_flag`, `capacity_quantity`, `start_quarter_code`
- `automaker.product.dim_vehicle_program`: `vehicle_family_id`, `powertrain_id`, `vehicle_program_code`, `vehicle_program_name`
- `automaker.supply.fact_inhouse_capacity`: `fiscal_quarter_id`, `vehicle_program_id`, `plant_id`, `country_id`, `inhouse_capacity_quantity`, `self_build_flag`

### Q2 2026 (10)

When does Optimus 4 production start relative to the much larger volume target versus Optimus 3?

- `automaker.supply.fact_generation_capacity`: `fiscal_quarter_id`, `vehicle_program_id`, `plant_id`, `start_quarter_code`, `capacity_quantity`, `step_up_flag`
- `automaker.product.dim_vehicle_program`: `vehicle_family_id`, `powertrain_id`, `vehicle_program_code`, `vehicle_program_name`
- `automaker.product.dim_vehicle_family`: `vehicle_family_code`, `vehicle_family_name`

### Q2 2026 (13)

How long will energy-storage deployments stay supply-constrained?

- `automaker.supply.fact_constraint`: `fiscal_quarter_id`, `component_id`, `vehicle_family_id`, `plant_id`, `duration_code`, `constrained_flag`
- `automaker.demand.fact_storage_demand`: `fiscal_quarter_id`, `use_case_id`, `country_id`, `vehicle_family_id`, `use_case_share`, `deployment_quantity`

### Q4 2025 (5)

How do battery, memory, and purpose-built hardware programs share R&D, and what advantage does that create across end markets?

- `automaker.supply.fact_shared_hardware`: `fiscal_quarter_id`, `component_id`, `vehicle_family_id`, `shared_flag`, `reused_flag`
- `automaker.price.fact_shared_rd`: `fiscal_quarter_id`, `component_id`, `vehicle_family_id`, `advantage_flag`, `rd_amount`
- `automaker.supply.dim_component`: `component_code`, `component_name`

### Q2 2025 (7)

Which cost reductions from the prior plan, such as less silicon carbide and no rare earths in the motor, are actually in the lower-cost vehicle that ramps later?

- `automaker.supply.fact_bom`: `fiscal_quarter_id`, `component_id`, `vehicle_program_id`, `in_vehicle_flag`, `removed_flag`
- `automaker.price.fact_content_cost`: `fiscal_quarter_id`, `component_id`, `vehicle_program_id`, `in_ramping_vehicle_flag`, `cost_reduction_amount`
- `automaker.supply.dim_component`: `component_code`, `component_name`
- `automaker.product.dim_vehicle_program`: `vehicle_family_id`, `powertrain_id`, `vehicle_program_code`, `vehicle_program_name`

## General Motors

### Q1 2026 (6)

Should investors expect more factory downtime as the next full-size pickup launches?

- `automaker.supply.fact_downtime`: `fiscal_quarter_id`, `plant_id`, `vehicle_program_id`, `downtime_days`, `more_downtime_flag`
- `automaker.product.dim_vehicle_family`: `vehicle_family_code`, `vehicle_family_name`
- `automaker.demand.fact_delivery`: `fiscal_quarter_id`, `vehicle_family_id`, `powertrain_id`, `country_id`, `region_id`, `cadence_code`
- `automaker.supply.fact_changeover`: `fiscal_quarter_id`, `vehicle_program_id`, `plant_id`, `delivery_quantity`, `lands_next_year_flag`, `effect_behind_flag`

### Q1 2026 (10)

Does the full-size truck changeover hit fourth-quarter volume, or is the volume effect already behind the company?

- `automaker.supply.fact_changeover`: `fiscal_quarter_id`, `vehicle_program_id`, `plant_id`, `effect_behind_flag`, `delivery_quantity`, `lands_next_year_flag`
- `automaker.demand.fact_delivery`: `fiscal_quarter_id`, `vehicle_family_id`, `powertrain_id`, `country_id`, `region_id`, `cadence_code`
- `automaker.supply.fact_downtime`: `fiscal_quarter_id`, `plant_id`, `vehicle_program_id`, `downtime_days`, `more_downtime_flag`
- `automaker.price.fact_emissions_volume`: `fiscal_quarter_id`, `regulation_id`, `vehicle_family_id`, `creates_volume_flag`, `offsets_trade_flag`

### Q1 2026 (16)

Which commodities are hedged, and are any raw materials already short or at risk if conflict persists?

- `automaker.supply.fact_shortage`: `fiscal_quarter_id`, `component_id`, `supplier_id`, `conflict_risk_flag`, `short_flag`
- `automaker.supply.fact_hedge_cover`: `fiscal_quarter_id`, `component_id`, `hedged_flag`, `coverage_months`

### Q1 2026 (17)

How does wholesale volume cadence change with the truck refresh, and can depleted truck inventory be rebuilt?

- `automaker.supply.fact_inventory`: `fiscal_quarter_id`, `vehicle_family_id`, `country_id`, `rebuild_flag`, `tight_discipline_flag`, `weeks_on_hand`
- `automaker.demand.fact_delivery`: `fiscal_quarter_id`, `vehicle_family_id`, `powertrain_id`, `country_id`, `region_id`, `cadence_code`

### Q1 2026 (18)

After Orion and remaining Mexico capacity come online, where can GM sell more high-value pickups and SUVs: upper trim, lower trim, or outside North America?

- `automaker.supply.fact_capacity_outlet`: `fiscal_quarter_id`, `plant_id`, `trim_id`, `region_id`, `vehicle_family_id`, `outlet_code`
- `automaker.product.dim_trim`: `vehicle_family_id`, `trim_code`, `trim_name`
- `automaker.supply.dim_plant`: `country_id`, `plant_code`, `plant_name`
- `automaker.geography.dim_region`: `region_code`, `region_name`

### Q1 2026 (19)

How much Mexico capacity stays after Orion depends on where USMCA talks land?

- `automaker.supply.fact_trade_capacity`: `fiscal_quarter_id`, `plant_id`, `country_id`, `regulation_id`, `depends_on_talks_flag`, `capacity_quantity`
- `automaker.supply.dim_plant`: `country_id`, `plant_code`, `plant_name`
- `automaker.geography.dim_country`: `region_id`, `country_code`, `country_name`
- `automaker.supply.fact_capacity_outlet`: `fiscal_quarter_id`, `plant_id`, `trim_id`, `region_id`, `vehicle_family_id`, `capacity_quantity`

### Q4 2025 (3)

Will tight inventory discipline continue, and is it a reason cash generation is running ahead of expectations?

- `automaker.supply.fact_inventory`: `fiscal_quarter_id`, `vehicle_family_id`, `country_id`, `tight_discipline_flag`, `rebuild_flag`, `weeks_on_hand`
- `automaker.price.fact_cash_flow`: `fiscal_quarter_id`, `region_id`, `finance_book_id`, `ahead_of_expectations_flag`, `cash_flow_amount`, `tighter_flag`
- `automaker.price.fact_incentive`: `fiscal_quarter_id`, `vehicle_family_id`, `country_id`, `room_to_recover_flag`, `in_line_with_plan_flag`, `incentive_amount`
- `automaker.channel.dim_channel`: `channel_code`, `channel_name`

### Q4 2025 (8)

What approvals are required to take Super Cruise abroad, and what functionality, including point-to-point, should customers see next?

- `automaker.supply.fact_feature_approval`: `fiscal_quarter_id`, `service_id`, `regulation_id`, `country_id`, `software_release_id`, `approval_required_flag`
- `automaker.software.dim_service`: `vehicle_family_id`, `service_code`, `service_name`
- `automaker.geography.dim_region`: `region_code`, `region_name`

### Q4 2025 (10)

How much downtime is in the full-size pickup launch guide, and do volume and price-mix effects land this year or in 2027?

- `automaker.supply.fact_downtime`: `fiscal_quarter_id`, `plant_id`, `vehicle_program_id`, `downtime_days`, `more_downtime_flag`
- `automaker.price.fact_price_mix`: `fiscal_quarter_id`, `vehicle_program_id`, `price_mix_rate`, `lands_this_year_flag`
- `automaker.product.dim_vehicle_family`: `vehicle_family_code`, `vehicle_family_name`
- `automaker.supply.fact_changeover`: `fiscal_quarter_id`, `vehicle_program_id`, `plant_id`, `lands_next_year_flag`, `delivery_quantity`, `effect_behind_flag`

### Q3 2025 (8)

How many weeks of aluminum, semiconductors, and rare earths do GM and suppliers hold, and how quickly can alternate supply be brought up?

- `automaker.supply.fact_weeks_cover`: `fiscal_quarter_id`, `component_id`, `supplier_id`, `alternate_weeks`, `weeks_on_hand`
- `automaker.supply.fact_inventory`: `fiscal_quarter_id`, `vehicle_family_id`, `country_id`, `rebuild_flag`, `weeks_on_hand`, `tight_discipline_flag`
- `automaker.supply.dim_component`: `component_code`, `component_name`
- `automaker.supply.dim_supplier`: `country_id`, `supplier_code`, `supplier_name`

### Q2 2025 (5)

About where could U.S. dealer inventory finish the year after share gains and a seasonal wholesale decline?

- `automaker.supply.fact_inventory`: `fiscal_quarter_id`, `vehicle_family_id`, `country_id`, `rebuild_flag`, `tight_discipline_flag`, `weeks_on_hand`
- `automaker.channel.dim_channel`: `channel_code`, `channel_name`

### Q2 2025 (7)

If the Korea tariff status quo lasts, do better local economics justify keeping current Korea production and capacity?

- `automaker.supply.fact_trade_capacity`: `fiscal_quarter_id`, `plant_id`, `country_id`, `regulation_id`, `keep_flag`, `capacity_quantity`
- `automaker.supply.dim_plant`: `country_id`, `plant_code`, `plant_name`
- `automaker.geography.dim_country`: `region_id`, `country_code`, `country_name`
- `automaker.price.fact_tariff_mitigation`: `fiscal_quarter_id`, `country_id`, `plant_id`, `beyond_this_year_flag`, `net_tariff_amount`, `relief_excluded_flag`
