# Railroad Inc price slice

This slice is part of the Railroad Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q1 2026 (1) — CSX

For CSX, What offsets the operating-ratio hit from higher fuel so the full-year ratio can still be held, with a bias to the high end?

- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.price.fact_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `productivity_initiative_id`, `cost_bucket_id`, `productivity_savings_amount`
- `railroad.price.dim_fuel_type`: `fuel_type_id`, `fuel_type_code`, `fuel_type_name`
- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (3) — CSX

For CSX, Is the first-quarter improvement in purchased services and other the run rate, or is there more to take out?

- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.price.fact_accessorial_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `price_program_id`, `accessorial_revenue_amount`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.price.fact_fuel`: `fiscal_quarter_id`, `scenario_id`, `fuel_type_id`, `service_type_id`, `fuel_gallon_quantity`, `fuel_expense_amount`, `fuel_price_per_gallon`, `fuel_surcharge_revenue_amount`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (4) — CSX

For CSX, Is the real-estate gain the expected run rate, and does it recur in the back half?

- `railroad.price.fact_other_income`: `fiscal_quarter_id`, `scenario_id`, `income_type_id`, `other_income_amount`, `real_estate_gain_amount`
- `railroad.price.dim_income_type`: `income_type_id`, `income_type_code`, `income_type_name`
- `railroad.price.fact_accessorial_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `price_program_id`, `accessorial_revenue_amount`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.price.fact_truck_rate`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `competitor_id`, `truck_spot_rate_per_load`, `truck_contract_rate_per_load`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (5) — CSX

For CSX, Is a higher return on capital mainly asset productivity, mix and price, or cost efficiency?

- `railroad.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `asset_category_id`, `division_id`, `capital_spending_amount`
- `railroad.price.fact_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `productivity_initiative_id`, `cost_bucket_id`, `productivity_savings_amount`
- `railroad.price.fact_return_on_capital`: `fiscal_quarter_id`, `scenario_id`, `return_on_capital_percent`, `invested_capital_amount`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_infrastructure_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `infrastructure_project_id`, `project_capital_spending_amount`
- `railroad.price.fact_labor_expense`: `fiscal_quarter_id`, `scenario_id`, `workforce_group_id`, `cost_bucket_id`, `labor_expense_amount`, `compensation_per_employee`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (6) — CSX

For CSX, How long is the lag before a tighter truck spot and contract market shows up in intermodal or merchandise price, and can any of it help in the second half?

- `railroad.price.fact_truck_rate`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `competitor_id`, `truck_spot_rate_per_load`, `truck_contract_rate_per_load`
- `railroad.price.dim_price_program`: `price_program_id`, `price_program_code`, `price_program_name`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (8) — CSX

For CSX, Is the sequential coal yield improvement an easing of index headwinds or a mix benefit?

- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.fact_fuel`: `fiscal_quarter_id`, `scenario_id`, `fuel_type_id`, `service_type_id`, `fuel_gallon_quantity`, `fuel_expense_amount`, `fuel_price_per_gallon`, `fuel_surcharge_revenue_amount`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.price.fact_accessorial_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `price_program_id`, `accessorial_revenue_amount`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (9) — CSX

For CSX, Besides the bridges that enable double-stack and the Chicago flow changes, what else this year improves productivity and margins?

- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.price.fact_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `productivity_initiative_id`, `cost_bucket_id`, `productivity_savings_amount`
- `railroad.demand.dim_metro`: `metro_id`, `metro_code`, `metro_name`, `state_id`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (10) — CSX

For CSX, How much of the flat volume outlook is project growth offset by macro pressure?

- `railroad.demand.fact_project_volume`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `commodity_id`, `region_id`, `project_carload_quantity`, `ramp_carload_quantity`
- `railroad.demand.dim_project`: `project_id`, `project_name`, `region_id`, `commodity_id`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_contracted_volume`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `shipper_id`, `commodity_id`, `contracted_carload_quantity`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_interchange_volume`: `fiscal_quarter_id`, `scenario_id`, `interchange_id`, `service_type_id`, `competitor_id`, `interchanged_carload_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (11) — CSX

For CSX, What is the size and timing of the cost headwinds, including incentive pay, and which productivity actions are aimed at 2027 rather than this year?

- `railroad.price.fact_labor_expense`: `fiscal_quarter_id`, `scenario_id`, `workforce_group_id`, `cost_bucket_id`, `labor_expense_amount`, `compensation_per_employee`
- `railroad.price.fact_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `productivity_initiative_id`, `cost_bucket_id`, `productivity_savings_amount`
- `railroad.supply.dim_productivity_initiative`: `productivity_initiative_id`, `productivity_initiative_name`, `division_id`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (12) — CSX

