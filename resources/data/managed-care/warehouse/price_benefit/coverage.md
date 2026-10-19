# Health Plan Inc price, benefit and margin slice

This slice is part of the Health Plan Inc warehouse. Quantity, capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

## UnitedHealth Group

### Q2 2026 (2)

How far is commercial medical-cost trend running versus the roughly 11% assumption?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_cost_by_line`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_cost_trend`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `medical_cost_trend_percent`, `assumed_trend_percent`

### Q2 2026 (3)

Which parts of the operating turnaround are largely finished, and where do the remaining gaps sit?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispensing_category`: `dispensing_category_id`, `dispensing_category_code`, `dispensing_category_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_drug_therapy_class`: `drug_therapy_class_id`, `drug_therapy_class_code`, `drug_therapy_class_name`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.dim_member_cost_sharing`: `member_cost_sharing_id`, `member_cost_sharing_code`, `member_cost_sharing_name`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_member_cost_sharing`: `fiscal_quarter_id`, `scenario_id`, `member_cost_sharing_id`, `drug_therapy_class_id`, `average_copayment_amount`, `coinsurance_percent`
- `healthplan.price.fact_pharmacy_cost`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `drug_therapy_class_id`, `dispensing_category_id`, `pharmacy_claim_cost_amount`, `manufacturer_rebate_amount`

### Q2 2026 (5)

What cost trend was assumed in the Medicare Advantage bids that were just finalized?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.dim_member_cost_sharing`: `member_cost_sharing_id`, `member_cost_sharing_code`, `member_cost_sharing_name`
- `healthplan.price.fact_bid_assumptions`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `bid_process_id`, `assumed_medical_cost_trend_percent`, `filed_premium_change_percent`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_cost_trend`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `medical_cost_trend_percent`, `assumed_trend_percent`

### Q2 2026 (12)

Why did Optum Insight beat expectations, and how should that be read against the rest of the year?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_id`, `bed_quantity`, `operating_room_quantity`, `available_slot_quantity`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.medical.fact_optum_employed_clinician_capacity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `site_of_care_id`, `employed_clinician_quantity`, `patient_panel_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.dim_optum_business`: `optum_business_id`, `optum_business_code`, `optum_business_name`
- `healthplan.price.fact_optum_business_result`: `fiscal_quarter_id`, `scenario_id`, `optum_business_id`, `business_revenue_amount`, `business_operating_income_amount`

### Q2 2026 (13)

Can AI pull Optum Health margins ahead of the long-term targets, or is the near-term work still basic operating repair?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_id`, `bed_quantity`, `operating_room_quantity`, `available_slot_quantity`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.medical.fact_optum_employed_clinician_capacity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `site_of_care_id`, `employed_clinician_quantity`, `patient_panel_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.dim_investment_program_type`: `investment_program_type_id`, `investment_program_type_code`, `investment_program_type_name`
- `healthplan.price.dim_optum_business`: `optum_business_id`, `optum_business_code`, `optum_business_name`
- `healthplan.price.fact_optum_business_result`: `fiscal_quarter_id`, `scenario_id`, `optum_business_id`, `business_revenue_amount`, `business_operating_income_amount`

### Q1 2026 (1)

Is Medicare Advantage cost trend holding near the roughly 10% level used in pricing, or is it still closer to the prior 7% to 8% range?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.fact_bid_assumptions`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `bid_process_id`, `assumed_medical_cost_trend_percent`, `filed_premium_change_percent`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_cost_trend`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `medical_cost_trend_percent`, `assumed_trend_percent`

### Q1 2026 (3)

How much of the Optum Health outperformance is contract and benefit design versus lower utilization?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.medical.dim_provider_organization_type`: `provider_organization_type_id`, `provider_organization_type_code`, `provider_organization_type_name`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.dim_optum_business`: `optum_business_id`, `optum_business_code`, `optum_business_name`
- `healthplan.price.fact_optum_business_result`: `fiscal_quarter_id`, `scenario_id`, `optum_business_id`, `business_revenue_amount`, `business_operating_income_amount`
- `healthplan.price.fact_provider_reimbursement`: `fiscal_quarter_id`, `scenario_id`, `payment_arrangement_id`, `provider_organization_type_id`, `reimbursement_amount`, `capitation_amount`

### Q1 2026 (4)

How much of the Optum Health beat versus the internal plan was prior-period development rather than a higher run rate?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.dim_earnings_bridge_component`: `earnings_bridge_component_id`, `earnings_bridge_component_code`, `earnings_bridge_component_name`
- `healthplan.price.fact_earnings_bridge`: `fiscal_quarter_id`, `scenario_id`, `earnings_bridge_component_id`, `bridge_amount`
- `healthplan.price.fact_reserve_development`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `earnings_bridge_component_id`, `prior_period_development_amount`, `current_period_reserve_amount`

