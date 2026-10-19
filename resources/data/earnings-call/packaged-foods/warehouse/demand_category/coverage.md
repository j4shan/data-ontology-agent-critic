# Food Inc category demand

General Mills and Mondelez each have their own reporting-segment dimension and brand dimension, and North America Retail appears only as a General Mills reporting segment, not as a channel. Realized price per pound or per kilogram shares brand and region keys with the matching brand-volume fact, and cocoa and wheat are carried as quantity at risk in tonnes beside cost per tonne. Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks.

## Numbered questions

## General Mills

### Q1 FY2027 (1) General Mills

Should North America Retail improve further from the minus 2% retail consumption in the quarter, or stabilize around that rate?

- `food.demand.fact_gis_consumption_quantity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `channel_id`, `region_id`, `consumption_pounds`
- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_volume_share`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `volume_share_percent`, `value_share_percent`

### Q1 FY2027 (2) General Mills

Versus a year ago, in how many North America Retail categories are volume and share still negative, and what is the fix in the remaining problem categories?

- `food.demand.fact_gis_volume_share`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `volume_share_percent`, `value_share_percent`
- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_consumption_quantity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `channel_id`, `region_id`, `consumption_pounds`

### Q1 FY2027 (4) General Mills

How much of the low-single-digit pet headwind is caution versus the first quarter simply having a smaller retailer-inventory hit than expected, aside from the extra month of Whitebridge?

- `food.demand.fact_retailer_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `retailer_id`, `gis_category_id`, `channel_id`, `retailer_inventory_case_count`, `inventory_reduction_case_count`
- `food.demand.fact_cohort_consumption_quantity`: `fiscal_quarter_id`, `scenario_id`, `income_cohort_id`, `gis_category_id`, `cohort_consumption_pounds`
- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`

### Q1 FY2027 (5) General Mills

How incremental was Love Made Fresh in dog food, and is the high-single-digit dog-food decline mostly Wilderness or other lines?

- `food.demand.fact_gis_brand_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `gis_category_id`, `channel_id`, `region_id`, `brand_volume_pounds`
- `food.demand.fact_distribution_quantity`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `channel_id`, `retail_door_count`
- `food.demand.fact_on_shelf_availability`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `channel_id`, `on_shelf_availability_percent`

### Q1 FY2027 (6) General Mills

How is the small wet-dog-food business performing?

- `food.demand.fact_gis_brand_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `gis_category_id`, `channel_id`, `region_id`, `brand_volume_pounds`
- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_shipment_quantity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `shipment_pounds`

### Q1 FY2027 (7) General Mills

Which innovation and renovation is tracking ahead of plan, what that says about the consumer, and what cereal acceleration is still to come?

- `food.demand.fact_innovation_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `innovation_type_id`, `innovation_sales_amount`, `innovation_sales_change_percent`
- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_elasticity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `income_cohort_id`, `elasticity_coefficient`, `trade_down_percent`

### Q1 FY2027 (9) General Mills

Have pricing plans changed from the start of the year after better foodservice and pet pricing, in the current inflation backdrop?

- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `sales_amount`, `organic_sales_change_percent`
- `food.demand.fact_innovation_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `innovation_type_id`, `innovation_sales_amount`, `innovation_sales_change_percent`

### Q1 FY2027 (15) General Mills

As shoppers use AI-generated lists at Instacart and Kroger, how does the company stay selected when the decision happens off the physical shelf?

- `food.demand.fact_gis_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `sales_amount`, `organic_sales_change_percent`
- `food.demand.fact_distribution_quantity`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `channel_id`, `retail_door_count`
- `food.demand.fact_on_shelf_availability`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `channel_id`, `on_shelf_availability_percent`

### Q1 FY2027 (16) General Mills

In pet, how much of the pressure is cyclical household and vet-visit softness versus the structural aging of large dogs where the margin sits?

- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_brand_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `gis_category_id`, `channel_id`, `region_id`, `brand_volume_pounds`
- `food.demand.fact_gis_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `sales_amount`, `organic_sales_change_percent`

### Q4 FY2026 (4) General Mills

How far below the full-year organic-sales guide should the first quarter start, and how does growth phase after that?

- `food.demand.fact_gis_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `sales_amount`, `organic_sales_change_percent`
- `food.demand.fact_mdlz_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `mdlz_category_id`, `sales_amount`, `organic_sales_change_percent`
- `food.demand.fact_mdlz_shipment_quantity`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `shipment_kilograms`

### Q4 FY2026 (5) General Mills

