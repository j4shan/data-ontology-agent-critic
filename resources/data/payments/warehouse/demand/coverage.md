# Payments Inc demand slice

This slice is part of the Payments Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q2 2026 (1) — Mastercard

Do agentic use cases such as microtransactions need stablecoins, or can existing Mastercard credentials cover them?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_agentic_volume`: `agentic_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `credential_type_id`, `agentic_transaction_quantity`, `agentic_volume_amount`
- `payments.supply.fact_acceptance_supply`: `acceptance_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `market_id`, `acceptance_location_quantity`, `merchant_quantity`
- `payments.supply.fact_credentials_supply`: `credentials_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `credential_type_id`, `active_credential_quantity`
- `payments.supply.fact_network_participants`: `network_participants_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `network_role_id`, `participant_quantity`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`

### Q2 2026 (3) — Mastercard

Which other markets are targeted for the domestic-switch style solutions already live in places such as the UAE?

- `payments.demand.dim_market`: `market_id`, `market_code`, `market_name`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`
- `payments.supply.fact_switch_capacity`: `switch_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `market_id`, `switch_capacity_quantity`
- `payments.demand.fact_switch_volume`: `switch_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `market_id`, `switch_transaction_quantity`
- `payments.price.fact_switch_revenue`: `switch_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `market_id`, `switch_revenue_amount`
- `payments.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`

### Q2 2026 (7) — Mastercard

What governance and first use cases should be expected for the agentic development roadmap?

- `payments.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `payments.demand.fact_agentic_volume`: `agentic_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `credential_type_id`, `agentic_transaction_quantity`, `agentic_volume_amount`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`
- `payments.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`

### Q2 2026 (8) — Mastercard

How should rebates and incentives as a percent of gross payments revenue trend in the back half?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.price.fact_event_revenue`: `event_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `special_event_id`, `event_revenue_amount`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`

### Q1 2026 (2) — Mastercard

Why has switched-transaction growth slowed from low double digits toward 9%?

- `payments.demand.fact_switched_transactions`: `switched_transactions_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `switched_transaction_quantity`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.demand.fact_agentic_volume`: `agentic_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `credential_type_id`, `agentic_transaction_quantity`, `agentic_volume_amount`
- `payments.demand.fact_token_volume`: `token_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `token_type_id`, `token_transaction_quantity`
- `payments.supply.fact_processing_capacity`: `processing_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `processing_asset_id`, `processing_capacity_quantity`, `processed_transaction_quantity`
- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`

### Q1 2026 (4) — Mastercard

What signals would cause a harder push on investment?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`
- `payments.price.fact_event_revenue`: `event_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `special_event_id`, `event_revenue_amount`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`

### Q1 2026 (5) — Mastercard

What is a normalized cross-border growth rate after Ramadan and Easter shifts?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.demand.dim_cross_border_type`: `cross_border_type_id`, `cross_border_type_code`, `cross_border_type_name`
- `payments.demand.fact_cross_border_by_flow`: `cross_border_by_flow_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `corridor_id`, `flow_cross_border_amount`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`

### Q4 2025 (1) — Mastercard

After the Capital One renegotiation, does Mastercard's share of that credit volume stay stable, or is volume migrating?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`
- `payments.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`

### Q4 2025 (2) — Mastercard

What is the consumer doing, and which spending patterns are changing?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_consumer_spend_volume`: `consumer_spend_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `income_cohort_id`, `region_id`, `consumer_spend_amount`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`

### Q4 2025 (3) — Mastercard

How sensitive is the business to foreign-exchange moves, and were guide rates set in a way that this FX trend continues?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `payments.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`

### Q4 2025 (5) — Mastercard

What consumer, domestic, and cross-border spend is in the guide, and is extra stimulus included?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.demand.fact_consumer_spend_volume`: `consumer_spend_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `income_cohort_id`, `region_id`, `consumer_spend_amount`
- `payments.demand.fact_cross_border_by_flow`: `cross_border_by_flow_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `corridor_id`, `flow_cross_border_amount`
- `payments.demand.dim_cross_border_type`: `cross_border_type_id`, `cross_border_type_code`, `cross_border_type_name`

### Q4 2025 (6) — Mastercard

How much 2026 pricing is built in relative to 2025?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`
- `payments.demand.fact_switched_transactions`: `switched_transactions_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `switched_transaction_quantity`

### Q4 2025 (7) — Mastercard

