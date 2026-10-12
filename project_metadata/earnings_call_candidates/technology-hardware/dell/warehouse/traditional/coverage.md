# Computer Inc traditional server and storage demand

This slice owns product category, customer type, channel, geography, the fiscal calendar, and traditional demand. Traditional servers, storage, PCs, and networking are categories. Unit demand and orders live here. The unit price lives on the price slice. AI-server shipments, backlog, and component supply live on the AI slice. Those identifiers are partial when a demand row names them.

## Numbered questions

### Q2 FY2027 (1)

Is the surge in traditional servers and storage real demand and share gain, or price and pre-buying?

- `computer.demand.fact_category_demand`: `demand_quantity`, `demand_growth_rate`, `product_category_id`, `fiscal_quarter_id`
- `computer.price.fact_growth_bridge`: `price_effect_amount`, `volume_effect_amount`, `share_effect_amount`, `prebuy_effect_amount`, `product_category_id`, `fiscal_quarter_id`
- `computer.price.fact_category_price`: `unit_price`, `price_change_amount`, `product_category_id`, `country_id`, `channel_id`, `fiscal_quarter_id`
- `computer.product.dim_product_category`: `category_code`

### Q2 FY2027 (3)

Is traditional server demand still almost all enterprise, or are neoclouds in that bucket now that CPU racks are included, and how does the AI-server customer mix compare?

- `computer.demand.fact_server_customer_mix`: `revenue_amount`, `includes_cpu_racks_flag`, `product_category_id`, `customer_type_id`, `fiscal_quarter_id`
- `computer.supply.fact_cpu_rack`: `in_traditional_bucket_flag`, `customer_type_id`, `fiscal_quarter_id`
- `computer.supply.fact_ai_order`: `order_amount`, `customer_type_id`, `ai_platform_id`, `fiscal_quarter_id`
- `computer.product.dim_customer_type`: `customer_type_code`
- `computer.product.dim_product_category`: `category_code`

### Q2 FY2027 (5)

How much enterprise demand is deferred because budgets cannot absorb the price increase, so buyers take part of the order now and leave the rest for next year?

- `computer.demand.fact_deferred_demand`: `order_taken_quantity`, `deferred_quantity`, `budget_constraint_flag`, `customer_type_id`, `product_category_id`, `fiscal_quarter_id`, `deferred_to_quarter_code`
- `computer.price.fact_category_price`: `price_change_amount`, `unit_price`, `product_category_id`, `fiscal_quarter_id`
- `computer.product.dim_customer_type`: `customer_type_code`

### Q1 FY2027 (1)

Is the quarter's strength a pull-forward in traditional servers and PCs, or does raising the second half mean demand continues?

- `computer.demand.fact_pull_forward`: `pull_forward_quantity`, `continuing_demand_flag`, `second_half_raised_flag`, `product_category_id`, `fiscal_quarter_id`
- `computer.demand.fact_category_demand`: `demand_quantity`, `order_quantity`, `product_category_id`, `fiscal_quarter_id`
- `computer.product.dim_product_category`: `category_code`

### Q1 FY2027 (2)

How much of the traditional-server outperformance is units versus price, and does it last through this year and into next year?

- `computer.price.fact_growth_bridge`: `volume_effect_amount`, `price_effect_amount`, `product_category_id`, `fiscal_quarter_id`
- `computer.demand.fact_category_demand`: `demand_quantity`, `demand_growth_rate`, `product_category_id`, `fiscal_quarter_id`
- `computer.price.fact_category_price`: `unit_price`, `price_change_amount`, `product_category_id`, `fiscal_quarter_id`
- `computer.geography.dim_fiscal_quarter`: `quarter_code`, `fiscal_year_id`
- `computer.geography.dim_fiscal_year`: `year_code`

### Q1 FY2027 (3)

Why is the revenue guide still weighted to the back half, and is that caution or delayed demand versus the usual seasonal mix?

- `computer.demand.fact_revenue_outlook`: `back_half_revenue_share`, `historical_back_half_share`, `caution_flag`, `delayed_demand_flag`, `fiscal_year_id`, `fiscal_quarter_id`
- `computer.geography.dim_fiscal_quarter`: `half_code`, `quarter_code`

