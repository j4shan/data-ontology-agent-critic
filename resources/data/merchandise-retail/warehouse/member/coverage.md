# Merchandise Inc member and traffic

This slice owns banners, members, cohorts, channels, and trip quantity. Shelf prices, warehouse capacity, and fuel gallons are owned in the other slices and are partial when named here.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `category_identity` | `category_id` | `sf:merchandise.price.dim_category` `category_id` |

## Numbered questions

## Costco

### Q4 FY2026 (2)

As membership growth converges with unit growth, can rising spend by existing members still carry the business at Costco?

- `merchandise.member.fact_member_count`: `growth_rate`, `member_quantity`
- `merchandise.network.fact_building_productivity`: `sales_per_building_amount`
- `merchandise.member.fact_member_spend`: `spend_per_member_amount`, `existing_member_carry_flag`

### Q4 FY2026 (4)

After about eight quarters of slower membership growth, what would reverse that trend and when at Costco?

- `merchandise.member.fact_member_count`: `growth_rate`, `slowed_flag`
- `merchandise.member.fact_member_signup`: `signup_quantity`
- `merchandise.member.dim_member_tier`: `tier_code`

### Q4 FY2026 (6)

How is Costco positioned as agent-style commerce changes how members shop?

- `merchandise.demand.fact_agent_commerce`: `interface_ready_flag`, `represented_in_answers_flag`
- `merchandise.member.fact_digital_engagement`: `engaged_share`
- `merchandise.demand.fact_traffic`: `traffic_quantity`

### Q4 FY2026 (7)

Do younger, more digital new members change what Costco should offer them?

- `merchandise.member.fact_digital_offer`: `offer_fits_younger_flag`
- `merchandise.member.dim_age_cohort`: `cohort_code`
- `merchandise.member.fact_digital_engagement`: `engaged_share`

### Q4 FY2026 (8)

How are new member households trending in international markets, especially Asia, as a source of membership growth at Costco?

- `merchandise.member.fact_household_growth`: `new_household_quantity`
- `merchandise.geography.dim_country`: `country_code`
- `merchandise.member.fact_member_count`: `member_quantity`

### Q4 FY2026 (11)

What does the spend curve look like as younger members mature, and how much lifetime value is still ahead of them at Costco?

- `merchandise.member.fact_member_tenure`: `tenure_year`, `spend_index`, `lifetime_value_ahead_amount`
- `merchandise.member.fact_member_spend`: `spend_per_member_amount`
- `merchandise.member.dim_age_cohort`: `cohort_code`

### Q4 FY2026 (13)

Is third-party delivery the long-term answer for younger members who want speed, or is more needed at Costco?

- `merchandise.demand.fact_delivery_use`: `order_share`, `speed_met_flag`, `long_term_answer_flag`
- `merchandise.member.dim_age_cohort`: `cohort_code`
- `merchandise.member.dim_channel`: `channel_code`

### Q3 FY2026 (6)

Are executive-membership gains mostly gold members trading up or new members choosing the higher tier at Costco?

- `merchandise.member.fact_member_signup`: `signup_quantity`
- `merchandise.member.dim_member_tier`: `tier_code`
- `merchandise.member.fact_member_count`: `member_quantity`

### Q2 FY2026 (1)

How did weather help or hurt January and February sales at Costco?

- `merchandise.demand.fact_monthly_sales`: `sales_amount`
- `merchandise.member.dim_weather_event`: `event_code`
- `merchandise.geography.dim_calendar_month`: `month_code`

### Q2 FY2026 (4)

Do more competitive openings this year hit nearby membership, and how should Costco appear when a member asks a chatbot?

- `merchandise.member.fact_competitor_opening`: `nearby_opening_quantity`, `membership_hit_flag`
- `merchandise.demand.fact_agent_commerce`: `represented_in_answers_flag`
- `merchandise.member.fact_member_signup`: `signup_quantity`

### Q2 FY2026 (7)

Is the U.S. renewal-rate dip the bottom, and when should the measured renewal rate turn up at Costco?

- `merchandise.member.fact_member_renewal`: `renewal_rate`, `dip_is_bottom_flag`
- `merchandise.geography.dim_country`: `country_code`
- `merchandise.member.dim_member_tier`: `tier_code`

### Q1 FY2026 (1)

Is there any concern in traffic even though absolute results are strong at Costco?

- `merchandise.demand.fact_traffic`: `traffic_quantity`, `concern_flag`
- `merchandise.price.fact_comp_sales`: `comp_rate`

### Q1 FY2026 (2)

With U.S. openings at a multi-decade high, does membership acquisition need to change as short-term promotions are lapped at Costco?

