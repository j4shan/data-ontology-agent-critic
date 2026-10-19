# Studio Inc price slice

This slice is part of the Studio Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q3 FY2026 (1) — Walt Disney

Several years into the long parks investment cycle, what revenue growth and margin upside should come from more park capacity and the cruise fleet, and how is price balanced against volume?

- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.supply.fact_park_project_capacity`: `park_project_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `project_vintage_id`, `added_capacity_quantity`
- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_park_capital_spending`: `park_capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `project_vintage_id`, `capital_spending_amount`

### Q3 FY2026 (2) — Walt Disney

Are returns on the earliest parks projects higher than on later spending, or do returns hold as the program scales?

- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.price.fact_park_capital_spending`: `park_capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `project_vintage_id`, `capital_spending_amount`
- `studio.demand.fact_subscriber_churn_volume`: `subscriber_churn_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `net_membership_change_quantity`
- `studio.price.fact_capital_spending_mv`: `capital_spending_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `capital_spending_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`

### Q3 FY2026 (3) — Walt Disney

Are the new U.S. park discounts meant to offset weak international visitation, or do they flag a broader attendance worry?

- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `studio.demand.fact_park_attendance`: `park_attendance_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `visitor_origin_id`, `attendance_quantity`
- `studio.demand.fact_park_visitor_spending_volume`: `park_visitor_spending_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `ticket_type_id`, `ticket_guest_quantity`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.dim_dis_segment`: `dis_segment_id`, `dis_segment_code`, `dis_segment_name`

### Q3 FY2026 (4) — Walt Disney

How are fuel costs and Middle East conflict showing up in park attendance, margins, and the Abu Dhabi project?

- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.price.fact_park_capital_spending`: `park_capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `project_vintage_id`, `capital_spending_amount`
- `studio.demand.fact_park_attendance`: `park_attendance_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `visitor_origin_id`, `attendance_quantity`
- `studio.supply.fact_park_project_capacity`: `park_project_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `project_vintage_id`, `added_capacity_quantity`
- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`

### Q3 FY2026 (5) — Walt Disney

How much of the reaffirmed earnings growth depends on content feeding parks and streaming, versus capacity in Experiences, cruise, and the streaming margin ramp?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_streaming_margin`: `streaming_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `streaming_operating_income_amount`, `streaming_margin_percent`
- `studio.demand.fact_streaming_engagement`: `streaming_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `content_type_id`, `device_type_id`, `hours_viewed_quantity`
- `studio.supply.fact_cruise_capacity`: `cruise_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `cruise_ship_id`, `berth_quantity`, `passenger_capacity_quantity`
- `studio.supply.fact_park_project_capacity`: `park_project_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `project_vintage_id`, `added_capacity_quantity`
- `studio.supply.fact_streaming_capacity`: `streaming_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `region_id`, `concurrent_stream_quantity`

### Q3 FY2026 (6) — Walt Disney

What is left in the Disney+ and Hulu integration, and will Disney+ host other entertainment services the way Hulu has with add-ons?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.price.fact_dis_segment_revenue`: `dis_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_revenue_amount`
- `studio.price.fact_streaming_revenue`: `streaming_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `revenue_type_id`, `streaming_revenue_amount`

### Q3 FY2026 (9) — Walt Disney

How do sports, the Super Bowl, and the upfront shape advertising trends across the platforms?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_advertising_revenue`: `advertising_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `advertiser_type_id`, `advertising_revenue_amount`
- `studio.price.fact_sports_revenue`: `sports_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `sports_league_id`, `linear_network_id`, `sports_revenue_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.dim_dis_segment`: `dis_segment_id`, `dis_segment_code`, `dis_segment_name`

### Q3 FY2026 (10) — Walt Disney

Where has technology investment already made the company faster, and where is the next upside?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`

### Q3 FY2026 (11) — Walt Disney

How is success defined for the TikTok arrangement inside the Disney+ strategy?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.dim_dis_segment`: `dis_segment_id`, `dis_segment_code`, `dis_segment_name`
- `studio.price.fact_dis_segment_revenue`: `dis_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_revenue_amount`
- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`

### Q3 FY2026 (12) — Walt Disney

