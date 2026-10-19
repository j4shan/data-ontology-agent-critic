# Chip Inc demand slice

This slice is part of the Chip Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q3 FY2026 (1) — Broadcom

For Broadcom, How large is the maximum off-balance-sheet exposure on each subsequent backstop tranche relative to the first tranche already disclosed?

- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.fact_networking_shipments`: `networking_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `switch_shipment_count`, `network_port_count`
- `chip.demand.fact_graphics_shipments`: `graphics_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `sales_channel_id`, `graphics_processor_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (1) — Broadcom

For Broadcom, After the long-term Google agreement, how should share at that customer be thought about?

- `chip.demand.fact_data_center_demand`: `data_center_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `data_center_gigawatt_quantity`, `accelerator_demand_count`
- `chip.demand.fact_customer_concentration`: `customer_concentration_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `product_family_id`, `active_customer_count`, `customer_unit_count`
- `chip.price.fact_networking_revenue`: `networking_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `networking_revenue_amount`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (3) — Broadcom

For Broadcom, Does a higher industry value per gigawatt change the prior view of the custom-compute opportunity into 2027?

- `chip.demand.fact_data_center_demand`: `data_center_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `data_center_gigawatt_quantity`, `accelerator_demand_count`
- `chip.price.fact_content_per_gigawatt`: `content_per_gigawatt_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `revenue_per_gigawatt_amount`
- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (5) — Broadcom

For Broadcom, Are next year's gigawatt shipment targets still about 10, unchanged from last quarter, and how is that volume shaped through the year?

- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.price.fact_content_per_gigawatt`: `content_per_gigawatt_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `revenue_per_gigawatt_amount`
- `chip.demand.fact_networking_shipments`: `networking_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `switch_shipment_count`, `network_port_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (7) — Broadcom

For Broadcom, Will more model-company deals be structured with Broadcom chips as a backstop, as in the Anthropic arrangement, and how might financing of those deals evolve?

- `chip.demand.fact_customer_concentration`: `customer_concentration_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `product_family_id`, `active_customer_count`, `customer_unit_count`
- `chip.price.fact_software_pricing_revenue`: `software_pricing_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `pricing_model_id`, `software_product_id`, `pricing_model_revenue_amount`
- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (8) — Broadcom

For Broadcom, Is there appetite to take on smaller XPU-attached programs in interconnect and storage, beyond the very large platforms?

- `chip.demand.fact_interconnect_demand`: `interconnect_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `interconnect_id`, `geography_id`, `interconnect_activity_count`
- `chip.demand.fact_interconnect_shipments`: `interconnect_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `interconnect_id`, `product_family_id`, `interconnect_link_count`
- `chip.supply.fact_software_capacity`: `software_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `software_product_id`, `supported_subscription_count`, `platform_release_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (9) — Broadcom

For Broadcom, Is generative AI changing infrastructure-software growth and renewals, and what is the longer-term growth path for that business?

- `chip.demand.fact_software_demand`: `software_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `software_product_id`, `customer_type_id`, `subscription_count`, `licensed_seat_count`
- `chip.price.fact_software_revenue`: `software_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `software_product_id`, `customer_type_id`, `software_revenue_amount`
- `chip.demand.fact_sovereign_demand`: `sovereign_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `product_family_id`, `sovereign_gigawatt_quantity`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (10) — Broadcom

For Broadcom, Do large out-year gigawatt commitments from consumer AI labs, plus Google offering cloud access to other accelerators, open custom-XPU demand to smaller customers that would not build their own chips?

- `chip.demand.fact_data_center_demand`: `data_center_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `data_center_gigawatt_quantity`, `accelerator_demand_count`
- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.fact_customer_concentration`: `customer_concentration_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `product_family_id`, `active_customer_count`, `customer_unit_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (4) — Broadcom

For Broadcom, How does separating prefill and decode in the GPU world change demand and mix for custom silicon?

- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.fact_data_center_demand`: `data_center_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `data_center_gigawatt_quantity`, `accelerator_demand_count`
- `chip.demand.fact_customer_concentration`: `customer_concentration_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `product_family_id`, `active_customer_count`, `customer_unit_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (5) — Broadcom

For Broadcom, How do the gigawatts by customer add up to substantially more than $100 billion next year?

