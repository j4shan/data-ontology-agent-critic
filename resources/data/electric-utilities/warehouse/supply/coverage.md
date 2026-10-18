# Utility Inc supply and capacity

This slice is part of the Utility Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity row does not store a price. A price row does not store the unit quantity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `dim_state_identity` | `state_id` | `utility.geography.dim_state` `state_id` |
| `dim_fiscal_quarter_identity` | `fiscal_quarter_id` | `utility.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `dim_customer_identity` | `customer_id` | `utility.customer.dim_customer` `customer_id` |
| `dim_contract_identity` | `contract_id` | `utility.customer.dim_contract` `contract_id` |

## Numbered questions

### Q2 2026 (4) — Duke Energy

For Duke Energy, what bottlenecks are appearing while 5 gigawatts are already under construction, and what should be watched on the next gas build?

- `utility.supply.fact_construction`: `under_construction_quantity`, `bottleneck_code`, `contracts_ready_flag`, `fiscal_quarter_id`, `project_id`, `technology_id`
- `utility.supply.fact_gas_build`: `next_wave_quantity`, `fuel_with_turbines_flag`, `fiscal_quarter_id`, `technology_id`, `turbine_class_id`
- `utility.supply.fact_bottleneck`: `bottleneck_code`, `watch_next_flag`, `fiscal_quarter_id`, `project_id`, `technology_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_turbine_class`: `turbine_class_id`, `class_code`, `class_name`, `technology_id`

### Q2 2026 (5) — Duke Energy

For Duke Energy, how does the new-nuclear effort come together beyond the near-term application work?

- `utility.supply.fact_nuclear_path`: `path_code`, `application_status_code`, `beyond_application_flag`, `fiscal_quarter_id`, `technology_id`, `project_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`

### Q2 2026 (7) — Duke Energy

For Duke Energy, is gas supply being secured for the next plants alongside the additional turbines, and could fuel supply constrain the build?

- `utility.supply.fact_turbine_supply`: `reserved_quantity`, `available_flag`, `fiscal_quarter_id`, `turbine_class_id`, `project_id`
- `utility.supply.fact_gas_supply`: `secured_flag`, `could_constrain_flag`, `fiscal_quarter_id`, `fuel_id`, `pipeline_id`, `project_id`
- `utility.supply.fact_construction`: `under_construction_quantity`, `bottleneck_code`, `contracts_ready_flag`, `fiscal_quarter_id`, `project_id`, `technology_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_turbine_class`: `turbine_class_id`, `class_code`, `class_name`, `technology_id`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`
- `utility.generation.dim_fuel`: `fuel_id`, `fuel_code`, `fuel_name`
- `utility.generation.dim_pipeline`: `pipeline_id`, `pipeline_code`, `pipeline_name`, `state_id`

### Q2 2026 (8) — Duke Energy

For Duke Energy, where does a possible sale of the Cayuga coal plant stand relative to Indiana's goals?

- `utility.supply.fact_coal_status`: `sale_status_code`, `aligned_with_state_flag`, `fiscal_quarter_id`, `plant_id`, `state_id`
- `utility.demand.fact_state_load`: `load_quantity`, `softer_flag`, `still_finalizing_flag`, `fiscal_quarter_id`, `state_id`, `load_class_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_plant`: `plant_id`, `plant_code`, `plant_name`, `state_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_load_class`: `load_class_id`, `class_code`, `class_name`

### Q2 2026 (9) — Duke Energy

For Duke Energy, is the nuclear preference large-scale reactors or small modular reactors, and is the company in a long-lead procurement?

- `utility.supply.fact_nuclear_choice`: `choice_code`, `long_lead_flag`, `fiscal_quarter_id`, `technology_id`
- `utility.supply.fact_long_lead`: `participating_flag`, `fiscal_quarter_id`, `technology_id`, `project_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`

### Q1 2026 (10) — Duke Energy

For Duke Energy, when do the energy-services projects not yet under construction start, and do local moratoriums threaten them?

- `utility.demand.fact_energy_services`: `signed_quantity`, `pipeline_quantity`, `not_yet_started_flag`, `fiscal_quarter_id`, `contract_id`, `state_id`
- `utility.supply.fact_construction`: `under_construction_quantity`, `bottleneck_code`, `contracts_ready_flag`, `fiscal_quarter_id`, `project_id`, `technology_id`
- `utility.supply.fact_moratorium`: `threatened_flag`, `fiscal_quarter_id`, `project_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`

