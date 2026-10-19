# Carrier Inc economics slice

Revenue, rate, margin, cost and capital dollars. A price fact does not store unit quantity; its denominator is on a quantity fact at a joinable grain.

## Numbered questions

### Q4 2025 (2) — AT&T

For AT&T, How will fiber prices for existing customers move, given cable peers are pricing the base differently?

- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.subscribers.dim_service`: `service_id`, `service_code`, `service_name`
- `carrier.subscribers.fact_fiber_penetration_base`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_subscriber_count`
- `carrier.subscribers.fact_subscriber_base`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `subscriber_count`, `account_count`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (5) — AT&T

For AT&T, Is the path to faster EBITDA growth later in the decade more about advanced products accelerating or legacy declines easing, and how linear is 2027?

- `carrier.subscribers.dim_enterprise_product`: `enterprise_product_id`, `enterprise_product_code`, `enterprise_product_name`
- `carrier.economics.fact_segment_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `ebitda_margin_percent`, `service_margin_percent`
- `carrier.network.dim_footprint_type`: `footprint_type_id`, `footprint_type_code`, `footprint_type_name`
- `carrier.subscribers.fact_converged_subscribers`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `footprint_type_id`, `converged_household_count`, `multi_service_account_count`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_att_segment_economics`: `fiscal_quarter_id`, `scenario_id`, `att_reporting_segment_id`, `att_segment_revenue_amount`, `att_segment_ebitda_amount`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (6) — AT&T

For AT&T, What cost items made mobility service margins rise this quarter versus the rest of the year?

- `carrier.economics.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `service_id`, `operating_expense_amount`
- `carrier.economics.fact_promotion_economics`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `promotion_amount`, `promotion_amortization_amount`
- `carrier.economics.fact_segment_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `ebitda_margin_percent`, `service_margin_percent`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.economics.fact_converged_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `footprint_type_id`, `converged_revenue_amount`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (7) — AT&T

For AT&T, What is behind the step-up in bad debt, and where do cost reductions come from as EBITDA growth is expected to accelerate?

- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.economics.fact_bad_debt_expense`: `fiscal_quarter_id`, `scenario_id`, `customer_segment_id`, `plan_type_id`, `bad_debt_amount`
- `carrier.economics.fact_att_segment_economics`: `fiscal_quarter_id`, `scenario_id`, `att_reporting_segment_id`, `att_segment_revenue_amount`, `att_segment_ebitda_amount`
- `carrier.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `ebitda_amount`, `operating_income_amount`, `free_cash_flow_amount`
- `carrier.economics.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `service_id`, `operating_expense_amount`
- `carrier.economics.fact_promotion_economics`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `promotion_amount`, `promotion_amortization_amount`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (4) — AT&T

For AT&T, What extra pressure hits mobility profit in the back half, and how much cost efficiency is still left?

- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.economics.fact_att_segment_economics`: `fiscal_quarter_id`, `scenario_id`, `att_reporting_segment_id`, `att_segment_revenue_amount`, `att_segment_ebitda_amount`
- `carrier.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `ebitda_amount`, `operating_income_amount`, `free_cash_flow_amount`
- `carrier.economics.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `service_id`, `operating_expense_amount`
- `carrier.economics.fact_promotion_economics`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `promotion_amount`, `promotion_amortization_amount`
- `carrier.economics.fact_segment_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `ebitda_margin_percent`, `service_margin_percent`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (5) — AT&T

For AT&T, Will fiber net adds still follow the usual second-half seasonal lift if Internet Air adds are also higher?

- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.network.dim_network_technology`: `network_technology_id`, `network_technology_code`, `network_technology_name`
- `carrier.network.fact_fiber_route_capacity`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_route_mile_count`, `strand_mile_count`
- `carrier.network.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `network_technology_id`, `spectrum_band_id`, `region_id`, `network_capacity_gigabits_per_second`, `site_count`
- `carrier.subscribers.dim_enterprise_product`: `enterprise_product_id`, `enterprise_product_code`, `enterprise_product_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (1) — AT&T

For AT&T, How large is the fourth-quarter phone upgrade and promotion cycle, including any lift from Apple intelligence, and when does Business Wireline stop worsening?

- `carrier.economics.fact_device_subsidy_rate`: `fiscal_quarter_id`, `scenario_id`, `device_type_id`, `financing_type_id`, `promotion_type_id`, `subsidy_amount_per_device`, `subsidy_amount`
- `carrier.subscribers.fact_device_upgrades`: `fiscal_quarter_id`, `scenario_id`, `device_type_id`, `financing_type_id`, `promotion_type_id`, `upgrade_count`, `device_activation_count`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.economics.fact_customer_lifetime_value_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `lifetime_value_amount`
- `carrier.economics.fact_promotion_economics`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `promotion_amount`, `promotion_amortization_amount`
- `carrier.subscribers.dim_att_reporting_segment`: `att_reporting_segment_id`, `att_reporting_segment_code`, `att_reporting_segment_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (2) — AT&T

