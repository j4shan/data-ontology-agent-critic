# Energy Inc price slice

This slice is part of the Energy Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q2 2026 (2) — Chevron

For Chevron, How large can power be in the mix beyond the first project, and what returns come with later projects?

- `energy.supply.dim_power_plant`: `power_plant_id`, `power_plant_name`, `country_id`
- `energy.supply.fact_power_generation`: `fiscal_quarter_id`, `scenario_id`, `power_plant_id`, `power_generation_quantity`
- `energy.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `segment_id`, `capital_spending_amount`
- `energy.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`
- `energy.price.fact_power_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `power_price_amount`
- `energy.price.fact_segment_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_capital_spending_amount`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (3) — Chevron

For Chevron, With Guyana turning to cash and other portfolio additions, does the Permian growth pause get revisited?

- `energy.price.fact_free_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.supply.fact_well_activity`: `fiscal_quarter_id`, `scenario_id`, `play_id`, `field_id`, `well_type_id`, `rig_type_id`, `well_quantity`, `rig_quantity`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.dim_distribution_type`: `distribution_type_id`, `distribution_type_code`, `distribution_type_name`
- `energy.price.dim_hedge_type`: `hedge_type_id`, `hedge_type_code`, `hedge_type_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (4) — Chevron

For Chevron, How does Iraq compete for capital on cost of supply and above-ground risk?

- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.supply.dim_project`: `project_id`, `project_name`, `asset_id`, `field_id`
- `energy.supply.fact_project_progress`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `asset_id`, `project_completion_percent`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.dim_trading_desk`: `trading_desk_id`, `trading_desk_code`, `trading_desk_name`
- `energy.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `segment_id`, `capital_spending_amount`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (5) — Chevron

For Chevron, Where are the cost savings ahead of schedule, and what was surprising in the efficiency portion?

- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `cost_category_id`, `operating_expense_amount`
- `energy.price.fact_free_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.price.fact_segment_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_capital_spending_amount`
- `energy.demand.dim_market`: `market_id`, `market_name`, `region_id`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (7) — Chevron

For Chevron, Where do exploration campaigns in Libya, Namibia, and Greece stand?

- `energy.supply.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `country_id`, `facility_capacity_quantity`
- `energy.price.fact_monthly_realized_price`: `fiscal_quarter_id`, `scenario_id`, `calendar_month_id`, `hydrocarbon_id`, `benchmark_id`, `country_id`, `monthly_realized_price_amount`, `monthly_price_differential_amount`
- `energy.price.fact_realized_price`: `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `country_id`, `benchmark_id`, `realized_price_amount`, `benchmark_price_amount`, `price_differential_amount`
- `energy.price.fact_segment_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_capital_spending_amount`
- `energy.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `energy.demand.dim_market`: `market_id`, `market_name`, `region_id`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (9) — Chevron

For Chevron, Why license the surfactant technology instead of keeping it inside the company?

- `energy.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`
- `energy.price.fact_free_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `energy.price.fact_trading_optimization`: `fiscal_quarter_id`, `scenario_id`, `trading_desk_id`, `market_id`, `calendar_month_id`, `trading_income_amount`, `optimization_income_amount`
- `energy.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `energy.demand.fact_monthly_market_demand`: `fiscal_quarter_id`, `scenario_id`, `calendar_month_id`, `refined_product_id`, `market_id`, `monthly_demand_quantity`
- `energy.supply.fact_monthly_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `calendar_month_id`, `hydrocarbon_id`, `field_id`, `asset_id`, `monthly_gross_production_quantity`, `monthly_net_production_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (10) — Chevron

For Chevron, What sets the long-term capital-spending range as Permian spend falls on efficiency but power spending is added?

