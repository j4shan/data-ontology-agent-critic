# PACCAR price, volume, and backlog

This slice owns the calendar, truck price, gross margin, profit per truck, tariffs, orders, backlog, and build slots. Price facts do not store unit volume. Delivery and order units do not store price. Backlog is unfilled orders, not dealer stock. Dealer inventory, regions, plants, and end markets are owned outside this slice.

Foreign identities are referenced from this slice and are partial here. Their complete populations are the datasets below, which this slice does not author:

| Identity | Column | Node |
| --- | --- | --- |
| `business_line_identity` | `business_line_id` | `sf:paccar.market.dim_business_line` |
| `demand_reason_identity` | `demand_reason_id` | `sf:paccar.retail.dim_demand_reason` |
| `end_market_identity` | `end_market_id` | `sf:paccar.market.dim_end_market` |
| `fleet_class_identity` | `fleet_class_id` | `sf:paccar.retail.dim_fleet_class` |
| `input_commodity_identity` | `input_commodity_id` | `sf:paccar.product.dim_input_commodity` |
| `plant_identity` | `plant_id` | `sf:paccar.product.dim_plant` |
| `powertrain_identity` | `powertrain_id` | `sf:paccar.product.dim_powertrain` |
| `region_identity` | `region_id` | `sf:paccar.organization.dim_region` |

## Numbered questions

### Q2 2026 (1) — What moved gross margin above the expectation

Mix and cost are separate pieces of gross margin, and both are compared with the prior expectation.

- `paccar.commercial.fact_gross_margin`: `gross_margin_rate`, `mix_effect_amount`, `cost_effect_amount`, `versus_expectation`, `cost_element_id`
- `paccar.commercial.dim_cost_element`: `element_code`

### Q2 2026 (2) — Market pricing and room from a higher local-for-local mix

Market price direction is on the price fact, which stores no units. Local content and the room it leaves for price are on the local-production fact.

- `paccar.commercial.fact_truck_price`: `market_price_direction`, `realized_price_rate`, `region_id`
- `paccar.product.fact_local_production`: `local_for_local_share`, `price_room_flag`, `region_id`
- `paccar.market.dim_industry_peer`: `peer_name`, `region_id`

### Q2 2026 (3) — Whether an emissions refund, rather than cost, drove profit per truck

Profit per truck, the refund inside it, and the underlying cost run rate are separate amounts. The refund fact says whether the refund drove the result.

- `paccar.commercial.fact_profit_per_truck`: `profit_per_truck_amount`, `refund_amount`, `underlying_cost_amount`, `cost_execution_amount`
- `paccar.commercial.fact_emissions_refund`: `refund_amount`, `drove_profit_flag`

### Q2 2026 (4) — Price step-up under the phased emissions rollout

The sequential step-up is the price fact. The phased-rollout flag is the emissions program. Quarter labels separate the fourth quarter from the third.

- `paccar.commercial.fact_truck_price`: `sequential_step_up_rate`, `realized_price_rate`, `powertrain_id`, `accounting_period_id`
- `paccar.product.fact_emissions_program`: `phased_rollout_flag`, `powertrain_id`
- `paccar.product.dim_powertrain`: `powertrain_code`
- `paccar.calendar.dim_accounting_period`: `quarter_label`

### Q2 2026 (5) — Third-quarter gross margin guided flat despite deliveries, North American mix, and a Europe shutdown

The guide direction, the delivery assumption, the North American mix, and the Europe-shutdown flag sit on the margin row. Actual deliveries and the regional build are the volume facts.

- `paccar.commercial.fact_gross_margin`: `guided_direction`, `gross_margin_rate`, `delivery_units`, `north_america_mix_rate`, `europe_shutdown_flag`
- `paccar.product.fact_regional_build`: `production_units`, `europe_shutdown_flag`, `north_america_mix_rate`, `region_id`
- `paccar.retail.fact_regional_delivery`: `delivery_units`, `region_id`
- `paccar.organization.dim_region`: `region_code`