How should the pieces of the agentic-commerce suite be framed this early?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_agentic_volume`: `agentic_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `credential_type_id`, `agentic_transaction_quantity`, `agentic_volume_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`
- `payments.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `payments.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`

### Q4 2025 (8) — Mastercard

Which spending can be cut or redirected if it is no longer favored by customers, to limit downside to revenue and profit?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.price.fact_revenue_line_fact`: `revenue_line_fact_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_line_id`, `revenue_line_amount`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_cross_border_revenue`: `cross_border_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_revenue_amount`
- `payments.price.fact_fraud_service_revenue`: `fraud_service_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `fraud_type_id`, `fraud_revenue_amount`
- `payments.price.fact_data_product_revenue`: `data_product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `data_product_revenue_amount`

### Q3 2025 (1) — Mastercard

Is there evidence of trade-down or different behavior by consumer cohort, and how does that frame early holiday spend?

- `payments.demand.fact_consumer_spend_volume`: `consumer_spend_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `income_cohort_id`, `region_id`, `consumer_spend_amount`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.supply.fact_network_participants`: `network_participants_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `network_role_id`, `participant_quantity`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`

### Q3 2025 (2) — Mastercard

Which growth drivers last through the next twelve to eighteen months, and how much is tokenization feeding agentic commerce?

- `payments.demand.fact_agentic_volume`: `agentic_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `credential_type_id`, `agentic_transaction_quantity`, `agentic_volume_amount`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`

### Q3 2025 (3) — Mastercard

What legal and risk issues come with accelerating agentic commerce?

- `payments.demand.fact_agentic_volume`: `agentic_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `credential_type_id`, `agentic_transaction_quantity`, `agentic_volume_amount`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`
- `payments.demand.fact_consumer_spend_volume`: `consumer_spend_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `income_cohort_id`, `region_id`, `consumer_spend_amount`
- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`

### Q3 2025 (4) — Mastercard

Why has rent acceptance not scaled, and what would change that new acceptance channel?

- `payments.supply.dim_acceptance_type`: `acceptance_type_id`, `acceptance_type_code`, `acceptance_type_name`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.demand.fact_agentic_volume`: `agentic_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `credential_type_id`, `agentic_transaction_quantity`, `agentic_volume_amount`
- `payments.demand.fact_consumer_spend_volume`: `consumer_spend_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `income_cohort_id`, `region_id`, `consumer_spend_amount`
- `payments.supply.fact_acceptance_supply`: `acceptance_supply_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `market_id`, `acceptance_location_quantity`, `merchant_quantity`

### Q3 2025 (5) — Mastercard

How can Mastercard take share in agentic commerce, and against whom?

- `payments.demand.fact_agentic_volume`: `agentic_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `credential_type_id`, `agentic_transaction_quantity`, `agentic_volume_amount`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.demand.fact_consumer_spend_volume`: `consumer_spend_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `income_cohort_id`, `region_id`, `consumer_spend_amount`
- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`

### Q3 2025 (6) — Mastercard

What early advertiser feedback and distribution plan sit behind the advertising announcement, including return on ad spend?

- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`
- `payments.demand.fact_consumer_spend_volume`: `consumer_spend_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `income_cohort_id`, `region_id`, `consumer_spend_amount`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`

### Q3 2025 (8) — Mastercard

Inside card-not-present and travel, which verticals or corridors are shifting?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.dim_card_type`: `card_type_id`, `card_type_code`, `card_type_name`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`
- `payments.demand.dim_fiscal_quarter`: `fiscal_quarter_id`, `fiscal_quarter_code`, `fiscal_quarter_name`

### Q3 2025 (9) — Mastercard

How much of a moat are licenses and merchant, PSP, and acquirer relationships, and does partnering with other networks change quality versus building alone?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.price.fact_event_revenue`: `event_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `special_event_id`, `event_revenue_amount`
- `payments.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`
- `payments.demand.fact_agentic_volume`: `agentic_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `credential_type_id`, `agentic_transaction_quantity`, `agentic_volume_amount`

### Q3 2025 (10) — Mastercard

Can the recent core-payments trend continue in 2026, and is there still pricing power in that business?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`

### Q2 FY2026 (1) — Visa

What drove the quarter's upside, and how does that change the second-half outlook?

- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`
- `payments.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`

### Q2 FY2026 (3) — Visa

Are agentic transactions accretive or dilutive on unit economics, and do they add to existing volume?

- `payments.demand.fact_agentic_volume`: `agentic_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `credential_type_id`, `agentic_transaction_quantity`, `agentic_volume_amount`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`

### Q2 FY2026 (4) — Visa

Why do the two programs matter to the payments ecosystem, and what does that data mean for Visa?

- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`
- `payments.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `payments.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`

### Q2 FY2026 (5) — Visa

What has driven the strongest contributors, and how sustainable are they?

- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`
- `payments.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`

### Q2 FY2026 (9) — Visa

Should the multiyear growth view for the newer commercial and money-movement businesses be reset higher?

- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `payments.demand.fact_money_movement_volume`: `money_movement_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `money_movement_volume_amount`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`
- `payments.price.fact_money_movement_revenue`: `money_movement_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `money_movement_revenue_amount`

### Q2 FY2026 (10) — Visa

Is monetization of the new capability a value-added-services fee or another line, and are more large banks the target?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.price.fact_value_added_revenue`: `value_added_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_revenue_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_vas_margin`: `vas_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_operating_income_amount`, `vas_margin_percent`
- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`

### Q1 FY2026 (2) — Visa

How would implementation of the credit-card competition proposal change routing and Visa's issuer relationships?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`
- `payments.demand.dim_card_type`: `card_type_id`, `card_type_code`, `card_type_name`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`

### Q1 FY2026 (3) — Visa

What drove better-than-expected commercial growth?

- `payments.demand.fact_commercial_volume`: `commercial_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `commercial_segment_id`, `commercial_volume_amount`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_commercial_revenue`: `commercial_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `commercial_segment_id`, `commercial_revenue_amount`
- `payments.demand.dim_card_type`: `card_type_id`, `card_type_code`, `card_type_name`
- `payments.demand.dim_commercial_segment`: `commercial_segment_id`, `commercial_segment_code`, `commercial_segment_name`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`

### Q1 FY2026 (5) — Visa

When does Flex Credential volume become large enough to bend the growth curve?

- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`
- `payments.demand.fact_agentic_volume`: `agentic_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `credential_type_id`, `agentic_transaction_quantity`, `agentic_volume_amount`
- `payments.price.fact_incentives`: `incentives_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `incentive_amount`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`

### Q1 FY2026 (6) — Visa

How much technology has been invested in the processing assets, and is that where momentum is showing up?

- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_data_processing_revenue`: `data_processing_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_line_id`, `data_processing_revenue_amount`

### Q1 FY2026 (7) — Visa

Is stablecoin growth more about settling payments or about disbursements and other money movement?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.demand.fact_money_movement_volume`: `money_movement_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `money_movement_volume_amount`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`

### Q1 FY2026 (8) — Visa

Is Pismo winning more with large or small banks, and how much larger could it be in two to three years?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`

### Q4 FY2025 (1) — Visa

Is agentic commerce a substitute for traditional ecommerce or an addition to the payments market?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`
- `payments.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `payments.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`

### Q4 FY2025 (4) — Visa

How does Visa's trusted-agent protocol differ from Stripe's agentic protocol, and which layer does each cover?

- `payments.demand.fact_agentic_volume`: `agentic_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `credential_type_id`, `agentic_transaction_quantity`, `agentic_volume_amount`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.demand.fact_consumer_spend_volume`: `consumer_spend_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `income_cohort_id`, `region_id`, `consumer_spend_amount`
- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`

### Q4 FY2025 (5) — Visa

How is cross-border growth splitting among ecommerce and travel?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.demand.fact_cross_border_by_flow`: `cross_border_by_flow_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `corridor_id`, `flow_cross_border_amount`
- `payments.demand.fact_travel_volume`: `travel_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `travel_volume_amount`
- `payments.demand.dim_cross_border_type`: `cross_border_type_id`, `cross_border_type_code`, `cross_border_type_name`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`

### Q4 FY2025 (6) — Visa

Where are the most tangible stablecoin opportunities over the next few years, including cards and banking-as-a-service?

- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.price.fact_value_added_revenue`: `value_added_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_revenue_amount`

### Q4 FY2025 (7) — Visa

Is the improvement in China timing sustainable?

- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`

### Q4 FY2025 (9) — Visa

Is higher spending opportunistic, or a structural need as more layers of the service stack scale?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.demand.dim_cross_border_type`: `cross_border_type_id`, `cross_border_type_code`, `cross_border_type_name`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_value_added_revenue`: `value_added_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_revenue_amount`

### Q3 FY2025 (1) — Visa

What bridges the deceleration from the prior quarter's growth rate?

- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_enterprise_margin_py`: `enterprise_margin_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`

### Q3 FY2025 (2) — Visa

Are investment priorities shifting toward AI and stablecoins?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.demand.fact_agentic_volume`: `agentic_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `credential_type_id`, `agentic_transaction_quantity`, `agentic_volume_amount`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.demand.fact_consumer_spend_volume`: `consumer_spend_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `income_cohort_id`, `region_id`, `consumer_spend_amount`
- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`

### Q3 FY2025 (3) — Visa

Why did the spread between international transaction fees and nominal cross-border volume compress to under a point?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_cross_border_revenue`: `cross_border_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_revenue_amount`
- `payments.demand.fact_cross_border_by_flow`: `cross_border_by_flow_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `corridor_id`, `flow_cross_border_amount`

### Q3 FY2025 (4) — Visa

How important is Visa Direct, especially debit, inside the volume-growth algorithm?

- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`

### Q3 FY2025 (5) — Visa

In cross-border money movement, do stablecoins matter more for pricing or for settlement, and who captures the value?

- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`
- `payments.price.fact_cross_border_revenue`: `cross_border_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_revenue_amount`
- `payments.demand.fact_cross_border_by_flow`: `cross_border_by_flow_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `corridor_id`, `flow_cross_border_amount`

### Q3 FY2025 (7) — Visa

Which corridors changed into July beyond inbound U.S. from Canada, including Europe to the U.S.?

- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.price.fact_enterprise_margin_py`: `enterprise_margin_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `payments.price.fact_revenue_line_fact`: `revenue_line_fact_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_line_id`, `revenue_line_amount`
