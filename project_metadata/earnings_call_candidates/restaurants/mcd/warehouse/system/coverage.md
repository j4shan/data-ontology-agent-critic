# McDonald's restaurant system warehouse coverage

This slice is the McDonald's restaurant system: restaurants, franchisees, operators, ownership spells, development, remodels, kitchens, and supply commodities. Guest checks and the corporate ledger are outside this slice.

Amounts that use a currency, a calendar day, or an accounting period reference those populations. This slice does not hold their complete populations.

## Complete populations

| Identity | Dataset | Column |
| --- | --- | --- |
| `restaurant_identity` | `mcdonalds.restaurant.dim_restaurant` | `restaurant_id` |
| `franchisee_identity` | `mcdonalds.restaurant.dim_franchisee` | `franchisee_id` |
| `operator_identity` | `mcdonalds.restaurant.dim_operator` | `operator_id` |
| `ownership_spell_identity` | `mcdonalds.restaurant.fact_restaurant_ownership_spell` | `ownership_spell_id` |
| `development_project_identity` | `mcdonalds.development.dim_development_project` | `development_project_id` |
| `remodel_identity` | `mcdonalds.development.fact_restaurant_remodel` | `remodel_id` |
| `kitchen_asset_identity` | `mcdonalds.development.dim_kitchen_asset` | `kitchen_asset_id` |
| `supplier_identity` | `mcdonalds.supply.dim_supplier` | `supplier_id` |
| `commodity_identity` | `mcdonalds.supply.dim_commodity` | `commodity_id` |
| `distribution_center_identity` | `mcdonalds.supply.dim_distribution_center` | `distribution_center_id` |
| `country_identity` | `mcdonalds.organization.dim_country` | `country_id` |
| `segment_identity` | `mcdonalds.organization.dim_segment` | `segment_id` |

## Referenced populations

These identities are referenced and are not marked complete.

| Identity | Node | Column |
| --- | --- | --- |
| `calendar_day_identity` | `sf:mcdonalds.calendar.dim_calendar_day` | `calendar_day_id` |
| `accounting_period_identity` | `sf:mcdonalds.finance.dim_accounting_period` | `accounting_period_id` |
| `currency_identity` | `sf:mcdonalds.finance.dim_currency` | `currency_id` |

## Questions

### Q2 2026 (3)

Why franchisee participation in the value program was lower, and whether that was disagreement on the traffic driver or cost pressure.

| Dataset | Columns |
| --- | --- |
| `mcdonalds.restaurant.fact_value_program_participation` | `participation_status`, `opt_out_reason`, `offer_cost_amount`, `traffic_count`, `franchisee_id`, `restaurant_id`, `accounting_period_id`, `country_id`, `segment_id` |
| `mcdonalds.restaurant.fact_restaurant_period_performance` | `guest_count`, `restaurant_id`, `accounting_period_id` |
| `mcdonalds.restaurant.dim_franchisee` | `franchisee_id`, `franchisee_name` |
| `mcdonalds.supply.fact_commodity_cost` | `commodity_id`, `country_id`, `accounting_period_id`, `unit_cost_amount`, `cost_change_rate` |
| `mcdonalds.supply.dim_commodity` | `commodity_id`, `commodity_code` |

### Q2 2026 (4)

Whether company-operated restaurants outperform franchise restaurants on service, and what it takes to move weak stores to stronger operators.

| Dataset | Columns |
| --- | --- |
| `mcdonalds.restaurant.fact_restaurant_period_performance` | `service_score`, `ownership_type`, `operator_id`, `franchisee_id`, `restaurant_id`, `accounting_period_id` |
| `mcdonalds.restaurant.fact_restaurant_ownership_spell` | `ownership_type`, `operator_id`, `franchisee_id`, `restaurant_id`, `start_calendar_day_id`, `end_calendar_day_id` |
| `mcdonalds.restaurant.dim_operator` | `operator_id`, `operator_strength_tier`, `franchisee_id` |
| `mcdonalds.restaurant.fact_operator_reassignment` | `restaurant_id`, `from_operator_id`, `to_operator_id`, `from_operator_strength_tier`, `to_operator_strength_tier`, `calendar_day_id`, `service_score_before`, `service_score_after`, `reassignment_cost_amount` |
| `mcdonalds.restaurant.dim_restaurant` | `restaurant_id`, `country_id`, `segment_id` |

