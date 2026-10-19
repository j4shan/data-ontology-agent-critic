# Chemical Inc price and margin

Sherwin-Williams coatings are measured in gallons through company stores and plants, with its own reporting-segment dimension. Ecolab is measured as site service in visits, customer sites, and technician hours, with its own reporting-segment dimension, and is not modeled as a paint-plant operating rate. Quantity and price or margin are separate facts joined by fiscal quarter, scenario, and the business keys. Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks.

## Numbered questions

## Sherwin-Williams

### Q1 2026 (1) Sherwin-Williams

Why is pricing more surgical by customer and end market than in earlier cost-inflation cycles?

- `chemical.price.fact_shw_realized_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `region_id`, `realized_price_dollars_per_gallon`
- `chemical.price.fact_shw_margin_bridge`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `margin_driver_id`, `margin_effect_amount`, `margin_effect_percent`
- `chemical.price.fact_surcharge_coverage_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `price_action_type_id`, `targeted_customer_count`, `approached_customer_count`

### Q1 2026 (4) Sherwin-Williams

Is the volume-guide swing from growth to a low-single-digit decline a rest-of-year market view, and what offsets keep earnings intact?

- `chemical.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `chemical.price.fact_shw_announced_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `price_action_type_id`, `announced_price_change_percent`
- `chemical.price.fact_shw_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`

### Q1 2026 (5) Sherwin-Williams

What is driving the margin improvement in Consumer Brands?

- `chemical.price.fact_shw_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `chemical.price.fact_shw_margin_bridge`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `margin_driver_id`, `margin_effect_amount`, `margin_effect_percent`
- `chemical.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`

### Q1 2026 (6) Sherwin-Williams

Is realization on the January price increase ahead of plan, and are those customer conversations finished?

- `chemical.price.fact_shw_realized_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `region_id`, `realized_price_dollars_per_gallon`
- `chemical.price.fact_shw_announced_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `price_action_type_id`, `announced_price_change_percent`
- `chemical.price.fact_surcharge_coverage_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `price_action_type_id`, `targeted_customer_count`, `approached_customer_count`

### Q1 2026 (7) Sherwin-Williams

What was first-quarter gross-margin expansion excluding Suvenil, and can gross margin rise in each quarter year over year?

- `chemical.price.fact_shw_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `chemical.price.fact_shw_margin_bridge`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `margin_driver_id`, `margin_effect_amount`, `margin_effect_percent`
- `chemical.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`

### Q1 2026 (9) Sherwin-Williams

Is the higher price in the guide only the January increase, or pricing added after early March?

- `chemical.price.fact_shw_announced_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `price_action_type_id`, `announced_price_change_percent`
- `chemical.price.fact_shw_realized_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `region_id`, `realized_price_dollars_per_gallon`
- `chemical.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`

### Q1 2026 (16) Sherwin-Williams

What is distinctive in refinish and EMEA decorative share gains, and is price part of it?

- `chemical.price.fact_competitor_coatings_price`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `coatings_product_id`, `competitor_price_dollars_per_gallon`
- `chemical.price.fact_surcharge_coverage_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `price_action_type_id`, `targeted_customer_count`, `approached_customer_count`
- `chemical.price.fact_shw_realized_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `region_id`, `realized_price_dollars_per_gallon`

### Q4 2025 (3) Sherwin-Williams

Why would fourth-quarter price-mix plus the January increase not produce a larger first-quarter price-mix?

- `chemical.price.fact_shw_realized_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `region_id`, `realized_price_dollars_per_gallon`
- `chemical.price.fact_shw_announced_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `price_action_type_id`, `announced_price_change_percent`
- `chemical.price.fact_shw_margin_bridge`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `margin_driver_id`, `margin_effect_amount`, `margin_effect_percent`

### Q4 2025 (6) Sherwin-Williams

If the emphasis shifts from price to volume, why would competitors not match and erase the share gain?

- `chemical.price.fact_competitor_coatings_price`: `fiscal_quarter_id`, `scenario_id`, `competitor_id`, `coatings_product_id`, `competitor_price_dollars_per_gallon`
- `chemical.price.fact_shw_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `chemical.price.fact_surcharge_coverage_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `price_action_type_id`, `targeted_customer_count`, `approached_customer_count`

### Q4 2025 (11) Sherwin-Williams

Is low-single-digit realization on the 7% increase a near-term rate or the full run rate over the next few quarters?

- `chemical.price.fact_shw_realized_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `region_id`, `realized_price_dollars_per_gallon`
- `chemical.price.fact_shw_announced_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `price_action_type_id`, `announced_price_change_percent`
- `chemical.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`

### Q4 2025 (13) Sherwin-Williams

What volume and price-mix are showing in DIY in the fourth quarter and in the 2026 outlook?

- `chemical.price.fact_shw_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `chemical.price.fact_shw_margin_bridge`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `margin_driver_id`, `margin_effect_amount`, `margin_effect_percent`
- `chemical.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`

