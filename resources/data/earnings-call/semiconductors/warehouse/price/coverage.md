# Chip Inc price slice

This slice is part of the Chip Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q3 FY2026 (5) — Broadcom

For Broadcom, How should dollars of content per gigawatt change across later XPU generations?

- `chip.price.fact_content_per_gigawatt`: `content_per_gigawatt_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `revenue_per_gigawatt_amount`
- `chip.price.fact_gross_margin`: `gross_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `gross_profit_amount`, `gross_margin_percent`
- `chip.price.fact_operating_expense`: `operating_expense_record_id`, `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (2) — Broadcom

For Broadcom, Why is gross margin falling faster than the shift between semiconductors and infrastructure software would explain, even with a stronger software quarter?

- `chip.price.fact_software_revenue`: `software_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `software_product_id`, `customer_type_id`, `software_revenue_amount`
- `chip.price.fact_software_pricing_revenue`: `software_pricing_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `pricing_model_id`, `software_product_id`, `pricing_model_revenue_amount`
- `chip.price.fact_semiconductor_revenue`: `semiconductor_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `semiconductor_revenue_amount`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (6) — Broadcom

For Broadcom, Does networking stay near 40% of AI revenue as custom accelerators ramp through the end of fiscal 2026 and into 2027, or does that mix fall?

- `chip.price.fact_semiconductor_revenue`: `semiconductor_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `semiconductor_revenue_amount`
- `chip.price.fact_networking_revenue`: `networking_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `networking_revenue_amount`
- `chip.price.fact_enterprise_results`: `enterprise_results_record_id`, `fiscal_quarter_id`, `scenario_id`, `total_revenue_amount`, `operating_income_amount`, `net_income_amount`, `diluted_earnings_per_share`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (12) — Broadcom

For Broadcom, How should revenue per gigawatt evolve versus the prior $15 billion to $20 billion range, given a 10-gigawatt year that would imply a much larger total?

- `chip.price.fact_content_per_gigawatt`: `content_per_gigawatt_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `revenue_per_gigawatt_amount`
- `chip.price.fact_accelerator_price`: `accelerator_price_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `revenue_per_accelerator_amount`
- `chip.price.fact_semiconductor_revenue`: `semiconductor_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `semiconductor_revenue_amount`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (1) — Broadcom

For Broadcom, Of the more-than-$100-billion AI figure, how much is custom accelerators versus networking, and where do rack sales sit?

- `chip.price.fact_semiconductor_revenue`: `semiconductor_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `semiconductor_revenue_amount`
- `chip.price.fact_networking_revenue`: `networking_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `networking_revenue_amount`
- `chip.price.fact_accelerator_price`: `accelerator_price_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `revenue_per_accelerator_amount`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (2) — Broadcom

For Broadcom, How does hyperscaler work on internally owned XPU designs change Broadcom's custom programs?

- `chip.price.fact_semiconductor_revenue`: `semiconductor_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `semiconductor_revenue_amount`
- `chip.price.fact_networking_revenue`: `networking_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `networking_revenue_amount`
- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (3) — Broadcom

For Broadcom, What is pushing networking toward 40% of AI revenue in the near term, and does that mix hold longer term?

- `chip.price.fact_semiconductor_revenue`: `semiconductor_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `semiconductor_revenue_amount`
- `chip.price.fact_networking_revenue`: `networking_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `networking_revenue_amount`
- `chip.price.fact_systems_revenue`: `systems_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `systems_revenue_amount`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (3) — Broadcom

For Broadcom, How much further do gross margins dilute as high-bandwidth memory is passed through and system sales grow?

- `chip.price.fact_gross_margin`: `gross_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `gross_profit_amount`, `gross_margin_percent`
- `chip.price.fact_semiconductor_revenue`: `semiconductor_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `semiconductor_revenue_amount`
- `chip.price.fact_systems_revenue`: `systems_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `systems_revenue_amount`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2025 (5) — Broadcom

For Broadcom, What makes up the sequential AI revenue increase of nearly $1.7 billion in the guide?

