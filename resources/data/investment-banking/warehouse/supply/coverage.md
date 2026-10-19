# Broker Inc supply slice

This slice is part of the Broker Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q1 2026 (4) — Goldman Sachs

For Goldman Sachs, Were extra provisions taken for macro problem losses beyond what is already visible?

- `broker.supply.fact_credit_exposure`: `credit_exposure_record_id`, `fiscal_quarter_id`, `scenario_id`, `credit_quality_id`, `counterparty_type_id`, `geography_id`, `risk_category_id`, `credit_exposure_amount`, `watched_exposure_amount`
- `broker.price.fact_provision_expense`: `provision_expense_record_id`, `fiscal_quarter_id`, `scenario_id`, `credit_quality_id`, `counterparty_type_id`, `provision_amount`, `net_charge_off_amount`
- `broker.demand.fact_deal_pipeline`: `deal_pipeline_record_id`, `fiscal_quarter_id`, `scenario_id`, `deal_type_id`, `deal_stage_id`, `advisory_sector_id`, `geography_id`, `sponsor_type_id`, `deal_count`, `deal_value_amount`, `active_mandate_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (7) — Goldman Sachs

For Goldman Sachs, Was weaker intermediation a tougher comparison, geopolitics, or client behavior that could last the rest of the year?

- `broker.supply.fact_deposit_base`: `deposit_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `deposit_type_id`, `wealth_channel_id`, `deposit_balance_amount`, `deposit_account_count`
- `broker.supply.fact_wealth_lending`: `wealth_lending_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `wealth_channel_id`, `collateral_type_id`, `wealth_loan_balance_amount`, `borrowing_client_count`
- `broker.demand.fact_client_activity`: `client_activity_record_id`, `fiscal_quarter_id`, `scenario_id`, `client_type_id`, `geography_id`, `reporting_unit_id`, `active_client_count`, `client_trade_count`, `client_meeting_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q1 2026 (10) — Goldman Sachs

For Goldman Sachs, Did the leverage-ratio change make acquisition financing more competitive, and how much of that financing is kept versus syndicated?

- `broker.supply.fact_syndication`: `syndication_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `client_type_id`, `retained_financing_amount`, `syndicated_financing_amount`
- `broker.demand.fact_financing_demand`: `financing_demand_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `client_type_id`, `geography_id`, `loan_commitment_amount`, `drawn_loan_balance_amount`, `financing_request_count`
- `broker.price.fact_ficc_revenue`: `ficc_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `product_desk_id`, `trading_activity_id`, `geography_id`, `ficc_revenue_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (5) — Goldman Sachs

For Goldman Sachs, Which backlogs are expected to turn into production through 2026?

- `broker.supply.fact_balance_sheet_capacity`: `balance_sheet_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `balance_category_id`, `reporting_unit_id`, `balance_amount`, `risk_weighted_asset_amount`, `leverage_exposure_amount`
- `broker.supply.fact_capital_capacity`: `capital_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `capital_instrument_id`, `reporting_unit_id`, `capital_amount`, `required_capital_amount`
- `broker.supply.fact_risk_capacity`: `risk_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `risk_category_id`, `reporting_unit_id`, `risk_weighted_asset_amount`, `risk_limit_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (6) — Goldman Sachs

For Goldman Sachs, What happens to Apple-related deposits that may run off, and what limited operating leverage in the quarter?

- `broker.supply.fact_balance_sheet_capacity`: `balance_sheet_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `balance_category_id`, `reporting_unit_id`, `balance_amount`, `risk_weighted_asset_amount`, `leverage_exposure_amount`
- `broker.supply.fact_deposit_base`: `deposit_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `deposit_type_id`, `wealth_channel_id`, `deposit_balance_amount`, `deposit_account_count`
- `broker.price.fact_enterprise_results`: `enterprise_results_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `total_revenue_amount`, `operating_income_amount`, `net_income_amount`, `diluted_earnings_per_share`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (10) — Goldman Sachs

For Goldman Sachs, How much of wealth growth is more production from existing advisers and clients versus hiring advisers and new customers?

- `broker.supply.fact_wealth_lending`: `wealth_lending_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `wealth_channel_id`, `collateral_type_id`, `wealth_loan_balance_amount`, `borrowing_client_count`
- `broker.supply.fact_client_cash`: `client_cash_record_id`, `fiscal_quarter_id`, `scenario_id`, `wealth_channel_id`, `deposit_type_id`, `client_cash_balance_amount`, `cash_holding_client_count`
- `broker.supply.fact_deposit_base`: `deposit_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `deposit_type_id`, `wealth_channel_id`, `deposit_balance_amount`, `deposit_account_count`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`

### Q4 2025 (4) — Morgan Stanley

For Morgan Stanley, Is trading later in its cycle than investment banking, and where do AI opportunities and risks sit on that path?

- `broker.supply.fact_balance_sheet_capacity`: `balance_sheet_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `balance_category_id`, `reporting_unit_id`, `balance_amount`, `risk_weighted_asset_amount`, `leverage_exposure_amount`
- `broker.supply.fact_deposit_base`: `deposit_base_record_id`, `fiscal_quarter_id`, `scenario_id`, `deposit_type_id`, `wealth_channel_id`, `deposit_balance_amount`, `deposit_account_count`
- `broker.supply.fact_syndication`: `syndication_record_id`, `fiscal_quarter_id`, `scenario_id`, `loan_type_id`, `client_type_id`, `retained_financing_amount`, `syndicated_financing_amount`
- `broker.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`
- `broker.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
