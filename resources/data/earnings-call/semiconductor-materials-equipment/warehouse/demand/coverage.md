# Wafer Tool Inc demand slice

This slice is part of the Wafer Tool Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q3 FY2026 (1) — Applied Materials

For Applied Materials, After a prior frame of semiconductor-systems growth above 30%, what growth outlook is reasonable now, including into calendar 2027?

- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.fact_system_shipments`: `system_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `deposition_type_id`, `etch_type_id`, `customer_type_id`, `geography_id`, `node_generation_id`, `system_shipment_count`
- `wafertool.demand.fact_deposition_shipments`: `deposition_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `deposition_type_id`, `customer_type_id`, `geography_id`, `deposition_system_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (2) — Applied Materials

For Applied Materials, China and global ICAPS are described as flat this year; how has that view changed in three months, when the prior consensus was that China would decline?

- `wafertool.demand.fact_application_bridge`: `application_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `end_application_id`, `customer_type_id`, `process_type_id`, `application_wafer_start_count`
- `wafertool.demand.fact_chamber_demand`: `chamber_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `chamber_demand_count`
- `wafertool.demand.fact_spare_shipments`: `spare_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `spare_category_id`, `service_type_id`, `spare_shipped_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (3) — Applied Materials

For Applied Materials, How does advanced packaging, including high-bandwidth memory packaging and 3D chiplet stacking, compare with last year, and how much of the above-20% growth does it explain?

- `wafertool.demand.fact_packaging_type_demand`: `packaging_type_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `packaging_type_id`, `geography_id`, `packaging_type_activity_count`
- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.fact_system_shipments`: `system_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `deposition_type_id`, `etch_type_id`, `customer_type_id`, `geography_id`, `node_generation_id`, `system_shipment_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (4) — Applied Materials

For Applied Materials, Given the equipment guide, does more than 20% growth imply a roughly $6.5 billion quarterly run rate for the rest of the calendar year?

- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.fact_system_shipments`: `system_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `deposition_type_id`, `etch_type_id`, `customer_type_id`, `geography_id`, `node_generation_id`, `system_shipment_count`
- `wafertool.demand.fact_service_demand`: `service_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_event_count`, `tool_serviced_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (8) — Applied Materials

For Applied Materials, For calendar 2026 and 2027, which grows faster, foundry and logic or DRAM, and does one stay ahead for several quarters?

- `wafertool.demand.fact_application_bridge`: `application_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `end_application_id`, `customer_type_id`, `process_type_id`, `application_wafer_start_count`
- `wafertool.supply.fact_component_supply`: `component_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_id`, `supplier_type_id`, `component_received_count`, `component_on_order_count`
- `wafertool.price.fact_enterprise_results`: `enterprise_results_record_id`, `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`, `operating_income_amount`, `net_income_amount`, `diluted_earnings_per_share`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (1) — Applied Materials

For Applied Materials, After customers were visited, how have near-term equipment conversations changed since the industry started discussing multi-trillion-dollar AI infrastructure spending?

- `wafertool.demand.fact_system_shipments`: `system_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `deposition_type_id`, `etch_type_id`, `customer_type_id`, `geography_id`, `node_generation_id`, `system_shipment_count`
- `wafertool.demand.fact_wafer_starts`: `wafer_starts_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `memory_type_id`, `node_generation_id`, `geography_id`, `wafer_start_count`, `fab_count`
- `wafertool.supply.fact_fab_projects`: `fab_projects_record_id`, `fiscal_quarter_id`, `scenario_id`, `fab_type_id`, `customer_type_id`, `geography_id`, `fab_project_count`, `planned_wafer_capacity_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (2) — Applied Materials

For Applied Materials, As gate-all-around and backside power are gained, where is leadership shifting among PVD, ALD, CVD, CMP, and etch relative to U.S. and Japanese peers?

- `wafertool.demand.fact_service_demand`: `service_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_event_count`, `tool_serviced_count`
- `wafertool.demand.fact_wafer_starts`: `wafer_starts_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `memory_type_id`, `node_generation_id`, `geography_id`, `wafer_start_count`, `fab_count`
- `wafertool.demand.fact_etch_shipments`: `etch_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `etch_type_id`, `customer_type_id`, `geography_id`, `etch_system_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (6) — Applied Materials

For Applied Materials, If domestic China spending falls next year, why would China's share of systems stay around the mid-20s?

- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.fact_system_shipments`: `system_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `deposition_type_id`, `etch_type_id`, `customer_type_id`, `geography_id`, `node_generation_id`, `system_shipment_count`
- `wafertool.demand.fact_deposition_shipments`: `deposition_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `deposition_type_id`, `customer_type_id`, `geography_id`, `deposition_system_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (4) — Lam Research