How much of Walt Disney World growth is new investment versus a rebound after Epic’s opening, and what supports continued returns?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.dim_dis_segment`: `dis_segment_id`, `dis_segment_code`, `dis_segment_name`
- `studio.price.fact_dis_segment_revenue`: `dis_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_revenue_amount`
- `studio.price.fact_streaming_revenue`: `streaming_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `revenue_type_id`, `streaming_revenue_amount`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`

### Q3 FY2026 (13) — Walt Disney

Is the higher Experiences profit outlook core outperformance or tariff refunds?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.fact_subscriber_churn_volume`: `subscriber_churn_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `net_membership_change_quantity`
- `studio.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `studio.demand.dim_dis_segment`: `dis_segment_id`, `dis_segment_code`, `dis_segment_name`
- `studio.demand.dim_content_origin`: `content_origin_id`, `content_origin_code`, `content_origin_name`

### Q2 FY2026 (1) — Walt Disney

What are the three main priorities, and where can one business reuse what another has learned?

- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `studio.demand.dim_dis_segment`: `dis_segment_id`, `dis_segment_code`, `dis_segment_name`
- `studio.price.fact_dis_segment_revenue`: `dis_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_revenue_amount`

### Q2 FY2026 (4) — Walt Disney

Does a “digital centerpiece” mean less third-party licensing, and how is reach on other platforms traded against Disney+ exclusivity?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.dim_dis_segment`: `dis_segment_id`, `dis_segment_code`, `dis_segment_name`
- `studio.price.fact_dis_segment_revenue`: `dis_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_revenue_amount`
- `studio.price.fact_streaming_revenue`: `streaming_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `revenue_type_id`, `streaming_revenue_amount`

### Q2 FY2026 (5) — Walt Disney

Are international-visitation and Epic-related headwinds at U.S. parks getting better or worse quarter to quarter?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_park_capital_spending`: `park_capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `project_vintage_id`, `capital_spending_amount`
- `studio.price.fact_marketing_expense`: `marketing_expense_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cost_bucket_id`, `marketing_expense_amount`
- `studio.demand.fact_podcast_engagement`: `podcast_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `podcast_hour_quantity`
- `studio.supply.fact_cruise_capacity`: `cruise_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `cruise_ship_id`, `berth_quantity`, `passenger_capacity_quantity`

### Q2 FY2026 (6) — Walt Disney

Has higher fuel cost changed behavior at domestic or international parks, and does that threaten the earnings-growth outlook?

- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_operating_expense_mv`: `operating_expense_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cost_bucket_id`, `operating_expense_amount`
- `studio.price.fact_marketing_expense`: `marketing_expense_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cost_bucket_id`, `marketing_expense_amount`
- `studio.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`

### Q2 FY2026 (7) — Walt Disney

What has World of Frozen in Paris shown, and when should the capital program lift attendance?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.price.fact_park_capital_spending`: `park_capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `project_vintage_id`, `capital_spending_amount`
- `studio.price.fact_capital_spending_mv`: `capital_spending_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `capital_spending_amount`
- `studio.demand.fact_park_attendance`: `park_attendance_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `visitor_origin_id`, `attendance_quantity`

### Q2 FY2026 (8) — Walt Disney

How will original franchises from Pixar and Marvel be rebuilt now that content sits under one leader?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_content_amortization`: `content_amortization_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `content_origin_id`, `content_amortization_amount`, `content_cash_spend_amount`
- `studio.price.fact_content_revenue`: `content_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `distribution_window_id`, `content_revenue_amount`
- `studio.price.fact_marketing_expense`: `marketing_expense_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cost_bucket_id`, `marketing_expense_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`

### Q2 FY2026 (9) — Walt Disney

Is there a shift toward short-form and user-generated content, and how would Disney participate?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_content_amortization`: `content_amortization_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `content_origin_id`, `content_amortization_amount`, `content_cash_spend_amount`
- `studio.price.fact_content_revenue`: `content_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `distribution_window_id`, `content_revenue_amount`
- `studio.price.fact_marketing_expense`: `marketing_expense_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cost_bucket_id`, `marketing_expense_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.dim_dis_segment`: `dis_segment_id`, `dis_segment_code`, `dis_segment_name`

### Q2 FY2026 (10) — Walt Disney

With NFL rights running through 2030, is it better to reopen talks now or wait for the opt-out?

- `studio.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `studio.demand.dim_sports_league`: `sports_league_id`, `sports_league_code`, `sports_league_name`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.fact_subscriber_churn_volume`: `subscriber_churn_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `net_membership_change_quantity`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 FY2026 (11) — Walt Disney

Where is generative AI already cutting cost or speeding revenue, and what is next?