- `chip.price.fact_semiconductor_revenue`: `semiconductor_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `semiconductor_revenue_amount`
- `chip.price.fact_systems_revenue`: `systems_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `systems_revenue_amount`
- `chip.price.fact_software_revenue`: `software_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `software_product_id`, `customer_type_id`, `software_revenue_amount`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2027 (7) — Nvidia

For Nvidia, Does revenue per gigawatt keep climbing past Vera Rubin, and is the ability to deploy more capacity linear or unlocked by something else?

- `chip.price.fact_content_per_gigawatt`: `content_per_gigawatt_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `revenue_per_gigawatt_amount`
- `chip.price.fact_accelerator_price`: `accelerator_price_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `revenue_per_accelerator_amount`
- `chip.supply.fact_manufacturing_capacity`: `manufacturing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `geography_id`, `product_family_id`, `packaging_capacity_count`, `test_capacity_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2027 (5) — Nvidia

For Nvidia, Is agentic CPU demand incremental to GPUs or a substitute, and is the cited Vera CPU revenue standalone or already inside Vera Rubin systems?

- `chip.price.fact_semiconductor_revenue`: `semiconductor_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `semiconductor_revenue_amount`
- `chip.price.fact_systems_revenue`: `systems_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `systems_revenue_amount`
- `chip.price.fact_content_per_gigawatt`: `content_per_gigawatt_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `revenue_per_gigawatt_amount`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (4) — Nvidia

For Nvidia, How feasible are space-based data centers, on what horizon, and how do the economics evolve from today?

- `chip.price.fact_content_per_gigawatt`: `content_per_gigawatt_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `revenue_per_gigawatt_amount`
- `chip.demand.fact_data_center_demand`: `data_center_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `data_center_gigawatt_quantity`, `accelerator_demand_count`
- `chip.supply.fact_cooling_capacity`: `cooling_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `cooling_type_id`, `product_family_id`, `cooled_system_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 FY2026 (7) — Nvidia

For Nvidia, Which application areas would have to accelerate for data-center capital spending to approach the multi-trillion dollar path discussed for 2030?

- `chip.price.fact_systems_revenue`: `systems_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `systems_revenue_amount`
- `chip.price.fact_content_per_gigawatt`: `content_per_gigawatt_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `revenue_per_gigawatt_amount`
- `chip.demand.fact_data_center_demand`: `data_center_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `data_center_gigawatt_quantity`, `accelerator_demand_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (1) — Nvidia

For Nvidia, Is the half-trillion-dollar Blackwell plus Rubin framework for calendar 2025 and 2026 still the right shape after shipments to date, and is there upside beyond it?

- `chip.price.fact_gross_margin`: `gross_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `gross_profit_amount`, `gross_margin_percent`
- `chip.price.fact_accelerator_price`: `accelerator_price_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `revenue_per_accelerator_amount`
- `chip.demand.fact_accelerator_shipments`: `accelerator_shipments_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `customer_type_id`, `geography_id`, `accelerator_shipment_count`, `system_shipment_count`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (3) — Nvidia

For Nvidia, What Nvidia content per gigawatt is embedded in that revenue framework, and how much of a multi-trillion 2030 data-center build needs vendor financing versus customer or government cash flow?

- `chip.price.fact_content_per_gigawatt`: `content_per_gigawatt_record_id`, `fiscal_quarter_id`, `scenario_id`, `customer_type_id`, `geography_id`, `revenue_per_gigawatt_amount`
- `chip.price.fact_systems_revenue`: `systems_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `systems_revenue_amount`
- `chip.price.fact_accelerator_price`: `accelerator_price_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `accelerator_type_id`, `revenue_per_accelerator_amount`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q3 FY2026 (6) — Nvidia

For Nvidia, What are the largest cost increases threatening mid-70s gross margin next year, how much is offset by cost work, pre-buys, or price, and how should operating expense grow against a much larger revenue base?

- `chip.price.fact_operating_expense`: `operating_expense_record_id`, `fiscal_quarter_id`, `scenario_id`, `cost_bucket_id`, `operating_expense_amount`
- `chip.price.fact_semiconductor_revenue`: `semiconductor_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_family_id`, `customer_type_id`, `geography_id`, `semiconductor_revenue_amount`
- `chip.price.fact_software_revenue`: `software_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `software_product_id`, `customer_type_id`, `software_revenue_amount`
- `chip.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `chip.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
