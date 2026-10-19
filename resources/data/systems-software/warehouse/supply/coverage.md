# Platform Inc supply slice

This slice is part of the Platform Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q4 FY2026 (3) — Microsoft

What is driving Azure’s acceleration into the mid-40s, and is that still the same capacity-constrained environment or better execution inside those constraints?

- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`
- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `platform.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`

### Q4 FY2026 (4) — Microsoft

How is Microsoft protected if the industry overbuilds data centers or chips?

- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_compute_capacity`: `compute_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_type_id`, `data_center_region_id`, `server_unit_quantity`, `gpu_unit_quantity`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`
- `platform.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`

### Q2 FY2026 (4) — Microsoft

How large are the capacity additions coming online in coming quarters at sites such as Fairwater Atlanta and Fairwater Wisconsin, regardless of first-party versus third-party allocation?

- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.price.fact_capital_spending_sw`: `capital_spending_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `capacity_type_id`, `capital_spending_amount`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.price.fact_subscription_revenue`: `subscription_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `subscription_revenue_amount`
- `platform.price.fact_enterprise_revenue_sw`: `enterprise_revenue_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`

### Q4 2025 (4) — ServiceNow

Does security still need acquisitions on the scale of Armis to expand the addressable market, or is further expansion expected to be organic?

- `platform.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`
- `platform.demand.dim_acquisition_type`: `acquisition_type_id`, `acquisition_type_code`, `acquisition_type_name`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`

### Q3 2025 (2) — ServiceNow

How much extra caution is in the outlook because the federal government was still closed, relative to the view 90 days earlier?

- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`

### Q3 2025 (8) — ServiceNow

Is Control Tower bought at the start of an AI program or only after a maturity threshold, and how large can that ramp be?

- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `platform.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`

### Q2 2025 (10) — ServiceNow

If the Moveworks close slips, when would ServiceNow hire sales capacity more aggressively so ramped reps are in place?

- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_capital_spending_sw`: `capital_spending_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `capacity_type_id`, `capital_spending_amount`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.supply.fact_data_center_capacity`: `data_center_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `capacity_megawatt_quantity`, `available_megawatt_quantity`
- `platform.supply.fact_compute_capacity`: `compute_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_type_id`, `data_center_region_id`, `server_unit_quantity`, `gpu_unit_quantity`
- `platform.supply.fact_support_capacity`: `support_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `support_tier_id`, `reporting_unit_id`, `support_case_quantity`
