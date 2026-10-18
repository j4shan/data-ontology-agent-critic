# Bank Inc balance sheet and deposits

This slice owns geography, the client, deposit products, deposit quantities, deposit prices, and the net-interest-income result. Loan balances, card yields, markets revenue, and expense live in the other slices and are partial when named here.

## Numbered questions

## Bank of America

### Q2 2026 (1)

How does deposit pricing behave in a higher-for-longer setting after this quarter's pricing beat peers while the full-year net-interest-income guide was left unchanged at Bank of America?

- `bank.deposit.fact_deposit_rate`: `rate_paid`, `peer_rate`, `beat_peers_flag`, `beta`
- `bank.balance.fact_nii_result`: `guide_unchanged_flag`, `nii_amount`
- `bank.geography.dim_rate_scenario`: `scenario_code`

### Q2 2026 (3)

Where is there still room to optimize both sides of the balance sheet at Bank of America?

- `bank.balance.fact_liability_mix`: `mix_share`, `room_to_optimize_flag`
- `bank.balance.fact_asset_mix`: `mix_share`, `attractive_flag`
- `bank.balance.fact_funding_capacity`: `remaining_optimization_amount`

### Q2 2026 (4)

If the rate path changes, does the net-interest-income guide move, and do stronger prime-brokerage and markets results offset the path to the high end of the 6% to 8% range at Bank of America?

- `bank.balance.fact_nii_bridge`: `guide_moves_with_path_flag`, `markets_offset_flag`, `effect_amount`
- `bank.markets.fact_markets_revenue`: `revenue_amount`
- `bank.markets.dim_markets_desk`: `desk_code`
- `bank.geography.dim_rate_scenario`: `scenario_code`

### Q2 2026 (6)

Does the net-interest-income guide assume a static earning-asset mix or a continued shift toward more loans at Bank of America?

- `bank.balance.fact_earning_asset`: `static_mix_flag`, `shift_toward_loans_flag`, `earning_asset_amount`
- `bank.balance.fact_nii_result`: `nii_amount`, `guide_low_amount`, `guide_high_amount`
- `bank.balance.fact_asset_mix`: `mix_share`

### Q2 2026 (8)

In the second half, is the story earning-asset growth with little net-interest-margin expansion at Bank of America?

- `bank.balance.fact_earning_asset`: `growth_rate`, `earning_asset_amount`
- `bank.balance.fact_nim`: `nim_rate`, `little_expansion_flag`, `expansion_amount`
- `bank.geography.dim_fiscal_quarter`: `guidance_horizon`, `quarter_code`

### Q1 2026 (1)

How much of the better net-interest-income outcome is dropped to the bottom line at Bank of America?

- `bank.balance.fact_nii_result`: `bottom_line_share`, `nii_amount`
- `bank.markets.fact_expense_actual`: `expense_amount`

### Q1 2026 (2)

Why are consumer loan and deposit balances sluggish when spending, employment, and new checking and card accounts are strong at Bank of America?

- `bank.credit.fact_loan_balance`: `sluggish_flag`, `loan_balance_amount`
- `bank.deposit.fact_deposit_balance`: `balance_sluggish_flag`, `deposit_balance_amount`
- `bank.deposit.fact_consumer_spend`: `spend_amount`, `employment_strong_flag`
- `bank.deposit.fact_checking_account`: `new_checking_quantity`, `new_card_account_quantity`

### Q1 2026 (4)

What loan and deposit growth is assumed inside the tweaked net-interest-income outlook at Bank of America?

- `bank.balance.fact_nii_result`: `nii_amount`, `growth_rate`
- `bank.credit.fact_loan_balance`: `growth_rate`, `loan_balance_amount`
- `bank.deposit.fact_deposit_balance`: `growth_rate`, `deposit_balance_amount`

### Q1 2026 (5)

How much funding optimization is left, and how does that interact with balance-sheet growth at Bank of America?

- `bank.balance.fact_funding_capacity`: `remaining_optimization_amount`, `growth_interaction_flag`
- `bank.balance.fact_earning_asset`: `growth_rate`, `earning_asset_amount`

### Q1 2026 (9)

If the Fed does not cut, can deposit costs stay contained given loan growth on the markets balance sheet at Bank of America?

- `bank.deposit.fact_deposit_rate`: `contained_without_cuts_flag`, `rate_paid`, `beta`
- `bank.credit.fact_loan_balance`: `growth_rate`
- `bank.geography.dim_rate_scenario`: `scenario_code`
- `bank.markets.fact_markets_balance`: `allocated_amount`

### Q1 2026 (10)

Why would first-quarter net-interest-income growth not hold for the year, including a shift from markets net interest income into fees under higher-for-longer at Bank of America?

