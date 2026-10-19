# Bank Inc credit, loans, and cards

Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks. Demand quantity, supply or capacity, and price or margin are stored on separate facts joined by the shared grain keys (fiscal quarter, scenario, and the business keys).

## Numbered questions

## Bank of America

### Q2 2026 (5) Bank of America

How is middle-market commercial and industrial loan growth trending into the back half?

- `bank.loan.fact_loan_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `loan_balance_amount`, `average_loan_balance_amount`
- `bank.loan.fact_loan_origination`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `origination_amount`, `origination_count`
- `bank.loan.fact_line_utilization`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `drawn_balance_amount`, `undrawn_commitment_amount`

### Q2 2026 (6) Bank of America

Does the net-interest-income guide assume a static earning-asset mix or a continued shift toward more loans?

- `bank.loan.fact_loan_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `loan_balance_amount`, `average_loan_balance_amount`
- `bank.loan.fact_loan_origination`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `origination_amount`, `origination_count`
- `bank.loan.fact_line_utilization`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `drawn_balance_amount`, `undrawn_commitment_amount`

### Q2 2026 (12) Bank of America

Is credit underwriting turning risk-on, and what is the second-order credit exposure from the data-center build-out beyond direct project loans?

- `bank.credit.fact_net_charge_off`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `net_charge_off_amount`, `net_charge_off_rate_percent`
- `bank.credit.fact_provision_expense`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `provision_expense_amount`
- `bank.credit.fact_allowance_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `allowance_balance_amount`
- `bank.loan.fact_loan_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `loan_balance_amount`, `average_loan_balance_amount`

### Q1 2026 (2) Bank of America

Why are consumer loan and deposit balances sluggish when spending, employment, and new checking and card accounts are strong?

- `bank.card.fact_card_balance`: `fiscal_quarter_id`, `scenario_id`, `card_program_id`, `customer_segment_id`, `card_balance_amount`, `revolving_balance_amount`
- `bank.card.fact_card_account_count`: `fiscal_quarter_id`, `scenario_id`, `card_program_id`, `card_account_count`, `new_card_account_count`
- `bank.card.fact_card_spend`: `fiscal_quarter_id`, `scenario_id`, `card_program_id`, `card_spend_amount`

### Q1 2026 (4) Bank of America

What loan and deposit growth is assumed inside the tweaked net-interest-income outlook?

- `bank.loan.fact_loan_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `loan_balance_amount`, `average_loan_balance_amount`
- `bank.loan.fact_loan_origination`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `origination_amount`, `origination_count`
- `bank.loan.fact_line_utilization`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `drawn_balance_amount`, `undrawn_commitment_amount`

### Q1 2026 (6) Bank of America

Is stronger loan growth early share taken from private credit, or broader demand and higher line utilization?

- `bank.loan.fact_loan_pipeline`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `pipeline_amount`
- `bank.loan.fact_loan_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `loan_balance_amount`, `average_loan_balance_amount`
- `bank.loan.fact_line_utilization`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `drawn_balance_amount`, `undrawn_commitment_amount`

### Q4 2025 (2) Bank of America

Card spending rose faster than balances and fees fell; what initiatives are supposed to accelerate card growth, and on what timing?

- `bank.card.fact_card_balance`: `fiscal_quarter_id`, `scenario_id`, `card_program_id`, `customer_segment_id`, `card_balance_amount`, `revolving_balance_amount`
- `bank.card.fact_card_account_count`: `fiscal_quarter_id`, `scenario_id`, `card_program_id`, `card_account_count`, `new_card_account_count`
- `bank.card.fact_card_spend`: `fiscal_quarter_id`, `scenario_id`, `card_program_id`, `card_spend_amount`

### Q4 2025 (7) Bank of America

Which asset classes look less attractive into 2026, and where is loan growth not being pushed, including any strategy change if card yields were capped near 10%?

- `bank.loan.fact_loan_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `loan_balance_amount`, `average_loan_balance_amount`
- `bank.loan.fact_loan_origination`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `origination_amount`, `origination_count`
- `bank.loan.fact_line_utilization`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `drawn_balance_amount`, `undrawn_commitment_amount`

### Q4 2025 (10) Bank of America

Are credit losses below trend, in which categories, and can consumer deposits reach mid-single-digit growth as rates fall?

- `bank.credit.fact_net_charge_off`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `net_charge_off_amount`, `net_charge_off_rate_percent`
- `bank.credit.fact_provision_expense`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `provision_expense_amount`
- `bank.credit.fact_allowance_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `allowance_balance_amount`
- `bank.loan.fact_loan_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `loan_balance_amount`, `average_loan_balance_amount`

### Q2 2025 (2) Bank of America

Is the step-up from loan, securities, and swap repricing linear through the third and fourth quarters or back-loaded?

- `bank.loan.fact_loan_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `loan_balance_amount`, `average_loan_balance_amount`
- `bank.loan.fact_loan_origination`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `origination_amount`, `origination_count`
- `bank.loan.fact_line_utilization`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `drawn_balance_amount`, `undrawn_commitment_amount`

