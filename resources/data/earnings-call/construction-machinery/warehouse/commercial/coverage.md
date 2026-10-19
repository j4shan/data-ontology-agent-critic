# Machinery Inc price, volume, backlog, trucks, and parts

Dealer stock is inventory on its own quantity fact, not a retail channel. Caterpillar machine and power processes and PACCAR truck, parts, and finance processes use separate facts and separate reporting-segment dimensions. Quantity, capacity, and price or margin are separate facts joined by fiscal period, scenario, and the business keys. Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks.

## Numbered questions

## Caterpillar

### Q2 2026 (4) Caterpillar

How much of the backlog increase was large power awards versus broad-based orders?

- `machinery.commercial.fact_cat_order_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `order_size_class_id`, `demand_motive_id`, `order_amount`
- `machinery.commercial.fact_cat_backlog_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `backlog_amount`, `backlog_change_amount`
- `machinery.commercial.fact_cat_order_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `order_units`

### Q2 2026 (10) Caterpillar

How large are orders already in hand for fourth-quarter 10-megawatt engine deliveries, and what extra cost comes with ramping that capacity?

- `machinery.commercial.fact_capacity_ramp_cost`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `cat_reporting_segment_id`, `capacity_ramp_cost_amount`
- `machinery.commercial.fact_cat_order_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `order_size_class_id`, `demand_motive_id`, `order_amount`
- `machinery.commercial.fact_cat_order_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `order_units`

### Q1 2026 (2) Caterpillar

Why is the long-term margin view unchanged after a higher sales outlook that should improve fixed-cost absorption?

- `machinery.commercial.fact_enterprise_earnings`: `accounting_period_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `machinery.commercial.fact_price_cost_bridge`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `price_effect_amount`, `cost_effect_amount`
- `machinery.commercial.fact_manufacturing_cost`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `manufacturing_cost_amount`

### Q1 2026 (4) Caterpillar

Does today's capacity change the 2030 gigawatt figure, and should Power & Energy price realization stay near the recent low-single-digit rate as new products arrive?

- `machinery.commercial.fact_power_price`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `engine_fuel_id`, `power_size_class_id`, `price_dollars_per_kilowatt`, `price_change_percent`
- `machinery.commercial.fact_machine_price`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `price_dollars_per_machine`, `price_change_percent`
- `machinery.commercial.fact_cat_backlog_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `backlog_amount`, `backlog_change_amount`

### Q1 2026 (6) Caterpillar

How should mining orders, the strongest since 2012, be reconciled with negative price and tariff-hit margins, and what does that mean for segment profitability as the cycle builds?

- `machinery.commercial.fact_price_cost_bridge`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `price_effect_amount`, `cost_effect_amount`
- `machinery.commercial.fact_cat_segment_margin`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `operating_profit_amount`, `operating_margin_percent`
- `machinery.commercial.fact_cat_order_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `order_units`

### Q4 2025 (1) Caterpillar

What is happening to orders and backlog outside power generation?

- `machinery.commercial.fact_cat_order_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `order_size_class_id`, `demand_motive_id`, `order_amount`
- `machinery.commercial.fact_cat_order_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `order_units`
- `machinery.commercial.fact_cat_backlog_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `backlog_units`

### Q4 2025 (3) Caterpillar

Why is 2026 sales growth modest when the backlog shipping in the next twelve months and orders are up sharply and retail is expected to rise?

- `machinery.commercial.fact_cat_backlog_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `backlog_amount`, `backlog_change_amount`
- `machinery.commercial.fact_cat_order_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `order_size_class_id`, `demand_motive_id`, `order_amount`
- `machinery.commercial.fact_cat_backlog_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `backlog_units`

### Q4 2024 (3) Caterpillar

Why is price/cost negative for the margin outlook when manufacturing cost had been a year-over-year help?

