# Wafer Tool Inc supply slice

This slice is part of the Wafer Tool Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q3 FY2026 (5) — Applied Materials

For Applied Materials, ICAPS was guided flat to slightly up; outside China, auto, industrial, and analog customers are talking about a cyclical recovery and tight supply, so is that guide still right?

- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.supply.fact_spares_inventory`: `spares_inventory_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `geography_id`, `spare_part_count`, `spare_part_shipment_count`
- `wafertool.supply.fact_cleanroom_capacity`: `cleanroom_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `geography_id`, `tool_family_id`, `cleanroom_area_square_feet`, `system_bay_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (7) — Applied Materials

For Applied Materials, What revenue growth and operating margin are targeted if wafer-fab equipment spending reaches about $150 billion?

- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.price.fact_backlog_revenue`: `backlog_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `customer_type_id`, `backlog_revenue_amount`
- `wafertool.price.fact_spares_revenue`: `spares_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `revenue_line_id`, `spares_revenue_amount`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (4) — Applied Materials

For Applied Materials, Besides node migrations and greenfield fabs, how are customers using existing footprints, and what does that mean for upgrades versus new tools?

- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.supply.fact_spares_inventory`: `spares_inventory_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `geography_id`, `spare_part_count`, `spare_part_shipment_count`
- `wafertool.supply.fact_cleanroom_capacity`: `cleanroom_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `geography_id`, `tool_family_id`, `cleanroom_area_square_feet`, `system_bay_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (1) — Applied Materials

For Applied Materials, Where does the 2026 wafer-fab equipment view sit versus peer ranges from the low teens to about 22%, and how does the company's own above-20% equipment growth compare?

- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.supply.fact_installed_base`: `installed_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `geography_id`, `customer_type_id`, `installed_tool_count`, `tool_under_contract_count`
- `wafertool.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `tool_family_id`, `geography_id`, `system_capacity_count`, `factory_output_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (5) — Applied Materials

For Applied Materials, If the semiconductor industry reaches $1 trillion sooner than expected, does wafer-fab equipment intensity stay near 15%, which would support about $150 billion of equipment?

- `wafertool.supply.fact_service_capacity`: `service_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `employee_group_id`, `geography_id`, `service_type_id`, `field_engineer_count`, `supported_tool_count`
- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.supply.fact_installed_base`: `installed_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `geography_id`, `customer_type_id`, `installed_tool_count`, `tool_under_contract_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (6) — Applied Materials

For Applied Materials, What drives the second-half acceleration if memory cleanroom space stays constrained until the following year: foundry and logic space, or something else?

- `wafertool.supply.fact_cleanroom_capacity`: `cleanroom_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `geography_id`, `tool_family_id`, `cleanroom_area_square_feet`, `system_bay_count`
- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.fact_system_shipments`: `system_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `deposition_type_id`, `etch_type_id`, `customer_type_id`, `geography_id`, `node_generation_id`, `system_shipment_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (7) — Applied Materials

For Applied Materials, With systems growing and utilization rising, why wouldn't services grow faster given value-added attach on a large installed base?

- `wafertool.supply.fact_installed_base`: `installed_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `geography_id`, `customer_type_id`, `installed_tool_count`, `tool_under_contract_count`
- `wafertool.supply.fact_contract_coverage`: `contract_coverage_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_contract_id`, `process_type_id`, `contract_covered_tool_count`
- `wafertool.supply.fact_tool_age_profile`: `tool_age_profile_record_id`, `fiscal_quarter_id`, `scenario_id`, `tool_age_id`, `tool_family_id`, `aged_tool_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (9) — Applied Materials

For Applied Materials, Before greenfield memory capacity arrives, how much of the near-term work is node conversion to squeeze out more bits from existing lines?

- `wafertool.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `tool_family_id`, `geography_id`, `system_capacity_count`, `factory_output_count`
- `wafertool.supply.fact_workforce_capacity`: `workforce_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `employee_group_id`, `geography_id`, `employee_count`, `open_role_count`
- `wafertool.supply.fact_service_capacity`: `service_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `employee_group_id`, `geography_id`, `service_type_id`, `field_engineer_count`, `supported_tool_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (4) — Applied Materials

For Applied Materials, Can wafer-fab equipment grow high single digits to near double digits next year, and can Applied outgrow that if fiscal 2026 mix is favorable and the back half is much stronger?

- `wafertool.supply.fact_backlog`: `backlog_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `customer_type_id`, `backlog_system_count`, `backlog_week_count`
- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.supply.fact_installed_base`: `installed_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `geography_id`, `customer_type_id`, `installed_tool_count`, `tool_under_contract_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (3) — Lam Research

For Lam Research, If outside forecasts call for NAND oversupply next year from weaker consumer demand while DRAM stays short, how does that sit with NAND revenue doubling on AI storage demand?

- `wafertool.supply.fact_installed_base`: `installed_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `geography_id`, `customer_type_id`, `installed_tool_count`, `tool_under_contract_count`
- `wafertool.supply.fact_backlog`: `backlog_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `customer_type_id`, `backlog_system_count`, `backlog_week_count`
- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (5) — Lam Research

For Lam Research, What are current lead times, and if second-half wafer-fab equipment spending moves above the low-$150-billion view, can shipments cover that upside?

- `wafertool.supply.fact_backlog`: `backlog_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `customer_type_id`, `backlog_system_count`, `backlog_week_count`
- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.supply.fact_spares_inventory`: `spares_inventory_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `geography_id`, `spare_part_count`, `spare_part_shipment_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (9) — Lam Research

For Lam Research, Are cleanrooms the binding limit on 2027, and how large could the year be if cleanroom space were not the constraint?

- `wafertool.supply.fact_cleanroom_capacity`: `cleanroom_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `geography_id`, `tool_family_id`, `cleanroom_area_square_feet`, `system_bay_count`
- `wafertool.supply.fact_spares_inventory`: `spares_inventory_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `geography_id`, `spare_part_count`, `spare_part_shipment_count`
- `wafertool.supply.fact_installed_base`: `installed_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `geography_id`, `customer_type_id`, `installed_tool_count`, `tool_under_contract_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (1) — Lam Research

For Lam Research, Are customer discussions for 2027 already locking delivery slots beyond 18 to 24 months, and how is the supply chain being prepared for that?

- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.supply.fact_spares_inventory`: `spares_inventory_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `geography_id`, `spare_part_count`, `spare_part_shipment_count`
- `wafertool.supply.fact_cleanroom_capacity`: `cleanroom_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `geography_id`, `tool_family_id`, `cleanroom_area_square_feet`, `system_bay_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (6) — Lam Research

For Lam Research, Of the wafer-fab equipment uptick, which products carry the most incremental leverage, including advanced packaging?

- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.supply.fact_installed_base`: `installed_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `geography_id`, `customer_type_id`, `installed_tool_count`, `tool_under_contract_count`
- `wafertool.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `tool_family_id`, `geography_id`, `system_capacity_count`, `factory_output_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (8) — Lam Research

For Lam Research, Of the move in the wafer-fab equipment view from about $135 billion to $140 billion-plus, was the larger driver NAND, CPU tightness, or AI strength?

- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.supply.fact_installed_base`: `installed_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `geography_id`, `customer_type_id`, `installed_tool_count`, `tool_under_contract_count`
- `wafertool.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `tool_family_id`, `geography_id`, `system_capacity_count`, `factory_output_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (1) — Lam Research

For Lam Research, How much is calendar 2026 wafer-fab equipment held down by fab readiness relative to a spending level implied by semiconductor revenue?

- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.supply.fact_installed_base`: `installed_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `geography_id`, `customer_type_id`, `installed_tool_count`, `tool_under_contract_count`
- `wafertool.supply.fact_backlog`: `backlog_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `customer_type_id`, `backlog_system_count`, `backlog_week_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (2) — Lam Research

For Lam Research, As Malaysia ramps, how should that supply-chain work show up in gross margin while revenue grows in 2026 and after?

- `wafertool.supply.fact_workforce_capacity`: `workforce_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `employee_group_id`, `geography_id`, `employee_count`, `open_role_count`
- `wafertool.supply.fact_installed_base`: `installed_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `geography_id`, `customer_type_id`, `installed_tool_count`, `tool_under_contract_count`
- `wafertool.supply.fact_backlog`: `backlog_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `customer_type_id`, `backlog_system_count`, `backlog_week_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (4) — Lam Research

For Lam Research, With wafer-fab equipment guided up about 23% after a point of share gain last year, does share hold or rise, what are the puts and takes by market, and what China contribution is assumed?

- `wafertool.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `tool_family_id`, `geography_id`, `system_capacity_count`, `factory_output_count`
- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.supply.fact_spares_inventory`: `spares_inventory_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `geography_id`, `spare_part_count`, `spare_part_shipment_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (6) — Lam Research

For Lam Research, As customers add onshore fabs, does Lam ship more from a manufacturing footprint that has doubled in four years, or keep the current geographic mix?

- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.supply.fact_chamber_capacity`: `chamber_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `tool_family_id`, `process_type_id`, `chamber_capacity_count`
- `wafertool.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `tool_family_id`, `geography_id`, `system_capacity_count`, `factory_output_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (8) — Lam Research

For Lam Research, After customers were caught short of GPU, XPU, CPU, and memory capacity, how much of the sudden demand is still unfilled in the equipment pipeline?

- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `tool_family_id`, `geography_id`, `system_capacity_count`, `factory_output_count`
- `wafertool.supply.fact_service_capacity`: `service_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `employee_group_id`, `geography_id`, `service_type_id`, `field_engineer_count`, `supported_tool_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (1) — Lam Research

For Lam Research, Over the prior six to eight weeks, have AI infrastructure announcements turned into expedited customer meetings and actual orders, or only into longer-dated visibility?

- `wafertool.supply.fact_backlog`: `backlog_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `customer_type_id`, `backlog_system_count`, `backlog_week_count`
- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.fact_system_shipments`: `system_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `deposition_type_id`, `etch_type_id`, `customer_type_id`, `geography_id`, `node_generation_id`, `system_shipment_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (3) — Lam Research

For Lam Research, Of data-center spending, how much is semiconductors, and how does wafer-fab equipment intensity in an AI data center compare with a mid-teens intensity for the industry overall?

- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.supply.fact_installed_base`: `installed_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `geography_id`, `customer_type_id`, `installed_tool_count`, `tool_under_contract_count`
- `wafertool.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `tool_family_id`, `geography_id`, `system_capacity_count`, `factory_output_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (5) — Lam Research

For Lam Research, With NAND utilization heading toward full and cleanroom space limited, should a quarter or more of constraint be assumed before new fabs add bits?

- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.supply.fact_cleanroom_capacity`: `cleanroom_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `geography_id`, `tool_family_id`, `cleanroom_area_square_feet`, `system_bay_count`
- `wafertool.supply.fact_installed_base`: `installed_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `geography_id`, `customer_type_id`, `installed_tool_count`, `tool_under_contract_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (8) — Lam Research

For Lam Research, Are customer engagements accelerating on newer products such as Akara and ALTUS Halo as wafer-fab equipment momentum improves?

- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.supply.fact_spares_inventory`: `spares_inventory_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `geography_id`, `spare_part_count`, `spare_part_shipment_count`
- `wafertool.supply.fact_cleanroom_capacity`: `cleanroom_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `geography_id`, `tool_family_id`, `cleanroom_area_square_feet`, `system_bay_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