- `energy.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `segment_id`, `capital_spending_amount`
- `energy.price.fact_segment_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_capital_spending_amount`
- `energy.price.fact_power_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `power_price_amount`
- `energy.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `energy.demand.fact_monthly_market_demand`: `fiscal_quarter_id`, `scenario_id`, `calendar_month_id`, `refined_product_id`, `market_id`, `monthly_demand_quantity`
- `energy.demand.fact_power_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `power_demand_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (11) — Chevron

For Chevron, After the disruption, is there evidence of demand destruction, and where do refining cracks go?

- `energy.price.fact_refined_product_price`: `fiscal_quarter_id`, `scenario_id`, `refined_product_id`, `market_id`, `benchmark_id`, `refined_product_price_amount`, `crack_spread_amount`
- `energy.demand.dim_chemical_product`: `chemical_product_id`, `chemical_product_code`, `chemical_product_name`
- `energy.demand.dim_market`: `market_id`, `market_name`, `region_id`
- `energy.demand.dim_refined_product`: `refined_product_id`, `refined_product_code`, `refined_product_name`
- `energy.demand.fact_chemical_product_demand`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_product_demand_quantity`
- `energy.demand.fact_export_volume`: `fiscal_quarter_id`, `scenario_id`, `trade_route_id`, `hydrocarbon_id`, `market_id`, `export_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (14) — Chevron

For Chevron, What is the latest view on further investment in Vaca Muerta?

- `energy.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `segment_id`, `capital_spending_amount`
- `energy.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`
- `energy.price.fact_segment_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_capital_spending_amount`
- `energy.price.fact_segment_earnings`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_earnings_amount`, `segment_revenue_amount`
- `energy.supply.dim_project`: `project_id`, `project_name`, `asset_id`, `field_id`
- `energy.supply.fact_project_progress`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `asset_id`, `project_completion_percent`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (1) — Chevron

For Chevron, What margin is being captured in refining and from waterborne crudes after the merger, and how did the first quarter show that?

- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.price.fact_realized_price`: `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `country_id`, `benchmark_id`, `realized_price_amount`, `benchmark_price_amount`, `price_differential_amount`
- `energy.price.fact_refining_margin`: `fiscal_quarter_id`, `scenario_id`, `refinery_id`, `refining_margin_per_barrel`
- `energy.supply.fact_affiliate_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `operator_affiliate_id`, `hydrocarbon_id`, `asset_id`, `country_id`, `affiliate_gross_production_quantity`, `affiliate_net_production_quantity`
- `energy.supply.fact_basin_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `basin_id`, `hydrocarbon_id`, `play_id`, `basin_capacity_quantity`
- `energy.supply.fact_carbon_capture`: `fiscal_quarter_id`, `scenario_id`, `low_carbon_project_id`, `asset_id`, `captured_carbon_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (8) — Chevron

For Chevron, Can a U.S.-heavy chemicals system capture a polyethylene price move while naphtha crackers elsewhere are short of feedstock?

- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.price.fact_chemical_price`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_price_amount`
- `energy.supply.fact_chemical_capacity`: `fiscal_quarter_id`, `scenario_id`, `chemical_plant_id`, `chemical_product_id`, `chemical_capacity_quantity`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.dim_distribution_type`: `distribution_type_id`, `distribution_type_code`, `distribution_type_name`
- `energy.price.dim_hedge_type`: `hedge_type_id`, `hedge_type_code`, `hedge_type_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (9) — Chevron

For Chevron, Have lower Bakken costs made it more clearly core, and has buyer interest risen with the oil price?

- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `cost_category_id`, `operating_expense_amount`
- `energy.supply.fact_project_progress`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `asset_id`, `project_completion_percent`
- `energy.price.dim_distribution_type`: `distribution_type_id`, `distribution_type_code`, `distribution_type_name`
- `energy.price.dim_hedge_type`: `hedge_type_id`, `hedge_type_code`, `hedge_type_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (10) — Chevron

For Chevron, How are the operated and non-operated Eastern Mediterranean gas assets being prioritized given the nearby conflict?

- `energy.supply.fact_affiliate_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `operator_affiliate_id`, `hydrocarbon_id`, `asset_id`, `country_id`, `affiliate_gross_production_quantity`, `affiliate_net_production_quantity`
- `energy.supply.fact_production_quantity`: `production_record_id`, `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `play_id`, `asset_id`, `country_id`, `gross_operated_production_quantity`, `net_entitlement_production_quantity`
- `energy.demand.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`
- `energy.demand.fact_lng_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `lng_cargo_quantity`, `lng_demand_quantity`
- `energy.supply.fact_monthly_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `calendar_month_id`, `hydrocarbon_id`, `field_id`, `asset_id`, `monthly_gross_production_quantity`, `monthly_net_production_quantity`
- `energy.supply.fact_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `asset_id`, `hydrocarbon_id`, `production_capacity_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (12) — Chevron

For Chevron, Has the exploration order changed in order to get oil to market faster?

- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.price.fact_chemical_price`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_price_amount`
- `energy.price.fact_lng_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `lng_price_amount`
- `energy.price.fact_power_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `power_price_amount`
- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.price.fact_refined_product_price`: `fiscal_quarter_id`, `scenario_id`, `refined_product_id`, `market_id`, `benchmark_id`, `refined_product_price_amount`, `crack_spread_amount`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (13) — Chevron

