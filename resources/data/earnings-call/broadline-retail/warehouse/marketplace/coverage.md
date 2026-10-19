# Broadline Inc marketplace slice

Marketplace, cloud-usage and shipment quantity facts, split by process and by Amazon versus eBay activity axes.

## Numbered questions

### Q2 2026 (4) — Amazon

For Amazon, Can spending on long-lived data centers slow in 2027, or do new sites still have to open for the demand already visible?

- `broadline.operations.fact_data_center_power`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `cloud_customer_type_id`, `power_megawatt_capacity`, `site_count`
- `broadline.economics.fact_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `logistics_asset_id`, `region_id`, `capital_expenditure_amount`
- `broadline.economics.fact_cloud_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `region_id`, `cloud_capital_expenditure_amount`
- `broadline.operations.fact_cloud_capacity`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `region_id`, `compute_capacity_vcpu_count`, `data_center_count`
- `broadline.marketplace.fact_search_demand`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `product_category_id`, `search_query_count`
- `broadline.operations.dim_logistics_asset`: `logistics_asset_id`, `logistics_asset_code`, `logistics_asset_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (2) — Amazon

For Amazon, How broad is the AWS backlog beyond the largest labs?

- `broadline.operations.dim_cloud_customer_type`: `cloud_customer_type_id`, `cloud_customer_type_code`, `cloud_customer_type_name`
- `broadline.economics.fact_aws_economics`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_revenue_amount`, `cloud_operating_income_amount`
- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `total_net_sales_amount`, `operating_income_amount`, `net_income_amount`, `free_cash_flow_amount`
- `broadline.marketplace.dim_amazon_business_activity`: `amazon_business_activity_id`, `amazon_business_activity_code`, `amazon_business_activity_name`
- `broadline.marketplace.dim_amazon_reporting_segment`: `amazon_reporting_segment_id`, `amazon_reporting_segment_code`, `amazon_reporting_segment_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (3) — Amazon

For Amazon, What has to be true in 2026 for Rufus and agentic shopping to count as progress?

- `broadline.marketplace.dim_process_type`: `process_type_id`, `process_type_code`, `process_type_name`
- `broadline.marketplace.fact_advertising_impressions`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `product_category_id`, `impression_count`, `click_count`
- `broadline.marketplace.fact_amazon_unit_sales`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `fulfillment_channel_id`, `unit_sold_count`
- `broadline.marketplace.fact_cloud_usage`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `region_id`, `compute_hour_quantity`, `api_request_count`
- `broadline.marketplace.fact_digital_content_usage`: `fiscal_quarter_id`, `scenario_id`, `subscription_type_id`, `product_category_id`, `stream_count`, `download_count`
- `broadline.marketplace.fact_grocery_orders`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `region_id`, `grocery_order_count`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (1) — Amazon

For Amazon, How capacity-constrained is AWS, and is Trainium demand spreading beyond the largest customers?

- `broadline.economics.fact_aws_economics`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_revenue_amount`, `cloud_operating_income_amount`
- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.operations.fact_cloud_region_capacity`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_region_count`, `availability_zone_count`
- `broadline.operations.fact_data_center_power`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `cloud_customer_type_id`, `power_megawatt_capacity`, `site_count`
- `broadline.marketplace.dim_amazon_business_activity`: `amazon_business_activity_id`, `amazon_business_activity_code`, `amazon_business_activity_name`
- `broadline.marketplace.dim_amazon_reporting_segment`: `amazon_reporting_segment_id`, `amazon_reporting_segment_code`, `amazon_reporting_segment_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (2) — Amazon

For Amazon, What does Trainium3 still have to prove to win broader adoption instead of filling demand with third-party chips?

- `broadline.economics.fact_seller_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `seller_type_id`, `fulfillment_channel_id`, `seller_service_revenue_amount`
- `broadline.marketplace.dim_amazon_business_activity`: `amazon_business_activity_id`, `amazon_business_activity_code`, `amazon_business_activity_name`
- `broadline.marketplace.dim_process_type`: `process_type_id`, `process_type_code`, `process_type_name`
- `broadline.marketplace.dim_seller_type`: `seller_type_id`, `seller_type_code`, `seller_type_name`
- `broadline.marketplace.fact_search_demand`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `product_category_id`, `search_query_count`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (3) — Amazon

