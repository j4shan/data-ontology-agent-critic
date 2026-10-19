# App Inc adoption slice

Seat, usage, adoption, pipeline and booking quantity facts for Salesforce clouds, Agentforce/Data Cloud, and Oracle database, OCI and applications. Quantity facts store no revenue.

## Numbered questions

### Q2 FY2027 (1) — Salesforce

For Salesforce, How will Salesforce and Anthropic take Claude-based Agentforce to customers, including whether the two sales forces sell it together?

- `app.adoption.dim_agentforce_product`: `agentforce_product_id`, `agentforce_product_code`, `agentforce_product_name`
- `app.adoption.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `app.adoption.fact_booking_quantity`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `sales_channel_id`, `booking_count`, `deal_count`
- `app.adoption.fact_cross_sell_quantity`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `agentforce_product_id`, `cross_sell_deal_count`, `multi_cloud_account_count`
- `app.adoption.fact_sales_pipeline`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `salesforce_cloud_id`, `region_id`, `pipeline_opportunity_count`, `lead_count`
- `app.delivery.dim_workforce_group`: `workforce_group_id`, `workforce_group_code`, `workforce_group_name`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2027 (2) — Salesforce

For Salesforce, What share of Agentforce ARR is paid production rather than pilots, and has the path from pilot to paid deployment and credit refill lengthened or shortened?

- `app.adoption.dim_deployment_stage`: `deployment_stage_id`, `deployment_stage_code`, `deployment_stage_name`
- `app.adoption.fact_credit_refill_activity`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `credit_refill_count`
- `app.adoption.fact_agentforce_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `customer_segment_id`, `token_consumption_count`, `agentic_work_unit_count`
- `app.economics.fact_agentforce_economics`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `pricing_model_id`, `agentforce_arr_amount`, `agentforce_revenue_amount`
- `app.adoption.fact_customer_adoption`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `deployment_stage_id`, `customer_segment_id`, `active_customer_count`, `production_customer_count`
- `app.adoption.fact_data_cloud_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `pricing_model_id`, `data_credit_consumption_count`, `record_processed_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2027 (3) — Salesforce

For Salesforce, In a steady state, can Salesforce earn similar ACV from customers on the full Agentforce stack, a headless setup, or the Claude-based offer, and how is headless monetization being set?

- `app.adoption.dim_agentforce_product`: `agentforce_product_id`, `agentforce_product_code`, `agentforce_product_name`
- `app.adoption.fact_agentforce_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `customer_segment_id`, `token_consumption_count`, `agentic_work_unit_count`
- `app.adoption.fact_cross_sell_quantity`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `agentforce_product_id`, `cross_sell_deal_count`, `multi_cloud_account_count`
- `app.adoption.fact_customer_adoption`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `deployment_stage_id`, `customer_segment_id`, `active_customer_count`, `production_customer_count`
- `app.adoption.fact_installed_base`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `buyer_industry_id`, `installed_customer_count`, `account_count`
- `app.adoption.fact_renewal_quantity`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `customer_segment_id`, `renewal_account_count`, `attrition_account_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (1) — Salesforce

For Salesforce, How does a headless CRM expand where Salesforce is used without letting customers or rivals rebuild the value outside Salesforce, and how is that usage monetized?

