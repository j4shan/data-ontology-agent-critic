# Machinery Inc dealer inventory and retail demand

Dealer stock is inventory on its own quantity fact, not a retail channel. Caterpillar machine and power processes and PACCAR truck, parts, and finance processes use separate facts and separate reporting-segment dimensions. Quantity, capacity, and price or margin are separate facts joined by fiscal period, scenario, and the business keys. Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks.

## Numbered questions

## Caterpillar

### Q2 2026 (2) Caterpillar

What full-year sales to end users are expected after a strong first half, and will production match retail demand?

- `machinery.retail.fact_retail_sales_quantity`: `accounting_period_id`, `scenario_id`, `dealer_id`, `cat_reporting_segment_id`, `region_id`, `end_user_type_id`, `retail_sales_units`
- `machinery.retail.fact_sales_to_users_amount`: `accounting_period_id`, `scenario_id`, `region_id`, `cat_reporting_segment_id`, `sales_to_users_amount`
- `machinery.retail.fact_delivery_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `delivery_recipient_id`, `delivery_units`

### Q2 2026 (7) Caterpillar

How do Construction Industries deliveries split between end users and rental fleets, including major-project loading?

- `machinery.retail.fact_delivery_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `delivery_recipient_id`, `delivery_units`
- `machinery.retail.fact_retail_sales_quantity`: `accounting_period_id`, `scenario_id`, `dealer_id`, `cat_reporting_segment_id`, `region_id`, `end_user_type_id`, `retail_sales_units`
- `machinery.market.fact_construction_activity_amount`: `accounting_period_id`, `scenario_id`, `construction_sector_id`, `project_scale_id`, `region_id`, `construction_demand_amount`

### Q2 2026 (8) Caterpillar

Outside mega-projects and rental loading, what is happening in private nonresidential and residential construction?

- `machinery.market.fact_construction_activity_amount`: `accounting_period_id`, `scenario_id`, `construction_sector_id`, `project_scale_id`, `region_id`, `construction_demand_amount`
- `machinery.retail.fact_delivery_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `delivery_recipient_id`, `delivery_units`
- `machinery.retail.fact_rental_fleet_quantity`: `accounting_period_id`, `scenario_id`, `rental_operator_id`, `equipment_source_id`, `region_id`, `planned_fleet_units`

### Q2 2026 (12) Caterpillar

As dealers plan to expand Cat Rental, how should the mix of Cat equipment versus alliance products evolve versus national rental companies?

- `machinery.retail.fact_rental_fleet_quantity`: `accounting_period_id`, `scenario_id`, `rental_operator_id`, `equipment_source_id`, `region_id`, `planned_fleet_units`
- `machinery.retail.fact_dealer_inventory_quantity`: `accounting_period_id`, `scenario_id`, `dealer_id`, `dealer_location_id`, `machine_model_id`, `cat_reporting_segment_id`, `region_id`, `on_hand_units`, `inventory_change_units`
- `machinery.retail.fact_dealer_stock_value`: `accounting_period_id`, `scenario_id`, `dealer_id`, `cat_reporting_segment_id`, `region_id`, `dealer_stock_amount`

### Q4 2024 (2) Caterpillar

With North American construction users expected down, do machine dealer inventories need to fall further after last year's destock?

- `machinery.retail.fact_dealer_inventory_quantity`: `accounting_period_id`, `scenario_id`, `dealer_id`, `dealer_location_id`, `machine_model_id`, `cat_reporting_segment_id`, `region_id`, `on_hand_units`, `inventory_change_units`
- `machinery.retail.fact_dealer_stock_value`: `accounting_period_id`, `scenario_id`, `dealer_id`, `cat_reporting_segment_id`, `region_id`, `dealer_stock_amount`
- `machinery.retail.fact_retail_sales_quantity`: `accounting_period_id`, `scenario_id`, `dealer_id`, `cat_reporting_segment_id`, `region_id`, `end_user_type_id`, `retail_sales_units`

## PACCAR

### Q4 2025 (1) PACCAR

What improves margin from the fourth quarter to the first despite flat deliveries?

- `machinery.retail.fact_delivery_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `delivery_recipient_id`, `delivery_units`
- `machinery.retail.fact_retail_sales_quantity`: `accounting_period_id`, `scenario_id`, `dealer_id`, `cat_reporting_segment_id`, `region_id`, `end_user_type_id`, `retail_sales_units`

### Q4 2025 (2) PACCAR

When do the recent orders turn into production?

