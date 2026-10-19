# Payments Inc price slice

This slice is part of the Payments Inc warehouse. Demand quantity, supply or capacity, and price or margin stay on separate facts. A quantity fact does not store a price. A price fact does not store the unit quantity; the denominator the price needs is a quantity or supply measure on its own fact, joined by the shared grain keys of fiscal quarter, scenario, and the business keys.

## Numbered questions

### Q2 2026 (2) — Mastercard

Did the World Cup lift the quarter's results, and should that moderate?

- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`
- `payments.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`

### Q2 2026 (4) — Mastercard

Is cyber demand inside value-added services tracking the strength seen in security software?

- `payments.price.fact_value_added_revenue`: `value_added_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_revenue_amount`
- `payments.price.fact_vas_margin`: `vas_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_operating_income_amount`, `vas_margin_percent`
- `payments.demand.fact_vas_transaction_volume`: `vas_transaction_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_transaction_quantity`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`

### Q2 2026 (5) — Mastercard

How broad-based is spending across income bands, and is the regional growth rate sustainable?

- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`
- `payments.price.fact_vas_margin`: `vas_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_operating_income_amount`, `vas_margin_percent`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`

### Q1 2026 (1) — Mastercard

How does the value-added-services strategy change around the planned divestiture?

- `payments.price.fact_value_added_revenue`: `value_added_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_revenue_amount`
- `payments.price.fact_vas_margin`: `vas_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_operating_income_amount`, `vas_margin_percent`
- `payments.demand.fact_vas_transaction_volume`: `vas_transaction_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_transaction_quantity`
- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`
- `payments.demand.fact_fraud_service_volume`: `fraud_service_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `fraud_type_id`, `value_added_service_id`, `fraud_protected_quantity`
- `payments.price.fact_data_product_revenue`: `data_product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `data_product_revenue_amount`

### Q1 2026 (3) — Mastercard

If the conflict runs longer, how does that change the industry and company outlook?

- `payments.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`
- `payments.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`

### Q1 2026 (6) — Mastercard

Has competitive intensity on deals changed?

- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_switched_transactions`: `switched_transactions_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `switched_transaction_quantity`

### Q1 2026 (7) — Mastercard

How does a stablecoin transaction compare economically with a local-currency transaction?

- `payments.price.fact_event_revenue`: `event_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `special_event_id`, `event_revenue_amount`
- `payments.demand.dim_cross_border_type`: `cross_border_type_id`, `cross_border_type_code`, `cross_border_type_name`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_switched_transactions`: `switched_transactions_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `switched_transaction_quantity`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`

### Q1 2026 (8) — Mastercard

What drove the uptick in the total-payments-advisory spread?

- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`
- `payments.demand.fact_commercial_volume`: `commercial_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `commercial_segment_id`, `commercial_volume_amount`

### Q1 2026 (9) — Mastercard

Was currency-neutral value-added-services growth steady organically after lapping Recorded Future?

- `payments.price.fact_value_added_revenue`: `value_added_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_revenue_amount`
- `payments.price.fact_vas_margin`: `vas_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_operating_income_amount`, `vas_margin_percent`
- `payments.demand.fact_vas_transaction_volume`: `vas_transaction_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_transaction_quantity`
- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`
- `payments.demand.fact_fraud_service_volume`: `fraud_service_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `fraud_type_id`, `value_added_service_id`, `fraud_protected_quantity`
- `payments.price.fact_data_product_revenue`: `data_product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `data_product_revenue_amount`

### Q4 2025 (4) — Mastercard

How does the 2026 renewal pipeline compare with 2025 on pricing and competitive intensity, and does a similar year imply a similar rebate-and-incentive outlook?

- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_event_revenue`: `event_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `special_event_id`, `event_revenue_amount`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`
- `payments.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`

### Q3 2025 (7) — Mastercard

Are recent infrastructure builds moving value-added services in the near term, and is the appetite greater for infrastructure or services assets?

- `payments.price.fact_value_added_revenue`: `value_added_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_revenue_amount`
- `payments.price.fact_vas_margin`: `vas_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_operating_income_amount`, `vas_margin_percent`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.demand.fact_vas_transaction_volume`: `vas_transaction_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_transaction_quantity`

### Q2 FY2026 (2) — Visa

Can a four-party network take on agent-transaction fraud risk the way American Express has in a three-party model?

