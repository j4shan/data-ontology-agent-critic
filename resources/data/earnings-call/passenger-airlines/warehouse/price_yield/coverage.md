# Airline Inc price, yield, loyalty, cargo, and maintenance revenue

Capacity is available seat-miles, traffic is revenue passenger-miles, and yield and unit cost use those denominators through shared geographic, cabin, and traveler keys. A route carries an origin airport and a destination airport. Cargo and maintenance are revenue and traffic measures, SkyMiles and MileagePlus stay in separate facts, and enterprise earnings are grained at enterprise level, not at a hub. Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks.

## Numbered questions

## Delta Air Lines

### Q1 2026 (1) Delta Air Lines

Does the mid-teens revenue outlook reflect bookings already on the books, or an assumption that higher fares and bag fees accelerate later in the quarter?

- `airline.price.fact_ancillary_revenue`: `fiscal_quarter_id`, `scenario_id`, `fee_type_id`, `geographic_entity_id`, `ancillary_revenue_amount`
- `airline.price.fact_fare_price`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `fare_product_id`, `average_fare_dollars_per_passenger`
- `airline.price.fact_baggage_quantity`: `fiscal_quarter_id`, `scenario_id`, `fee_type_id`, `geographic_entity_id`, `checked_bag_count`

### Q1 2026 (2) Delta Air Lines

How does second-quarter unit revenue differ across the four geographic entities in demand and in the ability to pass through higher costs?

- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `revenue_cents_per_seat_mile`, `unit_revenue_change_percent`
- `airline.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `airline.price.fact_skymiles_economics`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `delta_card_program_id`, `loyalty_revenue_amount`, `cobrand_spend_amount`

### Q1 2026 (3) Delta Air Lines

Where has demand been more elastic to higher fares, by geography, customer, or cabin?

- `airline.price.fact_yield`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `yield_cents_per_passenger_mile`, `yield_change_percent`
- `airline.price.fact_fare_price`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `fare_product_id`, `average_fare_dollars_per_passenger`
- `airline.price.fact_passenger_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `passenger_revenue_amount`

### Q1 2026 (4) Delta Air Lines

How are international margins and the premium-versus-main mix inside international expected to evolve?

- `airline.price.fact_cabin_margin`: `fiscal_quarter_id`, `scenario_id`, `cabin_id`, `geographic_entity_id`, `cabin_margin_percent`, `cabin_profit_amount`
- `airline.price.fact_passenger_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `passenger_revenue_amount`
- `airline.price.fact_geographic_margin`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `geographic_margin_percent`, `geographic_profit_amount`

### Q1 2026 (5) Delta Air Lines

Where does further segmentation of the premium cabin stand, and what gates a launch?

- `airline.price.fact_passenger_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `passenger_revenue_amount`
- `airline.price.fact_yield`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `yield_cents_per_passenger_mile`, `yield_change_percent`
- `airline.price.fact_cabin_margin`: `fiscal_quarter_id`, `scenario_id`, `cabin_id`, `geographic_entity_id`, `cabin_margin_percent`, `cabin_profit_amount`

### Q1 2026 (9) Delta Air Lines

Is Pacific yield, excluding China, improving as long-haul flows avoid the Middle East, including close-in premium?

- `airline.price.fact_yield`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `yield_cents_per_passenger_mile`, `yield_change_percent`
- `airline.price.fact_passenger_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `passenger_revenue_amount`
- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `revenue_cents_per_seat_mile`, `unit_revenue_change_percent`

### Q1 2026 (10) Delta Air Lines

What is driving maintenance-revenue growth, and how much of Delta's own engine work is done in-house?

- `airline.price.fact_maintenance_revenue`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `maintenance_revenue_amount`
- `airline.price.fact_skymiles_economics`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `delta_card_program_id`, `loyalty_revenue_amount`, `cobrand_spend_amount`
- `airline.price.fact_passenger_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `passenger_revenue_amount`

### Q1 2026 (13) Delta Air Lines

