# Beverage Inc bottler and commodity supply slice

This slice is part of the Beverage Inc warehouse. Quantity, capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

## Coca-Cola

### Q4 2025 (5)

How will incremental fairlife capacity early in the year flow through brand growth over 2026?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`
- `beverage.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`
- `beverage.supply.fact_dairy_plant_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `coca_cola_trademark_id`, `dairy_capacity_quantity`, `dairy_production_quantity`

### Q4 2025 (13)

Should marketing and innovation step up in India as refranchising proceeds, and how far have B2B digital and analytics gone for store-level execution before the bottler takes demand fulfillment?

- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_consumption_occasion`: `consumption_occasion_id`, `consumption_occasion_code`, `consumption_occasion_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_marketing_event`: `marketing_event_id`, `marketing_event_code`, `marketing_event_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_concentrate_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `bottler_id`, `concentrate_shipment_quantity`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`
- `beverage.supply.fact_bottler_execution_capacity`: `fiscal_quarter_id`, `scenario_id`, `bottler_id`, `country_id`, `coca_cola_trademark_id`, `execution_slot_quantity`, `case_capacity_quantity`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`
- `beverage.supply.fact_refranchising_progress`: `fiscal_quarter_id`, `scenario_id`, `bottler_id`, `country_id`, `bottling_business_quantity`, `transferred_business_quantity`, `partner_ownership_percent`

### Q2 2025 (2)

How much U.S. volume does the early-2026 fairlife capacity add unlock, and does it let the three fairlife product lines be managed differently?

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
- `beverage.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `beverage.supply.fact_dairy_plant_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `coca_cola_trademark_id`, `dairy_capacity_quantity`, `dairy_production_quantity`

### Q2 2025 (6)

Where is consumer strength or weakness showing up globally beyond weather and geopolitics, and did June softness continue into July?

- `beverage.demand.dim_calendar_month`: `calendar_month_id`, `calendar_month_code`, `calendar_month_name`, `fiscal_quarter_id`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_consumption_occasion`: `consumption_occasion_id`, `consumption_occasion_code`, `consumption_occasion_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_concentrate_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `bottler_id`, `concentrate_shipment_quantity`
- `beverage.demand.fact_consumption_occasions`: `fiscal_quarter_id`, `scenario_id`, `consumption_occasion_id`, `product_category_id`, `country_id`, `consumer_cohort_id`, `occasion_quantity`
- `beverage.demand.fact_monthly_unit_case_volume`: `fiscal_quarter_id`, `scenario_id`, `calendar_month_id`, `country_id`, `coca_cola_trademark_id`, `unit_case_quantity`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`

### Q2 2025 (7)

How do consumer preferences for cane and fiber shape innovation, and how is Simply Pop performing against competitors launching prebiotic drinks under a core trademark?

- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_consumption_occasion`: `consumption_occasion_id`, `consumption_occasion_code`, `consumption_occasion_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_concentrate_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `bottler_id`, `concentrate_shipment_quantity`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.fact_bottler_execution_capacity`: `fiscal_quarter_id`, `scenario_id`, `bottler_id`, `country_id`, `coca_cola_trademark_id`, `execution_slot_quantity`, `case_capacity_quantity`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`
- `beverage.supply.fact_packaging_mix_quantity`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `country_id`, `packaged_unit_case_quantity`

### Q4 2024 (5)

Where does the largely local supply chain still have import and export exposure if tariffs rise?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_glp1_exposure`: `glp1_exposure_id`, `glp1_exposure_code`, `glp1_exposure_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`
- `beverage.supply.fact_trade_lane_quantity`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `commodity_id`, `plant_id`, `imported_quantity`, `exported_quantity`

### Q4 2024 (10)

How much of North America's strong price/mix was fairlife or away-from-home, and does that comparison force a slowdown or is more distribution still available?

- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.dim_plant`: `plant_id`, `plant_name`, `country_id`, `plant_function_id`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`
- `beverage.supply.fact_dairy_plant_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `coca_cola_trademark_id`, `dairy_capacity_quantity`, `dairy_production_quantity`
- `beverage.supply.fact_packaging_mix_quantity`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `country_id`, `packaged_unit_case_quantity`

### Q4 2024 (11)

What does the local partner that took 40% of the India bottling business bring that could accelerate that market?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_coca_cola_trademark`: `coca_cola_trademark_id`, `coca_cola_trademark_code`, `coca_cola_trademark_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_coca_cola_net_revenue`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `net_revenue_amount`
- `beverage.price.fact_coca_cola_price_realization`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `coca_cola_trademark_id`, `sales_channel_id`, `revenue_per_unit_case_amount`, `price_mix_change_percent`, `price_change_percent`
- `beverage.supply.dim_bottler`: `bottler_id`, `bottler_name`, `country_id`, `bottler_ownership_id`
- `beverage.supply.dim_plant_function`: `plant_function_id`, `plant_function_code`, `plant_function_name`
- `beverage.supply.fact_refranchising_progress`: `fiscal_quarter_id`, `scenario_id`, `bottler_id`, `country_id`, `bottling_business_quantity`, `transferred_business_quantity`, `partner_ownership_percent`

### Q4 2024 (12)

How large a shift from aluminum cans toward plastic is required to offset a sharp rise in can cost?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_beverage_pack_volume`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `unit_case_quantity`, `package_quantity`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`
- `beverage.supply.fact_packaging_mix_quantity`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `country_id`, `packaged_unit_case_quantity`

