# Digital Realty land-bank power coverage

This slice is land, power, the campus, the hall, and development. Secured land-bank power is not the quarter that power becomes available, and neither is leased occupancy. Bookings, commencements, and customer vertical are owned in the other slices. Metro and region are referenced and not re-authored.

Foreign identities are referenced from this slice and are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column | Node |
| --- | --- | --- |
| `customer_identity` | `customer_id` | `sf:digitalrealty.interconnection.dim_customer` |
| `customer_vertical_identity` | `customer_vertical_id` | `sf:digitalrealty.interconnection.dim_customer_vertical` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:digitalrealty.calendar.dim_fiscal_quarter` |
| `fiscal_year_identity` | `fiscal_year_id` | `sf:digitalrealty.calendar.dim_fiscal_year` |
| `megawatt_band_identity` | `megawatt_band_id` | `sf:digitalrealty.lease.dim_megawatt_band` |
| `metro_identity` | `metro_id` | `sf:digitalrealty.interconnection.dim_metro` |
| `region_identity` | `region_id` | `sf:digitalrealty.interconnection.dim_region` |

## Complete populations

| Identity | Dataset | Column |
| --- | --- | --- |
| `market_setting_identity` | `digitalrealty.land.dim_market_setting` | `market_setting_id` |
| `campus_identity` | `digitalrealty.land.dim_campus` | `campus_id` |
| `hall_identity` | `digitalrealty.land.dim_hall` | `hall_id` |
| `land_parcel_identity` | `digitalrealty.land.dim_land_parcel` | `land_parcel_id` |
| `development_project_identity` | `digitalrealty.land.dim_development_project` | `development_project_id` |
| `power_source_identity` | `digitalrealty.land.dim_power_source` | `power_source_id` |
| `constraint_identity` | `digitalrealty.land.dim_constraint` | `constraint_id` |
| `cooling_design_identity` | `digitalrealty.land.dim_cooling_design` | `cooling_design_id` |
| `voltage_design_identity` | `digitalrealty.land.dim_voltage_design` | `voltage_design_id` |
| `funding_channel_identity` | `digitalrealty.land.dim_funding_channel` | `funding_channel_id` |
| `capex_purpose_identity` | `digitalrealty.land.dim_capex_purpose` | `capex_purpose_id` |
| `land_power_identity` | `digitalrealty.land.fact_land_power` | `land_power_id` |
| `power_availability_identity` | `digitalrealty.land.fact_power_availability` | `power_availability_id` |
| `power_horizon_identity` | `digitalrealty.land.fact_power_horizon` | `power_horizon_id` |
| `project_constraint_identity` | `digitalrealty.land.fact_project_constraint` | `project_constraint_id` |
| `capacity_stock_identity` | `digitalrealty.land.fact_capacity_stock` | `capacity_stock_id` |
| `development_cost_identity` | `digitalrealty.land.fact_development_cost` | `development_cost_id` |
| `developable_identity` | `digitalrealty.land.fact_developable` | `developable_id` |
| `industry_capacity_identity` | `digitalrealty.land.fact_industry_capacity` | `industry_capacity_id` |
| `labor_cover_identity` | `digitalrealty.land.fact_labor_cover` | `labor_cover_id` |
| `site_strategy_identity` | `digitalrealty.land.fact_site_strategy` | `site_strategy_id` |
| `behind_meter_identity` | `digitalrealty.land.fact_behind_meter` | `behind_meter_id` |
| `year_development_identity` | `digitalrealty.land.fact_year_development` | `year_development_id` |
| `fleet_requirement_identity` | `digitalrealty.land.fact_fleet_requirement` | `fleet_requirement_id` |
| `capex_mix_identity` | `digitalrealty.land.fact_capex_mix` | `capex_mix_id` |
| `fund_position_identity` | `digitalrealty.land.fact_fund_position` | `fund_position_id` |
| `deal_funding_identity` | `digitalrealty.land.fact_deal_funding` | `deal_funding_id` |
| `customer_interest_identity` | `digitalrealty.land.fact_customer_interest` | `customer_interest_id` |

## Numbered questions

### Q1 2026 (1) — Land-bank power secured, locations, and when it is available

`digitalrealty.land.fact_land_power.incremental_gw` and `location_count` by `region_id` and `metro_id`. Availability is `digitalrealty.land.fact_power_availability.available_gw` and `fiscal_quarter_id` joined on `land_power_id`. `digitalrealty.interconnection.dim_region.region_code` names the region.

### Q1 2026 (6) — Which constraint extends construction, and whether commitments hold

`digitalrealty.land.fact_project_constraint.delay_months` and `commitment_still_held_flag`. `constraint_id` joins `digitalrealty.land.dim_constraint.constraint_code` for power, equipment, labor, and local opposition. `development_project_id` is the project.

### Q1 2026 (10) — Americas cost per megawatt and harder-to-deliver markets

`digitalrealty.land.fact_development_cost.cost_per_mw`, `prior_cost_per_mw`, and `hard_to_deliver_flag`. `region_id` joins `region_code` americas. `metro_id` is the future market.

### Q4 2025 (1) — Whether Americas hyperscalers are looking further out for power

`digitalrealty.land.fact_power_horizon.horizon_months`, `prior_horizon_months`, and `further_out_flag`. `region_id` is americas. `customer_vertical_id` joins `vertical_code` hyperscaler.

### Q4 2025 (3) — Bottlenecks that limit growth while hyperscale demand stays high

`digitalrealty.land.fact_project_constraint.growth_limited_flag`, `hyperscale_demand_high_flag`, and `delay_months` by `constraint_id`. `development_project_id` is the constrained project.

### Q4 2025 (4) — When developable capacity beyond the pipeline becomes leasable

`digitalrealty.land.fact_developable.lifecycle_stage`, `developable_mw`, and `fiscal_quarter_id`. `lifecycle_stage` beyond_pipeline is the capacity outside the current pipeline. `development_project_id` is the project.

### Q4 2025 (6) — Industry capacity in 2027 and 2028, and labor secured for contracted growth

`digitalrealty.land.fact_industry_capacity.industry_mw`, `company_demand_mw`, and `booking_effect` by `fiscal_year_id`. Labor is `digitalrealty.land.fact_labor_cover.contracted_growth_mw`, `labor_secured_mw`, and `coverage_flag` for the same region.

### Q4 2025 (8) — Large-footprint sites in remote power-capable markets

`digitalrealty.land.fact_site_strategy.ai_demand_mw`, `chosen_flag`, and `market_setting_id` joined to `setting_code` remote. `metro_id` names the market when one is chosen.

### Q3 2025 (5) — Tertiary multi-hundred-megawatt deals on balance sheet or through the fund

`digitalrealty.land.fact_deal_funding.deal_mw` and `pursued_flag`. `funding_channel_id` joins `channel_code` balance_sheet or hyperscale_fund. `market_setting_id` joins `setting_code` tertiary. `megawatt_band_id` joins `band_code` multi_hundred.

### Q3 2025 (6) — Behind-the-meter power where the grid is constrained

`digitalrealty.land.fact_behind_meter.considered_flag`, `grid_constrained_flag`, and `additional_building_flag`. `power_source_id` joins `digitalrealty.land.dim_power_source.source_code` behind_the_meter_gas. `campus_id` joins `digitalrealty.land.dim_campus.campus_name` for the Northern Virginia site.

### Q3 2025 (7) — When future developable capacity becomes leasable, and the customer conversations

`digitalrealty.land.fact_developable.fiscal_quarter_id`, `developable_mw`, and `lifecycle_stage`. Conversations are `digitalrealty.land.fact_customer_interest.interest_mw` and `customer_id` on the same `development_project_id`.

### Q3 2025 (8) — 2027 development relative to 2026 if 2026 is already sold

`digitalrealty.land.fact_year_development.development_mw`, `sold_mw`, and `sold_share` by `fiscal_year_id` for 2026 and 2027. `region_id` places the table.

### Q3 2025 (9) — Liquid cooling and higher voltage versus the existing halls

`digitalrealty.land.fact_fleet_requirement.required_flag`, `existing_hall_capable_flag`, and `commencement_mw`. `cooling_design_id` joins `design_code` liquid. `voltage_design_id` joins `design_code` higher_voltage. Existing halls are `digitalrealty.land.dim_hall.cooling_design_id` and `voltage_design_id`.

### Q3 2025 (12) — Capex for density retrofits versus new capacity

`digitalrealty.land.fact_capex_mix.capital_spend_amount` and `density_kw`. `capex_purpose_id` joins `digitalrealty.land.dim_capex_purpose.purpose_code` retrofit_density or new_capacity. `fiscal_year_id` is the year.

### Q2 2025 (2) — Remote gigawatt supply and competition in core markets

`digitalrealty.land.fact_site_strategy.industry_remote_mw`, `core_market_demand_mw`, and `competitive_pressure_flag`. `market_setting_id` joins `setting_code` remote. `fiscal_year_id` is the year of the comparison.

### Q2 2025 (4) — How the hyperscale fund changes the financial model once developed

`digitalrealty.land.fact_fund_position.fee_amount`, `earnings_amount`, and `model_change_flag`. `funding_channel_id` joins `channel_code` hyperscale_fund. `fiscal_year_id` is the year the fund is funded and developed.

### Q2 2025 (5) — Majority operating stake and minority development stake in the fund

`digitalrealty.land.fact_fund_position.asset_role`, `ownership_share`, and `majority_flag`. `asset_role` separates operating from development. `funding_channel_id` is the hyperscale fund.

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `digitalrealty.land.dim_market_setting` | supporting population |
| `digitalrealty.land.dim_campus` | Q3 2025 (6) |
| `digitalrealty.land.dim_hall` | Q3 2025 (9) |
| `digitalrealty.land.dim_land_parcel` | supporting population |
| `digitalrealty.land.dim_development_project` | supporting population |
| `digitalrealty.land.dim_power_source` | Q3 2025 (6) |
| `digitalrealty.land.dim_constraint` | Q1 2026 (6) |
| `digitalrealty.land.dim_cooling_design` | supporting population |
| `digitalrealty.land.dim_voltage_design` | supporting population |
| `digitalrealty.land.dim_funding_channel` | supporting population |
| `digitalrealty.land.dim_capex_purpose` | Q3 2025 (12) |
| `digitalrealty.land.fact_land_power` | Q1 2026 (1) |
| `digitalrealty.land.fact_power_availability` | Q1 2026 (1) |
| `digitalrealty.land.fact_power_horizon` | Q4 2025 (1) |
| `digitalrealty.land.fact_project_constraint` | Q1 2026 (6), Q4 2025 (3) |
| `digitalrealty.land.fact_capacity_stock` | supporting population |
| `digitalrealty.land.fact_development_cost` | Q1 2026 (10) |
| `digitalrealty.land.fact_developable` | Q4 2025 (4), Q3 2025 (7) |
| `digitalrealty.land.fact_industry_capacity` | Q4 2025 (6) |
| `digitalrealty.land.fact_labor_cover` | Q4 2025 (6) |
| `digitalrealty.land.fact_site_strategy` | Q4 2025 (8), Q2 2025 (2) |
| `digitalrealty.land.fact_behind_meter` | Q3 2025 (6) |
| `digitalrealty.land.fact_year_development` | Q3 2025 (8) |
| `digitalrealty.land.fact_fleet_requirement` | Q3 2025 (9) |
| `digitalrealty.land.fact_capex_mix` | Q3 2025 (12) |
| `digitalrealty.land.fact_fund_position` | Q2 2025 (4), Q2 2025 (5) |
| `digitalrealty.land.fact_deal_funding` | Q3 2025 (5) |
| `digitalrealty.land.fact_customer_interest` | Q3 2025 (7) |
