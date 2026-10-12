# Health Plan Inc price, bid, and margin

This slice owns rates, bids, medical-cost trend rates, and margins for Health Plan Inc. A price row does not store a member count or a procedure count. Those quantities stay on the membership and medical slices.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `drug_identity` | `drug_id` | `sf:healthplan.medical.dim_drug` `drug_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `clinical_category_identity` | `clinical_category_id` | `sf:healthplan.medical.dim_clinical_category` `clinical_category_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `clinical_category_identity` | `clinical_category_id` | `sf:healthplan.medical.dim_clinical_category` `clinical_category_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `state_identity` | `state_id` | `sf:healthplan.geography.dim_state` `state_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `dispute_type_identity` | `dispute_type_id` | `sf:healthplan.medical.dim_dispute_type` `dispute_type_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `provider_group_identity` | `provider_group_id` | `sf:healthplan.provider.dim_provider_group` `provider_group_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `benefit_design_identity` | `benefit_design_id` | `sf:healthplan.product.dim_benefit_design` `benefit_design_id` |
| `drug_identity` | `drug_id` | `sf:healthplan.medical.dim_drug` `drug_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `state_program_identity` | `state_program_id` | `sf:healthplan.geography.dim_state_program` `state_program_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `care_service_identity` | `care_service_id` | `sf:healthplan.medical.dim_care_service` `care_service_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `clinical_category_identity` | `clinical_category_id` | `sf:healthplan.medical.dim_clinical_category` `clinical_category_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `risk_model_identity` | `risk_model_id` | `sf:healthplan.medical.dim_risk_model` `risk_model_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `benefit_design_identity` | `benefit_design_id` | `sf:healthplan.product.dim_benefit_design` `benefit_design_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `drug_identity` | `drug_id` | `sf:healthplan.medical.dim_drug` `drug_id` |
| `care_service_identity` | `care_service_id` | `sf:healthplan.medical.dim_care_service` `care_service_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `state_identity` | `state_id` | `sf:healthplan.geography.dim_state` `state_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |

## Numbered questions

## UnitedHealth Group

### Q2 2026 (1)

Where is the full-year Medicaid margin expected to finish versus the earlier negative range?

- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `prior_range_high_rate`
- `healthplan.price.fact_rate_update`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `rate_notice_id`, `rate_change_rate`, `embedded_outlook_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q2 2026 (2)

How far is commercial medical-cost trend running versus the roughly 11% assumption?

- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `assumption_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q2 2026 (4)

Where does Medicare Advantage cost trend sit versus 2025 and versus the trend used in the 2026 bids?

- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `assumption_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.price.dim_bid_cycle`: `line_of_business_id`, `bid_cycle_code`, `bid_cycle_name`
- `healthplan.price.fact_bid_posture`: `fiscal_quarter_id`, `bid_cycle_id`, `line_of_business_id`, `assumed_trend_rate`, `growth_posture_flag`, `margin_recovery_flag`

### Q2 2026 (5)

What cost trend was assumed in the Medicare Advantage bids that were just finalized?

- `healthplan.price.fact_bid_posture`: `fiscal_quarter_id`, `bid_cycle_id`, `line_of_business_id`, `assumed_trend_rate`, `growth_posture_flag`, `margin_recovery_flag`
- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `assumption_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.price.dim_bid_cycle`: `line_of_business_id`, `bid_cycle_code`, `bid_cycle_name`

### Q2 2026 (6)

Should this year's earnings outperformance be removed from the baseline used for 2027, or is it a recurring run rate?

- `healthplan.price.fact_earnings_bridge`: `fiscal_quarter_id`, `business_unit_id`, `earnings_scenario_id`, `line_of_business_id`, `development_amount`, `run_rate_amount`
- `healthplan.price.dim_earnings_scenario`: `business_unit_id`, `earnings_scenario_code`, `earnings_scenario_name`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.price.dim_rate_notice`: `line_of_business_id`, `rate_notice_code`, `rate_notice_name`

### Q2 2026 (7)

How much of the SG&A investment is one-time, and what benefit should carry into 2027?

- `healthplan.price.fact_sga_investment`: `fiscal_quarter_id`, `investment_program_id`, `business_unit_id`, `ai_program_id`, `carry_benefit_amount`, `recurring_amount`
- `healthplan.price.fact_earnings_bridge`: `fiscal_quarter_id`, `business_unit_id`, `earnings_scenario_id`, `line_of_business_id`, `contract_design_amount`, `development_amount`

### Q2 2026 (9)

How is Medicare Advantage utilization tracking versus the elevated-utilization piece of the original trend outlook?

- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `assumption_rate`
- `healthplan.medical.fact_utilization`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `utilization_driver_id`, `versus_assumption_index`, `favorable_flag`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.price.dim_cost_driver`: `clinical_category_id`, `cost_driver_code`, `cost_driver_name`