- `machinery.commercial.fact_price_cost_bridge`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `price_effect_amount`, `cost_effect_amount`
- `machinery.commercial.fact_enterprise_earnings`: `accounting_period_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `machinery.commercial.fact_manufacturing_cost`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `manufacturing_cost_amount`

### Q4 2024 (5) Caterpillar

What would push the operating-profit outlook from the top of the range back toward the midpoint?

- `machinery.commercial.fact_enterprise_earnings`: `accounting_period_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `machinery.commercial.fact_cat_segment_margin`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `operating_profit_amount`, `operating_margin_percent`
- `machinery.commercial.fact_cat_order_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `order_units`

### Q4 2024 (6) Caterpillar

How large were the delayed Energy & Transportation shipments, when do they land, and how does new capacity support 2025 growth after a softer 2024?

- `machinery.commercial.fact_delayed_shipment_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `delayed_shipment_amount`, `landed_shipment_amount`
- `machinery.commercial.fact_power_price`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `engine_fuel_id`, `power_size_class_id`, `price_dollars_per_kilowatt`, `price_change_percent`
- `machinery.commercial.fact_cat_order_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `order_size_class_id`, `demand_motive_id`, `order_amount`

### Q4 2024 (9) Caterpillar

If company sales are slightly lower, is inventory absorption a margin headwind for the whole company, not just construction?

- `machinery.commercial.fact_manufacturing_cost`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `manufacturing_cost_amount`
- `machinery.commercial.fact_cat_order_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `order_units`
- `machinery.commercial.fact_cat_segment_revenue`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `revenue_amount`

### Q4 2024 (10) Caterpillar

What supports pricing in the second half as merchandise programs roll off and comparisons get easier?

- `machinery.commercial.fact_merchandise_price_support`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `price_support_amount`
- `machinery.commercial.fact_machine_price`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `price_dollars_per_machine`, `price_change_percent`
- `machinery.commercial.fact_delayed_shipment_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `delayed_shipment_amount`, `landed_shipment_amount`

### Q4 2024 (11) Caterpillar

Is the margin framework still the right range after strong performance, even with a negative price impact?

- `machinery.commercial.fact_enterprise_earnings`: `accounting_period_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `machinery.commercial.fact_price_cost_bridge`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `price_effect_amount`, `cost_effect_amount`
- `machinery.commercial.fact_machine_price`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `price_dollars_per_machine`, `price_change_percent`

## PACCAR

### Q2 2026 (1) PACCAR

What moving parts made gross margin stronger than expected?

- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`
- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`
- `machinery.truck.fact_paccar_parts_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_units`

### Q2 2026 (2) PACCAR

Is market pricing rising, and does a higher local-for-local mix create more room to realize it?

- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`
- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`
- `machinery.truck.fact_truck_market_quantity`: `accounting_period_id`, `scenario_id`, `vehicle_class_id`, `region_id`, `industry_retail_units`

### Q2 2026 (3) PACCAR

Did an emissions-rule refund, rather than underlying cost, drive the strong profit per truck?

- `machinery.truck.fact_emissions_compliance_cost`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `emissions_standard_id`, `compliance_cost_dollars_per_truck`, `penalty_dollars_per_truck`
- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`
- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`

### Q2 2026 (4) PACCAR

Is the expected step-up in price realization still happening under the more phased emissions rollout?

- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`
- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`
- `machinery.truck.fact_emissions_compliance_cost`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `emissions_standard_id`, `compliance_cost_dollars_per_truck`, `penalty_dollars_per_truck`

### Q2 2026 (5) PACCAR

Why is third-quarter gross margin guided roughly flat despite higher deliveries and a richer North American mix while Europe is shut down?

- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`
- `machinery.truck.fact_truck_delivery_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_delivery_units`
- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`

### Q2 2026 (6) PACCAR

If the noncompliance penalty is below the cost of a compliant engine, how does that change the product and pricing strategy?

- `machinery.truck.fact_emissions_compliance_cost`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `emissions_standard_id`, `compliance_cost_dollars_per_truck`, `penalty_dollars_per_truck`
- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`
- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`

### Q2 2026 (7) PACCAR

Are customers prebuying ahead of the emissions change, or do they simply need trucks?

- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`
- `machinery.truck.fact_truck_dealer_inventory_quantity`: `accounting_period_id`, `scenario_id`, `paccar_dealer_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `dealer_stock_units`, `dealer_stock_change_units`
- `machinery.truck.fact_emissions_compliance_cost`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `emissions_standard_id`, `compliance_cost_dollars_per_truck`, `penalty_dollars_per_truck`

### Q2 2026 (8) PACCAR

Do emissions credits give any competitor a share or price advantage in 2027?

- `machinery.truck.fact_emissions_credit_quantity`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `emissions_standard_id`, `emissions_credit_count`
- `machinery.truck.fact_emissions_compliance_cost`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `emissions_standard_id`, `compliance_cost_dollars_per_truck`, `penalty_dollars_per_truck`
- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`

### Q2 2026 (9) PACCAR

What cadence are suppliers being asked to support from the fourth quarter into the first, and what supports parts growth exiting the year?

- `machinery.truck.fact_paccar_parts_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_units`
- `machinery.truck.fact_truck_production_quantity`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_production_units`, `build_slot_count`
- `machinery.truck.fact_truck_supplier_capacity`: `accounting_period_id`, `scenario_id`, `supplier_id`, `truck_component_id`, `component_capacity_units`

### Q2 2026 (10) PACCAR

As over-the-road demand broadens from large fleets to smaller fleets, how do parts margins change?

- `machinery.truck.fact_paccar_parts_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_units`
- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`
- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`

### Q2 2026 (11) PACCAR

Why were U.S. and Canada deliveries down, and what share of the next quarter's deliveries is that region?

- `machinery.truck.fact_truck_delivery_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_delivery_units`
- `machinery.truck.fact_truck_market_quantity`: `accounting_period_id`, `scenario_id`, `vehicle_class_id`, `region_id`, `industry_retail_units`
- `machinery.truck.fact_truck_backlog_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `truck_backlog_units`

### Q2 2026 (12) PACCAR

Why keep a wide U.S. and Canada retail range rather than narrowing it with half the year gone?

- `machinery.truck.fact_truck_market_quantity`: `accounting_period_id`, `scenario_id`, `vehicle_class_id`, `region_id`, `industry_retail_units`
- `machinery.truck.fact_truck_delivery_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_delivery_units`
- `machinery.truck.fact_truck_market_share`: `accounting_period_id`, `scenario_id`, `vehicle_class_id`, `region_id`, `market_share_percent`

### Q2 2026 (13) PACCAR

If freight rates are rising because there are fewer drivers rather than more freight, does that change how high orders and builds can go, and is fleet growth showing up?

- `machinery.truck.fact_freight_market_quantity`: `accounting_period_id`, `scenario_id`, `region_id`, `freight_load_count`
- `machinery.truck.fact_freight_rate`: `accounting_period_id`, `scenario_id`, `region_id`, `freight_rate_dollars_per_mile`
- `machinery.truck.fact_paccar_parts_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_units`

### Q2 2026 (14) PACCAR

Can orders placed as a 2026 prebuy now be pushed into 2027?

- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`
- `machinery.truck.fact_truck_backlog_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `truck_backlog_units`
- `machinery.truck.fact_emissions_compliance_cost`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `emissions_standard_id`, `compliance_cost_dollars_per_truck`, `penalty_dollars_per_truck`

### Q1 2026 (1) PACCAR

Why did parts start slowly, how does the second quarter look, and does the back half improve as orders pick up?

- `machinery.truck.fact_paccar_parts_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_units`
- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`
- `machinery.truck.fact_truck_backlog_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `truck_backlog_units`

### Q1 2026 (2) PACCAR

How much of the jump in profit per truck was cost execution versus mix?

- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`
- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`
- `machinery.truck.fact_emissions_compliance_cost`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `emissions_standard_id`, `compliance_cost_dollars_per_truck`, `penalty_dollars_per_truck`

### Q1 2026 (3) PACCAR

Do the simplified metal tariffs change the expected hit to aftermarket parts versus trucks?

- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`
- `machinery.truck.fact_paccar_parts_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_units`
- `machinery.commercial.fact_tariff_cost`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `country_id`, `tariff_cost_amount`

