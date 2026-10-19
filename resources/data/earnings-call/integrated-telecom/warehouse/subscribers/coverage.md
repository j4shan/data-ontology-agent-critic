# Carrier Inc subscribers slice

Subscriber quantity facts. A quantity fact does not store a price.

## Numbered questions

### Q1 2026 (1) — AT&T

For AT&T, How widely will OneConnect be rolled out, what advertising and target market support it, and can it add subscribers in the near term?

- `carrier.subscribers.dim_movement_type`: `movement_type_id`, `movement_type_code`, `movement_type_name`
- `carrier.subscribers.fact_market_subscribers`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `service_id`, `region_id`, `competitor_subscriber_count`
- `carrier.subscribers.fact_promotional_additions`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `sales_channel_id`, `promotional_gross_add_count`
- `carrier.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `customer_segment_id`, `advertising_amount`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (2) — AT&T

For AT&T, Can the recent improvement in phone churn hold after a period of double-digit pressure?

- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.economics.fact_customer_lifetime_value_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `lifetime_value_amount`
- `carrier.subscribers.dim_att_reporting_segment`: `att_reporting_segment_id`, `att_reporting_segment_code`, `att_reporting_segment_name`
- `carrier.subscribers.dim_enterprise_product`: `enterprise_product_id`, `enterprise_product_code`, `enterprise_product_name`
- `carrier.subscribers.dim_service`: `service_id`, `service_code`, `service_name`
- `carrier.subscribers.fact_phone_connections`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `device_type_id`, `region_id`, `phone_connection_count`, `connection_count`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (4) — AT&T

For AT&T, What is driving sequential account growth in consumer and mobility?

- `carrier.subscribers.dim_att_reporting_segment`: `att_reporting_segment_id`, `att_reporting_segment_code`, `att_reporting_segment_name`
- `carrier.subscribers.dim_service`: `service_id`, `service_code`, `service_name`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.subscribers.dim_contract_type`: `contract_type_id`, `contract_type_code`, `contract_type_name`
- `carrier.subscribers.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `carrier.subscribers.dim_enterprise_product`: `enterprise_product_id`, `enterprise_product_code`, `enterprise_product_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (7) — AT&T

For AT&T, Will the shift from device subsidies toward competing on service be gradual as OneConnect scales, or a sharper change in plans?

- `carrier.subscribers.dim_promotion_type`: `promotion_type_id`, `promotion_type_code`, `promotion_type_name`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.economics.fact_device_subsidy_rate`: `fiscal_quarter_id`, `scenario_id`, `device_type_id`, `financing_type_id`, `promotion_type_id`, `subsidy_amount_per_device`, `subsidy_amount`
- `carrier.subscribers.dim_financing_type`: `financing_type_id`, `financing_type_code`, `financing_type_name`
- `carrier.subscribers.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (8) — AT&T

For AT&T, As the DSL base fades, does that change the broadband growth outlook, including beyond AT&T’s own lines?

- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.network.dim_network_technology`: `network_technology_id`, `network_technology_code`, `network_technology_name`
- `carrier.subscribers.dim_service`: `service_id`, `service_code`, `service_name`
- `carrier.subscribers.dim_speed_tier`: `speed_tier_id`, `speed_tier_code`, `speed_tier_name`
- `carrier.subscribers.fact_fiber_penetration_base`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_subscriber_count`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (1) — AT&T

For AT&T, Where can the fiber convergence rate go over the decade, will penetration keep rising, and can former Lumen areas catch up?

- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.subscribers.fact_fiber_penetration_base`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_subscriber_count`
- `carrier.network.dim_footprint_type`: `footprint_type_id`, `footprint_type_code`, `footprint_type_name`
- `carrier.network.fact_fiber_route_capacity`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_route_mile_count`, `strand_mile_count`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (3) — AT&T

For AT&T, Which macro factors — population, immigration, business demand, prepaid-to-postpaid moves — shape 2026 postpaid phone growth, and how is AT&T answering competitors’ promotions?

- `carrier.subscribers.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.economics.fact_customer_lifetime_value_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `lifetime_value_amount`
- `carrier.economics.fact_device_subsidy_rate`: `fiscal_quarter_id`, `scenario_id`, `device_type_id`, `financing_type_id`, `promotion_type_id`, `subsidy_amount_per_device`, `subsidy_amount`
- `carrier.economics.fact_promotion_economics`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `promotion_amount`, `promotion_amortization_amount`
- `carrier.subscribers.dim_att_reporting_segment`: `att_reporting_segment_id`, `att_reporting_segment_code`, `att_reporting_segment_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (1) — AT&T

For AT&T, Should phone churn rise again in the second half the way it did this quarter, given competition and installment cohorts rolling off?

- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.economics.fact_customer_lifetime_value_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `lifetime_value_amount`
- `carrier.subscribers.fact_phone_connections`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `device_type_id`, `region_id`, `phone_connection_count`, `connection_count`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_bad_debt_expense`: `fiscal_quarter_id`, `scenario_id`, `customer_segment_id`, `plan_type_id`, `bad_debt_amount`
- `carrier.network.fact_capital_project_capacity`: `fiscal_quarter_id`, `scenario_id`, `initiative_id`, `network_technology_id`, `region_id`, `project_count`, `location_under_construction_count`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (6) — AT&T

