# Broker Inc price slice

This slice is part of the Broker Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q2 2026 (1) — Goldman Sachs

For Goldman Sachs, How did equities wallet share and client mix produce revenue growth far ahead of market volumes while risk-weighted assets fell?

- `broker.price.fact_wallet_share`: `wallet_share_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `wallet_share_percent`, `desk_revenue_amount`
- `broker.price.fact_equities_revenue`: `equities_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `client_type_id`, `equities_revenue_amount`
- `broker.price.fact_markets_revenue_mix`: `markets_revenue_mix_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `revenue_line_id`, `markets_revenue_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (4) — Goldman Sachs

For Goldman Sachs, How much of equities revenue is the Asia hyperscale trade, and does the recent correction threaten it?

- `broker.price.fact_ficc_revenue`: `ficc_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `ficc_revenue_amount`
- `broker.price.fact_equities_revenue`: `equities_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `client_type_id`, `equities_revenue_amount`
- `broker.price.fact_wallet_share`: `wallet_share_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `wallet_share_percent`, `desk_revenue_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (6) — Goldman Sachs

For Goldman Sachs, How much of the efficiency-ratio improvement is markets strength versus structural cost already taken out under the cloud and AI program?

- `broker.price.fact_efficiency`: `efficiency_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `efficiency_ratio_percent`, `compensation_ratio_percent`
- `broker.price.fact_underwriting_revenue`: `underwriting_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `underwriting_fee_amount`
- `broker.price.fact_asset_management_revenue`: `asset_management_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `fee_arrangement_id`, `management_fee_amount`, `performance_fee_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (7) — Goldman Sachs

For Goldman Sachs, For each dollar of merger fees, how much additional financing, risk-management, and execution revenue follows?

- `broker.price.fact_attached_revenue`: `attached_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `revenue_line_id`, `attached_revenue_amount`, `advisory_fee_amount`
- `broker.price.fact_asset_management_revenue`: `asset_management_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `fee_arrangement_id`, `management_fee_amount`, `performance_fee_amount`
- `broker.price.fact_advisory_revenue`: `advisory_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `advisory_sector_id`, `geography_id`, `fee_arrangement_id`, `advisory_fee_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (1) — Goldman Sachs

For Goldman Sachs, Are deposits being grown to fund equity financing, and how is that traded off against lower net interest income in asset and wealth management?

- `broker.price.fact_wealth_revenue`: `wealth_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `wealth_fee_amount`, `wealth_net_interest_income_amount`
- `broker.price.fact_deposit_margin`: `deposit_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `deposit_type_id`, `wealth_channel_id`, `deposit_net_interest_income_amount`, `average_deposit_rate_percent`
- `broker.price.fact_sweep_margin`: `sweep_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `sweep_net_interest_income_amount`, `sweep_spread_percent`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (2) — Goldman Sachs

For Goldman Sachs, What credit exposures are being watched as the macro picture feeds the growth outlook?

- `broker.price.fact_provision_expense`: `provision_expense_record_id`, `fiscal_quarter_id`, `scenario_id`, `credit_quality_id`, `counterparty_type_id`, `provision_amount`, `net_charge_off_amount`
- `broker.price.fact_equities_revenue`: `equities_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `client_type_id`, `equities_revenue_amount`
- `broker.price.fact_wallet_share`: `wallet_share_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `wallet_share_percent`, `desk_revenue_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (5) — Goldman Sachs

For Goldman Sachs, Was infrastructure and cloud spend front-loaded ahead of AI investment?

- `broker.price.fact_technology_investment`: `technology_investment_record_id`, `fiscal_quarter_id`, `scenario_id`, `technology_program_id`, `reporting_unit_id`, `technology_investment_amount`, `productivity_saving_amount`
- `broker.demand.fact_workplace_conversion`: `workplace_conversion_record_id`, `fiscal_quarter_id`, `scenario_id`, `workplace_stage_id`, `wealth_channel_id`, `participant_count`, `converted_account_count`, `workplace_asset_amount`
- `broker.supply.fact_technology_capacity`: `technology_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `technology_program_id`, `reporting_unit_id`, `engineer_count`, `deployed_use_case_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (6) — Goldman Sachs

For Goldman Sachs, How large a setback is the valuation reset and tighter financing for the sponsor cohort, and what share of fixed financing exposure is to direct-lending counterparties?

- `broker.price.fact_equities_revenue`: `equities_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `client_type_id`, `equities_revenue_amount`
- `broker.demand.fact_financing_demand`: `financing_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `client_type_id`, `geography_id`, `loan_commitment_amount`, `drawn_loan_balance_amount`, `financing_request_count`
- `broker.supply.fact_syndication`: `syndication_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `client_type_id`, `retained_financing_amount`, `syndicated_financing_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (9) — Goldman Sachs