- `payments.demand.dim_network_role`: `network_role_id`, `network_role_code`, `network_role_name`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`
- `payments.price.fact_revenue_line_fact`: `revenue_line_fact_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_line_id`, `revenue_line_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`

### Q2 FY2026 (6) — Visa

How much value-added-services strength is the World Cup versus a lasting step-up in fraud-protection demand?

- `payments.price.fact_value_added_revenue`: `value_added_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_revenue_amount`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`
- `payments.price.fact_vas_margin`: `vas_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_operating_income_amount`, `vas_margin_percent`
- `payments.demand.fact_fraud_service_volume`: `fraud_service_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `fraud_type_id`, `value_added_service_id`, `fraud_protected_quantity`
- `payments.demand.fact_vas_transaction_volume`: `vas_transaction_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_transaction_quantity`

### Q2 FY2026 (7) — Visa

As value-added services become a larger share of revenue, how do incremental margins compare with historical network margins?

- `payments.price.fact_value_added_revenue`: `value_added_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_revenue_amount`
- `payments.price.fact_vas_margin`: `vas_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_operating_income_amount`, `vas_margin_percent`
- `payments.price.fact_event_revenue`: `event_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `special_event_id`, `event_revenue_amount`
- `payments.demand.fact_vas_transaction_volume`: `vas_transaction_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_transaction_quantity`
- `payments.price.fact_data_product_revenue`: `data_product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `data_product_revenue_amount`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`

### Q2 FY2026 (8) — Visa

How large was the Ramadan effect on Middle East cross-border, once other one-time items are netted?

- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.demand.fact_cross_border_volume`: `cross_border_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_type_id`, `cross_border_volume_amount`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_cross_border_revenue`: `cross_border_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `corridor_id`, `cross_border_revenue_amount`

### Q1 FY2026 (1) — Visa

What value-added services are being purpose-built for major events?

- `payments.price.fact_value_added_revenue`: `value_added_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_revenue_amount`
- `payments.price.fact_vas_margin`: `vas_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_operating_income_amount`, `vas_margin_percent`
- `payments.demand.fact_vas_transaction_volume`: `vas_transaction_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_transaction_quantity`
- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`
- `payments.demand.fact_fraud_service_volume`: `fraud_service_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `fraud_type_id`, `value_added_service_id`, `fraud_protected_quantity`
- `payments.price.fact_data_product_revenue`: `data_product_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `data_product_revenue_amount`

### Q1 FY2026 (4) — Visa

Can value-added-services growth near 28% hold for the rest of the year, or was the quarter specific?

- `payments.price.fact_value_added_revenue`: `value_added_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_revenue_amount`
- `payments.price.fact_vas_margin`: `vas_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_operating_income_amount`, `vas_margin_percent`
- `payments.demand.fact_vas_transaction_volume`: `vas_transaction_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_transaction_quantity`
- `payments.demand.dim_scenario`: `scenario_id`, `scenario_code`, `scenario_name`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`

### Q4 FY2025 (2) — Visa

How much of the higher data-processing yield is value-added services?

- `payments.price.fact_value_added_revenue`: `value_added_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_revenue_amount`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_data_processing_revenue`: `data_processing_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `revenue_line_id`, `data_processing_revenue_amount`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`

### Q4 FY2025 (8) — Visa

Is the growth algorithm shifting because value-added services are a larger piece than a few years ago?

- `payments.price.fact_value_added_revenue`: `value_added_revenue_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_revenue_amount`
- `payments.price.fact_vas_margin`: `vas_margin_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_operating_income_amount`, `vas_margin_percent`
- `payments.demand.fact_vas_transaction_volume`: `vas_transaction_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `vas_transaction_quantity`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.demand.fact_visa_direct_volume`: `visa_direct_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `money_movement_type_id`, `card_type_id`, `visa_direct_volume_amount`
- `payments.supply.fact_fraud_capacity`: `fraud_capacity_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `value_added_service_id`, `protected_transaction_quantity`

### Q3 FY2025 (6) — Visa

Is the client-incentive rate, which has held near the high-20s percent, at an inflection because of renewal cycles?

- `payments.price.fact_incentive_rate`: `incentive_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `incentive_percent`
- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.price.fact_agentic_yield_rate`: `agentic_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `agentic_yield_percent`
- `payments.price.fact_enterprise_margin_py`: `enterprise_margin_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `operating_margin_percent`
- `payments.price.fact_incentives`: `incentives_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `incentive_amount`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`

### Q3 FY2025 (8) — Visa

Do stablecoins shrink, leave unchanged, or expand the payments revenue pool, and when does that become material?

- `payments.price.fact_net_yield_rate`: `net_yield_rate_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `net_yield_percent`, `yield_basis_points`
- `payments.demand.dim_reporting_unit`: `reporting_unit_id`, `reporting_unit_code`, `reporting_unit_name`
- `payments.demand.fact_gross_dollar_volume`: `gross_dollar_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `cross_border_type_id`, `gross_dollar_volume_amount`
- `payments.price.fact_enterprise_revenue_py`: `enterprise_revenue_py_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `net_revenue_amount`, `operating_income_amount`
- `payments.demand.fact_debit_volume`: `debit_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `payment_flow_id`, `debit_volume_amount`
- `payments.demand.fact_payments_volume`: `payments_volume_record_id`, `fiscal_quarter_id`, `scenario_id`, `reporting_unit_id`, `card_type_id`, `payment_flow_id`, `transaction_quantity`, `payment_volume_amount`
