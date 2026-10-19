# Airline Inc network demand

Capacity is available seat-miles, traffic is revenue passenger-miles, and yield and unit cost use those denominators through shared geographic, cabin, and traveler keys. A route carries an origin airport and a destination airport. Cargo and maintenance are revenue and traffic measures, SkyMiles and MileagePlus stay in separate facts, and enterprise earnings are grained at enterprise level, not at a hub. Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks.

## Numbered questions

## Delta Air Lines

### Q1 2026 (7) Delta Air Lines

What bounds back-half capacity growth, and is capacity being managed to earnings neutrality?

- `airline.supply.fact_available_seat_miles`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `route_id`, `cabin_id`, `aircraft_model_id`, `available_seat_miles`, `seat_count`, `departure_count`
- `airline.demand.fact_industry_traffic_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `competitor_id`, `industry_revenue_passenger_miles`
- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`

### Q1 2026 (11) Delta Air Lines

As corporate volume returns, can that be served without cutting basic-economy inventory?

- `airline.demand.fact_passenger_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `fare_product_id`, `passenger_count`
- `airline.demand.fact_corporate_traffic`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `industry_vertical_id`, `hub_id`, `corporate_revenue_passenger_miles`, `corporate_passenger_count`
- `airline.demand.fact_industry_traffic_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `competitor_id`, `industry_revenue_passenger_miles`

### Q1 2026 (12) Delta Air Lines

Where is corporate share still short of where it should be, by coast versus the interior?

- `airline.demand.fact_corporate_traffic`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `industry_vertical_id`, `hub_id`, `corporate_revenue_passenger_miles`, `corporate_passenger_count`
- `airline.demand.fact_share_position`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `hub_id`, `competitor_id`, `passenger_share_percent`
- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`

### Q1 2026 (16) Delta Air Lines

Is premium corporate strength a market trend or the result of Delta merchandising with corporate clients?

- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_revenue_passenger_miles`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `revenue_passenger_miles`, `passenger_count`
- `airline.demand.fact_passenger_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `fare_product_id`, `passenger_count`

### Q1 2026 (17) Delta Air Lines

How much of demand strength is customers accepting higher fares versus more bookings?

- `airline.demand.fact_revenue_passenger_miles`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `revenue_passenger_miles`, `passenger_count`
- `airline.demand.fact_passenger_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `fare_product_id`, `passenger_count`
- `airline.demand.fact_booking_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `fare_product_id`, `booking_window_id`, `booking_count`

### Q1 2026 (19) Delta Air Lines

How does brand-loyal share in focus cities compare with the coastal hubs?

- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_share_position`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `hub_id`, `competitor_id`, `passenger_share_percent`
- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`

### Q3 2025 (2) Delta Air Lines

Is corporate travel fully recovered once the prior-year disruption comparison is excluded?

- `airline.demand.fact_corporate_traffic`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `industry_vertical_id`, `hub_id`, `corporate_revenue_passenger_miles`, `corporate_passenger_count`
- `airline.demand.fact_event_traffic`: `fiscal_quarter_id`, `scenario_id`, `event_id`, `geographic_entity_id`, `event_revenue_passenger_miles`
- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`

### Q3 2025 (7) Delta Air Lines

How much premium growth is a change in loyalty-member behavior rather than oil and the consumer backdrop?

- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.supply.fact_available_seat_miles`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `route_id`, `cabin_id`, `aircraft_model_id`, `available_seat_miles`, `seat_count`, `departure_count`

### Q3 2025 (8) Delta Air Lines

What share of premium revenue is corporate?

- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_corporate_traffic`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `industry_vertical_id`, `hub_id`, `corporate_revenue_passenger_miles`, `corporate_passenger_count`
- `airline.demand.fact_industry_traffic_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `competitor_id`, `industry_revenue_passenger_miles`

### Q3 2025 (11) Delta Air Lines

Why is Austin, a non-hub, no longer dilutive the way non-hub flying used to be?

- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_share_position`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `hub_id`, `competitor_id`, `passenger_share_percent`

### Q3 2025 (15) Delta Air Lines

Is maintenance and cargo revenue strength sustainable into the fourth quarter?