Does fuel recapture keep accelerating in the back half if fuel stays high?

- `airline.price.fact_fuel_recapture_rate`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_recapture_percent`
- `airline.price.fact_skymiles_economics`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `delta_card_program_id`, `loyalty_revenue_amount`, `cobrand_spend_amount`
- `airline.price.fact_skymiles_miles_quantity`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `miles_earned_count`, `miles_redeemed_count`

### Q1 2026 (15) Delta Air Lines

What is different about demand holding up despite higher fares versus last year's macro and geopolitical shock?

- `airline.price.fact_fare_price`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `fare_product_id`, `average_fare_dollars_per_passenger`
- `airline.price.fact_yield`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `yield_cents_per_passenger_mile`, `yield_change_percent`
- `airline.price.fact_route_margin`: `fiscal_quarter_id`, `scenario_id`, `route_id`, `geographic_entity_id`, `route_margin_percent`

### Q1 2026 (18) Delta Air Lines

Where do international share opportunities sit as fuel rises, and were domestic and international price increases different?

- `airline.price.fact_fare_price`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `fare_product_id`, `average_fare_dollars_per_passenger`
- `airline.price.fact_geographic_margin`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `geographic_margin_percent`, `geographic_profit_amount`
- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `revenue_cents_per_seat_mile`, `unit_revenue_change_percent`

### Q3 2025 (1) Delta Air Lines

How much of the cash-flow improvement is the booking curve normalizing?

- `airline.price.fact_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `working_capital_amount`
- `airline.price.fact_air_traffic_liability`: `fiscal_quarter_id`, `scenario_id`, `air_traffic_liability_amount`
- `airline.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`

### Q3 2025 (3) Delta Air Lines

How much of the domestic improvement is unique to higher-income exposure?

- `airline.price.fact_fare_price`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `fare_product_id`, `average_fare_dollars_per_passenger`
- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `revenue_cents_per_seat_mile`, `unit_revenue_change_percent`
- `airline.price.fact_geographic_margin`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `geographic_margin_percent`, `geographic_profit_amount`

### Q3 2025 (6) Delta Air Lines

By how much are domestic main-cabin seats down, and how does that relate to main cabin turning positive?

- `airline.price.fact_passenger_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `passenger_revenue_amount`
- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `revenue_cents_per_seat_mile`, `unit_revenue_change_percent`
- `airline.price.fact_cabin_margin`: `fiscal_quarter_id`, `scenario_id`, `cabin_id`, `geographic_entity_id`, `cabin_margin_percent`, `cabin_profit_amount`

### Q3 2025 (9) Delta Air Lines

Why would premium overtaking the main cabin slip past next year if 2027 was the prior marker?

- `airline.price.fact_passenger_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `passenger_revenue_amount`
- `airline.price.fact_cabin_margin`: `fiscal_quarter_id`, `scenario_id`, `cabin_id`, `geographic_entity_id`, `cabin_margin_percent`, `cabin_profit_amount`
- `airline.price.fact_yield`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `yield_cents_per_passenger_mile`, `yield_change_percent`

### Q3 2025 (10) Delta Air Lines

What did Atlantic unit revenue do through the quarter, and what is required to get back to flat?

- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `revenue_cents_per_seat_mile`, `unit_revenue_change_percent`
- `airline.price.fact_skymiles_economics`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `delta_card_program_id`, `loyalty_revenue_amount`, `cobrand_spend_amount`
- `airline.price.fact_passenger_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `passenger_revenue_amount`

### Q3 2025 (14) Delta Air Lines

Is a fourth quarter matching third-quarter earnings a new seasonality, or did the third quarter under-earn?

- `airline.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `airline.price.fact_route_margin`: `fiscal_quarter_id`, `scenario_id`, `route_id`, `geographic_entity_id`, `route_margin_percent`
- `airline.price.fact_skymiles_economics`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `delta_card_program_id`, `loyalty_revenue_amount`, `cobrand_spend_amount`

### Q3 2025 (18) Delta Air Lines

