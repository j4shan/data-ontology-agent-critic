# Broadline Inc economics slice

Sales, GMV, take-rate, cloud, advertising, payment and margin dollars, each on its own process fact. A price fact stores no unit quantity.

## Numbered questions

### Q2 2026 (1) — Amazon

For Amazon, What drove the high AWS operating margin, and how sustainable is it if AI workloads were expected to be lower margin at first?

- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.economics.fact_aws_economics`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_revenue_amount`, `cloud_operating_income_amount`
- `broadline.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `broadline.economics.fact_amazon_segment_economics`: `fiscal_quarter_id`, `scenario_id`, `amazon_reporting_segment_id`, `amazon_segment_sales_amount`, `amazon_segment_operating_income_amount`
- `broadline.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `total_net_sales_amount`, `operating_income_amount`, `net_income_amount`, `free_cash_flow_amount`
- `broadline.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `gross_margin_percent`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (2) — Amazon

For Amazon, Does the full stack still require Amazon’s own leading model, given Bedrock spend jumped past the sum of prior quarters?

- `broadline.economics.fact_amazon_activity_sales`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `amazon_net_sales_amount`
- `broadline.economics.fact_amazon_segment_economics`: `fiscal_quarter_id`, `scenario_id`, `amazon_reporting_segment_id`, `amazon_segment_sales_amount`, `amazon_segment_operating_income_amount`
- `broadline.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `gross_margin_percent`
- `broadline.marketplace.fact_amazon_unit_sales`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `fulfillment_channel_id`, `unit_sold_count`
- `broadline.economics.fact_advertising_revenue`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `advertising_revenue_amount`
- `broadline.economics.fact_aws_economics`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_revenue_amount`, `cloud_operating_income_amount`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (6) — Amazon

For Amazon, How do higher memory and storage prices flow into capital spending this year and next, and what advertising opportunity sits in agentic shopping?

- `broadline.economics.fact_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `logistics_asset_id`, `region_id`, `capital_expenditure_amount`
- `broadline.economics.fact_cloud_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `region_id`, `cloud_capital_expenditure_amount`
- `broadline.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `broadline.economics.fact_advertising_revenue`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `advertising_revenue_amount`
- `broadline.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `total_net_sales_amount`, `operating_income_amount`, `net_income_amount`, `free_cash_flow_amount`
- `broadline.economics.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `region_id`, `operating_expense_amount`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (1) — Amazon

For Amazon, How long does the capital-spending cycle last, and what profitability should show that the spend earns a return?

- `broadline.economics.fact_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `logistics_asset_id`, `region_id`, `capital_expenditure_amount`
- `broadline.economics.fact_cloud_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `region_id`, `cloud_capital_expenditure_amount`
- `broadline.marketplace.fact_returns_quantity`: `fiscal_quarter_id`, `scenario_id`, `product_category_id`, `fulfillment_channel_id`, `returned_unit_count`
- `broadline.operations.fact_returns_capacity`: `fiscal_quarter_id`, `scenario_id`, `fulfillment_channel_id`, `region_id`, `daily_return_capacity_count`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (3) — Amazon

For Amazon, As AI spend spreads beyond a few labs in 2026, how could a deeper OpenAI relationship help both retail and AWS?

- `broadline.economics.fact_aws_economics`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_revenue_amount`, `cloud_operating_income_amount`
- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.marketplace.dim_amazon_business_activity`: `amazon_business_activity_id`, `amazon_business_activity_code`, `amazon_business_activity_name`
- `broadline.marketplace.dim_amazon_reporting_segment`: `amazon_reporting_segment_id`, `amazon_reporting_segment_code`, `amazon_reporting_segment_name`
- `broadline.marketplace.dim_seller_type`: `seller_type_id`, `seller_type_code`, `seller_type_name`
- `broadline.operations.dim_cloud_customer_type`: `cloud_customer_type_id`, `cloud_customer_type_code`, `cloud_customer_type_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (4) — Amazon

For Amazon, Where does global retail spend more this year to improve service, and where does it expect efficiency?

- `broadline.economics.fact_aws_economics`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_revenue_amount`, `cloud_operating_income_amount`
- `broadline.economics.fact_cloud_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `region_id`, `cloud_capital_expenditure_amount`
- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.economics.fact_seller_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `seller_type_id`, `fulfillment_channel_id`, `seller_service_revenue_amount`
- `broadline.marketplace.dim_amazon_business_activity`: `amazon_business_activity_id`, `amazon_business_activity_code`, `amazon_business_activity_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (2) — eBay

For eBay, How intense is consumer-to-consumer competition in the U.S. and internationally as eBay invests and adds Depop?

- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.economics.fact_ebay_revenue`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `ebay_revenue_amount`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.economics.fact_promoted_listing_economics`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `product_category_id`, `promoted_listing_revenue_amount`
- `broadline.marketplace.dim_ad_format`: `ad_format_id`, `ad_format_code`, `ad_format_name`
- `broadline.marketplace.dim_ebay_business_activity`: `ebay_business_activity_id`, `ebay_business_activity_code`, `ebay_business_activity_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (3) — eBay

For eBay, How hard will Depop need to market against a new U.S. entrant that eBay has already faced in the U.K. and Germany?

- `broadline.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.economics.fact_ebay_revenue`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `ebay_revenue_amount`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.economics.fact_promoted_listing_economics`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `product_category_id`, `promoted_listing_revenue_amount`
- `broadline.marketplace.dim_ad_format`: `ad_format_id`, `ad_format_code`, `ad_format_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (2) — eBay

For eBay, How do Live and AI product investments change cost of goods over time?

- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `gross_margin_percent`
- `broadline.marketplace.fact_ebay_listing_activity`: `fiscal_quarter_id`, `scenario_id`, `listing_type_id`, `product_category_id`, `listing_count`, `live_listing_count`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.economics.fact_promoted_listing_economics`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `product_category_id`, `promoted_listing_revenue_amount`
- `broadline.marketplace.dim_ad_format`: `ad_format_id`, `ad_format_code`, `ad_format_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (6) — eBay

For eBay, What drove the advertising surprise, how should that read into 2026, and how far along is AI search?

- `broadline.economics.fact_advertising_revenue`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `advertising_revenue_amount`
- `broadline.marketplace.dim_ad_format`: `ad_format_id`, `ad_format_code`, `ad_format_name`
- `broadline.marketplace.dim_process_type`: `process_type_id`, `process_type_code`, `process_type_name`
- `broadline.marketplace.fact_advertising_impressions`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `product_category_id`, `impression_count`, `click_count`
- `broadline.marketplace.fact_search_demand`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `product_category_id`, `search_query_count`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (7) — eBay

For eBay, What seller frictions remain after the work on authenticity and shipping cost?

- `broadline.economics.fact_shipping_economics`: `fiscal_quarter_id`, `scenario_id`, `delivery_speed_id`, `fulfillment_channel_id`, `shipping_cost_amount`, `shipping_revenue_amount`
- `broadline.operations.dim_fulfillment_channel`: `fulfillment_channel_id`, `fulfillment_channel_code`, `fulfillment_channel_name`
- `broadline.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `broadline.economics.fact_advertising_revenue`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `advertising_revenue_amount`
- `broadline.economics.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `region_id`, `operating_expense_amount`
- `broadline.economics.fact_seller_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `seller_type_id`, `fulfillment_channel_id`, `seller_service_revenue_amount`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (6) — eBay

For eBay, What revenue synergies come from listing across Depop and eBay in both directions?

- `broadline.economics.fact_ebay_revenue`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `ebay_revenue_amount`
- `broadline.economics.fact_promoted_listing_economics`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `product_category_id`, `promoted_listing_revenue_amount`
- `broadline.economics.fact_advertising_revenue`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `advertising_revenue_amount`
- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.marketplace.dim_ad_format`: `ad_format_id`, `ad_format_code`, `ad_format_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (1) — eBay

For eBay, Why isn’t strong growth showing up as much margin upside, and where are the incremental investments, including product development?

- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `gross_margin_percent`
- `broadline.economics.fact_payment_revenue`: `fiscal_quarter_id`, `scenario_id`, `payment_method_id`, `process_type_id`, `payment_revenue_amount`, `payment_volume_amount`
- `broadline.economics.fact_promoted_listing_economics`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `product_category_id`, `promoted_listing_revenue_amount`
- `broadline.marketplace.dim_ad_format`: `ad_format_id`, `ad_format_code`, `ad_format_name`
- `broadline.economics.fact_advertising_revenue`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `advertising_revenue_amount`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (4) — eBay

For eBay, Can the friction reduction that worked in trading cards be repeated in other categories?

- `broadline.economics.fact_selling_price_rate`: `fiscal_quarter_id`, `scenario_id`, `product_category_id`, `seller_type_id`, `average_selling_price_amount`
- `broadline.marketplace.fact_advertising_impressions`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `product_category_id`, `impression_count`, `click_count`
- `broadline.marketplace.fact_marketplace_orders`: `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `product_category_id`, `seller_type_id`, `buyer_type_id`, `order_count`, `unit_quantity`
- `broadline.economics.fact_advertising_revenue`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `advertising_revenue_amount`
- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `gross_margin_percent`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