For Chevron, Have California refineries used shipping rules or other operating changes to keep the market supplied?

- `energy.price.fact_trading_optimization`: `fiscal_quarter_id`, `scenario_id`, `trading_desk_id`, `market_id`, `calendar_month_id`, `trading_income_amount`, `optimization_income_amount`
- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.supply.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `country_id`, `facility_capacity_quantity`
- `energy.supply.fact_refinery_capacity`: `fiscal_quarter_id`, `scenario_id`, `refinery_id`, `refinery_capacity_quantity`
- `energy.supply.fact_storage_inventory`: `fiscal_quarter_id`, `scenario_id`, `storage_terminal_id`, `hydrocarbon_id`, `inventory_quantity`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (4) — Chevron

For Chevron, How much of the remaining cost reduction depends on the organizational changes now a few months old?

- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `cost_category_id`, `operating_expense_amount`
- `energy.price.fact_free_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_name`, `fiscal_quarter_id`
- `energy.price.dim_distribution_type`: `distribution_type_id`, `distribution_type_code`, `distribution_type_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (5) — Chevron

For Chevron, Now that Permian well productivity is showing up in capital efficiency, what does that momentum mean for a short-cycle asset?

- `energy.price.fact_export_price`: `fiscal_quarter_id`, `scenario_id`, `trade_route_id`, `hydrocarbon_id`, `benchmark_id`, `export_realized_price_amount`
- `energy.price.fact_monthly_realized_price`: `fiscal_quarter_id`, `scenario_id`, `calendar_month_id`, `hydrocarbon_id`, `benchmark_id`, `country_id`, `monthly_realized_price_amount`, `monthly_price_differential_amount`
- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.price.fact_realized_price`: `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `country_id`, `benchmark_id`, `realized_price_amount`, `benchmark_price_amount`, `price_differential_amount`
- `energy.price.fact_refining_margin`: `fiscal_quarter_id`, `scenario_id`, `refinery_id`, `refining_margin_per_barrel`
- `energy.supply.dim_project`: `project_id`, `project_name`, `asset_id`, `field_id`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (9) — Chevron

For Chevron, How is the Bakken performing versus expectations after a couple of quarters of cross-learning?

- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.dim_distribution_type`: `distribution_type_id`, `distribution_type_code`, `distribution_type_name`
- `energy.price.dim_hedge_type`: `hedge_type_id`, `hedge_type_code`, `hedge_type_name`
- `energy.price.dim_trading_desk`: `trading_desk_id`, `trading_desk_code`, `trading_desk_name`
- `energy.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `segment_id`, `capital_spending_amount`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (10) — Chevron

For Chevron, How much Venezuela heavy can U.S. refineries take without backing out Canadian heavy or changing the heavy-light spread?

- `energy.price.fact_export_price`: `fiscal_quarter_id`, `scenario_id`, `trade_route_id`, `hydrocarbon_id`, `benchmark_id`, `export_realized_price_amount`
- `energy.price.fact_monthly_realized_price`: `fiscal_quarter_id`, `scenario_id`, `calendar_month_id`, `hydrocarbon_id`, `benchmark_id`, `country_id`, `monthly_realized_price_amount`, `monthly_price_differential_amount`
- `energy.price.fact_realized_price`: `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `country_id`, `benchmark_id`, `realized_price_amount`, `benchmark_price_amount`, `price_differential_amount`
- `energy.price.fact_refined_product_price`: `fiscal_quarter_id`, `scenario_id`, `refined_product_id`, `market_id`, `benchmark_id`, `refined_product_price_amount`, `crack_spread_amount`
- `energy.price.fact_refining_margin`: `fiscal_quarter_id`, `scenario_id`, `refinery_id`, `refining_margin_per_barrel`
- `energy.demand.dim_benchmark`: `benchmark_id`, `benchmark_code`, `benchmark_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (11) — Chevron

For Chevron, What operating or strategic benefits would come from owning more of the chemicals joint venture than the current structure allows?

- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`
- `energy.price.fact_free_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `energy.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `cost_category_id`, `operating_expense_amount`
- `energy.price.fact_segment_earnings`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_earnings_amount`, `segment_revenue_amount`
- `energy.demand.dim_market`: `market_id`, `market_name`, `region_id`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (1) — Chevron

For Chevron, What drove the Permian result, including any difference between operated and non-operated acreage?

- `energy.price.fact_hedging_result`: `fiscal_quarter_id`, `scenario_id`, `hedge_type_id`, `hydrocarbon_id`, `hedging_gain_loss_amount`
- `energy.supply.fact_affiliate_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `operator_affiliate_id`, `hydrocarbon_id`, `asset_id`, `country_id`, `affiliate_gross_production_quantity`, `affiliate_net_production_quantity`
- `energy.supply.fact_production_quantity`: `production_record_id`, `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `play_id`, `asset_id`, `country_id`, `gross_operated_production_quantity`, `net_entitlement_production_quantity`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.dim_distribution_type`: `distribution_type_id`, `distribution_type_code`, `distribution_type_name`
- `energy.price.dim_hedge_type`: `hedge_type_id`, `hedge_type_code`, `hedge_type_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (2) — Chevron

For Chevron, Is the Bakken core, and does it compete as part of a broader Rockies position?

- `energy.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `segment_id`, `capital_spending_amount`
- `energy.price.fact_segment_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_capital_spending_amount`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.supply.dim_project`: `project_id`, `project_name`, `asset_id`, `field_id`
- `energy.supply.fact_project_progress`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `asset_id`, `project_completion_percent`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (3) — Chevron

For Chevron, What drove the acquired production to the high end of expectations?

- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.price.fact_chemical_price`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_price_amount`
- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.price.fact_realized_price`: `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `country_id`, `benchmark_id`, `realized_price_amount`, `benchmark_price_amount`, `price_differential_amount`
- `energy.supply.fact_affiliate_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `operator_affiliate_id`, `hydrocarbon_id`, `asset_id`, `country_id`, `affiliate_gross_production_quantity`, `affiliate_net_production_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (9) — Chevron

For Chevron, What is the state of the Permian if shale has to make room for other supply next year?

- `energy.supply.fact_affiliate_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `operator_affiliate_id`, `hydrocarbon_id`, `asset_id`, `country_id`, `affiliate_gross_production_quantity`, `affiliate_net_production_quantity`
- `energy.supply.fact_production_quantity`: `production_record_id`, `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `play_id`, `asset_id`, `country_id`, `gross_operated_production_quantity`, `net_entitlement_production_quantity`
- `energy.supply.fact_well_activity`: `fiscal_quarter_id`, `scenario_id`, `play_id`, `field_id`, `well_type_id`, `rig_type_id`, `well_quantity`, `rig_quantity`
- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.supply.dim_play`: `play_id`, `play_name`, `region_id`
- `energy.supply.fact_basin_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `basin_id`, `hydrocarbon_id`, `play_id`, `basin_capacity_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (1) — Exxon Mobil

