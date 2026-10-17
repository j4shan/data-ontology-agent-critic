# Burger Inc finance and back-office coverage

This slice is the ledger, royalties, rent, company-operated restaurant P&L, capital, franchisee cash support, and segment consolidation. Guest checks and the restaurant master are owned outside this slice. Franchisee profit is owned with that system slice. This slice carries company-operated margin and the support paid to franchisees.

Foreign identities are referenced from finance rows and are partial here. Their complete populations are the datasets below, which this slice does not author:

| Identity | Column | Node |
| --- | --- | --- |
| `restaurant_identity` | `restaurant_id` | `sf:burger.restaurant.dim_restaurant` |
| `franchisee_identity` | `franchisee_id` | `sf:burger.restaurant.dim_franchisee` |
| `country_identity` | `country_id` | `sf:burger.organization.dim_country` |
| `segment_identity` | `segment_id` | `sf:burger.organization.dim_segment` |
| `commodity_identity` | `commodity_id` | `sf:burger.supply.dim_commodity` |

`segment_code` on the finance facts is the local filter for `us`, `international_operated`, and `developmental_license`. `commodity_group` on the commodity-cost fact is the local filter for `beef` and `energy`.

## Numbered questions

### Q1 2026 (6) — U.S. franchisee profits and company-operated margins

Company-operated margin for U.S. restaurants is `burger.finance.fact_company_store_pl.company_operated_margin_amount` with `segment_code = us`. The same margin at segment level is `burger.finance.fact_segment_consolidation.company_operated_margin_amount` with `segment_code = us`. `accounting_period_id` places the result in the quarter. Franchisee profit is read from the system slice, joined through `franchisee_id` and `restaurant_id`.

### Q1 2026 (7) — International operated franchisee profit, energy prices, and support

Energy cost and the forward outlook are `burger.finance.fact_commodity_cost.cost_change_amount` and `cost_outlook_amount` where `commodity_group = energy` and `segment_code = international_operated`. Whether a 2022-style window is open again is `burger.finance.fact_support_payment.support_amount` with `support_purpose = energy_cost_support`, bounded by `start_calendar_day_id` and `end_calendar_day_id` on `burger.calendar.dim_calendar_day`. Segment context is `burger.finance.fact_segment_consolidation` for `international_operated`. Amounts carry `currency_id`. Franchisee profit itself stays on the system slice.

### Q1 2026 (11) — U.S. company-operated margin: operations, value menu, and price

`burger.finance.fact_company_store_pl` holds `sales_amount`, `food_cost_amount`, `labor_cost_amount`, `company_operated_margin_amount`, `value_sales_amount`, and `value_mix_flag` for `segment_code = us`. `burger.finance.fact_company_store_cost.cost_amount` with `cost_element_id` and `value_menu_cost_flag` separates labor and occupancy operations cost from value-menu cost. `burger.finance.fact_margin_bridge_month` splits `inflation_effect_amount`, `mix_effect_amount`, and `price_effect_amount`, with `value_mix_effect_amount` kept apart from `beef_inflation_effect_amount` and `energy_inflation_effect_amount`. Pricing taken is `price_effect_amount`.

### Q4 2025 (2) — Meal discount, sharp price points, sales, and margin

On `burger.finance.fact_margin_bridge_month`, `meal_discount_sales_effect_amount` and `sharp_price_point_sales_effect_amount` compare the two offers on sales. `meal_discount_margin_effect_amount` and `sharp_price_point_margin_effect_amount` show whether either pressured company-operated margin. The level of that margin is `company_operated_margin_amount` on the bridge and on `burger.finance.fact_company_store_pl`. Company cash behind the value offer is `burger.finance.fact_support_payment.support_amount` where `support_purpose = value_coinvestment`. Guest-check lines for those offers are owned outside this slice.

### Q4 2025 (3) — Restaurant technology and value-driven margin pressure

`burger.finance.fact_margin_bridge_month.technology_offset_amount` is the labor or throughput margin recovered from restaurant technology, stored beside the meal-discount and sharp-price margin effects. Technology capital is `burger.finance.fact_capex.capital_spend_amount` and `capital_budget_amount` where `project_type = technology`, with the project classification on `burger.finance.dim_capex_project.project_type`. Labor cost is `burger.finance.fact_company_store_pl.labor_cost_amount` and `burger.finance.fact_company_store_cost.cost_amount` for the labor cost element.

### Q4 2025 (4) — Capital budget and new-restaurant construction

`burger.finance.fact_capex.capital_budget_amount` and `capital_spend_amount` by `project_type` (`new_restaurant`, `remodel`, `technology`) and `accounting_period_id` show whether the budget is concentrated in new restaurants and whether that spend is rising period to period. `burger.finance.dim_capex_project.project_type` is the project classification.

### Q3 2025 (1) — U.S. restaurant margin while the value gap widens

