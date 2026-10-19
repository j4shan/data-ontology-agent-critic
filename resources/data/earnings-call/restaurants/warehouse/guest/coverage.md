# Burger Inc guest demand

Guest demand, menu, offers, loyalty and comparable sales for both restaurant companies.

Every fact below uses `fiscal_period_id` for the fiscal period and `scenario_id` for the scenario (`reported` or `guide` in `dim_scenario`). Measure descriptions in the YAML name the unit.

## McDonald's (MCD)

### Q2 2026 (1)

If U.S. value leadership is already restored, what are the near-term sales opportunities versus the slower work on chicken quality and the value menu?

- `burger.guest.fact_offer_redemption_quantity`: `redeemed_transaction_count`, `participating_restaurant_count`, `eligible_restaurant_count`, `offer_id`
- `burger.guest.fact_offer_sales_amount`: `offer_sales_amount`, `discount_amount`
- `burger.guest.dim_offer`: `offer_structure_code`

### Q2 2026 (2)

How quickly can U.S. operations and marketing problems be fixed, and what does that imply for U.S. sales over the next few quarters?

- `burger.guest.fact_marketing_amount`: `media_spend_amount`, `attributed_sales_amount`, `marketing_campaign_id`
- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`

### Q2 2026 (3)

Why was franchisee participation lower in the value program, and was that disagreement on the traffic driver or cost pressure?

- `burger.guest.fact_offer_redemption_quantity`: `redeemed_transaction_count`, `participating_restaurant_count`, `eligible_restaurant_count`, `offer_id`
- `burger.guest.fact_offer_sales_amount`: `offer_sales_amount`, `discount_amount`
- `burger.guest.dim_offer`: `offer_structure_code`

### Q2 2026 (6)

Has the way marketing is developed changed, or will it return to the prior process for anticipating demand?

- `burger.guest.fact_marketing_amount`: `media_spend_amount`, `attributed_sales_amount`, `marketing_campaign_id`
- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`

### Q2 2026 (9)

Is the new beverage lineup raising attachment, and how large a share of those sales are energy drinks?

- `burger.menu.fact_beverage_quantity`: `beverage_unit_count`, `attached_transaction_count`, `beverage_type_id`
- `burger.menu.dim_beverage_type`: `beverage_type_code`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`

### Q1 2026 (1)

How should U.S. sales trend through the rest of 2026 given value, marketing, and menu innovation against a weak consumer?

- `burger.guest.fact_marketing_amount`: `media_spend_amount`, `attributed_sales_amount`, `marketing_campaign_id`
- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`

### Q1 2026 (2)

Why does the value offer need another iteration, and how often should it change?

- `burger.guest.fact_offer_redemption_quantity`: `redeemed_transaction_count`, `participating_restaurant_count`, `eligible_restaurant_count`, `offer_id`
- `burger.guest.fact_offer_sales_amount`: `offer_sales_amount`, `discount_amount`
- `burger.guest.dim_offer`: `offer_structure_code`

### Q1 2026 (3)

Why have some markets, including France, been less successful on value than others that already had offers in place?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

### Q1 2026 (8)

How are higher-income and lower-income guest trends diverging?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

### Q1 2026 (9)

Did past World Cup sponsorships lift digital adoption more than overall demand, and can loyalty now turn the event into higher visit frequency?

- `burger.guest.fact_loyalty_activity_quantity`: `active_member_count`, `enrolled_member_count`, `visit_count`, `loyalty_program_id`
- `burger.guest.fact_loyalty_sales_amount`: `member_sales_amount`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`

### Q1 2026 (10)

Which parts of the U.K. turnaround can transfer to the U.S. and France?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

### Q1 2026 (12)

Why was an energy brand left out of the initial U.S. beverage launch?

- `burger.menu.fact_beverage_quantity`: `beverage_unit_count`, `attached_transaction_count`, `beverage_type_id`
- `burger.menu.dim_beverage_type`: `beverage_type_code`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`

### Q1 2026 (14)

After the April comparison, should the rest of the second quarter return to the prior run rate?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

### Q1 2026 (15)

Has the rise in gas prices already stepped down demand, especially among lower-income guests?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

### Q4 2025 (1)

What U.S. sales pace is expected in 2026 if value, marketing, and innovation all work together?

