# Beverage Inc price, mix and margin slice

This slice is part of the Beverage Inc warehouse. Quantity, capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

## Coca-Cola

### Q1 2026 (1)

How should volume and price/mix split for the rest of 2026 in North America and Asia after a strong unit-case quarter and two softer price/mix quarters?

- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_coca_cola_unit_case_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `unit_case_quantity`, `unit_case_growth_quantity`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.dim_tax_type`: `tax_type_id`, `tax_type_code`, `tax_type_name`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_coca_cola_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `price_mix_change_percent`, `price_change_percent`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.fact_packaging_mix_quantity`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `country_id`, `packaged_unit_case_quantity`

### Q1 2026 (2)

How much of the recent price/mix slowdown is an ongoing affordability choice versus one-off mix, and can unit-case growth stay consistent after the Easter lift?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_coca_cola_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `price_mix_change_percent`, `price_change_percent`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.fact_packaging_mix_quantity`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `country_id`, `packaged_unit_case_quantity`

### Q1 2026 (3)

How is the company working with bottlers as their costs rise, and how is the system set up for a higher-cost year and into next year?

- `beverage.demand.dim_consumption_occasion`: `consumption_occasion_id`, `consumption_occasion_code`, `consumption_occasion_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`
- `beverage.supply.fact_packaging_mix_quantity`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `country_id`, `packaged_unit_case_quantity`

### Q1 2026 (5)

Was the negative underlying gross-margin contribution in the quarter timing or inflation in coffee and tea, and how should that contribution progress as costs normalize?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.dim_tax_type`: `tax_type_id`, `tax_type_code`, `tax_type_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_coca_cola_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `price_mix_change_percent`, `price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`

### Q1 2026 (6)

How could the timing of the CCBA transaction change margin progression in the second half?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.dim_revenue_type`: `revenue_type_id`, `revenue_type_code`, `revenue_type_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_coca_cola_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `price_mix_change_percent`, `price_change_percent`
- `beverage.price.fact_concentrate_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `concentrate_revenue_amount`, `incidence_revenue_per_gallon_amount`

### Q1 2026 (7)

What is driving the strong China and India results, and how sustainable is that APAC performance through the year?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q1 2026 (8)

What caused Asia operating margin to contract sharply even with good top-line growth, and how should regional profitability look from here?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_concentrate_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `bottler_id`, `concentrate_shipment_quantity`
- `beverage.price.dim_coca_cola_reporting_division`: `coca_cola_reporting_division_id`, `coca_cola_reporting_division_code`, `coca_cola_reporting_division_name`
- `beverage.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_division_result`: `fiscal_quarter_id`, `scenario_id`, `coca_cola_reporting_division_id`, `division_revenue_amount`, `division_operating_income_amount`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`

### Q1 2026 (9)

Is the U.S. foodservice approach changing to participate in newer away-from-home formats such as drive-thru beverage chains?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_coca_cola_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `price_mix_change_percent`, `price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`

### Q1 2026 (10)

How are long-term bottler incentives supposed to speed insight sharing and demand creation between the company and bottlers?

- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_concentrate_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `bottler_id`, `concentrate_shipment_quantity`
- `beverage.price.fact_bottler_incentive`: `fiscal_quarter_id`, `scenario_id`, `bottler_id`, `bottler_incentive_amount`
- `beverage.price.fact_concentrate_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `concentrate_revenue_amount`, `incidence_revenue_per_gallon_amount`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`
- `beverage.supply.dim_delivery_process`: `delivery_process_id`, `delivery_process_code`, `delivery_process_name`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`

### Q1 2026 (11)

How long do first-quarter mix headwinds last, and what underlying price rate should be expected, including the unusually low Latin America print?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_coca_cola_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `price_mix_change_percent`, `price_change_percent`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q4 2025 (1)

