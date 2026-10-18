# Merchandise Inc merchandise, sales, and margin

Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks. Demand quantity, supply or capacity, and price or margin are stored on separate facts joined by the shared grain keys (fiscal quarter, scenario, and the business keys).

## Numbered questions

## Costco

### Q4 FY2026 (9) Costco

How is food inflation versus nonfood inflation running, and how much does bringing an item like the churro back add?

- `merchandise.sales.fact_category_sales`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `brand_tier_id`, `category_sales_amount`
- `merchandise.sales.fact_merchandise_units`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `unit_count`
- `merchandise.sales.fact_average_unit_price`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `average_price_amount`

### Q3 FY2026 (2) Costco

What drove the slight core-on-core margin decline while lapping prior-year items?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q3 FY2026 (3) Costco

Is Costco lowering prices ahead of expected cost declines, and how does that compare with peers?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q3 FY2026 (5) Costco

What limits retail media given Costco's tight SKU count versus other retailers?

- `merchandise.media.fact_retail_media_revenue`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `retail_media_revenue_amount`
- `merchandise.media.fact_retail_media_impressions`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `media_impression_count`
- `merchandise.media.fact_retail_media_price`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `media_cpm_amount`

### Q3 FY2026 (7) Costco

With fuel volumes up sharply, where can throughput still increase, and did wider gasoline price gaps reduce profit per gallon?

- `merchandise.fuel.fact_fuel_gallons`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `geography_segment_id`, `gallon_count`
- `merchandise.fuel.fact_fuel_price`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `fuel_price_per_gallon_amount`, `fuel_margin_amount`
- `merchandise.sales.fact_fuel_revenue`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `fuel_revenue_amount`

### Q3 FY2026 (9) Costco

Is AI search already lifting traffic or conversion in particular categories?

- `merchandise.sales.fact_traffic`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `visit_count`
- `merchandise.sales.fact_ticket`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `average_ticket_amount`
- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q2 FY2026 (1) Costco

