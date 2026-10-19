# Defense Inc demand slice

This slice is part of the Defense Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q1 2026 (1) — Lockheed Martin

Where does the F-35 program stand in production and sustainment given a higher aircraft request and added sustainment funding?

- `defense.demand.fact_sustainment_volume`: `sustainment_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `delivery_stream_id`, `supported_aircraft_quantity`, `flight_hour_quantity`
- `defense.supply.fact_production_capacity`: `production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `facility_type_id`, `capacity_unit_quantity`, `produced_unit_quantity`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.demand.fact_program_volume`: `program_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `customer_country_type_id`, `aircraft_quantity`, `missile_quantity`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.supply.fact_sustainment_capacity`: `sustainment_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `aircraft_platform_id`, `depot_induction_quantity`

### Q1 2026 (4) — Lockheed Martin

Can the classified missile program at Missiles and Fire Control be accelerated in a way that improves program economics, similar to other production deals in the industry?

- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.fact_program_volume`: `program_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `customer_country_type_id`, `aircraft_quantity`, `missile_quantity`
- `defense.supply.fact_production_capacity`: `production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `facility_type_id`, `capacity_unit_quantity`, `produced_unit_quantity`
- `defense.supply.fact_missile_ramp_capacity`: `missile_ramp_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `component_type_id`, `contracted_rate_quantity`, `demonstrated_rate_quantity`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`

### Q1 2026 (6) — Lockheed Martin

What pinch points limit a faster missile-capacity ramp, including solid rocket motors, and can more spending pull volume forward?

- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.supply.fact_missile_ramp_capacity`: `missile_ramp_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `component_type_id`, `contracted_rate_quantity`, `demonstrated_rate_quantity`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.fact_program_volume`: `program_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `customer_country_type_id`, `aircraft_quantity`, `missile_quantity`
- `defense.demand.fact_campaign_pipeline_volume`: `campaign_pipeline_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `campaign_stage_id`, `region_id`, `technology_area_id`, `campaign_unit_quantity`

### Q3 2025 (3) — Lockheed Martin

How confident is the supply chain, including solid rocket motors, in supporting a multi-year missile ramp?

- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.supply.fact_missile_ramp_capacity`: `missile_ramp_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `component_type_id`, `contracted_rate_quantity`, `demonstrated_rate_quantity`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.demand.fact_program_volume`: `program_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `customer_country_type_id`, `aircraft_quantity`, `missile_quantity`

### Q3 2025 (5) — Lockheed Martin

Is the lower Rotary and Mission Systems outlook mostly CH-53K volume or Black Hawk volume?

- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.demand.dim_lmt_program`: `lmt_program_id`, `lmt_program_code`, `lmt_program_name`, `lmt_segment_id`
- `defense.demand.dim_customer_country_type`: `customer_country_type_id`, `customer_country_type_code`, `customer_country_type_name`
- `defense.demand.fact_program_volume`: `program_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `customer_country_type_id`, `aircraft_quantity`, `missile_quantity`

### Q2 2025 (5) — Lockheed Martin

How large is the Golden Dome opportunity, and when would it show up in backlog?

- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_lmt_segment_revenue`: `lmt_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_revenue_amount`
- `defense.price.fact_backlog_amount_fact`: `backlog_amount_fact_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_amount`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`

### Q2 2026 (1) — RTX

Where do the defense framework agreements stand?

- `defense.demand.dim_rtx_franchise`: `rtx_franchise_id`, `rtx_franchise_code`, `rtx_franchise_name`, `rtx_segment_id`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_framework_volume`: `framework_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `framework_unit_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.supply.fact_rtx_production_capacity`: `rtx_production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `facility_type_id`, `capacity_unit_quantity`
- `defense.price.fact_rtx_segment_revenue`: `rtx_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `service_stream_id`, `segment_revenue_amount`

### Q2 2026 (2) — RTX

How should Pratt aftermarket, military, and original-equipment growth contribute for the rest of the year, and what is pushing original equipment down?

- `defense.demand.dim_service_stream`: `service_stream_id`, `service_stream_code`, `service_stream_name`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`

### Q2 2026 (4) — RTX

How durable is shop-visit demand for the PW4000 and V2500 given current utilization and customer conversations?

- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.demand.fact_shop_visit_volume`: `shop_visit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `engine_family_id`, `service_stream_id`, `shop_visit_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.price.fact_engine_revenue_rate`: `engine_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `engine_family_id`, `revenue_per_shop_visit`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.dim_customer_country_type`: `customer_country_type_id`, `customer_country_type_code`, `customer_country_type_name`

### Q2 2026 (7) — RTX

On a future Airbus aircraft, is the ask a risk-sharing role on engines or a royalty on aftermarket in exchange for a higher equipment price?

- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.demand.fact_program_volume`: `program_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `customer_country_type_id`, `aircraft_quantity`, `missile_quantity`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.supply.fact_production_capacity`: `production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `facility_type_id`, `capacity_unit_quantity`, `produced_unit_quantity`

### Q2 2026 (8) — RTX

With export demand, Golden Dome, and additional orders stacked on interceptor demand, how much further can production rates rise under the frameworks?

- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.supply.fact_rtx_production_capacity`: `rtx_production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `facility_type_id`, `capacity_unit_quantity`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`

