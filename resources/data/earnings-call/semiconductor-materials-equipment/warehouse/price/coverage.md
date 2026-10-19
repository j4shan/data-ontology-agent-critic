# Wafer Tool Inc price slice

This slice is part of the Wafer Tool Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q3 FY2026 (2) — Applied Materials

For Applied Materials, Memory customers are signing multi-year agreements on units and price; with about eight quarters of visibility, how much further are customers aligning purchases?

- `wafertool.price.fact_backlog_revenue`: `backlog_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `customer_type_id`, `backlog_revenue_amount`
- `wafertool.price.fact_spares_revenue`: `spares_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `revenue_line_id`, `spares_revenue_amount`
- `wafertool.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_line_id`, `geography_id`, `product_revenue_amount`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (3) — Applied Materials

For Applied Materials, With gross margin already above 50% and guided flat, what keeps it from moving as volume and mix change?

- `wafertool.price.fact_gross_margin`: `gross_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_line_id`, `process_type_id`, `gross_profit_amount`, `gross_margin_percent`
- `wafertool.price.fact_system_revenue`: `system_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_revenue_amount`
- `wafertool.price.fact_service_revenue`: `service_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_revenue_amount`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (4) — Applied Materials

For Applied Materials, As customer talks shift from annual price debates to delivery and time-to-market, with about two years of visibility, what does that change in pricing power or order terms?

- `wafertool.price.fact_system_revenue`: `system_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_revenue_amount`
- `wafertool.price.fact_service_revenue`: `service_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_revenue_amount`
- `wafertool.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_line_id`, `geography_id`, `product_revenue_amount`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (6) — Applied Materials

For Applied Materials, NAND revenue doubled off a small base; what is actually happening in that market, and was the October mention too small to call out?

- `wafertool.price.fact_service_revenue`: `service_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_revenue_amount`
- `wafertool.price.fact_service_price`: `service_price_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `revenue_per_installed_tool_amount`
- `wafertool.price.fact_system_revenue`: `system_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_revenue_amount`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (1) — Applied Materials

For Applied Materials, With eight-quarter rolling visibility, are customers changing order patterns, upfront payments, or price because equipment is tight?

- `wafertool.price.fact_enterprise_results`: `enterprise_results_record_id`, `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`, `operating_income_amount`, `net_income_amount`, `diluted_earnings_per_share`
- `wafertool.price.fact_cash_flow`: `cash_flow_record_id`, `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `capital_expenditure_amount`, `free_cash_flow_amount`
- `wafertool.price.fact_backlog_revenue`: `backlog_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `customer_type_id`, `backlog_revenue_amount`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (2) — Applied Materials

For Applied Materials, Does 30% year-over-year equipment growth imply roughly $14.5 billion to $15 billion of equipment revenue in the second half of the calendar year, and what does that say about calendar 2027 even if it is early?

- `wafertool.price.fact_system_revenue`: `system_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_revenue_amount`
- `wafertool.price.fact_service_revenue`: `service_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_revenue_amount`
- `wafertool.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_line_id`, `geography_id`, `product_revenue_amount`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (3) — Applied Materials

For Applied Materials, Over the next one to three years, does semiconductor industry growth come more from units or still from price, given that wafer-fab equipment is not keeping up with industry revenue because chips are price-led?

- `wafertool.price.fact_service_revenue`: `service_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_revenue_amount`
- `wafertool.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_line_id`, `geography_id`, `product_revenue_amount`
- `wafertool.price.fact_enterprise_results`: `enterprise_results_record_id`, `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`, `operating_income_amount`, `net_income_amount`, `diluted_earnings_per_share`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (3) — Applied Materials

For Applied Materials, How large is the reporting move of 200-millimeter business from services into semiconductor systems, for the first quarter and for fiscal 2025?

- `wafertool.price.fact_enterprise_results`: `enterprise_results_record_id`, `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`, `operating_income_amount`, `net_income_amount`, `diluted_earnings_per_share`
- `wafertool.price.fact_cash_flow`: `cash_flow_record_id`, `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `capital_expenditure_amount`, `free_cash_flow_amount`
- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (5) — Applied Materials

For Applied Materials, Does the second-half lift mean the first half stays near the current level, or does revenue grow modestly and then accelerate?

- `wafertool.price.fact_system_revenue`: `system_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_revenue_amount`
- `wafertool.price.fact_service_revenue`: `service_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_revenue_amount`
- `wafertool.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_line_id`, `geography_id`, `product_revenue_amount`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (7) — Applied Materials

For Applied Materials, If share outside export restrictions is not being lost, why is China revenue declining while a European peer is growing sharply there?

- `wafertool.price.fact_system_revenue`: `system_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_revenue_amount`
- `wafertool.price.fact_service_revenue`: `service_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_revenue_amount`
- `wafertool.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_line_id`, `geography_id`, `product_revenue_amount`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (8) — Applied Materials

For Applied Materials, Leading-edge customer revenue grew about 50% in 2025; what sits underneath that growth by device type?

