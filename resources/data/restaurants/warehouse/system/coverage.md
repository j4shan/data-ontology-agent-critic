# Burger Inc restaurant system

Restaurant operating models, franchising, licensing, labour, development and supply.

Every fact below uses `fiscal_period_id` for the fiscal period and `scenario_id` for the scenario (`reported` or `guide` in `dim_scenario`). Measure descriptions in the YAML name the unit.

## McDonald's (MCD)

### Q2 2026 (4)

Do company-operated restaurants outperform franchisees on service, and what would it take to move weak stores to stronger operators?

- `burger.restaurant.fact_franchise_restaurant_sales_amount`: `franchised_restaurant_sales_amount`, `franchisee_id`, `mcdonalds_segment_id`
- `burger.restaurant.fact_royalty_amount`: `royalty_amount`
- `burger.restaurant.fact_rent_amount`: `rent_amount`
- `burger.finance.fact_franchisee_cashflow_amount`: `franchisee_profit_amount`, `operating_cash_flow_amount`

### Q2 2026 (5)

Did the faster pace of new restaurants hurt same-store sales through cannibalization or by pulling resources off operations?

- `burger.development.fact_development_quantity`: `target_opening_count`, `actual_opening_count`, `ending_restaurant_count`
- `burger.restaurant.fact_restaurant_opening_quantity`: `opened_restaurant_count`
- `burger.restaurant.fact_restaurant_closure_quantity`: `closed_restaurant_count`
- `burger.finance.fact_capex_amount`: `capital_spend_amount`, `capital_budget_amount`, `project_type_id`

### Q2 2026 (7)

Can franchisees fund the U.S. operations, value, and experience work while their cash flow is under pressure?

- `burger.restaurant.fact_franchise_restaurant_sales_amount`: `franchised_restaurant_sales_amount`, `franchisee_id`, `mcdonalds_segment_id`
- `burger.restaurant.fact_royalty_amount`: `royalty_amount`
- `burger.restaurant.fact_rent_amount`: `rent_amount`
- `burger.finance.fact_franchisee_cashflow_amount`: `franchisee_profit_amount`, `operating_cash_flow_amount`

### Q2 2026 (8)

Were too many simultaneous product deployments hurting U.S. store operations, and should new-product news be slowed so throughput holds?

- `burger.restaurant.fact_labour_quantity`: `labour_hour_count`, `transaction_count`, `store_cohort_id`
- `burger.restaurant.fact_service_productivity_rate`: `transactions_per_labour_hour`
- `burger.restaurant.fact_service_duration`: `average_service_time_seconds`

### Q1 2026 (4)

How large is the opportunity to refranchise company stores in the U.S. and international operated markets if franchise economics are better?

- `burger.restaurant.fact_franchise_restaurant_sales_amount`: `franchised_restaurant_sales_amount`, `franchisee_id`, `mcdonalds_segment_id`
- `burger.restaurant.fact_royalty_amount`: `royalty_amount`
- `burger.restaurant.fact_rent_amount`: `rent_amount`
- `burger.finance.fact_franchisee_cashflow_amount`: `franchisee_profit_amount`, `operating_cash_flow_amount`

### Q1 2026 (5)

If stores are refranchised, should U.S. and international development targets change because margins are below the original plan?

- `burger.restaurant.fact_franchise_restaurant_sales_amount`: `franchised_restaurant_sales_amount`, `franchisee_id`, `mcdonalds_segment_id`
- `burger.restaurant.fact_royalty_amount`: `royalty_amount`
- `burger.restaurant.fact_rent_amount`: `rent_amount`
- `burger.finance.fact_franchisee_cashflow_amount`: `franchisee_profit_amount`, `operating_cash_flow_amount`

### Q1 2026 (6)

Are U.S. franchisee profits holding up even though company-operated margins are not?

- `burger.restaurant.fact_franchise_restaurant_sales_amount`: `franchised_restaurant_sales_amount`, `franchisee_id`, `mcdonalds_segment_id`
- `burger.restaurant.fact_royalty_amount`: `royalty_amount`
- `burger.restaurant.fact_rent_amount`: `rent_amount`
- `burger.finance.fact_franchisee_cashflow_amount`: `franchisee_profit_amount`, `operating_cash_flow_amount`

### Q1 2026 (7)

What is the outlook for international operated-market franchisee profit given the spike in energy prices, and is support like 2022 needed again?