- `studio.price.fact_dis_segment_revenue`: `dis_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_revenue_amount`
- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_streaming_revenue`: `streaming_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `revenue_type_id`, `streaming_revenue_amount`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_advertising_revenue`: `advertising_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `advertiser_type_id`, `advertising_revenue_amount`

### Q2 FY2026 (12) — Walt Disney

Is the higher sports profit outlook entirely the NFL Network transaction, and what else beat in the quarter?

- `studio.price.fact_sports_revenue`: `sports_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `sports_league_id`, `linear_network_id`, `sports_revenue_amount`
- `studio.supply.fact_sports_rights_capacity`: `sports_rights_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `sports_league_id`, `linear_network_id`, `live_event_quantity`
- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`

### Q1 FY2026 (1) — Walt Disney

How did Walt Disney World do inside the domestic parks improvement, and what do bookings say about demand from here?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_park_capital_spending`: `park_capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `project_vintage_id`, `capital_spending_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.dim_dis_segment`: `dis_segment_id`, `dis_segment_code`, `dis_segment_name`
- `studio.demand.fact_cruise_passengers`: `cruise_passengers_record_id`, `fiscal_quarter_id`, `scenario_id`, `cruise_ship_id`, `passenger_quantity`

### Q1 FY2026 (2) — Walt Disney

Is ESPN Unlimited uptake coming more from bundles or from authenticated TV, and what are the next Hulu integration steps?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.fact_subscriber_churn_volume`: `subscriber_churn_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `net_membership_change_quantity`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 FY2026 (4) — Walt Disney

How much is streaming investment still a profit drag, and how much operating leverage comes out next year?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_streaming_margin`: `streaming_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `streaming_operating_income_amount`, `streaming_margin_percent`
- `studio.price.fact_streaming_revenue`: `streaming_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `revenue_type_id`, `streaming_revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_advertising_revenue`: `advertising_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `advertiser_type_id`, `advertising_revenue_amount`
- `studio.price.fact_cruise_operating_rate`: `cruise_operating_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `cruise_ship_id`, `cruise_operating_income_amount`

### Q1 FY2026 (5) — Walt Disney

When does user-generated video appear on Disney+, does it stay short-form, and is the bookings increase international visitation or something else?

- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.demand.fact_subscriber_churn_volume`: `subscriber_churn_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `net_membership_change_quantity`

### Q4 FY2025 (1) — Walt Disney

What has early ESPN direct-to-consumer adoption and package choice shown, and does it change the sports outlook?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_sports_revenue`: `sports_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `sports_league_id`, `linear_network_id`, `sports_revenue_amount`
- `studio.price.fact_espn_revenue`: `espn_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `sports_league_id`, `revenue_type_id`, `espn_revenue_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`

### Q4 FY2025 (2) — Walt Disney

What studio growth is realistic this year with a large slate after a softer start implied in the first-quarter outlook?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.price.fact_cruise_operating_rate`: `cruise_operating_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `cruise_ship_id`, `cruise_operating_income_amount`
- `studio.supply.fact_production_slate`: `production_slate_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `distribution_window_id`, `slate_title_quantity`
- `studio.price.fact_dis_segment_revenue`: `dis_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_revenue_amount`
- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`

### Q4 FY2025 (3) — Walt Disney

How does Disney+ become a way into Hulu, ESPN, parks, and other assets, and can engagement plus advertising sustain double-digit streaming revenue growth?

- `studio.price.fact_advertising_revenue`: `advertising_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `advertiser_type_id`, `advertising_revenue_amount`
- `studio.price.fact_streaming_revenue`: `streaming_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `revenue_type_id`, `streaming_revenue_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.fact_streaming_engagement`: `streaming_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `content_type_id`, `device_type_id`, `hours_viewed_quantity`
- `studio.price.fact_dis_segment_revenue`: `dis_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_revenue_amount`
- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`

### Q4 FY2025 (5) — Walt Disney

Inside the high-single-digit Experiences profit outlook, how is demand trending and how much of the growth is revenue versus margin?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.price.fact_dis_segment_revenue`: `dis_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_revenue_amount`
- `studio.price.fact_streaming_revenue`: `streaming_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `revenue_type_id`, `streaming_revenue_amount`

### Q4 FY2025 (6) — Walt Disney

Could Disney bundle a wider set of streamers, and how does bundling ESPN affect Disney+ and Hulu?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.dim_dis_segment`: `dis_segment_id`, `dis_segment_code`, `dis_segment_name`
- `studio.price.fact_dis_segment_revenue`: `dis_segment_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_revenue_amount`
- `studio.price.fact_streaming_revenue`: `streaming_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `revenue_type_id`, `streaming_revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`

### Q4 FY2025 (7) — Walt Disney

Was lighter domestic park attendance competition or the macro environment, and how do cruise demand and cruise margins compare with the parks?

- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.price.fact_park_capital_spending`: `park_capital_spending_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `project_vintage_id`, `capital_spending_amount`
- `studio.demand.fact_park_attendance`: `park_attendance_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `visitor_origin_id`, `attendance_quantity`
- `studio.demand.fact_cruise_passengers`: `cruise_passengers_record_id`, `fiscal_quarter_id`, `scenario_id`, `cruise_ship_id`, `passenger_quantity`
- `studio.supply.fact_cruise_capacity`: `cruise_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `cruise_ship_id`, `berth_quantity`, `passenger_capacity_quantity`
- `studio.supply.fact_park_project_capacity`: `park_project_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `project_vintage_id`, `added_capacity_quantity`