For Amazon, How is Project Rainier different for customers, will it extend past Anthropic, and how is it repeated on Trainium3?

- `broadline.economics.fact_aws_economics`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_revenue_amount`, `cloud_operating_income_amount`
- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.marketplace.fact_cloud_usage`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `region_id`, `compute_hour_quantity`, `api_request_count`
- `broadline.operations.dim_cloud_customer_type`: `cloud_customer_type_id`, `cloud_customer_type_code`, `cloud_customer_type_name`
- `broadline.operations.fact_cloud_region_capacity`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_region_count`, `availability_zone_count`
- `broadline.operations.fact_data_center_power`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `cloud_customer_type_id`, `power_megawatt_capacity`, `site_count`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (1) — eBay

For eBay, Can eBay Live’s higher buyer engagement extend to other categories and a wider buyer base?

- `broadline.marketplace.fact_ebay_listing_activity`: `fiscal_quarter_id`, `scenario_id`, `listing_type_id`, `product_category_id`, `listing_count`, `live_listing_count`
- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.economics.fact_promoted_listing_economics`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `product_category_id`, `promoted_listing_revenue_amount`
- `broadline.marketplace.fact_ebay_transaction_volume`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `ebay_transaction_count`, `item_sold_count`
- `broadline.marketplace.fact_marketplace_orders`: `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `product_category_id`, `seller_type_id`, `buyer_type_id`, `order_count`, `unit_quantity`
- `broadline.economics.fact_ebay_revenue`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `ebay_revenue_amount`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (4) — eBay

For eBay, Did the Western Europe response — shifting fees from sellers toward buyers, then cutting fees — change the take-rate model Depop or eBay should expect?

- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.economics.fact_selling_price_rate`: `fiscal_quarter_id`, `scenario_id`, `product_category_id`, `seller_type_id`, `average_selling_price_amount`
- `broadline.marketplace.fact_marketplace_orders`: `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `product_category_id`, `seller_type_id`, `buyer_type_id`, `order_count`, `unit_quantity`
- `broadline.economics.fact_advertising_revenue`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `advertising_revenue_amount`
- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (5) — eBay

For eBay, As eBay laps nondurable category boosts, what supports organic GMV still running near 10%?

- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.marketplace.fact_ebay_transaction_volume`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `ebay_transaction_count`, `item_sold_count`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.economics.fact_promoted_listing_economics`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `product_category_id`, `promoted_listing_revenue_amount`
- `broadline.marketplace.fact_ebay_listing_activity`: `fiscal_quarter_id`, `scenario_id`, `listing_type_id`, `product_category_id`, `listing_count`, `live_listing_count`
- `broadline.economics.fact_ebay_revenue`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `ebay_revenue_amount`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (6) — eBay

For eBay, How deep is seller and buyer participation in eBay Live after several quarters of very fast growth, and how is AI changing merchandising there?

- `broadline.marketplace.fact_ebay_listing_activity`: `fiscal_quarter_id`, `scenario_id`, `listing_type_id`, `product_category_id`, `listing_count`, `live_listing_count`
- `broadline.marketplace.fact_marketplace_orders`: `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `product_category_id`, `seller_type_id`, `buyer_type_id`, `order_count`, `unit_quantity`
- `broadline.economics.fact_advertising_revenue`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `advertising_revenue_amount`
- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.economics.fact_ebay_revenue`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `ebay_revenue_amount`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (7) — eBay

For eBay, What longer-term GMV growth rate is realistic after the post-pandemic climb?

- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `gross_margin_percent`
- `broadline.economics.fact_selling_price_rate`: `fiscal_quarter_id`, `scenario_id`, `product_category_id`, `seller_type_id`, `average_selling_price_amount`
- `broadline.marketplace.fact_ebay_transaction_volume`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `ebay_transaction_count`, `item_sold_count`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (8) — eBay

For eBay, As advertising penetration nears about 3% of GMV, when should ad growth converge with GMV growth?

- `broadline.economics.fact_advertising_revenue`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `advertising_revenue_amount`
- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.marketplace.dim_ad_format`: `ad_format_id`, `ad_format_code`, `ad_format_name`
- `broadline.marketplace.dim_process_type`: `process_type_id`, `process_type_code`, `process_type_name`
- `broadline.marketplace.fact_advertising_impressions`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `seller_type_id`, `product_category_id`, `impression_count`, `click_count`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (9) — eBay