### Q1 2026 (5)

How confident is further Medicare Advantage margin recovery in 2027 now that the final rate is known?

- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.dim_rate_notice_type`: `rate_notice_type_id`, `rate_notice_type_code`, `rate_notice_type_name`
- `healthplan.price.fact_bid_assumptions`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `bid_process_id`, `assumed_medical_cost_trend_percent`, `filed_premium_change_percent`
- `healthplan.price.fact_medical_loss_ratio`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `medical_loss_ratio_percent`
- `healthplan.price.fact_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `premium_per_member_per_month_amount`
- `healthplan.price.fact_rate_update`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `state_id`, `rate_notice_type_id`, `announced_rate_change_percent`, `final_rate_change_percent`

### Q1 2026 (7)

Why is Optum Insight and Optum Rx earnings more weighted to the back half than in prior years?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_optum_employed_clinician_capacity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `site_of_care_id`, `employed_clinician_quantity`, `patient_panel_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.price.dim_optum_business`: `optum_business_id`, `optum_business_code`, `optum_business_name`
- `healthplan.price.fact_optum_business_result`: `fiscal_quarter_id`, `scenario_id`, `optum_business_id`, `business_revenue_amount`, `business_operating_income_amount`

### Q1 2026 (10)

What internal target exists for AI savings in G&A?

- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.fact_claim_inventory`: `fiscal_quarter_id`, `scenario_id`, `claim_status_id`, `plan_type_id`, `claim_quantity`, `claim_age_days`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.dim_investment_program_type`: `investment_program_type_id`, `investment_program_type_code`, `investment_program_type_name`
- `healthplan.price.fact_bid_assumptions`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `bid_process_id`, `assumed_medical_cost_trend_percent`, `filed_premium_change_percent`
- `healthplan.price.fact_investment_spending`: `fiscal_quarter_id`, `scenario_id`, `investment_program_type_id`, `investment_spending_amount`, `measured_savings_amount`

### Q1 2026 (12)

How should prior-period development in the quarter be split between UnitedHealthcare and Optum Health?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_optum_employed_clinician_capacity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `site_of_care_id`, `employed_clinician_quantity`, `patient_panel_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.dim_earnings_bridge_component`: `earnings_bridge_component_id`, `earnings_bridge_component_code`, `earnings_bridge_component_name`
- `healthplan.price.dim_optum_business`: `optum_business_id`, `optum_business_code`, `optum_business_name`
- `healthplan.price.dim_unitedhealth_segment`: `unitedhealth_segment_id`, `unitedhealth_segment_code`, `unitedhealth_segment_name`
- `healthplan.price.fact_optum_business_result`: `fiscal_quarter_id`, `scenario_id`, `optum_business_id`, `business_revenue_amount`, `business_operating_income_amount`
- `healthplan.price.fact_reserve_development`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `earnings_bridge_component_id`, `prior_period_development_amount`, `current_period_reserve_amount`

### Q4 2025 (2)

Why did fourth-quarter Optum Health operating income finish well below the level implied by the prior outlook?

- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.dim_optum_business`: `optum_business_id`, `optum_business_code`, `optum_business_name`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_insurance_operating_result`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `insurance_operating_income_amount`, `underwriting_income_amount`
- `healthplan.price.fact_optum_business_result`: `fiscal_quarter_id`, `scenario_id`, `optum_business_id`, `business_revenue_amount`, `business_operating_income_amount`

### Q4 2025 (7)

What is the 2026 medical-cost trend by Medicare, Medicaid, and commercial, and how did 2025 finish versus expectations?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_cost_by_line`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_cost_trend`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `medical_cost_trend_percent`, `assumed_trend_percent`

### Q4 2025 (8)