- `machinery.retail.fact_factory_production_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `machine_model_id`, `production_units`, `factory_shipment_units`
- `machinery.retail.fact_retail_sales_quantity`: `accounting_period_id`, `scenario_id`, `dealer_id`, `cat_reporting_segment_id`, `region_id`, `end_user_type_id`, `retail_sales_units`

### Q4 2025 (14) PACCAR

If demand improves, where would the supply chain fail to ramp?

- `machinery.retail.fact_retail_sales_quantity`: `accounting_period_id`, `scenario_id`, `dealer_id`, `cat_reporting_segment_id`, `region_id`, `end_user_type_id`, `retail_sales_units`
- `machinery.market.fact_construction_activity_amount`: `accounting_period_id`, `scenario_id`, `construction_sector_id`, `project_scale_id`, `region_id`, `construction_demand_amount`

### Q4 2025 (19) PACCAR

How much of the improved customer confidence is the freight environment versus clarity on the emissions rule?

- `machinery.retail.fact_service_contract_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_user_type_id`, `service_contract_count`
- `machinery.retail.fact_retail_sales_quantity`: `accounting_period_id`, `scenario_id`, `dealer_id`, `cat_reporting_segment_id`, `region_id`, `end_user_type_id`, `retail_sales_units`

### Q3 2025 (3) PACCAR

What are customers saying that supports the North American growth outlook, including bonus depreciation?

- `machinery.retail.fact_service_contract_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_user_type_id`, `service_contract_count`
- `machinery.retail.fact_sales_to_users_amount`: `accounting_period_id`, `scenario_id`, `region_id`, `cat_reporting_segment_id`, `sales_to_users_amount`

### Q3 2025 (6) PACCAR

Is the result a clear cost advantage for U.S. production, or only an even field with peers?

- `machinery.retail.fact_factory_production_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `machine_model_id`, `production_units`, `factory_shipment_units`
- `machinery.retail.fact_installed_base_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `machine_model_id`, `region_id`, `installed_base_units`, `active_installed_units`

### Q3 2025 (7) PACCAR

How large a tariff headwind is in the fourth-quarter outlook as rebates ramp?

- `machinery.retail.fact_sales_to_users_amount`: `accounting_period_id`, `scenario_id`, `region_id`, `cat_reporting_segment_id`, `sales_to_users_amount`
- `machinery.retail.fact_retail_sales_quantity`: `accounting_period_id`, `scenario_id`, `dealer_id`, `cat_reporting_segment_id`, `region_id`, `end_user_type_id`, `retail_sales_units`

### Q3 2025 (10) PACCAR

Are customers talking about incremental share since the tariff announcement, and how does that affect the Denton and Chillicothe plans?

- `machinery.retail.fact_rental_fleet_quantity`: `accounting_period_id`, `scenario_id`, `rental_operator_id`, `equipment_source_id`, `region_id`, `planned_fleet_units`
- `machinery.retail.fact_service_contract_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_user_type_id`, `service_contract_count`

### Q3 2025 (17) PACCAR

If the emissions rule is unchanged, do customers say prebuying starts in the first half or the second half?

- `machinery.retail.fact_sales_to_users_amount`: `accounting_period_id`, `scenario_id`, `region_id`, `cat_reporting_segment_id`, `sales_to_users_amount`
- `machinery.retail.fact_service_contract_quantity`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_user_type_id`, `service_contract_count`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `machinery.time.dim_accounting_period` | supporting population |
| `machinery.time.dim_scenario` | supporting population |
| `machinery.organization.dim_region` | supporting population |
| `machinery.organization.dim_country` | supporting population |
| `machinery.dealer.dim_dealer` | supporting population |
| `machinery.dealer.dim_dealer_location` | supporting population |
| `machinery.market.dim_cat_reporting_segment` | supporting population |
| `machinery.market.dim_paccar_reporting_segment` | supporting population |
| `machinery.product.dim_machine_model` | supporting population |
| `machinery.retail.dim_end_user_type` | supporting population |
| `machinery.retail.dim_delivery_recipient` | supporting population |
| `machinery.retail.dim_equipment_source` | supporting population |
| `machinery.retail.dim_rental_operator` | supporting population |
| `machinery.retail.fact_dealer_inventory_quantity` | Q2 2026 (12), Q4 2024 (2) |
| `machinery.retail.fact_dealer_stock_value` | Q2 2026 (12), Q4 2024 (2) |
| `machinery.retail.fact_retail_sales_quantity` | Q2 2026 (2), Q2 2026 (7), Q4 2024 (2), Q4 2025 (1), Q4 2025 (2), Q4 2025 (14), Q4 2025 (19), Q3 2025 (7) |
| `machinery.retail.fact_factory_production_quantity` | Q4 2025 (2), Q3 2025 (6) |
| `machinery.retail.fact_sales_to_users_amount` | Q2 2026 (2), Q3 2025 (3), Q3 2025 (7), Q3 2025 (17) |
| `machinery.retail.fact_delivery_quantity` | Q2 2026 (2), Q2 2026 (7), Q2 2026 (8), Q4 2025 (1) |
| `machinery.market.fact_construction_activity_amount` | Q2 2026 (7), Q2 2026 (8), Q4 2025 (14) |
| `machinery.retail.fact_rental_fleet_quantity` | Q2 2026 (8), Q2 2026 (12), Q3 2025 (10) |
| `machinery.retail.fact_installed_base_quantity` | Q3 2025 (6) |
| `machinery.retail.fact_service_contract_quantity` | Q4 2025 (19), Q3 2025 (3), Q3 2025 (10), Q3 2025 (17) |
