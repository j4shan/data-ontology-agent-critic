# Starbucks demand warehouse

This slice covers demand, daypart, channel, menu, Rewards, and marketing for Starbucks.
The identity file registers the ten populations whose complete dataset is here.
Coffeehouse, country, calendar day, and fiscal period are foreign keys.
Every local realization of those identities uses `entity_universe: partial`.
Their complete dimensions belong to the slices that own those populations.
Ownership type remains `ownership_type_id` on `sf:starbucks.store.dim_ownership_type`.
This slice does not include that dimension.
`comp_driver_code` value `service` keys the service portion of the comp bridge.
The service population itself stays with the labor slice.
Marketing dollars, spend role, and non-Rewards attribution are in this slice.
Operating margin stays with the ledger slice.

A guest check, a menu line, and a comparable-sales component are three populations.
Observed daypart sales and the daypart-pressure attribution are two populations.
Delivery incrementality is its own population beside the raw check.

## Complete populations

| Identity | Complete dataset | Column |
| --- | --- | --- |
| `beverage_platform_identity` | `starbucks.menu.dim_beverage_platform` | `beverage_platform_id` |
| `menu_item_identity` | `starbucks.menu.dim_menu_item` | `menu_item_id` |
| `rewards_member_identity` | `starbucks.rewards.dim_rewards_member` | `rewards_member_id` |
| `age_cohort_identity` | `starbucks.customer.dim_age_cohort` | `age_cohort_id` |
| `daypart_identity` | `starbucks.demand.dim_daypart` | `daypart_id` |
| `order_channel_identity` | `starbucks.demand.dim_order_channel` | `order_channel_id` |
| `competitor_format_identity` | `starbucks.demand.dim_competitor_format` | `competitor_format_id` |
| `transaction_identity` | `starbucks.demand.fact_transaction` | `transaction_id` |
| `transaction_line_identity` | `starbucks.demand.fact_transaction_line` | `transaction_line_id` |
| `marketing_campaign_identity` | `starbucks.marketing.dim_marketing_campaign` | `marketing_campaign_id` |

## Foreign keys

These dimensions are not in this slice. Local columns reference them with `entity_universe: partial`.

| Identity | Node | Column |
| --- | --- | --- |
| `coffeehouse_identity` | `sf:starbucks.store.dim_coffeehouse` | `coffeehouse_id` |
| `country_identity` | `sf:starbucks.organization.dim_country` | `country_id` |
| `calendar_day_identity` | `sf:starbucks.calendar.dim_calendar_day` | `calendar_day_id` |
| `fiscal_period_identity` | `sf:starbucks.finance.dim_fiscal_period` | `fiscal_period_id` |

## Questions

### Q3 FY2026 (1)

How far along is the recovery in sales volume, and what would keep comparable-store growth above the long-term 3% pace?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.demand.fact_comparable_sales_daily` | `comparable_sales_rate`, `comparable_transaction_count`, `volume_recovery_ratio`, `long_term_comp_pace_rate`, `transaction_count`, `net_sales_amount`, `calendar_day_id`, `fiscal_period_id` | Daily comp result and how far volume recovery has moved versus the long-term pace. |
| `starbucks.demand.fact_transaction` | `transaction_count`, `net_sales_amount`, `ticket_amount`, `calendar_day_id` | Raw guest-check volume. Separate from the comp result. |
| `starbucks.demand.fact_comp_bridge_component` | `comp_driver_code`, `comparable_sales_contribution_amount`, `transaction_count`, `net_sales_amount` | Which components would hold comparable growth above the long-term pace. |
| `starbucks.demand.fact_value_price_outlook` | `assumed_comp_rate`, `long_term_comp_pace_rate`, `comp_cadence_code`, `fiscal_period_id` | The pace and cadence the forward plan assumes. |

### Q3 FY2026 (2)

How has morning versus afternoon growth changed, and when does the afternoon become the larger growth driver?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.demand.dim_daypart` | `daypart_code`, `daypart_id` | Morning and afternoon are rows. |
| `starbucks.demand.fact_daypart_channel_sales` | `daypart_id`, `calendar_day_id`, `transaction_count`, `net_sales_amount`, `transaction_growth_rate`, `net_sales_growth_rate` | Observed growth by daypart over the year. Compare the two daypart rows to see when afternoon is the larger driver. |
| `starbucks.demand.fact_daypart_pressure` | `daypart_id`, `pressure_driver_code`, `transaction_change_rate`, `transaction_count` | Attributed daypart change beside the observed sales. |

