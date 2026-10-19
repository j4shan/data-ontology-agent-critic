# Colocation Inc interconnection

Cross-connect quantity, price, revenue per unit and on-ramps. Portfolio revenue and AFFO/FFO live in the finance slice described in MODEL.md; their question rows are filed with occupancy because the source slices retain three coverage files.

Every fact below uses `fiscal_period_id` for the fiscal period and `scenario_id` for the scenario (`reported` or `guide` in `dim_scenario`). Measure descriptions in the YAML name the unit.

## Equinix (EQIX)

### Q2 2026 (2)

Are AI strategies changing deal size, market mix, or interconnection attach rates?

- `colocation.interconnection.fact_cross_connect_quantity`: `active_cross_connect_count`, `added_cross_connect_count`, `interconnect_product_id`, `metro_id`
- `colocation.interconnection.fact_cross_connect_price`: `monthly_price_amount`
- `colocation.interconnection.fact_cross_connect_revenue_per_unit`: `revenue_per_cross_connect_amount`
- `colocation.interconnection.fact_interconnection_revenue_amount`: `interconnection_revenue_amount`, `region_id`

### Q2 2026 (3)

Where is the step-up in interconnection demand coming from, and is there room to price interconnection higher over time?

- `colocation.interconnection.fact_cross_connect_quantity`: `active_cross_connect_count`, `added_cross_connect_count`, `interconnect_product_id`, `metro_id`
- `colocation.interconnection.fact_cross_connect_price`: `monthly_price_amount`
- `colocation.interconnection.fact_cross_connect_revenue_per_unit`: `revenue_per_cross_connect_amount`
- `colocation.interconnection.fact_interconnection_revenue_amount`: `interconnection_revenue_amount`, `region_id`

### Q1 2026 (1)

Are the AI-provider and neo-cloud expansions, including the network nodes, additive to the prior installed base?

- `colocation.interconnection.fact_cross_connect_quantity`: `active_cross_connect_count`, `added_cross_connect_count`, `interconnect_product_id`, `metro_id`
- `colocation.interconnection.fact_cross_connect_price`: `monthly_price_amount`
- `colocation.interconnection.fact_cross_connect_revenue_per_unit`: `revenue_per_cross_connect_amount`
- `colocation.interconnection.fact_interconnection_revenue_amount`: `interconnection_revenue_amount`, `region_id`

### Q1 2026 (6)

Could interconnection growth outrun the rest of the business and become a larger share of revenue?

- `colocation.interconnection.fact_cross_connect_quantity`: `active_cross_connect_count`, `added_cross_connect_count`, `interconnect_product_id`, `metro_id`
- `colocation.interconnection.fact_cross_connect_price`: `monthly_price_amount`
- `colocation.interconnection.fact_cross_connect_revenue_per_unit`: `revenue_per_cross_connect_amount`
- `colocation.interconnection.fact_interconnection_revenue_amount`: `interconnection_revenue_amount`, `region_id`

### Q4 2025 (1)

Are the large AI bookings coming from enterprises adopting AI or from hyperscaler edge nodes?

- `colocation.interconnection.fact_cross_connect_quantity`: `active_cross_connect_count`, `added_cross_connect_count`, `interconnect_product_id`, `metro_id`
- `colocation.interconnection.fact_cross_connect_price`: `monthly_price_amount`
- `colocation.interconnection.fact_cross_connect_revenue_per_unit`: `revenue_per_cross_connect_amount`
- `colocation.interconnection.fact_interconnection_revenue_amount`: `interconnection_revenue_amount`, `region_id`

### Q4 2025 (8)

How do cloud providers' multi-cloud products affect the interconnection franchise?

- `colocation.interconnection.fact_cross_connect_quantity`: `active_cross_connect_count`, `added_cross_connect_count`, `interconnect_product_id`, `metro_id`
- `colocation.interconnection.fact_cross_connect_price`: `monthly_price_amount`
- `colocation.interconnection.fact_cross_connect_revenue_per_unit`: `revenue_per_cross_connect_amount`
- `colocation.interconnection.fact_interconnection_revenue_amount`: `interconnection_revenue_amount`, `region_id`

### Q4 2025 (9)

What is the updated timing of the shift from AI training to inference, and how important is interconnection to winning enterprise inference?

- `colocation.interconnection.fact_cross_connect_quantity`: `active_cross_connect_count`, `added_cross_connect_count`, `interconnect_product_id`, `metro_id`
- `colocation.interconnection.fact_cross_connect_price`: `monthly_price_amount`
- `colocation.interconnection.fact_cross_connect_revenue_per_unit`: `revenue_per_cross_connect_amount`
- `colocation.interconnection.fact_interconnection_revenue_amount`: `interconnection_revenue_amount`, `region_id`

### Q3 2025 (1)

How strategic are neo-cloud on-ramps relative to traditional cloud on-ramps?

- `colocation.interconnection.fact_cross_connect_quantity`: `active_cross_connect_count`, `added_cross_connect_count`, `interconnect_product_id`, `metro_id`
- `colocation.interconnection.fact_cross_connect_price`: `monthly_price_amount`
- `colocation.interconnection.fact_cross_connect_revenue_per_unit`: `revenue_per_cross_connect_amount`
- `colocation.interconnection.fact_interconnection_revenue_amount`: `interconnection_revenue_amount`, `region_id`

### Q3 2025 (10)

What is driving the cross-connect revenue and ARPU increase: power density or customer mix?

- `colocation.interconnection.fact_cross_connect_quantity`: `active_cross_connect_count`, `added_cross_connect_count`, `interconnect_product_id`, `metro_id`
- `colocation.interconnection.fact_cross_connect_price`: `monthly_price_amount`
- `colocation.interconnection.fact_cross_connect_revenue_per_unit`: `revenue_per_cross_connect_amount`
- `colocation.interconnection.fact_interconnection_revenue_amount`: `interconnection_revenue_amount`, `region_id`

## Digital Realty (DLR)

### Q1 2026 (3)

Can the 0–1 megawatt run rate move toward a higher level, and what does that mean for interconnection?

- `colocation.interconnection.fact_cross_connect_quantity`: `active_cross_connect_count`, `added_cross_connect_count`, `interconnect_product_id`, `metro_id`
- `colocation.interconnection.fact_cross_connect_price`: `monthly_price_amount`
- `colocation.interconnection.fact_cross_connect_revenue_per_unit`: `revenue_per_cross_connect_amount`
- `colocation.interconnection.fact_interconnection_revenue_amount`: `interconnection_revenue_amount`, `region_id`

### Q4 2025 (7)

Why were Malaysia, Israel, and Portugal entered with interconnection-focused sites rather than larger hyperscale builds?

- `colocation.interconnection.fact_cross_connect_quantity`: `active_cross_connect_count`, `added_cross_connect_count`, `interconnect_product_id`, `metro_id`
- `colocation.interconnection.fact_cross_connect_price`: `monthly_price_amount`
- `colocation.interconnection.fact_cross_connect_revenue_per_unit`: `revenue_per_cross_connect_amount`
- `colocation.interconnection.fact_interconnection_revenue_amount`: `interconnection_revenue_amount`, `region_id`
