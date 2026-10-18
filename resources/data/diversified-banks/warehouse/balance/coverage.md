# Bank Inc balance sheet, deposits, and net interest income

Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks. Demand quantity, supply or capacity, and price or margin are stored on separate facts joined by the shared grain keys (fiscal quarter, scenario, and the business keys).

## Numbered questions

## Bank of America

### Q2 2026 (1) Bank of America

How does deposit pricing behave in a higher-for-longer setting after this quarter's pricing beat peers while the full-year net-interest-income guide was left unchanged?

- `bank.deposit.fact_deposit_price`: `fiscal_quarter_id`, `scenario_id`, `deposit_product_id`, `customer_segment_id`, `deposit_rate_percent`, `deposit_beta_percent`
- `bank.deposit.fact_deposit_balance`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `deposit_product_id`, `customer_segment_id`, `deposit_balance_amount`, `average_deposit_balance_amount`

### Q2 2026 (3) Bank of America

Where is there still room to optimize both sides of the balance sheet?

- `bank.balance.fact_earning_asset_balance`: `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `earning_asset_amount`, `average_earning_asset_amount`
- `bank.balance.fact_funding_balance`: `fiscal_quarter_id`, `scenario_id`, `funding_type_id`, `funding_balance_amount`
- `bank.balance.fact_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `asset_class_id`, `interest_income_amount`
- `bank.balance.fact_interest_expense`: `fiscal_quarter_id`, `scenario_id`, `funding_type_id`, `interest_expense_amount`

### Q2 2026 (4) Bank of America

If the rate path changes, does the net-interest-income guide move, and do stronger prime-brokerage and markets results offset the path to the high end of the 6% to 8% range?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2026 (8) Bank of America

In the second half, is the story earning-asset growth with little net-interest-margin expansion?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2026 (10) Bank of America

Which areas drove the change in the operating-leverage outlook?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q1 2026 (1) Bank of America

How much of the better net-interest-income outcome is dropped to the bottom line?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q1 2026 (5) Bank of America

How much funding optimization is left, and how does that interact with balance-sheet growth?

- `bank.balance.fact_earning_asset_balance`: `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `earning_asset_amount`, `average_earning_asset_amount`
- `bank.balance.fact_funding_balance`: `fiscal_quarter_id`, `scenario_id`, `funding_type_id`, `funding_balance_amount`
- `bank.balance.fact_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `asset_class_id`, `interest_income_amount`
- `bank.balance.fact_interest_expense`: `fiscal_quarter_id`, `scenario_id`, `funding_type_id`, `interest_expense_amount`

### Q1 2026 (9) Bank of America

If the Fed does not cut, can deposit costs stay contained given loan growth on the markets balance sheet?

- `bank.deposit.fact_deposit_price`: `fiscal_quarter_id`, `scenario_id`, `deposit_product_id`, `customer_segment_id`, `deposit_rate_percent`, `deposit_beta_percent`
- `bank.deposit.fact_deposit_balance`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `deposit_product_id`, `customer_segment_id`, `deposit_balance_amount`, `average_deposit_balance_amount`

### Q1 2026 (10) Bank of America

Why would first-quarter net-interest-income growth not hold for the year, including a shift from markets net interest income into fees under higher-for-longer?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`
- `bank.balance.fact_net_interest_margin`: `fiscal_quarter_id`, `scenario_id`, `net_interest_margin_percent`
- `bank.deposit.fact_deposit_price`: `fiscal_quarter_id`, `scenario_id`, `deposit_product_id`, `customer_segment_id`, `deposit_rate_percent`, `deposit_beta_percent`
- `bank.balance.fact_earning_asset_balance`: `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `earning_asset_amount`, `average_earning_asset_amount`

### Q4 2025 (3) Bank of America

What is the operating-leverage message for this year and the next three years underneath the return target, after the fee restatement?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q4 2025 (4) Bank of America

Are deposit betas better or worse than expected, and how are clients behaving?

