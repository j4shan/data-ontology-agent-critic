# Health Plan Inc medical cost and provider slice

This slice is part of the Health Plan Inc warehouse. Quantity, capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

## UnitedHealth Group

### Q2 2026 (1)

Where is the full-year Medicaid margin expected to finish versus the earlier negative range?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.medical.fact_value_based_attributed_lives`: `fiscal_quarter_id`, `scenario_id`, `provider_group_id`, `payment_arrangement_id`, `plan_type_id`, `attributed_life_quantity`, `negotiation_life_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_work_requirement_attrition`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `legislation_id`, `assumed_attrition_quantity`, `affected_member_quantity`
- `healthplan.price.dim_legislation`: `legislation_id`, `legislation_code`, `legislation_name`

### Q2 2026 (4)

Where does Medicare Advantage cost trend sit versus 2025 and versus the trend used in the 2026 bids?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.fact_bid_assumptions`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `bid_process_id`, `assumed_medical_cost_trend_percent`, `filed_premium_change_percent`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_cost_by_line`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`

### Q2 2026 (6)

Should this year's earnings outperformance be removed from the baseline used for 2027, or is it a recurring run rate?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.dim_earnings_bridge_component`: `earnings_bridge_component_id`, `earnings_bridge_component_code`, `earnings_bridge_component_name`
- `healthplan.price.fact_earnings_bridge`: `fiscal_quarter_id`, `scenario_id`, `earnings_bridge_component_id`, `bridge_amount`
- `healthplan.price.fact_medical_cost_by_line`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`

### Q2 2026 (7)

How much of the SG&A investment is one-time, and what benefit should carry into 2027?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.dim_investment_program_type`: `investment_program_type_id`, `investment_program_type_code`, `investment_program_type_name`
- `healthplan.price.fact_bid_assumptions`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `bid_process_id`, `assumed_medical_cost_trend_percent`, `filed_premium_change_percent`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`

### Q2 2026 (8)

Why are independent dispute-resolution costs accelerating now, across win rates, dispute volume, and resolution timing?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_dispute_cases`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_case_quantity`, `resolved_case_quantity`, `resolution_duration_days`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`

### Q2 2026 (9)

How is Medicare Advantage utilization tracking versus the elevated-utilization piece of the original trend outlook?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `enrollment_channel_id`, `member_months_quantity`, `end_of_period_member_quantity`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.fact_bid_assumptions`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `bid_process_id`, `assumed_medical_cost_trend_percent`, `filed_premium_change_percent`

### Q2 2026 (10)

What run-rate margin is the capitated, value-based portion of Optum Health earning, and is that a trough?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_optum_employed_clinician_capacity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `site_of_care_id`, `employed_clinician_quantity`, `patient_panel_quantity`
- `healthplan.medical.fact_provider_panel_capacity`: `fiscal_quarter_id`, `scenario_id`, `provider_group_id`, `clinical_service_id`, `panel_slot_quantity`, `attributed_member_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.medical.fact_value_based_attributed_lives`: `fiscal_quarter_id`, `scenario_id`, `provider_group_id`, `payment_arrangement_id`, `plan_type_id`, `attributed_life_quantity`, `negotiation_life_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (11)

What is happening to outpatient surgical volumes?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.medical.fact_value_based_attributed_lives`: `fiscal_quarter_id`, `scenario_id`, `provider_group_id`, `payment_arrangement_id`, `plan_type_id`, `attributed_life_quantity`, `negotiation_life_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_work_requirement_attrition`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `legislation_id`, `assumed_attrition_quantity`, `affected_member_quantity`
- `healthplan.price.dim_legislation`: `legislation_id`, `legislation_code`, `legislation_name`

### Q1 2026 (2)

How much of Medicare Advantage trend is the acuity and provider-billing dynamic, and is that limited to Medicare Advantage?

- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_coding_submissions`: `fiscal_quarter_id`, `scenario_id`, `risk_model_version_id`, `provider_group_id`, `plan_type_id`, `submitted_code_quantity`, `chronic_condition_code_quantity`, `encounter_quantity`
- `healthplan.medical.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_id`, `bed_quantity`, `operating_room_quantity`, `available_slot_quantity`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (8)