### Q1 FY2027 (4)

How wide is the range of IT budgets while customers prioritize locking supply, and is some of the spend coming from other categories?

- `computer.demand.fact_it_budget`: `budget_range_low_amount`, `budget_range_high_amount`, `supply_lock_priority_flag`, `reallocated_from_other_amount`, `customer_type_id`, `fiscal_quarter_id`
- `computer.supply.fact_component_constraint`: `limits_upside_flag`, `component_commodity_id`, `fiscal_quarter_id`

### Q1 FY2027 (6)

Would the prior medium-term revenue framework be higher now, given agentic uses of traditional servers and share gains?

- `computer.demand.fact_revenue_framework`: `prior_framework_growth_rate`, `current_implied_growth_rate`, `would_be_higher_flag`, `agentic_traditional_share`, `share_gain_rate`, `workload_id`, `fiscal_year_id`
- `computer.product.dim_workload`: `workload_code`
- `computer.demand.fact_category_demand`: `demand_growth_rate`, `product_category_id`, `fiscal_quarter_id`

### Q3 FY2026 (3)

Where is the PC refresh — still Windows end-of-life, or are new factors extending the cycle?

- `computer.demand.fact_pc_refresh`: `contribution_share`, `cycle_extended_flag`, `refresh_driver_id`, `pc_tier_id`, `fiscal_quarter_id`
- `computer.product.dim_refresh_driver`: `driver_code`
- `computer.product.dim_pc_tier`: `tier_code`

### Q3 FY2026 (6)

If traditional-server demand is up double digits but revenue is not, where is the upgrade cycle, and is double-digit growth a fair baseline?

- `computer.demand.fact_upgrade_cycle`: `demand_growth_rate`, `recognized_revenue_growth_rate`, `installed_base_age_years`, `double_digit_baseline_flag`, `server_generation_id`, `product_category_id`, `fiscal_quarter_id`
- `computer.demand.fact_category_demand`: `demand_quantity`, `demand_growth_rate`, `product_category_id`, `fiscal_quarter_id`
- `computer.product.dim_server_generation`: `generation_code`

## Datasets

| Qualified name | Role | Questions served |
| --- | --- | --- |
| `computer.geography.dim_region` | dimension | join support |
| `computer.geography.dim_country` | dimension | join support |
| `computer.geography.dim_fiscal_year` | dimension | Q1 FY2027 (2) |
| `computer.geography.dim_fiscal_quarter` | dimension | Q1 FY2027 (2), Q1 FY2027 (3) |
| `computer.geography.dim_calendar_day` | dimension | join support |
| `computer.channel.dim_channel` | dimension | join support |
| `computer.product.dim_business_unit` | dimension | join support |
| `computer.product.dim_product_category` | dimension | Q2 FY2027 (1), Q2 FY2027 (3), Q1 FY2027 (1) |
| `computer.product.dim_server_generation` | dimension | Q3 FY2026 (6) |
| `computer.product.dim_customer_type` | dimension | Q2 FY2027 (3), Q2 FY2027 (5) |
| `computer.product.dim_workload` | dimension | Q1 FY2027 (6) |
| `computer.product.dim_pc_tier` | dimension | Q3 FY2026 (3) |
| `computer.product.dim_refresh_driver` | dimension | Q3 FY2026 (3) |
| `computer.demand.fact_category_demand` | fact | Q2 FY2027 (1), Q1 FY2027 (1), Q1 FY2027 (2), Q1 FY2027 (6), Q3 FY2026 (6) |
| `computer.demand.fact_server_customer_mix` | fact | Q2 FY2027 (3) |
| `computer.demand.fact_deferred_demand` | fact | Q2 FY2027 (5) |
| `computer.demand.fact_it_budget` | fact | Q1 FY2027 (4) |
| `computer.demand.fact_pull_forward` | fact | Q1 FY2027 (1) |
| `computer.demand.fact_revenue_outlook` | fact | Q1 FY2027 (3) |
| `computer.demand.fact_upgrade_cycle` | fact | Q3 FY2026 (6) |
| `computer.demand.fact_pc_refresh` | fact | Q3 FY2026 (3) |
| `computer.demand.fact_revenue_framework` | fact | Q1 FY2027 (6) |
