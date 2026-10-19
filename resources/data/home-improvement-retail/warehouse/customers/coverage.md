# Hardware Store Inc customers slice

Customer and transaction quantity facts. Ticket dollars are not stored here; transaction_count is the average-ticket denominator.

## Numbered questions

### Q2 FY2026 (1) — Home Depot

For Home Depot, Which of the many stronger categories are leading, and how should those look in the back half?

- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (2) — Home Depot

For Home Depot, Why are total company comps so far from U.S. Home Depot comps, once SRS is separated?

- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.customers.dim_fulfillment_type`: `fulfillment_type_id`, `fulfillment_type_code`, `fulfillment_type_name`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (4) — Home Depot

For Home Depot, How much of the quarter was Home Depot’s own actions versus customers coming back to home improvement?

- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.fact_pro_order_activity`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `sales_channel_id`, `pro_account_count`, `order_count`
- `hardwarestore.customers.fact_project_demand`: `fiscal_quarter_id`, `scenario_id`, `project_type_id`, `customer_type_id`, `region_id`, `project_count`, `consultation_count`
- `hardwarestore.customers.fact_sales_transactions`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `transaction_count`, `unit_quantity`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (2) — Home Depot

For Home Depot, Which demand pieces are still stuck — existing-home sales, financing — even though comps have stabilized?

- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_fulfillment_type`: `fulfillment_type_id`, `fulfillment_type_code`, `fulfillment_type_name`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (3) — Home Depot

For Home Depot, How is Pro progress being measured when the business is only slightly up?

- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.fact_pro_order_activity`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `sales_channel_id`, `pro_account_count`, `order_count`
- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.economics.fact_pro_sales`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `pro_sales_amount`
- `hardwarestore.operations.dim_employee_group`: `employee_group_id`, `employee_group_code`, `employee_group_name`
- `hardwarestore.customers.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (4) — Home Depot

For Home Depot, Is home-improvement demand in a longer soft period because housing is less affordable and rates are higher?

- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.fact_weather_demand`: `fiscal_quarter_id`, `scenario_id`, `weather_type_id`, `region_id`, `department_id`, `weather_transaction_count`
- `hardwarestore.customers.dim_fulfillment_type`: `fulfillment_type_id`, `fulfillment_type_code`, `fulfillment_type_name`
- `hardwarestore.customers.dim_weather_type`: `weather_type_id`, `weather_type_code`, `weather_type_name`
- `hardwarestore.customers.fact_project_demand`: `fiscal_quarter_id`, `scenario_id`, `project_type_id`, `customer_type_id`, `region_id`, `project_count`, `consultation_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (5) — Home Depot

For Home Depot, Does success in wholesale mean roofing and drywall grow on their own, or do they have to cross-sell into the Pro?

- `hardwarestore.customers.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `hardwarestore.customers.dim_promotion_type`: `promotion_type_id`, `promotion_type_code`, `promotion_type_name`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.fact_pro_order_activity`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `sales_channel_id`, `pro_account_count`, `order_count`
- `hardwarestore.economics.fact_pro_sales`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `pro_sales_amount`
- `hardwarestore.operations.dim_employee_group`: `employee_group_id`, `employee_group_code`, `employee_group_name`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (6) — Home Depot

For Home Depot, Has the gap between the best and worst markets changed?

- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.fact_market_transactions`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `department_id`, `region_id`, `competitor_transaction_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (2) — Home Depot

For Home Depot, How did markets with weak housing turnover, such as Florida and Texas, compare with markets where turnover looked more normal, into early 2026?

- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.dim_weather_type`: `weather_type_id`, `weather_type_code`, `weather_type_name`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (4) — Home Depot

For Home Depot, Is the customer more value-conscious, and is spending lower when a home does turn over?

- `hardwarestore.customers.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `hardwarestore.customers.dim_fulfillment_type`: `fulfillment_type_id`, `fulfillment_type_code`, `fulfillment_type_name`
- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.dim_project_type`: `project_type_id`, `project_type_code`, `project_type_name`
- `hardwarestore.customers.fact_credit_accounts`: `fiscal_quarter_id`, `scenario_id`, `payment_type_id`, `customer_type_id`, `credit_account_count`, `active_cardholder_count`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2025 (1) — Home Depot

For Home Depot, Was the hope for better demand later in the year based on housing, or on something Home Depot itself would do?

- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_fulfillment_type`: `fulfillment_type_id`, `fulfillment_type_code`, `fulfillment_type_name`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `hardwarestore.customers.dim_weather_type`: `weather_type_id`, `weather_type_code`, `weather_type_name`