Have any Optum Care turnaround initiatives produced surprises versus the plan?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_dispute_cases`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_case_quantity`, `resolved_case_quantity`, `resolution_duration_days`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`

### Q3 2025 (1)

Where does Optum Insight stand competitively, and when should investment translate into faster growth?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_coding_submissions`: `fiscal_quarter_id`, `scenario_id`, `risk_model_version_id`, `provider_group_id`, `plan_type_id`, `submitted_code_quantity`, `chronic_condition_code_quantity`, `encounter_quantity`
- `healthplan.medical.fact_optum_employed_clinician_capacity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `site_of_care_id`, `employed_clinician_quantity`, `patient_panel_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.dim_investment_program_type`: `investment_program_type_id`, `investment_program_type_code`, `investment_program_type_name`
- `healthplan.price.dim_optum_business`: `optum_business_id`, `optum_business_code`, `optum_business_name`
- `healthplan.price.fact_investment_spending`: `fiscal_quarter_id`, `scenario_id`, `investment_program_type_id`, `investment_spending_amount`, `measured_savings_amount`
- `healthplan.price.fact_optum_business_result`: `fiscal_quarter_id`, `scenario_id`, `optum_business_id`, `business_revenue_amount`, `business_operating_income_amount`

### Q3 2025 (2)

Is commercial margin still on track to return to the 7% to 9% range in 2027, and is the 2025 baseline closer to 3% to 5%?

- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.membership.dim_employer_account_size`: `employer_account_size_id`, `employer_account_size_code`, `employer_account_size_name`
- `healthplan.membership.dim_employer_sector`: `employer_sector_id`, `employer_sector_code`, `employer_sector_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_employer_covered_lives`: `fiscal_quarter_id`, `scenario_id`, `employer_account_size_id`, `employer_sector_id`, `funding_arrangement_id`, `covered_life_quantity`, `member_months_quantity`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_loss_ratio`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `medical_loss_ratio_percent`

### Q3 2025 (5)

How large was the third-quarter step-up in discretionary investment, and how much is run rate versus one-time?

- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_employer_account_size`: `employer_account_size_id`, `employer_account_size_code`, `employer_account_size_name`
- `healthplan.membership.dim_employer_sector`: `employer_sector_id`, `employer_sector_code`, `employer_sector_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_employer_covered_lives`: `fiscal_quarter_id`, `scenario_id`, `employer_account_size_id`, `employer_sector_id`, `funding_arrangement_id`, `covered_life_quantity`, `member_months_quantity`
- `healthplan.price.dim_earnings_bridge_component`: `earnings_bridge_component_id`, `earnings_bridge_component_code`, `earnings_bridge_component_name`
- `healthplan.price.fact_earnings_bridge`: `fiscal_quarter_id`, `scenario_id`, `earnings_bridge_component_id`, `bridge_amount`
- `healthplan.price.fact_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `premium_per_member_per_month_amount`

### Q3 2025 (9)

What employer medical-cost trend is being seen this year and next?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_dispute_cases`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_case_quantity`, `resolved_case_quantity`, `resolution_duration_days`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_cost_trend`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `medical_cost_trend_percent`, `assumed_trend_percent`

### Q3 2025 (10)

How wide is the Optum Health portfolio rationalization under the new approach?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_optum_employed_clinician_capacity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `site_of_care_id`, `employed_clinician_quantity`, `patient_panel_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.dim_optum_business`: `optum_business_id`, `optum_business_code`, `optum_business_name`
- `healthplan.price.fact_optum_business_result`: `fiscal_quarter_id`, `scenario_id`, `optum_business_id`, `business_revenue_amount`, `business_operating_income_amount`

## Elevance Health

### Q2 2026 (3)

How did first-half exchange results compare with plan once risk adjustment was clearer, and where does the risk-adjustment position stand?

- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.fact_coding_submissions`: `fiscal_quarter_id`, `scenario_id`, `risk_model_version_id`, `provider_group_id`, `plan_type_id`, `submitted_code_quantity`, `chronic_condition_code_quantity`, `encounter_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_metal_tier`: `metal_tier_id`, `metal_tier_code`, `metal_tier_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_pharmacy_benefit_member_months`: `fiscal_quarter_id`, `scenario_id`, `pharmacy_benefit_program_id`, `state_id`, `member_months_quantity`, `member_quantity`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_risk_adjustment_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `state_id`, `risk_adjustment_receivable_amount`, `risk_adjustment_payable_amount`, `risk_adjustment_accrual_amount`

### Q2 2026 (6)

For 2027, are ACA and Medicare Advantage bids aimed at growth or at further margin recovery?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
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
- `healthplan.price.fact_medical_loss_ratio`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `medical_loss_ratio_percent`

### Q2 2026 (8)

How much operating leverage do the one-time investments create next year, and are they technology or people?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispensing_category`: `dispensing_category_id`, `dispensing_category_code`, `dispensing_category_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_drug_therapy_class`: `drug_therapy_class_id`, `drug_therapy_class_code`, `drug_therapy_class_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.dim_investment_program_type`: `investment_program_type_id`, `investment_program_type_code`, `investment_program_type_name`
- `healthplan.price.dim_member_cost_sharing`: `member_cost_sharing_id`, `member_cost_sharing_code`, `member_cost_sharing_name`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_member_cost_sharing`: `fiscal_quarter_id`, `scenario_id`, `member_cost_sharing_id`, `drug_therapy_class_id`, `average_copayment_amount`, `coinsurance_percent`
- `healthplan.price.fact_pharmacy_cost`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `drug_therapy_class_id`, `dispensing_category_id`, `pharmacy_claim_cost_amount`, `manufacturer_rebate_amount`

### Q2 2026 (9)

Why did better Medicaid rates not lift the margin outlook, and why are more exits still required?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_drug_therapy_class`: `drug_therapy_class_id`, `drug_therapy_class_code`, `drug_therapy_class_name`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.price.dim_member_cost_sharing`: `member_cost_sharing_id`, `member_cost_sharing_code`, `member_cost_sharing_name`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_loss_ratio`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `medical_loss_ratio_percent`
- `healthplan.price.fact_member_cost_sharing`: `fiscal_quarter_id`, `scenario_id`, `member_cost_sharing_id`, `drug_therapy_class_id`, `average_copayment_amount`, `coinsurance_percent`

### Q2 2026 (14)

Are Medicare Advantage utilization trends more favorable, and is that expected to continue?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.fact_medical_cost_trend`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `medical_cost_trend_percent`, `assumed_trend_percent`

### Q1 2026 (6)

With Medicaid margin ahead of plan, what rate increases are embedded in the 2026 outlook?

- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.dim_rate_notice_type`: `rate_notice_type_id`, `rate_notice_type_code`, `rate_notice_type_name`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_medical_loss_ratio`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `medical_loss_ratio_percent`
- `healthplan.price.fact_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `premium_per_member_per_month_amount`
- `healthplan.price.fact_rate_update`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `state_id`, `rate_notice_type_id`, `announced_rate_change_percent`, `final_rate_change_percent`

### Q1 2026 (8)

How much of the quarter's outperformance is claims management versus flu and weather?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispensing_category`: `dispensing_category_id`, `dispensing_category_code`, `dispensing_category_name`
- `healthplan.medical.dim_drug_therapy_class`: `drug_therapy_class_id`, `drug_therapy_class_code`, `drug_therapy_class_name`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.price.dim_member_cost_sharing`: `member_cost_sharing_id`, `member_cost_sharing_code`, `member_cost_sharing_name`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_cost_by_line`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_member_cost_sharing`: `fiscal_quarter_id`, `scenario_id`, `member_cost_sharing_id`, `drug_therapy_class_id`, `average_copayment_amount`, `coinsurance_percent`
- `healthplan.price.fact_pharmacy_cost`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `drug_therapy_class_id`, `dispensing_category_id`, `pharmacy_claim_cost_amount`, `manufacturer_rebate_amount`

### Q1 2026 (14)

How much of the targeted 2027 earnings growth depends on pricing and trend the company can influence if Medicaid stays pressured?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `enrollment_channel_id`, `member_months_quantity`, `end_of_period_member_quantity`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_cost_trend`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `medical_cost_trend_percent`, `assumed_trend_percent`

### Q4 2025 (4)

What is the 2026 Medicaid rate outlook, and how should rates be thought about after this year?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_medicaid_redetermination`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `plan_type_id`, `redetermined_member_quantity`, `disenrolled_member_quantity`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.dim_rate_notice_type`: `rate_notice_type_id`, `rate_notice_type_code`, `rate_notice_type_name`
- `healthplan.price.fact_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `premium_per_member_per_month_amount`
- `healthplan.price.fact_rate_update`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `state_id`, `rate_notice_type_id`, `announced_rate_change_percent`, `final_rate_change_percent`

### Q4 2025 (5)

Which Medicare or commercial opportunities support a return to faster earnings growth in 2027 after two years of elevated trend?

- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `enrollment_channel_id`, `member_months_quantity`, `end_of_period_member_quantity`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.fact_bid_assumptions`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `bid_process_id`, `assumed_medical_cost_trend_percent`, `filed_premium_change_percent`

