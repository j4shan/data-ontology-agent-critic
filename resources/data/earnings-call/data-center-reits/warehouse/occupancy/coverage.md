# Colocation Inc occupancy and leasing

Retail cabinet occupancy separate from wholesale leased megawatts, bookings, churn, leases and pipeline.

Every fact below uses `fiscal_period_id` for the fiscal period and `scenario_id` for the scenario (`reported` or `guide` in `dim_scenario`). Measure descriptions in the YAML name the unit.

## Equinix (EQIX)

### Q2 2026 (5)

How should the three regions grow relative to the portfolio, and is growth inside the range similar each year?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q2 2026 (6)

How much of the multi-year upside comes from renewal spreads?

- `colocation.wholesale.fact_lease_commencement_event`: `leased_mw`, `commencement_lag_day_count`, `wholesale_lease_id`
- `colocation.wholesale.fact_lease_expiration_quantity`: `expiring_mw`, `expiring_lease_count`
- `colocation.wholesale.fact_renewal_spread_rate`: `renewal_spread_rate`, `annual_escalator_rate`

### Q2 2026 (7)

What operating and risk steps keep the CapEx plan deployable if realized demand misses the forecast?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q2 2026 (8)

What supports higher development spending when others are also adding large-scale capacity?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q2 2026 (11)

Is the leasing pipeline showing open-weight models driving private AI or enterprise inference?

- `colocation.commercial.fact_pipeline_quantity`: `pipeline_mw`, `pipeline_booking_count`, `workload_phase_id`, `deployment_model_id`, `model_access_type_id`
- `colocation.wholesale.fact_wholesale_booking_quantity`: `booked_mw`, `deal_size_band_id`

### Q1 2026 (2)

Are tenants committing earlier and for longer terms, and how is that showing up in price, term, or deposits on pre-leasing?

- `colocation.commercial.fact_pipeline_quantity`: `pipeline_mw`, `pipeline_booking_count`, `workload_phase_id`, `deployment_model_id`, `model_access_type_id`
- `colocation.wholesale.fact_wholesale_booking_quantity`: `booked_mw`, `deal_size_band_id`

### Q1 2026 (3)

Are higher memory, fuel, and IT costs pulling demand forward or pushing deals out?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q1 2026 (4)

Does AI inference require more incremental capital than traditional workloads, and does higher density raise or lower returns?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q1 2026 (5)

How much of the sequential bookings dip is seasonal, and what is the mix of traditional enterprise versus larger deals?

- `colocation.commercial.fact_pipeline_quantity`: `pipeline_mw`, `pipeline_booking_count`, `workload_phase_id`, `deployment_model_id`, `model_access_type_id`
- `colocation.wholesale.fact_wholesale_booking_quantity`: `booked_mw`, `deal_size_band_id`

### Q1 2026 (7)

Have Middle East geopolitical issues affected the ability to sell or add capacity there?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q1 2026 (8)

Is the low churn rate delayed demand that returns above the usual range, or can the full year stay at the low end?

- `colocation.commercial.fact_churn_rate`: `churn_rate`, `churn_reason_id`, `region_id`
- `colocation.commercial.fact_churn_base_amount`: `beginning_recurring_revenue_amount`, `expiring_recurring_revenue_amount`

### Q1 2026 (9)

What framework sizes the one-time fees on xScale leases, and what is the status of pre-leasing at the Manukau campus?

- `colocation.commercial.fact_pipeline_quantity`: `pipeline_mw`, `pipeline_booking_count`, `workload_phase_id`, `deployment_model_id`, `model_access_type_id`
- `colocation.wholesale.fact_wholesale_booking_quantity`: `booked_mw`, `deal_size_band_id`

### Q1 2026 (10)

Are agent workloads pulling investment from public cloud toward the edge, and how do customers choose colocation versus on-premises?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q1 2026 (11)

Is the current annual development spend the run rate for the next few years, or is it front-loaded?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q1 2026 (12)

