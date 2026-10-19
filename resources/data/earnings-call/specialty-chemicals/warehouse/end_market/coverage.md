# Chemical Inc end market and site-service demand

Sherwin-Williams coatings are measured in gallons through company stores and plants, with its own reporting-segment dimension. Ecolab is measured as site service in visits, customer sites, and technician hours, with its own reporting-segment dimension, and is not modeled as a paint-plant operating rate. Quantity and price or margin are separate facts joined by fiscal quarter, scenario, and the business keys. Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks.

## Numbered questions

## Sherwin-Williams

### Q1 2026 (8) Sherwin-Williams

Will residential repaint stay solid, and will refinish, general industrial, and coil strength continue?

- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_housing_activity_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `housing_completion_count`, `repaint_cycle_years`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`

### Q1 2026 (11) Sherwin-Williams

How much of packaging outgrowth is the regulatory conversion, and does growth move back toward the industry after that catalyst is lapped?

- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`
- `chemical.demand.fact_industry_coatings_volume`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `industry_volume_gallons`
- `chemical.demand.fact_site_activity_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `open_site_count`, `closed_site_count`

### Q1 2026 (12) Sherwin-Williams

Is the lower Performance Coatings volume guide from current order weakness or March pull-forward, and where is U.S. industrial demand expanding?

- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_industry_coatings_volume`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `industry_volume_gallons`
- `chemical.demand.fact_weather_affected_volume`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `weather_regime_id`, `weather_affected_gallons`

### Q1 2026 (13) Sherwin-Williams

Are Performance Coatings customers locking production schedules or shifting to short-cycle orders?

- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_industry_coatings_volume`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `industry_volume_gallons`
- `chemical.demand.fact_shw_channel_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_channel_id`, `channel_inventory_gallons`

### Q1 2026 (14) Sherwin-Williams

Are customers prebuying ahead of inflationary price increases?

- `chemical.demand.fact_shw_channel_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_channel_id`, `channel_inventory_gallons`
- `chemical.demand.fact_customer_retention_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `customer_type_id`, `retained_customer_count`, `base_customer_count`
- `chemical.demand.fact_program_coverage_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `covered_site_count`, `targeted_site_count`, `covered_customer_count`

### Q1 2026 (15) Sherwin-Williams

If U.S. architectural demand stays weak through the decade, how does strategy change, and is Paint Stores tracking a low-single-digit sales decline?

- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`
- `chemical.demand.fact_acquired_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `acquisition_id`, `ecl_reporting_segment_id`, `acquired_sales_amount`, `acquired_sales_change_percent`

### Q4 2025 (1) Sherwin-Williams

What drove Performance Coatings margin outperformance beyond a mix shift toward packaging and auto refinish?

- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_industry_coatings_volume`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `industry_volume_gallons`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`

### Q4 2025 (4) Sherwin-Williams

How is severe winter weather changing current demand, and could it pull first-quarter results below last year?

- `chemical.demand.fact_weather_affected_volume`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `weather_regime_id`, `weather_affected_gallons`
- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`

### Q4 2025 (5) Sherwin-Williams

Has packaging recovered past the prior correction, and how much industry conversion is left?

- `chemical.demand.fact_industry_coatings_volume`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `industry_volume_gallons`
- `chemical.demand.fact_site_activity_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `open_site_count`, `closed_site_count`
- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`

### Q4 2025 (7) Sherwin-Williams

Were residential repaint volumes flat or down if price rose faster than sales?

- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_housing_activity_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `housing_completion_count`, `repaint_cycle_years`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`

### Q4 2025 (8) Sherwin-Williams

How does Consumer Brands bridge from fourth-quarter growth that included Suvenil to the first-quarter and full-year outlook?

- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`
- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_acquired_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `acquisition_id`, `ecl_reporting_segment_id`, `acquired_sales_amount`, `acquired_sales_change_percent`

### Q4 2025 (9) Sherwin-Williams