What margin improvement into next year is in the company's control?

- `airline.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `airline.price.fact_cabin_margin`: `fiscal_quarter_id`, `scenario_id`, `cabin_id`, `geographic_entity_id`, `cabin_margin_percent`, `cabin_profit_amount`
- `airline.price.fact_geographic_margin`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `geographic_margin_percent`, `geographic_profit_amount`

### Q3 2025 (19) Delta Air Lines

How sustainable is co-brand spend growth?

- `airline.price.fact_skymiles_economics`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `delta_card_program_id`, `loyalty_revenue_amount`, `cobrand_spend_amount`
- `airline.price.fact_maintenance_revenue`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `maintenance_revenue_amount`
- `airline.price.fact_mileageplus_economics`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `united_card_program_id`, `loyalty_revenue_amount`, `cobrand_spend_amount`

### Q4 2024 (1) Delta Air Lines

Which geographic entity improved the most versus the initial fourth-quarter expectation, and how does that change 2025 capacity allocation?

- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `revenue_cents_per_seat_mile`, `unit_revenue_change_percent`
- `airline.price.fact_yield`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `yield_cents_per_passenger_mile`, `yield_change_percent`
- `airline.price.fact_geographic_margin`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `geographic_margin_percent`, `geographic_profit_amount`

### Q4 2024 (2) Delta Air Lines

How is SkyMiles monetized through the new partnerships?

- `airline.price.fact_skymiles_economics`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `delta_card_program_id`, `loyalty_revenue_amount`, `cobrand_spend_amount`
- `airline.price.fact_skymiles_miles_quantity`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `miles_earned_count`, `miles_redeemed_count`
- `airline.price.fact_route_margin`: `fiscal_quarter_id`, `scenario_id`, `route_id`, `geographic_entity_id`, `route_margin_percent`

### Q4 2024 (3) Delta Air Lines

With difficult comparisons, including last year's competitor grounding, should unit revenue accelerate into the spring?

- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `revenue_cents_per_seat_mile`, `unit_revenue_change_percent`
- `airline.price.fact_ancillary_revenue`: `fiscal_quarter_id`, `scenario_id`, `fee_type_id`, `geographic_entity_id`, `ancillary_revenue_amount`
- `airline.price.fact_skymiles_economics`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `delta_card_program_id`, `loyalty_revenue_amount`, `cobrand_spend_amount`

### Q4 2024 (5) Delta Air Lines

How quickly can higher fuel be recaptured compared with the historical lag?

- `airline.price.fact_fuel_recapture_rate`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_recapture_percent`
- `airline.price.fact_fare_price`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `fare_product_id`, `average_fare_dollars_per_passenger`
- `airline.price.fact_skymiles_economics`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `delta_card_program_id`, `loyalty_revenue_amount`, `cobrand_spend_amount`

### Q3 2024 (5) Delta Air Lines

How deep can the revenue premium versus domestic leisure carriers go as those carriers change product and network?

- `airline.price.fact_yield`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `yield_cents_per_passenger_mile`, `yield_change_percent`
- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `revenue_cents_per_seat_mile`, `unit_revenue_change_percent`
- `airline.price.fact_passenger_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `passenger_revenue_amount`

## United Airlines

### Q1 2026 (2) United Airlines

If fuel stays high for a long time, how does that change which hubs are run for system profit, including versus competitors?

- `airline.price.fact_fuel_recapture_rate`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_recapture_percent`
- `airline.price.fact_geographic_margin`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `geographic_margin_percent`, `geographic_profit_amount`
- `airline.price.fact_yield`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `yield_cents_per_passenger_mile`, `yield_change_percent`

### Q4 2025 (1) United Airlines

What would turn the main cabin positive, and is a specific rate of change assumed?

