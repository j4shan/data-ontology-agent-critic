# Energy Inc demand slice

This slice is part of the Energy Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q2 2026 (1) — Chevron

For Chevron, What drove the sequential production increase at Tengiz, one of the main volume drivers?

- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.supply.dim_operator_affiliate`: `operator_affiliate_id`, `operator_affiliate_name`, `country_id`
- `energy.demand.fact_export_volume`: `fiscal_quarter_id`, `scenario_id`, `trade_route_id`, `hydrocarbon_id`, `market_id`, `export_quantity`
- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.price.fact_chemical_price`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_price_amount`
- `energy.price.fact_free_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (13) — Chevron

For Chevron, When receivables are repaid, do Venezuela terms shift to the new fiscal framework?

- `energy.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `energy.demand.fact_chemical_product_demand`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_product_demand_quantity`
- `energy.demand.fact_crude_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `hydrocarbon_id`, `crude_demand_quantity`
- `energy.demand.fact_export_volume`: `fiscal_quarter_id`, `scenario_id`, `trade_route_id`, `hydrocarbon_id`, `market_id`, `export_quantity`

### Q1 2026 (2) — Chevron

For Chevron, Have Venezuela fiscal terms changed enough to do more than recycle cash and pay down the legacy balance?

- `energy.price.fact_free_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.price.fact_chemical_price`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_price_amount`
- `energy.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `cost_category_id`, `operating_expense_amount`
- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (3) — Chevron

For Chevron, How close are the power contracts with the technology customer to a decision?

- `energy.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `energy.demand.fact_power_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `power_demand_quantity`
- `energy.demand.fact_refined_product_demand`: `fiscal_quarter_id`, `scenario_id`, `refined_product_id`, `market_id`, `customer_segment_id`, `refined_product_demand_quantity`
- `energy.price.fact_power_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `power_price_amount`
- `energy.supply.dim_power_plant`: `power_plant_id`, `power_plant_name`, `country_id`
- `energy.supply.fact_power_generation`: `fiscal_quarter_id`, `scenario_id`, `power_plant_id`, `power_generation_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (4) — Chevron

For Chevron, How should recovery of historical Venezuela receivables be weighed against looking only forward?

- `energy.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `energy.demand.fact_chemical_product_demand`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_product_demand_quantity`
- `energy.demand.fact_crude_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `hydrocarbon_id`, `crude_demand_quantity`
- `energy.demand.fact_export_volume`: `fiscal_quarter_id`, `scenario_id`, `trade_route_id`, `hydrocarbon_id`, `market_id`, `export_quantity`

### Q1 2026 (5) — Chevron

For Chevron, Where could local product shortages hit, given exposure beyond the regulated refining system?