Does flat Paint Stores guidance imply share gain if the market is down and new stores add about a point of sales?

- `chemical.demand.fact_shw_market_share`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `region_id`, `market_share_percent`
- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`

### Q4 2025 (10) Sherwin-Williams

What is delaying the five-to-seven-year repaint cycle after demand was pulled into 2021, including contractor labor?

- `chemical.demand.fact_housing_activity_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `housing_completion_count`, `repaint_cycle_years`
- `chemical.demand.fact_contractor_backlog`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `region_id`, `backlog_job_count`, `backlog_duration_weeks`
- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`

### Q4 2025 (12) Sherwin-Williams

How does a coatings merger change the opportunity set in industrial-facing businesses?

- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_industry_coatings_volume`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `industry_volume_gallons`
- `chemical.demand.fact_acquired_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `acquisition_id`, `ecl_reporting_segment_id`, `acquired_sales_amount`, `acquired_sales_change_percent`

### Q3 2025 (2) Sherwin-Williams

How far do mortgage rates need to fall before they catalyze Paint Stores demand?

- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`
- `chemical.demand.fact_shw_market_share`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `region_id`, `market_share_percent`

### Q3 2025 (5) Sherwin-Williams

Is the more cautious tone on the second half of next year from specific demand signals or from current-trend conservatism?

- `chemical.demand.fact_contractor_backlog`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `region_id`, `backlog_job_count`, `backlog_duration_weeks`
- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`

### Q3 2025 (6) Sherwin-Williams

What are contractor backlogs and visibility over the next three to six months, and which Paint Stores submarkets sound confident versus cautious?

- `chemical.demand.fact_contractor_backlog`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `region_id`, `backlog_job_count`, `backlog_duration_weeks`
- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`

### Q3 2025 (7) Sherwin-Williams

Where are U.S. industry gallons down by architectural subsegment?

- `chemical.demand.fact_industry_coatings_volume`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `industry_volume_gallons`
- `chemical.demand.fact_shw_market_share`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `region_id`, `market_share_percent`
- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`

### Q3 2025 (8) Sherwin-Williams

Why is Performance Coatings showing negative operating leverage on positive sales, and do the same mix and cost dynamics persist in the fourth quarter?

- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`
- `chemical.demand.fact_industry_coatings_volume`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `industry_volume_gallons`

### Q3 2025 (9) Sherwin-Williams

How does a roughly flat second-half Paint Stores volume compare with a first-half organic decline in a lower-for-longer market?

- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_shw_market_share`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `region_id`, `market_share_percent`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`

### Q3 2025 (13) Sherwin-Williams

Does pushing share gains in another soft year pull forward gains that would normally arrive in a recovery?

- `chemical.demand.fact_shw_market_share`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `region_id`, `market_share_percent`
- `chemical.demand.fact_ecl_market_share`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `market_share_percent`
- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`

### Q3 2025 (14) Sherwin-Williams

Did non-residential Paint Stores businesses accelerate because delayed price rolled through or because those markets' demand accelerated?

- `chemical.demand.fact_shw_market_share`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `region_id`, `market_share_percent`
- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`

### Q2 2025 (2) Sherwin-Williams

In which of the six Paint Stores subsegments would incremental competitive disruption yield the most share over the next year?

- `chemical.demand.fact_shw_market_share`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `region_id`, `market_share_percent`
- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`

### Q2 2025 (4) Sherwin-Williams

Has competitor disruption changed how growth spend is split between Paint Stores and Consumer Brands?

- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`
- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_shw_market_share`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `region_id`, `market_share_percent`

### Q2 2025 (6) Sherwin-Williams

Is industry volume weakness expected to spill into early 2026, and which Paint Stores verticals would improve first?

- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`
- `chemical.demand.fact_industry_coatings_volume`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `industry_volume_gallons`

### Q2 2025 (7) Sherwin-Williams

How do Paint Stores volume declines compare with industry volumes in the quarter and for the full year?

- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`
- `chemical.demand.fact_industry_coatings_volume`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `industry_volume_gallons`

### Q2 2025 (8) Sherwin-Williams

Will new commercial and new residential hold current levels in the second half or fall with completions?

- `chemical.demand.fact_housing_activity_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `housing_completion_count`, `repaint_cycle_years`
- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`

### Q2 2025 (9) Sherwin-Williams

What role does price play in pursuing share and volume across end markets?

- `chemical.demand.fact_industry_coatings_volume`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `industry_volume_gallons`
- `chemical.demand.fact_shw_market_share`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `region_id`, `market_share_percent`
- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`

### Q2 2025 (13) Sherwin-Williams

What unfavorable mix drove Performance Coatings price, and was there a mix drag in Consumer Brands as well?

- `chemical.demand.fact_shw_volume_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `coatings_product_id`, `region_id`, `sold_gallons`
- `chemical.demand.fact_shw_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `sales_amount`
- `chemical.demand.fact_industry_coatings_volume`: `fiscal_quarter_id`, `scenario_id`, `shw_end_market_id`, `region_id`, `industry_volume_gallons`

## Ecolab

### Q1 2026 (2) Ecolab

Does the guide assume stable demand with modest improvement, or a more cautious customer posture from energy costs and geopolitics?

- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_customer_retention_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `customer_type_id`, `retained_customer_count`, `base_customer_count`
- `chemical.demand.fact_contractor_backlog`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_end_market_id`, `region_id`, `backlog_job_count`, `backlog_duration_weeks`

### Q1 2026 (3) Ecolab

How is Ovivo tracking versus plan, and what cross-sell exists with core high-tech offerings and with CoolIT?

- `chemical.demand.fact_cross_sell_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `cross_sell_sales_amount`
- `chemical.demand.fact_acquired_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `acquisition_id`, `ecl_reporting_segment_id`, `acquired_sales_amount`, `acquired_sales_change_percent`
- `chemical.demand.fact_ecl_market_share`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `market_share_percent`

### Q1 2026 (4) Ecolab

How much faster is One Ecolab growing than the core, and what would accelerate it further?

- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`
- `chemical.demand.fact_ecl_market_share`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `market_share_percent`

### Q1 2026 (7) Ecolab

How do Ovivo, March raw-material inflation, and softer Heavy and Paper sales combine in Global Water margins?

- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`
- `chemical.demand.fact_cross_sell_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `cross_sell_sales_amount`
- `chemical.demand.fact_acquired_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `acquisition_id`, `ecl_reporting_segment_id`, `acquired_sales_amount`, `acquired_sales_change_percent`

### Q1 2026 (9) Ecolab

Are Paper and basic industries turning because growth is improving or because mill closures have stopped?

- `chemical.demand.fact_site_activity_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `open_site_count`, `closed_site_count`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`
- `chemical.demand.fact_cross_sell_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `cross_sell_sales_amount`

### Q1 2026 (10) Ecolab

How fast is CoolIT growing above 30%, and do data-center competitors emphasize water-treatment chemistry or equipment?

- `chemical.demand.fact_ecl_market_share`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `market_share_percent`
- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`

### Q1 2026 (11) Ecolab

Is CoolIT dilution based on the original 30% growth case or on the much faster current sales rate?

- `chemical.demand.fact_acquired_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `acquisition_id`, `ecl_reporting_segment_id`, `acquired_sales_amount`, `acquired_sales_change_percent`
- `chemical.demand.fact_cross_sell_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `cross_sell_sales_amount`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`

### Q1 2026 (12) Ecolab

What share of pest locations is on the new connected traps?

- `chemical.demand.fact_program_coverage_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `covered_site_count`, `targeted_site_count`, `covered_customer_count`
- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`

### Q1 2026 (15) Ecolab

Has the Middle East conflict changed customer confidence in any end market?

- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_ecl_market_share`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `market_share_percent`
- `chemical.demand.fact_customer_retention_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `customer_type_id`, `retained_customer_count`, `base_customer_count`

