# Health Plan Inc membership and channel slice

This slice is part of the Health Plan Inc warehouse. Quantity, capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

## UnitedHealth Group

### Q1 2026 (6)

Will the company join the GLP-1 Balance Program, and is industry participation expected to meet the required thresholds?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`

### Q4 2025 (4)

How do 2026 Medicaid rates compare with 2025, and would an earlier start to work requirements change the margin view?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `enrollment_channel_id`, `member_months_quantity`, `end_of_period_member_quantity`
- `healthplan.membership.fact_work_requirement_attrition`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `legislation_id`, `assumed_attrition_quantity`, `affected_member_quantity`
- `healthplan.price.dim_legislation`: `legislation_id`, `legislation_code`, `legislation_name`

### Q4 2025 (5)

How do Part D subsidy changes shift Optum Rx earnings toward the first half?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_dispensing_category`: `dispensing_category_id`, `dispensing_category_code`, `dispensing_category_name`
- `healthplan.medical.dim_drug_therapy_class`: `drug_therapy_class_id`, `drug_therapy_class_code`, `drug_therapy_class_name`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_optum_employed_clinician_capacity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `site_of_care_id`, `employed_clinician_quantity`, `patient_panel_quantity`
- `healthplan.medical.fact_pharmacy_claims`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `drug_therapy_class_id`, `dispensing_category_id`, `prescription_claim_quantity`, `day_supply_quantity`, `unique_member_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.dim_optum_business`: `optum_business_id`, `optum_business_code`, `optum_business_name`
- `healthplan.price.fact_optum_business_result`: `fiscal_quarter_id`, `scenario_id`, `optum_business_id`, `business_revenue_amount`, `business_operating_income_amount`

### Q3 2025 (3)

How does the expected 2026 Medicare Advantage membership decline split among individual, dual-eligible, and group lives?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_employer_account_size`: `employer_account_size_id`, `employer_account_size_code`, `employer_account_size_name`
- `healthplan.membership.dim_employer_sector`: `employer_sector_id`, `employer_sector_code`, `employer_sector_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_employer_covered_lives`: `fiscal_quarter_id`, `scenario_id`, `employer_account_size_id`, `employer_sector_id`, `funding_arrangement_id`, `covered_life_quantity`, `member_months_quantity`
- `healthplan.membership.fact_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `enrollment_channel_id`, `member_months_quantity`, `end_of_period_member_quantity`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`

### Q3 2025 (4)

Does the company agree that industry Medicare Advantage enrollment is roughly flat, and what share of lives is a realistic value-based-care market?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_optum_employed_clinician_capacity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `site_of_care_id`, `employed_clinician_quantity`, `patient_panel_quantity`
- `healthplan.medical.fact_provider_panel_capacity`: `fiscal_quarter_id`, `scenario_id`, `provider_group_id`, `clinical_service_id`, `panel_slot_quantity`, `attributed_member_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `enrollment_channel_id`, `member_months_quantity`, `end_of_period_member_quantity`

### Q3 2025 (6)

What utilization is expected in the fourth quarter, including any step-up in Part D?

- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispensing_category`: `dispensing_category_id`, `dispensing_category_code`, `dispensing_category_name`
- `healthplan.medical.dim_drug_therapy_class`: `drug_therapy_class_id`, `drug_therapy_class_code`, `drug_therapy_class_name`
- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.medical.fact_pharmacy_claims`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `drug_therapy_class_id`, `dispensing_category_id`, `prescription_claim_quantity`, `day_supply_quantity`, `unique_member_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.fact_medical_cost_trend`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `medical_cost_trend_percent`, `assumed_trend_percent`

### Q3 2025 (7)