For Goldman Sachs, Which businesses does AI accelerate, and is the competitive gap still open after this quarter's step-up?

- `broker.price.fact_enterprise_results`: `enterprise_results_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `total_revenue_amount`, `operating_income_amount`, `net_income_amount`, `diluted_earnings_per_share`
- `broker.demand.fact_deal_pipeline`: `deal_pipeline_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `deal_stage_id`, `advisory_sector_id`, `geography_id`, `sponsor_type_id`, `deal_count`, `deal_value_amount`, `active_mandate_count`
- `broker.demand.fact_issuance_volume`: `issuance_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `client_type_id`, `issuance_count`, `issued_principal_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (1) — Goldman Sachs

For Goldman Sachs, How is wealth meant to scale from here, and how much has the revenue floor been raised by what has already been executed?

- `broker.price.fact_wealth_revenue`: `wealth_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `wealth_fee_amount`, `wealth_net_interest_income_amount`
- `broker.price.fact_equities_revenue`: `equities_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `client_type_id`, `equities_revenue_amount`
- `broker.price.fact_wallet_share`: `wallet_share_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `wallet_share_percent`, `desk_revenue_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (2) — Goldman Sachs

For Goldman Sachs, Absent big peaks and troughs, is the firm rebasing from mid-teens returns toward the high teens?

- `broker.price.fact_capital_return`: `capital_return_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `capital_instrument_id`, `return_on_equity_percent`, `return_on_tangible_equity_percent`
- `broker.price.fact_advisory_revenue`: `advisory_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `advisory_sector_id`, `geography_id`, `fee_arrangement_id`, `advisory_fee_amount`
- `broker.price.fact_underwriting_revenue`: `underwriting_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `underwriting_fee_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (7) — Goldman Sachs

For Goldman Sachs, What revenue and efficiency should the strategy produce, and is revenue per employee the metric to watch?

- `broker.price.fact_efficiency`: `efficiency_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `efficiency_ratio_percent`, `compensation_ratio_percent`
- `broker.price.fact_revenue_per_employee`: `revenue_per_employee_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_per_employee_amount`
- `broker.price.fact_asset_management_revenue`: `asset_management_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `fee_arrangement_id`, `management_fee_amount`, `performance_fee_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (8) — Goldman Sachs

For Goldman Sachs, Where are the most compelling opportunities, and with financing approaching the share of trading revenue seen at larger peers, is the gap Goldman set out to close now closed?

- `broker.price.fact_equities_revenue`: `equities_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `client_type_id`, `equities_revenue_amount`
- `broker.price.fact_wallet_share`: `wallet_share_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `wallet_share_percent`, `desk_revenue_amount`
- `broker.price.fact_ficc_revenue`: `ficc_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `ficc_revenue_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (9) — Goldman Sachs

For Goldman Sachs, As rates fall, what offsets private-banking and lending revenue between loan demand and deposits?

- `broker.price.fact_financing_revenue`: `financing_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `client_type_id`, `financing_revenue_amount`, `financing_spread_basis_points`
- `broker.price.fact_deposit_margin`: `deposit_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `deposit_type_id`, `wealth_channel_id`, `deposit_net_interest_income_amount`, `average_deposit_rate_percent`
- `broker.price.fact_advisory_revenue`: `advisory_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `advisory_sector_id`, `geography_id`, `fee_arrangement_id`, `advisory_fee_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (1) — Goldman Sachs

For Goldman Sachs, Where can excess capital be deployed organically, and what is delaying monetization of historical principal investments in a good banking backdrop?

- `broker.price.fact_principal_investment`: `principal_investment_record_id`, `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `geography_id`, `principal_investment_gain_amount`, `monetized_gain_amount`
- `broker.demand.fact_issuance_volume`: `issuance_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `client_type_id`, `issuance_count`, `issued_principal_amount`
- `broker.supply.fact_capital_capacity`: `capital_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `capital_instrument_id`, `reporting_unit_id`, `capital_amount`, `required_capital_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (2) — Goldman Sachs

For Goldman Sachs, How much efficiency can AI unlock over time?

- `broker.price.fact_efficiency`: `efficiency_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `efficiency_ratio_percent`, `compensation_ratio_percent`
- `broker.price.fact_advisory_revenue`: `advisory_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `advisory_sector_id`, `geography_id`, `fee_arrangement_id`, `advisory_fee_amount`
- `broker.price.fact_underwriting_revenue`: `underwriting_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `underwriting_fee_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (4) — Goldman Sachs

For Goldman Sachs, Are the investments being made return-enhancing after the change in capital treatment, and which of the gains look durable?

- `broker.price.fact_capital_return`: `capital_return_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `capital_instrument_id`, `return_on_equity_percent`, `return_on_tangible_equity_percent`
- `broker.price.fact_principal_investment`: `principal_investment_record_id`, `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `geography_id`, `principal_investment_gain_amount`, `monetized_gain_amount`
- `broker.price.fact_equities_revenue`: `equities_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `client_type_id`, `equities_revenue_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (5) — Goldman Sachs

For Goldman Sachs, For the clients being covered more intensively, how much of the opportunity is more capital versus how they are covered?

- `broker.price.fact_sweep_margin`: `sweep_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `sweep_net_interest_income_amount`, `sweep_spread_percent`
- `broker.demand.fact_equities_market_activity`: `equities_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `market_share_volume_quantity`, `client_share_volume_quantity`, `trade_count`
- `broker.demand.fact_client_activity`: `client_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `client_type_id`, `geography_id`, `reporting_unit_id`, `active_client_count`, `client_trade_count`, `client_meeting_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (8) — Goldman Sachs

For Goldman Sachs, Is the medium-term return target still right, and from here is the driver the numerator or the denominator?

- `broker.price.fact_capital_return`: `capital_return_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `capital_instrument_id`, `return_on_equity_percent`, `return_on_tangible_equity_percent`
- `broker.price.fact_ficc_revenue`: `ficc_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `ficc_revenue_amount`
- `broker.price.fact_equities_revenue`: `equities_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `client_type_id`, `equities_revenue_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (1) — Morgan Stanley

For Morgan Stanley, Are workplace-channel net new assets at a peak given the IPO environment, or can the integrated firm still do better?

- `broker.price.fact_wealth_revenue`: `wealth_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `wealth_fee_amount`, `wealth_net_interest_income_amount`
- `broker.demand.fact_wealth_flows`: `wealth_flows_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `geography_id`, `net_new_asset_amount`, `asset_inflow_amount`, `asset_outflow_amount`, `client_account_count`
- `broker.demand.fact_workplace_conversion`: `workplace_conversion_record_id`, `fiscal_quarter_id`, `scenario_id`, `workplace_stage_id`, `wealth_channel_id`, `participant_count`, `converted_account_count`, `workplace_asset_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (5) — Morgan Stanley

