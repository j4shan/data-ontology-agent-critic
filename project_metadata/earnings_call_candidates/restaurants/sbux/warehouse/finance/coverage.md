# Coffee Inc finance warehouse coverage

Finance and back-office datasets for Coffee Inc. Coffeehouses, transactions, and guest perception scores are owned outside this slice. Country, ownership type, and coffeehouse keys are partial foreign keys. Productivity rates and the guest value-perception score are foreign keys with no logical identity and no complete population here.

Coffee Inc fiscal periods live on `coffee.finance.dim_fiscal_period`. The fiscal year ends on the Sunday closest to September 30. Quarters are 13 weeks, and the fourth quarter is 14 weeks in a 53-week year. Periods follow a 4-4-5 week pattern. `fiscal_half_number` 1 is the first half. `fiscal_half_number` 2 is the second half. `fiscal_quarter_number` 4 is the fourth quarter.

## Dataset index

| Qualified name | Questions |
| --- | --- |
| `coffee.calendar.dim_calendar_day` | Q3 FY2026 (8), Q1 FY2026 (12) |
| `coffee.finance.dim_fiscal_period` | Q3 FY2026 (8), Q3 FY2026 (11), Q2 FY2026 (3), Q1 FY2026 (3), Q1 FY2026 (12), Q4 FY2025 (6), Q4 FY2025 (8) |
| `coffee.finance.dim_currency` | — |
| `coffee.finance.dim_legal_entity` | — |
| `coffee.finance.dim_gl_account` | — |
| `coffee.finance.fact_journal_line` | — |
| `coffee.finance.fact_exchange_rate` | — |
| `coffee.finance.dim_cost_element` | Q3 FY2026 (11), Q2 FY2026 (3), Q1 FY2026 (3), Q1 FY2026 (12), Q1 FY2026 (14), Q4 FY2025 (6) |
| `coffee.finance.dim_commodity` | Q1 FY2026 (12), Q4 FY2025 (6) |
| `coffee.finance.dim_tariff` | Q3 FY2026 (8) |
| `coffee.finance.fact_commodity_price_savings` | Q1 FY2026 (12), Q4 FY2025 (6) |
| `coffee.finance.fact_tariff_refund` | Q3 FY2026 (8) |
| `coffee.finance.fact_marketing_spend` | Q3 FY2026 (11), Q1 FY2026 (14) |
| `coffee.finance.fact_na_company_operated_operating_margin` | Q1 FY2026 (12) |
| `coffee.finance.fact_margin_bridge` | Q3 FY2026 (8), Q1 FY2026 (12), Q1 FY2026 (14) |
| `coffee.finance.dim_guidance_scenario` | Q1 FY2026 (4), Q1 FY2026 (8) |
| `coffee.finance.fact_guidance_scenario` | Q1 FY2026 (4), Q1 FY2026 (8) |
| `coffee.finance.fact_guidance_scenario_driver` | Q1 FY2026 (4) |
| `coffee.finance.fact_cost_savings_roadmap` | Q1 FY2026 (3), Q4 FY2025 (6) |
| `coffee.finance.fact_green_apron_cost_stage` | Q2 FY2026 (3) |
| `coffee.finance.fact_price_cost_plan` | Q1 FY2026 (12), Q4 FY2025 (8) |

Datasets with no question number are back-office only. That coverage is listed after the questions.

## Questions

### Q3 FY2026 (8) — tariff refunds in the fourth quarter, and whether guidance includes them

- `coffee.finance.fact_tariff_refund`
  - `refund_status_code` — `received` or `expected`
  - `received_fiscal_period_id` — Coffee Inc fiscal period the refund was received
  - `refund_amount`
  - `included_in_guidance_code` — `included` or `excluded`
  - `additional_refund_expected_code` — `expected` or `not_expected`
  - `expected_in_fourth_quarter_code` — `fourth_quarter` or `not_fourth_quarter`
  - `expected_fiscal_period_id` — period of a further refund
  - `tariff_id`
- `coffee.finance.dim_fiscal_period.fiscal_quarter_number` — quarter 4 is the fourth quarter, joined from `received_fiscal_period_id` and `expected_fiscal_period_id`
- `coffee.finance.dim_fiscal_period.period_start_calendar_day_id` and `period_end_calendar_day_id` — dates of those periods, joined to `coffee.calendar.dim_calendar_day`
- `coffee.finance.dim_tariff` — tariff program of the refund
- `coffee.finance.fact_margin_bridge`
  - `bridge_driver_code` = `tariff_refund`
  - `tariff_id`
  - `component_amount`
  - `margin_impact_amount`
  - `cost_element_id` is empty on a tariff-refund line, so the refund stays off coffee cost