### Q4 2025 (6) — Duke Energy

For Duke Energy, what still has to be cleared before firm construction contracts can be signed for the gas plants in the plan?

- `utility.supply.fact_gas_build`: `next_wave_quantity`, `fuel_with_turbines_flag`, `fiscal_quarter_id`, `technology_id`, `turbine_class_id`
- `utility.supply.fact_construction`: `under_construction_quantity`, `bottleneck_code`, `contracts_ready_flag`, `fiscal_quarter_id`, `project_id`, `technology_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_turbine_class`: `turbine_class_id`, `class_code`, `class_name`, `technology_id`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`

### Q4 2025 (7) — Duke Energy

For Duke Energy, what is the timing and capital for gas, nuclear, and hydro uprate opportunities?

- `utility.supply.fact_uprate`: `uprate_quantity`, `timing_code`, `fiscal_quarter_id`, `technology_id`, `plant_id`
- `utility.price.fact_capital_plan`: `capital_amount`, `inside_window_amount`, `later_amount`, `layered_even_flag`, `fiscal_quarter_id`, `capital_program_id`, `project_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_plant`: `plant_id`, `plant_code`, `plant_name`, `state_id`
- `utility.price.dim_capital_program`: `capital_program_id`, `program_code`, `program_name`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`

### Q4 2025 (9) — Duke Energy

For Duke Energy, is flexible interconnection being used to speed data-center connections, and would customers accept it?

- `utility.demand.fact_data_center_load`: `load_quantity`, `funnel_accelerated_flag`, `in_sales_range_flag`, `joint_announcement_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.supply.fact_interconnection`: `flexible_flag`, `speeds_connection_flag`, `customer_accepts_flag`, `fiscal_quarter_id`, `customer_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`

### Q3 2025 (3) — Duke Energy

For Duke Energy, if more natural-gas pipeline capacity reaches the Southeast, would the Carolinas resource plan shift further toward gas?

- `utility.supply.fact_resource_plan`: `gas_share_rate`, `would_shift_flag`, `fiscal_quarter_id`, `state_id`, `technology_id`
- `utility.supply.fact_gas_supply`: `secured_flag`, `could_constrain_flag`, `fiscal_quarter_id`, `fuel_id`, `pipeline_id`, `project_id`
- `utility.supply.fact_pipeline_capacity`: `expansion_quantity`, `gating_code`, `in_service_year`, `fiscal_quarter_id`, `pipeline_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_fuel`: `fuel_id`, `fuel_code`, `fuel_name`
- `utility.generation.dim_pipeline`: `pipeline_id`, `pipeline_code`, `pipeline_name`, `state_id`

### Q2 2026 (3) — Southern Company

As Southern Power tolling agreements roll off, can that capacity be repurposed for hyperscalers, and does it sit inside the existing pipeline?