- `app.adoption.dim_agentforce_product`: `agentforce_product_id`, `agentforce_product_code`, `agentforce_product_name`
- `app.adoption.fact_subscription_seats`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `customer_segment_id`, `buyer_industry_id`, `seat_count`, `active_user_count`
- `app.adoption.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `app.adoption.fact_agentforce_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `customer_segment_id`, `token_consumption_count`, `agentic_work_unit_count`
- `app.adoption.fact_customer_adoption`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `deployment_stage_id`, `customer_segment_id`, `active_customer_count`, `production_customer_count`
- `app.adoption.fact_installed_base`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `buyer_industry_id`, `installed_customer_count`, `account_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (4) — Salesforce

For Salesforce, Is Slack becoming the entry point for broader agentic adoption, and is that showing up in pipeline and second-half agentic bookings?

- `app.adoption.fact_slack_adoption`: `fiscal_quarter_id`, `scenario_id`, `customer_segment_id`, `buyer_industry_id`, `active_slack_user_count`, `slack_message_count`
- `app.economics.fact_slack_revenue`: `fiscal_quarter_id`, `scenario_id`, `customer_segment_id`, `buyer_industry_id`, `slack_revenue_amount`
- `app.adoption.dim_agentforce_product`: `agentforce_product_id`, `agentforce_product_code`, `agentforce_product_name`
- `app.adoption.dim_ai_workload`: `ai_workload_id`, `ai_workload_code`, `ai_workload_name`
- `app.adoption.dim_pricing_model`: `pricing_model_id`, `pricing_model_code`, `pricing_model_name`
- `app.adoption.dim_salesforce_cloud`: `salesforce_cloud_id`, `salesforce_cloud_code`, `salesforce_cloud_name`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (1) — Salesforce

For Salesforce, Can a large, fast-growing Agentforce business coexist with sustained growth in the rest of the portfolio, and what supports a second-half acceleration?

- `app.adoption.dim_agentforce_product`: `agentforce_product_id`, `agentforce_product_code`, `agentforce_product_name`
- `app.adoption.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `app.adoption.fact_agentforce_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `customer_segment_id`, `token_consumption_count`, `agentic_work_unit_count`
- `app.adoption.fact_ai_data_platform_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `ai_workload_id`, `ai_query_count`, `private_model_training_count`
- `app.adoption.fact_credit_refill_activity`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `deployment_stage_id`, `credit_refill_count`
- `app.adoption.fact_cross_sell_quantity`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `agentforce_product_id`, `cross_sell_deal_count`, `multi_cloud_account_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (2) — Salesforce

For Salesforce, Where is the line between partnering with frontier-model providers and competing with them, and where does Salesforce expect to keep the right to win?

- `app.adoption.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `app.adoption.dim_partner_type`: `partner_type_id`, `partner_type_code`, `partner_type_name`
- `app.delivery.fact_model_integration_capacity`: `fiscal_quarter_id`, `scenario_id`, `partner_type_id`, `agentforce_product_id`, `model_integration_count`
- `app.adoption.dim_agentforce_product`: `agentforce_product_id`, `agentforce_product_code`, `agentforce_product_name`
- `app.adoption.fact_ai_data_platform_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `ai_workload_id`, `ai_query_count`, `private_model_training_count`
- `app.adoption.fact_cross_sell_quantity`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `agentforce_product_id`, `cross_sell_deal_count`, `multi_cloud_account_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (1) — Salesforce

For Salesforce, Are large customers actually replacing Salesforce with in-house builds on generative models, or does that differ from what the field is seeing?

- `app.adoption.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `app.adoption.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `app.adoption.fact_application_wins`: `fiscal_quarter_id`, `scenario_id`, `oracle_product_id`, `customer_segment_id`, `customer_win_count`, `renewal_count`
- `app.adoption.fact_competitor_displacement`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `salesforce_cloud_id`, `displacement_evaluation_count`
- `app.adoption.fact_customer_adoption`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `deployment_stage_id`, `customer_segment_id`, `active_customer_count`, `production_customer_count`
- `app.adoption.fact_installed_base`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `buyer_industry_id`, `installed_customer_count`, `account_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (4) — Salesforce

For Salesforce, What halo is Agentforce creating for the other clouds, and what is behind the Slack growth reacceleration?

- `app.adoption.dim_agentforce_product`: `agentforce_product_id`, `agentforce_product_code`, `agentforce_product_name`
- `app.adoption.dim_salesforce_cloud`: `salesforce_cloud_id`, `salesforce_cloud_code`, `salesforce_cloud_name`
- `app.adoption.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `app.adoption.fact_booking_quantity`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `sales_channel_id`, `booking_count`, `deal_count`
- `app.adoption.fact_cross_sell_quantity`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `agentforce_product_id`, `cross_sell_deal_count`, `multi_cloud_account_count`
- `app.adoption.fact_data_cloud_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `pricing_model_id`, `data_credit_consumption_count`, `record_processed_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (7) — Salesforce

For Salesforce, What did the return to basic pipeline and lead follow-up change in the sales pipeline?

