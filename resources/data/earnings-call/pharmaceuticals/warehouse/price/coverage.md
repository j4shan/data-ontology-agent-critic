# Pharma Inc price slice

This slice is part of the Pharma Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q2 2026 (3) — Eli Lilly

For Eli Lilly, What milestones are required for a biologics-license path, and is that unique to retatrutide or available to later incretins?

- `pharma.price.fact_business_development`: `business_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `deal_value_amount`, `milestone_payment_amount`
- `pharma.price.fact_alliance_revenue`: `alliance_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `revenue_line_id`, `geography_id`, `alliance_revenue_amount`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (8) — Eli Lilly

For Eli Lilly, How sustainable is the favorability in rebates now that CVS is back on formulary?

- `pharma.price.fact_gross_to_net`: `gross_to_net_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `payer_channel_id`, `gross_sales_amount`, `rebate_amount`, `net_sales_amount`
- `pharma.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `geography_id`, `revenue_line_id`, `product_sales_amount`
- `pharma.price.fact_incretin_revenue`: `incretin_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `payer_channel_id`, `geography_id`, `incretin_sales_amount`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (9) — Eli Lilly

For Eli Lilly, Can psychiatry and vaccines be scaled, or are those assets one-off science bets?

- `pharma.price.fact_business_development`: `business_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `deal_value_amount`, `milestone_payment_amount`
- `pharma.price.fact_alliance_revenue`: `alliance_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `revenue_line_id`, `geography_id`, `alliance_revenue_amount`
- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (4) — Eli Lilly

For Eli Lilly, How will Medicare patients be activated, is that a fourth-quarter or 2027 effect, and how does the price point affect persistence?

- `pharma.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `geography_id`, `revenue_line_id`, `product_sales_amount`
- `pharma.price.fact_oncology_revenue`: `oncology_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `oncology_sales_amount`
- `pharma.price.fact_enterprise_results`: `enterprise_results_record_id`, `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`, `operating_income_amount`, `net_income_amount`, `diluted_earnings_per_share`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (6) — Eli Lilly

For Eli Lilly, After about 15,000 patients started, does the launch curve still match the frame, and how much of the raised guidance is Foundayo versus Mounjaro and Zepbound?

- `pharma.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `geography_id`, `revenue_line_id`, `product_sales_amount`
- `pharma.price.fact_oncology_revenue`: `oncology_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `indication_id`, `geography_id`, `oncology_sales_amount`
- `pharma.price.fact_other_product_revenue`: `other_product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `geography_id`, `other_product_sales_amount`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (4) — Eli Lilly

For Eli Lilly, What Medicare volume ramp is embedded in the back half, how that sets the revenue range, and whether it pulls more employers into commercial coverage?

- `pharma.price.fact_alliance_revenue`: `alliance_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `revenue_line_id`, `geography_id`, `alliance_revenue_amount`
- `pharma.supply.fact_regulatory_progress`: `regulatory_progress_record_id`, `fiscal_quarter_id`, `scenario_id`, `regulatory_pathway_id`, `geography_id`, `product_id`, `clinical_phase_id`, `filing_count`, `approval_count`
- `pharma.supply.fact_patent_runway`: `patent_runway_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `geography_id`, `exclusivity_month_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (6) — Eli Lilly

For Eli Lilly, What is the contracting environment across the incretin portfolio, and how elastic is cash-channel pricing through the year?

- `pharma.price.fact_incretin_revenue`: `incretin_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `payer_channel_id`, `geography_id`, `incretin_sales_amount`
- `pharma.price.fact_gross_to_net`: `gross_to_net_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `payer_channel_id`, `gross_sales_amount`, `rebate_amount`, `net_sales_amount`
- `pharma.price.fact_net_price`: `net_price_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `payer_channel_id`, `dosage_form_id`, `net_price_per_unit_amount`, `list_price_per_unit_amount`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (3) — Eli Lilly

For Eli Lilly, Do the new access structures create more gross-to-net pressure than ordinary rebates, and do they make clinical profile matter more for positioning?

- `pharma.price.fact_gross_to_net`: `gross_to_net_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `payer_channel_id`, `gross_sales_amount`, `rebate_amount`, `net_sales_amount`
- `pharma.price.fact_net_price`: `net_price_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `payer_channel_id`, `dosage_form_id`, `net_price_per_unit_amount`, `list_price_per_unit_amount`
- `pharma.price.fact_gross_margin`: `gross_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `product_id`, `gross_profit_amount`, `gross_margin_percent`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (4) — Merck

For Merck, Where are the largest portfolio gaps that business development could fill, and what deal size is the sweet spot?

- `pharma.price.fact_business_development`: `business_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `deal_value_amount`, `milestone_payment_amount`
- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (2) — Merck

For Merck, Are there plans to study the antibody-drug conjugate in first-line and in PD-L1-low patients, including head-to-head against KEYNOTE-189?

- `pharma.price.fact_operating_expense`: `operating_expense_record_id`, `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `therapy_area_id`, `operating_expense_amount`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.fact_clinical_development`: `clinical_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `clinical_phase_id`, `product_id`, `pipeline_asset_count`, `trial_participant_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (4) — Merck

For Merck, What share of Keytruda sales is now early-stage, and which of the approved tumor types drive that?

- `pharma.price.fact_contract_revenue`: `contract_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `product_id`, `contract_net_sales_amount`
- `pharma.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `geography_id`, `revenue_line_id`, `product_sales_amount`
- `pharma.price.fact_incretin_revenue`: `incretin_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `payer_channel_id`, `geography_id`, `incretin_sales_amount`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (5) — Merck

For Merck, Are the recent administration deals with other drugmakers a reasonable framework for the industry, including Merck?

- `pharma.price.fact_business_development`: `business_development_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `indication_id`, `deal_value_amount`, `milestone_payment_amount`
- `pharma.price.fact_other_product_revenue`: `other_product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `therapy_area_id`, `geography_id`, `other_product_sales_amount`
- `pharma.demand.fact_product_demand`: `product_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `indication_id`, `geography_id`, `patient_segment_id`, `patient_count`, `prescription_count`, `new_patient_start_count`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (7) — Merck

For Merck, What are the 2026 pushes and pulls on the top line, alongside the expense comments already given?

- `pharma.price.fact_operating_expense`: `operating_expense_record_id`, `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `therapy_area_id`, `operating_expense_amount`
- `pharma.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `therapy_area_id`, `geography_id`, `revenue_line_id`, `product_sales_amount`
- `pharma.price.fact_net_price`: `net_price_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_id`, `payer_channel_id`, `dosage_form_id`, `net_price_per_unit_amount`, `list_price_per_unit_amount`
- `pharma.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `pharma.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