- `burger.restaurant.fact_franchise_restaurant_sales_amount`: `franchised_restaurant_sales_amount`, `franchisee_id`, `mcdonalds_segment_id`
- `burger.restaurant.fact_royalty_amount`: `royalty_amount`
- `burger.restaurant.fact_rent_amount`: `rent_amount`
- `burger.finance.fact_franchisee_cashflow_amount`: `franchisee_profit_amount`, `operating_cash_flow_amount`

### Q1 2026 (13)

How do higher build costs and supply-chain strain change the next U.S. remodel cycle, including how much company capital franchisees would need?

- `burger.restaurant.fact_franchise_restaurant_sales_amount`: `franchised_restaurant_sales_amount`, `franchisee_id`, `mcdonalds_segment_id`
- `burger.restaurant.fact_royalty_amount`: `royalty_amount`
- `burger.restaurant.fact_rent_amount`: `rent_amount`
- `burger.finance.fact_franchisee_cashflow_amount`: `franchisee_profit_amount`, `operating_cash_flow_amount`

### Q1 2026 (16)

Will developmental-license markets have to deliver more of the path to 50,000 restaurants because U.S. and operated-market cash flow is tight?

- `burger.development.fact_development_quantity`: `target_opening_count`, `actual_opening_count`, `ending_restaurant_count`
- `burger.restaurant.fact_restaurant_opening_quantity`: `opened_restaurant_count`
- `burger.restaurant.fact_restaurant_closure_quantity`: `closed_restaurant_count`
- `burger.finance.fact_capex_amount`: `capital_spend_amount`, `capital_budget_amount`, `project_type_id`

### Q4 2025 (4)

Is the higher capital budget mostly faster new-store construction, and is unit growth in slow-population markets a share grab while the industry is stressed?

- `burger.development.fact_development_quantity`: `target_opening_count`, `actual_opening_count`, `ending_restaurant_count`
- `burger.restaurant.fact_restaurant_opening_quantity`: `opened_restaurant_count`
- `burger.restaurant.fact_restaurant_closure_quantity`: `closed_restaurant_count`
- `burger.finance.fact_capex_amount`: `capital_spend_amount`, `capital_budget_amount`, `project_type_id`

### Q4 2025 (5)

What kitchen equipment or layout changes are required to hit taste and quality goals, including anything like a new experience-of-the-future remodel?

- `burger.development.fact_development_quantity`: `target_opening_count`, `actual_opening_count`, `ending_restaurant_count`
- `burger.restaurant.fact_restaurant_opening_quantity`: `opened_restaurant_count`
- `burger.restaurant.fact_restaurant_closure_quantity`: `closed_restaurant_count`
- `burger.finance.fact_capex_amount`: `capital_spend_amount`, `capital_budget_amount`, `project_type_id`

### Q3 2025 (5)

Is the double-digit higher-income traffic gain an acceleration that shows trade-down, and is China the exception that is not positive inside developmental-license markets?

- `burger.development.fact_development_quantity`: `target_opening_count`, `actual_opening_count`, `ending_restaurant_count`
- `burger.restaurant.fact_restaurant_opening_quantity`: `opened_restaurant_count`
- `burger.restaurant.fact_restaurant_closure_quantity`: `closed_restaurant_count`
- `burger.finance.fact_capex_amount`: `capital_spend_amount`, `capital_budget_amount`, `project_type_id`

## Starbucks (SBUX)

### Q3 FY2026 (4)

Does that competitive dynamic change in markets where Starbucks is opening against other coffee specialists?

- `burger.development.fact_development_quantity`: `target_opening_count`, `actual_opening_count`, `ending_restaurant_count`
- `burger.restaurant.fact_restaurant_opening_quantity`: `opened_restaurant_count`
- `burger.restaurant.fact_restaurant_closure_quantity`: `closed_restaurant_count`
- `burger.finance.fact_capex_amount`: `capital_spend_amount`, `capital_budget_amount`, `project_type_id`

### Q3 FY2026 (5)

How much are store uplifts helping U.S. results, how is that measured per store, and what characterizes stores that may still close?

