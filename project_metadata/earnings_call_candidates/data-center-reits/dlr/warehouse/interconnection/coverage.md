# Digital Realty interconnection and customer-mix coverage

This slice owns the metro, the region, the customer, the customer vertical, and interconnection. A new-market interconnection site is not a hyperscale build. Small-block bookings and land settings are referenced and not re-authored.

Foreign identities are referenced from this slice and are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column | Node |
| --- | --- | --- |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:digitalrealty.calendar.dim_fiscal_quarter` |
| `fiscal_year_identity` | `fiscal_year_id` | `sf:digitalrealty.calendar.dim_fiscal_year` |
| `market_setting_identity` | `market_setting_id` | `sf:digitalrealty.land.dim_market_setting` |
| `megawatt_band_identity` | `megawatt_band_id` | `sf:digitalrealty.lease.dim_megawatt_band` |

## Complete populations

| Identity | Dataset | Column |
| --- | --- | --- |
| `region_identity` | `digitalrealty.interconnection.dim_region` | `region_id` |
| `metro_identity` | `digitalrealty.interconnection.dim_metro` | `metro_id` |
| `customer_vertical_identity` | `digitalrealty.interconnection.dim_customer_vertical` | `customer_vertical_id` |
| `customer_identity` | `digitalrealty.interconnection.dim_customer` | `customer_id` |
| `entry_product_identity` | `digitalrealty.interconnection.dim_entry_product` | `entry_product_id` |
| `interconnect_flow_identity` | `digitalrealty.interconnection.fact_interconnect_flow` | `interconnect_flow_id` |
| `market_entry_identity` | `digitalrealty.interconnection.fact_market_entry` | `market_entry_id` |
| `large_block_mix_identity` | `digitalrealty.interconnection.fact_large_block_mix` | `large_block_mix_id` |
| `latency_demand_identity` | `digitalrealty.interconnection.fact_latency_demand` | `latency_demand_id` |
| `peer_supply_identity` | `digitalrealty.interconnection.fact_peer_supply` | `peer_supply_id` |

## Numbered questions

### Q4 2025 (7) — Malaysia, Israel, and Portugal entered as interconnection sites

`digitalrealty.interconnection.fact_market_entry.interconnection_choice_flag` and `local_hyperscale_project_flag`. `entry_product_id` joins `digitalrealty.interconnection.dim_entry_product.product_code` interconnection_site or hyperscale_build. `metro_id` joins `digitalrealty.interconnection.dim_metro.country_name` for Malaysia, Israel, and Portugal.

### Q3 2025 (2) — Latency-sensitive AI in major metros versus gigawatt campuses

`digitalrealty.interconnection.fact_latency_demand.demand_mw`. `market_setting_id` joins `digitalrealty.land.dim_market_setting.setting_code` major_metro or remote. `customer_vertical_id` joins `vertical_code` hyperscaler.

### Q3 2025 (4) — Large-block demand across neo-clouds, model developers, chip companies, and hyperscalers

`digitalrealty.interconnection.fact_large_block_mix.pipeline_mw` and `concentration_share`. `customer_vertical_id` joins `vertical_code` for neo_cloud, model_developer, chip_company, and hyperscaler. `region_id` places the pipeline.

### Q2 2025 (7) — Share taken in 0 to 1 megawatt while peers build larger blocks

`digitalrealty.interconnection.fact_peer_supply.peer_supply_mw`, `company_booking_mw`, and `share_taken_flag`. `megawatt_band_id` joins `digitalrealty.lease.dim_megawatt_band.band_code`. Company small-block demand is `digitalrealty.lease.fact_market_demand.company_booked_mw` for mw_0_1.

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `digitalrealty.interconnection.dim_region` | supporting population |
| `digitalrealty.interconnection.dim_metro` | Q4 2025 (7) |
| `digitalrealty.interconnection.dim_customer_vertical` | supporting population |
| `digitalrealty.interconnection.dim_customer` | supporting population |
| `digitalrealty.interconnection.dim_entry_product` | Q4 2025 (7) |
| `digitalrealty.interconnection.fact_interconnect_flow` | supporting population |
| `digitalrealty.interconnection.fact_market_entry` | Q4 2025 (7) |
| `digitalrealty.interconnection.fact_large_block_mix` | Q3 2025 (4) |
| `digitalrealty.interconnection.fact_latency_demand` | Q3 2025 (2) |
| `digitalrealty.interconnection.fact_peer_supply` | Q2 2025 (7) |
