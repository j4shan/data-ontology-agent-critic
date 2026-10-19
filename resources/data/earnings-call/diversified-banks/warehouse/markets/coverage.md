# Bank Inc markets, wealth, capital, and expense

Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks. Demand quantity, supply or capacity, and price or margin are stored on separate facts joined by the shared grain keys (fiscal quarter, scenario, and the business keys).

## Numbered questions

## Bank of America

### Q2 2026 (2) Bank of America

How sustainable is the 200 to 300 basis points of operating leverage discussed in November once comparisons get harder, and what role does AI play?

- `bank.technology.fact_ai_spend`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `ai_spend_amount`
- `bank.technology.fact_ai_outcome`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `hours_saved_count`, `revenue_per_employee_amount`
- `bank.people.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `employee_group_id`, `headcount_count`

### Q2 2026 (7) Bank of America

If revenue runs hotter, will spending be pulled forward and reduce this year's operating leverage?

- `bank.expense.fact_expense`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `expense_category_id`, `expense_amount`
- `bank.segment.fact_segment_profit`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `pretax_income_amount`, `segment_revenue_amount`
- `bank.people.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `employee_group_id`, `headcount_count`

### Q2 2026 (9) Bank of America

Will the firm invest in lower-return businesses such as equities financing, below the 16% to 18% target, to support later earnings growth if banking and markets pipelines stay full?

- `bank.markets.fact_trading_revenue`: `fiscal_quarter_id`, `scenario_id`, `markets_desk_id`, `trading_revenue_amount`
- `bank.markets.fact_markets_balance`: `fiscal_quarter_id`, `scenario_id`, `markets_desk_id`, `markets_balance_amount`
- `bank.markets.fact_fee_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `fee_line_id`, `fee_revenue_amount`

### Q2 2026 (11) Bank of America

Are cards still on the path toward about 5% growth, why were net client flows softer, and is traditional commercial and industrial demand returning away from hyperscalers?

- `bank.wealth.fact_wealth_aum`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `aum_amount`
- `bank.wealth.fact_wealth_net_flow`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_flow_amount`
- `bank.wealth.fact_advisor_count`: `fiscal_quarter_id`, `scenario_id`, `employee_group_id`, `advisor_count`, `advisor_hires_count`

### Q1 2026 (3) Bank of America

Where is headcount being added or reduced, and where is AI in replacing attrition?

- `bank.technology.fact_ai_spend`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `ai_spend_amount`
- `bank.technology.fact_ai_outcome`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `hours_saved_count`, `revenue_per_employee_amount`
- `bank.people.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `employee_group_id`, `headcount_count`

### Q1 2026 (7) Bank of America

Why would Bank of America be a beneficiary of AI rather than a victim, including the effect on revenue per employee?

- `bank.technology.fact_ai_spend`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `ai_spend_amount`
- `bank.technology.fact_ai_outcome`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `hours_saved_count`, `revenue_per_employee_amount`
- `bank.people.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `employee_group_id`, `headcount_count`

### Q1 2026 (8) Bank of America

Five years out, do AI benefits show up as stickier relationships or as efficiency?

- `bank.technology.fact_ai_spend`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `ai_spend_amount`
- `bank.technology.fact_ai_outcome`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `hours_saved_count`, `revenue_per_employee_amount`
- `bank.people.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `employee_group_id`, `headcount_count`

### Q1 2026 (11) Bank of America

How does wealth recruiting and retention compare with the November acquisition targets?

- `bank.wealth.fact_wealth_aum`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `aum_amount`
- `bank.wealth.fact_wealth_net_flow`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_flow_amount`
- `bank.wealth.fact_advisor_count`: `fiscal_quarter_id`, `scenario_id`, `employee_group_id`, `advisor_count`, `advisor_hires_count`

### Q1 2026 (12) Bank of America

How should trading revenue and its mix grow over the near to medium term, and are commercial drawdowns since Middle East tensions defensive or normal?

- `bank.markets.fact_trading_revenue`: `fiscal_quarter_id`, `scenario_id`, `markets_desk_id`, `trading_revenue_amount`
- `bank.markets.fact_markets_balance`: `fiscal_quarter_id`, `scenario_id`, `markets_desk_id`, `markets_balance_amount`
- `bank.markets.fact_fee_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `fee_line_id`, `fee_revenue_amount`

### Q4 2025 (1) Bank of America

How does AI spend this year compare with last year, and what outcomes is that spend meant to produce?

- `bank.technology.fact_ai_spend`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `ai_spend_amount`
- `bank.technology.fact_ai_outcome`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `hours_saved_count`, `revenue_per_employee_amount`
- `bank.people.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `employee_group_id`, `headcount_count`

