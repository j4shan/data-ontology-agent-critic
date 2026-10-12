# Truck Inc end markets, plants, and product mix

This slice owns the end market, the truck family, the powertrain, the plant, the supplier, and the mix of regions, local-for-local production, emissions rules, and parts sourcing. Dealer inventory, retail ranges, price, volume, and backlog are owned outside this slice. Those identities are partial here and are not re-authored.

Foreign identities are referenced from this slice and are partial here. Their complete populations are the datasets below, which this slice does not author:

| Identity | Column | Node |
| --- | --- | --- |
| `accounting_period_identity` | `accounting_period_id` | `sf:truck.calendar.dim_accounting_period` |
| `currency_identity` | `currency_id` | `sf:truck.commercial.dim_currency` |
| `region_identity` | `region_id` | `sf:truck.organization.dim_region` |

## Numbered questions

### Q2 2026 (6) — Penalty versus the cost of a compliant engine

The penalty and the compliant-engine cost are the compliance fact. The pricing strategy that follows is read with the truck price.

- `truck.product.fact_compliance_economics`: `penalty_amount`, `compliant_engine_cost`, `strategy_note`, `powertrain_id`
- `truck.product.dim_powertrain`: `powertrain_code`
- `truck.commercial.fact_truck_price`: `realized_price_rate`, `communicated_price_increase`, `powertrain_id`

### Q2 2026 (8) — Whether emissions credits give a peer a share or price advantage

Share and price advantage flags are the credit fact. Truck Inc share and price are the commercial facts.

- `truck.market.fact_emissions_credit`: `share_advantage_flag`, `price_advantage_flag`, `industry_peer_id`, `powertrain_id`
- `truck.market.dim_industry_peer`: `peer_name`
- `truck.commercial.fact_share_choice`: `market_share_rate`
- `truck.commercial.fact_truck_price`: `realized_price_rate`

### Q2 2026 (9) — Supplier cadence from the fourth quarter into the first, and parts growth

The support window and the parts-growth flag are the cadence. Parts revenue and outlook are the parts result.

- `truck.product.fact_supplier_cadence`: `support_window`, `parts_growth_support_flag`, `supplier_id`, `business_line_id`
- `truck.product.dim_supplier`: `supplier_name`
- `truck.commercial.fact_parts_result`: `parts_revenue_amount`, `outlook_direction`, `business_line_id`
- `truck.market.dim_business_line`: `line_code`

### Q1 2026 (4) — European orders and electric trucks in China

European order amount and the conflict flag are one fact. The electric-unit change in China is another, on the electric powertrain.

- `truck.market.fact_europe_order`: `order_amount`, `conflict_effect_flag`, `region_id`, `end_market_id`
- `truck.market.fact_china_electric`: `electric_unit_change`, `powertrain_id`, `region_id`
- `truck.organization.dim_region`: `region_code`
- `truck.product.dim_powertrain`: `powertrain_code`

### Q1 2026 (7) — Whether memory chips or aluminum constrain the second-half build

The constraint flag and the ramp risk name the input. North American mix and production units show how mix is tracking against that ramp.

- `truck.product.fact_supply_constraint`: `constraint_flag`, `ramp_risk_note`, `input_commodity_id`, `supplier_id`
- `truck.product.dim_input_commodity`: `commodity_code`
- `truck.product.fact_regional_build`: `north_america_mix_rate`, `production_units`, `region_id`

### Q4 2025 (6) — How much of the U.S. and Canada production shortfall was the shift to local-for-local

Shortfall units and the plan before the shift are the local-production fact. The region code selects the United States and Canada.

- `truck.product.fact_local_production`: `production_shortfall_units`, `plan_before_shift_units`, `local_for_local_share`, `region_id`
- `truck.organization.dim_region`: `region_code`

### Q4 2025 (14) — Where the supply chain would fail to ramp if demand improves

The constraint flag and the ramp-risk note name the failure point. The flex choice shows the production the chain would have to support.

- `truck.product.fact_supply_constraint`: `constraint_flag`, `ramp_risk_note`, `supplier_id`, `input_commodity_id`
- `truck.product.dim_supplier`: `supplier_name`
- `truck.product.dim_input_commodity`: `commodity_code`
- `truck.commercial.fact_build_slot`: `flex_choice`, `prebuy_units`