### Q1 2026 (17) Ecolab

Will transportation and green energy remain the main drivers of Light Water?

- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`
- `chemical.demand.fact_ecl_market_share`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `market_share_percent`

### Q4 2025 (1) Ecolab

How do paper, basic industries, and institutional inventory headwinds fade through the year against momentum in other businesses?

- `chemical.demand.fact_site_activity_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `open_site_count`, `closed_site_count`
- `chemical.demand.fact_ecl_distributor_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_channel_id`, `distributor_inventory_units`, `inventory_reduction_units`
- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`

### Q4 2025 (2) Ecolab

What growth rate and roadblocks apply to global high tech across water, semiconductors, and data centers after Ovivo?

- `chemical.demand.fact_ecl_market_share`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `market_share_percent`
- `chemical.demand.fact_cross_sell_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `cross_sell_sales_amount`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`

### Q4 2025 (4) Ecolab

Why are light and heavy water diverging, with food and beverage improving and paper still a drag?

- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`
- `chemical.demand.fact_site_activity_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `open_site_count`, `closed_site_count`

### Q4 2025 (5) Ecolab

After normalizing for distributor inventory reductions, are underlying volumes actually rising?

- `chemical.demand.fact_ecl_distributor_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_channel_id`, `distributor_inventory_units`, `inventory_reduction_units`
- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_shw_channel_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `shw_channel_id`, `channel_inventory_gallons`

### Q4 2025 (6) Ecolab

What feedback is coming from the first One Ecolab customers, and when does the rollout to the next cohort become a sales driver?

- `chemical.demand.fact_program_coverage_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `covered_site_count`, `targeted_site_count`, `covered_customer_count`
- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`

### Q4 2025 (7) Ecolab

Where is IQ Suite penetration today versus the level expected in two to three years?

- `chemical.demand.fact_program_coverage_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `covered_site_count`, `targeted_site_count`, `covered_customer_count`
- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`

### Q4 2025 (11) Ecolab

Is the expected acceleration in organic sales from basic industries stabilizing, or from faster growth in the higher-growth platforms as well?

- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`
- `chemical.demand.fact_cross_sell_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `cross_sell_sales_amount`
- `chemical.demand.fact_site_activity_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `open_site_count`, `closed_site_count`

### Q4 2025 (13) Ecolab

How is customer retention trending in Institutional and Specialty?

- `chemical.demand.fact_customer_retention_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `customer_type_id`, `retained_customer_count`, `base_customer_count`
- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`

### Q3 2025 (1) Ecolab

How are data-center share gains being won and measured, and how does Ovivo change that position?

- `chemical.demand.fact_ecl_market_share`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `market_share_percent`
- `chemical.demand.fact_acquired_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `acquisition_id`, `ecl_reporting_segment_id`, `acquired_sales_amount`, `acquired_sales_change_percent`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`

### Q3 2025 (5) Ecolab

Where will One Ecolab stand with the top customers by year-end, and how far does the rollout extend next year?

- `chemical.demand.fact_program_coverage_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `covered_site_count`, `targeted_site_count`, `covered_customer_count`
- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`

### Q3 2025 (7) Ecolab

How long before the faster growth engines are large enough to lift the 85% core that is growing more slowly?

- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`
- `chemical.demand.fact_cross_sell_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `cross_sell_sales_amount`
- `chemical.demand.fact_acquired_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `acquisition_id`, `ecl_reporting_segment_id`, `acquired_sales_amount`, `acquired_sales_change_percent`

### Q3 2025 (9) Ecolab

Did water volume grow, and was basic industries and paper volume down at a high-single-digit rate?

- `chemical.demand.fact_site_activity_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `open_site_count`, `closed_site_count`
- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`

### Q3 2025 (10) Ecolab

How much did One Ecolab cross-sell contribute to organic growth?

- `chemical.demand.fact_cross_sell_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `cross_sell_sales_amount`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`
- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`