For AT&T, Why did Internet Air net adds stabilize even as more areas opened for sale, and could cable plant complement fiber in some regions?

- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.network.fact_fiber_route_capacity`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_route_mile_count`, `strand_mile_count`
- `carrier.network.fact_store_capacity`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `region_id`, `store_location_count`
- `carrier.subscribers.fact_fiber_penetration_base`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_subscriber_count`
- `carrier.subscribers.fact_prepaid_subscribers`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `region_id`, `prepaid_subscriber_count`
- `carrier.subscribers.fact_promotional_additions`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `sales_channel_id`, `promotional_gross_add_count`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (4) — AT&T

For AT&T, How does wireless competition differ between consumer and business, and what is sustaining postpaid phone revenue per user?

- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.subscribers.dim_service`: `service_id`, `service_code`, `service_name`
- `carrier.economics.fact_customer_lifetime_value_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `lifetime_value_amount`
- `carrier.network.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `network_technology_id`, `spectrum_band_id`, `region_id`, `network_capacity_gigabits_per_second`, `site_count`
- `carrier.subscribers.dim_att_reporting_segment`: `att_reporting_segment_id`, `att_reporting_segment_code`, `att_reporting_segment_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (5) — AT&T

For AT&T, If passings and penetration hold, should fiber net adds accelerate next year, and does that pull capital spending up?

- `carrier.subscribers.fact_fiber_penetration_base`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_subscriber_count`
- `carrier.economics.fact_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `initiative_id`, `network_technology_id`, `capital_expenditure_amount`
- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.network.fact_capital_project_capacity`: `fiscal_quarter_id`, `scenario_id`, `initiative_id`, `network_technology_id`, `region_id`, `project_count`, `location_under_construction_count`
- `carrier.network.fact_locations_passed`: `fiscal_quarter_id`, `scenario_id`, `network_technology_id`, `footprint_type_id`, `region_id`, `location_passed_count`, `premises_passed_count`
- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (6) — AT&T

For AT&T, What cost, price, and value levers matter for mobility next year if upgrades and churn stay low?

- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.economics.fact_customer_lifetime_value_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `lifetime_value_amount`
- `carrier.economics.fact_device_subsidy_rate`: `fiscal_quarter_id`, `scenario_id`, `device_type_id`, `financing_type_id`, `promotion_type_id`, `subsidy_amount_per_device`, `subsidy_amount`
- `carrier.economics.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `service_id`, `operating_expense_amount`
- `carrier.economics.fact_promotion_economics`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `promotion_amount`, `promotion_amortization_amount`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (1) — Verizon

For Verizon, What upgrade activity is expected for the rest of the year as device subsidies change, and how is profit from lower subsidies balanced against using devices to win gross adds?

- `carrier.economics.fact_device_subsidy_rate`: `fiscal_quarter_id`, `scenario_id`, `device_type_id`, `financing_type_id`, `promotion_type_id`, `subsidy_amount_per_device`, `subsidy_amount`
- `carrier.subscribers.dim_financing_type`: `financing_type_id`, `financing_type_code`, `financing_type_name`
- `carrier.subscribers.dim_promotion_type`: `promotion_type_id`, `promotion_type_code`, `promotion_type_name`
- `carrier.subscribers.fact_device_upgrades`: `fiscal_quarter_id`, `scenario_id`, `device_type_id`, `financing_type_id`, `promotion_type_id`, `upgrade_count`, `device_activation_count`
- `carrier.subscribers.fact_promotional_additions`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `sales_channel_id`, `promotional_gross_add_count`
- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (2) — Verizon

For Verizon, How much of the operating-cost savings is already in hand, and how should fixed wireless and fiber play out as acquired fiber is absorbed into a converged offer?

- `carrier.economics.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `service_id`, `operating_expense_amount`
- `carrier.network.dim_network_technology`: `network_technology_id`, `network_technology_code`, `network_technology_name`
- `carrier.subscribers.dim_service`: `service_id`, `service_code`, `service_name`
- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.network.dim_footprint_type`: `footprint_type_id`, `footprint_type_code`, `footprint_type_name`
- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (4) — Verizon

For Verizon, Which AI uses are actually cutting cost, how should headcount trend, and how is capital spending split between wireless and fiber?

- `carrier.economics.fact_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `initiative_id`, `network_technology_id`, `capital_expenditure_amount`
- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.network.dim_network_technology`: `network_technology_id`, `network_technology_code`, `network_technology_name`
- `carrier.subscribers.dim_service`: `service_id`, `service_code`, `service_name`
- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (5) — Verizon

For Verizon, How has the save budget changed inside micro-segmentation, what does that do to repricing the existing base, and is the postpaid phone share of industry net adds still about 10% to 15%?

- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_customer_lifetime_value_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `lifetime_value_amount`
- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.subscribers.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `carrier.subscribers.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (4) — Verizon