### Q3 FY2025 (3) — Home Depot

For Home Depot, Can home-improvement demand recover without more housing activity or lower interest rates?

- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.dim_fulfillment_type`: `fulfillment_type_id`, `fulfillment_type_code`, `fulfillment_type_name`
- `hardwarestore.customers.dim_weather_type`: `weather_type_id`, `weather_type_code`, `weather_type_name`
- `hardwarestore.customers.fact_pro_order_activity`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `sales_channel_id`, `pro_account_count`, `order_count`
- `hardwarestore.customers.fact_project_demand`: `fiscal_quarter_id`, `scenario_id`, `project_type_id`, `customer_type_id`, `region_id`, `project_count`, `consultation_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2025 (7) — Home Depot

For Home Depot, Is there evidence of fatigue among higher-income customers as white-collar job losses show up?

- `hardwarestore.customers.fact_services_demand`: `fiscal_quarter_id`, `scenario_id`, `retail_service_id`, `customer_type_id`, `department_id`, `service_job_count`, `rental_count`
- `hardwarestore.customers.fact_project_demand`: `fiscal_quarter_id`, `scenario_id`, `project_type_id`, `customer_type_id`, `region_id`, `project_count`, `consultation_count`
- `hardwarestore.customers.fact_quote_pipeline`: `fiscal_quarter_id`, `scenario_id`, `project_type_id`, `customer_type_id`, `region_id`, `quote_count`, `booked_job_count`
- `hardwarestore.customers.fact_seasonal_demand`: `fiscal_quarter_id`, `scenario_id`, `season_id`, `department_id`, `customer_type_id`, `seasonal_transaction_count`
- `hardwarestore.economics.fact_credit_income`: `fiscal_quarter_id`, `scenario_id`, `payment_type_id`, `customer_type_id`, `credit_income_amount`
- `hardwarestore.customers.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2027 (3) — Lowe's

For Lowe's, How unusual was the July promotional environment, and how much of the comp did it take?

- `hardwarestore.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `sales_channel_id`, `advertising_amount`
- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.economics.fact_markdown_economics`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `department_id`, `clearance_sales_amount`, `markdown_amount`
- `hardwarestore.customers.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.dim_promotion_type`: `promotion_type_id`, `promotion_type_code`, `promotion_type_name`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2027 (4) — Lowe's

For Lowe's, How do coastal housing markets compare with softer inland markets in Lowe’s results?

- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2027 (5) — Lowe's

For Lowe's, After a rain-hit holiday weekend, how should last year’s weather shift be read against this year’s seasonal demand?

- `hardwarestore.customers.dim_weather_type`: `weather_type_id`, `weather_type_code`, `weather_type_name`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.fact_seasonal_demand`: `fiscal_quarter_id`, `scenario_id`, `season_id`, `department_id`, `customer_type_id`, `seasonal_transaction_count`
- `hardwarestore.customers.fact_weather_demand`: `fiscal_quarter_id`, `scenario_id`, `weather_type_id`, `region_id`, `department_id`, `weather_transaction_count`
- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.economics.fact_seasonal_sales`: `fiscal_quarter_id`, `scenario_id`, `season_id`, `department_id`, `seasonal_sales_amount`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (2) — Lowe's

For Lowe's, How much of the recent consumer strength is tax stimulus rather than a better home-improvement backdrop?

- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.dim_fulfillment_type`: `fulfillment_type_id`, `fulfillment_type_code`, `fulfillment_type_name`
- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.dim_weather_type`: `weather_type_id`, `weather_type_code`, `weather_type_name`
- `hardwarestore.customers.fact_project_demand`: `fiscal_quarter_id`, `scenario_id`, `project_type_id`, `customer_type_id`, `region_id`, `project_count`, `consultation_count`
- `hardwarestore.customers.fact_seasonal_demand`: `fiscal_quarter_id`, `scenario_id`, `season_id`, `department_id`, `customer_type_id`, `seasonal_transaction_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (6) — Lowe's

For Lowe's, How large is exposure to the big projects that are the weakest part of demand?