### Q4 2025 (14) Sherwin-Williams

What net price tailwind is expected in 2026 versus trend pricing without a sharp cyclical recovery?

- `chemical.price.fact_shw_realized_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `region_id`, `realized_price_dollars_per_gallon`
- `chemical.price.fact_shw_announced_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `price_action_type_id`, `announced_price_change_percent`
- `chemical.price.fact_shw_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`

### Q3 2025 (1) Sherwin-Williams

How was the 7% Paint Stores price increase sized against raw materials and other costs?

- `chemical.price.fact_shw_announced_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `price_action_type_id`, `announced_price_change_percent`
- `chemical.price.fact_shw_realized_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `region_id`, `realized_price_dollars_per_gallon`
- `chemical.price.fact_shw_margin_bridge`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `margin_driver_id`, `margin_effect_amount`, `margin_effect_percent`

### Q3 2025 (10) Sherwin-Williams

Can gross margin hold at or above 50% without a material volume recovery?

- `chemical.price.fact_shw_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `chemical.price.fact_incremental_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `incremental_margin_percent`
- `chemical.price.fact_shw_announced_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `price_action_type_id`, `announced_price_change_percent`

### Q3 2025 (11) Sherwin-Williams

How much does weak volume hurt the gross-margin rate, and what volume growth yields about 100 basis points of leverage?

- `chemical.price.fact_shw_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `chemical.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `chemical.price.fact_incremental_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `incremental_margin_percent`

### Q3 2025 (12) Sherwin-Williams

Is a roughly 30% incremental margin on low-single-digit store volume a useful benchmark for other segments when demand improves?

- `chemical.price.fact_incremental_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `incremental_margin_percent`
- `chemical.price.fact_shw_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `chemical.price.fact_ecl_incremental_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `incremental_margin_percent`

### Q2 2025 (5) Sherwin-Williams

How much of the gross-margin pressure was architectural volume, and what would the rate have been if volume were flat or up?

- `chemical.price.fact_shw_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `chemical.price.fact_incremental_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `incremental_margin_percent`
- `chemical.price.fact_shw_realized_price`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `coatings_product_id`, `region_id`, `realized_price_dollars_per_gallon`

## Ecolab

### Q1 2026 (1) Ecolab

Why is gross margin expected to stabilize in the second half, and how does the energy surcharge fit that path?

- `chemical.price.fact_ecl_announced_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `price_action_type_id`, `announced_price_change_percent`, `surcharge_change_percent`
- `chemical.price.fact_surcharge_coverage_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `price_action_type_id`, `targeted_customer_count`, `approached_customer_count`
- `chemical.price.fact_ecl_operating_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `operating_income_amount`, `operating_margin_percent`

### Q1 2026 (6) Ecolab

What puts and takes sit between current margins and the 2027 targets in Institutional and other markets?

