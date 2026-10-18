# Bank Inc markets, capital, and expense

This slice owns markets revenue, capital, fees, expenses, and AI outcomes. Deposit quantities, loan quantities, and net interest income live in the other slices and are partial when named here. A markets balance does not store the revenue, and a fee does not store the unit quantity.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `business_line_identity` | `business_line_id` | `sf:bank.customer.dim_business_line` `business_line_id` |
| `card_program_identity` | `card_program_id` | `sf:bank.credit.dim_card_program` `card_program_id` |
| `channel_identity` | `channel_id` | `sf:bank.customer.dim_channel` `channel_id` |
| `competitor_identity` | `competitor_id` | `sf:bank.customer.dim_competitor` `competitor_id` |
| `country_identity` | `country_id` | `sf:bank.geography.dim_country` `country_id` |
| `customer_segment_identity` | `customer_segment_id` | `sf:bank.customer.dim_customer_segment` `customer_segment_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:bank.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `rate_scenario_identity` | `rate_scenario_id` | `sf:bank.geography.dim_rate_scenario` `rate_scenario_id` |

## Numbered questions

## Bank of America

### Q2 2026 (2)

How sustainable is the 200 to 300 basis points of operating leverage discussed in November once comparisons get harder, and what role does AI play at Bank of America?

- `bank.markets.fact_operating_leverage`: `leverage_bps`, `sustainable_flag`, `comparison_harder_flag`
- `bank.markets.fact_ai_outcome`: `efficiency_flag`, `revenue_flag`
- `bank.markets.fact_ai_spend`: `spend_amount`

### Q2 2026 (7)

If revenue runs hotter, will spending be pulled forward and reduce this year's operating leverage at Bank of America?

- `bank.markets.fact_operating_leverage`: `reduced_by_spend_flag`, `leverage_bps`
- `bank.markets.fact_expense_actual`: `pulled_forward_flag`, `expense_amount`
- `bank.markets.fact_expense_guide`: `guide_amount`, `increase_amount`

### Q2 2026 (9)

Will Bank of America invest in lower-return businesses such as equities financing, below the 16% to 18% target, to support later earnings growth if banking and markets pipelines stay full?

- `bank.markets.fact_return_hurdle`: `target_low_rate`, `target_high_rate`, `below_hurdle_flag`, `invest_anyway_flag`
- `bank.markets.fact_lower_margin_capacity`: `capacity_amount`
- `bank.markets.fact_ib_pipeline`: `full_flag`, `pipeline_amount`
- `bank.markets.dim_markets_desk`: `desk_code`

### Q2 2026 (10)

Which areas drove the change in the operating-leverage outlook at Bank of America?

- `bank.markets.fact_operating_leverage`: `leverage_bps`
- `bank.markets.fact_expense_actual`: `expense_amount`, `growth_rate`
- `bank.customer.dim_business_line`: `line_code`
- `bank.markets.dim_expense_bucket`: `bucket_code`

### Q1 2026 (3)

Where is headcount being added or reduced, and where is AI in replacing attrition at Bank of America?

- `bank.markets.fact_headcount`: `headcount_quantity`, `direction_code`, `attrition_replaced_by_ai_flag`
- `bank.markets.fact_ai_outcome`: `efficiency_flag`
- `bank.markets.dim_ai_use_case`: `use_case_code`

### Q1 2026 (7)

Why would Bank of America be a beneficiary of AI rather than a victim, including the effect on revenue per employee?

- `bank.markets.fact_ai_outcome`: `revenue_flag`, `efficiency_flag`, `extends_franchise_flag`
- `bank.markets.fact_revenue_per_employee`: `revenue_per_employee_amount`
- `bank.markets.dim_ai_use_case`: `use_case_code`

### Q1 2026 (8)

Five years out, do AI benefits show up as stickier relationships or as efficiency at Bank of America?

- `bank.markets.fact_ai_outcome`: `stickier_relationship_flag`, `efficiency_flag`
- `bank.markets.fact_relationship_outcome`: `retention_index`, `stickier_flag`

### Q1 2026 (11)

How does wealth recruiting and retention compare with the November acquisition targets at Bank of America?

- `bank.markets.fact_wealth_advisor_flow`: `recruited_quantity`, `retained_quantity`, `versus_target_flag`
- `bank.markets.dim_advisor_cohort`: `cohort_code`

### Q1 2026 (12)

How should trading revenue and its mix grow over the near to medium term, and are commercial drawdowns since Middle East tensions defensive or normal at Bank of America?

- `bank.markets.fact_trading_mix`: `mix_share`, `medium_term_growth_rate`
- `bank.markets.fact_markets_revenue`: `revenue_amount`
- `bank.credit.fact_line_utilization`: `utilization_rate`, `defensive_draw_flag`

### Q4 2025 (1)

How does AI spend this year compare with last year, and what outcomes is that spend meant to produce at Bank of America?

- `bank.markets.fact_ai_spend`: `spend_amount`, `versus_prior_year_amount`
- `bank.markets.fact_ai_outcome`: `efficiency_flag`, `revenue_flag`
- `bank.markets.dim_expense_bucket`: `bucket_code`

### Q4 2025 (3)

What is the operating-leverage message for this year and the next three years underneath the return target, after the fee restatement at Bank of America?

- `bank.markets.fact_operating_leverage`: `leverage_bps`, `sustainable_flag`
- `bank.markets.fact_fee_revenue`: `fee_amount`, `growth_rate`
- `bank.markets.fact_efficiency_ratio`: `efficiency_rate`
- `bank.customer.dim_business_line`: `line_code`

### Q2 2025 (3)

Which regulatory costs are keeping expenses above the prior view, and what does sustainable expense growth look like after this year at Bank of America?

- `bank.markets.fact_regulatory_cost`: `cost_amount`, `above_prior_view_flag`
- `bank.markets.fact_expense_actual`: `expense_amount`, `growth_rate`
- `bank.markets.dim_regulatory_item`: `item_code`

### Q2 2025 (4)

Can the efficiency ratio get back under 60%, where it was before the pandemic, or has the business mix changed enough that the high 50s is a floor at Bank of America?

- `bank.markets.fact_efficiency_ratio`: `efficiency_rate`, `floor_rate`, `under_sixty_flag`
- `bank.customer.dim_business_line`: `line_code`

## JPMorgan Chase

### Q2 2026 (1)

How sustainable is the current risk-on stance across the businesses at JPMorgan Chase?

- `bank.markets.fact_risk_stance`: `risk_on_flag`, `sustainable_flag`
- `bank.markets.fact_client_activity`: `activity_index`, `risk_on_flag`
- `bank.markets.fact_markets_revenue`: `revenue_amount`, `sustainable_flag`
- `bank.markets.fact_ib_pipeline`: `pipeline_amount`, `full_flag`

### Q2 2026 (3)

Where is JPMorgan Chase in its investment cycle, and what does that imply for medium-term operating leverage?

- `bank.markets.fact_investment_cycle`: `stage_code`, `spend_still_ahead_flag`
- `bank.markets.fact_operating_leverage`: `leverage_bps`
- `bank.markets.fact_expense_actual`: `expense_amount`
- `bank.markets.dim_expense_bucket`: `bucket_code`

### Q2 2026 (6)

Over the next few years, can AI and technology slow expense growth enough to make operating leverage more likely at JPMorgan Chase?

- `bank.markets.fact_ai_outcome`: `efficiency_flag`
- `bank.markets.fact_expense_actual`: `growth_rate`, `expense_amount`
- `bank.markets.fact_operating_leverage`: `leverage_bps`, `sustainable_flag`

### Q2 2026 (7)

Is the environment as good as it gets, or early-cycle because of AI investment, defense spending, and supply-chain shifts at JPMorgan Chase?

- `bank.markets.fact_client_activity`: `early_cycle_flag`, `activity_index`
- `bank.markets.dim_investment_theme`: `theme_code`
- `bank.credit.fact_loan_purpose_mix`: `mix_share`
- `bank.credit.dim_borrower_purpose`: `purpose_code`

### Q2 2026 (9)

Which products or geographies were unusually strong this quarter and may be hard to sustain at JPMorgan Chase?

- `bank.markets.fact_markets_standout`: `standout_flag`, `hard_to_sustain_flag`
- `bank.geography.dim_country`: `country_code`
- `bank.markets.dim_markets_desk`: `desk_code`

### Q2 2026 (14)

Besides revenue-related costs, are technology or marketing expenses being pulled forward inside the higher expense outlook at JPMorgan Chase?

- `bank.markets.fact_expense_actual`: `pulled_forward_flag`, `expense_amount`
- `bank.markets.fact_expense_guide`: `increase_amount`, `guide_amount`
- `bank.markets.dim_expense_bucket`: `bucket_code`

### Q2 2026 (15)

Is markets balance-sheet allocation at a peak, or can more be allocated if activity stays high at JPMorgan Chase?

- `bank.markets.fact_markets_balance`: `allocated_amount`, `at_peak_flag`, `limit_headroom_amount`
- `bank.markets.fact_rwa_usage`: `rwa_amount`
- `bank.markets.dim_capital_constraint`: `constraint_code`

### Q1 2026 (6)

Was markets strength in March ordinary client activity or deployment of excess capital, and was any of it bad volatility at JPMorgan Chase?

- `bank.markets.fact_markets_revenue`: `revenue_amount`, `ordinary_client_flag`
- `bank.markets.dim_activity_driver`: `driver_code`
- `bank.markets.fact_markets_balance`: `allocated_amount`

### Q1 2026 (10)

Does AI extend JPMorgan Chase into businesses that were previously harder to assemble?

- `bank.markets.fact_ai_outcome`: `extends_franchise_flag`
- `bank.markets.dim_ai_use_case`: `use_case_code`, `use_case_name`

### Q1 2026 (11)

Why has trading stayed strong across shocks in commodities, rates, credit, and equities at JPMorgan Chase?

- `bank.markets.fact_markets_revenue`: `revenue_amount`, `sustainable_flag`
- `bank.markets.fact_client_activity`: `activity_index`
- `bank.markets.dim_markets_desk`: `desk_code`

### Q1 2026 (14)

Has any investment-banking pipeline been paused or pushed out at JPMorgan Chase?

- `bank.markets.fact_ib_pipeline`: `pipeline_amount`, `paused_flag`, `pushed_out_flag`
- `bank.markets.dim_ib_product`: `product_code`

### Q1 2026 (15)

Does the G-SIB surcharge limit how far the markets business can grow, and how does that enter capital allocation at JPMorgan Chase?

- `bank.markets.fact_gsib_surcharge`: `surcharge_bps`, `limits_growth_flag`
- `bank.markets.fact_capital_allocation`: `allocated_amount`, `decision_code`
- `bank.markets.dim_capital_constraint`: `constraint_code`

### Q4 2025 (2)

Which fee lines are expected to drive fee-revenue growth across the businesses at JPMorgan Chase?

- `bank.markets.fact_fee_revenue`: `fee_amount`, `growth_rate`
- `bank.markets.dim_fee_line`: `fee_code`
- `bank.customer.dim_business_line`: `line_code`

### Q4 2025 (6)

Where is technology and AI spend going in 2026 versus last year, and what payoffs are expected at JPMorgan Chase?

- `bank.markets.fact_ai_spend`: `spend_amount`, `versus_prior_year_amount`
- `bank.markets.fact_expense_actual`: `expense_amount`
- `bank.markets.dim_expense_bucket`: `bucket_code`
- `bank.markets.fact_ai_outcome`: `efficiency_flag`, `revenue_flag`

### Q2 2025 (2)

Did the open-banking hold period change pricing for fintech relationships at JPMorgan Chase?

- `bank.markets.fact_open_banking_price`: `fee_rate`, `changed_after_hold_flag`
- `bank.customer.dim_channel`: `channel_code`
- `bank.markets.dim_fee_line`: `fee_code`

### Q2 2025 (7)

If capital and liquidity rules were simplified, would that raise the natural return or be given back in client pricing at JPMorgan Chase?

- `bank.markets.fact_capital_relief`: `relief_flag`, `kept_in_return_flag`, `given_back_in_price_flag`
- `bank.markets.fact_return_hurdle`: `target_low_rate`, `target_high_rate`

### Q2 2025 (8)

Have tariff and tax uncertainties that froze client activity in the spring cleared enough for second-half activity to continue at JPMorgan Chase?

- `bank.markets.fact_tariff_pause`: `frozen_flag`, `cleared_flag`
- `bank.markets.fact_client_activity`: `activity_index`
- `bank.markets.dim_ib_product`: `product_code`

### Q2 2025 (10)

Is growth in lower-margin areas a supply issue or a demand issue if leverage rules loosen at JPMorgan Chase?

- `bank.markets.fact_lower_margin_capacity`: `demand_limited_flag`, `supply_limited_flag`, `capacity_amount`
- `bank.markets.dim_capital_constraint`: `constraint_code`

### Q2 2025 (11)

How are customers responding to the Sapphire price changes, and how does that sit in the card competitive set at JPMorgan Chase?

- `bank.markets.fact_sapphire_price`: `annual_fee_amount`, `response_code`
- `bank.credit.dim_card_program`: `program_code`
- `bank.customer.dim_competitor`: `competitor_code`

### Q2 2025 (12)

How much of markets strength was the environment versus balance-sheet use, and has the environment calmed at JPMorgan Chase?

- `bank.markets.fact_environment_contribution`: `environment_share`, `balance_sheet_share`, `calmed_flag`
- `bank.markets.fact_markets_balance`: `allocated_amount`
- `bank.markets.fact_markets_revenue`: `revenue_amount`
