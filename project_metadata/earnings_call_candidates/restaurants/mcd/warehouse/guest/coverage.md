# Burger Inc guest demand warehouse

This slice covers guest demand, menu, marketing, loyalty, and commercial sales.
Restaurant, franchisee, country, segment, calendar day, and accounting period
identifiers are foreign keys. Those populations are not defined in this slice.
Country and segment filters, including the U.S., international operated markets,
developmental license, France, the U.K., China, and Australia, use `country_id`
and `segment_id`. April versus the rest of a quarter uses `calendar_day_id`
inside `accounting_period_id`.

No dataset stores a row count of itself.

## Questions

### Q2 2026 (1)

Near-term U.S. sales once value leadership is back, set against the slower chicken-quality work and the value menu.

- `burger.sales.fact_value_score_country`: `country_id`, `segment_id`, `value_score`, `value_leadership_index`, `comparable_sales_amount`
- `burger.sales.fact_restaurant_day_sales`: `country_id`, `segment_id`, `comparable_sales_amount`, `traffic_contribution_amount`, `check_contribution_amount`, `price_contribution_amount`
- `burger.menu.dim_product`: `chicken_quality_index`, `is_value_menu_item`, `menu_tier`, `product_id`
- `burger.menu.dim_product_category`: `category_family`, `product_category_id`
- `burger.menu.dim_protein`: `protein_name`, `is_chicken`, `protein_id`
- `burger.menu.fact_protein_mix_period`: `country_id`, `segment_id`, `quantity_share_rate`, `protein_id`
- `burger.offer.dim_offer`: `offer_structure`, `offer_name`, `offer_id`
- `burger.offer.fact_offer_performance`: `country_id`, `segment_id`, `offer_sales_amount`, `traffic_lift_rate`, `offer_id`

### Q2 2026 (2)

How quickly U.S. operations and marketing problems can be fixed, and what that implies for sales over the next quarter.

- `burger.sales.fact_market_period_outlook`: `country_id`, `segment_id`, `accounting_period_id`, `operations_fix_lead_time_days`, `marketing_fix_lead_time_days`, `comparable_sales_amount`, `next_period_comparable_sales_amount`, `guest_count`
- `burger.guest.fact_restaurant_day_throughput`: `country_id`, `segment_id`, `service_time_seconds`, `throughput_rate`, `guest_count`
- `burger.marketing.dim_marketing_campaign`: `development_process_name`, `supersedes_prior_process_flag`, `marketing_campaign_id`
- `burger.marketing.fact_marketing_campaign`: `country_id`, `segment_id`, `attributed_guest_count`, `demand_lift_rate`, `marketing_campaign_id`
- `burger.sales.fact_restaurant_day_sales`: `country_id`, `segment_id`, `accounting_period_id`, `comparable_sales_amount`, `guest_count`

### Q2 2026 (6)

Whether marketing development has changed, or demand is still anticipated the way it was under the prior process.

- `burger.marketing.dim_marketing_campaign`: `development_process_name`, `supersedes_prior_process_flag`, `demand_anticipation_method`, `marketing_campaign_id`
- `burger.marketing.fact_marketing_campaign`: `forecast_guest_count`, `attributed_guest_count`, `demand_lift_rate`, `marketing_campaign_id`
- `burger.marketing.bridge_campaign_offer`: `marketing_campaign_id`, `offer_id`

### Q2 2026 (8)

Whether too many products launching at once is hurting throughput and guest counts.

- `burger.guest.fact_restaurant_day_throughput`: `concurrent_launch_count`, `throughput_rate`, `service_time_seconds`, `guest_count`, `restaurant_id`, `calendar_day_id`
- `burger.menu.dim_product`: `product_id`, `launch_calendar_day_id`, `product_name`
- `burger.guest.dim_guest_visit`: `guest_visit_id`, `calendar_day_id`, `restaurant_id`

### Q2 2026 (9)

Whether the beverage lineup is raising attachment, and how large a share of those sales is energy drinks.

