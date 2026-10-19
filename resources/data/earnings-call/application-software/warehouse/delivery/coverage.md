# App Inc delivery slice

Data-center, cloud-region, sales, partner and sovereign capacity facts. Capacity facts store no price.

## Numbered questions

### Q4 FY2026 (4) — Salesforce

For Salesforce, If most bookings are already cross-sell and token upsell, what blocks the remaining installed base from becoming productive on agents this year?

- `app.adoption.fact_cross_sell_quantity`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `agentforce_product_id`, `cross_sell_deal_count`, `multi_cloud_account_count`
- `app.adoption.fact_installed_base`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `buyer_industry_id`, `installed_customer_count`, `account_count`
- `app.economics.fact_account_value_rate`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `buyer_industry_id`, `annual_order_value_per_account_amount`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_pricing_model`: `pricing_model_id`, `pricing_model_code`, `pricing_model_name`
- `app.adoption.fact_agentforce_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `customer_segment_id`, `token_consumption_count`, `agentic_work_unit_count`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (2) — Salesforce

For Salesforce, As the sales force expands, how quickly do the new reps ramp and what productivity should they reach?

- `app.delivery.fact_sales_capacity`: `fiscal_quarter_id`, `scenario_id`, `workforce_group_id`, `region_id`, `sales_rep_count`, `delivery_employee_count`
- `app.delivery.dim_workforce_group`: `workforce_group_id`, `workforce_group_code`, `workforce_group_name`
- `app.delivery.fact_partner_capacity`: `fiscal_quarter_id`, `scenario_id`, `partner_type_id`, `sales_channel_id`, `partner_count`, `certified_consultant_count`
- `app.adoption.dim_agentforce_product`: `agentforce_product_id`, `agentforce_product_code`, `agentforce_product_name`
- `app.adoption.dim_contract_type`: `contract_type_id`, `contract_type_code`, `contract_type_name`
- `app.adoption.dim_deal_structure`: `deal_structure_id`, `deal_structure_code`, `deal_structure_name`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (3) — Salesforce

For Salesforce, What is the competitive advantage of Salesforce’s data and infrastructure layer, now including Informatica, and how does it pull the rest of the company?

- `app.adoption.dim_agentforce_product`: `agentforce_product_id`, `agentforce_product_code`, `agentforce_product_name`
- `app.adoption.fact_cross_sell_quantity`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `agentforce_product_id`, `cross_sell_deal_count`, `multi_cloud_account_count`
- `app.delivery.dim_workforce_group`: `workforce_group_id`, `workforce_group_code`, `workforce_group_name`
- `app.delivery.fact_site_delivery_capacity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `site_under_construction_count`, `planned_site_count`
- `app.adoption.dim_ai_workload`: `ai_workload_id`, `ai_workload_code`, `ai_workload_name`
- `app.adoption.dim_partner_type`: `partner_type_id`, `partner_type_code`, `partner_type_name`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (5) — Salesforce

For Salesforce, Has Agentforce pricing confusion among customers and partners faded as momentum built?

- `app.economics.fact_usage_pricing_rate`: `fiscal_quarter_id`, `scenario_id`, `pricing_model_id`, `agentforce_product_id`, `price_per_token_amount`, `price_per_work_unit_amount`
- `app.adoption.fact_agentforce_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `customer_segment_id`, `token_consumption_count`, `agentic_work_unit_count`
- `app.adoption.fact_data_cloud_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `pricing_model_id`, `data_credit_consumption_count`, `record_processed_count`
- `app.delivery.fact_model_integration_capacity`: `fiscal_quarter_id`, `scenario_id`, `partner_type_id`, `agentforce_product_id`, `model_integration_count`
- `app.economics.fact_agentforce_economics`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `pricing_model_id`, `agentforce_arr_amount`, `agentforce_revenue_amount`
- `app.economics.fact_agentforce_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `customer_segment_id`, `revenue_per_work_unit_amount`, `revenue_per_token_amount`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (6) — Salesforce

