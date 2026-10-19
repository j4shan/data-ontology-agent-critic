# Broadline Inc operations slice

Fulfillment, logistics, store and cloud capacity facts. Capacity facts store no price.

## Numbered questions

### Q2 2026 (3) — Amazon

For Amazon, Was the AWS acceleration mostly capacity that came online, and how do second-half gigawatts compare with the first half and with 2027?

- `broadline.economics.fact_aws_economics`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_revenue_amount`, `cloud_operating_income_amount`
- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.marketplace.dim_amazon_business_activity`: `amazon_business_activity_id`, `amazon_business_activity_code`, `amazon_business_activity_name`
- `broadline.economics.fact_advertising_revenue`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `advertising_revenue_amount`
- `broadline.economics.fact_payment_revenue`: `fiscal_quarter_id`, `scenario_id`, `payment_method_id`, `process_type_id`, `payment_revenue_amount`, `payment_volume_amount`
- `broadline.economics.fact_promoted_listing_economics`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `product_category_id`, `promoted_listing_revenue_amount`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (5) — Amazon

For Amazon, Are Kiro, Transform, and workplace tools a real move into the application layer that lifts the infrastructure platform, and what funds the extra capacity?

- `broadline.economics.fact_advertising_revenue`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `advertising_revenue_amount`
- `broadline.economics.fact_aws_economics`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_revenue_amount`, `cloud_operating_income_amount`
- `broadline.economics.fact_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `logistics_asset_id`, `region_id`, `capital_expenditure_amount`
- `broadline.economics.fact_cloud_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `region_id`, `cloud_capital_expenditure_amount`
- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.marketplace.dim_amazon_business_activity`: `amazon_business_activity_id`, `amazon_business_activity_code`, `amazon_business_activity_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (6) — Amazon

For Amazon, What are consumers doing with faster delivery and a wider grocery and essentials assortment, and does that differ by country?

- `broadline.operations.dim_logistics_asset`: `logistics_asset_id`, `logistics_asset_code`, `logistics_asset_name`
- `broadline.economics.fact_grocery_sales`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `region_id`, `grocery_sales_amount`
- `broadline.economics.fact_shipping_economics`: `fiscal_quarter_id`, `scenario_id`, `delivery_speed_id`, `fulfillment_channel_id`, `shipping_cost_amount`, `shipping_revenue_amount`
- `broadline.marketplace.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `broadline.marketplace.dim_process_type`: `process_type_id`, `process_type_code`, `process_type_name`
- `broadline.marketplace.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (1) — Amazon

For Amazon, How much investment is required over the next couple of years to match compute with the revenue backlog, and how does custom silicon change Amazon’s position?

- `broadline.operations.fact_cloud_capacity`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `region_id`, `compute_capacity_vcpu_count`, `data_center_count`
- `broadline.economics.fact_advertising_revenue`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `advertising_revenue_amount`
- `broadline.economics.fact_amazon_activity_sales`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `amazon_net_sales_amount`
- `broadline.economics.fact_amazon_segment_economics`: `fiscal_quarter_id`, `scenario_id`, `amazon_reporting_segment_id`, `amazon_segment_sales_amount`, `amazon_segment_operating_income_amount`
- `broadline.economics.fact_aws_economics`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_revenue_amount`, `cloud_operating_income_amount`
- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (4) — Amazon

For Amazon, How large an unlock is full OpenAI model access on Bedrock versus Amazon’s own model, and when can Trainium racks be sold despite tight capacity?

- `broadline.marketplace.fact_amazon_unit_sales`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `fulfillment_channel_id`, `unit_sold_count`
- `broadline.economics.fact_amazon_activity_sales`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `amazon_net_sales_amount`
- `broadline.economics.fact_amazon_segment_economics`: `fiscal_quarter_id`, `scenario_id`, `amazon_reporting_segment_id`, `amazon_segment_sales_amount`, `amazon_segment_operating_income_amount`
- `broadline.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `gross_margin_percent`
- `broadline.marketplace.dim_ad_format`: `ad_format_id`, `ad_format_code`, `ad_format_name`
- `broadline.marketplace.dim_amazon_business_activity`: `amazon_business_activity_id`, `amazon_business_activity_code`, `amazon_business_activity_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (5) — Amazon

For Amazon, How large can Amazon LEO be in consumer and enterprise over the next few years, and what new services does the Globalstar spectrum enable?

- `broadline.marketplace.dim_amazon_business_activity`: `amazon_business_activity_id`, `amazon_business_activity_code`, `amazon_business_activity_name`
- `broadline.economics.fact_amazon_activity_sales`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `amazon_net_sales_amount`
- `broadline.economics.fact_amazon_segment_economics`: `fiscal_quarter_id`, `scenario_id`, `amazon_reporting_segment_id`, `amazon_segment_sales_amount`, `amazon_segment_operating_income_amount`
- `broadline.economics.fact_aws_economics`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_revenue_amount`, `cloud_operating_income_amount`
- `broadline.economics.fact_cloud_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `region_id`, `cloud_capital_expenditure_amount`
- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (2) — Amazon

For Amazon, How is the Anthropic capacity project tracking after a full quarter, and are there operating-income limits on further spend?

- `broadline.economics.fact_amazon_segment_economics`: `fiscal_quarter_id`, `scenario_id`, `amazon_reporting_segment_id`, `amazon_segment_sales_amount`, `amazon_segment_operating_income_amount`
- `broadline.economics.fact_aws_economics`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_revenue_amount`, `cloud_operating_income_amount`
- `broadline.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `total_net_sales_amount`, `operating_income_amount`, `net_income_amount`, `free_cash_flow_amount`
- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.economics.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `region_id`, `operating_expense_amount`
- `broadline.operations.fact_advertiser_capacity`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `advertiser_count`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (5) — Amazon