### Q2 2026 (5)

Whether a faster new-restaurant pace hurt same-store sales through cannibalization or by pulling resources off operations.

| Dataset | Columns |
| --- | --- |
| `mcdonalds.development.fact_restaurant_opening` | `restaurant_id`, `calendar_day_id`, `country_id`, `segment_id`, `cannibalizes_nearby_flag`, `nearby_comparable_sales_change_rate`, `cannibalized_guest_count`, `operations_hours_diverted` |
| `mcdonalds.restaurant.fact_restaurant_period_performance` | `comparable_sales_amount`, `comparable_sales_change_rate`, `same_store_guest_count`, `guest_count`, `operations_score`, `restaurant_id`, `accounting_period_id`, `country_id`, `segment_id` |
| `mcdonalds.development.fact_segment_development_result` | `segment_id`, `accounting_period_id`, `actual_opening_count`, `target_opening_count` |
| `mcdonalds.development.fact_development_capex` | `country_id`, `accounting_period_id`, `opening_count` |
| `mcdonalds.development.dim_development_project` | `development_project_id`, `project_type`, `country_id`, `segment_id` |
| `mcdonalds.organization.dim_country` | `country_id`, `country_name` |
| `mcdonalds.organization.dim_segment` | `segment_id`, `segment_code` |

### Q2 2026 (7)

Whether franchisees can fund operations, value, and experience work while cash flow is pressured.

| Dataset | Columns |
| --- | --- |
| `mcdonalds.restaurant.fact_franchisee_period_cash_flow` | `franchisee_id`, `country_id`, `segment_id`, `accounting_period_id`, `currency_id`, `operating_cash_flow_amount`, `franchisee_profit_amount`, `operations_funding_need_amount`, `value_funding_need_amount`, `experience_funding_need_amount`, `funding_shortfall_amount`, `company_support_amount` |
| `mcdonalds.development.fact_restaurant_remodel` | `franchisee_id`, `country_id`, `segment_id`, `experience_scope`, `franchisee_funded_amount`, `company_funded_amount`, `remodel_cost_amount` |
| `mcdonalds.supply.fact_commodity_cost` | `commodity_id`, `country_id`, `accounting_period_id`, `unit_cost_amount`, `cost_change_rate` |
| `mcdonalds.supply.dim_commodity` | `commodity_id`, `commodity_code`, `commodity_group` |
| `mcdonalds.restaurant.dim_franchisee` | `franchisee_id`, `franchisee_structure`, `segment_id` |

### Q1 2026 (4)

How large the opportunity is to refranchise company stores in the U.S. and international operated markets when franchise economics are better.

| Dataset | Columns |
| --- | --- |
| `mcdonalds.restaurant.fact_company_operated_period_margin` | `restaurant_id`, `country_id`, `segment_id`, `accounting_period_id`, `currency_id`, `ownership_type`, `company_operated_margin_amount`, `company_operated_margin_rate`, `sales_amount` |
| `mcdonalds.restaurant.fact_franchisee_period_cash_flow` | `franchisee_id`, `country_id`, `segment_id`, `accounting_period_id`, `currency_id`, `franchisee_profit_amount`, `franchisee_restaurant_margin_amount`, `average_restaurant_profit_amount`, `operated_restaurant_count` |
| `mcdonalds.restaurant.fact_restaurant_ownership_spell` | `restaurant_id`, `ownership_type`, `refranchise_flag`, `franchisee_id`, `country_id`, `segment_id`, `start_calendar_day_id`, `end_calendar_day_id`, `transfer_consideration_amount` |
| `mcdonalds.organization.dim_segment` | `segment_id`, `segment_code`, `segment_name` |
| `mcdonalds.organization.dim_country` | `country_id`, `country_name`, `segment_id` |
| `mcdonalds.restaurant.dim_restaurant` | `restaurant_id`, `country_id`, `segment_id` |
| `mcdonalds.restaurant.dim_franchisee` | `franchisee_id`, `segment_id`, `country_id` |

### Q1 2026 (5)

Whether U.S. and international development targets should change if stores are refranchised because margins are below the original plan.

