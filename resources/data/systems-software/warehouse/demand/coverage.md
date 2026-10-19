# Platform Inc demand slice

This slice is part of the Platform Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q4 FY2026 (1) — Microsoft

How large could open and custom-model usage become over the next one to two years if many enterprises are still hesitant to adopt open models?

- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_model_usage`: `model_usage_record_id`, `fiscal_quarter_id`, `scenario_id`, `model_type_id`, `msft_product_id`, `token_quantity`, `inference_request_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.price.fact_subscription_revenue`: `subscription_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `subscription_revenue_amount`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.price.fact_cloud_margin`: `cloud_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `gross_income_amount`, `gross_margin_percent`

### Q4 FY2026 (2) — Microsoft

If customers shift toward open and custom models, how does Microsoft benefit while it still has large exposure to frontier labs?

- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.price.fact_cloud_margin`: `cloud_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `gross_income_amount`, `gross_margin_percent`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_deferred_deals`: `deferred_deals_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `deployment_type_id`, `now_product_id`, `deferred_deal_quantity`
- `platform.price.fact_segment_revenue_msft`: `segment_revenue_msft_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_segment_id`, `segment_revenue_amount`
- `platform.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `revenue_type_id`, `product_revenue_amount`

### Q4 FY2026 (5) — Microsoft

How are rising component prices absorbed without either large price increases or margin compression?

- `platform.demand.fact_cloud_consumption`: `cloud_consumption_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `model_type_id`, `compute_hour_quantity`, `workload_unit_quantity`
- `platform.supply.fact_compute_capacity`: `compute_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_type_id`, `data_center_region_id`, `server_unit_quantity`, `gpu_unit_quantity`
- `platform.price.fact_cloud_margin`: `cloud_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `gross_income_amount`, `gross_margin_percent`
- `platform.demand.dim_msft_product`: `msft_product_id`, `msft_product_code`, `msft_product_name`, `msft_segment_id`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.demand.fact_model_usage`: `model_usage_record_id`, `fiscal_quarter_id`, `scenario_id`, `model_type_id`, `msft_product_id`, `token_quantity`, `inference_request_quantity`

### Q4 FY2026 (6) — Microsoft

Are Microsoft 365 Copilot customers still mostly in pilots, or have they moved into broad deployments?

- `platform.demand.fact_cloud_consumption`: `cloud_consumption_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `model_type_id`, `compute_hour_quantity`, `workload_unit_quantity`
- `platform.demand.fact_copilot_seats`: `copilot_seats_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `deal_stage_id`, `paid_seat_quantity`, `active_user_quantity`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.demand.fact_model_usage`: `model_usage_record_id`, `fiscal_quarter_id`, `scenario_id`, `model_type_id`, `msft_product_id`, `token_quantity`, `inference_request_quantity`
- `platform.demand.fact_gaming_users`: `gaming_users_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `region_id`, `active_gamer_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`

### Q4 FY2026 (7) — Microsoft

From here, is Copilot monetization driven more by extra seats, moves to higher SKUs such as E7, or consumption?

- `platform.demand.fact_copilot_seats`: `copilot_seats_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `deal_stage_id`, `paid_seat_quantity`, `active_user_quantity`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`
- `platform.demand.dim_acquisition_type`: `acquisition_type_id`, `acquisition_type_code`, `acquisition_type_name`
- `platform.demand.fact_cloud_consumption`: `cloud_consumption_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `model_type_id`, `compute_hour_quantity`, `workload_unit_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `revenue_type_id`, `product_revenue_amount`

### Q4 FY2026 (8) — Microsoft

What does Project Perception, after the latest frontier-model releases, change for the security business and for customer trust in Microsoft?

- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_deferred_deals`: `deferred_deals_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `deployment_type_id`, `now_product_id`, `deferred_deal_quantity`
- `platform.price.fact_subscription_revenue`: `subscription_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `subscription_revenue_amount`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.price.fact_cloud_margin`: `cloud_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `gross_income_amount`, `gross_margin_percent`

### Q4 FY2026 (9) — Microsoft

How does return on capital spending decided today compare with a year ago, and can internal silicon still lift monetization?

- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.price.fact_cloud_margin`: `cloud_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `gross_income_amount`, `gross_margin_percent`
- `platform.price.fact_capital_spending_sw`: `capital_spending_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `capacity_type_id`, `capital_spending_amount`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_deferred_deals`: `deferred_deals_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `deployment_type_id`, `now_product_id`, `deferred_deal_quantity`