- `bank.deposit.fact_deposit_price`: `fiscal_quarter_id`, `scenario_id`, `deposit_product_id`, `customer_segment_id`, `deposit_rate_percent`, `deposit_beta_percent`
- `bank.deposit.fact_deposit_balance`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `deposit_product_id`, `customer_segment_id`, `deposit_balance_amount`, `average_deposit_balance_amount`

### Q4 2025 (5) Bank of America

Is the markets net-interest-income growth rate reasonable for the year, or do rate cuts make markets versus non-markets NII harder?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`
- `bank.balance.fact_net_interest_margin`: `fiscal_quarter_id`, `scenario_id`, `net_interest_margin_percent`
- `bank.deposit.fact_deposit_price`: `fiscal_quarter_id`, `scenario_id`, `deposit_product_id`, `customer_segment_id`, `deposit_rate_percent`, `deposit_beta_percent`
- `bank.balance.fact_earning_asset_balance`: `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `earning_asset_amount`, `average_earning_asset_amount`

### Q4 2025 (6) Bank of America

How much liability optimization is left given core deposit trends, and how much is already in the guide?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q4 2025 (8) Bank of America

Why are deposits sluggish despite hundreds of thousands of new checking accounts, and does a turn in 2026 help operating leverage?

- `bank.deposit.fact_deposit_balance`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `deposit_product_id`, `customer_segment_id`, `deposit_balance_amount`, `average_deposit_balance_amount`
- `bank.deposit.fact_deposit_account_count`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `deposit_product_id`, `customer_segment_id`, `deposit_account_count`, `new_deposit_account_count`
- `bank.deposit.fact_deposit_price`: `fiscal_quarter_id`, `scenario_id`, `deposit_product_id`, `customer_segment_id`, `deposit_rate_percent`, `deposit_beta_percent`

### Q2 2025 (1) Bank of America

How is progress measured on growing retail deposit share?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2025 (6) Bank of America

Will housing-related investment rise enough to offset the fade in wind and solar financing?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

## JPMorgan Chase

### Q2 2026 (1) JPMorgan Chase

How sustainable is the current risk-on stance across the businesses?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2026 (2) JPMorgan Chase

How is consumer-bank deposit growth progressing toward the stated retail market-share goal, and does higher-for-longer change the pace?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2026 (4) JPMorgan Chase

What drove the higher net-interest-income outlook excluding markets, and how should the third quarter, fourth quarter, and exit rate into next year phase?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2026 (5) JPMorgan Chase

How much of that NII revision is balance-sheet mix versus other factors?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`
- `bank.balance.fact_net_interest_margin`: `fiscal_quarter_id`, `scenario_id`, `net_interest_margin_percent`
- `bank.deposit.fact_deposit_price`: `fiscal_quarter_id`, `scenario_id`, `deposit_product_id`, `customer_segment_id`, `deposit_rate_percent`, `deposit_beta_percent`
- `bank.balance.fact_earning_asset_balance`: `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `earning_asset_amount`, `average_earning_asset_amount`

### Q2 2026 (8) JPMorgan Chase

At what higher rate level would deposit volumes and betas change meaningfully?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2026 (9) JPMorgan Chase

Which products or geographies were unusually strong this quarter and may be hard to sustain?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2026 (11) JPMorgan Chase

What is the status of the smart-cash tool, who it will be offered to, and how does that fit with having to pay more for deposits over time?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2026 (12) JPMorgan Chase

What is the consumer-bank ambition across major European markets?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2026 (15) JPMorgan Chase

Is markets balance-sheet allocation at a peak, or can more be allocated if activity stays high?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q1 2026 (1) JPMorgan Chase

How does deposit competition change as smart-cash tools spread, and does the outlook include mitigating actions?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q1 2026 (2) JPMorgan Chase

If rates are not cut for the rest of the year, what offsets higher rates and the asset-sensitive position?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q1 2026 (3) JPMorgan Chase

