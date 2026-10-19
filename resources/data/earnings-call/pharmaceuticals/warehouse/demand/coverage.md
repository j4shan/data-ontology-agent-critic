# Pharma Inc demand slice

This slice is part of the Pharma Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q2 2026 (1) — Eli Lilly

For Eli Lilly, How is the consumer obesity market evolving versus the international self-pay market, including a more aesthetic use?

- `pharma.demand.fact_market_access_demand`: `market_access_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `eligible_patient_count`, `activated_patient_count`
- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.fact_cardio_metabolic_demand`: `cardio_metabolic_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `patient_segment_id`, `cardio_patient_count`, `pcsk9_eligible_patient_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (2) — Eli Lilly

For Eli Lilly, What would create an inflection in the lagging market, and what share dynamics showed up in the UAE after Novo launched and claimed a large early share?

- `pharma.demand.fact_market_access_demand`: `market_access_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `eligible_patient_count`, `activated_patient_count`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (6) — Eli Lilly

For Eli Lilly, What is the post-Verzenio breast-cancer strategy, including an all-oral combination?

- `pharma.demand.fact_cardio_metabolic_demand`: `cardio_metabolic_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `patient_segment_id`, `cardio_patient_count`, `pcsk9_eligible_patient_count`
- `pharma.demand.fact_combination_type_demand`: `combination_type_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `combination_type_id`, `geography_id`, `combination_type_activity_count`
- `pharma.demand.fact_combination_demand`: `combination_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `combination_type_id`, `product_id`, `indication_id`, `combination_patient_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (3) — Eli Lilly

For Eli Lilly, Where does each potential asset open the market?

- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.demand.fact_market_access_demand`: `market_access_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `eligible_patient_count`, `activated_patient_count`
- `pharma.price.fact_business_development`: `business_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `deal_value_amount`, `milestone_payment_amount`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (5) — Eli Lilly

For Eli Lilly, What would immunology, neuroscience, or oncology have to show to match the scale of obesity and metabolic?

- `pharma.demand.fact_oncology_demand`: `oncology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `patient_segment_id`, `oncology_patient_count`, `treatment_line_count`
- `pharma.demand.fact_immunology_demand`: `immunology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `immunology_patient_count`
- `pharma.demand.fact_cardio_metabolic_demand`: `cardio_metabolic_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `patient_segment_id`, `cardio_patient_count`, `pcsk9_eligible_patient_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (7) — Eli Lilly

For Eli Lilly, With the bridge program extended into 2027, what is being done with stakeholders to secure longer-term Medicare access?

- `pharma.demand.fact_market_access_demand`: `market_access_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `eligible_patient_count`, `activated_patient_count`
- `pharma.supply.fact_research_capacity`: `research_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `employee_group_id`, `therapy_area_id`, `scientist_count`, `research_program_count`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (2) — Eli Lilly

For Eli Lilly, How should international Mounjaro grow sequentially from the current base now that those markets are open?

- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.demand.fact_market_access_demand`: `market_access_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `eligible_patient_count`, `activated_patient_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (3) — Eli Lilly

For Eli Lilly, What stops immunology from being invested in as early and aggressively as obesity?

- `pharma.demand.fact_immunology_demand`: `immunology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `immunology_patient_count`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (5) — Eli Lilly

For Eli Lilly, Are combinations of Zepbound with immunology, oncology, or neuroscience being pursued?

- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_oncology_demand`: `oncology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `patient_segment_id`, `oncology_patient_count`, `treatment_line_count`
- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (7) — Eli Lilly

For Eli Lilly, Could the metabolic profile become a long-term differentiator in liver disease and in immunology indications?

- `pharma.demand.fact_immunology_demand`: `immunology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `immunology_patient_count`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_oncology_demand`: `oncology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `patient_segment_id`, `oncology_patient_count`, `treatment_line_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (2) — Eli Lilly

For Eli Lilly, How are new-country launches trending versus plan, and how does growth come off that higher base?

- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.demand.fact_age_group_demand`: `age_group_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `patient_age_group_id`, `product_id`, `therapy_area_id`, `age_group_patient_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (4) — Eli Lilly

For Eli Lilly, Is the commercial strategy more consumer-centric through Lilly Direct?

- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_oncology_demand`: `oncology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `patient_segment_id`, `oncology_patient_count`, `treatment_line_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (5) — Eli Lilly

For Eli Lilly, Could a GLP-1/GIP such as the incretin in development be a drug for Alzheimer's because of neural effects?

- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `manufacturing_site_id`, `dosage_form_id`, `therapy_area_id`, `dose_capacity_count`, `batch_capacity_count`, `utilized_batch_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (6) — Eli Lilly

For Eli Lilly, How far can the orthopedics market be extended, and should new-patient starts slow?

- `pharma.demand.fact_market_access_demand`: `market_access_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `eligible_patient_count`, `activated_patient_count`
- `pharma.demand.fact_persistence`: `persistence_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `patient_segment_id`, `dosage_form_id`, `persisting_patient_count`, `started_patient_count`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (1) — Merck

For Merck, Could a broad sac-TMT plus pembrolizumab trial be run head-to-head against KEYNOTE-189, and could sac-TMT be combined with both pembrolizumab and a PD-1/VEGF agent in first-line lung cancer?

- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.price.fact_operating_expense`: `operating_expense_record_id`, `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `therapy_area_id`, `operating_expense_amount`
- `pharma.demand.fact_trial_activity`: `trial_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `trial_id`, `product_id`, `indication_id`, `geography_id`, `enrolled_participant_count`, `trial_site_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (2) — Merck

For Merck, In the new immunology indications, is TL1A activity beyond what a TNF would have been expected to do?

- `pharma.demand.fact_immunology_demand`: `immunology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `immunology_patient_count`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_oncology_demand`: `oncology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `patient_segment_id`, `oncology_patient_count`, `treatment_line_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (3) — Merck

For Merck, Ahead of AstraZeneca's AVANZAR data, what would matter most for sac-TMT development?

- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.price.fact_business_development`: `business_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `deal_value_amount`, `milestone_payment_amount`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (4) — Merck

For Merck, How does the ulcerative-colitis profile, with a second study still coming, change the Crohn's and fibrosis opportunity?

- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.fact_oncology_demand`: `oncology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `patient_segment_id`, `oncology_patient_count`, `treatment_line_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (5) — Merck

For Merck, What initial access and reimbursement pace is expected for the oral PCSK9 launch, and does the outcomes trial change that?

- `pharma.demand.fact_cardio_metabolic_demand`: `cardio_metabolic_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `patient_segment_id`, `cardio_patient_count`, `pcsk9_eligible_patient_count`
- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.demand.fact_trial_activity`: `trial_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `trial_id`, `product_id`, `indication_id`, `geography_id`, `enrolled_participant_count`, `trial_site_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (7) — Merck

For Merck, Is the injectable PCSK9 switch opportunity larger, or the PCSK9-naive population, once an oral is available?

- `pharma.demand.fact_cardio_metabolic_demand`: `cardio_metabolic_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `patient_segment_id`, `cardio_patient_count`, `pcsk9_eligible_patient_count`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (1) — Merck

For Merck, Can the asset hit its targets if it requires every-four-week dosing, given that many patients respond suboptimally to VEGF?

- `pharma.demand.fact_persistence`: `persistence_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `patient_segment_id`, `dosage_form_id`, `persisting_patient_count`, `started_patient_count`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (2) — Merck

For Merck, Does the recent readout concern the chance of an overall-survival benefit in LITESPARK-022?

- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.fact_oncology_demand`: `oncology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `patient_segment_id`, `oncology_patient_count`, `treatment_line_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (3) — Merck

For Merck, Into ASCO, how is sac-TMT in lung cancer positioned against a competitor PD-1/VEGF plenary?

- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.fact_oncology_demand`: `oncology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `patient_segment_id`, `oncology_patient_count`, `treatment_line_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (5) — Merck

