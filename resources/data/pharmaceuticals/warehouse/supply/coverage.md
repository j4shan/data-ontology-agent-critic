# Pharma Inc supply slice

This slice is part of the Pharma Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q2 2026 (4) — Eli Lilly

For Eli Lilly, What has the early Medicare obesity rollout shown on the ramp and on orals versus injectables?

- `pharma.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `manufacturing_site_id`, `dosage_form_id`, `therapy_area_id`, `dose_capacity_count`, `batch_capacity_count`, `utilized_batch_count`
- `pharma.supply.fact_supply_output`: `supply_output_record_id`, `fiscal_quarter_id`, `scenario_id`, `manufacturing_site_id`, `product_id`, `dosage_form_id`, `dose_supplied_count`, `unit_supplied_count`
- `pharma.supply.fact_research_capacity`: `research_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `employee_group_id`, `therapy_area_id`, `scientist_count`, `research_program_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (5) — Eli Lilly

For Eli Lilly, Does a commercial strategy need to defend against compounded supply until formal approval, and which extra indications does higher-efficacy retatrutide open?

- `pharma.supply.fact_regulatory_progress`: `regulatory_progress_record_id`, `fiscal_quarter_id`, `scenario_id`, `regulatory_pathway_id`, `geography_id`, `product_id`, `clinical_phase_id`, `filing_count`, `approval_count`
- `pharma.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `manufacturing_site_id`, `dosage_form_id`, `therapy_area_id`, `dose_capacity_count`, `batch_capacity_count`, `utilized_batch_count`
- `pharma.supply.fact_supply_output`: `supply_output_record_id`, `fiscal_quarter_id`, `scenario_id`, `manufacturing_site_id`, `product_id`, `dosage_form_id`, `dose_supplied_count`, `unit_supplied_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (7) — Eli Lilly

For Eli Lilly, Which regions outside the U.S. are growing fastest, and is the prescribing base expanding?

- `pharma.supply.fact_trial_region_capacity`: `trial_region_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `trial_region_id`, `therapy_area_id`, `region_trial_site_count`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (1) — Eli Lilly

For Eli Lilly, How do margins hold across a wide range of price scenarios given manufacturing already built, and how does that capacity function as a moat?

- `pharma.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `manufacturing_site_id`, `dosage_form_id`, `therapy_area_id`, `dose_capacity_count`, `batch_capacity_count`, `utilized_batch_count`
- `pharma.supply.fact_cold_chain_capacity`: `cold_chain_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `geography_id`, `dosage_form_id`, `cold_chain_dose_capacity_count`
- `pharma.supply.fact_batch_output`: `batch_output_record_id`, `fiscal_quarter_id`, `scenario_id`, `manufacturing_site_id`, `therapy_area_id`, `completed_batch_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (2) — Eli Lilly

For Eli Lilly, What has the launch taught about the ramp, and does generic semaglutide in selected markets change it this early?

- `pharma.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `manufacturing_site_id`, `dosage_form_id`, `therapy_area_id`, `dose_capacity_count`, `batch_capacity_count`, `utilized_batch_count`
- `pharma.supply.fact_supply_output`: `supply_output_record_id`, `fiscal_quarter_id`, `scenario_id`, `manufacturing_site_id`, `product_id`, `dosage_form_id`, `dose_supplied_count`, `unit_supplied_count`
- `pharma.supply.fact_research_capacity`: `research_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `employee_group_id`, `therapy_area_id`, `scientist_count`, `research_program_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (1) — Eli Lilly

For Eli Lilly, Which ex-U.S. accelerated pathways could allow an orforglipron launch in 2026, similar to a U.S. pathway already obtained?

- `pharma.supply.fact_regulatory_progress`: `regulatory_progress_record_id`, `fiscal_quarter_id`, `scenario_id`, `regulatory_pathway_id`, `geography_id`, `product_id`, `clinical_phase_id`, `filing_count`, `approval_count`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_incretin_demand`: `incretin_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `payer_channel_id`, `patient_segment_id`, `geography_id`, `incretin_patient_count`, `incretin_prescription_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (1) — Eli Lilly

For Eli Lilly, Is a priority-review voucher being sought, and what are the launch-timing puts and takes if it is not?

- `pharma.supply.fact_batch_output`: `batch_output_record_id`, `fiscal_quarter_id`, `scenario_id`, `manufacturing_site_id`, `therapy_area_id`, `completed_batch_count`
- `pharma.price.fact_net_price`: `net_price_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `payer_channel_id`, `dosage_form_id`, `net_price_per_unit_amount`, `list_price_per_unit_amount`
- `pharma.price.fact_gross_margin`: `gross_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `product_id`, `gross_profit_amount`, `gross_margin_percent`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (6) — Merck

For Merck, Is the higher dose only for patients who need escalation after 40 mg, and are combinations being studied?

- `pharma.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `manufacturing_site_id`, `dosage_form_id`, `therapy_area_id`, `dose_capacity_count`, `batch_capacity_count`, `utilized_batch_count`
- `pharma.supply.fact_supply_output`: `supply_output_record_id`, `fiscal_quarter_id`, `scenario_id`, `manufacturing_site_id`, `product_id`, `dosage_form_id`, `dose_supplied_count`, `unit_supplied_count`
- `pharma.supply.fact_research_capacity`: `research_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `employee_group_id`, `therapy_area_id`, `scientist_count`, `research_program_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (3) — Merck

For Merck, How long is the Keytruda intellectual-property runway, and how fast must QLEX ramp before an intravenous biosimilar arrives?

- `pharma.supply.fact_patent_runway`: `patent_runway_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `geography_id`, `exclusivity_month_count`
- `pharma.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `manufacturing_site_id`, `dosage_form_id`, `therapy_area_id`, `dose_capacity_count`, `batch_capacity_count`, `utilized_batch_count`
- `pharma.supply.fact_supply_output`: `supply_output_record_id`, `fiscal_quarter_id`, `scenario_id`, `manufacturing_site_id`, `product_id`, `dosage_form_id`, `dose_supplied_count`, `unit_supplied_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