### Q2 2026 (10) — Parts margins as over-the-road demand moves from large fleets to smaller fleets

Parts gross margin is cut by fleet class. Over-the-road is the end market.

- `paccar.commercial.fact_parts_result`: `parts_gross_margin_rate`, `fleet_class_id`, `parts_revenue_amount`
- `paccar.retail.dim_fleet_class`: `class_code`, `class_name`
- `paccar.market.dim_end_market`: `market_code`

### Q2 2026 (13) — Freight rates from fewer drivers, and what that means for orders and fleet growth

The rate cause separates fewer drivers from more freight. Orders and the fleet-growth reason say how high builds can go.

- `paccar.commercial.fact_freight_environment`: `freight_rate_direction`, `driver_supply_direction`, `freight_volume_direction`, `rate_cause`
- `paccar.commercial.fact_order_intake`: `order_units`, `demand_reason_id`
- `paccar.retail.fact_buy_reason`: `order_share`, `demand_reason_id`
- `paccar.retail.dim_demand_reason`: `reason_code`
- `paccar.retail.fact_fleet_capacity`: `trucks_in_service`, `excess_capacity_units`

### Q2 2026 (14) — Whether a 2026 prebuy can be pushed into 2027

From-year and to-year on the deferral are the slot move. Backlog units are the unfilled book the slots sit in.

- `paccar.commercial.fact_slot_deferral`: `from_delivery_year`, `to_delivery_year`, `deferred_units`, `customer_pushout_flag`, `demand_reason_id`
- `paccar.retail.dim_demand_reason`: `reason_code`
- `paccar.commercial.fact_backlog`: `backlog_units`, `coverage_rate`

### Q1 2026 (1) — Parts started slowly, and whether the back half improves with orders

The slow-start flag, the outlook direction, and the acceleration flag are the parts result. Truck orders are the order fact.

- `paccar.commercial.fact_parts_result`: `parts_revenue_amount`, `slow_start_flag`, `outlook_direction`, `acceleration_flag`, `accounting_period_id`
- `paccar.commercial.fact_order_intake`: `order_units`, `accounting_period_id`
- `paccar.calendar.dim_accounting_period`: `half_code`, `quarter_label`

### Q1 2026 (2) — How much of the jump in profit per truck was cost versus mix

Cost execution, mix, and the parts contribution are separate amounts on the profit-per-truck fact.

- `paccar.commercial.fact_profit_per_truck`: `profit_per_truck_amount`, `cost_execution_amount`, `mix_effect_amount`, `parts_contribution_amount`

### Q1 2026 (3) — Simplified metal tariffs on parts versus trucks

Tariff cost and the prior outlook are by business line and input, so parts and trucks, and steel and aluminum, stay apart.

- `paccar.commercial.fact_tariff_bridge`: `tariff_cost_amount`, `prior_outlook_amount`, `business_line_id`, `input_commodity_id`
- `paccar.market.dim_business_line`: `line_code`
- `paccar.product.dim_input_commodity`: `commodity_code`

### Q1 2026 (5) — Whether the sequential gross-profit jump was a reversal of older tariffs

Revenue change and gross-profit change are separate, so a small revenue move can be compared with a large profit move. The reversal flag marks older tariffs.

- `paccar.commercial.fact_gross_margin`: `revenue_change_amount`, `gross_profit_change_amount`, `tariff_reversal_flag`, `gross_margin_rate`

### Q1 2026 (6) — Shifts and build slots for a prebuy versus the current rate and last year

Shift count, prebuy units, slots versus last year, and open versus filled slots are the build-slot fact.

- `paccar.commercial.fact_build_slot`: `shift_count`, `prebuy_units`, `versus_last_year_units`, `filled_slots`, `open_slots`, `accounting_period_id`

### Q1 2026 (8) — Price versus cost from the second quarter through the second half

Price effect and cost effect are separate. The half code places the comparison. Realized price stores no units.

- `paccar.commercial.fact_price_cost`: `price_effect_amount`, `cost_effect_amount`, `gap_amount`, `half_code`
- `paccar.commercial.fact_truck_price`: `realized_price_rate`, `sequential_step_up_rate`