### Q4 2025 (9) Bank of America

If the stablecoin yield loophole is not closed, what happens to deposit trends?

- `bank.payments.fact_payments_volume`: `fiscal_quarter_id`, `scenario_id`, `bank_product_id`, `channel_id`, `payment_transaction_count`, `payment_volume_amount`
- `bank.deposit.fact_deposit_balance`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `deposit_product_id`, `customer_segment_id`, `deposit_balance_amount`, `average_deposit_balance_amount`
- `bank.markets.fact_fee_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `fee_line_id`, `fee_revenue_amount`

### Q2 2025 (3) Bank of America

Which regulatory costs are keeping expenses above the prior view, and what does sustainable expense growth look like after this year?

- `bank.expense.fact_expense`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `expense_category_id`, `expense_amount`
- `bank.segment.fact_segment_profit`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `pretax_income_amount`, `segment_revenue_amount`
- `bank.people.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `employee_group_id`, `headcount_count`

### Q2 2025 (4) Bank of America

Can the efficiency ratio get back under 60%, where it was before the pandemic, or has the business mix changed enough that the high 50s is a floor?

- `bank.expense.fact_expense`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `expense_category_id`, `expense_amount`
- `bank.segment.fact_segment_profit`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `pretax_income_amount`, `segment_revenue_amount`
- `bank.people.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `employee_group_id`, `headcount_count`

### Q2 2025 (5) Bank of America

How could stablecoin adoption affect payments revenue and deposits, and would banks respond as a consortium or one by one?

- `bank.payments.fact_payments_volume`: `fiscal_quarter_id`, `scenario_id`, `bank_product_id`, `channel_id`, `payment_transaction_count`, `payment_volume_amount`
- `bank.deposit.fact_deposit_balance`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `deposit_product_id`, `customer_segment_id`, `deposit_balance_amount`, `average_deposit_balance_amount`
- `bank.markets.fact_fee_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `fee_line_id`, `fee_revenue_amount`

## JPMorgan Chase

### Q2 2026 (3) JPMorgan Chase

Where is the firm in its investment cycle, and what does that imply for medium-term operating leverage?

- `bank.expense.fact_expense`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `expense_category_id`, `expense_amount`
- `bank.segment.fact_segment_profit`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `pretax_income_amount`, `segment_revenue_amount`
- `bank.people.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `employee_group_id`, `headcount_count`

### Q2 2026 (6) JPMorgan Chase

Over the next few years, can AI and technology slow expense growth enough to make operating leverage more likely?

- `bank.technology.fact_ai_spend`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `ai_spend_amount`
- `bank.technology.fact_ai_outcome`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `hours_saved_count`, `revenue_per_employee_amount`
- `bank.people.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `employee_group_id`, `headcount_count`

### Q2 2026 (7) JPMorgan Chase

Is the environment as good as it gets, or early-cycle because of AI investment, defense spending, and supply-chain shifts?

- `bank.technology.fact_ai_spend`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `ai_spend_amount`
- `bank.technology.fact_ai_outcome`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `hours_saved_count`, `revenue_per_employee_amount`
- `bank.people.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `employee_group_id`, `headcount_count`

### Q2 2026 (10) JPMorgan Chase

Is commercial-lending capex demand broadening beyond AI?

- `bank.technology.fact_ai_spend`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `ai_spend_amount`
- `bank.technology.fact_ai_outcome`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `hours_saved_count`, `revenue_per_employee_amount`
- `bank.people.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `employee_group_id`, `headcount_count`

### Q2 2026 (14) JPMorgan Chase

Besides revenue-related costs, are technology or marketing expenses being pulled forward inside the higher expense outlook?