For eBay, How much of GMV strength is order volume versus average selling price, and has core eBay pulled demand forward excluding Depop?

- `broadline.economics.fact_selling_price_rate`: `fiscal_quarter_id`, `scenario_id`, `product_category_id`, `seller_type_id`, `average_selling_price_amount`
- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.marketplace.fact_ebay_transaction_volume`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `ebay_transaction_count`, `item_sold_count`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.marketplace.dim_ebay_business_activity`: `ebay_business_activity_id`, `ebay_business_activity_code`, `ebay_business_activity_name`
- `broadline.marketplace.dim_listing_type`: `listing_type_id`, `listing_type_code`, `listing_type_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (1) — eBay

For eBay, Why did GMV grow so much faster than the 6% U.S. buyer growth, and how do order frequency and selling price explain that?

- `broadline.economics.fact_selling_price_rate`: `fiscal_quarter_id`, `scenario_id`, `product_category_id`, `seller_type_id`, `average_selling_price_amount`
- `broadline.marketplace.fact_marketplace_orders`: `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `product_category_id`, `seller_type_id`, `buyer_type_id`, `order_count`, `unit_quantity`
- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.marketplace.dim_buyer_type`: `buyer_type_id`, `buyer_type_code`, `buyer_type_name`
- `broadline.marketplace.dim_listing_type`: `listing_type_id`, `listing_type_code`, `listing_type_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (3) — eBay

For eBay, With weaker sentiment but still-strong spending, what is assumed for the rest of the year?

- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.fact_ebay_transaction_volume`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `ebay_transaction_count`, `item_sold_count`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (4) — eBay

For eBay, On a two-year stack, what would stop the current GMV momentum from continuing?

- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.fact_ebay_transaction_volume`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `ebay_transaction_count`, `item_sold_count`
- `broadline.operations.dim_delivery_speed`: `delivery_speed_id`, `delivery_speed_code`, `delivery_speed_name`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (5) — eBay

For eBay, What investments matter most over the next six to twelve months to keep enthusiast buyers growing?

- `broadline.marketplace.dim_buyer_type`: `buyer_type_id`, `buyer_type_code`, `buyer_type_name`
- `broadline.marketplace.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `broadline.marketplace.fact_marketplace_orders`: `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `product_category_id`, `seller_type_id`, `buyer_type_id`, `order_count`, `unit_quantity`
- `broadline.marketplace.fact_marketplace_users`: `fiscal_quarter_id`, `scenario_id`, `buyer_type_id`, `region_id`, `active_buyer_count`
- `broadline.operations.dim_delivery_speed`: `delivery_speed_id`, `delivery_speed_code`, `delivery_speed_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (1) — eBay

For eBay, Beyond short-lived category boosts, what structural change is behind the jump to double-digit growth?

- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.marketplace.fact_ebay_transaction_volume`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `ebay_transaction_count`, `item_sold_count`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `gross_margin_percent`
- `broadline.economics.fact_promoted_listing_economics`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `product_category_id`, `promoted_listing_revenue_amount`
- `broadline.economics.fact_selling_price_rate`: `fiscal_quarter_id`, `scenario_id`, `product_category_id`, `seller_type_id`, `average_selling_price_amount`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (2) — eBay

For eBay, How much of this year’s GMV guide comes from newer bets such as Caramel and eBay Live?

- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.marketplace.fact_ebay_listing_activity`: `fiscal_quarter_id`, `scenario_id`, `listing_type_id`, `product_category_id`, `listing_count`, `live_listing_count`
- `broadline.marketplace.fact_ebay_transaction_volume`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `ebay_transaction_count`, `item_sold_count`
- `broadline.economics.fact_ebay_revenue`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `ebay_revenue_amount`
- `broadline.economics.fact_promoted_listing_economics`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `product_category_id`, `promoted_listing_revenue_amount`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (3) — eBay

For eBay, Are competitive conditions changing in key international markets where macro is already weighing on growth?

- `broadline.marketplace.dim_region`: `region_id`, `region_code`, `region_name`
- `broadline.marketplace.fact_market_orders`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `product_category_id`, `region_id`, `competitor_order_count`
- `broadline.operations.dim_delivery_speed`: `delivery_speed_id`, `delivery_speed_code`, `delivery_speed_name`
- `broadline.operations.dim_fulfillment_channel`: `fulfillment_channel_id`, `fulfillment_channel_code`, `fulfillment_channel_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (5) — eBay

For eBay, How does growth cadence through 2026 change as nondurable boosts are lapped in the second half?

- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.marketplace.fact_ebay_transaction_volume`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `ebay_transaction_count`, `item_sold_count`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `gross_margin_percent`
- `broadline.economics.fact_promoted_listing_economics`: `fiscal_quarter_id`, `scenario_id`, `ad_format_id`, `product_category_id`, `promoted_listing_revenue_amount`
- `broadline.economics.fact_selling_price_rate`: `fiscal_quarter_id`, `scenario_id`, `product_category_id`, `seller_type_id`, `average_selling_price_amount`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (7) — eBay

For eBay, Is the long-term payoff from eBay Live more transaction volume, a new customer group, or engagement?

- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.marketplace.fact_ebay_transaction_volume`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `ebay_transaction_count`, `item_sold_count`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.economics.fact_payment_revenue`: `fiscal_quarter_id`, `scenario_id`, `payment_method_id`, `process_type_id`, `payment_revenue_amount`, `payment_volume_amount`
- `broadline.marketplace.fact_ebay_listing_activity`: `fiscal_quarter_id`, `scenario_id`, `listing_type_id`, `product_category_id`, `listing_count`, `live_listing_count`
- `broadline.economics.fact_cloud_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `cloud_service_id`, `cloud_customer_type_id`, `cloud_operating_margin_percent`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (8) — eBay

For eBay, How sustainable is the trading-card business into tougher comparisons?

- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.marketplace.fact_ebay_transaction_volume`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `ebay_transaction_count`, `item_sold_count`
- `broadline.economics.fact_ebay_revenue`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `ebay_revenue_amount`
- `broadline.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `amazon_business_activity_id`, `product_category_id`, `gross_margin_percent`
- `broadline.marketplace.dim_buyer_type`: `buyer_type_id`, `buyer_type_code`, `buyer_type_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (2) — eBay

For eBay, How much of the marketplace acceleration is temporary to this year versus durable into 2026?

- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.economics.fact_selling_price_rate`: `fiscal_quarter_id`, `scenario_id`, `product_category_id`, `seller_type_id`, `average_selling_price_amount`
- `broadline.marketplace.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `broadline.marketplace.dim_ebay_business_activity`: `ebay_business_activity_id`, `ebay_business_activity_code`, `ebay_business_activity_name`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (5) — eBay

For eBay, What are the three points of headwind inside the 2026 view of positive GMV growth?

- `broadline.economics.fact_ebay_gmv`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `gross_merchandise_value_amount`
- `broadline.economics.fact_ebay_take_rate`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `listing_type_id`, `marketplace_take_rate_percent`
- `broadline.marketplace.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `broadline.marketplace.fact_ebay_transaction_volume`: `fiscal_quarter_id`, `scenario_id`, `ebay_business_activity_id`, `product_category_id`, `listing_type_id`, `ebay_transaction_count`, `item_sold_count`
- `broadline.marketplace.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `broadline.marketplace.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