### Q4 FY2025 (8) — Walt Disney

What are the 2026 streaming cost pushes and offsets, including savings from combining technology stacks?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_streaming_revenue`: `streaming_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `revenue_type_id`, `streaming_revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_advertising_revenue`: `advertising_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `advertiser_type_id`, `advertising_revenue_amount`
- `studio.price.fact_operating_expense_mv`: `operating_expense_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cost_bucket_id`, `operating_expense_amount`
- `studio.price.fact_streaming_margin`: `streaming_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `streaming_operating_income_amount`, `streaming_margin_percent`

### Q4 FY2025 (9) — Walt Disney

Is there an opportunity or risk in licensing IP to new video-creation platforms, and can generative AI lower production cost?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.demand.fact_subscriber_churn_volume`: `subscriber_churn_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `net_membership_change_quantity`
- `studio.price.fact_marketing_expense`: `marketing_expense_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cost_bucket_id`, `marketing_expense_amount`
- `studio.demand.fact_podcast_engagement`: `podcast_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `podcast_hour_quantity`
- `studio.supply.fact_cruise_capacity`: `cruise_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `cruise_ship_id`, `berth_quantity`, `passenger_capacity_quantity`
- `studio.supply.fact_content_library`: `content_library_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `content_origin_id`, `title_quantity`, `content_hour_quantity`

### Q1 2026 (1) — Netflix

How is the primary engagement-quality metric trending in 2026 after an all-time high in 2025?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.fact_streaming_engagement`: `streaming_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `content_type_id`, `device_type_id`, `hours_viewed_quantity`
- `studio.demand.fact_podcast_engagement`: `podcast_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `podcast_hour_quantity`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_enterprise_margin_mv`: `enterprise_margin_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`

### Q1 2026 (2) — Netflix

Is live-event spending, such as an NFL package, judged on the same return as scripted series, or does it raise ad prices and ad growth in a way one-off shows do not?

- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.demand.fact_subscriber_churn_volume`: `subscriber_churn_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `net_membership_change_quantity`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.fact_live_event_audience`: `live_event_audience_record_id`, `fiscal_quarter_id`, `scenario_id`, `sports_league_id`, `content_type_id`, `viewer_quantity`
- `studio.supply.fact_sports_rights_capacity`: `sports_rights_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `sports_league_id`, `linear_network_id`, `live_event_quantity`

### Q1 2026 (3) — Netflix

What is the podcast business model, and how is early engagement shown to be incremental to the rest of the service?

- `studio.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.fact_streaming_engagement`: `streaming_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `content_type_id`, `device_type_id`, `hours_viewed_quantity`
- `studio.demand.fact_podcast_engagement`: `podcast_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `podcast_hour_quantity`
- `studio.price.fact_streaming_revenue`: `streaming_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `revenue_type_id`, `streaming_revenue_amount`

### Q1 2026 (4) — Netflix

