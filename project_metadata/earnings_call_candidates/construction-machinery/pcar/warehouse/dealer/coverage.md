# Truck Inc dealer inventory and retail demand

This slice owns the dealer, the sales region, retail-market ranges, deliveries, dealer and industry truck inventory, used trucks, and fleet capacity and age. Truck families, end markets, plants, price, parts margin, and backlog are owned outside this slice. A column that belongs to another slice is a partial identity and is not re-authored here.

Foreign identities are referenced from this slice and are partial here. Their complete populations are the datasets below, which this slice does not author:

| Identity | Column | Node |
| --- | --- | --- |
| `accounting_period_identity` | `accounting_period_id` | `sf:truck.calendar.dim_accounting_period` |
| `powertrain_identity` | `powertrain_id` | `sf:truck.product.dim_powertrain` |
| `truck_family_identity` | `truck_family_id` | `sf:truck.product.dim_truck_family` |

## Numbered questions

### Q2 2026 (7) — Prebuy versus customers who simply need trucks

Order share and the customer comment are by demand reason. Prebuy and ordinary need are reason codes.

- `truck.retail.fact_buy_reason`: `order_share`, `customer_comment`, `demand_reason_id`, `region_id`
- `truck.retail.dim_demand_reason`: `reason_code`, `reason_name`
- `truck.commercial.fact_order_intake`: `order_units`, `demand_reason_id`

### Q2 2026 (11) — Why U.S. and Canada deliveries were down, and their share of the next quarter

Delivery units, direction, and next-quarter share are by region. The region code selects the United States and Canada, Europe, and other markets.

- `truck.retail.fact_regional_delivery`: `delivery_units`, `delivery_direction`, `next_quarter_share`, `region_id`
- `truck.organization.dim_region`: `region_code`, `region_name`

### Q2 2026 (12) — Why the U.S. and Canada retail range stays wide

The low and high ends of the range, the wide-range flag, and year-to-date orders are the retail outlook.

- `truck.retail.fact_retail_outlook`: `retail_low_units`, `retail_high_units`, `range_kept_wide_flag`, `year_to_date_order_units`, `region_id`
- `truck.organization.dim_region`: `region_code`

### Q1 2026 (11) — Whether 2027 conversations are a prebuy or replacement

Order share by reason is the buy-reason fact. The emissions program says which half a prebuy would occupy if the rule stays.

- `truck.retail.fact_buy_reason`: `order_share`, `customer_comment`, `demand_reason_id`
- `truck.retail.dim_demand_reason`: `reason_code`
- `truck.product.fact_emissions_program`: `prebuy_half`, `rule_unchanged_flag`

### Q1 2026 (13) — How much non-prebuy demand is fleet growth versus replacement, and the parts effect

Order share by reason separates fleet growth from replacement. The replacement-pressure flag on parts says whether that replacement lifts parts.

- `truck.retail.fact_buy_reason`: `order_share`, `demand_reason_id`
- `truck.retail.dim_demand_reason`: `reason_code`
- `truck.commercial.fact_parts_result`: `replacement_pressure_flag`, `parts_revenue_amount`, `outlook_direction`

### Q4 2025 (7) — How a flat first quarter splits between the U.S. and Canada and Europe

Production units and delivery units are by region, so a flat total can be split. The quarter label selects the first quarter.

- `truck.product.fact_regional_build`: `production_units`, `region_id`
- `truck.retail.fact_regional_delivery`: `delivery_units`, `delivery_direction`, `region_id`
- `truck.organization.dim_region`: `region_code`
- `truck.calendar.dim_accounting_period`: `quarter_label`

### Q4 2025 (9) — Why the North America outlook stayed unchanged after Europe and South America were raised

Outlook direction and retail units are by region. Order units show the robust orders that did not move the North America outlook.

- `truck.retail.fact_region_outlook`: `outlook_direction`, `retail_units`, `region_id`
- `truck.commercial.fact_order_intake`: `order_units`, `region_id`
- `truck.organization.dim_region`: `region_code`

### Q4 2025 (11) — Whether the order pickup is replacement or fleet growth, and the used-truck market

Order share by reason is the buy reason. Used-truck values are tied to the same reason.

- `truck.retail.fact_buy_reason`: `order_share`, `demand_reason_id`
- `truck.retail.dim_demand_reason`: `reason_code`
- `truck.retail.fact_used_truck`: `used_value_index`, `demand_reason_id`, `region_id`