- `chemical.price.fact_ecl_operating_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `operating_income_amount`, `operating_margin_percent`
- `chemical.price.fact_ecl_margin_bridge`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `margin_driver_id`, `margin_effect_amount`, `margin_effect_percent`
- `chemical.price.fact_ecl_incremental_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `incremental_margin_percent`

### Q1 2026 (13) Ecolab

Is value capture rising as a percentage of the portfolio, and is it higher in the newer businesses?

- `chemical.price.fact_value_delivered_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `delivered_value_amount`, `captured_value_amount`
- `chemical.price.fact_ecl_realized_service_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `realized_price_dollars_per_visit`
- `chemical.price.fact_ecl_announced_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `price_action_type_id`, `announced_price_change_percent`, `surcharge_change_percent`

### Q1 2026 (14) Ecolab

What share of customers targeted for the energy surcharge have already been approached?

- `chemical.price.fact_surcharge_coverage_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `price_action_type_id`, `targeted_customer_count`, `approached_customer_count`
- `chemical.price.fact_ecl_announced_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `price_action_type_id`, `announced_price_change_percent`, `surcharge_change_percent`
- `chemical.price.fact_ecl_realized_service_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `realized_price_dollars_per_visit`

### Q4 2025 (3) Ecolab

Why were pest incremental margins much stronger than Life Sciences incremental margins?

- `chemical.price.fact_ecl_incremental_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `incremental_margin_percent`
- `chemical.price.fact_ecl_operating_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `operating_income_amount`, `operating_margin_percent`
- `chemical.price.fact_incremental_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `incremental_margin_percent`

### Q4 2025 (8) Ecolab

What would push results to the high or low end of the 2026 guide?

- `chemical.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `chemical.price.fact_ecl_realized_service_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `realized_price_dollars_per_visit`
- `chemical.price.fact_ecl_announced_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `price_action_type_id`, `announced_price_change_percent`, `surcharge_change_percent`

### Q4 2025 (9) Ecolab

Does the 2025 tariff surcharge create a larger price contribution in the first half of 2026 than in the second half?

- `chemical.price.fact_ecl_announced_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `price_action_type_id`, `announced_price_change_percent`, `surcharge_change_percent`
- `chemical.price.fact_surcharge_coverage_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `price_action_type_id`, `targeted_customer_count`, `approached_customer_count`
- `chemical.price.fact_ecl_realized_service_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `realized_price_dollars_per_visit`

### Q4 2025 (12) Ecolab

Is the Life Sciences margin setback from the capability build a multi-quarter drag or a one-quarter dip?

- `chemical.price.fact_ecl_operating_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `operating_income_amount`, `operating_margin_percent`
- `chemical.price.fact_ecl_incremental_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `incremental_margin_percent`
- `chemical.price.fact_ecl_margin_bridge`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `margin_driver_id`, `margin_effect_amount`, `margin_effect_percent`

### Q3 2025 (3) Ecolab

Excluding the tariff surcharge, is underlying price getting easier because the value case is clearer, or harder because of price fatigue?

- `chemical.price.fact_value_delivered_amount`: `fiscal_quarter_id`, `scenario_id`, `ecl_business_unit_id`, `delivered_value_amount`, `captured_value_amount`
- `chemical.price.fact_ecl_announced_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `price_action_type_id`, `announced_price_change_percent`, `surcharge_change_percent`
- `chemical.price.fact_surcharge_coverage_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `price_action_type_id`, `targeted_customer_count`, `approached_customer_count`

### Q3 2025 (4) Ecolab

How is the water top line flowing through segment margin, split across the businesses inside water?

- `chemical.price.fact_ecl_incremental_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `incremental_margin_percent`
- `chemical.price.fact_incremental_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `incremental_margin_percent`
- `chemical.price.fact_ecl_realized_service_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `realized_price_dollars_per_visit`

### Q3 2025 (6) Ecolab

As pest and Life Sciences lap growth investments, is SG&A leverage a straight line to the 2027 targets or another step-up in spend?