- `burger.sales.fact_beverage_test_market`: `attachment_rate`, `energy_share_rate`, `beverage_unit_count`, `beverage_sales_amount`, `attached_check_count`, `check_count`, `includes_energy_flag`, `beverage_platform_id`, `country_id`, `segment_id`
- `burger.menu.dim_beverage_platform`: `platform_name`, `is_energy_drink`, `beverage_platform_id`
- `burger.menu.dim_product_category`: `category_family`, `product_category_id`
- `burger.sales.fact_check_line`: `quantity`, `net_sales_amount`, `beverage_platform_id`, `product_category_id`, `check_id`
- `burger.sales.fact_check`: `check_id`, `item_count`, `net_sales_amount`, `channel_id`
- `burger.sales.dim_check`: `check_id`, `channel_id`
- `burger.guest.dim_channel`: `channel_name`, `is_digital`, `channel_id`

### Q1 2026 (1)

How U.S. sales should trend through the rest of 2026 given value, marketing, menu innovation, and a weak consumer.

- `burger.sales.fact_market_period_outlook`: `country_id`, `segment_id`, `accounting_period_id`, `comparable_sales_amount`, `next_period_comparable_sales_amount`, `value_driver_sales_amount`, `marketing_driver_sales_amount`, `menu_innovation_driver_sales_amount`, `consumer_pressure_index`, `guest_count`
- `burger.sales.fact_restaurant_day_sales`: `country_id`, `segment_id`, `comparable_sales_amount`, `guest_count`, `traffic_contribution_amount`, `check_contribution_amount`, `price_contribution_amount`
- `burger.sales.fact_value_score_country`: `value_score`, `value_mix_rate`, `country_id`, `segment_id`
- `burger.marketing.fact_marketing_campaign`: `attributed_sales_amount`, `attributed_guest_count`, `demand_lift_rate`, `country_id`, `segment_id`
- `burger.menu.fact_menu_daypart`: `sales_amount`, `quantity_sold`, `product_id`, `country_id`, `segment_id`
- `burger.guest.fact_cohort_daypart_demand`: `demand_index`, `guest_count`, `gas_price_amount`, `income_cohort_id`, `country_id`, `segment_id`
- `burger.marketing.bridge_campaign_offer`: `marketing_campaign_id`, `offer_id`

### Q1 2026 (2)

Why the value offer needs another iteration, and how often it should change.

- `burger.offer.dim_offer`: `offer_id`, `prior_offer_id`, `iteration_number`, `change_cadence_days`, `offer_structure`
- `burger.offer.fact_offer_performance`: `traffic_lift_rate`, `incremental_guest_count`, `redeemed_check_count`, `offer_sales_amount`, `average_check_amount`, `offer_id`, `country_id`, `segment_id`

### Q1 2026 (3)

Why some markets, including France, have trailed other markets that already had value offers in place.

- `burger.sales.fact_value_score_country`: `country_id`, `value_score`, `value_leadership_index`, `value_mix_rate`, `comparable_sales_amount`, `guest_count`
- `burger.offer.fact_offer_performance`: `country_id`, `offer_sales_amount`, `traffic_lift_rate`, `discount_rate`, `incremental_guest_count`, `offer_id`
- `burger.offer.dim_offer`: `offer_structure`, `price_certainty_model`, `offer_id`

### Q1 2026 (8)

How higher-income and lower-income guest trends are diverging.

- `burger.guest.fact_cohort_daypart_demand`: `income_cohort_id`, `guest_count`, `guest_count_change_rate`, `sales_amount`, `traffic_share_rate`, `demand_index`, `country_id`, `segment_id`
- `burger.guest.dim_income_cohort`: `cohort_name`, `income_band_name`, `income_cohort_id`
- `burger.guest.dim_guest_visit`: `income_cohort_id`, `guest_visit_id`, `is_baseline_visit`
- `burger.sales.fact_check`: `income_cohort_id`, `guest_count`, `net_sales_amount`, `check_id`
- `burger.sales.dim_check`: `income_cohort_id`, `check_id`
- `burger.loyalty.fact_loyalty_member_period`: `income_cohort_id`, `visit_frequency_rate`, `visit_count`

### Q1 2026 (9)

Whether World Cup activity lifted digital adoption more than overall demand, and whether loyalty can turn that into higher visit frequency.

