# Social Inc compute, models, and capacity

This slice owns compute supply, capital spending, models, and glasses units. Ad prices and query counts are owned in the other slices and are partial when named here. Capacity does not store a supply price.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `deal_class_identity` | `deal_class_id` | `sf:social.monetization.dim_deal_class` `deal_class_id` |
| `device_form_identity` | `device_form_id` | `sf:social.audience.dim_device_form` `device_form_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:social.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `revenue_pool_identity` | `revenue_pool_id` | `sf:social.monetization.dim_revenue_pool` `revenue_pool_id` |
| `surface_identity` | `surface_id` | `sf:social.audience.dim_surface` `surface_id` |

## Numbered questions

## Alphabet

### Q1 2026 (1)

With compute still tight, which parts of Search should get next-generation capacity over the next 12 months if the goal is a return on that spend at Alphabet?

- `social.infrastructure.fact_compute_allocation`: `allocation_share`, `screen_code`
- `social.infrastructure.fact_compute_capacity`: `capacity_units`, `tight_flag`
- `social.infrastructure.fact_return_signal`: `on_path_flag`, `signal_code`
- `social.audience.dim_surface`: `surface_code`

### Q1 2026 (2)

How does the capital-spending path, including a large 2027 increase, line up with serving the cloud backlog already booked at Alphabet?

- `social.infrastructure.fact_capex_plan`: `spend_amount`, `step_up_flag`, `year_2027_increase_flag`
- `social.infrastructure.fact_cloud_backlog`: `backlog_amount`, `growth_amount`

### Q1 2026 (4)

How does Alphabet’s infrastructure approach compare with peers on both compute supply and margin?

- `social.infrastructure.fact_infra_peer`: `supply_position_code`, `margin_position_code`
- `social.infrastructure.fact_compute_capacity`: `capacity_units`
- `social.monetization.fact_cloud_margin`: `margin_rate`, `peer_position_code`

### Q1 2026 (5)

When capacity is constrained, what screens decide which internal projects get incremental compute versus external cloud customers at Alphabet?

- `social.infrastructure.fact_compute_allocation`: `allocation_share`, `screen_code`
- `social.infrastructure.dim_capacity_source`: `source_code`
- `social.audience.dim_surface`: `surface_code`

### Q1 2026 (7)

Is supply-chain price inflation included in the 2026 and 2027 capital-spending commentary, and how is compute split between internal use and external cloud at Alphabet?

- `social.infrastructure.fact_supply_price`: `inflation_rate`, `included_in_capex_flag`
- `social.infrastructure.fact_capex_plan`: `includes_inflation_flag`, `spend_amount`
- `social.infrastructure.fact_capex_split`: `internal_share`, `external_share`

### Q4 2025 (3)

With 2026 capital spending stepping up, what is the path to closing the internal and external compute gaps, and what operating results should follow as those gaps close at Alphabet?

- `social.infrastructure.fact_capex_plan`: `spend_amount`, `step_up_flag`
- `social.infrastructure.fact_capacity_gap`: `gap_units`, `closing_flag`, `internal_or_external_code`
- `social.infrastructure.fact_operating_result`: `result_code`, `follows_gap_close_flag`

### Q4 2025 (5)

Is there an operating-income or free-cash-flow hurdle that decides which investment projects get resources, or is core performance the binding constraint at Alphabet?

- `social.infrastructure.fact_investment_screen`: `oi_hurdle_flag`, `fcf_hurdle_flag`, `core_performance_binding_flag`
- `social.infrastructure.fact_free_cash_flow`: `fcf_amount`, `hurdle_binding_flag`

### Q3 2025 (2)

How close is a deeper tie between Waymo and core Gemini capabilities at Alphabet?

- `social.infrastructure.fact_waymo_link`: `tie_depth_code`
- `social.infrastructure.dim_product_bet`: `bet_code`
- `social.infrastructure.dim_model_family`: `family_code`

### Q3 2025 (4)

Where can core costs be reduced to absorb faster infrastructure growth at Alphabet?

- `social.infrastructure.fact_core_opex`: `cost_amount`, `reducible_flag`
- `social.infrastructure.fact_capex_plan`: `spend_amount`, `step_up_flag`
- `social.infrastructure.dim_cost_bucket`: `bucket_code`

### Q3 2025 (5)

With each generation of custom silicon, how much of the gain is internal efficiency versus revenue from selling that capability outside at Alphabet?

- `social.infrastructure.fact_silicon_economics`: `efficiency_gain_share`, `external_revenue_share`
- `social.infrastructure.dim_silicon_generation`: `generation_code`

### Q3 2025 (9)

Is frontier-model innovation still rapid ahead of the next Gemini generation, or is the pace slowing at Alphabet?

- `social.infrastructure.fact_model_release`: `cadence_code`, `slowing_flag`
- `social.infrastructure.dim_model_family`: `family_code`
- `social.infrastructure.dim_lab_program`: `program_code`

### Q2 2025 (2)

Why is compute still tight even with a large step-up in capital spending at Alphabet?

- `social.infrastructure.fact_compute_capacity`: `capacity_units`, `tight_flag`
- `social.infrastructure.fact_capex_plan`: `spend_amount`, `step_up_flag`

### Q2 2025 (4)

What technical hurdles still block scalable agents on commercial queries at Alphabet?

- `social.infrastructure.fact_agent_readiness`: `ready_scale_flag`, `blocker_code`
- `social.audience.fact_commercial_mix`: `commercial_share`
- `social.infrastructure.dim_agent_kind`: `kind_code`

### Q2 2025 (7)

How is Google doing at keeping key AI talent, and how should AI operating costs sit next to the capital-spending step-up?

- `social.infrastructure.fact_talent_retention`: `retention_rate`
- `social.infrastructure.fact_talent_cost`: `cost_amount`
- `social.infrastructure.fact_capex_plan`: `spend_amount`, `step_up_flag`

### Q2 2025 (10)

After a strong cloud quarter, how should the back half be read if supply constraints now ease into 2026 rather than late 2025 at Alphabet?

- `social.monetization.fact_cloud_revenue`: `revenue_amount`, `quarter_strong_flag`
- `social.infrastructure.fact_constraint_timing`: `eases_in_code`
- `social.infrastructure.fact_compute_capacity`: `tight_flag`

### Q2 2025 (12)

Is the larger capital-spending plan mainly a response to cloud demand at Alphabet?

- `social.infrastructure.fact_capex_plan`: `spend_amount`, `responds_to_cloud_flag`, `step_up_flag`
- `social.infrastructure.fact_cloud_backlog`: `backlog_amount`

## Meta Platforms

### Q2 2026 (1)

Among consumer agents, business agents, API tools, and compute rental, which can reach material scale in 2026 and 2027 given today’s products and compute at Meta Platforms?

- `social.infrastructure.fact_agent_readiness`: `ready_scale_flag`, `material_year_code`
- `social.infrastructure.fact_compute_capacity`: `capacity_units`, `tight_flag`
- `social.infrastructure.dim_agent_kind`: `kind_code`

### Q2 2026 (2)

How much of the enterprise opportunity can be sold through the existing advertising and marketing motion, versus a go-to-market system that still has to be built at Meta Platforms?

- `social.infrastructure.fact_enterprise_motion`: `covered_by_ads_motion_flag`, `new_gtm_required_flag`
- `social.infrastructure.dim_agent_kind`: `kind_code`

### Q2 2026 (4)

How far along is the shift to larger models and more compute for ranking and recommendations at Meta Platforms?

- `social.infrastructure.fact_ranking_model`: `larger_model_flag`, `production_share`
- `social.infrastructure.fact_compute_allocation`: `allocation_share`
- `social.audience.dim_surface`: `surface_code`

### Q2 2026 (5)

Why sell compute to others while also buying capacity from third parties at Meta Platforms?

- `social.infrastructure.fact_capacity_sale`: `sale_amount`, `reason_code`
- `social.infrastructure.fact_capacity_purchase`: `purchase_amount`, `reason_code`
- `social.infrastructure.dim_capacity_source`: `source_code`

### Q2 2026 (6)

How is the AI lab performing about a year after the senior team arrived, and when should faster model or chip releases show up at Meta Platforms?

- `social.infrastructure.fact_lab_output`: `output_index`, `year_since_team`
- `social.infrastructure.fact_chip_release`: `cadence_code`
- `social.infrastructure.fact_model_release`: `cadence_code`

### Q2 2026 (7)

What advantages is the lab building that should last beyond a single model generation at Meta Platforms?

- `social.infrastructure.fact_lab_output`: `durable_advantage_flag`, `output_index`
- `social.infrastructure.dim_lab_program`: `program_code`

### Q2 2026 (8)

Why compete at both the cheaper end of the model range and the high-performance end at Meta Platforms?

- `social.infrastructure.fact_model_role`: `cheap_end_flag`, `frontier_end_flag`
- `social.infrastructure.dim_model_family`: `family_code`

### Q2 2026 (9)

If open-weight models spread, does Meta still need to build its own closed frontier models?

- `social.infrastructure.fact_open_weight_case`: `spread_flag`, `still_need_closed_flag`
- `social.infrastructure.fact_model_role`: `frontier_end_flag`
- `social.infrastructure.dim_model_family`: `family_code`

### Q1 2026 (1)

Over the next 12 to 24 months, which signals — Meta AI usage, Muse progress, or core ranking — would show the AI capital spending is on a path to an acceptable return?

- `social.infrastructure.fact_return_signal`: `signal_code`, `on_path_flag`
- `social.audience.fact_assistant_usage`: `usage_index`
- `social.infrastructure.fact_ranking_model`: `production_share`
- `social.infrastructure.dim_model_family`: `family_code`

### Q1 2026 (2)

How is lab effort split between further training toward personal superintelligence and shipping products at Meta Platforms?

- `social.infrastructure.fact_lab_agenda`: `training_share`, `shipping_share`
- `social.infrastructure.dim_model_family`: `family_code`

### Q1 2026 (3)

How could 2027 capital spending step up from here, given peers have flagged large increases at Meta Platforms?

- `social.infrastructure.fact_capex_plan`: `spend_amount`, `year_2027_increase_flag`, `step_up_flag`
- `social.geography.dim_fiscal_quarter`: `guidance_horizon`

### Q1 2026 (4)

How do the media and commerce parts of the business become more agentic for consumers, alongside offering compute to enterprises at Meta Platforms?

- `social.infrastructure.fact_agent_readiness`: `ready_scale_flag`, `material_year_code`
- `social.monetization.fact_commerce_roadmap`: `utility_advanced_flag`
- `social.infrastructure.dim_agent_kind`: `kind_code`
- `social.audience.dim_surface`: `surface_code`

### Q1 2026 (5)

What limits launching AI glasses under more EssilorLuxottica brands this year, and what unit volume would count as a successful 2026 at Meta Platforms?

- `social.infrastructure.fact_glasses_volume`: `unit_quantity`, `success_threshold_quantity`, `brand_gate_flag`
- `social.infrastructure.dim_partner_brand`: `brand_code`
- `social.audience.dim_device_form`: `form_code`

### Q1 2026 (6)

How much of the workforce reduction is efficiency from AI rather than other cuts at Meta Platforms?

- `social.infrastructure.fact_headcount_ai`: `reduction_quantity`, `ai_efficiency_share`
- `social.infrastructure.dim_org_layer`: `layer_code`

### Q1 2026 (7)

What does Muse Spark unlock for products still in development, and what is the consumer versus enterprise release pace over the next nine months at Meta Platforms?

- `social.infrastructure.fact_product_unlock`: `unlock_code`, `consumer_pace_code`, `enterprise_pace_code`
- `social.infrastructure.dim_model_family`: `family_code`

### Q1 2026 (9)

Is a personal agent a near-term product or a longer-term goal now that Muse Spark is live at Meta Platforms?

- `social.infrastructure.fact_personal_agent`: `near_term_flag`
- `social.infrastructure.dim_agent_kind`: `kind_code`
- `social.infrastructure.dim_model_family`: `family_code`

### Q1 2026 (12)

What role does Manus play in agentic products, and where does that effort stand at Meta Platforms?

- `social.infrastructure.fact_manus_role`: `role_code`, `stand_code`
- `social.infrastructure.dim_product_bet`: `bet_code`
- `social.infrastructure.dim_agent_kind`: `kind_code`

### Q4 2025 (2)

How do internal compute needs now compare with the product roadmap, after a period of being capacity constrained at Meta Platforms?

- `social.infrastructure.fact_capacity_gap`: `gap_units`, `closing_flag`, `internal_or_external_code`
- `social.infrastructure.fact_compute_capacity`: `capacity_units`, `tight_flag`
- `social.infrastructure.dim_product_bet`: `bet_code`

### Q4 2025 (4)

How far is the new model team toward a frontier model this year at Meta Platforms?

- `social.infrastructure.fact_model_release`: `this_year_frontier_flag`, `cadence_code`
- `social.infrastructure.fact_lab_output`: `output_index`
- `social.infrastructure.dim_model_family`: `family_code`

### Q4 2025 (5)

Does 2026 still produce positive free cash flow as more of the data-center build moves through joint ventures at Meta Platforms?

- `social.infrastructure.fact_free_cash_flow`: `fcf_amount`, `positive_flag`
- `social.infrastructure.fact_data_center_jv`: `jv_share`, `on_balance_sheet_share`

### Q4 2025 (9)

Where is the ranking and recommendation roadmap, and is further gain waiting on newer models at Meta Platforms?

- `social.infrastructure.fact_ranking_model`: `production_share`, `waiting_on_next_flag`
- `social.audience.fact_engagement_gain`: `gain_index`
- `social.infrastructure.dim_model_family`: `family_code`

### Q4 2025 (10)

Does Meta need a leading general-purpose model, or is a model that is excellent at specific tasks enough?

- `social.infrastructure.fact_model_role`: `general_purpose_required_flag`, `task_specific_enough_flag`
- `social.infrastructure.dim_model_family`: `family_code`

### Q3 2025 (1)

Which early tests of 2026 ranking and ad models already support a return on the infrastructure build at Meta Platforms?

- `social.infrastructure.fact_return_signal`: `test_supports_return_flag`, `on_path_flag`, `signal_code`
- `social.infrastructure.fact_ranking_model`: `production_share`
- `social.infrastructure.fact_capex_plan`: `spend_amount`

### Q3 2025 (2)

How should next year’s faster expense growth and capital spending be read against core growth, earnings, and free cash flow at Meta Platforms?

- `social.infrastructure.fact_expense_growth`: `expense_growth_rate`, `capex_growth_rate`, `versus_core_growth_rate`
- `social.infrastructure.fact_free_cash_flow`: `fcf_amount`, `positive_flag`
- `social.infrastructure.fact_capex_plan`: `spend_amount`

### Q3 2025 (5)

Are the newer lab efforts timed to an updated frontier model next year at Meta Platforms?

- `social.infrastructure.fact_model_release`: `this_year_frontier_flag`, `cadence_code`
- `social.infrastructure.fact_lab_agenda`: `shipping_share`
- `social.infrastructure.dim_lab_program`: `program_code`

### Q3 2025 (6)

What user tools should come out of this AI cycle, and is there a reason margins would differ from prior product cycles at Meta Platforms?

- `social.infrastructure.fact_product_unlock`: `unlock_code`
- `social.infrastructure.fact_cycle_margin`: `differs_from_prior_cycle_flag`
- `social.infrastructure.dim_product_bet`: `bet_code`

### Q3 2025 (7)

Is the lab aimed at long-range milestones or at products that can earn revenue quickly, and is a personal AI for billions of people still the goal at Meta Platforms?

- `social.infrastructure.fact_lab_agenda`: `long_range_flag`, `near_term_revenue_flag`, `personal_ai_goal_flag`
- `social.infrastructure.dim_lab_program`: `program_code`

### Q3 2025 (9)

Can glasses volume alone repay the hardware investment, or does that require advertising, services, or commerce on the device at Meta Platforms?

- `social.infrastructure.fact_glasses_volume`: `unit_quantity`
- `social.infrastructure.fact_glasses_payback`: `volume_alone_repays_flag`, `needs_services_flag`
- `social.monetization.dim_revenue_pool`: `pool_code`

### Q3 2025 (10)

Once a leading frontier model exists, does the value sit with the platform or with scaled first-party apps at Meta Platforms?

- `social.infrastructure.fact_value_capture`: `layer_code`
- `social.infrastructure.dim_org_layer`: `layer_code`
- `social.infrastructure.dim_model_family`: `family_code`