Why did Tier 3 branded drugs on Medicare Advantage and stand-alone Part D plans move from copay to coinsurance?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispensing_category`: `dispensing_category_id`, `dispensing_category_code`, `dispensing_category_name`
- `healthplan.medical.dim_drug_therapy_class`: `drug_therapy_class_id`, `drug_therapy_class_code`, `drug_therapy_class_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_pharmacy_claims`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `drug_therapy_class_id`, `dispensing_category_id`, `prescription_claim_quantity`, `day_supply_quantity`, `unique_member_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.dim_member_cost_sharing`: `member_cost_sharing_id`, `member_cost_sharing_code`, `member_cost_sharing_name`
- `healthplan.price.fact_member_cost_sharing`: `fiscal_quarter_id`, `scenario_id`, `member_cost_sharing_id`, `drug_therapy_class_id`, `average_copayment_amount`, `coinsurance_percent`

### Q3 2025 (11)

How much of the Optum Health turnaround is walking away from risk versus repairing the remaining book?

- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_coding_submissions`: `fiscal_quarter_id`, `scenario_id`, `risk_model_version_id`, `provider_group_id`, `plan_type_id`, `submitted_code_quantity`, `chronic_condition_code_quantity`, `encounter_quantity`
- `healthplan.medical.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_id`, `bed_quantity`, `operating_room_quantity`, `available_slot_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.dim_optum_business`: `optum_business_id`, `optum_business_code`, `optum_business_name`
- `healthplan.price.fact_optum_business_result`: `fiscal_quarter_id`, `scenario_id`, `optum_business_id`, `business_revenue_amount`, `business_operating_income_amount`

## Elevance Health

### Q2 2026 (1)

Is the back half of the year more favorable than the front half for the negative Medicaid margin, and where does the year exit?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_id`, `bed_quantity`, `operating_room_quantity`, `available_slot_quantity`
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

### Q2 2026 (2)

How large are the planned Medicaid exits relative to the Medicaid revenue base?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_drug_therapy_class`: `drug_therapy_class_id`, `drug_therapy_class_code`, `drug_therapy_class_name`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_work_requirement_attrition`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `legislation_id`, `assumed_attrition_quantity`, `affected_member_quantity`
- `healthplan.price.dim_legislation`: `legislation_id`, `legislation_code`, `legislation_name`
- `healthplan.price.dim_member_cost_sharing`: `member_cost_sharing_id`, `member_cost_sharing_code`, `member_cost_sharing_name`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_member_cost_sharing`: `fiscal_quarter_id`, `scenario_id`, `member_cost_sharing_id`, `drug_therapy_class_id`, `average_copayment_amount`, `coinsurance_percent`

### Q2 2026 (7)

What criteria decide which Medicaid programs are exited, such as program type, state, or share position?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.dim_investment_program_type`: `investment_program_type_id`, `investment_program_type_code`, `investment_program_type_name`
- `healthplan.price.dim_rate_notice_type`: `rate_notice_type_id`, `rate_notice_type_code`, `rate_notice_type_name`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_investment_spending`: `fiscal_quarter_id`, `scenario_id`, `investment_program_type_id`, `investment_spending_amount`, `measured_savings_amount`
- `healthplan.price.fact_rate_update`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `state_id`, `rate_notice_type_id`, `announced_rate_change_percent`, `final_rate_change_percent`

### Q2 2026 (10)

Over two to three years, what Medicaid pressures remain if this year is the trough?

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

### Q2 2026 (15)

Is there anything unusual in commercial enrollment between fee-based and employer-group risk, and how is pricing being balanced against elevated trend?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.fact_coding_submissions`: `fiscal_quarter_id`, `scenario_id`, `risk_model_version_id`, `provider_group_id`, `plan_type_id`, `submitted_code_quantity`, `chronic_condition_code_quantity`, `encounter_quantity`
- `healthplan.membership.dim_employer_account_size`: `employer_account_size_id`, `employer_account_size_code`, `employer_account_size_name`
- `healthplan.membership.dim_employer_sector`: `employer_sector_id`, `employer_sector_code`, `employer_sector_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_employer_covered_lives`: `fiscal_quarter_id`, `scenario_id`, `employer_account_size_id`, `employer_sector_id`, `funding_arrangement_id`, `covered_life_quantity`, `member_months_quantity`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.fact_bid_assumptions`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `bid_process_id`, `assumed_medical_cost_trend_percent`, `filed_premium_change_percent`
- `healthplan.price.fact_medical_cost_trend`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `medical_cost_trend_percent`, `assumed_trend_percent`

