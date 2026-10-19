# Defense Inc price slice

This slice is part of the Defense Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q1 2026 (2) — Lockheed Martin

What risk comes with multiyear missile contracts that commit to much higher production rates in later years?

- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.demand.fact_program_volume`: `program_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `customer_country_type_id`, `aircraft_quantity`, `missile_quantity`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.demand.fact_campaign_pipeline_volume`: `campaign_pipeline_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `campaign_stage_id`, `region_id`, `technology_area_id`, `campaign_unit_quantity`
- `defense.supply.fact_production_capacity`: `production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `facility_type_id`, `capacity_unit_quantity`, `produced_unit_quantity`

### Q1 2026 (3) — Lockheed Martin

How is risk trending on the classified Aeronautics program, and is the customer willing to add funding to keep it on track?

- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.demand.dim_lmt_program`: `lmt_program_id`, `lmt_program_code`, `lmt_program_name`, `lmt_segment_id`
- `defense.demand.dim_customer_country_type`: `customer_country_type_id`, `customer_country_type_code`, `customer_country_type_name`
- `defense.demand.fact_program_volume`: `program_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `customer_country_type_id`, `aircraft_quantity`, `missile_quantity`

### Q1 2026 (5) — Lockheed Martin

Was the first-quarter working-capital use mostly the F-35, and how should cash flow cadence look in the second quarter versus the second half?

- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_cash_flow`: `cash_flow_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cash_flow_type_id`, `cash_flow_amount`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_working_capital`: `working_capital_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `working_capital_amount`, `receivable_amount`, `inventory_amount`
- `defense.price.fact_capital_spending`: `capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `investment_type_id`, `capital_spending_amount`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`

### Q1 2026 (7) — Lockheed Martin

Are AI tools for the enterprise and for weapon systems being built internally?

- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_enterprise_revenue`: `enterprise_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `defense.price.fact_enterprise_margin`: `enterprise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `defense.demand.dim_lmt_segment`: `lmt_segment_id`, `lmt_segment_code`, `lmt_segment_name`

### Q1 2026 (8) — Lockheed Martin

How are new defense entrants changing competition for talent and the way contracts are won?

- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.demand.dim_lmt_segment`: `lmt_segment_id`, `lmt_segment_code`, `lmt_segment_name`
- `defense.demand.dim_lmt_program`: `lmt_program_id`, `lmt_program_code`, `lmt_program_name`, `lmt_segment_id`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`

### Q4 2025 (1) — Lockheed Martin

What is the timing of multiyear deals for PAC-3 and THAAD, and how should Missiles and Fire Control margins evolve over the long term?

- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.demand.dim_lmt_segment`: `lmt_segment_id`, `lmt_segment_code`, `lmt_segment_name`

### Q4 2025 (2) — Lockheed Martin

Where is the company still ahead on disruptive technology, and where are newer entrants ahead?

- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_research_spending`: `research_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `technology_area_id`, `research_amount`
- `defense.price.fact_engine_revenue_rate`: `engine_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `engine_family_id`, `revenue_per_shop_visit`

### Q4 2025 (3) — Lockheed Martin

How durable are the PAC-3 and THAAD growth plans if appropriations remain annual and funding has been uneven in past cycles?

- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_enterprise_revenue`: `enterprise_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `defense.price.fact_enterprise_margin`: `enterprise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`

### Q4 2025 (4) — Lockheed Martin

What changed in the opportunity set to justify higher research and development and capital spending as a share of sales?

- `defense.price.fact_research_spending`: `research_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `technology_area_id`, `research_amount`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_capital_spending`: `capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `investment_type_id`, `capital_spending_amount`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`

### Q4 2025 (5) — Lockheed Martin

What does the strategic investment in F-35 sustainment cover, and what outcome is expected?

- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_capital_spending`: `capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `investment_type_id`, `capital_spending_amount`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.demand.fact_sustainment_volume`: `sustainment_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `delivery_stream_id`, `supported_aircraft_quantity`, `flight_hour_quantity`

### Q4 2025 (6) — Lockheed Martin

How are the PAC-3 and THAAD frameworks split between performance opportunity and risk?

- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.dim_lmt_segment`: `lmt_segment_id`, `lmt_segment_code`, `lmt_segment_name`
- `defense.demand.dim_lmt_program`: `lmt_program_id`, `lmt_program_code`, `lmt_program_name`, `lmt_segment_id`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`

### Q4 2025 (7) — Lockheed Martin

With double-digit growth likely at Missiles and Fire Control, how should the company growth and margin model, and the ranking of segments, change?

- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_enterprise_margin`: `enterprise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_enterprise_revenue`: `enterprise_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `defense.price.fact_program_margin`: `program_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `program_operating_income_amount`, `program_margin_percent`