- `burger.marketing.dim_marketing_campaign`: `is_world_cup_campaign`, `digital_led_flag`, `campaign_name`, `marketing_campaign_id`
- `burger.marketing.fact_marketing_campaign`: `digital_adoption_lift_rate`, `demand_lift_rate`, `incremental_visit_count`, `attributed_guest_count`, `marketing_campaign_id`, `country_id`
- `burger.loyalty.dim_loyalty_member`: `loyalty_member_id`, `country_id`, `income_cohort_id`
- `burger.loyalty.fact_loyalty_member_period`: `loyalty_member_id`, `accounting_period_id`, `visit_count`, `visit_frequency_rate`, `digital_transaction_count`, `digital_adoption_rate`
- `burger.guest.dim_channel`: `is_digital`, `channel_name`, `channel_id`
- `burger.sales.dim_check`: `loyalty_member_id`, `channel_id`, `check_id`
- `burger.sales.fact_check`: `loyalty_member_id`, `channel_id`, `guest_count`, `net_sales_amount`

### Q1 2026 (10)

Which U.K. tactics can transfer to the U.S. and France.

- `burger.marketing.dim_marketing_campaign`: `tactic_name`, `campaign_name`, `marketing_campaign_id`
- `burger.marketing.fact_marketing_campaign`: `country_id`, `segment_id`, `attributed_sales_amount`, `attributed_guest_count`, `demand_lift_rate`, `marketing_campaign_id`
- `burger.sales.fact_value_score_country`: `country_id`, `segment_id`, `value_score`, `comparable_sales_amount`, `guest_count`

### Q1 2026 (12)

Why an energy brand was left out of the initial U.S. beverage launch.

- `burger.menu.dim_beverage_platform`: `platform_name`, `is_energy_brand`, `is_energy_drink`, `excluded_from_initial_us_launch_flag`, `exclusion_reason`, `beverage_platform_id`
- `burger.sales.fact_beverage_test_market`: `country_id`, `segment_id`, `includes_energy_flag`, `beverage_platform_id`, `attachment_rate`, `energy_share_rate`, `beverage_sales_amount`, `platform_mix_rate`

### Q1 2026 (14)

After the April comparison, whether the rest of the second quarter returns to the prior run rate.

- `burger.sales.fact_restaurant_day_sales`: `calendar_day_id`, `accounting_period_id`, `country_id`, `segment_id`, `comparable_sales_amount`, `comparable_guest_count`, `average_check_amount`, `guest_count`, `traffic_contribution_amount`, `price_contribution_amount`

### Q1 2026 (15)

Whether the rise in gas prices has already reduced demand, especially among lower-income guests.

- `burger.guest.fact_cohort_daypart_demand`: `gas_price_amount`, `guest_count`, `guest_count_change_rate`, `demand_index`, `sales_amount`, `income_cohort_id`, `calendar_day_id`, `country_id`
- `burger.guest.dim_income_cohort`: `cohort_name`, `income_cohort_id`

### Q1 2026 (17)

How chicken share has moved in the U.S. and other markets, and whether higher beef cost is shifting mix toward chicken.

- `burger.menu.fact_protein_mix_period`: `protein_id`, `country_id`, `segment_id`, `accounting_period_id`, `quantity_share_rate`, `sales_share_rate`, `quantity_sold`, `protein_cost_index`, `mix_shift_rate`
- `burger.menu.dim_protein`: `protein_name`, `is_chicken`, `is_beef`, `protein_id`
- `burger.menu.dim_product_category`: `category_family`, `product_category_id`
- `burger.sales.fact_check_line`: `quantity`, `net_sales_amount`, `protein_id`, `product_category_id`, `country_id`, `segment_id`

### Q4 2025 (1)

What U.S. sales pace to expect in 2026 if value, marketing, and menu innovation work together.

- `burger.sales.fact_market_period_outlook`: `country_id`, `segment_id`, `accounting_period_id`, `comparable_sales_amount`, `value_driver_sales_amount`, `marketing_driver_sales_amount`, `menu_innovation_driver_sales_amount`, `guest_count`
- `burger.sales.fact_value_score_country`: `value_score`, `value_mix_rate`, `country_id`, `segment_id`
- `burger.marketing.fact_marketing_campaign`: `attributed_sales_amount`, `attributed_guest_count`, `country_id`, `segment_id`
- `burger.offer.fact_offer_performance`: `offer_sales_amount`, `traffic_lift_rate`, `country_id`, `segment_id`
- `burger.marketing.bridge_campaign_offer`: `marketing_campaign_id`, `offer_id`
- `burger.sales.fact_restaurant_day_sales`: `comparable_sales_amount`, `traffic_contribution_amount`, `check_contribution_amount`, `price_contribution_amount`, `country_id`, `segment_id`