For CSX, Is the revenue outlook more or less optimistic on volume, and how does it split between price and volume given current staffing?

- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.price.fact_accessorial_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `price_program_id`, `accessorial_revenue_amount`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.price.fact_fuel`: `fiscal_quarter_id`, `scenario_id`, `fuel_type_id`, `service_type_id`, `fuel_gallon_quantity`, `fuel_expense_amount`, `fuel_price_per_gallon`, `fuel_surcharge_revenue_amount`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (1) — CSX

For CSX, How should the price-cost spread be thought about, separate from the base operating ratio?

- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.price.fact_labor_expense`: `fiscal_quarter_id`, `scenario_id`, `workforce_group_id`, `cost_bucket_id`, `labor_expense_amount`, `compensation_per_employee`
- `railroad.price.fact_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `productivity_initiative_id`, `cost_bucket_id`, `productivity_savings_amount`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (2) — CSX

For CSX, How much of the operating-ratio improvement is items already known to roll off, and what inflation is inside the guide?

- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`

### Q4 2025 (3) — CSX

For CSX, How does low-single-digit revenue growth split between volume and yield, and what longer-term operating ratio is realistic?

- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (6) — CSX

For CSX, What dollar buckets and headcount targets sit inside the savings programs?

- `railroad.price.fact_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `productivity_initiative_id`, `cost_bucket_id`, `productivity_savings_amount`
- `railroad.price.fact_labor_expense`: `fiscal_quarter_id`, `scenario_id`, `workforce_group_id`, `cost_bucket_id`, `labor_expense_amount`, `compensation_per_employee`
- `railroad.supply.dim_productivity_initiative`: `productivity_initiative_id`, `productivity_initiative_name`, `division_id`
- `railroad.supply.dim_workforce_group`: `workforce_group_id`, `workforce_group_code`, `workforce_group_name`
- `railroad.supply.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `workforce_group_id`, `division_id`, `employee_quantity`, `trainee_quantity`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (8) — CSX

For CSX, What is driving coal revenue per unit, and what is assumed in the revenue outlook?

- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.fact_fuel`: `fiscal_quarter_id`, `scenario_id`, `fuel_type_id`, `service_type_id`, `fuel_gallon_quantity`, `fuel_expense_amount`, `fuel_price_per_gallon`, `fuel_surcharge_revenue_amount`
- `railroad.demand.fact_port_volume`: `fiscal_quarter_id`, `scenario_id`, `port_id`, `commodity_id`, `coal_grade_id`, `port_carload_quantity`, `port_ton_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (9) — CSX

For CSX, How long do natural-gas prices have to stay high before coal or other volumes respond?

- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.price.fact_accessorial_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `price_program_id`, `accessorial_revenue_amount`
- `railroad.price.fact_other_income`: `fiscal_quarter_id`, `scenario_id`, `income_type_id`, `other_income_amount`, `real_estate_gain_amount`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.demand.fact_port_volume`: `fiscal_quarter_id`, `scenario_id`, `port_id`, `commodity_id`, `coal_grade_id`, `port_carload_quantity`, `port_ton_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (10) — CSX

For CSX, Has anything in the business changed the long-term earnings framework once the macro is normal again?

- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `productivity_initiative_id`, `cost_bucket_id`, `productivity_savings_amount`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_project_volume`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `commodity_id`, `region_id`, `project_carload_quantity`, `ramp_carload_quantity`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.dim_fuel_type`: `fuel_type_id`, `fuel_type_code`, `fuel_type_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (12) — CSX

For CSX, Does low-single-digit revenue growth imply negative mix if price is in the usual range and volume grows?

- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.price.fact_accessorial_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `price_program_id`, `accessorial_revenue_amount`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.price.fact_fuel`: `fiscal_quarter_id`, `scenario_id`, `fuel_type_id`, `service_type_id`, `fuel_gallon_quantity`, `fuel_expense_amount`, `fuel_price_per_gallon`, `fuel_surcharge_revenue_amount`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (13) — CSX