### Q2 2026 (10)

What run-rate margin is the capitated, value-based portion of Optum Health earning, and is that a trough?

- `healthplan.price.fact_value_based_margin`: `fiscal_quarter_id`, `business_unit_id`, `provider_group_id`, `margin_rate`, `trough_flag`, `versus_last_year_rate`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`

### Q2 2026 (12)

Why did Optum Insight beat expectations, and how should that be read against the rest of the year?

- `healthplan.price.fact_segment_result`: `fiscal_quarter_id`, `business_unit_id`, `outlook_raised_flag`, `beat_flag`, `revenue_amount`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`

### Q2 2026 (13)

Can AI pull Optum Health margins ahead of the long-term targets, or is the near-term work still basic operating repair?

- `healthplan.price.fact_ai_savings`: `fiscal_quarter_id`, `ai_program_id`, `business_unit_id`, `margin_target_id`, `basic_repair_flag`, `above_target_flag`
- `healthplan.price.dim_margin_target`: `line_of_business_id`, `business_unit_id`, `margin_target_code`, `margin_target_name`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.price.dim_ai_program`: `business_unit_id`, `ai_program_code`, `ai_program_name`

### Q1 2026 (1)

Is Medicare Advantage cost trend holding near the roughly 10% level used in pricing, or is it still closer to the prior 7% to 8% range?

- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `assumption_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.medical.fact_utilization`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `utilization_driver_id`, `favorable_flag`, `versus_assumption_index`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `prior_range_high_rate`, `prior_range_low_rate`

### Q1 2026 (3)

How much of the Optum Health outperformance is contract and benefit design versus lower utilization?

- `healthplan.price.fact_earnings_bridge`: `fiscal_quarter_id`, `business_unit_id`, `earnings_scenario_id`, `line_of_business_id`, `contract_design_amount`, `development_amount`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.product.dim_benefit_design`: `line_of_business_id`, `benefit_design_code`, `benefit_design_name`
- `healthplan.medical.fact_utilization`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `utilization_driver_id`, `utilization_index`, `versus_assumption_index`

### Q1 2026 (4)

How much of the Optum Health beat versus the internal plan was prior-period development rather than a higher run rate?

- `healthplan.price.dim_earnings_scenario`: `business_unit_id`, `earnings_scenario_code`, `earnings_scenario_name`
- `healthplan.price.fact_earnings_bridge`: `fiscal_quarter_id`, `business_unit_id`, `earnings_scenario_id`, `line_of_business_id`, `development_amount`, `run_rate_amount`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.time.dim_fiscal_quarter`: `guidance_horizon`, `fiscal_quarter_code`, `fiscal_quarter_name`

### Q1 2026 (5)

How confident is further Medicare Advantage margin recovery in 2027 now that the final rate is known?

- `healthplan.price.dim_rate_notice`: `line_of_business_id`, `rate_notice_code`, `rate_notice_name`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`
- `healthplan.price.fact_rate_update`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `rate_notice_id`, `final_rate_known_flag`, `recovery_confidence_code`
- `healthplan.price.fact_bid_posture`: `fiscal_quarter_id`, `bid_cycle_id`, `line_of_business_id`, `margin_recovery_flag`, `assumed_trend_rate`, `growth_posture_flag`

### Q1 2026 (6)

Will the company join the GLP-1 Balance Program, and is industry participation expected to meet the required thresholds?

