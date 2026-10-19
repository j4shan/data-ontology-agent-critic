# Insurance Inc economics slice

Premium, loss, reserve, investment and ratio dollars and percents. Loss and combined ratios name their earned-premium denominator fact at the same grain.

## Numbered questions

### Q1 2026 (1) — Chubb

For Chubb, How does the market behave if the conflict lasts longer than expected?

- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_average_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `average_premium_per_policy_amount`
- `insurance.economics.fact_chubb_segment_premium`: `fiscal_quarter_id`, `scenario_id`, `chubb_reporting_segment_id`, `commercial_size_id`, `chubb_net_written_premium_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_earned_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `earned_premium_amount`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (2) — Chubb

For Chubb, Can the smaller end of Chubb's excess-and-surplus business be several times larger in five years?

- `insurance.economics.fact_chubb_segment_premium`: `fiscal_quarter_id`, `scenario_id`, `chubb_reporting_segment_id`, `commercial_size_id`, `chubb_net_written_premium_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_earned_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `earned_premium_amount`
- `insurance.economics.fact_incurred_loss_by_cohort`: `fiscal_quarter_id`, `scenario_id`, `accident_year_id`, `line_of_business_id`, `claim_type_id`, `cohort_incurred_loss_amount`, `paid_loss_amount`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (6) — Chubb

For Chubb, Does that mix create room to lower acquisition expense?

- `insurance.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_average_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `average_premium_per_policy_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_underwriting_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `line_of_business_id`, `underwriting_expense_amount`
- `insurance.exposure.fact_personal_auto_exposure`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `us_region_id`, `personal_auto_vehicle_count`, `personal_auto_policy_count`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (7) — Chubb

For Chubb, How should private credit's role in the portfolio evolve, and how healthy is the existing book?

- `insurance.economics.dim_investment_asset`: `investment_asset_id`, `investment_asset_code`, `investment_asset_name`
- `insurance.underwriting.fact_investment_holdings_capacity`: `fiscal_quarter_id`, `scenario_id`, `investment_asset_id`, `portfolio_holding_count`
- `insurance.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `enterprise_operating_income_amount`, `enterprise_net_income_amount`, `book_value_amount`
- `insurance.economics.fact_foreign_exchange_economics`: `fiscal_quarter_id`, `scenario_id`, `currency_id`, `region_id`, `foreign_exchange_gain_amount`
- `insurance.economics.fact_investment_income`: `fiscal_quarter_id`, `scenario_id`, `investment_asset_id`, `currency_id`, `net_investment_income_amount`, `realized_gain_amount`
- `insurance.exposure.dim_line_of_business`: `line_of_business_id`, `line_of_business_code`, `line_of_business_name`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (1) — Chubb

For Chubb, In the current pricing environment, can recent margin performance be sustained in 2026?

- `insurance.economics.fact_chubb_segment_economics`: `fiscal_quarter_id`, `scenario_id`, `chubb_reporting_segment_id`, `chubb_underwriting_income_amount`, `chubb_combined_ratio_percent`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.exposure.dim_accident_year`: `accident_year_id`, `accident_year_code`, `accident_year_name`, `accident_year_number`
- `insurance.exposure.dim_line_of_business`: `line_of_business_id`, `line_of_business_code`, `line_of_business_name`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (3) — Chubb

For Chubb, How do competitive dynamics differ across Asia?