What incremental investment does the new PBM legislation require?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.membership.fact_work_requirement_attrition`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `legislation_id`, `assumed_attrition_quantity`, `affected_member_quantity`
- `healthplan.price.dim_investment_program_type`: `investment_program_type_id`, `investment_program_type_code`, `investment_program_type_name`
- `healthplan.price.dim_legislation`: `legislation_id`, `legislation_code`, `legislation_name`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`

### Q1 2026 (9)

Where do the value-based life tranches under negotiation stand, and are new provider groups being added?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_provider_organization_type`: `provider_organization_type_id`, `provider_organization_type_code`, `provider_organization_type_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_optum_employed_clinician_capacity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `site_of_care_id`, `employed_clinician_quantity`, `patient_panel_quantity`
- `healthplan.medical.fact_provider_panel_capacity`: `fiscal_quarter_id`, `scenario_id`, `provider_group_id`, `clinical_service_id`, `panel_slot_quantity`, `attributed_member_quantity`
- `healthplan.medical.fact_value_based_attributed_lives`: `fiscal_quarter_id`, `scenario_id`, `provider_group_id`, `payment_arrangement_id`, `plan_type_id`, `attributed_life_quantity`, `negotiation_life_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.fact_provider_reimbursement`: `fiscal_quarter_id`, `scenario_id`, `payment_arrangement_id`, `provider_organization_type_id`, `reimbursement_amount`, `capitation_amount`

### Q1 2026 (11)

Can AI efficiency gains accelerate in 2027 and 2028 enough to lift segment margins above long-term targets?

- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_employer_account_size`: `employer_account_size_id`, `employer_account_size_code`, `employer_account_size_name`
- `healthplan.membership.dim_employer_sector`: `employer_sector_id`, `employer_sector_code`, `employer_sector_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_employer_covered_lives`: `fiscal_quarter_id`, `scenario_id`, `employer_account_size_id`, `employer_sector_id`, `funding_arrangement_id`, `covered_life_quantity`, `member_months_quantity`
- `healthplan.membership.fact_medicaid_redetermination`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `plan_type_id`, `redetermined_member_quantity`, `disenrolled_member_quantity`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.fact_bid_assumptions`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `bid_process_id`, `assumed_medical_cost_trend_percent`, `filed_premium_change_percent`

### Q1 2026 (13)

When the delayed Medicare Advantage risk-model recalibration arrives, how large is the cut to chronic-condition codes for value-based providers?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_coding_submissions`: `fiscal_quarter_id`, `scenario_id`, `risk_model_version_id`, `provider_group_id`, `plan_type_id`, `submitted_code_quantity`, `chronic_condition_code_quantity`, `encounter_quantity`
- `healthplan.medical.fact_optum_employed_clinician_capacity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `site_of_care_id`, `employed_clinician_quantity`, `patient_panel_quantity`
- `healthplan.medical.fact_provider_panel_capacity`: `fiscal_quarter_id`, `scenario_id`, `provider_group_id`, `clinical_service_id`, `panel_slot_quantity`, `attributed_member_quantity`
- `healthplan.medical.fact_value_based_attributed_lives`: `fiscal_quarter_id`, `scenario_id`, `provider_group_id`, `payment_arrangement_id`, `plan_type_id`, `attributed_life_quantity`, `negotiation_life_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`

### Q1 2026 (14)

How are physician, hospital, and drug trends running versus expectations in each book, and which clinical and network actions are moving them?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_id`, `bed_quantity`, `operating_room_quantity`, `available_slot_quantity`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_cost_trend`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `medical_cost_trend_percent`, `assumed_trend_percent`

### Q4 2025 (1)

With 2026 Medicare Advantage membership guided down sharply, are margins at a bottom, and should 2027 margins improve as benefits are refined?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `enrollment_channel_id`, `member_months_quantity`, `end_of_period_member_quantity`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.fact_bid_assumptions`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `bid_process_id`, `assumed_medical_cost_trend_percent`, `filed_premium_change_percent`
- `healthplan.price.fact_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `premium_per_member_per_month_amount`

### Q4 2025 (3)

How does the coding headwind from the risk model and chart review compare with UnitedHealth's experience under the prior model and with the industry?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_coding_submissions`: `fiscal_quarter_id`, `scenario_id`, `risk_model_version_id`, `provider_group_id`, `plan_type_id`, `submitted_code_quantity`, `chronic_condition_code_quantity`, `encounter_quantity`
- `healthplan.medical.fact_optum_employed_clinician_capacity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `site_of_care_id`, `employed_clinician_quantity`, `patient_panel_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`

### Q4 2025 (6)

How should member losses tied to UnitedHealthcare be weighed against the new Optum Rx clients?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.dim_optum_business`: `optum_business_id`, `optum_business_code`, `optum_business_name`
- `healthplan.price.dim_unitedhealth_segment`: `unitedhealth_segment_id`, `unitedhealth_segment_code`, `unitedhealth_segment_name`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_cost_by_line`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`

