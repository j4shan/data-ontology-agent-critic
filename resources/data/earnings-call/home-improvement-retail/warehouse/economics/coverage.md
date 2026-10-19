# Hardware Store Inc economics slice

Sales, ticket, margin, cost and capital dollars. A rate fact names its denominator fact at a joinable grain.

## Numbered questions

### Q2 FY2026 (3) — Home Depot

For Home Depot, Why does the full-year comp outlook not simply carry the second-quarter trend into an easier back half?

- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.fact_online_orders`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `fulfillment_type_id`, `department_id`, `online_order_count`, `online_unit_quantity`
- `hardwarestore.customers.fact_pro_order_activity`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `sales_channel_id`, `pro_account_count`, `order_count`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (5) — Home Depot

For Home Depot, How much of the higher average ticket was inflation on the same item versus mix or other factors?

- `hardwarestore.economics.fact_average_ticket_rate`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `average_ticket_amount`, `average_units_per_transaction_rate`
- `hardwarestore.customers.fact_sales_transactions`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `transaction_count`, `unit_quantity`
- `hardwarestore.economics.fact_competitor_price_rate`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `department_id`, `region_id`, `competitor_price_amount`
- `hardwarestore.economics.fact_selling_price_rate`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `brand_type_id`, `average_selling_price_amount`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `hardwarestore.customers.fact_services_demand`: `fiscal_quarter_id`, `scenario_id`, `retail_service_id`, `customer_type_id`, `department_id`, `service_job_count`, `rental_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`

### Q2 FY2026 (6) — Home Depot

For Home Depot, How do tariff-related price and cost effects move from this quarter into the back half and 2027, including any expense timing that offsets gross margin?

- `hardwarestore.economics.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `store_format_id`, `operating_expense_amount`
- `hardwarestore.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `brand_type_id`, `gross_margin_percent`
- `hardwarestore.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `sales_channel_id`, `advertising_amount`
- `hardwarestore.economics.fact_competitor_price_rate`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `department_id`, `region_id`, `competitor_price_amount`
- `hardwarestore.economics.fact_delivery_economics`: `fiscal_quarter_id`, `scenario_id`, `fulfillment_type_id`, `department_id`, `delivery_fee_revenue_amount`, `delivery_cost_amount`
- `hardwarestore.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`, `operating_income_amount`, `net_earnings_amount`, `free_cash_flow_amount`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (7) — Home Depot

For Home Depot, What happens to average unit retail in the back half as last year’s tariff prices are lapped but costs stay high?

- `hardwarestore.economics.fact_competitor_price_rate`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `department_id`, `region_id`, `competitor_price_amount`
- `hardwarestore.economics.fact_selling_price_rate`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `brand_type_id`, `average_selling_price_amount`
- `hardwarestore.customers.fact_sales_transactions`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `transaction_count`, `unit_quantity`
- `hardwarestore.economics.fact_average_ticket_rate`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `average_ticket_amount`, `average_units_per_transaction_rate`
- `hardwarestore.economics.fact_inventory_cost`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `supplier_type_id`, `inventory_cost_amount`, `shrink_cost_amount`
- `hardwarestore.operations.fact_inventory_availability`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `store_format_id`, `region_id`, `inventory_unit_count`, `on_hand_unit_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (1) — Home Depot

For Home Depot, How large is the big-ticket project bucket that is still weak while many individual categories are positive?

- `hardwarestore.customers.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `hardwarestore.customers.dim_project_type`: `project_type_id`, `project_type_code`, `project_type_name`
- `hardwarestore.customers.fact_pro_order_activity`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `sales_channel_id`, `pro_account_count`, `order_count`
- `hardwarestore.customers.fact_project_demand`: `fiscal_quarter_id`, `scenario_id`, `project_type_id`, `customer_type_id`, `region_id`, `project_count`, `consultation_count`
- `hardwarestore.customers.fact_quote_pipeline`: `fiscal_quarter_id`, `scenario_id`, `project_type_id`, `customer_type_id`, `region_id`, `quote_count`, `booked_job_count`
- `hardwarestore.customers.fact_sales_transactions`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `transaction_count`, `unit_quantity`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (7) — Home Depot

For Home Depot, As tariff-driven price increases are lapped, how do ticket and traffic split, and what turns traffic positive?

