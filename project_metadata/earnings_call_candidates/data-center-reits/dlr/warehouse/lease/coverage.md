# Data Hall Inc lease commencement and occupancy coverage

This slice is the lease, the booking, the commencement, and the occupancy snapshot. Those are different facts. Renewals, expirations, cash NOI, and size-band demand sit here. Calendar year, quarter, and day are complete here. Land, power, metro, and customer vertical are referenced and not re-authored.

Foreign identities are referenced from this slice and are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column | Node |
| --- | --- | --- |
| `campus_identity` | `campus_id` | `sf:datahall.land.dim_campus` |
| `customer_identity` | `customer_id` | `sf:datahall.interconnection.dim_customer` |
| `customer_vertical_identity` | `customer_vertical_id` | `sf:datahall.interconnection.dim_customer_vertical` |
| `market_setting_identity` | `market_setting_id` | `sf:datahall.land.dim_market_setting` |
| `metro_identity` | `metro_id` | `sf:datahall.interconnection.dim_metro` |
| `region_identity` | `region_id` | `sf:datahall.interconnection.dim_region` |

## Complete populations

| Identity | Dataset | Column |
| --- | --- | --- |
| `fiscal_year_identity` | `datahall.calendar.dim_fiscal_year` | `fiscal_year_id` |
| `fiscal_quarter_identity` | `datahall.calendar.dim_fiscal_quarter` | `fiscal_quarter_id` |
| `calendar_day_identity` | `datahall.calendar.dim_calendar_day` | `calendar_day_id` |
| `megawatt_band_identity` | `datahall.lease.dim_megawatt_band` | `megawatt_band_id` |
| `expense_line_identity` | `datahall.lease.dim_expense_line` | `expense_line_id` |
| `currency_identity` | `datahall.lease.dim_currency` | `currency_id` |
| `lease_identity` | `datahall.lease.dim_lease` | `lease_id` |
| `booking_identity` | `datahall.lease.fact_booking` | `booking_id` |
| `commencement_identity` | `datahall.lease.fact_commencement` | `commencement_id` |
| `occupancy_identity` | `datahall.lease.fact_occupancy` | `occupancy_id` |
| `renewal_identity` | `datahall.lease.fact_renewal` | `renewal_id` |
| `expiration_identity` | `datahall.lease.fact_expiration` | `expiration_id` |
| `forward_renewal_identity` | `datahall.lease.fact_forward_renewal` | `forward_renewal_id` |
| `cash_noi_identity` | `datahall.lease.fact_cash_noi` | `cash_noi_id` |
| `market_demand_identity` | `datahall.lease.fact_market_demand` | `market_demand_id` |
| `enterprise_block_identity` | `datahall.lease.fact_enterprise_block` | `enterprise_block_id` |
| `inference_demand_identity` | `datahall.lease.fact_inference_demand` | `inference_demand_id` |
| `growth_bridge_identity` | `datahall.lease.fact_growth_bridge` | `growth_bridge_id` |
| `multiyear_growth_identity` | `datahall.lease.fact_multiyear_growth` | `multiyear_growth_id` |
| `commencement_capacity_identity` | `datahall.lease.fact_commencement_capacity` | `commencement_capacity_id` |
| `small_block_runrate_identity` | `datahall.lease.fact_small_block_runrate` | `small_block_runrate_id` |
| `booking_outlook_identity` | `datahall.lease.fact_booking_outlook` | `booking_outlook_id` |
| `competitor_position_identity` | `datahall.lease.fact_competitor_position` | `competitor_position_id` |
| `enterprise_ai_timing_identity` | `datahall.lease.fact_enterprise_ai_timing` | `enterprise_ai_timing_id` |

## Numbered questions

### Q1 2026 (2) — Commencement lag from a large lease, utility delay, or booking ahead

`datahall.lease.fact_commencement.lag_months`, `lease_mw`, `large_lease_flag`, `utility_delay_flag`, and `booked_ahead_flag`. `lease_id` joins `datahall.lease.dim_lease`. Utility months sit on `datahall.land.fact_project_constraint.delay_months` where `datahall.land.dim_constraint.constraint_code` is power.