| Dataset | Columns |
| --- | --- |
| `mcdonalds.development.fact_segment_development_result` | `segment_id`, `accounting_period_id`, `target_opening_count`, `actual_opening_count`, `plan_margin_rate`, `actual_margin_rate`, `refranchise_case_target_opening_count` |
| `mcdonalds.development.dim_development_project` | `development_project_id`, `project_type`, `segment_id`, `country_id`, `plan_margin_rate` |
| `mcdonalds.development.fact_restaurant_opening` | `development_project_id`, `segment_id`, `country_id`, `calendar_day_id`, `restaurant_id` |
| `mcdonalds.restaurant.fact_company_operated_period_margin` | `segment_id`, `country_id`, `accounting_period_id`, `company_operated_margin_amount`, `company_operated_margin_rate` |
| `mcdonalds.restaurant.fact_franchisee_period_cash_flow` | `segment_id`, `country_id`, `accounting_period_id`, `franchisee_profit_amount`, `average_restaurant_profit_amount` |
| `mcdonalds.restaurant.fact_restaurant_ownership_spell` | `ownership_type`, `refranchise_flag`, `segment_id`, `country_id` |
| `mcdonalds.organization.dim_segment` | `segment_id`, `segment_code` |

### Q1 2026 (13)

How higher build costs and supply-chain strain change the next U.S. remodel cycle, including company capital franchisees would need.

| Dataset | Columns |
| --- | --- |
| `mcdonalds.development.fact_restaurant_opening` | `restaurant_id`, `country_id`, `segment_id`, `build_cost_amount`, `currency_id`, `calendar_day_id` |
| `mcdonalds.development.fact_restaurant_remodel` | `remodel_id`, `restaurant_id`, `country_id`, `segment_id`, `experience_scope`, `funding_party`, `remodel_cost_amount`, `company_funded_amount`, `franchisee_funded_amount`, `currency_id` |
| `mcdonalds.development.fact_remodel_kitchen_equipment` | `remodel_id`, `kitchen_asset_id`, `equipment_cost_amount`, `company_funded_amount`, `franchisee_funded_amount` |
| `mcdonalds.development.fact_development_capex` | `country_id`, `segment_id`, `accounting_period_id`, `new_construction_capex_amount`, `remodel_capex_amount`, `kitchen_equipment_capex_amount`, `currency_id` |
| `mcdonalds.development.dim_development_project` | `development_project_id`, `project_type`, `country_id` |
| `mcdonalds.supply.fact_commodity_cost` | `commodity_id`, `country_id`, `accounting_period_id`, `unit_cost_amount`, `cost_change_rate` |
| `mcdonalds.supply.fact_supplier_shipment` | `supplier_id`, `distribution_center_id`, `commodity_id`, `country_id`, `accounting_period_id`, `shipped_quantity`, `received_quantity`, `shipped_cost_amount` |
| `mcdonalds.supply.dim_commodity` | `commodity_id`, `commodity_code` |
| `mcdonalds.supply.dim_supplier` | `supplier_id`, `supplier_name`, `country_id` |
| `mcdonalds.supply.dim_distribution_center` | `distribution_center_id`, `country_id`, `segment_id` |
| `mcdonalds.organization.dim_country` | `country_id`, `country_name` |

### Q1 2026 (16)

Whether developmental-license markets must deliver more of the path to 50,000 restaurants because U.S. and operated-market cash flow is tight.

| Dataset | Columns |
| --- | --- |
| `mcdonalds.development.fact_segment_development_result` | `segment_id`, `accounting_period_id`, `actual_opening_count`, `target_opening_count`, `ending_restaurant_count`, `system_goal_restaurant_count`, `remaining_openings_to_goal_count`, `segment_share_of_remaining_openings_rate`, `cash_funded_opening_capacity_count` |
| `mcdonalds.development.fact_restaurant_opening` | `segment_id`, `country_id`, `calendar_day_id`, `restaurant_id` |
| `mcdonalds.restaurant.fact_franchisee_period_cash_flow` | `segment_id`, `country_id`, `accounting_period_id`, `operating_cash_flow_amount`, `funding_shortfall_amount`, `franchisee_profit_amount` |
| `mcdonalds.restaurant.dim_franchisee` | `franchisee_id`, `franchisee_structure`, `segment_id` |
| `mcdonalds.organization.dim_segment` | `segment_id`, `segment_code` |
| `mcdonalds.organization.dim_country` | `country_id`, `country_name`, `segment_id` |