- `hardwarestore.customers.fact_sales_transactions`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `transaction_count`, `unit_quantity`
- `hardwarestore.economics.fact_average_ticket_rate`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `average_ticket_amount`, `average_units_per_transaction_rate`
- `hardwarestore.economics.fact_selling_price_rate`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `brand_type_id`, `average_selling_price_amount`
- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.economics.fact_competitor_price_rate`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `department_id`, `region_id`, `competitor_price_amount`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (3) — Home Depot

For Home Depot, Will SRS’s more aggressive pricing last past the first quarter and spread beyond roofing in a way that moves Home Depot’s gross margin?

- `hardwarestore.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `brand_type_id`, `gross_margin_percent`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.economics.fact_competitor_price_rate`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `department_id`, `region_id`, `competitor_price_amount`
- `hardwarestore.economics.fact_selling_price_rate`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `brand_type_id`, `average_selling_price_amount`
- `hardwarestore.operations.fact_inventory_availability`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `store_format_id`, `region_id`, `inventory_unit_count`, `on_hand_unit_count`
- `hardwarestore.customers.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (5) — Home Depot

For Home Depot, Inside the comp outlook, how do ticket and transactions move, and is big-ticket strength replacement and innovation or still held back by large projects?

- `hardwarestore.customers.fact_sales_transactions`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `transaction_count`, `unit_quantity`
- `hardwarestore.economics.fact_average_ticket_rate`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `average_ticket_amount`, `average_units_per_transaction_rate`
- `hardwarestore.economics.fact_selling_price_rate`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `brand_type_id`, `average_selling_price_amount`
- `hardwarestore.customers.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `hardwarestore.customers.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `hardwarestore.customers.dim_project_type`: `project_type_id`, `project_type_code`, `project_type_name`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (6) — Home Depot

For Home Depot, Are discretionary big-ticket projects improving, and how much of the inventory increase is GMS versus higher cost?

- `hardwarestore.economics.fact_inventory_cost`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `supplier_type_id`, `inventory_cost_amount`, `shrink_cost_amount`
- `hardwarestore.customers.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `hardwarestore.customers.dim_project_type`: `project_type_id`, `project_type_code`, `project_type_name`
- `hardwarestore.customers.fact_pro_order_activity`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `sales_channel_id`, `pro_account_count`, `order_count`
- `hardwarestore.customers.fact_project_demand`: `fiscal_quarter_id`, `scenario_id`, `project_type_id`, `customer_type_id`, `region_id`, `project_count`, `consultation_count`
- `hardwarestore.customers.fact_quote_pipeline`: `fiscal_quarter_id`, `scenario_id`, `project_type_id`, `customer_type_id`, `region_id`, `quote_count`, `booked_job_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2025 (2) — Home Depot

For Home Depot, How much of average ticket was commodities versus same-item inflation, and will the industry be more promotional in the fourth quarter?

- `hardwarestore.economics.fact_average_ticket_rate`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `average_ticket_amount`, `average_units_per_transaction_rate`
- `hardwarestore.customers.fact_sales_transactions`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `transaction_count`, `unit_quantity`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `hardwarestore.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `sales_channel_id`, `advertising_amount`
- `hardwarestore.economics.fact_competitor_price_rate`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `department_id`, `region_id`, `competitor_price_amount`
- `hardwarestore.economics.fact_markdown_economics`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `department_id`, `clearance_sales_amount`, `markdown_amount`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`

### Q3 FY2025 (4) — Home Depot

For Home Depot, Have Pro investments raised fixed costs enough that softer sales now deleverage the model?

- `hardwarestore.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.fact_pro_order_activity`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `sales_channel_id`, `pro_account_count`, `order_count`
- `hardwarestore.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `brand_type_id`, `gross_margin_percent`
- `hardwarestore.economics.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `store_format_id`, `operating_expense_amount`
- `hardwarestore.economics.fact_pro_sales`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `pro_sales_amount`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2025 (5) — Home Depot

For Home Depot, Do slower transactions and a higher ticket show price elasticity, or something else in the price changes made in the quarter?