What should be expected for volume share and value share?

- `food.demand.fact_gis_volume_share`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `volume_share_percent`, `value_share_percent`
- `food.demand.fact_mdlz_volume_share`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `volume_share_percent`, `value_share_percent`
- `food.demand.fact_glp_affected_volume`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `health_cohort_id`, `region_id`, `affected_volume_kilograms`

### Q4 FY2026 (6) General Mills

If North America Retail dollar-share losses are not mainly private label, how much has gone to smaller insurgent brands, and how does the remarkability work take it back?

- `food.demand.fact_gis_volume_share`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `volume_share_percent`, `value_share_percent`
- `food.demand.fact_retailer_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `retailer_id`, `gis_category_id`, `channel_id`, `retailer_inventory_case_count`, `inventory_reduction_case_count`
- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`

### Q4 FY2026 (9) General Mills

How do at-home spending trends differ by income cohort, and where does improvement come from in fiscal 2027?

- `food.demand.fact_cohort_consumption_quantity`: `fiscal_quarter_id`, `scenario_id`, `income_cohort_id`, `gis_category_id`, `cohort_consumption_pounds`
- `food.demand.fact_gis_elasticity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `income_cohort_id`, `elasticity_coefficient`, `trade_down_percent`
- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`

### Q4 FY2026 (12) General Mills

What has to happen to reach the high end of the organic-sales range and positive growth for the year?

- `food.demand.fact_gis_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `sales_amount`, `organic_sales_change_percent`
- `food.demand.fact_mdlz_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `mdlz_category_id`, `sales_amount`, `organic_sales_change_percent`
- `food.demand.fact_mdlz_shipment_quantity`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `shipment_kilograms`

### Q4 FY2026 (13) General Mills

Is there visibility that pet retailer-inventory swings will smooth out, given consumption has been healthier than reported results?

- `food.demand.fact_gis_shipment_quantity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `shipment_pounds`
- `food.demand.fact_retailer_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `retailer_id`, `gis_category_id`, `channel_id`, `retailer_inventory_case_count`, `inventory_reduction_case_count`
- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`

### Q3 FY2026 (2) General Mills

What have competitors done in key categories after General Mills' price investments, given category price/mix stayed positive?

- `food.demand.fact_gis_elasticity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `income_cohort_id`, `elasticity_coefficient`, `trade_down_percent`
- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_shipment_quantity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `shipment_pounds`

### Q3 FY2026 (3) General Mills

How is this year's innovation tracking against the 25% growth goal, and what should seasonal events and early fiscal 2027 commentary imply?

- `food.demand.fact_innovation_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `innovation_type_id`, `innovation_sales_amount`, `innovation_sales_change_percent`
- `food.demand.fact_gis_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `sales_amount`, `organic_sales_change_percent`
- `food.demand.fact_cohort_consumption_quantity`: `fiscal_quarter_id`, `scenario_id`, `income_cohort_id`, `gis_category_id`, `cohort_consumption_pounds`

### Q3 FY2026 (4) General Mills

How large is the recent Love Made Fresh acceleration, how much more distribution is available, and how is on-shelf availability tracking?

- `food.demand.fact_on_shelf_availability`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `channel_id`, `on_shelf_availability_percent`
- `food.demand.fact_distribution_quantity`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `channel_id`, `retail_door_count`
- `food.demand.fact_gis_brand_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `gis_category_id`, `channel_id`, `region_id`, `brand_volume_pounds`

### Q3 FY2026 (8) General Mills

Is positive organic revenue growth in the fourth quarter still reachable for the total company, North America Retail, or both, or has the language moved to only improved trends?

- `food.demand.fact_gis_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `sales_amount`, `organic_sales_change_percent`
- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_consumption_quantity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `channel_id`, `region_id`, `consumption_pounds`

### Q3 FY2026 (9) General Mills

Is foodservice weakness in bakery flour volumes likely to persist, and what does it say about that channel?

- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_brand_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `gis_category_id`, `channel_id`, `region_id`, `brand_volume_pounds`
- `food.demand.fact_gis_volume_share`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `volume_share_percent`, `value_share_percent`

### Q3 FY2026 (10) General Mills

After hitting the cooler-distribution goal for Love Made Fresh, is the next step more doors or higher turns in doors already won?

