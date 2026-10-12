# Device Inc demand and device family

This slice owns device family, generation, SKU, channel, geography, calendar, and the demand facts. Demand quantity, sell-through, the installed base, and the upgrade program live here. Shipments, memory and silicon supply, the device price file, and service attachment are owned in the other slices. A demand row names those populations only as a partial identity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `component_commodity_identity` | `component_commodity_id` | `sf:device.component.dim_component_commodity` `component_commodity_id` |

## Numbered questions

### Q3 FY2026 (1)

How much of the guided growth slowdown is supply constraint versus currency, and which constraints are spreading?

- `device.demand.fact_guided_growth`: `guided_growth_rate`, `prior_period_growth_rate`, `supply_constraint_effect_amount`, `fx_effect_amount`, `fiscal_quarter_id`, `comparison_quarter_code`
- `device.supply.fact_constraint_spread`: `spreading_flag`, `versus_prior_quarter_code`, `component_commodity_id`, `device_family_id`, `fiscal_quarter_id`
- `device.component.dim_component_commodity`: `commodity_code`, `commodity_name`
- `device.geography.dim_fiscal_quarter`: `quarter_code`, `quarter_label`

### Q3 FY2026 (3)

What adoption is expected for the Apple Upgrade Program across the installed base, and does it shorten replacement for iPhone only or also Mac and iPad?

- `device.demand.fact_upgrade_program`: `adoption_rate`, `replacement_interval_months`, `shortens_replacement_flag`, `device_family_id`, `country_id`, `fiscal_quarter_id`
- `device.demand.fact_installed_base`: `installed_quantity`, `device_family_id`, `country_id`
- `device.product.dim_device_family`: `family_code`

### Q3 FY2026 (8)

Which new markets open as more AI runs on the device?

- `device.demand.fact_on_device_market`: `use_case_name`, `new_market_flag`, `in_current_product_set_flag`, `feature_id`, `device_family_id`, `fiscal_quarter_id`
- `device.product.dim_feature`: `feature_code`
- `device.product.dim_device_family`: `family_code`
- `device.services.dim_compute_location`: `location_code`

### Q2 FY2026 (1)

Do agents imply a new phone form factor or new products, or do they sit on the current iPhone?

- `device.demand.fact_agent_hardware`: `sits_on_current_iphone_flag`, `requires_new_form_factor_flag`, `requires_new_product_flag`, `form_factor_id`, `device_family_id`, `feature_id`, `fiscal_quarter_id`
- `device.product.dim_form_factor`: `form_factor_code`
- `device.product.dim_device_family`: `family_code`

### Q2 FY2026 (3)

Which new segments — education, value, or emerging markets — is MacBook Neo reaching, and how does the roadmap address other underpenetrated markets?

- `device.demand.fact_segment_penetration`: `mix_share`, `penetration_rate`, `roadmap_addresses_flag`, `customer_segment_id`, `product_generation_id`, `device_family_id`, `country_id`, `fiscal_quarter_id`
- `device.product.dim_customer_segment`: `segment_code`
- `device.product.dim_product_generation`: `generation_code`
- `device.geography.dim_country`: `country_code`, `region_id`

### Q2 FY2026 (5)

In this memory dislocation, is the priority share at the low end where competitors are strained, or profitability?

- `device.demand.fact_competitive_position`: `priority_code`, `low_end_focus_flag`, `competitor_constraint_index`, `share_change_rate`, `device_family_id`, `country_id`, `fiscal_quarter_id`
- `device.supply.fact_component_cost`: `dislocated_flag`, `inflation_rate`, `component_commodity_id`
- `device.price.fact_price_decision`: `used_price_lever_flag`, `lever_reason_code`, `device_family_id`
- `device.price.fact_product_margin`: `product_gross_margin_rate`, `fiscal_quarter_id`

### Q2 FY2026 (7)

What is sustaining iPhone growth above 20% despite supply limits, and how durable is it?

- `device.demand.fact_iphone_driver`: `growth_rate`, `above_twenty_percent_flag`, `durable_flag`, `contribution_amount`, `demand_driver_id`, `device_family_id`, `fiscal_quarter_id`
- `device.demand.fact_unmet_demand`: `constrained_revenue_amount`, `still_constrained_at_exit_flag`, `device_family_id`, `fiscal_quarter_id`
- `device.product.dim_demand_driver`: `driver_code`
- `device.supply.fact_constraint_spread`: `spreading_flag`, `component_commodity_id`, `device_family_id`