### Q3 2025 (1) — Lockheed Martin

After charges on fixed-price development work in missiles, aeronautics, and helicopters, what makes those issues less likely to recur?

- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.demand.fact_program_volume`: `program_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `customer_country_type_id`, `aircraft_quantity`, `missile_quantity`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_research_spending`: `research_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `technology_area_id`, `research_amount`
- `defense.price.fact_program_charges`: `program_charges_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `program_charge_amount`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`

### Q3 2025 (2) — Lockheed Martin

Does backlog growth support mid-single-digit growth next year, and what mix, margin, and cash-flow profile comes with it?

- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_program_margin`: `program_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `program_operating_income_amount`, `program_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`

### Q3 2025 (4) — Lockheed Martin

How much revenue growth should a step-up in capital spending from the recent share of sales produce?

- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_capital_spending`: `capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `investment_type_id`, `capital_spending_amount`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_enterprise_revenue`: `enterprise_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `defense.supply.fact_production_capacity`: `production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `facility_type_id`, `capacity_unit_quantity`, `produced_unit_quantity`
- `defense.price.fact_rtx_segment_revenue`: `rtx_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `service_stream_id`, `segment_revenue_amount`

### Q3 2025 (6) — Lockheed Martin

What is the F-35 growth and margin outlook after the recent production and sustainment agreements, and what risk remains on Block 4?

- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.demand.dim_delivery_stream`: `delivery_stream_id`, `delivery_stream_code`, `delivery_stream_name`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`

### Q3 2025 (7) — Lockheed Martin

What is driving the low Space margin implied for the fourth quarter?

- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_enterprise_margin`: `enterprise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`

### Q3 2025 (8) — Lockheed Martin

How should margins on the latest F-35 lots compare with prior lots if price rose by less than inflation?

- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_cash_flow`: `cash_flow_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cash_flow_type_id`, `cash_flow_amount`
- `defense.price.fact_capital_spending`: `capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `investment_type_id`, `capital_spending_amount`
- `defense.price.fact_operating_expense`: `operating_expense_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cost_bucket_id`, `operating_expense_amount`

### Q3 2025 (9) — Lockheed Martin

Which larger international campaigns are active across the segments?

- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `defense.demand.dim_lmt_segment`: `lmt_segment_id`, `lmt_segment_code`, `lmt_segment_name`
- `defense.demand.dim_lmt_program`: `lmt_program_id`, `lmt_program_code`, `lmt_program_name`, `lmt_segment_id`
- `defense.demand.dim_customer_country_type`: `customer_country_type_id`, `customer_country_type_code`, `customer_country_type_name`

### Q3 2025 (10) — Lockheed Martin

Does a structural step-up in capital spending or independent research change the long-term investment ratios?

- `defense.price.fact_capital_spending`: `capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `investment_type_id`, `capital_spending_amount`
- `defense.supply.fact_production_capacity`: `production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `facility_type_id`, `capacity_unit_quantity`, `produced_unit_quantity`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_research_spending`: `research_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `technology_area_id`, `research_amount`
- `defense.price.fact_pension_adjustment`: `pension_adjustment_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `adjustment_amount`

### Q3 2025 (11) — Lockheed Martin

Is the soft fourth-quarter margin at the missile business the classified program, despite growth in core programs?

- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_enterprise_margin`: `enterprise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `defense.demand.fact_program_volume`: `program_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `customer_country_type_id`, `aircraft_quantity`, `missile_quantity`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.supply.fact_missile_ramp_capacity`: `missile_ramp_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `component_type_id`, `contracted_rate_quantity`, `demonstrated_rate_quantity`

### Q3 2025 (13) — Lockheed Martin

How large is the Golden Dome opportunity relative to the initial funding and the company's existing systems?

- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (1) — Lockheed Martin

What is different now in the review of the classified aeronautics program versus the prior quarter's process?

- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_segment_price_rate`: `segment_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `revenue_per_flight_hour`
- `defense.demand.fact_program_volume`: `program_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `customer_country_type_id`, `aircraft_quantity`, `missile_quantity`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`

### Q2 2025 (2) — Lockheed Martin

How do the program charges flow through to cash?

- `defense.price.fact_cash_flow`: `cash_flow_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cash_flow_type_id`, `cash_flow_amount`
- `defense.demand.dim_lmt_program`: `lmt_program_id`, `lmt_program_code`, `lmt_program_name`, `lmt_segment_id`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_program_charges`: `program_charges_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `program_charge_amount`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`

### Q2 2025 (3) — Lockheed Martin

Why does the budget request fewer F-35s, and how easily can international customers fill any relinquished U.S. slots?

- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.demand.dim_lmt_segment`: `lmt_segment_id`, `lmt_segment_code`, `lmt_segment_name`
- `defense.demand.dim_lmt_program`: `lmt_program_id`, `lmt_program_code`, `lmt_program_name`, `lmt_segment_id`
- `defense.demand.dim_customer_country_type`: `customer_country_type_id`, `customer_country_type_code`, `customer_country_type_name`

### Q2 2025 (4) — Lockheed Martin

Are the updated second-half margins in helicopters, aeronautics, and the company overall the run rate going forward, or do they step up next year?

- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_enterprise_margin`: `enterprise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `defense.price.fact_program_margin`: `program_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `program_operating_income_amount`, `program_margin_percent`

### Q2 2025 (6) — Lockheed Martin

Given F-35's role in recent operations, how should funding uncertainty on the next lots be read against earlier unit cuts?

- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.price.fact_enterprise_revenue`: `enterprise_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `defense.price.fact_enterprise_margin`: `enterprise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `defense.price.fact_cash_flow`: `cash_flow_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cash_flow_type_id`, `cash_flow_amount`

### Q2 2026 (3) — RTX

How far can Raytheon margins go over the next few years as productivity, foreign versus domestic mix, and mature versus newer programs shift?

- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`

### Q2 2026 (5) — RTX

Are more on-wing engines planned for Airbus this year than at the start of the year, and what is the Collins original-equipment outlook?

- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.supply.fact_rtx_production_capacity`: `rtx_production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `facility_type_id`, `capacity_unit_quantity`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`

### Q2 2026 (6) — RTX

Why is the Collins margin rate not rising with the higher original-equipment sales, and what is the pace of the remaining margin opportunity?

- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_enterprise_margin`: `enterprise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `defense.price.fact_program_margin`: `program_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `program_operating_income_amount`, `program_margin_percent`

### Q1 2026 (2) — RTX

How do framework agreements treat the capital already spent, and can mix shift long-term margins?

- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.price.fact_capital_spending`: `capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `investment_type_id`, `capital_spending_amount`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`

### Q1 2026 (5) — RTX

How are the newer metal tariffs and the trade ruling showing up so far?

- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`

### Q1 2026 (8) — RTX

Why does Collins margin guidance imply a flat-to-down rest of year versus the first quarter, against the usual seasonal pattern?

- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_enterprise_margin`: `enterprise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`

### Q4 2025 (7) — RTX

How should longer-term Pratt margin be read as V2500 work scope and life extensions help now, but aircraft on ground later return to service?

- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.supply.fact_installed_base`: `installed_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `engine_family_id`, `installed_engine_quantity`, `in_service_aircraft_quantity`

### Q4 2025 (8) — RTX

How much of the constraint on higher production sits deeper in the supply chain rather than at the prime?

- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.supply.fact_rtx_production_capacity`: `rtx_production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `facility_type_id`, `capacity_unit_quantity`
- `defense.price.fact_enterprise_revenue`: `enterprise_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `defense.price.fact_enterprise_margin`: `enterprise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `defense.price.fact_cash_flow`: `cash_flow_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cash_flow_type_id`, `cash_flow_amount`
- `defense.price.fact_capital_spending`: `capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `investment_type_id`, `capital_spending_amount`

### Q3 2025 (3) — RTX

How should Raytheon margin expansion hold up as growth accelerates and international mix rises?

- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_program_margin`: `program_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `program_operating_income_amount`, `program_margin_percent`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`

### Q3 2025 (5) — RTX

What is the current 737 MAX and 787 production rate, and how do incremental margins on those programs feed the Collins margin?

- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_enterprise_margin`: `enterprise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `defense.price.fact_program_margin`: `program_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `program_operating_income_amount`, `program_margin_percent`

### Q3 2025 (8) — RTX

Is the higher Pratt commercial original-equipment outlook mix from GTF Advantage and spares, and how does that hit profit given negative engine margin?

- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_enterprise_margin`: `enterprise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`

### Q3 2025 (11) — RTX

With Raytheon margin above the prior 12% marker, is that the destination given volume, international mix, and mature fixed-price work?

- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.demand.dim_customer_country_type`: `customer_country_type_id`, `customer_country_type_code`, `customer_country_type_name`

### Q3 2025 (13) — RTX

What are the main pieces of the 2026 cash-conversion bridge?

- `defense.price.fact_cash_flow`: `cash_flow_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cash_flow_type_id`, `cash_flow_amount`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.supply.fact_rtx_production_capacity`: `rtx_production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `facility_type_id`, `capacity_unit_quantity`
- `defense.price.fact_rtx_segment_revenue`: `rtx_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `service_stream_id`, `segment_revenue_amount`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