- `burger.guest.fact_marketing_amount`: `media_spend_amount`, `attributed_sales_amount`, `marketing_campaign_id`
- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`

### Q4 2025 (2)

Within the value architecture, did the standardized meal discount or the sharp price points do more for sales, and did either pressure restaurant margins?

- `burger.guest.fact_offer_redemption_quantity`: `redeemed_transaction_count`, `participating_restaurant_count`, `eligible_restaurant_count`, `offer_id`
- `burger.guest.fact_offer_sales_amount`: `offer_sales_amount`, `discount_amount`
- `burger.guest.dim_offer`: `offer_structure_code`

### Q4 2025 (6)

Will U.S. franchisees keep the value strategy once company financial support ends?

- `burger.guest.fact_offer_redemption_quantity`: `redeemed_transaction_count`, `participating_restaurant_count`, `eligible_restaurant_count`, `offer_id`
- `burger.guest.fact_offer_sales_amount`: `offer_sales_amount`, `discount_amount`
- `burger.guest.dim_offer`: `offer_structure_code`

### Q4 2025 (7)

How much does higher loyalty frequency move the system, and what still blocks finishing the global technology stack?

- `burger.guest.fact_loyalty_activity_quantity`: `active_member_count`, `enrolled_member_count`, `visit_count`, `loyalty_program_id`
- `burger.guest.fact_loyalty_sales_amount`: `member_sales_amount`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`

### Q4 2025 (8)

How will the U.S. beverage rollout proceed this year now that the earlier beverage concept is less central?

- `burger.menu.fact_beverage_quantity`: `beverage_unit_count`, `attached_transaction_count`, `beverage_type_id`
- `burger.menu.dim_beverage_type`: `beverage_type_code`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`

### Q4 2025 (9)

How should first-quarter sales be read through weather and the remaining food-safety comparison?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

### Q4 2025 (10)

How is the U.S. menu being adjusted for guests using GLP-1 medicines, including oral versions?

- `burger.menu.fact_product_quantity`: `sold_quantity`, `product_id`, `country_id`
- `burger.menu.fact_product_price`: `unit_price_amount`, `product_id`
- `burger.menu.dim_product`: `product_name`, `menu_category_id`, `protein_type_id`, `beverage_type_id`

### Q4 2025 (11)

Where do value scores and value mix sit in the U.S., and what premium items can balance that barbell in 2026?

- `burger.guest.fact_offer_redemption_quantity`: `redeemed_transaction_count`, `participating_restaurant_count`, `eligible_restaurant_count`, `offer_id`
- `burger.guest.fact_offer_sales_amount`: `offer_sales_amount`, `discount_amount`
- `burger.guest.dim_offer`: `offer_structure_code`

### Q3 2025 (1)

How can U.S. restaurant margins improve at the same time the value gap versus competitors widens?

- `burger.guest.fact_offer_redemption_quantity`: `redeemed_transaction_count`, `participating_restaurant_count`, `eligible_restaurant_count`, `offer_id`
- `burger.guest.fact_offer_sales_amount`: `offer_sales_amount`, `discount_amount`
- `burger.guest.dim_offer`: `offer_structure_code`

### Q3 2025 (2)

How large is the company co-investment in the U.S. value strategy, and what traffic or value-score result lets franchisees continue it without that support?

- `burger.guest.fact_offer_redemption_quantity`: `redeemed_transaction_count`, `participating_restaurant_count`, `eligible_restaurant_count`, `offer_id`
- `burger.guest.fact_offer_sales_amount`: `offer_sales_amount`, `discount_amount`
- `burger.guest.dim_offer`: `offer_structure_code`

### Q3 2025 (3)

Is the underlying U.S. guest-count baseline improving into 2026, or only the promoted sales?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

### Q3 2025 (4)

Across the two beverage tests, what does the sales mix look like with and without the energy drink?

- `burger.menu.fact_beverage_quantity`: `beverage_unit_count`, `attached_transaction_count`, `beverage_type_id`
- `burger.menu.dim_beverage_type`: `beverage_type_code`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`

### Q3 2025 (6)

Does a wider everyday-value-meal discount give U.S. customers the same price certainty Australia uses, enough to support more national pricing?

- `burger.guest.fact_offer_redemption_quantity`: `redeemed_transaction_count`, `participating_restaurant_count`, `eligible_restaurant_count`, `offer_id`
- `burger.guest.fact_offer_sales_amount`: `offer_sales_amount`, `discount_amount`
- `burger.guest.dim_offer`: `offer_structure_code`

### Q3 2025 (7)

Is the value push taking share across income groups, and are digital and product moves working at the higher end?

- `burger.guest.fact_offer_redemption_quantity`: `redeemed_transaction_count`, `participating_restaurant_count`, `eligible_restaurant_count`, `offer_id`
- `burger.guest.fact_offer_sales_amount`: `offer_sales_amount`, `discount_amount`
- `burger.guest.dim_offer`: `offer_structure_code`

### Q3 2025 (8)

Is higher-income traffic shifting from fast casual into quick service, and has the everyday value meal helped the weaker breakfast daypart?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

### Q3 2025 (9)

Can McDonald's now gain at both ends, keeping lower-income guests with value and picking up middle- and upper-income trade-down?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

## Starbucks (SBUX)

### Q3 FY2026 (1)

How far along is the recovery in sales volume, and what would keep comparable-store growth above the long-term 3% pace for the next few years?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