- `utility.supply.fact_wholesale_fleet`: `contracted_quantity`, `upgrade_included_flag`, `fiscal_quarter_id`, `plant_id`, `contract_id`
- `utility.supply.fact_tolling`: `rolling_off_quantity`, `can_repurpose_flag`, `renegotiation_started_flag`, `fiscal_quarter_id`, `plant_id`, `contract_id`
- `utility.price.fact_hyperscaler_contract`: `long_term_flag`, `standard_toll_flag`, `bears_overrun_flag`, `fiscal_quarter_id`, `contract_id`, `counterparty_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_plant`: `plant_id`, `plant_code`, `plant_name`, `state_id`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.price.dim_counterparty`: `counterparty_id`, `counterparty_code`, `counterparty_name`, `customer_id`

### Q2 2026 (4) — Southern Company

For Southern Company, would those hyperscaler deals be long-term energy and capacity contracts rather than standard tolls?

- `utility.supply.fact_wholesale_fleet`: `contracted_quantity`, `upgrade_included_flag`, `fiscal_quarter_id`, `plant_id`, `contract_id`
- `utility.price.fact_hyperscaler_contract`: `long_term_flag`, `standard_toll_flag`, `bears_overrun_flag`, `fiscal_quarter_id`, `contract_id`, `counterparty_id`
- `utility.supply.fact_generation_capacity`: `capacity_quantity`, `incremental_required_flag`, `company_owned_flag`, `fiscal_quarter_id`, `technology_id`, `state_id`, `plant_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_plant`: `plant_id`, `plant_code`, `plant_name`, `state_id`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.price.dim_counterparty`: `counterparty_id`, `counterparty_code`, `counterparty_name`, `customer_id`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`

### Q2 2026 (6) — Southern Company

For Southern Company, what is new on FERC pipeline investment timing as incremental requests could point to more gas plants?

- `utility.supply.fact_pipeline_capacity`: `expansion_quantity`, `gating_code`, `in_service_year`, `fiscal_quarter_id`, `pipeline_id`, `state_id`
- `utility.supply.fact_gas_build`: `next_wave_quantity`, `fuel_with_turbines_flag`, `fiscal_quarter_id`, `technology_id`, `turbine_class_id`
- `utility.supply.fact_rfp`: `includes_latest_flag`, `upside_room_flag`, `covers_year_code`, `fiscal_quarter_id`, `rfp_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_pipeline`: `pipeline_id`, `pipeline_code`, `pipeline_name`, `state_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_turbine_class`: `turbine_class_id`, `class_code`, `class_name`, `technology_id`

### Q2 2026 (7) — Southern Company

For Southern Company, did generation RFPs through 2032 already include the latest load-pipeline progress, and is there room for further upside if more of the pipeline converts?

- `utility.supply.fact_rfp`: `includes_latest_flag`, `upside_room_flag`, `covers_year_code`, `fiscal_quarter_id`, `rfp_id`, `state_id`
- `utility.demand.fact_load_pipeline`: `pipeline_quantity`, `high_confidence_quantity`, `advanced_quantity`, `fiscal_quarter_id`, `load_class_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_rfp`: `rfp_id`, `rfp_code`, `rfp_name`, `state_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_load_class`: `load_class_id`, `class_code`, `class_name`

### Q2 2026 (14) — Southern Company

How are Southern Power upgrade and brownfield conversations trending with current and new counterparties?

- `utility.supply.fact_wholesale_fleet`: `contracted_quantity`, `upgrade_included_flag`, `fiscal_quarter_id`, `plant_id`, `contract_id`
- `utility.supply.fact_fleet_upgrade`: `upgrade_quantity`, `remaining_quantity`, `fiscal_quarter_id`, `plant_id`, `technology_id`
- `utility.supply.fact_site_type`: `greenfield_flag`, `brownfield_flag`, `fiscal_quarter_id`, `site_id`, `project_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_plant`: `plant_id`, `plant_code`, `plant_name`, `state_id`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_site`: `site_id`, `site_code`, `site_type_code`, `state_id`

### Q1 2026 (2) — Southern Company

Have renegotiations started on Southern Power tolls that are rolling off, including with hyperscalers?

- `utility.supply.fact_wholesale_fleet`: `contracted_quantity`, `upgrade_included_flag`, `fiscal_quarter_id`, `plant_id`, `contract_id`
- `utility.supply.fact_tolling`: `rolling_off_quantity`, `can_repurpose_flag`, `renegotiation_started_flag`, `fiscal_quarter_id`, `plant_id`, `contract_id`
- `utility.price.fact_hyperscaler_contract`: `long_term_flag`, `standard_toll_flag`, `bears_overrun_flag`, `fiscal_quarter_id`, `contract_id`, `counterparty_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_plant`: `plant_id`, `plant_code`, `plant_name`, `state_id`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.price.dim_counterparty`: `counterparty_id`, `counterparty_code`, `counterparty_name`, `customer_id`

### Q1 2026 (6) — Southern Company

What is the timing and remaining size of gas-fleet upgrades at Southern Power?

- `utility.supply.fact_wholesale_fleet`: `contracted_quantity`, `upgrade_included_flag`, `fiscal_quarter_id`, `plant_id`, `contract_id`
- `utility.supply.fact_fleet_upgrade`: `upgrade_quantity`, `remaining_quantity`, `fiscal_quarter_id`, `plant_id`, `technology_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_plant`: `plant_id`, `plant_code`, `plant_name`, `state_id`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`

### Q1 2026 (7) — Southern Company