### Q3 FY2026 (3)

What distinguishes Starbucks refreshers, and does advertising by non-specialist restaurants create a halo?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.menu.dim_beverage_platform` | `platform_code`, `beverage_platform_id` | The refresher platform is a row. |
| `starbucks.menu.fact_platform_customer_feedback` | `beverage_platform_id`, `feedback_theme_code`, `fiscal_period_id` | Themes guests cite for the refresher platform. |
| `starbucks.menu.fact_platform_sales_mix` | `beverage_platform_id`, `net_sales_amount`, `unit_count`, `transaction_count` | Refresher sales next to the other platforms. |
| `starbucks.demand.dim_competitor_format` | `format_code`, `competitor_format_id` | non_specialist_advertiser is the advertising format under test. |
| `starbucks.marketing.dim_marketing_campaign` | `campaign_role_code`, `marketing_campaign_id` | A campaign with role non_specialist_halo is the halo test. |
| `starbucks.marketing.fact_campaign_demand_response` | `marketing_campaign_id`, `beverage_platform_id`, `attributed_transaction_count`, `net_sales_amount`, `transaction_count` | Refresher demand attributed to that campaign. |
| `starbucks.demand.fact_daypart_competitor_channel` | `competitor_format_id`, `beverage_platform_id`, `net_sales_amount`, `transaction_count` | Refresher demand in markets facing the non-specialist advertising format. |

### Q3 FY2026 (4)

Does that competitive dynamic change where Starbucks opens against other coffee specialists?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.demand.dim_competitor_format` | `format_code`, `competitor_format_id` | coffee_specialist is the format for those markets. |
| `starbucks.demand.fact_competitive_opening` | `coffeehouse_id`, `competitor_format_id`, `is_white_space_flag`, `country_id`, `calendar_day_id`, `net_sales_amount`, `transaction_count` | Openings and white-space locations against each competitive format. coffeehouse_id is a partial foreign key. |
| `starbucks.demand.fact_daypart_competitor_channel` | `competitor_format_id`, `daypart_id`, `order_channel_id`, `transaction_count`, `net_sales_amount` | Whether demand by daypart and channel differs in coffee-specialist markets. |

### Q3 FY2026 (7)

How much of third-quarter comparable sales came from longer hours, closures, and delivery versus brand initiatives?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.demand.fact_comp_bridge_component` | `comp_driver_code`, `comparable_sales_contribution_amount`, `transaction_count`, `net_sales_amount`, `ticket_amount`, `fiscal_period_id`, `marketing_campaign_id` | The comp bridge itself. Use hours_effect, closure_transfer, delivery, and brand_initiative. |

### Q3 FY2026 (11)

How did marketing spend change year over year, and is there room for advertising to rise as a percent of sales or only to mix differently?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.marketing.fact_marketing_spend` | `marketing_spend_amount`, `prior_year_marketing_spend_amount`, `net_sales_amount`, `spend_to_sales_ratio`, `media_channel_code`, `fiscal_period_id`, `spend_role_code` | Spend versus the prior year, spend as a percent of sales, and the media mix. |
| `starbucks.marketing.dim_marketing_campaign` | `marketing_campaign_id`, `campaign_role_code` | Which campaign the dollars belong to. |

### Q3 FY2026 (12)