How many liquid-cooling deployments are active or signed, and how quickly is direct-to-chip or immersion demand growing?

- `colocation.wholesale.fact_lease_commencement_event`: `leased_mw`, `commencement_lag_day_count`, `wholesale_lease_id`
- `colocation.wholesale.fact_lease_expiration_quantity`: `expiring_mw`, `expiring_lease_count`
- `colocation.wholesale.fact_renewal_spread_rate`: `renewal_spread_rate`, `annual_escalator_rate`

### Q4 2025 (2)

Do AI deals differ from traditional deals in size or location, and has demand accelerated since the prior update?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q4 2025 (3)

How much of the churn-improvement opportunity is in the company's control versus customer workload optimization?

- `colocation.commercial.fact_churn_rate`: `churn_rate`, `churn_reason_id`, `region_id`
- `colocation.commercial.fact_churn_base_amount`: `beginning_recurring_revenue_amount`, `expiring_recurring_revenue_amount`

### Q4 2025 (5)

How much further can pricing move, and what causes the growth rate to vary inside the projected range?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q4 2025 (6)

Can cost reductions continue, or do bookings at this pace require more staffing?

- `colocation.commercial.fact_pipeline_quantity`: `pipeline_mw`, `pipeline_booking_count`, `workload_phase_id`, `deployment_model_id`, `model_access_type_id`
- `colocation.wholesale.fact_wholesale_booking_quantity`: `booked_mw`, `deal_size_band_id`

### Q4 2025 (7)

How much of the bookings came from new cabinets in constrained markets such as Northern Virginia and Frankfurt versus a broader demand acceleration?

- `colocation.commercial.fact_pipeline_quantity`: `pipeline_mw`, `pipeline_booking_count`, `workload_phase_id`, `deployment_model_id`, `model_access_type_id`
- `colocation.wholesale.fact_wholesale_booking_quantity`: `booked_mw`, `deal_size_band_id`

### Q3 2025 (2)

Is selling capacity further ahead of delivery driving pre-lease strength, and how much of upcoming capacity in key markets is pre-leased?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q3 2025 (3)

Is pricing firm or improving because of capacity constraints, including on pre-sales?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q3 2025 (4)

Which of the new land sites are largest, and where is the plan xScale versus retail?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q3 2025 (5)

How is the Chicago campus split between xScale and retail?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q3 2025 (6)

What demand and pre-leasing are showing up in larger-footprint retail?

- `colocation.commercial.fact_pipeline_quantity`: `pipeline_mw`, `pipeline_booking_count`, `workload_phase_id`, `deployment_model_id`, `model_access_type_id`
- `colocation.wholesale.fact_wholesale_booking_quantity`: `booked_mw`, `deal_size_band_id`

### Q3 2025 (7)

Why are constant-currency growth rates diverging across regions relative to profit?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q3 2025 (9)

Was the annualized and pre-sold bookings level a one-off, or a new quarterly run rate, and is pre-sold capacity priced differently?

- `colocation.commercial.fact_pipeline_quantity`: `pipeline_mw`, `pipeline_booking_count`, `workload_phase_id`, `deployment_model_id`, `model_access_type_id`
- `colocation.wholesale.fact_wholesale_booking_quantity`: `booked_mw`, `deal_size_band_id`

## Digital Realty (DLR)

### Q1 2026 (2)

Is the jump in commencement lag to about 19 months from one large lease, utility delays, or customers booking further ahead?

- `colocation.wholesale.fact_lease_commencement_event`: `leased_mw`, `commencement_lag_day_count`, `wholesale_lease_id`
- `colocation.wholesale.fact_lease_expiration_quantity`: `expiring_mw`, `expiring_lease_count`
- `colocation.wholesale.fact_renewal_spread_rate`: `renewal_spread_rate`, `annual_escalator_rate`

### Q1 2026 (4)

If hyperscalers change designs, how relevant are fixed-price renewal options on larger contracts?

