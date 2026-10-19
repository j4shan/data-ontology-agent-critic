# Hardware Store Inc operations slice

Store, distribution, inventory and workforce capacity facts. Capacity facts store no selling price.

## Numbered questions

### Q2 FY2026 (8) — Home Depot

For Home Depot, How does the roughly $400 million SRS and GMS cross-sell build from the second quarter into the second half?

- `hardwarestore.customers.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `hardwarestore.customers.fact_credit_accounts`: `fiscal_quarter_id`, `scenario_id`, `payment_type_id`, `customer_type_id`, `credit_account_count`, `active_cardholder_count`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.fact_delivery_orders`: `fiscal_quarter_id`, `scenario_id`, `fulfillment_type_id`, `customer_type_id`, `department_id`, `delivery_order_count`

### Q1 FY2026 (8) — Home Depot

For Home Depot, How fast is Pro adoption of trade credit, and how far has the merchandise execution rollout gone?

- `hardwarestore.customers.dim_promotion_type`: `promotion_type_id`, `promotion_type_code`, `promotion_type_name`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.fact_credit_accounts`: `fiscal_quarter_id`, `scenario_id`, `payment_type_id`, `customer_type_id`, `credit_account_count`, `active_cardholder_count`
- `hardwarestore.customers.fact_pro_order_activity`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `sales_channel_id`, `pro_account_count`, `order_count`
- `hardwarestore.economics.fact_credit_income`: `fiscal_quarter_id`, `scenario_id`, `payment_type_id`, `customer_type_id`, `credit_income_amount`
- `hardwarestore.economics.fact_pro_sales`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `pro_sales_amount`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (1) — Home Depot

For Home Depot, Which digital planning and delivery initiatives are the main 2026 efforts to improve value for the customer?

- `hardwarestore.customers.dim_retail_service`: `retail_service_id`, `retail_service_code`, `retail_service_name`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.fact_delivery_orders`: `fiscal_quarter_id`, `scenario_id`, `fulfillment_type_id`, `customer_type_id`, `department_id`, `delivery_order_count`
- `hardwarestore.customers.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `hardwarestore.customers.dim_department`: `department_id`, `department_code`, `department_name`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2027 (2) — Lowe's

For Lowe's, How did Foundation Building Materials and the other acquired distribution business perform, and why did the full-year outlook move toward the low end?

- `hardwarestore.customers.dim_department`: `department_id`, `department_code`, `department_name`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.fact_services_demand`: `fiscal_quarter_id`, `scenario_id`, `retail_service_id`, `customer_type_id`, `department_id`, `service_job_count`, `rental_count`
- `hardwarestore.operations.fact_distribution_capacity`: `fiscal_quarter_id`, `scenario_id`, `fulfillment_type_id`, `region_id`, `distribution_center_count`, `distribution_square_foot_count`
- `hardwarestore.operations.fact_workforce_capacity`: `fiscal_quarter_id`, `scenario_id`, `employee_group_id`, `region_id`, `employee_count`, `full_time_equivalent_count`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2025 (1) — Lowe's

For Lowe's, Which Foundation Building Materials capabilities — order management, credit, and similar tools — matter most to the Pro?

- `hardwarestore.customers.dim_department`: `department_id`, `department_code`, `department_name`
- `hardwarestore.customers.dim_promotion_type`: `promotion_type_id`, `promotion_type_code`, `promotion_type_name`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.fact_pro_order_activity`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `project_type_id`, `sales_channel_id`, `pro_account_count`, `order_count`
- `hardwarestore.customers.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2025 (3) — Lowe's

For Lowe's, What supports the implied back-half acceleration in same-store sales?

- `hardwarestore.economics.fact_average_ticket_rate`: `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `department_id`, `sales_channel_id`, `average_ticket_amount`, `average_units_per_transaction_rate`
- `hardwarestore.economics.fact_comparable_sales_rate`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `region_id`, `comparable_sales_percent`, `comparable_transaction_percent`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.fact_customer_traffic`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `store_format_id`, `region_id`, `store_visit_count`, `online_session_count`
- `hardwarestore.customers.fact_housing_market_demand`: `fiscal_quarter_id`, `scenario_id`, `housing_indicator_id`, `region_id`, `housing_start_count`, `existing_home_sale_count`
- `hardwarestore.customers.fact_online_orders`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `fulfillment_type_id`, `department_id`, `online_order_count`, `online_unit_quantity`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2025 (5) — Lowe's

For Lowe's, Does a larger Pro distribution network force a second round of investment in Lowe’s own supply chain?

- `hardwarestore.operations.dim_employee_group`: `employee_group_id`, `employee_group_code`, `employee_group_name`
- `hardwarestore.economics.dim_capital_project_type`: `capital_project_type_id`, `capital_project_type_code`, `capital_project_type_name`
- `hardwarestore.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `hardwarestore.customers.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `hardwarestore.customers.dim_promotion_type`: `promotion_type_id`, `promotion_type_code`, `promotion_type_name`
- `hardwarestore.customers.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `hardwarestore.customers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `hardwarestore.customers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
