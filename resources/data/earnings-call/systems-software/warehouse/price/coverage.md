# Platform Inc price slice

This slice is part of the Platform Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q3 FY2026 (3) — Microsoft

How confident is Microsoft that it can work through physical component constraints to deliver the sharp second-half capital-spending step-up, including greater use of partners?

- `platform.price.fact_capital_spending_sw`: `capital_spending_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `capacity_type_id`, `capital_spending_amount`
- `platform.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`

### Q3 FY2026 (6) — Microsoft

How should the gap between capital-spending growth and revenue growth close, including what share of spend is equipment replacement versus first-party capacity?

- `platform.price.fact_capital_spending_sw`: `capital_spending_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `capacity_type_id`, `capital_spending_amount`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.supply.fact_support_capacity`: `support_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `support_tier_id`, `reporting_unit_id`, `support_case_quantity`
- `platform.price.fact_segment_revenue_msft`: `segment_revenue_msft_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_segment_id`, `segment_revenue_amount`

### Q3 FY2026 (8) — Microsoft

Under the revised OpenAI arrangement, how does Microsoft’s model mix change, and did any commercial terms change how related capacity or revenue should be modeled?

- `platform.price.fact_subscription_revenue`: `subscription_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `subscription_revenue_amount`
- `platform.price.fact_guidance_revenue`: `guidance_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_type_id`, `guided_revenue_amount`
- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `platform.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `platform.demand.fact_cloud_consumption`: `cloud_consumption_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `model_type_id`, `compute_hour_quantity`, `workload_unit_quantity`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`

### Q2 FY2026 (1) — Microsoft

How much Azure growth should follow from the capacity being added, and what return is expected as that capital spending converts to revenue?

- `platform.price.fact_capital_spending_sw`: `capital_spending_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `capacity_type_id`, `capital_spending_amount`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `platform.demand.dim_acquisition_type`: `acquisition_type_id`, `acquisition_type_code`, `acquisition_type_name`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`

### Q2 FY2026 (5) — Microsoft

How core is custom silicon becoming, and does the inference accelerator change the gross-margin profile of inference?

- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.price.fact_cloud_margin`: `cloud_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `gross_income_amount`, `gross_margin_percent`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`

### Q2 FY2026 (6) — Microsoft

After CPU-side operational changes, are customers accelerating cloud migrations because AI workloads need cloud compute, storage, and tools alongside accelerators?

- `platform.price.fact_cloud_margin`: `cloud_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `gross_income_amount`, `gross_margin_percent`
- `platform.demand.fact_cloud_consumption`: `cloud_consumption_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `model_type_id`, `compute_hour_quantity`, `workload_unit_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.demand.dim_msft_product`: `msft_product_id`, `msft_product_code`, `msft_product_name`, `msft_segment_id`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`

### Q1 FY2026 (1) — Microsoft

If application and computing architectures shift toward something like AGI, what would that change about Microsoft’s software and cloud position under the OpenAI agreement?

- `platform.price.fact_cloud_margin`: `cloud_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `gross_income_amount`, `gross_margin_percent`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.price.fact_guidance_revenue`: `guidance_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_type_id`, `guided_revenue_amount`

### Q1 2026 (2) — ServiceNow

After AI is priced inside the platform rather than as a sidecar, how will Now Assist revenue be measured?

- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.supply.fact_support_capacity`: `support_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `support_tier_id`, `reporting_unit_id`, `support_case_quantity`
- `platform.supply.fact_production_capacity_sw`: `production_capacity_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `release_quantity`

### Q1 2026 (5) — ServiceNow

What price can ServiceNow charge for the value of that autonomous service-desk outcome?

- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `platform.price.fact_current_rpo`: `current_rpo_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `current_rpo_amount`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`
- `platform.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `platform.demand.fact_cloud_consumption`: `cloud_consumption_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `model_type_id`, `compute_hour_quantity`, `workload_unit_quantity`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`

### Q1 2026 (6) — ServiceNow

How much of the first-quarter beat was organic versus acquired (including the named tuck-ins), and when should AI benefits show up in the full-year outlook aside from Armis and currency?

- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.price.fact_currency_revenue`: `currency_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `currency_effect_id`, `currency_effect_amount`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`

### Q1 2026 (7) — ServiceNow

What current remaining performance obligation headwind does Armis create, and why does that support keeping the full-year outlook unchanged after the quarterly beat?

- `platform.price.fact_current_rpo`: `current_rpo_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `current_rpo_amount`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.price.fact_remaining_performance_obligation`: `remaining_performance_obligation_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `acquisition_type_id`, `rpo_amount`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`

### Q1 2026 (8) — ServiceNow

What are customers saying about recent acquisitions, how long until the sales force can sell them, and how conservative are the initial ramp assumptions?

- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`

### Q4 2025 (1) — ServiceNow