- `colocation.wholesale.fact_lease_commencement_event`: `leased_mw`, `commencement_lag_day_count`, `wholesale_lease_id`
- `colocation.wholesale.fact_lease_expiration_quantity`: `expiring_mw`, `expiring_lease_count`
- `colocation.wholesale.fact_renewal_spread_rate`: `renewal_spread_rate`, `annual_escalator_rate`

### Q1 2026 (5)

Which operating-expense lines, other than energy, slowed constant-currency cash NOI growth?

- `colocation.commercial.fact_operating_cost_amount`: `operating_cost_amount`, `cost_reduction_amount`, `cost_category_id`
- `colocation.power.fact_development_spend_amount`: `development_spend_amount`, `development_project_id`

### Q1 2026 (7)

How far down the deal-size spectrum is AI showing up in leasing above 1 megawatt, and what does that mean for filling remaining capacity?

- `colocation.commercial.fact_pipeline_quantity`: `pipeline_mw`, `pipeline_booking_count`, `workload_phase_id`, `deployment_model_id`, `model_access_type_id`
- `colocation.wholesale.fact_wholesale_booking_quantity`: `booked_mw`, `deal_size_band_id`

### Q1 2026 (8)

How should greater-than-1-megawatt bookings trend for the rest of the year given additional large buildings in Charlotte and Atlanta?

- `colocation.commercial.fact_pipeline_quantity`: `pipeline_mw`, `pipeline_booking_count`, `workload_phase_id`, `deployment_model_id`, `model_access_type_id`
- `colocation.wholesale.fact_wholesale_booking_quantity`: `booked_mw`, `deal_size_band_id`

### Q4 2025 (2)

What does inference scaling in 2026 look like for the industry and for the portfolio?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q4 2025 (3)

Are any bottlenecks limiting growth even with hyperscale capital spending staying high?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q4 2025 (5)

How much of 0–1 megawatt strength is share gain versus underlying demand, and does the picture change if the band is widened to 2 or 3 megawatts?

- `colocation.commercial.fact_pipeline_quantity`: `pipeline_mw`, `pipeline_booking_count`, `workload_phase_id`, `deployment_model_id`, `model_access_type_id`
- `colocation.wholesale.fact_wholesale_booking_quantity`: `booked_mw`, `deal_size_band_id`

### Q4 2025 (6)

How could industry capacity arriving in 2027 and 2028 affect bookings, and how far out is labor secured for contracted growth?

- `colocation.commercial.fact_pipeline_quantity`: `pipeline_mw`, `pipeline_booking_count`, `workload_phase_id`, `deployment_model_id`, `model_access_type_id`
- `colocation.wholesale.fact_wholesale_booking_quantity`: `booked_mw`, `deal_size_band_id`

### Q4 2025 (9)

What is showing up in enterprise demand for roughly 5 to 15 megawatt blocks?

- `colocation.commercial.fact_pipeline_quantity`: `pipeline_mw`, `pipeline_booking_count`, `workload_phase_id`, `deployment_model_id`, `model_access_type_id`
- `colocation.wholesale.fact_wholesale_booking_quantity`: `booked_mw`, `deal_size_band_id`

### Q4 2025 (10)

Given strong renewal spreads, is there appetite for shorter terms or higher annual escalators?

- `colocation.wholesale.fact_lease_commencement_event`: `leased_mw`, `commencement_lag_day_count`, `wholesale_lease_id`
- `colocation.wholesale.fact_lease_expiration_quantity`: `expiring_mw`, `expiring_lease_count`
- `colocation.wholesale.fact_renewal_spread_rate`: `renewal_spread_rate`, `annual_escalator_rate`

### Q3 2025 (1)

What puts and takes determine whether growth can hold or accelerate next year while development investment continues?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q3 2025 (3)

How much room is there to lift renewal spreads on 2026 expirations?