- `chip.demand.fact_data_center_demand`: `data_center_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `data_center_gigawatt_quantity`, `accelerator_demand_count`
- `chip.demand.fact_customer_concentration`: `customer_concentration_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `product_family_id`, `active_customer_count`, `customer_unit_count`
- `chip.demand.fact_sovereign_demand`: `sovereign_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `product_family_id`, `sovereign_gigawatt_quantity`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (6) — Broadcom

For Broadcom, Of the Anthropic program cited at about $20 billion for a gigawatt this year, how much is chips versus rack, and is rack inside the $100 billion chip figure?

- `chip.demand.fact_data_center_demand`: `data_center_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `data_center_gigawatt_quantity`, `accelerator_demand_count`
- `chip.demand.fact_sovereign_demand`: `sovereign_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `product_family_id`, `sovereign_gigawatt_quantity`
- `chip.price.fact_content_per_gigawatt`: `content_per_gigawatt_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `revenue_per_gigawatt_amount`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (7) — Broadcom

For Broadcom, Why do customers stay on direct-attached copper through 400-gigabit SerDes rather than moving off that interconnect?

- `chip.demand.fact_end_market_bridge`: `end_market_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `end_market_id`, `end_market_unit_count`
- `chip.demand.fact_data_center_demand`: `data_center_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `data_center_gigawatt_quantity`, `accelerator_demand_count`
- `chip.demand.fact_customer_concentration`: `customer_concentration_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `product_family_id`, `active_customer_count`, `customer_unit_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (1) — Broadcom

For Broadcom, If TPUs are sold more broadly to other customers, does that substitute for ASICs those customers would otherwise have built?

- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.fact_data_center_demand`: `data_center_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `data_center_gigawatt_quantity`, `accelerator_demand_count`
- `chip.demand.fact_customer_concentration`: `customer_concentration_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `product_family_id`, `active_customer_count`, `customer_unit_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (4) — Broadcom

For Broadcom, How does custom-silicon content grow from generation to generation, and how does a competitor's context-specific accelerator change that?

- `chip.demand.fact_architecture_shipments`: `architecture_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `architecture_generation_id`, `product_family_id`, `architecture_accelerator_count`
- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.fact_data_center_demand`: `data_center_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `data_center_gigawatt_quantity`, `accelerator_demand_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2027 (3) — Nvidia

For Nvidia, Which products account for the step-up in the fiscal 2028 growth view versus the prior multi-year outlook, including Vera, CPUs, and related platforms?

- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.fact_workload_bridge`: `workload_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `workload_id`, `workload_accelerator_count`
- `chip.demand.fact_end_market_bridge`: `end_market_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `end_market_id`, `end_market_unit_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2027 (4) — Nvidia

For Nvidia, Does the rise of open models add or subtract from compute demand relative to closed frontier models that still drive a large share of end consumption?

- `chip.demand.fact_end_market_bridge`: `end_market_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `end_market_id`, `end_market_unit_count`
- `chip.price.fact_software_pricing_revenue`: `software_pricing_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `pricing_model_id`, `software_product_id`, `pricing_model_revenue_amount`
- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2027 (5) — Nvidia

For Nvidia, If recursive self-improvement and more agentic systems take hold, does industry demand inflect further beyond the already stated 100% demand growth?

- `chip.demand.fact_deployment_demand`: `deployment_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `deployment_type_id`, `product_family_id`, `deployment_system_count`
- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.fact_networking_shipments`: `networking_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `switch_shipment_count`, `network_port_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (1) — Nvidia

For Nvidia, Why was data-center reporting split, how do the two segments differ competitively, and how does the surprising CPU result sit across them?

- `chip.demand.fact_data_center_demand`: `data_center_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `data_center_gigawatt_quantity`, `accelerator_demand_count`
- `chip.price.fact_content_per_gigawatt`: `content_per_gigawatt_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `revenue_per_gigawatt_amount`
- `chip.supply.fact_cooling_capacity`: `cooling_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `cooling_type_id`, `product_family_id`, `cooled_system_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (2) — Nvidia

For Nvidia, How should data-center growth, excluding China, be read against hyperscaler capital spending that is also expected to roughly double, and against a multi-trillion data-center end market?

- `chip.demand.fact_data_center_demand`: `data_center_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `data_center_gigawatt_quantity`, `accelerator_demand_count`
- `chip.supply.fact_cooling_capacity`: `cooling_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `cooling_type_id`, `product_family_id`, `cooled_system_count`
- `chip.supply.fact_system_capacity`: `system_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `geography_id`, `system_assembly_capacity_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (3) — Nvidia