### Q2 FY2026 (12)

In China, is Apple gaining because competitors are more supply-constrained, and how is the India iPhone opportunity evolving with the installed base and a larger middle class?

- `device.demand.fact_competitive_position`: `share_change_rate`, `competitor_constraint_index`, `country_id`, `device_family_id`, `fiscal_quarter_id`
- `device.demand.fact_regional_outlook`: `middle_class_tailwind_flag`, `installed_base_opportunity_quantity`, `demand_direction`, `country_id`, `device_family_id`
- `device.demand.fact_installed_base`: `installed_quantity`, `country_id`, `device_family_id`
- `device.demand.fact_sell_through`: `sell_through_quantity`, `country_id`, `channel_id`, `device_family_id`
- `device.geography.dim_country`: `country_code`

### Q1 FY2026 (2)

Which one or two factors are driving iPhone strength, and how sustainable are they?

- `device.demand.fact_iphone_driver`: `contribution_amount`, `durable_flag`, `demand_driver_id`, `device_family_id`, `fiscal_quarter_id`, `growth_rate`
- `device.product.dim_demand_driver`: `driver_name`, `driver_code`
- `device.product.dim_device_family`: `family_code`

### Q1 FY2026 (5)

How is overall smartphone demand holding up as memory prices rise, given worries about shortages and demand destruction?

- `device.demand.fact_industry_smartphone_demand`: `industry_demand_index`, `demand_destruction_flag`, `component_commodity_id`, `country_id`, `fiscal_quarter_id`
- `device.supply.fact_component_cost`: `inflation_rate`, `cost_change_amount`, `component_commodity_id`
- `device.supply.fact_constraint_spread`: `spreading_flag`, `versus_prior_quarter_code`, `component_commodity_id`
- `device.component.dim_component_commodity`: `commodity_code`

### Q1 FY2026 (9)

What is driving iPhone traction in India, and how large is the remaining installed-base opportunity?

- `device.demand.fact_regional_outlook`: `demand_direction`, `installed_base_opportunity_quantity`, `middle_class_tailwind_flag`, `country_id`, `device_family_id`, `fiscal_quarter_id`
- `device.demand.fact_sell_through`: `sell_through_quantity`, `country_id`, `channel_id`, `device_family_id`, `calendar_day_id`
- `device.demand.fact_installed_base`: `installed_quantity`, `country_id`, `device_family_id`
- `device.geography.dim_country`: `country_code`

### Q1 FY2026 (12)

What share of the active iPhone or device base can run Apple Intelligence, and is that why broader AI services are launching gradually?

- `device.demand.fact_installed_base`: `ai_capable_quantity`, `ai_capable_share`, `installed_quantity`, `device_family_id`, `country_id`, `calendar_day_id`
- `device.services.fact_services_driver`: `driver_code`, `contribution_amount`, `fiscal_quarter_id`
- `device.product.dim_feature`: `feature_code`
- `device.product.dim_device_family`: `family_code`

### Q4 FY2025 (1)

Is iPhone 17 strength mainly an aging installed base replacing phones, or specific features versus prior cycles?

- `device.demand.fact_replacement_cycle`: `upgrade_pool_share`, `feature_driven_share`, `prior_cycle_feature_share`, `product_generation_id`, `device_family_id`, `country_id`, `fiscal_quarter_id`
- `device.demand.fact_installed_base`: `aging_base_share`, `installed_quantity`, `device_family_id`
- `device.product.dim_product_generation`: `generation_code`

### Q4 FY2025 (2)

How should iPhone in China trend in the December quarter, and has that region turned?

- `device.demand.fact_regional_outlook`: `demand_direction`, `december_driver_code`, `country_id`, `device_family_id`, `fiscal_quarter_id`
- `device.geography.dim_country`: `country_code`, `region_id`
- `device.geography.dim_region`: `region_code`
- `device.geography.dim_fiscal_quarter`: `quarter_code`
- `device.product.dim_device_family`: `family_code`

### Q4 FY2025 (5)