- `healthplan.price.fact_glp1_decision`: `fiscal_quarter_id`, `glp1_program_id`, `line_of_business_id`, `join_flag`, `threshold_met_flag`
- `healthplan.price.dim_glp1_program`: `drug_id`, `line_of_business_id`, `glp1_program_code`, `glp1_program_name`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.medical.dim_drug`: `clinical_category_id`, `drug_code`, `drug_name`

### Q1 2026 (7)

Why is Optum Insight and Optum Rx earnings more weighted to the back half than in prior years?

- `healthplan.price.fact_earnings_cadence`: `fiscal_quarter_id`, `business_unit_id`, `line_of_business_id`, `back_half_favorable_flag`, `one_time_back_half_flag`, `exit_margin_rate`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.price.fact_subsidy_timing`: `fiscal_quarter_id`, `subsidy_id`, `business_unit_id`, `back_half_weight`, `first_half_weight`, `subsidy_amount`
- `healthplan.price.fact_segment_result`: `fiscal_quarter_id`, `business_unit_id`, `beat_flag`, `outlook_raised_flag`, `revenue_amount`

### Q1 2026 (8)

What incremental investment does the new PBM legislation require?

- `healthplan.price.fact_pbm_investment`: `fiscal_quarter_id`, `legislation_id`, `business_unit_id`, `incremental_investment_amount`, `in_plan_flag`
- `healthplan.price.dim_legislation`: `legislation_code`, `legislation_name`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`

### Q1 2026 (10)

What internal target exists for AI savings in G&A?

- `healthplan.price.fact_ai_savings`: `fiscal_quarter_id`, `ai_program_id`, `business_unit_id`, `margin_target_id`, `above_target_flag`, `savings_amount`
- `healthplan.price.dim_ai_program`: `business_unit_id`, `ai_program_code`, `ai_program_name`
- `healthplan.price.fact_sga_investment`: `fiscal_quarter_id`, `investment_program_id`, `business_unit_id`, `ai_program_id`, `one_time_amount`, `recurring_amount`

### Q1 2026 (11)

Can AI efficiency gains accelerate in 2027 and 2028 enough to lift segment margins above long-term targets?

- `healthplan.price.fact_ai_savings`: `fiscal_quarter_id`, `ai_program_id`, `business_unit_id`, `margin_target_id`, `above_target_flag`, `savings_amount`
- `healthplan.price.dim_ai_program`: `business_unit_id`, `ai_program_code`, `ai_program_name`
- `healthplan.price.fact_recovery_block`: `fiscal_quarter_id`, `legislation_id`, `line_of_business_id`, `block_code`, `trough_year_flag`
- `healthplan.price.fact_long_term_target`: `fiscal_quarter_id`, `margin_target_id`, `line_of_business_id`, `business_unit_id`, `baseline_rate`, `revised_flag`

### Q4 2025 (2)

Why did fourth-quarter Optum Health operating income finish well below the level implied by the prior outlook?

- `healthplan.price.fact_operating_income`: `fiscal_quarter_id`, `business_unit_id`, `outlook_amount`, `below_outlook_flag`, `operating_income_amount`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `prior_year_trend_rate`

### Q4 2025 (5)

How do Part D subsidy changes shift Optum Rx earnings toward the first half?

- `healthplan.price.fact_subsidy_timing`: `fiscal_quarter_id`, `subsidy_id`, `business_unit_id`, `first_half_weight`, `back_half_weight`, `subsidy_amount`
- `healthplan.price.dim_subsidy`: `line_of_business_id`, `subsidy_code`, `subsidy_name`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q4 2025 (7)

What is the 2026 medical-cost trend by Medicare, Medicaid, and commercial, and how did 2025 finish versus expectations?

- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `prior_year_trend_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `outlook_held_flat_flag`, `prior_range_high_rate`
- `healthplan.membership.fact_membership`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `business_unit_id`, `customer_segment_id`, `member_count`

### Q3 2025 (2)

Is commercial margin still on track to return to the 7% to 9% range in 2027, and is the 2025 baseline closer to 3% to 5%?

- `healthplan.price.fact_long_term_target`: `fiscal_quarter_id`, `margin_target_id`, `line_of_business_id`, `business_unit_id`, `baseline_rate`, `revised_flag`
- `healthplan.price.dim_margin_target`: `line_of_business_id`, `business_unit_id`, `margin_target_code`, `margin_target_name`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q3 2025 (5)

