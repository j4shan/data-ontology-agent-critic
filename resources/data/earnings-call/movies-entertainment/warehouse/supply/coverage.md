# Studio Inc supply slice

This slice is part of the Studio Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q2 FY2026 (2) — Walt Disney

Can the parks model of high spend per guest be rebuilt inside Disney+ through merchandise, park access, and games?

- `studio.supply.fact_park_project_capacity`: `park_project_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `project_vintage_id`, `added_capacity_quantity`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.supply.fact_park_capacity_fact`: `park_capacity_fact_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `guest_capacity_quantity`, `available_ride_capacity_quantity`
- `studio.price.fact_park_capital_spending`: `park_capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `project_vintage_id`, `capital_spending_amount`
- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`

### Q4 2025 (1) — Netflix

Where is the incremental content investment going if amortization growth is set to accelerate — events, reality, films, or licensed titles?

- `studio.demand.dim_content_origin`: `content_origin_id`, `content_origin_code`, `content_origin_name`
- `studio.supply.fact_content_library`: `content_library_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `content_origin_id`, `title_quantity`, `content_hour_quantity`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `studio.demand.fact_podcast_engagement`: `podcast_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `podcast_hour_quantity`
- `studio.supply.fact_production_slate`: `production_slate_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `distribution_window_id`, `slate_title_quantity`

### Q4 2025 (3) — Netflix

What did recent live events, including a combat sports bout and NFL games on Christmas, show about that format?

- `studio.supply.fact_sports_rights_capacity`: `sports_rights_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `sports_league_id`, `linear_network_id`, `live_event_quantity`
- `studio.demand.dim_sports_league`: `sports_league_id`, `sports_league_code`, `sports_league_name`
- `studio.demand.fact_live_event_audience`: `live_event_audience_record_id`, `fiscal_quarter_id`, `scenario_id`, `sports_league_id`, `content_type_id`, `viewer_quantity`
- `studio.price.fact_sports_revenue`: `sports_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `sports_league_id`, `linear_network_id`, `sports_revenue_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