### Q4 2025 (6)

Which investment buckets were pulled forward, and how much of that spending is still inside the 2026 outlook?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_id`, `bed_quantity`, `operating_room_quantity`, `available_slot_quantity`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.dim_investment_program_type`: `investment_program_type_id`, `investment_program_type_code`, `investment_program_type_name`
- `healthplan.price.fact_investment_spending`: `fiscal_quarter_id`, `scenario_id`, `investment_program_type_id`, `investment_spending_amount`, `measured_savings_amount`

### Q4 2025 (10)

How can the Medicare Advantage rate notice be mitigated on top of this year's benefit cuts, and what does it mean for industry margins?

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
- `healthplan.price.dim_rate_notice_type`: `rate_notice_type_id`, `rate_notice_type_code`, `rate_notice_type_name`
- `healthplan.price.fact_premium_rate`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `premium_per_member_per_month_amount`
- `healthplan.price.fact_rate_update`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `state_id`, `rate_notice_type_id`, `announced_rate_change_percent`, `final_rate_change_percent`

### Q4 2025 (11)

Which Carelon services are taking risk, and can that offset the margin shift in CarelonRx?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.fact_carelon_home_care_quantity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `state_id`, `home_visit_quantity`, `served_member_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.price.dim_carelon_business`: `carelon_business_id`, `carelon_business_code`, `carelon_business_name`
- `healthplan.price.fact_carelon_business_result`: `fiscal_quarter_id`, `scenario_id`, `carelon_business_id`, `business_revenue_amount`, `business_operating_income_amount`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_medical_loss_ratio`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `medical_loss_ratio_percent`

### Q4 2025 (14)

How much of CarelonRx and Carelon services revenue and margin comes from health-benefits enrollment losses versus external clients?

- `healthplan.medical.dim_care_program`: `care_program_id`, `care_program_code`, `care_program_name`
- `healthplan.medical.dim_payment_arrangement`: `payment_arrangement_id`, `payment_arrangement_code`, `payment_arrangement_name`
- `healthplan.medical.fact_carelon_home_care_quantity`: `fiscal_quarter_id`, `scenario_id`, `care_program_id`, `state_id`, `home_visit_quantity`, `served_member_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.price.dim_blue_plan_client_type`: `blue_plan_client_type_id`, `blue_plan_client_type_code`, `blue_plan_client_type_name`
- `healthplan.price.dim_carelon_business`: `carelon_business_id`, `carelon_business_code`, `carelon_business_name`
- `healthplan.price.dim_elevance_segment`: `elevance_segment_id`, `elevance_segment_code`, `elevance_segment_name`
- `healthplan.price.dim_revenue_type`: `revenue_type_id`, `revenue_type_code`, `revenue_type_name`
- `healthplan.price.fact_blue_plan_service_revenue`: `fiscal_quarter_id`, `scenario_id`, `blue_plan_client_type_id`, `carelon_business_id`, `service_contract_revenue_amount`
- `healthplan.price.fact_carelon_business_result`: `fiscal_quarter_id`, `scenario_id`, `carelon_business_id`, `business_revenue_amount`, `business_operating_income_amount`
- `healthplan.price.fact_services_contract_revenue`: `fiscal_quarter_id`, `scenario_id`, `revenue_type_id`, `state_id`, `contract_revenue_amount`, `external_client_revenue_amount`

### Q2 2025 (1)

How much of the ACA pressure is unit-cost trend versus the risk pool, and why is risk adjustment unchanged despite higher morbidity?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_provider_group`: `provider_group_id`, `provider_group_name`, `provider_employment_model_id`
- `healthplan.medical.dim_risk_model_version`: `risk_model_version_id`, `risk_model_version_code`, `risk_model_version_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_coding_submissions`: `fiscal_quarter_id`, `scenario_id`, `risk_model_version_id`, `provider_group_id`, `plan_type_id`, `submitted_code_quantity`, `chronic_condition_code_quantity`, `encounter_quantity`
- `healthplan.medical.fact_medical_utilization`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `site_of_care_id`, `encounter_quantity`, `admission_quantity`, `procedure_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_metal_tier`: `metal_tier_id`, `metal_tier_code`, `metal_tier_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_risk_adjustment_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `state_id`, `risk_adjustment_receivable_amount`, `risk_adjustment_payable_amount`, `risk_adjustment_accrual_amount`

### Q2 2025 (3)

Are Medicaid base-period rates being set too low relative to forward trend, leaving the company repeatedly underpaid?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_provider_employment_model`: `provider_employment_model_id`, `provider_employment_model_code`, `provider_employment_model_name`
- `healthplan.membership.dim_enrollment_channel`: `enrollment_channel_id`, `enrollment_channel_code`, `enrollment_channel_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.membership.fact_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `enrollment_channel_id`, `member_months_quantity`, `end_of_period_member_quantity`
- `healthplan.membership.fact_work_requirement_attrition`: `fiscal_quarter_id`, `scenario_id`, `state_id`, `legislation_id`, `assumed_attrition_quantity`, `affected_member_quantity`
- `healthplan.price.dim_legislation`: `legislation_id`, `legislation_code`, `legislation_name`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`

