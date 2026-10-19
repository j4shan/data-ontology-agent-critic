# Surgical Supply Inc finance and payment context

Enterprise and Stryker segment finance, tariffs, hospital capital budgets, and provider payment context separate from maker revenue.

Every fact below uses `fiscal_period_id` for the fiscal period and `scenario_id` for the scenario (`reported` or `guide` in `dim_scenario`). Measure descriptions in the YAML name the unit.

## Stryker (SYK)

### Q2 2026 (3)

What margin and earnings path is embedded in the second-half outlook?

- `surgicalsupply.finance.fact_enterprise_amount`: `revenue_amount`, `gross_profit_amount`, `operating_income_amount`
- `surgicalsupply.finance.fact_enterprise_margin_rate`: `gross_margin_rate`, `operating_margin_rate`, `revenue_growth_rate`
- `surgicalsupply.finance.fact_stryker_segment_amount`: `segment_revenue_amount`, `segment_operating_income_amount`, `stryker_segment_id`

### Q2 2026 (4)

How is the orthopedic industry responding to the large Medicare cut in hip, knee, and shoulder physician payment?

- `surgicalsupply.payment.fact_payment_context_amount`: `provider_payment_amount`, `payer_type_id`, `payment_program_id`
- `surgicalsupply.payment.fact_payment_change_rate`: `payment_change_rate`
- `surgicalsupply.procedure.fact_company_procedure_quantity`: `company_procedure_count`, `procedure_family_id`

### Q1 2026 (2)

Is operating margin still expected to be up about 50 basis points this year, and how are higher input costs being offset?

- `surgicalsupply.finance.fact_enterprise_amount`: `revenue_amount`, `gross_profit_amount`, `operating_income_amount`
- `surgicalsupply.finance.fact_enterprise_margin_rate`: `gross_margin_rate`, `operating_margin_rate`, `revenue_growth_rate`
- `surgicalsupply.finance.fact_stryker_segment_amount`: `segment_revenue_amount`, `segment_operating_income_amount`, `stryker_segment_id`

### Q4 2025 (1)

What supports starting the year with slightly higher organic-growth guidance, and is a 10% year still possible?

- `surgicalsupply.finance.fact_enterprise_amount`: `revenue_amount`, `gross_profit_amount`, `operating_income_amount`
- `surgicalsupply.finance.fact_enterprise_margin_rate`: `gross_margin_rate`, `operating_margin_rate`, `revenue_growth_rate`
- `surgicalsupply.finance.fact_stryker_segment_amount`: `segment_revenue_amount`, `segment_operating_income_amount`, `stryker_segment_id`

### Q4 2025 (5)

Are patient volumes being affected by changes in exchange coverage?

- `surgicalsupply.payment.fact_payment_context_amount`: `provider_payment_amount`, `payer_type_id`, `payment_program_id`
- `surgicalsupply.payment.fact_payment_change_rate`: `payment_change_rate`
- `surgicalsupply.procedure.fact_company_procedure_quantity`: `company_procedure_count`, `procedure_family_id`

## Intuitive Surgical (ISRG)

### Q4 2025 (5)

How did hospital purchasing, Medicaid coverage, and expiring exchange subsidies show up in late 2025, including any pull-forward of procedures?

- `surgicalsupply.payment.fact_payment_context_amount`: `provider_payment_amount`, `payer_type_id`, `payment_program_id`
- `surgicalsupply.payment.fact_payment_change_rate`: `payment_change_rate`
- `surgicalsupply.procedure.fact_company_procedure_quantity`: `company_procedure_count`, `procedure_family_id`

### Q3 2025 (6)

What gross-margin puts and takes follow from the implied fourth-quarter margin into the next year?

- `surgicalsupply.finance.fact_enterprise_amount`: `revenue_amount`, `gross_profit_amount`, `operating_income_amount`
- `surgicalsupply.finance.fact_enterprise_margin_rate`: `gross_margin_rate`, `operating_margin_rate`, `revenue_growth_rate`
- `surgicalsupply.finance.fact_stryker_segment_amount`: `segment_revenue_amount`, `segment_operating_income_amount`, `stryker_segment_id`

### Q2 2025 (1)

What drove the gross-margin upside, including the new facility, and how much of it is sustainable?

- `surgicalsupply.finance.fact_enterprise_amount`: `revenue_amount`, `gross_profit_amount`, `operating_income_amount`
- `surgicalsupply.finance.fact_enterprise_margin_rate`: `gross_margin_rate`, `operating_margin_rate`, `revenue_growth_rate`
- `surgicalsupply.finance.fact_stryker_segment_amount`: `segment_revenue_amount`, `segment_operating_income_amount`, `stryker_segment_id`