### Q3 FY2026 (2)

How has morning versus afternoon growth changed over the past year, and when does the afternoon become the larger growth driver?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

### Q3 FY2026 (3)

What do customers say distinguishes Starbucks refreshers from other chains, and does advertising by non-specialist restaurants create a halo?

- `burger.menu.fact_beverage_quantity`: `beverage_unit_count`, `attached_transaction_count`, `beverage_type_id`
- `burger.menu.dim_beverage_type`: `beverage_type_code`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`

### Q3 FY2026 (10)

Will some stores run 24 hours, and what could extended hours add to the U.S. system once fully rolled out?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

### Q3 FY2026 (12)

What share of stores have digital menu boards, and how does the afternoon daypart perform in those stores?

- `burger.menu.fact_product_quantity`: `sold_quantity`, `product_id`, `country_id`
- `burger.menu.fact_product_price`: `unit_price_amount`, `product_id`
- `burger.menu.dim_product`: `product_name`, `menu_category_id`, `protein_type_id`, `beverage_type_id`

### Q3 FY2026 (14)

As delivery becomes a larger share of sales, how incremental is it versus lost in-store visits?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

### Q2 FY2026 (2)

How much comparable-sales runway is left from operations improvements alone?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

### Q2 FY2026 (4)

How did comparable sales progress through the quarter?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

### Q2 FY2026 (5)

How did Rewards membership behave in April after the March program change, and was that disruption or acceleration?

- `burger.guest.fact_loyalty_activity_quantity`: `active_member_count`, `enrolled_member_count`, `visit_count`, `loyalty_program_id`
- `burger.guest.fact_loyalty_sales_amount`: `member_sales_amount`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`

### Q1 FY2026 (4)

What scenarios put fiscal 2026 earnings at the high end versus the low end of the wide range?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

### Q1 FY2026 (5)

Why are non-Rewards customers growing faster than members, and what narrows that gap now that members are positive again?

- `burger.guest.fact_loyalty_activity_quantity`: `active_member_count`, `enrolled_member_count`, `visit_count`, `loyalty_program_id`
- `burger.guest.fact_loyalty_sales_amount`: `member_sales_amount`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`

### Q1 FY2026 (7)

How much of the comparable sales was service versus innovation versus marketing?

- `burger.guest.fact_marketing_amount`: `media_spend_amount`, `attributed_sales_amount`, `marketing_campaign_id`
- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`

### Q1 FY2026 (8)

Does guidance leave room for more investment this year on top of annualizing the labor model?

- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `comparable_transaction_rate`, `country_id`, `operating_model_id`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`, `restaurant_id`

### Q1 FY2026 (10)

How much has the menu been cut since the turnaround started, and where are holes that need new items and marketing?

- `burger.guest.fact_marketing_amount`: `media_spend_amount`, `attributed_sales_amount`, `marketing_campaign_id`
- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`

### Q1 FY2026 (13)

How much can health-and-wellness items, including protein beverages, contribute to comps, and what mix is protein today?

- `burger.menu.fact_beverage_quantity`: `beverage_unit_count`, `attached_transaction_count`, `beverage_type_id`
- `burger.menu.dim_beverage_type`: `beverage_type_code`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`

### Q1 FY2026 (14)

How much of the non-Rewards recovery is broad marketing, and how much of the North America margin decline is a permanent marketing rebase versus temporary turnaround spend?

- `burger.guest.fact_loyalty_activity_quantity`: `active_member_count`, `enrolled_member_count`, `visit_count`, `loyalty_program_id`
- `burger.guest.fact_loyalty_sales_amount`: `member_sales_amount`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`

### Q4 FY2025 (1)

Are comparable sales different by cafe versus other order types, given the business is now more cold beverage and more channels than the old in-cafe model?

- `burger.menu.fact_beverage_quantity`: `beverage_unit_count`, `attached_transaction_count`, `beverage_type_id`
- `burger.menu.dim_beverage_type`: `beverage_type_code`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`

### Q4 FY2025 (5)

What is driving flatter morning transactions that beat the rest of the business, and is afternoon weakness macro, competition, or a shift toward energy drinks?

- `burger.menu.fact_beverage_quantity`: `beverage_unit_count`, `attached_transaction_count`, `beverage_type_id`
- `burger.menu.dim_beverage_type`: `beverage_type_code`
- `burger.sales.fact_transaction_quantity`: `transaction_count`, `guest_count`

### Q4 FY2025 (9)

How has spending by guests under 35 changed, and is that a near-term headwind for coffee?

- `burger.menu.fact_product_quantity`: `sold_quantity`, `product_id`, `country_id`
- `burger.menu.fact_product_price`: `unit_price_amount`, `product_id`
- `burger.menu.dim_product`: `product_name`, `menu_category_id`, `protein_type_id`, `beverage_type_id`
