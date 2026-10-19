# Broker Inc demand slice

This slice is part of the Broker Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q2 2026 (2) — Goldman Sachs

For Goldman Sachs, Across markets, where is incremental capital best allocated?

- `broker.demand.fact_issuance_volume`: `issuance_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `client_type_id`, `issuance_count`, `issued_principal_amount`
- `broker.demand.fact_equities_market_activity`: `equities_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `market_share_volume_quantity`, `client_share_volume_quantity`, `trade_count`
- `broker.demand.fact_ficc_market_activity`: `ficc_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `trade_count`, `notional_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (3) — Goldman Sachs

For Goldman Sachs, How durable is the AI capital-expenditure cycle if the market is showing more greed than fear?

- `broker.demand.fact_issuance_volume`: `issuance_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `client_type_id`, `issuance_count`, `issued_principal_amount`
- `broker.demand.fact_equities_market_activity`: `equities_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `market_share_volume_quantity`, `client_share_volume_quantity`, `trade_count`
- `broker.demand.fact_ficc_market_activity`: `ficc_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `trade_count`, `notional_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (5) — Goldman Sachs

For Goldman Sachs, How much does the supplementary leverage ratio constrain growth in financing?

- `broker.demand.fact_financing_demand`: `financing_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `client_type_id`, `geography_id`, `loan_commitment_amount`, `drawn_loan_balance_amount`, `financing_request_count`
- `broker.supply.fact_balance_sheet_capacity`: `balance_sheet_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `balance_category_id`, `reporting_unit_id`, `balance_amount`, `risk_weighted_asset_amount`, `leverage_exposure_amount`
- `broker.supply.fact_syndication`: `syndication_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `client_type_id`, `retained_financing_amount`, `syndicated_financing_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (8) — Goldman Sachs

For Goldman Sachs, How much of Global Banking and Markets loan growth is FICC financing versus deal financing, and how much more balance sheet can be allocated given the M&A backdrop?

- `broker.demand.fact_financing_demand`: `financing_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `client_type_id`, `geography_id`, `loan_commitment_amount`, `drawn_loan_balance_amount`, `financing_request_count`
- `broker.price.fact_financing_revenue`: `financing_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `client_type_id`, `financing_revenue_amount`, `financing_spread_basis_points`
- `broker.supply.fact_syndication`: `syndication_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `client_type_id`, `retained_financing_amount`, `syndicated_financing_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (3) — Goldman Sachs

For Goldman Sachs, How has the sponsor pipeline changed on valuation versus timing with markets still near highs despite the Middle East conflict?

- `broker.demand.fact_equities_market_activity`: `equities_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `market_share_volume_quantity`, `client_share_volume_quantity`, `trade_count`
- `broker.price.fact_wallet_share`: `wallet_share_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `wallet_share_percent`, `desk_revenue_amount`
- `broker.demand.fact_deal_pipeline`: `deal_pipeline_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `deal_stage_id`, `advisory_sector_id`, `geography_id`, `sponsor_type_id`, `deal_count`, `deal_value_amount`, `active_mandate_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (8) — Goldman Sachs

For Goldman Sachs, What is a reasonable penetration goal for lending inside wealth, and does credit stay as large a growth contributor?

- `broker.demand.fact_private_credit_demand`: `private_credit_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `wealth_channel_id`, `client_type_id`, `subscription_amount`, `subscribing_client_count`
- `broker.supply.fact_wealth_lending`: `wealth_lending_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `wealth_channel_id`, `collateral_type_id`, `wealth_loan_balance_amount`, `borrowing_client_count`
- `broker.demand.fact_wealth_flows`: `wealth_flows_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `geography_id`, `net_new_asset_amount`, `asset_inflow_amount`, `asset_outflow_amount`, `client_account_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (3) — Goldman Sachs

For Goldman Sachs, If the right deal appeared, would a large asset-and-wealth acquisition be used to shift the mix?

- `broker.demand.fact_wealth_flows`: `wealth_flows_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `geography_id`, `net_new_asset_amount`, `asset_inflow_amount`, `asset_outflow_amount`, `client_account_count`
- `broker.supply.fact_syndication`: `syndication_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `client_type_id`, `retained_financing_amount`, `syndicated_financing_amount`
- `broker.price.fact_wealth_revenue`: `wealth_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `wealth_fee_amount`, `wealth_net_interest_income_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (4) — Goldman Sachs

For Goldman Sachs, What inning is the capital-markets cycle in, and which issuance sits in banking versus other lines?