For Southern Company, when does the Georgia all-source process give visibility into company-owned resources and capital, and could some capacity be needed before 2032?

- `utility.supply.fact_rfp`: `includes_latest_flag`, `upside_room_flag`, `covers_year_code`, `fiscal_quarter_id`, `rfp_id`, `state_id`
- `utility.supply.fact_generation_capacity`: `capacity_quantity`, `incremental_required_flag`, `company_owned_flag`, `fiscal_quarter_id`, `technology_id`, `state_id`, `plant_id`
- `utility.supply.fact_schedule`: `in_service_year`, `milestone_code`, `remaining_flag`, `fiscal_quarter_id`, `project_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_rfp`: `rfp_id`, `rfp_code`, `rfp_name`, `state_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_plant`: `plant_id`, `plant_code`, `plant_name`, `state_id`

### Q1 2026 (8) — Southern Company

For Southern Company, where do turbine and labor supply stand, and when is the next all-source request needed as more large-load contracts are signed?

- `utility.supply.fact_turbine_supply`: `reserved_quantity`, `available_flag`, `fiscal_quarter_id`, `turbine_class_id`, `project_id`
- `utility.supply.fact_labor_supply`: `available_flag`, `constraint_flag`, `fiscal_quarter_id`, `project_id`
- `utility.demand.fact_large_load`: `load_quantity`, `top_of_range_flag`, `incremental_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.supply.fact_generation_capacity`: `capacity_quantity`, `incremental_required_flag`, `company_owned_flag`, `fiscal_quarter_id`, `technology_id`, `state_id`, `plant_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_turbine_class`: `turbine_class_id`, `class_code`, `class_name`, `technology_id`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`

### Q1 2026 (9) — Southern Company

How much Southern Power capacity is contracted today, including the upgrade megawatts?

- `utility.supply.fact_wholesale_fleet`: `contracted_quantity`, `upgrade_included_flag`, `fiscal_quarter_id`, `plant_id`, `contract_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_plant`: `plant_id`, `plant_code`, `plant_name`, `state_id`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`

### Q3 2025 (2) — Southern Company

For Southern Company, how could upcoming commission elections affect generation certifications in Georgia?

- `utility.supply.fact_regulation_timing`: `approval_status_code`, `can_extend_flag`, `election_risk_flag`, `fiscal_quarter_id`, `state_id`, `rfp_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.generation.dim_rfp`: `rfp_id`, `rfp_code`, `rfp_name`, `state_id`

### Q3 2025 (4) — Southern Company

For Southern Company, what is the timing of Southeast gas supply and the pipeline expansion needed to serve it?

- `utility.supply.fact_gas_supply`: `secured_flag`, `could_constrain_flag`, `fiscal_quarter_id`, `fuel_id`, `pipeline_id`, `project_id`
- `utility.supply.fact_pipeline_capacity`: `expansion_quantity`, `gating_code`, `in_service_year`, `fiscal_quarter_id`, `pipeline_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_fuel`: `fuel_id`, `fuel_code`, `fuel_name`
- `utility.generation.dim_pipeline`: `pipeline_id`, `pipeline_code`, `pipeline_name`, `state_id`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`

### Q3 2025 (6) — Southern Company

For Southern Company, is there still room to add more large load by 2029, and which years would the next requests for generation cover?

- `utility.demand.fact_large_load`: `load_quantity`, `top_of_range_flag`, `incremental_flag`, `fiscal_quarter_id`, `state_id`, `customer_id`
- `utility.supply.fact_headroom`: `headroom_quantity`, `next_request_year`, `fiscal_quarter_id`, `state_id`, `rfp_id`
- `utility.supply.fact_rfp`: `includes_latest_flag`, `upside_room_flag`, `covers_year_code`, `fiscal_quarter_id`, `rfp_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`
- `utility.customer.dim_customer`: `customer_id`, `customer_name`, `customer_code`, `customer_segment_id`
- `utility.generation.dim_rfp`: `rfp_id`, `rfp_code`, `rfp_name`, `state_id`

### Q3 2025 (7) — Southern Company

Are customers now willing to pay fully loaded economics for contract-based gas plants at Southern Power?

- `utility.supply.fact_wholesale_fleet`: `contracted_quantity`, `upgrade_included_flag`, `fiscal_quarter_id`, `plant_id`, `contract_id`
- `utility.supply.fact_new_build`: `capacity_quantity`, `needs_offtake_flag`, `needed_sooner_flag`, `fiscal_quarter_id`, `technology_id`, `project_id`
- `utility.price.fact_contract_price`: `offered_price_amount`, `covers_return_flag`, `customers_willing_flag`, `fiscal_quarter_id`, `contract_id`, `counterparty_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_plant`: `plant_id`, `plant_code`, `plant_name`, `state_id`
- `utility.customer.dim_contract`: `contract_id`, `contract_code`, `contract_name`, `customer_id`, `load_class_id`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`