For Morgan Stanley, How is the trading mix shifting between financing and intermediation, and how sustainable is that?

- `broker.price.fact_ficc_revenue`: `ficc_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `ficc_revenue_amount`
- `broker.price.fact_equities_revenue`: `equities_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `client_type_id`, `equities_revenue_amount`
- `broker.price.fact_markets_revenue_mix`: `markets_revenue_mix_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `revenue_line_id`, `markets_revenue_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (7) — Morgan Stanley

For Morgan Stanley, How durable are Asia equities volumes and pricing power?

- `broker.price.fact_equities_revenue`: `equities_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `client_type_id`, `equities_revenue_amount`
- `broker.price.fact_wallet_share`: `wallet_share_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `wallet_share_percent`, `desk_revenue_amount`
- `broker.price.fact_deposit_margin`: `deposit_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `deposit_type_id`, `wealth_channel_id`, `deposit_net_interest_income_amount`, `average_deposit_rate_percent`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (3) — Morgan Stanley

For Morgan Stanley, As tools make it easier to move cash, how much net interest income can still be earned on client cash?

- `broker.price.fact_sweep_margin`: `sweep_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `sweep_net_interest_income_amount`, `sweep_spread_percent`
- `broker.price.fact_deposit_margin`: `deposit_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `deposit_type_id`, `wealth_channel_id`, `deposit_net_interest_income_amount`, `average_deposit_rate_percent`
- `broker.supply.fact_client_cash`: `client_cash_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `deposit_type_id`, `client_cash_balance_amount`, `cash_holding_client_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (5) — Morgan Stanley

For Morgan Stanley, Is on-chain activity the plan for reducing friction, and how should tax-day seasonality affect wealth cash and net new assets this year?

- `broker.price.fact_wealth_revenue`: `wealth_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `wealth_fee_amount`, `wealth_net_interest_income_amount`
- `broker.demand.fact_wealth_flows`: `wealth_flows_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `geography_id`, `net_new_asset_amount`, `asset_inflow_amount`, `asset_outflow_amount`, `client_account_count`
- `broker.demand.fact_tokenization_activity`: `tokenization_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `technology_program_id`, `tokenized_transaction_count`, `tokenized_asset_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (7) — Morgan Stanley

For Morgan Stanley, Why is AI a support for the wealth revenue model rather than a threat from cash-sweep and automation tools?

- `broker.price.fact_sweep_margin`: `sweep_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `sweep_net_interest_income_amount`, `sweep_spread_percent`
- `broker.price.fact_wealth_revenue`: `wealth_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `wealth_fee_amount`, `wealth_net_interest_income_amount`
- `broker.price.fact_advisory_revenue`: `advisory_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `advisory_sector_id`, `geography_id`, `fee_arrangement_id`, `advisory_fee_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (10) — Morgan Stanley

For Morgan Stanley, Does a larger financing mix make trading less volatile in a bear market?

- `broker.price.fact_markets_revenue_mix`: `markets_revenue_mix_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `revenue_line_id`, `markets_revenue_amount`
- `broker.price.fact_wallet_share`: `wallet_share_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `wallet_share_percent`, `desk_revenue_amount`
- `broker.demand.fact_issuance_volume`: `issuance_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `client_type_id`, `issuance_count`, `issued_principal_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (11) — Morgan Stanley

For Morgan Stanley, Is the low-30s margin a ceiling, or can it go higher given the dynamics described?

- `broker.price.fact_wealth_revenue`: `wealth_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `wealth_fee_amount`, `wealth_net_interest_income_amount`
- `broker.price.fact_deposit_margin`: `deposit_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `deposit_type_id`, `wealth_channel_id`, `deposit_net_interest_income_amount`, `average_deposit_rate_percent`
- `broker.price.fact_sweep_margin`: `sweep_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `sweep_net_interest_income_amount`, `sweep_spread_percent`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (2) — Morgan Stanley