- `energy.demand.dim_market`: `market_id`, `market_name`, `region_id`
- `energy.supply.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `country_id`, `facility_capacity_quantity`
- `energy.demand.fact_chemical_product_demand`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_product_demand_quantity`
- `energy.demand.fact_export_volume`: `fiscal_quarter_id`, `scenario_id`, `trade_route_id`, `hydrocarbon_id`, `market_id`, `export_quantity`
- `energy.demand.fact_monthly_market_demand`: `fiscal_quarter_id`, `scenario_id`, `calendar_month_id`, `refined_product_id`, `market_id`, `monthly_demand_quantity`
- `energy.demand.fact_refined_product_demand`: `fiscal_quarter_id`, `scenario_id`, `refined_product_id`, `market_id`, `customer_segment_id`, `refined_product_demand_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (7) — Chevron

For Chevron, How much LNG is uncommitted and available for arbitrage in a tighter market?

- `energy.demand.fact_lng_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `lng_cargo_quantity`, `lng_demand_quantity`
- `energy.demand.dim_market`: `market_id`, `market_name`, `region_id`
- `energy.price.fact_lng_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `lng_price_amount`
- `energy.supply.fact_lng_production`: `fiscal_quarter_id`, `scenario_id`, `lng_terminal_id`, `lng_production_quantity`, `lng_cargo_quantity`
- `energy.demand.dim_trade_route`: `trade_route_id`, `trade_route_name`, `market_id`
- `energy.demand.fact_chemical_product_demand`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_product_demand_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (11) — Chevron

For Chevron, Which government policies help or hurt during a supply shock?

- `energy.supply.fact_chemical_capacity`: `fiscal_quarter_id`, `scenario_id`, `chemical_plant_id`, `chemical_product_id`, `chemical_capacity_quantity`
- `energy.supply.fact_chemical_production`: `fiscal_quarter_id`, `scenario_id`, `chemical_plant_id`, `chemical_product_id`, `chemical_production_quantity`
- `energy.supply.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `country_id`, `facility_capacity_quantity`
- `energy.supply.fact_refinery_capacity`: `fiscal_quarter_id`, `scenario_id`, `refinery_id`, `refinery_capacity_quantity`
- `energy.demand.dim_chemical_product`: `chemical_product_id`, `chemical_product_code`, `chemical_product_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (2) — Chevron

For Chevron, What condition are the Venezuela assets in, and how large could the resource be in the portfolio?

- `energy.supply.fact_affiliate_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `operator_affiliate_id`, `hydrocarbon_id`, `asset_id`, `country_id`, `affiliate_gross_production_quantity`, `affiliate_net_production_quantity`
- `energy.supply.fact_monthly_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `calendar_month_id`, `hydrocarbon_id`, `field_id`, `asset_id`, `monthly_gross_production_quantity`, `monthly_net_production_quantity`
- `energy.supply.fact_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `asset_id`, `hydrocarbon_id`, `production_capacity_quantity`
- `energy.supply.fact_production_quantity`: `production_record_id`, `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `play_id`, `asset_id`, `country_id`, `gross_operated_production_quantity`, `net_entitlement_production_quantity`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (3) — Chevron

For Chevron, How do Kazakhstan's planned compensation cuts interact with Tengiz maintenance?

- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.price.fact_realized_price`: `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `country_id`, `benchmark_id`, `realized_price_amount`, `benchmark_price_amount`, `price_differential_amount`
- `energy.supply.dim_field`: `field_id`, `field_name`, `country_id`
- `energy.supply.fact_monthly_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `calendar_month_id`, `hydrocarbon_id`, `field_id`, `asset_id`, `monthly_gross_production_quantity`, `monthly_net_production_quantity`
- `energy.supply.fact_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `asset_id`, `hydrocarbon_id`, `production_capacity_quantity`
- `energy.supply.fact_production_quantity`: `production_record_id`, `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `play_id`, `asset_id`, `country_id`, `gross_operated_production_quantity`, `net_entitlement_production_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (6) — Chevron

For Chevron, How do Libya and Iraq compare with peers' interest, and is a smaller LNG portfolio a different long-term view?

- `energy.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `energy.demand.fact_lng_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `lng_cargo_quantity`, `lng_demand_quantity`
- `energy.price.fact_lng_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `lng_price_amount`
- `energy.supply.dim_lng_terminal`: `lng_terminal_id`, `lng_terminal_name`, `country_id`
- `energy.supply.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `country_id`, `facility_capacity_quantity`
- `energy.supply.fact_lng_capacity`: `fiscal_quarter_id`, `scenario_id`, `lng_terminal_id`, `lng_capacity_quantity`, `lng_train_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (8) — Chevron

For Chevron, Are early surfactant results outside the Permian, in the DJ or Bakken, similar?

- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.supply.dim_basin`: `basin_id`, `basin_name`, `region_id`
- `energy.supply.fact_basin_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `basin_id`, `hydrocarbon_id`, `play_id`, `basin_capacity_quantity`
- `energy.demand.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`
- `energy.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `energy.demand.dim_chemical_product`: `chemical_product_id`, `chemical_product_code`, `chemical_product_name`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (5) — Chevron

For Chevron, Has the way the base business is managed changed, and is that repeatable?

- `energy.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.price.fact_chemical_price`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_price_amount`
- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.price.fact_realized_price`: `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `country_id`, `benchmark_id`, `realized_price_amount`, `benchmark_price_amount`, `price_differential_amount`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (6) — Chevron

For Chevron, Is the heavier upstream mix acceptable, or should downstream and chemicals be larger over time?

- `energy.demand.dim_hydrocarbon`: `hydrocarbon_id`, `hydrocarbon_code`, `hydrocarbon_name`
- `energy.demand.dim_market`: `market_id`, `market_name`, `region_id`
- `energy.supply.dim_facility_type`: `facility_type_id`, `facility_type_code`, `facility_type_name`
- `energy.demand.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`
- `energy.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `energy.demand.dim_chemical_product`: `chemical_product_id`, `chemical_product_code`, `chemical_product_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (7) — Chevron

For Chevron, Is the beat in affiliate distributions mostly Tengiz?

- `energy.price.fact_shareholder_distributions`: `fiscal_quarter_id`, `scenario_id`, `distribution_type_id`, `distribution_amount`, `dividend_per_share_amount`
- `energy.supply.dim_operator_affiliate`: `operator_affiliate_id`, `operator_affiliate_name`, `country_id`
- `energy.price.dim_distribution_type`: `distribution_type_id`, `distribution_type_code`, `distribution_type_name`
- `energy.supply.dim_field`: `field_id`, `field_name`, `country_id`
- `energy.supply.fact_affiliate_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `operator_affiliate_id`, `hydrocarbon_id`, `asset_id`, `country_id`, `affiliate_gross_production_quantity`, `affiliate_net_production_quantity`
- `energy.demand.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (10) — Chevron

