# Airline Inc fleet, capacity, fuel, and unit cost

Capacity is available seat-miles, traffic is revenue passenger-miles, and yield and unit cost use those denominators through shared geographic, cabin, and traveler keys. A route carries an origin airport and a destination airport. Cargo and maintenance are revenue and traffic measures, SkyMiles and MileagePlus stay in separate facts, and enterprise earnings are grained at enterprise level, not at a hub. Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks.

## Numbered questions

## Delta Air Lines

### Q1 2026 (6) Delta Air Lines

Are there constraints on sourcing jet fuel in Asia-Pacific or elsewhere?

- `airline.supply.fact_fuel_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `aircraft_model_id`, `fuel_gallons_consumed`
- `airline.supply.fact_fuel_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_cost_dollars_per_gallon`
- `airline.supply.fact_fuel_expense`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_expense_amount`

### Q1 2026 (8) Delta Air Lines

Would a longer fuel shock change the fleet plan, including earlier retirements or exiting an aircraft type?

- `airline.supply.fact_fleet_retirement_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `aircraft_retirement_count`
- `airline.supply.fact_fleet_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `manufacturer_id`, `aircraft_delivery_count`
- `airline.supply.fact_fleet_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `fleet_category_id`, `aircraft_count`, `average_aircraft_age_years`

### Q1 2026 (14) Delta Air Lines

How are lingering pilot-recovery costs fixed before peak summer, when the operation is tighter?

- `airline.supply.fact_labor_cost`: `fiscal_quarter_id`, `scenario_id`, `labor_group_id`, `labor_cost_amount`
- `airline.supply.fact_fuel_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_cost_dollars_per_gallon`
- `airline.supply.fact_fuel_expense`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_expense_amount`

### Q3 2025 (4) Delta Air Lines

What mix benefit arrives in 2026 and 2027 as new aircraft are delivered?

- `airline.supply.fact_fleet_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `manufacturer_id`, `aircraft_delivery_count`
- `airline.supply.fact_fleet_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `fleet_category_id`, `aircraft_count`, `average_aircraft_age_years`
- `airline.supply.fact_aircraft_utilization`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `block_hours`

### Q3 2025 (5) Delta Air Lines

How much of the unit-cost efficiency from growing into the workforce, fleet, and airports carries into next year?

- `airline.supply.fact_unit_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cost_cents_per_seat_mile`, `ex_fuel_cost_cents_per_seat_mile`
- `airline.supply.fact_aircraft_utilization`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `block_hours`
- `airline.supply.fact_fuel_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_cost_dollars_per_gallon`

### Q3 2025 (12) Delta Air Lines

How is Atlantic capacity next year being spread more evenly?

- `airline.supply.fact_maintenance_events`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `maintenance_event_count`
- `airline.supply.fact_fuel_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_cost_dollars_per_gallon`
- `airline.supply.fact_maintenance_cost`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `maintenance_cost_amount`

### Q3 2025 (13) Delta Air Lines

Are heavy-maintenance events higher or lower next year, and what inflation is showing up in maintenance and parts?

- `airline.supply.fact_maintenance_events`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `maintenance_event_count`
- `airline.supply.fact_maintenance_cost`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `maintenance_cost_amount`
- `airline.supply.fact_shop_capacity_quantity`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `shop_capacity_event_count`

### Q3 2024 (2) Delta Air Lines

How is domestic capacity being set as lower-cost airlines cut capacity?

- `airline.supply.fact_maintenance_cost`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `maintenance_cost_amount`
- `airline.supply.fact_competitor_capacity`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `geographic_entity_id`, `competitor_available_seat_miles`
- `airline.supply.fact_fuel_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_cost_dollars_per_gallon`

## United Airlines

### Q1 2026 (4) United Airlines

What visibility is there on jet-fuel shortages in Asia or Europe, and what is the backup plan?

- `airline.supply.fact_fuel_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `aircraft_model_id`, `fuel_gallons_consumed`
- `airline.supply.fact_fleet_retirement_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `aircraft_retirement_count`
- `airline.supply.fact_fuel_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_cost_dollars_per_gallon`