- `bank.balance.fact_nii_result`: `growth_rate`, `hold_for_year_flag`
- `bank.markets.fact_fee_mix_shift`: `nii_to_fee_flag`, `fee_share`
- `bank.markets.fact_markets_revenue`: `revenue_amount`
- `bank.geography.dim_rate_scenario`: `scenario_code`

### Q4 2025 (4)

Are deposit betas better or worse than expected, and how are clients behaving at Bank of America?

- `bank.deposit.fact_deposit_rate`: `beta`, `rate_paid`
- `bank.deposit.fact_client_behavior`: `rate_seeking_index`, `beta_versus_plan_code`
- `bank.customer.dim_customer_segment`: `segment_code`

### Q4 2025 (5)

Is the markets net-interest-income growth rate reasonable for the year, or do rate cuts make markets versus non-markets NII harder at Bank of America?

- `bank.balance.fact_nii_result`: `growth_rate`, `nii_amount`
- `bank.balance.fact_nii_bridge`: `effect_amount`
- `bank.customer.dim_business_line`: `line_code`
- `bank.geography.dim_rate_scenario`: `scenario_code`

### Q4 2025 (6)

How much liability optimization is left given core deposit trends, and how much is already in the guide at Bank of America?

- `bank.balance.fact_funding_capacity`: `remaining_optimization_amount`, `embedded_in_guide_flag`
- `bank.balance.fact_liability_mix`: `room_to_optimize_flag`, `mix_share`
- `bank.deposit.fact_deposit_balance`: `growth_rate`, `deposit_balance_amount`

### Q4 2025 (8)

Why are deposits sluggish despite hundreds of thousands of new checking accounts, and does a turn in 2026 help operating leverage at Bank of America?

- `bank.deposit.fact_deposit_balance`: `balance_sluggish_flag`, `deposit_balance_amount`, `growth_rate`
- `bank.deposit.fact_checking_account`: `new_checking_quantity`
- `bank.markets.fact_operating_leverage`: `leverage_bps`

### Q4 2025 (9)

If the stablecoin yield loophole is not closed, what happens to deposit trends at Bank of America?

- `bank.deposit.fact_stablecoin_flow`: `outflow_quantity`, `yield_loophole_open_flag`
- `bank.deposit.fact_deposit_balance`: `growth_rate`, `deposit_balance_amount`

### Q2 2025 (1)

How is progress measured on growing retail deposit share at Bank of America?

- `bank.deposit.fact_deposit_share`: `share_rate`, `target_share_rate`, `scorecard_index`
- `bank.customer.dim_customer_segment`: `segment_code`

### Q2 2025 (2)

Is the step-up from loan, securities, and swap repricing linear through the third and fourth quarters or back-loaded at Bank of America?

- `bank.balance.fact_repricing_path`: `step_share`, `back_loaded_flag`, `linear_flag`
- `bank.balance.dim_asset_class`: `asset_class_code`
- `bank.geography.dim_fiscal_quarter`: `quarter_code`

### Q2 2025 (5)

How could stablecoin adoption affect payments revenue and deposits, and would banks respond as a consortium or one by one at Bank of America?

- `bank.deposit.fact_stablecoin_flow`: `outflow_quantity`, `consortium_response_flag`
- `bank.markets.fact_payments_revenue`: `revenue_amount`, `stablecoin_effect_amount`
- `bank.deposit.fact_deposit_balance`: `deposit_balance_amount`

## JPMorgan Chase

### Q2 2026 (2)

How is consumer-bank deposit growth progressing toward the stated retail market-share goal, and does higher-for-longer change the pace at JPMorgan Chase?

- `bank.deposit.fact_deposit_balance`: `growth_rate`, `deposit_balance_amount`
- `bank.deposit.fact_deposit_share`: `share_rate`, `target_share_rate`
- `bank.geography.dim_rate_scenario`: `scenario_code`
- `bank.customer.dim_customer_segment`: `segment_code`

### Q2 2026 (4)

What drove the higher net-interest-income outlook excluding markets, and how should the third quarter, fourth quarter, and exit rate into next year phase at JPMorgan Chase?

- `bank.balance.fact_nii_result`: `nii_amount`, `growth_rate`
- `bank.balance.fact_nii_bridge`: `effect_amount`
- `bank.customer.dim_business_line`: `line_code`
- `bank.geography.dim_fiscal_quarter`: `quarter_code`, `guidance_horizon`

### Q2 2026 (5)

How much of that NII revision is balance-sheet mix versus other factors at JPMorgan Chase?

- `bank.balance.fact_nii_bridge`: `effect_amount`
- `bank.balance.dim_nii_driver`: `driver_code`
- `bank.balance.fact_asset_mix`: `mix_share`

### Q2 2026 (8)

At what higher rate level would deposit volumes and betas change meaningfully at JPMorgan Chase?