### Q1 2026 (1) — RTX

Can the supply chain, including rare earths, keep up with missile demand?

- `defense.demand.fact_program_volume`: `program_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `customer_country_type_id`, `aircraft_quantity`, `missile_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.demand.fact_missile_type_volume`: `missile_type_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `missile_type_id`, `region_id`, `missile_type_quantity`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`

### Q1 2026 (3) — RTX

Is missile growth through 2030 in line with a high-teens rate, and what does the sensor business add as Andover expands?

- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.supply.fact_missile_ramp_capacity`: `missile_ramp_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `component_type_id`, `contracted_rate_quantity`, `demonstrated_rate_quantity`
- `defense.price.fact_lmt_segment_margin`: `lmt_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`

### Q1 2026 (4) — RTX

What products address high-volume, low-cost drones rather than replenishing existing interceptors?

- `defense.demand.fact_program_volume`: `program_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `customer_country_type_id`, `aircraft_quantity`, `missile_quantity`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_framework_volume`: `framework_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `framework_unit_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.demand.fact_bookings_volume`: `bookings_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `contract_type_id`, `booked_unit_quantity`

### Q1 2026 (6) — RTX

How is Hot Section Plus priced now that it is off warranty, and are more approvals needed before it is offered on shop visits?

- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.price.fact_engine_revenue_rate`: `engine_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `engine_family_id`, `revenue_per_shop_visit`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.demand.fact_shop_visit_volume`: `shop_visit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `engine_family_id`, `service_stream_id`, `shop_visit_quantity`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`

### Q1 2026 (7) — RTX

How does the shift to the GTF Advantage change negative engine margin?

- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_enterprise_margin`: `enterprise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `defense.demand.dim_rtx_franchise`: `rtx_franchise_id`, `rtx_franchise_code`, `rtx_franchise_name`, `rtx_segment_id`

### Q1 2026 (9) — RTX

What year-end GTF aircraft-on-ground level is consistent with shop output and the earlier charge?

- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.price.fact_engine_revenue_rate`: `engine_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `engine_family_id`, `revenue_per_shop_visit`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`

### Q1 2026 (10) — RTX

How should commercial engine deliveries cadence through the second quarter and second half, and are higher input costs slowing the supply chain?

- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.demand.fact_shop_visit_volume`: `shop_visit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `engine_family_id`, `service_stream_id`, `shop_visit_quantity`

### Q1 2026 (11) — RTX

Where do engine negotiations with Airbus stand, and can Collins interiors support the coming wide-body ramp?

- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.demand.dim_rtx_franchise`: `rtx_franchise_id`, `rtx_franchise_code`, `rtx_franchise_name`, `rtx_segment_id`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`

### Q4 2025 (1) — RTX

What are the next milestones in year three of the GTF fleet-management plan?

- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.supply.fact_rtx_production_capacity`: `rtx_production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `facility_type_id`, `capacity_unit_quantity`
- `defense.price.fact_rtx_segment_revenue`: `rtx_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `service_stream_id`, `segment_revenue_amount`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_enterprise_revenue`: `enterprise_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`

### Q4 2025 (3) — RTX

Why does Pratt commercial aftermarket growth slow to high single digits in 2026 after a strong fourth quarter?

- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.price.fact_aftermarket_revenue`: `aftermarket_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `aftermarket_revenue_amount`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.supply.fact_production_capacity`: `production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `facility_type_id`, `capacity_unit_quantity`, `produced_unit_quantity`
- `defense.supply.fact_rtx_production_capacity`: `rtx_production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `facility_type_id`, `capacity_unit_quantity`
- `defense.price.fact_rtx_segment_revenue`: `rtx_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `service_stream_id`, `segment_revenue_amount`

### Q4 2025 (4) — RTX

How fast are the larger Raytheon businesses growing, beyond the effector businesses called out near 20%?

- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.supply.fact_rtx_production_capacity`: `rtx_production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `facility_type_id`, `capacity_unit_quantity`
- `defense.price.fact_rtx_segment_revenue`: `rtx_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `service_stream_id`, `segment_revenue_amount`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_enterprise_revenue`: `enterprise_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`

### Q4 2025 (5) — RTX

Which segment has the most room to exceed guidance given recent demand?

- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.price.fact_rtx_segment_revenue`: `rtx_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `service_stream_id`, `segment_revenue_amount`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `defense.demand.dim_rtx_segment`: `rtx_segment_id`, `rtx_segment_code`, `rtx_segment_name`
- `defense.demand.dim_rtx_franchise`: `rtx_franchise_id`, `rtx_franchise_code`, `rtx_franchise_name`, `rtx_segment_id`

### Q4 2025 (6) — RTX

What is the eventual Raytheon margin as volume rises and foreign backlog converts?

- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`