- `insurance.exposure.dim_commercial_size`: `commercial_size_id`, `commercial_size_code`, `commercial_size_name`
- `insurance.exposure.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `insurance.economics.fact_chubb_segment_premium`: `fiscal_quarter_id`, `scenario_id`, `chubb_reporting_segment_id`, `commercial_size_id`, `chubb_net_written_premium_amount`
- `insurance.exposure.dim_chubb_reporting_segment`: `chubb_reporting_segment_id`, `chubb_reporting_segment_code`, `chubb_reporting_segment_name`
- `insurance.exposure.dim_coverage_line`: `coverage_line_id`, `coverage_line_code`, `coverage_line_name`
- `insurance.exposure.dim_line_of_business`: `line_of_business_id`, `line_of_business_code`, `line_of_business_name`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (4) — Chubb

For Chubb, How do those overseas results show up in margins?

- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_chubb_segment_economics`: `fiscal_quarter_id`, `scenario_id`, `chubb_reporting_segment_id`, `chubb_underwriting_income_amount`, `chubb_combined_ratio_percent`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.economics.fact_average_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `average_premium_per_policy_amount`
- `insurance.economics.fact_chubb_segment_premium`: `fiscal_quarter_id`, `scenario_id`, `chubb_reporting_segment_id`, `commercial_size_id`, `chubb_net_written_premium_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (6) — Chubb

For Chubb, How is foreign-exchange volatility treated in enterprise risk for a global book?

- `insurance.economics.fact_foreign_exchange_economics`: `fiscal_quarter_id`, `scenario_id`, `currency_id`, `region_id`, `foreign_exchange_gain_amount`
- `insurance.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `enterprise_operating_income_amount`, `enterprise_net_income_amount`, `book_value_amount`
- `insurance.economics.dim_currency`: `currency_id`, `currency_code`, `currency_name`
- `insurance.economics.fact_average_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `average_premium_per_policy_amount`
- `insurance.economics.fact_chubb_segment_premium`: `fiscal_quarter_id`, `scenario_id`, `chubb_reporting_segment_id`, `commercial_size_id`, `chubb_net_written_premium_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (1) — Chubb

For Chubb, Does the loss figure include assessment and subrogation from the ground up?

- `insurance.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `insurance.economics.fact_catastrophe_loss`: `fiscal_quarter_id`, `scenario_id`, `peril_id`, `line_of_business_id`, `region_id`, `catastrophe_loss_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_foreign_exchange_economics`: `fiscal_quarter_id`, `scenario_id`, `currency_id`, `region_id`, `foreign_exchange_gain_amount`
- `insurance.economics.fact_incurred_loss_by_cohort`: `fiscal_quarter_id`, `scenario_id`, `accident_year_id`, `line_of_business_id`, `claim_type_id`, `cohort_incurred_loss_amount`, `paid_loss_amount`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (3) — Chubb

For Chubb, What drove favorable long-tail reserve development, and how did it affect the loss ratio's durability?

- `insurance.economics.fact_reserve_development`: `fiscal_quarter_id`, `scenario_id`, `accident_year_id`, `line_of_business_id`, `reserve_development_amount`, `prior_year_development_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `insurance.economics.fact_catastrophe_loss`: `fiscal_quarter_id`, `scenario_id`, `peril_id`, `line_of_business_id`, `region_id`, `catastrophe_loss_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (3) — Chubb

For Chubb, After elevated catastrophe losses, what is happening in property, and what is expected at January 1 renewals on both primary and reinsurance?

- `insurance.exposure.dim_claim_type`: `claim_type_id`, `claim_type_code`, `claim_type_name`
- `insurance.exposure.dim_line_of_business`: `line_of_business_id`, `line_of_business_code`, `line_of_business_name`
- `insurance.exposure.dim_policy_type`: `policy_type_id`, `policy_type_code`, `policy_type_name`
- `insurance.economics.fact_catastrophe_loss`: `fiscal_quarter_id`, `scenario_id`, `peril_id`, `line_of_business_id`, `region_id`, `catastrophe_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.economics.fact_rate_change_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `region_id`, `premium_rate_change_percent`, `renewal_rate_change_percent`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (4) — Chubb

For Chubb, Which accident years and lines, such as general liability or commercial auto, drove the reserve development?