For Merck, How are FDA discussions going on advancing the Phase II program, and is the clinical package still expected to be sufficient?

- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.supply.fact_research_capacity`: `research_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `employee_group_id`, `therapy_area_id`, `scientist_count`, `research_program_count`
- `pharma.supply.fact_trial_site_capacity`: `trial_site_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `geography_id`, `therapy_area_id`, `active_trial_site_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (6) — Merck

For Merck, What should be kept in mind when U.S. outcomes may not translate globally?

- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.fact_oncology_demand`: `oncology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `patient_segment_id`, `oncology_patient_count`, `treatment_line_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (7) — Merck

For Merck, What gates FDA acceptance of the enlicitide application, and which shorter titration durations are being pursued?

- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.demand.fact_age_group_demand`: `age_group_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `patient_age_group_id`, `product_id`, `therapy_area_id`, `age_group_patient_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (8) — Merck

For Merck, What role is TL1A expected to play in inflammatory bowel disease inside a broader pipeline?

- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (1) — Merck

For Merck, Does the vaccine case rest on robust data across two geographies and two seasons, is anything visible in the event-driven trial, and will an interim be disclosed?

- `pharma.demand.fact_vaccine_demand`: `vaccine_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `geography_id`, `patient_segment_id`, `vaccine_dose_count`, `vaccinated_person_count`
- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.demand.fact_trial_activity`: `trial_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `trial_id`, `product_id`, `indication_id`, `geography_id`, `enrolled_participant_count`, `trial_site_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (4) — Merck

For Merck, How important is a dual HIV regimen versus bictegravir, and what is the unmet need versus that standard?

- `pharma.demand.fact_hiv_demand`: `hiv_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `patient_segment_id`, `geography_id`, `hiv_patient_count`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (5) — Merck

For Merck, Can Merck grow sustainably, or is the pattern modest growth in good periods and pressure in weaker ones?

- `pharma.demand.fact_oncology_demand`: `oncology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `patient_segment_id`, `oncology_patient_count`, `treatment_line_count`
- `pharma.demand.fact_vaccine_demand`: `vaccine_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `geography_id`, `patient_segment_id`, `vaccine_dose_count`, `vaccinated_person_count`
- `pharma.price.fact_business_development`: `business_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `deal_value_amount`, `milestone_payment_amount`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (6) — Merck

For Merck, What should and should not be expected from the Cadence presentation, and which endpoints may be explored in the Phase III heart-failure study?

- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (7) — Merck

For Merck, With other TL1A players advancing, how do duration and real-world tolerability compare with Phase III, beyond the near-term ulcerative-colitis study?

- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.price.fact_other_product_revenue`: `other_product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `geography_id`, `other_product_sales_amount`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (1) — Merck

For Merck, Which immunology indications were selected for the expanded TL1A program, relative to the broad plan that came with the Prometheus deal?

- `pharma.demand.fact_immunology_demand`: `immunology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `immunology_patient_count`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_oncology_demand`: `oncology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `patient_segment_id`, `oncology_patient_count`, `treatment_line_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (2) — Merck

For Merck, Is the excitement greater for the TROP2 signal or the PD-1/VEGF class, and does that change appetite for another round of Phase III combinations?

- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.demand.fact_combination_type_demand`: `combination_type_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `combination_type_id`, `geography_id`, `combination_type_activity_count`
- `pharma.demand.fact_combination_demand`: `combination_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `combination_type_id`, `product_id`, `indication_id`, `combination_patient_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (3) — Merck

For Merck, What competitive uptake is expected heading into RSV season?

- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.fact_oncology_demand`: `oncology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `patient_segment_id`, `oncology_patient_count`, `treatment_line_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (6) — Merck

For Merck, How confident is an overall-survival hit in the WELIREG study, and how important is that?

- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.fact_oncology_demand`: `oncology_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `patient_segment_id`, `oncology_patient_count`, `treatment_line_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