- `airline.price.fact_passenger_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `passenger_revenue_amount`
- `airline.price.fact_yield`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `yield_cents_per_passenger_mile`, `yield_change_percent`
- `airline.price.fact_cabin_margin`: `fiscal_quarter_id`, `scenario_id`, `cabin_id`, `geographic_entity_id`, `cabin_margin_percent`, `cabin_profit_amount`

### Q4 2025 (2) United Airlines

If card-program rules change, what can be done around the loyalty economics over the next couple of years?

- `airline.price.fact_mileageplus_economics`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `united_card_program_id`, `loyalty_revenue_amount`, `cobrand_spend_amount`
- `airline.price.fact_skymiles_economics`: `fiscal_quarter_id`, `scenario_id`, `skymiles_tier_id`, `delta_card_program_id`, `loyalty_revenue_amount`, `cobrand_spend_amount`
- `airline.price.fact_yield`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `yield_cents_per_passenger_mile`, `yield_change_percent`

### Q4 2025 (3) United Airlines

What near-term program enhancements are possible on top of the existing card agreements?

- `airline.price.fact_mileageplus_economics`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `united_card_program_id`, `loyalty_revenue_amount`, `cobrand_spend_amount`
- `airline.price.fact_geographic_margin`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `geographic_margin_percent`, `geographic_profit_amount`
- `airline.price.fact_mileageplus_miles_quantity`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `miles_earned_count`, `miles_redeemed_count`

### Q4 2025 (8) United Airlines

Are recent international routes still opening at a margin premium to their geography, and how long does that last?

- `airline.price.fact_route_margin`: `fiscal_quarter_id`, `scenario_id`, `route_id`, `geographic_entity_id`, `route_margin_percent`
- `airline.price.fact_geographic_margin`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `geographic_margin_percent`, `geographic_profit_amount`
- `airline.price.fact_cabin_margin`: `fiscal_quarter_id`, `scenario_id`, `cabin_id`, `geographic_entity_id`, `cabin_margin_percent`, `cabin_profit_amount`

### Q4 2025 (11) United Airlines

How should price and cost deliver about a point of annual margin improvement given the comparison?

- `airline.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `airline.price.fact_cabin_margin`: `fiscal_quarter_id`, `scenario_id`, `cabin_id`, `geographic_entity_id`, `cabin_margin_percent`, `cabin_profit_amount`
- `airline.price.fact_geographic_margin`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `geographic_margin_percent`, `geographic_profit_amount`

### Q3 2025 (1) United Airlines

If main-cabin supply were cut in a step, would main-cabin margins close the gap with premium?

- `airline.price.fact_cabin_margin`: `fiscal_quarter_id`, `scenario_id`, `cabin_id`, `geographic_entity_id`, `cabin_margin_percent`, `cabin_profit_amount`
- `airline.price.fact_passenger_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `passenger_revenue_amount`
- `airline.price.fact_yield`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `yield_cents_per_passenger_mile`, `yield_change_percent`

### Q3 2025 (3) United Airlines

How widespread is premium leisure yield exceeding some corporate yields, and is that a lasting change?

- `airline.price.fact_yield`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `yield_cents_per_passenger_mile`, `yield_change_percent`
- `airline.price.fact_passenger_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `passenger_revenue_amount`
- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `revenue_cents_per_seat_mile`, `unit_revenue_change_percent`

### Q3 2025 (5) United Airlines

Does the smaller seasonal drop in air-traffic liability reflect pricing, or a longer booking curve?

- `airline.price.fact_air_traffic_liability`: `fiscal_quarter_id`, `scenario_id`, `air_traffic_liability_amount`
- `airline.price.fact_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `operating_cash_flow_amount`, `working_capital_amount`
- `airline.price.fact_ancillary_price`: `fiscal_quarter_id`, `scenario_id`, `fee_type_id`, `geographic_entity_id`, `fee_dollars_per_bag`

### Q3 2025 (6) United Airlines

Why grow so much in Latin America in the quarter if unit revenue did not support it?

- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `revenue_cents_per_seat_mile`, `unit_revenue_change_percent`
- `airline.price.fact_mileageplus_economics`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `united_card_program_id`, `loyalty_revenue_amount`, `cobrand_spend_amount`
- `airline.price.fact_passenger_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `passenger_revenue_amount`

