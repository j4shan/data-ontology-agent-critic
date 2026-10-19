# Defense Inc supply slice

This slice is part of the Defense Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q3 2025 (12) — Lockheed Martin

Are prices for later phases of the classified aeronautics program locked in with suppliers?

- `defense.supply.fact_production_capacity`: `production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `facility_type_id`, `capacity_unit_quantity`, `produced_unit_quantity`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.dim_lmt_program`: `lmt_program_id`, `lmt_program_code`, `lmt_program_name`, `lmt_segment_id`

### Q4 2025 (2) — RTX

Where would government support for capacity spending change the portfolio or the programs that get investment?

- `defense.supply.fact_production_capacity`: `production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `facility_type_id`, `capacity_unit_quantity`, `produced_unit_quantity`
- `defense.supply.fact_rtx_production_capacity`: `rtx_production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `facility_type_id`, `capacity_unit_quantity`
- `defense.price.fact_capital_spending`: `capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `investment_type_id`, `capital_spending_amount`
- `defense.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `defense.demand.dim_customer_country_type`: `customer_country_type_id`, `customer_country_type_code`, `customer_country_type_name`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