### Q2 2026 (16)

What are the early puts and takes for 2027 by business versus the long-term growth path?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_drug_therapy_class`: `drug_therapy_class_id`, `drug_therapy_class_code`, `drug_therapy_class_name`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.dim_member_cost_sharing`: `member_cost_sharing_id`, `member_cost_sharing_code`, `member_cost_sharing_name`
- `healthplan.price.dim_revenue_type`: `revenue_type_id`, `revenue_type_code`, `revenue_type_name`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_member_cost_sharing`: `fiscal_quarter_id`, `scenario_id`, `member_cost_sharing_id`, `drug_therapy_class_id`, `average_copayment_amount`, `coinsurance_percent`

### Q1 2026 (1)

Are employers emphasizing different priorities in the pharmacy and commercial selling seasons, including AI or a softer economy?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispensing_category`: `dispensing_category_id`, `dispensing_category_code`, `dispensing_category_name`
- `healthplan.medical.dim_drug_therapy_class`: `drug_therapy_class_id`, `drug_therapy_class_code`, `drug_therapy_class_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_employer_account_size`: `employer_account_size_id`, `employer_account_size_code`, `employer_account_size_name`
- `healthplan.membership.dim_employer_sector`: `employer_sector_id`, `employer_sector_code`, `employer_sector_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.fact_employer_covered_lives`: `fiscal_quarter_id`, `scenario_id`, `employer_account_size_id`, `employer_sector_id`, `funding_arrangement_id`, `covered_life_quantity`, `member_months_quantity`
- `healthplan.price.dim_member_cost_sharing`: `member_cost_sharing_id`, `member_cost_sharing_code`, `member_cost_sharing_name`
- `healthplan.price.fact_member_cost_sharing`: `fiscal_quarter_id`, `scenario_id`, `member_cost_sharing_id`, `drug_therapy_class_id`, `average_copayment_amount`, `coinsurance_percent`
- `healthplan.price.fact_pharmacy_cost`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `drug_therapy_class_id`, `dispensing_category_id`, `pharmacy_claim_cost_amount`, `manufacturer_rebate_amount`

### Q1 2026 (2)

Are Medicaid membership declines concentrated in lower-utilizing members, and how does that sit against the high-single-digit decline outlook excluding Indiana growth?

- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_membership_change_reason`: `membership_change_reason_id`, `membership_change_reason_code`, `membership_change_reason_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_medicaid_redetermination`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `plan_type_id`, `redetermined_member_quantity`, `disenrolled_member_quantity`
- `healthplan.membership.fact_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `enrollment_channel_id`, `member_months_quantity`, `end_of_period_member_quantity`
- `healthplan.membership.fact_membership_change`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `state_id`, `membership_change_reason_id`, `member_change_quantity`, `changed_member_quantity`
- `healthplan.price.fact_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `premium_per_member_per_month_amount`

### Q1 2026 (5)

What did the second Blue Bid sell in 2026, what does the 2027 pipeline look like, and which Carelon services attach?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.fact_carelon_home_care_quantity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `state_id`, `home_visit_quantity`, `served_member_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_blue_plan_bid_quantity`: `fiscal_quarter_id`, `scenario_id`, `blue_plan_client_type_id`, `carelon_business_id`, `bid_quantity`, `won_bid_quantity`, `pipeline_bid_quantity`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.dim_blue_plan_client_type`: `blue_plan_client_type_id`, `blue_plan_client_type_code`, `blue_plan_client_type_name`
- `healthplan.price.dim_carelon_business`: `carelon_business_id`, `carelon_business_code`, `carelon_business_name`
- `healthplan.price.fact_bid_assumptions`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `bid_process_id`, `assumed_medical_cost_trend_percent`, `filed_premium_change_percent`
- `healthplan.price.fact_blue_plan_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `blue_plan_client_type_id`, `carelon_business_id`, `service_contract_revenue_amount`

### Q1 2026 (10)

What member attrition from work requirements is assumed for 2027, and which states are stay-or-leave decisions?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_membership_change_reason`: `membership_change_reason_id`, `membership_change_reason_code`, `membership_change_reason_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `enrollment_channel_id`, `member_months_quantity`, `end_of_period_member_quantity`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.membership.fact_work_requirement_attrition`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `legislation_id`, `assumed_attrition_quantity`, `affected_member_quantity`
- `healthplan.price.dim_legislation`: `legislation_id`, `legislation_code`, `legislation_name`

