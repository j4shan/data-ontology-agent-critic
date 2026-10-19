# Social Inc monetization, segments, and Reality Labs

Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks. Demand quantity, supply or capacity, and price or margin are stored on separate facts joined by the shared grain keys (fiscal quarter, scenario, and the business keys).

## Numbered questions

## Alphabet

### Q1 2026 (1) Alphabet

With compute still tight, which parts of Search should get next-generation capacity over the next 12 months if the goal is a return on that spend?

- `social.search.fact_search_query_volume`: `fiscal_quarter_id`, `scenario_id`, `query_intent_id`, `presentation_feature_id`, `consumer_surface_id`, `query_count`
- `social.search.fact_search_clicks`: `fiscal_quarter_id`, `scenario_id`, `query_intent_id`, `presentation_feature_id`, `paid_click_count`, `total_click_count`
- `social.search.fact_search_cpc`: `fiscal_quarter_id`, `scenario_id`, `query_intent_id`, `advertiser_size_id`, `cost_per_click_amount`

### Q1 2026 (3) Alphabet

What is pushing Search queries to a record, and how much room is left to cover more of those queries with ads?

- `social.search.fact_search_query_volume`: `fiscal_quarter_id`, `scenario_id`, `query_intent_id`, `presentation_feature_id`, `consumer_surface_id`, `query_count`
- `social.search.fact_search_clicks`: `fiscal_quarter_id`, `scenario_id`, `query_intent_id`, `presentation_feature_id`, `paid_click_count`, `total_click_count`
- `social.search.fact_search_cpc`: `fiscal_quarter_id`, `scenario_id`, `query_intent_id`, `advertiser_size_id`, `cost_per_click_amount`

### Q1 2026 (4) Alphabet

How does Alphabet’s infrastructure approach compare with peers on both compute supply and margin?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q4 2025 (2) Alphabet

How do generative creation tools fit YouTube’s longer-term content model?

- `social.ads.fact_video_watch`: `fiscal_quarter_id`, `scenario_id`, `video_format_id`, `consumer_surface_id`, `view_count`, `watch_minutes_count`
- `social.ads.fact_ad_price`: `fiscal_quarter_id`, `scenario_id`, `consumer_surface_id`, `ad_format_id`, `average_price_per_ad_amount`, `cpm_amount`
- `social.audience.fact_surface_audience`: `fiscal_quarter_id`, `scenario_id`, `consumer_surface_id`, `surface_daily_user_count`, `surface_monthly_user_count`

### Q4 2025 (4) Alphabet

Why did YouTube ad growth look softer if direct response was healthy and retail was strong in Search?

- `social.ads.fact_video_watch`: `fiscal_quarter_id`, `scenario_id`, `video_format_id`, `consumer_surface_id`, `view_count`, `watch_minutes_count`
- `social.ads.fact_ad_price`: `fiscal_quarter_id`, `scenario_id`, `consumer_surface_id`, `ad_format_id`, `average_price_per_ad_amount`, `cpm_amount`
- `social.audience.fact_surface_audience`: `fiscal_quarter_id`, `scenario_id`, `consumer_surface_id`, `surface_daily_user_count`, `surface_monthly_user_count`

### Q4 2025 (5) Alphabet

Is there an operating-income or free-cash-flow hurdle that decides which investment projects get resources, or is core performance the binding constraint?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q3 2025 (1) Alphabet

What has to stay true so Search and advertisers are not worse off if agentic shopping and travel monetize below classic Search?

- `social.search.fact_search_query_volume`: `fiscal_quarter_id`, `scenario_id`, `query_intent_id`, `presentation_feature_id`, `consumer_surface_id`, `query_count`
- `social.search.fact_search_clicks`: `fiscal_quarter_id`, `scenario_id`, `query_intent_id`, `presentation_feature_id`, `paid_click_count`, `total_click_count`
- `social.search.fact_search_cpc`: `fiscal_quarter_id`, `scenario_id`, `query_intent_id`, `advertiser_size_id`, `cost_per_click_amount`

### Q3 2025 (4) Alphabet

Where can core costs be reduced to absorb faster infrastructure growth?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q3 2025 (5) Alphabet

With each generation of custom silicon, how much of the gain is internal efficiency versus revenue from selling that capability outside?

- `social.segment.fact_segment_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `segment_revenue_amount`
- `social.segment.fact_segment_operating_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `segment_operating_income_amount`

### Q2 2025 (3) Alphabet

Within Search growth, how much is paid-click volume versus pricing?

- `social.search.fact_search_query_volume`: `fiscal_quarter_id`, `scenario_id`, `query_intent_id`, `presentation_feature_id`, `consumer_surface_id`, `query_count`
- `social.search.fact_search_clicks`: `fiscal_quarter_id`, `scenario_id`, `query_intent_id`, `presentation_feature_id`, `paid_click_count`, `total_click_count`
- `social.search.fact_search_cpc`: `fiscal_quarter_id`, `scenario_id`, `query_intent_id`, `advertiser_size_id`, `cost_per_click_amount`

### Q2 2025 (4) Alphabet