- `insurance.economics.fact_reserve_development`: `fiscal_quarter_id`, `scenario_id`, `accident_year_id`, `line_of_business_id`, `reserve_development_amount`, `prior_year_development_amount`
- `insurance.exposure.dim_coverage_line`: `coverage_line_id`, `coverage_line_code`, `coverage_line_name`
- `insurance.economics.fact_reserve_balance`: `fiscal_quarter_id`, `scenario_id`, `accident_year_id`, `line_of_business_id`, `reserve_balance_amount`
- `insurance.exposure.dim_line_of_business`: `line_of_business_id`, `line_of_business_code`, `line_of_business_name`
- `insurance.economics.fact_incurred_loss_by_cohort`: `fiscal_quarter_id`, `scenario_id`, `accident_year_id`, `line_of_business_id`, `claim_type_id`, `cohort_incurred_loss_amount`, `paid_loss_amount`
- `insurance.exposure.dim_chubb_reporting_segment`: `chubb_reporting_segment_id`, `chubb_reporting_segment_code`, `chubb_reporting_segment_name`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (7) — Chubb

For Chubb, Does the data show a growing appetite for casualty as troubled lines are fixed?

- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.economics.fact_catastrophe_loss`: `fiscal_quarter_id`, `scenario_id`, `peril_id`, `line_of_business_id`, `region_id`, `catastrophe_loss_amount`
- `insurance.economics.fact_earned_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `earned_premium_amount`
- `insurance.economics.fact_incurred_loss_by_cohort`: `fiscal_quarter_id`, `scenario_id`, `accident_year_id`, `line_of_business_id`, `claim_type_id`, `cohort_incurred_loss_amount`, `paid_loss_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (1) — Progressive

For Progressive, Can 2025 be even stronger even if a prior tailwind fades, given how this cycle differs from earlier ones?

- `insurance.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_average_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `average_premium_per_policy_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (4) — Progressive

For Progressive, How are margins balanced against growing as fast as possible if that growth pushes loss costs up?

- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_catastrophe_loss`: `fiscal_quarter_id`, `scenario_id`, `peril_id`, `line_of_business_id`, `region_id`, `catastrophe_loss_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (5) — Progressive

For Progressive, Does higher shopping keep advertising spend seasonally skewed?

- `insurance.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_written_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `gross_written_premium_amount`, `net_written_premium_amount`
- `insurance.economics.fact_earned_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `earned_premium_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (1) — Progressive

For Progressive, If Progressive cuts price, does policy growth have to improve in both revenue premium and policy count?

- `insurance.economics.fact_average_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `average_premium_per_policy_amount`
- `insurance.exposure.fact_progressive_policies_in_force`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `progressive_policy_in_force_count`, `insured_vehicle_count`
- `insurance.exposure.fact_personal_auto_exposure`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `us_region_id`, `personal_auto_vehicle_count`, `personal_auto_policy_count`
- `insurance.exposure.fact_policies_in_force`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `policy_in_force_count`, `insured_unit_count`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.economics.fact_progressive_premium`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `progressive_earned_premium_amount`, `progressive_written_premium_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (2) — Progressive

For Progressive, Are current margins high enough that price cuts should be considered soon?

- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.exposure.dim_line_of_business`: `line_of_business_id`, `line_of_business_code`, `line_of_business_name`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (3) — Progressive

For Progressive, If competition intensifies in 2025, how effective are incremental advertising and price?

- `insurance.exposure.dim_policy_type`: `policy_type_id`, `policy_type_code`, `policy_type_name`
- `insurance.exposure.fact_market_policies`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `line_of_business_id`, `region_id`, `competitor_policy_count`
- `insurance.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_catastrophe_loss`: `fiscal_quarter_id`, `scenario_id`, `peril_id`, `line_of_business_id`, `region_id`, `catastrophe_loss_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2023 (2) — Progressive

For Progressive, How large is the advertising step-up in the expense ratio?

- `insurance.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.economics.fact_underwriting_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `line_of_business_id`, `underwriting_expense_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2023 (4) — Progressive

For Progressive, What has scale from several years of growth done to the non-advertising expense ratio?

- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `insurance.economics.fact_average_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `average_premium_per_policy_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.exposure.fact_earned_exposure`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `region_id`, `policy_year_count`, `vehicle_year_count`
- `insurance.exposure.fact_policies_in_force`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `policy_in_force_count`, `insured_unit_count`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2023 (2) — Progressive