Are iPhone buyers shifting between upgraders and switchers, are U.S. carrier promotions helping, and where is channel inventory?

- `device.demand.fact_buyer_mix`: `upgrader_quantity`, `switcher_quantity`, `carrier_promotion_id`, `channel_id`, `country_id`, `device_family_id`, `calendar_day_id`
- `device.channel.dim_carrier_promotion`: `promotion_name`, `channel_id`
- `device.supply.fact_channel_inventory`: `on_hand_quantity`, `channel_id`, `country_id`, `device_family_id`, `calendar_day_id`
- `device.demand.fact_sell_through`: `sell_through_quantity`, `channel_id`, `country_id`, `device_family_id`
- `device.geography.dim_country`: `country_code`

### Q4 FY2025 (6)

Was September weakness in China a pause until iPhone Air arrived, and what else lifts the December view there?

- `device.demand.fact_regional_outlook`: `pause_until_generation_flag`, `december_driver_code`, `demand_direction`, `product_generation_id`, `country_id`, `device_family_id`, `fiscal_quarter_id`
- `device.product.dim_product_generation`: `generation_code`
- `device.geography.dim_country`: `country_code`
- `device.geography.dim_fiscal_quarter`: `quarter_code`

### Q4 FY2025 (7)

Will iPhone supply still be constrained exiting December, and how much revenue did constraints hold back this quarter?

- `device.demand.fact_unmet_demand`: `constrained_revenue_amount`, `still_constrained_at_exit_flag`, `device_family_id`, `fiscal_quarter_id`
- `device.demand.fact_device_demand`: `demand_quantity`, `device_family_id`, `channel_id`, `country_id`, `calendar_day_id`
- `device.supply.fact_device_shipment`: `shipment_quantity`, `device_family_id`, `channel_id`, `country_id`, `calendar_day_id`
- `device.supply.fact_constraint_spread`: `spreading_flag`, `component_commodity_id`, `device_family_id`
- `device.product.dim_device_family`: `family_code`

### Q4 FY2025 (8)

How much of the China momentum is smartphone subsidies, and what share of buyers is using them?

- `device.demand.fact_subsidy_uptake`: `buyer_share_using_subsidy`, `subsidy_attributed_demand_quantity`, `underlying_demand_quantity`, `country_id`, `device_family_id`, `fiscal_quarter_id`
- `device.demand.fact_sell_through`: `sell_through_quantity`, `country_id`, `device_family_id`
- `device.geography.dim_country`: `country_code`

### Q4 FY2025 (11)

How should holiday attach of other products to iPhone be read given where consumer budgets are?

- `device.demand.fact_product_attach`: `attach_rate`, `wallet_pressure_index`, `holiday_flag`, `device_family_id`, `attached_family_code`, `country_id`, `fiscal_quarter_id`
- `device.product.dim_device_family`: `family_code`
- `device.price.fact_price_file`: `unit_price`, `device_family_id`, `channel_id`, `country_id`, `calendar_day_id`

### Q4 FY2025 (12)

Has iPhone 17 mix shifted between Pro and Pro Max versus prior cycles?

- `device.demand.fact_generation_mix`: `mix_share`, `prior_cycle_mix_share`, `product_generation_id`, `device_family_id`, `fiscal_quarter_id`
- `device.product.dim_product_generation`: `generation_code`
- `device.product.dim_device_family`: `family_code`

### Q4 FY2025 (14)

Does iPhone Air reception say anything about demand for a foldable, or are those form factors different?

- `device.demand.fact_generation_mix`: `mix_share`, `same_demand_as_other_form_flag`, `form_factor_id`, `product_generation_id`, `device_family_id`, `fiscal_quarter_id`
- `device.product.dim_form_factor`: `form_factor_code`
- `device.product.dim_product_generation`: `generation_code`
- `device.demand.fact_device_demand`: `demand_quantity`, `device_family_id`, `channel_id`, `country_id`, `calendar_day_id`

### Q4 FY2025 (16)

Are AI features actually swaying purchases, or are record sales still about iOS retention and other factors?

- `device.demand.fact_purchase_reason`: `reason_code`, `purchase_share`, `sways_purchase_flag`, `feature_id`, `device_family_id`, `country_id`, `fiscal_quarter_id`
- `device.demand.fact_sell_through`: `sell_through_quantity`, `device_family_id`, `channel_id`, `country_id`
- `device.product.dim_feature`: `feature_code`
- `device.product.dim_device_family`: `family_code`

