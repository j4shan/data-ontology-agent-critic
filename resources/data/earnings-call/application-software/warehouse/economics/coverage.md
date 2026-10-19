# App Inc economics slice

Revenue, ARR, RPO/CRPO, margin, pricing-rate, capex and enterprise dollars. Rate facts name their usage or seat denominator fact at a joinable grain.

## Numbered questions

### Q2 FY2027 (4) — Salesforce

For Salesforce, With net-new AOV growth at a four-year high and attrition near a record low, how sticky is the recurring-revenue base from here?

- `app.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`, `operating_income_amount`, `net_income_amount`, `free_cash_flow_amount`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.fact_data_cloud_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `pricing_model_id`, `data_credit_consumption_count`, `record_processed_count`
- `app.adoption.fact_installed_base`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `buyer_industry_id`, `installed_customer_count`, `account_count`
- `app.adoption.fact_renewal_quantity`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `customer_segment_id`, `renewal_account_count`, `attrition_account_count`
- `app.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (2) — Salesforce

For Salesforce, How should agentic work-unit and token consumption translate into revenue when Agentforce ARR lags the usage growth?

- `app.adoption.fact_agentforce_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `customer_segment_id`, `token_consumption_count`, `agentic_work_unit_count`
- `app.economics.fact_agentforce_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `customer_segment_id`, `revenue_per_work_unit_amount`, `revenue_per_token_amount`
- `app.adoption.dim_pricing_model`: `pricing_model_id`, `pricing_model_code`, `pricing_model_name`
- `app.economics.fact_agentforce_economics`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `pricing_model_id`, `agentforce_arr_amount`, `agentforce_revenue_amount`
- `app.economics.fact_usage_pricing_rate`: `fiscal_quarter_id`, `scenario_id`, `pricing_model_id`, `agentforce_product_id`, `price_per_token_amount`, `price_per_work_unit_amount`
- `app.adoption.fact_data_cloud_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `pricing_model_id`, `data_credit_consumption_count`, `record_processed_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (3) — Salesforce

For Salesforce, Why has gross margin not fallen even as token demand has surged?

- `app.adoption.dim_pricing_model`: `pricing_model_id`, `pricing_model_code`, `pricing_model_name`
- `app.adoption.fact_agentforce_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `customer_segment_id`, `token_consumption_count`, `agentic_work_unit_count`
- `app.economics.fact_salesforce_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `salesforce_gross_margin_percent`
- `app.adoption.dim_contract_type`: `contract_type_id`, `contract_type_code`, `contract_type_name`
- `app.adoption.dim_deal_structure`: `deal_structure_id`, `deal_structure_code`, `deal_structure_name`
- `app.adoption.fact_credit_refill_activity`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `credit_refill_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (3) — Salesforce

For Salesforce, How do tokens and agentic work units convert into money under agentic enterprise license agreements, and how does that pricing path affect gross margin?

- `app.adoption.dim_pricing_model`: `pricing_model_id`, `pricing_model_code`, `pricing_model_name`
- `app.economics.fact_usage_pricing_rate`: `fiscal_quarter_id`, `scenario_id`, `pricing_model_id`, `agentforce_product_id`, `price_per_token_amount`, `price_per_work_unit_amount`
- `app.adoption.fact_agentforce_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `customer_segment_id`, `token_consumption_count`, `agentic_work_unit_count`
- `app.economics.fact_agentforce_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `customer_segment_id`, `revenue_per_work_unit_amount`, `revenue_per_token_amount`
- `app.adoption.dim_contract_type`: `contract_type_id`, `contract_type_code`, `contract_type_name`
- `app.adoption.dim_deal_structure`: `deal_structure_id`, `deal_structure_code`, `deal_structure_name`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (3) — Oracle

For Oracle, How is pricing shifting between contracted and spot capacity, and does last year’s gross-margin framework still hold as component prices rise?

