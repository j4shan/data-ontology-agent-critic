# Caterpillar price, volume, and backlog

This slice owns the calendar, price realization, segment volume, orders, backlog, margin, manufacturing cost, tariffs, and the sales and profit outlook. Dealer inventory, retail demand, and the power-product and end-market populations are owned outside this slice. Price columns do not store unit volume, and volume columns do not store price. Backlog is unfilled orders, not dealer stock and not a shipment.

Foreign identities are referenced from this slice and are partial here. Their complete populations are the datasets below, which this slice does not author:

| Identity | Column | Node |
| --- | --- | --- |
| `customer_identity` | `customer_id` | `sf:caterpillar.power.dim_customer` |
| `end_market_identity` | `end_market_id` | `sf:caterpillar.market.dim_end_market` |
| `power_product_identity` | `power_product_id` | `sf:caterpillar.product.dim_power_product` |
| `project_identity` | `project_id` | `sf:caterpillar.power.dim_project` |
| `segment_identity` | `segment_id` | `sf:caterpillar.market.dim_segment` |

## Numbered questions

### Q2 2026 (4) — How much of the backlog increase was large power awards versus broad-based orders

The bridge stores the two pieces and the total change. Order scope on intake is the same distinction at the order, not at dealer inventory.

- `caterpillar.commercial.fact_backlog_bridge`: `large_power_award_amount`, `broad_based_order_amount`, `backlog_change_amount`, `segment_id`
- `caterpillar.commercial.fact_order_intake`: `order_amount`, `order_scope_code`, `segment_id`
- `caterpillar.commercial.fact_backlog_position`: `backlog_amount`, `backlog_change_amount`

### Q2 2026 (5) — Whether Power & Energy incremental margins hold while capacity is still being added

The incremental margin rate and the sustainability flag are separate from the ramp cost of capacity still coming online.

- `caterpillar.commercial.fact_incremental_margin`: `incremental_margin_rate`, `sustainability_flag`, `segment_id`
- `caterpillar.commercial.fact_capacity_ramp_cost`: `ramp_cost_amount`, `capacity_still_coming_online_flag`, `power_product_id`, `segment_id`
- `caterpillar.market.dim_segment`: `segment_code`

### Q2 2026 (10) — Fourth-quarter 10-megawatt orders in hand and the extra ramp cost

Orders in hand are units and amount. Ramp cost is a different amount on the ramp-cost fact. The quarter label selects the fourth quarter.

- `caterpillar.commercial.fact_ten_megawatt_orders`: `orders_in_hand_units`, `orders_in_hand_amount`, `power_product_id`, `accounting_period_id`
- `caterpillar.commercial.fact_capacity_ramp_cost`: `ramp_cost_amount`, `power_product_id`, `accounting_period_id`
- `caterpillar.product.dim_power_product`: `product_code`
- `caterpillar.calendar.dim_accounting_period`: `quarter_label`, `fiscal_year`

### Q1 2026 (2) — Why the long-term margin view is unchanged after a higher sales outlook

The unchanged flag, the sales outlook, and fixed-cost absorption are on the profit outlook. The framework name identifies the analyst-day range.

- `caterpillar.commercial.fact_operating_profit_outlook`: `margin_view_unchanged_flag`, `sales_outlook_amount`, `fixed_cost_absorption_amount`, `margin_framework_id`
- `caterpillar.commercial.fact_sales_outlook`: `sales_outlook_amount`, `sales_growth_rate`
- `caterpillar.commercial.dim_margin_framework`: `framework_name`, `low_rate`, `high_rate`

### Q1 2026 (6) — Mining orders versus negative price and tariff-hit margins

Order strength, including the 2012 comparison, is the mining-order fact. Price realization and the tariff margin effect are separate from that order amount. Segment margin is the profitability result.

- `caterpillar.commercial.fact_mining_order_cycle`: `order_amount`, `order_strength_index`, `comparison_year`, `segment_id`, `end_market_id`
- `caterpillar.commercial.fact_price_realization`: `price_realization_rate`, `segment_id`
- `caterpillar.commercial.fact_tariff_impact`: `tariff_margin_effect_amount`, `segment_id`
- `caterpillar.commercial.fact_segment_margin`: `operating_margin_amount`, `margin_rate`, `segment_id`
- `caterpillar.market.dim_segment`: `segment_code`
- `caterpillar.market.dim_end_market`: `market_code`

### Q4 2025 (1) — Orders and backlog outside power generation

The exclude flag and the segment code keep Construction Industries and Resource Industries apart from Power & Energy. Backlog amount is unfilled orders, not dealer stock.

- `caterpillar.commercial.fact_order_intake`: `order_amount`, `excludes_power_generation_flag`, `sequential_change_amount`, `segment_id`
- `caterpillar.commercial.fact_backlog_position`: `backlog_amount`, `backlog_change_amount`, `segment_id`
- `caterpillar.market.dim_segment`: `segment_code`