What share of stores have digital menu boards, and how does the afternoon daypart perform in those stores?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.marketing.fact_digital_menu_board_daypart` | `coffeehouse_id`, `has_digital_menu_board`, `daypart_id`, `transaction_count`, `net_sales_amount`, `ticket_amount`, `unit_count`, `calendar_day_id` | Board flag on the demand test. Share of stores is distinct coffeehouse_id with the flag true. Afternoon performance is the afternoon daypart rows. |
| `starbucks.demand.dim_daypart` | `daypart_code`, `daypart_id` | Identifies the afternoon row. |

### Q3 FY2026 (14)

As delivery becomes a larger share of sales, how incremental is it versus lost in-store visits?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.demand.fact_delivery_incrementality` | `delivery_transaction_count`, `cafe_transaction_count`, `incremental_delivery_transaction_count`, `substituted_in_store_visit_count`, `delivery_net_sales_amount`, `cafe_net_sales_amount`, `transaction_count`, `net_sales_amount` | Incremental delivery checks versus cafe visits the delivery check replaced. |
| `starbucks.demand.dim_order_channel` | `channel_code`, `order_channel_id` | delivery and cafe are channel rows. The incrementality fact names those channels in its measures. |
| `starbucks.demand.fact_transaction` | `order_channel_id`, `transaction_count`, `net_sales_amount` | Raw checks by channel, before the incrementality split. |

### Q2 FY2026 (4)

How did comparable sales progress through the quarter?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.demand.fact_comparable_sales_daily` | `calendar_day_id`, `fiscal_period_id`, `comparable_sales_rate`, `comparable_transaction_count`, `transaction_count`, `net_sales_amount`, `ticket_amount` | Comp rate and volume by day inside the fiscal period. |

### Q2 FY2026 (5)

How did Rewards membership behave in April after the March program change?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.rewards.fact_rewards_membership_census` | `calendar_day_id`, `program_phase_code`, `active_member_count`, `enrolled_member_count`, `visit_frequency`, `transaction_count`, `net_sales_amount` | Daily member counts and visit frequency before and after the March change. April is the after phase. |
| `starbucks.rewards.fact_rewards_member_day` | `rewards_member_id`, `calendar_day_id`, `program_phase_code`, `transaction_count`, `net_sales_amount`, `ticket_amount` | Member-level activity around the change. |
| `starbucks.rewards.dim_rewards_member` | `rewards_member_id`, `member_status_code` | The member population the activity refers to. |

### Q1 FY2026 (5)

Why are non-Rewards customers growing faster than members?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.rewards.fact_rewards_participation_sales` | `rewards_participation_code`, `transaction_count`, `transaction_growth_rate`, `net_sales_amount`, `ticket_amount`, `daypart_id`, `order_channel_id`, `calendar_day_id` | Check and sales growth for non_rewards versus rewards_member, by daypart and channel. |
| `starbucks.demand.fact_transaction` | `rewards_participation_code`, `rewards_member_id`, `transaction_count`, `net_sales_amount`, `ticket_amount` | The check-level participation behind that aggregate. |
| `starbucks.marketing.fact_campaign_demand_response` | `rewards_participation_code`, `attributed_transaction_count`, `net_sales_amount`, `marketing_campaign_id` | How much of the non-Rewards growth is attributed to a campaign. |
| `starbucks.rewards.dim_rewards_member` | `rewards_member_id` | Members only. Non-Rewards guests are the non_rewards participation, not rows of this dimension. |

### Q1 FY2026 (6)

Should morning and afternoon be run differently given competitors that are almost entirely drive-thru and takeout?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.demand.dim_daypart` | `daypart_code`, `daypart_id` | Morning and afternoon rows. |
| `starbucks.demand.dim_order_channel` | `channel_code`, `order_channel_id` | Cafe, drive-thru, delivery, and mobile order rows. |
| `starbucks.demand.dim_competitor_format` | `format_code`, `competitor_format_id` | drive_thru_takeout is the competitor format. |
| `starbucks.demand.fact_daypart_channel_sales` | `daypart_id`, `order_channel_id`, `transaction_count`, `net_sales_amount`, `ticket_amount`, `unit_count` | Starbucks morning and afternoon demand by channel. |
| `starbucks.demand.fact_daypart_competitor_channel` | `daypart_id`, `order_channel_id`, `competitor_format_id`, `transaction_count`, `net_sales_amount`, `ticket_amount` | The same daypart and channel split in markets that include the drive-thru and takeout format. |

### Q1 FY2026 (7)