### Q1 2026 (13)

How far did the bronze-plan mix shift, and how does that compare with industry metal-tier data?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_metal_tier`: `metal_tier_id`, `metal_tier_code`, `metal_tier_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`

### Q4 2025 (1)

How does the 2026 cost-trend assumption compare with 2025 across commercial, Medicaid, Medicare, and the exchanges?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
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
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_cost_trend`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `medical_cost_trend_percent`, `assumed_trend_percent`

### Q4 2025 (2)

What happened in Medicare annual enrollment to drive the membership revision, and how does the commercial-risk decline split between the exchanges and employer group?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.fact_coding_submissions`: `fiscal_quarter_id`, `scenario_id`, `risk_model_version_id`, `provider_group_id`, `plan_type_id`, `submitted_code_quantity`, `chronic_condition_code_quantity`, `encounter_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
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

### Q4 2025 (7)

What changed in the long-term margin targets for Medicaid, Medicare, and commercial, and is the lower CarelonRx target only membership loss?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
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
- `healthplan.membership.fact_medicaid_redetermination`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `plan_type_id`, `redetermined_member_quantity`, `disenrolled_member_quantity`
- `healthplan.membership.fact_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `enrollment_channel_id`, `member_months_quantity`, `end_of_period_member_quantity`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`

### Q4 2025 (8)

Where did ACA membership start after open enrollment, and has January utilization changed?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_carelon_home_care_quantity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `state_id`, `home_visit_quantity`, `served_member_quantity`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_metal_tier`: `metal_tier_id`, `metal_tier_code`, `metal_tier_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_exchange_enrollment`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `metal_tier_id`, `plan_type_id`, `enrolled_member_quantity`, `member_months_quantity`

### Q4 2025 (12)

Is the expected Medicaid membership decline same-store or a state or contract exit, and why does a larger decline not add more margin pressure?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_member_cohort`: `member_cohort_id`, `member_cohort_code`, `member_cohort_name`
- `healthplan.membership.dim_membership_change_reason`: `membership_change_reason_id`, `membership_change_reason_code`, `membership_change_reason_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_cohort_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `member_cohort_id`, `dual_eligibility_status_id`, `member_months_quantity`, `member_quantity`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.fact_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `premium_per_member_per_month_amount`

### Q2 2025 (6)

What further ACA membership attrition and risk-pool shift is assumed, including people moving from Medicaid?

- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_membership_change_reason`: `membership_change_reason_id`, `membership_change_reason_code`, `membership_change_reason_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_eligibility_recheck`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `plan_type_id`, `rechecked_member_quantity`, `removed_member_quantity`
- `healthplan.membership.fact_medicaid_redetermination`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `plan_type_id`, `redetermined_member_quantity`, `disenrolled_member_quantity`
- `healthplan.membership.fact_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `enrollment_channel_id`, `member_months_quantity`, `end_of_period_member_quantity`
- `healthplan.membership.fact_work_requirement_attrition`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `legislation_id`, `assumed_attrition_quantity`, `affected_member_quantity`
- `healthplan.price.dim_legislation`: `legislation_id`, `legislation_code`, `legislation_name`

### Q2 2025 (8)

Why did proactive risk-pool work during Medicaid redeterminations still fail to keep up with the shifts?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.fact_coding_submissions`: `fiscal_quarter_id`, `scenario_id`, `risk_model_version_id`, `provider_group_id`, `plan_type_id`, `submitted_code_quantity`, `chronic_condition_code_quantity`, `encounter_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.medical.fact_value_based_attributed_lives`: `fiscal_quarter_id`, `scenario_id`, `provider_group_id`, `payment_arrangement_id`, `plan_type_id`, `attributed_life_quantity`, `negotiation_life_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_work_requirement_attrition`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `legislation_id`, `assumed_attrition_quantity`, `affected_member_quantity`
- `healthplan.price.dim_legislation`: `legislation_id`, `legislation_code`, `legislation_name`