For Verizon, What explains flat mobility service-revenue growth — subscriber gains and wholesale versus higher promotion amortization — and what sits inside organic EBITDA growth?

- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_promotion_economics`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `promotion_amount`, `promotion_amortization_amount`
- `carrier.economics.fact_segment_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `ebitda_margin_percent`, `service_margin_percent`
- `carrier.economics.fact_wholesale_revenue`: `fiscal_quarter_id`, `scenario_id`, `partner_type_id`, `service_id`, `wholesale_revenue_amount`
- `carrier.subscribers.fact_promotional_additions`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `sales_channel_id`, `promotional_gross_add_count`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (5) — Verizon

For Verizon, If broad price increases are the wrong tool in a mature market, where can Verizon add value and still lift revenue per user?

- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.economics.fact_converged_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `footprint_type_id`, `converged_revenue_amount`
- `carrier.economics.fact_customer_lifetime_value_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `lifetime_value_amount`
- `carrier.economics.fact_segment_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `ebitda_margin_percent`, `service_margin_percent`
- `carrier.economics.fact_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `service_revenue_amount`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (5) — Verizon

For Verizon, How does fiber expansion square with free-cash-flow growth if capital spending has to fund a larger footprint?

- `carrier.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `ebitda_amount`, `operating_income_amount`, `free_cash_flow_amount`
- `carrier.economics.fact_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `initiative_id`, `network_technology_id`, `capital_expenditure_amount`
- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.network.dim_footprint_type`: `footprint_type_id`, `footprint_type_code`, `footprint_type_name`
- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.network.fact_fiber_route_capacity`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_route_mile_count`, `strand_mile_count`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (7) — Verizon

For Verizon, What themes run through the cost opportunities, and how does organic fiber passing of roughly 650,000 homes fit with the larger fiber plan?

- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_bad_debt_expense`: `fiscal_quarter_id`, `scenario_id`, `customer_segment_id`, `plan_type_id`, `bad_debt_amount`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.economics.fact_customer_lifetime_value_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `lifetime_value_amount`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (4) — Verizon

For Verizon, How fast are converged bundles being taken in the base, and how is that offer different from competitors?

- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.economics.fact_converged_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `footprint_type_id`, `converged_revenue_amount`
- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.subscribers.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `carrier.subscribers.dim_promotion_type`: `promotion_type_id`, `promotion_type_code`, `promotion_type_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (7) — Verizon

For Verizon, How much has postpaid phone acquisition cost risen, what is assumed for the second half, and how is the budget split between retention and acquisition?

- `carrier.subscribers.fact_promotional_additions`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `sales_channel_id`, `promotional_gross_add_count`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.subscribers.dim_movement_type`: `movement_type_id`, `movement_type_code`, `movement_type_name`
- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_customer_lifetime_value_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `lifetime_value_amount`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (9) — Verizon

For Verizon, Where can efficiency keep improving without price increases, and what is left on churn?

- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.economics.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `service_id`, `operating_expense_amount`
- `carrier.economics.fact_promotion_economics`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `promotion_amount`, `promotion_amortization_amount`
- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (10) — Verizon

For Verizon, What is improving business revenue and margin, and is that structural?

- `carrier.economics.fact_segment_margin_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `ebitda_margin_percent`, `service_margin_percent`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_converged_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `footprint_type_id`, `converged_revenue_amount`
- `carrier.economics.fact_device_revenue`: `fiscal_quarter_id`, `scenario_id`, `device_type_id`, `financing_type_id`, `equipment_revenue_amount`
- `carrier.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `ebitda_amount`, `operating_income_amount`, `free_cash_flow_amount`
- `carrier.economics.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `enterprise_product_id`, `customer_segment_id`, `enterprise_revenue_amount`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