### Q4 2025 (4)

Whether higher capital expenditure is mostly faster new-store construction, and whether unit growth in slow-population markets is a share grab.

| Dataset | Columns |
| --- | --- |
| `mcdonalds.development.fact_development_capex` | `country_id`, `segment_id`, `accounting_period_id`, `currency_id`, `new_construction_capex_amount`, `remodel_capex_amount`, `kitchen_equipment_capex_amount`, `other_capex_amount`, `opening_count`, `market_share_rate`, `market_share_change_rate` |
| `mcdonalds.organization.dim_country` | `country_id`, `country_name`, `population_growth_band`, `segment_id` |
| `mcdonalds.development.fact_restaurant_opening` | `country_id`, `segment_id`, `calendar_day_id`, `restaurant_id`, `build_cost_amount` |
| `mcdonalds.development.fact_segment_development_result` | `segment_id`, `accounting_period_id`, `actual_opening_count`, `target_opening_count` |
| `mcdonalds.development.dim_development_project` | `development_project_id`, `project_type`, `country_id` |
| `mcdonalds.organization.dim_segment` | `segment_id`, `segment_code` |

### Q4 2025 (5)

Which kitchen equipment or layout changes are required for taste and quality, including an experience remodel.

| Dataset | Columns |
| --- | --- |
| `mcdonalds.development.dim_kitchen_asset` | `kitchen_asset_id`, `asset_name`, `equipment_family`, `layout_role`, `supports_taste_quality_flag`, `experience_program_flag`, `reference_country_id` |
| `mcdonalds.development.fact_remodel_kitchen_equipment` | `remodel_id`, `kitchen_asset_id`, `equipment_cost_amount`, `company_funded_amount`, `franchisee_funded_amount` |
| `mcdonalds.development.fact_restaurant_remodel` | `remodel_id`, `restaurant_id`, `country_id`, `segment_id`, `experience_scope`, `kitchen_equipment_change_flag`, `layout_change_flag`, `taste_quality_program_flag`, `remodel_cost_amount` |
| `mcdonalds.organization.dim_country` | `country_id`, `country_name` |
| `mcdonalds.restaurant.dim_restaurant` | `restaurant_id`, `country_id` |

### Q4 2025 (6)

Whether U.S. franchisees keep the value strategy after company financial support ends.

| Dataset | Columns |
| --- | --- |
| `mcdonalds.restaurant.fact_value_program_participation` | `franchisee_id`, `restaurant_id`, `country_id`, `segment_id`, `accounting_period_id`, `participation_status`, `continued_after_support_flag`, `company_support_amount` |
| `mcdonalds.restaurant.fact_value_strategy_coinvestment` | `country_id`, `segment_id`, `accounting_period_id`, `company_coinvestment_amount`, `support_in_force_flag`, `currency_id` |
| `mcdonalds.restaurant.fact_franchisee_period_cash_flow` | `franchisee_id`, `country_id`, `segment_id`, `accounting_period_id`, `franchisee_profit_amount`, `company_support_amount`, `value_funding_need_amount` |
| `mcdonalds.restaurant.dim_franchisee` | `franchisee_id`, `country_id`, `segment_id` |
| `mcdonalds.organization.dim_country` | `country_id`, `country_name` |
| `mcdonalds.organization.dim_segment` | `segment_id`, `segment_code` |

### Q3 2025 (2)

How large the company co-investment in the U.S. value strategy is, and what traffic or value-score result lets franchisees continue without that support.

