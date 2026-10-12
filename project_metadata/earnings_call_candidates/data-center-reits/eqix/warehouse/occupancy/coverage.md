# Equinix occupancy and bookings coverage

This slice is bookings, pre-leases, occupancy snapshots, churn, renewals, price, and revenue. A booking is not an occupancy snapshot, and a lease is not either one. Development capacity and interconnection are owned in the other slices. Calendar year, quarter, and day are complete here because bookings and revenue are stated on them. Metro, region, customer, and customer vertical are referenced and not re-authored.

Foreign identities are referenced from this slice and are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column | Node |
| --- | --- | --- |
| `campus_identity` | `campus_id` | `sf:equinix.power.dim_campus` |
| `customer_identity` | `customer_id` | `sf:equinix.interconnection.dim_customer` |
| `customer_vertical_identity` | `customer_vertical_id` | `sf:equinix.interconnection.dim_customer_vertical` |
| `development_project_identity` | `development_project_id` | `sf:equinix.power.dim_development_project` |
| `ibx_identity` | `ibx_id` | `sf:equinix.power.dim_ibx` |
| `metro_identity` | `metro_id` | `sf:equinix.interconnection.dim_metro` |
| `region_identity` | `region_id` | `sf:equinix.interconnection.dim_region` |

## Complete populations

| Identity | Dataset | Column |
| --- | --- | --- |
| `fiscal_year_identity` | `equinix.calendar.dim_fiscal_year` | `fiscal_year_id` |
| `fiscal_quarter_identity` | `equinix.calendar.dim_fiscal_quarter` | `fiscal_quarter_id` |
| `calendar_day_identity` | `equinix.calendar.dim_calendar_day` | `calendar_day_id` |
| `product_line_identity` | `equinix.occupancy.dim_product_line` | `product_line_id` |
| `workload_type_identity` | `equinix.occupancy.dim_workload_type` | `workload_type_id` |
| `deal_band_identity` | `equinix.occupancy.dim_deal_band` | `deal_band_id` |
| `churn_driver_identity` | `equinix.occupancy.dim_churn_driver` | `churn_driver_id` |
| `cost_pressure_identity` | `equinix.occupancy.dim_cost_pressure` | `cost_pressure_id` |
| `lease_identity` | `equinix.occupancy.dim_lease` | `lease_id` |
| `cabinet_identity` | `equinix.occupancy.dim_cabinet` | `cabinet_id` |
| `booking_identity` | `equinix.occupancy.fact_booking` | `booking_id` |
| `pipeline_identity` | `equinix.occupancy.fact_pipeline` | `pipeline_id` |
| `prelease_identity` | `equinix.occupancy.fact_prelease` | `prelease_id` |
| `prelease_delivery_identity` | `equinix.occupancy.fact_prelease_delivery` | `prelease_delivery_id` |
| `churn_quarter_identity` | `equinix.occupancy.fact_churn_quarter` | `churn_quarter_id` |
| `renewal_identity` | `equinix.occupancy.fact_renewal` | `renewal_id` |
| `revenue_quarter_identity` | `equinix.occupancy.fact_revenue_quarter` | `revenue_quarter_id` |
| `revenue_guide_identity` | `equinix.occupancy.fact_revenue_guide` | `revenue_guide_id` |
| `price_realization_identity` | `equinix.occupancy.fact_price_realization` | `price_realization_id` |
| `operating_cost_identity` | `equinix.occupancy.fact_operating_cost` | `operating_cost_id` |
| `demand_timing_identity` | `equinix.occupancy.fact_demand_timing` | `demand_timing_id` |
| `xscale_fee_identity` | `equinix.occupancy.fact_xscale_fee` | `xscale_fee_id` |
| `retail_demand_identity` | `equinix.occupancy.fact_retail_demand` | `retail_demand_id` |
| `placement_choice_identity` | `equinix.occupancy.fact_placement_choice` | `placement_choice_id` |
| `occupancy_quarter_identity` | `equinix.occupancy.fact_occupancy_quarter` | `occupancy_quarter_id` |
| `booking_runrate_identity` | `equinix.occupancy.fact_booking_runrate` | `booking_runrate_id` |
| `cabinet_delivery_identity` | `equinix.occupancy.fact_cabinet_delivery` | `cabinet_delivery_id` |

## Numbered questions

### Q2 2026 (2) — AI deal size, market mix, and interconnection attach

Deal size and market are `equinix.occupancy.fact_booking.deal_size_kw`, `metro_id`, and `ai_booking_flag`, with `workload_type_id` joined to `equinix.occupancy.dim_workload_type.workload_code`. Attach is `equinix.interconnection.fact_attach_rate.attach_rate` against `historical_attach_rate` for the same `metro_id` and `workload_type_id`.

### Q2 2026 (4) — Nonrecurring share under the long-term guide

