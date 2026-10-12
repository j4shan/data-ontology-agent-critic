# Apple price versus services attach

This slice owns the device price file, price decisions, margin, and services. Services attach is its own fact. It may name a shipment or an installed-base snapshot, and it does not store shipment quantity or the device unit price. Channel, country, device family, and calendar day are owned by the demand slice and are partial here. Component cost and shipments are owned by the supply slice and are partial when a price row names them.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `calendar_day_identity` | `calendar_day_id` | `sf:apple.geography.dim_calendar_day` `calendar_day_id` |
| `channel_identity` | `channel_id` | `sf:apple.channel.dim_channel` `channel_id` |
| `component_identity` | `component_id` | `sf:apple.component.dim_component` `component_id` |
| `country_identity` | `country_id` | `sf:apple.geography.dim_country` `country_id` |
| `device_family_identity` | `device_family_id` | `sf:apple.product.dim_device_family` `device_family_id` |
| `device_shipment_identity` | `device_shipment_id` | `sf:apple.supply.fact_device_shipment` `device_shipment_id` |
| `feature_identity` | `feature_id` | `sf:apple.product.dim_feature` `feature_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:apple.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `installed_base_identity` | `installed_base_id` | `sf:apple.demand.fact_installed_base` `installed_base_id` |

## Numbered questions

### Q3 FY2026 (4)

Will the new Siri be a holiday iPhone demand driver, and what does the public beta imply for compute cost and recovery through iCloud+?

- `apple.demand.fact_feature_demand`: `beta_usage_rate`, `holiday_demand_lift_rate`, `expected_demand_driver_flag`, `feature_id`, `device_family_id`, `fiscal_quarter_id`
- `apple.services.fact_compute_economics`: `compute_cost_amount`, `recovered_through_service_amount`, `request_share`, `compute_location_id`, `service_offering_id`, `feature_id`
- `apple.services.dim_service_offering`: `offering_code`
- `apple.product.dim_feature`: `feature_code`
- `apple.product.dim_device_family`: `family_code`

### Q3 FY2026 (7)

What is slowing Services growth, including whether the App Store is the main driver of the further deceleration in the outlook?

- `apple.services.fact_services_growth`: `services_growth_rate`, `app_store_growth_rate`, `outlook_growth_rate`, `deceleration_driver_code`, `app_store_is_main_driver_flag`, `fiscal_quarter_id`, `outlook_quarter_code`
- `apple.services.dim_service_offering`: `offering_code`

### Q3 FY2026 (9)

Does Siri raise Apple's capital intensity even with on-device work, given traffic that still hits first-party and third-party cloud?

- `apple.services.fact_compute_economics`: `request_share`, `capital_intensity_rate`, `compute_cost_amount`, `compute_location_id`, `feature_id`, `fiscal_quarter_id`
- `apple.services.fact_capital_plan`: `capital_spend_amount`, `first_party_share`, `third_party_share`, `compute_location_id`, `fiscal_quarter_id`
- `apple.services.dim_compute_location`: `location_code`
- `apple.product.dim_feature`: `feature_code`

### Q2 FY2026 (2)

After June, can product gross margin stay in a narrow band despite component costs and constraints, or is visibility too short?

- `apple.price.fact_product_margin`: `product_gross_margin_rate`, `margin_band_low`, `margin_band_high`, `visibility_beyond_quarter_flag`, `fiscal_quarter_id`
- `apple.price.fact_margin_bridge`: `component_cost_effect_amount`, `memory_cost_effect_amount`, `fiscal_quarter_id`
- `apple.supply.fact_constraint_spread`: `spreading_flag`, `versus_prior_quarter_code`, `component_commodity_id`, `fiscal_quarter_id`
- `apple.supply.fact_component_cost`: `cost_change_amount`, `dislocated_flag`, `component_commodity_id`

### Q2 FY2026 (4)

Has new App Store ad inventory been a meaningful piece of Services growth, and how do planned Maps ads extend that?

- `apple.services.fact_ad_inventory`: `revenue_amount`, `share_of_services_growth`, `meaningful_flag`, `planned_extension_flag`, `service_offering_id`, `fiscal_quarter_id`
- `apple.services.fact_services_growth`: `services_growth_rate`, `fiscal_quarter_id`
- `apple.services.dim_service_offering`: `offering_code`

### Q2 FY2026 (6)

Which layers of an agentic stack does Apple build versus partners, and does that require more of Apple's own infrastructure?

- `apple.services.fact_agent_stack`: `apple_builds_flag`, `requires_apple_infrastructure_flag`, `stack_layer_id`, `model_source_id`, `fiscal_quarter_id`
- `apple.services.fact_ai_pnl`: `infrastructure_investment_amount`, `net_cash_amount`, `requires_more_investment_flag`, `fiscal_quarter_id`
- `apple.services.dim_stack_layer`: `layer_code`
- `apple.services.dim_model_source`: `source_code`

### Q2 FY2026 (9)

Is Services gross margin getting harder to expand because of mix, or is there still volume leverage and loss improvement left?

- `apple.services.fact_services_margin`: `services_gross_margin_rate`, `mix_pressure_amount`, `volume_leverage_amount`, `loss_improvement_amount`, `expansion_harder_flag`, `fiscal_quarter_id`

### Q2 FY2026 (10)

How is effort balanced between Apple's own models and the Google collaboration, and does that require more investment?

- `apple.services.fact_ai_pnl`: `own_model_spend_amount`, `partner_model_spend_amount`, `requires_more_investment_flag`, `partner_id`, `model_source_id`, `fiscal_quarter_id`
- `apple.services.dim_partner`: `partner_name`, `partner_role`
- `apple.services.dim_model_source`: `source_code`

### Q2 FY2026 (11)

Is the milder sequential product-margin move mix, currency, or both?

- `apple.price.fact_product_margin`: `sequential_change_amount`, `product_gross_margin_rate`, `fiscal_quarter_id`
- `apple.price.fact_margin_bridge`: `mix_effect_amount`, `fx_effect_amount`, `fiscal_quarter_id`

### Q1 FY2026 (1)

What revenue can AI add, relative to the operating-cost increase already visible?

- `apple.services.fact_ai_pnl`: `ai_revenue_opportunity_amount`, `ai_opex_amount`, `in_run_rate_flag`, `fiscal_quarter_id`
- `apple.services.fact_opex`: `step_up_amount`, `opex_amount`, `opex_component_id`, `fiscal_quarter_id`

### Q1 FY2026 (3)

Why was Google the choice for the Siri partnership, and is there a revenue share similar to Search?

- `apple.services.fact_partnership_economics`: `chosen_for_siri_flag`, `siri_revenue_share_rate`, `search_revenue_share_rate`, `similar_to_search_flag`, `partner_id`, `service_offering_id`, `fiscal_quarter_id`
- `apple.services.dim_partner`: `partner_name`, `partner_role`
- `apple.services.dim_service_offering`: `offering_code`

### Q1 FY2026 (4)

How is gross margin holding in the high 40s despite memory and NAND inflation — mix, Services margin, or something else?

- `apple.price.fact_product_margin`: `product_gross_margin_rate`, `in_high_forties_flag`, `fiscal_quarter_id`
- `apple.price.fact_margin_bridge`: `memory_cost_effect_amount`, `nand_cost_effect_amount`, `mix_effect_amount`, `services_mix_effect_amount`, `fiscal_quarter_id`
- `apple.services.fact_services_margin`: `services_gross_margin_rate`, `fiscal_quarter_id`
- `apple.supply.fact_component_cost`: `inflation_rate`, `component_commodity_id`
- `apple.component.dim_component_commodity`: `commodity_code`

### Q1 FY2026 (7)

If App Store growth was slower than total Services, what else drove Services and what would reaccelerate the store?

- `apple.services.fact_services_growth`: `services_growth_rate`, `app_store_growth_rate`, `deceleration_driver_code`, `fiscal_quarter_id`
- `apple.services.fact_services_driver`: `driver_code`, `contribution_amount`, `service_offering_id`, `fiscal_quarter_id`
- `apple.services.dim_service_offering`: `offering_code`

### Q1 FY2026 (8)

Would product price be used as a lever for unprecedented memory moves, beyond the usual currency cases?

- `apple.price.fact_price_decision`: `used_price_lever_flag`, `lever_reason_code`, `product_price_change_amount`, `device_family_id`, `fiscal_quarter_id`
- `apple.price.fact_price_file`: `unit_price`, `currency_id`, `device_family_id`, `channel_id`, `country_id`, `calendar_day_id`
- `apple.supply.fact_component_cost`: `inflation_rate`, `dislocated_flag`, `component_commodity_id`
- `apple.component.dim_component_commodity`: `commodity_code`

### Q1 FY2026 (11)

Is AI expected to be mostly on device, and is enough data-center capacity reserved for a wide Siri launch without a hyperscale-style capital-spending surge?

- `apple.services.fact_compute_economics`: `request_share`, `compute_location_id`, `feature_id`, `fiscal_quarter_id`
- `apple.services.fact_capital_plan`: `reserved_capacity_units`, `reserved_for_wide_launch_flag`, `hyperscale_surge_flag`, `capital_spend_amount`, `compute_location_id`, `fiscal_quarter_id`
- `apple.services.dim_compute_location`: `location_code`
- `apple.product.dim_feature`: `feature_code`

### Q4 FY2025 (3)

Was the Services upside organic, or did a partner payment or antitrust outcome contribute?

- `apple.services.fact_partner_payment`: `payment_amount`, `one_time_flag`, `antitrust_outcome_flag`, `organic_services_flag`, `partner_id`, `service_offering_id`, `fiscal_quarter_id`
- `apple.services.fact_services_growth`: `services_growth_rate`, `fiscal_quarter_id`

### Q4 FY2025 (4)

What accelerated Services — new-iPhone cross-sell, installed-base growth, or bundles such as Apple One and AppleCare?

- `apple.services.fact_services_driver`: `driver_code`, `contribution_amount`, `service_offering_id`, `device_family_id`, `fiscal_quarter_id`
- `apple.services.dim_service_offering`: `offering_code`
- `apple.demand.fact_installed_base`: `installed_quantity`, `device_family_id`, `country_id`
- `apple.product.dim_device_family`: `family_code`

### Q4 FY2025 (9)

What is inside the December operating-expense step-up, and should expense growth keep outrunning revenue?

- `apple.services.fact_opex`: `opex_amount`, `step_up_amount`, `opex_growth_rate`, `revenue_growth_rate`, `expense_outruns_revenue_flag`, `opex_component_id`, `fiscal_quarter_id`
- `apple.services.dim_opex_component`: `component_code`, `component_name`
- `apple.geography.dim_fiscal_quarter`: `quarter_code`

### Q4 FY2025 (13)

How should the private-cloud compute build be thought about from here?

- `apple.services.fact_capital_plan`: `capital_spend_amount`, `reserved_capacity_units`, `capex_project_id`, `compute_location_id`, `fiscal_quarter_id`
- `apple.services.dim_capex_project`: `project_type`, `project_name`
- `apple.services.dim_compute_location`: `location_code`
- `apple.services.fact_model_strategy`: `emphasis_share`, `model_source_id`, `fiscal_quarter_id`

### Q4 FY2025 (15)

Will the model strategy stay a mix of Apple's own models, partners, and possible acquisitions, or will one path dominate?

- `apple.services.fact_model_strategy`: `emphasis_share`, `dominant_path_flag`, `includes_acquisition_flag`, `model_source_id`, `fiscal_quarter_id`
- `apple.services.dim_model_source`: `source_code`, `source_name`

### Q4 FY2025 (17)

Will Apple change its mix of own and third-party data centers as others add capacity, and what role does M5 silicon play?

- `apple.services.fact_capital_plan`: `first_party_share`, `third_party_share`, `m5_in_data_center_flag`, `component_id`, `compute_location_id`, `fiscal_quarter_id`
- `apple.component.dim_component`: `component_code`, `component_name`
- `apple.services.dim_compute_location`: `location_code`
- `apple.supply.fact_custom_silicon`: `internal_content_share`, `component_id`

## Datasets

| Qualified name | Role | Questions served |
| --- | --- | --- |
| `apple.price.dim_currency` | dimension | join support |
| `apple.services.dim_service_family` | dimension | join support |
| `apple.services.dim_service_offering` | dimension | Q3 FY2026 (4), Q3 FY2026 (7), Q2 FY2026 (4), Q1 FY2026 (3), Q1 FY2026 (7), Q4 FY2025 (4) |
| `apple.services.dim_service_plan` | dimension | join support |
| `apple.services.dim_partner` | dimension | Q2 FY2026 (10), Q1 FY2026 (3) |
| `apple.services.dim_model_source` | dimension | Q2 FY2026 (6), Q2 FY2026 (10), Q4 FY2025 (15) |
| `apple.services.dim_compute_location` | dimension | Q3 FY2026 (9), Q1 FY2026 (11), Q4 FY2025 (13), Q4 FY2025 (17) |
| `apple.services.dim_capex_project` | dimension | Q4 FY2025 (13) |
| `apple.services.dim_opex_component` | dimension | Q4 FY2025 (9) |
| `apple.services.dim_stack_layer` | dimension | Q2 FY2026 (6) |
| `apple.price.fact_price_file` | fact | Q1 FY2026 (8) |
| `apple.price.fact_price_decision` | fact | Q1 FY2026 (8) |
| `apple.price.fact_product_margin` | fact | Q2 FY2026 (2), Q2 FY2026 (11), Q1 FY2026 (4) |
| `apple.price.fact_margin_bridge` | fact | Q2 FY2026 (2), Q2 FY2026 (11), Q1 FY2026 (4) |
| `apple.services.fact_services_growth` | fact | Q3 FY2026 (7), Q2 FY2026 (4), Q1 FY2026 (7), Q4 FY2025 (3) |
| `apple.services.fact_services_margin` | fact | Q2 FY2026 (9), Q1 FY2026 (4) |
| `apple.services.fact_ad_inventory` | fact | Q2 FY2026 (4) |
| `apple.services.fact_service_attachment` | fact | join support |
| `apple.services.fact_services_driver` | fact | Q1 FY2026 (7), Q4 FY2025 (4) |
| `apple.services.fact_partner_payment` | fact | Q4 FY2025 (3) |
| `apple.services.fact_partnership_economics` | fact | Q1 FY2026 (3) |
| `apple.services.fact_compute_economics` | fact | Q3 FY2026 (4), Q3 FY2026 (9), Q1 FY2026 (11) |
| `apple.services.fact_capital_plan` | fact | Q3 FY2026 (9), Q1 FY2026 (11), Q4 FY2025 (13), Q4 FY2025 (17) |
| `apple.services.fact_opex` | fact | Q1 FY2026 (1), Q4 FY2025 (9) |
| `apple.services.fact_ai_pnl` | fact | Q2 FY2026 (6), Q2 FY2026 (10), Q1 FY2026 (1) |
| `apple.services.fact_model_strategy` | fact | Q4 FY2025 (13), Q4 FY2025 (15) |
| `apple.services.fact_agent_stack` | fact | Q2 FY2026 (6) |