### Q1 2026 (9) — Incremental margin this cycle versus the last

The rate is stored once per cycle. Tariffs, the share opportunity, and whether there is a new-product wave are separate columns.

- `paccar.commercial.fact_incremental_margin`: `incremental_margin_rate`, `comparison_cycle`, `tariff_effect_amount`, `share_opportunity_flag`, `new_product_wave_flag`

### Q1 2026 (10) — What drives the second-half parts acceleration, and whether it needs higher freight rates

The acceleration flag and the freight-required flag are the parts result. Freight rate direction and excess fleet capacity are the surrounding demand.

- `paccar.commercial.fact_parts_result`: `acceleration_flag`, `outlook_direction`, `freight_required_flag`, `parts_revenue_amount`
- `paccar.commercial.fact_freight_environment`: `freight_rate_direction`, `freight_volume_direction`
- `paccar.retail.fact_fleet_capacity`: `excess_capacity_units`, `freight_demand_index`

### Q1 2026 (12) — Customers pushing delivery dates out, and when the production credit applies

The pushout flag and deferred units are the slot deferral. The credit amount and the label of when it applies are the production credit. Tariff cost is the cost the credit sits beside.

- `paccar.commercial.fact_slot_deferral`: `customer_pushout_flag`, `deferred_units`, `from_delivery_year`, `to_delivery_year`
- `paccar.commercial.fact_production_credit`: `credit_amount`, `applies_from_label`
- `paccar.commercial.fact_tariff_bridge`: `tariff_cost_amount`

### Q1 2026 (14) — Backlog shifting from small fleets toward large fleets, and lease and rental

Mix share and shift direction are by fleet class. Truck gross margin is the margin fact. Lease and rental demand is financial services.

- `paccar.commercial.fact_backlog_mix`: `mix_share`, `shift_direction`, `fleet_class_id`
- `paccar.retail.dim_fleet_class`: `class_code`
- `paccar.commercial.fact_gross_margin`: `gross_margin_rate`
- `paccar.commercial.fact_lease_rental`: `lease_demand_amount`, `rental_demand_amount`, `fleet_class_id`, `business_line_id`

### Q4 2025 (1) — What improves margin from the fourth quarter to the first despite flat deliveries

Starting and next-quarter margin rates are the sequence. Delivery direction on that row, and delivery units by region, show the flat volume.

- `paccar.commercial.fact_margin_sequence`: `margin_rate`, `next_quarter_margin_rate`, `delivery_direction`, `accounting_period_id`
- `paccar.retail.fact_regional_delivery`: `delivery_units`, `delivery_direction`
- `paccar.calendar.dim_accounting_period`: `quarter_label`

### Q4 2025 (2) — When recent orders turn into production

The production quarter label is when the orders build. Order units are the book. Filled slots are the schedule those orders land in.

- `paccar.commercial.fact_production_timing`: `production_quarter_label`, `order_to_build_note`, `accounting_period_id`
- `paccar.commercial.fact_order_intake`: `order_units`, `order_amount`
- `paccar.commercial.fact_build_slot`: `filled_slots`, `open_slots`

### Q4 2025 (3) — Fourth-quarter price-cost gap versus the first-quarter tariff benefit

The price effect, the cost effect, and the gap are one fact. The quarterly tariff benefit is the tariff bridge.

- `paccar.commercial.fact_price_cost`: `gap_amount`, `price_effect_amount`, `cost_effect_amount`, `accounting_period_id`
- `paccar.commercial.fact_tariff_bridge`: `quarter_benefit_amount`, `tariff_cost_amount`, `accounting_period_id`
- `paccar.calendar.dim_accounting_period`: `quarter_label`

### Q4 2025 (4) — Market share versus profit per truck as tariffs hit competitors

The two priority flags say which one PACCAR chooses. Profit per truck is its own amount. The cost position is the tariff bridge.

