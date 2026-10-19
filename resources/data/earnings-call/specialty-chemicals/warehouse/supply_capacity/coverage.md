# Chemical Inc supply, stores, plants, and service capacity

Sherwin-Williams coatings are measured in gallons through company stores and plants, with its own reporting-segment dimension. Ecolab is measured as site service in visits, customer sites, and technician hours, with its own reporting-segment dimension, and is not modeled as a paint-plant operating rate. Quantity and price or margin are separate facts joined by fiscal quarter, scenario, and the business keys. Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks.

## Numbered questions

## Sherwin-Williams

### Q1 2026 (2) Sherwin-Williams

Which inputs pushed the raw-material outlook from low-single-digit to low-to-mid-single-digit, and have VAM and propylene peaked versus spot?

- `chemical.supply.fact_coating_input_cost`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `supplier_id`, `contract_cost_dollars_per_pound`, `cost_inflation_percent`
- `chemical.supply.fact_coating_spot_price`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `spot_cost_dollars_per_pound`
- `chemical.supply.fact_ecl_input_cost`: `fiscal_quarter_id`, `scenario_id`, `ecl_raw_input_id`, `ecl_reporting_segment_id`, `delivered_cost_dollars_per_kilogram`, `cost_inflation_percent`

### Q1 2026 (3) Sherwin-Williams

How are growth spend and net store openings and closures being set while share gains continue?

- `chemical.supply.fact_shw_growth_spend`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `growth_spend_amount`
- `chemical.supply.fact_store_network_quantity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `store_opening_count`, `store_closure_count`, `net_store_count`
- `chemical.supply.fact_coating_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `coating_plant_id`, `coatings_product_id`, `production_gallons`

### Q1 2026 (10) Sherwin-Williams

Why is the raw-material exit rate only low-to-mid single digits when outside estimates are much higher?

- `chemical.supply.fact_coating_input_cost`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `supplier_id`, `contract_cost_dollars_per_pound`, `cost_inflation_percent`
- `chemical.supply.fact_coating_spot_price`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `spot_cost_dollars_per_pound`
- `chemical.supply.fact_ecl_input_cost`: `fiscal_quarter_id`, `scenario_id`, `ecl_raw_input_id`, `ecl_reporting_segment_id`, `delivered_cost_dollars_per_kilogram`, `cost_inflation_percent`

### Q4 2025 (2) Sherwin-Williams

What labor, raw-basket, and titanium-dioxide utilization assumptions sit inside the gross-margin guide?

- `chemical.supply.fact_coating_input_quantity`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `coating_plant_id`, `input_consumed_pounds`
- `chemical.supply.fact_coating_input_cost`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `supplier_id`, `contract_cost_dollars_per_pound`, `cost_inflation_percent`
- `chemical.supply.fact_coating_spot_price`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `spot_cost_dollars_per_pound`

### Q3 2025 (3) Sherwin-Williams

How is the return on growth investment judged across share gains, new stores, and time to steady-state profit?