What budget tailwinds and headwinds are showing up in demand, and how should AI consumption monetization layer into results on the way from the cleared $500 million ACV mark toward $1 billion?

- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`

### Q4 2025 (2) — ServiceNow

How did U.S. federal perform versus expectations through the shutdown, and what does the 2026 federal pipeline look like?

- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`

### Q4 2025 (3) — ServiceNow

How much of the gross-margin pressure from LLM inference and API costs is temporary until consumption is monetized, versus structural?

- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.price.fact_cloud_margin`: `cloud_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `gross_income_amount`, `gross_margin_percent`
- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`

### Q4 2025 (5) — ServiceNow

How do customers choose between the OpenAI and Anthropic partnerships, and how is each partner’s investment expected to pull ServiceNow revenue forward?

- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_subscription_revenue`: `subscription_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `subscription_revenue_amount`
- `platform.price.fact_enterprise_revenue_sw`: `enterprise_revenue_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`

### Q4 2025 (6) — ServiceNow

Are real-time monitoring, kill switches, agent grading, and red-teaming the objections that stall enterprise AI programs, and how does the platform address them?

- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_enterprise_revenue_sw`: `enterprise_revenue_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `platform.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`

### Q3 2025 (1) — ServiceNow

Is Now Assist being sold more broadly by the sales force and partners, rather than only as a top-down motion, and how does that change the outlook?

- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.fact_deferred_deals`: `deferred_deals_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `deployment_type_id`, `now_product_id`, `deferred_deal_quantity`
- `platform.price.fact_current_rpo`: `current_rpo_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `current_rpo_amount`
- `platform.demand.fact_deployment_volume`: `deployment_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `deployment_type_id`, `now_product_id`, `deployment_quantity`
- `platform.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (4) — ServiceNow

In the large fourth-quarter renewal cohort, are customers more willing to expand into Pro Plus than first expected?

- `platform.price.fact_renewal_revenue`: `renewal_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `deal_stage_id`, `renewal_revenue_amount`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.demand.fact_renewal_volume`: `renewal_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `deal_stage_id`, `renewal_contract_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.price.fact_subscription_revenue`: `subscription_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `subscription_revenue_amount`

### Q2 2025 (3) — ServiceNow

How are customers using Now Assist consumption packs, and how large can that revenue become?

- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.demand.fact_deferred_deals`: `deferred_deals_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `deployment_type_id`, `now_product_id`, `deferred_deal_quantity`
- `platform.price.fact_current_rpo`: `current_rpo_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `current_rpo_amount`
- `platform.demand.fact_deployment_volume`: `deployment_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `deployment_type_id`, `now_product_id`, `deployment_quantity`

### Q2 2025 (4) — ServiceNow

Why did the full-year operating-margin outlook stay flat after a stronger second quarter if productivity in engineering and sales is rising — reinvestment, timing, or caution?

- `platform.price.fact_enterprise_margin_sw`: `enterprise_margin_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`, `gross_margin_percent`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.demand.fact_bookings_demand`: `bookings_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `pricing_model_id`, `contract_quantity`
- `platform.demand.fact_search_queries`: `search_queries_record_id`, `fiscal_quarter_id`, `scenario_id`, `region_id`, `query_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.supply.fact_support_capacity`: `support_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `support_tier_id`, `reporting_unit_id`, `support_case_quantity`

### Q2 2025 (5) — ServiceNow

Does selling AI require more on-site engineers, so that the cost of sale is structurally higher?

- `platform.price.fact_cloud_cost_rate`: `cloud_cost_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `msft_product_id`, `workload_type_id`, `cost_per_compute_hour`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.price.fact_seat_price_rate`: `seat_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `license_tier_id`, `price_per_seat_amount`
- `platform.price.fact_operating_expense_sw`: `operating_expense_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cost_bucket_id`, `operating_expense_amount`
- `platform.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`

### Q2 2025 (7) — ServiceNow

Are more new logos landing on the platform because of the AI roadmap, including RaptorDB and Now Assist?

- `platform.price.fact_now_revenue`: `now_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `revenue_type_id`, `revenue_amount`
- `platform.demand.fact_workflow_volume_by_vertical`: `workflow_volume_by_vertical_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `industry_vertical_id`, `vertical_user_quantity`
- `platform.demand.fact_workflow_subscriptions`: `workflow_subscriptions_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `deployment_type_id`, `subscribed_user_quantity`, `workflow_instance_quantity`
- `platform.demand.fact_deferred_deals`: `deferred_deals_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `deployment_type_id`, `now_product_id`, `deferred_deal_quantity`
- `platform.supply.fact_cloud_utilization`: `cloud_utilization_record_id`, `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capacity_type_id`, `utilization_percent`
- `platform.supply.fact_production_capacity_sw`: `production_capacity_sw_record_id`, `fiscal_quarter_id`, `scenario_id`, `now_product_id`, `release_quantity`