- `paccar.commercial.fact_share_choice`: `profit_per_truck_priority_flag`, `share_priority_flag`, `market_share_rate`
- `paccar.commercial.fact_profit_per_truck`: `profit_per_truck_amount`
- `paccar.commercial.fact_tariff_bridge`: `cost_position_code`, `tariff_cost_amount`

### Q4 2025 (5) — Whether truck margins should differ from the historical cycle average

Current margin and the historical average are the cycle-margin fact. North American production units are the regional build.

- `paccar.commercial.fact_cycle_margin`: `margin_rate`, `historical_cycle_average_rate`, `differs_from_average_flag`, `region_id`
- `paccar.product.fact_regional_build`: `production_units`, `region_id`
- `paccar.organization.dim_region`: `region_code`

### Q4 2025 (8) — How full first- and second-quarter build slots are after January orders

Open and filled slots are by period. The January-strength flag marks the order intake those slots are absorbing.

- `paccar.commercial.fact_build_slot`: `open_slots`, `filled_slots`, `accounting_period_id`
- `paccar.commercial.fact_order_intake`: `january_strength_flag`, `order_units`
- `paccar.calendar.dim_accounting_period`: `quarter_label`

### Q4 2025 (10) — If higher truck rates reflect fewer drivers, what that means for orders

The rate cause is fewer drivers or more freight. Order units are the order response.

- `paccar.commercial.fact_freight_environment`: `rate_cause`, `freight_rate_direction`, `driver_supply_direction`, `freight_volume_direction`
- `paccar.commercial.fact_order_intake`: `order_units`

### Q4 2025 (12) — How parts gross margin scales in 2026

The parts gross margin rate and the outlook direction are the parts result. The fiscal year places 2026.

- `paccar.commercial.fact_parts_result`: `parts_gross_margin_rate`, `outlook_direction`, `parts_revenue_amount`, `accounting_period_id`
- `paccar.calendar.dim_accounting_period`: `fiscal_year`

### Q4 2025 (15) — What price increase for the 2027 emissions engines has been communicated

The communicated increase is the price fact for the low-NOx powertrain. Compliant-engine cost is the cost being priced.

- `paccar.commercial.fact_truck_price`: `communicated_price_increase`, `powertrain_id`, `realized_price_rate`
- `paccar.product.dim_powertrain`: `powertrain_code`
- `paccar.product.fact_compliance_economics`: `compliant_engine_cost`, `powertrain_id`

### Q4 2025 (16) — Whether production would be flexed up for a prebuy or kept limited

The flex choice and prebuy units are the build slots. The prebuy half is the emissions program. The regional outlook is the volume being protected.

- `paccar.commercial.fact_build_slot`: `flex_choice`, `prebuy_units`, `versus_last_year_units`
- `paccar.product.fact_emissions_program`: `prebuy_half`, `rule_unchanged_flag`
- `paccar.retail.fact_region_outlook`: `retail_units`, `outlook_direction`

### Q4 2025 (18) — Whether last year's tariff surcharges are being rolled back

The surcharge amount and the rollback flag are the surcharge fact. Remaining tariff cost and realized price show what is left in the truck price.

- `paccar.commercial.fact_tariff_surcharge`: `surcharge_amount`, `rollback_flag`, `still_in_price_flag`
- `paccar.commercial.fact_tariff_bridge`: `tariff_cost_amount`
- `paccar.commercial.fact_truck_price`: `realized_price_rate`

### Q4 2025 (19) — How much of the improved confidence is freight versus emissions-rule clarity

The two contributions split the confidence index. Order units are the orders that confidence is supporting. The rule-unchanged flag is the regulatory side.

- `paccar.commercial.fact_customer_confidence`: `confidence_index`, `freight_contribution`, `emissions_clarity_contribution`
- `paccar.commercial.fact_order_intake`: `order_units`
- `paccar.product.fact_emissions_program`: `rule_unchanged_flag`

### Q3 2025 (2) — Whether price increases start to offset tariff cost

Realized price and the step-up are the price fact. Tariff cost is the bridge. The price effect and cost effect show the offset.