For Progressive, How are severity trends developing, and should they normalize?

- `insurance.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `insurance.economics.fact_severity_rate`: `fiscal_quarter_id`, `scenario_id`, `claim_type_id`, `peril_id`, `line_of_business_id`, `average_severity_amount`
- `insurance.economics.fact_catastrophe_loss`: `fiscal_quarter_id`, `scenario_id`, `peril_id`, `line_of_business_id`, `region_id`, `catastrophe_loss_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_foreign_exchange_economics`: `fiscal_quarter_id`, `scenario_id`, `currency_id`, `region_id`, `foreign_exchange_gain_amount`
- `insurance.economics.fact_incurred_loss_by_cohort`: `fiscal_quarter_id`, `scenario_id`, `accident_year_id`, `line_of_business_id`, `claim_type_id`, `cohort_incurred_loss_amount`, `paid_loss_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2023 (3) — Progressive

For Progressive, Should the growth decision be read off industry profitability and capital, and only after the industry heals?

- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_enterprise_economics`: `fiscal_quarter_id`, `scenario_id`, `enterprise_operating_income_amount`, `enterprise_net_income_amount`, `book_value_amount`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.exposure.dim_line_of_business`: `line_of_business_id`, `line_of_business_code`, `line_of_business_name`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2023 (4) — Progressive

For Progressive, What is happening in the business that carries a larger new-business penalty than other personal-lines books?

- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.exposure.dim_line_of_business`: `line_of_business_id`, `line_of_business_code`, `line_of_business_name`
- `insurance.economics.fact_catastrophe_loss`: `fiscal_quarter_id`, `scenario_id`, `peril_id`, `line_of_business_id`, `region_id`, `catastrophe_loss_amount`
- `insurance.economics.fact_incurred_loss_by_cohort`: `fiscal_quarter_id`, `scenario_id`, `accident_year_id`, `line_of_business_id`, `claim_type_id`, `cohort_incurred_loss_amount`, `paid_loss_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2023 (5) — Progressive

For Progressive, What drove adverse development, and is it the start of a multi-month trend?

- `insurance.economics.fact_reserve_development`: `fiscal_quarter_id`, `scenario_id`, `accident_year_id`, `line_of_business_id`, `reserve_development_amount`, `prior_year_development_amount`
- `insurance.economics.fact_reserve_balance`: `fiscal_quarter_id`, `scenario_id`, `accident_year_id`, `line_of_business_id`, `reserve_balance_amount`
- `insurance.exposure.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `insurance.economics.fact_written_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `customer_segment_id`, `distribution_channel_id`, `region_id`, `gross_written_premium_amount`, `net_written_premium_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2023 (6) — Progressive

For Progressive, Was the expense-ratio decline mostly from pulling marketing while seeking price increases, and what has to be seen before marketing spend returns?

- `insurance.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.economics.fact_underwriting_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `line_of_business_id`, `underwriting_expense_amount`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2023 (7) — Progressive

For Progressive, Is there any impact from the auto-workers strike?

- `insurance.economics.fact_severity_rate`: `fiscal_quarter_id`, `scenario_id`, `claim_type_id`, `peril_id`, `line_of_business_id`, `average_severity_amount`
- `insurance.exposure.dim_claim_type`: `claim_type_id`, `claim_type_code`, `claim_type_name`
- `insurance.exposure.dim_coverage_line`: `coverage_line_id`, `coverage_line_code`, `coverage_line_name`
- `insurance.economics.fact_incurred_loss_by_cohort`: `fiscal_quarter_id`, `scenario_id`, `accident_year_id`, `line_of_business_id`, `claim_type_id`, `cohort_incurred_loss_amount`, `paid_loss_amount`
- `insurance.exposure.dim_line_of_business`: `line_of_business_id`, `line_of_business_code`, `line_of_business_name`
- `insurance.exposure.dim_peril`: `peril_id`, `peril_code`, `peril_name`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