### Q1 2026 (3) — 0 to 1 megawatt run rate and interconnection flow-through

`datahall.lease.fact_small_block_runrate.current_run_rate_mw`, `higher_run_rate_mw`, and `achievable_flag` with `megawatt_band_id` joined to `datahall.lease.dim_megawatt_band.band_code` mw_0_1. Interconnection is `datahall.interconnection.fact_interconnect_flow.flow_through_rate` and `interconnect_revenue_amount` for that band.

### Q1 2026 (4) — Fixed-price renewal options if hyperscale designs change

`datahall.lease.fact_renewal.fixed_price_option_flag`, `design_changed_flag`, and `spread_rate`. `megawatt_band_id` selects larger bands. `customer_vertical_id` joins `datahall.interconnection.dim_customer_vertical.vertical_code` hyperscaler.

### Q1 2026 (5) — Expense lines other than energy slowing cash NOI

`datahall.lease.fact_cash_noi.constant_currency_growth_rate`, `cash_noi_growth_rate`, and `expense_amount`. `expense_line_id` joins `datahall.lease.dim_expense_line.line_code`, keeping energy apart from labor, property tax, insurance, and other. `currency_id` is the currency.

### Q1 2026 (7) — AI share of leasing above 1 megawatt and unsold capacity

`datahall.lease.fact_booking.booked_mw` and `ai_flag` with `megawatt_band_id` joined to `band_code` mw_1_plus. Unsold capacity is `datahall.lease.fact_occupancy.unsold_mw` for the same metro. `customer_vertical_id` is the mix.

### Q1 2026 (8) — Greater-than-1-megawatt bookings and new buildings in Charlotte and Atlanta

`datahall.lease.fact_booking_outlook.booked_mw`, `remaining_year_mw`, and `new_building_mw`. `metro_id` joins `datahall.interconnection.dim_metro.metro_name` for Charlotte and Atlanta. `megawatt_band_id` is mw_1_plus. `fiscal_year_id` is the year.

### Q1 2026 (9) — Leased versus under-development space and power

`datahall.land.fact_capacity_stock.leased_space_mw`, `development_space_mw`, `leased_power_mw`, `development_power_mw`, `long_term_power_mw`, and `horizon_years`. Current leased megawatts are also `datahall.lease.fact_occupancy.leased_mw`. `region_id` and `fiscal_year_id` place the stock.

### Q4 2025 (2) — Inference scaling for the industry and the portfolio

`datahall.lease.fact_inference_demand.industry_inference_mw`, `portfolio_inference_mw`, and `product_fit_flag` for `fiscal_year_id`. `region_id` places the portfolio.

### Q4 2025 (5) — 0 to 1 megawatt share gain, and the picture if the band widens

`datahall.lease.fact_market_demand.company_booked_mw`, `market_booked_mw`, and `share_gain_flag`. `megawatt_band_id` joins `band_code` for mw_0_1 and for mw_2_to_3. `region_id` is the market.

### Q4 2025 (9) — Enterprise demand for 5 to 15 megawatt blocks

`datahall.lease.fact_enterprise_block.block_mw` with `megawatt_band_id` joined to `band_code` mw_5_to_15. `customer_id` joins `datahall.interconnection.dim_customer.customer_vertical_id` and `vertical_code` enterprise. `metro_id` places the block.

### Q4 2025 (10) — Renewal spreads versus shorter terms or higher escalators

`datahall.lease.fact_renewal.spread_rate`, `term_months`, `escalator_rate`, `shorter_term_flag`, and `higher_escalator_flag`. `lease_id` is the renewed lease. `fiscal_quarter_id` is the quarter.

### Q3 2025 (1) — Next-year growth versus development spend and currency

`datahall.lease.fact_growth_bridge.core_growth_rate`, `development_drag_amount`, `fx_effect_amount`, and `can_accelerate_flag`. `currency_id` joins `datahall.lease.dim_currency.currency_code`. `fiscal_year_id` is the year.

### Q3 2025 (3) — Room to lift renewal spreads on 2026 expirations