### Q3 FY2026 (11) — marketing spend year over year, percent of sales, and media mix

- `coffee.finance.fact_marketing_spend`
  - `fiscal_period_id` and `prior_year_fiscal_period_id`
  - `marketing_spend_amount`
  - `prior_year_marketing_spend_amount`
  - `marketing_spend_yoy_change_amount`
  - `marketing_spend_pct_of_sales`
  - `prior_year_marketing_spend_pct_of_sales`
  - `media_channel_code`
  - `media_mix_pct`
  - `advertising_capacity_code` — `percent_of_sales_increase` or `media_mix_shift_only`
- `coffee.finance.dim_fiscal_period` — aligns the current period with its prior-year period
- `coffee.finance.dim_cost_element.cost_element_code` = `marketing` — marketing as a P&L cost element; spend dollars and mix are on the marketing-spend fact

### Q2 FY2026 (3) — Green Apron cost staging versus productivity

Finance owns the P&L staging. Productivity rates are a foreign key only.

- `coffee.finance.fact_green_apron_cost_stage`
  - `fiscal_period_id` — when the stage hits the P&L
  - `stage_name`
  - `staged_pnl_cost_amount`
  - `cumulative_staged_pnl_cost_amount`
  - `cost_element_id` — store labor
  - `productivity_rate_id` — foreign key, no logical identity, no complete population
- `coffee.finance.dim_fiscal_period.fiscal_period_in_year` and `fiscal_year` — order the stages through the year
- `coffee.finance.dim_cost_element.cost_element_code` = `store_labor`

### Q1 FY2026 (3) — cost opportunities this year versus later years

- `coffee.finance.fact_cost_savings_roadmap`
  - `opportunity_name`
  - `roadmap_fiscal_year` — the year the roadmap calls this year
  - `landing_horizon_code` — `this_year` or `later_years`
  - `landing_fiscal_year`
  - `first_recognition_fiscal_period_id`
  - `savings_amount`
  - `cost_element_id`
- `coffee.finance.dim_cost_element.cost_element_code` — which element the opportunity reduces
- `coffee.finance.dim_fiscal_period` — fiscal year and period of first recognition

### Q1 FY2026 (4) — scenarios that put fiscal 2026 earnings at the high end versus the low end

- `coffee.finance.dim_guidance_scenario`
  - `scenario_end_code` — `high_end` or `low_end`
  - `guidance_fiscal_year` — Coffee Inc fiscal year of the range
  - `scenario_name`
- `coffee.finance.fact_guidance_scenario.guided_earnings_amount` — earnings at that end
- `coffee.finance.fact_guidance_scenario_driver`
  - `driver_role_code` — `sales` or `cost`
  - `driver_code`
  - `driver_description`
  - `driver_amount`

### Q1 FY2026 (8) — room for more investment on top of annualizing the labor model

- `coffee.finance.fact_guidance_scenario`
  - `labor_model_annualization_cost_amount` — annualization already in the scenario
  - `incremental_investment_capacity_amount` — capacity still open above that annualization
  - `additional_investment_room_code` — `room_remains` or `no_room`
- `coffee.finance.dim_guidance_scenario.scenario_end_code` and `guidance_fiscal_year` — which end of the fiscal 2026 range the room belongs to

### Q1 FY2026 (12) — operating margin in the first half versus the second half, and when product and distribution inflation eases

- `coffee.finance.fact_na_company_operated_operating_margin`
  - `fiscal_period_id`
  - `country_id` and `ownership_type_id` — partial keys; rows are North America company-operated
  - `market_scope_code` = `north_america`
  - `operating_margin_amount`
  - `operating_margin_pct`
  - `net_revenue_amount`
- `coffee.finance.dim_fiscal_period.fiscal_half_number` — join `fiscal_period_id` and compare half 1 with half 2. Sum `country_id` within a half for the North America total. The half is an attribute of the fiscal period, so the fact grain stays the period.
- `coffee.calendar.dim_calendar_day` — dates of the period bounds used in that half comparison
- Product inflation by period: `coffee.finance.fact_commodity_price_savings.commodity_inflation_amount`, with `commodity_id`, `cost_element_id`, and `fiscal_period_id`
- `coffee.finance.dim_commodity.commodity_group_code` — `coffee` or `other`
- `coffee.finance.dim_cost_element.cost_element_code` — `coffee`, `other_product_cost`, and `distribution`
- Planned ease points: `coffee.finance.fact_price_cost_plan`
  - `planned_product_inflation_amount`
  - `planned_distribution_inflation_amount`
  - `product_inflation_ease_fiscal_period_id`
  - `distribution_inflation_ease_fiscal_period_id`