### Q1 2026 (7) United Airlines

Does cutting about five points of capacity create maintenance-cost leverage, or does maintenance stay lumpy?

- `airline.supply.fact_maintenance_cost`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `maintenance_cost_amount`
- `airline.supply.fact_fuel_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_cost_dollars_per_gallon`
- `airline.supply.fact_maintenance_events`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `maintenance_event_count`

### Q1 2026 (8) United Airlines

What fuel price would be required to put mid-single-digit capacity growth back in the second half, and how much irrational capacity could return?

- `airline.supply.fact_fuel_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_cost_dollars_per_gallon`
- `airline.supply.fact_hub_capacity`: `fiscal_quarter_id`, `scenario_id`, `hub_id`, `geographic_entity_id`, `hub_available_seat_miles`
- `airline.supply.fact_fuel_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `aircraft_model_id`, `fuel_gallons_consumed`

### Q1 2026 (9) United Airlines

What longer-term margin uplift is expected from merchandising, fleet, and loyalty, including newer narrow-bodies on those routes?

- `airline.supply.fact_fleet_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `manufacturer_id`, `aircraft_delivery_count`
- `airline.supply.fact_fleet_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `fleet_category_id`, `aircraft_count`, `average_aircraft_age_years`
- `airline.supply.fact_unit_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cost_cents_per_seat_mile`, `ex_fuel_cost_cents_per_seat_mile`

### Q1 2026 (10) United Airlines

What supports full fuel-cost recapture, and does it require other carriers to cut capacity?

- `airline.supply.fact_fuel_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_cost_dollars_per_gallon`
- `airline.supply.fact_maintenance_cost`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `maintenance_cost_amount`
- `airline.supply.fact_competitor_capacity`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `geographic_entity_id`, `competitor_available_seat_miles`

### Q4 2025 (4) United Airlines

What is keeping unit cost in check despite product investment, and what efficiencies remain for next year?

- `airline.supply.fact_unit_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cost_cents_per_seat_mile`, `ex_fuel_cost_cents_per_seat_mile`
- `airline.supply.fact_aircraft_utilization`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `block_hours`
- `airline.supply.fact_fuel_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_cost_dollars_per_gallon`

### Q4 2025 (5) United Airlines

With a large narrow-body and wide-body delivery plan and few retirements, what guardrails limit capacity growth, and where in the network?

- `airline.supply.fact_fleet_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `manufacturer_id`, `aircraft_delivery_count`
- `airline.supply.fact_fleet_retirement_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `aircraft_retirement_count`
- `airline.supply.fact_fleet_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `fleet_category_id`, `aircraft_count`, `average_aircraft_age_years`

### Q4 2025 (10) United Airlines

Does a competitor adding unprofitable Chicago flying change the view that domestic is the best geography next year?

- `airline.supply.fact_competitor_capacity`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `geographic_entity_id`, `competitor_available_seat_miles`
- `airline.supply.fact_maintenance_events`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `maintenance_event_count`

### Q4 2025 (12) United Airlines

Excluding labor, is this year's unit-cost performance the right benchmark for next year?

- `airline.supply.fact_unit_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cost_cents_per_seat_mile`, `ex_fuel_cost_cents_per_seat_mile`
- `airline.supply.fact_labor_cost`: `fiscal_quarter_id`, `scenario_id`, `labor_group_id`, `labor_cost_amount`
- `airline.supply.fact_maintenance_cost`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `maintenance_cost_amount`

### Q4 2025 (14) United Airlines

How does capacity discipline persist as aircraft deliveries ramp?