- `food.demand.fact_distribution_quantity`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `channel_id`, `retail_door_count`
- `food.demand.fact_on_shelf_availability`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `channel_id`, `on_shelf_availability_percent`
- `food.demand.fact_gis_brand_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `gis_category_id`, `channel_id`, `region_id`, `brand_volume_pounds`

### Q3 FY2026 (12) General Mills

Excluding Totino's, is the snacks business stable?

- `food.demand.fact_gis_brand_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `gis_category_id`, `channel_id`, `region_id`, `brand_volume_pounds`
- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_shipment_quantity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `shipment_pounds`

### Q3 FY2026 (13) General Mills

Which parts of North America Retail and pet were hit by retailer inventory adjustments, and how does each reverse in the fourth quarter?

- `food.demand.fact_retailer_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `retailer_id`, `gis_category_id`, `channel_id`, `retailer_inventory_case_count`, `inventory_reduction_case_count`
- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `sales_amount`, `organic_sales_change_percent`

### Q3 FY2026 (14) General Mills

What swing factors could push fourth-quarter results toward either end of a wide implied range while the full-year guide is held?

- `food.demand.fact_gis_shipment_quantity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `shipment_pounds`
- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_brand_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `gis_category_id`, `channel_id`, `region_id`, `brand_volume_pounds`

### Q2 FY2026 (2) General Mills

How fast should the gap between improving volume share and value share narrow in the third and fourth quarters as last year's prices are lapped, where should that stand entering fiscal 2027, and how does a higher cost of volume affect price/mix?

- `food.demand.fact_gis_volume_share`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `volume_share_percent`, `value_share_percent`
- `food.demand.fact_mdlz_volume_share`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `volume_share_percent`, `value_share_percent`
- `food.demand.fact_glp_affected_volume`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `health_cohort_id`, `region_id`, `affected_volume_kilograms`

### Q2 FY2026 (3) General Mills

How is consumer behavior in the broader dog-feeding category, which has been weaker than hoped, even as core pet improves?

- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_elasticity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `income_cohort_id`, `elasticity_coefficient`, `trade_down_percent`
- `food.demand.fact_gis_brand_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `gis_category_id`, `channel_id`, `region_id`, `brand_volume_pounds`

### Q2 FY2026 (6) General Mills

Beyond the first-quarter international timing benefit that was due to unwind, were there incremental timing tailwinds or headwinds in the second quarter?

- `food.demand.fact_gis_brand_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `gis_category_id`, `channel_id`, `region_id`, `brand_volume_pounds`
- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_shipment_quantity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `shipment_pounds`

### Q2 FY2026 (7) General Mills

Is Love Made Fresh helping the Blue Buffalo base business, or are the two still separate?

- `food.demand.fact_gis_brand_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `gis_category_id`, `channel_id`, `region_id`, `brand_volume_pounds`
- `food.demand.fact_distribution_quantity`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `channel_id`, `retail_door_count`
- `food.demand.fact_on_shelf_availability`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `channel_id`, `on_shelf_availability_percent`

### Q2 FY2026 (9) General Mills

How is the higher cost of volume, expected to pressure third-quarter margins, embedded in the reaffirmed full-year outlook?

- `food.demand.fact_glp_affected_volume`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `health_cohort_id`, `region_id`, `affected_volume_kilograms`
- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_brand_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `gis_category_id`, `channel_id`, `region_id`, `brand_volume_pounds`

### Q2 FY2026 (10) General Mills

Have category pounds, which were lagging the full-year view because of a few categories, improved in the quarter?

- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_brand_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `gis_category_id`, `channel_id`, `region_id`, `brand_volume_pounds`
- `food.demand.fact_gis_shipment_quantity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `shipment_pounds`

### Q2 FY2026 (12) General Mills

What is the current Wilderness strategy, and what changes are possible?

- `food.demand.fact_gis_brand_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `gis_category_id`, `channel_id`, `region_id`, `brand_volume_pounds`
- `food.demand.fact_gis_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `sales_amount`, `organic_sales_change_percent`
- `food.demand.fact_innovation_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `innovation_type_id`, `innovation_sales_amount`, `innovation_sales_change_percent`

### Q2 FY2026 (13) General Mills

Which North America Retail and pet consumption measures would indicate that profit growth is realistic in fiscal 2027 after the volume-recovery year?

- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `sales_amount`, `organic_sales_change_percent`
- `food.demand.fact_gis_consumption_quantity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `channel_id`, `region_id`, `consumption_pounds`

### Q2 FY2026 (15) General Mills

Which unmeasured channels are taking pet share from traditional channels?

