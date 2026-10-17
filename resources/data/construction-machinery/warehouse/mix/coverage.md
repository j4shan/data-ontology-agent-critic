# Machinery Inc end markets and power-versus-construction mix

This slice owns the operating segment, the end market, the machine model, the power product, and the capacity, application, and installed-base facts that separate Power & Energy from Construction Industries. Dealer inventory, retail demand, price, volume, and backlog are owned outside this slice. Those identities are partial on the facts that need them and are not re-authored here.

Foreign identities are referenced from this slice and are partial here. Their complete populations are the datasets below, which this slice does not author:

| Identity | Column | Node |
| --- | --- | --- |
| `accounting_period_identity` | `accounting_period_id` | `sf:machinery.calendar.dim_accounting_period` |
| `currency_identity` | `currency_id` | `sf:machinery.commercial.dim_currency` |

## Numbered questions

### Q2 2026 (1) — Whether the 10-megawatt ramp sits inside the 2030 gigawatt target

The 10-megawatt product, the ramp gigawatts, and the inside-versus-additive flag are separate from the 2030 target gigawatts.

- `machinery.product.dim_power_product`: `product_code`, `product_name`
- `machinery.power.fact_engine_capacity_ramp`: `ramp_gigawatts`, `inclusion_versus_target`, `power_product_id`, `capacity_horizon_id`
- `machinery.power.fact_gigawatt_target`: `target_gigawatts`, `capacity_horizon_id`
- `machinery.power.dim_capacity_horizon`: `horizon_year`

### Q2 2026 (3) — Construction volume after the inventory swing versus lighter power volume as capacity comes on

Segment volume is the unit fact and carries no price. The inventory swing is dealer stock. Capacity coming online is the power ramp, not the volume fact.

- `machinery.commercial.fact_segment_volume`: `volume_units`, `volume_versus_expectation`, `segment_id`
- `machinery.market.dim_segment`: `segment_code`
- `machinery.retail.fact_inventory_swing`: `inventory_change_units`, `swing_direction`, `segment_id`
- `machinery.power.fact_engine_capacity_ramp`: `capacity_online_units`, `capacity_still_coming_online_flag`, `segment_id`

### Q2 2026 (6) — Gas reciprocating slots for 2027 and 2028 across prime, flexible, and backup

Open slots and the sold-out flag are by power product, application, and horizon year.

- `machinery.power.fact_application_slots`: `open_slots`, `sold_out_flag`, `power_product_id`, `power_application_id`, `capacity_horizon_id`
- `machinery.product.dim_power_product`: `product_code`
- `machinery.power.dim_power_application`: `application_code`
- `machinery.power.dim_capacity_horizon`: `horizon_year`

### Q2 2026 (9) — Power & Energy aftermarket today versus backlog that enters the installed base later

Current service amount and mix are the aftermarket fact. Backlog that delivers in 2029 and beyond is the installed-base entry, not today's service.

- `machinery.power.fact_aftermarket_service`: `service_amount`, `current_mix_rate`, `segment_id`, `accounting_period_id`
- `machinery.power.fact_installed_base_entry`: `backlog_entering_base_amount`, `delivery_year_label`, `capacity_horizon_id`, `segment_id`
- `machinery.power.dim_capacity_horizon`: `horizon_year`
- `machinery.commercial.fact_backlog_position`: `backlog_amount`, `segment_id`
- `machinery.market.dim_segment`: `segment_code`

### Q2 2026 (11) — Diesel standby redundancy by workload and by site connection

Training versus inference and behind-the-meter versus grid-connected are dimensions. The redundancy requirement is the fact.

- `machinery.power.fact_redundancy_design`: `redundancy_requirement`, `workload_id`, `site_connection_id`, `power_product_id`, `end_market_id`
- `machinery.power.dim_workload`: `workload_code`
- `machinery.power.dim_site_connection`: `connection_code`
- `machinery.product.dim_power_product`: `product_code`
- `machinery.market.dim_end_market`: `market_code`

### Q1 2026 (1) — Which large-engine end market drove capacity, and whether the ramp is smooth or a lump

The end market and the smooth-versus-lump profile are on the capacity-timing fact. Prime power and oil and gas are end-market codes.

- `machinery.power.fact_capacity_timing`: `ramp_profile`, `capacity_added_gigawatts`, `end_market_id`, `power_product_id`, `capacity_horizon_id`
- `machinery.market.dim_end_market`: `market_code`, `market_name`
- `machinery.product.dim_power_product`: `product_code`

