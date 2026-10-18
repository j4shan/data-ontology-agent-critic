# Merchandise Inc merchandise price and mix

This slice owns items, prices, inflation, and category mix. Member counts and site capacity are owned in the other slices and are partial when named here. A unit-volume fact does not store the shelf price.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `banner_identity` | `banner_id` | `sf:merchandise.member.dim_banner` `banner_id` |
| `competitor_identity` | `competitor_id` | `sf:merchandise.member.dim_competitor` `competitor_id` |
| `country_identity` | `country_id` | `sf:merchandise.geography.dim_country` `country_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:merchandise.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `income_cohort_identity` | `income_cohort_id` | `sf:merchandise.member.dim_income_cohort` `income_cohort_id` |

## Numbered questions

## Costco

### Q4 FY2026 (1)

How is Costco judging the return on the price investment funded by tariff refunds, given monthly sales have not clearly accelerated?

- `merchandise.price.fact_price_investment`: `investment_amount`, `funding_source_code`, `return_clear_flag`
- `merchandise.demand.fact_monthly_sales`: `sales_amount`
- `merchandise.price.fact_shelf_price`: `shelf_price_amount`

### Q4 FY2026 (3)

How long did last year's tariff-driven assortment swaps last, and how does the holiday assortment look now at Costco?

- `merchandise.price.fact_assortment`: `items_removed_quantity`, `items_added_quantity`, `holiday_ready_flag`, `duration_quarters`
- `merchandise.price.dim_season`: `season_code`
- `merchandise.price.dim_inflation_driver`: `driver_code`

### Q4 FY2026 (5)

How much visibility does Costco have on vendor price increases over the next few months, and where can it substitute items?

- `merchandise.price.fact_vendor_cost`: `cost_amount`, `visibility_flag`, `notified_increase_flag`
- `merchandise.price.fact_assortment`: `substitutable_flag`, `items_added_quantity`

### Q4 FY2026 (9)

How is food inflation versus nonfood inflation running, and how much does bringing an item like the churro back add at Costco?

- `merchandise.price.fact_inflation_observation`: `inflation_rate`
- `merchandise.price.dim_department`: `department_code`
- `merchandise.price.fact_traffic_item`: `restored_flag`, `sales_lift_amount`
- `merchandise.price.dim_item`: `item_code`

### Q4 FY2026 (10)

Is the member still strong in both value categories and premium categories such as jewelry and travel at Costco?

- `merchandise.price.fact_category_demand`: `sales_amount`, `premium_strong_flag`, `value_strong_flag`
- `merchandise.price.dim_category`: `category_code`

### Q4 FY2026 (12)

As egg deflation fades and tariff-rebate reinvestment and oil effects pass, where does price and inflation go next at Costco?

- `merchandise.price.fact_inflation_observation`: `inflation_rate`
- `merchandise.price.dim_inflation_driver`: `driver_code`
- `merchandise.price.fact_fuel_price`: `price_per_gallon`

### Q3 FY2026 (1)

How should same-store sales be read as Costco laps outsized drivers such as gift cards and gold?

- `merchandise.price.fact_comp_sales`: `comp_rate`
- `merchandise.price.fact_lap_driver`: `driver_code`, `being_lapped_flag`
- `merchandise.price.dim_item`: `item_code`

### Q3 FY2026 (2)

What drove the slight core-on-core margin decline while lapping prior-year items at Costco?

- `merchandise.price.fact_merchandise_margin`: `margin_rate`, `decline_flag`
- `merchandise.price.fact_lap_driver`: `being_lapped_flag`
- `merchandise.price.dim_department`: `department_code`

### Q3 FY2026 (3)

Is Costco lowering prices ahead of expected cost declines, and how does that compare with peers?

- `merchandise.price.fact_shelf_price`: `shelf_price_amount`, `lowered_ahead_of_cost_flag`
- `merchandise.price.fact_vendor_cost`: `cost_amount`
- `merchandise.price.fact_price_gap`: `gap_index`, `peer_cutting_flag`

### Q2 FY2026 (3)

Are spring and summer assortments changing the way last fall's did, and how have rising gas prices historically affected the club at Costco?

- `merchandise.price.fact_assortment`: `items_added_quantity`, `items_removed_quantity`
- `merchandise.price.dim_season`: `season_code`
- `merchandise.price.fact_fuel_price`: `price_per_gallon`
- `merchandise.demand.fact_traffic`: `traffic_quantity`

### Q1 FY2026 (8)

Was food inflationary in the quarter, was general merchandise up low single digits, and was most ticket growth just inflation at Costco?

- `merchandise.price.fact_inflation_observation`: `inflation_rate`
- `merchandise.price.dim_department`: `department_code`
- `merchandise.price.fact_average_ticket`: `ticket_amount`, `mostly_inflation_flag`

### Q1 FY2026 (9)

Why has paid-member growth slowed, and when do nonfood comps clear the gift-card comparison relative to tax-refund timing at Costco?

- `merchandise.member.fact_member_count`: `growth_rate`, `slowed_flag`
- `merchandise.price.fact_comp_sales`: `comp_rate`
- `merchandise.price.fact_lap_driver`: `driver_code`, `being_lapped_flag`
- `merchandise.price.fact_stimulus_effect`: `refund_timing_code`, `fading_flag`

## Walmart

### Q2 FY2027 (1)

Have the latest price investments already lifted units, how much of the funding is vendor support versus Walmart, and how are the lower prices sustained when they are lapped in the next year?

- `merchandise.price.fact_price_investment`: `investment_amount`, `funding_source_code`, `in_guide_amount`
- `merchandise.price.fact_unit_volume`: `unit_quantity`
- `merchandise.price.fact_comp_sales`: `comp_rate`

### Q2 FY2027 (4)

What is the multi-year outlook for health and wellness, including the effect of fair-pricing rules at Walmart?

- `merchandise.price.fact_health_outlook`: `growth_rate`, `fair_pricing_constraint_flag`
- `merchandise.price.fact_regulatory_price`: `constrained_flag`
- `merchandise.price.dim_category`: `category_code`

### Q2 FY2027 (5)

If the expected U.S. comp acceleration from lagged price cuts does not arrive, would Walmart invest more in price into the back half and next year as tax-refund benefits fade?

- `merchandise.price.fact_comp_sales`: `comp_rate`, `acceleration_missing_flag`
- `merchandise.price.fact_price_investment`: `investment_amount`, `in_guide_amount`
- `merchandise.price.fact_stimulus_effect`: `fading_flag`, `refund_timing_code`

### Q2 FY2027 (7)

How much of the general-merchandise slowdown versus grocery was stimulus fading versus fuel pressure on lower-income shoppers, and has back-to-school started to lift general merchandise at Walmart?

- `merchandise.price.fact_category_demand`: `sales_amount`
- `merchandise.price.fact_stimulus_effect`: `fading_flag`
- `merchandise.price.fact_basket_mix`: `mix_share`
- `merchandise.price.dim_season`: `season_code`
- `merchandise.price.dim_category`: `category_code`

### Q2 FY2027 (8)

What payback decides whether a rollback becomes permanent, and how much of the current rollback set is clearing that hurdle at Walmart?

- `merchandise.price.fact_rollback_payback`: `payback_met_flag`, `unit_lift_lag_months`
- `merchandise.price.fact_price_investment`: `permanent_flag`, `investment_amount`
- `merchandise.price.fact_unit_volume`: `unit_quantity`

### Q2 FY2027 (10)

How is Walmart telling customers and members about tariff-refund reinvestment, and are other retailers doing the same?

- `merchandise.price.fact_price_investment`: `funding_source_code`, `investment_amount`
- `merchandise.price.fact_price_gap`: `peer_cutting_flag`, `gap_index`
- `merchandise.member.dim_competitor`: `competitor_code`

### Q2 FY2027 (12)

With average ticket running below inflation, is the basket shifting through trade-down, category mix, or smaller-ticket items at Walmart?

- `merchandise.price.fact_average_ticket`: `ticket_amount`, `below_inflation_flag`
- `merchandise.price.fact_inflation_observation`: `inflation_rate`
- `merchandise.price.fact_basket_mix`: `trade_down_flag`, `smaller_ticket_flag`, `mix_share`

### Q1 FY2027 (5)

How sustainable is general-merchandise strength and the ticket assumption into the back half, and how does marketplace expansion support share in that segment at Walmart?

- `merchandise.price.fact_category_demand`: `sales_amount`
- `merchandise.price.fact_average_ticket`: `ticket_amount`
- `merchandise.network.fact_marketplace_supply`: `sku_quantity`, `seller_quantity`
- `merchandise.price.fact_share_position`: `share_change_rate`

### Q1 FY2027 (7)

Are competitors already cutting price to regain share, where do Walmart's price gaps sit, and what tariff rates are in this year's plan?

- `merchandise.price.fact_price_gap`: `gap_index`, `peer_cutting_flag`
- `merchandise.price.fact_share_position`: `share_change_rate`
- `merchandise.price.fact_tariff_plan`: `duty_rate`, `assumed_in_plan_flag`
- `merchandise.member.dim_competitor`: `competitor_code`

### Q1 FY2027 (11)

What is happening in underlying health and wellness after the moderation, and does GLP-1 price pressure free spending for other categories at Walmart?

- `merchandise.price.fact_health_outlook`: `underlying_sales_amount`, `growth_rate`
- `merchandise.price.fact_glp1_price`: `price_index`, `frees_other_spend_flag`
- `merchandise.price.fact_category_demand`: `sales_amount`

### Q1 FY2027 (12)

How much has mix into health and wellness and grocery held back U.S. gross margin, now that mix is a margin source again at Walmart?

- `merchandise.price.fact_merchandise_margin`: `margin_rate`, `mix_source_flag`
- `merchandise.price.fact_basket_mix`: `mix_share`
- `merchandise.price.dim_department`: `department_code`

### Q4 FY2026 (2)

What inflation, including lower drug prices, is assumed in the outlook at Walmart?

- `merchandise.price.fact_inflation_observation`: `inflation_rate`
- `merchandise.price.fact_glp1_price`: `price_index`
- `merchandise.price.dim_inflation_driver`: `driver_code`
- `merchandise.price.fact_comp_sales`: `comp_rate`

### Q4 FY2025 (1)

Is Walmart becoming more sensitive to the economy, with less of a countercyclical share gain, and is that in the sales and earnings outlook?

- `merchandise.price.fact_share_position`: `share_change_rate`, `countercyclical_flag`, `in_outlook_flag`
- `merchandise.price.fact_comp_sales`: `comp_rate`

### Q4 FY2025 (2)

How should mix affect gross margin as general merchandise improves, and have advertising, membership, or marketplace reached scale at Walmart?

- `merchandise.price.fact_merchandise_margin`: `margin_rate`, `mix_source_flag`
- `merchandise.price.fact_category_demand`: `sales_amount`
- `merchandise.network.fact_alternative_revenue`: `contribution_amount`, `versus_potential_code`
- `merchandise.network.fact_membership_profit`: `scale_reached_flag`

### Q4 FY2025 (5)

How did markdowns compare with plan, how much price investment is in next year's guide, and what is the longer-term view of the extra Canada investment at Walmart?

- `merchandise.price.fact_markdown_result`: `markdown_versus_plan_code`
- `merchandise.price.fact_price_investment`: `in_guide_amount`, `investment_amount`
- `merchandise.geography.dim_country`: `country_code`