- `chemical.supply.fact_shw_growth_spend`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `growth_spend_amount`
- `chemical.supply.fact_store_network_quantity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `store_opening_count`, `store_closure_count`, `net_store_count`
- `chemical.supply.fact_ecl_growth_spend`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `growth_spend_amount`

### Q3 2025 (4) Sherwin-Williams

What integration actions are planned at Suvenil?

- `chemical.supply.fact_integration_amount`: `fiscal_quarter_id`, `scenario_id`, `acquisition_id`, `shw_reporting_segment_id`, `integration_cost_amount`
- `chemical.supply.fact_coating_input_quantity`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `coating_plant_id`, `input_consumed_pounds`
- `chemical.supply.fact_coating_input_cost`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `supplier_id`, `contract_cost_dollars_per_pound`, `cost_inflation_percent`

### Q2 2025 (1) Sherwin-Williams

What supports caution that demand could deteriorate in the back half, and where would that show up?

- `chemical.supply.fact_restructuring_savings`: `fiscal_quarter_id`, `scenario_id`, `cost_action_id`, `shw_reporting_segment_id`, `savings_amount`
- `chemical.supply.fact_coating_input_quantity`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `coating_plant_id`, `input_consumed_pounds`
- `chemical.supply.fact_coating_input_cost`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `supplier_id`, `contract_cost_dollars_per_pound`, `cost_inflation_percent`

### Q2 2025 (3) Sherwin-Williams

Is added SG&A mainly headcount, or does it imply a higher store-count target?

- `chemical.supply.fact_headcount_quantity`: `fiscal_quarter_id`, `scenario_id`, `workforce_role_id`, `shw_reporting_segment_id`, `headcount_count`, `headcount_addition_count`
- `chemical.supply.fact_store_network_quantity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `store_opening_count`, `store_closure_count`, `net_store_count`
- `chemical.supply.fact_coating_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `coating_plant_id`, `coatings_product_id`, `production_gallons`

### Q2 2025 (10) Sherwin-Williams

Where do the doubled restructuring savings come from, and do they accelerate in the back half?

- `chemical.supply.fact_restructuring_savings`: `fiscal_quarter_id`, `scenario_id`, `cost_action_id`, `shw_reporting_segment_id`, `savings_amount`
- `chemical.supply.fact_coating_input_quantity`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `coating_plant_id`, `input_consumed_pounds`
- `chemical.supply.fact_coating_input_cost`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `supplier_id`, `contract_cost_dollars_per_pound`, `cost_inflation_percent`

### Q2 2025 (11) Sherwin-Williams

With volumes below plan, is the margin pain from lower operating rates split evenly between manufacturing and Paint Stores?

- `chemical.supply.fact_coating_production_quantity`: `fiscal_quarter_id`, `scenario_id`, `coating_plant_id`, `coatings_product_id`, `production_gallons`
- `chemical.supply.fact_coating_operating_rate`: `fiscal_quarter_id`, `scenario_id`, `coating_plant_id`, `coatings_product_id`, `operating_rate_percent`
- `chemical.supply.fact_store_network_quantity`: `fiscal_quarter_id`, `scenario_id`, `region_id`, `store_opening_count`, `store_closure_count`, `net_store_count`

### Q2 2025 (12) Sherwin-Williams

Which raw-material baskets drive expected second-half deflation?

- `chemical.supply.fact_coating_input_cost`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `supplier_id`, `contract_cost_dollars_per_pound`, `cost_inflation_percent`
- `chemical.supply.fact_coating_input_quantity`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `coating_plant_id`, `input_consumed_pounds`
- `chemical.supply.fact_coating_spot_price`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `spot_cost_dollars_per_pound`

### Q2 2025 (14) Sherwin-Williams

What supply-chain inefficiencies became a larger headwind in the quarter?

- `chemical.supply.fact_supply_disruption_cost`: `fiscal_quarter_id`, `scenario_id`, `supply_issue_id`, `shw_reporting_segment_id`, `supply_disruption_cost_amount`
- `chemical.supply.fact_restructuring_savings`: `fiscal_quarter_id`, `scenario_id`, `cost_action_id`, `shw_reporting_segment_id`, `savings_amount`
- `chemical.supply.fact_coating_input_quantity`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `coating_plant_id`, `input_consumed_pounds`

## Ecolab

### Q1 2026 (5) Ecolab

Is Life Sciences organic strength the expected step-change, and how does growth change when new capacity comes online?

- `chemical.supply.fact_service_capacity_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `workforce_role_id`, `available_service_hours`, `service_employee_count`
- `chemical.supply.fact_capex_amount`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `shw_reporting_segment_id`, `capex_amount`
- `chemical.supply.fact_ecl_growth_spend`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `growth_spend_amount`

### Q1 2026 (8) Ecolab

Is Specialty growth inside Institutional and Specialty coming from digital and productivity tools rather than chemical volume, given weak foot traffic?

- `chemical.supply.fact_digital_install_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `installed_tool_count`, `connected_site_count`
- `chemical.supply.fact_ecl_growth_spend`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `growth_spend_amount`
- `chemical.supply.fact_capex_amount`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `shw_reporting_segment_id`, `capex_amount`

### Q1 2026 (16) Ecolab

Why is raw inflation described as high-single-digit in the second quarter without a further increase later in the year?

- `chemical.supply.fact_ecl_input_cost`: `fiscal_quarter_id`, `scenario_id`, `ecl_raw_input_id`, `ecl_reporting_segment_id`, `delivered_cost_dollars_per_kilogram`, `cost_inflation_percent`
- `chemical.supply.fact_coating_input_cost`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `supplier_id`, `contract_cost_dollars_per_pound`, `cost_inflation_percent`
- `chemical.supply.fact_ecl_input_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_raw_input_id`, `input_consumed_kilograms`

### Q4 2025 (10) Ecolab

Is specialty growth from earlier capacity investments now in the run rate, or is more still to come?

- `chemical.supply.fact_capex_amount`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `shw_reporting_segment_id`, `capex_amount`
- `chemical.supply.fact_ecl_growth_spend`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `growth_spend_amount`
- `chemical.supply.fact_digital_install_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `installed_tool_count`, `connected_site_count`

### Q3 2025 (2) Ecolab

How do resource shifts, innovation, and share gains offset end-market weakness as basic industries and paper return toward growth?

- `chemical.supply.fact_shw_growth_spend`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `growth_spend_amount`
- `chemical.supply.fact_ecl_growth_spend`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `growth_spend_amount`
- `chemical.supply.fact_ecl_headcount_quantity`: `fiscal_quarter_id`, `scenario_id`, `workforce_role_id`, `ecl_reporting_segment_id`, `headcount_count`

