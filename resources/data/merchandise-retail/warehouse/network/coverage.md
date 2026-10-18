# Merchandise Inc network, fuel, and capacity

This slice owns sites, openings, fuel gallons, fuel margin, and media capacity. Member counts and shelf prices are owned in the other slices and are partial when named here. Gallons do not store the price per gallon.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `banner_identity` | `banner_id` | `sf:merchandise.member.dim_banner` `banner_id` |
| `brand_identity` | `brand_id` | `sf:merchandise.price.dim_brand` `brand_id` |
| `category_identity` | `category_id` | `sf:merchandise.price.dim_category` `category_id` |
| `channel_identity` | `channel_id` | `sf:merchandise.member.dim_channel` `channel_id` |
| `competitor_identity` | `competitor_id` | `sf:merchandise.member.dim_competitor` `competitor_id` |
| `country_identity` | `country_id` | `sf:merchandise.geography.dim_country` `country_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:merchandise.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `income_cohort_identity` | `income_cohort_id` | `sf:merchandise.member.dim_income_cohort` `income_cohort_id` |
| `member_tier_identity` | `member_tier_id` | `sf:merchandise.member.dim_member_tier` `member_tier_id` |

## Numbered questions

## Costco

### Q4 FY2026 (14)

Where is SG&A pressure building, and can expenses still leverage if comps stay around 6% at Costco?

- `merchandise.network.fact_sga`: `sga_amount`, `leverage_flag`, `pressure_bucket_code`
- `merchandise.network.fact_leverage_threshold`: `comp_rate_required`, `still_leverages_flag`
- `merchandise.price.fact_comp_sales`: `comp_rate`

### Q3 FY2026 (4)

Does a mid-single-digit comp still leverage SG&A the way a 4% to 5% comp used to at Costco?

- `merchandise.network.fact_leverage_threshold`: `comp_rate_required`, `historical_rate`, `still_leverages_flag`
- `merchandise.price.fact_comp_sales`: `comp_rate`
- `merchandise.network.fact_sga`: `leverage_flag`

### Q3 FY2026 (5)

What limits retail media given Costco's tight SKU count versus other retailers?

- `merchandise.network.fact_ad_inventory`: `inventory_quantity`, `sku_count`
- `merchandise.network.fact_retail_media_revenue`: `revenue_amount`, `limited_by_sku_flag`
- `merchandise.network.dim_media_product`: `product_code`

### Q3 FY2026 (7)

With fuel volumes up sharply, where can throughput still increase, and did wider gasoline price gaps reduce profit per gallon at Costco?

- `merchandise.network.fact_fuel_volume`: `gallon_quantity`
- `merchandise.network.fact_fuel_margin`: `profit_per_gallon`, `wider_gap_hurt_flag`
- `merchandise.network.fact_site_capacity`: `throughput_headroom`, `constrained_flag`

### Q3 FY2026 (8)

What does the warehouse pipeline look like in Europe and Asia over the next few years at Costco?

- `merchandise.network.fact_warehouse_pipeline`: `opening_quantity`, `years_out`
- `merchandise.geography.dim_country`: `country_code`
- `merchandise.geography.dim_region`: `region_code`

### Q3 FY2026 (9)

Is AI search already lifting traffic or conversion in particular categories at Costco?

- `merchandise.network.fact_ai_effect`: `traffic_lift_flag`, `conversion_lift_flag`
- `merchandise.demand.fact_traffic`: `traffic_quantity`
- `merchandise.price.dim_category`: `category_code`
- `merchandise.network.dim_ai_application`: `application_code`

### Q2 FY2026 (2)

How large are the savings from checkout and front-end tests, and how widely can they roll at Costco?

- `merchandise.network.fact_checkout_saving`: `saving_amount`, `rollout_share`
- `merchandise.network.dim_site`: `site_code`

### Q2 FY2026 (5)

With Canada volumes near $300 million, what are shopability and capacity constraints, and what is the business-center reopening plan at Costco?

- `merchandise.network.fact_site_capacity`: `capacity_index`, `constrained_flag`
- `merchandise.network.fact_building_productivity`: `sales_per_building_amount`
- `merchandise.network.fact_business_center`: `reopen_quantity`
- `merchandise.geography.dim_country`: `country_code`

### Q2 FY2026 (6)

How do newly available real-estate sites change which markets Costco can enter over the long term?

- `merchandise.network.fact_real_estate_access`: `newly_available_flag`, `market_opened_flag`
- `merchandise.network.fact_warehouse_pipeline`: `opening_quantity`
- `merchandise.network.dim_real_estate_market`: `market_code`

### Q2 FY2026 (8)

What is the roadmap for digital advertising and the marketplace, and where is AI being applied at Costco?

- `merchandise.network.fact_retail_media_revenue`: `revenue_amount`, `growth_rate`
- `merchandise.network.fact_marketplace_supply`: `seller_quantity`, `sku_quantity`
- `merchandise.network.fact_ai_effect`: `applied_to_supply_chain_flag`
- `merchandise.network.dim_ai_application`: `application_code`

### Q1 FY2026 (3)

Can newer warehouse classes keep lifting sales per building above the prior class, and what productivity steps support that at Costco?

- `merchandise.network.fact_building_productivity`: `sales_per_building_amount`, `above_prior_class_flag`
- `merchandise.network.dim_site_class`: `class_code`
- `merchandise.network.fact_productivity_plan`: `productivity_rate`

### Q1 FY2026 (6)

What does the Europe and Asia opening pipeline look like, and what is the remodel philosophy at Costco?

- `merchandise.network.fact_warehouse_pipeline`: `opening_quantity`, `years_out`
- `merchandise.network.fact_remodel_plan`: `capital_amount`, `philosophy_code`
- `merchandise.geography.dim_region`: `region_code`

### Q1 FY2026 (7)

Did higher health-care costs block SG&A leverage, and what productivity rate is expected from here at Costco?

- `merchandise.network.fact_healthcare_cost`: `cost_amount`, `blocked_leverage_flag`
- `merchandise.network.fact_sga`: `leverage_flag`, `sga_amount`
- `merchandise.network.fact_productivity_plan`: `productivity_rate`

### Q1 FY2026 (10)

What is the long-term warehouse potential in the U.S. and worldwide, and are the deepest price investments concentrated in Kirkland at Costco?

- `merchandise.network.fact_warehouse_potential`: `remaining_site_quantity`
- `merchandise.price.fact_price_investment`: `investment_amount`
- `merchandise.price.dim_brand`: `brand_code`
- `merchandise.geography.dim_country`: `country_code`

## Walmart

### Q2 FY2027 (3)

Are the new tariff rates higher or lower than the prior emergency-tariff regime, and should operating income still grow faster than sales into next year once price-investment traffic arrives at Walmart?

- `merchandise.price.fact_tariff_plan`: `duty_rate`, `higher_than_prior_flag`
- `merchandise.network.fact_income_bridge`: `income_growth_rate`, `sales_growth_rate`, `income_faster_flag`
- `merchandise.demand.fact_traffic`: `traffic_quantity`

### Q2 FY2027 (6)

What incremental margin is the digital business producing, and how does Walmart lap today's rollbacks next year without losing store traffic?

- `merchandise.network.fact_ecommerce_profit`: `incremental_margin_rate`
- `merchandise.network.fact_digital_margin`: `margin_rate`
- `merchandise.demand.fact_traffic`: `traffic_quantity`
- `merchandise.price.fact_price_investment`: `permanent_flag`

### Q2 FY2027 (9)

Are any inventory pockets a concern, and what inflation is expected for the rest of the year at Walmart?

- `merchandise.network.fact_inventory_position`: `on_hand_quantity`, `concern_flag`
- `merchandise.price.fact_inflation_observation`: `inflation_rate`
- `merchandise.price.dim_category`: `category_code`

### Q2 FY2027 (11)

How do second-half comps split between traffic and ticket under the price investments, and was the 7% U.S. expense growth timing or higher liability claims at Walmart?

- `merchandise.network.fact_comp_bridge`: `traffic_share`, `ticket_share`
- `merchandise.demand.fact_traffic`: `traffic_quantity`
- `merchandise.price.fact_average_ticket`: `ticket_amount`
- `merchandise.network.fact_claims_cost`: `cost_amount`, `timing_not_runrate_flag`
- `merchandise.network.fact_expense_ratio`: `expense_rate`

### Q1 FY2027 (1)

What would let enterprise and U.S. e-commerce incremental margins move above the recent range if fuel stays high at Walmart?

- `merchandise.network.fact_ecommerce_profit`: `incremental_margin_rate`
- `merchandise.price.fact_fuel_price`: `price_per_gallon`
- `merchandise.network.fact_alternative_revenue`: `contribution_amount`

### Q1 FY2027 (3)

When do the alternative-revenue platforms launched in Canada and Mexico show up in enterprise margin at Walmart?

- `merchandise.network.fact_alternative_revenue`: `contribution_amount`, `versus_potential_code`
- `merchandise.network.fact_retail_media_revenue`: `revenue_amount`
- `merchandise.geography.dim_country`: `country_code`
- `merchandise.network.fact_operating_income`: `income_amount`

### Q1 FY2027 (4)

Where do the main alternative-revenue streams sit versus their potential, if double-digit operating-income growth is harder in this environment at Walmart?

- `merchandise.network.fact_alternative_revenue`: `contribution_amount`, `versus_potential_code`
- `merchandise.network.fact_membership_profit`: `profit_amount`, `scale_reached_flag`
- `merchandise.network.fact_retail_media_revenue`: `revenue_amount`
- `merchandise.network.dim_media_product`: `product_code`

### Q1 FY2027 (8)

Which categories are driving the order lift from the shopping assistant, and how is AI split between customer experience and the supply chain at Walmart?

- `merchandise.demand.fact_assistant_order`: `order_lift_quantity`
- `merchandise.network.fact_ai_effect`: `applied_to_supply_chain_flag`, `conversion_lift_flag`
- `merchandise.price.dim_category`: `category_code`
- `merchandise.network.dim_ai_application`: `application_code`

### Q1 FY2027 (9)

How much volume is on 30- and 60-minute delivery, and how fast does that coverage expand beyond the share of the population already reached at Walmart?

- `merchandise.network.fact_fast_delivery_volume`: `order_quantity`
- `merchandise.network.fact_fast_delivery_coverage`: `coverage_share`, `expansion_pace_code`
- `merchandise.network.dim_fulfillment_speed`: `speed_code`

### Q1 FY2027 (10)

How does marketplace growth split among sellers, SKUs, and order value, and where is the biggest expansion opportunity for the rest of the year at Walmart?

- `merchandise.network.fact_marketplace_supply`: `seller_quantity`, `sku_quantity`
- `merchandise.network.fact_marketplace_value`: `order_value_amount`, `growth_component_code`
- `merchandise.price.dim_category`: `category_code`

### Q1 FY2027 (13)

Why can second-quarter operating income growth accelerate versus the first quarter even with a full quarter of fuel headwind at Walmart?

- `merchandise.network.fact_operating_income`: `income_amount`, `acceleration_flag`
- `merchandise.network.fact_fuel_margin`: `profit_per_gallon`
- `merchandise.price.fact_merchandise_margin`: `margin_rate`

### Q4 FY2026 (3)

How much of the margin outlook is mix, and are inventory gains only from automation or also from other programs by region at Walmart?

- `merchandise.price.fact_merchandise_margin`: `margin_rate`, `mix_source_flag`
- `merchandise.network.fact_inventory_position`: `on_hand_quantity`
- `merchandise.network.fact_automation_gain`: `gain_flag`, `region_program_flag`
- `merchandise.geography.dim_region`: `region_code`

### Q4 FY2026 (4)

Should advertising growth moderate from here, and which advertiser types or categories are accelerating versus still underpenetrated at Walmart?

- `merchandise.network.fact_retail_media_revenue`: `growth_rate`, `revenue_amount`
- `merchandise.network.fact_advertiser_mix`: `growth_rate`, `underpenetrated_flag`
- `merchandise.network.dim_advertiser_type`: `advertiser_code`
- `merchandise.price.dim_category`: `category_code`

### Q4 FY2026 (5)

What threatens e-commerce share momentum, and does that change the near-term profit path at Walmart?

- `merchandise.network.fact_share_threat`: `threat_flag`, `profit_path_changed_flag`
- `merchandise.network.fact_ecommerce_profit`: `incremental_margin_rate`, `profitable_flag`
- `merchandise.member.dim_competitor`: `competitor_code`

### Q4 FY2025 (3)

If e-commerce incremental margins are already healthy, why not reinvest faster to grow the top of the funnel at Walmart?

- `merchandise.network.fact_ecommerce_profit`: `incremental_margin_rate`, `reinvest_faster_flag`
- `merchandise.demand.fact_traffic`: `traffic_quantity`

### Q4 FY2025 (6)

What is the dilution and integration plan for VIZIO, and how fast can Walmart Connect keep growing?

- `merchandise.network.fact_device_media`: `dilution_amount`, `integration_stage_code`
- `merchandise.network.fact_retail_media_revenue`: `growth_rate`, `revenue_amount`
- `merchandise.price.dim_brand`: `brand_code`

### Q4 FY2025 (7)

What are the main drivers of better e-commerce profit, and what share of profit dollars already comes from high-margin alternative revenue at Walmart?

- `merchandise.network.fact_ecommerce_profit`: `incremental_margin_rate`
- `merchandise.network.fact_alternative_revenue`: `contribution_amount`
- `merchandise.network.dim_media_product`: `product_code`

### Q4 FY2025 (8)

Do e-commerce incremental margins rise from here, and when does e-commerce itself become profitable at Walmart?

- `merchandise.network.fact_ecommerce_profit`: `incremental_margin_rate`, `profitable_flag`

### Q4 FY2025 (9)

What would make the expense ratio better or worse than expected this year, and how should that ratio trend longer term at Walmart?

- `merchandise.network.fact_expense_ratio`: `expense_rate`, `better_or_worse_code`, `long_term_direction`
- `merchandise.network.fact_income_bridge`: `sales_growth_rate`

### Q4 FY2025 (10)

How is PhonePe growing and how profitable is it, and where can returns on investment still rise at Walmart?

- `merchandise.network.fact_payments_arm`: `growth_rate`, `profit_amount`, `roi_headroom_flag`
- `merchandise.network.dim_payments_business`: `business_code`
