# Studio Inc demand slice

This slice is part of the Studio Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q3 FY2026 (7) — Walt Disney

What would show that streaming is the better path than shifting back toward licensing, given engagement pressure from higher-volume competitors?

- `studio.demand.fact_streaming_engagement`: `streaming_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `content_type_id`, `device_type_id`, `hours_viewed_quantity`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.fact_subscriber_churn_volume`: `subscriber_churn_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `net_membership_change_quantity`
- `studio.demand.fact_impressions_volume`: `impressions_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `advertiser_type_id`, `impression_quantity`
- `studio.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`

### Q3 FY2026 (8) — Walt Disney

Would free ad-supported channels work as a top of funnel for paid Disney+, or as a separate product?

- `studio.demand.fact_subscriber_churn_volume`: `subscriber_churn_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `net_membership_change_quantity`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.dim_customer_type`: `customer_type_id`, `customer_type_code`, `customer_type_name`
- `studio.demand.dim_dis_segment`: `dis_segment_id`, `dis_segment_code`, `dis_segment_name`
- `studio.demand.dim_sports_league`: `sports_league_id`, `sports_league_code`, `sports_league_name`
- `studio.demand.fact_paid_memberships`: `paid_memberships_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `plan_type_id`, `region_id`, `paid_membership_quantity`, `membership_addition_quantity`

### Q2 FY2026 (3) — Walt Disney

How does domestic Disney+ engagement grow from Disney’s own content versus opening the app as a portal for other programmers?

- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.fact_streaming_engagement`: `streaming_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `content_type_id`, `device_type_id`, `hours_viewed_quantity`
- `studio.demand.fact_podcast_engagement`: `podcast_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `podcast_hour_quantity`
- `studio.demand.dim_dis_segment`: `dis_segment_id`, `dis_segment_code`, `dis_segment_name`
- `studio.demand.fact_theatrical_admissions`: `theatrical_admissions_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `region_id`, `admission_quantity`
- `studio.demand.fact_live_event_audience`: `live_event_audience_record_id`, `fiscal_quarter_id`, `scenario_id`, `sports_league_id`, `content_type_id`, `viewer_quantity`

### Q1 FY2026 (3) — Walt Disney

How will user-generated AI content be curated on Disney platforms, and could it change demand for new and library franchise programming?

- `studio.demand.fact_franchise_volume`: `franchise_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `franchise_id`, `content_type_id`, `franchise_viewing_quantity`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.fact_theatrical_admissions`: `theatrical_admissions_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `region_id`, `admission_quantity`
- `studio.supply.fact_content_library`: `content_library_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `content_origin_id`, `title_quantity`, `content_hour_quantity`
- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_content_amortization`: `content_amortization_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `content_origin_id`, `content_amortization_amount`, `content_cash_spend_amount`

### Q4 FY2025 (4) — Walt Disney

If media companies break up or combine, does Disney need to participate or face a stronger competitor?

- `studio.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `studio.demand.dim_dis_segment`: `dis_segment_id`, `dis_segment_code`, `dis_segment_name`
- `studio.demand.fact_podcast_engagement`: `podcast_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `podcast_hour_quantity`
- `studio.supply.fact_cruise_capacity`: `cruise_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `cruise_ship_id`, `berth_quantity`, `passenger_capacity_quantity`
- `studio.supply.fact_content_library`: `content_library_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `content_origin_id`, `title_quantity`, `content_hour_quantity`
- `studio.price.fact_dis_segment_revenue`: `dis_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_revenue_amount`

### Q1 2025 (4) — Netflix

What discovery tools can lift engagement across a very large library?

- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.fact_streaming_engagement`: `streaming_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `content_type_id`, `device_type_id`, `hours_viewed_quantity`
- `studio.demand.fact_podcast_engagement`: `podcast_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `podcast_hour_quantity`
- `studio.supply.fact_content_library`: `content_library_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `content_origin_id`, `title_quantity`, `content_hour_quantity`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.demand.fact_paid_memberships`: `paid_memberships_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `plan_type_id`, `region_id`, `paid_membership_quantity`, `membership_addition_quantity`