`datahall.lease.fact_expiration.expiring_rent_amount`, `expected_renewal_rent_amount`, and `spread_room_rate`. `fiscal_year_id` selects the 2026 expirations. `lease_id` is the expiring lease.

### Q3 2025 (10) — Average enterprise deployment size and share

`datahall.lease.fact_enterprise_block.block_mw`, `share_gain_flag`, and `competitor_block_mw`. Share is `datahall.lease.fact_competitor_position.company_share` and `competitor_share` for `customer_vertical_id` enterprise.

### Q3 2025 (11) — Whether double-digit spreads above 1 megawatt are a new level

`datahall.lease.fact_renewal.spread_rate` and `prior_spread_rate` with `megawatt_band_id` joined to `band_code` mw_1_plus. The forward book is `datahall.lease.fact_forward_renewal.spread_rate` and `book_level_flag`.

### Q2 2025 (1) — Whether the 0 to 1 megawatt inflection is market-wide or share gain

`datahall.lease.fact_market_demand.company_booked_mw`, `market_booked_mw`, and `share_gain_flag` with `band_code` mw_0_1. `fiscal_quarter_id` is the quarter the inflection is measured.

### Q2 2025 (3) — Sustainable multi-year growth after this year's rate

`datahall.lease.fact_multiyear_growth.this_year_growth_rate`, `sustainable_growth_rate`, `fx_effect_amount`, and `development_runway_flag`. `currency_id` is the currency. `fiscal_year_id` is the starting year.

### Q2 2025 (6) — Existing space to pull 0 to 1 megawatt bookings into 2026 commencements

`datahall.lease.fact_commencement_capacity.available_mw`, `demanded_mw`, and `can_pull_forward_flag`. `fiscal_year_id` is 2026. `megawatt_band_id` is mw_0_1. `metro_id` places the space.

### Q2 2025 (8) — When enterprise AI compounds demand in tier-one markets

`datahall.lease.fact_enterprise_ai_timing.start_year_number` and `reserved_mw`. `market_setting_id` joins `datahall.land.dim_market_setting.setting_code` tier_one. `metro_id` is the market.

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `datahall.calendar.dim_fiscal_year` | supporting population |
| `datahall.calendar.dim_fiscal_quarter` | supporting population |
| `datahall.calendar.dim_calendar_day` | supporting population |
| `datahall.lease.dim_megawatt_band` | Q1 2026 (3) |
| `datahall.lease.dim_expense_line` | Q1 2026 (5) |
| `datahall.lease.dim_currency` | Q3 2025 (1) |
| `datahall.lease.dim_lease` | supporting population |
| `datahall.lease.fact_booking` | Q1 2026 (7) |
| `datahall.lease.fact_commencement` | Q1 2026 (2) |
| `datahall.lease.fact_occupancy` | Q1 2026 (7), Q1 2026 (9) |
| `datahall.lease.fact_renewal` | Q1 2026 (4), Q4 2025 (10), Q3 2025 (11) |
| `datahall.lease.fact_expiration` | Q3 2025 (3) |
| `datahall.lease.fact_forward_renewal` | Q3 2025 (11) |
| `datahall.lease.fact_cash_noi` | Q1 2026 (5) |
| `datahall.lease.fact_market_demand` | Q4 2025 (5), Q2 2025 (1) |
| `datahall.lease.fact_enterprise_block` | Q4 2025 (9), Q3 2025 (10) |
| `datahall.lease.fact_inference_demand` | Q4 2025 (2) |
| `datahall.lease.fact_growth_bridge` | Q3 2025 (1) |
| `datahall.lease.fact_multiyear_growth` | Q2 2025 (3) |
| `datahall.lease.fact_commencement_capacity` | Q2 2025 (6) |
| `datahall.lease.fact_small_block_runrate` | Q1 2026 (3) |
| `datahall.lease.fact_booking_outlook` | Q1 2026 (8) |
| `datahall.lease.fact_competitor_position` | Q3 2025 (10) |
| `datahall.lease.fact_enterprise_ai_timing` | Q2 2025 (8) |
