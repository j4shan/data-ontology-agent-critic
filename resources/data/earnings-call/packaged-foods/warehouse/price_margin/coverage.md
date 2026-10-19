# Food Inc price and margin

General Mills and Mondelez each have their own reporting-segment dimension and brand dimension, and North America Retail appears only as a General Mills reporting segment, not as a channel. Realized price per pound or per kilogram shares brand and region keys with the matching brand-volume fact, and cocoa and wheat are carried as quantity at risk in tonnes beside cost per tonne. Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks.

## Numbered questions

## General Mills

### Q1 FY2027 (8) General Mills

How do gross-margin puts and takes work through the year as input-cost inflation, which accelerated late last year, is set against productivity and a rising mix benefit?

- `food.price.fact_gis_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `food.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `food.price.fact_mdlz_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`

### Q1 FY2027 (10) General Mills

If inflation is similar in the first three fiscal quarters and steps up in the fourth, can the company stay ahead of sticky inflation in later years, and is price a usable lever after the recent value reset?

- `food.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `food.price.fact_gis_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `food.price.fact_gis_realized_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `realized_price_dollars_per_pound`

### Q1 FY2027 (11) General Mills

How much was marketing up year over year this quarter, and does that rate hold for the rest of the year?

- `food.price.fact_gis_advertising_spend`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `advertising_spend_amount`
- `food.price.fact_gis_realized_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `realized_price_dollars_per_pound`
- `food.price.fact_gis_list_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `list_price_dollars_per_pound`, `list_price_change_percent`

### Q1 FY2027 (13) General Mills

Beyond cereal entry prices and larger formats, where else has price-pack architecture changed, and have results matched North America Retail cereal?

- `food.price.fact_gis_price_pack_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `gis_category_id`, `price_pack_format_id`, `price_dollars_per_pound`
- `food.price.fact_gis_realized_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `realized_price_dollars_per_pound`
- `food.price.fact_gis_list_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `list_price_dollars_per_pound`, `list_price_change_percent`

### Q1 FY2027 (17) General Mills

If peers raise list prices while General Mills holds them, how much market-share gain is in the plan as consumers shift?

- `food.price.fact_gis_list_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `list_price_dollars_per_pound`, `list_price_change_percent`
- `food.price.fact_gis_realized_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `realized_price_dollars_per_pound`
- `food.price.fact_gis_price_gap`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `competitor_type_id`, `region_id`, `price_gap_percent`

### Q4 FY2026 (1) General Mills

What was learned from last year's price investments that supports pivoting fiscal 2027 spend toward better-for-you innovation and renovation, and how confident is management that the shift delivers?

- `food.price.fact_gis_realized_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `realized_price_dollars_per_pound`
- `food.price.fact_gis_advertising_spend`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `advertising_spend_amount`
- `food.price.fact_mdlz_advertising_spend`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `advertising_spend_amount`, `advertising_change_percent`

### Q4 FY2026 (2) General Mills

Has the mid-year shift toward waiting for promotions faded?

- `food.price.fact_promotion_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `promotion_type_id`, `promoted_price_dollars_per_pound`
- `food.price.fact_gis_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `food.price.fact_gis_advertising_spend`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `advertising_spend_amount`

### Q4 FY2026 (3) General Mills

Is category growth still below long-term trends for cyclical reasons?

- `food.price.fact_category_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `category_sales_amount`
- `food.price.fact_gis_price_pack_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `gis_category_id`, `price_pack_format_id`, `price_dollars_per_pound`
- `food.price.fact_gis_realized_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `realized_price_dollars_per_pound`

### Q4 FY2026 (8) General Mills

What dollar category growth is expected, and does the guide assume General Mills grows in line with the category by year-end as dollar share improves?

- `food.price.fact_category_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `category_sales_amount`
- `food.price.fact_gis_realized_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `realized_price_dollars_per_pound`
- `food.price.fact_gis_list_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `list_price_dollars_per_pound`, `list_price_change_percent`

### Q4 FY2026 (10) General Mills

Ignoring the extra week, are gross margins roughly flat in fiscal 2027 if the sales and profit ranges match the inflation rate?

- `food.price.fact_gis_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `food.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `food.price.fact_mdlz_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`

### Q3 FY2026 (1) General Mills

Once this year's price investments and remarkability work are lapped, can volume grow in fiscal 2027 even if category growth stays below its long-term rate?

- `food.price.fact_category_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `category_sales_amount`
- `food.price.fact_promotion_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `promotion_type_id`, `promoted_price_dollars_per_pound`
- `food.price.fact_gis_realized_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `realized_price_dollars_per_pound`