### Q2 2025 (3) Ecolab

How are pest-intelligence rollouts coming together, and what are the puts and takes for pest growth?

- `chemical.supply.fact_digital_install_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `installed_tool_count`, `connected_site_count`
- `chemical.supply.fact_ecl_growth_spend`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `growth_spend_amount`
- `chemical.supply.fact_ecl_headcount_quantity`: `fiscal_quarter_id`, `scenario_id`, `workforce_role_id`, `ecl_reporting_segment_id`, `headcount_count`

### Q2 2025 (4) Ecolab

How is delivered product cost trending into the second half given tariffs and mixed raw materials?

- `chemical.supply.fact_ecl_input_cost`: `fiscal_quarter_id`, `scenario_id`, `ecl_raw_input_id`, `ecl_reporting_segment_id`, `delivered_cost_dollars_per_kilogram`, `cost_inflation_percent`
- `chemical.supply.fact_ecl_input_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_raw_input_id`, `input_consumed_kilograms`
- `chemical.supply.fact_coating_input_cost`: `fiscal_quarter_id`, `scenario_id`, `coating_raw_input_id`, `supplier_id`, `contract_cost_dollars_per_pound`, `cost_inflation_percent`

### Q2 2025 (10) Ecolab

Do returns and paybacks on the three priority growth areas differ from traditional institutional investments?

- `chemical.supply.fact_ecl_growth_spend`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `growth_spend_amount`
- `chemical.supply.fact_shw_growth_spend`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `growth_spend_amount`
- `chemical.supply.fact_capex_amount`: `fiscal_quarter_id`, `scenario_id`, `facility_type_id`, `shw_reporting_segment_id`, `capex_amount`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `chemical.network.dim_coating_store` | supporting population |
| `chemical.network.dim_coating_plant` | supporting population |
| `chemical.network.dim_supplier` | supporting population |
| `chemical.network.dim_acquisition` | supporting population |
| `chemical.network.dim_workforce_role` | supporting population |
| `chemical.network.dim_cost_action` | supporting population |
| `chemical.network.dim_facility_type` | supporting population |
| `chemical.network.dim_supply_issue` | supporting population |
| `chemical.supply.fact_coating_input_quantity` | Q4 2025 (2), Q3 2025 (4), Q2 2025 (1), Q2 2025 (10), Q2 2025 (12), Q2 2025 (14) |
| `chemical.supply.fact_coating_input_cost` | Q1 2026 (2), Q1 2026 (10), Q4 2025 (2), Q3 2025 (4), Q2 2025 (1), Q2 2025 (10), Q2 2025 (12), Q1 2026 (16), Q2 2025 (4) |
| `chemical.supply.fact_coating_spot_price` | Q1 2026 (2), Q1 2026 (10), Q4 2025 (2), Q2 2025 (12) |
| `chemical.supply.fact_ecl_input_quantity` | Q1 2026 (16), Q2 2025 (4) |
| `chemical.supply.fact_ecl_input_cost` | Q1 2026 (2), Q1 2026 (10), Q1 2026 (16), Q2 2025 (4) |
| `chemical.supply.fact_store_network_quantity` | Q1 2026 (3), Q3 2025 (3), Q2 2025 (3), Q2 2025 (11) |
| `chemical.supply.fact_coating_plant_capacity` | supporting population |
| `chemical.supply.fact_coating_production_quantity` | Q1 2026 (3), Q2 2025 (3), Q2 2025 (11) |
| `chemical.supply.fact_coating_operating_rate` | Q2 2025 (11) |
| `chemical.supply.fact_service_capacity_quantity` | Q1 2026 (5) |
| `chemical.supply.fact_service_delivery_cost` | supporting population |
| `chemical.supply.fact_shw_growth_spend` | Q1 2026 (3), Q3 2025 (3), Q3 2025 (2), Q2 2025 (10) |
| `chemical.supply.fact_ecl_growth_spend` | Q3 2025 (3), Q1 2026 (5), Q1 2026 (8), Q4 2025 (10), Q3 2025 (2), Q2 2025 (3), Q2 2025 (10) |
| `chemical.supply.fact_capex_amount` | Q1 2026 (5), Q1 2026 (8), Q4 2025 (10), Q2 2025 (10) |
| `chemical.supply.fact_headcount_quantity` | Q2 2025 (3) |
| `chemical.supply.fact_ecl_headcount_quantity` | Q3 2025 (2), Q2 2025 (3) |
| `chemical.supply.fact_restructuring_savings` | Q2 2025 (1), Q2 2025 (10), Q2 2025 (14) |
| `chemical.supply.fact_integration_amount` | Q3 2025 (4) |
| `chemical.supply.fact_supply_disruption_cost` | Q2 2025 (14) |
| `chemical.supply.fact_digital_install_quantity` | Q1 2026 (8), Q4 2025 (10), Q2 2025 (3) |
