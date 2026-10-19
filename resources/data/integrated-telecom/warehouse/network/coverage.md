# Carrier Inc network slice

Network capacity facts. A capacity fact does not store a price.

## Numbered questions

### Q1 2026 (3) — AT&T

For AT&T, What does an “open” network mean for how AT&T sells, partners, or buys assets, and for return on capital?

- `carrier.network.fact_open_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `partner_type_id`, `network_technology_id`, `wholesale_route_count`
- `carrier.economics.fact_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `initiative_id`, `network_technology_id`, `capital_expenditure_amount`
- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.network.fact_capital_project_capacity`: `fiscal_quarter_id`, `scenario_id`, `initiative_id`, `network_technology_id`, `region_id`, `project_count`, `location_under_construction_count`
- `carrier.subscribers.fact_satellite_subscribers`: `fiscal_quarter_id`, `scenario_id`, `partner_type_id`, `network_technology_id`, `satellite_subscriber_count`
- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (5) — AT&T

For AT&T, How is satellite, including the AST partnership, a threat or complement on fiber and broadband versus what fixed wireless already taught, and would AT&T offer wholesale access to new satellite players?

- `carrier.network.dim_network_technology`: `network_technology_id`, `network_technology_code`, `network_technology_name`
- `carrier.subscribers.dim_service`: `service_id`, `service_code`, `service_name`
- `carrier.subscribers.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `carrier.subscribers.dim_partner_type`: `partner_type_id`, `partner_type_code`, `partner_type_name`
- `carrier.subscribers.fact_fixed_wireless_subscribers`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `customer_segment_id`, `fixed_wireless_subscriber_count`
- `carrier.subscribers.fact_satellite_subscribers`: `fiscal_quarter_id`, `scenario_id`, `partner_type_id`, `network_technology_id`, `satellite_subscriber_count`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (6) — AT&T

For AT&T, How does the EchoStar spectrum change the business and its return, and what cost and return come from copper retirement?

- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.network.fact_copper_retirement_capacity`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `copper_location_retired_count`, `copper_line_count`
- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.economics.fact_legacy_revenue`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `network_technology_id`, `legacy_revenue_amount`
- `carrier.economics.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `service_id`, `operating_expense_amount`
- `carrier.economics.fact_promotion_economics`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `promotion_amount`, `promotion_amortization_amount`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (4) — AT&T

For AT&T, What changes in the fiber build as the pace steps up from the low 30s toward about 40 million locations?

- `carrier.subscribers.fact_fiber_penetration_base`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_subscriber_count`
- `carrier.network.fact_locations_passed`: `fiscal_quarter_id`, `scenario_id`, `network_technology_id`, `footprint_type_id`, `region_id`, `location_passed_count`, `premises_passed_count`
- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.network.dim_network_technology`: `network_technology_id`, `network_technology_code`, `network_technology_name`
- `carrier.network.dim_spectrum_band`: `spectrum_band_id`, `spectrum_band_code`, `spectrum_band_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (8) — AT&T

For AT&T, How targeted should fixed wireless be versus fiber in 2026, and does flat handset amortization mean competition stays intense?