How large was the third-quarter step-up in discretionary investment, and how much is run rate versus one-time?

- `healthplan.price.fact_discretionary_spend`: `fiscal_quarter_id`, `investment_program_id`, `business_unit_id`, `run_rate_amount`, `step_up_amount`, `one_time_amount`
- `healthplan.price.dim_earnings_scenario`: `business_unit_id`, `earnings_scenario_code`, `earnings_scenario_name`
- `healthplan.price.fact_sga_investment`: `fiscal_quarter_id`, `investment_program_id`, `business_unit_id`, `ai_program_id`, `one_time_amount`, `carry_benefit_amount`
- `healthplan.price.fact_investment_leverage`: `fiscal_quarter_id`, `investment_program_id`, `business_unit_id`, `next_year_leverage_rate`, `investment_amount`, `technology_flag`

### Q3 2025 (7)

Why did Tier 3 branded drugs on Medicare Advantage and stand-alone Part D plans move from copay to coinsurance?

- `healthplan.price.fact_member_cost_share`: `fiscal_quarter_id`, `benefit_design_id`, `drug_id`, `line_of_business_id`, `design_change_flag`, `coinsurance_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.medical.dim_drug`: `clinical_category_id`, `drug_code`, `drug_name`
- `healthplan.product.dim_benefit_design`: `line_of_business_id`, `benefit_design_code`, `benefit_design_name`

### Q3 2025 (8)

Is the Medicaid margin still in a roughly negative 1% to 1.5% range, and what blocks a recovery in 2027 and 2028?

- `healthplan.price.fact_recovery_block`: `fiscal_quarter_id`, `legislation_id`, `line_of_business_id`, `block_code`, `trough_year_flag`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`
- `healthplan.price.dim_legislation`: `legislation_code`, `legislation_name`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q3 2025 (9)

What employer medical-cost trend is being seen this year and next?

- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `trend_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.channel.dim_employer_account`: `customer_segment_id`, `employer_account_code`, `employer_account_name`

### Q3 2025 (12)

Is mitigation of the risk-adjustment headwind coming from recontracting UnitedHealthcare or from other payers?

- `healthplan.price.fact_recontract_savings`: `fiscal_quarter_id`, `business_unit_id`, `line_of_business_id`, `payer_source_code`, `savings_amount`
- `healthplan.price.fact_coding_headwind`: `fiscal_quarter_id`, `risk_model_id`, `business_unit_id`, `line_of_business_id`, `headwind_amount`, `versus_industry_amount`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.price.fact_risk_adjustment`: `fiscal_quarter_id`, `line_of_business_id`, `accrual_amount`, `clearer_position_flag`, `unchanged_flag`

## Elevance Health

### Q2 2026 (1)

Is the back half of the year more favorable than the front half for the negative Medicaid margin, and where does the year exit?

- `healthplan.price.fact_earnings_cadence`: `fiscal_quarter_id`, `business_unit_id`, `line_of_business_id`, `back_half_favorable_flag`, `exit_margin_rate`, `one_time_back_half_flag`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`
- `healthplan.price.fact_rate_update`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `rate_notice_id`, `embedded_outlook_rate`, `final_rate_known_flag`
- `healthplan.price.fact_subsidy_timing`: `fiscal_quarter_id`, `subsidy_id`, `business_unit_id`, `back_half_weight`, `first_half_weight`, `subsidy_amount`

### Q2 2026 (2)

How large are the planned Medicaid exits relative to the Medicaid revenue base?

- `healthplan.price.fact_contract_revenue`: `fiscal_quarter_id`, `state_program_id`, `business_unit_id`, `line_of_business_id`, `revenue_amount`, `share_of_book_rate`
- `healthplan.membership.fact_contract_exit`: `fiscal_quarter_id`, `state_id`, `state_program_id`, `line_of_business_id`, `exit_flag`, `exited_lives_count`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.membership.fact_competitive_position`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `state_id`, `planned_exit_flag`, `reacceleration_timing_code`

### Q2 2026 (3)

How did first-half exchange results compare with plan once risk adjustment was clearer, and where does the risk-adjustment position stand?