### Q3 FY2026 (1) — Microsoft

How does strong AI demand show up in commercial bookings when seat and consumption contracts renew on different cycles?

- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.demand.fact_ai_seat_volume`: `ai_seat_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `ai_product_id`, `deal_stage_id`, `ai_seat_quantity`
- `platform.demand.fact_copilot_seats`: `copilot_seats_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `deal_stage_id`, `paid_seat_quantity`, `active_user_quantity`
- `platform.price.fact_cloud_margin`: `cloud_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `gross_income_amount`, `gross_margin_percent`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`

### Q3 FY2026 (2) — Microsoft

Over a longer horizon, which customers are actually funding the AI demand Microsoft is seeing?

- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.supply.fact_support_capacity`: `support_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `support_tier_id`, `reporting_unit_id`, `support_case_quantity`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`

### Q3 FY2026 (4) — Microsoft

How should the added capacity be split between first-party products and third-party Azure?

- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.price.fact_cloud_margin`: `cloud_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `gross_income_amount`, `gross_margin_percent`
- `platform.price.fact_capital_spending_sw`: `capital_spending_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `capacity_type_id`, `capital_spending_amount`

### Q3 FY2026 (5) — Microsoft

Why can AI carry better margins over time even though the build-out is expensive?

- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`
- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`

### Q3 FY2026 (7) — Microsoft

What in Copilot adoption is working or not, and how does that shape the E7 and Copilot Cowork product plans?

- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.price.fact_cloud_margin`: `cloud_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `gross_income_amount`, `gross_margin_percent`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`
- `platform.demand.fact_cloud_consumption`: `cloud_consumption_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `model_type_id`, `compute_hour_quantity`, `workload_unit_quantity`

### Q3 FY2026 (9) — Microsoft

How does Microsoft keep seat-based predictability, as in E7, while growing consumption, and what mix of consumption versus seats is expected in three to five years?

- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`
- `platform.demand.fact_copilot_seats`: `copilot_seats_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `deal_stage_id`, `paid_seat_quantity`, `active_user_quantity`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.price.fact_cloud_margin`: `cloud_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `gross_income_amount`, `gross_margin_percent`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`

### Q2 FY2026 (2) — Microsoft

With servers depreciated over about six years but remaining performance obligations lasting about two and a half, how is AI-heavy hardware expected to earn revenue and gross profit across its useful life?

- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.price.fact_cloud_margin`: `cloud_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `gross_income_amount`, `gross_margin_percent`
- `platform.supply.fact_support_capacity`: `support_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `support_tier_id`, `reporting_unit_id`, `support_case_quantity`
- `platform.price.fact_segment_revenue_msft`: `segment_revenue_msft_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_segment_id`, `segment_revenue_amount`
- `platform.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `revenue_type_id`, `product_revenue_amount`

### Q2 FY2026 (3) — Microsoft

How durable is the backlog when a large share, about 45%, is tied to OpenAI?

- `platform.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.supply.fact_support_capacity`: `support_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `support_tier_id`, `reporting_unit_id`, `support_case_quantity`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`

### Q2 FY2026 (7) — Microsoft

How much can enterprise spend with Microsoft expand as customers move from early AI projects to broader “frontier” transformations?

- `platform.demand.fact_model_usage`: `model_usage_record_id`, `fiscal_quarter_id`, `scenario_id`, `model_type_id`, `msft_product_id`, `token_quantity`, `inference_request_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.price.fact_segment_revenue_msft`: `segment_revenue_msft_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_segment_id`, `segment_revenue_amount`
- `platform.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `revenue_type_id`, `product_revenue_amount`
- `platform.price.fact_enterprise_revenue_sw`: `enterprise_revenue_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`

### Q1 FY2026 (2) — Microsoft

How broad is the bookings and RPO surge beyond a handful of very large contracts, including on a global basis?

- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`
- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (3) — Microsoft

What evidence shows software and consumer internet can monetize the industry’s AI investment, and which signals would indicate Microsoft is overbuilding for current demand?

- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.price.fact_cloud_margin`: `cloud_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `gross_income_amount`, `gross_margin_percent`

### Q1 FY2026 (4) — Microsoft