| Dataset | Columns |
| --- | --- |
| `mcdonalds.restaurant.fact_value_strategy_coinvestment` | `country_id`, `segment_id`, `accounting_period_id`, `currency_id`, `company_coinvestment_amount`, `franchisee_investment_amount`, `observed_traffic_count`, `observed_value_score`, `continuation_traffic_threshold`, `continuation_value_score_threshold`, `support_in_force_flag` |
| `mcdonalds.restaurant.fact_restaurant_period_performance` | `restaurant_id`, `country_id`, `segment_id`, `accounting_period_id`, `guest_count`, `value_score` |
| `mcdonalds.restaurant.fact_value_program_participation` | `restaurant_id`, `franchisee_id`, `country_id`, `segment_id`, `traffic_count`, `company_support_amount`, `continued_after_support_flag` |
| `mcdonalds.restaurant.fact_franchisee_period_cash_flow` | `franchisee_id`, `country_id`, `segment_id`, `company_support_amount`, `franchisee_profit_amount` |
| `mcdonalds.organization.dim_country` | `country_id`, `country_name`, `segment_id` |
| `mcdonalds.organization.dim_segment` | `segment_id`, `segment_code` |

## Datasets and questions

| Dataset | Questions |
| --- | --- |
| `mcdonalds.development.dim_development_project` | Q2 2026 (5), Q1 2026 (5), Q1 2026 (13), Q4 2025 (4) |
| `mcdonalds.development.dim_kitchen_asset` | Q4 2025 (5) |
| `mcdonalds.development.fact_development_capex` | Q2 2026 (5), Q1 2026 (13), Q4 2025 (4) |
| `mcdonalds.development.fact_remodel_kitchen_equipment` | Q1 2026 (13), Q4 2025 (5) |
| `mcdonalds.development.fact_restaurant_opening` | Q2 2026 (5), Q1 2026 (5), Q1 2026 (13), Q1 2026 (16), Q4 2025 (4) |
| `mcdonalds.development.fact_restaurant_remodel` | Q2 2026 (7), Q1 2026 (13), Q4 2025 (5) |
| `mcdonalds.development.fact_segment_development_result` | Q2 2026 (5), Q1 2026 (5), Q1 2026 (16), Q4 2025 (4) |
| `mcdonalds.organization.dim_country` | Q2 2026 (5), Q1 2026 (4), Q1 2026 (13), Q1 2026 (16), Q4 2025 (4), Q4 2025 (5), Q4 2025 (6), Q3 2025 (2) |
| `mcdonalds.organization.dim_segment` | Q2 2026 (5), Q1 2026 (4), Q1 2026 (5), Q1 2026 (16), Q4 2025 (4), Q4 2025 (6), Q3 2025 (2) |
| `mcdonalds.restaurant.dim_franchisee` | Q2 2026 (3), Q2 2026 (7), Q1 2026 (4), Q1 2026 (16), Q4 2025 (6) |
| `mcdonalds.restaurant.dim_operator` | Q2 2026 (4) |
| `mcdonalds.restaurant.dim_restaurant` | Q2 2026 (4), Q1 2026 (4), Q4 2025 (5) |
| `mcdonalds.restaurant.fact_company_operated_period_margin` | Q1 2026 (4), Q1 2026 (5) |
| `mcdonalds.restaurant.fact_franchisee_period_cash_flow` | Q2 2026 (7), Q1 2026 (4), Q1 2026 (5), Q1 2026 (16), Q4 2025 (6), Q3 2025 (2) |
| `mcdonalds.restaurant.fact_operator_reassignment` | Q2 2026 (4) |
| `mcdonalds.restaurant.fact_restaurant_ownership_spell` | Q2 2026 (4), Q1 2026 (4), Q1 2026 (5) |
| `mcdonalds.restaurant.fact_restaurant_period_performance` | Q2 2026 (3), Q2 2026 (4), Q2 2026 (5), Q3 2025 (2) |
| `mcdonalds.restaurant.fact_value_program_participation` | Q2 2026 (3), Q4 2025 (6), Q3 2025 (2) |
| `mcdonalds.restaurant.fact_value_strategy_coinvestment` | Q4 2025 (6), Q3 2025 (2) |
| `mcdonalds.supply.dim_commodity` | Q2 2026 (3), Q2 2026 (7), Q1 2026 (13) |
| `mcdonalds.supply.dim_distribution_center` | Q1 2026 (13) |
| `mcdonalds.supply.dim_supplier` | Q1 2026 (13) |
| `mcdonalds.supply.fact_commodity_cost` | Q2 2026 (3), Q2 2026 (7), Q1 2026 (13) |
| `mcdonalds.supply.fact_supplier_shipment` | Q1 2026 (13) |