### Q2 2025 (5)

What would be done differently in ACA pricing and in state rate negotiations to make results more predictable?

- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_facility`: `facility_id`, `facility_name`, `site_of_care_id`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_funding_arrangement`: `funding_arrangement_id`, `funding_arrangement_code`, `funding_arrangement_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.fact_bid_assumptions`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `bid_process_id`, `assumed_medical_cost_trend_percent`, `filed_premium_change_percent`
- `healthplan.price.fact_medical_cost_trend`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `medical_cost_trend_percent`, `assumed_trend_percent`
- `healthplan.price.fact_medical_loss_ratio`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `medical_loss_ratio_percent`
- `healthplan.price.fact_premium_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `funding_arrangement_id`, `state_id`, `premium_earned_amount`, `premium_written_amount`

### Q2 2025 (9)

If Medicaid cost trend slowed slightly while underlying utilization rose, what drove the utilization, and are states carving benefits in without matching rates?

- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.membership.dim_dual_eligibility_status`: `dual_eligibility_status_id`, `dual_eligibility_status_code`, `dual_eligibility_status_name`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_pharmacy_benefit_program`: `pharmacy_benefit_program_id`, `pharmacy_benefit_program_code`, `pharmacy_benefit_program_name`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.price.fact_dispute_cost`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_cost_amount`, `dispute_fee_amount`
- `healthplan.price.fact_medical_cost_amount`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `incurred_medical_cost_amount`, `paid_medical_cost_amount`
- `healthplan.price.fact_medical_cost_trend`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `medical_cost_trend_percent`, `assumed_trend_percent`

### Q2 2025 (11)

How large is the expected fourth-quarter ACA acuity surge, and what other one-time items sit in the back-half outlook?

- `healthplan.medical.dim_claim_status`: `claim_status_id`, `claim_status_code`, `claim_status_name`
- `healthplan.medical.dim_clinical_service`: `clinical_service_id`, `clinical_service_code`, `clinical_service_name`
- `healthplan.medical.dim_dispute_type`: `dispute_type_id`, `dispute_type_code`, `dispute_type_name`
- `healthplan.medical.dim_site_of_care`: `site_of_care_id`, `site_of_care_code`, `site_of_care_name`
- `healthplan.medical.fact_dispute_cases`: `fiscal_quarter_id`, `scenario_id`, `dispute_type_id`, `plan_type_id`, `dispute_case_quantity`, `resolved_case_quantity`, `resolution_duration_days`
- `healthplan.medical.fact_service_member_months`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `clinical_service_id`, `member_months_quantity`
- `healthplan.medical.fact_site_of_care_cases`: `fiscal_quarter_id`, `scenario_id`, `clinical_service_id`, `site_of_care_id`, `case_quantity`, `shifted_case_quantity`
- `healthplan.membership.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `healthplan.membership.dim_plan_type`: `plan_type_id`, `plan_type_code`, `plan_type_name`
- `healthplan.membership.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `healthplan.membership.dim_state`: `state_id`, `state_name`, `region_id`
- `healthplan.price.dim_bid_process`: `bid_process_id`, `bid_process_code`, `bid_process_name`
- `healthplan.price.fact_bid_assumptions`: `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `bid_process_id`, `assumed_medical_cost_trend_percent`, `filed_premium_change_percent`