### Q1 2026 (3) — Large reciprocating capacity rather than more gas-turbine investment

Each product has its own investment amount and whether it was the allocation selected.

- `machinery.power.fact_turbine_versus_recip`: `capacity_investment_amount`, `allocation_choice`, `power_product_id`, `capacity_horizon_id`
- `machinery.product.dim_power_product`: `product_code`, `product_name`

### Q1 2026 (4) — Whether today's capacity changes the 2030 gigawatt figure, and Power & Energy price realization

The target-changed flag is the gigawatt fact. Price realization, including the new-product mix, is the price fact and stores no volume.

- `machinery.power.fact_gigawatt_target`: `target_changed_flag`, `target_gigawatts`, `capacity_horizon_id`
- `machinery.power.dim_capacity_horizon`: `horizon_year`
- `machinery.commercial.fact_price_realization`: `price_realization_rate`, `new_product_mix_flag`, `segment_id`
- `machinery.market.dim_segment`: `segment_code`

### Q1 2026 (5) — The tightest supplier constraint and the 2030 prime versus backup split

Constraint rank names the tightest supplier. Output share by application is the prime-versus-backup split for the 2030 horizon.

- `machinery.power.fact_supplier_bottleneck`: `constraint_rank`, `constraint_note`, `supplier_id`, `power_product_id`, `capacity_horizon_id`
- `machinery.power.dim_supplier`: `supplier_name`
- `machinery.power.fact_prime_backup_split`: `output_share`, `power_application_id`, `power_product_id`, `capacity_horizon_id`
- `machinery.power.dim_power_application`: `application_code`
- `machinery.power.dim_capacity_horizon`: `horizon_year`
- `machinery.product.dim_power_product`: `product_code`

### Q4 2025 (2) — Power capacity through 2026 and 2027, and overcapacity if data-center demand slows

Machinery Inc's ramp by horizon year is separate from industry gigawatts and from the data-center slowdown flag.

- `machinery.power.fact_engine_capacity_ramp`: `ramp_gigawatts`, `capacity_horizon_id`, `capacity_online_units`
- `machinery.power.dim_capacity_horizon`: `horizon_year`
- `machinery.power.fact_data_center_demand`: `demand_outlook_amount`, `demand_slowdown_flag`, `end_market_id`
- `machinery.power.fact_overcapacity_risk`: `industry_capacity_gigawatts`, `overcapacity_flag`, `capacity_horizon_id`, `end_market_id`
- `machinery.market.dim_end_market`: `market_code`

### Q4 2025 (4) — Battery storage beside reciprocating engines on one project

Project content is one row per power product on the project, so battery storage and the reciprocating engine are separate amounts.

- `machinery.power.fact_project_content`: `content_amount`, `content_units`, `project_id`, `power_product_id`, `end_market_id`
- `machinery.power.dim_project`: `project_name`
- `machinery.product.dim_power_product`: `product_code`
- `machinery.market.dim_end_market`: `market_code`

### Q4 2025 (5) — Backup diesel versus battery storage in prime-power designs

Role share by companion product and horizon year shows how backup diesel and battery storage evolve for prime power.

- `machinery.power.fact_backup_role_evolution`: `role_share`, `power_application_id`, `power_product_id`, `capacity_horizon_id`
- `machinery.power.dim_power_application`: `application_code`
- `machinery.product.dim_power_product`: `product_code`
- `machinery.power.dim_capacity_horizon`: `horizon_year`

### Q4 2025 (7) — Utility conversations on turbines in plant applications

The utility customer, the turbine, the plant-application use case, and whether the conversation has become an order are on the conversation fact.

- `machinery.power.fact_utility_conversation`: `use_case_code`, `order_timing_status`, `customer_id`, `power_product_id`, `end_market_id`
- `machinery.power.dim_customer`: `customer_name`, `customer_role`
- `machinery.product.dim_power_product`: `product_code`
- `machinery.market.dim_end_market`: `market_code`

### Q4 2025 (8) — Engine waste heat for cooling versus combined-cycle efficiency

Each architecture has its own efficiency index at the data-center end market.

- `machinery.power.fact_site_energy_comparison`: `efficiency_index`, `generation_architecture_id`, `end_market_id`, `power_product_id`
- `machinery.power.dim_generation_architecture`: `architecture_code`, `architecture_name`
- `machinery.market.dim_end_market`: `market_code`

### Q4 2025 (9) — Construction Industries replacement demand versus data-center activity

Demand amount by driver separates replacement from data-center activity inside Construction Industries.