- `app.adoption.fact_sales_pipeline`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `salesforce_cloud_id`, `region_id`, `pipeline_opportunity_count`, `lead_count`
- `app.adoption.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `app.adoption.fact_booking_quantity`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `sales_channel_id`, `booking_count`, `deal_count`
- `app.delivery.fact_partner_capacity`: `fiscal_quarter_id`, `scenario_id`, `partner_type_id`, `sales_channel_id`, `partner_count`, `certified_consultant_count`
- `app.adoption.dim_agentforce_product`: `agentforce_product_id`, `agentforce_product_code`, `agentforce_product_name`
- `app.adoption.dim_salesforce_cloud`: `salesforce_cloud_id`, `salesforce_cloud_code`, `salesforce_cloud_name`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (2) — Oracle

For Oracle, As more vendors add AI data-center capacity, what happens to Oracle’s renewals, new-customer wins, and margins?

- `app.adoption.fact_application_wins`: `fiscal_quarter_id`, `scenario_id`, `oracle_product_id`, `customer_segment_id`, `customer_win_count`, `renewal_count`
- `app.delivery.dim_capacity_type`: `capacity_type_id`, `capacity_type_code`, `capacity_type_name`
- `app.delivery.dim_workforce_group`: `workforce_group_id`, `workforce_group_code`, `workforce_group_name`
- `app.delivery.fact_data_center_capacity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `data_center_count`, `power_megawatt_capacity`, `gpu_unit_count`
- `app.delivery.fact_site_delivery_capacity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `site_under_construction_count`, `planned_site_count`
- `app.delivery.fact_sovereign_capacity`: `fiscal_quarter_id`, `scenario_id`, `oracle_cloud_venue_id`, `customer_segment_id`, `sovereign_region_count`, `dedicated_region_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (4) — Oracle

For Oracle, Why did application growth tick down even as named customer wins stayed strong?

- `app.adoption.fact_application_wins`: `fiscal_quarter_id`, `scenario_id`, `oracle_product_id`, `customer_segment_id`, `customer_win_count`, `renewal_count`
- `app.economics.fact_oracle_application_revenue`: `fiscal_quarter_id`, `scenario_id`, `oracle_product_id`, `customer_segment_id`, `oracle_application_revenue_amount`
- `app.adoption.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `app.adoption.dim_oracle_business`: `oracle_business_id`, `oracle_business_code`, `oracle_business_name`
- `app.adoption.dim_oracle_product`: `oracle_product_id`, `oracle_product_code`, `oracle_product_name`
- `app.adoption.fact_customer_adoption`: `fiscal_quarter_id`, `scenario_id`, `salesforce_cloud_id`, `deployment_stage_id`, `customer_segment_id`, `active_customer_count`, `production_customer_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (5) — Oracle

For Oracle, Where can the share of RPO and pipeline that is bring-your-own-hardware or otherwise not a GPU-included deal go, and how does the value of those deals differ from GPU deals?

- `app.adoption.dim_deal_structure`: `deal_structure_id`, `deal_structure_code`, `deal_structure_name`
- `app.delivery.fact_chip_capacity`: `fiscal_quarter_id`, `scenario_id`, `deal_structure_id`, `capacity_type_id`, `chip_unit_count`
- `app.economics.fact_oracle_rpo`: `fiscal_quarter_id`, `scenario_id`, `oracle_business_id`, `deal_structure_id`, `customer_segment_id`, `remaining_performance_obligation_amount`, `oracle_pipeline_amount`
- `app.adoption.dim_oracle_business`: `oracle_business_id`, `oracle_business_code`, `oracle_business_name`
- `app.adoption.fact_oracle_pipeline`: `fiscal_quarter_id`, `scenario_id`, `oracle_business_id`, `deal_structure_id`, `customer_segment_id`, `oracle_pipeline_opportunity_count`
- `app.economics.fact_contract_economics`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `deal_structure_id`, `contract_value_amount`, `prepaid_contract_amount`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (3) — Oracle

For Oracle, Are enterprises asking to train private models on their own data, and is that enough to deliver the AI Database growth inflection described at the analyst day?

- `app.adoption.dim_ai_workload`: `ai_workload_id`, `ai_workload_code`, `ai_workload_name`
- `app.adoption.fact_ai_data_platform_usage`: `fiscal_quarter_id`, `scenario_id`, `agentforce_product_id`, `ai_workload_id`, `ai_query_count`, `private_model_training_count`
- `app.adoption.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `app.adoption.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `app.adoption.dim_deal_structure`: `deal_structure_id`, `deal_structure_code`, `deal_structure_name`
- `app.adoption.dim_pricing_model`: `pricing_model_id`, `pricing_model_code`, `pricing_model_name`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (5) — Oracle