- `paccar.commercial.fact_truck_price`: `realized_price_rate`, `sequential_step_up_rate`
- `paccar.commercial.fact_tariff_bridge`: `tariff_cost_amount`
- `paccar.commercial.fact_price_cost`: `price_effect_amount`, `cost_effect_amount`, `gap_amount`

### Q3 2025 (5) — How the full-run-rate rebate compares with tariff costs on parts, steel, and aluminum

Run-rate rebate and tariff cost are cut by input and business line. Commodity codes select steel, aluminum, and parts.

- `paccar.commercial.fact_tariff_rebate`: `rebate_amount`, `run_rate_rebate_amount`, `input_commodity_id`, `business_line_id`
- `paccar.commercial.fact_tariff_bridge`: `tariff_cost_amount`, `input_commodity_id`, `business_line_id`
- `paccar.product.dim_input_commodity`: `commodity_code`
- `paccar.market.dim_business_line`: `line_code`

### Q3 2025 (6) — A cost advantage for U.S. production, or only an even field

The cost-position code is on the tariff bridge and on the peer comparison. The region code selects U.S. production.

- `paccar.commercial.fact_tariff_bridge`: `cost_position_code`, `region_id`
- `paccar.market.fact_peer_position`: `cost_position_code`, `region_id`
- `paccar.organization.dim_region`: `region_code`

### Q3 2025 (7) — How large a tariff headwind is in the fourth-quarter outlook as rebates ramp

The headwind is the tariff bridge. The rebate amount and the run rate show the ramp. Gross margin is the result the headwind hits.

- `paccar.commercial.fact_tariff_bridge`: `headwind_amount`, `accounting_period_id`
- `paccar.commercial.fact_tariff_rebate`: `rebate_amount`, `run_rate_rebate_amount`
- `paccar.commercial.fact_gross_margin`: `gross_margin_rate`
- `paccar.calendar.dim_accounting_period`: `quarter_label`

### Q3 2025 (9) — Truck pricing realized in the quarter and expected next quarter

Realized price and next-quarter price are separate rates on the price fact, which stores no units.

- `paccar.commercial.fact_truck_price`: `realized_price_rate`, `next_quarter_price_rate`, `accounting_period_id`
- `paccar.calendar.dim_accounting_period`: `quarter_label`

### Q3 2025 (12) — Whether pricing taken to cover tariffs will be given back to gain share

The given-back flag is the price fact. The share-priority flag is the share choice. The surcharge is the tariff piece that could be returned.

- `paccar.commercial.fact_truck_price`: `price_given_back_flag`, `realized_price_rate`
- `paccar.commercial.fact_share_choice`: `share_priority_flag`, `market_share_rate`
- `paccar.commercial.fact_tariff_surcharge`: `surcharge_amount`

### Q3 2025 (15) — Whether rebate savings are passed through by removing the tariff surcharge

The passthrough flag is the rebate. The surcharge amount and rollback flag are the surcharge. Realized price is what remains.

- `paccar.commercial.fact_tariff_rebate`: `passthrough_by_surcharge_removal_flag`, `rebate_amount`
- `paccar.commercial.fact_tariff_surcharge`: `surcharge_amount`, `rollback_flag`
- `paccar.commercial.fact_truck_price`: `realized_price_rate`

### Q3 2025 (16) — Whether fourth-quarter order coverage is similar by region

Coverage rate by region and the similar-across-regions flag are the coverage fact. Backlog units are the unfilled book behind that coverage.

- `paccar.commercial.fact_order_coverage`: `coverage_rate`, `similar_across_regions_flag`, `region_id`, `accounting_period_id`
- `paccar.commercial.fact_backlog`: `backlog_units`, `coverage_rate`, `region_id`
- `paccar.organization.dim_region`: `region_code`
- `paccar.calendar.dim_accounting_period`: `quarter_label`

### Q3 2025 (18) — Whether tariff surcharges fade while core price increases continue

Core price change and surcharge change are separate. The fading and continuing flags keep the two paths apart.

