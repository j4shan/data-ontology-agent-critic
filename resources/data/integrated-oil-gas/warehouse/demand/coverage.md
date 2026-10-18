# Energy Inc demand, customer, and geography

This slice is part of the Energy Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity row does not store a price. A price row does not store the unit quantity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `dim_play_identity` | `play_id` | `energy.resource.dim_play` `play_id` |

## Numbered questions

### Q4 2025 (9) — Exxon Mobil

For Exxon Mobil, are there green shoots in base chemicals on supply or demand, versus competitors?

- `energy.demand.fact_chemical_demand`: `demand_quantity`, `feedstock_short_flag`, `green_shoot_flag`, `fiscal_quarter_id`, `product_id`, `country_id`
- `energy.supply.fact_chemical_capacity`: `capacity_quantity`, `us_heavy_flag`, `feedstock_advantage_flag`, `fiscal_quarter_id`, `facility_id`, `country_id`
- `energy.demand.fact_product_demand`: `demand_quantity`, `destruction_flag`, `shortage_flag`, `fiscal_quarter_id`, `product_id`, `market_id`, `country_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`
- `energy.geography.dim_country`: `country_id`, `country_code`, `country_name`, `region_id`
- `energy.resource.dim_facility`: `facility_id`, `facility_code`, `facility_name`, `country_id`, `market_id`
- `energy.geography.dim_market`: `market_id`, `market_code`, `market_name`, `region_id`

### Q3 2025 (11) — Exxon Mobil

For Exxon Mobil, how should the data-center capital boom be read against a lower company capital-spending outlook?

- `energy.demand.fact_data_center_demand`: `interest_quantity`, `material_flag`, `ordinary_gas_alternative_flag`, `fiscal_quarter_id`, `customer_id`, `product_id`
- `energy.price.fact_capital_spend`: `spend_amount`, `below_range_flag`, `in_range_flag`, `fiscal_quarter_id`, `capital_item_id`
- `energy.supply.fact_power_capacity`: `capacity_quantity`, `later_project_flag`, `fiscal_quarter_id`, `project_id`, `facility_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`
- `energy.price.dim_capital_item`: `capital_item_id`, `item_code`, `item_name`
- `energy.resource.dim_project`: `project_id`, `project_code`, `project_name`, `country_id`, `asset_id`

### Q4 2024 (3) — Exxon Mobil

For Exxon Mobil, is there demand for low-carbon gas for data centers versus ordinary gas power?

- `energy.demand.fact_data_center_demand`: `interest_quantity`, `material_flag`, `ordinary_gas_alternative_flag`, `fiscal_quarter_id`, `customer_id`, `product_id`
- `energy.demand.fact_low_carbon_demand`: `demand_quantity`, `prefers_low_carbon_flag`, `fiscal_quarter_id`, `customer_id`, `product_id`
- `energy.price.fact_capture_commercial`: `commercial_stage_code`, `challenge_code`, `customer_interest_flag`, `fiscal_quarter_id`, `customer_id`, `contract_id`
- `energy.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `energy.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `energy.customer.dim_product`: `product_id`, `product_code`, `product_name`
- `energy.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `product_id`