- `colocation.wholesale.fact_lease_commencement_event`: `leased_mw`, `commencement_lag_day_count`, `wholesale_lease_id`
- `colocation.wholesale.fact_lease_expiration_quantity`: `expiring_mw`, `expiring_lease_count`
- `colocation.wholesale.fact_renewal_spread_rate`: `renewal_spread_rate`, `annual_escalator_rate`

### Q3 2025 (4)

Is large-block demand diversified across neo clouds, model developers, and chip companies, or still concentrated in the largest hyperscalers?

- `colocation.commercial.fact_pipeline_quantity`: `pipeline_mw`, `pipeline_booking_count`, `workload_phase_id`, `deployment_model_id`, `model_access_type_id`
- `colocation.wholesale.fact_wholesale_booking_quantity`: `booked_mw`, `deal_size_band_id`

### Q3 2025 (8)

How large can 2027 development be relative to 2026 if most 2026 capacity is already sold?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q3 2025 (9)

Do 2026 and 2027 hyperscale commencements require liquid cooling and higher-voltage designs that most existing halls lack?

- `colocation.wholesale.fact_lease_commencement_event`: `leased_mw`, `commencement_lag_day_count`, `wholesale_lease_id`
- `colocation.wholesale.fact_lease_expiration_quantity`: `expiring_mw`, `expiring_lease_count`
- `colocation.wholesale.fact_renewal_spread_rate`: `renewal_spread_rate`, `annual_escalator_rate`

### Q3 2025 (10)

What is the average enterprise deployment size, and is share being gained there?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q3 2025 (11)

Are double-digit renewal spreads on leases above 1 megawatt a temporary artifact or a new level?

- `colocation.wholesale.fact_lease_commencement_event`: `leased_mw`, `commencement_lag_day_count`, `wholesale_lease_id`
- `colocation.wholesale.fact_lease_expiration_quantity`: `expiring_mw`, `expiring_lease_count`
- `colocation.wholesale.fact_renewal_spread_rate`: `renewal_spread_rate`, `annual_escalator_rate`

### Q3 2025 (12)

Is future capital spending tilted toward retrofits for denser deployments or toward new capacity?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q2 2025 (1)

Is the inflection in 0–1 megawatt growth market-wide or mostly share gain?

- `colocation.commercial.fact_pipeline_quantity`: `pipeline_mw`, `pipeline_booking_count`, `workload_phase_id`, `deployment_model_id`, `model_access_type_id`
- `colocation.wholesale.fact_wholesale_booking_quantity`: `booked_mw`, `deal_size_band_id`

### Q2 2025 (3)

What does sustainable multi-year growth look like after this year's rate?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`

### Q2 2025 (6)

If 0–1 megawatt bookings persist, is there existing space to pull more of that business into 2026 commencements?

- `colocation.wholesale.fact_lease_commencement_event`: `leased_mw`, `commencement_lag_day_count`, `wholesale_lease_id`
- `colocation.wholesale.fact_lease_expiration_quantity`: `expiring_mw`, `expiring_lease_count`
- `colocation.wholesale.fact_renewal_spread_rate`: `renewal_spread_rate`, `annual_escalator_rate`

### Q2 2025 (7)

As small-block bookings grow, is share being taken while peers build larger blocks?

- `colocation.commercial.fact_pipeline_quantity`: `pipeline_mw`, `pipeline_booking_count`, `workload_phase_id`, `deployment_model_id`, `model_access_type_id`
- `colocation.wholesale.fact_wholesale_booking_quantity`: `booked_mw`, `deal_size_band_id`

### Q2 2025 (8)

When do customers say enterprise AI adoption starts to compound demand in tier-one markets?

- `colocation.retail.fact_retail_cabinet_occupied_quantity`: `leased_cabinet_count`, `occupied_cabinet_count`, `retail_facility_id`
- `colocation.retail.fact_retail_cabinet_capacity_quantity`: `total_cabinet_count`, `available_cabinet_count`
- `colocation.retail.fact_retail_booking_amount`: `annualized_booking_amount`, `metro_id`