For Lam Research, Relative to 2026 industry growth, is 2027 likely similar, better, or worse?

- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.fact_system_shipments`: `system_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `deposition_type_id`, `etch_type_id`, `customer_type_id`, `geography_id`, `node_generation_id`, `system_shipment_count`
- `wafertool.demand.fact_service_demand`: `service_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_event_count`, `tool_serviced_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (6) — Lam Research

For Lam Research, As the roughly $40 billion NAND upgrade opportunity is realized faster than expected, how much of it renews when layers already upgraded have to move again?

- `wafertool.demand.fact_upgrade_demand`: `upgrade_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `upgrade_request_count`, `upgrade_completed_count`
- `wafertool.price.fact_spares_revenue`: `spares_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `revenue_line_id`, `spares_revenue_amount`
- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (7) — Lam Research

For Lam Research, Share gains have been concentrated in high-bandwidth memory tools such as through-silicon via and plating; what is the share opportunity in conventional DRAM?

- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.fact_system_shipments`: `system_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `deposition_type_id`, `etch_type_id`, `customer_type_id`, `geography_id`, `node_generation_id`, `system_shipment_count`
- `wafertool.demand.fact_service_demand`: `service_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_event_count`, `tool_serviced_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (8) — Lam Research

For Lam Research, How should etch and deposition spending track total data-center spending if AI outlays slow or models become more efficient?

- `wafertool.demand.fact_deposition_shipments`: `deposition_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `deposition_type_id`, `customer_type_id`, `geography_id`, `deposition_system_count`
- `wafertool.demand.fact_etch_shipments`: `etch_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `etch_type_id`, `customer_type_id`, `geography_id`, `etch_system_count`
- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (3) — Lam Research

For Lam Research, Why would this memory cycle differ from past ones because of high-bandwidth memory, trade ratios, and new AI applications?

- `wafertool.demand.fact_application_bridge`: `application_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `end_application_id`, `customer_type_id`, `process_type_id`, `application_wafer_start_count`
- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.supply.fact_component_supply`: `component_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_id`, `supplier_type_id`, `component_received_count`, `component_on_order_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (4) — Lam Research

For Lam Research, Are lower prepayments a China signal, what is China demand doing, and what is expected over the next few quarters?

- `wafertool.demand.fact_spare_shipments`: `spare_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `spare_category_id`, `service_type_id`, `spare_shipped_count`
- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.fact_system_shipments`: `system_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `deposition_type_id`, `etch_type_id`, `customer_type_id`, `geography_id`, `node_generation_id`, `system_shipment_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (3) — Lam Research

For Lam Research, When does 4F-squared DRAM see volume adoption versus 6F2, and what happens to Lam's available market and share, including Akara, at that transition?

- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.fact_system_shipments`: `system_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `deposition_type_id`, `etch_type_id`, `customer_type_id`, `geography_id`, `node_generation_id`, `system_shipment_count`
- `wafertool.demand.fact_service_demand`: `service_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_event_count`, `tool_serviced_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (5) — Lam Research

For Lam Research, Was the point of share gain mainly in foundry and logic, or across DRAM and NAND as well?

- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.fact_system_shipments`: `system_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `deposition_type_id`, `etch_type_id`, `customer_type_id`, `geography_id`, `node_generation_id`, `system_shipment_count`
- `wafertool.demand.fact_service_demand`: `service_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_event_count`, `tool_serviced_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (7) — Lam Research

For Lam Research, Are customers moving molybdenum ALD from single-wafer to batch tools, and what does that do to Lam?

- `wafertool.demand.fact_system_shipments`: `system_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `deposition_type_id`, `etch_type_id`, `customer_type_id`, `geography_id`, `node_generation_id`, `system_shipment_count`
- `wafertool.demand.fact_wafer_starts`: `wafer_starts_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `memory_type_id`, `node_generation_id`, `geography_id`, `wafer_start_count`, `fab_count`
- `wafertool.demand.fact_application_bridge`: `application_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `end_application_id`, `customer_type_id`, `process_type_id`, `application_wafer_start_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (4) — Lam Research

For Lam Research, Are NAND orders already accelerating with the public infrastructure announcements, or is that still ahead?

- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.fact_spare_shipments`: `spare_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `spare_category_id`, `service_type_id`, `spare_shipped_count`
- `wafertool.supply.fact_backlog`: `backlog_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `customer_type_id`, `backlog_system_count`, `backlog_week_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