### Q1 2026 (4) PACCAR

Is the conflict showing up in European orders, and what is PACCAR seeing as electric trucks rise sharply in China?

- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`
- `machinery.truck.fact_paccar_parts_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_units`
- `machinery.truck.fact_truck_backlog_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `truck_backlog_units`

### Q1 2026 (5) PACCAR

Was the sequential jump in truck gross profit a reversal of older tariffs?

- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`
- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`
- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`

### Q1 2026 (6) PACCAR

How many shifts or build slots are planned for a prebuy later this year versus the current rate and last year?

- `machinery.truck.fact_truck_production_quantity`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_production_units`, `build_slot_count`
- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`
- `machinery.truck.fact_truck_backlog_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `truck_backlog_units`

### Q1 2026 (7) PACCAR

Could memory chips or aluminum constrain the second-half build, and how is mix tracking versus that ramp?

- `machinery.truck.fact_truck_supplier_capacity`: `accounting_period_id`, `scenario_id`, `supplier_id`, `truck_component_id`, `component_capacity_units`
- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`
- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`

### Q1 2026 (8) PACCAR

How should price momentum and price versus cost progress from the second quarter through the second half?

- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`
- `machinery.commercial.fact_price_cost_bridge`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `price_effect_amount`, `cost_effect_amount`
- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`

### Q1 2026 (9) PACCAR

How will incremental margins this cycle compare with the last cycle, given tariffs and a share opportunity rather than a wave of new products?

- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`
- `machinery.commercial.fact_price_cost_bridge`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `price_effect_amount`, `cost_effect_amount`
- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`

### Q1 2026 (10) PACCAR

What drives the expected second-half parts acceleration, and does it still require higher freight rates?

- `machinery.truck.fact_freight_market_quantity`: `accounting_period_id`, `scenario_id`, `region_id`, `freight_load_count`
- `machinery.truck.fact_freight_rate`: `accounting_period_id`, `scenario_id`, `region_id`, `freight_rate_dollars_per_mile`
- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`

### Q1 2026 (11) PACCAR

Are customer conversations about 2027 a prebuy or ordinary replacement demand?

- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`
- `machinery.truck.fact_emissions_compliance_cost`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `emissions_standard_id`, `compliance_cost_dollars_per_truck`, `penalty_dollars_per_truck`
- `machinery.truck.fact_truck_backlog_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `truck_backlog_units`

### Q1 2026 (12) PACCAR

Are customers pushing delivery dates out, and when does the announced production credit apply?

- `machinery.truck.fact_truck_delivery_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_delivery_units`
- `machinery.truck.fact_truck_backlog_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `truck_backlog_units`
- `machinery.truck.fact_emissions_compliance_cost`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `emissions_standard_id`, `compliance_cost_dollars_per_truck`, `penalty_dollars_per_truck`

### Q1 2026 (13) PACCAR

How much of the non-prebuy demand is fleet growth versus replacement, and does more replacement pressure parts growth?

- `machinery.truck.fact_paccar_parts_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_units`
- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`
- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`

### Q1 2026 (14) PACCAR

Is backlog mix shifting from small fleets toward large fleets, and how does that affect truck margins and lease and rental?

- `machinery.truck.fact_paccar_financial_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `financial_services_revenue_amount`, `lease_revenue_amount`
- `machinery.truck.fact_paccar_parts_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_units`
- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`

### Q4 2025 (3) PACCAR

How should the fourth-quarter price-cost gap be framed against the tariff benefit expected in the first quarter?

- `machinery.commercial.fact_price_cost_bridge`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `price_effect_amount`, `cost_effect_amount`
- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`
- `machinery.commercial.fact_manufacturing_cost`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `manufacturing_cost_amount`

### Q4 2025 (4) PACCAR

As tariffs hit competitors, does PACCAR prioritize market share or profit per truck?

- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`
- `machinery.truck.fact_truck_market_quantity`: `accounting_period_id`, `scenario_id`, `vehicle_class_id`, `region_id`, `industry_retail_units`
- `machinery.truck.fact_truck_market_share`: `accounting_period_id`, `scenario_id`, `vehicle_class_id`, `region_id`, `market_share_percent`