- `burger.restaurant.fact_restaurant_closure_quantity`: `closed_restaurant_count`, `operating_model_id`
- `burger.restaurant.fact_closure_sales_transfer_amount`: `transferred_sales_amount`, `closed_store_sales_amount`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`

### Q3 FY2026 (6)

How do company-operated comparable sales and operations in North America compare with licensed stores, and what can Starbucks do to close the gap?

- `burger.restaurant.fact_license_store_sales_amount`: `licensed_store_sales_amount`, `licensee_id`, `starbucks_segment_id`
- `burger.restaurant.fact_license_fee_amount`: `license_fee_amount`
- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `operating_model_id`

### Q3 FY2026 (7)

How much of the third-quarter comparable sales came from longer hours, closures, and delivery versus brand initiatives?

- `burger.restaurant.fact_restaurant_closure_quantity`: `closed_restaurant_count`, `operating_model_id`
- `burger.restaurant.fact_closure_sales_transfer_amount`: `transferred_sales_amount`, `closed_store_sales_amount`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`

### Q3 FY2026 (9)

Are Green Apron labor hours now enough for higher traffic, or is there room to get more transactions from the same hours?

- `burger.restaurant.fact_labour_quantity`: `labour_hour_count`, `transaction_count`, `store_cohort_id`
- `burger.restaurant.fact_service_productivity_rate`: `transactions_per_labour_hour`
- `burger.restaurant.fact_service_duration`: `average_service_time_seconds`

### Q3 FY2026 (11)

How did marketing spend change year over year, and is there still room for advertising to rise as a percent of sales or only to mix differently?

- `burger.restaurant.fact_franchise_restaurant_sales_amount`: `franchised_restaurant_sales_amount`, `franchisee_id`, `mcdonalds_segment_id`
- `burger.restaurant.fact_royalty_amount`: `royalty_amount`
- `burger.restaurant.fact_rent_amount`: `rent_amount`
- `burger.finance.fact_franchisee_cashflow_amount`: `franchisee_profit_amount`, `operating_cash_flow_amount`

### Q3 FY2026 (13)

What limits the remodel pace, when could the system be finished, and how much can 2027 accelerate?

- `burger.development.fact_development_quantity`: `target_opening_count`, `actual_opening_count`, `ending_restaurant_count`
- `burger.restaurant.fact_restaurant_opening_quantity`: `opened_restaurant_count`
- `burger.restaurant.fact_restaurant_closure_quantity`: `closed_restaurant_count`
- `burger.finance.fact_capex_amount`: `capital_spend_amount`, `capital_budget_amount`, `project_type_id`

### Q2 FY2026 (1)

Are stores hitting service-time targets, how did the algorithm changes help, and what does scheduled ordering add?

- `burger.restaurant.fact_labour_quantity`: `labour_hour_count`, `transaction_count`, `store_cohort_id`
- `burger.restaurant.fact_service_productivity_rate`: `transactions_per_labour_hour`
- `burger.restaurant.fact_service_duration`: `average_service_time_seconds`

### Q2 FY2026 (3)

How is Green Apron cost staged through the year relative to the productivity planned against it?

- `burger.restaurant.fact_labour_quantity`: `labour_hour_count`, `transaction_count`, `store_cohort_id`
- `burger.restaurant.fact_service_productivity_rate`: `transactions_per_labour_hour`
- `burger.restaurant.fact_service_duration`: `average_service_time_seconds`

### Q2 FY2026 (6)

Where do labor dollars per operating week settle over the next couple of years, and can existing hours be made efficient enough to fund more transactions?

- `burger.restaurant.fact_labour_quantity`: `labour_hour_count`, `transaction_count`, `store_cohort_id`
- `burger.restaurant.fact_service_productivity_rate`: `transactions_per_labour_hour`
- `burger.restaurant.fact_service_duration`: `average_service_time_seconds`

### Q2 FY2026 (7)

Are the original Green Apron store cohorts still improving, or does the gain become habitual?

- `burger.restaurant.fact_labour_quantity`: `labour_hour_count`, `transaction_count`, `store_cohort_id`
- `burger.restaurant.fact_service_productivity_rate`: `transactions_per_labour_hour`
- `burger.restaurant.fact_service_duration`: `average_service_time_seconds`

### Q1 FY2026 (1)

How much of North America traffic was sales transferred from September closures, and what was the underlying improvement?