- `bank.expense.fact_expense`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `expense_category_id`, `expense_amount`
- `bank.segment.fact_segment_profit`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `pretax_income_amount`, `segment_revenue_amount`
- `bank.people.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `employee_group_id`, `headcount_count`

### Q1 2026 (6) JPMorgan Chase

Was markets strength in March ordinary client activity or deployment of excess capital, and was any of it bad volatility?

- `bank.capital.fact_cet1_ratio`: `fiscal_quarter_id`, `scenario_id`, `cet1_ratio_percent`, `cet1_capital_amount`, `risk_weighted_asset_amount`
- `bank.capital.fact_tangible_book_value`: `fiscal_quarter_id`, `scenario_id`, `tangible_book_value_amount`, `tangible_book_value_per_share_amount`
- `bank.capital.fact_buyback`: `fiscal_quarter_id`, `scenario_id`, `buyback_amount`, `shares_repurchased_count`
- `bank.capital.fact_dividend`: `fiscal_quarter_id`, `scenario_id`, `dividend_amount`, `dividend_per_share_amount`

### Q1 2026 (10) JPMorgan Chase

Does AI extend the firm into businesses that were previously harder to assemble?

- `bank.technology.fact_ai_spend`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `ai_spend_amount`
- `bank.technology.fact_ai_outcome`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `hours_saved_count`, `revenue_per_employee_amount`
- `bank.people.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `employee_group_id`, `headcount_count`

### Q1 2026 (11) JPMorgan Chase

Why has trading stayed strong across shocks in commodities, rates, credit, and equities?

- `bank.markets.fact_trading_revenue`: `fiscal_quarter_id`, `scenario_id`, `markets_desk_id`, `trading_revenue_amount`
- `bank.markets.fact_markets_balance`: `fiscal_quarter_id`, `scenario_id`, `markets_desk_id`, `markets_balance_amount`
- `bank.markets.fact_fee_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `fee_line_id`, `fee_revenue_amount`

### Q1 2026 (15) JPMorgan Chase

Does the G-SIB surcharge limit how far the markets business can grow, and how does that enter capital allocation?

- `bank.capital.fact_cet1_ratio`: `fiscal_quarter_id`, `scenario_id`, `cet1_ratio_percent`, `cet1_capital_amount`, `risk_weighted_asset_amount`
- `bank.capital.fact_tangible_book_value`: `fiscal_quarter_id`, `scenario_id`, `tangible_book_value_amount`, `tangible_book_value_per_share_amount`
- `bank.capital.fact_buyback`: `fiscal_quarter_id`, `scenario_id`, `buyback_amount`, `shares_repurchased_count`
- `bank.capital.fact_dividend`: `fiscal_quarter_id`, `scenario_id`, `dividend_amount`, `dividend_per_share_amount`

### Q4 2025 (2) JPMorgan Chase

Which fee lines are expected to drive fee-revenue growth across the businesses?

- `bank.segment.fact_segment_profit`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `pretax_income_amount`, `segment_revenue_amount`
- `bank.markets.fact_fee_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `fee_line_id`, `fee_revenue_amount`
- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q4 2025 (6) JPMorgan Chase

Where is technology and AI spend going in 2026 versus last year, and what payoffs are expected?

- `bank.technology.fact_ai_spend`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `ai_spend_amount`
- `bank.technology.fact_ai_outcome`: `fiscal_quarter_id`, `scenario_id`, `ai_use_case_id`, `hours_saved_count`, `revenue_per_employee_amount`
- `bank.people.fact_headcount`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `employee_group_id`, `headcount_count`

### Q2 2025 (3) JPMorgan Chase

What is stopping banks from offering a joint deposit-like product, as with Zelle, before stablecoin firms offer a more convenient alternative?

- `bank.payments.fact_payments_volume`: `fiscal_quarter_id`, `scenario_id`, `bank_product_id`, `channel_id`, `payment_transaction_count`, `payment_volume_amount`
- `bank.deposit.fact_deposit_balance`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `deposit_product_id`, `customer_segment_id`, `deposit_balance_amount`, `average_deposit_balance_amount`
- `bank.markets.fact_fee_revenue`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `fee_line_id`, `fee_revenue_amount`

### Q2 2025 (7) JPMorgan Chase

If capital and liquidity rules were simplified, would that raise the natural return or be given back in client pricing?

- `bank.capital.fact_cet1_ratio`: `fiscal_quarter_id`, `scenario_id`, `cet1_ratio_percent`, `cet1_capital_amount`, `risk_weighted_asset_amount`
- `bank.capital.fact_tangible_book_value`: `fiscal_quarter_id`, `scenario_id`, `tangible_book_value_amount`, `tangible_book_value_per_share_amount`
- `bank.capital.fact_buyback`: `fiscal_quarter_id`, `scenario_id`, `buyback_amount`, `shares_repurchased_count`
- `bank.capital.fact_dividend`: `fiscal_quarter_id`, `scenario_id`, `dividend_amount`, `dividend_per_share_amount`