### Q2 2025 (10)

How are Carelon margins tracking versus the initial plan, and when does pressure from large-employer pharmacy growth, specialty drugs, and CareBridge normalize?

- `healthplan.medical.dim_dispensing_category`: `dispensing_category_id`, `dispensing_category_code`, `dispensing_category_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_drug_therapy_class`: `drug_therapy_class_id`, `drug_therapy_class_code`, `drug_therapy_class_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.dim_blue_plan_client_type`: `blue_plan_client_type_id`, `blue_plan_client_type_code`, `blue_plan_client_type_name`
- `healthplan.price.dim_carelon_business`: `carelon_business_id`, `carelon_business_code`, `carelon_business_name`
- `healthplan.price.fact_blue_plan_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `blue_plan_client_type_id`, `carelon_business_id`, `service_contract_revenue_amount`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_pharmacy_cost`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `drug_therapy_class_id`, `dispensing_category_id`, `pharmacy_claim_cost_amount`, `manufacturer_rebate_amount`

### Q2 2025 (12)

Is it time to exit states or shrink Medicaid populations where the rate disconnect persists?

- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_work_requirement_attrition`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `legislation_id`, `assumed_attrition_quantity`, `affected_member_quantity`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.dim_earnings_bridge_component`: `earnings_bridge_component_id`, `earnings_bridge_component_code`, `earnings_bridge_component_name`
- `healthplan.price.dim_legislation`: `legislation_id`, `legislation_code`, `legislation_name`
- `healthplan.price.dim_rate_notice_type`: `rate_notice_type_id`, `rate_notice_type_code`, `rate_notice_type_name`
- `healthplan.price.fact_earnings_bridge`: `fiscal_quarter_id`, `scenario_id`, `earnings_bridge_component_id`, `bridge_amount`
- `healthplan.price.fact_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `premium_per_member_per_month_amount`
- `healthplan.price.fact_rate_update`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `state_id`, `rate_notice_type_id`, `announced_rate_change_percent`, `final_rate_change_percent`

### Q2 2025 (14)

Are delayed exchange eligibility rechecks finished, and is the resulting member attrition already in the updated outlook?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_drug_therapy_class`: `drug_therapy_class_id`, `drug_therapy_class_code`, `drug_therapy_class_name`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_eligibility_recheck`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `plan_type_id`, `rechecked_member_quantity`, `removed_member_quantity`
- `healthplan.price.dim_member_cost_sharing`: `member_cost_sharing_id`, `member_cost_sharing_code`, `member_cost_sharing_name`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_member_cost_sharing`: `fiscal_quarter_id`, `scenario_id`, `member_cost_sharing_id`, `drug_therapy_class_id`, `average_copayment_amount`, `coinsurance_percent`
- `healthplan.price.fact_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `premium_per_member_per_month_amount`