- `chemical.price.fact_ecl_operating_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `operating_income_amount`, `operating_margin_percent`
- `chemical.price.fact_ecl_incremental_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `incremental_margin_percent`
- `chemical.price.fact_ecl_margin_bridge`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `margin_driver_id`, `margin_effect_amount`, `margin_effect_percent`

### Q3 2025 (8) Ecolab

How much of the price surcharge was realized, and does roughly 3% pricing persist for the next few quarters?

- `chemical.price.fact_ecl_realized_service_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `realized_price_dollars_per_visit`
- `chemical.price.fact_ecl_announced_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `price_action_type_id`, `announced_price_change_percent`, `surcharge_change_percent`
- `chemical.price.fact_surcharge_coverage_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `price_action_type_id`, `targeted_customer_count`, `approached_customer_count`

### Q3 2025 (13) Ecolab

Can low-to-mid-teens earnings growth still be reached with little volume growth, as in the prior price-led case?

- `chemical.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `chemical.price.fact_ecl_margin_bridge`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `margin_driver_id`, `margin_effect_amount`, `margin_effect_percent`
- `chemical.price.fact_incremental_margin`: `fiscal_quarter_id`, `scenario_id`, `shw_reporting_segment_id`, `incremental_margin_percent`

### Q2 2025 (1) Ecolab

What puts and takes kept the second-half outlook from moving up after an in-line quarter?

- `chemical.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `chemical.price.fact_ecl_realized_service_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `realized_price_dollars_per_visit`
- `chemical.price.fact_ecl_announced_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `price_action_type_id`, `announced_price_change_percent`, `surcharge_change_percent`

### Q2 2025 (2) Ecolab

Why did pricing land near 2% rather than a higher rate, and what pricing is expected in the second half?

- `chemical.price.fact_ecl_realized_service_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `realized_price_dollars_per_visit`
- `chemical.price.fact_ecl_announced_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `price_action_type_id`, `announced_price_change_percent`, `surcharge_change_percent`
- `chemical.price.fact_ecl_operating_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `operating_income_amount`, `operating_margin_percent`

### Q2 2025 (5) Ecolab

Is about half of the announced U.S. surcharge still expected to be realized, and are competitors supporting it?