For CSX, Is operating-ratio improvement spread through the year or weighted to the front or back?

- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.demand.dim_lane`: `lane_id`, `lane_name`, `origin_metro_name`, `destination_metro_name`, `interchange_id`
- `railroad.demand.fact_port_volume`: `fiscal_quarter_id`, `scenario_id`, `port_id`, `commodity_id`, `coal_grade_id`, `port_carload_quantity`, `port_ton_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (14) — CSX

For CSX, Of the guided operating-ratio improvement, how much is the identified cost savings versus other items?

- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.price.fact_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `productivity_initiative_id`, `cost_bucket_id`, `productivity_savings_amount`
- `railroad.price.fact_accessorial_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `price_program_id`, `accessorial_revenue_amount`
- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (4) — CSX

For CSX, Did costs improve as operating metrics improved through the quarter after a weak April?

- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.supply.fact_service_performance`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_dwell_hours`, `car_velocity_miles_per_day`, `trip_plan_compliance_percent`, `average_train_length_cars`
- `railroad.price.fact_accessorial_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `price_program_id`, `accessorial_revenue_amount`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (5) — CSX

For CSX, What is the sequential outlook for coal revenue per unit, and how much smaller are the benchmark and diesel headwinds in the second half versus the first?

- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_fuel`: `fiscal_quarter_id`, `scenario_id`, `fuel_type_id`, `service_type_id`, `fuel_gallon_quantity`, `fuel_expense_amount`, `fuel_price_per_gallon`, `fuel_surcharge_revenue_amount`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.supply.fact_locomotive_efficiency`: `fiscal_quarter_id`, `scenario_id`, `locomotive_type_id`, `division_id`, `gross_ton_miles_per_gallon`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (7) — CSX

For CSX, Why was the intermodal snapback slower than the air pocket, and can volumes accelerate from the quarter-to-date pace?

- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.demand.dim_commercial_channel`: `commercial_channel_id`, `commercial_channel_code`, `commercial_channel_name`
- `railroad.demand.dim_intermodal_trade`: `intermodal_trade_id`, `intermodal_trade_code`, `intermodal_trade_name`
- `railroad.demand.dim_service_type`: `service_type_id`, `service_type_code`, `service_type_name`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (8) — CSX

For CSX, Was there an upside surprise late in the quarter inside the other-revenue run rate?

- `railroad.price.fact_accessorial_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `price_program_id`, `accessorial_revenue_amount`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_fuel`: `fiscal_quarter_id`, `scenario_id`, `fuel_type_id`, `service_type_id`, `fuel_gallon_quantity`, `fuel_expense_amount`, `fuel_price_per_gallon`, `fuel_surcharge_revenue_amount`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (11) — CSX

For CSX, Does the stated cost of inconvenience capture the whole service penalty?

- `railroad.price.fact_accessorial_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `price_program_id`, `accessorial_revenue_amount`
- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (12) — CSX

For CSX, Can better service produce positive net price in the back half after mix and fuel absorbed price this quarter?

- `railroad.price.fact_fuel`: `fiscal_quarter_id`, `scenario_id`, `fuel_type_id`, `service_type_id`, `fuel_gallon_quantity`, `fuel_expense_amount`, `fuel_price_per_gallon`, `fuel_surcharge_revenue_amount`
- `railroad.price.dim_fuel_type`: `fuel_type_id`, `fuel_type_code`, `fuel_type_name`
- `railroad.price.fact_accessorial_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `price_program_id`, `accessorial_revenue_amount`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (13) — CSX

For CSX, Have customer conversations on railroad-specific projects increased or paused because of tariffs, and how large is the partnership ramp?

- `railroad.demand.fact_project_volume`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `commodity_id`, `region_id`, `project_carload_quantity`, `ramp_carload_quantity`
- `railroad.demand.dim_project`: `project_id`, `project_name`, `region_id`, `commodity_id`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_infrastructure_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `infrastructure_project_id`, `project_capital_spending_amount`
- `railroad.demand.dim_shipper`: `shipper_id`, `shipper_name`, `shipper_segment_id`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (1) — CSX

For CSX, How does price get back to a positive spread versus cost next year after labor inflation is already set?

- `railroad.price.fact_labor_expense`: `fiscal_quarter_id`, `scenario_id`, `workforce_group_id`, `cost_bucket_id`, `labor_expense_amount`, `compensation_per_employee`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.dim_price_program`: `price_program_id`, `price_program_code`, `price_program_name`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (2) — CSX