How does Microsoft judge whether AI-native customers can honor commitments that are enormous relative to their revenue, and what guardrails limit concentration in any one customer?

- `platform.demand.fact_deferred_deals`: `deferred_deals_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `deployment_type_id`, `now_product_id`, `deferred_deal_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.price.fact_segment_revenue_msft`: `segment_revenue_msft_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_segment_id`, `segment_revenue_amount`
- `platform.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `revenue_type_id`, `product_revenue_amount`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_cloud_margin`: `cloud_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `gross_income_amount`, `gross_margin_percent`

### Q1 FY2026 (5) — Microsoft

How large is the Azure revenue not captured because capacity is short, and what keeps those workloads from moving to other providers?

- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.supply.fact_support_capacity`: `support_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `support_tier_id`, `reporting_unit_id`, `support_case_quantity`
- `platform.price.fact_segment_revenue_msft`: `segment_revenue_msft_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_segment_id`, `segment_revenue_amount`
- `platform.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `revenue_type_id`, `product_revenue_amount`

### Q1 FY2026 (6) — Microsoft

What criteria decide whether Microsoft keeps a very large AI contract on its own paper or lets another hyperscaler take it?

- `platform.demand.dim_acquisition_type`: `acquisition_type_id`, `acquisition_type_code`, `acquisition_type_name`
- `platform.demand.fact_model_usage`: `model_usage_record_id`, `fiscal_quarter_id`, `scenario_id`, `model_type_id`, `msft_product_id`, `token_quantity`, `inference_request_quantity`
- `platform.demand.fact_renewal_volume`: `renewal_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `deal_stage_id`, `renewal_contract_quantity`
- `platform.demand.dim_msft_product`: `msft_product_id`, `msft_product_code`, `msft_product_name`, `msft_segment_id`
- `platform.demand.dim_model_type`: `model_type_id`, `model_type_code`, `model_type_name`
- `platform.demand.dim_ai_product`: `ai_product_id`, `ai_product_code`, `ai_product_name`

### Q1 2026 (1) — ServiceNow

During the Iran conflict, were the Middle East deferrals concentrated in government or sovereign buyers versus private companies, were they on-premises, were they AI or non-AI, and would they return quickly if the conflict eased in the second quarter?

- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.demand.fact_model_usage`: `model_usage_record_id`, `fiscal_quarter_id`, `scenario_id`, `model_type_id`, `msft_product_id`, `token_quantity`, `inference_request_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`

### Q1 2026 (3) — ServiceNow

How does Control Tower stay differentiated as agent orchestration becomes crowded?

- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_current_rpo`: `current_rpo_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `current_rpo_amount`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.dim_now_product`: `now_product_id`, `now_product_code`, `now_product_name`
- `platform.demand.fact_cloud_consumption`: `cloud_consumption_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `model_type_id`, `compute_hour_quantity`, `workload_unit_quantity`

### Q1 2026 (4) — ServiceNow

How does the autonomous workforce, including the level-1 service desk, complement Now Assist rather than overlap it?

- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_current_rpo`: `current_rpo_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `current_rpo_amount`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.dim_now_product`: `now_product_id`, `now_product_code`, `now_product_name`
- `platform.demand.fact_deferred_deals`: `deferred_deals_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `deployment_type_id`, `now_product_id`, `deferred_deal_quantity`

### Q4 2025 (7) — ServiceNow

While seats are still growing, does hybrid pricing eventually give way to consumption or value-based pricing with little seat component?

- `platform.demand.fact_cloud_consumption`: `cloud_consumption_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `model_type_id`, `compute_hour_quantity`, `workload_unit_quantity`
- `platform.demand.fact_copilot_seats`: `copilot_seats_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `deal_stage_id`, `paid_seat_quantity`, `active_user_quantity`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.supply.fact_compute_capacity`: `compute_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `component_type_id`, `data_center_region_id`, `server_unit_quantity`, `gpu_unit_quantity`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`
- `platform.demand.fact_ai_seat_volume`: `ai_seat_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `ai_product_id`, `deal_stage_id`, `ai_seat_quantity`

### Q4 2025 (8) — ServiceNow

Of AI training and inference expected to run through the platform in 2026, what share sits on ServiceNow models versus third-party foundation models?

- `platform.demand.fact_model_usage`: `model_usage_record_id`, `fiscal_quarter_id`, `scenario_id`, `model_type_id`, `msft_product_id`, `token_quantity`, `inference_request_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`

### Q3 2025 (3) — ServiceNow

How did bookings linearity develop through the quarter, and is AI-credit consumption running ahead of plan?

- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`