## PepsiCo

### Q2 2026 (7)

Are affordability, package, and innovation actions already in market and now a matter of scaling, or are further catalysts still ahead?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_region`: `region_id`, `region_code`, `region_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.dim_tax_type`: `tax_type_id`, `tax_type_code`, `tax_type_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_organic_revenue_growth`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `country_id`, `organic_growth_percent`, `volume_contribution_percent`, `price_contribution_percent`
- `beverage.price.fact_price_bridge`: `fiscal_quarter_id`, `scenario_id`, `price_bridge_component_id`, `region_id`, `product_category_id`, `bridge_contribution_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`

### Q1 2026 (1)

What cost assumptions changed because of the Iran conflict, how locked are hedges and contracts, and what internal offsets protect 2026 earnings visibility?

- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.price.dim_price_bridge_component`: `price_bridge_component_id`, `price_bridge_component_code`, `price_bridge_component_name`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `country_id`, `input_cost_amount`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`

### Q1 2026 (10)

Has competitive pricing or shelf behavior intensified, and could industry cost inflation interrupt PepsiCo's own affordability investments?

- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_pepsico_food_brand`: `pepsico_food_brand_id`, `pepsico_food_brand_code`, `pepsico_food_brand_name`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_finished_beverage_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `product_category_id`, `delivery_process_id`, `finished_case_quantity`, `shipped_unit_case_quantity`
- `beverage.demand.fact_pepsico_beverage_unit_case_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `unit_case_quantity`
- `beverage.demand.fact_pepsico_food_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_food_brand_id`, `sales_channel_id`, `food_weight_quantity`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.dim_delivery_process`: `delivery_process_id`, `delivery_process_code`, `delivery_process_name`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`

### Q3 2025 (5)

What is driving better U.S. Pepsi brand momentum and share, messaging or more marketing, and does optimizing marketing ROI mean lower spend?

- `beverage.demand.dim_consumer_cohort`: `consumer_cohort_id`, `consumer_cohort_code`, `consumer_cohort_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_marketing_event`: `marketing_event_id`, `marketing_event_code`, `marketing_event_name`
- `beverage.demand.dim_pepsico_beverage_brand`: `pepsico_beverage_brand_id`, `pepsico_beverage_brand_code`, `pepsico_beverage_brand_name`
- `beverage.demand.dim_pepsico_food_brand`: `pepsico_food_brand_id`, `pepsico_food_brand_code`, `pepsico_food_brand_name`
- `beverage.demand.dim_pepsico_snack_brand`: `pepsico_snack_brand_id`, `pepsico_snack_brand_code`, `pepsico_snack_brand_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.dim_snack_pack`: `snack_pack_id`, `snack_pack_code`, `snack_pack_name`
- `beverage.demand.fact_pepsico_beverage_unit_case_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_beverage_brand_id`, `sales_channel_id`, `unit_case_quantity`
- `beverage.demand.fact_pepsico_food_volume`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `pepsico_food_brand_id`, `sales_channel_id`, `food_weight_quantity`
- `beverage.price.fact_snack_pack_price`: `fiscal_quarter_id`, `scenario_id`, `snack_pack_id`, `pepsico_snack_brand_id`, `country_id`, `pack_price_change_percent`
- `beverage.supply.dim_commodity`: `commodity_id`, `commodity_code`, `commodity_name`
- `beverage.supply.fact_commodity_cover_duration`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `coverage_duration_months`

### Q4 2024 (8)

Has the view of the energy-drink category or PepsiCo's platform changed, and what execution or partner actions are planned to grow that part of the portfolio?

- `beverage.demand.dim_beverage_pack`: `beverage_pack_id`, `beverage_pack_code`, `beverage_pack_name`
- `beverage.demand.dim_country`: `country_id`, `country_name`, `region_id`
- `beverage.demand.dim_customer`: `customer_id`, `customer_name`, `customer_type_id`
- `beverage.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`, `fiscal_year`, `quarter_number`
- `beverage.demand.dim_product_category`: `product_category_id`, `product_category_code`, `product_category_name`
- `beverage.demand.dim_sales_channel`: `sales_channel_id`, `sales_channel_code`, `sales_channel_name`
- `beverage.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `beverage.demand.fact_finished_beverage_shipments`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `product_category_id`, `delivery_process_id`, `finished_case_quantity`, `shipped_unit_case_quantity`
- `beverage.price.dim_tax_type`: `tax_type_id`, `tax_type_code`, `tax_type_name`
- `beverage.price.fact_beverage_pack_price`: `fiscal_quarter_id`, `scenario_id`, `beverage_pack_id`, `product_category_id`, `country_id`, `pack_price_change_percent`
- `beverage.price.fact_packaging_cost`: `fiscal_quarter_id`, `scenario_id`, `packaging_material_id`, `product_category_id`, `packaging_cost_amount`, `cost_change_percent`
- `beverage.supply.dim_delivery_process`: `delivery_process_id`, `delivery_process_code`, `delivery_process_name`
- `beverage.supply.dim_packaging_material`: `packaging_material_id`, `packaging_material_code`, `packaging_material_name`
- `beverage.supply.fact_case_fill_rate`: `fiscal_quarter_id`, `scenario_id`, `country_id`, `customer_id`, `product_category_id`, `case_fill_percent`