Inside the 4% to 5% organic sales outlook for 2026, what is the expected balance of price/mix and volume, and what is a normalized price/mix rate after geographic mix and timing hurt the fourth quarter?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.dim_tax_type`: `tax_type_id`, `tax_type_code`, `tax_type_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.fact_packaging_mix_quantity`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `country_id`, `packaged_unit_case_quantity`

### Q4 2025 (3)

Is the North America operating margin, now at a new high, a sustainable level, or does it require more reinvestment?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_beverage_pack_volume`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `unit_case_quantity`, `package_quantity`
- `beverage.price.dim_coca_cola_reporting_division`: `coca_cola_reporting_division_id`, `coca_cola_reporting_division_code`, `coca_cola_reporting_division_name`
- `beverage.price.dim_tax_type`: `tax_type_id`, `tax_type_code`, `tax_type_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_division_result`: `fiscal_quarter_id`, `scenario_id`, `coca_cola_reporting_division_id`, `division_revenue_amount`, `division_operating_income_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q4 2025 (4)

How should India, China, and Mexico, the more volatile markets of 2025, be expected to behave in 2026, including volume around Mexico's excise tax?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.dim_tax_type`: `tax_type_id`, `tax_type_code`, `tax_type_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_coca_cola_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `price_mix_change_percent`, `price_change_percent`
- `beverage.price.fact_excise_tax`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `tax_type_id`, `tax_amount`, `tax_rate_percent`

### Q4 2025 (8)

Will currency benefits be reinvested in the business or taken to earnings, and how does the multiyear hedge position 2027 versus the 2026 currency tailwind?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_tax_type`: `tax_type_id`, `tax_type_code`, `tax_type_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_currency_translation`: `fiscal_quarter_id`, `scenario_id`, `currency_id`, `country_id`, `translation_effect_amount`, `exchange_rate_amount`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_currency`: `currency_id`, `currency_code`, `currency_name`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`

### Q4 2025 (9)

How do U.S. SNAP changes affect demand, and did the first read on the Mexican tax make the 2026 organic-sales outlook more conservative?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_concentrate_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `concentrate_revenue_amount`, `incidence_revenue_per_gallon_amount`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`

### Q4 2025 (10)

What extra detail sits behind the timing of investments called out in EMEA and Asia Pacific?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_concentrate_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `bottler_id`, `concentrate_shipment_quantity`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`

### Q4 2025 (11)

After adjusting for currency, what is underneath the slower earnings growth rate: more investment, early-year caution, or something else in the business?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_currency_translation`: `fiscal_quarter_id`, `scenario_id`, `currency_id`, `country_id`, `translation_effect_amount`, `exchange_rate_amount`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_currency`: `currency_id`, `currency_code`, `currency_name`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`

### Q4 2025 (12)

Where does the new chief executive see the largest innovation opportunities, and how are those executed against a weaker global consumer?

- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_consumption_occasion`: `consumption_occasion_id`, `consumption_occasion_code`, `consumption_occasion_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_glp1_exposure`: `glp1_exposure_id`, `glp1_exposure_code`, `glp1_exposure_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_concentrate_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `bottler_id`, `concentrate_shipment_quantity`
- `beverage.demand.fact_consumption_occasions`: `fiscal_quarter_id`, `scenario_id`, `consumption_occasion_id`, `product_category_id`, `country_id`, `consumer_cohort_id`, `occasion_quantity`
- `beverage.price.fact_concentrate_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `concentrate_revenue_amount`, `incidence_revenue_per_gallon_amount`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`

### Q2 2025 (1)

What specifically is being pivoted in second-half plans even though organic sales and profit were strong, and does the environment feel tougher?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q2 2025 (3)

How realistic is fairlife expansion outside North America over the next few years given the dairy manufacturing footprint?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `beverage.supply.fact_dairy_plant_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `coca_cola_trademark_id`, `dairy_capacity_quantity`, `dairy_production_quantity`

### Q2 2025 (4)

How quickly should Mexico and India rebound after the plan changes made for the second half?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_consumption_occasion`: `consumption_occasion_id`, `consumption_occasion_code`, `consumption_occasion_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_coca_cola_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `price_mix_change_percent`, `price_change_percent`
- `beverage.price.fact_concentrate_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `concentrate_revenue_amount`, `incidence_revenue_per_gallon_amount`

### Q2 2025 (5)

How does operating leverage across the income statement change if productivity stays better and currency pressure fades or turns positive?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_coca_cola_reporting_division`: `coca_cola_reporting_division_id`, `coca_cola_reporting_division_code`, `coca_cola_reporting_division_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_division_result`: `fiscal_quarter_id`, `scenario_id`, `coca_cola_reporting_division_id`, `division_revenue_amount`, `division_operating_income_amount`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_coca_cola_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `price_mix_change_percent`, `price_change_percent`
- `beverage.supply.dim_currency`: `currency_id`, `currency_code`, `currency_name`

### Q2 2025 (10)

How confident is management that concentrate volume turns positive in the second half after transitory hits and a tough comparison, and is the fourth-quarter concentrate comparison especially difficult?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_beverage_pack_volume`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `unit_case_quantity`, `package_quantity`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.fact_packaging_mix_quantity`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `country_id`, `packaged_unit_case_quantity`