For CSX, How are next-year intermodal price talks progressing in a loose truck market, and can mix lift revenue growth above the low single digits?

- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_truck_rate`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `competitor_id`, `truck_spot_rate_per_load`, `truck_contract_rate_per_load`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.price.fact_accessorial_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `price_program_id`, `accessorial_revenue_amount`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (3) — CSX

For CSX, After fuel, coal, hurricane, and softer autos and metals, why is revenue down and the operating margin lower?

- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_fuel`: `fiscal_quarter_id`, `scenario_id`, `fuel_type_id`, `service_type_id`, `fuel_gallon_quantity`, `fuel_expense_amount`, `fuel_price_per_gallon`, `fuel_surcharge_revenue_amount`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (6) — CSX

For CSX, With little margin progress likely this year, what would have to change for margin to expand in the current environment?

- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_labor_expense`: `fiscal_quarter_id`, `scenario_id`, `workforce_group_id`, `cost_bucket_id`, `labor_expense_amount`, `compensation_per_employee`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (7) — CSX

For CSX, What categories did truck-to-rail wins fall into, and how is merchandise pricing holding up?

- `railroad.price.dim_price_program`: `price_program_id`, `price_program_code`, `price_program_name`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.fact_truck_rate`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `competitor_id`, `truck_spot_rate_per_load`, `truck_contract_rate_per_load`
- `railroad.demand.fact_truck_market_volume`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `competitor_id`, `truck_load_quantity`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.dim_fuel_type`: `fuel_type_id`, `fuel_type_code`, `fuel_type_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (8) — CSX

For CSX, Is the modest domestic-intermodal uptick enough to move intermodal yield, relative to international?

- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.dim_commercial_channel`: `commercial_channel_id`, `commercial_channel_code`, `commercial_channel_name`
- `railroad.demand.dim_intermodal_trade`: `intermodal_trade_id`, `intermodal_trade_code`, `intermodal_trade_name`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`

### Q3 2024 (11) — CSX

For CSX, Is better chemical pricing a healthy market or a quality mix shift?

- `railroad.price.dim_price_program`: `price_program_id`, `price_program_code`, `price_program_name`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_project_volume`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `commodity_id`, `region_id`, `project_carload_quantity`, `ramp_carload_quantity`
- `railroad.demand.fact_truck_market_volume`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `competitor_id`, `truck_load_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2024 (12) — CSX

For CSX, If freight that moved to the West Coast ahead of the port strike switches back, what happens to intermodal yields?

- `railroad.demand.dim_coast`: `coast_id`, `coast_code`, `coast_name`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.dim_commercial_channel`: `commercial_channel_id`, `commercial_channel_code`, `commercial_channel_name`
- `railroad.demand.dim_port`: `port_id`, `port_name`, `metro_id`, `coast_id`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (1) — Union Pacific

For Union Pacific, Can operating-ratio improvement continue if fuel and fuel-surcharge lag are a headwind, and where is incremental productivity showing up?

- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_fuel`: `fiscal_quarter_id`, `scenario_id`, `fuel_type_id`, `service_type_id`, `fuel_gallon_quantity`, `fuel_expense_amount`, `fuel_price_per_gallon`, `fuel_surcharge_revenue_amount`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.price.fact_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `productivity_initiative_id`, `cost_bucket_id`, `productivity_savings_amount`
- `railroad.supply.dim_productivity_initiative`: `productivity_initiative_id`, `productivity_initiative_name`, `division_id`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (8) — Union Pacific

For Union Pacific, Given current utilization, service, and inflation, what do incremental margins look like if volume turns up?