- `app.economics.fact_capacity_pricing_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `capacity_type_id`, `contracted_price_per_capacity_unit_amount`, `spot_price_per_capacity_unit_amount`
- `app.adoption.dim_contract_type`: `contract_type_id`, `contract_type_code`, `contract_type_name`
- `app.economics.fact_data_center_economics`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `data_center_cost_amount`, `component_cost_amount`
- `app.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `app.economics.fact_oracle_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `oracle_business_id`, `oracle_gross_margin_percent`
- `app.economics.fact_usage_pricing_rate`: `fiscal_quarter_id`, `scenario_id`, `pricing_model_id`, `agentforce_product_id`, `price_per_token_amount`, `price_per_work_unit_amount`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (4) — Oracle

For Oracle, Who is driving the RPO that does not require more Oracle capital spending — prepaid and bring-your-own-chip deals from AI labs, semiconductor companies, or sovereign buyers?

- `app.adoption.dim_deal_structure`: `deal_structure_id`, `deal_structure_code`, `deal_structure_name`
- `app.delivery.fact_chip_capacity`: `fiscal_quarter_id`, `scenario_id`, `deal_structure_id`, `capacity_type_id`, `chip_unit_count`
- `app.adoption.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `app.delivery.fact_sovereign_capacity`: `fiscal_quarter_id`, `scenario_id`, `oracle_cloud_venue_id`, `customer_segment_id`, `sovereign_region_count`, `dedicated_region_count`
- `app.economics.fact_oracle_rpo`: `fiscal_quarter_id`, `scenario_id`, `oracle_business_id`, `deal_structure_id`, `customer_segment_id`, `remaining_performance_obligation_amount`, `oracle_pipeline_amount`
- `app.economics.fact_sovereign_economics`: `fiscal_quarter_id`, `scenario_id`, `oracle_cloud_venue_id`, `customer_segment_id`, `sovereign_revenue_amount`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (5) — Oracle

For Oracle, How are sovereign cloud and sovereign AI progressing, and what do they do to capital spending and margins?

- `app.adoption.dim_oracle_cloud_venue`: `oracle_cloud_venue_id`, `oracle_cloud_venue_code`, `oracle_cloud_venue_name`
- `app.delivery.fact_sovereign_capacity`: `fiscal_quarter_id`, `scenario_id`, `oracle_cloud_venue_id`, `customer_segment_id`, `sovereign_region_count`, `dedicated_region_count`
- `app.economics.fact_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `capacity_type_id`, `region_id`, `capital_expenditure_amount`
- `app.economics.fact_oracle_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `oracle_business_id`, `oracle_gross_margin_percent`
- `app.economics.fact_sovereign_economics`: `fiscal_quarter_id`, `scenario_id`, `oracle_cloud_venue_id`, `customer_segment_id`, `sovereign_revenue_amount`
- `app.adoption.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (6) — Oracle

For Oracle, Did gross margin fall this quarter because new capacity carried cost before the related revenue started, and how does that margin gap close as those deployments fill?

- `app.economics.fact_oracle_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `oracle_business_id`, `oracle_gross_margin_percent`
- `app.economics.fact_data_center_economics`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `data_center_cost_amount`, `component_cost_amount`
- `app.economics.fact_sovereign_economics`: `fiscal_quarter_id`, `scenario_id`, `oracle_cloud_venue_id`, `customer_segment_id`, `sovereign_revenue_amount`
- `app.adoption.fact_credit_refill_activity`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `credit_refill_count`
- `app.adoption.fact_customer_adoption`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `deployment_stage_id`, `customer_segment_id`, `active_customer_count`, `production_customer_count`
- `app.adoption.fact_oci_consumption`: `fiscal_quarter_id`, `scenario_id`, `oracle_business_id`, `capacity_type_id`, `ai_workload_id`, `oci_consumption_unit_count`, `gpu_hour_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (7) — Oracle

For Oracle, Does the AI data platform show up as extra Oracle Database and OCI consumption, or as a separate software revenue line?

- `app.adoption.fact_oracle_database_usage`: `fiscal_quarter_id`, `scenario_id`, `oracle_product_id`, `oracle_cloud_venue_id`, `database_instance_count`, `database_consumption_unit_count`
- `app.adoption.dim_oracle_product`: `oracle_product_id`, `oracle_product_code`, `oracle_product_name`
- `app.adoption.dim_oracle_business`: `oracle_business_id`, `oracle_business_code`, `oracle_business_name`
- `app.adoption.dim_oracle_cloud_venue`: `oracle_cloud_venue_id`, `oracle_cloud_venue_code`, `oracle_cloud_venue_name`
- `app.adoption.dim_pricing_model`: `pricing_model_id`, `pricing_model_code`, `pricing_model_name`
- `app.adoption.fact_oci_consumption`: `fiscal_quarter_id`, `scenario_id`, `oracle_business_id`, `capacity_type_id`, `ai_workload_id`, `oci_consumption_unit_count`, `gpu_hour_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (1) — Oracle