### Q3 FY2026 (5) General Mills

Versus the pre-COVID period, when a similar innovation rate, restored promotion, and marketing spend stabilized organic sales, what response is each of those spends getting now?

- `food.price.fact_gis_advertising_spend`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `advertising_spend_amount`
- `food.price.fact_promotion_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `promotion_type_id`, `promoted_price_dollars_per_pound`
- `food.price.fact_category_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `category_sales_amount`

### Q3 FY2026 (6) General Mills

If organic sales stabilize in fiscal 2027, can gross margin return to the mid-30s rather than the low-30s?

- `food.price.fact_gis_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `food.price.fact_mdlz_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `food.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`

### Q3 FY2026 (11) General Mills

Are salty-snack price cuts and innovation only adjacent to General Mills, or are they taking share from its brands, and what returns snacks to growth after a high-single-digit decline?

- `food.price.fact_gis_realized_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `realized_price_dollars_per_pound`
- `food.price.fact_gis_list_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `list_price_dollars_per_pound`, `list_price_change_percent`
- `food.price.fact_gis_price_gap`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `competitor_type_id`, `region_id`, `price_gap_percent`

### Q2 FY2026 (1) General Mills

After a large peer cut prices sharply, will other competitors have to follow, and does General Mills still have a first-mover advantage on closing price gaps?

- `food.price.fact_gis_price_gap`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `competitor_type_id`, `region_id`, `price_gap_percent`
- `food.price.fact_gis_realized_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `realized_price_dollars_per_pound`
- `food.price.fact_gis_list_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `list_price_dollars_per_pound`, `list_price_change_percent`

### Q2 FY2026 (4) General Mills

Can volumes stay positive after the company laps its own price cuts?

- `food.price.fact_gis_price_gap`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `competitor_type_id`, `region_id`, `price_gap_percent`
- `food.price.fact_gis_realized_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `realized_price_dollars_per_pound`
- `food.price.fact_gis_list_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `list_price_dollars_per_pound`, `list_price_change_percent`

### Q2 FY2026 (5) General Mills

Are larger promotions needed because shoppers are waiting for deals, and how does everyday-low-price compare with high-low in this environment versus past downturns?

- `food.price.fact_promotion_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `promotion_type_id`, `promoted_price_dollars_per_pound`
- `food.price.fact_gis_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `food.price.fact_gis_advertising_spend`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `advertising_spend_amount`

### Q2 FY2026 (11) General Mills

What share of the portfolio has had price investment, and if the cost-to-compete environment worsens, what savings are visible to respond?

- `food.price.fact_gis_realized_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `realized_price_dollars_per_pound`
- `food.price.fact_gis_list_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `list_price_dollars_per_pound`, `list_price_change_percent`
- `food.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`

### Q2 FY2026 (14) General Mills

In the portion of the portfolio where price adjustments and remarkability are still missing the high hit rate, is there a common thread beyond Totino's?

- `food.price.fact_promotion_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `promotion_type_id`, `promoted_price_dollars_per_pound`
- `food.price.fact_gis_advertising_spend`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `advertising_spend_amount`
- `food.price.fact_gis_realized_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `region_id`, `realized_price_dollars_per_pound`

## Mondelez

### Q1 2026 (2) Mondelez

Which European geographies still have pricing negotiations open heading into the second quarter?

- `food.price.fact_mdlz_realized_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `realized_price_dollars_per_kilogram`
- `food.price.fact_mdlz_list_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `list_price_dollars_per_kilogram`, `list_price_change_percent`
- `food.price.fact_mdlz_price_gap`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `competitor_type_id`, `region_id`, `price_gap_percent`

### Q1 2026 (3) Mondelez

How has the European competitive environment evolved with cocoa volatility, and how is that expected to look for the rest of the year?

- `food.price.fact_mdlz_realized_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `realized_price_dollars_per_kilogram`
- `food.price.fact_mdlz_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `food.price.fact_mdlz_list_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `list_price_dollars_per_kilogram`, `list_price_change_percent`

### Q1 2026 (6) Mondelez

How should gross margin progress after the quarter's inventory-phasing effect was smaller than feared?

- `food.price.fact_mdlz_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `food.price.fact_gis_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `food.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`

### Q4 2025 (1) Mondelez

Where does the chocolate strategy stand after the drop in cocoa, and how does it play out from here?

- `food.price.fact_mdlz_realized_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `realized_price_dollars_per_kilogram`
- `food.price.fact_mdlz_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `food.price.fact_mdlz_list_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `list_price_dollars_per_kilogram`, `list_price_change_percent`