For Nvidia, How does Vera Rubin and extreme co-design change Nvidia's share of inference into late 2026 and 2027 as frontier models and workload techniques change?

- `chip.demand.fact_workload_bridge`: `workload_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `workload_id`, `workload_accelerator_count`
- `chip.price.fact_software_pricing_revenue`: `software_pricing_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `pricing_model_id`, `software_product_id`, `pricing_model_revenue_amount`
- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (4) — Nvidia

For Nvidia, How much traction are the more specialized CPX and LPX products getting, given a view that a slice of the market is inference-specific rather than a full platform?

- `chip.demand.fact_end_market_bridge`: `end_market_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `end_market_id`, `end_market_unit_count`
- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.fact_workload_bridge`: `workload_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `workload_id`, `workload_accelerator_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (6) — Nvidia

For Nvidia, Are neoclouds reported in hyperscale or in the AI-cloud portion of ACIE, and how large are the two segments relative to each other?

- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.fact_software_demand`: `software_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `software_product_id`, `customer_type_id`, `subscription_count`, `licensed_seat_count`
- `chip.supply.fact_software_capacity`: `software_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `software_product_id`, `supported_subscription_count`, `platform_release_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (7) — Nvidia

For Nvidia, Of the items left out of the trillion-dollar Blackwell and Rubin visibility, is the Vera CPU the largest upside versus LPX, Rubin CPX, and Vera racks?

- `chip.demand.fact_customer_concentration`: `customer_concentration_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `product_family_id`, `active_customer_count`, `customer_unit_count`
- `chip.demand.fact_cpu_shipments`: `cpu_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `cpu_shipment_count`
- `chip.supply.fact_packaging_output`: `packaging_output_record_id`, `fiscal_quarter_id`, `scenario_id`, `packaging_type_id`, `product_family_id`, `packaged_chip_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (1) — Nvidia

For Nvidia, How confident is management that the largest cloud customers can keep growing capital spending into next year as their cash generation is pressured, and can Nvidia still grow if that spending does not?

- `chip.demand.fact_workload_bridge`: `workload_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `workload_id`, `workload_accelerator_count`
- `chip.demand.fact_end_market_bridge`: `end_market_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `end_market_id`, `end_market_unit_count`
- `chip.demand.fact_data_center_demand`: `data_center_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `data_center_gigawatt_quantity`, `accelerator_demand_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (2) — Nvidia

For Nvidia, Why does CUDA still matter as more AI investment dollars shift toward inference?

- `chip.demand.fact_workload_bridge`: `workload_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `workload_id`, `workload_accelerator_count`
- `chip.price.fact_semiconductor_revenue`: `semiconductor_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `semiconductor_revenue_amount`
- `chip.price.fact_systems_revenue`: `systems_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `systems_revenue_amount`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (5) — Nvidia

For Nvidia, Did non-hyperscale data-center customers grow faster than hyperscalers, are they running different workloads, and when could they become the larger share?

- `chip.demand.fact_data_center_demand`: `data_center_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `data_center_gigawatt_quantity`, `accelerator_demand_count`
- `chip.price.fact_content_per_gigawatt`: `content_per_gigawatt_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `revenue_per_gigawatt_amount`
- `chip.supply.fact_cooling_capacity`: `cooling_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `cooling_type_id`, `product_family_id`, `cooled_system_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (6) — Nvidia

For Nvidia, Why bring Vera CPUs to market as a standalone product, and is that driven by more heterogeneous workloads?

- `chip.demand.fact_workload_bridge`: `workload_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `workload_id`, `workload_accelerator_count`
- `chip.demand.fact_end_market_bridge`: `end_market_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `end_market_id`, `end_market_unit_count`
- `chip.demand.fact_cpu_shipments`: `cpu_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `cpu_shipment_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (4) — Nvidia

For Nvidia, Where does the share of shipments tied to inference go over the next year, and how large can Rubin CPX be for long-context workloads?

- `chip.demand.fact_workload_bridge`: `workload_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `workload_id`, `workload_accelerator_count`
- `chip.demand.fact_end_market_bridge`: `end_market_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `end_market_id`, `end_market_unit_count`
- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (7) — Nvidia

For Nvidia, Has the role of custom AI ASICs changed given a broader customer set and the Anthropic relationship?

- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.fact_data_center_demand`: `data_center_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `data_center_gigawatt_quantity`, `accelerator_demand_count`
- `chip.demand.fact_customer_concentration`: `customer_concentration_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `product_family_id`, `active_customer_count`, `customer_unit_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