- `airline.supply.fact_fleet_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `manufacturer_id`, `aircraft_delivery_count`
- `airline.supply.fact_fuel_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_cost_dollars_per_gallon`
- `airline.supply.fact_headcount_quantity`: `fiscal_quarter_id`, `scenario_id`, `labor_group_id`, `headcount_count`

### Q3 2025 (2) United Airlines

After maintenance shifts and the flight-attendant agreement, is fourth-quarter unit cost still near the second-quarter reference?

- `airline.supply.fact_labor_cost`: `fiscal_quarter_id`, `scenario_id`, `labor_group_id`, `labor_cost_amount`
- `airline.supply.fact_unit_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cost_cents_per_seat_mile`, `ex_fuel_cost_cents_per_seat_mile`
- `airline.supply.fact_maintenance_cost`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `maintenance_cost_amount`

### Q3 2025 (10) United Airlines

Is the maintenance expense that moved a real deferral, and is a flight-attendant accrual in the fourth-quarter outlook?

- `airline.supply.fact_maintenance_cost`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `maintenance_cost_amount`
- `airline.supply.fact_labor_cost`: `fiscal_quarter_id`, `scenario_id`, `labor_group_id`, `labor_cost_amount`
- `airline.supply.fact_fuel_expense`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_expense_amount`

### Q3 2025 (11) United Airlines

Where does the mid-continent hub rebuild stand?

- `airline.supply.fact_hub_capacity`: `fiscal_quarter_id`, `scenario_id`, `hub_id`, `geographic_entity_id`, `hub_available_seat_miles`
- `airline.supply.fact_fuel_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `aircraft_model_id`, `fuel_gallons_consumed`

### Q3 2025 (12) United Airlines

What factors decide whether another wide-body type is still too expensive to add?

- `airline.supply.fact_fleet_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `manufacturer_id`, `aircraft_delivery_count`
- `airline.supply.fact_fleet_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `fleet_category_id`, `aircraft_count`, `average_aircraft_age_years`
- `airline.supply.fact_fleet_retirement_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `aircraft_retirement_count`

### Q3 2025 (13) United Airlines

Are Airbus and Boeing deliveries now ahead of the original plan?

- `airline.supply.fact_fleet_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `manufacturer_id`, `aircraft_delivery_count`
- `airline.supply.fact_headcount_quantity`: `fiscal_quarter_id`, `scenario_id`, `labor_group_id`, `headcount_count`
- `airline.supply.fact_fleet_retirement_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `aircraft_retirement_count`

### Q2 2025 (1) United Airlines

How should unit cost excluding fuel trend after a low-single-digit increase, including the distribution-expense item?

- `airline.supply.fact_unit_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `cost_cents_per_seat_mile`, `ex_fuel_cost_cents_per_seat_mile`
- `airline.supply.fact_fuel_expense`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_expense_amount`
- `airline.supply.fact_fuel_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_cost_dollars_per_gallon`

### Q2 2025 (7) United Airlines

Why do industry capacity cuts keep showing up after peak summer rather than earlier?

- `airline.supply.fact_competitor_capacity`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `geographic_entity_id`, `competitor_available_seat_miles`
- `airline.supply.fact_maintenance_cost`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `maintenance_cost_amount`
- `airline.supply.fact_fuel_cost`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `fuel_cost_dollars_per_gallon`

### Q2 2025 (10) United Airlines

What cadence of gauge benefit is expected over the next two years?

- `airline.supply.fact_aircraft_utilization`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `block_hours`
- `airline.supply.fact_maintenance_events`: `fiscal_quarter_id`, `scenario_id`, `maintenance_type_id`, `maintenance_provider_id`, `maintenance_event_count`
- `airline.supply.fact_fleet_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `manufacturer_id`, `aircraft_delivery_count`

### Q2 2025 (12) United Airlines

Are pilots now in balance with deliveries, or still overstaffed?

- `airline.supply.fact_headcount_quantity`: `fiscal_quarter_id`, `scenario_id`, `labor_group_id`, `headcount_count`
- `airline.supply.fact_labor_cost`: `fiscal_quarter_id`, `scenario_id`, `labor_group_id`, `labor_cost_amount`
- `airline.supply.fact_fleet_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `manufacturer_id`, `aircraft_delivery_count`

### Q2 2025 (13) United Airlines

What is being debated about returning Newark to a less restricted operating level after the cap?

