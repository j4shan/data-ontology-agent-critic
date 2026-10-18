# Social Inc audience and usage

This slice owns surfaces, audiences, and usage quantities. Ad prices, cloud revenue, and compute capacity are owned in the other slices and are partial when named here.

## Numbered questions

## Alphabet

### Q1 2026 (3)

What is pushing Search queries to a record, and how much room is left to cover more of those queries with ads at Alphabet?

- `social.audience.fact_query_volume`: `query_quantity`, `record_flag`
- `social.monetization.fact_ad_coverage`: `coverage_share`, `room_left_flag`
- `social.audience.dim_surface`: `surface_code`

### Q4 2025 (2)

How do generative creation tools fit YouTube’s longer-term content model at Alphabet?

- `social.audience.fact_content_supply`: `content_quantity`, `generative_fit_flag`
- `social.audience.dim_surface`: `surface_code`
- `social.audience.dim_content_type`: `content_code`

### Q4 2025 (6)

How are usage and retention trending for the native Gemini app, and is that monthly-active base the right cohort to compare with rival assistants at Alphabet?

- `social.audience.fact_user_base`: `user_quantity`, `monthly_active_quantity`
- `social.audience.fact_retention`: `retention_rate`
- `social.audience.fact_assistant_usage`: `usage_index`
- `social.audience.dim_surface`: `surface_code`

### Q2 2025 (5)

How important are new devices, including glasses, to scaling AI, and could the phone stop being the center of the consumer experience at Alphabet?

- `social.audience.fact_device_mix`: `usage_share`, `phone_still_center_flag`
- `social.infrastructure.fact_glasses_volume`: `unit_quantity`
- `social.audience.dim_device_form`: `form_code`

### Q2 2025 (6)

How does usage of Search with AI Mode differ from the standalone Gemini app, including which consumers use each at Alphabet?

- `social.audience.fact_surface_audience`: `distinct_audience_flag`
- `social.audience.fact_assistant_usage`: `usage_index`
- `social.audience.dim_surface`: `surface_code`
- `social.audience.dim_audience_segment`: `segment_code`

## Meta Platforms

### Q2 2026 (3)

Can mainstream consumer adoption close the gap between heavy AI-builder use and people who still treat AI like search at Meta Platforms?

- `social.audience.fact_assistant_usage`: `usage_index`, `search_like_share`, `power_user_share`, `mainstream_gap_flag`
- `social.audience.dim_surface`: `surface_code`

### Q1 2026 (8)

How do new consumer AI apps change the direction of Meta AI, Dreamer, and the broader agent strategy?

- `social.infrastructure.fact_dreamer_direction`: `direction_code`
- `social.audience.fact_assistant_usage`: `usage_index`
- `social.infrastructure.dim_product_bet`: `bet_code`
- `social.infrastructure.dim_agent_kind`: `kind_code`

### Q1 2026 (10)

What changes in ranking when the interaction history those models can use gets much longer at Meta Platforms?

- `social.audience.fact_interaction_depth`: `history_length`, `ranking_change_flag`
- `social.infrastructure.fact_ranking_model`: `larger_model_flag`
- `social.audience.dim_surface`: `surface_code`

### Q4 2025 (8)

What is the plan for bringing Horizon Worlds to mobile, and what do AI and Horizon open in gaming or new communication at Meta Platforms?

- `social.audience.fact_horizon_roadmap`: `mobile_plan_flag`, `gaming_open_flag`
- `social.audience.dim_surface`: `surface_code`
- `social.audience.dim_content_type`: `content_code`

### Q4 2025 (11)

Is Meta AI usage at the point where product improvements are starting to show up in engagement?

- `social.audience.fact_assistant_usage`: `usage_index`
- `social.audience.fact_engagement_gain`: `gain_index`
- `social.infrastructure.fact_monetization_path`: `usage_to_money_stage`
- `social.audience.dim_surface`: `surface_code`

### Q3 2025 (3)

What do today’s Meta AI interactions imply for how superintelligence-class models would change utility and behavior?

- `social.infrastructure.fact_superintelligence_utility`: `utility_change_code`
- `social.audience.fact_assistant_usage`: `usage_index`
- `social.audience.dim_surface`: `surface_code`

### Q3 2025 (8)

What Meta AI adoption is most encouraging, and how far along is the path from usage to monetization?

- `social.infrastructure.fact_monetization_path`: `usage_to_money_stage`, `encouraging_flag`
- `social.audience.fact_assistant_usage`: `usage_index`
- `social.audience.dim_surface`: `surface_code`