### Q4 2025 (5) PACCAR

As the market normalizes, should truck margins differ from the historical cycle average?

- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`
- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`
- `machinery.truck.fact_truck_market_quantity`: `accounting_period_id`, `scenario_id`, `vehicle_class_id`, `region_id`, `industry_retail_units`

### Q4 2025 (6) PACCAR

How much of the U.S. and Canada production shortfall was the shift to local-for-local manufacturing?

- `machinery.truck.fact_truck_delivery_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_delivery_units`
- `machinery.truck.fact_truck_production_quantity`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_production_units`, `build_slot_count`
- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`

### Q4 2025 (7) PACCAR

How does a flat first quarter split between the U.S. and Canada and Europe?

- `machinery.truck.fact_truck_delivery_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_delivery_units`
- `machinery.truck.fact_truck_market_quantity`: `accounting_period_id`, `scenario_id`, `vehicle_class_id`, `region_id`, `industry_retail_units`
- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`

### Q4 2025 (8) PACCAR

How full are first- and second-quarter build slots after the January order strength?

- `machinery.truck.fact_truck_backlog_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `truck_backlog_units`
- `machinery.truck.fact_truck_production_quantity`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_production_units`, `build_slot_count`
- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`

### Q4 2025 (10) PACCAR

If higher truck rates reflect fewer drivers rather than more freight, what does that mean for orders this cycle?

- `machinery.truck.fact_freight_market_quantity`: `accounting_period_id`, `scenario_id`, `region_id`, `freight_load_count`
- `machinery.truck.fact_freight_rate`: `accounting_period_id`, `scenario_id`, `region_id`, `freight_rate_dollars_per_mile`
- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`

### Q4 2025 (11) PACCAR

Is the order pickup replacement or fleet growth, and how does that change the used-truck market?

- `machinery.truck.fact_freight_market_quantity`: `accounting_period_id`, `scenario_id`, `region_id`, `freight_load_count`
- `machinery.truck.fact_paccar_parts_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_units`
- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`

### Q4 2025 (12) PACCAR

How does parts gross margin scale in 2026 as that business reaccelerates?

- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`
- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`
- `machinery.truck.fact_paccar_parts_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_units`

### Q4 2025 (13) PACCAR

Where do PACCAR and industry truck inventories stand, and how does truck pricing evolve through the year?

- `machinery.truck.fact_truck_dealer_inventory_quantity`: `accounting_period_id`, `scenario_id`, `paccar_dealer_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `dealer_stock_units`, `dealer_stock_change_units`
- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`
- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`

### Q4 2025 (15) PACCAR

What price increase for the 2027 emissions engines has been communicated to customers?

- `machinery.truck.fact_emissions_compliance_cost`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `emissions_standard_id`, `compliance_cost_dollars_per_truck`, `penalty_dollars_per_truck`
- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`
- `machinery.truck.fact_emissions_credit_quantity`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `emissions_standard_id`, `emissions_credit_count`

### Q4 2025 (16) PACCAR

Would production be flexed up for a stronger prebuy, or kept limited because 2027 demand is expected to fall after the rule?

- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`
- `machinery.truck.fact_emissions_compliance_cost`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `emissions_standard_id`, `compliance_cost_dollars_per_truck`, `penalty_dollars_per_truck`
- `machinery.truck.fact_truck_production_quantity`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_production_units`, `build_slot_count`

### Q4 2025 (17) PACCAR

How much dealer stocking is expected ahead of the emissions change?