### Q4 2025 (3) — Modest sales growth against backlog shipping within twelve months, orders, and retail

The sales-growth rate and the modest-growth flag are the outlook. Twelve-month shipping backlog, order change, and retail demand are three other facts.

- `caterpillar.commercial.fact_sales_outlook`: `sales_growth_rate`, `modest_growth_flag`, `sales_outlook_amount`
- `caterpillar.commercial.fact_backlog_shipping_window`: `shipping_within_twelve_months_amount`, `segment_id`
- `caterpillar.commercial.fact_order_intake`: `order_amount`, `sequential_change_amount`
- `caterpillar.retail.fact_retail_demand`: `retail_demand_amount`, `retail_demand_units`, `expected_direction`

### Q4 2025 (6) — Whether backlog growth was a one-time pull-forward

Pull-forward amount and the one-time flag are separate from the next-quarter project amount.

- `caterpillar.commercial.fact_backlog_pullforward`: `pullforward_amount`, `one_time_flag`, `next_quarter_project_amount`, `project_id`, `accounting_period_id`
- `caterpillar.commercial.fact_backlog_position`: `backlog_change_amount`, `backlog_amount`
- `caterpillar.power.dim_project`: `project_name`

### Q4 2024 (3) — Negative price/cost versus manufacturing cost that had been a help

Price effect and manufacturing-cost effect are separate columns. The prior-year help flag records that manufacturing cost had been favorable.

- `caterpillar.commercial.fact_price_cost_bridge`: `price_cost_effect_amount`, `price_realization_effect_amount`, `manufacturing_cost_effect_amount`, `prior_year_manufacturing_cost_help_flag`, `segment_id`
- `caterpillar.commercial.fact_manufacturing_cost`: `manufacturing_cost_amount`, `year_over_year_help_flag`, `segment_id`
- `caterpillar.commercial.fact_segment_margin`: `operating_margin_amount`, `margin_rate`
- `caterpillar.commercial.dim_cost_element`: `element_code`

### Q4 2024 (5) — What would move operating profit from the top of the range toward the midpoint

Range position, profit, revenue, and the pressure condition are the outlook. The framework holds the range.

- `caterpillar.commercial.fact_operating_profit_outlook`: `range_position`, `operating_profit_amount`, `revenue_amount`, `pressure_condition`, `margin_framework_id`
- `caterpillar.commercial.dim_margin_framework`: `low_rate`, `high_rate`, `framework_name`

### Q4 2024 (6) — Delayed Energy & Transportation shipments, when they land, and 2025 capacity

Delayed amount, the landing period, and capacity-supported sales are the shipment fact. The segment code selects Energy & Transportation. New capacity gigawatts are the ramp fact.

- `caterpillar.commercial.fact_delayed_shipment`: `delayed_amount`, `capacity_support_amount`, `prior_year_sales_amount`, `segment_id`, `accounting_period_id`
- `caterpillar.commercial.fact_shipment_landing`: `landed_amount`, `landing_period_id`, `segment_id`
- `caterpillar.calendar.dim_accounting_period`: `period_label`, `fiscal_year`, `quarter_label`
- `caterpillar.market.dim_segment`: `segment_code`
- `caterpillar.power.fact_engine_capacity_ramp`: `capacity_online_units`, `ramp_gigawatts`, `capacity_horizon_id`
- `caterpillar.commercial.fact_sales_outlook`: `sales_outlook_amount`, `sales_growth_rate`

### Q4 2024 (7) — Sequential Construction Industries revenue and margin

Revenue, margin, the sequential change, and whether pressure is concentrated in the segment are on the segment-margin fact.

- `caterpillar.commercial.fact_segment_margin`: `revenue_amount`, `operating_margin_amount`, `margin_rate`, `sequential_change_amount`, `pressure_concentrated_flag`, `segment_id`
- `caterpillar.market.dim_segment`: `segment_code`
- `caterpillar.calendar.dim_accounting_period`: `quarter_label`

### Q4 2024 (8) — Sequential Construction and Resource Industries orders versus Energy & Transportation

Order amount and the sequential change are by segment, so the three books can be compared.

- `caterpillar.commercial.fact_order_intake`: `order_amount`, `sequential_change_amount`, `segment_id`, `accounting_period_id`
- `caterpillar.market.dim_segment`: `segment_code`, `segment_name`

### Q4 2024 (9) — Inventory absorption as a company-wide margin headwind

The absorption effect, the sales direction, and the company-wide flag show whether the headwind is only construction. Production units are the factory level, not dealer stock.