### Q4 2025 (3) Mondelez

How does cocoa cost phase through 2026, and how do potential chocolate price investments phase over the year?

- `food.price.fact_mdlz_realized_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `realized_price_dollars_per_kilogram`
- `food.price.fact_mdlz_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `food.price.fact_mdlz_advertising_spend`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `advertising_spend_amount`, `advertising_change_percent`

### Q4 2025 (4) Mondelez

Is North America weakness cyclical or structural, and what pricing actions follow a large peer cutting snack prices?

- `food.price.fact_mdlz_realized_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `realized_price_dollars_per_kilogram`
- `food.price.fact_gis_price_gap`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `competitor_type_id`, `region_id`, `price_gap_percent`
- `food.price.fact_mdlz_list_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `list_price_dollars_per_kilogram`, `list_price_change_percent`

### Q4 2025 (5) Mondelez

With chocolate pricing expected flat while cocoa is down, is the net price-cost relationship in the guide roughly neutral after hedges and inventory accounting, or still a benefit?

- `food.price.fact_mdlz_realized_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `realized_price_dollars_per_kilogram`
- `food.price.fact_mdlz_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `food.price.fact_mdlz_list_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `list_price_dollars_per_kilogram`, `list_price_change_percent`

### Q4 2025 (6) Mondelez

How large is the 2026 advertising step-up versus a normal level?

- `food.price.fact_mdlz_advertising_spend`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `advertising_spend_amount`, `advertising_change_percent`
- `food.price.fact_mdlz_realized_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `realized_price_dollars_per_kilogram`
- `food.price.fact_mdlz_list_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `list_price_dollars_per_kilogram`, `list_price_change_percent`

### Q4 2025 (9) Mondelez

Going into 2027, are media, compensation, and channel investments largely lapped so leverage comes from mix, lower cocoa, and overhead, or do multiyear investments continue?

- `food.price.fact_mdlz_advertising_spend`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `advertising_spend_amount`, `advertising_change_percent`
- `food.price.fact_mdlz_realized_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `realized_price_dollars_per_kilogram`
- `food.price.fact_mdlz_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`

### Q4 2025 (10) Mondelez

Is there a path for European chocolate profit back to pre-2025 levels, and does that recovery start in 2027 as prices come down?

