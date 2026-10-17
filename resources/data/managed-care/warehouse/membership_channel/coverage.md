# Health Plan Inc membership and channel

This slice owns line of business, geography, channel, employer, and membership counts for Health Plan Inc. Membership quantity lives here. Medical utilization and provider capacity are owned in medical_provider. Premiums, medical-cost trend rates, and margins are owned in price_benefit. A membership row names those populations only as a partial identity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `provider_group_identity` | `provider_group_id` | `sf:healthplan.provider.dim_provider_group` `provider_group_id` |
| `care_service_identity` | `care_service_id` | `sf:healthplan.medical.dim_care_service` `care_service_id` |
| `clinical_program_identity` | `clinical_program_id` | `sf:healthplan.medical.dim_clinical_program` `clinical_program_id` |

## Numbered questions

## UnitedHealth Group

### Q2 2026 (3)

Which parts of the operating turnaround are largely finished, and where do the remaining gaps sit?

- `healthplan.membership.fact_turnaround_status`: `fiscal_quarter_id`, `business_unit_id`, `finished_flag`, `open_gap_flag`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`

### Q1 2026 (9)

Where do the value-based life tranches under negotiation stand, and are new provider groups being added?

- `healthplan.membership.fact_value_based_lives`: `fiscal_quarter_id`, `business_unit_id`, `provider_group_id`, `line_of_business_id`, `negotiation_lives_count`, `new_group_flag`
- `healthplan.provider.dim_provider`: `provider_group_id`, `provider_code`, `provider_name`
- `healthplan.provider.dim_provider_group`: `provider_group_code`, `provider_group_name`

### Q1 2026 (12)

How should prior-period development in the quarter be split between UnitedHealthcare and Optum Health?

- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.price.fact_earnings_bridge`: `fiscal_quarter_id`, `business_unit_id`, `earnings_scenario_id`, `line_of_business_id`, `development_amount`, `contract_design_amount`
- `healthplan.price.dim_earnings_scenario`: `business_unit_id`, `earnings_scenario_code`, `earnings_scenario_name`
- `healthplan.price.fact_segment_result`: `fiscal_quarter_id`, `business_unit_id`, `beat_flag`, `revenue_amount`, `outlook_raised_flag`

### Q4 2025 (1)

With 2026 Medicare Advantage membership guided down sharply, are margins at a bottom, and should 2027 margins improve as benefits are refined?

- `healthplan.membership.fact_membership`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `business_unit_id`, `customer_segment_id`, `decline_rate`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`
- `healthplan.product.dim_benefit_design`: `line_of_business_id`, `benefit_design_code`, `benefit_design_name`
- `healthplan.price.dim_rate_notice`: `line_of_business_id`, `rate_notice_code`, `rate_notice_name`

### Q4 2025 (4)

How do 2026 Medicaid rates compare with 2025, and would an earlier start to work requirements change the margin view?

- `healthplan.membership.fact_work_requirement`: `fiscal_quarter_id`, `state_id`, `line_of_business_id`, `early_start_flag`, `attrition_count`, `stay_or_leave_code`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `outlook_held_flat_flag`, `full_year_margin_rate`
- `healthplan.price.fact_rate_update`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `rate_notice_id`, `embedded_outlook_rate`, `rate_change_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q4 2025 (6)

How should member losses tied to UnitedHealthcare be weighed against the new Optum Rx clients?

- `healthplan.membership.fact_external_lives`: `fiscal_quarter_id`, `business_unit_id`, `line_of_business_id`, `client_source_code`, `external_lives_count`, `health_plan_lives_lost_count`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.price.fact_contract_revenue`: `fiscal_quarter_id`, `state_program_id`, `business_unit_id`, `line_of_business_id`, `source_code`, `revenue_amount`
- `healthplan.membership.fact_membership`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `business_unit_id`, `customer_segment_id`, `member_change_count`

### Q4 2025 (8)

Have any Optum Care turnaround initiatives produced surprises versus the plan?

- `healthplan.membership.fact_initiative_result`: `fiscal_quarter_id`, `business_unit_id`, `clinical_program_id`, `on_plan_flag`, `surprise_flag`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`