### Q3 2025 (7) United Airlines

How does fourth-quarter unit revenue sequence between domestic and international, including the holiday booking curve?

- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `revenue_cents_per_seat_mile`, `unit_revenue_change_percent`
- `airline.price.fact_fare_price`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `fare_product_id`, `average_fare_dollars_per_passenger`
- `airline.price.fact_geographic_margin`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `geographic_margin_percent`, `geographic_profit_amount`

### Q3 2025 (8) United Airlines

If unit cost rises a few percent a year, what revenue drivers produce about a point of annual margin expansion?

- `airline.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `revenue_cents_per_seat_mile`, `unit_revenue_change_percent`
- `airline.price.fact_geographic_margin`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `geographic_margin_percent`, `geographic_profit_amount`

### Q2 2025 (3) United Airlines

What changed from the stable case to the lower second-half outlook?

- `airline.price.fact_ancillary_revenue`: `fiscal_quarter_id`, `scenario_id`, `fee_type_id`, `geographic_entity_id`, `ancillary_revenue_amount`
- `airline.price.fact_fuel_recapture_rate`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_recapture_percent`
- `airline.price.fact_mileageplus_economics`: `fiscal_quarter_id`, `scenario_id`, `mileageplus_tier_id`, `united_card_program_id`, `loyalty_revenue_amount`, `cobrand_spend_amount`

### Q2 2025 (4) United Airlines

Which levers, including the main cabin, could make the fourth-quarter unit-revenue step better than the conservative case?