How much of the comparable sales was service versus innovation versus marketing?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.demand.fact_comp_bridge_component` | `comp_driver_code`, `comparable_sales_contribution_amount`, `transaction_count`, `net_sales_amount`, `marketing_campaign_id`, `beverage_platform_id` | Innovation and marketing are components this slice owns. service is keyed on comp_driver_code and the service population is not complete here. |
| `starbucks.marketing.dim_marketing_campaign` | `marketing_campaign_id`, `campaign_role_code` | The marketing and menu-innovation campaigns the bridge can point to. |
| `starbucks.marketing.fact_campaign_demand_response` | `marketing_campaign_id`, `attributed_transaction_count`, `net_sales_amount`, `beverage_platform_id` | Campaign-level demand behind the marketing and innovation portions. |

### Q1 FY2026 (10)

How much has the menu been cut since the turnaround started, and where are holes that need new items and marketing?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.menu.dim_menu_item` | `menu_item_id`, `item_name`, `item_status_code`, `menu_role_code` | The item population the cut is counted from. |
| `starbucks.menu.fact_menu_assortment_snapshot` | `menu_item_id`, `on_menu_flag`, `on_menu_at_turnaround_start_flag`, `removed_since_turnaround_flag`, `assortment_hole_flag`, `needs_new_item_flag`, `needs_marketing_flag`, `fiscal_period_id` | Items removed since the turnaround started, and items flagged as holes. |
| `starbucks.menu.fact_menu_hole` | `hole_code`, `removed_menu_item_id`, `beverage_platform_id`, `marketing_campaign_id`, `hole_reason_code`, `needs_new_item_flag`, `needs_marketing_flag` | Gaps that need a new item or a campaign, including gaps tied to a removed item. |
| `starbucks.menu.bridge_campaign_menu_item` | `marketing_campaign_id`, `menu_item_id`, `net_sales_amount`, `unit_count` | Items already attached to a campaign. |

### Q1 FY2026 (13)

How much can protein beverages contribute to comps, and what mix is protein today?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.menu.dim_beverage_platform` | `platform_code`, `beverage_platform_id` | The protein platform is a row. |
| `starbucks.menu.fact_platform_sales_mix` | `beverage_platform_id`, `mix_share_of_units`, `comparable_sales_contribution_amount`, `unit_count`, `net_sales_amount`, `transaction_count` | Current protein mix and the platform's comparable-sales contribution. |
| `starbucks.demand.fact_transaction_line` | `beverage_platform_id`, `unit_count`, `net_sales_amount`, `menu_item_id` | Protein units on the menu line. |
| `starbucks.demand.fact_channel_platform_comp` | `beverage_platform_id`, `comparable_sales_rate`, `net_sales_amount`, `transaction_count` | Protein comparable sales beside the other platforms. |

### Q1 FY2026 (14)

How much of the non-Rewards recovery is broad marketing, and how much of the North America margin decline is a permanent marketing rebase versus temporary turnaround spend?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.rewards.fact_rewards_participation_sales` | `rewards_participation_code`, `transaction_growth_rate`, `transaction_count`, `net_sales_amount` | The non-Rewards recovery in checks and sales. |
| `starbucks.marketing.fact_campaign_demand_response` | `rewards_participation_code`, `marketing_campaign_id`, `attributed_transaction_count`, `net_sales_amount` | Non-Rewards checks and sales attributed to a campaign. |
| `starbucks.marketing.dim_marketing_campaign` | `campaign_role_code`, `marketing_campaign_id` | broad_marketing identifies the broad campaigns. |
| `starbucks.marketing.fact_marketing_spend` | `spend_role_code`, `marketing_spend_amount`, `net_sales_amount`, `spend_to_sales_ratio`, `prior_year_marketing_spend_amount` | Temporary turnaround spend versus a permanent marketing rebase, in dollars and as a percent of sales. The margin decline itself is outside this slice. |

### Q4 FY2025 (1)