- `hardwarestore.customers.fact_project_demand`: `fiscal_quarter_id`, `scenario_id`, `project_type_id`, `customer_type_id`, `region_id`, `project_count`, `consultation_count`
- `hardwarestore.customers.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `hardwarestore.customers.dim_project_type`: `project_type_id`, `project_type_code`, `project_type_name`
- `hardwarestore.customers.dim_weather_type`: `weather_type_id`, `weather_type_code`, `weather_type_name`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.fact_pro_order_activity`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `sales_channel_id`, `pro_account_count`, `order_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (2) — Lowe's

For Lowe's, After storms contributed about 50 basis points, what does underlying demand look like?

- `hardwarestore.customers.dim_weather_type`: `weather_type_id`, `weather_type_code`, `weather_type_name`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (3) — Lowe's

For Lowe's, How should lawn, landscape, and exterior demand recover after storms and a hard winter?

- `hardwarestore.customers.dim_weather_type`: `weather_type_id`, `weather_type_code`, `weather_type_name`
- `hardwarestore.customers.fact_seasonal_demand`: `fiscal_quarter_id`, `scenario_id`, `season_id`, `department_id`, `customer_type_id`, `seasonal_transaction_count`
- `hardwarestore.customers.dim_department`: `department_id`, `department_code`, `department_name`
- `hardwarestore.customers.dim_project_type`: `project_type_id`, `project_type_code`, `project_type_name`
- `hardwarestore.customers.dim_promotion_type`: `promotion_type_id`, `promotion_type_code`, `promotion_type_name`
- `hardwarestore.customers.dim_season`: `season_id`, `season_code`, `season_name`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (4) — Lowe's

For Lowe's, What sales actions are aimed at the cost-cautious customer in the coming year?

- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.fact_pro_order_activity`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `sales_channel_id`, `pro_account_count`, `order_count`
- `hardwarestore.customers.fact_sales_transactions`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `transaction_count`, `unit_quantity`
- `hardwarestore.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `hardwarestore.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `sales_channel_id`, `advertising_amount`
- `hardwarestore.economics.fact_average_ticket_rate`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `average_ticket_amount`, `average_units_per_transaction_rate`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (6) — Lowe's

For Lowe's, If the year lands well above or below a wider-than-usual outlook range, what would have to be true in demand?

- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_weather_type`: `weather_type_id`, `weather_type_code`, `weather_type_name`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.fact_project_demand`: `fiscal_quarter_id`, `scenario_id`, `project_type_id`, `customer_type_id`, `region_id`, `project_count`, `consultation_count`
- `hardwarestore.customers.fact_seasonal_demand`: `fiscal_quarter_id`, `scenario_id`, `season_id`, `department_id`, `customer_type_id`, `seasonal_transaction_count`
- `hardwarestore.customers.fact_services_demand`: `fiscal_quarter_id`, `scenario_id`, `retail_service_id`, `customer_type_id`, `department_id`, `service_job_count`, `rental_count`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2025 (2) — Lowe's

For Lowe's, Who are the acquired customers, and how do they overlap with Lowe’s existing Pro base?

- `hardwarestore.customers.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `hardwarestore.customers.fact_pro_order_activity`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `sales_channel_id`, `pro_account_count`, `order_count`
- `hardwarestore.economics.fact_pro_sales`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `pro_sales_amount`
- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.dim_project_type`: `project_type_id`, `project_type_code`, `project_type_name`
- `hardwarestore.customers.dim_promotion_type`: `promotion_type_id`, `promotion_type_code`, `promotion_type_name`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2025 (4) — Lowe's

For Lowe's, How much seasonal demand, on the order of the cited shift, moved between quarters because of weather?

- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.fact_online_orders`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `fulfillment_type_id`, `department_id`, `online_order_count`, `online_unit_quantity`
- `hardwarestore.customers.fact_pro_order_activity`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `sales_channel_id`, `pro_account_count`, `order_count`
- `hardwarestore.customers.fact_seasonal_demand`: `fiscal_quarter_id`, `scenario_id`, `season_id`, `department_id`, `customer_type_id`, `seasonal_transaction_count`
- `hardwarestore.customers.fact_weather_demand`: `fiscal_quarter_id`, `scenario_id`, `weather_type_id`, `region_id`, `department_id`, `weather_transaction_count`
- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