- `wafertool.price.fact_service_revenue`: `service_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_revenue_amount`
- `wafertool.price.fact_spares_revenue`: `spares_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `revenue_line_id`, `spares_revenue_amount`
- `wafertool.price.fact_system_revenue`: `system_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_revenue_amount`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (1) — Lam Research

For Lam Research, If customer-support revenue grows around the mid-30s this year, how much of that persists into 2027, how much is NAND, and when does Reliant recover?

- `wafertool.price.fact_system_revenue`: `system_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_revenue_amount`
- `wafertool.price.fact_service_revenue`: `service_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_revenue_amount`
- `wafertool.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_line_id`, `geography_id`, `product_revenue_amount`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (2) — Lam Research

For Lam Research, How much of the gross-margin step-up since 2023 is the shift of volume into the lower-cost Malaysia plant, and does further scaling there keep lifting margin?

- `wafertool.price.fact_gross_margin`: `gross_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_line_id`, `process_type_id`, `gross_profit_amount`, `gross_margin_percent`
- `wafertool.price.fact_operating_expense`: `operating_expense_record_id`, `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `wafertool.price.fact_warranty_cost`: `warranty_cost_record_id`, `fiscal_quarter_id`, `scenario_id`, `tool_family_id`, `cost_bucket_id`, `warranty_cost_amount`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (2) — Lam Research

For Lam Research, What changed in NAND versus 90 days ago, when it was still a low-teens share of sales, such that it is now expected to grow through the year toward the upgrade opportunity?

- `wafertool.price.fact_cash_flow`: `cash_flow_record_id`, `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `capital_expenditure_amount`, `free_cash_flow_amount`
- `wafertool.price.fact_spares_revenue`: `spares_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `revenue_line_id`, `spares_revenue_amount`
- `wafertool.price.fact_system_revenue`: `system_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_revenue_amount`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (5) — Lam Research

For Lam Research, As memory customers sign long-term price agreements, does that become prepayments and pricing power for Lam, and if not, why not?

- `wafertool.price.fact_system_revenue`: `system_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_revenue_amount`
- `wafertool.price.fact_service_revenue`: `service_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_revenue_amount`
- `wafertool.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_line_id`, `geography_id`, `product_revenue_amount`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (7) — Lam Research

For Lam Research, Services growth is held back by utilization already being high and by Reliant weakness, but a large upgrade pool is supposed to land by the end of 2027; why is that not showing up more in services yet?

- `wafertool.price.fact_spares_revenue`: `spares_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `revenue_line_id`, `spares_revenue_amount`
- `wafertool.demand.fact_service_demand`: `service_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_event_count`, `tool_serviced_count`
- `wafertool.demand.fact_application_bridge`: `application_bridge_record_id`, `fiscal_quarter_id`, `scenario_id`, `end_application_id`, `customer_type_id`, `process_type_id`, `application_wafer_start_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (9) — Lam Research

For Lam Research, If the year is second-half loaded, is the March quarter the trough, or does the first half stay near that level until the inflection?

- `wafertool.price.fact_enterprise_results`: `enterprise_results_record_id`, `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`, `operating_income_amount`, `net_income_amount`, `diluted_earnings_per_share`
- `wafertool.price.fact_cash_flow`: `cash_flow_record_id`, `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `capital_expenditure_amount`, `free_cash_flow_amount`
- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (2) — Lam Research

For Lam Research, What accounts for the higher December-quarter revenue outlook versus the level discussed three months earlier, and how much was pulled forward from the next year's first half?

- `wafertool.price.fact_enterprise_results`: `enterprise_results_record_id`, `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`, `operating_income_amount`, `net_income_amount`, `diluted_earnings_per_share`
- `wafertool.price.fact_system_revenue`: `system_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_revenue_amount`
- `wafertool.price.fact_service_revenue`: `service_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_revenue_amount`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (6) — Lam Research

For Lam Research, If next year is second-half loaded but the first half is only flat to slightly up versus the second half of 2025, how large is the second-half step-up?

- `wafertool.price.fact_enterprise_results`: `enterprise_results_record_id`, `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`, `operating_income_amount`, `net_income_amount`, `diluted_earnings_per_share`
- `wafertool.price.fact_cash_flow`: `cash_flow_record_id`, `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `capital_expenditure_amount`, `free_cash_flow_amount`
- `wafertool.demand.fact_system_orders`: `system_orders_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_order_count`, `customer_order_count`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (7) — Lam Research

For Lam Research, Was the September China revenue jump multinational spending in China or domestic customers, and why was it larger than expected?

- `wafertool.price.fact_system_revenue`: `system_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `process_type_id`, `tool_family_id`, `customer_type_id`, `geography_id`, `system_revenue_amount`
- `wafertool.price.fact_service_revenue`: `service_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `service_type_id`, `process_type_id`, `geography_id`, `service_revenue_amount`
- `wafertool.price.fact_product_revenue`: `product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_line_id`, `geography_id`, `product_revenue_amount`
- `wafertool.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `wafertool.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