Are comparable sales different by cafe versus other order types, given a colder and more multi-channel business?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.demand.dim_order_channel` | `channel_code`, `order_channel_id`, `premise_code` | Cafe versus drive-thru, delivery, and mobile order. |
| `starbucks.menu.dim_beverage_platform` | `platform_code`, `temperature_class_code`, `beverage_platform_id` | Cold platforms versus hot platforms. |
| `starbucks.demand.fact_channel_platform_comp` | `order_channel_id`, `beverage_platform_id`, `comparable_sales_rate`, `transaction_count`, `net_sales_amount`, `ticket_amount`, `unit_count` | Comparable sales by channel and platform. |
| `starbucks.demand.fact_daypart_channel_sales` | `order_channel_id`, `transaction_count`, `net_sales_amount`, `ticket_amount` | Observed channel sales behind the comp. |
| `starbucks.demand.fact_transaction_line` | `beverage_platform_id`, `order_channel_id`, `unit_count`, `net_sales_amount` | Cold-platform units by channel on the menu line. |

### Q4 FY2025 (2)

How have customers received protein-platform pricing, and what price increases look sustainable?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.menu.dim_beverage_platform` | `platform_code`, `beverage_platform_id` | The protein platform row. |
| `starbucks.menu.fact_platform_price` | `beverage_platform_id`, `price_amount`, `price_change_amount`, `price_reception_code`, `sustainable_increase_flag`, `ticket_amount`, `net_sales_amount`, `unit_count`, `discount_amount` | Protein price, ticket, reception, and whether the increase is sustainable. |
| `starbucks.demand.fact_value_price_outlook` | `planned_price_change_amount`, `value_perception_score`, `fiscal_period_id` | The later pricing plan the protein result is read against. |

### Q4 FY2025 (5)

What is driving flatter morning transactions, and is afternoon weakness macro, competition, or a shift toward energy drinks?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.demand.dim_daypart` | `daypart_code`, `daypart_id` | Morning and afternoon rows. |
| `starbucks.demand.fact_daypart_channel_sales` | `daypart_id`, `transaction_count`, `transaction_growth_rate`, `net_sales_amount`, `calendar_day_id` | Observed morning and afternoon transactions. |
| `starbucks.demand.fact_daypart_pressure` | `daypart_id`, `pressure_driver_code`, `transaction_change_rate`, `competitor_format_id`, `beverage_platform_id`, `transaction_count` | Attribution to macro, competition, or energy_drink_shift. |
| `starbucks.menu.dim_beverage_platform` | `platform_code`, `beverage_platform_id` | The energy platform row. |
| `starbucks.menu.fact_platform_sales_mix` | `beverage_platform_id`, `unit_count`, `mix_share_of_units`, `transaction_count`, `net_sales_amount` | Energy-platform mix beside the afternoon question. |
| `starbucks.demand.dim_competitor_format` | `format_code`, `competitor_format_id` | energy_occasion and the other formats the pressure row can name. |

### Q4 FY2025 (8)

How do improved value perceptions shape 2026 pricing, and does that plan assume comps build through the year?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.demand.fact_value_price_outlook` | `value_perception_score`, `planned_price_change_amount`, `assumed_comp_rate`, `comp_cadence_code`, `long_term_comp_pace_rate`, `fiscal_period_id`, `ticket_amount`, `net_sales_amount` | Value perception, the planned price change, and whether the assumed comp builds through the year. |
| `starbucks.demand.fact_comparable_sales_daily` | `comparable_sales_rate`, `calendar_day_id`, `fiscal_period_id` | The intra-year comp path the cadence code is compared with. |
| `starbucks.menu.fact_platform_price` | `price_amount`, `price_change_amount`, `sustainable_increase_flag`, `ticket_amount` | Realized price increases already in the ticket. |

### Q4 FY2025 (9)

How has spending by guests under 35 changed?

| Qualified name | Columns | Role |
| --- | --- | --- |
| `starbucks.customer.dim_age_cohort` | `cohort_code`, `age_cohort_id` | under_35 is a cohort row. |
| `starbucks.customer.fact_age_cohort_spend` | `age_cohort_id`, `calendar_day_id`, `beverage_platform_id`, `transaction_count`, `net_sales_amount`, `ticket_amount`, `unit_count`, `discount_amount` | Spend, checks, ticket, and units for guests under 35, including coffee platforms. |

## Datasets and the questions they serve