### Q4 2025 (13) — Where PACCAR and industry truck inventories stand, and how price evolves

Company inventory and industry inventory are separate counts. Dealer on-hand is the dealer lot. Price through the year is the price fact and stores no units.

- `truck.retail.fact_industry_inventory`: `company_inventory_units`, `industry_inventory_units`, `region_id`
- `truck.retail.fact_dealer_inventory`: `on_hand_units`, `dealer_id`
- `truck.commercial.fact_truck_price`: `realized_price_rate`, `next_quarter_price_rate`, `market_price_direction`

### Q4 2025 (17) — How much dealer stocking is expected ahead of the emissions change

Stock-order units and the emissions-stocking flag are dealer inventory, not retail deliveries and not factory backlog.

- `truck.retail.fact_dealer_inventory`: `stock_order_units`, `emissions_stocking_flag`, `on_hand_units`, `powertrain_id`, `dealer_id`
- `truck.product.dim_powertrain`: `powertrain_code`
- `truck.retail.dim_demand_reason`: `reason_code`

### Q3 2025 (3) — What customers say supports the North American outlook, including bonus depreciation

The regional outlook is the growth assumption. The incentive code selects bonus depreciation. The customer comment is what buyers are saying.

- `truck.retail.fact_region_outlook`: `outlook_direction`, `retail_units`, `region_id`
- `truck.commercial.fact_purchase_incentive`: `incentive_code`, `customer_support_note`, `region_id`
- `truck.retail.fact_buy_reason`: `customer_comment`, `region_id`
- `truck.organization.dim_region`: `region_code`

### Q3 2025 (8) — Whether the North America outlook still assumes an emissions prebuy

The prebuy-assumed flag and the retail range are the outlook for the region. The reason code names the prebuy.

- `truck.retail.fact_retail_outlook`: `prebuy_assumed_flag`, `retail_low_units`, `retail_high_units`, `region_id`
- `truck.retail.dim_demand_reason`: `reason_code`
- `truck.organization.dim_region`: `region_code`

### Q3 2025 (13) — How much excess truck capacity is in fleets relative to freight demand

Trucks in service, the freight-demand index, and excess capacity are the fleet fact. Freight volume and rate direction are the freight environment.

- `truck.retail.fact_fleet_capacity`: `trucks_in_service`, `freight_demand_index`, `excess_capacity_units`, `region_id`
- `truck.commercial.fact_freight_environment`: `freight_volume_direction`, `freight_rate_direction`

### Q3 2025 (14) — If customers keep trucks longer, what that means for parts next year

Trade-cycle direction is fleet age. Parts revenue, the outlook, and the replacement-pressure flag are next year's parts result.

- `truck.retail.fact_fleet_age`: `trade_cycle_direction`, `age_index`, `fleet_class_id`
- `truck.commercial.fact_parts_result`: `parts_revenue_amount`, `outlook_direction`, `replacement_pressure_flag`, `accounting_period_id`
- `truck.calendar.dim_accounting_period`: `fiscal_year`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `truck.organization.dim_region` | Q2 2026 (11), Q2 2026 (12), Q4 2025 (7), Q4 2025 (9), Q3 2025 (3), Q3 2025 (8) |
| `truck.organization.dim_country` | supporting population |
| `truck.dealer.dim_dealer` | supporting population |
| `truck.dealer.dim_dealer_location` | supporting population |
| `truck.retail.dim_fleet_class` | supporting population |
| `truck.retail.dim_demand_reason` | Q2 2026 (7), Q1 2026 (11), Q1 2026 (13), Q4 2025 (11), Q4 2025 (17), Q3 2025 (8) |
| `truck.retail.fact_dealer_inventory` | Q4 2025 (13), Q4 2025 (17) |
| `truck.retail.fact_industry_inventory` | Q4 2025 (13) |
| `truck.retail.fact_retail_outlook` | Q2 2026 (12), Q3 2025 (8) |
| `truck.retail.fact_regional_delivery` | Q2 2026 (11), Q4 2025 (7) |
| `truck.retail.fact_used_truck` | Q4 2025 (11) |
| `truck.retail.fact_fleet_capacity` | Q3 2025 (13) |
| `truck.retail.fact_fleet_age` | Q3 2025 (14) |
| `truck.retail.fact_buy_reason` | Q2 2026 (7), Q1 2026 (11), Q1 2026 (13), Q4 2025 (11), Q3 2025 (3) |
| `truck.retail.fact_region_outlook` | Q4 2025 (9), Q3 2025 (3) |
