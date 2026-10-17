# Health Plan Inc medical cost and provider capacity

This slice owns providers, clinical categories, utilization, dispute volume, and network capacity for Health Plan Inc. Procedure counts and panel slots live here. Membership counts stay in membership_channel. Trend rates, dispute cost, and margins stay in price_benefit.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `benefit_design_identity` | `benefit_design_id` | `sf:healthplan.product.dim_benefit_design` `benefit_design_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `membership_cohort_identity` | `membership_cohort_id` | `sf:healthplan.product.dim_membership_cohort` `membership_cohort_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `state_identity` | `state_id` | `sf:healthplan.geography.dim_state` `state_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |
| `business_unit_identity` | `business_unit_id` | `sf:healthplan.product.dim_business_unit` `business_unit_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `state_identity` | `state_id` | `sf:healthplan.geography.dim_state` `state_id` |
| `state_program_identity` | `state_program_id` | `sf:healthplan.geography.dim_state_program` `state_program_id` |
| `benefit_design_identity` | `benefit_design_id` | `sf:healthplan.product.dim_benefit_design` `benefit_design_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:healthplan.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `line_of_business_identity` | `line_of_business_id` | `sf:healthplan.product.dim_line_of_business` `line_of_business_id` |

## Numbered questions

## UnitedHealth Group

### Q2 2026 (8)

Why are independent dispute-resolution costs accelerating now, across win rates, dispute volume, and resolution timing?

- `healthplan.medical.fact_dispute_volume`: `fiscal_quarter_id`, `dispute_type_id`, `line_of_business_id`, `case_count`, `resolution_days`, `win_rate`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `dispute_type_id`, `line_of_business_id`, `accelerating_flag`, `cost_amount`
- `healthplan.medical.dim_dispute_type`: `dispute_type_code`, `dispute_type_name`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q2 2026 (11)

What is happening to outpatient surgical volumes?

- `healthplan.medical.fact_outpatient_surgery`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `facility_id`, `procedure_count`, `catch_up_risk_flag`
- `healthplan.medical.dim_clinical_category`: `clinical_category_code`, `clinical_category_name`
- `healthplan.medical.fact_utilization`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `utilization_driver_id`, `favorable_flag`, `utilization_index`
- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `assumption_rate`

### Q1 2026 (2)

How much of Medicare Advantage trend is the acuity and provider-billing dynamic, and is that limited to Medicare Advantage?

- `healthplan.medical.fact_coding_intensity`: `fiscal_quarter_id`, `risk_model_id`, `provider_group_id`, `line_of_business_id`, `clinical_category_id`, `limited_to_medicare_flag`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.medical.dim_utilization_driver`: `utilization_driver_code`, `utilization_driver_name`
- `healthplan.membership.fact_membership_mix`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `customer_segment_id`, `acuity_index`, `indiana_excluded_decline_rate`

### Q1 2026 (13)

When the delayed Medicare Advantage risk-model recalibration arrives, how large is the cut to chronic-condition codes for value-based providers?

- `healthplan.medical.fact_coding_intensity`: `fiscal_quarter_id`, `risk_model_id`, `provider_group_id`, `line_of_business_id`, `clinical_category_id`, `chronic_code_cut_count`
- `healthplan.medical.dim_risk_model`: `risk_model_code`, `risk_model_name`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.provider.dim_provider_group`: `provider_group_code`, `provider_group_name`

### Q1 2026 (14)

How are physician, hospital, and drug trends running versus expectations in each book, and which clinical and network actions are moving them?

- `healthplan.medical.fact_clinical_action`: `fiscal_quarter_id`, `clinical_program_id`, `clinical_category_id`, `line_of_business_id`, `network_id`, `action_on_flag`
- `healthplan.medical.dim_clinical_category`: `clinical_category_code`, `clinical_category_name`
- `healthplan.medical.dim_clinical_program`: `clinical_category_id`, `clinical_program_code`, `clinical_program_name`
- `healthplan.medical.fact_network_capacity`: `fiscal_quarter_id`, `network_id`, `provider_group_id`, `clinical_category_id`, `accepting_patient_flag`, `panel_slot_count`

### Q4 2025 (3)

How does the coding headwind from the risk model and chart review compare with UnitedHealth's experience under the prior model and with the industry?

- `healthplan.medical.dim_risk_model`: `risk_model_code`, `risk_model_name`
- `healthplan.price.fact_coding_headwind`: `fiscal_quarter_id`, `risk_model_id`, `business_unit_id`, `line_of_business_id`, `versus_prior_model_amount`, `headwind_amount`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.price.fact_risk_adjustment`: `fiscal_quarter_id`, `line_of_business_id`, `accrual_amount`, `clearer_position_flag`, `unchanged_flag`