In a recession with higher leveraged-lending defaults, how much loss comes back to banks, and would a private-credit default cycle be systemic?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q1 2026 (4) JPMorgan Chase

How did scenario weights and macro risks flow into reserves this quarter?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q1 2026 (7) JPMorgan Chase

How much of the shift to private credit is credit banks would not have done, can share be recaptured, and are collateral standards and spreads tightening?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q1 2026 (8) JPMorgan Chase

Is consumer deposit growth back on the higher path?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q1 2026 (12) JPMorgan Chase

How much long-duration private-markets financing can large banks do, and how large is JPMorgan's private-credit exposure?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q1 2026 (13) JPMorgan Chase

Does higher-for-longer pressure refinancing of single-B and double-B paper coming due?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q4 2025 (1) JPMorgan Chase

What else, besides the factors already discussed, is limiting deposit growth despite strong new checking accounts?

- `bank.deposit.fact_deposit_balance`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `deposit_product_id`, `customer_segment_id`, `deposit_balance_amount`, `average_deposit_balance_amount`
- `bank.deposit.fact_deposit_account_count`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `deposit_product_id`, `customer_segment_id`, `deposit_account_count`, `new_deposit_account_count`
- `bank.deposit.fact_deposit_price`: `fiscal_quarter_id`, `scenario_id`, `deposit_product_id`, `customer_segment_id`, `deposit_rate_percent`, `deposit_beta_percent`

### Q4 2025 (3) JPMorgan Chase

If regulators capped credit-card APRs, how would that hit the industry and what would a large issuer change?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q4 2025 (4) JPMorgan Chase

Is the Apple Card migration a new technology stack or an enhancement of the current system, and why does it take about two years?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q4 2025 (5) JPMorgan Chase

What balance-sheet growth sits under the net-interest-income outlook?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q4 2025 (8) JPMorgan Chase

With rates lower and the outlook solid, is corporate credit steady, improving, or a concern?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2025 (1) JPMorgan Chase

What is raising the wholesale lending profile: private credit, M&A financing, inventory, or something else?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2025 (2) JPMorgan Chase

Did the open-banking hold period change pricing for fintech relationships?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2025 (5) JPMorgan Chase

What supports more confidence in deposit margin and mid- to upper-single-digit deposit growth?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2025 (8) JPMorgan Chase

Have tariff and tax uncertainties that froze client activity in the spring cleared enough for second-half activity to continue?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2025 (9) JPMorgan Chase

What duration extension or hedges have been added so the balance sheet is less sensitive before rate cuts?

- `bank.balance.fact_earning_asset_balance`: `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `earning_asset_amount`, `average_earning_asset_amount`
- `bank.balance.fact_funding_balance`: `fiscal_quarter_id`, `scenario_id`, `funding_type_id`, `funding_balance_amount`
- `bank.balance.fact_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `asset_class_id`, `interest_income_amount`
- `bank.balance.fact_interest_expense`: `fiscal_quarter_id`, `scenario_id`, `funding_type_id`, `interest_expense_amount`

### Q2 2025 (10) JPMorgan Chase

Is growth in lower-margin areas a supply issue or a demand issue if leverage rules loosen?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2025 (12) JPMorgan Chase

How much of markets strength was the environment versus balance-sheet use, and has the environment calmed?

- `bank.balance.fact_segment_net_interest_income`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `net_interest_income_amount`

### Q2 2025 (13) JPMorgan Chase

Are commercial and corporate customers pushing deposit pricing to offset tariffs?

- `bank.deposit.fact_deposit_price`: `fiscal_quarter_id`, `scenario_id`, `deposit_product_id`, `customer_segment_id`, `deposit_rate_percent`, `deposit_beta_percent`
- `bank.deposit.fact_deposit_balance`: `fiscal_quarter_id`, `scenario_id`, `reporting_segment_id`, `deposit_product_id`, `customer_segment_id`, `deposit_balance_amount`, `average_deposit_balance_amount`
