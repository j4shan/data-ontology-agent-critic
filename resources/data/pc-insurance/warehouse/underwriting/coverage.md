# Insurance Inc underwriting slice

Underwriting, agency, claims and digital capacity facts. Capacity facts store no premium price.

## Numbered questions

### Q1 2026 (4) — Chubb

For Chubb, Has technology changed whether the digital transformation is front-loaded or back-loaded?

- `insurance.economics.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `insurance.underwriting.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `insurance.economics.fact_advertising_expense`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `customer_segment_id`, `insurance_advertising_amount`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.economics.fact_underwriting_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `line_of_business_id`, `underwriting_expense_amount`
- `insurance.exposure.dim_distribution_channel`: `distribution_channel_id`, `distribution_channel_code`, `distribution_channel_name`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (5) — Chubb

For Chubb, How does the roughly 150 basis points of combined-ratio improvement from digital transformation phase over three to four years?

- `insurance.economics.fact_chubb_segment_economics`: `fiscal_quarter_id`, `scenario_id`, `chubb_reporting_segment_id`, `chubb_underwriting_income_amount`, `chubb_combined_ratio_percent`
- `insurance.economics.fact_combined_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `combined_ratio_percent`, `expense_ratio_percent`
- `insurance.underwriting.dim_initiative`: `initiative_id`, `initiative_code`, `initiative_name`
- `insurance.economics.fact_incurred_loss_by_cohort`: `fiscal_quarter_id`, `scenario_id`, `accident_year_id`, `line_of_business_id`, `claim_type_id`, `cohort_incurred_loss_amount`, `paid_loss_amount`
- `insurance.economics.fact_loss_and_premium`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_earned_premium_amount`, `incurred_loss_amount`
- `insurance.economics.fact_loss_ratio_rate`: `fiscal_quarter_id`, `scenario_id`, `line_of_business_id`, `region_id`, `loss_ratio_percent`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2023 (1) — Progressive

For Progressive, How should segmentation and continuous product-model delivery be thought about for forecasting mix?

- `insurance.economics.fact_average_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `average_premium_per_policy_amount`
- `insurance.economics.fact_progressive_premium`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `progressive_earned_premium_amount`, `progressive_written_premium_amount`
- `insurance.exposure.dim_progressive_product`: `progressive_product_id`, `progressive_product_code`, `progressive_product_name`
- `insurance.exposure.fact_personal_auto_exposure`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `us_region_id`, `personal_auto_vehicle_count`, `personal_auto_policy_count`
- `insurance.exposure.fact_progressive_policies_in_force`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `progressive_policy_in_force_count`, `insured_vehicle_count`
- `insurance.underwriting.fact_catastrophe_model_capacity`: `fiscal_quarter_id`, `scenario_id`, `peril_id`, `region_id`, `modeled_combination_count`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2023 (5) — Progressive

For Progressive, What do base and contingent commissions look like when Progressive is profitable and most competitors are not?

- `insurance.economics.fact_commission_economics`: `fiscal_quarter_id`, `scenario_id`, `distribution_channel_id`, `line_of_business_id`, `commission_amount`, `contingent_commission_amount`
- `insurance.economics.fact_average_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `average_premium_per_policy_amount`
- `insurance.economics.fact_progressive_premium`: `fiscal_quarter_id`, `scenario_id`, `progressive_product_id`, `distribution_channel_id`, `progressive_earned_premium_amount`, `progressive_written_premium_amount`
- `insurance.exposure.dim_competitor`: `competitor_id`, `competitor_code`, `competitor_name`
- `insurance.exposure.dim_progressive_product`: `progressive_product_id`, `progressive_product_code`, `progressive_product_name`
- `insurance.exposure.fact_market_policies`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `line_of_business_id`, `region_id`, `competitor_policy_count`
- `insurance.exposure.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `insurance.exposure.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
