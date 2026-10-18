# Bank Inc credit and loans

This slice owns loan products, card programs, credit quantities, and credit prices. Deposit rates, net interest income, and markets revenue live in the other slices and are partial when named here. A loan balance does not store a spread.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `asset_class_identity` | `asset_class_id` | `sf:bank.balance.dim_asset_class` `asset_class_id` |
| `business_line_identity` | `business_line_id` | `sf:bank.customer.dim_business_line` `business_line_id` |
| `competitor_identity` | `competitor_id` | `sf:bank.customer.dim_competitor` `competitor_id` |
| `country_identity` | `country_id` | `sf:bank.geography.dim_country` `country_id` |
| `customer_segment_identity` | `customer_segment_id` | `sf:bank.customer.dim_customer_segment` `customer_segment_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:bank.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `rate_scenario_identity` | `rate_scenario_id` | `sf:bank.geography.dim_rate_scenario` `rate_scenario_id` |

## Numbered questions

## Bank of America

### Q2 2026 (5)

How is middle-market commercial and industrial loan growth trending into the back half at Bank of America?

- `bank.credit.fact_loan_balance`: `loan_balance_amount`, `growth_rate`
- `bank.credit.fact_loan_outlook`: `outlook_direction`
- `bank.credit.dim_loan_product`: `product_code`
- `bank.customer.dim_customer_segment`: `segment_code`

### Q2 2026 (11)

Are cards still on the path toward about 5% growth, why were net client flows softer, and is traditional commercial and industrial demand returning away from hyperscalers at Bank of America?

- `bank.credit.fact_card_balance`: `growth_rate`, `on_five_percent_path_flag`, `card_balance_amount`
- `bank.customer.fact_client_flow`: `net_flow_amount`, `softer_flag`
- `bank.credit.fact_loan_purpose_mix`: `mix_share`
- `bank.credit.dim_borrower_purpose`: `purpose_code`

### Q2 2026 (12)

Is credit underwriting turning risk-on, and what is the second-order credit exposure from the data-center build-out beyond direct project loans at Bank of America?

- `bank.credit.fact_underwriting_stance`: `risk_on_flag`, `covenant_loosening_flag`, `standards_held_flag`
- `bank.credit.fact_data_center_exposure`: `direct_amount`
- `bank.credit.fact_second_order_exposure`: `indirect_amount`
- `bank.credit.dim_exposure_ring`: `ring_code`

### Q1 2026 (6)

Is stronger loan growth early share taken from private credit, or broader demand and higher line utilization at Bank of America?

- `bank.credit.fact_growth_source`: `source_code`, `private_credit_share_taken_flag`, `broader_demand_flag`
- `bank.credit.fact_line_utilization`: `utilization_rate`
- `bank.credit.fact_private_credit_book`: `migrated_amount`, `recapture_flag`

### Q4 2025 (2)

Card spending rose faster than balances and fees fell; what initiatives are supposed to accelerate card growth, and on what timing at Bank of America?

- `bank.deposit.fact_consumer_spend`: `spend_amount`
- `bank.credit.fact_card_balance`: `card_balance_amount`, `growth_rate`
- `bank.credit.fact_card_fee`: `fee_amount`, `fee_down_flag`
- `bank.credit.dim_card_program`: `program_code`

### Q4 2025 (7)

Which asset classes look less attractive into 2026, and where is loan growth not being pushed, including any strategy change if card yields were capped near 10% at Bank of America?

- `bank.balance.fact_asset_mix`: `attractive_flag`, `growth_pushed_flag`
- `bank.credit.fact_card_yield`: `yield_rate`, `cap_near_ten_flag`, `product_change_flag`
- `bank.credit.fact_loan_outlook`: `outlook_direction`
- `bank.balance.dim_asset_class`: `asset_class_code`

### Q4 2025 (10)

Are credit losses below trend, in which categories, and can consumer deposits reach mid-single-digit growth as rates fall at Bank of America?

- `bank.credit.fact_credit_loss`: `loss_rate`, `below_trend_flag`
- `bank.credit.dim_loss_category`: `loss_code`
- `bank.deposit.fact_deposit_balance`: `growth_rate`
- `bank.geography.dim_rate_scenario`: `scenario_code`

### Q2 2025 (6)

Will housing-related investment rise enough to offset the fade in wind and solar financing at Bank of America?

- `bank.credit.fact_housing_pipeline`: `pipeline_amount`
- `bank.credit.fact_renewable_book`: `balance_amount`, `fade_flag`
- `bank.credit.dim_borrower_purpose`: `purpose_code`

### Q2 2025 (7)

What are borrowers saying about loan growth, and how confident is that pipeline at Bank of America?

- `bank.credit.fact_borrower_pipeline`: `pipeline_amount`, `confidence_index`
- `bank.credit.fact_loan_balance`: `growth_rate`

## JPMorgan Chase

### Q2 2026 (10)

Is commercial-lending capex demand broadening beyond AI at JPMorgan Chase?

- `bank.credit.fact_loan_purpose_mix`: `mix_share`
- `bank.credit.dim_borrower_purpose`: `purpose_code`
- `bank.credit.fact_loan_outlook`: `broadening_flag`

### Q2 2026 (13)

Are competitors loosening credit underwriting at JPMorgan Chase?

- `bank.credit.fact_underwriting_stance`: `covenant_loosening_flag`, `standards_held_flag`, `risk_on_flag`
- `bank.customer.dim_competitor`: `competitor_code`
- `bank.credit.dim_underwriting_term`: `term_code`

### Q1 2026 (3)

In a recession with higher leveraged-lending defaults, how much loss comes back to banks, and would a private-credit default cycle be systemic at JPMorgan Chase?

- `bank.credit.fact_credit_loss`: `loss_rate`
- `bank.credit.fact_private_credit_book`: `exposure_amount`, `systemic_flag`
- `bank.credit.dim_credit_category`: `category_code`

### Q1 2026 (4)

How did scenario weights and macro risks flow into reserves this quarter at JPMorgan Chase?

- `bank.credit.fact_reserve_build`: `reserve_amount`, `scenario_weight`
- `bank.credit.dim_macro_scenario`: `scenario_code`

### Q1 2026 (7)

How much of the shift to private credit is credit banks would not have done, can share be recaptured, and are collateral standards and spreads tightening at JPMorgan Chase?

- `bank.credit.fact_private_credit_book`: `migrated_amount`, `bank_would_not_have_done_flag`, `recapture_flag`
- `bank.credit.fact_collateral_standard`: `tightening_flag`, `standard_index`
- `bank.credit.fact_credit_spread`: `spread_bps`, `tightening_flag`

### Q1 2026 (9)

What loan advance rates and credit enhancement protect the positions being discussed at JPMorgan Chase?

- `bank.credit.fact_advance_rate`: `advance_rate`
- `bank.credit.fact_credit_enhancement`: `enhancement_rate`, `loss_absorption_rate`
- `bank.credit.dim_collateral_type`: `collateral_code`

### Q1 2026 (12)

How much long-duration private-markets financing can large banks do, and how large is JPMorgan's private-credit exposure?

- `bank.credit.fact_private_credit_book`: `exposure_amount`
- `bank.markets.fact_lower_margin_capacity`: `capacity_amount`, `supply_limited_flag`
- `bank.credit.dim_loan_product`: `product_code`

### Q1 2026 (13)

Does higher-for-longer pressure refinancing of single-B and double-B paper coming due at JPMorgan Chase?

- `bank.credit.fact_refinancing_wall`: `maturity_amount`, `borrower_capacity_flag`, `pressure_flag`
- `bank.geography.dim_rate_scenario`: `scenario_code`
- `bank.credit.dim_credit_category`: `category_code`

### Q4 2025 (3)

If regulators capped credit-card APRs, how would that hit the industry and what would a large issuer change at JPMorgan Chase?

- `bank.credit.fact_card_yield`: `yield_rate`, `cap_near_ten_flag`, `product_change_flag`
- `bank.credit.fact_card_fee`: `fee_amount`
- `bank.credit.dim_card_program`: `program_code`

### Q4 2025 (4)

Is the Apple Card migration a new technology stack or an enhancement of the current system, and why does it take about two years at JPMorgan Chase?

- `bank.credit.fact_card_migration`: `stack_new_flag`, `timeline_months`
- `bank.credit.dim_card_program`: `program_code`, `program_name`

### Q4 2025 (7)

Are loan demand signs broadening into traditional commercial and industrial, mortgage, or auto, and what is expected for 2026 at JPMorgan Chase?

- `bank.credit.fact_loan_outlook`: `outlook_direction`, `broadening_flag`
- `bank.credit.dim_loan_product`: `product_code`
- `bank.credit.fact_loan_balance`: `growth_rate`

### Q4 2025 (8)

With rates lower and the outlook solid, is corporate credit steady, improving, or a concern at JPMorgan Chase?

- `bank.credit.fact_corporate_credit_view`: `stance_code`
- `bank.credit.fact_credit_loss`: `loss_rate`
- `bank.geography.dim_rate_scenario`: `scenario_code`

### Q2 2025 (1)

What is raising the wholesale lending profile: private credit, M&A financing, inventory, or something else at JPMorgan Chase?

- `bank.credit.fact_loan_purpose_mix`: `mix_share`
- `bank.credit.dim_borrower_purpose`: `purpose_code`
- `bank.credit.fact_loan_balance`: `growth_rate`
- `bank.credit.dim_loan_product`: `product_code`

### Q2 2025 (4)

Over the next six to twelve months, should credit quality be a concern given rates, tariffs, and slower consumer spending, and where is consumer or commercial stress building at JPMorgan Chase?

- `bank.credit.fact_delinquency`: `delinquency_rate`, `stress_building_flag`
- `bank.credit.fact_credit_loss`: `loss_rate`
- `bank.deposit.fact_consumer_spend`: `spend_amount`
- `bank.credit.dim_credit_category`: `category_code`

### Q2 2025 (6)

Why was commercial loan growth stronger in the quarter, and where was it strong by geography at JPMorgan Chase?

- `bank.credit.fact_loan_balance`: `growth_rate`, `loan_balance_amount`
- `bank.geography.dim_country`: `country_code`
- `bank.customer.dim_customer_segment`: `segment_code`