- `bank.deposit.fact_rate_threshold`: `threshold_rate`, `volume_changes_above_flag`
- `bank.deposit.fact_deposit_rate`: `beta`, `rate_paid`

### Q2 2026 (11)

What is the status of the smart-cash tool, who it will be offered to, and how does that fit with having to pay more for deposits over time at JPMorgan Chase?

- `bank.deposit.fact_smart_cash_offer`: `audience_code`, `rollout_status`, `offered_rate`
- `bank.deposit.fact_deposit_rate`: `rate_paid`
- `bank.deposit.dim_deposit_product`: `product_code`

### Q2 2026 (12)

What is the consumer-bank ambition across major European markets at JPMorgan Chase?

- `bank.customer.fact_europe_ambition`: `market_open_flag`, `customer_quantity`, `product_live_count`
- `bank.geography.dim_country`: `country_code`
- `bank.customer.dim_channel`: `channel_code`

### Q1 2026 (1)

How does deposit competition change as smart-cash tools spread, and does the outlook include mitigating actions at JPMorgan Chase?

- `bank.deposit.fact_deposit_competition`: `tool_adoption_rate`, `mitigation_in_guide_flag`
- `bank.deposit.fact_smart_cash_offer`: `rollout_status`, `offered_rate`
- `bank.deposit.fact_deposit_rate`: `rate_paid`

### Q1 2026 (2)

If rates are not cut for the rest of the year, what offsets higher rates and the asset-sensitive position at JPMorgan Chase?

- `bank.balance.fact_balance_position`: `asset_sensitive_flag`
- `bank.balance.fact_nii_bridge`: `effect_amount`, `markets_offset_flag`
- `bank.geography.dim_rate_scenario`: `scenario_code`

### Q1 2026 (5)

What drove loan and deposit growth this quarter, and how does that change the full-year outlook at JPMorgan Chase?

- `bank.credit.fact_loan_balance`: `growth_rate`, `loan_balance_amount`
- `bank.deposit.fact_deposit_balance`: `growth_rate`, `deposit_balance_amount`
- `bank.credit.fact_loan_outlook`: `outlook_direction`
- `bank.balance.fact_nii_result`: `nii_amount`

### Q1 2026 (8)

Is consumer deposit growth back on the higher path at JPMorgan Chase?

- `bank.deposit.fact_deposit_balance`: `growth_rate`, `deposit_balance_amount`
- `bank.deposit.fact_deposit_share`: `share_rate`
- `bank.customer.dim_customer_segment`: `segment_code`

### Q4 2025 (1)

What else, besides the factors already discussed, is limiting deposit growth despite strong new checking accounts at JPMorgan Chase?

- `bank.deposit.fact_deposit_balance`: `growth_rate`, `balance_sluggish_flag`
- `bank.deposit.fact_checking_account`: `new_checking_quantity`
- `bank.deposit.fact_client_behavior`: `rate_seeking_index`

### Q4 2025 (5)

What balance-sheet growth sits under the net-interest-income outlook at JPMorgan Chase?

- `bank.balance.fact_earning_asset`: `earning_asset_amount`, `growth_rate`
- `bank.credit.fact_loan_balance`: `loan_balance_amount`, `growth_rate`
- `bank.deposit.fact_deposit_balance`: `deposit_balance_amount`, `growth_rate`
- `bank.balance.fact_nii_result`: `nii_amount`

### Q2 2025 (3)

What is stopping banks from offering a joint deposit-like product, as with Zelle, before stablecoin firms offer a more convenient alternative at JPMorgan Chase?

- `bank.deposit.fact_stablecoin_flow`: `consortium_response_flag`, `outflow_quantity`
- `bank.deposit.dim_deposit_product`: `product_code`
- `bank.markets.fact_payments_revenue`: `revenue_amount`

### Q2 2025 (5)

What supports more confidence in deposit margin and mid- to upper-single-digit deposit growth at JPMorgan Chase?

- `bank.deposit.fact_deposit_margin`: `margin_rate`, `confidence_flag`
- `bank.deposit.fact_deposit_balance`: `growth_rate`, `deposit_balance_amount`

### Q2 2025 (9)

What duration extension or hedges have been added so the balance sheet is less sensitive before rate cuts at JPMorgan Chase?

- `bank.balance.fact_balance_position`: `duration_years`, `hedge_added_flag`, `asset_sensitive_flag`
- `bank.balance.dim_hedge_program`: `hedge_code`
- `bank.balance.fact_nii_result`: `nii_amount`

### Q2 2025 (13)

Are commercial and corporate customers pushing deposit pricing to offset tariffs at JPMorgan Chase?

- `bank.deposit.fact_deposit_rate`: `rate_paid`, `beta`
- `bank.customer.dim_customer_segment`: `segment_code`
- `bank.deposit.fact_client_behavior`: `rate_seeking_index`