### Q4 2024 (1)

Within the 5% to 6% organic-revenue outlook for 2025, how do volume, price, and mix split, and how does pricing differ from a typical year given low-end consumer stress, currency, and still-accepted price increases?

- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_consumption_occasion`: `consumption_occasion_id`, `consumption_occasion_code`, `consumption_occasion_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_coca_cola_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `price_mix_change_percent`, `price_change_percent`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q4 2024 (2)

How should 2025 organic sales phase, and do emerging-market or inflationary-country price contributions fade through the year?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.dim_revenue_type`: `revenue_type_id`, `revenue_type_code`, `revenue_type_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_concentrate_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `concentrate_revenue_amount`, `incidence_revenue_per_gallon_amount`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`

### Q4 2024 (3)

How does 5% to 6% organic sales growth compare with industry growth and the industry exit rate?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_concentrate_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `bottler_id`, `concentrate_shipment_quantity`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`

### Q4 2024 (4)

What drives the implied underlying margin and profit progress in 2025 after currency and a higher tax rate?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.dim_tax_type`: `tax_type_id`, `tax_type_code`, `tax_type_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_currency_translation`: `fiscal_quarter_id`, `scenario_id`, `currency_id`, `country_id`, `translation_effect_amount`, `exchange_rate_amount`
- `beverage.supply.dim_currency`: `currency_id`, `currency_code`, `currency_name`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`

### Q4 2024 (6)

What share of the U.S. portfolio could be touched by potential regulatory change, and how fast can the portfolio be adapted?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `price_mix_change_percent`, `price_change_percent`
- `beverage.price.fact_concentrate_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `concentrate_revenue_amount`, `incidence_revenue_per_gallon_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q4 2024 (9)

Is a volume slowdown in Mexico embedded in the outlook, and would a weaker peso or recession risk change that playbook?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.dim_tax_type`: `tax_type_id`, `tax_type_code`, `tax_type_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `price_mix_change_percent`, `price_change_percent`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q4 2024 (13)

How does Asia Pacific price/mix, down despite some pricing, reconcile with share gains in South Korea and Japan and share losses in Indonesia and Bangladesh?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_coca_cola_reporting_division`: `coca_cola_reporting_division_id`, `coca_cola_reporting_division_code`, `coca_cola_reporting_division_name`
- `beverage.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_coca_cola_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `price_mix_change_percent`, `price_change_percent`
- `beverage.price.fact_price_bridge`: `fiscal_quarter_id`, `scenario_id`, `price_bridge_component_id`, `region_id`, `product_category_id`, `bridge_contribution_percent`

## PepsiCo

### Q2 2026 (1)

Has U.S. consumer behavior improved as fuel and other inflation eased, and does that still support the high end of the organic-sales range in the back half?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_glp1_exposure`: `glp1_exposure_id`, `glp1_exposure_code`, `glp1_exposure_name`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
- `beverage.price.fact_pepsico_beverage_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_pepsico_beverage_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `effective_price_change_percent`

### Q2 2026 (3)

Looking further out, does reviving North America organic growth require more spending and an earnings reset?

- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `beverage.price.fact_marketing_spending`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `product_category_id`, `marketing_spending_amount`, `advertising_spending_amount`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
- `beverage.price.fact_promotion_spending`: `fiscal_quarter_id`, `scenario_id`, `customer_id`, `product_category_id`, `promotion_spending_amount`, `price_investment_amount`

### Q2 2026 (4)

Will price rollbacks spread beyond the largest U.S. customer, and have those reinvestments already shown up as better volume in convenience and away-from-home?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_pepsico_food_brand`: `pepsico_food_brand_id`, `pepsico_food_brand_code`, `pepsico_food_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_pepsico_beverage_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_pepsico_beverage_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `effective_price_change_percent`
- `beverage.price.fact_pepsico_food_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_food_brand_id`, `sales_channel_id`, `net_revenue_amount`

### Q2 2026 (5)

Is the second-half reinvestment mostly absorbing commodity pressure rather than funding extra demand-building?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.demand.fact_beverage_pack_volume`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `unit_case_quantity`, `package_quantity`
- `beverage.demand.fact_snack_pack_volume`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `snack_weight_quantity`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`

### Q2 2026 (8)