How did weather help or hurt January and February sales?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`
- `merchandise.sales.fact_comparable_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `comparable_sales_percent`, `comparable_sales_amount`
- `merchandise.margin.fact_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `store_format_id`, `gross_margin_amount`, `gross_margin_percent`

### Q2 FY2026 (2) Costco

How large are the savings from checkout and front-end tests, and how widely can they roll?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q2 FY2026 (6) Costco

How do newly available real-estate sites change which markets Costco can enter over the long term?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q2 FY2026 (8) Costco

What is the roadmap for digital advertising and the marketplace, and where is AI being applied?

- `merchandise.marketplace.fact_marketplace_gmv`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `gmv_amount`, `marketplace_order_count`
- `merchandise.marketplace.fact_marketplace_order_value`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `average_order_value_amount`
- `merchandise.marketplace.fact_marketplace_seller_count`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `seller_count`

### Q1 FY2026 (1) Costco

Is there any concern in traffic even though absolute results are strong?

- `merchandise.sales.fact_traffic`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `visit_count`
- `merchandise.sales.fact_ticket`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `average_ticket_amount`
- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q1 FY2026 (8) Costco

Was food inflationary in the quarter, was general merchandise up low single digits, and was most ticket growth just inflation?

- `merchandise.sales.fact_traffic`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `visit_count`
- `merchandise.sales.fact_ticket`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `average_ticket_amount`
- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q1 FY2026 (10) Costco

What is the long-term warehouse potential in the U.S. and worldwide, and are the deepest price investments concentrated in Kirkland?

- `merchandise.brand.fact_private_brand_sales`: `fiscal_quarter_id`, `scenario_id`, `brand_tier_id`, `category_id`, `private_brand_sales_amount`
- `merchandise.sales.fact_category_sales`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `brand_tier_id`, `category_sales_amount`

### Q1 FY2026 (11) Costco

How far has personalization rolled, and what conversion or attachment has it produced?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

## Walmart

### Q2 FY2027 (2) Walmart

Is higher fuel adding a new burden on lower-income shoppers, and does the unit response to rollbacks show up immediately or with a lag of several months?

- `merchandise.fuel.fact_fuel_gallons`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `geography_segment_id`, `gallon_count`
- `merchandise.fuel.fact_fuel_price`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `fuel_price_per_gallon_amount`, `fuel_margin_amount`
- `merchandise.sales.fact_fuel_revenue`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `fuel_revenue_amount`

### Q2 FY2027 (3) Walmart

Are the new tariff rates higher or lower than the prior emergency-tariff regime, and should operating income still grow faster than sales into next year once price-investment traffic arrives?

- `merchandise.sales.fact_traffic`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `visit_count`
- `merchandise.sales.fact_ticket`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `average_ticket_amount`
- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q2 FY2027 (4) Walmart

What is the multi-year outlook for health and wellness, including the effect of fair-pricing rules?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q2 FY2027 (5) Walmart

If the expected U.S. comp acceleration from lagged price cuts does not arrive, would Walmart invest more in price into the back half and next year as tax-refund benefits fade?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q2 FY2027 (6) Walmart

What incremental margin is the digital business producing, and how does Walmart lap today's rollbacks next year without losing store traffic?

- `merchandise.sales.fact_traffic`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `visit_count`
- `merchandise.sales.fact_ticket`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `average_ticket_amount`
- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q2 FY2027 (7) Walmart

How much of the general-merchandise slowdown versus grocery was stimulus fading versus fuel pressure on lower-income shoppers, and has back-to-school started to lift general merchandise?

- `merchandise.fuel.fact_fuel_gallons`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `geography_segment_id`, `gallon_count`
- `merchandise.fuel.fact_fuel_price`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `fuel_price_per_gallon_amount`, `fuel_margin_amount`
- `merchandise.sales.fact_fuel_revenue`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `fuel_revenue_amount`

### Q2 FY2027 (8) Walmart

What payback decides whether a rollback becomes permanent, and how much of the current rollback set is clearing that hurdle?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q2 FY2027 (11) Walmart

How do second-half comps split between traffic and ticket under the price investments, and was the 7% U.S. expense growth timing or higher liability claims?

- `merchandise.sales.fact_traffic`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `visit_count`
- `merchandise.sales.fact_ticket`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `average_ticket_amount`
- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q2 FY2027 (12) Walmart

With average ticket running below inflation, is the basket shifting through trade-down, category mix, or smaller-ticket items?

- `merchandise.sales.fact_traffic`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `visit_count`
- `merchandise.sales.fact_ticket`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `average_ticket_amount`
- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q1 FY2027 (1) Walmart

What would let enterprise and U.S. e-commerce incremental margins move above the recent range if fuel stays high?

- `merchandise.fuel.fact_fuel_gallons`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `geography_segment_id`, `gallon_count`
- `merchandise.fuel.fact_fuel_price`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `fuel_price_per_gallon_amount`, `fuel_margin_amount`
- `merchandise.sales.fact_fuel_revenue`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `fuel_revenue_amount`

### Q1 FY2027 (2) Walmart

What keeps the traffic acceleration at Walmart U.S. and Sam's going, and could tariff rebates fund that versus offsetting energy costs?

- `merchandise.sales.fact_traffic`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `visit_count`
- `merchandise.sales.fact_ticket`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `average_ticket_amount`
- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q1 FY2027 (3) Walmart

When do the alternative-revenue platforms launched in Canada and Mexico show up in enterprise margin?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`
- `merchandise.sales.fact_comparable_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `comparable_sales_percent`, `comparable_sales_amount`
- `merchandise.margin.fact_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `store_format_id`, `gross_margin_amount`, `gross_margin_percent`

### Q1 FY2027 (4) Walmart