### Q3 2025 (6)

What utilization is expected in the fourth quarter, including any step-up in Part D?

- `healthplan.medical.fact_part_d_utilization`: `fiscal_quarter_id`, `line_of_business_id`, `drug_id`, `benefit_design_id`, `step_up_flag`, `utilization_index`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.medical.fact_utilization`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `utilization_driver_id`, `utilization_index`, `versus_assumption_index`
- `healthplan.price.fact_pricing_balance`: `fiscal_quarter_id`, `line_of_business_id`, `benefit_design_id`, `fourth_quarter_better_flag`, `price_change_rate`, `trend_coverage_rate`

## Elevance Health

### Q2 2026 (11)

Is the first-half utilization pattern a bounce-back from a lighter flu and weather effect than peers reported?

- `healthplan.medical.fact_flu_weather`: `fiscal_quarter_id`, `utilization_driver_id`, `line_of_business_id`, `disruption_index`, `peer_gap_index`, `bounce_back_flag`
- `healthplan.medical.fact_peer_utilization`: `fiscal_quarter_id`, `line_of_business_id`, `utilization_driver_id`, `peer_utilization_index`, `company_gap_index`
- `healthplan.medical.dim_utilization_driver`: `utilization_driver_code`, `utilization_driver_name`
- `healthplan.medical.fact_utilization`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `utilization_driver_id`, `utilization_index`, `versus_assumption_index`

### Q2 2026 (12)

Is outpatient-surgery cost pressure coming from volume or from higher-acuity procedures, and is a second-half catch-up a risk?

- `healthplan.medical.fact_procedure_mix`: `fiscal_quarter_id`, `clinical_category_id`, `line_of_business_id`, `acuity_share`, `volume_driven_flag`
- `healthplan.medical.fact_outpatient_surgery`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `facility_id`, `catch_up_risk_flag`, `high_acuity_procedure_count`
- `healthplan.medical.dim_clinical_category`: `clinical_category_code`, `clinical_category_name`
- `healthplan.membership.fact_membership_mix`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `customer_segment_id`, `acuity_index`, `indiana_excluded_decline_rate`

### Q2 2026 (13)

Did reserve posture become more conservative in the second quarter in any business?

- `healthplan.medical.fact_reserve_posture`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `stance_code`, `more_conservative_flag`
- `healthplan.membership.fact_seasonality`: `fiscal_quarter_id`, `line_of_business_id`, `benefit_design_id`, `favorability_index`, `reverses_later_flag`

### Q2 2026 (14)

Are Medicare Advantage utilization trends more favorable, and is that expected to continue?

- `healthplan.medical.fact_utilization`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `utilization_driver_id`, `favorable_flag`, `utilization_index`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `assumption_rate`
- `healthplan.price.fact_book_margin`: `fiscal_quarter_id`, `line_of_business_id`, `business_unit_id`, `margin_target_id`, `full_year_margin_rate`, `margin_rate`

### Q1 2026 (7)

How far have Carelon risk-based programs expanded, and what operating actions limit upside risk in medical cost?

- `healthplan.medical.fact_program_scope`: `fiscal_quarter_id`, `care_service_id`, `business_unit_id`, `clinical_program_id`, `trend_cap_flag`, `program_count`
- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `trend_rate`
- `healthplan.medical.dim_care_service`: `business_unit_id`, `care_service_code`, `care_service_name`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`

### Q1 2026 (8)

How much of the quarter's outperformance is claims management versus flu and weather?

- `healthplan.medical.fact_flu_weather`: `fiscal_quarter_id`, `utilization_driver_id`, `line_of_business_id`, `disruption_index`, `bounce_back_flag`, `peer_gap_index`
- `healthplan.medical.fact_claim_action`: `fiscal_quarter_id`, `clinical_program_id`, `line_of_business_id`, `temporary_driver_flag`, `action_count`
- `healthplan.medical.dim_utilization_driver`: `utilization_driver_code`, `utilization_driver_name`
- `healthplan.medical.fact_utilization`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `utilization_driver_id`, `utilization_index`, `versus_assumption_index`

### Q1 2026 (12)

Where is site-of-care optimization showing up, in Carelon risk programs or in the broader benefits book?