`equinix.occupancy.fact_revenue_guide.nonrecurring_share` is the guide share. The level is `equinix.occupancy.fact_revenue_quarter.nonrecurring_revenue_amount` against `total_revenue_amount`, with `recurring_revenue_amount` kept apart. `fiscal_year_id` places the guide.

### Q2 2026 (5) — Regional growth versus the portfolio

`equinix.occupancy.fact_revenue_quarter.revenue_growth_rate` and `constant_currency_growth_rate` by `region_id` compare with `portfolio_growth_rate`. `equinix.interconnection.dim_region.region_code` separates Americas, EMEA, and Asia-Pacific. `equinix.occupancy.fact_revenue_guide.year_similarity_flag` says whether the path inside the range is similar each year.

### Q2 2026 (6) — Renewal spreads in the multi-year upside

`equinix.occupancy.fact_renewal.renewal_spread_rate`, `revenue_bridge_amount`, and `multiyear_upside_amount` are the renewal contribution. `equinix.occupancy.fact_revenue_guide.renewal_contribution_amount` places that contribution in the guide. `fiscal_year_id` is the year of the bridge.

### Q2 2026 (11) — Pipeline mix of open-weight, private AI, and enterprise inference

`equinix.occupancy.fact_pipeline.pipeline_kw` with `open_weight_flag`, `private_ai_flag`, and `enterprise_inference_flag`. `workload_type_id` joins `equinix.occupancy.dim_workload_type.workload_code`. `metro_id` and `customer_vertical_id` place the slice.

### Q1 2026 (2) — Earlier and longer pre-lease terms, price, and deposits

`equinix.occupancy.fact_prelease.preleased_kw`, `commitment_lead_months`, `earlier_commitment_flag`, `term_months`, `price_per_kw_amount`, and `deposit_amount`. The delivery quarter is `equinix.occupancy.fact_prelease_delivery.fiscal_quarter_id` joined on `prelease_id`. `campus_id` and `customer_id` name where and who.

### Q1 2026 (3) — Memory, fuel, and IT cost pressure on booking timing

`equinix.occupancy.fact_demand_timing.timing_effect` and `affected_booking_amount`. `cost_pressure_id` joins `equinix.occupancy.dim_cost_pressure.pressure_code` for memory, fuel, and IT. `customer_vertical_id` and `metro_id` say who moved and where.

### Q1 2026 (5) — Seasonal bookings dip and enterprise versus large-deal mix

`equinix.occupancy.fact_booking.seasonal_flag`, `annualized_booking_amount`, and `deal_band_id` joined to `equinix.occupancy.dim_deal_band.band_code`. `customer_vertical_id` joins `equinix.interconnection.dim_customer_vertical.vertical_code` for enterprise. `equinix.calendar.dim_fiscal_quarter.season_code` is the quarter.

### Q1 2026 (8) — Low churn versus the full-year range

`equinix.occupancy.fact_churn_quarter.churn_rate`, `full_year_low_rate`, `full_year_high_rate`, and `delayed_demand_flag`. `fiscal_quarter_id` is the quarter. `region_id` keeps the result regional.

### Q1 2026 (9) — xScale one-time fees and Manukau pre-leasing

`equinix.occupancy.fact_xscale_fee.onetime_fee_amount` and `fee_framework_code` size the fee, with `lease_id` and `campus_id`. Pre-leasing status at a campus such as Manukau is `equinix.occupancy.fact_prelease.preleased_kw` on that `campus_id`, with delivery on `equinix.occupancy.fact_prelease_delivery.fiscal_quarter_id`. The campus population is `equinix.power.dim_campus.campus_name`.

### Q1 2026 (10) — Edge and colocation versus on-premises or public cloud

`equinix.occupancy.fact_placement_choice.location_choice` and `investment_shift_flag`. `workload_type_id` joins `equinix.occupancy.dim_workload_type.workload_code` for agentic workloads. `metro_id` is the market. `customer_id` is the customer.

### Q4 2025 (1) — AI bookings from enterprises versus hyperscaler edge nodes

`equinix.occupancy.fact_booking.ai_booking_flag` and `annualized_booking_amount`. `customer_vertical_id` joins `equinix.interconnection.dim_customer_vertical.vertical_code` for enterprise and hyperscaler. `workload_type_id` joins `workload_code` for hyperscaler_edge. `metro_id` is the location.

### Q4 2025 (2) — AI deal size and location versus traditional bookings

`equinix.occupancy.fact_booking.deal_size_kw`, `metro_id`, `ai_booking_flag`, and `prior_run_rate_amount`. `workload_type_id` separates AI workloads from `workload_code` traditional. `fiscal_quarter_id` shows whether demand has accelerated since the prior run rate.

### Q4 2025 (3) — Controllable churn versus customer workload optimization

`equinix.occupancy.fact_churn_quarter.controllable_share` and `customer_optimization_share`. `churn_driver_id` joins `equinix.occupancy.dim_churn_driver.driver_code`. `churn_rate` is the level. `customer_vertical_id` names the vertical.

### Q4 2025 (5) — How far pricing can move and what varies growth inside the range