- `railroad.demand.fact_truck_market_volume`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `service_type_id`, `competitor_id`, `truck_load_quantity`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (1) — Union Pacific

For Union Pacific, If price is not the margin driver in 2026, how does faster inflation get covered?

- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.price.fact_labor_expense`: `fiscal_quarter_id`, `scenario_id`, `workforce_group_id`, `cost_bucket_id`, `labor_expense_amount`, `compensation_per_employee`
- `railroad.price.fact_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `productivity_initiative_id`, `cost_bucket_id`, `productivity_savings_amount`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (2) — Union Pacific

For Union Pacific, How variable is the gross traffic gain from the combination relative to the cost of handling that traffic?

- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.demand.fact_seasonal_volume`: `fiscal_quarter_id`, `scenario_id`, `peak_season_id`, `service_type_id`, `commodity_id`, `seasonal_carload_quantity`, `seasonal_revenue_ton_mile_quantity`
- `railroad.supply.fact_locomotive_efficiency`: `fiscal_quarter_id`, `scenario_id`, `locomotive_type_id`, `division_id`, `gross_ton_miles_per_gallon`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (5) — Union Pacific

For Union Pacific, With record train length and velocity, why wouldn't the operating ratio improve by more?

- `railroad.supply.fact_service_performance`: `fiscal_quarter_id`, `scenario_id`, `terminal_id`, `service_type_id`, `terminal_dwell_hours`, `car_velocity_miles_per_day`, `trip_plan_compliance_percent`, `average_train_length_cars`
- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (6) — Union Pacific

For Union Pacific, What volume and price are in the outlook, and how are customers absorbing new contracts in a soft demand environment?

- `railroad.demand.fact_contracted_volume`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `shipper_id`, `commodity_id`, `contracted_carload_quantity`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_project_volume`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `commodity_id`, `region_id`, `project_carload_quantity`, `ramp_carload_quantity`
- `railroad.price.dim_price_program`: `price_program_id`, `price_program_code`, `price_program_name`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (10) — Union Pacific

For Union Pacific, Does the compensation-per-employee increase include items that productivity, process, and technology are expected to offset?

- `railroad.price.fact_labor_expense`: `fiscal_quarter_id`, `scenario_id`, `workforce_group_id`, `cost_bucket_id`, `labor_expense_amount`, `compensation_per_employee`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.price.fact_fuel`: `fiscal_quarter_id`, `scenario_id`, `fuel_type_id`, `service_type_id`, `fuel_gallon_quantity`, `fuel_expense_amount`, `fuel_price_per_gallon`, `fuel_surcharge_revenue_amount`
- `railroad.price.fact_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `productivity_initiative_id`, `cost_bucket_id`, `productivity_savings_amount`
- `railroad.price.fact_truck_rate`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `competitor_id`, `truck_spot_rate_per_load`, `truck_contract_rate_per_load`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (2) — Union Pacific

For Union Pacific, What are the fourth-quarter operating-ratio puts and takes if volume is down mid-single digits?

- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (3) — Union Pacific

For Union Pacific, Does closer collaboration among competitors create a commercial risk during the review?

- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.demand.dim_commercial_channel`: `commercial_channel_id`, `commercial_channel_code`, `commercial_channel_name`
- `railroad.demand.dim_intermodal_trade`: `intermodal_trade_id`, `intermodal_trade_code`, `intermodal_trade_name`
- `railroad.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (4) — Union Pacific

For Union Pacific, With productivity challenged and the outlook showing more negatives than positives, how quickly can resources held for new business be adjusted?

- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_contracted_volume`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `shipper_id`, `commodity_id`, `contracted_carload_quantity`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_port_volume`: `fiscal_quarter_id`, `scenario_id`, `port_id`, `commodity_id`, `coal_grade_id`, `port_carload_quantity`, `port_ton_quantity`
- `railroad.demand.fact_project_volume`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `commodity_id`, `region_id`, `project_carload_quantity`, `ramp_carload_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (5) — Union Pacific

For Union Pacific, What mix sits inside the yield increase excluding fuel?

- `railroad.price.dim_fuel_type`: `fuel_type_id`, `fuel_type_code`, `fuel_type_name`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_fuel`: `fiscal_quarter_id`, `scenario_id`, `fuel_type_id`, `service_type_id`, `fuel_gallon_quantity`, `fuel_expense_amount`, `fuel_price_per_gallon`, `fuel_surcharge_revenue_amount`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `railroad.supply.fact_locomotive_efficiency`: `fiscal_quarter_id`, `scenario_id`, `locomotive_type_id`, `division_id`, `gross_ton_miles_per_gallon`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (8) — Union Pacific