### Q2 2025 (2) — Southern Company

For Southern Company, where do turbine procurement and gas supply stand for combined-cycle units aimed at 2029 and 2030?

- `utility.supply.fact_new_build`: `capacity_quantity`, `needs_offtake_flag`, `needed_sooner_flag`, `fiscal_quarter_id`, `technology_id`, `project_id`
- `utility.supply.fact_turbine_supply`: `reserved_quantity`, `available_flag`, `fiscal_quarter_id`, `turbine_class_id`, `project_id`
- `utility.supply.fact_gas_supply`: `secured_flag`, `could_constrain_flag`, `fiscal_quarter_id`, `fuel_id`, `pipeline_id`, `project_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`
- `utility.generation.dim_turbine_class`: `turbine_class_id`, `class_code`, `class_name`, `technology_id`
- `utility.generation.dim_fuel`: `fuel_id`, `fuel_code`, `fuel_name`

### Q2 2025 (5) — Southern Company

For Southern Company, where do new-nuclear discussions stand after the resource plan's upgrade cases?

- `utility.supply.fact_uprate`: `uprate_quantity`, `timing_code`, `fiscal_quarter_id`, `technology_id`, `plant_id`
- `utility.supply.fact_nuclear_path`: `path_code`, `application_status_code`, `beyond_application_flag`, `fiscal_quarter_id`, `technology_id`, `project_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_plant`: `plant_id`, `plant_code`, `plant_name`, `state_id`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`

### Q2 2025 (7) — Southern Company

For Southern Company, how confident is delivery of purchased combined-cycle capacity as early as 2028 given equipment and construction timing?

- `utility.supply.fact_purchased_capacity`: `purchased_quantity`, `delivery_confidence_code`, `fiscal_quarter_id`, `technology_id`, `project_id`
- `utility.supply.fact_new_build`: `capacity_quantity`, `needs_offtake_flag`, `needed_sooner_flag`, `fiscal_quarter_id`, `technology_id`, `project_id`
- `utility.supply.fact_schedule`: `in_service_year`, `milestone_code`, `remaining_flag`, `fiscal_quarter_id`, `project_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`

### Q2 2025 (9) — Southern Company

For Southern Company, what gating items remain on a FERC gas-pipeline expansion?

- `utility.supply.fact_pipeline_capacity`: `expansion_quantity`, `gating_code`, `in_service_year`, `fiscal_quarter_id`, `pipeline_id`, `state_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_pipeline`: `pipeline_id`, `pipeline_code`, `pipeline_name`, `state_id`
- `utility.geography.dim_state`: `state_id`, `state_code`, `state_name`, `region_id`

### Q2 2025 (10) — Southern Company

For Southern Company, what generation-cost inflation is being assumed for future combined cycles and peakers?

- `utility.supply.fact_new_build`: `capacity_quantity`, `needs_offtake_flag`, `needed_sooner_flag`, `fiscal_quarter_id`, `technology_id`, `project_id`
- `utility.price.fact_cost_inflation`: `inflation_amount`, `cost_per_kw_amount`, `assumed_flag`, `fiscal_quarter_id`, `technology_id`, `cost_bucket_id`
- `utility.geography.dim_fiscal_quarter`: `fiscal_quarter_id`, `quarter_code`, `quarter_label`, `guidance_horizon`
- `utility.generation.dim_technology`: `technology_id`, `technology_code`, `technology_name`
- `utility.generation.dim_project`: `project_id`, `project_code`, `project_name`, `plant_id`, `technology_id`, `state_id`
- `utility.price.dim_cost_bucket`: `cost_bucket_id`, `bucket_code`, `bucket_name`