For Morgan Stanley, What drives margin from here?

- `broker.price.fact_deposit_margin`: `deposit_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `deposit_type_id`, `wealth_channel_id`, `deposit_net_interest_income_amount`, `average_deposit_rate_percent`
- `broker.price.fact_sweep_margin`: `sweep_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `sweep_net_interest_income_amount`, `sweep_spread_percent`
- `broker.price.fact_advisory_revenue`: `advisory_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `advisory_sector_id`, `geography_id`, `fee_arrangement_id`, `advisory_fee_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (5) — Morgan Stanley

For Morgan Stanley, Can incremental margins stay near last year's rate if revenue momentum continues?

- `broker.price.fact_deposit_margin`: `deposit_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `deposit_type_id`, `wealth_channel_id`, `deposit_net_interest_income_amount`, `average_deposit_rate_percent`
- `broker.price.fact_advisory_revenue`: `advisory_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `advisory_sector_id`, `geography_id`, `fee_arrangement_id`, `advisory_fee_amount`
- `broker.price.fact_underwriting_revenue`: `underwriting_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `underwriting_fee_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (7) — Morgan Stanley

For Morgan Stanley, With about a quarter of asset gathering international, how do international and domestic growth and returns compare over the medium term?

- `broker.price.fact_ficc_revenue`: `ficc_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `ficc_revenue_amount`
- `broker.price.fact_equities_revenue`: `equities_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `client_type_id`, `equities_revenue_amount`
- `broker.price.fact_wealth_revenue`: `wealth_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `wealth_fee_amount`, `wealth_net_interest_income_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (1) — Morgan Stanley

For Morgan Stanley, How do regulatory changes affect incremental return on capital relative to the firm's targets?

- `broker.price.fact_capital_return`: `capital_return_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `capital_instrument_id`, `return_on_equity_percent`, `return_on_tangible_equity_percent`
- `broker.price.fact_advisory_revenue`: `advisory_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `advisory_sector_id`, `geography_id`, `fee_arrangement_id`, `advisory_fee_amount`
- `broker.price.fact_underwriting_revenue`: `underwriting_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `underwriting_fee_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (5) — Morgan Stanley

For Morgan Stanley, Why is asset management not a candidate for deploying capital if the business is already scaling?

- `broker.price.fact_asset_management_revenue`: `asset_management_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `fee_arrangement_id`, `management_fee_amount`, `performance_fee_amount`
- `broker.demand.fact_ficc_market_activity`: `ficc_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `trade_count`, `notional_amount`
- `broker.demand.fact_wealth_flows`: `wealth_flows_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `geography_id`, `net_new_asset_amount`, `asset_inflow_amount`, `asset_outflow_amount`, `client_account_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (6) — Morgan Stanley

For Morgan Stanley, With several rate cuts expected, what offsets keep net interest income steady?

- `broker.price.fact_deposit_margin`: `deposit_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `deposit_type_id`, `wealth_channel_id`, `deposit_net_interest_income_amount`, `average_deposit_rate_percent`
- `broker.price.fact_wealth_revenue`: `wealth_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `wealth_fee_amount`, `wealth_net_interest_income_amount`
- `broker.supply.fact_deposit_base`: `deposit_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `deposit_type_id`, `wealth_channel_id`, `deposit_balance_amount`, `deposit_account_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