- `healthplan.medical.fact_site_shift`: `fiscal_quarter_id`, `site_of_care_id`, `care_service_id`, `line_of_business_id`, `program_scope_code`, `admission_count`
- `healthplan.medical.dim_site_of_care`: `site_of_care_code`, `site_of_care_name`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.medical.dim_clinical_category`: `clinical_category_code`, `clinical_category_name`

### Q1 2026 (15)

What drove the step-up in days claims payable, including membership mix?

- `healthplan.medical.fact_claims_payable`: `fiscal_quarter_id`, `line_of_business_id`, `claim_inventory_id`, `membership_cohort_id`, `days_payable_count`, `inventory_claim_count`
- `healthplan.medical.dim_claim_inventory`: `claim_inventory_code`, `claim_inventory_name`

### Q4 2025 (11)

Which Carelon services are taking risk, and can that offset the margin shift in CarelonRx?

- `healthplan.medical.dim_care_service`: `business_unit_id`, `care_service_code`, `care_service_name`
- `healthplan.price.fact_services_margin`: `fiscal_quarter_id`, `business_unit_id`, `care_service_id`, `margin_target_id`, `margin_rate`, `pharmacy_pressure_flag`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.membership.fact_service_attach`: `fiscal_quarter_id`, `care_service_id`, `blue_bid_id`, `business_unit_id`, `attached_service_count`, `risk_bearing_flag`

### Q2 2025 (4)

What cost-structure actions are different through this year and next, and what is their timing and size?

- `healthplan.medical.fact_claim_action`: `fiscal_quarter_id`, `clinical_program_id`, `line_of_business_id`, `action_count`, `temporary_driver_flag`
- `healthplan.price.fact_sga_investment`: `fiscal_quarter_id`, `investment_program_id`, `business_unit_id`, `ai_program_id`, `one_time_amount`, `recurring_amount`
- `healthplan.medical.dim_clinical_program`: `clinical_category_id`, `clinical_program_code`, `clinical_program_name`
- `healthplan.price.fact_controllable_earnings`: `fiscal_quarter_id`, `line_of_business_id`, `ai_program_id`, `controllable_share`, `medicaid_pressure_flag`

### Q2 2025 (7)

Is higher provider coding showing up in every segment or only in a subset of providers?

- `healthplan.medical.fact_coding_intensity`: `fiscal_quarter_id`, `risk_model_id`, `provider_group_id`, `line_of_business_id`, `clinical_category_id`, `subset_only_flag`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`
- `healthplan.provider.dim_provider`: `provider_group_id`, `provider_code`, `provider_name`
- `healthplan.price.dim_margin_target`: `line_of_business_id`, `business_unit_id`, `margin_target_code`, `margin_target_name`

### Q2 2025 (9)

If Medicaid cost trend slowed slightly while underlying utilization rose, what drove the utilization, and are states carving benefits in without matching rates?

- `healthplan.medical.fact_benefit_carve`: `fiscal_quarter_id`, `state_id`, `state_program_id`, `benefit_design_id`, `rate_matched_flag`, `carved_benefit_count`
- `healthplan.price.fact_cost_trend`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `cost_driver_id`, `business_unit_id`, `assumption_rate`
- `healthplan.medical.fact_utilization`: `fiscal_quarter_id`, `line_of_business_id`, `clinical_category_id`, `utilization_driver_id`, `favorable_flag`, `utilization_index`
- `healthplan.product.dim_line_of_business`: `line_of_business_code`, `line_of_business_name`

### Q2 2025 (10)

How are Carelon margins tracking versus the initial plan, and when does pressure from large-employer pharmacy growth, specialty drugs, and CareBridge normalize?

- `healthplan.medical.fact_specialty_volume`: `fiscal_quarter_id`, `drug_id`, `care_service_id`, `business_unit_id`, `growth_rate`, `script_count`
- `healthplan.price.fact_services_margin`: `fiscal_quarter_id`, `business_unit_id`, `care_service_id`, `margin_target_id`, `pharmacy_pressure_flag`, `margin_rate`
- `healthplan.product.dim_business_unit`: `business_unit_code`, `business_unit_name`
- `healthplan.price.fact_specialty_cost`: `fiscal_quarter_id`, `drug_id`, `care_service_id`, `pressure_flag`, `unit_cost_rate`

### Q2 2025 (11)

How large is the expected fourth-quarter ACA acuity surge, and what other one-time items sit in the back-half outlook?

- `healthplan.medical.fact_exchange_morbidity`: `fiscal_quarter_id`, `line_of_business_id`, `risk_pool_id`, `back_half_surge_flag`, `morbidity_index`
- `healthplan.price.fact_earnings_cadence`: `fiscal_quarter_id`, `business_unit_id`, `line_of_business_id`, `one_time_back_half_flag`, `exit_margin_rate`, `back_half_favorable_flag`
- `healthplan.price.fact_earnings_bridge`: `fiscal_quarter_id`, `business_unit_id`, `earnings_scenario_id`, `line_of_business_id`, `contract_design_amount`, `development_amount`
- `healthplan.membership.fact_membership_mix`: `fiscal_quarter_id`, `line_of_business_id`, `state_id`, `customer_segment_id`, `acuity_index`, `indiana_excluded_decline_rate`