- `food.demand.fact_gis_category_volume`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `region_id`, `volume_pounds`, `volume_case_count`
- `food.demand.fact_gis_volume_share`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `volume_share_percent`, `value_share_percent`
- `food.demand.fact_gis_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `sales_amount`, `organic_sales_change_percent`

## Mondelez

### Q1 2026 (1) Mondelez

What is driving emerging markets, and where are developed markets improving, including the return to volume-share growth in European chocolate and the March inflection in U.S. biscuits that justified flexibility in the 2026 guide?

- `food.demand.fact_mdlz_category_volume`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `mdlz_category_id`, `region_id`, `volume_kilograms`
- `food.demand.fact_mdlz_volume_share`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `volume_share_percent`, `value_share_percent`
- `food.demand.fact_mdlz_brand_volume`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `mdlz_category_id`, `channel_id`, `region_id`, `brand_volume_kilograms`

### Q1 2026 (5) Mondelez

What price elasticity and trade-down is showing up by European market, given a fragile consumer but only a small organic-sales decline?

- `food.demand.fact_mdlz_elasticity`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `market_development_id`, `elasticity_coefficient`, `trade_down_percent`
- `food.demand.fact_gis_elasticity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `income_cohort_id`, `elasticity_coefficient`, `trade_down_percent`
- `food.demand.fact_mdlz_shipment_quantity`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `shipment_kilograms`

### Q1 2026 (7) Mondelez

Where is the innovation focus now that supply disruption is behind the company, and which consumer insights are shaping it?

- `food.demand.fact_mdlz_innovation_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `innovation_type_id`, `innovation_sales_amount`
- `food.demand.fact_innovation_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `innovation_type_id`, `innovation_sales_amount`, `innovation_sales_change_percent`
- `food.demand.fact_mdlz_elasticity`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `market_development_id`, `elasticity_coefficient`, `trade_down_percent`

### Q1 2026 (8) Mondelez

Can North America improve toward low-single-digit growth this year even if U.S. consumer confidence weakens because of the Middle East conflict?

- `food.demand.fact_mdlz_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `mdlz_category_id`, `sales_amount`, `organic_sales_change_percent`
- `food.demand.fact_mdlz_consumption_quantity`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `consumption_kilograms`
- `food.demand.fact_gis_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gis_category_id`, `sales_amount`, `organic_sales_change_percent`

### Q4 2025 (7) Mondelez

What will grow Latin America volumes after a couple of down years, and what volume assumption is in guidance?

- `food.demand.fact_mdlz_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `mdlz_category_id`, `sales_amount`, `organic_sales_change_percent`
- `food.demand.fact_glp_affected_volume`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `health_cohort_id`, `region_id`, `affected_volume_kilograms`
- `food.demand.fact_mdlz_category_volume`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `mdlz_category_id`, `region_id`, `volume_kilograms`

### Q4 2025 (8) Mondelez

In which regions should the 2026 volume trajectory change show up, and are North America channel strategies a material driver?

- `food.demand.fact_mdlz_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `mdlz_category_id`, `sales_amount`, `organic_sales_change_percent`
- `food.demand.fact_glp_affected_volume`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `health_cohort_id`, `region_id`, `affected_volume_kilograms`
- `food.demand.fact_mdlz_consumption_quantity`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `consumption_kilograms`

### Q3 2025 (1) Mondelez

How is European pricing landing into year-end and next year, including price-gap management in specific markets?

- `food.demand.fact_mdlz_elasticity`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `market_development_id`, `elasticity_coefficient`, `trade_down_percent`
- `food.demand.fact_mdlz_brand_volume`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `mdlz_category_id`, `channel_id`, `region_id`, `brand_volume_kilograms`
- `food.demand.fact_mdlz_volume_share`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `volume_share_percent`, `value_share_percent`

### Q3 2025 (2) Mondelez

With cocoa largely locked, what drove the fourth-quarter outlook change, and what are the puts and takes for next year's organic sales given planned investment and elasticity?

- `food.demand.fact_mdlz_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `mdlz_category_id`, `sales_amount`, `organic_sales_change_percent`
- `food.demand.fact_mdlz_shipment_quantity`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `shipment_kilograms`
- `food.demand.fact_mdlz_consumption_quantity`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `consumption_kilograms`

### Q3 2025 (3) Mondelez

What is the path for the U.S. business back to growth?