For Exxon Mobil, How did April refining margins follow the strong March, and what can the downstream do to balance that market this year?

- `energy.price.fact_refining_margin`: `fiscal_quarter_id`, `scenario_id`, `refinery_id`, `refining_margin_per_barrel`
- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.price.fact_chemical_price`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_price_amount`
- `energy.price.fact_lng_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `lng_price_amount`
- `energy.price.fact_power_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `power_price_amount`
- `energy.price.fact_refined_product_price`: `fiscal_quarter_id`, `scenario_id`, `refined_product_id`, `market_id`, `benchmark_id`, `refined_product_price_amount`, `crack_spread_amount`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (2) — Exxon Mobil

For Exxon Mobil, Does a higher price and the need for U.S. barrels change Permian activity, for the industry or for Exxon?

- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.price.fact_chemical_price`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_price_amount`
- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.price.fact_realized_price`: `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `country_id`, `benchmark_id`, `realized_price_amount`, `benchmark_price_amount`, `price_differential_amount`
- `energy.demand.fact_refined_product_demand`: `fiscal_quarter_id`, `scenario_id`, `refined_product_id`, `market_id`, `customer_segment_id`, `refined_product_demand_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (4) — Exxon Mobil

For Exxon Mobil, Does the concentration of the LNG portfolio in Qatar change the portfolio strategy versus a more diversified upstream?

- `energy.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`
- `energy.price.fact_free_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `energy.price.fact_lng_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `lng_price_amount`
- `energy.price.fact_shareholder_distributions`: `fiscal_quarter_id`, `scenario_id`, `distribution_type_id`, `distribution_amount`, `dividend_per_share_amount`
- `energy.demand.dim_hydrocarbon`: `hydrocarbon_id`, `hydrocarbon_code`, `hydrocarbon_name`
- `energy.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (7) — Exxon Mobil