### Q3 2025 (5) — ServiceNow

What is driving the reported 55-fold consumption increase — a broad base or specific verticals and use cases — and how does the $500 million Now Assist ACV target sit versus the path to $1 billion?

- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.supply.fact_support_capacity`: `support_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `support_tier_id`, `reporting_unit_id`, `support_case_quantity`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`

### Q3 2025 (6) — ServiceNow

Why is the fourth-quarter subscription growth outlook a bit below where CRPO growth appears to be settling, and how much of that is public sector versus renewal timing?

- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.fact_sovereign_volume`: `sovereign_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `deployment_type_id`, `customer_type_id`, `sovereign_user_quantity`
- `platform.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`

### Q3 2025 (7) — ServiceNow

As large enterprises drop AI pilots, how important are industry-specific workflows versus horizontal ones in winning the consolidated platform decision?

- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.demand.fact_platform_users`: `platform_users_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_type_id`, `active_user_quantity`
- `platform.demand.fact_model_usage`: `model_usage_record_id`, `fiscal_quarter_id`, `scenario_id`, `model_type_id`, `msft_product_id`, `token_quantity`, `inference_request_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.supply.fact_production_capacity_sw`: `production_capacity_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `release_quantity`

### Q3 2025 (9) — ServiceNow

Did this year’s Now Assist pricing change unlock deals, and are lighthouse references now pulling in more customers?

- `platform.demand.fact_deferred_deals`: `deferred_deals_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `deployment_type_id`, `now_product_id`, `deferred_deal_quantity`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`

### Q3 2025 (10) — ServiceNow

Which workflow is adopted first for Now Assist, do customers then expand into customer service and HR, and how much of the $500 million ACV is subscription uplift versus token consumption?

- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.demand.fact_deferred_deals`: `deferred_deals_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `deployment_type_id`, `now_product_id`, `deferred_deal_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_current_rpo`: `current_rpo_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `current_rpo_amount`

### Q3 2025 (11) — ServiceNow

Is security growth accelerating as it crosses $1 billion of ACV, and how much of that is from AI inside security?

- `platform.demand.dim_acquisition_type`: `acquisition_type_id`, `acquisition_type_code`, `acquisition_type_name`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`

### Q3 2025 (12) — ServiceNow

What does Moveworks add to the AI suite beyond the Now Assist results already achieved without it?

- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_current_rpo`: `current_rpo_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `current_rpo_amount`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `platform.demand.dim_now_product`: `now_product_id`, `now_product_code`, `now_product_name`

### Q2 2025 (1) — ServiceNow

Are customers positioning AI Control Tower as the control plane for third-party agents as well as ServiceNow’s, and could ServiceNow agents replace those third-party agents if the joint NVIDIA model succeeds?

- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_model_usage`: `model_usage_record_id`, `fiscal_quarter_id`, `scenario_id`, `model_type_id`, `msft_product_id`, `token_quantity`, `inference_request_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_subscription_revenue`: `subscription_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `subscription_revenue_amount`

### Q2 2025 (2) — ServiceNow

After Logik AI closed, where is the nearest front-office opportunity among service, sales, and marketing?

- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`

### Q2 2025 (6) — ServiceNow

What drove the revenue upside — self-hosted mix, linearity, or a specific business — and is the jump in technology-workflow mix a one-time item or a new trend?

- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`

### Q2 2025 (8) — ServiceNow

After recent leadership changes, how is go-to-market health differing across the United States, Europe, and Asia Pacific?

- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`

### Q2 2025 (9) — ServiceNow

Could the agent cycle shift mix away from technology workflows toward CRM, industry workflows, or Creator, or should today’s mix hold?

- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `platform.demand.dim_now_product`: `now_product_id`, `now_product_code`, `now_product_name`
- `platform.demand.dim_acquisition_type`: `acquisition_type_id`, `acquisition_type_code`, `acquisition_type_name`
- `platform.demand.fact_cloud_consumption`: `cloud_consumption_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `model_type_id`, `compute_hour_quantity`, `workload_unit_quantity`
