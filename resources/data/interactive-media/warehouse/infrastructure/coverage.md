# Social Inc infrastructure, cloud, and corporate finance

Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks. Demand quantity, supply or capacity, and price or margin are stored on separate facts joined by the shared grain keys (fiscal quarter, scenario, and the business keys).

## Numbered questions

## Alphabet

### Q1 2026 (2) Alphabet

How does the capital-spending path, including a large 2027 increase, line up with serving the cloud backlog already booked?

- `social.cloud.fact_cloud_revenue`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `region_id`, `cloud_revenue_amount`
- `social.cloud.fact_cloud_backlog`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `backlog_amount`
- `social.cloud.fact_cloud_customer_count`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `cloud_customer_count`

### Q1 2026 (5) Alphabet

When capacity is constrained, what screens decide which internal projects get incremental compute versus external cloud customers?

- `social.cloud.fact_cloud_revenue`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `region_id`, `cloud_revenue_amount`
- `social.cloud.fact_cloud_backlog`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `backlog_amount`
- `social.cloud.fact_cloud_customer_count`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `cloud_customer_count`

### Q1 2026 (7) Alphabet

Is supply-chain price inflation included in the 2026 and 2027 capital-spending commentary, and how is compute split between internal use and external cloud?

- `social.cloud.fact_cloud_revenue`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `region_id`, `cloud_revenue_amount`
- `social.cloud.fact_cloud_backlog`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `backlog_amount`
- `social.cloud.fact_cloud_customer_count`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `cloud_customer_count`

### Q1 2026 (8) Alphabet

How much of backlog growth is TPU sales versus cloud, and can the margins on very large generative-AI deals match the existing cloud business?

- `social.cloud.fact_cloud_revenue`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `region_id`, `cloud_revenue_amount`
- `social.cloud.fact_cloud_backlog`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `backlog_amount`
- `social.cloud.fact_cloud_customer_count`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `cloud_customer_count`

### Q4 2025 (3) Alphabet

With 2026 capital spending stepping up, what is the path to closing the internal and external compute gaps, and what operating results should follow as those gaps close?

- `social.capex.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `capex_program_id`, `capex_amount`
- `social.cost.fact_depreciation`: `fiscal_quarter_id`, `scenario_id`, `capex_program_id`, `depreciation_amount`
- `social.infra.fact_compute_capacity`: `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capex_program_id`, `server_count`, `compute_unit_count`
- `social.cashflow.fact_free_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `free_cash_flow_amount`, `operating_cash_flow_amount`

### Q3 2025 (10) Alphabet

Have the large cloud deals signed over the prior nine months changed the long-term profit profile of cloud?

- `social.cloud.fact_cloud_revenue`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `region_id`, `cloud_revenue_amount`
- `social.cloud.fact_cloud_backlog`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `backlog_amount`
- `social.cloud.fact_cloud_customer_count`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `cloud_customer_count`

### Q2 2025 (2) Alphabet

Why is compute still tight even with a large step-up in capital spending?

- `social.capex.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `capex_program_id`, `capex_amount`
- `social.cost.fact_depreciation`: `fiscal_quarter_id`, `scenario_id`, `capex_program_id`, `depreciation_amount`
- `social.infra.fact_compute_capacity`: `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capex_program_id`, `server_count`, `compute_unit_count`
- `social.cashflow.fact_free_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `free_cash_flow_amount`, `operating_cash_flow_amount`

### Q2 2025 (10) Alphabet

After a strong cloud quarter, how should the back half be read if supply constraints now ease into 2026 rather than late 2025?

- `social.cloud.fact_cloud_revenue`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `region_id`, `cloud_revenue_amount`
- `social.cloud.fact_cloud_backlog`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `backlog_amount`
- `social.cloud.fact_cloud_customer_count`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `cloud_customer_count`

### Q2 2025 (12) Alphabet

Is the larger capital-spending plan mainly a response to cloud demand?

- `social.cloud.fact_cloud_revenue`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `region_id`, `cloud_revenue_amount`
- `social.cloud.fact_cloud_backlog`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `backlog_amount`
- `social.cloud.fact_cloud_customer_count`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `cloud_customer_count`

## Meta

### Q1 2026 (1) Meta

Over the next 12 to 24 months, which signals — Meta AI usage, Muse progress, or core ranking — would show the AI capital spending is on a path to an acceptable return?

- `social.capex.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `capex_program_id`, `capex_amount`
- `social.cost.fact_depreciation`: `fiscal_quarter_id`, `scenario_id`, `capex_program_id`, `depreciation_amount`
- `social.infra.fact_compute_capacity`: `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capex_program_id`, `server_count`, `compute_unit_count`
- `social.cashflow.fact_free_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `free_cash_flow_amount`, `operating_cash_flow_amount`

### Q1 2026 (3) Meta

How could 2027 capital spending step up from here, given peers have flagged large increases?

- `social.capex.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `capex_program_id`, `capex_amount`
- `social.cost.fact_depreciation`: `fiscal_quarter_id`, `scenario_id`, `capex_program_id`, `depreciation_amount`
- `social.infra.fact_compute_capacity`: `fiscal_quarter_id`, `scenario_id`, `data_center_region_id`, `capex_program_id`, `server_count`, `compute_unit_count`
- `social.cashflow.fact_free_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `free_cash_flow_amount`, `operating_cash_flow_amount`

### Q4 2025 (5) Meta

Does 2026 still produce positive free cash flow as more of the data-center build moves through joint ventures?

- `social.cashflow.fact_free_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `free_cash_flow_amount`, `operating_cash_flow_amount`
- `social.capex.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `capex_program_id`, `capex_amount`
- `social.cashflow.fact_cash_balance`: `fiscal_quarter_id`, `scenario_id`, `cash_and_securities_amount`

### Q4 2025 (6) Meta

With so much capacity coming, what non-ad businesses — subscriptions, model licensing, or cloud-style access — become realistic?

- `social.cloud.fact_cloud_revenue`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `region_id`, `cloud_revenue_amount`
- `social.cloud.fact_cloud_backlog`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `backlog_amount`
- `social.cloud.fact_cloud_customer_count`: `fiscal_quarter_id`, `scenario_id`, `cloud_product_id`, `cloud_customer_count`

### Q3 2025 (2) Meta

How should next year’s faster expense growth and capital spending be read against core growth, earnings, and free cash flow?

- `social.cashflow.fact_free_cash_flow`: `fiscal_quarter_id`, `scenario_id`, `free_cash_flow_amount`, `operating_cash_flow_amount`
- `social.capex.fact_capital_spending`: `fiscal_quarter_id`, `scenario_id`, `capex_program_id`, `capex_amount`
- `social.cashflow.fact_cash_balance`: `fiscal_quarter_id`, `scenario_id`, `cash_and_securities_amount`