For Exxon Mobil, Which parts of the business reverse the short-term timing effects, given the long-term targets span many moving pieces?

- `energy.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`
- `energy.price.fact_lng_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `lng_price_amount`
- `energy.price.fact_segment_earnings`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_earnings_amount`, `segment_revenue_amount`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_hydrocarbon`: `hydrocarbon_id`, `hydrocarbon_code`, `hydrocarbon_name`
- `energy.demand.fact_lng_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `lng_cargo_quantity`, `lng_demand_quantity`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (1) — Exxon Mobil

For Exxon Mobil, What happens to Guyana growth as the Stabroek license expiration approaches?

- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.price.fact_chemical_price`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_price_amount`
- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.price.fact_realized_price`: `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `country_id`, `benchmark_id`, `realized_price_amount`, `benchmark_price_amount`, `price_differential_amount`
- `energy.supply.fact_affiliate_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `operator_affiliate_id`, `hydrocarbon_id`, `asset_id`, `country_id`, `affiliate_gross_production_quantity`, `affiliate_net_production_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (2) — Exxon Mobil

For Exxon Mobil, With Permian exit and full-year rates both around the same level, is there upside in the intra-year cadence?

- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.price.fact_chemical_price`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_price_amount`
- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.price.fact_realized_price`: `fiscal_quarter_id`, `scenario_id`, `hydrocarbon_id`, `field_id`, `country_id`, `benchmark_id`, `realized_price_amount`, `benchmark_price_amount`, `price_differential_amount`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`

### Q4 2025 (5) — Exxon Mobil

For Exxon Mobil, How do Papua New Guinea and Mozambique LNG sit on the cost curve versus Gulf Coast LNG, ahead of investment decisions?

- `energy.supply.dim_asset`: `asset_id`, `asset_name`, `country_id`, `field_id`
- `energy.supply.dim_lng_terminal`: `lng_terminal_id`, `lng_terminal_name`, `country_id`
- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.supply.dim_play`: `play_id`, `play_name`, `region_id`
- `energy.supply.dim_project`: `project_id`, `project_name`, `asset_id`, `field_id`
- `energy.supply.fact_carbon_capture`: `fiscal_quarter_id`, `scenario_id`, `low_carbon_project_id`, `asset_id`, `captured_carbon_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (6) — Exxon Mobil

For Exxon Mobil, How do carbon-capture and battery contributions relate to the lithium business?

- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.supply.fact_carbon_capture`: `fiscal_quarter_id`, `scenario_id`, `low_carbon_project_id`, `asset_id`, `captured_carbon_quantity`
- `energy.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`
- `energy.price.fact_segment_earnings`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_earnings_amount`, `segment_revenue_amount`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.dim_distribution_type`: `distribution_type_id`, `distribution_type_code`, `distribution_type_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (7) — Exxon Mobil

For Exxon Mobil, Is data-center interest in carbon capture as an emissions offset real, and can it be material?

- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.supply.fact_carbon_capture`: `fiscal_quarter_id`, `scenario_id`, `low_carbon_project_id`, `asset_id`, `captured_carbon_quantity`
- `energy.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `energy.demand.fact_export_volume`: `fiscal_quarter_id`, `scenario_id`, `trade_route_id`, `hydrocarbon_id`, `market_id`, `export_quantity`
- `energy.demand.fact_refined_product_demand`: `fiscal_quarter_id`, `scenario_id`, `refined_product_id`, `market_id`, `customer_segment_id`, `refined_product_demand_quantity`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (8) — Exxon Mobil

For Exxon Mobil, What base decline should be assumed for the upstream, and what mid-cycle return is expected in refining and chemicals?