- `machinery.truck.fact_truck_dealer_inventory_quantity`: `accounting_period_id`, `scenario_id`, `paccar_dealer_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `dealer_stock_units`, `dealer_stock_change_units`
- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`
- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`

### Q4 2025 (18) PACCAR

Are last year's tariff surcharges being rolled back now that the newer tariff rules ease the cost?

- `machinery.commercial.fact_price_cost_bridge`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `price_effect_amount`, `cost_effect_amount`
- `machinery.commercial.fact_manufacturing_cost`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `manufacturing_cost_amount`
- `machinery.commercial.fact_tariff_cost`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `country_id`, `tariff_cost_amount`

### Q3 2025 (1) PACCAR

Does the tariff regime improve PACCAR's competitive position given where competitors build, and when does the rebate hit results?

- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`
- `machinery.commercial.fact_tariff_cost`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `country_id`, `tariff_cost_amount`
- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`

### Q3 2025 (2) PACCAR

Now that tariff rules are clearer, do price increases start to offset the cost?

- `machinery.commercial.fact_price_cost_bridge`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `price_effect_amount`, `cost_effect_amount`
- `machinery.commercial.fact_manufacturing_cost`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `manufacturing_cost_amount`
- `machinery.commercial.fact_tariff_cost`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `country_id`, `tariff_cost_amount`

### Q3 2025 (4) PACCAR

What deadline does the emissions agency face if the 2027 rule changes, given supplier planning?

- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`
- `machinery.truck.fact_emissions_compliance_cost`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `emissions_standard_id`, `compliance_cost_dollars_per_truck`, `penalty_dollars_per_truck`
- `machinery.truck.fact_emissions_credit_quantity`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `emissions_standard_id`, `emissions_credit_count`

### Q3 2025 (5) PACCAR

At full run rate, how does the rebate compare with tariff costs on parts, steel, and aluminum?

- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`
- `machinery.commercial.fact_price_cost_bridge`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `price_effect_amount`, `cost_effect_amount`
- `machinery.commercial.fact_manufacturing_cost`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `manufacturing_cost_amount`

### Q3 2025 (8) PACCAR

Does the North America outlook still assume an emissions prebuy?

- `machinery.truck.fact_emissions_compliance_cost`: `accounting_period_id`, `scenario_id`, `truck_brand_id`, `vehicle_class_id`, `emissions_standard_id`, `compliance_cost_dollars_per_truck`, `penalty_dollars_per_truck`
- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`
- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`

### Q3 2025 (9) PACCAR

What truck pricing was realized in the quarter, and what is expected next quarter?

- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`
- `machinery.truck.fact_truck_margin`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `gross_profit_amount`, `gross_margin_percent`, `profit_dollars_per_truck`
- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`

### Q3 2025 (11) PACCAR

With the tariff offset in place for several years, does parts and component sourcing move more production to the U.S.?

- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`
- `machinery.truck.fact_truck_delivery_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_delivery_units`
- `machinery.truck.fact_paccar_parts_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_units`

### Q3 2025 (12) PACCAR

Will any of the pricing taken to cover tariffs be given back to gain share?

- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`
- `machinery.truck.fact_truck_market_quantity`: `accounting_period_id`, `scenario_id`, `vehicle_class_id`, `region_id`, `industry_retail_units`
- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`

### Q3 2025 (13) PACCAR

How much excess truck capacity is in fleets relative to freight demand?

- `machinery.truck.fact_freight_market_quantity`: `accounting_period_id`, `scenario_id`, `region_id`, `freight_load_count`
- `machinery.truck.fact_paccar_parts_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_units`
- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`

### Q3 2025 (14) PACCAR

If customers keep trucks longer, what does that mean for parts next year?

- `machinery.truck.fact_paccar_parts_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_units`
- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`
- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`

### Q3 2025 (15) PACCAR

Are rebate savings passed through by simply removing the existing per-truck tariff surcharge?

- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`
- `machinery.truck.fact_truck_order_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_order_units`
- `machinery.truck.fact_truck_delivery_quantity`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `truck_delivery_units`

### Q3 2025 (18) PACCAR

Do tariff surcharges fade while core price increases continue?

