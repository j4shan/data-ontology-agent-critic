# Utility Inc demand, customer, and geography

This slice is part of the Utility Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity row does not store a price. A price row does not store the unit quantity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `dim_project_identity` | `project_id` | `utility.generation.dim_project` `project_id` |
| `dim_site_identity` | `site_id` | `utility.generation.dim_site` `site_id` |

## Numbered questions

### Q2 2026 (2) — Duke Energy

For Duke Energy, given affordability pressure in Indiana, would a generation-company structure be used to serve large load?

- `utility.demand.fact_state_load`: `load_quantity`, `softer_flag`, `still_finalizing_flag`, `fiscal_quarter_id`, `state_id`, `load_class_id`
- `utility.demand.fact_large_load`: `load_quantity`, `top_of_range_flag`, `incremental_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.supply.fact_generation_structure`: `would_use_flag`, `structure_code`, `fiscal_quarter_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_load_class`: `load_class_id`, `class_code`, `class_name`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`

### Q2 2026 (3) — Duke Energy

For Duke Energy, how much of the potential Florida and Indiana large-load capital lands inside the next five-year plan versus the mid-2030s?

- `utility.demand.fact_state_load`: `load_quantity`, `softer_flag`, `still_finalizing_flag`, `fiscal_quarter_id`, `state_id`, `load_class_id`
- `utility.price.fact_capital_plan`: `capital_amount`, `inside_window_amount`, `later_amount`, `layered_even_flag`, `fiscal_quarter_id`, `capital_program_id`, `project_id`
- `utility.demand.fact_large_load`: `load_quantity`, `top_of_range_flag`, `incremental_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_load_class`: `load_class_id`, `class_code`, `class_name`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`

### Q2 2026 (6) — Duke Energy

For Duke Energy, how many gigawatts of the high-confidence load pipeline sit in Indiana and Florida versus the Carolinas?

- `utility.demand.fact_state_load`: `load_quantity`, `softer_flag`, `still_finalizing_flag`, `fiscal_quarter_id`, `state_id`, `load_class_id`
- `utility.demand.fact_load_pipeline`: `pipeline_quantity`, `high_confidence_quantity`, `advanced_quantity`, `fiscal_quarter_id`, `load_class_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_load_class`: `load_class_id`, `class_code`, `class_name`

### Q1 2026 (2) — Duke Energy

For Duke Energy, where does the South Carolina large-load tariff docket stand, and could it catalyze more load?

- `utility.demand.fact_state_load`: `load_quantity`, `softer_flag`, `still_finalizing_flag`, `fiscal_quarter_id`, `state_id`, `load_class_id`
- `utility.price.fact_tariff_terms`: `credit_terms_code`, `reaches_back_flag`, `docket_status_code`, `fiscal_quarter_id`, `tariff_id`, `customer_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_load_class`: `load_class_id`, `class_code`, `class_name`
- `utility.customer.dim_tariff`: `tariff_id`, `tariff_code`, `tariff_name`, `state_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`

### Q1 2026 (5) — Duke Energy

For Duke Energy, how could the energy-services agreement pipeline beyond the signed set expand the capital plan over time?

- `utility.demand.fact_energy_services`: `signed_quantity`, `pipeline_quantity`, `not_yet_started_flag`, `fiscal_quarter_id`, `contract_id`, `state_id`
- `utility.demand.fact_load_pipeline`: `pipeline_quantity`, `high_confidence_quantity`, `advanced_quantity`, `fiscal_quarter_id`, `load_class_id`, `state_id`
- `utility.price.fact_capital_plan`: `capital_amount`, `inside_window_amount`, `later_amount`, `layered_even_flag`, `fiscal_quarter_id`, `capital_program_id`, `project_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_load_class`: `load_class_id`, `class_code`, `class_name`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`

### Q1 2026 (8) — Duke Energy

For Duke Energy, has top-of-funnel data-center interest accelerated, and are any regions emerging as larger hubs?

- `utility.demand.fact_load_pipeline`: `pipeline_quantity`, `high_confidence_quantity`, `advanced_quantity`, `fiscal_quarter_id`, `load_class_id`, `state_id`
- `utility.demand.fact_state_load`: `load_quantity`, `softer_flag`, `still_finalizing_flag`, `fiscal_quarter_id`, `state_id`, `load_class_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.customer.dim_load_class`: `load_class_id`, `class_code`, `class_name`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`

### Q4 2025 (3) — Duke Energy

For Duke Energy, how confident is the company in rolling incremental data-center opportunities into the capital plan?

- `utility.demand.fact_data_center_load`: `load_quantity`, `funnel_accelerated_flag`, `in_sales_range_flag`, `joint_announcement_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.price.fact_capital_plan`: `capital_amount`, `inside_window_amount`, `later_amount`, `layered_even_flag`, `fiscal_quarter_id`, `capital_program_id`, `project_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`

### Q4 2025 (10) — Duke Energy

For Duke Energy, how much data-center load is already inside the enterprise and Carolinas sales-growth ranges, and how would more signed agreements change those ranges?