### Q3 2025 (8)

Is the Medicaid margin still in a roughly negative 1% to 1.5% range, and what blocks a recovery in 2027 and 2028?

- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_medicaid_redetermination`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `plan_type_id`, `redetermined_member_quantity`, `disenrolled_member_quantity`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.fact_bid_assumptions`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `bid_process_id`, `assumed_medical_cost_trend_percent`, `filed_premium_change_percent`
- `healthplan.price.fact_medical_loss_ratio`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `medical_loss_ratio_percent`

### Q3 2025 (12)

Is mitigation of the risk-adjustment headwind coming from recontracting UnitedHealthcare or from other payers?

- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_coding_submissions`: `fiscal_quarter_id`, `scenario_id`, `risk_model_version_id`, `provider_group_id`, `plan_type_id`, `submitted_code_quantity`, `chronic_condition_code_quantity`, `encounter_quantity`
- `healthplan.medical.fact_dispute_cases`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_case_quantity`, `resolved_case_quantity`, `resolution_duration_days`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.dim_revenue_type`: `revenue_type_id`, `revenue_type_code`, `revenue_type_name`
- `healthplan.price.fact_risk_adjustment_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `state_id`, `risk_adjustment_receivable_amount`, `risk_adjustment_payable_amount`, `risk_adjustment_accrual_amount`

## Elevance Health

### Q2 2026 (4)

What cost trend was assumed for Medicaid, the exchanges, and Medicare Advantage, and what did the second quarter actually show?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `enrollment_channel_id`, `member_months_quantity`, `end_of_period_member_quantity`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`

### Q2 2026 (5)

Why did seasonal favorability increase from the first quarter to the second, and does any of that reverse later in the year?

- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_id`, `bed_quantity`, `operating_room_quantity`, `available_slot_quantity`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`

### Q2 2026 (11)

Is the first-half utilization pattern a bounce-back from a lighter flu and weather effect than peers reported?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`

### Q2 2026 (12)

Is outpatient-surgery cost pressure coming from volume or from higher-acuity procedures, and is a second-half catch-up a risk?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_carelon_home_care_quantity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `state_id`, `home_visit_quantity`, `served_member_quantity`
- `healthplan.medical.fact_coding_submissions`: `fiscal_quarter_id`, `scenario_id`, `risk_model_version_id`, `provider_group_id`, `plan_type_id`, `submitted_code_quantity`, `chronic_condition_code_quantity`, `encounter_quantity`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`

### Q2 2026 (13)

Did reserve posture become more conservative in the second quarter in any business?

- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.fact_claim_inventory`: `fiscal_quarter_id`, `scenario_id`, `claim_status_id`, `plan_type_id`, `claim_quantity`, `claim_age_days`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_employer_account_size`: `employer_account_size_id`, `employer_account_size_code`, `employer_account_size_name`
- `healthplan.membership.dim_employer_sector`: `employer_sector_id`, `employer_sector_code`, `employer_sector_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_employer_covered_lives`: `fiscal_quarter_id`, `scenario_id`, `employer_account_size_id`, `employer_sector_id`, `funding_arrangement_id`, `covered_life_quantity`, `member_months_quantity`
- `healthplan.membership.fact_medicaid_redetermination`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `plan_type_id`, `redetermined_member_quantity`, `disenrolled_member_quantity`

### Q1 2026 (3)

How are members behaving after deductibles reset, and are higher fuel prices or the broader economy changing utilization?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_cost_trend`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `medical_cost_trend_percent`, `assumed_trend_percent`

### Q1 2026 (4)

How does the Carelon and CarelonRx margin get back to the reiterated full-year outlook after a weaker quarter?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_carelon_home_care_quantity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `state_id`, `home_visit_quantity`, `served_member_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_blue_plan_bid_quantity`: `fiscal_quarter_id`, `scenario_id`, `blue_plan_client_type_id`, `carelon_business_id`, `bid_quantity`, `won_bid_quantity`, `pipeline_bid_quantity`
- `healthplan.price.dim_blue_plan_client_type`: `blue_plan_client_type_id`, `blue_plan_client_type_code`, `blue_plan_client_type_name`
- `healthplan.price.dim_carelon_business`: `carelon_business_id`, `carelon_business_code`, `carelon_business_name`