For Chevron, What could Argentina production become over two or three years, and what gates it, given acreage comparable to the DJ?

- `energy.supply.fact_basin_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `basin_id`, `hydrocarbon_id`, `play_id`, `basin_capacity_quantity`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.price.fact_chemical_price`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_price_amount`
- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.price.fact_realized_price`: `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `country_id`, `benchmark_id`, `realized_price_amount`, `benchmark_price_amount`, `price_differential_amount`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (3) — Exxon Mobil

For Exxon Mobil, How does force majeure on the Qatar trains interact with the remaining contract length, and does the contract get extended?

- `energy.supply.dim_lng_terminal`: `lng_terminal_id`, `lng_terminal_name`, `country_id`
- `energy.supply.fact_lng_capacity`: `fiscal_quarter_id`, `scenario_id`, `lng_terminal_id`, `lng_capacity_quantity`, `lng_train_quantity`
- `energy.supply.fact_lng_production`: `fiscal_quarter_id`, `scenario_id`, `lng_terminal_id`, `lng_production_quantity`, `lng_cargo_quantity`
- `energy.demand.fact_lng_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `lng_cargo_quantity`, `lng_demand_quantity`
- `energy.price.fact_lng_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `lng_price_amount`
- `energy.supply.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `country_id`, `facility_capacity_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (5) — Exxon Mobil

For Exxon Mobil, Can heavy-oil technology bring Canada, including Aspen, back faster given short supply?

- `energy.supply.dim_field`: `field_id`, `field_name`, `country_id`
- `energy.price.dim_trading_desk`: `trading_desk_id`, `trading_desk_code`, `trading_desk_name`
- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.price.fact_trading_optimization`: `fiscal_quarter_id`, `scenario_id`, `trading_desk_id`, `market_id`, `calendar_month_id`, `trading_income_amount`, `optimization_income_amount`
- `energy.supply.dim_asset`: `asset_id`, `asset_name`, `country_id`, `field_id`
- `energy.supply.dim_basin`: `basin_id`, `basin_name`, `region_id`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (6) — Exxon Mobil

For Exxon Mobil, Is cold-box lead time the main reason damaged Qatar trains take three to five years to return?

- `energy.supply.dim_lng_terminal`: `lng_terminal_id`, `lng_terminal_name`, `country_id`
- `energy.supply.fact_lng_capacity`: `fiscal_quarter_id`, `scenario_id`, `lng_terminal_id`, `lng_capacity_quantity`, `lng_train_quantity`
- `energy.supply.fact_lng_production`: `fiscal_quarter_id`, `scenario_id`, `lng_terminal_id`, `lng_production_quantity`, `lng_cargo_quantity`
- `energy.demand.fact_lng_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `lng_cargo_quantity`, `lng_demand_quantity`
- `energy.price.fact_lng_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `lng_price_amount`
- `energy.supply.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `country_id`, `facility_capacity_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (3) — Exxon Mobil

For Exxon Mobil, Do assets added beyond the 2030s still have to look like Guyana, the Permian, and LNG?

- `energy.demand.dim_hydrocarbon`: `hydrocarbon_id`, `hydrocarbon_code`, `hydrocarbon_name`
- `energy.demand.fact_lng_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `lng_cargo_quantity`, `lng_demand_quantity`
- `energy.price.fact_lng_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `lng_price_amount`
- `energy.supply.dim_lng_terminal`: `lng_terminal_id`, `lng_terminal_name`, `country_id`
- `energy.supply.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `country_id`, `facility_capacity_quantity`
- `energy.supply.fact_lng_capacity`: `fiscal_quarter_id`, `scenario_id`, `lng_terminal_id`, `lng_capacity_quantity`, `lng_train_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (4) — Exxon Mobil

For Exxon Mobil, How far does the Permian technology toolkit scale beyond U.S. shale?

- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.supply.dim_play`: `play_id`, `play_name`, `region_id`
- `energy.demand.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`
- `energy.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `energy.demand.dim_chemical_product`: `chemical_product_id`, `chemical_product_code`, `chemical_product_name`
- `energy.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (2) — Exxon Mobil

For Exxon Mobil, How much of the Permian beat and higher full-year guide is the advanced proppant versus spacing or development changes?

- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.price.fact_chemical_price`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_price_amount`
- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.price.fact_realized_price`: `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `country_id`, `benchmark_id`, `realized_price_amount`, `benchmark_price_amount`, `price_differential_amount`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`

### Q3 2025 (4) — Exxon Mobil

