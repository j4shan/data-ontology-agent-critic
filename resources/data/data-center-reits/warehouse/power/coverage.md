# Colocation Inc power and development capacity coverage

This slice is the campus, the IBX, land, development projects, power, cooling, and the capital plan. Power and IT capacity are not occupancy. Bookings, revenue, and interconnection are owned in the other slices. A campus such as Chicago or Manukau is a row of the campus population, not a separate dataset. Metro, region, product line, workload, and customer vertical are referenced and not re-authored.

Foreign identities are referenced from this slice and are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column | Node |
| --- | --- | --- |
| `customer_vertical_identity` | `customer_vertical_id` | `sf:colocation.interconnection.dim_customer_vertical` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:colocation.calendar.dim_fiscal_quarter` |
| `fiscal_year_identity` | `fiscal_year_id` | `sf:colocation.calendar.dim_fiscal_year` |
| `metro_identity` | `metro_id` | `sf:colocation.interconnection.dim_metro` |
| `product_line_identity` | `product_line_id` | `sf:colocation.occupancy.dim_product_line` |
| `region_identity` | `region_id` | `sf:colocation.interconnection.dim_region` |
| `workload_type_identity` | `workload_type_id` | `sf:colocation.occupancy.dim_workload_type` |

## Complete populations

| Identity | Dataset | Column |
| --- | --- | --- |
| `campus_identity` | `colocation.power.dim_campus` | `campus_id` |
| `ibx_identity` | `colocation.power.dim_ibx` | `ibx_id` |
| `land_site_identity` | `colocation.power.dim_land_site` | `land_site_id` |
| `development_project_identity` | `colocation.power.dim_development_project` | `development_project_id` |
| `power_source_identity` | `colocation.power.dim_power_source` | `power_source_id` |
| `cooling_technology_identity` | `colocation.power.dim_cooling_technology` | `cooling_technology_id` |
| `density_class_identity` | `colocation.power.dim_density_class` | `density_class_id` |
| `development_spend_identity` | `colocation.power.fact_development_spend` | `development_spend_id` |
| `demand_case_identity` | `colocation.power.fact_demand_case` | `demand_case_id` |
| `market_power_identity` | `colocation.power.fact_market_power` | `market_power_id` |
| `capacity_plan_identity` | `colocation.power.fact_capacity_plan` | `capacity_plan_id` |
| `industry_supply_identity` | `colocation.power.fact_industry_supply` | `industry_supply_id` |
| `project_power_identity` | `colocation.power.fact_project_power` | `project_power_id` |
| `power_milestone_identity` | `colocation.power.fact_power_milestone` | `power_milestone_id` |
| `campus_mix_identity` | `colocation.power.fact_campus_mix` | `campus_mix_id` |
| `cooling_deployment_identity` | `colocation.power.fact_cooling_deployment` | `cooling_deployment_id` |
| `edge_constraint_identity` | `colocation.power.fact_edge_constraint` | `edge_constraint_id` |
| `workload_capital_identity` | `colocation.power.fact_workload_capital` | `workload_capital_id` |
| `enterprise_power_identity` | `colocation.power.fact_enterprise_power` | `enterprise_power_id` |
| `delivery_schedule_identity` | `colocation.power.fact_delivery_schedule` | `delivery_schedule_id` |
| `affo_path_identity` | `colocation.power.fact_affo_path` | `affo_path_id` |
| `region_operation_identity` | `colocation.power.fact_region_operations` | `region_operation_id` |

## Numbered questions

### Q2 2026 (1) — Development-spend increase and the revenue-growth outlook

`colocation.power.fact_development_spend.spend_increase_amount`, `capital_spend_amount`, `prior_plan_amount`, and `demand_support_flag`. The outlook those additions feed is `colocation.occupancy.fact_revenue_guide.growth_outlook_low_rate`, `growth_outlook_high_rate`, and `demand_supported_flag` on `fiscal_year_id`.

### Q2 2026 (7) — Deploying the capital plan if demand misses

`colocation.power.fact_demand_case.lower_demand_mw`, `base_demand_mw`, `deployable_flag`, and `risk_step_code` against `colocation.power.fact_development_spend.capital_spend_amount` for the same `fiscal_year_id` and `region_id`.

### Q2 2026 (8) — Equinix additions versus industry supply

`colocation.power.fact_industry_supply.company_addition_mw`, `industry_addition_mw`, and `demand_durable_flag`. Spend beside that supply is `colocation.power.fact_development_spend.capital_spend_amount` for the same region and year.

### Q2 2026 (9) — Power support for incremental capacity in constrained top markets

`colocation.power.fact_market_power.planned_it_mw`, `power_available_mw`, and `power_supported_mw` where `top_market_flag` and `constrained_flag` are set. `metro_id` joins `colocation.interconnection.dim_metro.metro_name`.

### Q2 2026 (10) — Annual IT gigawatts versus the developable pool

`colocation.power.fact_capacity_plan.annual_it_gw`, `developable_gw`, `spend_per_mw`, and `capex_amount` for `fiscal_year_id`.

### Q1 2026 (4) — Capital intensity and returns for AI inference versus traditional density

`colocation.power.fact_workload_capital.capital_per_mw`, `historical_capital_per_mw`, `return_rate`, and `density_raises_return_flag`. `workload_type_id` joins `colocation.occupancy.dim_workload_type.workload_code`. `density_class_id` is the density class.

### Q1 2026 (7) — Middle East ability to sell or add capacity

`colocation.power.fact_region_operations.sell_capacity_flag`, `add_capacity_flag`, and `disruption_flag`. `region_id` joins `colocation.interconnection.dim_region.region_code` for middle_east. `metro_id` is the market inside that region.

### Q1 2026 (11) — This year's development spend versus the multi-year program

`colocation.power.fact_development_spend.capital_spend_amount`, `run_rate_amount`, `front_loaded_flag`, and `multiyear_program_amount` by `fiscal_year_id`.

### Q1 2026 (12) — Liquid, direct-to-chip, and immersion deployments

`colocation.power.fact_cooling_deployment.deployment_status`, `deployment_count`, and `growth_rate`. `cooling_technology_id` joins `colocation.power.dim_cooling_technology.technology_code` for liquid, direct_to_chip, and immersion. `campus_id` places the deployment.

### Q1 2026 (13) — Edge workloads hitting space, power, or thermal limits

`colocation.power.fact_edge_constraint.space_constrained_flag`, `power_constrained_flag`, `thermal_constrained_flag`, and `density_kw_per_cabinet`. `workload_type_id` selects agentic workloads. `ibx_id` and `metro_id` place the constraint.

### Q4 2025 (4) — Whether power has caught up with enterprise demand

`colocation.power.fact_enterprise_power.available_power_mw`, `required_power_mw`, and `caught_up_flag`. `customer_vertical_id` joins `colocation.interconnection.dim_customer_vertical.vertical_code` for enterprise. `metro_id` is the market.

### Q3 2025 (2) — Capacity sold ahead of delivery and the pre-leased share

`colocation.power.fact_delivery_schedule.sell_ahead_flag`, `upcoming_capacity_mw`, `preleased_mw`, and `presold_share`. `metro_id` is the key market. `development_project_id` is the project still to deliver.

### Q3 2025 (4) — Largest new land sites and xScale versus retail

`colocation.power.dim_land_site.relative_size_rank` and `site_name`. `product_line_id` joins `colocation.occupancy.dim_product_line.product_line_code` for xscale or retail. `metro_id` is the city market.

### Q3 2025 (5) — Chicago campus split between xScale and retail

`colocation.power.fact_campus_mix.planned_mw` and `planned_share` by `product_line_id`. `campus_id` joins `colocation.power.dim_campus.campus_name` for the Chicago campus. `colocation.occupancy.dim_product_line.product_line_code` separates xscale and retail.

### Q3 2025 (8) — Power availability and schedule on xScale projects

`colocation.power.fact_project_power.power_available_flag` and `schedule_confidence`. Delivery and power dates are `colocation.power.fact_power_milestone.fiscal_quarter_id` with `milestone_code` of scheduled_capacity_delivery or power_delivery. `development_project_id` joins `colocation.power.dim_development_project.xscale_flag`. `power_source_id` names the source.

### Q3 2025 (11) — Faster builds, capitalized expense, and the AFFO path

`colocation.power.fact_affo_path.analyst_day_affo_growth`, `accelerated_build_affo_growth`, `capitalized_expense_amount`, and `shape_change_flag` by `fiscal_year_id`.

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `colocation.power.dim_campus` | Q3 2025 (5) |
| `colocation.power.dim_ibx` | supporting population |
| `colocation.power.dim_land_site` | Q3 2025 (4) |
| `colocation.power.dim_development_project` | Q3 2025 (8) |
| `colocation.power.dim_power_source` | supporting population |
| `colocation.power.dim_cooling_technology` | Q1 2026 (12) |
| `colocation.power.dim_density_class` | supporting population |
| `colocation.power.fact_development_spend` | Q2 2026 (1), Q2 2026 (7), Q2 2026 (8), Q1 2026 (11) |
| `colocation.power.fact_demand_case` | Q2 2026 (7) |
| `colocation.power.fact_market_power` | Q2 2026 (9) |
| `colocation.power.fact_capacity_plan` | Q2 2026 (10) |
| `colocation.power.fact_industry_supply` | Q2 2026 (8) |
| `colocation.power.fact_project_power` | Q3 2025 (8) |
| `colocation.power.fact_power_milestone` | Q3 2025 (8) |
| `colocation.power.fact_campus_mix` | Q3 2025 (5) |
| `colocation.power.fact_cooling_deployment` | Q1 2026 (12) |
| `colocation.power.fact_edge_constraint` | Q1 2026 (13) |
| `colocation.power.fact_workload_capital` | Q1 2026 (4) |
| `colocation.power.fact_enterprise_power` | Q4 2025 (4) |
| `colocation.power.fact_delivery_schedule` | Q3 2025 (2) |
| `colocation.power.fact_affo_path` | Q3 2025 (11) |
| `colocation.power.fact_region_operations` | Q1 2026 (7) |