- `hardwarestore.customers.fact_sales_transactions`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `transaction_count`, `unit_quantity`
- `hardwarestore.economics.fact_average_ticket_rate`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `average_ticket_amount`, `average_units_per_transaction_rate`
- `hardwarestore.economics.fact_selling_price_rate`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `brand_type_id`, `average_selling_price_amount`
- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.economics.fact_competitor_price_rate`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `department_id`, `region_id`, `competitor_price_amount`
- `hardwarestore.customers.fact_market_transactions`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `department_id`, `region_id`, `competitor_transaction_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2025 (6) — Home Depot

For Home Depot, How does a more cautious consumer sit next to big-ticket sales that are still outperforming?

- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.fact_sales_transactions`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `transaction_count`, `unit_quantity`
- `hardwarestore.economics.fact_average_ticket_rate`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `average_ticket_amount`, `average_units_per_transaction_rate`
- `hardwarestore.customers.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2025 (8) — Home Depot

For Home Depot, Over the next few years, how much can GMS and SRS margins improve from the current dilution?

- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `brand_type_id`, `gross_margin_percent`
- `hardwarestore.economics.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `customer_type_id`, `sales_channel_id`, `net_sales_amount`
- `hardwarestore.economics.fact_average_ticket_rate`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `average_ticket_amount`, `average_units_per_transaction_rate`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2025 (9) — Home Depot

For Home Depot, How should storm comparisons hit fourth-quarter comps and the first half of the next year?

- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.fact_online_orders`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `fulfillment_type_id`, `department_id`, `online_order_count`, `online_unit_quantity`
- `hardwarestore.customers.fact_pro_order_activity`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `sales_channel_id`, `pro_account_count`, `order_count`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2027 (1) — Lowe's

For Lowe's, What competitive pressure showed up at the end of the quarter, and how does that read against the July comparable sales?

- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.customers.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.fact_online_orders`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `fulfillment_type_id`, `department_id`, `online_order_count`, `online_unit_quantity`
- `hardwarestore.customers.fact_pro_order_activity`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `sales_channel_id`, `pro_account_count`, `order_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2027 (6) — Lowe's

For Lowe's, What changed in the second-half outlook versus the initial view that the back half would improve?

- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.fact_online_orders`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `fulfillment_type_id`, `department_id`, `online_order_count`, `online_unit_quantity`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (1) — Lowe's

For Lowe's, Was March strength a pull-forward, and how should that be set against the comp outlook?

- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.customers.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (3) — Lowe's

For Lowe's, What member-spend result is HomeCare+ supposed to produce?

- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `hardwarestore.economics.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `customer_type_id`, `sales_channel_id`, `net_sales_amount`
- `hardwarestore.economics.fact_average_ticket_rate`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `average_ticket_amount`, `average_units_per_transaction_rate`

### Q1 FY2027 (4) — Lowe's

For Lowe's, How much of the room left for promotions was used in the first quarter, and what is the promotional stance from here?

- `hardwarestore.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `sales_channel_id`, `advertising_amount`
- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.economics.fact_markdown_economics`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `department_id`, `clearance_sales_amount`, `markdown_amount`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.fact_online_orders`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `fulfillment_type_id`, `department_id`, `online_order_count`, `online_unit_quantity`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (5) — Lowe's

For Lowe's, If about 70% of categories were positive but the total comp was only slightly up, what is dragging the rest?

- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`, `operating_income_amount`, `net_earnings_amount`, `free_cash_flow_amount`
- `hardwarestore.customers.dim_housing_indicator`: `housing_indicator_id`, `housing_indicator_code`, `housing_indicator_name`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (1) — Lowe's

For Lowe's, What incremental margin is left once acquisition integration is behind the company?

- `hardwarestore.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `hardwarestore.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`, `operating_income_amount`, `net_earnings_amount`, `free_cash_flow_amount`
- `hardwarestore.economics.fact_gross_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `brand_type_id`, `gross_margin_percent`
- `hardwarestore.economics.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `store_format_id`, `operating_expense_amount`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (5) — Lowe's

For Lowe's, How should transactions and ticket move through the year?

- `hardwarestore.customers.fact_sales_transactions`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `transaction_count`, `unit_quantity`
- `hardwarestore.economics.fact_average_ticket_rate`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `average_ticket_amount`, `average_units_per_transaction_rate`
- `hardwarestore.economics.fact_selling_price_rate`: `fiscal_quarter_id`, `scenario_id`, `department_id`, `brand_type_id`, `average_selling_price_amount`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.fact_market_transactions`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `department_id`, `region_id`, `competitor_transaction_count`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