- `utility.demand.fact_data_center_load`: `load_quantity`, `funnel_accelerated_flag`, `in_sales_range_flag`, `joint_announcement_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.demand.fact_sales`: `sales_quantity`, `growth_rate`, `target_year_code`, `in_range_flag`, `fiscal_quarter_id`, `state_id`, `customer_segment_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `utility.customer.dim_customer_segment`: `customer_segment_id`, `segment_code`, `segment_name`

### Q2 2026 (1) — Southern Company

For Southern Company, how does better visibility on contracted megawatts and the 2028 load ramp change how far regulatory plans can be extended?

- `utility.demand.fact_large_load`: `load_quantity`, `top_of_range_flag`, `incremental_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.demand.fact_sales`: `sales_quantity`, `growth_rate`, `target_year_code`, `in_range_flag`, `fiscal_quarter_id`, `state_id`, `customer_segment_id`
- `utility.supply.fact_regulation_timing`: `approval_status_code`, `can_extend_flag`, `election_risk_flag`, `fiscal_quarter_id`, `state_id`, `rfp_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `utility.customer.dim_customer_segment`: `customer_segment_id`, `segment_code`, `segment_name`
- `utility.generation.dim_rfp`: `rfp_id`, `rfp_code`, `rfp_name`, `state_id`

### Q2 2026 (2) — Southern Company

For Southern Company, are the 3 gigawatts still being finalized inside the 2030 window, and what milestones remain?

- `utility.demand.fact_contracted_load`: `contracted_quantity`, `still_finalizing_flag`, `fiscal_quarter_id`, `contract_id`, `state_id`
- `utility.supply.fact_generation_capacity`: `capacity_quantity`, `incremental_required_flag`, `company_owned_flag`, `fiscal_quarter_id`, `technology_id`, `state_id`, `plant_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_plant`: `plant_id`, `plant_code`, `plant_name`, `state_id`

### Q2 2026 (8) — Southern Company

For Southern Company, does every incremental large load in Alabama require incremental generation, given signed contracts and an oversubscribed request?

- `utility.demand.fact_state_load`: `load_quantity`, `softer_flag`, `still_finalizing_flag`, `fiscal_quarter_id`, `state_id`, `load_class_id`
- `utility.demand.fact_large_load`: `load_quantity`, `top_of_range_flag`, `incremental_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.supply.fact_generation_capacity`: `capacity_quantity`, `incremental_required_flag`, `company_owned_flag`, `fiscal_quarter_id`, `technology_id`, `state_id`, `plant_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_load_class`: `load_class_id`, `class_code`, `class_name`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`

### Q2 2026 (9) — Southern Company

For Southern Company, how is the OpenAI demand-response commitment being factored into the broader project pipeline?

- `utility.demand.fact_demand_response`: `response_quantity`, `first_of_kind_flag`, `in_pipeline_flag`, `fiscal_quarter_id`, `customer_id`, `state_id`
- `utility.demand.fact_data_center_load`: `load_quantity`, `funnel_accelerated_flag`, `in_sales_range_flag`, `joint_announcement_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.supply.fact_pipeline_capacity`: `expansion_quantity`, `gating_code`, `in_service_year`, `fiscal_quarter_id`, `pipeline_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.generation.dim_pipeline`: `pipeline_id`, `pipeline_code`, `pipeline_name`, `state_id`

### Q2 2026 (11) — Southern Company

For Southern Company, has the customer-rate benefit of data centers changed the political reception in Georgia?

- `utility.demand.fact_state_load`: `load_quantity`, `softer_flag`, `still_finalizing_flag`, `fiscal_quarter_id`, `state_id`, `load_class_id`
- `utility.demand.fact_data_center_load`: `load_quantity`, `funnel_accelerated_flag`, `in_sales_range_flag`, `joint_announcement_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.price.fact_customer_rate`: `rate_amount`, `political_reception_code`, `larger_credit_chance_flag`, `fiscal_quarter_id`, `state_id`, `tariff_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_load_class`: `load_class_id`, `class_code`, `class_name`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `utility.customer.dim_tariff`: `tariff_id`, `tariff_code`, `tariff_name`, `state_id`

### Q2 2026 (12) — Southern Company

For Southern Company, is the gigawatt of demand response a first for a data center, and have the customer savings been quantified?

- `utility.demand.fact_demand_response`: `response_quantity`, `first_of_kind_flag`, `in_pipeline_flag`, `fiscal_quarter_id`, `customer_id`, `state_id`
- `utility.demand.fact_data_center_load`: `load_quantity`, `funnel_accelerated_flag`, `in_sales_range_flag`, `joint_announcement_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.price.fact_customer_savings`: `savings_amount`, `quantified_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`

### Q2 2026 (15) — Southern Company

For Southern Company, what has the recent data-center ramp taught about sales trends?

- `utility.demand.fact_data_center_load`: `load_quantity`, `funnel_accelerated_flag`, `in_sales_range_flag`, `joint_announcement_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.demand.fact_sales`: `sales_quantity`, `growth_rate`, `target_year_code`, `in_range_flag`, `fiscal_quarter_id`, `state_id`, `customer_segment_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `utility.customer.dim_customer_segment`: `customer_segment_id`, `segment_code`, `segment_name`