For AT&T, Does a higher-churn, higher-gross-add industry still leave room for mobility margin expansion after 2025?

- `carrier.subscribers.fact_promotional_additions`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `sales_channel_id`, `promotional_gross_add_count`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.economics.fact_segment_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `ebitda_margin_percent`, `service_margin_percent`
- `carrier.network.dim_footprint_type`: `footprint_type_id`, `footprint_type_code`, `footprint_type_name`
- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.subscribers.dim_att_reporting_segment`: `att_reporting_segment_id`, `att_reporting_segment_code`, `att_reporting_segment_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (7) — AT&T

For AT&T, Are fiber and fixed wireless aimed at different customers, or does fixed wireless feed fiber and lower acquisition cost?

- `carrier.subscribers.dim_service`: `service_id`, `service_code`, `service_name`
- `carrier.subscribers.fact_fixed_wireless_subscribers`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `customer_segment_id`, `fixed_wireless_subscriber_count`
- `carrier.network.dim_network_technology`: `network_technology_id`, `network_technology_code`, `network_technology_name`
- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (3) — AT&T

For AT&T, Is fiber inside AT&T’s territory kept only for AT&T, or can others use it?

- `carrier.subscribers.dim_att_reporting_segment`: `att_reporting_segment_id`, `att_reporting_segment_code`, `att_reporting_segment_name`
- `carrier.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `ebitda_amount`, `operating_income_amount`, `free_cash_flow_amount`
- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.economics.fact_wholesale_revenue`: `fiscal_quarter_id`, `scenario_id`, `partner_type_id`, `service_id`, `wholesale_revenue_amount`
- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.network.dim_network_technology`: `network_technology_id`, `network_technology_code`, `network_technology_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (3) — Verizon

For Verizon, Is the target of roughly 8 to 9 million fixed-wireless subscribers by 2028 still the plan?

- `carrier.subscribers.fact_fixed_wireless_subscribers`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `customer_segment_id`, `fixed_wireless_subscriber_count`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.network.dim_network_technology`: `network_technology_id`, `network_technology_code`, `network_technology_name`
- `carrier.subscribers.dim_service`: `service_id`, `service_code`, `service_name`
- `carrier.subscribers.fact_prepaid_subscribers`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `region_id`, `prepaid_subscriber_count`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (1) — Verizon

For Verizon, What investment drives the stronger 2026 postpaid phone outlook — lower churn, or more marketing and promotions for gross adds?

- `carrier.subscribers.fact_promotional_additions`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `sales_channel_id`, `promotional_gross_add_count`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.economics.fact_customer_lifetime_value_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `lifetime_value_amount`
- `carrier.economics.fact_device_subsidy_rate`: `fiscal_quarter_id`, `scenario_id`, `device_type_id`, `financing_type_id`, `promotion_type_id`, `subsidy_amount_per_device`, `subsidy_amount`
- `carrier.economics.fact_promotion_economics`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `promotion_amount`, `promotion_amortization_amount`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (3) — Verizon

For Verizon, How is Verizon keeping customer lifetime value up if the market fears values will be lower in 2026 and 2027 while selling more aggressively?

- `carrier.economics.fact_customer_lifetime_value_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `lifetime_value_amount`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.subscribers.fact_converged_subscribers`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `footprint_type_id`, `converged_household_count`, `multi_service_account_count`
- `carrier.subscribers.fact_promotional_additions`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `sales_channel_id`, `promotional_gross_add_count`
- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `customer_segment_id`, `advertising_amount`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (1) — Verizon

For Verizon, How does the new leadership expect to turn consumer volumes in the first months?

- `carrier.subscribers.dim_service`: `service_id`, `service_code`, `service_name`
- `carrier.subscribers.fact_promotional_additions`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `sales_channel_id`, `promotional_gross_add_count`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.network.dim_network_technology`: `network_technology_id`, `network_technology_code`, `network_technology_name`
- `carrier.network.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `network_technology_id`, `spectrum_band_id`, `region_id`, `network_capacity_gigabits_per_second`, `site_count`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (2) — Verizon

For Verizon, Is the existing customer base overpriced relative to the market, given the view that repeated price increases were not sustainable?

- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.subscribers.fact_subscriber_base`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `subscriber_count`, `account_count`
- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `customer_segment_id`, `advertising_amount`
- `carrier.economics.fact_bad_debt_expense`: `fiscal_quarter_id`, `scenario_id`, `customer_segment_id`, `plan_type_id`, `bad_debt_amount`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (3) — Verizon