- `airline.price.fact_passenger_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `passenger_revenue_amount`
- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `revenue_cents_per_seat_mile`, `unit_revenue_change_percent`
- `airline.price.fact_cabin_margin`: `fiscal_quarter_id`, `scenario_id`, `cabin_id`, `geographic_entity_id`, `cabin_margin_percent`, `cabin_profit_amount`

### Q2 2025 (8) United Airlines

How much of the booking improvement is Newark versus the broader system, and is the fourth-quarter unit-revenue gain domestic or international?

- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `revenue_cents_per_seat_mile`, `unit_revenue_change_percent`
- `airline.price.fact_fare_price`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `fare_product_id`, `average_fare_dollars_per_passenger`
- `airline.price.fact_geographic_margin`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `geographic_margin_percent`, `geographic_profit_amount`

### Q2 2025 (9) United Airlines

How does the partner arrangement change the longer-term margin view?

- `airline.price.fact_geographic_margin`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `geographic_margin_percent`, `geographic_profit_amount`
- `airline.price.fact_yield`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `yield_cents_per_passenger_mile`, `yield_change_percent`
- `airline.price.fact_unit_revenue`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `revenue_cents_per_seat_mile`, `unit_revenue_change_percent`

### Q2 2025 (11) United Airlines

Which geography contributes most to the longer-term margin expansion?

- `airline.price.fact_geographic_margin`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `geographic_margin_percent`, `geographic_profit_amount`
- `airline.price.fact_route_margin`: `fiscal_quarter_id`, `scenario_id`, `route_id`, `geographic_entity_id`, `route_margin_percent`
- `airline.price.fact_yield`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cabin_id`, `traveler_type_id`, `yield_cents_per_passenger_mile`, `yield_change_percent`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `airline.loyalty.dim_skymiles_tier` | supporting population |
| `airline.loyalty.dim_mileageplus_tier` | supporting population |
| `airline.loyalty.dim_delta_card_program` | supporting population |
| `airline.loyalty.dim_united_card_program` | supporting population |
| `airline.loyalty.dim_skyteam_partner` | supporting population |
| `airline.loyalty.dim_star_alliance_partner` | supporting population |
| `airline.price.dim_fee_type` | supporting population |
| `airline.price.dim_currency` | supporting population |
| `airline.price.fact_passenger_revenue` | Q1 2026 (3), Q1 2026 (4), Q1 2026 (5), Q1 2026 (9), Q1 2026 (10), Q3 2025 (6), Q3 2025 (9), Q3 2025 (10), Q3 2024 (5), Q4 2025 (1), Q3 2025 (1), Q3 2025 (3), Q3 2025 (6), Q2 2025 (4) |
| `airline.price.fact_yield` | Q1 2026 (3), Q1 2026 (5), Q1 2026 (9), Q1 2026 (15), Q3 2025 (9), Q4 2024 (1), Q3 2024 (5), Q1 2026 (2), Q4 2025 (1), Q4 2025 (2), Q3 2025 (1), Q3 2025 (3), Q2 2025 (9), Q2 2025 (11) |
| `airline.price.fact_unit_revenue` | Q1 2026 (2), Q1 2026 (9), Q1 2026 (18), Q3 2025 (3), Q3 2025 (6), Q3 2025 (10), Q4 2024 (1), Q4 2024 (3), Q3 2024 (5), Q3 2025 (3), Q3 2025 (6), Q3 2025 (7), Q3 2025 (8), Q2 2025 (4), Q2 2025 (8), Q2 2025 (9) |
| `airline.price.fact_fare_price` | Q1 2026 (1), Q1 2026 (3), Q1 2026 (15), Q1 2026 (18), Q3 2025 (3), Q4 2024 (5), Q3 2025 (7), Q2 2025 (8) |
| `airline.price.fact_ancillary_revenue` | Q1 2026 (1), Q4 2024 (3), Q2 2025 (3) |
| `airline.price.fact_baggage_quantity` | Q1 2026 (1) |
| `airline.price.fact_ancillary_price` | Q3 2025 (5) |
| `airline.price.fact_cabin_margin` | Q1 2026 (4), Q1 2026 (5), Q3 2025 (6), Q3 2025 (9), Q3 2025 (18), Q4 2025 (1), Q4 2025 (8), Q4 2025 (11), Q3 2025 (1), Q2 2025 (4) |
| `airline.price.fact_geographic_margin` | Q1 2026 (4), Q1 2026 (18), Q3 2025 (3), Q3 2025 (18), Q4 2024 (1), Q1 2026 (2), Q4 2025 (3), Q4 2025 (8), Q4 2025 (11), Q3 2025 (7), Q3 2025 (8), Q2 2025 (8), Q2 2025 (9), Q2 2025 (11) |
| `airline.price.fact_route_margin` | Q1 2026 (15), Q3 2025 (14), Q4 2024 (2), Q4 2025 (8), Q2 2025 (11) |
| `airline.price.fact_enterprise_earnings` | Q1 2026 (2), Q3 2025 (1), Q3 2025 (14), Q3 2025 (18), Q4 2025 (11), Q3 2025 (8) |
| `airline.price.fact_skymiles_economics` | Q1 2026 (2), Q1 2026 (10), Q1 2026 (13), Q3 2025 (10), Q3 2025 (14), Q3 2025 (19), Q4 2024 (2), Q4 2024 (3), Q4 2024 (5), Q4 2025 (2) |
| `airline.price.fact_mileageplus_economics` | Q3 2025 (19), Q4 2025 (2), Q4 2025 (3), Q3 2025 (6), Q2 2025 (3) |
| `airline.price.fact_skymiles_miles_quantity` | Q1 2026 (13), Q4 2024 (2) |
| `airline.price.fact_mileageplus_miles_quantity` | Q4 2025 (3) |
| `airline.price.fact_fuel_recapture_rate` | Q1 2026 (13), Q4 2024 (5), Q1 2026 (2), Q2 2025 (3) |
| `airline.price.fact_cargo_revenue` | supporting population |
| `airline.price.fact_maintenance_revenue` | Q1 2026 (10), Q3 2025 (19) |
| `airline.price.fact_air_traffic_liability` | Q3 2025 (1), Q3 2025 (5) |
| `airline.price.fact_cash_flow` | Q3 2025 (1), Q3 2025 (5) |