- `airline.demand.fact_cargo_ton_miles`: `fiscal_quarter_id`, `scenario_id`, `cargo_type_id`, `geographic_entity_id`, `cargo_ton_miles`, `cargo_weight_tons`
- `airline.demand.fact_revenue_passenger_miles`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `revenue_passenger_miles`, `passenger_count`
- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`

### Q3 2025 (16) Delta Air Lines

How is first-quarter network planning being set given last year's close-in corporate weakness?

- `airline.supply.fact_available_seat_miles`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `route_id`, `cabin_id`, `aircraft_model_id`, `available_seat_miles`, `seat_count`, `departure_count`
- `airline.demand.fact_booking_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `fare_product_id`, `booking_window_id`, `booking_count`
- `airline.demand.fact_corporate_traffic`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `industry_vertical_id`, `hub_id`, `corporate_revenue_passenger_miles`, `corporate_passenger_count`

### Q3 2025 (17) Delta Air Lines

Does shoulder-season Transatlantic strength still hold without last year's currency tailwind?

- `airline.demand.fact_revenue_passenger_miles`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `revenue_passenger_miles`, `passenger_count`
- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`

### Q3 2025 (20) Delta Air Lines

Is the main-cabin improvement more flying or Delta taking share as industry capacity comes out?

- `airline.demand.fact_industry_traffic_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `competitor_id`, `industry_revenue_passenger_miles`
- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_corporate_traffic`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `industry_vertical_id`, `hub_id`, `corporate_revenue_passenger_miles`, `corporate_passenger_count`

### Q3 2025 (21) Delta Air Lines

Are domestic revenue trends different in hubs than in point-to-point leisure markets where competitor capacity is down?

- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_share_position`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `hub_id`, `competitor_id`, `passenger_share_percent`
- `airline.demand.fact_industry_traffic_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `competitor_id`, `industry_revenue_passenger_miles`

### Q4 2024 (4) Delta Air Lines

How do business and leisure, and older versus younger travelers, differ right now?

- `airline.demand.fact_cohort_traffic`: `fiscal_quarter_id`, `scenario_id`, `age_cohort_id`, `traveler_type_id`, `cohort_revenue_passenger_miles`
- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`

### Q3 2024 (1) Delta Air Lines

How is the election period being separated from the underlying domestic and short-haul Latin demand trend?

- `airline.demand.fact_event_traffic`: `fiscal_quarter_id`, `scenario_id`, `event_id`, `geographic_entity_id`, `event_revenue_passenger_miles`
- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_revenue_passenger_miles`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `revenue_passenger_miles`, `passenger_count`

### Q3 2024 (3) Delta Air Lines

Are the benefits of tighter industry capacity front-loaded for the airline that is not cutting?

- `airline.demand.fact_industry_traffic_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `competitor_id`, `industry_revenue_passenger_miles`
- `airline.supply.fact_available_seat_miles`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `route_id`, `cabin_id`, `aircraft_model_id`, `available_seat_miles`, `seat_count`, `departure_count`
- `airline.demand.fact_corporate_traffic`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `industry_vertical_id`, `hub_id`, `corporate_revenue_passenger_miles`, `corporate_passenger_count`

### Q3 2024 (4) Delta Air Lines

What corporate recovery is expected next year?

- `airline.demand.fact_corporate_traffic`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `industry_vertical_id`, `hub_id`, `corporate_revenue_passenger_miles`, `corporate_passenger_count`
- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`

## United Airlines

### Q1 2026 (1) United Airlines

Could a larger brand that captures passengers now flying foreign competitors include a United hub in Europe, and how do Star Alliance partners fit?

- `airline.demand.fact_share_position`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `hub_id`, `competitor_id`, `passenger_share_percent`
- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`

### Q1 2026 (3) United Airlines

In a high-fare scenario, how would premium and business traffic hold up if demand is usually inelastic?

- `airline.demand.fact_revenue_passenger_miles`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `revenue_passenger_miles`, `passenger_count`
- `airline.demand.fact_passenger_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `fare_product_id`, `passenger_count`
- `airline.demand.fact_cohort_traffic`: `fiscal_quarter_id`, `scenario_id`, `age_cohort_id`, `traveler_type_id`, `cohort_revenue_passenger_miles`

### Q1 2026 (5) United Airlines

Is there a structural share opportunity on the Atlantic or longer haul while Middle East carriers are disrupted, or will they be aggressive when they return?

- `airline.demand.fact_share_position`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `hub_id`, `competitor_id`, `passenger_share_percent`
- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_corporate_traffic`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `industry_vertical_id`, `hub_id`, `corporate_revenue_passenger_miles`, `corporate_passenger_count`