For Oracle, How does the AI data-center business become the AI layer inside sovereign clouds, and what does that add for Oracle?

- `app.adoption.dim_oracle_business`: `oracle_business_id`, `oracle_business_code`, `oracle_business_name`
- `app.adoption.dim_oracle_cloud_venue`: `oracle_cloud_venue_id`, `oracle_cloud_venue_code`, `oracle_cloud_venue_name`
- `app.delivery.fact_sovereign_capacity`: `fiscal_quarter_id`, `scenario_id`, `oracle_cloud_venue_id`, `customer_segment_id`, `sovereign_region_count`, `dedicated_region_count`
- `app.economics.fact_oracle_cloud_revenue`: `fiscal_quarter_id`, `scenario_id`, `oracle_business_id`, `oracle_cloud_venue_id`, `oracle_cloud_revenue_amount`
- `app.economics.fact_oracle_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `oracle_business_id`, `oracle_gross_margin_percent`
- `app.economics.fact_sovereign_economics`: `fiscal_quarter_id`, `scenario_id`, `oracle_cloud_venue_id`, `customer_segment_id`, `sovereign_revenue_amount`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (6) — Oracle

For Oracle, Are customers, not only investors, asking whether AI will replace Oracle’s application software?

- `app.adoption.dim_oracle_business`: `oracle_business_id`, `oracle_business_code`, `oracle_business_name`
- `app.adoption.dim_oracle_product`: `oracle_product_id`, `oracle_product_code`, `oracle_product_name`
- `app.adoption.fact_application_wins`: `fiscal_quarter_id`, `scenario_id`, `oracle_product_id`, `customer_segment_id`, `customer_win_count`, `renewal_count`
- `app.economics.fact_oracle_application_revenue`: `fiscal_quarter_id`, `scenario_id`, `oracle_product_id`, `customer_segment_id`, `oracle_application_revenue_amount`
- `app.adoption.fact_oracle_pipeline`: `fiscal_quarter_id`, `scenario_id`, `oracle_business_id`, `deal_structure_id`, `customer_segment_id`, `oracle_pipeline_opportunity_count`
- `app.delivery.fact_sovereign_capacity`: `fiscal_quarter_id`, `scenario_id`, `oracle_cloud_venue_id`, `customer_segment_id`, `sovereign_region_count`, `dedicated_region_count`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (2) — Oracle

For Oracle, What would Oracle have to change to move a data center from one customer to another if a large customer could not pay?

- `app.delivery.dim_capacity_type`: `capacity_type_id`, `capacity_type_code`, `capacity_type_name`
- `app.delivery.dim_workforce_group`: `workforce_group_id`, `workforce_group_code`, `workforce_group_name`
- `app.delivery.fact_data_center_capacity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `data_center_count`, `power_megawatt_capacity`, `gpu_unit_count`
- `app.delivery.fact_site_delivery_capacity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `capacity_type_id`, `site_under_construction_count`, `planned_site_count`
- `app.delivery.fact_sovereign_capacity`: `fiscal_quarter_id`, `scenario_id`, `oracle_cloud_venue_id`, `customer_segment_id`, `sovereign_region_count`, `dedicated_region_count`
- `app.economics.fact_capacity_pricing_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `capacity_type_id`, `contracted_price_per_capacity_unit_amount`, `spot_price_per_capacity_unit_amount`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (4) — Oracle

For Oracle, Why should the applications business accelerate this year when large SaaS peers are slowing?

- `app.adoption.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `app.adoption.dim_oracle_business`: `oracle_business_id`, `oracle_business_code`, `oracle_business_name`
- `app.adoption.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `app.adoption.dim_oracle_product`: `oracle_product_id`, `oracle_product_code`, `oracle_product_name`
- `app.adoption.fact_application_wins`: `fiscal_quarter_id`, `scenario_id`, `oracle_product_id`, `customer_segment_id`, `customer_win_count`, `renewal_count`
- `app.adoption.fact_oci_consumption`: `fiscal_quarter_id`, `scenario_id`, `oracle_business_id`, `capacity_type_id`, `ai_workload_id`, `oci_consumption_unit_count`, `gpu_hour_count`
- `app.adoption.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
