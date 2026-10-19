# Payments Inc supply slice

This slice is part of the Payments Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q2 2026 (6) — Mastercard

How does being network-agnostic change the cyber, fraud, and identity services portfolio?

- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`
- `payments.price.fact_fraud_service_revenue`: `fraud_service_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `fraud_type_id`, `fraud_revenue_amount`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.price.fact_value_added_revenue`: `value_added_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_revenue_amount`
- `payments.price.fact_vas_margin`: `vas_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_operating_income_amount`, `vas_margin_percent`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`

### Q1 FY2026 (9) — Visa

How do more tokens change conversations with issuers, merchants, and acquirers?

- `payments.supply.fact_network_participants`: `network_participants_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `network_role_id`, `participant_quantity`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`
- `payments.demand.fact_agentic_volume`: `agentic_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `credential_type_id`, `agentic_transaction_quantity`, `agentic_volume_amount`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`

### Q4 FY2025 (3) — Visa

How much of the fraud and identity opportunity will Visa participate in versus other providers?

- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`
- `payments.price.fact_fraud_service_revenue`: `fraud_service_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `fraud_type_id`, `fraud_revenue_amount`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