## Datasets

| Qualified name | Role | Questions served |
| --- | --- | --- |
| `device.geography.dim_region` | dimension | Q4 FY2025 (2) |
| `device.geography.dim_fiscal_quarter` | dimension | Q3 FY2026 (1), Q4 FY2025 (2), Q4 FY2025 (6) |
| `device.geography.dim_country` | dimension | Q2 FY2026 (3), Q2 FY2026 (12), Q1 FY2026 (9), Q4 FY2025 (2), Q4 FY2025 (5), Q4 FY2025 (6), Q4 FY2025 (8) |
| `device.geography.dim_calendar_day` | dimension | join support |
| `device.channel.dim_channel` | dimension | join support |
| `device.channel.dim_carrier_promotion` | dimension | Q4 FY2025 (5) |
| `device.product.dim_device_family` | dimension | Q3 FY2026 (3), Q3 FY2026 (8), Q2 FY2026 (1), Q1 FY2026 (2), Q1 FY2026 (12), Q4 FY2025 (2), Q4 FY2025 (7), Q4 FY2025 (11), Q4 FY2025 (12), Q4 FY2025 (16) |
| `device.product.dim_form_factor` | dimension | Q2 FY2026 (1), Q4 FY2025 (14) |
| `device.product.dim_customer_segment` | dimension | Q2 FY2026 (3) |
| `device.product.dim_feature` | dimension | Q3 FY2026 (8), Q1 FY2026 (12), Q4 FY2025 (16) |
| `device.product.dim_demand_driver` | dimension | Q2 FY2026 (7), Q1 FY2026 (2) |
| `device.product.dim_product_generation` | dimension | Q2 FY2026 (3), Q4 FY2025 (1), Q4 FY2025 (6), Q4 FY2025 (12), Q4 FY2025 (14) |
| `device.product.dim_sku` | dimension | join support |
| `device.demand.fact_guided_growth` | fact | Q3 FY2026 (1) |
| `device.demand.fact_device_demand` | fact | Q4 FY2025 (7), Q4 FY2025 (14) |
| `device.demand.fact_sell_through` | fact | Q2 FY2026 (12), Q1 FY2026 (9), Q4 FY2025 (5), Q4 FY2025 (8), Q4 FY2025 (16) |
| `device.demand.fact_installed_base` | fact | Q3 FY2026 (3), Q2 FY2026 (12), Q1 FY2026 (9), Q1 FY2026 (12), Q4 FY2025 (1) |
| `device.demand.fact_upgrade_program` | fact | Q3 FY2026 (3) |
| `device.demand.fact_replacement_cycle` | fact | Q4 FY2025 (1) |
| `device.demand.fact_buyer_mix` | fact | Q4 FY2025 (5) |
| `device.demand.fact_unmet_demand` | fact | Q2 FY2026 (7), Q4 FY2025 (7) |
| `device.demand.fact_iphone_driver` | fact | Q2 FY2026 (7), Q1 FY2026 (2) |
| `device.demand.fact_segment_penetration` | fact | Q2 FY2026 (3) |
| `device.demand.fact_competitive_position` | fact | Q2 FY2026 (5), Q2 FY2026 (12) |
| `device.demand.fact_regional_outlook` | fact | Q2 FY2026 (12), Q1 FY2026 (9), Q4 FY2025 (2), Q4 FY2025 (6) |
| `device.demand.fact_subsidy_uptake` | fact | Q4 FY2025 (8) |
| `device.demand.fact_on_device_market` | fact | Q3 FY2026 (8) |
| `device.demand.fact_agent_hardware` | fact | Q2 FY2026 (1) |
| `device.demand.fact_purchase_reason` | fact | Q4 FY2025 (16) |
| `device.demand.fact_product_attach` | fact | Q4 FY2025 (11) |
| `device.demand.fact_generation_mix` | fact | Q4 FY2025 (12), Q4 FY2025 (14) |
| `device.demand.fact_industry_smartphone_demand` | fact | Q1 FY2026 (5) |
| `device.demand.fact_feature_demand` | fact | join support |