- `energy.price.fact_refining_margin`: `fiscal_quarter_id`, `scenario_id`, `refinery_id`, `refining_margin_per_barrel`
- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.demand.dim_hydrocarbon`: `hydrocarbon_id`, `hydrocarbon_code`, `hydrocarbon_name`
- `energy.demand.dim_market`: `market_id`, `market_name`, `region_id`
- `energy.supply.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `country_id`, `facility_capacity_quantity`
- `energy.supply.fact_refinery_capacity`: `fiscal_quarter_id`, `scenario_id`, `refinery_id`, `refinery_capacity_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (9) — Exxon Mobil

For Exxon Mobil, Are there green shoots in base chemicals on supply or demand, versus competitors?

- `energy.demand.dim_chemical_product`: `chemical_product_id`, `chemical_product_code`, `chemical_product_name`
- `energy.demand.dim_customer_segment`: `customer_segment_id`, `customer_segment_code`, `customer_segment_name`
- `energy.demand.dim_market`: `market_id`, `market_name`, `region_id`
- `energy.demand.fact_chemical_product_demand`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_product_demand_quantity`
- `energy.supply.dim_chemical_plant`: `chemical_plant_id`, `chemical_plant_name`, `country_id`
- `energy.supply.fact_chemical_capacity`: `fiscal_quarter_id`, `scenario_id`, `chemical_plant_id`, `chemical_product_id`, `chemical_capacity_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (1) — Exxon Mobil

For Exxon Mobil, Is capital spending below the range this year mostly captured deflation?

- `energy.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `segment_id`, `capital_spending_amount`
- `energy.price.fact_segment_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_capital_spending_amount`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `cost_category_id`, `operating_expense_amount`
- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.supply.dim_project`: `project_id`, `project_name`, `asset_id`, `field_id`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (3) — Exxon Mobil

For Exxon Mobil, How does the long-term gas and LNG demand outlook change organic or inorganic priorities?

- `energy.demand.fact_lng_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `lng_cargo_quantity`, `lng_demand_quantity`
- `energy.supply.dim_lng_terminal`: `lng_terminal_id`, `lng_terminal_name`, `country_id`
- `energy.supply.fact_affiliate_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `operator_affiliate_id`, `hydrocarbon_id`, `asset_id`, `country_id`, `affiliate_gross_production_quantity`, `affiliate_net_production_quantity`
- `energy.supply.fact_basin_production_capacity`: `fiscal_quarter_id`, `scenario_id`, `basin_id`, `hydrocarbon_id`, `play_id`, `basin_capacity_quantity`
- `energy.supply.fact_facility_capacity`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `country_id`, `facility_capacity_quantity`
- `energy.supply.fact_monthly_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `calendar_month_id`, `hydrocarbon_id`, `field_id`, `asset_id`, `monthly_gross_production_quantity`, `monthly_net_production_quantity`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (5) — Exxon Mobil

For Exxon Mobil, Do capital efficiency and the balance sheet support a step-up in acquisitions?