- `airline.supply.fact_hub_capacity`: `fiscal_quarter_id`, `scenario_id`, `hub_id`, `geographic_entity_id`, `hub_available_seat_miles`
- `airline.supply.fact_fuel_quantity`: `fiscal_quarter_id`, `scenario_id`, `geographic_entity_id`, `aircraft_model_id`, `fuel_gallons_consumed`

### Q2 2025 (14) United Airlines

How many long-range narrow-bodies arrive this year, and how soon do they fly internationally?

- `airline.supply.fact_fleet_delivery_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `manufacturer_id`, `aircraft_delivery_count`
- `airline.supply.fact_fleet_quantity`: `fiscal_quarter_id`, `scenario_id`, `aircraft_model_id`, `fleet_category_id`, `aircraft_count`, `average_aircraft_age_years`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `airline.fleet.dim_aircraft_model` | supporting population |
| `airline.fleet.dim_fleet_category` | supporting population |
| `airline.fleet.dim_manufacturer` | supporting population |
| `airline.fleet.dim_maintenance_type` | supporting population |
| `airline.fleet.dim_maintenance_provider` | supporting population |
| `airline.fleet.dim_cargo_type` | supporting population |
| `airline.fleet.dim_labor_group` | supporting population |
| `airline.supply.fact_fuel_quantity` | Q1 2026 (6), Q1 2026 (4), Q1 2026 (8), Q3 2025 (11), Q2 2025 (13) |
| `airline.supply.fact_fuel_cost` | Q1 2026 (6), Q1 2026 (14), Q3 2025 (5), Q3 2025 (12), Q3 2024 (2), Q1 2026 (4), Q1 2026 (7), Q1 2026 (8), Q1 2026 (10), Q4 2025 (4), Q4 2025 (14), Q2 2025 (1), Q2 2025 (7) |
| `airline.supply.fact_fuel_expense` | Q1 2026 (6), Q1 2026 (14), Q3 2025 (10), Q2 2025 (1) |
| `airline.supply.fact_unit_cost` | Q3 2025 (5), Q1 2026 (9), Q4 2025 (4), Q4 2025 (12), Q3 2025 (2), Q2 2025 (1) |
| `airline.supply.fact_labor_cost` | Q1 2026 (14), Q4 2025 (12), Q3 2025 (2), Q3 2025 (10), Q2 2025 (12) |
| `airline.supply.fact_headcount_quantity` | Q4 2025 (14), Q3 2025 (13), Q2 2025 (12) |
| `airline.supply.fact_maintenance_cost` | Q3 2025 (12), Q3 2025 (13), Q3 2024 (2), Q1 2026 (7), Q1 2026 (10), Q4 2025 (12), Q3 2025 (2), Q3 2025 (10), Q2 2025 (7) |
| `airline.supply.fact_maintenance_events` | Q3 2025 (12), Q3 2025 (13), Q1 2026 (7), Q4 2025 (10), Q2 2025 (10) |
| `airline.supply.fact_fleet_delivery_quantity` | Q1 2026 (8), Q3 2025 (4), Q1 2026 (9), Q4 2025 (5), Q4 2025 (14), Q3 2025 (12), Q3 2025 (13), Q2 2025 (10), Q2 2025 (12), Q2 2025 (14) |
| `airline.supply.fact_fleet_retirement_quantity` | Q1 2026 (8), Q1 2026 (4), Q4 2025 (5), Q3 2025 (12), Q3 2025 (13) |
| `airline.supply.fact_fleet_quantity` | Q1 2026 (8), Q3 2025 (4), Q1 2026 (9), Q4 2025 (5), Q3 2025 (12), Q2 2025 (14) |
| `airline.supply.fact_aircraft_utilization` | Q3 2025 (4), Q3 2025 (5), Q4 2025 (4), Q2 2025 (10) |
| `airline.supply.fact_hub_capacity` | Q1 2026 (8), Q3 2025 (11), Q2 2025 (13) |
| `airline.supply.fact_competitor_capacity` | Q3 2024 (2), Q1 2026 (10), Q4 2025 (10), Q2 2025 (7) |
| `airline.supply.fact_shop_capacity_quantity` | Q3 2025 (13) |
