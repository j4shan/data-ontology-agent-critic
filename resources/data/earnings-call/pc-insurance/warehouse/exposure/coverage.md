# Insurance Inc exposure slice

Policy, exposure and claim quantity facts. Premium dollars are not stored here; policies in force are rate denominators.

## Numbered questions

### Q1 2026 (3) — Chubb

For Chubb, Is competition this time just carriers chasing top-line growth in a softening market, or something else?

- `insurance.exposure.fact_market_policies`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `line_of_business_id`, `region_id`, `competitor_policy_count`
- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_earned_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `earned_premium_amount`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (5) — Chubb

For Chubb, Do elevated sales of the products discussed stay high if volumes normalize?

- `insurance.economics.fact_average_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `average_premium_per_policy_amount`
- `insurance.economics.fact_chubb_segment_premium`: `fiscal_quarter_id`, `scenario_id`, `chubb_reporting_segment_id`, `commercial_size_id`, `chubb_net_written_premium_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_earned_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `earned_premium_amount`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (2) — Chubb

For Chubb, Outside Mexico, what is the Latin America opportunity and growth momentum?

- `insurance.exposure.dim_region`: `region_id`, `region_code`, `region_name`
- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_average_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `average_premium_per_policy_amount`
- `insurance.economics.fact_chubb_segment_premium`: `fiscal_quarter_id`, `scenario_id`, `chubb_reporting_segment_id`, `commercial_size_id`, `chubb_net_written_premium_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_earned_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `earned_premium_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (2) — Chubb

For Chubb, Is the organic growth rate a reasonable 2025 target, and is this the point to look harder at inorganic growth?

- `insurance.economics.fact_average_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `average_premium_per_policy_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.economics.fact_rate_change_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `region_id`, `premium_rate_change_percent`, `renewal_rate_change_percent`
- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_chubb_segment_premium`: `fiscal_quarter_id`, `scenario_id`, `chubb_reporting_segment_id`, `commercial_size_id`, `chubb_net_written_premium_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (1) — Chubb

For Chubb, Given pricing and growth, should growth accelerate from here in the book excluding financial lines and workers' compensation?

- `insurance.exposure.dim_coverage_line`: `coverage_line_id`, `coverage_line_code`, `coverage_line_name`
- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_earned_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `earned_premium_amount`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (2) — Chubb

For Chubb, Will international growth be driven by Asia and other regions, and could the election affect that?

- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_earned_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `earned_premium_amount`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.economics.fact_rate_change_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `region_id`, `premium_rate_change_percent`, `renewal_rate_change_percent`
- `insurance.economics.fact_written_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `gross_written_premium_amount`, `net_written_premium_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (5) — Chubb

For Chubb, Is the remediation of troubled commercial casualty largely behind the company, so those lines can keep accelerating?

- `insurance.exposure.dim_line_of_business`: `line_of_business_id`, `line_of_business_code`, `line_of_business_name`
- `insurance.underwriting.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_chubb_segment_premium`: `fiscal_quarter_id`, `scenario_id`, `chubb_reporting_segment_id`, `commercial_size_id`, `chubb_net_written_premium_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_earned_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `earned_premium_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (6) — Chubb

For Chubb, Was the third quarter a normal mix of property and casualty, and is shifting further toward property still comfortable?