- `burger.restaurant.fact_restaurant_closure_quantity`: `closed_restaurant_count`, `operating_model_id`
- `burger.restaurant.fact_closure_sales_transfer_amount`: `transferred_sales_amount`, `closed_store_sales_amount`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`

### Q1 FY2026 (2)

Are the earliest Green Apron stores still adding traffic from the service model?

- `burger.restaurant.fact_labour_quantity`: `labour_hour_count`, `transaction_count`, `store_cohort_id`
- `burger.restaurant.fact_service_productivity_rate`: `transactions_per_labour_hour`
- `burger.restaurant.fact_service_duration`: `average_service_time_seconds`

### Q1 FY2026 (6)

Should morning and afternoon be run differently, and what should Starbucks do about competitors that are almost entirely drive-thru and takeout?

- `burger.restaurant.fact_franchise_restaurant_sales_amount`: `franchised_restaurant_sales_amount`, `franchisee_id`, `mcdonalds_segment_id`
- `burger.restaurant.fact_royalty_amount`: `royalty_amount`
- `burger.restaurant.fact_rent_amount`: `rent_amount`
- `burger.finance.fact_franchisee_cashflow_amount`: `franchisee_profit_amount`, `operating_cash_flow_amount`

### Q1 FY2026 (9)

How fast can U.S. unit growth reaccelerate, and what penetration and return work supports a much larger long-term store count?

- `burger.development.fact_development_quantity`: `target_opening_count`, `actual_opening_count`, `ending_restaurant_count`
- `burger.restaurant.fact_restaurant_opening_quantity`: `opened_restaurant_count`
- `burger.restaurant.fact_restaurant_closure_quantity`: `closed_restaurant_count`
- `burger.finance.fact_capex_amount`: `capital_spend_amount`, `capital_budget_amount`, `project_type_id`

### Q1 FY2026 (11)

Is being under a four-minute service promise the right throughput level, or is there more to gain over the next year?

- `burger.restaurant.fact_labour_quantity`: `labour_hour_count`, `transaction_count`, `store_cohort_id`
- `burger.restaurant.fact_service_productivity_rate`: `transactions_per_labour_hour`
- `burger.restaurant.fact_service_duration`: `average_service_time_seconds`

### Q4 FY2025 (3)

Where is the Green Apron consumer response after a few months, and do August stores differ from stores upgraded earlier in the year?

- `burger.restaurant.fact_labour_quantity`: `labour_hour_count`, `transaction_count`, `store_cohort_id`
- `burger.restaurant.fact_service_productivity_rate`: `transactions_per_labour_hour`
- `burger.restaurant.fact_service_duration`: `average_service_time_seconds`

### Q4 FY2025 (4)

Was added Green Apron staffing mainly to stop traffic declines or to drive transactions, and can staffing go further?

- `burger.restaurant.fact_labour_quantity`: `labour_hour_count`, `transaction_count`, `store_cohort_id`
- `burger.restaurant.fact_service_productivity_rate`: `transactions_per_labour_hour`
- `burger.restaurant.fact_service_duration`: `average_service_time_seconds`

### Q4 FY2025 (6)

Is the added staffing already in place, what further Green Apron investment remains, and do 2026 product-cost savings offset commodity inflation?

- `burger.restaurant.fact_labour_quantity`: `labour_hour_count`, `transaction_count`, `store_cohort_id`
- `burger.restaurant.fact_service_productivity_rate`: `transactions_per_labour_hour`
- `burger.restaurant.fact_service_duration`: `average_service_time_seconds`

### Q4 FY2025 (7)

Are closing coffeehouses low-volume or high-cost, how much sales transfers, and do closures lower restaurant margins while also lowering overhead?

- `burger.restaurant.fact_restaurant_closure_quantity`: `closed_restaurant_count`, `operating_model_id`
- `burger.restaurant.fact_closure_sales_transfer_amount`: `transferred_sales_amount`, `closed_store_sales_amount`
- `burger.sales.fact_comparable_base_quantity`: `comparable_restaurant_count`, `comparable_transaction_count`

### Q4 FY2025 (10)

After meetings with licensees, is there a chance to simplify the licensed business in a way that helps company-owned stores?

- `burger.restaurant.fact_license_store_sales_amount`: `licensed_store_sales_amount`, `licensee_id`, `starbucks_segment_id`
- `burger.restaurant.fact_license_fee_amount`: `license_fee_amount`
- `burger.sales.fact_comparable_sales_rate`: `comparable_sales_rate`, `operating_model_id`