- `machinery.commercial.fact_price_cost_bridge`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `cost_element_id`, `price_effect_amount`, `cost_effect_amount`
- `machinery.truck.fact_truck_price`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `truck_brand_id`, `vehicle_class_id`, `region_id`, `price_dollars_per_truck`, `price_change_percent`
- `machinery.truck.fact_paccar_parts_amount`: `accounting_period_id`, `scenario_id`, `paccar_reporting_segment_id`, `customer_fleet_type_id`, `parts_revenue_amount`, `parts_margin_percent`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `machinery.commercial.dim_currency` | supporting population |
| `machinery.commercial.dim_cost_element` | supporting population |
| `machinery.commercial.dim_order_size_class` | supporting population |
| `machinery.commercial.dim_demand_motive` | supporting population |
| `machinery.truck.dim_truck_brand` | supporting population |
| `machinery.truck.dim_vehicle_class` | supporting population |
| `machinery.truck.dim_paccar_dealer` | supporting population |
| `machinery.truck.dim_truck_component` | supporting population |
| `machinery.truck.dim_customer_fleet_type` | supporting population |
| `machinery.commercial.dim_competitor` | supporting population |
| `machinery.commercial.dim_emissions_standard` | supporting population |
| `machinery.commercial.fact_cat_order_quantity` | Q2 2026 (4), Q2 2026 (10), Q1 2026 (6), Q4 2025 (1), Q4 2024 (5), Q4 2024 (9) |
| `machinery.commercial.fact_cat_order_amount` | Q2 2026 (4), Q2 2026 (10), Q4 2025 (1), Q4 2025 (3), Q4 2024 (6) |
| `machinery.commercial.fact_cat_backlog_quantity` | Q4 2025 (1), Q4 2025 (3) |
| `machinery.commercial.fact_cat_backlog_amount` | Q2 2026 (4), Q1 2026 (4), Q4 2025 (3) |
| `machinery.commercial.fact_machine_price` | Q1 2026 (4), Q4 2024 (10), Q4 2024 (11) |
| `machinery.commercial.fact_power_price` | Q1 2026 (4), Q4 2024 (6) |
| `machinery.commercial.fact_cat_segment_revenue` | Q4 2024 (9) |
| `machinery.commercial.fact_cat_segment_margin` | Q1 2026 (6), Q4 2024 (5) |
| `machinery.commercial.fact_enterprise_earnings` | Q1 2026 (2), Q4 2024 (3), Q4 2024 (5), Q4 2024 (11) |
| `machinery.commercial.fact_price_cost_bridge` | Q1 2026 (2), Q1 2026 (6), Q4 2024 (3), Q4 2024 (11), Q1 2026 (8), Q1 2026 (9), Q4 2025 (3), Q4 2025 (18), Q3 2025 (2), Q3 2025 (5), Q3 2025 (18) |
| `machinery.commercial.fact_manufacturing_cost` | Q1 2026 (2), Q4 2024 (3), Q4 2024 (9), Q4 2025 (3), Q4 2025 (18), Q3 2025 (2), Q3 2025 (5) |
| `machinery.commercial.fact_tariff_cost` | Q1 2026 (3), Q4 2025 (18), Q3 2025 (1), Q3 2025 (2) |
| `machinery.commercial.fact_capacity_ramp_cost` | Q2 2026 (10) |
| `machinery.commercial.fact_delayed_shipment_amount` | Q4 2024 (6), Q4 2024 (10) |
| `machinery.truck.fact_truck_order_quantity` | Q2 2026 (14), Q1 2026 (1), Q1 2026 (4), Q1 2026 (5), Q1 2026 (6), Q1 2026 (11), Q1 2026 (13), Q4 2025 (7), Q4 2025 (8), Q4 2025 (10), Q4 2025 (11), Q4 2025 (13), Q3 2025 (1), Q3 2025 (8), Q3 2025 (9), Q3 2025 (14), Q3 2025 (15) |
| `machinery.truck.fact_truck_delivery_quantity` | Q2 2026 (5), Q2 2026 (11), Q2 2026 (12), Q1 2026 (12), Q4 2025 (6), Q4 2025 (7), Q3 2025 (11), Q3 2025 (15) |
| `machinery.truck.fact_truck_backlog_quantity` | Q2 2026 (11), Q2 2026 (14), Q1 2026 (1), Q1 2026 (4), Q1 2026 (6), Q1 2026 (11), Q1 2026 (12), Q4 2025 (8) |
| `machinery.truck.fact_truck_price` | Q2 2026 (2), Q2 2026 (3), Q2 2026 (4), Q2 2026 (6), Q2 2026 (7), Q2 2026 (8), Q2 2026 (10), Q1 2026 (8), Q4 2025 (5), Q4 2025 (6), Q4 2025 (13), Q4 2025 (15), Q4 2025 (17), Q3 2025 (4), Q3 2025 (8), Q3 2025 (9), Q3 2025 (12), Q3 2025 (18) |
| `machinery.truck.fact_truck_margin` | Q2 2026 (1), Q2 2026 (2), Q2 2026 (3), Q2 2026 (4), Q2 2026 (5), Q2 2026 (6), Q1 2026 (2), Q1 2026 (5), Q1 2026 (7), Q1 2026 (8), Q1 2026 (9), Q1 2026 (10), Q4 2025 (3), Q4 2025 (5), Q4 2025 (12), Q4 2025 (16), Q4 2025 (17), Q3 2025 (9) |
| `machinery.truck.fact_truck_market_quantity` | Q2 2026 (2), Q2 2026 (11), Q2 2026 (12), Q4 2025 (4), Q4 2025 (5), Q4 2025 (7), Q3 2025 (12) |
| `machinery.truck.fact_paccar_parts_quantity` | Q2 2026 (1), Q2 2026 (9), Q2 2026 (10), Q2 2026 (13), Q1 2026 (1), Q1 2026 (3), Q1 2026 (4), Q1 2026 (13), Q1 2026 (14), Q4 2025 (11), Q4 2025 (12), Q3 2025 (11), Q3 2025 (13), Q3 2025 (14) |
| `machinery.truck.fact_paccar_parts_amount` | Q2 2026 (1), Q2 2026 (5), Q2 2026 (10), Q1 2026 (2), Q1 2026 (3), Q1 2026 (5), Q1 2026 (7), Q1 2026 (9), Q1 2026 (13), Q1 2026 (14), Q4 2025 (4), Q4 2025 (12), Q3 2025 (1), Q3 2025 (5), Q3 2025 (11), Q3 2025 (12), Q3 2025 (13), Q3 2025 (14), Q3 2025 (15), Q3 2025 (18) |
| `machinery.commercial.fact_machine_parts_amount` | supporting population |
| `machinery.commercial.fact_financial_services_amount` | supporting population |
| `machinery.truck.fact_paccar_financial_amount` | Q1 2026 (14) |
| `machinery.truck.fact_emissions_compliance_cost` | Q2 2026 (3), Q2 2026 (4), Q2 2026 (6), Q2 2026 (7), Q2 2026 (8), Q2 2026 (14), Q1 2026 (2), Q1 2026 (11), Q1 2026 (12), Q4 2025 (15), Q4 2025 (16), Q3 2025 (4), Q3 2025 (8) |
| `machinery.truck.fact_freight_market_quantity` | Q2 2026 (13), Q1 2026 (10), Q4 2025 (10), Q4 2025 (11), Q3 2025 (13) |
| `machinery.truck.fact_truck_production_quantity` | Q2 2026 (9), Q1 2026 (6), Q4 2025 (6), Q4 2025 (8), Q4 2025 (16) |
| `machinery.truck.fact_truck_supplier_capacity` | Q2 2026 (9), Q1 2026 (7) |
| `machinery.commercial.fact_merchandise_price_support` | Q4 2024 (10) |
| `machinery.truck.fact_truck_market_share` | Q2 2026 (12), Q4 2025 (4) |
| `machinery.truck.fact_emissions_credit_quantity` | Q2 2026 (8), Q4 2025 (15), Q3 2025 (4) |
| `machinery.truck.fact_freight_rate` | Q2 2026 (13), Q1 2026 (10), Q4 2025 (10) |
| `machinery.truck.fact_truck_dealer_inventory_quantity` | Q2 2026 (7), Q4 2025 (13), Q4 2025 (17) |