### Q3 2025 (1)

Where does Optum Insight stand competitively, and when should investment translate into faster growth?

- `healthplan.membership.fact_competitive_position`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `state_id`, `reacceleration_timing_code`, `competitor_loss_flag`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.price.fact_segment_result`: `fiscal_quarter_id`, `business_unit_id`, `beat_flag`, `outlook_raised_flag`, `revenue_amount`

### Q3 2025 (3)

How does the expected 2026 Medicare Advantage membership decline split among individual, dual-eligible, and group lives?

- `healthplan.membership.fact_ma_split`: `fiscal_quarter_id`, `product_id`, `line_of_business_id`, `customer_segment_id`, `individual_lives_count`, `dual_lives_count`
- `healthplan.membership.fact_membership`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `business_unit_id`, `customer_segment_id`, `decline_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `outlook_held_flat_flag`

### Q3 2025 (4)

Does the company agree that industry Medicare Advantage enrollment is roughly flat, and what share of lives is a realistic value-based-care market?

- `healthplan.membership.fact_industry_enrollment`: `fiscal_quarter_id`, `line_of_business_id`, `addressable_share`, `flat_enrollment_flag`, `industry_lives_count`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q3 2025 (10)

How wide is the Optum Health portfolio rationalization under the new approach?

- `healthplan.membership.fact_portfolio_scope`: `fiscal_quarter_id`, `business_unit_id`, `line_of_business_id`, `exited_contract_count`, `retained_contract_count`, `risk_exit_flag`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.price.fact_value_based_margin`: `fiscal_quarter_id`, `business_unit_id`, `provider_group_id`, `margin_rate`, `trough_flag`, `versus_last_year_rate`

### Q3 2025 (11)

How much of the Optum Health turnaround is walking away from risk versus repairing the remaining book?

- `healthplan.membership.fact_portfolio_scope`: `fiscal_quarter_id`, `business_unit_id`, `line_of_business_id`, `risk_exit_flag`, `exited_contract_count`, `retained_contract_count`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`

## Elevance Health

### Q2 2026 (5)

Why did seasonal favorability increase from the first quarter to the second, and does any of that reverse later in the year?

- `healthplan.membership.fact_seasonality`: `fiscal_quarter_id`, `line_of_business_id`, `benefit_design_id`, `favorability_index`, `reverses_later_flag`
- `healthplan.product.dim_benefit_design`: `line_of_business_id`, `benefit_design_code`, `benefit_design_name`

### Q2 2026 (7)

What criteria decide which Medicaid programs are exited, such as program type, state, or share position?

- `healthplan.membership.fact_contract_exit`: `fiscal_quarter_id`, `state_id`, `state_program_id`, `line_of_business_id`, `exit_criteria_code`, `share_position_rate`
- `healthplan.geography.dim_state_program`: `state_id`, `line_of_business_id`, `state_program_code`, `state_program_name`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.membership.fact_competitive_position`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `state_id`, `competitor_loss_flag`, `planned_exit_flag`

### Q1 2026 (1)

Are employers emphasizing different priorities in the pharmacy and commercial selling seasons, including AI or a softer economy?

- `healthplan.membership.fact_selling_season`: `fiscal_quarter_id`, `employer_account_id`, `business_unit_id`, `channel_id`, `priority_code`, `changed_versus_prior_flag`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.channel.dim_employer_account`: `customer_segment_id`, `employer_account_code`, `employer_account_name`
- `healthplan.price.dim_ai_program`: `business_unit_id`, `ai_program_code`, `ai_program_name`

### Q1 2026 (2)

Are Medicaid membership declines concentrated in lower-utilizing members, and how does that sit against the high-single-digit decline outlook excluding Indiana growth?

