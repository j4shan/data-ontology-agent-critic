# Beverage Inc bottler and commodity supply

This slice owns bottlers, plants, commodity cover, and service levels for Beverage Inc. Capacity and cover live here. Commodity cost and the price file live in price_margin. Unit cases live in demand_channel.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `country_identity` | `country_id` | `sf:beverage.geography.dim_country` `country_id` |
| `country_identity` | `country_id` | `sf:beverage.geography.dim_country` `country_id` |
| `country_identity` | `country_id` | `sf:beverage.geography.dim_country` `country_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:beverage.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `brand_identity` | `brand_id` | `sf:beverage.product.dim_brand` `brand_id` |
| `country_identity` | `country_id` | `sf:beverage.geography.dim_country` `country_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:beverage.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `country_identity` | `country_id` | `sf:beverage.geography.dim_country` `country_id` |
| `brand_identity` | `brand_id` | `sf:beverage.product.dim_brand` `brand_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:beverage.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:beverage.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `country_identity` | `country_id` | `sf:beverage.geography.dim_country` `country_id` |
| `brand_identity` | `brand_id` | `sf:beverage.product.dim_brand` `brand_id` |
| `customer_identity` | `customer_id` | `sf:beverage.customer.dim_customer` `customer_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:beverage.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `brand_identity` | `brand_id` | `sf:beverage.product.dim_brand` `brand_id` |
| `country_identity` | `country_id` | `sf:beverage.geography.dim_country` `country_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:beverage.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `country_identity` | `country_id` | `sf:beverage.geography.dim_country` `country_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:beverage.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `brand_identity` | `brand_id` | `sf:beverage.product.dim_brand` `brand_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:beverage.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `country_identity` | `country_id` | `sf:beverage.geography.dim_country` `country_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:beverage.time.dim_fiscal_quarter` `fiscal_quarter_id` |
| `region_identity` | `region_id` | `sf:beverage.geography.dim_region` `region_id` |
| `brand_identity` | `brand_id` | `sf:beverage.product.dim_brand` `brand_id` |

## Numbered questions

## Coca-Cola

### Q2 2025 (2)

How much U.S. volume does the early-2026 fairlife capacity add unlock, and does it let the three fairlife product lines be managed differently?

- `beverage.supply.fact_plant_capacity`: `fiscal_quarter_id`, `plant_id`, `brand_id`, `country_id`, `capacity_quantity`, `replicable_abroad_flag`
- `beverage.demand.fact_brand_volume`: `fiscal_quarter_id`, `brand_id`, `country_id`, `product_line_id`, `line_managed_separately_flag`, `unit_case_quantity`
- `beverage.product.dim_product_line`: `brand_id`, `product_line_code`, `product_line_name`
- `beverage.supply.dim_plant`: `country_id`, `bottler_id`, `plant_code`, `plant_name`

### Q2 2025 (3)

How realistic is fairlife expansion outside North America over the next few years given the dairy manufacturing footprint?

- `beverage.supply.fact_plant_capacity`: `fiscal_quarter_id`, `plant_id`, `brand_id`, `country_id`, `replicable_abroad_flag`, `capacity_quantity`
- `beverage.supply.dim_plant`: `country_id`, `bottler_id`, `plant_code`, `plant_name`
- `beverage.geography.dim_region`: `region_code`, `region_name`
- `beverage.product.dim_brand`: `category_id`, `brand_code`, `brand_name`

### Q4 2024 (5)

Where does the largely local supply chain still have import and export exposure if tariffs rise?

- `beverage.supply.fact_trade_lane`: `fiscal_quarter_id`, `country_id`, `commodity_id`, `plant_id`, `local_flag`, `export_exposed_flag`
- `beverage.price.fact_tariff`: `fiscal_quarter_id`, `country_id`, `commodity_id`, `exposed_flag`, `tariff_rate`

### Q4 2024 (11)

What does the local partner that took 40% of the India bottling business bring that could accelerate that market?

- `beverage.supply.fact_bottler_partner`: `fiscal_quarter_id`, `bottler_id`, `country_id`, `accelerates_flag`, `ownership_share`
- `beverage.supply.dim_bottler`: `country_id`, `bottler_code`, `bottler_name`
- `beverage.demand.fact_refranchising`: `fiscal_quarter_id`, `country_id`, `bottler_id`, `marketing_steps_up_flag`, `remaining_share`
- `beverage.geography.dim_country`: `region_id`, `country_code`, `country_name`

## PepsiCo

### Q1 2026 (1)

What cost assumptions changed because of the Iran conflict, how locked are hedges and contracts, and what internal offsets protect 2026 earnings visibility?

- `beverage.supply.fact_commodity_cover`: `fiscal_quarter_id`, `commodity_id`, `currency_id`, `locked_share`, `coverage_months`
- `beverage.price.fact_input_cost`: `fiscal_quarter_id`, `commodity_id`, `country_id`, `cost_amount`, `internal_offset_flag`, `changed_flag`
- `beverage.supply.dim_currency`: `country_id`, `currency_code`, `currency_name`
- `beverage.time.dim_fiscal_quarter`: `guidance_horizon`, `fiscal_quarter_code`, `fiscal_quarter_name`

### Q1 2026 (8)

Are PepsiCo Beverages North America value shares still declining, and will the strategic review cover share recovery as well as the bottler network?

- `beverage.supply.fact_bottler_review`: `fiscal_quarter_id`, `bottler_id`, `region_id`, `brand_id`, `covers_network_flag`, `covers_share_flag`
- `beverage.demand.fact_value_share`: `fiscal_quarter_id`, `brand_id`, `region_id`, `category_id`, `declining_flag`, `value_share_rate`
- `beverage.supply.dim_bottler`: `country_id`, `bottler_code`, `bottler_name`
- `beverage.geography.dim_region`: `region_code`, `region_name`