- `healthplan.price.fact_risk_adjustment`: `fiscal_quarter_id`, `line_of_business_id`, `clearer_position_flag`, `accrual_amount`, `unchanged_flag`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.membership.fact_exchange_enrollment`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `metal_tier_id`, `versus_plan_lives_count`, `member_count`
- `healthplan.price.fact_coding_headwind`: `fiscal_quarter_id`, `risk_model_id`, `business_unit_id`, `line_of_business_id`, `headwind_amount`, `versus_industry_amount`

### Q2 2026 (4)

What cost trend was assumed for Medicaid, the exchanges, and Medicare Advantage, and what did the second quarter actually show?

- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `assumption_rate`
- `healthplan.price.fact_bid_posture`: `fiscal_quarter_id`, `bid_cycle_id`, `line_of_business_id`, `assumed_trend_rate`, `growth_posture_flag`, `margin_recovery_flag`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.membership.fact_membership`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `business_unit_id`, `customer_segment_id`, `member_count`

### Q2 2026 (6)

For 2027, are ACA and Medicare Advantage bids aimed at growth or at further margin recovery?

- `healthplan.price.fact_bid_posture`: `fiscal_quarter_id`, `bid_cycle_id`, `line_of_business_id`, `growth_posture_flag`, `margin_recovery_flag`, `assumed_trend_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.price.dim_bid_cycle`: `line_of_business_id`, `bid_cycle_code`, `bid_cycle_name`
- `healthplan.price.fact_recovery_block`: `fiscal_quarter_id`, `legislation_id`, `line_of_business_id`, `block_code`, `trough_year_flag`

### Q2 2026 (8)

How much operating leverage do the one-time investments create next year, and are they technology or people?

- `healthplan.price.fact_investment_leverage`: `fiscal_quarter_id`, `investment_program_id`, `business_unit_id`, `next_year_leverage_rate`, `technology_flag`, `investment_amount`
- `healthplan.price.dim_investment_program`: `business_unit_id`, `investment_program_code`, `investment_program_name`

### Q2 2026 (9)

Why did better Medicaid rates not lift the margin outlook, and why are more exits still required?

- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `outlook_held_flat_flag`, `full_year_margin_rate`
- `healthplan.price.fact_rate_update`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `rate_notice_id`, `embedded_outlook_rate`, `final_rate_known_flag`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.membership.fact_membership`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `business_unit_id`, `customer_segment_id`, `outlook_direction`

### Q2 2026 (10)

Over two to three years, what Medicaid pressures remain if this year is the trough?

- `healthplan.price.fact_recovery_block`: `fiscal_quarter_id`, `legislation_id`, `line_of_business_id`, `block_code`, `trough_year_flag`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`
- `healthplan.membership.fact_work_requirement`: `fiscal_quarter_id`, `state_id`, `line_of_business_id`, `attrition_count`, `early_start_flag`, `stay_or_leave_code`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q2 2026 (15)

Is there anything unusual in commercial enrollment between fee-based and employer-group risk, and how is pricing being balanced against elevated trend?

- `healthplan.price.fact_pricing_balance`: `fiscal_quarter_id`, `line_of_business_id`, `benefit_design_id`, `price_change_rate`, `trend_coverage_rate`, `fourth_quarter_better_flag`
- `healthplan.membership.fact_funding_mix`: `fiscal_quarter_id`, `line_of_business_id`, `channel_id`, `employer_account_id`, `fee_based_lives_count`, `moved_to_fee_based_flag`
- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `assumption_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q2 2026 (16)

What are the early puts and takes for 2027 by business versus the long-term growth path?

- `healthplan.price.fact_outlook_driver`: `fiscal_quarter_id`, `business_unit_id`, `line_of_business_id`, `versus_framework_code`, `supports_faster_growth_flag`, `driver_amount`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `assumption_rate`

### Q1 2026 (4)

How does the Carelon and CarelonRx margin get back to the reiterated full-year outlook after a weaker quarter?

- `healthplan.price.fact_services_margin`: `fiscal_quarter_id`, `business_unit_id`, `care_service_id`, `margin_target_id`, `full_year_outlook_rate`, `margin_rate`
- `healthplan.price.fact_segment_result`: `fiscal_quarter_id`, `business_unit_id`, `outlook_raised_flag`, `beat_flag`, `revenue_amount`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`