### Q4 2025 (8)

How the U.S. beverage rollout proceeds, including restaurants and platforms still to be added.

- `burger.sales.fact_beverage_test_market`: `country_id`, `segment_id`, `beverage_platform_id`, `rolled_out_restaurant_count`, `remaining_rollout_restaurant_count`, `test_restaurant_count`, `beverage_sales_amount`, `beverage_unit_count`, `attachment_rate`, `includes_energy_flag`
- `burger.menu.dim_beverage_platform`: `rollout_wave_name`, `platform_name`, `excluded_from_initial_us_launch_flag`, `beverage_platform_id`

### Q4 2025 (10)

How the U.S. menu is being adjusted for guests using GLP-1 medicines, including by daypart.

- `burger.menu.dim_product`: `glp1_menu_role`, `suits_glp1_guest_flag`, `product_name`, `menu_tier`, `product_id`
- `burger.menu.fact_menu_daypart`: `product_id`, `daypart_id`, `country_id`, `segment_id`, `glp1_guest_share_rate`, `operator_request_count`, `consumption_index`, `quantity_sold`, `sales_amount`
- `burger.guest.dim_daypart`: `daypart_name`, `is_breakfast`, `daypart_id`
- `burger.sales.fact_check`: `daypart_id`, `guest_count`, `net_sales_amount`, `country_id`, `segment_id`
- `burger.sales.dim_check`: `daypart_id`, `check_id`, `country_id`, `segment_id`
- `burger.sales.fact_check_line`: `product_id`, `daypart_id`, `quantity`, `net_sales_amount`, `country_id`, `segment_id`

### Q4 2025 (11)

Where U.S. value scores and value mix sit, and which premium items can balance that barbell.

- `burger.sales.fact_value_score_country`: `country_id`, `segment_id`, `value_score`, `value_mix_rate`, `premium_mix_rate`, `comparable_sales_amount`
- `burger.menu.dim_product`: `menu_tier`, `product_name`, `is_value_menu_item`, `product_id`
- `burger.offer.dim_offer`: `offer_structure`, `offer_name`, `offer_id`
- `burger.sales.fact_check_line`: `product_id`, `net_sales_amount`, `quantity`, `country_id`, `segment_id`
- `burger.menu.fact_menu_daypart`: `product_id`, `sales_amount`, `quantity_sold`, `country_id`, `segment_id`
- `burger.sales.fact_check`: `offer_id`, `net_sales_amount`, `discount_amount`, `country_id`, `segment_id`

### Q3 2025 (3)

Whether underlying guest counts are improving, or only promoted sales are.

- `burger.sales.fact_restaurant_day_sales`: `baseline_guest_count`, `promoted_guest_count`, `promoted_sales_amount`, `guest_count`, `comparable_sales_amount`, `country_id`, `segment_id`, `calendar_day_id`
- `burger.guest.dim_guest_visit`: `is_baseline_visit`, `is_promoted_visit`, `guest_visit_id`, `country_id`, `segment_id`

### Q3 2025 (4)

What the beverage-test mix looks like with the energy drink and without it.

- `burger.sales.fact_beverage_test_market`: `includes_energy_flag`, `beverage_platform_id`, `beverage_unit_count`, `beverage_sales_amount`, `platform_mix_rate`, `energy_share_rate`, `attachment_rate`, `country_id`
- `burger.menu.dim_beverage_platform`: `platform_name`, `is_energy_drink`, `beverage_platform_id`
- `burger.sales.fact_check_line`: `beverage_platform_id`, `quantity`, `net_sales_amount`, `product_id`

### Q3 2025 (5)

Whether higher-income traffic is accelerating from trade-down, and whether China is the exception inside developmental-license markets.

- `burger.guest.fact_cohort_daypart_demand`: `income_cohort_id`, `country_id`, `segment_id`, `calendar_day_id`, `guest_count`, `guest_count_change_rate`, `trade_down_guest_count`, `traffic_share_rate`
- `burger.guest.dim_income_cohort`: `cohort_name`, `income_cohort_id`

### Q3 2025 (6)

