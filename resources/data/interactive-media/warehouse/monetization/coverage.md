# Social Inc monetization and price

This slice owns ad prices, conversion, subscriptions, and cloud margin. Query counts and compute capacity are owned in the other slices and are partial when named here. A price fact does not store the click quantity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `country_identity` | `country_id` | `sf:social.geography.dim_country` `country_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:social.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `query_class_identity` | `query_class_id` | `sf:social.audience.dim_query_class` `query_class_id` |
| `surface_identity` | `surface_id` | `sf:social.audience.dim_surface` `surface_id` |

## Numbered questions

## Alphabet

### Q1 2026 (6)

Are AI tools shortening purchase journeys and lifting conversion, and how much of Search strength is that behavior versus newer advertiser AI tools at Alphabet?

- `social.audience.fact_journey`: `shortened_flag`, `journey_steps`
- `social.monetization.fact_conversion`: `conversion_rate`
- `social.monetization.fact_tool_contribution`: `contribution_share`
- `social.monetization.dim_ad_product`: `product_code`

### Q1 2026 (8)

How much of backlog growth is TPU sales versus cloud, and can the margins on very large generative-AI deals match the existing cloud business at Alphabet?

- `social.monetization.fact_backlog_composition`: `tpu_share`, `cloud_share`
- `social.monetization.fact_deal_economics`: `margin_rate`
- `social.monetization.fact_cloud_margin`: `matches_existing_flag`, `margin_rate`
- `social.monetization.dim_deal_class`: `class_code`

### Q4 2025 (1)

Where did agentic commerce advance most in 2025, and where should utility for users and advertisers move further in 2026 at Alphabet?

- `social.monetization.fact_commerce_roadmap`: `utility_advanced_flag`, `year_focus_code`
- `social.audience.dim_surface`: `surface_code`
- `social.monetization.dim_revenue_pool`: `pool_code`

### Q4 2025 (4)

Why did YouTube ad growth look softer if direct response was healthy and retail was strong in Search at Alphabet?

- `social.monetization.fact_youtube_ad`: `growth_rate`, `direct_response_healthy_flag`, `softer_flag`
- `social.monetization.fact_ad_revenue`: `revenue_amount`, `growth_rate`
- `social.monetization.dim_advertiser_vertical`: `vertical_code`
- `social.audience.dim_surface`: `surface_code`

### Q4 2025 (7)

As AI Search sessions get longer and more of the answer stays on the page, how does revenue keep up with that utility, including any role for subscriptions at Alphabet?

- `social.audience.fact_session_engagement`: `session_minutes`, `on_page_share`, `longer_flag`
- `social.monetization.fact_ad_revenue`: `revenue_amount`
- `social.monetization.fact_subscription_role`: `needed_for_revenue_flag`
- `social.monetization.dim_subscription_plan`: `plan_code`

### Q3 2025 (1)

What has to stay true so Search and advertisers are not worse off if agentic shopping and travel monetize below classic Search at Alphabet?

- `social.monetization.fact_agentic_yield`: `monetization_rate`, `below_classic_flag`, `advertiser_worse_flag`
- `social.audience.dim_surface`: `surface_code`
- `social.monetization.dim_revenue_pool`: `pool_code`

### Q3 2025 (3)

Inside AI Overviews and AI Mode, what is happening to clicks per query, conversion, and price even as query growth accelerates at Alphabet?

- `social.audience.fact_click_volume`: `click_quantity`, `clicks_per_query`
- `social.monetization.fact_conversion`: `conversion_rate`
- `social.monetization.fact_ad_price`: `price_index`, `cpc_amount`
- `social.audience.fact_query_volume`: `query_quantity`
- `social.audience.dim_surface`: `surface_code`

### Q3 2025 (6)

How do longer AI Mode queries change return on ad spend at Alphabet?

- `social.audience.fact_session_engagement`: `session_minutes`, `longer_flag`
- `social.monetization.fact_advertiser_roas`: `roas_rate`
- `social.audience.dim_surface`: `surface_code`

### Q3 2025 (7)

Can products such as AI Max lift the share of queries that are commercial above the historical level at Alphabet?

- `social.audience.fact_commercial_mix`: `commercial_share`, `above_historical_flag`
- `social.monetization.dim_ad_product`: `product_code`
- `social.audience.dim_query_class`: `class_code`

### Q3 2025 (8)

What supports the view that AI Overviews, AI Mode, and similar assistants expand marketing revenue, not only engagement at Alphabet?

- `social.monetization.fact_marketing_expansion`: `revenue_expands_flag`, `engagement_only_flag`
- `social.audience.fact_engagement_gain`: `gain_index`
- `social.audience.dim_surface`: `surface_code`

### Q3 2025 (10)

Have the large cloud deals signed over the prior nine months changed the long-term profit profile of cloud at Alphabet?

- `social.monetization.fact_deal_economics`: `margin_rate`, `changed_long_term_profile_flag`
- `social.monetization.fact_cloud_margin`: `margin_rate`
- `social.monetization.dim_deal_class`: `class_code`

### Q2 2025 (1)

As consumer behavior shifts, should investors track volume or monetization, given that click economics may not describe AI usage at Alphabet?

- `social.audience.fact_query_volume`: `query_quantity`
- `social.monetization.fact_search_bridge`: `volume_effect_amount`, `price_effect_amount`
- `social.monetization.dim_monetization_lens`: `lens_code`

### Q2 2025 (3)

Within Search growth, how much is paid-click volume versus pricing at Alphabet?

- `social.monetization.fact_search_bridge`: `volume_effect_amount`, `price_effect_amount`
- `social.audience.fact_click_volume`: `click_quantity`
- `social.monetization.fact_ad_price`: `cpc_amount`, `price_index`

### Q2 2025 (8)

Can click-through rates still rise as AI Overviews reduce ad impressions on a results page at Alphabet?

- `social.monetization.fact_click_through`: `ctr_rate`, `can_still_rise_flag`
- `social.monetization.fact_impression`: `impression_quantity`, `reduced_by_overview_flag`
- `social.audience.dim_surface`: `surface_code`

### Q2 2025 (9)

Does the ad environment for the second half look as firm as the prior year, or are there unusual category risks at Alphabet?

- `social.monetization.fact_advertiser_demand`: `demand_index`, `firm_versus_prior_flag`, `category_risk_flag`
- `social.monetization.dim_advertiser_vertical`: `vertical_code`

### Q2 2025 (11)

How are Gemini subscriptions inside Google One progressing, and what would speed consumer adoption?

- `social.monetization.fact_subscription`: `subscriber_quantity`, `attach_rate`, `adoption_speed_code`
- `social.monetization.dim_subscription_plan`: `plan_code`
- `social.audience.dim_surface`: `surface_code`

## Meta Platforms

### Q1 2026 (11)

What engagement and monetization unlocks come from moving ads from smaller models to Muse Spark and later large models at Meta Platforms?

- `social.infrastructure.fact_ranking_model`: `production_share`, `ad_benefit_captured_flag`
- `social.monetization.fact_ad_revenue`: `revenue_amount`, `growth_rate`
- `social.audience.fact_engagement_gain`: `gain_index`
- `social.infrastructure.dim_model_family`: `family_code`

### Q4 2025 (1)

Which revenue pools — personal intelligence or external compute — are the largest long-term payoffs for the investment, over three to ten years at Meta Platforms?

- `social.monetization.fact_non_ad_revenue`: `revenue_amount`, `realistic_flag`
- `social.monetization.dim_revenue_pool`: `pool_code`
- `social.infrastructure.fact_return_signal`: `on_path_flag`, `signal_code`

### Q4 2025 (3)

Has advertising growth yet captured the full first-order benefit of the model and capacity work at Meta Platforms?

- `social.infrastructure.fact_ranking_model`: `ad_benefit_captured_flag`, `production_share`
- `social.monetization.fact_ad_revenue`: `growth_rate`, `revenue_amount`

### Q4 2025 (6)

With so much capacity coming, what non-ad businesses — subscriptions, model licensing, or cloud-style access — become realistic at Meta Platforms?

- `social.monetization.fact_non_ad_revenue`: `revenue_amount`, `realistic_flag`
- `social.monetization.fact_licensing`: `revenue_amount`
- `social.monetization.fact_subscription`: `subscriber_quantity`
- `social.monetization.dim_revenue_pool`: `pool_code`

### Q4 2025 (7)

Is the advertising acceleration, excluding currency, a broader pickup in e-commerce activity at Meta Platforms?

- `social.monetization.fact_ad_revenue`: `ex_fx_growth_rate`, `growth_rate`, `acceleration_flag`
- `social.monetization.fact_ecommerce_ad`: `ecommerce_driven_flag`
- `social.monetization.dim_advertiser_vertical`: `vertical_code`

### Q3 2025 (4)

How large are next year’s ad and engagement gains expected to be versus the progress of the prior two years at Meta Platforms?

- `social.audience.fact_engagement_gain`: `gain_index`, `versus_two_year_pace`
- `social.monetization.fact_ad_revenue`: `growth_rate`, `acceleration_flag`