`equinix.occupancy.fact_price_realization.price_change_rate` and `growth_variance_driver`. `presale_price_differential` is the pre-sale gap. The growth level is `equinix.occupancy.fact_revenue_quarter.revenue_growth_rate` by `region_id`.

### Q4 2025 (6) — Cost reductions versus staffing at the current booking pace

`equinix.occupancy.fact_operating_cost.cost_reduction_amount`, `operating_cost_amount`, `staffing_count`, `staffing_need_flag`, and `booking_pace_amount`. `fiscal_quarter_id` is the trend. `region_id` places the cost.

### Q4 2025 (7) — Bookings from new cabinets in constrained metros versus broader demand

`equinix.occupancy.fact_booking.new_cabinet_flag`, `constrained_market_flag`, `cabinet_count`, and `annualized_booking_amount`. `metro_id` joins `equinix.interconnection.dim_metro.metro_name` for Northern Virginia and Frankfurt. New supply is `equinix.occupancy.fact_cabinet_delivery.delivered_cabinet_count` for the same metro and quarter.

### Q3 2025 (3) — Price firmness where capacity is constrained, including pre-sales

`equinix.occupancy.fact_price_realization.price_change_rate`, `capacity_constrained_flag`, and `presale_price_differential`. `metro_id` joins `equinix.interconnection.dim_metro.constrained_flag`. Available power beside that price is `equinix.power.fact_market_power.power_available_mw` for the same metro.

### Q3 2025 (6) — Larger-footprint retail demand and pre-leasing

`equinix.occupancy.fact_retail_demand.retail_demand_kw`, `preleased_kw`, and `remaining_capacity_kw`. `product_line_id` joins `equinix.occupancy.dim_product_line.product_line_code` for larger_footprint_retail. `metro_id` and `campus_id` place the demand.

### Q3 2025 (7) — Constant-currency regional growth versus profit

`equinix.occupancy.fact_revenue_quarter.constant_currency_growth_rate` and `profit_amount` by `region_id`. `revenue_growth_rate` is the reported rate. `equinix.interconnection.dim_region.region_code` names the region.

### Q3 2025 (9) — Pre-sold bookings as a one-off or a new run rate

`equinix.occupancy.fact_booking_runrate.annualized_presold_amount`, `normal_run_rate_amount`, `one_off_flag`, and `presold_price_differential`. `fiscal_quarter_id` is the quarter. `region_id` places the run rate.

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `equinix.calendar.dim_fiscal_year` | supporting population |
| `equinix.calendar.dim_fiscal_quarter` | Q1 2026 (5) |
| `equinix.calendar.dim_calendar_day` | supporting population |
| `equinix.occupancy.dim_product_line` | Q3 2025 (6) |
| `equinix.occupancy.dim_workload_type` | Q2 2026 (2), Q2 2026 (11), Q1 2026 (10) |
| `equinix.occupancy.dim_deal_band` | Q1 2026 (5) |
| `equinix.occupancy.dim_churn_driver` | Q4 2025 (3) |
| `equinix.occupancy.dim_cost_pressure` | Q1 2026 (3) |
| `equinix.occupancy.dim_lease` | supporting population |
| `equinix.occupancy.dim_cabinet` | supporting population |
| `equinix.occupancy.fact_booking` | Q2 2026 (2), Q1 2026 (5), Q4 2025 (1), Q4 2025 (2), Q4 2025 (7) |
| `equinix.occupancy.fact_pipeline` | Q2 2026 (11) |
| `equinix.occupancy.fact_prelease` | Q1 2026 (2), Q1 2026 (9) |
| `equinix.occupancy.fact_prelease_delivery` | Q1 2026 (2), Q1 2026 (9) |
| `equinix.occupancy.fact_churn_quarter` | Q1 2026 (8), Q4 2025 (3) |
| `equinix.occupancy.fact_renewal` | Q2 2026 (6) |
| `equinix.occupancy.fact_revenue_quarter` | Q2 2026 (4), Q2 2026 (5), Q4 2025 (5), Q3 2025 (7) |
| `equinix.occupancy.fact_revenue_guide` | Q2 2026 (4), Q2 2026 (5), Q2 2026 (6) |
| `equinix.occupancy.fact_price_realization` | Q4 2025 (5), Q3 2025 (3) |
| `equinix.occupancy.fact_operating_cost` | Q4 2025 (6) |
| `equinix.occupancy.fact_demand_timing` | Q1 2026 (3) |
| `equinix.occupancy.fact_xscale_fee` | Q1 2026 (9) |
| `equinix.occupancy.fact_retail_demand` | Q3 2025 (6) |
| `equinix.occupancy.fact_placement_choice` | Q1 2026 (10) |
| `equinix.occupancy.fact_occupancy_quarter` | supporting population |
| `equinix.occupancy.fact_booking_runrate` | Q3 2025 (9) |
| `equinix.occupancy.fact_cabinet_delivery` | Q4 2025 (7) |