Whether a wider everyday-value-meal discount gives U.S. guests the price certainty associated with the Australia market, enough to support a national price.

- `burger.offer.dim_offer`: `offer_structure`, `price_certainty_model`, `offer_id`, `offer_name`
- `burger.offer.fact_offer_performance`: `country_id`, `discount_rate`, `sharp_price_amount`, `discount_amount`, `offer_sales_amount`, `offer_id`
- `burger.sales.fact_value_score_country`: `country_id`, `segment_id`, `everyday_meal_discount_rate`, `national_price_certainty_rate`, `value_mix_rate`, `value_score`

### Q3 2025 (7)

Whether the value push is taking share across income groups, and whether digital and product moves are working at the higher end.

- `burger.guest.fact_cohort_daypart_demand`: `income_cohort_id`, `traffic_share_rate`, `digital_guest_count`, `digital_sales_amount`, `menu_driven_guest_count`, `value_offer_guest_count`, `guest_count`, `country_id`, `segment_id`
- `burger.guest.dim_income_cohort`: `cohort_name`, `income_cohort_id`
- `burger.guest.dim_channel`: `is_digital`, `channel_name`, `channel_id`
- `burger.sales.fact_check`: `income_cohort_id`, `channel_id`, `loyalty_member_id`, `net_sales_amount`, `guest_count`
- `burger.sales.dim_check`: `income_cohort_id`, `channel_id`, `loyalty_member_id`, `check_id`
- `burger.sales.fact_check_line`: `income_cohort_id`, `product_id`, `quantity`, `net_sales_amount`
- `burger.loyalty.dim_loyalty_member`: `loyalty_member_id`, `income_cohort_id`, `enrollment_channel_id`
- `burger.loyalty.fact_loyalty_member_period`: `income_cohort_id`, `digital_adoption_rate`, `digital_transaction_count`, `visit_frequency_rate`

### Q3 2025 (8)

Whether higher-income traffic is trading down from fast casual, and whether the everyday value meal has helped breakfast.

- `burger.guest.fact_cohort_daypart_demand`: `income_cohort_id`, `daypart_id`, `fast_casual_trade_down_guest_count`, `trade_down_guest_count`, `value_offer_guest_count`, `guest_count`, `guest_count_change_rate`
- `burger.guest.dim_daypart`: `daypart_name`, `is_breakfast`, `daypart_id`
- `burger.guest.dim_income_cohort`: `cohort_name`, `income_cohort_id`
- `burger.sales.fact_check`: `daypart_id`, `offer_id`, `income_cohort_id`, `guest_count`, `net_sales_amount`
- `burger.sales.dim_check`: `daypart_id`, `offer_id`, `income_cohort_id`, `check_id`

### Q3 2025 (9)

Whether lower-income guests can be held with value while higher-income trade-down is gained.

- `burger.guest.fact_cohort_daypart_demand`: `income_cohort_id`, `retained_guest_count`, `trade_down_guest_count`, `value_offer_guest_count`, `guest_count`, `guest_count_change_rate`, `calendar_day_id`
- `burger.guest.dim_income_cohort`: `cohort_name`, `income_cohort_id`
- `burger.sales.fact_check`: `income_cohort_id`, `offer_id`, `guest_count`, `net_sales_amount`
- `burger.sales.dim_check`: `income_cohort_id`, `offer_id`, `check_id`

### Q4 2025 (7)

How much higher loyalty frequency moves the system, and what still blocks finishing the global technology stack.

- `burger.loyalty.fact_loyalty_member_period`: `visit_frequency_rate`, `visit_count`, `member_sales_amount`, `country_id`, `segment_id`
- `burger.technology.fact_technology_rollout`: `loyalty_visit_lift_rate`, `system_sales_lift_amount`, `stores_live_count`, `stores_blocked_count`, `blocker_reason`, `technology_program_id`, `country_id`
- `burger.technology.dim_technology_program`: `program_name`, `stack_role`

### Q4 2025 (9)

How first-quarter sales should be read through weather and the remaining food-safety comparison.

- `burger.sales.fact_restaurant_day_sales`: `weather_event_code`, `food_safety_comparison_flag`, `comparable_sales_amount`, `sales_excluding_temporary_drag_amount`, `calendar_day_id`

## Datasets