- `food.demand.fact_mdlz_volume_share`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `volume_share_percent`, `value_share_percent`
- `food.demand.fact_mdlz_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `mdlz_category_id`, `sales_amount`, `organic_sales_change_percent`
- `food.demand.fact_mdlz_category_volume`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `mdlz_category_id`, `region_id`, `volume_kilograms`

### Q3 2025 (5) Mondelez

In emerging markets, where is elasticity showing fatigue or price-gap problems versus behaving as expected?

- `food.demand.fact_mdlz_elasticity`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `market_development_id`, `elasticity_coefficient`, `trade_down_percent`
- `food.demand.fact_mdlz_category_volume`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `mdlz_category_id`, `region_id`, `volume_kilograms`
- `food.demand.fact_mdlz_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `mdlz_category_id`, `sales_amount`, `organic_sales_change_percent`

### Q3 2025 (6) Mondelez

Is the implied fourth-quarter organic-sales step-up mostly Europe, and what is expected in North America given softer recent scanner data?

- `food.demand.fact_mdlz_consumption_quantity`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `consumption_kilograms`
- `food.demand.fact_mdlz_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `mdlz_category_id`, `sales_amount`, `organic_sales_change_percent`
- `food.demand.fact_mdlz_shipment_quantity`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `shipment_kilograms`

### Q3 2025 (9) Mondelez

Is emphasizing value while protecting the profit pool the right North America approach over the next six to twelve months, or do price investment and profit protection have to be traded off?

- `food.demand.fact_glp_affected_volume`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `health_cohort_id`, `region_id`, `affected_volume_kilograms`
- `food.demand.fact_retailer_inventory_quantity`: `fiscal_quarter_id`, `scenario_id`, `retailer_id`, `gis_category_id`, `channel_id`, `retailer_inventory_case_count`, `inventory_reduction_case_count`
- `food.demand.fact_mdlz_consumption_quantity`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `consumption_kilograms`

### Q2 2025 (3) Mondelez

If U.S. biscuit category volume stays down while prices rise and the consumer is under pressure, how much U.S. pricing is planned and where could that flex the wrong way?

- `food.demand.fact_mdlz_category_volume`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `mdlz_category_id`, `region_id`, `volume_kilograms`
- `food.demand.fact_mdlz_elasticity`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `market_development_id`, `elasticity_coefficient`, `trade_down_percent`
- `food.demand.fact_gis_elasticity`: `fiscal_quarter_id`, `scenario_id`, `gis_category_id`, `region_id`, `income_cohort_id`, `elasticity_coefficient`, `trade_down_percent`

### Q2 2025 (4) Mondelez

How is GLP-1 use, including expected pill forms, affecting indulgent snacking, and could North America volume stay under pressure?

- `food.demand.fact_glp_affected_volume`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `health_cohort_id`, `region_id`, `affected_volume_kilograms`
- `food.demand.fact_mdlz_consumption_quantity`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `consumption_kilograms`
- `food.demand.fact_mdlz_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `mdlz_category_id`, `sales_amount`, `organic_sales_change_percent`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `food.time.dim_fiscal_quarter` | supporting population |
| `food.time.dim_scenario` | supporting population |
| `food.geography.dim_region` | supporting population |
| `food.geography.dim_market_development` | supporting population |
| `food.geography.dim_country` | supporting population |
| `food.segment.dim_gis_reporting_segment` | supporting population |
| `food.segment.dim_mdlz_reporting_segment` | supporting population |
| `food.category.dim_gis_category` | supporting population |
| `food.category.dim_mdlz_category` | supporting population |
| `food.brand.dim_gis_brand` | supporting population |
| `food.brand.dim_mdlz_brand` | supporting population |
| `food.channel.dim_channel` | supporting population |
| `food.channel.dim_retailer` | supporting population |
| `food.consumer.dim_income_cohort` | supporting population |
| `food.consumer.dim_health_cohort` | supporting population |
| `food.consumer.dim_competitor_type` | supporting population |
| `food.innovation.dim_innovation_type` | supporting population |
| `food.demand.fact_gis_category_volume` | Q1 FY2027 (1), Q1 FY2027 (2), Q1 FY2027 (4), Q1 FY2027 (6), Q1 FY2027 (7), Q1 FY2027 (9), Q1 FY2027 (16), Q4 FY2026 (6), Q4 FY2026 (9), Q4 FY2026 (13), Q3 FY2026 (2), Q3 FY2026 (8), Q3 FY2026 (9), Q3 FY2026 (12), Q3 FY2026 (13), Q3 FY2026 (14), Q2 FY2026 (3), Q2 FY2026 (6), Q2 FY2026 (9), Q2 FY2026 (10), Q2 FY2026 (13), Q2 FY2026 (15) |
| `food.demand.fact_mdlz_category_volume` | Q1 2026 (1), Q4 2025 (7), Q3 2025 (3), Q3 2025 (5), Q2 2025 (3) |
| `food.demand.fact_gis_brand_volume` | Q1 FY2027 (5), Q1 FY2027 (6), Q1 FY2027 (16), Q3 FY2026 (4), Q3 FY2026 (9), Q3 FY2026 (10), Q3 FY2026 (12), Q3 FY2026 (14), Q2 FY2026 (3), Q2 FY2026 (6), Q2 FY2026 (7), Q2 FY2026 (9), Q2 FY2026 (10), Q2 FY2026 (12) |
| `food.demand.fact_mdlz_brand_volume` | Q1 2026 (1), Q3 2025 (1) |
| `food.demand.fact_gis_shipment_quantity` | Q1 FY2027 (6), Q4 FY2026 (13), Q3 FY2026 (2), Q3 FY2026 (12), Q3 FY2026 (14), Q2 FY2026 (6), Q2 FY2026 (10) |
| `food.demand.fact_mdlz_shipment_quantity` | Q4 FY2026 (4), Q4 FY2026 (12), Q1 2026 (5), Q3 2025 (2), Q3 2025 (6) |
| `food.demand.fact_gis_consumption_quantity` | Q1 FY2027 (1), Q1 FY2027 (2), Q3 FY2026 (8), Q2 FY2026 (13) |
| `food.demand.fact_mdlz_consumption_quantity` | Q1 2026 (8), Q4 2025 (8), Q3 2025 (2), Q3 2025 (6), Q3 2025 (9), Q2 2025 (4) |
| `food.demand.fact_gis_volume_share` | Q1 FY2027 (1), Q1 FY2027 (2), Q4 FY2026 (5), Q4 FY2026 (6), Q3 FY2026 (9), Q2 FY2026 (2), Q2 FY2026 (15) |
| `food.demand.fact_mdlz_volume_share` | Q4 FY2026 (5), Q2 FY2026 (2), Q1 2026 (1), Q3 2025 (1), Q3 2025 (3) |
| `food.demand.fact_gis_sales_amount` | Q1 FY2027 (9), Q1 FY2027 (15), Q1 FY2027 (16), Q4 FY2026 (4), Q4 FY2026 (12), Q3 FY2026 (3), Q3 FY2026 (8), Q3 FY2026 (13), Q2 FY2026 (12), Q2 FY2026 (13), Q2 FY2026 (15), Q1 2026 (8) |
| `food.demand.fact_mdlz_sales_amount` | Q4 FY2026 (4), Q4 FY2026 (12), Q1 2026 (8), Q4 2025 (7), Q4 2025 (8), Q3 2025 (2), Q3 2025 (3), Q3 2025 (5), Q3 2025 (6), Q2 2025 (4) |
| `food.demand.fact_gis_elasticity` | Q1 FY2027 (7), Q4 FY2026 (9), Q3 FY2026 (2), Q2 FY2026 (3), Q1 2026 (5), Q2 2025 (3) |
| `food.demand.fact_mdlz_elasticity` | Q1 2026 (5), Q1 2026 (7), Q3 2025 (1), Q3 2025 (5), Q2 2025 (3) |
| `food.demand.fact_cohort_consumption_quantity` | Q1 FY2027 (4), Q4 FY2026 (9), Q3 FY2026 (3) |
| `food.demand.fact_glp_affected_volume` | Q4 FY2026 (5), Q2 FY2026 (2), Q2 FY2026 (9), Q4 2025 (7), Q4 2025 (8), Q3 2025 (9), Q2 2025 (4) |
| `food.demand.fact_innovation_sales_amount` | Q1 FY2027 (7), Q1 FY2027 (9), Q3 FY2026 (3), Q2 FY2026 (12), Q1 2026 (7) |
| `food.demand.fact_retailer_inventory_quantity` | Q1 FY2027 (4), Q4 FY2026 (6), Q4 FY2026 (13), Q3 FY2026 (13), Q3 2025 (9) |
| `food.demand.fact_distribution_quantity` | Q1 FY2027 (5), Q1 FY2027 (15), Q3 FY2026 (4), Q3 FY2026 (10), Q2 FY2026 (7) |
| `food.demand.fact_mdlz_innovation_sales_amount` | Q1 2026 (7) |
| `food.demand.fact_on_shelf_availability` | Q1 FY2027 (5), Q1 FY2027 (15), Q3 FY2026 (4), Q3 FY2026 (10), Q2 FY2026 (7) |