For Oracle, How are long-term contracts that are not prepaid GPU deals protected when memory and other component costs jump?

- `app.adoption.dim_contract_type`: `contract_type_id`, `contract_type_code`, `contract_type_name`
- `app.adoption.dim_deal_structure`: `deal_structure_id`, `deal_structure_code`, `deal_structure_name`
- `app.economics.fact_contract_economics`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `deal_structure_id`, `contract_value_amount`, `prepaid_contract_amount`
- `app.delivery.fact_chip_capacity`: `fiscal_quarter_id`, `scenario_id`, `deal_structure_id`, `capacity_type_id`, `chip_unit_count`
- `app.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `app.economics.fact_data_center_economics`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `data_center_cost_amount`, `component_cost_amount`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (4) — Oracle

For Oracle, After the debt raise, do AI data-center returns still look acceptable once build cost and the cost of capital are both counted?

- `app.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `app.economics.fact_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `capacity_type_id`, `region_id`, `capital_expenditure_amount`
- `app.economics.fact_data_center_economics`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `data_center_cost_amount`, `component_cost_amount`
- `app.delivery.dim_capacity_type`: `capacity_type_id`, `capacity_type_code`, `capacity_type_name`
- `app.delivery.dim_workforce_group`: `workforce_group_id`, `workforce_group_code`, `workforce_group_name`
- `app.delivery.fact_data_center_capacity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `data_center_count`, `power_megawatt_capacity`, `gpu_unit_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (1) — Oracle

For Oracle, How long will it take AI workload margins across OCI data centers to reach the roughly 30% to 40% range cited over a contract’s life, and what has to happen to get there?

- `app.economics.fact_capacity_pricing_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `capacity_type_id`, `contracted_price_per_capacity_unit_amount`, `spot_price_per_capacity_unit_amount`
- `app.adoption.dim_ai_workload`: `ai_workload_id`, `ai_workload_code`, `ai_workload_name`
- `app.adoption.dim_contract_type`: `contract_type_id`, `contract_type_code`, `contract_type_name`
- `app.adoption.fact_ai_data_platform_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `ai_workload_id`, `ai_query_count`, `private_model_training_count`
- `app.adoption.fact_oci_consumption`: `fiscal_quarter_id`, `scenario_id`, `oracle_business_id`, `capacity_type_id`, `ai_workload_id`, `oci_consumption_unit_count`, `gpu_hour_count`
- `app.delivery.dim_capacity_type`: `capacity_type_id`, `capacity_type_code`, `capacity_type_name`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (3) — Oracle

For Oracle, For a single data center, how does cash flow move from the commitment through hardware purchase to cash-flow positive, and how does that roll up across sites?

- `app.delivery.fact_site_delivery_capacity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `site_under_construction_count`, `planned_site_count`
- `app.delivery.dim_capacity_type`: `capacity_type_id`, `capacity_type_code`, `capacity_type_name`
- `app.delivery.dim_workforce_group`: `workforce_group_id`, `workforce_group_code`, `workforce_group_name`
- `app.delivery.fact_data_center_capacity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `data_center_count`, `power_megawatt_capacity`, `gpu_unit_count`
- `app.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `app.economics.fact_capacity_pricing_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `capacity_type_id`, `contracted_price_per_capacity_unit_amount`, `spot_price_per_capacity_unit_amount`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