| Qualified name | Questions |
| --- | --- |
| `burger.guest.dim_channel` | Q2 2026 (9); Q1 2026 (9); Q3 2025 (7) |
| `burger.guest.dim_daypart` | Q4 2025 (10); Q3 2025 (8) |
| `burger.guest.dim_guest_visit` | Q2 2026 (8); Q1 2026 (8); Q3 2025 (3) |
| `burger.guest.dim_income_cohort` | Q1 2026 (8); Q1 2026 (15); Q3 2025 (5); Q3 2025 (7); Q3 2025 (8); Q3 2025 (9) |
| `burger.guest.fact_cohort_daypart_demand` | Q1 2026 (1); Q1 2026 (8); Q1 2026 (15); Q3 2025 (5); Q3 2025 (7); Q3 2025 (8); Q3 2025 (9) |
| `burger.guest.fact_restaurant_day_throughput` | Q2 2026 (2); Q2 2026 (8) |
| `burger.loyalty.dim_loyalty_member` | Q1 2026 (9); Q3 2025 (7) |
| `burger.loyalty.fact_loyalty_member_period` | Q1 2026 (8); Q1 2026 (9); Q4 2025 (7); Q3 2025 (7) |
| `burger.marketing.bridge_campaign_offer` | Q2 2026 (6); Q1 2026 (1); Q4 2025 (1) |
| `burger.marketing.dim_marketing_campaign` | Q2 2026 (2); Q2 2026 (6); Q1 2026 (9); Q1 2026 (10) |
| `burger.marketing.fact_marketing_campaign` | Q2 2026 (2); Q2 2026 (6); Q1 2026 (1); Q1 2026 (9); Q1 2026 (10); Q4 2025 (1) |
| `burger.menu.dim_beverage_platform` | Q2 2026 (9); Q1 2026 (12); Q4 2025 (8); Q3 2025 (4) |
| `burger.menu.dim_product` | Q2 2026 (1); Q2 2026 (8); Q4 2025 (10); Q4 2025 (11) |
| `burger.menu.dim_product_category` | Q2 2026 (1); Q2 2026 (9); Q1 2026 (17) |
| `burger.menu.dim_protein` | Q2 2026 (1); Q1 2026 (17) |
| `burger.menu.fact_menu_daypart` | Q1 2026 (1); Q4 2025 (10); Q4 2025 (11) |
| `burger.menu.fact_protein_mix_period` | Q2 2026 (1); Q1 2026 (17) |
| `burger.offer.dim_offer` | Q2 2026 (1); Q1 2026 (2); Q1 2026 (3); Q4 2025 (11); Q3 2025 (6) |
| `burger.offer.fact_offer_performance` | Q2 2026 (1); Q1 2026 (2); Q1 2026 (3); Q4 2025 (1); Q3 2025 (6) |
| `burger.sales.dim_check` | Q2 2026 (9); Q1 2026 (8); Q1 2026 (9); Q4 2025 (10); Q3 2025 (7); Q3 2025 (8); Q3 2025 (9) |
| `burger.sales.fact_beverage_test_market` | Q2 2026 (9); Q1 2026 (12); Q4 2025 (8); Q3 2025 (4) |
| `burger.sales.fact_check` | Q2 2026 (9); Q1 2026 (8); Q1 2026 (9); Q4 2025 (10); Q4 2025 (11); Q3 2025 (7); Q3 2025 (8); Q3 2025 (9) |
| `burger.sales.fact_check_line` | Q2 2026 (9); Q1 2026 (17); Q4 2025 (10); Q4 2025 (11); Q3 2025 (4); Q3 2025 (7) |
| `burger.sales.fact_market_period_outlook` | Q2 2026 (2); Q1 2026 (1); Q4 2025 (1) |
| `burger.sales.fact_restaurant_day_sales` | Q2 2026 (1); Q2 2026 (2); Q1 2026 (1); Q1 2026 (14); Q4 2025 (1); Q4 2025 (9); Q3 2025 (3) |
| `burger.technology.dim_technology_program` | Q4 2025 (7) |
| `burger.technology.fact_technology_rollout` | Q4 2025 (7) |
| `burger.sales.fact_value_score_country` | Q2 2026 (1); Q1 2026 (1); Q1 2026 (3); Q1 2026 (10); Q4 2025 (1); Q4 2025 (11); Q3 2025 (6) |