### Q3 2025 (1) — RTX

What sits under the higher aerospace original-equipment outlook, and how confident is delivery of LEAP engines against Airbus's full-year target?

- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.supply.fact_rtx_production_capacity`: `rtx_production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `facility_type_id`, `capacity_unit_quantity`
- `defense.supply.fact_engine_delivery_capacity`: `engine_delivery_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `aircraft_platform_id`, `engine_family_id`, `engine_capacity_quantity`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`

### Q3 2025 (2) — RTX

Does the full-year shop-output increase imply a steep fourth-quarter GTF maintenance ramp, and what limits Raytheon growth if demand is not the constraint?

- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.fact_shop_visit_volume`: `shop_visit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `engine_family_id`, `service_stream_id`, `shop_visit_quantity`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`

### Q3 2025 (4) — RTX

Did the GTF spare-engine ratio fall, or were spare engines discounted for customers hit by the powder-metal issue?

- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.supply.fact_rtx_production_capacity`: `rtx_production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `facility_type_id`, `capacity_unit_quantity`
- `defense.supply.fact_installed_base`: `installed_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `engine_family_id`, `installed_engine_quantity`, `in_service_aircraft_quantity`
- `defense.supply.fact_engine_delivery_capacity`: `engine_delivery_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `aircraft_platform_id`, `engine_family_id`, `engine_capacity_quantity`
- `defense.demand.dim_rtx_franchise`: `rtx_franchise_id`, `rtx_franchise_code`, `rtx_franchise_name`, `rtx_segment_id`

### Q3 2025 (6) — RTX

Has the timing of GTF compensation and the decline in aircraft on ground changed, and is the provision still enough?

- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `defense.price.fact_rtx_franchise_margin`: `rtx_franchise_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `franchise_operating_income_amount`, `franchise_margin_percent`
- `defense.price.fact_engine_revenue_rate`: `engine_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `engine_family_id`, `revenue_per_shop_visit`
- `defense.demand.fact_program_volume`: `program_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `customer_country_type_id`, `aircraft_quantity`, `missile_quantity`

### Q3 2025 (7) — RTX

Were weaker Collins incremental margins a tariff effect?

- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.supply.fact_production_capacity`: `production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `facility_type_id`, `capacity_unit_quantity`, `produced_unit_quantity`
- `defense.supply.fact_rtx_production_capacity`: `rtx_production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `facility_type_id`, `capacity_unit_quantity`
- `defense.price.fact_rtx_segment_revenue`: `rtx_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `service_stream_id`, `segment_revenue_amount`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`

### Q3 2025 (9) — RTX

Is GTF delivery growth still about the mid-teens for the year, which would require a very strong fourth quarter?

- `defense.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.supply.fact_production_capacity`: `production_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `facility_type_id`, `capacity_unit_quantity`, `produced_unit_quantity`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.price.fact_segment_price_rate`: `segment_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `revenue_per_flight_hour`
- `defense.demand.dim_delivery_stream`: `delivery_stream_id`, `delivery_stream_code`, `delivery_stream_name`

### Q3 2025 (10) — RTX

How visible are V2500 shop visits next year if retirements stay low, traffic growth is below the old trend, and many GTF aircraft return to service?

- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.demand.fact_shop_visit_volume`: `shop_visit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `engine_family_id`, `service_stream_id`, `shop_visit_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.demand.fact_rtx_delivery_volume`: `rtx_delivery_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `service_stream_id`, `engine_quantity`, `shipset_quantity`
- `defense.supply.fact_installed_base`: `installed_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `engine_family_id`, `installed_engine_quantity`, `in_service_aircraft_quantity`
- `defense.price.fact_rtx_segment_revenue`: `rtx_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `service_stream_id`, `segment_revenue_amount`

### Q3 2025 (12) — RTX

What is inside the Collins aftermarket increase, including retrofits, and is spare-parts pricing seeing more customer pushback at Collins and Pratt?

- `defense.demand.fact_backlog_volume`: `backlog_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_unit_quantity`
- `defense.demand.fact_aftermarket_volume`: `aftermarket_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_franchise_id`, `region_id`, `aftermarket_unit_quantity`
- `defense.price.fact_backlog_amount_fact`: `backlog_amount_fact_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `customer_country_type_id`, `backlog_amount`
- `defense.price.fact_contract_price_rate`: `contract_price_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `lmt_program_id`, `contract_type_id`, `price_per_unit_amount`
- `defense.demand.dim_customer_country_type`: `customer_country_type_id`, `customer_country_type_code`, `customer_country_type_name`
- `defense.price.fact_rtx_segment_margin`: `rtx_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `rtx_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