### Q3 2025 (11) Ecolab

What underlying food-and-beverage market dynamics sit under the best organic growth in several quarters?

- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`
- `chemical.demand.fact_cross_sell_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_program_id`, `ecl_business_unit_id`, `cross_sell_sales_amount`
- `chemical.demand.fact_ecl_market_share`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `market_share_percent`

### Q3 2025 (12) Ecolab

Have pest customer-acquisition costs or competition from major players stepped up?

- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`
- `chemical.demand.fact_customer_retention_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `customer_type_id`, `retained_customer_count`, `base_customer_count`

### Q3 2025 (14) Ecolab

Is the company equipped for direct-to-chip cooling, or are more bolt-on deals required?

- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`
- `chemical.demand.fact_ecl_market_share`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `market_share_percent`

### Q2 2025 (8) Ecolab

Is the second-half challenge getting better price in water, including paper and heavy industry where volume is contracting?

- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_site_activity_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `open_site_count`, `closed_site_count`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`

### Q2 2025 (11) Ecolab

Does weakness in basic industries require portfolio, resource, or productivity actions, or is the current approach enough?

- `chemical.demand.fact_site_activity_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `site_type_id`, `open_site_count`, `closed_site_count`
- `chemical.demand.fact_ecl_service_volume`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `service_visit_count`, `active_customer_site_count`, `treated_water_gallons`
- `chemical.demand.fact_ecl_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `sales_amount`, `organic_sales_change_percent`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `chemical.time.dim_fiscal_quarter` | supporting population |
| `chemical.time.dim_scenario` | supporting population |
| `chemical.geography.dim_region` | supporting population |
| `chemical.geography.dim_country` | supporting population |
| `chemical.market.dim_shw_reporting_segment` | supporting population |
| `chemical.market.dim_ecl_reporting_segment` | supporting population |
| `chemical.market.dim_shw_end_market` | supporting population |
| `chemical.market.dim_ecl_business_unit` | supporting population |
| `chemical.customer.dim_customer_type` | supporting population |
| `chemical.channel.dim_shw_channel` | supporting population |
| `chemical.channel.dim_ecl_channel` | supporting population |
| `chemical.product.dim_coatings_product` | supporting population |
| `chemical.service.dim_ecl_service_type` | supporting population |
| `chemical.site.dim_site_type` | supporting population |
| `chemical.customer.dim_competitor` | supporting population |
| `chemical.market.dim_weather_regime` | supporting population |
| `chemical.demand.fact_shw_volume_quantity` | Q1 2026 (8), Q1 2026 (12), Q1 2026 (13), Q1 2026 (15), Q4 2025 (1), Q4 2025 (4), Q4 2025 (5), Q4 2025 (7), Q4 2025 (8), Q4 2025 (9), Q4 2025 (10), Q4 2025 (12), Q3 2025 (2), Q3 2025 (5), Q3 2025 (6), Q3 2025 (7), Q3 2025 (8), Q3 2025 (9), Q3 2025 (13), Q3 2025 (14), Q2 2025 (2), Q2 2025 (4), Q2 2025 (6), Q2 2025 (7), Q2 2025 (8), Q2 2025 (9), Q2 2025 (13) |
| `chemical.demand.fact_ecl_service_volume` | Q1 2026 (2), Q1 2026 (4), Q1 2026 (10), Q1 2026 (12), Q1 2026 (15), Q1 2026 (17), Q4 2025 (1), Q4 2025 (4), Q4 2025 (5), Q4 2025 (6), Q4 2025 (7), Q4 2025 (13), Q3 2025 (5), Q3 2025 (9), Q3 2025 (10), Q3 2025 (12), Q3 2025 (14), Q2 2025 (8), Q2 2025 (11) |
| `chemical.demand.fact_shw_sales_amount` | Q1 2026 (8), Q1 2026 (11), Q1 2026 (15), Q4 2025 (1), Q4 2025 (4), Q4 2025 (7), Q4 2025 (8), Q4 2025 (9), Q3 2025 (2), Q3 2025 (5), Q3 2025 (6), Q3 2025 (8), Q3 2025 (9), Q3 2025 (14), Q2 2025 (2), Q2 2025 (4), Q2 2025 (6), Q2 2025 (7), Q2 2025 (8), Q2 2025 (13) |
| `chemical.demand.fact_ecl_sales_amount` | Q1 2026 (4), Q1 2026 (7), Q1 2026 (9), Q1 2026 (10), Q1 2026 (11), Q1 2026 (12), Q1 2026 (17), Q4 2025 (2), Q4 2025 (4), Q4 2025 (6), Q4 2025 (7), Q4 2025 (11), Q4 2025 (13), Q3 2025 (1), Q3 2025 (5), Q3 2025 (7), Q3 2025 (9), Q3 2025 (10), Q3 2025 (11), Q3 2025 (12), Q3 2025 (14), Q2 2025 (8), Q2 2025 (11) |
| `chemical.demand.fact_industry_coatings_volume` | Q1 2026 (11), Q1 2026 (12), Q1 2026 (13), Q4 2025 (1), Q4 2025 (5), Q4 2025 (12), Q3 2025 (7), Q3 2025 (8), Q2 2025 (6), Q2 2025 (7), Q2 2025 (9), Q2 2025 (13) |
| `chemical.demand.fact_shw_market_share` | Q4 2025 (9), Q3 2025 (2), Q3 2025 (7), Q3 2025 (9), Q3 2025 (13), Q3 2025 (14), Q2 2025 (2), Q2 2025 (4), Q2 2025 (9) |
| `chemical.demand.fact_ecl_market_share` | Q3 2025 (13), Q1 2026 (3), Q1 2026 (4), Q1 2026 (10), Q1 2026 (15), Q1 2026 (17), Q4 2025 (2), Q3 2025 (1), Q3 2025 (11), Q3 2025 (14) |
| `chemical.demand.fact_customer_retention_quantity` | Q1 2026 (14), Q1 2026 (2), Q1 2026 (15), Q4 2025 (13), Q3 2025 (12) |
| `chemical.demand.fact_store_traffic_quantity` | supporting population |
| `chemical.demand.fact_contractor_backlog` | Q4 2025 (10), Q3 2025 (5), Q3 2025 (6), Q1 2026 (2) |
| `chemical.demand.fact_site_activity_quantity` | Q1 2026 (11), Q4 2025 (5), Q1 2026 (9), Q4 2025 (1), Q4 2025 (4), Q4 2025 (11), Q3 2025 (9), Q2 2025 (8), Q2 2025 (11) |
| `chemical.demand.fact_program_coverage_quantity` | Q1 2026 (14), Q1 2026 (12), Q4 2025 (6), Q4 2025 (7), Q3 2025 (5) |
| `chemical.demand.fact_cross_sell_amount` | Q1 2026 (3), Q1 2026 (7), Q1 2026 (9), Q1 2026 (11), Q4 2025 (2), Q4 2025 (11), Q3 2025 (7), Q3 2025 (10), Q3 2025 (11) |
| `chemical.demand.fact_acquired_sales_amount` | Q1 2026 (15), Q4 2025 (8), Q4 2025 (12), Q1 2026 (3), Q1 2026 (7), Q1 2026 (11), Q3 2025 (1), Q3 2025 (7) |
| `chemical.demand.fact_weather_affected_volume` | Q1 2026 (12), Q4 2025 (4) |
| `chemical.demand.fact_housing_activity_quantity` | Q1 2026 (8), Q4 2025 (7), Q4 2025 (10), Q2 2025 (8) |
| `chemical.demand.fact_shw_channel_inventory_quantity` | Q1 2026 (13), Q1 2026 (14), Q4 2025 (5) |
| `chemical.demand.fact_ecl_distributor_inventory_quantity` | Q4 2025 (1), Q4 2025 (5) |