- `paccar.commercial.fact_price_component`: `core_price_change`, `surcharge_change`, `surcharge_fading_flag`, `core_continuing_flag`
- `paccar.commercial.fact_tariff_surcharge`: `surcharge_amount`, `still_in_price_flag`
- `paccar.commercial.fact_truck_price`: `realized_price_rate`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `paccar.calendar.dim_calendar_day` | supporting population |
| `paccar.calendar.dim_accounting_period` | Q2 2026 (4), Q1 2026 (1), Q4 2025 (1), Q4 2025 (3), Q4 2025 (8), Q4 2025 (12), Q3 2025 (7), Q3 2025 (9), Q3 2025 (16) |
| `paccar.commercial.dim_currency` | supporting population |
| `paccar.commercial.dim_cost_element` | Q2 2026 (1) |
| `paccar.commercial.fact_truck_price` | Q2 2026 (2), Q2 2026 (4), Q1 2026 (8), Q4 2025 (15), Q4 2025 (18), Q3 2025 (2), Q3 2025 (9), Q3 2025 (12), Q3 2025 (15), Q3 2025 (18) |
| `paccar.commercial.fact_price_component` | Q3 2025 (18) |
| `paccar.commercial.fact_gross_margin` | Q2 2026 (1), Q2 2026 (5), Q1 2026 (5), Q1 2026 (14), Q3 2025 (7) |
| `paccar.commercial.fact_profit_per_truck` | Q2 2026 (3), Q1 2026 (2), Q4 2025 (4) |
| `paccar.commercial.fact_emissions_refund` | Q2 2026 (3) |
| `paccar.commercial.fact_tariff_bridge` | Q1 2026 (3), Q1 2026 (12), Q4 2025 (3), Q4 2025 (4), Q4 2025 (18), Q3 2025 (2), Q3 2025 (5), Q3 2025 (6), Q3 2025 (7) |
| `paccar.commercial.fact_tariff_rebate` | Q3 2025 (5), Q3 2025 (7), Q3 2025 (15) |
| `paccar.commercial.fact_tariff_surcharge` | Q4 2025 (18), Q3 2025 (12), Q3 2025 (15), Q3 2025 (18) |
| `paccar.commercial.fact_order_intake` | Q2 2026 (13), Q1 2026 (1), Q4 2025 (2), Q4 2025 (8), Q4 2025 (10), Q4 2025 (19) |
| `paccar.commercial.fact_backlog` | Q2 2026 (14), Q3 2025 (16) |
| `paccar.commercial.fact_backlog_mix` | Q1 2026 (14) |
| `paccar.commercial.fact_slot_deferral` | Q2 2026 (14), Q1 2026 (12) |
| `paccar.commercial.fact_build_slot` | Q1 2026 (6), Q4 2025 (2), Q4 2025 (8), Q4 2025 (16) |
| `paccar.commercial.fact_production_timing` | Q4 2025 (2) |
| `paccar.commercial.fact_price_cost` | Q1 2026 (8), Q4 2025 (3), Q3 2025 (2) |
| `paccar.commercial.fact_incremental_margin` | Q1 2026 (9) |
| `paccar.commercial.fact_parts_result` | Q2 2026 (10), Q1 2026 (1), Q1 2026 (10), Q4 2025 (12) |
| `paccar.commercial.fact_share_choice` | Q4 2025 (4), Q3 2025 (12) |
| `paccar.commercial.fact_freight_environment` | Q2 2026 (13), Q1 2026 (10), Q4 2025 (10) |
| `paccar.commercial.fact_customer_confidence` | Q4 2025 (19) |
| `paccar.commercial.fact_production_credit` | Q1 2026 (12) |
| `paccar.commercial.fact_purchase_incentive` | supporting population |
| `paccar.commercial.fact_lease_rental` | Q1 2026 (14) |
| `paccar.commercial.fact_cycle_margin` | Q4 2025 (5) |
| `paccar.commercial.fact_margin_sequence` | Q4 2025 (1) |
| `paccar.commercial.fact_order_coverage` | Q3 2025 (16) |