- `caterpillar.commercial.fact_inventory_absorption`: `absorption_margin_effect_amount`, `company_wide_flag`, `sales_direction`, `production_units`, `segment_id`
- `caterpillar.commercial.fact_sales_outlook`: `sales_growth_rate`, `sales_outlook_amount`
- `caterpillar.market.dim_segment`: `segment_code`

### Q4 2024 (10) — Second-half pricing as merchandise programs roll off

Program status and half code show the roll-off. Price realization in that half, including competitive pressure, is the price fact and stores no volume.

- `caterpillar.commercial.fact_merchandise_program`: `program_status`, `half_code`, `price_support_amount`, `accounting_period_id`
- `caterpillar.commercial.fact_price_realization`: `price_realization_rate`, `half_code`, `competitive_pressure_note`, `segment_id`

### Q4 2024 (11) — Whether the margin framework still holds with a negative price impact

The framework-still-valid flag and the price-impact direction sit beside the margin rate and the price realization rate. The disruption flag marks the range that was set earlier.

- `caterpillar.commercial.fact_operating_profit_outlook`: `framework_still_valid_flag`, `price_impact_direction`, `margin_framework_id`
- `caterpillar.commercial.fact_segment_margin`: `margin_rate`, `operating_margin_amount`
- `caterpillar.commercial.fact_price_realization`: `price_realization_rate`
- `caterpillar.commercial.dim_margin_framework`: `low_rate`, `high_rate`, `set_during_supply_disruption_flag`, `framework_name`

### Q4 2024 (12) — Resource Industries conversations and early-year orders after the fourth-quarter improvement

Fourth-quarter improvement, early-year orders, and conversation status are the mining-order fact. The customer and the mining end market name who the conversation is with.

- `caterpillar.commercial.fact_mining_order_cycle`: `fourth_quarter_improvement_flag`, `early_year_order_amount`, `conversation_status`, `order_amount`, `customer_id`, `end_market_id`, `segment_id`
- `caterpillar.power.dim_customer`: `customer_name`, `customer_role`
- `caterpillar.market.dim_end_market`: `market_code`
- `caterpillar.market.dim_segment`: `segment_code`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `caterpillar.calendar.dim_calendar_day` | supporting population |
| `caterpillar.calendar.dim_accounting_period` | Q2 2026 (10), Q4 2024 (6), Q4 2024 (7) |
| `caterpillar.commercial.dim_currency` | supporting population |
| `caterpillar.commercial.dim_margin_framework` | Q1 2026 (2), Q4 2024 (5), Q4 2024 (11) |
| `caterpillar.commercial.dim_cost_element` | Q4 2024 (3) |
| `caterpillar.commercial.fact_segment_volume` | supporting population |
| `caterpillar.commercial.fact_price_realization` | Q1 2026 (6), Q4 2024 (10), Q4 2024 (11) |
| `caterpillar.commercial.fact_order_intake` | Q2 2026 (4), Q4 2025 (1), Q4 2025 (3), Q4 2024 (8) |
| `caterpillar.commercial.fact_backlog_position` | Q2 2026 (4), Q4 2025 (1), Q4 2025 (6) |
| `caterpillar.commercial.fact_backlog_bridge` | Q2 2026 (4) |
| `caterpillar.commercial.fact_backlog_pullforward` | Q4 2025 (6) |
| `caterpillar.commercial.fact_backlog_shipping_window` | Q4 2025 (3) |
| `caterpillar.commercial.fact_segment_margin` | Q1 2026 (6), Q4 2024 (3), Q4 2024 (7), Q4 2024 (11) |
| `caterpillar.commercial.fact_incremental_margin` | Q2 2026 (5) |
| `caterpillar.commercial.fact_price_cost_bridge` | Q4 2024 (3) |
| `caterpillar.commercial.fact_operating_profit_outlook` | Q1 2026 (2), Q4 2024 (5), Q4 2024 (11) |
| `caterpillar.commercial.fact_manufacturing_cost` | Q4 2024 (3) |
| `caterpillar.commercial.fact_tariff_impact` | Q1 2026 (6) |
| `caterpillar.commercial.fact_merchandise_program` | Q4 2024 (10) |
| `caterpillar.commercial.fact_inventory_absorption` | Q4 2024 (9) |
| `caterpillar.commercial.fact_sales_outlook` | Q1 2026 (2), Q4 2025 (3), Q4 2024 (6), Q4 2024 (9) |
| `caterpillar.commercial.fact_delayed_shipment` | Q4 2024 (6) |
| `caterpillar.commercial.fact_shipment_landing` | Q4 2024 (6) |
| `caterpillar.commercial.fact_mining_order_cycle` | Q1 2026 (6), Q4 2024 (12) |
| `caterpillar.commercial.fact_capacity_ramp_cost` | Q2 2026 (5), Q2 2026 (10) |
| `caterpillar.commercial.fact_ten_megawatt_orders` | Q2 2026 (10) |