- `carrier.network.dim_network_technology`: `network_technology_id`, `network_technology_code`, `network_technology_name`
- `carrier.subscribers.dim_service`: `service_id`, `service_code`, `service_name`
- `carrier.subscribers.fact_fixed_wireless_subscribers`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `customer_segment_id`, `fixed_wireless_subscriber_count`
- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.economics.fact_promotion_economics`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `promotion_amount`, `promotion_amortization_amount`
- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (2) — AT&T

For AT&T, Does the churn outlook argue for slower price increases, and are spectrum purchases assumed in the long-term plan?

- `carrier.economics.fact_churn_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `churn_percent`, `phone_churn_percent`
- `carrier.economics.fact_arpu_rate`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `plan_type_id`, `region_id`, `average_revenue_per_user_amount`, `average_revenue_per_account_amount`
- `carrier.economics.fact_bad_debt_expense`: `fiscal_quarter_id`, `scenario_id`, `customer_segment_id`, `plan_type_id`, `bad_debt_amount`
- `carrier.economics.fact_customer_lifetime_value_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `sales_channel_id`, `lifetime_value_amount`
- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.network.dim_spectrum_band`: `spectrum_band_id`, `spectrum_band_code`, `spectrum_band_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (3) — AT&T

For AT&T, Are returns on the next wave of fiber locations as good as on the first 30 million, or were the best markets built first?

- `carrier.subscribers.fact_fiber_penetration_base`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_subscriber_count`
- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.network.dim_network_technology`: `network_technology_id`, `network_technology_code`, `network_technology_name`
- `carrier.network.dim_spectrum_band`: `spectrum_band_id`, `spectrum_band_code`, `spectrum_band_name`
- `carrier.network.fact_capital_project_capacity`: `fiscal_quarter_id`, `scenario_id`, `initiative_id`, `network_technology_id`, `region_id`, `project_count`, `location_under_construction_count`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (2) — Verizon

For Verizon, Is the higher medium-term fiber-passing target more in-footprint opportunity or expansion outside the current footprint?

- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.network.dim_footprint_type`: `footprint_type_id`, `footprint_type_code`, `footprint_type_name`
- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.network.fact_fiber_route_capacity`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_route_mile_count`, `strand_mile_count`
- `carrier.subscribers.fact_converged_subscribers`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `footprint_type_id`, `converged_household_count`, `multi_service_account_count`
- `carrier.subscribers.fact_fiber_penetration_base`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_subscriber_count`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (4) — Verizon

For Verizon, How large should the fiber footprint get, and should fixed wireless get more investment as another broadband path?

- `carrier.subscribers.dim_service`: `service_id`, `service_code`, `service_name`
- `carrier.network.dim_network_technology`: `network_technology_id`, `network_technology_code`, `network_technology_name`
- `carrier.subscribers.fact_fixed_wireless_subscribers`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `customer_segment_id`, `fixed_wireless_subscriber_count`
- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.network.fact_fiber_route_capacity`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_route_mile_count`, `strand_mile_count`
- `carrier.subscribers.fact_broadband_subscribers`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `speed_tier_id`, `footprint_type_id`, `region_id`, `broadband_subscriber_count`, `household_count`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (3) — Verizon

For Verizon, How are gross adds trending in fixed wireless and Fios into the back half, and will multi-dwelling fiber trials matter in 2026?

- `carrier.network.dim_network_technology`: `network_technology_id`, `network_technology_code`, `network_technology_name`
- `carrier.subscribers.dim_service`: `service_id`, `service_code`, `service_name`
- `carrier.subscribers.fact_fixed_wireless_subscribers`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `customer_segment_id`, `fixed_wireless_subscriber_count`
- `carrier.subscribers.fact_promotional_additions`: `fiscal_quarter_id`, `scenario_id`, `promotion_type_id`, `service_id`, `sales_channel_id`, `promotional_gross_add_count`
- `carrier.economics.fact_fiber_revenue_rate`: `fiscal_quarter_id`, `scenario_id`, `footprint_type_id`, `region_id`, `fiber_arpu_amount`
- `carrier.economics.fact_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_id`, `customer_segment_id`, `service_revenue_amount`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (6) — Verizon

For Verizon, How would new spectrum, from a government process or from EchoStar, be prioritized against the rest of the network plan?

- `carrier.economics.fact_capital_expenditure`: `fiscal_quarter_id`, `scenario_id`, `initiative_id`, `network_technology_id`, `capital_expenditure_amount`
- `carrier.network.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `carrier.network.fact_capital_project_capacity`: `fiscal_quarter_id`, `scenario_id`, `initiative_id`, `network_technology_id`, `region_id`, `project_count`, `location_under_construction_count`
- `carrier.network.fact_network_capacity`: `fiscal_quarter_id`, `scenario_id`, `network_technology_id`, `spectrum_band_id`, `region_id`, `network_capacity_gigabits_per_second`, `site_count`
- `carrier.network.fact_spectrum_deployment`: `fiscal_quarter_id`, `scenario_id`, `spectrum_band_id`, `network_technology_id`, `deployed_site_count`
- `carrier.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `carrier.subscribers.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `carrier.subscribers.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