- `broker.demand.fact_issuance_volume`: `issuance_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `client_type_id`, `issuance_count`, `issued_principal_amount`
- `broker.demand.fact_deal_pipeline`: `deal_pipeline_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `deal_stage_id`, `advisory_sector_id`, `geography_id`, `sponsor_type_id`, `deal_count`, `deal_value_amount`, `active_mandate_count`
- `broker.demand.fact_equities_market_activity`: `equities_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `market_share_volume_quantity`, `client_share_volume_quantity`, `trade_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (3) — Goldman Sachs

For Goldman Sachs, Are the large strategic deals happening, and in which geographies?

- `broker.demand.fact_deal_pipeline`: `deal_pipeline_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `deal_stage_id`, `advisory_sector_id`, `geography_id`, `sponsor_type_id`, `deal_count`, `deal_value_amount`, `active_mandate_count`
- `broker.demand.fact_equities_market_activity`: `equities_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `market_share_volume_quantity`, `client_share_volume_quantity`, `trade_count`
- `broker.demand.fact_sponsor_activity`: `sponsor_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `sponsor_type_id`, `advisory_sector_id`, `geography_id`, `sponsor_deal_count`, `active_sponsor_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (6) — Goldman Sachs

For Goldman Sachs, How could tokenization change market structure, and how would Goldman participate once rules are clear?

- `broker.demand.fact_equities_market_activity`: `equities_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `market_share_volume_quantity`, `client_share_volume_quantity`, `trade_count`
- `broker.price.fact_wallet_share`: `wallet_share_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `wallet_share_percent`, `desk_revenue_amount`
- `broker.demand.fact_issuance_volume`: `issuance_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `client_type_id`, `issuance_count`, `issued_principal_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (7) — Goldman Sachs

For Goldman Sachs, If investment banking and issuance accelerate, can trading stay this robust or should markets moderate?

- `broker.demand.fact_issuance_volume`: `issuance_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `client_type_id`, `issuance_count`, `issued_principal_amount`
- `broker.price.fact_markets_revenue_mix`: `markets_revenue_mix_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `revenue_line_id`, `markets_revenue_amount`
- `broker.demand.fact_equities_market_activity`: `equities_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `market_share_volume_quantity`, `client_share_volume_quantity`, `trade_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (2) — Morgan Stanley

For Morgan Stanley, What share of current investment raises productivity over the next few years without a change in strategic targets?

- `broker.demand.fact_equities_market_activity`: `equities_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `market_share_volume_quantity`, `client_share_volume_quantity`, `trade_count`
- `broker.price.fact_equities_revenue`: `equities_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `client_type_id`, `equities_revenue_amount`
- `broker.price.fact_wallet_share`: `wallet_share_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `wallet_share_percent`, `desk_revenue_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (3) — Morgan Stanley

For Morgan Stanley, When workplace stock is recognized, does it arrive at the IPO, on a vesting schedule, and as self-directed assets before it becomes advisor-led?

- `broker.demand.fact_workplace_conversion`: `workplace_conversion_record_id`, `fiscal_quarter_id`, `scenario_id`, `workplace_stage_id`, `wealth_channel_id`, `participant_count`, `converted_account_count`, `workplace_asset_amount`
- `broker.demand.fact_deal_pipeline`: `deal_pipeline_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `deal_stage_id`, `advisory_sector_id`, `geography_id`, `sponsor_type_id`, `deal_count`, `deal_value_amount`, `active_mandate_count`
- `broker.demand.fact_wealth_flows`: `wealth_flows_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `geography_id`, `net_new_asset_amount`, `asset_inflow_amount`, `asset_outflow_amount`, `client_account_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (4) — Morgan Stanley

For Morgan Stanley, How do today's investment-banking opportunities compare with history by geography, and what did the sponsor comment imply?

- `broker.demand.fact_sponsor_activity`: `sponsor_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `sponsor_type_id`, `advisory_sector_id`, `geography_id`, `sponsor_deal_count`, `active_sponsor_count`
- `broker.supply.fact_credit_exposure`: `credit_exposure_record_id`, `fiscal_quarter_id`, `scenario_id`, `credit_quality_id`, `counterparty_type_id`, `geography_id`, `risk_category_id`, `credit_exposure_amount`, `watched_exposure_amount`
- `broker.price.fact_wallet_share`: `wallet_share_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `wallet_share_percent`, `desk_revenue_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (6) — Morgan Stanley

For Morgan Stanley, How is workplace competition changing, and what is being done to hold historically high client conversion?