### Q1 2026 (6)

With Medicaid margin ahead of plan, what rate increases are embedded in the 2026 outlook?

- `healthplan.price.fact_rate_update`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `rate_notice_id`, `embedded_outlook_rate`, `final_rate_known_flag`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.membership.fact_membership`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `business_unit_id`, `customer_segment_id`, `decline_rate`

### Q1 2026 (11)

What efficiency gains is AI already showing, and how do the related investments track against those gains?

- `healthplan.price.fact_sga_investment`: `fiscal_quarter_id`, `investment_program_id`, `business_unit_id`, `ai_program_id`, `one_time_amount`, `recurring_amount`
- `healthplan.price.dim_ai_program`: `business_unit_id`, `ai_program_code`, `ai_program_name`
- `healthplan.price.fact_ai_savings`: `fiscal_quarter_id`, `ai_program_id`, `business_unit_id`, `margin_target_id`, `savings_amount`, `above_target_flag`
- `healthplan.price.fact_investment_leverage`: `fiscal_quarter_id`, `investment_program_id`, `business_unit_id`, `investment_amount`, `still_in_outlook_amount`, `technology_flag`

### Q1 2026 (14)

How much of the targeted 2027 earnings growth depends on pricing and trend the company can influence if Medicaid stays pressured?

- `healthplan.price.fact_controllable_earnings`: `fiscal_quarter_id`, `line_of_business_id`, `ai_program_id`, `controllable_share`, `medicaid_pressure_flag`
- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `assumption_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.price.dim_ai_program`: `business_unit_id`, `ai_program_code`, `ai_program_name`

### Q4 2025 (1)

How does the 2026 cost-trend assumption compare with 2025 across commercial, Medicaid, Medicare, and the exchanges?

- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `assumption_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.price.dim_margin_target`: `line_of_business_id`, `business_unit_id`, `margin_target_code`, `margin_target_name`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`

### Q4 2025 (3)

What pricing and cost drivers sit behind 2026 health-benefits margins, including the negative Medicaid margin and a better fourth quarter?

- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `outlook_held_flat_flag`, `full_year_margin_rate`
- `healthplan.price.fact_pricing_balance`: `fiscal_quarter_id`, `line_of_business_id`, `benefit_design_id`, `fourth_quarter_better_flag`, `price_change_rate`, `trend_coverage_rate`
- `healthplan.medical.fact_part_d_utilization`: `fiscal_quarter_id`, `line_of_business_id`, `drug_id`, `benefit_design_id`, `step_up_flag`, `utilization_index`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q4 2025 (4)

What is the 2026 Medicaid rate outlook, and how should rates be thought about after this year?

- `healthplan.price.fact_rate_update`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `rate_notice_id`, `embedded_outlook_rate`, `recovery_confidence_code`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.price.fact_state_rate_gap`: `fiscal_quarter_id`, `state_id`, `rate_notice_id`, `line_of_business_id`, `later_cycle_rate`, `base_rate_gap`

### Q4 2025 (5)

Which Medicare or commercial opportunities support a return to faster earnings growth in 2027 after two years of elevated trend?

- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `prior_year_trend_rate`
- `healthplan.price.fact_outlook_driver`: `fiscal_quarter_id`, `business_unit_id`, `line_of_business_id`, `supports_faster_growth_flag`, `driver_amount`, `versus_framework_code`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`
- `healthplan.price.fact_pricing_balance`: `fiscal_quarter_id`, `line_of_business_id`, `benefit_design_id`, `trend_coverage_rate`, `fourth_quarter_better_flag`, `price_change_rate`

### Q4 2025 (6)

Which investment buckets were pulled forward, and how much of that spending is still inside the 2026 outlook?

- `healthplan.price.dim_investment_program`: `business_unit_id`, `investment_program_code`, `investment_program_name`
- `healthplan.price.fact_investment_leverage`: `fiscal_quarter_id`, `investment_program_id`, `business_unit_id`, `still_in_outlook_amount`, `investment_amount`, `next_year_leverage_rate`

### Q4 2025 (7)

What changed in the long-term margin targets for Medicaid, Medicare, and commercial, and is the lower CarelonRx target only membership loss?

