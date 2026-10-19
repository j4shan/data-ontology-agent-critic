# Merchandise Inc store network and supply

Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks. Demand quantity, supply or capacity, and price or margin are stored on separate facts joined by the shared grain keys (fiscal quarter, scenario, and the business keys).

## Numbered questions

## Costco

### Q4 FY2026 (1) Costco

How is Costco judging the return on the price investment funded by tariff refunds, given monthly sales have not clearly accelerated?

- `merchandise.supply.fact_tariff_refund`: `fiscal_quarter_id`, `scenario_id`, `vendor_id`, `tariff_refund_amount`
- `merchandise.sales.fact_price_investment`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `price_investment_amount`
- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q4 FY2026 (3) Costco

How long did last year's tariff-driven assortment swaps last, and how does the holiday assortment look now?

- `merchandise.supply.fact_vendor_price`: `fiscal_quarter_id`, `scenario_id`, `vendor_id`, `category_id`, `vendor_cost_change_percent`, `tariff_cost_amount`
- `merchandise.supply.fact_inventory`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `inventory_amount`, `inventory_unit_count`
- `merchandise.assortment.fact_assortment_count`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `vendor_id`, `active_sku_count`, `new_sku_count`

### Q4 FY2026 (5) Costco

How much visibility does Costco have on vendor price increases over the next few months, and where can it substitute items?

- `merchandise.supply.fact_vendor_price`: `fiscal_quarter_id`, `scenario_id`, `vendor_id`, `category_id`, `vendor_cost_change_percent`, `tariff_cost_amount`
- `merchandise.supply.fact_inventory`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `inventory_amount`, `inventory_unit_count`
- `merchandise.assortment.fact_assortment_count`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `vendor_id`, `active_sku_count`, `new_sku_count`

### Q4 FY2026 (12) Costco

As egg deflation fades and tariff-rebate reinvestment and oil effects pass, where does price and inflation go next?

- `merchandise.supply.fact_vendor_price`: `fiscal_quarter_id`, `scenario_id`, `vendor_id`, `category_id`, `vendor_cost_change_percent`, `tariff_cost_amount`
- `merchandise.supply.fact_inventory`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `inventory_amount`, `inventory_unit_count`
- `merchandise.assortment.fact_assortment_count`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `vendor_id`, `active_sku_count`, `new_sku_count`

### Q4 FY2026 (14) Costco

Where is SG&A pressure building, and can expenses still leverage if comps stay around 6%?

- `merchandise.profit.fact_operating_income`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `store_format_id`, `operating_income_amount`
- `merchandise.expense.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `operating_expense_amount`

### Q3 FY2026 (1) Costco

How should same-store sales be read as Costco laps outsized drivers such as gift cards and gold?

- `merchandise.network.fact_store_count`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `market_id`, `store_count`, `selling_square_feet_count`
- `merchandise.network.fact_store_opening`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `stores_opened_count`, `stores_closed_count`

### Q3 FY2026 (4) Costco

Does a mid-single-digit comp still leverage SG&A the way a 4% to 5% comp used to?

- `merchandise.profit.fact_operating_income`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `store_format_id`, `operating_income_amount`
- `merchandise.expense.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `operating_expense_amount`

### Q3 FY2026 (8) Costco

What does the warehouse pipeline look like in Europe and Asia over the next few years?

- `merchandise.network.fact_store_count`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `market_id`, `store_count`, `selling_square_feet_count`
- `merchandise.network.fact_store_opening`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `stores_opened_count`, `stores_closed_count`

### Q2 FY2026 (3) Costco

Are spring and summer assortments changing the way last fall's did, and how have rising gas prices historically affected the club?

- `merchandise.supply.fact_inventory`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `inventory_amount`, `inventory_unit_count`
- `merchandise.assortment.fact_assortment_count`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `vendor_id`, `active_sku_count`, `new_sku_count`
- `merchandise.supply.fact_in_stock`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `in_stock_percent`, `active_item_count`

### Q2 FY2026 (5) Costco

With Canada volumes near $300 million, what are shopability and capacity constraints, and what is the business-center reopening plan?

- `merchandise.network.fact_store_count`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `market_id`, `store_count`, `selling_square_feet_count`
- `merchandise.network.fact_store_opening`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `stores_opened_count`, `stores_closed_count`