- Margin effect of those drivers: `coffee.finance.fact_margin_bridge.bridge_driver_code` `product_inflation` and `distribution`, with `component_amount` and `margin_impact_amount` by `fiscal_period_id`

### Q1 FY2026 (14) — permanent marketing rebase versus temporary turnaround spend in the North America margin decline

- `coffee.finance.fact_margin_bridge`
  - `market_scope_code` = `north_america`
  - `ownership_type_id` — company-operated
  - `fiscal_period_id`
  - `bridge_driver_code` — `marketing_permanent_rebase` or `marketing_temporary_turnaround`
  - `marketing_spend_nature_code` — `permanent_rebase` or `temporary_turnaround`
  - `cost_element_id` — marketing
  - `marketing_spend_id`
  - `component_amount`
  - `margin_impact_amount`
- `coffee.finance.fact_marketing_spend` — dollars, percent of sales, and media mix behind `marketing_spend_id`
- `coffee.finance.dim_cost_element.cost_element_code` = `marketing`

### Q4 FY2025 (6) — whether 2026 product-cost savings offset commodity inflation

- `coffee.finance.fact_commodity_price_savings`
  - `commodity_price_amount`
  - `commodity_inflation_amount`
  - `product_cost_savings_amount`
  - `net_savings_against_inflation_amount` — savings minus inflation for the same commodity, cost element, and period. A positive amount means savings offset inflation.
  - `fiscal_period_id` joined to `coffee.finance.dim_fiscal_period.fiscal_year` for fiscal 2026
  - `cost_element_id` — coffee and other product cost stay separate
- `coffee.finance.dim_commodity.commodity_group_code`
- `coffee.finance.dim_cost_element.cost_element_code` — `coffee` and `other_product_cost`
- `coffee.finance.fact_cost_savings_roadmap` — product-cost opportunities whose `landing_horizon_code` is `this_year` and whose `landing_fiscal_year` is 2026

### Q4 FY2025 (8) — how the price and cost plan responds for 2026, including whether comps build through the year

Finance owns the price and cost plan. The guest value-perception score stays outside this slice.

- `coffee.finance.fact_price_cost_plan`
  - `fiscal_period_id`
  - `planned_price_change_pct`
  - `planned_cost_change_pct`
  - `planned_comp_sales_pct`
  - `comps_build_through_year_code` — `builds_through_year` or `does_not_build_through_year`
  - `value_perception_score_id` — foreign key only, with no score column and no logical identity
- `coffee.finance.dim_fiscal_period.fiscal_period_in_year` and `fiscal_year` — the period sequence the comp build follows

## Back-office coverage beyond the numbered questions

These items are separate from the earnings-question map above.

### General and administrative

- `coffee.finance.dim_cost_element.cost_element_code` = `general_and_administrative`
- `coffee.finance.dim_gl_account.cost_element_id` — profit-and-loss accounts that map to that element (`financial_statement_section`)
- `coffee.finance.fact_journal_line.cost_element_id` and `signed_amount` — posted G&A
- `coffee.finance.fact_margin_bridge.bridge_driver_code` = `general_and_administrative`, with `cost_element_id`, `component_amount`, and `margin_impact_amount`

### Occupancy

- `coffee.finance.dim_cost_element.cost_element_code` = `occupancy`
- `coffee.finance.dim_gl_account.cost_element_id`
- `coffee.finance.fact_journal_line.cost_element_id` and `signed_amount`
- `coffee.finance.fact_margin_bridge.bridge_driver_code` = `occupancy`, with `cost_element_id`, `component_amount`, and `margin_impact_amount`

### Currency

- `coffee.finance.dim_currency` — complete currency population (`currency_id`, `currency_code`, `currency_name`)
- `coffee.finance.fact_exchange_rate` — `from_currency_id`, `to_currency_id`, `calendar_day_id`, `exchange_rate`
- `coffee.finance.dim_legal_entity.functional_currency_id` — currency of each legal entity's books
- `currency_id` on journal lines and on the amount facts denominates those measures

### Legal entity

- `coffee.finance.dim_legal_entity` — complete legal-entity population (`legal_entity_id`, `legal_entity_name`, `country_id`, `functional_currency_id`)
- `coffee.finance.fact_journal_line.legal_entity_id` — entity whose books hold the posting