- `healthplan.price.dim_margin_target`: `line_of_business_id`, `business_unit_id`, `margin_target_code`, `margin_target_name`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`
- `healthplan.price.fact_long_term_target`: `fiscal_quarter_id`, `margin_target_id`, `line_of_business_id`, `business_unit_id`, `baseline_rate`, `revised_flag`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q4 2025 (10)

How can the Medicare Advantage rate notice be mitigated on top of this year's benefit cuts, and what does it mean for industry margins?

- `healthplan.price.fact_industry_margin`: `fiscal_quarter_id`, `line_of_business_id`, `rate_notice_id`, `industry_margin_rate`, `notice_effect_rate`
- `healthplan.product.dim_benefit_design`: `line_of_business_id`, `benefit_design_code`, `benefit_design_name`
- `healthplan.price.dim_rate_notice`: `line_of_business_id`, `rate_notice_code`, `rate_notice_name`
- `healthplan.price.fact_rate_update`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `rate_notice_id`, `embedded_outlook_rate`, `final_rate_known_flag`

### Q4 2025 (14)

How much of CarelonRx and Carelon services revenue and margin comes from health-benefits enrollment losses versus external clients?

- `healthplan.price.fact_contract_revenue`: `fiscal_quarter_id`, `state_program_id`, `business_unit_id`, `line_of_business_id`, `source_code`, `revenue_amount`
- `healthplan.membership.fact_external_lives`: `fiscal_quarter_id`, `business_unit_id`, `line_of_business_id`, `client_source_code`, `external_lives_count`, `health_plan_lives_lost_count`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.medical.dim_care_service`: `business_unit_id`, `care_service_code`, `care_service_name`

### Q2 2025 (1)

How much of the ACA pressure is unit-cost trend versus the risk pool, and why is risk adjustment unchanged despite higher morbidity?

- `healthplan.price.fact_unit_cost`: `fiscal_quarter_id`, `line_of_business_id`, `cost_driver_id`, `clinical_category_id`, `share_of_pressure_rate`, `unit_cost_rate`
- `healthplan.price.fact_risk_adjustment`: `fiscal_quarter_id`, `line_of_business_id`, `unchanged_flag`, `accrual_amount`, `clearer_position_flag`
- `healthplan.price.dim_cost_driver`: `clinical_category_id`, `cost_driver_code`, `cost_driver_name`
- `healthplan.medical.fact_risk_pool`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `morbidity_index`, `worse_than_plan_flag`

### Q2 2025 (2)

How much of the guidance cut is the public exchanges versus Medicaid, and is the Medicaid issue a delayed rate catch-up?

- `healthplan.price.fact_guidance_bridge`: `fiscal_quarter_id`, `line_of_business_id`, `delayed_rate_flag`, `program_share`, `revision_amount`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q2 2025 (3)

Are Medicaid base-period rates being set too low relative to forward trend, leaving the company repeatedly underpaid?

- `healthplan.price.fact_state_rate_gap`: `fiscal_quarter_id`, `state_id`, `rate_notice_id`, `line_of_business_id`, `base_rate_gap`, `later_cycle_rate`
- `healthplan.price.fact_rate_update`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `rate_notice_id`, `embedded_outlook_rate`, `final_rate_known_flag`
- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `assumption_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q2 2025 (5)

What would be done differently in ACA pricing and in state rate negotiations to make results more predictable?

- `healthplan.price.fact_aca_price`: `fiscal_quarter_id`, `line_of_business_id`, `bid_cycle_id`, `predictability_flag`, `price_change_rate`
- `healthplan.price.fact_state_rate_gap`: `fiscal_quarter_id`, `state_id`, `rate_notice_id`, `line_of_business_id`, `base_rate_gap`, `later_cycle_rate`
- `healthplan.medical.fact_risk_pool`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `worse_than_plan_flag`, `morbidity_index`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q2 2025 (13)

Where do commercial margins stand now, and how fast can they return to target?

- `healthplan.price.fact_long_term_target`: `fiscal_quarter_id`, `margin_target_id`, `line_of_business_id`, `business_unit_id`, `baseline_rate`, `revised_flag`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.price.dim_margin_target`: `line_of_business_id`, `business_unit_id`, `margin_target_code`, `margin_target_name`