- `merchandise.network.fact_warehouse_pipeline`: `opening_quantity`
- `merchandise.member.fact_member_signup`: `signup_quantity`, `promotion_lapped_flag`
- `merchandise.geography.dim_country`: `country_code`

### Q1 FY2026 (4)

What offset renewal softness among more digital members at Costco?

- `merchandise.member.fact_member_renewal`: `renewal_rate`, `digital_soft_flag`
- `merchandise.member.dim_join_path`: `path_code`

### Q1 FY2026 (5)

What share of members now engage digitally versus before at Costco?

- `merchandise.member.fact_digital_engagement`: `engaged_share`, `versus_prior_share`
- `merchandise.member.fact_member_count`: `member_quantity`

### Q1 FY2026 (11)

How far has personalization rolled, and what conversion or attachment has it produced at Costco?

- `merchandise.member.fact_personalization`: `coverage_share`, `conversion_lift`, `attachment_lift`

### Q1 FY2026 (12)

Is the expected further dip in renewal rates conservatism, and how did comps move through November into December by customer at Costco?

- `merchandise.member.fact_member_renewal`: `renewal_rate`, `outlook_dip_flag`
- `merchandise.demand.fact_monthly_sales`: `sales_amount`
- `merchandise.geography.dim_calendar_month`: `month_code`
- `merchandise.member.dim_age_cohort`: `cohort_code`

## Walmart

### Q2 FY2027 (2)

Is higher fuel adding a new burden on lower-income shoppers, and does the unit response to rollbacks show up immediately or with a lag of several months at Walmart?

- `merchandise.network.fact_fuel_burden`: `burden_flag`
- `merchandise.demand.fact_income_trade`: `traffic_index`
- `merchandise.price.fact_rollback_payback`: `unit_lift_lag_months`, `payback_met_flag`
- `merchandise.member.dim_income_cohort`: `cohort_code`

### Q1 FY2027 (2)

What keeps the traffic acceleration at Walmart U.S. and Sam's going, and could tariff rebates fund that versus offsetting energy costs?

- `merchandise.demand.fact_traffic`: `traffic_quantity`
- `merchandise.member.dim_banner`: `banner_code`
- `merchandise.price.fact_price_investment`: `funding_source_code`
- `merchandise.network.fact_fuel_burden`: `burden_flag`

### Q1 FY2027 (6)

Can trade-in from higher-income shoppers offset pressure on the lower end as fuel rises and tax stimulus fades, and could grocery price competition mute inflation and squeeze margin as egg deflation ends at Walmart?

- `merchandise.demand.fact_income_trade`: `traffic_index`, `trade_in_flag`
- `merchandise.member.dim_income_cohort`: `cohort_code`
- `merchandise.price.fact_inflation_observation`: `inflation_rate`
- `merchandise.price.fact_merchandise_margin`: `margin_rate`
- `merchandise.price.dim_inflation_driver`: `driver_code`

### Q1 FY2027 (14)

Are higher gas prices shifting trips online versus in store, or changing what people buy at Walmart?

- `merchandise.price.fact_fuel_price`: `price_per_gallon`
- `merchandise.demand.fact_trip_frequency`: `trip_quantity`
- `merchandise.member.dim_channel`: `channel_code`
- `merchandise.price.fact_basket_mix`: `mix_share`

### Q4 FY2026 (1)

How could agent-style shopping change customer traffic, loyalty, and advertising monetization at Walmart?

- `merchandise.demand.fact_agent_commerce`: `interface_ready_flag`
- `merchandise.demand.fact_traffic`: `traffic_quantity`
- `merchandise.member.fact_loyalty_response`: `response_code`
- `merchandise.network.fact_retail_media_revenue`: `revenue_amount`

### Q4 FY2026 (6)

How do U.S. shoppers differ by income, how have GLP-1 users changed trip frequency and basket size, and how does that change inventory plans at Walmart?

- `merchandise.demand.fact_income_trade`: `traffic_index`
- `merchandise.demand.fact_trip_frequency`: `trip_quantity`, `basket_size_index`
- `merchandise.price.fact_glp1_price`: `price_index`
- `merchandise.network.fact_inventory_position`: `on_hand_quantity`
- `merchandise.member.dim_income_cohort`: `cohort_code`

### Q4 FY2025 (4)

Is Walmart Plus growth steady or accelerating, how much is the assist tier, and what like-for-like inflation is assumed in grocery versus general merchandise?

- `merchandise.member.fact_loyalty_response`: `response_code`, `assist_tier_share`, `growth_pace_code`
- `merchandise.member.dim_member_tier`: `tier_code`
- `merchandise.price.fact_inflation_observation`: `inflation_rate`
- `merchandise.price.dim_department`: `department_code`