### Q2 2025 (7) Bank of America

What are borrowers saying about loan growth, and how confident is that pipeline?

- `bank.loan.fact_loan_pipeline`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `pipeline_amount`
- `bank.loan.fact_loan_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `loan_balance_amount`, `average_loan_balance_amount`
- `bank.loan.fact_line_utilization`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `drawn_balance_amount`, `undrawn_commitment_amount`

## JPMorgan Chase

### Q2 2026 (13) JPMorgan Chase

Are competitors loosening credit underwriting?

- `bank.credit.fact_net_charge_off`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `net_charge_off_amount`, `net_charge_off_rate_percent`
- `bank.credit.fact_provision_expense`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `provision_expense_amount`
- `bank.credit.fact_allowance_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `allowance_balance_amount`
- `bank.loan.fact_loan_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `loan_balance_amount`, `average_loan_balance_amount`

### Q1 2026 (5) JPMorgan Chase

What drove loan and deposit growth this quarter, and how does that change the full-year outlook?

- `bank.loan.fact_loan_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `loan_balance_amount`, `average_loan_balance_amount`
- `bank.loan.fact_loan_origination`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `origination_amount`, `origination_count`
- `bank.loan.fact_line_utilization`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `drawn_balance_amount`, `undrawn_commitment_amount`

### Q1 2026 (9) JPMorgan Chase

What loan advance rates and credit enhancement protect the positions being discussed?

- `bank.loan.fact_loan_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `loan_balance_amount`, `average_loan_balance_amount`
- `bank.loan.fact_loan_origination`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `origination_amount`, `origination_count`
- `bank.loan.fact_line_utilization`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `drawn_balance_amount`, `undrawn_commitment_amount`

### Q1 2026 (14) JPMorgan Chase

Has any investment-banking pipeline been paused or pushed out?

- `bank.loan.fact_loan_pipeline`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `pipeline_amount`
- `bank.loan.fact_loan_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `loan_balance_amount`, `average_loan_balance_amount`
- `bank.loan.fact_line_utilization`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `drawn_balance_amount`, `undrawn_commitment_amount`

### Q4 2025 (7) JPMorgan Chase

Are loan demand signs broadening into traditional commercial and industrial, mortgage, or auto, and what is expected for 2026?

- `bank.loan.fact_loan_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `loan_balance_amount`, `average_loan_balance_amount`
- `bank.loan.fact_loan_origination`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `origination_amount`, `origination_count`
- `bank.loan.fact_line_utilization`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `drawn_balance_amount`, `undrawn_commitment_amount`

### Q2 2025 (4) JPMorgan Chase

Over the next six to twelve months, should credit quality be a concern given rates, tariffs, and slower consumer spending, and where is consumer or commercial stress building?

- `bank.credit.fact_net_charge_off`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `net_charge_off_amount`, `net_charge_off_rate_percent`
- `bank.credit.fact_provision_expense`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `provision_expense_amount`
- `bank.credit.fact_allowance_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `allowance_balance_amount`
- `bank.loan.fact_loan_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `loan_balance_amount`, `average_loan_balance_amount`

### Q2 2025 (6) JPMorgan Chase

Why was commercial loan growth stronger in the quarter, and where was it strong by geography?

- `bank.loan.fact_loan_balance`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `loan_balance_amount`, `average_loan_balance_amount`
- `bank.loan.fact_loan_origination`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `origination_amount`, `origination_count`
- `bank.loan.fact_line_utilization`: `fiscal_quarter_id`, `scenario_id`, `loan_product_id`, `industry_client_type_id`, `drawn_balance_amount`, `undrawn_commitment_amount`

### Q2 2025 (11) JPMorgan Chase

How are customers responding to the Sapphire price changes, and how does that sit in the card competitive set?

- `bank.card.fact_card_price`: `fiscal_quarter_id`, `scenario_id`, `card_program_id`, `annual_fee_amount`, `card_apr_percent`
- `bank.card.fact_card_balance`: `fiscal_quarter_id`, `scenario_id`, `card_program_id`, `customer_segment_id`, `card_balance_amount`, `revolving_balance_amount`