How fast is the total advertiser base growing?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.fact_advertiser_demand`: `advertiser_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `advertiser_type_id`, `streaming_service_id`, `advertiser_quantity`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_enterprise_margin_mv`: `enterprise_margin_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `studio.price.fact_advertising_revenue`: `advertising_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `advertiser_type_id`, `advertising_revenue_amount`

### Q1 2026 (5) — Netflix

How does the competitive landscape for content look entering 2026?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.fact_streaming_engagement`: `streaming_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `content_type_id`, `device_type_id`, `hours_viewed_quantity`
- `studio.demand.fact_theatrical_admissions`: `theatrical_admissions_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `region_id`, `admission_quantity`
- `studio.demand.fact_live_event_audience`: `live_event_audience_record_id`, `fiscal_quarter_id`, `scenario_id`, `sports_league_id`, `content_type_id`, `viewer_quantity`
- `studio.demand.fact_podcast_engagement`: `podcast_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `podcast_hour_quantity`

### Q4 2025 (2) — Netflix

How does the film strategy change with a global pay-one window from Sony and a pending Warner deal?

- `studio.price.fact_content_revenue`: `content_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `distribution_window_id`, `content_revenue_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.supply.fact_production_slate`: `production_slate_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `distribution_window_id`, `slate_title_quantity`
- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`

### Q4 2025 (4) — Netflix

Which kinds of podcasts are expected to work on the service?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `studio.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `studio.demand.fact_paid_memberships`: `paid_memberships_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `plan_type_id`, `region_id`, `paid_membership_quantity`, `membership_addition_quantity`
- `studio.demand.fact_streaming_engagement`: `streaming_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `content_type_id`, `device_type_id`, `hours_viewed_quantity`

### Q4 2025 (5) — Netflix

How far along is the games offering after the 2025 product changes?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_enterprise_margin_mv`: `enterprise_margin_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `studio.price.fact_operating_expense_mv`: `operating_expense_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cost_bucket_id`, `operating_expense_amount`
- `studio.price.fact_free_cash_flow_mv`: `free_cash_flow_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `free_cash_flow_amount`

### Q4 2025 (6) — Netflix

Why is vertical video not a higher priority?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_cruise_operating_rate`: `cruise_operating_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `cruise_ship_id`, `cruise_operating_income_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.fact_subscriber_churn_volume`: `subscriber_churn_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `net_membership_change_quantity`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.dim_content_origin`: `content_origin_id`, `content_origin_code`, `content_origin_name`

### Q2 2025 (1) — Netflix

After currency lifted the revenue outlook, what in constant currency improved — underlying revenue or items such as content amortization?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.demand.fact_podcast_engagement`: `podcast_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `podcast_hour_quantity`
- `studio.supply.fact_content_library`: `content_library_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `content_origin_id`, `title_quantity`, `content_hour_quantity`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_content_amortization`: `content_amortization_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `content_origin_id`, `content_amortization_amount`, `content_cash_spend_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`

### Q2 2025 (2) — Netflix

Why is the full-year operating-margin outlook still about 30% after the year-to-date upside and a higher third-quarter margin?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_enterprise_margin_mv`: `enterprise_margin_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `studio.price.fact_streaming_margin`: `streaming_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `streaming_operating_income_amount`, `streaming_margin_percent`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (3) — Netflix

How has the view of the consumer and the macro economy changed over the prior 90 days?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_streaming_revenue`: `streaming_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `revenue_type_id`, `streaming_revenue_amount`
- `studio.price.fact_enterprise_margin_mv`: `enterprise_margin_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`

### Q2 2025 (4) — Netflix

With a heavy back-half slate, is the business hit-driven even if no title is more than about 1% of viewing, and can original and licensed momentum continue into 2026?

- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_content_amortization`: `content_amortization_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `content_origin_id`, `content_amortization_amount`, `content_cash_spend_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.dim_content_origin`: `content_origin_id`, `content_origin_code`, `content_origin_name`
- `studio.supply.fact_production_slate`: `production_slate_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `distribution_window_id`, `slate_title_quantity`

### Q2 2025 (5) — Netflix

Is domestic viewing-share stagnation a concern?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.demand.fact_linear_viewing`: `linear_viewing_record_id`, `fiscal_quarter_id`, `scenario_id`, `linear_network_id`, `linear_hours_quantity`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.fact_franchise_volume`: `franchise_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `franchise_id`, `content_type_id`, `franchise_viewing_quantity`
- `studio.demand.fact_content_hours_by_language`: `content_hours_by_language_record_id`, `fiscal_quarter_id`, `scenario_id`, `language_market_id`, `streaming_service_id`, `language_hours_quantity`
- `studio.demand.fact_subscriber_churn_volume`: `subscriber_churn_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `net_membership_change_quantity`

### Q2 2025 (6) — Netflix

Is there an opening to bring notable YouTube creators and their content exclusively to Netflix?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_content_amortization`: `content_amortization_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `content_origin_id`, `content_amortization_amount`, `content_cash_spend_amount`
- `studio.price.fact_content_revenue`: `content_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `distribution_window_id`, `content_revenue_amount`
- `studio.price.fact_marketing_expense`: `marketing_expense_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cost_bucket_id`, `marketing_expense_amount`
- `studio.demand.dim_content_origin`: `content_origin_id`, `content_origin_code`, `content_origin_name`
- `studio.demand.fact_streaming_engagement`: `streaming_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `content_type_id`, `device_type_id`, `hours_viewed_quantity`

### Q2 2025 (7) — Netflix

What are the generative-AI initiatives in production and the product?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.supply.fact_production_slate`: `production_slate_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `distribution_window_id`, `slate_title_quantity`
- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_streaming_revenue`: `streaming_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `revenue_type_id`, `streaming_revenue_amount`
- `studio.price.fact_enterprise_margin_mv`: `enterprise_margin_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`

### Q2 2025 (8) — Netflix

What near-term monetization exists in games, including partnerships such as Grand Theft Auto and Roblox?

- `studio.price.fact_dis_segment_margin`: `dis_segment_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `dis_segment_id`, `segment_operating_income_amount`, `segment_margin_percent`
- `studio.price.fact_streaming_revenue`: `streaming_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `revenue_type_id`, `streaming_revenue_amount`
- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_advertising_revenue`: `advertising_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `advertiser_type_id`, `advertising_revenue_amount`
- `studio.price.fact_content_amortization`: `content_amortization_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `content_origin_id`, `content_amortization_amount`, `content_cash_spend_amount`

### Q1 2025 (1) — Netflix

If the internal ambition is to double revenue and triple operating income by 2030, how much more content spending does that require over five years?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.price.fact_content_revenue`: `content_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `content_type_id`, `distribution_window_id`, `content_revenue_amount`
- `studio.price.fact_cruise_operating_rate`: `cruise_operating_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `cruise_ship_id`, `cruise_operating_income_amount`
- `studio.price.fact_streaming_margin`: `streaming_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `streaming_operating_income_amount`, `streaming_margin_percent`

### Q1 2025 (2) — Netflix

How is member retention trending after a strong quarter of paid net adds?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.demand.fact_subscriber_churn_volume`: `subscriber_churn_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `net_membership_change_quantity`
- `studio.demand.fact_paid_memberships`: `paid_memberships_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `plan_type_id`, `region_id`, `paid_membership_quantity`, `membership_addition_quantity`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.price.fact_cruise_operating_rate`: `cruise_operating_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `cruise_ship_id`, `cruise_operating_income_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2025 (3) — Netflix

Could video podcasts work as a category on the service?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `studio.demand.fact_paid_memberships`: `paid_memberships_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `plan_type_id`, `region_id`, `paid_membership_quantity`, `membership_addition_quantity`
- `studio.demand.fact_streaming_engagement`: `streaming_engagement_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `content_type_id`, `device_type_id`, `hours_viewed_quantity`
- `studio.demand.fact_advertiser_demand`: `advertiser_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `advertiser_type_id`, `streaming_service_id`, `advertiser_quantity`

### Q1 2025 (5) — Netflix

Which types of games have resonated so far on the path toward broader appeal?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_enterprise_margin_mv`: `enterprise_margin_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `studio.price.fact_operating_expense_mv`: `operating_expense_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `cost_bucket_id`, `operating_expense_amount`
- `studio.price.fact_free_cash_flow_mv`: `free_cash_flow_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `free_cash_flow_amount`

### Q1 2025 (6) — Netflix

What is driving the expected reacceleration of U.S. and Canada revenue in the second quarter?

- `studio.price.fact_netflix_revenue`: `netflix_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `plan_type_id`, `region_id`, `revenue_amount`
- `studio.price.fact_enterprise_revenue_mv`: `enterprise_revenue_mv_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_amount`, `operating_income_amount`
- `studio.price.fact_park_revenue_rate`: `park_revenue_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `park_location_id`, `revenue_per_guest_amount`, `spending_per_guest_amount`
- `studio.price.fact_streaming_revenue`: `streaming_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `revenue_type_id`, `streaming_revenue_amount`
- `studio.price.fact_advertising_revenue`: `advertising_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `streaming_service_id`, `advertiser_type_id`, `advertising_revenue_amount`
- `studio.price.fact_sports_revenue`: `sports_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `sports_league_id`, `linear_network_id`, `sports_revenue_amount`