### Q1 2026 (7)

How far have Carelon risk-based programs expanded, and what operating actions limit upside risk in medical cost?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.fact_carelon_home_care_quantity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `state_id`, `home_visit_quantity`, `served_member_quantity`
- `healthplan.medical.fact_coding_submissions`: `fiscal_quarter_id`, `scenario_id`, `risk_model_version_id`, `provider_group_id`, `plan_type_id`, `submitted_code_quantity`, `chronic_condition_code_quantity`, `encounter_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.price.fact_medical_cost_trend`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `medical_cost_trend_percent`, `assumed_trend_percent`
- `healthplan.price.fact_medical_loss_ratio`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `medical_loss_ratio_percent`

### Q1 2026 (9)

Did higher-than-expected exchange enrollment come with a worse risk pool, including people moving from Medicaid?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_coding_submissions`: `fiscal_quarter_id`, `scenario_id`, `risk_model_version_id`, `provider_group_id`, `plan_type_id`, `submitted_code_quantity`, `chronic_condition_code_quantity`, `encounter_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_metal_tier`: `metal_tier_id`, `metal_tier_code`, `metal_tier_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_exchange_enrollment`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `metal_tier_id`, `plan_type_id`, `enrolled_member_quantity`, `member_months_quantity`
- `healthplan.price.fact_risk_adjustment_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `state_id`, `risk_adjustment_receivable_amount`, `risk_adjustment_payable_amount`, `risk_adjustment_accrual_amount`

### Q1 2026 (11)

What efficiency gains is AI already showing, and how do the related investments track against those gains?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.dim_investment_program_type`: `investment_program_type_id`, `investment_program_type_code`, `investment_program_type_name`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_investment_spending`: `fiscal_quarter_id`, `scenario_id`, `investment_program_type_id`, `investment_spending_amount`, `measured_savings_amount`

### Q1 2026 (12)

Where is site-of-care optimization showing up, in Carelon risk programs or in the broader benefits book?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_carelon_home_care_quantity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `state_id`, `home_visit_quantity`, `served_member_quantity`
- `healthplan.medical.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_id`, `bed_quantity`, `operating_room_quantity`, `available_slot_quantity`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.price.dim_blue_plan_client_type`: `blue_plan_client_type_id`, `blue_plan_client_type_code`, `blue_plan_client_type_name`

### Q1 2026 (15)

What drove the step-up in days claims payable, including membership mix?

- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispensing_category`: `dispensing_category_id`, `dispensing_category_code`, `dispensing_category_name`
- `healthplan.medical.dim_drug_therapy_class`: `drug_therapy_class_id`, `drug_therapy_class_code`, `drug_therapy_class_name`
- `healthplan.medical.fact_claim_inventory`: `fiscal_quarter_id`, `scenario_id`, `claim_status_id`, `plan_type_id`, `claim_quantity`, `claim_age_days`
- `healthplan.medical.fact_pharmacy_claims`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `drug_therapy_class_id`, `dispensing_category_id`, `prescription_claim_quantity`, `day_supply_quantity`, `unique_member_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_employer_account_size`: `employer_account_size_id`, `employer_account_size_code`, `employer_account_size_name`
- `healthplan.membership.dim_employer_sector`: `employer_sector_id`, `employer_sector_code`, `employer_sector_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_employer_covered_lives`: `fiscal_quarter_id`, `scenario_id`, `employer_account_size_id`, `employer_sector_id`, `funding_arrangement_id`, `covered_life_quantity`, `member_months_quantity`

### Q4 2025 (3)

What pricing and cost drivers sit behind 2026 health-benefits margins, including the negative Medicaid margin and a better fourth quarter?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`

### Q4 2025 (9)

Do larger-than-expected membership declines say anything about competitive position, even if exiting weak markets is intentional?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_carelon_home_care_quantity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `state_id`, `home_visit_quantity`, `served_member_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_member_cohort`: `member_cohort_id`, `member_cohort_code`, `member_cohort_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_blue_plan_bid_quantity`: `fiscal_quarter_id`, `scenario_id`, `blue_plan_client_type_id`, `carelon_business_id`, `bid_quantity`, `won_bid_quantity`, `pipeline_bid_quantity`
- `healthplan.membership.fact_cohort_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `member_cohort_id`, `dual_eligibility_status_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.dim_blue_plan_client_type`: `blue_plan_client_type_id`, `blue_plan_client_type_code`, `blue_plan_client_type_name`
- `healthplan.price.dim_carelon_business`: `carelon_business_id`, `carelon_business_code`, `carelon_business_name`