- `energy.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `segment_id`, `capital_spending_amount`
- `energy.price.fact_segment_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_capital_spending_amount`
- `energy.supply.dim_project`: `project_id`, `project_name`, `asset_id`, `field_id`
- `energy.supply.fact_project_progress`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `asset_id`, `project_completion_percent`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.dim_distribution_type`: `distribution_type_id`, `distribution_type_code`, `distribution_type_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (8) — Exxon Mobil

For Exxon Mobil, What exploration opportunities are in the next one to two years, and has the approach changed?

- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.dim_distribution_type`: `distribution_type_id`, `distribution_type_code`, `distribution_type_name`
- `energy.price.dim_hedge_type`: `hedge_type_id`, `hedge_type_code`, `hedge_type_name`
- `energy.price.dim_trading_desk`: `trading_desk_id`, `trading_desk_code`, `trading_desk_name`
- `energy.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `segment_id`, `capital_spending_amount`
- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (10) — Exxon Mobil

For Exxon Mobil, What is driving the broader industry push back into exploration?

- `energy.supply.fact_well_activity`: `fiscal_quarter_id`, `scenario_id`, `play_id`, `field_id`, `well_type_id`, `rig_type_id`, `well_quantity`, `rig_quantity`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.dim_distribution_type`: `distribution_type_id`, `distribution_type_code`, `distribution_type_name`
- `energy.price.dim_hedge_type`: `hedge_type_id`, `hedge_type_code`, `hedge_type_name`
- `energy.price.dim_trading_desk`: `trading_desk_id`, `trading_desk_code`, `trading_desk_name`
- `energy.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `segment_id`, `capital_spending_amount`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 2025 (11) — Exxon Mobil

For Exxon Mobil, How should the data-center capital boom be read against a lower company capital-spending outlook?

- `energy.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `segment_id`, `capital_spending_amount`
- `energy.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`
- `energy.price.fact_segment_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_capital_spending_amount`
- `energy.demand.fact_power_demand`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `power_demand_quantity`
- `energy.price.fact_free_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `energy.price.fact_power_price`: `fiscal_quarter_id`, `scenario_id`, `market_id`, `benchmark_id`, `power_price_amount`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (4) — Exxon Mobil

For Exxon Mobil, What is the timing of the near-term start-ups beyond Guyana that contribute the earnings queued up?

- `energy.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `segment_id`, `capital_spending_amount`
- `energy.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_earnings_amount`, `enterprise_revenue_amount`
- `energy.price.fact_segment_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_capital_spending_amount`
- `energy.price.fact_segment_earnings`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_earnings_amount`, `segment_revenue_amount`
- `energy.supply.dim_asset`: `asset_id`, `asset_name`, `country_id`, `field_id`
- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (5) — Exxon Mobil

For Exxon Mobil, Is capital spending the main risk to the return target, given the projects organization?

- `energy.price.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `segment_id`, `capital_spending_amount`
- `energy.price.fact_segment_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `segment_capital_spending_amount`
- `energy.supply.dim_project`: `project_id`, `project_name`, `asset_id`, `field_id`
- `energy.supply.fact_project_progress`: `fiscal_quarter_id`, `scenario_id`, `project_id`, `asset_id`, `project_completion_percent`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.dim_distribution_type`: `distribution_type_id`, `distribution_type_code`, `distribution_type_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (8) — Exxon Mobil

For Exxon Mobil, What commodity and margin levels are assumed in the cash-flow growth plan tied to higher U.S. production?

- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.price.fact_free_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.dim_hedge_type`: `hedge_type_id`, `hedge_type_code`, `hedge_type_name`
- `energy.price.fact_chemical_price`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_price_amount`
- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (9) — Exxon Mobil

For Exxon Mobil, Why is the Gulf of Mexico a small deepwater position relative to Angola and Guyana?

- `energy.supply.dim_low_carbon_project`: `low_carbon_project_id`, `low_carbon_project_name`, `asset_id`
- `energy.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `energy.price.dim_trading_desk`: `trading_desk_id`, `trading_desk_code`, `trading_desk_name`
- `energy.price.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `segment_id`, `cost_category_id`, `operating_expense_amount`
- `energy.price.fact_production_expense`: `fiscal_quarter_id`, `scenario_id`, `field_id`, `cost_category_id`, `segment_id`, `production_expense_amount`, `unit_production_expense_amount`
- `energy.price.fact_trading_optimization`: `fiscal_quarter_id`, `scenario_id`, `trading_desk_id`, `market_id`, `calendar_month_id`, `trading_income_amount`, `optimization_income_amount`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2024 (11) — Exxon Mobil

For Exxon Mobil, Are there regional or product green shoots in chemicals, and do new complexes change the margin position?

- `energy.price.fact_chemical_margin`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_margin_per_pound`
- `energy.supply.fact_chemical_capacity`: `fiscal_quarter_id`, `scenario_id`, `chemical_plant_id`, `chemical_product_id`, `chemical_capacity_quantity`
- `energy.price.fact_chemical_price`: `fiscal_quarter_id`, `scenario_id`, `chemical_product_id`, `market_id`, `chemical_price_amount`
- `energy.price.fact_refined_product_price`: `fiscal_quarter_id`, `scenario_id`, `refined_product_id`, `market_id`, `benchmark_id`, `refined_product_price_amount`, `crack_spread_amount`
- `energy.price.fact_refining_margin`: `fiscal_quarter_id`, `scenario_id`, `refinery_id`, `refining_margin_per_barrel`
- `energy.demand.dim_chemical_product`: `chemical_product_id`, `chemical_product_code`, `chemical_product_name`
- `energy.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `energy.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