### Q1 2026 (6) United Airlines

How is brand-loyal share at Chicago O'Hare holding up versus the competitor under a proposed summer operations cap?

- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_share_position`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `hub_id`, `competitor_id`, `passenger_share_percent`
- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`

### Q4 2025 (6) United Airlines

Was most of the shutdown hit domestic revenue, so is the sequential improvement mostly domestic?

- `airline.demand.fact_event_traffic`: `fiscal_quarter_id`, `scenario_id`, `event_id`, `geographic_entity_id`, `event_revenue_passenger_miles`
- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_revenue_passenger_miles`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `revenue_passenger_miles`, `passenger_count`

### Q4 2025 (7) United Airlines

Which cost opportunities matter most next year: operation, procurement, or follow-through on this year's savings?

- `airline.demand.fact_share_position`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `hub_id`, `competitor_id`, `passenger_share_percent`
- `airline.demand.fact_industry_traffic_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `competitor_id`, `industry_revenue_passenger_miles`
- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`

### Q4 2025 (9) United Airlines

If industry revenue was flat versus the economy, what does that imply for broader industry growth?

- `airline.demand.fact_industry_traffic_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `competitor_id`, `industry_revenue_passenger_miles`
- `airline.demand.fact_corporate_traffic`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `industry_vertical_id`, `hub_id`, `corporate_revenue_passenger_miles`, `corporate_passenger_count`
- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`

### Q4 2025 (13) United Airlines

Is a World Cup demand tailwind in the outlook, and how large could it be?

- `airline.demand.fact_event_traffic`: `fiscal_quarter_id`, `scenario_id`, `event_id`, `geographic_entity_id`, `event_revenue_passenger_miles`
- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_revenue_passenger_miles`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `revenue_passenger_miles`, `passenger_count`

### Q3 2025 (4) United Airlines

Can the industry revenue relationship to the economy exceed the pre-pandemic pattern?

- `airline.demand.fact_industry_traffic_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `competitor_id`, `industry_revenue_passenger_miles`
- `airline.demand.fact_corporate_traffic`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `industry_vertical_id`, `hub_id`, `corporate_revenue_passenger_miles`, `corporate_passenger_count`
- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`

### Q3 2025 (9) United Airlines

How much of a head start do fourth-quarter bookings and advanced yields have, including the Atlantic?

- `airline.demand.fact_booking_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `fare_product_id`, `booking_window_id`, `booking_count`
- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_revenue_passenger_miles`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `revenue_passenger_miles`, `passenger_count`

### Q3 2025 (14) United Airlines

What range of outcomes from a government shutdown is already in the quarter's outlook?

- `airline.demand.fact_event_traffic`: `fiscal_quarter_id`, `scenario_id`, `event_id`, `geographic_entity_id`, `event_revenue_passenger_miles`
- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`

### Q3 2025 (15) United Airlines

As more low-end capacity exits, how does the shorter booking window at discount carriers affect brand-loyal demand?

- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_industry_traffic_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `competitor_id`, `industry_revenue_passenger_miles`
- `airline.demand.fact_share_position`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `hub_id`, `competitor_id`, `passenger_share_percent`

### Q2 2025 (2) United Airlines

Is demand back to the January level after the Newark recovery, or only on the way?

- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_revenue_passenger_miles`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `revenue_passenger_miles`, `passenger_count`
- `airline.demand.fact_passenger_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `fare_product_id`, `passenger_count`

### Q2 2025 (5) United Airlines

What would let United close the remaining gap with the competitor that has a different labor, hub, maintenance, and loyalty setup?

- `airline.demand.fact_share_position`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `hub_id`, `competitor_id`, `passenger_share_percent`
- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`

### Q2 2025 (6) United Airlines

Which geographies or industries are driving the summer corporate acceleration, and are bookings back to the prior turn-of-year level?