### Q1 FY2026 (3) Costco

Can newer warehouse classes keep lifting sales per building above the prior class, and what productivity steps support that?

- `merchandise.network.fact_store_count`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `market_id`, `store_count`, `selling_square_feet_count`
- `merchandise.network.fact_store_opening`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `stores_opened_count`, `stores_closed_count`

### Q1 FY2026 (6) Costco

What does the Europe and Asia opening pipeline look like, and what is the remodel philosophy?

- `merchandise.network.fact_store_count`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `market_id`, `store_count`, `selling_square_feet_count`
- `merchandise.network.fact_store_opening`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `stores_opened_count`, `stores_closed_count`

### Q1 FY2026 (7) Costco

Did higher health-care costs block SG&A leverage, and what productivity rate is expected from here?

- `merchandise.profit.fact_operating_income`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `store_format_id`, `operating_income_amount`
- `merchandise.expense.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `operating_expense_amount`

## Walmart

### Q2 FY2027 (1) Walmart

Have the latest price investments already lifted units, how much of the funding is vendor support versus Walmart, and how are the lower prices sustained when they are lapped in the next year?

- `merchandise.supply.fact_tariff_refund`: `fiscal_quarter_id`, `scenario_id`, `vendor_id`, `tariff_refund_amount`
- `merchandise.sales.fact_price_investment`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `price_investment_amount`
- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q2 FY2027 (9) Walmart

Are any inventory pockets a concern, and what inflation is expected for the rest of the year?

- `merchandise.supply.fact_inventory`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `inventory_amount`, `inventory_unit_count`
- `merchandise.assortment.fact_assortment_count`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `vendor_id`, `active_sku_count`, `new_sku_count`
- `merchandise.supply.fact_in_stock`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `in_stock_percent`, `active_item_count`

### Q1 FY2027 (7) Walmart

Are competitors already cutting price to regain share, where do Walmart's price gaps sit, and what tariff rates are in this year's plan?

- `merchandise.supply.fact_vendor_price`: `fiscal_quarter_id`, `scenario_id`, `vendor_id`, `category_id`, `vendor_cost_change_percent`, `tariff_cost_amount`
- `merchandise.supply.fact_inventory`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `inventory_amount`, `inventory_unit_count`
- `merchandise.assortment.fact_assortment_count`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `vendor_id`, `active_sku_count`, `new_sku_count`

### Q4 FY2026 (3) Walmart

How much of the margin outlook is mix, and are inventory gains only from automation or also from other programs by region?

- `merchandise.supply.fact_inventory`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `inventory_amount`, `inventory_unit_count`
- `merchandise.assortment.fact_assortment_count`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `vendor_id`, `active_sku_count`, `new_sku_count`
- `merchandise.supply.fact_in_stock`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `in_stock_percent`, `active_item_count`

### Q4 FY2026 (6) Walmart

How do U.S. shoppers differ by income, how have GLP-1 users changed trip frequency and basket size, and how does that change inventory plans?

- `merchandise.supply.fact_inventory`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `inventory_amount`, `inventory_unit_count`
- `merchandise.assortment.fact_assortment_count`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `vendor_id`, `active_sku_count`, `new_sku_count`
- `merchandise.supply.fact_in_stock`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `in_stock_percent`, `active_item_count`

### Q4 FY2025 (5) Walmart

How did markdowns compare with plan, how much price investment is in next year's guide, and what is the longer-term view of the extra Canada investment?

- `merchandise.supply.fact_tariff_refund`: `fiscal_quarter_id`, `scenario_id`, `vendor_id`, `tariff_refund_amount`
- `merchandise.sales.fact_price_investment`: `fiscal_quarter_id`, `scenario_id`, `category_id`, `price_investment_amount`
- `merchandise.sales.fact_net_sales`: `fiscal_quarter_id`, `scenario_id`, `store_format_id`, `banner_id`, `geography_segment_id`, `net_sales_amount`

### Q4 FY2025 (9) Walmart

What would make the expense ratio better or worse than expected this year, and how should that ratio trend longer term?

- `merchandise.profit.fact_operating_income`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `store_format_id`, `operating_income_amount`
- `merchandise.expense.fact_operating_expense`: `fiscal_quarter_id`, `scenario_id`, `geography_segment_id`, `operating_expense_amount`