For Union Pacific, If the truckload market inflects, how fast can domestic intermodal yields move, and what is the lag?

- `railroad.price.fact_truck_rate`: `fiscal_quarter_id`, `scenario_id`, `lane_id`, `competitor_id`, `truck_spot_rate_per_load`, `truck_contract_rate_per_load`
- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.price.fact_yield_rate`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `revenue_per_revenue_ton_mile`, `length_of_haul_miles`
- `railroad.price.dim_price_program`: `price_program_id`, `price_program_code`, `price_program_name`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.demand.dim_commercial_channel`: `commercial_channel_id`, `commercial_channel_code`, `commercial_channel_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (10) — Union Pacific

For Union Pacific, What macro deterioration, including housing, would change the volume outlook?

- `railroad.demand.dim_metro`: `metro_id`, `metro_code`, `metro_name`, `state_id`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_contracted_volume`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `shipper_id`, `commodity_id`, `contracted_carload_quantity`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_interchange_volume`: `fiscal_quarter_id`, `scenario_id`, `interchange_id`, `service_type_id`, `competitor_id`, `interchanged_carload_quantity`
- `railroad.demand.fact_port_volume`: `fiscal_quarter_id`, `scenario_id`, `port_id`, `commodity_id`, `coal_grade_id`, `port_carload_quantity`, `port_ton_quantity`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (11) — Union Pacific

For Union Pacific, What is driving the business wins in the fourth-quarter outlook, and can that pipeline grow volume next year despite trade uncertainty?

- `railroad.price.fact_freight_revenue`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `freight_revenue_amount`
- `railroad.demand.fact_bid_volume`: `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `lane_id`, `contract_type_id`, `bid_carload_quantity`, `awarded_carload_quantity`
- `railroad.demand.fact_contracted_volume`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `shipper_id`, `commodity_id`, `contracted_carload_quantity`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.price.dim_price_program`: `price_program_id`, `price_program_code`, `price_program_name`
- `railroad.price.fact_contract_rate`: `fiscal_quarter_id`, `scenario_id`, `contract_type_id`, `service_type_id`, `commodity_id`, `price_program_id`, `rate_per_carload`, `rate_per_revenue_ton_mile`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (3) — Union Pacific

For Union Pacific, How much further can the operating ratio move from the level already reached?

- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_enterprise_revenue`: `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.supply.dim_division`: `division_id`, `division_name`, `region_id`
- `railroad.supply.fact_locomotive_efficiency`: `fiscal_quarter_id`, `scenario_id`, `locomotive_type_id`, `division_id`, `gross_ton_miles_per_gallon`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (6) — Union Pacific

For Union Pacific, What second-half operating ratio and price/mix are expected, and how sustainable is coal strength beyond the contract win?

- `railroad.price.fact_operating_ratio`: `fiscal_quarter_id`, `scenario_id`, `operating_ratio_percent`, `operating_income_amount`
- `railroad.price.dim_cost_bucket`: `cost_bucket_id`, `cost_bucket_code`, `cost_bucket_name`
- `railroad.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `railroad.demand.fact_freight_volume`: `freight_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `commodity_id`, `coal_grade_id`, `intermodal_trade_id`, `commercial_channel_id`, `routing_id`, `handling_type_id`, `lane_id`, `shipper_id`, `carload_quantity`, `ton_quantity`, `revenue_ton_mile_quantity`, `gross_ton_mile_quantity`
- `railroad.demand.fact_project_volume`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `commodity_id`, `region_id`, `project_carload_quantity`, `ramp_carload_quantity`
- `railroad.price.dim_price_program`: `price_program_id`, `price_program_code`, `price_program_name`
- `railroad.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `railroad.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
