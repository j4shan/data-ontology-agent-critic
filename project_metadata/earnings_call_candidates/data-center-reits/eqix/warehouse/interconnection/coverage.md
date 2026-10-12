# Colocation Inc interconnection, customer vertical, and metro coverage

This slice owns the metro, the region, the customer, the customer vertical, and interconnection. A cross-connect is not a lease line. Interconnection revenue is not space revenue and not power. Total company revenue, bookings, and power density stay in the slices that own those populations. Those identities are partial here and are not re-authored.

Foreign identities are referenced from this slice and are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column | Node |
| --- | --- | --- |
| `density_class_identity` | `density_class_id` | `sf:colocation.power.dim_density_class` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:colocation.calendar.dim_fiscal_quarter` |
| `fiscal_year_identity` | `fiscal_year_id` | `sf:colocation.calendar.dim_fiscal_year` |
| `ibx_identity` | `ibx_id` | `sf:colocation.power.dim_ibx` |
| `workload_type_identity` | `workload_type_id` | `sf:colocation.occupancy.dim_workload_type` |

## Complete populations

| Identity | Dataset | Column |
| --- | --- | --- |
| `region_identity` | `colocation.interconnection.dim_region` | `region_id` |
| `metro_identity` | `colocation.interconnection.dim_metro` | `metro_id` |
| `customer_vertical_identity` | `colocation.interconnection.dim_customer_vertical` | `customer_vertical_id` |
| `customer_identity` | `colocation.interconnection.dim_customer` | `customer_id` |
| `network_identity` | `colocation.interconnection.dim_network` | `network_id` |
| `interconnect_type_identity` | `colocation.interconnection.dim_interconnect_type` | `interconnect_type_id` |
| `demand_source_identity` | `colocation.interconnection.dim_demand_source` | `demand_source_id` |
| `cloud_product_identity` | `colocation.interconnection.dim_cloud_product` | `cloud_product_id` |
| `cross_connect_identity` | `colocation.interconnection.fact_cross_connect` | `cross_connect_id` |
| `interconnect_net_add_identity` | `colocation.interconnection.fact_interconnect_net_add` | `net_add_id` |
| `interconnect_price_identity` | `colocation.interconnection.fact_interconnect_price` | `interconnect_price_id` |
| `interconnect_revenue_identity` | `colocation.interconnection.fact_interconnect_revenue` | `interconnect_revenue_id` |
| `attach_rate_identity` | `colocation.interconnection.fact_attach_rate` | `attach_rate_id` |
| `on_ramp_identity` | `colocation.interconnection.fact_on_ramp` | `on_ramp_id` |
| `multicloud_effect_identity` | `colocation.interconnection.fact_multicloud_effect` | `multicloud_effect_id` |
| `inference_link_identity` | `colocation.interconnection.fact_inference_link` | `inference_link_id` |
| `arpu_driver_identity` | `colocation.interconnection.fact_arpu_driver` | `arpu_driver_id` |
| `customer_mix_identity` | `colocation.interconnection.fact_customer_mix` | `customer_mix_id` |

## Numbered questions

### Q2 2026 (3) — Where interconnection net adds come from, and price room

`colocation.interconnection.fact_interconnect_net_add.net_add_count` and `price_opportunity_flag` by `demand_source_id`. Price room is `colocation.interconnection.fact_interconnect_price.price_amount` and `price_increase_room_flag`. `customer_vertical_id` and `metro_id` are the mix and the market.

### Q1 2026 (1) — AI-provider and neo-cloud nodes versus the installed base

`colocation.interconnection.fact_on_ramp.node_count`, `installed_base_node_count`, and `additive_flag`. `interconnect_type_id` joins `colocation.interconnection.dim_interconnect_type.type_code` for neo_cloud_on_ramp and network_node. `customer_vertical_id` joins `vertical_code` for ai_provider and neo_cloud. `metro_id` places the node.

### Q1 2026 (6) — Interconnection growth versus the rest of revenue

`colocation.interconnection.fact_interconnect_revenue.interconnect_revenue_amount`, `interconnect_growth_rate`, and `revenue_share`. Total revenue and its growth are `colocation.occupancy.fact_revenue_quarter.total_revenue_amount` and `revenue_growth_rate` on the same `fiscal_quarter_id` and `region_id`.

### Q4 2025 (8) — Multi-cloud products and the interconnection franchise

`colocation.interconnection.fact_multicloud_effect.interconnect_demand_change` and `franchise_effect`. `cloud_product_id` joins `colocation.interconnection.dim_cloud_product.multicloud_flag` and `network_id`. `metro_id` places the effect.

### Q4 2025 (9) — Training-to-inference timing and interconnection for enterprise inference

`colocation.interconnection.fact_inference_link.training_share`, `inference_share`, `timing_stage`, and `interconnect_importance_score`. `workload_type_id` joins `colocation.occupancy.dim_workload_type.workload_code` for training and enterprise_inference. `fiscal_year_id` is the timing.

### Q3 2025 (1) — Neo-cloud on-ramps versus traditional cloud on-ramps

`colocation.interconnection.fact_on_ramp.node_count` and `strategic_rank` by `interconnect_type_id`. `colocation.interconnection.dim_interconnect_type.type_code` separates neo_cloud_on_ramp from cloud_on_ramp. `customer_vertical_id` keeps enterprise demand visible. `metro_id` is the market.

### Q3 2025 (10) — Cross-connect revenue and ARPU from density or mix

`colocation.interconnection.fact_arpu_driver.cross_connect_revenue_amount`, `arpu_amount`, `density_effect_amount`, and `mix_effect_amount`. `density_class_id` joins `colocation.power.dim_density_class.class_name`. `customer_vertical_id` is the mix. `colocation.interconnection.fact_customer_mix.interconnect_share` is the vertical share in the metro.

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `colocation.interconnection.dim_region` | supporting population |
| `colocation.interconnection.dim_metro` | supporting population |
| `colocation.interconnection.dim_customer_vertical` | supporting population |
| `colocation.interconnection.dim_customer` | supporting population |
| `colocation.interconnection.dim_network` | supporting population |
| `colocation.interconnection.dim_interconnect_type` | Q1 2026 (1), Q3 2025 (1) |
| `colocation.interconnection.dim_demand_source` | supporting population |
| `colocation.interconnection.dim_cloud_product` | Q4 2025 (8) |
| `colocation.interconnection.fact_cross_connect` | supporting population |
| `colocation.interconnection.fact_interconnect_net_add` | Q2 2026 (3) |
| `colocation.interconnection.fact_interconnect_price` | Q2 2026 (3) |
| `colocation.interconnection.fact_interconnect_revenue` | Q1 2026 (6) |
| `colocation.interconnection.fact_attach_rate` | supporting population |
| `colocation.interconnection.fact_on_ramp` | Q1 2026 (1), Q3 2025 (1) |
| `colocation.interconnection.fact_multicloud_effect` | Q4 2025 (8) |
| `colocation.interconnection.fact_inference_link` | Q4 2025 (9) |
| `colocation.interconnection.fact_arpu_driver` | Q3 2025 (10) |
| `colocation.interconnection.fact_customer_mix` | Q3 2025 (10) |