- `insurance.exposure.dim_line_of_business`: `line_of_business_id`, `line_of_business_code`, `line_of_business_name`
- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_average_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `average_premium_per_policy_amount`
- `insurance.economics.fact_catastrophe_loss`: `fiscal_quarter_id`, `scenario_id`, `peril_id`, `line_of_business_id`, `region_id`, `catastrophe_loss_amount`
- `insurance.economics.fact_chubb_segment_economics`: `fiscal_quarter_id`, `scenario_id`, `chubb_reporting_segment_id`, `chubb_underwriting_income_amount`, `chubb_combined_ratio_percent`
- `insurance.economics.fact_chubb_segment_premium`: `fiscal_quarter_id`, `scenario_id`, `chubb_reporting_segment_id`, `commercial_size_id`, `chubb_net_written_premium_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (2) — Progressive

For Progressive, How much further can advertising spend rise to capture growth, and how should that spend be compared with policies-in-force growth?

- `insurance.exposure.dim_policy_type`: `policy_type_id`, `policy_type_code`, `policy_type_name`
- `insurance.exposure.fact_policies_in_force`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `policy_in_force_count`, `insured_unit_count`
- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_average_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `average_premium_per_policy_amount`
- `insurance.economics.fact_written_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `gross_written_premium_amount`, `net_written_premium_amount`
- `insurance.exposure.fact_catastrophe_exposure`: `fiscal_quarter_id`, `scenario_id`, `peril_id`, `region_id`, `line_of_business_id`, `exposed_policy_count`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (3) — Progressive

For Progressive, Why is policy life expectancy still ticking down, and how does that compare with the longer stretch of elongation?

- `insurance.exposure.fact_life_exposure`: `fiscal_quarter_id`, `scenario_id`, `chubb_reporting_segment_id`, `customer_segment_id`, `life_policy_count`
- `insurance.exposure.fact_renewal_exposure`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `distribution_channel_id`, `renewal_policy_count`, `retained_policy_count`
- `insurance.economics.fact_average_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `average_premium_per_policy_amount`
- `insurance.economics.fact_written_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `gross_written_premium_amount`, `net_written_premium_amount`
- `insurance.exposure.dim_line_of_business`: `line_of_business_id`, `line_of_business_code`, `line_of_business_name`
- `insurance.exposure.dim_policy_type`: `policy_type_id`, `policy_type_code`, `policy_type_name`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (4) — Progressive

For Progressive, With personal-auto policy life expectancy elongated for more than a year, does pushing life expectancy create a combined-ratio headwind?

- `insurance.exposure.dim_line_of_business`: `line_of_business_id`, `line_of_business_code`, `line_of_business_name`
- `insurance.exposure.fact_earned_exposure`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `region_id`, `policy_year_count`, `vehicle_year_count`
- `insurance.exposure.fact_personal_auto_exposure`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `us_region_id`, `personal_auto_vehicle_count`, `personal_auto_policy_count`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.exposure.dim_progressive_product`: `progressive_product_id`, `progressive_product_code`, `progressive_product_name`
- `insurance.exposure.fact_life_exposure`: `fiscal_quarter_id`, `scenario_id`, `chubb_reporting_segment_id`, `customer_segment_id`, `life_policy_count`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2023 (3) — Progressive

For Progressive, Which competitors are already in a position to take share, and what does that environment look like?

- `insurance.exposure.fact_market_policies`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `line_of_business_id`, `region_id`, `competitor_policy_count`
- `insurance.exposure.dim_commercial_size`: `commercial_size_id`, `commercial_size_code`, `commercial_size_name`
- `insurance.exposure.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `insurance.exposure.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_reinsurance_type`: `reinsurance_type_id`, `reinsurance_type_code`, `reinsurance_type_name`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2023 (1) — Progressive

For Progressive, Is it reasonable to assume growth reaccelerates into 2024?

- `insurance.exposure.dim_policy_type`: `policy_type_id`, `policy_type_code`, `policy_type_name`
- `insurance.exposure.fact_policies_in_force`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `policy_in_force_count`, `insured_unit_count`
- `insurance.economics.fact_average_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `average_premium_per_policy_amount`
- `insurance.economics.fact_written_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `gross_written_premium_amount`, `net_written_premium_amount`
- `insurance.exposure.fact_catastrophe_exposure`: `fiscal_quarter_id`, `scenario_id`, `peril_id`, `region_id`, `line_of_business_id`, `exposed_policy_count`
- `insurance.exposure.fact_commercial_exposure`: `fiscal_quarter_id`, `scenario_id`, `commercial_size_id`, `line_of_business_id`, `customer_segment_id`, `commercial_policy_count`, `insured_location_count`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
