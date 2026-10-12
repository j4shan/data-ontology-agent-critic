# Caterpillar dealer inventory and retail demand

This slice owns the dealer, the sales region, retail demand, sales to users, dealer inventory, rental-fleet plans, and construction demand outside mega-projects and rental restocking. Segments, machine models, power products, end markets, accounting periods, price, and backlog are owned outside this slice. A column that belongs to another slice is a partial identity and is not re-authored here.

Foreign identities are referenced from this slice and are partial here. Their complete populations are the datasets below, which this slice does not author:

| Identity | Column | Node |
| --- | --- | --- |
| `accounting_period_identity` | `accounting_period_id` | `sf:caterpillar.calendar.dim_accounting_period` |
| `currency_identity` | `currency_id` | `sf:caterpillar.commercial.dim_currency` |
| `demand_driver_identity` | `demand_driver_id` | `sf:caterpillar.market.dim_demand_driver` |
| `machine_model_identity` | `machine_model_id` | `sf:caterpillar.product.dim_machine_model` |
| `segment_identity` | `segment_id` | `sf:caterpillar.market.dim_segment` |

## Numbered questions

### Q2 2026 (2) — Full-year sales to end users, and whether production matches retail demand

Sales to users after a strong first half are on the outlook fact. Production is matched to retail demand on its own fact, and dealer inventory stays a third fact.

- `caterpillar.retail.fact_user_sales_outlook`: `first_half_sales_to_users_amount`, `full_year_sales_to_users_amount`, `sales_to_users_outlook_amount`, `accounting_period_id`
- `caterpillar.retail.fact_production_versus_retail`: `production_units`, `retail_demand_units`, `build_to_retail_flag`, `segment_id`
- `caterpillar.retail.fact_retail_demand`: `retail_demand_units`, `retail_demand_amount`, `expected_direction`
- `caterpillar.retail.fact_dealer_inventory`: `on_hand_units`, `inventory_change_units`, `dealer_id`

### Q2 2026 (7) — Construction Industries deliveries to end users versus rental fleets

Deliveries are split by sales channel. Major-project loading is its own unit count on the same row. The channel code distinguishes end users from rental fleets.

- `caterpillar.retail.fact_delivery_split`: `delivery_units`, `major_project_units`, `sales_channel_id`, `segment_id`, `demand_driver_id`
- `caterpillar.retail.dim_sales_channel`: `channel_code`, `channel_name`
- `caterpillar.market.dim_segment`: `segment_code`
- `caterpillar.market.dim_demand_driver`: `driver_code`

### Q2 2026 (8) — Private nonresidential and residential construction outside mega-projects and rental

The ex-mega fact keeps private nonresidential and residential demand with the major-project and rental-restock exclusions flagged.

- `caterpillar.retail.fact_construction_ex_mega`: `demand_amount`, `excludes_major_project_flag`, `excludes_rental_restock_flag`, `demand_driver_id`, `segment_id`
- `caterpillar.market.dim_demand_driver`: `driver_code`, `driver_name`
- `caterpillar.market.dim_segment`: `segment_code`

### Q2 2026 (12) — Cat Rental fleet mix versus alliance products and national rental companies

The fleet plan is units and mix share by equipment origin and rental peer, so Cat equipment at Cat Rental can be compared with alliance products and with national rental fleets.

- `caterpillar.retail.fact_rental_fleet_plan`: `planned_units`, `mix_share`, `dealer_id`, `rental_peer_id`, `equipment_origin_id`
- `caterpillar.retail.dim_rental_peer`: `peer_code`, `peer_name`
- `caterpillar.retail.dim_equipment_origin`: `origin_code`, `origin_name`

### Q4 2024 (2) — North American construction dealer inventories after last year's destock

Expected user-sales direction and whether a further destock is required sit on the North America stock fact. Prior-year destock units stay on dealer inventory so the new reduction is not the same number as last year's.

- `caterpillar.retail.fact_north_america_stock`: `expected_user_sales_direction`, `further_destock_flag`, `on_hand_units`, `region_id`, `segment_id`
- `caterpillar.organization.dim_region`: `region_code`
- `caterpillar.market.dim_segment`: `segment_code`
- `caterpillar.retail.fact_dealer_inventory`: `prior_year_destock_units`, `inventory_change_units`, `destock_flag`, `on_hand_units`
- `caterpillar.retail.fact_retail_demand`: `expected_direction`, `retail_demand_units`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `caterpillar.organization.dim_region` | Q4 2024 (2) |
| `caterpillar.organization.dim_country` | supporting population |
| `caterpillar.dealer.dim_dealer` | supporting population |
| `caterpillar.dealer.dim_dealer_location` | supporting population |
| `caterpillar.retail.dim_sales_channel` | Q2 2026 (7) |
| `caterpillar.retail.dim_rental_peer` | Q2 2026 (12) |
| `caterpillar.retail.dim_equipment_origin` | Q2 2026 (12) |
| `caterpillar.retail.fact_dealer_inventory` | Q2 2026 (2), Q4 2024 (2) |
| `caterpillar.retail.fact_retail_demand` | Q2 2026 (2), Q4 2024 (2) |
| `caterpillar.retail.fact_production_versus_retail` | Q2 2026 (2) |
| `caterpillar.retail.fact_user_sales_outlook` | Q2 2026 (2) |
| `caterpillar.retail.fact_delivery_split` | Q2 2026 (7) |
| `caterpillar.retail.fact_construction_ex_mega` | Q2 2026 (8) |
| `caterpillar.retail.fact_rental_fleet_plan` | Q2 2026 (12) |
| `caterpillar.retail.fact_north_america_stock` | Q4 2024 (2) |
| `caterpillar.retail.fact_inventory_swing` | supporting population |