- `airline.demand.fact_corporate_traffic`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `industry_vertical_id`, `hub_id`, `corporate_revenue_passenger_miles`, `corporate_passenger_count`
- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_revenue_passenger_miles`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `revenue_passenger_miles`, `passenger_count`

### Q2 2025 (15) United Airlines

Is anti-tourism in some European cities changing passenger flows?

- `airline.demand.fact_loyalty_traffic_united`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_loyalty_traffic_delta`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `geographic_entity_id`, `member_revenue_passenger_miles`
- `airline.demand.fact_revenue_passenger_miles`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `revenue_passenger_miles`, `passenger_count`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `airline.time.dim_fiscal_quarter` | supporting population |
| `airline.time.dim_scenario` | supporting population |
| `airline.geography.dim_geographic_entity` | supporting population |
| `airline.geography.dim_city` | supporting population |
| `airline.geography.dim_hub` | supporting population |
| `airline.geography.dim_origin_airport` | supporting population |
| `airline.geography.dim_destination_airport` | supporting population |
| `airline.geography.dim_route` | supporting population |
| `airline.customer.dim_cabin` | supporting population |
| `airline.customer.dim_fare_product` | supporting population |
| `airline.customer.dim_traveler_type` | supporting population |
| `airline.customer.dim_industry_vertical` | supporting population |
| `airline.customer.dim_age_cohort` | supporting population |
| `airline.customer.dim_competitor` | supporting population |
| `airline.customer.dim_event` | supporting population |
| `airline.customer.dim_booking_window` | supporting population |
| `airline.supply.fact_available_seat_miles` | Q1 2026 (7), Q3 2025 (7), Q3 2025 (16), Q3 2024 (3) |
| `airline.demand.fact_revenue_passenger_miles` | Q1 2026 (16), Q1 2026 (17), Q3 2025 (15), Q3 2025 (17), Q3 2024 (1), Q1 2026 (3), Q4 2025 (6), Q4 2025 (13), Q3 2025 (9), Q2 2025 (2), Q2 2025 (6), Q2 2025 (15) |
| `airline.demand.fact_passenger_quantity` | Q1 2026 (11), Q1 2026 (16), Q1 2026 (17), Q1 2026 (3), Q2 2025 (2) |
| `airline.demand.fact_booking_quantity` | Q1 2026 (17), Q3 2025 (16), Q3 2025 (9) |
| `airline.demand.fact_corporate_traffic` | Q1 2026 (11), Q1 2026 (12), Q3 2025 (2), Q3 2025 (8), Q3 2025 (16), Q3 2025 (20), Q3 2024 (3), Q3 2024 (4), Q1 2026 (5), Q4 2025 (9), Q3 2025 (4), Q2 2025 (6) |
| `airline.demand.fact_loyalty_traffic_delta` | Q1 2026 (7), Q1 2026 (12), Q1 2026 (16), Q1 2026 (19), Q3 2025 (2), Q3 2025 (7), Q3 2025 (8), Q3 2025 (11), Q3 2025 (15), Q3 2025 (17), Q3 2025 (20), Q3 2025 (21), Q4 2024 (4), Q3 2024 (1), Q3 2024 (4), Q1 2026 (1), Q1 2026 (6), Q2 2025 (5), Q2 2025 (15) |
| `airline.demand.fact_loyalty_traffic_united` | Q1 2026 (19), Q3 2025 (7), Q1 2026 (1), Q1 2026 (5), Q1 2026 (6), Q4 2025 (6), Q4 2025 (7), Q4 2025 (9), Q4 2025 (13), Q3 2025 (4), Q3 2025 (9), Q3 2025 (14), Q3 2025 (15), Q2 2025 (2), Q2 2025 (5), Q2 2025 (6), Q2 2025 (15) |
| `airline.demand.fact_share_position` | Q1 2026 (12), Q1 2026 (19), Q3 2025 (11), Q3 2025 (21), Q1 2026 (1), Q1 2026 (5), Q1 2026 (6), Q4 2025 (7), Q3 2025 (15), Q2 2025 (5) |
| `airline.demand.fact_industry_traffic_quantity` | Q1 2026 (7), Q1 2026 (11), Q3 2025 (8), Q3 2025 (20), Q3 2025 (21), Q3 2024 (3), Q4 2025 (7), Q4 2025 (9), Q3 2025 (4), Q3 2025 (15) |
| `airline.demand.fact_event_traffic` | Q3 2025 (2), Q3 2024 (1), Q4 2025 (6), Q4 2025 (13), Q3 2025 (14) |
| `airline.demand.fact_cargo_ton_miles` | Q3 2025 (15) |
| `airline.demand.fact_cohort_traffic` | Q4 2024 (4), Q1 2026 (3) |