### Q3 2025 (1) — Whether the tariff regime improves PACCAR's position given where competitors build, and when the rebate hits

Peer build location and the cost position are the peer fact. Rebate amount and timing are the rebate fact.

- `truck.market.fact_peer_position`: `build_location_note`, `cost_position_code`, `industry_peer_id`, `region_id`
- `truck.market.dim_industry_peer`: `peer_name`, `region_id`
- `truck.commercial.fact_tariff_rebate`: `rebate_amount`, `rebate_timing_note`
- `truck.commercial.fact_tariff_bridge`: `cost_position_code`

### Q3 2025 (4) — What deadline the emissions agency faces, given supplier planning

The agency deadline and the unchanged-rule flag are the emissions program. The supplier support window is the lead time the deadline has to respect.

- `truck.product.fact_emissions_program`: `agency_deadline_note`, `rule_unchanged_flag`, `phased_rollout_flag`
- `truck.product.fact_supplier_cadence`: `support_window`, `supplier_id`
- `truck.product.dim_supplier`: `supplier_name`

### Q3 2025 (10) — Incremental share since the tariff announcement, and the Denton and Chillicothe plans

The incremental-share flag is the share choice. Plant code selects Denton and Chillicothe, and the plan note says what changes.

- `truck.commercial.fact_share_choice`: `incremental_share_flag`, `market_share_rate`
- `truck.product.fact_plant_response`: `share_comment_flag`, `plan_change_note`, `plant_id`
- `truck.product.dim_plant`: `plant_code`, `plant_name`
- `truck.retail.fact_buy_reason`: `customer_comment`

### Q3 2025 (11) — Whether parts sourcing moves more production to the United States

The U.S. shift flag and the multi-year offset flag are the sourcing plan. The parts business line and the run-rate rebate are the tariff context.

- `truck.product.fact_sourcing_plan`: `us_shift_flag`, `multi_year_offset_flag`, `business_line_id`, `region_id`
- `truck.market.dim_business_line`: `line_code`
- `truck.commercial.fact_tariff_rebate`: `run_rate_rebate_amount`

### Q3 2025 (17) — Whether a prebuy starts in the first half or the second half if the rule is unchanged

The prebuy half and the unchanged-rule flag are the emissions program. Customer comments are the buy reason.

- `truck.product.fact_emissions_program`: `prebuy_half`, `rule_unchanged_flag`
- `truck.retail.fact_buy_reason`: `customer_comment`, `demand_reason_id`
- `truck.retail.dim_demand_reason`: `reason_code`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `truck.market.dim_end_market` | supporting population |
| `truck.product.dim_truck_family` | supporting population |
| `truck.product.dim_powertrain` | Q2 2026 (6), Q1 2026 (4) |
| `truck.product.dim_plant` | Q3 2025 (10) |
| `truck.product.dim_supplier` | Q2 2026 (9), Q4 2025 (14), Q3 2025 (4) |
| `truck.product.dim_input_commodity` | Q1 2026 (7), Q4 2025 (14) |
| `truck.market.dim_industry_peer` | Q2 2026 (8), Q3 2025 (1) |
| `truck.market.dim_business_line` | Q2 2026 (9), Q3 2025 (11) |
| `truck.product.fact_local_production` | Q4 2025 (6) |
| `truck.product.fact_regional_build` | Q1 2026 (7) |
| `truck.market.fact_europe_order` | Q1 2026 (4) |
| `truck.market.fact_china_electric` | Q1 2026 (4) |
| `truck.product.fact_emissions_program` | Q3 2025 (4), Q3 2025 (17) |
| `truck.market.fact_emissions_credit` | Q2 2026 (8) |
| `truck.product.fact_compliance_economics` | Q2 2026 (6) |
| `truck.product.fact_supplier_cadence` | Q2 2026 (9), Q3 2025 (4) |
| `truck.product.fact_supply_constraint` | Q1 2026 (7), Q4 2025 (14) |
| `truck.product.fact_plant_response` | Q3 2025 (10) |
| `truck.product.fact_sourcing_plan` | Q3 2025 (11) |
| `truck.market.fact_peer_position` | Q3 2025 (1) |