### Q4 2025 (13)

How much of the commercial-risk membership decline is pricing on government accounts versus employers moving to fee-based coverage, and does the long-term margin assume more attrition?

- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.fact_value_based_attributed_lives`: `fiscal_quarter_id`, `scenario_id`, `provider_group_id`, `payment_arrangement_id`, `plan_type_id`, `attributed_life_quantity`, `negotiation_life_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_employer_account_size`: `employer_account_size_id`, `employer_account_size_code`, `employer_account_size_name`
- `healthplan.membership.dim_employer_sector`: `employer_sector_id`, `employer_sector_code`, `employer_sector_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_employer_covered_lives`: `fiscal_quarter_id`, `scenario_id`, `employer_account_size_id`, `employer_sector_id`, `funding_arrangement_id`, `covered_life_quantity`, `member_months_quantity`
- `healthplan.membership.fact_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `enrollment_channel_id`, `member_months_quantity`, `end_of_period_member_quantity`
- `healthplan.price.fact_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `premium_per_member_per_month_amount`

### Q2 2025 (2)

How much of the guidance cut is the public exchanges versus Medicaid, and is the Medicaid issue a delayed rate catch-up?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `enrollment_channel_id`, `member_months_quantity`, `end_of_period_member_quantity`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.dim_rate_notice_type`: `rate_notice_type_id`, `rate_notice_type_code`, `rate_notice_type_name`
- `healthplan.price.fact_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `premium_per_member_per_month_amount`
- `healthplan.price.fact_rate_update`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `state_id`, `rate_notice_type_id`, `announced_rate_change_percent`, `final_rate_change_percent`

### Q2 2025 (4)

What cost-structure actions are different through this year and next, and what is their timing and size?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.medical.fact_dispute_cases`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_case_quantity`, `resolved_case_quantity`, `resolution_duration_days`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_cost_trend`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `medical_cost_trend_percent`, `assumed_trend_percent`

### Q2 2025 (7)

Is higher provider coding showing up in every segment or only in a subset of providers?

- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispensing_category`: `dispensing_category_id`, `dispensing_category_code`, `dispensing_category_name`
- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_claim_inventory`: `fiscal_quarter_id`, `scenario_id`, `claim_status_id`, `plan_type_id`, `claim_quantity`, `claim_age_days`
- `healthplan.medical.fact_coding_submissions`: `fiscal_quarter_id`, `scenario_id`, `risk_model_version_id`, `provider_group_id`, `plan_type_id`, `submitted_code_quantity`, `chronic_condition_code_quantity`, `encounter_quantity`
- `healthplan.medical.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_id`, `bed_quantity`, `operating_room_quantity`, `available_slot_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`

### Q2 2025 (13)

Where do commercial margins stand now, and how fast can they return to target?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_employer_account_size`: `employer_account_size_id`, `employer_account_size_code`, `employer_account_size_name`
- `healthplan.membership.dim_employer_sector`: `employer_sector_id`, `employer_sector_code`, `employer_sector_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_blue_plan_bid_quantity`: `fiscal_quarter_id`, `scenario_id`, `blue_plan_client_type_id`, `carelon_business_id`, `bid_quantity`, `won_bid_quantity`, `pipeline_bid_quantity`
- `healthplan.membership.fact_employer_covered_lives`: `fiscal_quarter_id`, `scenario_id`, `employer_account_size_id`, `employer_sector_id`, `funding_arrangement_id`, `covered_life_quantity`, `member_months_quantity`
- `healthplan.membership.fact_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `enrollment_channel_id`, `member_months_quantity`, `end_of_period_member_quantity`
- `healthplan.price.dim_blue_plan_client_type`: `blue_plan_client_type_id`, `blue_plan_client_type_code`, `blue_plan_client_type_name`
- `healthplan.price.dim_carelon_business`: `carelon_business_id`, `carelon_business_code`, `carelon_business_name`
