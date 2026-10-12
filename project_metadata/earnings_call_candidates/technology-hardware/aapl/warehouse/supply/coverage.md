# Apple memory and silicon supply

This slice owns purchased memory and silicon, suppliers, sourcing, shipments, production, and channel inventory. Apple sits downstream of silicon: a silicon source is a company Apple can buy finished silicon from. The slice does not describe a wafer fab. Device family, channel, country, and calendar day are owned by the demand slice and are partial here. The device price file and service attachment are owned by the price slice.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `calendar_day_identity` | `calendar_day_id` | `sf:apple.geography.dim_calendar_day` `calendar_day_id` |
| `channel_identity` | `channel_id` | `sf:apple.channel.dim_channel` `channel_id` |
| `country_identity` | `country_id` | `sf:apple.geography.dim_country` `country_id` |
| `currency_identity` | `currency_id` | `sf:apple.price.dim_currency` `currency_id` |
| `device_family_identity` | `device_family_id` | `sf:apple.product.dim_device_family` `device_family_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:apple.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `product_generation_identity` | `product_generation_id` | `sf:apple.product.dim_product_generation` `product_generation_id` |
| `sku_identity` | `sku_id` | `sf:apple.product.dim_sku` `sku_id` |

## Numbered questions

### Q3 FY2026 (2)

Is wider memory sourcing meant to keep supply and cost in a range where capability does not force a disproportionate price increase?

- `apple.supply.fact_memory_coverage`: `wider_sourcing_flag`, `cost_in_range_flag`, `capability_holds_flag`, `component_commodity_id`, `device_family_id`, `fiscal_quarter_id`
- `apple.supply.fact_component_cost`: `inflation_rate`, `cost_change_amount`, `dislocated_flag`, `component_commodity_id`
- `apple.price.fact_price_decision`: `disproportionate_increase_flag`, `used_price_lever_flag`, `lever_reason_code`, `device_family_id`
- `apple.price.fact_price_file`: `unit_price`, `device_family_id`, `channel_id`, `country_id`, `calendar_day_id`

### Q3 FY2026 (5)

Can additional silicon sources ease the constraint in a useful time frame?

- `apple.supply.fact_silicon_capacity`: `additional_source_flag`, `eases_constraint_flag`, `relief_timing_days`, `useful_timeframe_flag`, `silicon_source_id`, `component_id`, `fiscal_quarter_id`
- `apple.supply.dim_silicon_source`: `source_role`, `source_name`
- `apple.supply.fact_constraint_spread`: `spreading_flag`, `component_commodity_id`, `device_family_id`

### Q3 FY2026 (6)

Is the intent to lock multi-year supply at agreed prices, and how are product prices being set while costs are dislocated?

- `apple.supply.fact_supply_agreement`: `multi_year_flag`, `agreed_unit_cost`, `contract_coverage_share`, `spot_exposure_share`, `sourcing_mode_id`, `component_commodity_id`, `fiscal_quarter_id`
- `apple.supply.fact_component_cost`: `dislocated_flag`, `cost_change_amount`, `component_commodity_id`
- `apple.price.fact_price_decision`: `used_price_lever_flag`, `product_price_change_amount`, `lever_reason_code`, `device_family_id`
- `apple.price.fact_price_file`: `unit_price`, `device_family_id`, `channel_id`, `country_id`, `calendar_day_id`
- `apple.supply.dim_sourcing_mode`: `mode_code`

### Q2 FY2026 (8)

How is memory, not only the main chip, being secured for iPhone, including sources outside the usual partners, and why is iPhone not expected to be constrained in June?

- `apple.supply.fact_memory_coverage`: `outside_usual_partner_flag`, `coverage_sufficient_flag`, `quarter_constraint_expected_flag`, `component_commodity_id`, `supplier_id`, `device_family_id`, `fiscal_quarter_id`
- `apple.component.dim_component_commodity`: `commodity_code`
- `apple.supplier.dim_supplier`: `usual_partner_flag`, `supplier_name`
- `apple.product.dim_device_family`: `family_code`
- `apple.geography.dim_fiscal_quarter`: `quarter_code`

### Q1 FY2026 (6)

For memory, is Apple moving toward longer supply agreements or still buying more on the spot market?

- `apple.supply.fact_supply_agreement`: `multi_year_flag`, `spot_exposure_share`, `contract_coverage_share`, `sourcing_mode_id`, `component_commodity_id`, `fiscal_quarter_id`
- `apple.supply.dim_sourcing_mode`: `mode_code`
- `apple.component.dim_component_commodity`: `commodity_code`

### Q1 FY2026 (10)

Is deeper in-house silicon already supporting gross margin, and where does more internalization go next?

- `apple.supply.fact_custom_silicon`: `internal_content_share`, `supports_margin_flag`, `next_internalization_area`, `component_id`, `device_family_id`, `fiscal_quarter_id`
- `apple.price.fact_margin_bridge`: `custom_silicon_effect_amount`, `fiscal_quarter_id`
- `apple.component.dim_component`: `component_code`

### Q4 FY2025 (10)

Why do tariff costs rise less than the iPhone production step-up from September to December, and how should the timing of those costs be read?

- `apple.supply.fact_tariff_accrual`: `tariff_cost_amount`, `prior_quarter_tariff_cost_amount`, `lags_production_flag`, `device_family_id`, `fiscal_quarter_id`
- `apple.supply.fact_production`: `production_quantity`, `sequential_step_up_quantity`, `device_family_id`, `fiscal_quarter_id`
- `apple.product.dim_device_family`: `family_code`
- `apple.geography.dim_fiscal_quarter`: `quarter_code`

## Datasets

| Qualified name | Role | Questions served |
| --- | --- | --- |
| `apple.component.dim_component_class` | dimension | join support |
| `apple.component.dim_component_commodity` | dimension | Q2 FY2026 (8), Q1 FY2026 (6) |
| `apple.supply.dim_silicon_source` | dimension | Q3 FY2026 (5) |
| `apple.supplier.dim_supplier` | dimension | Q2 FY2026 (8) |
| `apple.supplier.dim_supplier_site` | dimension | join support |
| `apple.supply.dim_sourcing_mode` | dimension | Q3 FY2026 (6), Q1 FY2026 (6) |
| `apple.component.dim_component` | dimension | Q1 FY2026 (10) |
| `apple.supply.fact_constraint_spread` | fact | Q3 FY2026 (5) |
| `apple.supply.fact_memory_coverage` | fact | Q3 FY2026 (2), Q2 FY2026 (8) |
| `apple.supply.fact_supply_agreement` | fact | Q3 FY2026 (6), Q1 FY2026 (6) |
| `apple.supply.fact_component_cost` | fact | Q3 FY2026 (2), Q3 FY2026 (6) |
| `apple.supply.fact_silicon_capacity` | fact | Q3 FY2026 (5) |
| `apple.supply.fact_device_shipment` | fact | join support |
| `apple.supply.fact_shipment_line` | fact | join support |
| `apple.supply.fact_channel_inventory` | fact | join support |
| `apple.supply.fact_production` | fact | Q4 FY2025 (10) |
| `apple.supply.fact_tariff_accrual` | fact | Q4 FY2025 (10) |
| `apple.supply.fact_custom_silicon` | fact | Q1 FY2026 (10) |