For Amazon, What is the AWS backlog, and where is AI supply still short of internal and customer demand as capacity arrives through 2026?

- `broadline.economics.fact_aws_economics`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_revenue_amount`, `cloud_operating_income_amount`
- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.operations.fact_cloud_region_capacity`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_region_count`, `availability_zone_count`
- `broadline.operations.fact_data_center_power`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `cloud_customer_type_id`, `power_megawatt_capacity`, `site_count`
- `broadline.marketplace.dim_amazon_business_activity`: `amazon_business_activity_id`, `amazon_business_activity_code`, `amazon_business_activity_name`
- `broadline.marketplace.dim_amazon_reporting_segment`: `amazon_reporting_segment_id`, `amazon_reporting_segment_code`, `amazon_reporting_segment_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (4) — Amazon

For Amazon, Do perishable groceries change the role of Amazon Fresh stores, given many buyers had never bought perishables from Amazon?

- `broadline.operations.dim_logistics_asset`: `logistics_asset_id`, `logistics_asset_code`, `logistics_asset_name`
- `broadline.economics.fact_amazon_activity_sales`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `amazon_net_sales_amount`
- `broadline.economics.fact_amazon_segment_economics`: `fiscal_quarter_id`, `scenario_id`, `amazon_reporting_segment_id`, `amazon_segment_sales_amount`, `amazon_segment_operating_income_amount`
- `broadline.economics.fact_grocery_sales`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `region_id`, `grocery_sales_amount`
- `broadline.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `gross_margin_percent`
- `broadline.economics.fact_shipping_economics`: `fiscal_quarter_id`, `scenario_id`, `delivery_speed_id`, `fulfillment_channel_id`, `shipping_cost_amount`, `shipping_revenue_amount`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (5) — Amazon

For Amazon, How do robotics and physical AI create efficiency that can be reinvested in operations?

- `broadline.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `broadline.economics.fact_fulfillment_economics`: `fiscal_quarter_id`, `scenario_id`, `fulfillment_channel_id`, `region_id`, `fulfillment_expense_amount`
- `broadline.economics.fact_physical_store_sales`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `region_id`, `physical_store_sales_amount`
- `broadline.economics.fact_seller_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `seller_type_id`, `fulfillment_channel_id`, `seller_service_revenue_amount`
- `broadline.economics.fact_shipping_economics`: `fiscal_quarter_id`, `scenario_id`, `delivery_speed_id`, `fulfillment_channel_id`, `shipping_cost_amount`, `shipping_revenue_amount`
- `broadline.marketplace.dim_amazon_business_activity`: `amazon_business_activity_id`, `amazon_business_activity_code`, `amazon_business_activity_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (6) — Amazon

For Amazon, How will Amazon serve customers who buy through agents rather than the usual site?

- `broadline.operations.fact_data_center_power`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `cloud_customer_type_id`, `power_megawatt_capacity`, `site_count`
- `broadline.economics.fact_amazon_activity_sales`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `amazon_net_sales_amount`
- `broadline.economics.fact_amazon_segment_economics`: `fiscal_quarter_id`, `scenario_id`, `amazon_reporting_segment_id`, `amazon_segment_sales_amount`, `amazon_segment_operating_income_amount`
- `broadline.economics.fact_aws_economics`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_revenue_amount`, `cloud_operating_income_amount`
- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `gross_margin_percent`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (7) — Amazon

For Amazon, How much of the AWS acceleration is core infrastructure versus AI, how important is AgentCore in bringing enterprises, and how much of ad growth is core versus the DSP and Prime Video?

- `broadline.marketplace.dim_ad_format`: `ad_format_id`, `ad_format_code`, `ad_format_name`
- `broadline.marketplace.dim_amazon_business_activity`: `amazon_business_activity_id`, `amazon_business_activity_code`, `amazon_business_activity_name`
- `broadline.economics.fact_advertising_revenue`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `advertising_revenue_amount`
- `broadline.economics.fact_aws_economics`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_revenue_amount`, `cloud_operating_income_amount`
- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `total_net_sales_amount`, `operating_income_amount`, `net_income_amount`, `free_cash_flow_amount`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (4) — eBay

For eBay, How will buyer behavior change as agents roll out, and does that hit advertising or the site architecture?

- `broadline.economics.fact_advertising_revenue`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `advertising_revenue_amount`
- `broadline.marketplace.dim_ad_format`: `ad_format_id`, `ad_format_code`, `ad_format_name`
- `broadline.marketplace.dim_buyer_type`: `buyer_type_id`, `buyer_type_code`, `buyer_type_name`
- `broadline.marketplace.dim_process_type`: `process_type_id`, `process_type_code`, `process_type_name`
- `broadline.marketplace.fact_advertising_impressions`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `product_category_id`, `impression_count`, `click_count`
- `broadline.marketplace.fact_marketplace_orders`: `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `product_category_id`, `seller_type_id`, `buyer_type_id`, `order_count`, `unit_quantity`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (3) — eBay

For eBay, What technical or commercial constraints limit partnerships with AI assistants and agents?

- `broadline.marketplace.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `broadline.operations.fact_fulfillment_capacity`: `fiscal_quarter_id`, `scenario_id`, `logistics_asset_id`, `region_id`, `facility_count`, `facility_square_foot_count`
- `broadline.operations.fact_logistics_capacity`: `fiscal_quarter_id`, `scenario_id`, `delivery_speed_id`, `region_id`, `daily_package_capacity_count`, `delivery_vehicle_count`
- `broadline.operations.fact_cloud_capacity`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `region_id`, `compute_capacity_vcpu_count`, `data_center_count`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