- `healthplan.membership.fact_membership_mix`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `customer_segment_id`, `indiana_excluded_decline_rate`, `acuity_index`
- `healthplan.membership.fact_membership`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `business_unit_id`, `customer_segment_id`, `decline_rate`
- `healthplan.geography.dim_state`: `region_id`, `state_code`, `state_name`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q1 2026 (3)

How are members behaving after deductibles reset, and are higher fuel prices or the broader economy changing utilization?

- `healthplan.membership.fact_deductible_behavior`: `fiscal_quarter_id`, `line_of_business_id`, `customer_segment_id`, `macro_pressure_flag`, `utilization_index`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.channel.dim_employer_account`: `customer_segment_id`, `employer_account_code`, `employer_account_name`
- `healthplan.medical.fact_utilization`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `utilization_driver_id`, `utilization_index`, `versus_assumption_index`

### Q1 2026 (5)

What did the second Blue Bid sell in 2026, what does the 2027 pipeline look like, and which Carelon services attach?

- `healthplan.membership.fact_service_attach`: `fiscal_quarter_id`, `care_service_id`, `blue_bid_id`, `business_unit_id`, `attached_service_count`, `risk_bearing_flag`
- `healthplan.membership.fact_blue_bid`: `fiscal_quarter_id`, `employer_account_id`, `business_unit_id`, `pipeline_count`, `won_bid_count`
- `healthplan.medical.dim_care_service`: `business_unit_id`, `care_service_code`, `care_service_name`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`

### Q1 2026 (9)

Did higher-than-expected exchange enrollment come with a worse risk pool, including people moving from Medicaid?

- `healthplan.membership.fact_migration`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `migrated_lives_count`, `attrition_count`, `historical_attrition_rate`
- `healthplan.membership.fact_exchange_enrollment`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `metal_tier_id`, `member_count`, `open_enrollment_lives_count`
- `healthplan.medical.fact_risk_pool`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `worse_than_plan_flag`, `morbidity_index`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q1 2026 (10)

What member attrition from work requirements is assumed for 2027, and which states are stay-or-leave decisions?

- `healthplan.membership.fact_work_requirement`: `fiscal_quarter_id`, `state_id`, `line_of_business_id`, `attrition_count`, `stay_or_leave_code`, `early_start_flag`
- `healthplan.membership.fact_membership`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `business_unit_id`, `customer_segment_id`, `decline_rate`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.price.fact_recovery_block`: `fiscal_quarter_id`, `legislation_id`, `line_of_business_id`, `block_code`, `trough_year_flag`

### Q1 2026 (13)

How far did the bronze-plan mix shift, and how does that compare with industry metal-tier data?

- `healthplan.membership.fact_metal_mix`: `fiscal_quarter_id`, `metal_tier_id`, `line_of_business_id`, `industry_mix_share`, `mix_share`
- `healthplan.product.dim_metal_tier`: `metal_tier_code`, `metal_tier_name`

### Q4 2025 (2)

What happened in Medicare annual enrollment to drive the membership revision, and how does the commercial-risk decline split between the exchanges and employer group?

- `healthplan.membership.fact_enrollment_event`: `fiscal_quarter_id`, `line_of_business_id`, `product_id`, `channel_id`, `revision_lives_count`, `post_enrollment_lives_count`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.membership.fact_funding_mix`: `fiscal_quarter_id`, `line_of_business_id`, `channel_id`, `employer_account_id`, `risk_lives_count`, `moved_to_fee_based_flag`
- `healthplan.membership.fact_exchange_enrollment`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `metal_tier_id`, `open_enrollment_lives_count`, `member_count`

### Q4 2025 (8)

Where did ACA membership start after open enrollment, and has January utilization changed?