What technical hurdles still block scalable agents on commercial queries?

- `social.search.fact_search_query_volume`: `fiscal_quarter_id`, `scenario_id`, `query_intent_id`, `presentation_feature_id`, `consumer_surface_id`, `query_count`
- `social.search.fact_search_clicks`: `fiscal_quarter_id`, `scenario_id`, `query_intent_id`, `presentation_feature_id`, `paid_click_count`, `total_click_count`
- `social.search.fact_search_cpc`: `fiscal_quarter_id`, `scenario_id`, `query_intent_id`, `advertiser_size_id`, `cost_per_click_amount`

### Q2 2025 (9) Alphabet

Does the ad environment for the second half look as firm as the prior year, or are there unusual category risks?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

## Meta

### Q2 2026 (1) Meta

Among consumer agents, business agents, API tools, and compute rental, which can reach material scale in 2026 and 2027 given today’s products and compute?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q2 2026 (2) Meta

How much of the enterprise opportunity can be sold through the existing advertising and marketing motion, versus a go-to-market system that still has to be built?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`
- `social.ads.fact_ad_impressions`: `fiscal_quarter_id`, `scenario_id`, `consumer_surface_id`, `ad_format_id`, `region_id`, `impression_count`
- `social.ads.fact_ad_price`: `fiscal_quarter_id`, `scenario_id`, `consumer_surface_id`, `ad_format_id`, `average_price_per_ad_amount`, `cpm_amount`

### Q2 2026 (4) Meta

How far along is the shift to larger models and more compute for ranking and recommendations?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q2 2026 (5) Meta

Why sell compute to others while also buying capacity from third parties?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q2 2026 (7) Meta

What advantages is the lab building that should last beyond a single model generation?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q2 2026 (8) Meta

Why compete at both the cheaper end of the model range and the high-performance end?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q2 2026 (9) Meta

If open-weight models spread, does Meta still need to build its own closed frontier models?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q1 2026 (2) Meta

How is lab effort split between further training toward personal superintelligence and shipping products?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q1 2026 (4) Meta

How do the media and commerce parts of the business become more agentic for consumers, alongside offering compute to enterprises?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q1 2026 (7) Meta

What does Muse Spark unlock for products still in development, and what is the consumer versus enterprise release pace over the next nine months?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q1 2026 (9) Meta

Is a personal agent a near-term product or a longer-term goal now that Muse Spark is live?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q1 2026 (10) Meta

What changes in ranking when the interaction history those models can use gets much longer?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q1 2026 (12) Meta

What role does Manus play in agentic products, and where does that effort stand?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q4 2025 (1) Meta

Which revenue pools — personal intelligence or external compute — are the largest long-term payoffs for the investment, over three to ten years?

- `social.segment.fact_segment_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `segment_revenue_amount`
- `social.segment.fact_segment_operating_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `segment_operating_income_amount`

### Q4 2025 (3) Meta

Has advertising growth yet captured the full first-order benefit of the model and capacity work?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`
- `social.ads.fact_ad_impressions`: `fiscal_quarter_id`, `scenario_id`, `consumer_surface_id`, `ad_format_id`, `region_id`, `impression_count`
- `social.ads.fact_ad_price`: `fiscal_quarter_id`, `scenario_id`, `consumer_surface_id`, `ad_format_id`, `average_price_per_ad_amount`, `cpm_amount`

### Q4 2025 (4) Meta

How far is the new model team toward a frontier model this year?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q4 2025 (7) Meta

Is the advertising acceleration, excluding currency, a broader pickup in e-commerce activity?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`
- `social.ads.fact_ad_impressions`: `fiscal_quarter_id`, `scenario_id`, `consumer_surface_id`, `ad_format_id`, `region_id`, `impression_count`
- `social.ads.fact_ad_price`: `fiscal_quarter_id`, `scenario_id`, `consumer_surface_id`, `ad_format_id`, `average_price_per_ad_amount`, `cpm_amount`

### Q4 2025 (8) Meta

What is the plan for bringing Horizon Worlds to mobile, and what do AI and Horizon open in gaming or new communication?

- `social.reality.fact_reality_labs_result`: `fiscal_quarter_id`, `scenario_id`, `device_id`, `reality_labs_revenue_amount`, `reality_labs_operating_loss_amount`
- `social.reality.fact_headset_units`: `fiscal_quarter_id`, `scenario_id`, `device_id`, `headset_unit_count`
- `social.reality.fact_headset_price`: `fiscal_quarter_id`, `scenario_id`, `device_id`, `average_headset_price_amount`

### Q4 2025 (10) Meta

Does Meta need a leading general-purpose model, or is a model that is excellent at specific tasks enough?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q3 2025 (1) Meta

Which early tests of 2026 ranking and ad models already support a return on the infrastructure build?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q3 2025 (5) Meta

Are the newer lab efforts timed to an updated frontier model next year?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`

### Q3 2025 (10) Meta

Once a leading frontier model exists, does the value sit with the platform or with scaled first-party apps?

- `social.ads.fact_ad_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `consumer_surface_id`, `ad_format_id`, `ad_revenue_amount`