- `chemical.price.fact_ecl_announced_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `price_action_type_id`, `announced_price_change_percent`, `surcharge_change_percent`
- `chemical.price.fact_ecl_realized_service_price`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `ecl_business_unit_id`, `ecl_service_type_id`, `site_type_id`, `region_id`, `realized_price_dollars_per_visit`
- `chemical.price.fact_surcharge_coverage_quantity`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `price_action_type_id`, `targeted_customer_count`, `approached_customer_count`

### Q2 2025 (6) Ecolab

What is pulling Institutional and Life Sciences margins up despite a sluggish macro and growth spend?

- `chemical.price.fact_ecl_operating_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `operating_income_amount`, `operating_margin_percent`
- `chemical.price.fact_ecl_margin_bridge`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `margin_driver_id`, `margin_effect_amount`, `margin_effect_percent`
- `chemical.price.fact_ecl_incremental_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `incremental_margin_percent`

### Q2 2025 (7) Ecolab

Does confidence in the operating-margin target hold if volume stays near 1% inside roughly 3% organic growth?

- `chemical.price.fact_ecl_operating_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `operating_income_amount`, `operating_margin_percent`
- `chemical.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `chemical.price.fact_ecl_margin_bridge`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `margin_driver_id`, `margin_effect_amount`, `margin_effect_percent`

### Q2 2025 (9) Ecolab

What is driving the expected sequential drop in Life Sciences margin from nearly 20% back toward the mid-teens?

- `chemical.price.fact_ecl_operating_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `operating_income_amount`, `operating_margin_percent`
- `chemical.price.fact_ecl_incremental_margin`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `incremental_margin_percent`
- `chemical.price.fact_ecl_margin_bridge`: `fiscal_quarter_id`, `scenario_id`, `ecl_reporting_segment_id`, `margin_driver_id`, `margin_effect_amount`, `margin_effect_percent`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `chemical.price.dim_coating_raw_input` | supporting population |
| `chemical.price.dim_ecl_raw_input` | supporting population |
| `chemical.price.dim_price_action_type` | supporting population |
| `chemical.price.dim_currency` | supporting population |
| `chemical.price.dim_margin_driver` | supporting population |
| `chemical.program.dim_ecl_program` | supporting population |
| `chemical.price.fact_shw_realized_price` | Q1 2026 (1), Q1 2026 (6), Q1 2026 (9), Q1 2026 (16), Q4 2025 (3), Q4 2025 (11), Q4 2025 (14), Q3 2025 (1), Q2 2025 (5) |
| `chemical.price.fact_ecl_realized_service_price` | Q1 2026 (13), Q1 2026 (14), Q4 2025 (8), Q4 2025 (9), Q3 2025 (4), Q3 2025 (8), Q2 2025 (1), Q2 2025 (2), Q2 2025 (5) |
| `chemical.price.fact_shw_announced_price` | Q1 2026 (4), Q1 2026 (6), Q1 2026 (9), Q4 2025 (3), Q4 2025 (11), Q4 2025 (14), Q3 2025 (1), Q3 2025 (10) |
| `chemical.price.fact_ecl_announced_price` | Q1 2026 (1), Q1 2026 (13), Q1 2026 (14), Q4 2025 (8), Q4 2025 (9), Q3 2025 (3), Q3 2025 (8), Q2 2025 (1), Q2 2025 (2), Q2 2025 (5) |
| `chemical.price.fact_surcharge_coverage_quantity` | Q1 2026 (1), Q1 2026 (6), Q1 2026 (16), Q4 2025 (6), Q1 2026 (1), Q1 2026 (14), Q4 2025 (9), Q3 2025 (3), Q3 2025 (8), Q2 2025 (5) |
| `chemical.price.fact_shw_gross_margin` | Q1 2026 (4), Q1 2026 (5), Q1 2026 (7), Q4 2025 (6), Q4 2025 (13), Q4 2025 (14), Q3 2025 (10), Q3 2025 (11), Q3 2025 (12), Q2 2025 (5) |
| `chemical.price.fact_ecl_operating_margin` | Q1 2026 (1), Q1 2026 (6), Q4 2025 (3), Q4 2025 (12), Q3 2025 (6), Q2 2025 (2), Q2 2025 (6), Q2 2025 (7), Q2 2025 (9) |
| `chemical.price.fact_shw_margin_bridge` | Q1 2026 (1), Q1 2026 (5), Q1 2026 (7), Q4 2025 (3), Q4 2025 (13), Q3 2025 (1) |
| `chemical.price.fact_ecl_margin_bridge` | Q1 2026 (6), Q4 2025 (12), Q3 2025 (6), Q3 2025 (13), Q2 2025 (6), Q2 2025 (7), Q2 2025 (9) |
| `chemical.price.fact_enterprise_earnings` | Q1 2026 (4), Q1 2026 (5), Q1 2026 (7), Q1 2026 (9), Q4 2025 (11), Q4 2025 (13), Q3 2025 (11), Q4 2025 (8), Q3 2025 (13), Q2 2025 (1), Q2 2025 (7) |
| `chemical.price.fact_value_delivered_amount` | Q1 2026 (13), Q3 2025 (3) |
| `chemical.price.fact_competitor_coatings_price` | Q1 2026 (16), Q4 2025 (6) |
| `chemical.price.fact_incremental_margin` | Q3 2025 (10), Q3 2025 (11), Q3 2025 (12), Q2 2025 (5), Q4 2025 (3), Q3 2025 (4), Q3 2025 (13) |
| `chemical.price.fact_ecl_incremental_margin` | Q3 2025 (12), Q1 2026 (6), Q4 2025 (3), Q4 2025 (12), Q3 2025 (4), Q3 2025 (6), Q2 2025 (6), Q2 2025 (9) |