For Verizon, Are perks and myPlan meant to work like a broader app relative to peers, and where is the benefit?

- `carrier.subscribers.fact_subscriber_base`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `subscriber_count`, `account_count`
- `carrier.subscribers.fact_subscriber_movement`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `movement_type_id`, `sales_channel_id`, `subscriber_movement_count`, `account_movement_count`
- `carrier.subscribers.fact_phone_connections`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `device_type_id`, `region_id`, `phone_connection_count`, `connection_count`
- `carrier.subscribers.fact_broadband_subscribers`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `speed_tier_id`, `footprint_type_id`, `region_id`, `broadband_subscriber_count`, `household_count`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (6) — Verizon

For Verizon, Which tools cut churn before a customer is about to leave, and where does AI help those offers?

- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.subscribers.dim_promotion_type`: `promotion_type_id`, `promotion_type_code`, `promotion_type_name`
- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `customer_segment_id`, `advertising_amount`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_bad_debt_expense`: `fiscal_quarter_id`, `scenario_id`, `customer_segment_id`, `plan_type_id`, `bad_debt_amount`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (1) — Verizon

For Verizon, What is slowing postpaid revenue-per-user growth, and why should upgrade rates fall from the teens toward mid-single digits?

- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.economics.fact_device_subsidy_rate`: `fiscal_quarter_id`, `scenario_id`, `device_type_id`, `financing_type_id`, `promotion_type_id`, `subsidy_amount_per_device`, `subsidy_amount`
- `carrier.economics.fact_customer_lifetime_value_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `lifetime_value_amount`
- `carrier.economics.fact_segment_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `ebitda_margin_percent`, `service_margin_percent`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (2) — Verizon

For Verizon, How much of consumer net adds were free lines, and is prepaid weakness migration into postpaid?

- `carrier.subscribers.dim_contract_type`: `contract_type_id`, `contract_type_code`, `contract_type_name`
- `carrier.subscribers.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `carrier.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `ebitda_amount`, `operating_income_amount`, `free_cash_flow_amount`
- `carrier.network.fact_copper_retirement_capacity`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `copper_location_retired_count`, `copper_line_count`
- `carrier.subscribers.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `carrier.subscribers.dim_movement_type`: `movement_type_id`, `movement_type_code`, `movement_type_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (5) — Verizon

For Verizon, Is fixed-wireless deployment speeding up with more investment, and is July promotion intensity like the quarter just reported?

- `carrier.subscribers.fact_fixed_wireless_subscribers`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `customer_segment_id`, `fixed_wireless_subscriber_count`
- `carrier.economics.fact_device_subsidy_rate`: `fiscal_quarter_id`, `scenario_id`, `device_type_id`, `financing_type_id`, `promotion_type_id`, `subsidy_amount_per_device`, `subsidy_amount`
- `carrier.economics.fact_promotion_economics`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `promotion_amount`, `promotion_amortization_amount`
- `carrier.network.dim_network_technology`: `network_technology_id`, `network_technology_code`, `network_technology_name`
- `carrier.network.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `network_technology_id`, `spectrum_band_id`, `region_id`, `network_capacity_gigabits_per_second`, `site_count`
- `carrier.network.fact_spectrum_deployment`: `fiscal_quarter_id`, `scenario_id`, `spectrum_band_id`, `network_technology_id`, `deployed_site_count`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (8) — Verizon

For Verizon, How sustainable is the recent jump in consumer phone gross adds, and what is the June customer-experience change, including AI, actually doing?

- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.economics.fact_customer_lifetime_value_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `lifetime_value_amount`
- `carrier.subscribers.dim_contract_type`: `contract_type_id`, `contract_type_code`, `contract_type_name`
- `carrier.subscribers.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `carrier.subscribers.dim_service`: `service_id`, `service_code`, `service_name`
- `carrier.subscribers.fact_enterprise_connections`: `fiscal_quarter_id`, `scenario_id`, `enterprise_product_id`, `customer_segment_id`, `enterprise_connection_count`, `iot_connection_count`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