### Q1 2026 (3) — Southern Company

For Southern Company, is large-load visibility ahead of the plan that supported the regulatory stay-outs?

- `utility.demand.fact_large_load`: `load_quantity`, `top_of_range_flag`, `incremental_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.price.fact_stay_out`: `ahead_of_stay_out_flag`, `can_extend_flag`, `fiscal_quarter_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`

### Q1 2026 (5) — Southern Company

For Southern Company, why does the Georgia large-load report look softer while other states, including Alabama, keep finalizing contracts?

- `utility.demand.fact_state_load`: `load_quantity`, `softer_flag`, `still_finalizing_flag`, `fiscal_quarter_id`, `state_id`, `load_class_id`
- `utility.demand.fact_contracted_load`: `contracted_quantity`, `still_finalizing_flag`, `fiscal_quarter_id`, `contract_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_load_class`: `load_class_id`, `class_code`, `class_name`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`

### Q3 2025 (3) — Southern Company

For Southern Company, what operational, regulatory, or signed data-center milestones would make a 2027 rebase more definite?

- `utility.demand.fact_contracted_load`: `contracted_quantity`, `still_finalizing_flag`, `fiscal_quarter_id`, `contract_id`, `state_id`
- `utility.price.fact_rebase`: `rebase_year_code`, `aimed_at_top_flag`, `more_definite_flag`, `fiscal_quarter_id`, `capital_program_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`

### Q3 2025 (5) — Southern Company

For Southern Company, how much of the later-decade large-load figure is the same projects ramping versus new projects?

- `utility.demand.fact_large_load`: `load_quantity`, `top_of_range_flag`, `incremental_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.demand.fact_project_ramp`: `ramp_quantity`, `same_projects_flag`, `new_project_quantity`, `fiscal_quarter_id`, `state_id`, `project_id`
- `utility.demand.fact_contracted_load`: `contracted_quantity`, `still_finalizing_flag`, `fiscal_quarter_id`, `contract_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`

### Q3 2025 (8) — Southern Company

For Southern Company, what is the difference between contracted and committed large load, and how many gigawatts are in advanced negotiation?

- `utility.demand.fact_contracted_load`: `contracted_quantity`, `still_finalizing_flag`, `fiscal_quarter_id`, `contract_id`, `state_id`
- `utility.demand.fact_committed_load`: `committed_quantity`, `stage_gap_quantity`, `fiscal_quarter_id`, `load_class_id`, `state_id`
- `utility.demand.fact_load_pipeline`: `pipeline_quantity`, `high_confidence_quantity`, `advanced_quantity`, `fiscal_quarter_id`, `load_class_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_load_class`: `load_class_id`, `class_code`, `class_name`

### Q3 2025 (9) — Southern Company

For Southern Company, in which year is the targeted sales-growth rate expected to be reached?

- `utility.demand.fact_sales`: `sales_quantity`, `growth_rate`, `target_year_code`, `in_range_flag`, `fiscal_quarter_id`, `state_id`, `customer_segment_id`
- `utility.demand.fact_large_load`: `load_quantity`, `top_of_range_flag`, `incremental_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_customer_segment`: `customer_segment_id`, `segment_code`, `segment_name`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`

### Q3 2025 (10) — Southern Company

For Southern Company, is the average large-load project a few hundred megawatts, and are the later-stage projects greenfield or brownfield?

- `utility.demand.fact_project_size`: `project_count`, `average_mw_quantity`, `fiscal_quarter_id`, `state_id`, `site_id`
- `utility.supply.fact_site_type`: `greenfield_flag`, `brownfield_flag`, `fiscal_quarter_id`, `site_id`, `project_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.generation.dim_site`: `site_id`, `site_code`, `site_type_code`, `state_id`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`

### Q2 2025 (6) — Southern Company

For Southern Company, is the large-load update expected to come in above the prior pipeline figure?

- `utility.demand.fact_load_pipeline`: `pipeline_quantity`, `high_confidence_quantity`, `advanced_quantity`, `fiscal_quarter_id`, `load_class_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.customer.dim_load_class`: `load_class_id`, `class_code`, `class_name`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`

### Q2 2025 (8) — Southern Company

For Southern Company, after completing the resource-plan process, how durable is the demand outlook over the next few years?

- `utility.demand.fact_demand_outlook`: `outlook_quantity`, `durable_flag`, `fiscal_quarter_id`, `state_id`
- `utility.supply.fact_resource_plan`: `gas_share_rate`, `would_shift_flag`, `fiscal_quarter_id`, `state_id`, `technology_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`

### Q2 2025 (11) — Southern Company

For Southern Company, why are fewer data-center announcements being made jointly with the company in Georgia and Mississippi than at some other utilities?

- `utility.demand.fact_data_center_load`: `load_quantity`, `funnel_accelerated_flag`, `in_sales_range_flag`, `joint_announcement_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.demand.fact_state_load`: `load_quantity`, `softer_flag`, `still_finalizing_flag`, `fiscal_quarter_id`, `state_id`, `load_class_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `utility.customer.dim_load_class`: `load_class_id`, `class_code`, `class_name`