- `machinery.power.fact_construction_driver_mix`: `demand_amount`, `demand_driver_id`, `segment_id`, `end_market_id`, `accounting_period_id`
- `machinery.market.dim_demand_driver`: `driver_code`, `driver_name`
- `machinery.market.dim_segment`: `segment_code`
- `machinery.market.dim_end_market`: `market_code`

### Q4 2024 (1) — Whether the data-center demand view changed as capacity was added

The outlook change is the demand fact. Gigawatts being added are the capacity ramp.

- `machinery.power.fact_data_center_demand`: `demand_outlook_change`, `demand_outlook_amount`, `demand_slowdown_flag`
- `machinery.power.fact_engine_capacity_ramp`: `ramp_gigawatts`, `capacity_online_units`, `capacity_horizon_id`
- `machinery.market.dim_end_market`: `market_code`

### Q4 2024 (4) — Solar turbine lead times and whether more factory capacity is needed

Lead time in months and the additional-roofline flag are the Solar lead-time fact. The product code selects the Solar turbine.

- `machinery.power.fact_solar_lead_time`: `lead_time_months`, `additional_roofline_needed_flag`, `power_product_id`, `accounting_period_id`
- `machinery.product.dim_power_product`: `product_code`, `product_name`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `machinery.market.dim_segment` | Q2 2026 (3), Q2 2026 (9), Q1 2026 (4), Q4 2025 (9) |
| `machinery.market.dim_end_market` | Q2 2026 (11), Q1 2026 (1), Q4 2025 (2), Q4 2025 (4), Q4 2025 (7), Q4 2025 (8), Q4 2025 (9), Q4 2024 (1) |
| `machinery.market.dim_demand_driver` | Q4 2025 (9) |
| `machinery.product.dim_product_family` | supporting population |
| `machinery.product.dim_machine_model` | supporting population |
| `machinery.product.dim_power_product` | Q2 2026 (1), Q2 2026 (6), Q2 2026 (11), Q1 2026 (1), Q1 2026 (3), Q1 2026 (5), Q4 2025 (4), Q4 2025 (5), Q4 2025 (7), Q4 2024 (4) |
| `machinery.power.dim_power_application` | Q2 2026 (6), Q1 2026 (5), Q4 2025 (5) |
| `machinery.power.dim_workload` | Q2 2026 (11) |
| `machinery.power.dim_site_connection` | Q2 2026 (11) |
| `machinery.power.dim_supplier` | Q1 2026 (5) |
| `machinery.power.dim_project` | Q4 2025 (4) |
| `machinery.power.dim_customer` | Q4 2025 (7) |
| `machinery.power.dim_generation_architecture` | Q4 2025 (8) |
| `machinery.power.dim_capacity_horizon` | Q2 2026 (1), Q2 2026 (6), Q2 2026 (9), Q1 2026 (4), Q1 2026 (5), Q4 2025 (2), Q4 2025 (5) |
| `machinery.power.fact_gigawatt_target` | Q2 2026 (1), Q1 2026 (4) |
| `machinery.power.fact_engine_capacity_ramp` | Q2 2026 (1), Q2 2026 (3), Q4 2025 (2), Q4 2024 (1) |
| `machinery.power.fact_capacity_timing` | Q1 2026 (1) |
| `machinery.power.fact_application_slots` | Q2 2026 (6) |
| `machinery.power.fact_prime_backup_split` | Q1 2026 (5) |
| `machinery.power.fact_redundancy_design` | Q2 2026 (11) |
| `machinery.power.fact_aftermarket_service` | Q2 2026 (9) |
| `machinery.power.fact_installed_base_entry` | Q2 2026 (9) |
| `machinery.power.fact_project_content` | Q4 2025 (4) |
| `machinery.power.fact_utility_conversation` | Q4 2025 (7) |
| `machinery.power.fact_site_energy_comparison` | Q4 2025 (8) |
| `machinery.power.fact_construction_driver_mix` | Q4 2025 (9) |
| `machinery.power.fact_supplier_bottleneck` | Q1 2026 (5) |
| `machinery.power.fact_data_center_demand` | Q4 2025 (2), Q4 2024 (1) |
| `machinery.power.fact_overcapacity_risk` | Q4 2025 (2) |
| `machinery.power.fact_turbine_versus_recip` | Q1 2026 (3) |
| `machinery.power.fact_solar_lead_time` | Q4 2024 (4) |
| `machinery.power.fact_backup_role_evolution` | Q4 2025 (5) |