For Salesforce, If agents let customers hold or cut headcount, how does Salesforce still grow AOV?

- `app.adoption.dim_agentforce_product`: `agentforce_product_id`, `agentforce_product_code`, `agentforce_product_name`
- `app.adoption.fact_agentforce_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `customer_segment_id`, `token_consumption_count`, `agentic_work_unit_count`
- `app.adoption.fact_cross_sell_quantity`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `agentforce_product_id`, `cross_sell_deal_count`, `multi_cloud_account_count`
- `app.adoption.fact_customer_adoption`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `deployment_stage_id`, `customer_segment_id`, `active_customer_count`, `production_customer_count`
- `app.adoption.fact_installed_base`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `buyer_industry_id`, `installed_customer_count`, `account_count`
- `app.adoption.fact_renewal_quantity`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `customer_segment_id`, `renewal_account_count`, `attrition_account_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (1) — Oracle

For Oracle, If peers keep spending heavily on capacity, could Oracle’s capital-spending peak extend past fiscal 2028 rather than ease after the next two years?

- `app.economics.fact_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `capacity_type_id`, `region_id`, `capital_expenditure_amount`
- `app.delivery.fact_data_center_capacity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `data_center_count`, `power_megawatt_capacity`, `gpu_unit_count`
- `app.delivery.fact_site_delivery_capacity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `site_under_construction_count`, `planned_site_count`
- `app.economics.fact_capacity_pricing_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `capacity_type_id`, `contracted_price_per_capacity_unit_amount`, `spot_price_per_capacity_unit_amount`
- `app.economics.fact_data_center_economics`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `data_center_cost_amount`, `component_cost_amount`
- `app.adoption.fact_oci_consumption`: `fiscal_quarter_id`, `scenario_id`, `oracle_business_id`, `capacity_type_id`, `ai_workload_id`, `oci_consumption_unit_count`, `gpu_hour_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (2) — Oracle

For Oracle, Where do the New Mexico and Wisconsin data centers stand, and could delivery slips put the raised fiscal 2027 revenue outlook or further RPO growth at risk?

- `app.delivery.fact_site_delivery_capacity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `site_under_construction_count`, `planned_site_count`
- `app.delivery.fact_data_center_capacity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `data_center_count`, `power_megawatt_capacity`, `gpu_unit_count`
- `app.economics.fact_capacity_pricing_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `capacity_type_id`, `contracted_price_per_capacity_unit_amount`, `spot_price_per_capacity_unit_amount`
- `app.economics.fact_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `capacity_type_id`, `region_id`, `capital_expenditure_amount`
- `app.economics.fact_data_center_economics`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `data_center_cost_amount`, `component_cost_amount`
- `app.delivery.dim_capacity_type`: `capacity_type_id`, `capacity_type_code`, `capacity_type_name`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (3) — Oracle

For Oracle, How is core database demand trending across OCI and Azure, separate from the AI infrastructure surge?

- `app.adoption.fact_oracle_database_usage`: `fiscal_quarter_id`, `scenario_id`, `oracle_product_id`, `oracle_cloud_venue_id`, `database_instance_count`, `database_consumption_unit_count`
- `app.adoption.dim_oracle_business`: `oracle_business_id`, `oracle_business_code`, `oracle_business_name`
- `app.adoption.dim_oracle_cloud_venue`: `oracle_cloud_venue_id`, `oracle_cloud_venue_code`, `oracle_cloud_venue_name`
- `app.adoption.dim_oracle_product`: `oracle_product_id`, `oracle_product_code`, `oracle_product_name`
- `app.adoption.fact_oci_consumption`: `fiscal_quarter_id`, `scenario_id`, `oracle_business_id`, `capacity_type_id`, `ai_workload_id`, `oci_consumption_unit_count`, `gpu_hour_count`
- `app.economics.fact_database_revenue`: `fiscal_quarter_id`, `scenario_id`, `oracle_product_id`, `oracle_cloud_venue_id`, `database_revenue_amount`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (1) — Oracle

For Oracle, Is the AI-infrastructure halo now showing up in traditional cloud pipeline, including Dedicated Region, sovereign clouds, Alloy, and application deals, even if those deals are smaller than the AI contracts in RPO?

- `app.adoption.dim_oracle_cloud_venue`: `oracle_cloud_venue_id`, `oracle_cloud_venue_code`, `oracle_cloud_venue_name`
- `app.delivery.fact_sovereign_capacity`: `fiscal_quarter_id`, `scenario_id`, `oracle_cloud_venue_id`, `customer_segment_id`, `sovereign_region_count`, `dedicated_region_count`
- `app.adoption.dim_oracle_business`: `oracle_business_id`, `oracle_business_code`, `oracle_business_name`
- `app.adoption.fact_sales_pipeline`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `salesforce_cloud_id`, `region_id`, `pipeline_opportunity_count`, `lead_count`
- `app.economics.fact_oracle_rpo`: `fiscal_quarter_id`, `scenario_id`, `oracle_business_id`, `deal_structure_id`, `customer_segment_id`, `remaining_performance_obligation_amount`, `oracle_pipeline_amount`
- `app.economics.fact_sovereign_economics`: `fiscal_quarter_id`, `scenario_id`, `oracle_cloud_venue_id`, `customer_segment_id`, `sovereign_revenue_amount`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (2) — Oracle

For Oracle, As work shifts toward inference, should new data centers sit closer to users and fiber rather than only next to power in large centralized sites?

- `app.delivery.fact_inference_capacity`: `fiscal_quarter_id`, `scenario_id`, `ai_workload_id`, `region_id`, `inference_site_count`
- `app.delivery.fact_data_center_capacity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `data_center_count`, `power_megawatt_capacity`, `gpu_unit_count`
- `app.delivery.fact_site_delivery_capacity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `site_under_construction_count`, `planned_site_count`
- `app.adoption.dim_ai_workload`: `ai_workload_id`, `ai_workload_code`, `ai_workload_name`
- `app.delivery.dim_capacity_type`: `capacity_type_id`, `capacity_type_code`, `capacity_type_name`
- `app.delivery.dim_workforce_group`: `workforce_group_id`, `workforce_group_code`, `workforce_group_name`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (7) — Oracle

For Oracle, If many vendors want to be the AI interaction layer across enterprise systems, what role does Oracle keep given Agent Studio and the data inside its database and applications?

- `app.adoption.dim_oracle_business`: `oracle_business_id`, `oracle_business_code`, `oracle_business_name`
- `app.adoption.dim_oracle_product`: `oracle_product_id`, `oracle_product_code`, `oracle_product_name`
- `app.adoption.dim_oracle_cloud_venue`: `oracle_cloud_venue_id`, `oracle_cloud_venue_code`, `oracle_cloud_venue_name`
- `app.adoption.dim_partner_type`: `partner_type_id`, `partner_type_code`, `partner_type_name`
- `app.adoption.fact_application_wins`: `fiscal_quarter_id`, `scenario_id`, `oracle_product_id`, `customer_segment_id`, `customer_win_count`, `renewal_count`
- `app.adoption.fact_oracle_database_usage`: `fiscal_quarter_id`, `scenario_id`, `oracle_product_id`, `oracle_cloud_venue_id`, `database_instance_count`, `database_consumption_unit_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (5) — Oracle

For Oracle, Is the combined applications-and-infrastructure selling motion, including merged vertical and horizontal teams, what changes the applications trajectory?

- `app.adoption.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `app.adoption.dim_oracle_business`: `oracle_business_id`, `oracle_business_code`, `oracle_business_name`
- `app.adoption.dim_buyer_industry`: `buyer_industry_id`, `buyer_industry_code`, `buyer_industry_name`
- `app.adoption.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `app.adoption.dim_oracle_product`: `oracle_product_id`, `oracle_product_code`, `oracle_product_name`
- `app.adoption.dim_partner_type`: `partner_type_id`, `partner_type_code`, `partner_type_name`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