For Exxon Mobil, Was the graphite acquisition facilities, technology, or both, and how tightly does it tie to refining and chemicals?

- `energy.demand.dim_market`: `market_id`, `market_name`, `region_id`
- `energy.price.fact_refining_margin`: `fiscal_quarter_id`, `scenario_id`, `refinery_id`, `refining_margin_per_barrel`
- `energy.supply.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `country_id`, `facility_capacity_quantity`
- `energy.supply.fact_refinery_capacity`: `fiscal_quarter_id`, `scenario_id`, `refinery_id`, `refinery_capacity_quantity`
- `energy.demand.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`
- `energy.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (7) — Exxon Mobil

For Exxon Mobil, Where does Mozambique stand on security, and is an early investment decision still likely?

- `energy.supply.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `country_id`, `facility_capacity_quantity`
- `energy.demand.dim_market`: `market_id`, `market_name`, `region_id`
- `energy.demand.fact_lng_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `lng_cargo_quantity`, `lng_demand_quantity`
- `energy.price.fact_lng_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `lng_price_amount`
- `energy.price.fact_segment_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_capital_spending_amount`
- `energy.supply.dim_facility_type`: `facility_type_id`, `facility_type_code`, `facility_type_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (1) — Exxon Mobil

For Exxon Mobil, What Guyana milestones matter this year, and how is the asset tracking?

- `energy.supply.dim_asset`: `asset_id`, `asset_name`, `country_id`, `field_id`
- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.supply.dim_play`: `play_id`, `play_name`, `region_id`
- `energy.supply.dim_project`: `project_id`, `project_name`, `asset_id`, `field_id`
- `energy.supply.fact_affiliate_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `operator_affiliate_id`, `hydrocarbon_id`, `asset_id`, `country_id`, `affiliate_gross_production_quantity`, `affiliate_net_production_quantity`
- `energy.supply.fact_carbon_capture`: `fiscal_quarter_id`, `scenario_id`, `low_carbon_project_id`, `asset_id`, `captured_carbon_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (2) — Exxon Mobil

For Exxon Mobil, How would North American tariffs hit Canadian upstream and downstream versus U.S. downstream?

- `energy.demand.dim_hydrocarbon`: `hydrocarbon_id`, `hydrocarbon_code`, `hydrocarbon_name`
- `energy.price.fact_refining_margin`: `fiscal_quarter_id`, `scenario_id`, `refinery_id`, `refining_margin_per_barrel`
- `energy.supply.dim_asset`: `asset_id`, `asset_name`, `country_id`, `field_id`
- `energy.supply.dim_facility_type`: `facility_type_id`, `facility_type_code`, `facility_type_name`
- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.supply.dim_operator_affiliate`: `operator_affiliate_id`, `operator_affiliate_name`, `country_id`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (3) — Exxon Mobil

For Exxon Mobil, Is there demand for low-carbon gas for data centers versus ordinary gas power?

- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.supply.fact_carbon_capture`: `fiscal_quarter_id`, `scenario_id`, `low_carbon_project_id`, `asset_id`, `captured_carbon_quantity`
- `energy.demand.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`
- `energy.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `energy.demand.fact_lng_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `lng_cargo_quantity`, `lng_demand_quantity`
- `energy.demand.fact_power_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `power_demand_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (6) — Exxon Mobil

For Exxon Mobil, How does LNG contracting change as permit constraints ease, and is the medium-term market oversupplied?

- `energy.demand.fact_lng_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `lng_cargo_quantity`, `lng_demand_quantity`
- `energy.demand.dim_market`: `market_id`, `market_name`, `region_id`
- `energy.demand.dim_trade_route`: `trade_route_id`, `trade_route_name`, `market_id`
- `energy.demand.fact_chemical_product_demand`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_product_demand_quantity`
- `energy.demand.fact_crude_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `hydrocarbon_id`, `crude_demand_quantity`
- `energy.demand.fact_export_volume`: `fiscal_quarter_id`, `scenario_id`, `trade_route_id`, `hydrocarbon_id`, `market_id`, `export_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (10) — Exxon Mobil

For Exxon Mobil, How has the commercial side of carbon capture evolved, and what challenges remain?

- `energy.supply.fact_carbon_capture`: `fiscal_quarter_id`, `scenario_id`, `low_carbon_project_id`, `asset_id`, `captured_carbon_quantity`
- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.demand.dim_market`: `market_id`, `market_name`, `region_id`
- `energy.demand.dim_trade_route`: `trade_route_id`, `trade_route_name`, `market_id`
- `energy.demand.fact_chemical_product_demand`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_product_demand_quantity`
- `energy.demand.fact_crude_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `hydrocarbon_id`, `crude_demand_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