Where do the main alternative-revenue streams sit versus their potential, if double-digit operating-income growth is harder in this environment?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`
- `merchandise.sales.fact_comparable_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `comparable_sales_percent`, `comparable_sales_amount`
- `merchandise.margin.fact_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `store_format_id`, `gross_margin_amount`, `gross_margin_percent`

### Q1 FY2027 (5) Walmart

How sustainable is general-merchandise strength and the ticket assumption into the back half, and how does marketplace expansion support share in that segment?

- `merchandise.sales.fact_traffic`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `visit_count`
- `merchandise.sales.fact_ticket`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `average_ticket_amount`
- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q1 FY2027 (6) Walmart

Can trade-in from higher-income shoppers offset pressure on the lower end as fuel rises and tax stimulus fades, and could grocery price competition mute inflation and squeeze margin as egg deflation ends?

- `merchandise.fuel.fact_fuel_gallons`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `geography_segment_id`, `gallon_count`
- `merchandise.fuel.fact_fuel_price`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `fuel_price_per_gallon_amount`, `fuel_margin_amount`
- `merchandise.sales.fact_fuel_revenue`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `fuel_revenue_amount`

### Q1 FY2027 (8) Walmart

Which categories are driving the order lift from the shopping assistant, and how is AI split between customer experience and the supply chain?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q1 FY2027 (9) Walmart

How much volume is on 30- and 60-minute delivery, and how fast does that coverage expand beyond the share of the population already reached?

- `merchandise.sales.fact_ecommerce_sales`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `fulfillment_type_id`, `ecommerce_sales_amount`, `ecommerce_order_count`
- `merchandise.sales.fact_traffic`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `visit_count`

### Q1 FY2027 (10) Walmart

How does marketplace growth split among sellers, SKUs, and order value, and where is the biggest expansion opportunity for the rest of the year?

- `merchandise.marketplace.fact_marketplace_gmv`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `gmv_amount`, `marketplace_order_count`
- `merchandise.marketplace.fact_marketplace_order_value`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `average_order_value_amount`
- `merchandise.marketplace.fact_marketplace_seller_count`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `seller_count`

### Q1 FY2027 (11) Walmart

What is happening in underlying health and wellness after the moderation, and does GLP-1 price pressure free spending for other categories?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q1 FY2027 (12) Walmart

How much has mix into health and wellness and grocery held back U.S. gross margin, now that mix is a margin source again?

- `merchandise.margin.fact_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `store_format_id`, `gross_margin_amount`, `gross_margin_percent`
- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`
- `merchandise.margin.fact_category_margin`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `category_gross_margin_amount`, `category_gross_margin_percent`

### Q1 FY2027 (13) Walmart

Why can second-quarter operating income growth accelerate versus the first quarter even with a full quarter of fuel headwind?

- `merchandise.fuel.fact_fuel_gallons`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `geography_segment_id`, `gallon_count`
- `merchandise.fuel.fact_fuel_price`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `fuel_price_per_gallon_amount`, `fuel_margin_amount`
- `merchandise.sales.fact_fuel_revenue`: `fiscal_quarter_id`, `scenario_id`, `banner_id`, `fuel_revenue_amount`

### Q1 FY2027 (14) Walmart

Are higher gas prices shifting trips online versus in store, or changing what people buy?

- `merchandise.sales.fact_ecommerce_sales`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `fulfillment_type_id`, `ecommerce_sales_amount`, `ecommerce_order_count`
- `merchandise.sales.fact_traffic`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `visit_count`

### Q4 FY2026 (1) Walmart

How could agent-style shopping change customer traffic, loyalty, and advertising monetization?

- `merchandise.sales.fact_traffic`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `visit_count`
- `merchandise.sales.fact_ticket`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `average_ticket_amount`
- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q4 FY2026 (2) Walmart

What inflation, including lower drug prices, is assumed in the outlook?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q4 FY2026 (4) Walmart

Should advertising growth moderate from here, and which advertiser types or categories are accelerating versus still underpenetrated?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q4 FY2026 (5) Walmart

What threatens e-commerce share momentum, and does that change the near-term profit path?

- `merchandise.sales.fact_ecommerce_sales`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `fulfillment_type_id`, `ecommerce_sales_amount`, `ecommerce_order_count`
- `merchandise.sales.fact_traffic`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `visit_count`

### Q4 FY2025 (1) Walmart

Is Walmart becoming more sensitive to the economy, with less of a countercyclical share gain, and is that in the sales and earnings outlook?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`
- `merchandise.sales.fact_comparable_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `comparable_sales_percent`, `comparable_sales_amount`
- `merchandise.margin.fact_gross_margin`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `store_format_id`, `gross_margin_amount`, `gross_margin_percent`

### Q4 FY2025 (3) Walmart

If e-commerce incremental margins are already healthy, why not reinvest faster to grow the top of the funnel?

- `merchandise.sales.fact_ecommerce_sales`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `fulfillment_type_id`, `ecommerce_sales_amount`, `ecommerce_order_count`
- `merchandise.sales.fact_traffic`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `visit_count`

### Q4 FY2025 (6) Walmart

What is the dilution and integration plan for VIZIO, and how fast can Walmart Connect keep growing?

- `merchandise.media.fact_retail_media_revenue`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `retail_media_revenue_amount`
- `merchandise.media.fact_retail_media_impressions`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `media_impression_count`
- `merchandise.media.fact_retail_media_price`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `media_cpm_amount`

### Q4 FY2025 (7) Walmart

What are the main drivers of better e-commerce profit, and what share of profit dollars already comes from high-margin alternative revenue?

- `merchandise.sales.fact_ecommerce_sales`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `fulfillment_type_id`, `ecommerce_sales_amount`, `ecommerce_order_count`
- `merchandise.sales.fact_traffic`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `visit_count`

### Q4 FY2025 (8) Walmart

Do e-commerce incremental margins rise from here, and when does e-commerce itself become profitable?

- `merchandise.sales.fact_ecommerce_sales`: `fiscal_quarter_id`, `scenario_id`, `sales_channel_id`, `fulfillment_type_id`, `ecommerce_sales_amount`, `ecommerce_order_count`
- `merchandise.sales.fact_traffic`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `visit_count`

### Q4 FY2025 (10) Walmart

How is PhonePe growing and how profitable is it, and where can returns on investment still rise?

- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`
