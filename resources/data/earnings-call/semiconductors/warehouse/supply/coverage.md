# Chip Inc supply slice

This slice is part of the Chip Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q3 FY2026 (2) — Broadcom

For Broadcom, How do a richer XPU mix and higher memory cost affect gross margin in fiscal 2027 and 2028, and why would two frontier labs become the largest AI customers while Google remains supply constrained?

- `chip.supply.fact_workforce_capacity`: `workforce_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `employee_group_id`, `employee_count`, `open_role_count`
- `chip.supply.fact_memory_supply`: `memory_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_id`, `supply_source_id`, `memory_stack_count`
- `chip.price.fact_gross_margin`: `gross_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `gross_profit_amount`, `gross_margin_percent`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (3) — Broadcom

For Broadcom, What attach rate should be assumed for Tomahawk Ultra on the ASICs ramping over the next couple of years?

- `chip.supply.fact_backlog`: `backlog_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `backlog_unit_count`, `backlog_week_count`
- `chip.supply.fact_wafer_supply`: `wafer_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `supply_source_id`, `component_id`, `wafer_supply_count`, `component_supply_count`
- `chip.supply.fact_memory_supply`: `memory_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_id`, `supply_source_id`, `memory_stack_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (4) — Broadcom

For Broadcom, Are land, power, and shell the largest constraints into fiscal 2027, and which other supply limits sit behind them?

- `chip.supply.fact_software_capacity`: `software_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `software_product_id`, `supported_subscription_count`, `platform_release_count`
- `chip.supply.fact_wafer_supply`: `wafer_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `supply_source_id`, `component_id`, `wafer_supply_count`, `component_supply_count`
- `chip.supply.fact_memory_supply`: `memory_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_id`, `supply_source_id`, `memory_stack_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (4) — Broadcom

For Broadcom, If a customer asks for more volume, can Broadcom obtain incremental wafers and high-bandwidth memory the way some competitors appear to?

- `chip.supply.fact_memory_supply`: `memory_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_id`, `supply_source_id`, `memory_stack_count`
- `chip.demand.fact_workload_bridge`: `workload_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `workload_id`, `workload_accelerator_count`
- `chip.demand.fact_end_market_bridge`: `end_market_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `end_market_id`, `end_market_unit_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (11) — Broadcom

For Broadcom, Why were AI bookings in the quarter so large relative to near-term shipments if supply can be added when customers ask?

- `chip.supply.fact_wafer_supply`: `wafer_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `supply_source_id`, `component_id`, `wafer_supply_count`, `component_supply_count`
- `chip.supply.fact_memory_supply`: `memory_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_id`, `supply_source_id`, `memory_stack_count`
- `chip.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `geography_id`, `product_family_id`, `packaging_capacity_count`, `test_capacity_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (2) — Broadcom

For Broadcom, Are the follow-on order and the fifth customer's order delivered as an XPU, a rack, or another configuration?

- `chip.supply.fact_backlog`: `backlog_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `backlog_unit_count`, `backlog_week_count`
- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.fact_software_demand`: `software_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `software_product_id`, `customer_type_id`, `subscription_count`, `licensed_seat_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (6) — Broadcom

For Broadcom, How resilient is supply from key materials partners, including co-packaged optics, across existing programs and the two new custom processors?

- `chip.supply.fact_packaging_output`: `packaging_output_record_id`, `fiscal_quarter_id`, `scenario_id`, `packaging_type_id`, `product_family_id`, `packaged_chip_count`
- `chip.supply.fact_wafer_supply`: `wafer_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `supply_source_id`, `component_id`, `wafer_supply_count`, `component_supply_count`
- `chip.supply.fact_memory_supply`: `memory_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_id`, `supply_source_id`, `memory_stack_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2027 (1) — Nvidia

For Nvidia, What gives management confidence to outline about 70% growth a year ahead, which constraint separates that from roughly 100% demand growth, and can that gap close over time?

- `chip.supply.fact_backlog`: `backlog_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `backlog_unit_count`, `backlog_week_count`
- `chip.supply.fact_wafer_supply`: `wafer_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `supply_source_id`, `component_id`, `wafer_supply_count`, `component_supply_count`
- `chip.supply.fact_memory_supply`: `memory_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_id`, `supply_source_id`, `memory_stack_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2027 (2) — Nvidia

For Nvidia, How is inference share expected to move as agentic workloads grow, full-stack value per generation rises, ACIE outgrows hyperscale, and Groq 3 LPX ramps?

- `chip.supply.fact_memory_supply`: `memory_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_id`, `supply_source_id`, `memory_stack_count`
- `chip.supply.fact_wafer_supply`: `wafer_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `supply_source_id`, `component_id`, `wafer_supply_count`, `component_supply_count`
- `chip.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `geography_id`, `product_family_id`, `packaging_capacity_count`, `test_capacity_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2027 (6) — Nvidia

For Nvidia, Which supply bottlenecks are most acute between data-center power and shell, DRAM, and wafer foundry capacity?

- `chip.supply.fact_foundry_capacity`: `foundry_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `supply_source_id`, `product_family_id`, `allocated_wafer_count`
- `chip.supply.fact_process_capacity`: `process_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_node_id`, `supply_source_id`, `process_wafer_capacity_count`
- `chip.supply.fact_cooling_capacity`: `cooling_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `cooling_type_id`, `product_family_id`, `cooled_system_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (8) — Nvidia

For Nvidia, Should the Vera Rubin ramp look like the GB300 ramp, which was described as the fastest in company history, given new silicon in a similar rack?

- `chip.supply.fact_wafer_supply`: `wafer_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `supply_source_id`, `component_id`, `wafer_supply_count`, `component_supply_count`
- `chip.supply.fact_software_capacity`: `software_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `software_product_id`, `supported_subscription_count`, `platform_release_count`
- `chip.supply.fact_foundry_capacity`: `foundry_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `supply_source_id`, `product_family_id`, `allocated_wafer_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (3) — Nvidia

For Nvidia, Does supply visibility into calendar 2027 support holding gross margin in the mid-70s, and are there memory-consumption changes that would protect margin after that?

- `chip.supply.fact_software_capacity`: `software_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `software_product_id`, `supported_subscription_count`, `platform_release_count`
- `chip.price.fact_gross_margin`: `gross_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `gross_profit_amount`, `gross_margin_percent`
- `chip.supply.fact_memory_supply`: `memory_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_id`, `supply_source_id`, `memory_stack_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (2) — Nvidia

For Nvidia, Can supply catch demand within twelve to eighteen months, or does the gap last longer, given sold-out GPUs and the next wave of models?

- `chip.supply.fact_packaging_output`: `packaging_output_record_id`, `fiscal_quarter_id`, `scenario_id`, `packaging_type_id`, `product_family_id`, `packaged_chip_count`
- `chip.supply.fact_wafer_supply`: `wafer_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `supply_source_id`, `component_id`, `wafer_supply_count`, `component_supply_count`
- `chip.supply.fact_memory_supply`: `memory_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_id`, `supply_source_id`, `memory_stack_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (5) — Nvidia

For Nvidia, What is the single largest constraint on growth among power, financing, memory, and foundry?

- `chip.supply.fact_memory_supply`: `memory_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_id`, `supply_source_id`, `memory_stack_count`
- `chip.supply.fact_foundry_capacity`: `foundry_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `supply_source_id`, `product_family_id`, `allocated_wafer_count`
- `chip.supply.fact_process_capacity`: `process_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_node_id`, `supply_source_id`, `process_wafer_capacity_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
