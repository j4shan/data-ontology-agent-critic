# Beverage Inc demand and channel slice

This slice is part of the Beverage Inc warehouse. Quantity, capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

## Coca-Cola

### Q1 2026 (4)

How will the European Coke Zero relaunch sit alongside Diet Coke so the system does not starve one no-sugar trademark of attention?

- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_glp1_exposure`: `glp1_exposure_id`, `glp1_exposure_code`, `glp1_exposure_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_coca_cola_unit_case_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `unit_case_quantity`, `unit_case_growth_quantity`
- `beverage.demand.fact_concentrate_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `bottler_id`, `concentrate_shipment_quantity`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_coca_cola_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `price_mix_change_percent`, `price_change_percent`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`

### Q4 2025 (2)

How are worsening consumer conditions assumed to trend through 2026 relative to the milder backdrop described a few months earlier?

- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_consumption_occasion`: `consumption_occasion_id`, `consumption_occasion_code`, `consumption_occasion_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_marketing_event`: `marketing_event_id`, `marketing_event_code`, `marketing_event_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_concentrate_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `bottler_id`, `concentrate_shipment_quantity`
- `beverage.demand.fact_event_incremental_volume`: `fiscal_quarter_id`, `scenario_id`, `marketing_event_id`, `country_id`, `product_category_id`, `incremental_unit_case_quantity`
- `beverage.price.fact_concentrate_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `concentrate_revenue_amount`, `incidence_revenue_per_gallon_amount`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`

### Q4 2025 (6)

What sales uplift is expected from World Cup activation in the summer?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_marketing_event`: `marketing_event_id`, `marketing_event_code`, `marketing_event_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_event_incremental_volume`: `fiscal_quarter_id`, `scenario_id`, `marketing_event_id`, `country_id`, `product_category_id`, `incremental_unit_case_quantity`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q4 2025 (7)

Could the comparison with last year's temporary Hispanic-consumer disruption in North America help the first part of 2026?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_glp1_exposure`: `glp1_exposure_id`, `glp1_exposure_code`, `glp1_exposure_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_concentrate_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `bottler_id`, `concentrate_shipment_quantity`
- `beverage.demand.fact_glp1_exposed_beverage_volume`: `fiscal_quarter_id`, `scenario_id`, `glp1_exposure_id`, `product_category_id`, `country_id`, `beverage_unit_case_quantity`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`

### Q2 2025 (8)

How is the European consumer holding up versus other developed markets, given EMEA is expected to drive unit cases in the second half?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_glp1_exposure`: `glp1_exposure_id`, `glp1_exposure_code`, `glp1_exposure_name`
- `beverage.demand.dim_marketing_event`: `marketing_event_id`, `marketing_event_code`, `marketing_event_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_beverage_pack_volume`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `unit_case_quantity`, `package_quantity`
- `beverage.demand.fact_concentrate_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `bottler_id`, `concentrate_shipment_quantity`
- `beverage.demand.fact_event_incremental_volume`: `fiscal_quarter_id`, `scenario_id`, `marketing_event_id`, `country_id`, `product_category_id`, `incremental_unit_case_quantity`
- `beverage.demand.fact_glp1_exposed_beverage_volume`: `fiscal_quarter_id`, `scenario_id`, `glp1_exposure_id`, `product_category_id`, `country_id`, `beverage_unit_case_quantity`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`

### Q2 2025 (9)

With most refranchising done, how is the capability to create demand and recruit consumers actually intensifying?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_concentrate_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `bottler_id`, `concentrate_shipment_quantity`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`

### Q4 2024 (7)

Has GLP-1 use changed consumption, and has that changed innovation strategy?

- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_consumption_occasion`: `consumption_occasion_id`, `consumption_occasion_code`, `consumption_occasion_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_glp1_exposure`: `glp1_exposure_id`, `glp1_exposure_code`, `glp1_exposure_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_coca_cola_unit_case_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `unit_case_quantity`, `unit_case_growth_quantity`
- `beverage.demand.fact_concentrate_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `bottler_id`, `concentrate_shipment_quantity`
- `beverage.demand.fact_consumption_occasions`: `fiscal_quarter_id`, `scenario_id`, `consumption_occasion_id`, `product_category_id`, `country_id`, `consumer_cohort_id`, `occasion_quantity`
- `beverage.demand.fact_glp1_exposed_beverage_volume`: `fiscal_quarter_id`, `scenario_id`, `glp1_exposure_id`, `product_category_id`, `country_id`, `beverage_unit_case_quantity`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`
- `beverage.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`

### Q4 2024 (8)

Is Walmart's modern-soda shelf a fad or a lasting consumer shift, and how does Coca-Cola plan to compete there relative to something like fairlife?

- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_coca_cola_unit_case_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `unit_case_quantity`, `unit_case_growth_quantity`
- `beverage.demand.fact_concentrate_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `bottler_id`, `concentrate_shipment_quantity`
- `beverage.price.dim_tax_type`: `tax_type_id`, `tax_type_code`, `tax_type_name`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`
- `beverage.supply.fact_dairy_plant_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `coca_cola_trademark_id`, `dairy_capacity_quantity`, `dairy_production_quantity`

## PepsiCo

### Q2 2026 (2)

Were weaker-than-hoped Frito-Lay North America and PepsiCo Beverages North America volumes a shortfall in the new initiatives or the consumer backdrop?

- `beverage.demand.dim_consumption_occasion`: `consumption_occasion_id`, `consumption_occasion_code`, `consumption_occasion_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_glp1_exposure`: `glp1_exposure_id`, `glp1_exposure_code`, `glp1_exposure_name`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_pepsico_beverage_unit_case_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `unit_case_quantity`
- `beverage.demand.fact_pepsico_snack_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `snack_weight_quantity`, `snack_serving_quantity`
- `beverage.price.dim_pepsico_reporting_division`: `pepsico_reporting_division_id`, `pepsico_reporting_division_code`, `pepsico_reporting_division_name`
- `beverage.price.fact_pepsico_division_result`: `fiscal_quarter_id`, `scenario_id`, `pepsico_reporting_division_id`, `division_revenue_amount`, `division_operating_income_amount`
- `beverage.price.fact_pepsico_snack_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `net_revenue_amount`

### Q2 2026 (6)

How do category growth and consumer health differ across international regions, and should second-quarter international growth be extrapolated for the rest of the year?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_consumption_occasion`: `consumption_occasion_id`, `consumption_occasion_code`, `consumption_occasion_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_glp1_exposure`: `glp1_exposure_id`, `glp1_exposure_code`, `glp1_exposure_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_consumption_occasions`: `fiscal_quarter_id`, `scenario_id`, `consumption_occasion_id`, `product_category_id`, `country_id`, `consumer_cohort_id`, `occasion_quantity`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`

### Q1 2026 (2)

Is international demand still solid, or is there macro risk after the conflict?

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

### Q1 2026 (9)

Is the expected sequential improvement in Frito-Lay North America broad-based, or should organic sales keep rising from the 1% just reported, and what guardrails apply for the rest of the year?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_glp1_exposure`: `glp1_exposure_id`, `glp1_exposure_code`, `glp1_exposure_name`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.demand.fact_pepsico_snack_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `snack_weight_quantity`, `snack_serving_quantity`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_pepsico_snack_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`

### Q1 2026 (14)

What does World Cup activation look like for Frito-Lay versus past events, and is any uplift in the outlook?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_marketing_event`: `marketing_event_id`, `marketing_event_code`, `marketing_event_name`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.demand.fact_pepsico_snack_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `snack_weight_quantity`, `snack_serving_quantity`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_pepsico_snack_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`

### Q3 2025 (7)

How large a headwind is SKU rationalization on organic growth?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.demand.fact_beverage_pack_volume`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `unit_case_quantity`, `package_quantity`
- `beverage.demand.fact_snack_pack_volume`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `snack_weight_quantity`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`

### Q3 2025 (10)

Why address beverage protein with in-house brands such as Muscle Milk and Propel rather than buying or partnering, as in energy and prebiotic?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_pepsico_food_brand`: `pepsico_food_brand_id`, `pepsico_food_brand_code`, `pepsico_food_brand_name`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_pepsico_beverage_unit_case_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `unit_case_quantity`
- `beverage.demand.fact_pepsico_food_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_food_brand_id`, `sales_channel_id`, `food_weight_quantity`
- `beverage.demand.fact_pepsico_snack_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `snack_weight_quantity`, `snack_serving_quantity`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.supply.dim_currency`: `currency_id`, `currency_code`, `currency_name`

### Q4 2024 (2)

How is Frito-Lay and the beverage business being managed differently in 2025 than in the second half of last year, given a muted North America top line?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_glp1_exposure`: `glp1_exposure_id`, `glp1_exposure_code`, `glp1_exposure_name`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.demand.fact_pepsico_snack_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `snack_weight_quantity`, `snack_serving_quantity`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_pepsico_snack_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`

### Q4 2024 (3)

How did Mexico perform in the fourth quarter in the same subdued consumer environment?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_glp1_exposure`: `glp1_exposure_id`, `glp1_exposure_code`, `glp1_exposure_name`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_glp1_exposed_beverage_volume`: `fiscal_quarter_id`, `scenario_id`, `glp1_exposure_id`, `product_category_id`, `country_id`, `beverage_unit_case_quantity`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_pepsico_beverage_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_pepsico_beverage_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `effective_price_change_percent`

### Q4 2024 (12)

How aggressive does PepsiCo want to be in protein drinks given that segment's growth?

- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_pepsico_food_brand`: `pepsico_food_brand_id`, `pepsico_food_brand_code`, `pepsico_food_brand_name`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_pepsico_beverage_unit_case_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `unit_case_quantity`
- `beverage.demand.fact_pepsico_food_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_food_brand_id`, `sales_channel_id`, `food_weight_quantity`
- `beverage.demand.fact_pepsico_snack_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_snack_brand_id`, `sales_channel_id`, `snack_weight_quantity`, `snack_serving_quantity`
- `beverage.price.dim_pepsico_reporting_division`: `pepsico_reporting_division_id`, `pepsico_reporting_division_code`, `pepsico_reporting_division_name`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
