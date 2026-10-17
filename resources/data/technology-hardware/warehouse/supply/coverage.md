# Device Inc memory and silicon supply

This slice owns purchased memory and silicon, suppliers, sourcing, shipments, production, and channel inventory. Device Inc sits downstream of silicon: a silicon source is a company Device Inc can buy finished silicon from. The slice does not describe a wafer fab. Device family, channel, country, and calendar day are owned by the demand slice and are partial here. The device price file and service attachment are owned by the price slice.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `calendar_day_identity` | `calendar_day_id` | `sf:device.geography.dim_calendar_day` `calendar_day_id` |
| `channel_identity` | `channel_id` | `sf:device.channel.dim_channel` `channel_id` |
| `country_identity` | `country_id` | `sf:device.geography.dim_country` `country_id` |
| `currency_identity` | `currency_id` | `sf:device.price.dim_currency` `currency_id` |
| `device_family_identity` | `device_family_id` | `sf:device.product.dim_device_family` `device_family_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:device.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `product_generation_identity` | `product_generation_id` | `sf:device.product.dim_product_generation` `product_generation_id` |
| `sku_identity` | `sku_id` | `sf:device.product.dim_sku` `sku_id` |

## Numbered questions

### Q3 FY2026 (2)

Is wider memory sourcing meant to keep supply and cost in a range where capability does not force a disproportionate price increase?

- `device.supply.fact_memory_coverage`: `wider_sourcing_flag`, `cost_in_range_flag`, `capability_holds_flag`, `component_commodity_id`, `device_family_id`, `fiscal_quarter_id`
- `device.supply.fact_component_cost`: `inflation_rate`, `cost_change_amount`, `dislocated_flag`, `component_commodity_id`
- `device.price.fact_price_decision`: `disproportionate_increase_flag`, `used_price_lever_flag`, `lever_reason_code`, `device_family_id`
- `device.price.fact_price_file`: `unit_price`, `device_family_id`, `channel_id`, `country_id`, `calendar_day_id`

### Q3 FY2026 (5)

Can additional silicon sources ease the constraint in a useful time frame?

- `device.supply.fact_silicon_capacity`: `additional_source_flag`, `eases_constraint_flag`, `relief_timing_days`, `useful_timeframe_flag`, `silicon_source_id`, `component_id`, `fiscal_quarter_id`
- `device.supply.dim_silicon_source`: `source_role`, `source_name`
- `device.supply.fact_constraint_spread`: `spreading_flag`, `component_commodity_id`, `device_family_id`

### Q3 FY2026 (6)

Is the intent to lock multi-year supply at agreed prices, and how are product prices being set while costs are dislocated?

- `device.supply.fact_supply_agreement`: `multi_year_flag`, `agreed_unit_cost`, `contract_coverage_share`, `spot_exposure_share`, `sourcing_mode_id`, `component_commodity_id`, `fiscal_quarter_id`
- `device.supply.fact_component_cost`: `dislocated_flag`, `cost_change_amount`, `component_commodity_id`
- `device.price.fact_price_decision`: `used_price_lever_flag`, `product_price_change_amount`, `lever_reason_code`, `device_family_id`
- `device.price.fact_price_file`: `unit_price`, `device_family_id`, `channel_id`, `country_id`, `calendar_day_id`
- `device.supply.dim_sourcing_mode`: `mode_code`

### Q2 FY2026 (8)

How is memory, not only the main chip, being secured for iPhone, including sources outside the usual partners, and why is iPhone not expected to be constrained in June?

- `device.supply.fact_memory_coverage`: `outside_usual_partner_flag`, `coverage_sufficient_flag`, `quarter_constraint_expected_flag`, `component_commodity_id`, `supplier_id`, `device_family_id`, `fiscal_quarter_id`
- `device.component.dim_component_commodity`: `commodity_code`
- `device.supplier.dim_supplier`: `usual_partner_flag`, `supplier_name`
- `device.product.dim_device_family`: `family_code`
- `device.geography.dim_fiscal_quarter`: `quarter_code`

### Q1 FY2026 (6)

For memory, is Apple moving toward longer supply agreements or still buying more on the spot market?

- `device.supply.fact_supply_agreement`: `multi_year_flag`, `spot_exposure_share`, `contract_coverage_share`, `sourcing_mode_id`, `component_commodity_id`, `fiscal_quarter_id`
- `device.supply.dim_sourcing_mode`: `mode_code`
- `device.component.dim_component_commodity`: `commodity_code`

### Q1 FY2026 (10)

Is deeper in-house silicon already supporting gross margin, and where does more internalization go next?

- `device.supply.fact_custom_silicon`: `internal_content_share`, `supports_margin_flag`, `next_internalization_area`, `component_id`, `device_family_id`, `fiscal_quarter_id`
- `device.price.fact_margin_bridge`: `custom_silicon_effect_amount`, `fiscal_quarter_id`
- `device.component.dim_component`: `component_code`

### Q4 FY2025 (10)

Why do tariff costs rise less than the iPhone production step-up from September to December, and how should the timing of those costs be read?

- `device.supply.fact_tariff_accrual`: `tariff_cost_amount`, `prior_quarter_tariff_cost_amount`, `lags_production_flag`, `device_family_id`, `fiscal_quarter_id`
- `device.supply.fact_production`: `production_quantity`, `sequential_step_up_quantity`, `device_family_id`, `fiscal_quarter_id`
- `device.product.dim_device_family`: `family_code`
- `device.geography.dim_fiscal_quarter`: `quarter_code`

## Datasets

| Qualified name | Role | Questions served |
| --- | --- | --- |
| `device.component.dim_component_class` | dimension | join support |
| `device.component.dim_component_commodity` | dimension | Q2 FY2026 (8), Q1 FY2026 (6) |
| `device.supply.dim_silicon_source` | dimension | Q3 FY2026 (5) |
| `device.supplier.dim_supplier` | dimension | Q2 FY2026 (8) |
| `device.supplier.dim_supplier_site` | dimension | join support |
| `device.supply.dim_sourcing_mode` | dimension | Q3 FY2026 (6), Q1 FY2026 (6) |
| `device.component.dim_component` | dimension | Q1 FY2026 (10) |
| `device.supply.fact_constraint_spread` | fact | Q3 FY2026 (5) |
| `device.supply.fact_memory_coverage` | fact | Q3 FY2026 (2), Q2 FY2026 (8) |
| `device.supply.fact_supply_agreement` | fact | Q3 FY2026 (6), Q1 FY2026 (6) |
| `device.supply.fact_component_cost` | fact | Q3 FY2026 (2), Q3 FY2026 (6) |
| `device.supply.fact_silicon_capacity` | fact | Q3 FY2026 (5) |
| `device.supply.fact_device_shipment` | fact | join support |
| `device.supply.fact_shipment_line` | fact | join support |
| `device.supply.fact_channel_inventory` | fact | join support |
| `device.supply.fact_production` | fact | Q4 FY2025 (10) |
| `device.supply.fact_tariff_accrual` | fact | Q4 FY2025 (10) |
| `device.supply.fact_custom_silicon` | fact | Q1 FY2026 (10) |