Given the gap between U.S. and international results, is the company overinvesting in a mature U.S. market and underinvesting where growth is higher?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`

### Q2 2026 (9)

After the price increase on smaller Frito-Lay bags, what is being done so convenience-channel affordability does not worsen?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_beverage_pack_volume`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `unit_case_quantity`, `package_quantity`
- `beverage.demand.fact_pepsico_snack_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `snack_weight_quantity`, `snack_serving_quantity`
- `beverage.price.dim_pepsico_reporting_division`: `pepsico_reporting_division_id`, `pepsico_reporting_division_code`, `pepsico_reporting_division_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_pepsico_snack_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `net_revenue_amount`

### Q2 2026 (10)

Does optimizing return on investment mean dropping discounts that did not work, or shifting spend to grow volume faster?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_marketing_event`: `marketing_event_id`, `marketing_event_code`, `marketing_event_name`
- `beverage.demand.dim_pepsico_food_brand`: `pepsico_food_brand_id`, `pepsico_food_brand_code`, `pepsico_food_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_beverage_pack_volume`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `unit_case_quantity`, `package_quantity`
- `beverage.demand.fact_event_incremental_volume`: `fiscal_quarter_id`, `scenario_id`, `marketing_event_id`, `country_id`, `product_category_id`, `incremental_unit_case_quantity`
- `beverage.demand.fact_pepsico_food_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_food_brand_id`, `sales_channel_id`, `food_weight_quantity`
- `beverage.price.dim_tax_type`: `tax_type_id`, `tax_type_code`, `tax_type_name`
- `beverage.price.fact_promotion_spending`: `fiscal_quarter_id`, `scenario_id`, `customer_id`, `product_category_id`, `promotion_spending_amount`, `price_investment_amount`
- `beverage.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`

### Q1 2026 (3)

How sustainable is the Frito-Lay North America volume inflection after possible ship-ahead of shelf resets and winter storms, and what are repeat rates on the refill orders?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.price.dim_pepsico_reporting_division`: `pepsico_reporting_division_id`, `pepsico_reporting_division_code`, `pepsico_reporting_division_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.price.fact_pepsico_snack_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q1 2026 (4)

Does Frito-Lay North America still expect both organic revenue growth and core operating-margin expansion this year?

- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `beverage.price.dim_pepsico_reporting_division`: `pepsico_reporting_division_id`, `pepsico_reporting_division_code`, `pepsico_reporting_division_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
- `beverage.price.fact_pepsico_division_result`: `fiscal_quarter_id`, `scenario_id`, `pepsico_reporting_division_id`, `division_revenue_amount`, `division_operating_income_amount`
- `beverage.price.fact_pepsico_snack_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `net_revenue_amount`

### Q1 2026 (5)

How much of PepsiCo Beverages North America volume pressure is smaller packs and price-pack architecture, and should volume declines moderate through the year?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.demand.fact_pepsico_beverage_unit_case_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `unit_case_quantity`
- `beverage.demand.fact_snack_pack_volume`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `snack_weight_quantity`
- `beverage.price.dim_pepsico_reporting_division`: `pepsico_reporting_division_id`, `pepsico_reporting_division_code`, `pepsico_reporting_division_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`

### Q1 2026 (6)

How should innovation versus distribution gains in Frito-Lay North America compare in the second quarter versus the first, as protein and better-for-you items ship?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_pepsico_beverage_unit_case_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `unit_case_quantity`
- `beverage.demand.fact_pepsico_snack_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `snack_weight_quantity`, `snack_serving_quantity`
- `beverage.price.dim_pepsico_reporting_division`: `pepsico_reporting_division_id`, `pepsico_reporting_division_code`, `pepsico_reporting_division_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_pepsico_snack_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `net_revenue_amount`

### Q1 2026 (7)

Of the Frito-Lay North America price adjustments, how much is already in place versus still to come after a modest first-quarter price decline?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.price.dim_pepsico_reporting_division`: `pepsico_reporting_division_id`, `pepsico_reporting_division_code`, `pepsico_reporting_division_name`
- `beverage.price.dim_tax_type`: `tax_type_id`, `tax_type_code`, `tax_type_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_pepsico_snack_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`

### Q1 2026 (8)

Are PepsiCo Beverages North America value shares still declining, and will the strategic review cover share recovery as well as the bottler network?

- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_pepsico_food_brand`: `pepsico_food_brand_id`, `pepsico_food_brand_code`, `pepsico_food_brand_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_pepsico_reporting_division`: `pepsico_reporting_division_id`, `pepsico_reporting_division_code`, `pepsico_reporting_division_name`
- `beverage.price.fact_pepsico_beverage_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_pepsico_beverage_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `effective_price_change_percent`
- `beverage.price.fact_pepsico_food_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_food_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_pepsico_food_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_food_brand_id`, `sales_channel_id`, `revenue_per_pound_amount`
- `beverage.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`

### Q1 2026 (11)

What are the main productivity buckets this year, what is different from prior years, and how do the gains scale into next year?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q1 2026 (12)

Who is driving the increase in consumption occasions, and are those occasions different from the core user?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_consumption_occasion`: `consumption_occasion_id`, `consumption_occasion_code`, `consumption_occasion_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.demand.fact_consumption_occasions`: `fiscal_quarter_id`, `scenario_id`, `consumption_occasion_id`, `product_category_id`, `country_id`, `consumer_cohort_id`, `occasion_quantity`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`

### Q1 2026 (13)

Did Frito-Lay North America investment targets change this year, and where is the greater opportunity to spend?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.demand.fact_pepsico_snack_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `snack_weight_quantity`, `snack_serving_quantity`
- `beverage.price.dim_pepsico_reporting_division`: `pepsico_reporting_division_id`, `pepsico_reporting_division_code`, `pepsico_reporting_division_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_pepsico_snack_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`

### Q3 2025 (1)

How much of the food and beverage volume pressure is the shift to smaller packs versus soft category trends or share loss, and can the innovation pipeline turn volume?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_tax_type`: `tax_type_id`, `tax_type_code`, `tax_type_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`
- `beverage.supply.fact_packaging_mix_quantity`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `country_id`, `packaged_unit_case_quantity`

### Q3 2025 (2)

Which of innovation, functional products, portfolio reshaping, and price-pack architecture matter most for accelerating 2026 revenue, and is the long-term growth algorithm visible inside 2026?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.dim_revenue_type`: `revenue_type_id`, `revenue_type_code`, `revenue_type_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`

### Q3 2025 (3)

Where is fixed cost being resized, and will the structure match current demand by the end of 2025 or is more work left for 2026?

- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_pepsico_beverage_unit_case_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `unit_case_quantity`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`

### Q3 2025 (4)

How healthy is the consumer in Latin America, Asia Pacific, and India after a weather-hit quarter and a better September, and what supports the expected acceleration?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q3 2025 (6)

Was Frito-Lay North America's return to growth in the last month mostly an easier comparison, or innovation and everyday execution, on the way to flat fourth-quarter organic sales?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_pepsico_snack_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `snack_weight_quantity`, `snack_serving_quantity`
- `beverage.price.dim_pepsico_reporting_division`: `pepsico_reporting_division_id`, `pepsico_reporting_division_code`, `pepsico_reporting_division_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
- `beverage.price.fact_pepsico_snack_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `net_revenue_amount`

### Q3 2025 (8)

How are Frito-Lay North America price investments at entry price points on core brands performing?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.demand.fact_beverage_pack_volume`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `unit_case_quantity`, `package_quantity`
- `beverage.demand.fact_snack_pack_volume`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `snack_weight_quantity`
- `beverage.price.dim_cost_category`: `cost_category_id`, `cost_category_code`, `cost_category_name`
- `beverage.price.dim_pepsico_reporting_division`: `pepsico_reporting_division_id`, `pepsico_reporting_division_code`, `pepsico_reporting_division_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_pepsico_division_result`: `fiscal_quarter_id`, `scenario_id`, `pepsico_reporting_division_id`, `division_revenue_amount`, `division_operating_income_amount`
- `beverage.price.fact_pepsico_snack_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `net_revenue_amount`

### Q3 2025 (9)

Where has volume turned positive in the last four weeks, and is that company-wide or only where service levels recovered?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`
- `beverage.supply.dim_currency`: `currency_id`, `currency_code`, `currency_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`

### Q3 2025 (11)

Is the path back to the growth algorithm a U.S. cost-structure problem offset by international growth and U.S. innovation that may need a more complex supply chain?

- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`
- `beverage.supply.fact_packaging_mix_quantity`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `country_id`, `packaged_unit_case_quantity`

### Q3 2025 (12)

In the U.S., how much of the slowdown is structural healthier eating versus cyclical value-seeking, and how does that compare with international markets?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q3 2025 (13)

Is a stated margin target for Frito-Lay a useful way to set the path for that business?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_pepsico_reporting_division`: `pepsico_reporting_division_id`, `pepsico_reporting_division_code`, `pepsico_reporting_division_name`
- `beverage.price.dim_tax_type`: `tax_type_id`, `tax_type_code`, `tax_type_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.price.fact_pepsico_snack_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q4 2024 (1)

Why does 2025 earnings guidance imply less leverage than recent years, and does that mean a step-up in investment, including price investment at Frito-Lay, with a range left open so spend can rise if needed?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_pepsico_reporting_division`: `pepsico_reporting_division_id`, `pepsico_reporting_division_code`, `pepsico_reporting_division_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_enterprise_result`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `operating_income_amount`, `net_income_amount`, `operating_cash_flow_amount`, `free_cash_flow_amount`
- `beverage.price.fact_pepsico_division_result`: `fiscal_quarter_id`, `scenario_id`, `pepsico_reporting_division_id`, `division_revenue_amount`, `division_operating_income_amount`
- `beverage.price.fact_pepsico_snack_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.fact_packaging_mix_quantity`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `country_id`, `packaged_unit_case_quantity`

### Q4 2024 (4)

For Frito-Lay, which matters more: price running ahead of the wallet, a shift toward healthier choices, or snacks losing meal occasions to cheaper food?

- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_consumption_occasion`: `consumption_occasion_id`, `consumption_occasion_code`, `consumption_occasion_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_marketing_event`: `marketing_event_id`, `marketing_event_code`, `marketing_event_name`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_consumption_occasions`: `fiscal_quarter_id`, `scenario_id`, `consumption_occasion_id`, `product_category_id`, `country_id`, `consumer_cohort_id`, `occasion_quantity`
- `beverage.demand.fact_event_incremental_volume`: `fiscal_quarter_id`, `scenario_id`, `marketing_event_id`, `country_id`, `product_category_id`, `incremental_unit_case_quantity`
- `beverage.price.dim_pepsico_reporting_division`: `pepsico_reporting_division_id`, `pepsico_reporting_division_code`, `pepsico_reporting_division_name`
- `beverage.price.dim_tax_type`: `tax_type_id`, `tax_type_code`, `tax_type_name`
- `beverage.price.fact_pepsico_snack_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`

### Q4 2024 (5)

How much of the low-single-digit organic-sales outlook is international versus North America, and when should North America improve?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q4 2024 (6)

What is different in recent salty-snack trends that supports confidence the category is on better footing after earlier upturns reversed?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_consumption_occasion`: `consumption_occasion_id`, `consumption_occasion_code`, `consumption_occasion_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`

### Q4 2024 (7)

What infrastructure absorbed the one-time gains that were reinvested, and what is the 2025 expectation for advertising and marketing as a percent of sales after it rose in the fourth quarter?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_marketing_spending`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `product_category_id`, `marketing_spending_amount`, `advertising_spending_amount`
- `beverage.price.fact_pepsico_beverage_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `effective_price_change_percent`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`

### Q4 2024 (9)

What is the 2025 pricing and promotion approach in the international segment that was asked about alongside Mountain Dew?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q4 2024 (10)

How incremental is the latest beverage partnership, and how is the Mountain Dew franchise expected to perform?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q4 2024 (11)

Does rising GLP-1 use explain the salty-snack slowdown as outside studies suggest, or does that overstate the impact?

- `beverage.demand.dim_consumption_occasion`: `consumption_occasion_id`, `consumption_occasion_code`, `consumption_occasion_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_glp1_exposure`: `glp1_exposure_id`, `glp1_exposure_code`, `glp1_exposure_name`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_glp1_exposed_beverage_volume`: `fiscal_quarter_id`, `scenario_id`, `glp1_exposure_id`, `product_category_id`, `country_id`, `beverage_unit_case_quantity`
- `beverage.price.fact_pepsico_beverage_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_pepsico_snack_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_pepsico_snack_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `revenue_per_pound_amount`, `effective_price_change_percent`
- `beverage.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`

### Q4 2024 (13)

What about Europe allowed volume to improve even as pricing normalized, and is that balance sustainable next year?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.price.fact_pepsico_beverage_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_pepsico_beverage_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `effective_price_change_percent`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q4 2024 (14)

Can international profit still fund North America investment given the currency environment?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_currency_translation`: `fiscal_quarter_id`, `scenario_id`, `currency_id`, `country_id`, `translation_effect_amount`, `exchange_rate_amount`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_currency`: `currency_id`, `currency_code`, `currency_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