| Qualified name | Questions |
| --- | --- |
| `starbucks.customer.dim_age_cohort` | Q4 FY2025 (9) |
| `starbucks.customer.fact_age_cohort_spend` | Q4 FY2025 (9) |
| `starbucks.demand.dim_competitor_format` | Q3 FY2026 (3), Q3 FY2026 (4), Q1 FY2026 (6), Q4 FY2025 (5) |
| `starbucks.demand.dim_daypart` | Q3 FY2026 (2), Q3 FY2026 (12), Q1 FY2026 (6), Q4 FY2025 (5) |
| `starbucks.demand.dim_order_channel` | Q3 FY2026 (14), Q1 FY2026 (6), Q4 FY2025 (1) |
| `starbucks.demand.fact_channel_platform_comp` | Q1 FY2026 (13), Q4 FY2025 (1) |
| `starbucks.demand.fact_comp_bridge_component` | Q3 FY2026 (1), Q3 FY2026 (7), Q1 FY2026 (7) |
| `starbucks.demand.fact_comparable_sales_daily` | Q3 FY2026 (1), Q2 FY2026 (4), Q4 FY2025 (8) |
| `starbucks.demand.fact_competitive_opening` | Q3 FY2026 (4) |
| `starbucks.demand.fact_daypart_channel_sales` | Q3 FY2026 (2), Q1 FY2026 (6), Q4 FY2025 (1), Q4 FY2025 (5) |
| `starbucks.demand.fact_daypart_competitor_channel` | Q3 FY2026 (3), Q3 FY2026 (4), Q1 FY2026 (6) |
| `starbucks.demand.fact_daypart_pressure` | Q3 FY2026 (2), Q4 FY2025 (5) |
| `starbucks.demand.fact_delivery_incrementality` | Q3 FY2026 (14) |
| `starbucks.demand.fact_transaction` | Q3 FY2026 (1), Q3 FY2026 (14), Q1 FY2026 (5) |
| `starbucks.demand.fact_transaction_line` | Q1 FY2026 (13), Q4 FY2025 (1) |
| `starbucks.demand.fact_value_price_outlook` | Q3 FY2026 (1), Q4 FY2025 (2), Q4 FY2025 (8) |
| `starbucks.marketing.dim_marketing_campaign` | Q3 FY2026 (3), Q3 FY2026 (11), Q1 FY2026 (7), Q1 FY2026 (14) |
| `starbucks.marketing.fact_campaign_demand_response` | Q3 FY2026 (3), Q1 FY2026 (5), Q1 FY2026 (7), Q1 FY2026 (14) |
| `starbucks.marketing.fact_digital_menu_board_daypart` | Q3 FY2026 (12) |
| `starbucks.marketing.fact_marketing_spend` | Q3 FY2026 (11), Q1 FY2026 (14) |
| `starbucks.menu.bridge_campaign_menu_item` | Q1 FY2026 (10) |
| `starbucks.menu.dim_beverage_platform` | Q3 FY2026 (3), Q1 FY2026 (13), Q4 FY2025 (1), Q4 FY2025 (2), Q4 FY2025 (5) |
| `starbucks.menu.dim_menu_item` | Q1 FY2026 (10) |
| `starbucks.menu.fact_menu_assortment_snapshot` | Q1 FY2026 (10) |
| `starbucks.menu.fact_menu_hole` | Q1 FY2026 (10) |
| `starbucks.menu.fact_platform_customer_feedback` | Q3 FY2026 (3) |
| `starbucks.menu.fact_platform_price` | Q4 FY2025 (2), Q4 FY2025 (8) |
| `starbucks.menu.fact_platform_sales_mix` | Q3 FY2026 (3), Q1 FY2026 (13), Q4 FY2025 (5) |
| `starbucks.rewards.dim_rewards_member` | Q2 FY2026 (5), Q1 FY2026 (5) |
| `starbucks.rewards.fact_rewards_member_day` | Q2 FY2026 (5) |
| `starbucks.rewards.fact_rewards_membership_census` | Q2 FY2026 (5) |
| `starbucks.rewards.fact_rewards_participation_sales` | Q1 FY2026 (5), Q1 FY2026 (14) |