- `healthplan.membership.fact_enrollment_event`: `fiscal_quarter_id`, `line_of_business_id`, `product_id`, `channel_id`, `early_utilization_index`, `post_enrollment_lives_count`
- `healthplan.membership.fact_exchange_enrollment`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `metal_tier_id`, `open_enrollment_lives_count`, `member_count`
- `healthplan.medical.fact_utilization`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `utilization_driver_id`, `utilization_index`, `versus_assumption_index`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q4 2025 (9)

Do larger-than-expected membership declines say anything about competitive position, even if exiting weak markets is intentional?

- `healthplan.membership.fact_competitive_position`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `state_id`, `competitor_loss_flag`, `planned_exit_flag`
- `healthplan.membership.fact_contract_exit`: `fiscal_quarter_id`, `state_id`, `state_program_id`, `line_of_business_id`, `exit_criteria_code`, `share_position_rate`

### Q4 2025 (12)

Is the expected Medicaid membership decline same-store or a state or contract exit, and why does a larger decline not add more margin pressure?

- `healthplan.membership.fact_membership_bridge`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `membership_cohort_id`, `attrition_count`, `exit_lives_count`
- `healthplan.membership.fact_membership`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `business_unit_id`, `customer_segment_id`, `decline_rate`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`
- `healthplan.product.dim_membership_cohort`: `line_of_business_id`, `membership_cohort_code`, `membership_cohort_name`

### Q4 2025 (13)

How much of the commercial-risk membership decline is pricing on government accounts versus employers moving to fee-based coverage, and does the long-term margin assume more attrition?

- `healthplan.membership.fact_funding_mix`: `fiscal_quarter_id`, `line_of_business_id`, `channel_id`, `employer_account_id`, `moved_to_fee_based_flag`, `risk_lives_count`
- `healthplan.membership.fact_membership_bridge`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `membership_cohort_id`, `attrition_count`, `pressure_flag`
- `healthplan.price.dim_margin_target`: `line_of_business_id`, `business_unit_id`, `margin_target_code`, `margin_target_name`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`

### Q2 2025 (6)

What further ACA membership attrition and risk-pool shift is assumed, including people moving from Medicaid?

- `healthplan.membership.fact_migration`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `historical_attrition_rate`, `attrition_count`, `migrated_lives_count`
- `healthplan.membership.fact_exchange_enrollment`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `metal_tier_id`, `member_count`, `open_enrollment_lives_count`
- `healthplan.medical.fact_risk_pool`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `worse_than_plan_flag`, `morbidity_index`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q2 2025 (8)

Why did proactive risk-pool work during Medicaid redeterminations still fail to keep up with the shifts?

- `healthplan.membership.fact_redetermination`: `fiscal_quarter_id`, `state_id`, `line_of_business_id`, `membership_cohort_id`, `kept_up_flag`, `managed_shift_index`
- `healthplan.medical.fact_risk_pool`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `worse_than_plan_flag`, `morbidity_index`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q2 2025 (12)

Is it time to exit states or shrink Medicaid populations where the rate disconnect persists?

- `healthplan.membership.fact_contract_exit`: `fiscal_quarter_id`, `state_id`, `state_program_id`, `line_of_business_id`, `exit_criteria_code`, `share_position_rate`
- `healthplan.price.fact_state_rate_gap`: `fiscal_quarter_id`, `state_id`, `rate_notice_id`, `line_of_business_id`, `later_cycle_rate`, `base_rate_gap`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `outlook_held_flat_flag`, `full_year_margin_rate`

### Q2 2025 (14)

Are delayed exchange eligibility rechecks finished, and is the resulting member attrition already in the updated outlook?

- `healthplan.membership.fact_eligibility_recheck`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `in_outlook_flag`, `recheck_finished_flag`, `attrition_count`
- `healthplan.membership.fact_exchange_enrollment`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `metal_tier_id`, `member_count`, `open_enrollment_lives_count`
- `healthplan.membership.fact_work_requirement`: `fiscal_quarter_id`, `state_id`, `line_of_business_id`, `attrition_count`, `early_start_flag`, `stay_or_leave_code`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