U.S. company-operated margin, value sales, and the value-mix flag are on `burger.finance.fact_company_store_pl` (`company_operated_margin_amount`, `value_sales_amount`, `value_mix_flag`, `segment_code = us`). The bridge columns `price_effect_amount`, `mix_effect_amount`, and `value_mix_effect_amount` show pricing and mix beside margin. Company co-investment in the value offer is `burger.finance.fact_support_payment.support_amount` with `support_purpose = value_coinvestment`. Competitor value scores are outside this finance slice.

### Q3 2025 (10) — Company-operated margin drop: inflation, value mix, and beef

`burger.finance.fact_margin_bridge_month.inflation_effect_amount` is general cost inflation. `value_mix_effect_amount` is the shift into lower-margin value. `beef_inflation_effect_amount` is the beef portion of inflation. The beef outlook is `burger.finance.fact_commodity_cost.cost_outlook_amount` where `commodity_group = beef`. The margin level is `company_operated_margin_amount` on `burger.finance.fact_company_store_pl`. `cost_element_id` on `burger.finance.fact_company_store_cost` keeps food cost apart from labor.

## Derived coverage

These topics are implied by the same calls and are not numbered questions on those calls.

### G&A

`burger.finance.fact_ga_expense.ga_amount` by `legal_entity_id`, `gl_account_id`, `cost_element_id`, `segment_code`, `accounting_period_id`, and `currency_id`. Consolidated G&A is `burger.finance.fact_segment_consolidation.ga_amount`. Accounts with `burger.finance.dim_gl_account.statement_line = general_admin` tie the amount to `burger.finance.fact_journal_line.signed_amount`.

### Royalty income

`burger.finance.fact_royalty_charge.royalty_income_amount` by `franchisee_id`, `restaurant_id`, `accounting_period_id`, `currency_id`, and `segment_code`. Consolidated royalty income is `burger.finance.fact_segment_consolidation.royalty_income_amount`. The chart line is `statement_line = franchise_royalty_income`. `journal_line_id` links a posted charge to the ledger.

### Rent income

`burger.finance.fact_rent_charge.rent_income_amount` by franchisee, restaurant, period, currency, and segment. Consolidated rent income is `burger.finance.fact_segment_consolidation.rent_income_amount`. The chart line is `statement_line = rent_income`. Company-operated occupancy stays on `occupancy_cost_amount` and is a different amount from franchisee rent income.

### Currency

`burger.finance.dim_currency` is the currency population. Daily translation is `burger.finance.fact_exchange_rate.rate_amount` for `from_currency_id`, `to_currency_id`, and `calendar_day_id`. Segment translation is `burger.finance.fact_segment_consolidation.local_currency_id`, `reporting_currency_id`, and `fx_rate_used`. Ledger lines carry `currency_id` and `signed_amount`.

### Segment consolidation

`burger.finance.fact_segment_consolidation` is one row per segment and accounting period for `us`, `international_operated`, and `developmental_license`. It carries consolidated `sales_amount`, `royalty_income_amount`, `rent_income_amount`, `ga_amount`, and `company_operated_margin_amount` in `reporting_currency_id`.

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `burger.calendar.dim_calendar_day` | Q1 2026 (7); derived: currency |
| `burger.finance.dim_accounting_period` | Q1 2026 (6), (7), (11); Q4 2025 (2), (3), (4); Q3 2025 (1), (10) |
| `burger.finance.dim_currency` | Q1 2026 (7); derived: currency |
| `burger.finance.dim_legal_entity` | derived: G&A, royalty, rent |
| `burger.finance.dim_gl_account` | derived: G&A, royalty, rent |
| `burger.finance.dim_cost_element` | Q1 2026 (11); Q4 2025 (3); Q3 2025 (10); derived: G&A |
| `burger.finance.fact_journal_line` | derived: G&A, royalty, rent, currency |
| `burger.finance.fact_ga_expense` | derived: G&A |
| `burger.finance.fact_exchange_rate` | derived: currency |
| `burger.finance.fact_company_store_pl` | Q1 2026 (6), (11); Q4 2025 (2); Q3 2025 (1), (10) |
| `burger.finance.fact_margin_bridge_month` | Q1 2026 (11); Q4 2025 (2), (3); Q3 2025 (1), (10) |
| `burger.finance.fact_company_store_cost` | Q1 2026 (11); Q4 2025 (3); Q3 2025 (10) |
| `burger.finance.fact_royalty_charge` | derived: royalty |
| `burger.finance.fact_rent_charge` | derived: rent |
| `burger.finance.fact_commodity_cost` | Q1 2026 (7); Q3 2025 (10) |
| `burger.finance.dim_capex_project` | Q4 2025 (3), (4) |
| `burger.finance.fact_capex` | Q4 2025 (3), (4) |
| `burger.finance.fact_support_payment` | Q1 2026 (7); Q4 2025 (2); Q3 2025 (1) |
| `burger.finance.fact_segment_consolidation` | Q1 2026 (6), (7); derived: consolidation, G&A, royalty, rent, currency |