- `broker.demand.fact_workplace_conversion`: `workplace_conversion_record_id`, `fiscal_quarter_id`, `scenario_id`, `workplace_stage_id`, `wealth_channel_id`, `participant_count`, `converted_account_count`, `workplace_asset_amount`
- `broker.demand.fact_client_activity`: `client_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `client_type_id`, `geography_id`, `reporting_unit_id`, `active_client_count`, `client_trade_count`, `client_meeting_count`
- `broker.demand.fact_financing_demand`: `financing_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `client_type_id`, `geography_id`, `loan_commitment_amount`, `drawn_loan_balance_amount`, `financing_request_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2026 (8) — Morgan Stanley

For Morgan Stanley, What indicators would show activity cracking from here?

- `broker.demand.fact_equities_market_activity`: `equities_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `market_share_volume_quantity`, `client_share_volume_quantity`, `trade_count`
- `broker.demand.fact_ficc_market_activity`: `ficc_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `trade_count`, `notional_amount`
- `broker.demand.fact_client_activity`: `client_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `client_type_id`, `geography_id`, `reporting_unit_id`, `active_client_count`, `client_trade_count`, `client_meeting_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (1) — Morgan Stanley

For Morgan Stanley, How does stress in private credit change distribution of those products through the wealth channel?

- `broker.demand.fact_private_credit_demand`: `private_credit_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `wealth_channel_id`, `client_type_id`, `subscription_amount`, `subscribing_client_count`
- `broker.demand.fact_wealth_flows`: `wealth_flows_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `geography_id`, `net_new_asset_amount`, `asset_inflow_amount`, `asset_outflow_amount`, `client_account_count`
- `broker.supply.fact_advisor_capacity`: `advisor_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `employee_group_id`, `wealth_channel_id`, `advisor_count`, `client_household_count`, `open_advisor_role_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (2) — Morgan Stanley

For Morgan Stanley, What is driving organic growth in wealth beyond workplace?

- `broker.demand.fact_wealth_flows`: `wealth_flows_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `geography_id`, `net_new_asset_amount`, `asset_inflow_amount`, `asset_outflow_amount`, `client_account_count`
- `broker.demand.fact_workplace_conversion`: `workplace_conversion_record_id`, `fiscal_quarter_id`, `scenario_id`, `workplace_stage_id`, `wealth_channel_id`, `participant_count`, `converted_account_count`, `workplace_asset_amount`
- `broker.demand.fact_private_credit_demand`: `private_credit_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `wealth_channel_id`, `client_type_id`, `subscription_amount`, `subscribing_client_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (4) — Morgan Stanley

For Morgan Stanley, Under the proposed capital rules, which businesses become more attractive to lean into?

- `broker.demand.fact_issuance_volume`: `issuance_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `client_type_id`, `issuance_count`, `issued_principal_amount`
- `broker.supply.fact_capital_capacity`: `capital_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `capital_instrument_id`, `reporting_unit_id`, `capital_amount`, `required_capital_amount`
- `broker.price.fact_underwriting_revenue`: `underwriting_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `underwriting_fee_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (6) — Morgan Stanley

For Morgan Stanley, Is concern about private credit coming from advisors or from investors, and are clients looking at asset classes other than credit?