- `food.price.fact_mdlz_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `food.price.fact_mdlz_realized_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `realized_price_dollars_per_kilogram`
- `food.price.fact_mdlz_list_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `list_price_dollars_per_kilogram`, `list_price_change_percent`

### Q4 2025 (11) Mondelez

Which in-year milestones, such as retailer-brand pricing and the company's own elasticity, will show whether the chocolate plan is working?

- `food.price.fact_mdlz_price_gap`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `competitor_type_id`, `region_id`, `price_gap_percent`
- `food.price.fact_mdlz_realized_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `realized_price_dollars_per_kilogram`
- `food.price.fact_mdlz_list_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `list_price_dollars_per_kilogram`, `list_price_change_percent`

### Q3 2025 (4) Mondelez

If next year's earnings can be described relative to the algorithm, should the top line be thought of the same way?

- `food.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `food.price.fact_category_sales_amount`: `fiscal_quarter_id`, `scenario_id`, `mdlz_category_id`, `region_id`, `category_sales_amount`
- `food.price.fact_mdlz_realized_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `realized_price_dollars_per_kilogram`

### Q3 2025 (10) Mondelez

Is any 2026 investment being pulled into the fourth quarter, and does the 2026 earnings outlook already refill spend enough that 2027 does not need another reset?

- `food.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`
- `food.price.fact_mdlz_advertising_spend`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `advertising_spend_amount`, `advertising_change_percent`
- `food.price.fact_promotion_price`: `fiscal_quarter_id`, `scenario_id`, `gis_brand_id`, `promotion_type_id`, `promoted_price_dollars_per_pound`

### Q2 2025 (1) Mondelez

What second-half puts and takes, including a weaker U.S., leave full-year guidance unchanged after a strong first half?

- `food.price.fact_gis_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `gis_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `food.price.fact_mdlz_realized_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `realized_price_dollars_per_kilogram`
- `food.price.fact_mdlz_list_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `list_price_dollars_per_kilogram`, `list_price_change_percent`

### Q2 2025 (2) Mondelez

After buying the recent cocoa dip, is more pricing or revenue-growth management still needed in the back half under the higher-cocoa scenario?

- `food.price.fact_mdlz_realized_price`: `fiscal_quarter_id`, `scenario_id`, `mdlz_brand_id`, `region_id`, `realized_price_dollars_per_kilogram`
- `food.price.fact_mdlz_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `mdlz_reporting_segment_id`, `gross_profit_amount`, `gross_margin_percent`
- `food.price.fact_enterprise_earnings`: `fiscal_quarter_id`, `scenario_id`, `enterprise_revenue_amount`, `enterprise_earnings_amount`, `enterprise_operating_margin_percent`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `food.price.dim_price_pack_format` | supporting population |
| `food.price.dim_promotion_type` | supporting population |
| `food.price.dim_pricing_strategy` | supporting population |
| `food.price.dim_currency` | supporting population |
| `food.price.fact_gis_realized_price` | Q1 FY2027 (10), Q1 FY2027 (11), Q1 FY2027 (13), Q1 FY2027 (17), Q4 FY2026 (1), Q4 FY2026 (3), Q4 FY2026 (8), Q3 FY2026 (1), Q3 FY2026 (11), Q2 FY2026 (1), Q2 FY2026 (4), Q2 FY2026 (11), Q2 FY2026 (14) |
| `food.price.fact_mdlz_realized_price` | Q1 2026 (2), Q1 2026 (3), Q4 2025 (1), Q4 2025 (3), Q4 2025 (4), Q4 2025 (5), Q4 2025 (6), Q4 2025 (9), Q4 2025 (10), Q4 2025 (11), Q3 2025 (4), Q2 2025 (1), Q2 2025 (2) |
| `food.price.fact_gis_list_price` | Q1 FY2027 (11), Q1 FY2027 (13), Q1 FY2027 (17), Q4 FY2026 (8), Q3 FY2026 (11), Q2 FY2026 (1), Q2 FY2026 (4), Q2 FY2026 (11) |
| `food.price.fact_mdlz_list_price` | Q1 2026 (2), Q1 2026 (3), Q4 2025 (1), Q4 2025 (4), Q4 2025 (5), Q4 2025 (6), Q4 2025 (10), Q4 2025 (11), Q2 2025 (1) |
| `food.price.fact_gis_price_gap` | Q1 FY2027 (17), Q3 FY2026 (11), Q2 FY2026 (1), Q2 FY2026 (4), Q4 2025 (4) |
| `food.price.fact_mdlz_price_gap` | Q1 2026 (2), Q4 2025 (11) |
| `food.price.fact_gis_gross_margin` | Q1 FY2027 (8), Q1 FY2027 (10), Q4 FY2026 (2), Q4 FY2026 (10), Q3 FY2026 (6), Q2 FY2026 (5), Q1 2026 (6), Q2 2025 (1) |
| `food.price.fact_mdlz_gross_margin` | Q1 FY2027 (8), Q4 FY2026 (10), Q3 FY2026 (6), Q1 2026 (3), Q1 2026 (6), Q4 2025 (1), Q4 2025 (3), Q4 2025 (5), Q4 2025 (9), Q4 2025 (10), Q2 2025 (2) |
| `food.price.fact_enterprise_earnings` | Q1 FY2027 (8), Q1 FY2027 (10), Q4 FY2026 (10), Q3 FY2026 (6), Q2 FY2026 (11), Q1 2026 (6), Q3 2025 (4), Q3 2025 (10), Q2 2025 (2) |
| `food.price.fact_gis_advertising_spend` | Q1 FY2027 (11), Q4 FY2026 (1), Q4 FY2026 (2), Q3 FY2026 (5), Q2 FY2026 (5), Q2 FY2026 (14) |
| `food.price.fact_mdlz_advertising_spend` | Q4 FY2026 (1), Q4 2025 (3), Q4 2025 (6), Q4 2025 (9), Q3 2025 (10) |
| `food.price.fact_gis_price_pack_price` | Q1 FY2027 (13), Q4 FY2026 (3) |
| `food.price.fact_promotion_price` | Q4 FY2026 (2), Q3 FY2026 (1), Q3 FY2026 (5), Q2 FY2026 (5), Q2 FY2026 (14), Q3 2025 (10) |
| `food.price.fact_category_sales_amount` | Q4 FY2026 (3), Q4 FY2026 (8), Q3 FY2026 (1), Q3 FY2026 (5), Q3 2025 (4) |