- `broker.demand.fact_private_credit_demand`: `private_credit_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `asset_class_id`, `wealth_channel_id`, `client_type_id`, `subscription_amount`, `subscribing_client_count`
- `broker.demand.fact_wealth_flows`: `wealth_flows_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `geography_id`, `net_new_asset_amount`, `asset_inflow_amount`, `asset_outflow_amount`, `client_account_count`
- `broker.supply.fact_credit_exposure`: `credit_exposure_record_id`, `fiscal_quarter_id`, `scenario_id`, `credit_quality_id`, `counterparty_type_id`, `geography_id`, `risk_category_id`, `credit_exposure_amount`, `watched_exposure_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (8) — Morgan Stanley

For Morgan Stanley, How sustainable is Asia momentum beyond prime brokerage?

- `broker.demand.fact_deal_pipeline`: `deal_pipeline_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `deal_stage_id`, `advisory_sector_id`, `geography_id`, `sponsor_type_id`, `deal_count`, `deal_value_amount`, `active_mandate_count`
- `broker.demand.fact_issuance_volume`: `issuance_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `client_type_id`, `issuance_count`, `issued_principal_amount`
- `broker.demand.fact_equities_market_activity`: `equities_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `market_share_volume_quantity`, `client_share_volume_quantity`, `trade_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (9) — Morgan Stanley

For Morgan Stanley, How is E*TRADE used in the selling process, and what does the sponsor-led pipeline look like?

- `broker.demand.fact_deal_pipeline`: `deal_pipeline_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `deal_stage_id`, `advisory_sector_id`, `geography_id`, `sponsor_type_id`, `deal_count`, `deal_value_amount`, `active_mandate_count`
- `broker.demand.fact_equities_market_activity`: `equities_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `market_share_volume_quantity`, `client_share_volume_quantity`, `trade_count`
- `broker.demand.fact_ficc_market_activity`: `ficc_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `trade_count`, `notional_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (1) — Morgan Stanley

For Morgan Stanley, Why were targets left unchanged, and which businesses look like they are at a peak and over-earning?

- `broker.demand.fact_equities_market_activity`: `equities_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `market_share_volume_quantity`, `client_share_volume_quantity`, `trade_count`
- `broker.price.fact_equities_revenue`: `equities_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `client_type_id`, `equities_revenue_amount`
- `broker.price.fact_enterprise_results`: `enterprise_results_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `total_revenue_amount`, `operating_income_amount`, `net_income_amount`, `diluted_earnings_per_share`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (3) — Morgan Stanley

For Morgan Stanley, Can the client wallet keep expanding for secular rather than cyclical reasons?

- `broker.demand.fact_client_activity`: `client_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `client_type_id`, `geography_id`, `reporting_unit_id`, `active_client_count`, `client_trade_count`, `client_meeting_count`
- `broker.demand.fact_financing_demand`: `financing_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `client_type_id`, `geography_id`, `loan_commitment_amount`, `drawn_loan_balance_amount`, `financing_request_count`
- `broker.demand.fact_wealth_flows`: `wealth_flows_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `geography_id`, `net_new_asset_amount`, `asset_inflow_amount`, `asset_outflow_amount`, `client_account_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (6) — Morgan Stanley

For Morgan Stanley, Where is investment going back into the business to build moats while results make higher highs and higher lows?

- `broker.demand.fact_wealth_flows`: `wealth_flows_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `geography_id`, `net_new_asset_amount`, `asset_inflow_amount`, `asset_outflow_amount`, `client_account_count`
- `broker.price.fact_wealth_revenue`: `wealth_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `wealth_fee_amount`, `wealth_net_interest_income_amount`
- `broker.price.fact_enterprise_results`: `enterprise_results_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `total_revenue_amount`, `operating_income_amount`, `net_income_amount`, `diluted_earnings_per_share`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (2) — Morgan Stanley

For Morgan Stanley, Is boardroom tolerance for macro volatility higher than in the spring tariff shock, even as tariff rhetoric picks up again?

- `broker.demand.fact_equities_market_activity`: `equities_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `market_share_volume_quantity`, `client_share_volume_quantity`, `trade_count`
- `broker.demand.fact_ficc_market_activity`: `ficc_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `trade_count`, `notional_amount`
- `broker.demand.fact_client_activity`: `client_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `client_type_id`, `geography_id`, `reporting_unit_id`, `active_client_count`, `client_trade_count`, `client_meeting_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (3) — Morgan Stanley

For Morgan Stanley, Beyond new-adviser strength, how are wealth flows trending, and what is the recruiting backdrop?

- `broker.demand.fact_wealth_flows`: `wealth_flows_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `geography_id`, `net_new_asset_amount`, `asset_inflow_amount`, `asset_outflow_amount`, `client_account_count`
- `broker.price.fact_wealth_revenue`: `wealth_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `asset_class_id`, `wealth_fee_amount`, `wealth_net_interest_income_amount`
- `broker.price.fact_sweep_margin`: `sweep_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `sweep_net_interest_income_amount`, `sweep_spread_percent`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q2 2025 (4) — Morgan Stanley

For Morgan Stanley, How do stablecoins and tokenization change market structure once legislation passes, and how would the firm participate?

- `broker.demand.fact_issuance_volume`: `issuance_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `issuance_type_id`, `advisory_sector_id`, `geography_id`, `client_type_id`, `issuance_count`, `issued_principal_amount`
- `broker.demand.fact_equities_market_activity`: `equities_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `market_share_volume_quantity`, `client_share_volume_quantity`, `trade_count`
- `broker.demand.fact_ficc_market_activity`: `ficc_market_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `geography_id`, `client_type_id`, `trade_count`, `notional_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
