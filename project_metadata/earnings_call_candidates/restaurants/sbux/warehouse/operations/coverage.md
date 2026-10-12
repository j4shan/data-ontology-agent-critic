# Coffee Inc coffeehouse operations coverage

This slice is the coffeehouse-operations warehouse for Coffee Inc: coffeehouses, licensees, store partners, Green Apron labor, service time, hours, remodels, closures, and the new-unit pipeline.

Demand transactions and the general ledger are outside this slice. Calendar days join to `coffee.calendar.dim_calendar_day`. Fiscal periods join to `coffee.finance.dim_fiscal_period`. Civil dates and `period_label` values in this slice are the local labels for those keys. Green Apron amounts here are coffeehouse labor dollars and productivity. P&L recognition of that cost is `coffee.finance.fact_green_apron_cost_stage`. Closure margin and overhead amounts are coffeehouse operating amounts.

Green Apron rollout waves are `coffee.labor.dim_labor_model_cohort`. Install date is on `coffee.labor.fact_green_apron_cohort_assignment`. Weeks since install are on `coffee.labor.fact_green_apron_weekly_outcome`.

## Datasets and questions

| Qualified name | Questions |
| --- | --- |
| `coffee.organization.dim_country` | Q3 FY2026 (5) (6) (10) (13); Q1 FY2026 (1) (9); Q4 FY2025 (10) |
| `coffee.organization.dim_licensee` | Q3 FY2026 (6); Q4 FY2025 (10) |
| `coffee.store.dim_coffeehouse` | Q3 FY2026 (5) (6) (10); Q1 FY2026 (1) (9); Q4 FY2025 (7) (10) |
| `coffee.store.dim_ownership_type` | Q3 FY2026 (6); Q4 FY2025 (10) |
| `coffee.store.fact_ownership_operating_comparison` | Q3 FY2026 (6); Q4 FY2025 (10) |
| `coffee.labor.dim_labor_model_cohort` | Q3 FY2026 (9); Q2 FY2026 (3) (7); Q1 FY2026 (2); Q4 FY2025 (3) (4) (6) |
| `coffee.labor.dim_operating_week` | Q3 FY2026 (6) (13); Q2 FY2026 (1) (2) (3) (6) (7); Q1 FY2026 (1) (2) (11); Q4 FY2025 (3) |
| `coffee.labor.dim_service_interval` | Q2 FY2026 (1) (2); Q1 FY2026 (11) |
| `coffee.labor.dim_daypart_schedule` | Q3 FY2026 (10) |
| `coffee.labor.dim_partner` | Q2 FY2026 (1) |
| `coffee.labor.fact_coffeehouse_operating_week` | Q3 FY2026 (9) (10); Q2 FY2026 (2) (6); Q1 FY2026 (1) (11); Q4 FY2025 (4) |
| `coffee.labor.fact_green_apron_cohort_assignment` | Q3 FY2026 (9); Q2 FY2026 (7); Q1 FY2026 (2); Q4 FY2025 (3) (6) |
| `coffee.labor.fact_green_apron_weekly_outcome` | Q3 FY2026 (9); Q2 FY2026 (3) (7); Q1 FY2026 (2); Q4 FY2025 (3) (4) |
| `coffee.labor.fact_service_performance` | Q2 FY2026 (1) (2); Q1 FY2026 (11) |
| `coffee.labor.fact_daypart_hours` | Q3 FY2026 (10) |
| `coffee.labor.fact_green_apron_labor_investment` | Q3 FY2026 (9); Q2 FY2026 (3) (6); Q4 FY2025 (4) (6) |
| `coffee.labor.fact_partner_service_feedback` | Q2 FY2026 (1) |
| `coffee.capital_store.dim_remodel` | Q3 FY2026 (5) (13) |
| `coffee.capital_store.fact_remodel` | Q3 FY2026 (5) (13) |
| `coffee.capital_store.fact_remodel_pace` | Q3 FY2026 (13) |
| `coffee.capital_store.dim_closure` | Q3 FY2026 (5); Q1 FY2026 (1); Q4 FY2025 (7) |
| `coffee.capital_store.fact_closure` | Q3 FY2026 (5); Q1 FY2026 (1); Q4 FY2025 (7) |
| `coffee.capital_store.fact_new_unit_pipeline` | Q1 FY2026 (9) |

## Questions

### Q3 FY2026 (5)

How store uplifts help U.S. results, how that lift is measured per store, and what characterizes stores that may still close.

- `coffee.capital_store.fact_remodel`: `coffeehouse_id`, `remodel_id`, `sales_lift_amount`, `sales_lift_percent`, `remodel_cost`, `remodel_start_date`, `remodel_finish_date`, `start_calendar_day_id`, `finish_calendar_day_id`
- `coffee.capital_store.dim_remodel`: `remodel_id`, `coffeehouse_id`, `remodel_program_name`, `remodel_scope_code`
- `coffee.store.dim_coffeehouse`: `coffeehouse_id`, `country_id`, `open_status_code`
- `coffee.organization.dim_country`: `country_id`, `country_code`, `country_name`, `region_name`
- `coffee.capital_store.fact_closure`: `closure_id`, `coffeehouse_id`, `average_unit_volume`, `store_operating_cost`, `sales_transferred_amount`
- `coffee.capital_store.dim_closure`: `closure_id`, `coffeehouse_id`, `closure_status_code`, `closure_reason_code`

### Q3 FY2026 (6)

Company-operated comparable sales and operations in North America versus licensed stores.

- `coffee.store.fact_ownership_operating_comparison`: `ownership_type_id`, `country_id`, `operating_week_id`, `comparable_sales_percent`, `transaction_count`, `average_ticket_time_seconds`, `hours_open`, `labor_hours`, `labor_dollars`, `transactions_per_labor_hour`, `applicable_operations_action_code`
- `coffee.store.dim_ownership_type`: `ownership_type_id`, `ownership_type_code`, `ownership_type_name`
- `coffee.organization.dim_country`: `country_id`, `region_name`, `country_name`
- `coffee.organization.dim_licensee`: `licensee_id`, `licensee_name`, `license_model_code`, `country_id`
- `coffee.store.dim_coffeehouse`: `coffeehouse_id`, `ownership_type_id`, `licensee_id`, `country_id`
- `coffee.labor.dim_operating_week`: `operating_week_id`, `fiscal_year`, `fiscal_week_in_year`

### Q3 FY2026 (9)

Whether Green Apron labor hours are enough for higher traffic, or whether the same hours can produce more transactions.

- `coffee.labor.fact_green_apron_weekly_outcome`: `green_apron_labor_hours`, `labor_hours`, `labor_dollars`, `transaction_count`, `transactions_per_labor_hour`, `coffeehouse_id`, `operating_week_id`, `labor_model_cohort_id`
- `coffee.labor.fact_coffeehouse_operating_week`: `labor_hours`, `labor_dollars`, `transaction_count`, `transactions_per_labor_hour`, `hours_open`, `coffeehouse_id`, `operating_week_id`
- `coffee.labor.fact_green_apron_labor_investment`: `labor_hours`, `labor_hours_planned`, `transactions_per_labor_hour`, `transactions_per_labor_hour_planned`, `labor_model_cohort_id`
- `coffee.labor.fact_green_apron_cohort_assignment`: `coffeehouse_id`, `labor_model_cohort_id`, `install_date`
- `coffee.labor.dim_labor_model_cohort`: `labor_model_cohort_id`, `wave_name`, `program_name`

### Q3 FY2026 (10)

Whether some coffeehouses run 24 hours and what extended hours add to the U.S. system.

- `coffee.labor.fact_coffeehouse_operating_week`: `operates_24_hours`, `hours_open`, `extended_hours_open`, `extended_hours_transaction_count`, `extended_hours_sales_amount`, `coffeehouse_id`
- `coffee.labor.fact_daypart_hours`: `coffeehouse_id`, `operating_week_id`, `daypart_schedule_id`, `hours_open`, `transaction_count`
- `coffee.labor.dim_daypart_schedule`: `daypart_schedule_id`, `daypart_name`, `is_overnight`, `is_extended_hours`, `start_minute_of_day`, `end_minute_of_day`
- `coffee.store.dim_coffeehouse`: `coffeehouse_id`, `country_id`
- `coffee.organization.dim_country`: `country_id`, `country_code`, `country_name`

### Q3 FY2026 (13)

What limits remodel pace and whether 2027 can accelerate.

- `coffee.capital_store.fact_remodel_pace`: `country_id`, `fiscal_period_id`, `period_label`, `fiscal_year`, `contractor_capacity_count`, `stores_available_to_remodel_count`, `planned_remodel_count`, `remodels_started_count`, `remodels_finished_count`
- `coffee.capital_store.fact_remodel`: `remodel_id`, `coffeehouse_id`, `remodel_start_date`, `remodel_finish_date`, `start_calendar_day_id`, `finish_calendar_day_id`
- `coffee.capital_store.dim_remodel`: `remodel_id`, `remodel_program_name`, `coffeehouse_id`
- `coffee.organization.dim_country`: `country_id`, `country_name`, `country_code`
- `coffee.labor.dim_operating_week`: `fiscal_period_id`, `fiscal_year`, `period_label`

### Q2 FY2026 (1)

Whether coffeehouses hit service-time targets, how algorithm changes helped, and what scheduled ordering adds.

- `coffee.labor.fact_service_performance`: `coffeehouse_id`, `operating_week_id`, `service_interval_id`, `ticket_time_seconds`, `transaction_count`, `within_target_transaction_count`, `scheduling_algorithm_code`, `scheduled_order_transaction_count`
- `coffee.labor.dim_service_interval`: `service_interval_id`, `interval_name`, `target_ticket_time_seconds`, `daypart_schedule_id`
- `coffee.labor.fact_partner_service_feedback`: `partner_id`, `coffeehouse_id`, `operating_week_id`, `service_feedback_score`
- `coffee.labor.dim_partner`: `partner_id`, `coffeehouse_id`, `partner_role_name`, `partner_status_code`
- `coffee.labor.dim_operating_week`: `operating_week_id`, `week_start_date`, `fiscal_week_in_year`

### Q2 FY2026 (2)

How much comparable-sales runway is left from operations improvements alone.

- `coffee.labor.fact_coffeehouse_operating_week`: `operations_comparable_sales_percent`, `ticket_time_gap_seconds`, `average_ticket_time_seconds`, `transaction_count`, `coffeehouse_id`, `operating_week_id`
- `coffee.labor.fact_service_performance`: `ticket_time_seconds`, `within_target_transaction_count`, `transaction_count`, `service_interval_id`
- `coffee.labor.dim_service_interval`: `service_interval_id`, `target_ticket_time_seconds`
- `coffee.labor.dim_operating_week`: `operating_week_id`, `fiscal_year`, `fiscal_week_in_year`

### Q2 FY2026 (3)

How Green Apron cost is staged through the year versus the productivity planned against it.

- `coffee.labor.fact_green_apron_labor_investment`: `fiscal_period_id`, `period_label`, `fiscal_year`, `labor_model_cohort_id`, `country_id`, `labor_dollars`, `labor_dollars_planned`, `labor_hours`, `labor_hours_planned`, `transactions_per_labor_hour`, `transactions_per_labor_hour_planned`
- `coffee.labor.dim_labor_model_cohort`: `labor_model_cohort_id`, `wave_name`, `wave_sequence_number`, `program_name`
- `coffee.labor.dim_operating_week`: `fiscal_period_id`, `fiscal_year`, `period_label`, `fiscal_week_in_year`
- `coffee.labor.fact_green_apron_weekly_outcome`: `transactions_per_labor_hour`, `labor_dollars`, `labor_hours`, `operating_week_id`, `labor_model_cohort_id`

### Q2 FY2026 (6)

Where labor dollars per operating week settle, and whether existing hours can fund more transactions.

- `coffee.labor.fact_coffeehouse_operating_week`: `labor_dollars`, `labor_hours`, `hours_open`, `transactions_per_labor_hour`, `transaction_count`, `operating_week_id`, `coffeehouse_id`
- `coffee.labor.dim_operating_week`: `operating_week_id`, `fiscal_year`, `fiscal_week_in_year`, `week_start_date`
- `coffee.labor.fact_green_apron_labor_investment`: `labor_dollars`, `labor_dollars_planned`, `labor_dollars_remaining`, `transactions_per_labor_hour_planned`, `fiscal_year`, `period_label`

### Q2 FY2026 (7)

Whether the original Green Apron cohorts are still improving.

- `coffee.labor.fact_green_apron_weekly_outcome`: `weeks_since_install`, `transaction_count`, `transaction_count_change`, `transactions_per_labor_hour`, `ticket_time_seconds`, `labor_model_cohort_id`, `coffeehouse_id`, `operating_week_id`
- `coffee.labor.fact_green_apron_cohort_assignment`: `coffeehouse_id`, `labor_model_cohort_id`, `install_date`, `install_calendar_day_id`
- `coffee.labor.dim_labor_model_cohort`: `labor_model_cohort_id`, `wave_name`, `wave_sequence_number`
- `coffee.labor.dim_operating_week`: `operating_week_id`, `week_start_date`, `fiscal_week_in_year`

### Q1 FY2026 (1)

How much North America traffic was sales transferred from September closures, and what the underlying improvement was.

- `coffee.capital_store.fact_closure`: `sales_transferred_amount`, `transferred_transaction_count`, `closure_date`, `closure_calendar_day_id`, `fiscal_period_id`, `period_label`, `fiscal_year`, `coffeehouse_id`, `closure_id`
- `coffee.labor.fact_coffeehouse_operating_week`: `transaction_count`, `transactions_received_from_closures`, `coffeehouse_id`, `operating_week_id`
- `coffee.store.dim_coffeehouse`: `coffeehouse_id`, `country_id`, `open_status_code`
- `coffee.organization.dim_country`: `country_id`, `region_name`, `country_name`
- `coffee.capital_store.dim_closure`: `closure_id`, `closure_status_code`, `coffeehouse_id`
- `coffee.labor.dim_operating_week`: `operating_week_id`, `week_start_date`, `fiscal_period_id`, `period_label`

### Q1 FY2026 (2)

Whether the earliest Green Apron stores are still adding traffic.

- `coffee.labor.fact_green_apron_weekly_outcome`: `transaction_count`, `transaction_count_change`, `weeks_since_install`, `labor_model_cohort_id`, `coffeehouse_id`, `operating_week_id`
- `coffee.labor.dim_labor_model_cohort`: `labor_model_cohort_id`, `wave_name`, `wave_sequence_number`
- `coffee.labor.fact_green_apron_cohort_assignment`: `coffeehouse_id`, `labor_model_cohort_id`, `install_date`, `install_calendar_day_id`
- `coffee.labor.dim_operating_week`: `operating_week_id`, `week_start_date`, `fiscal_week_in_year`

### Q1 FY2026 (9)

How fast U.S. unit growth can reaccelerate, and what penetration and return work supports a larger store count.

- `coffee.capital_store.fact_new_unit_pipeline`: `coffeehouse_id`, `trade_area_penetration_rate`, `site_return_rate`, `projected_average_unit_volume`, `pipeline_stage_code`, `expected_open_date`, `expected_open_calendar_day_id`, `fiscal_period_id`, `period_label`, `fiscal_year`
- `coffee.store.dim_coffeehouse`: `coffeehouse_id`, `country_id`, `open_status_code`
- `coffee.organization.dim_country`: `country_id`, `country_code`, `country_name`, `region_name`

### Q1 FY2026 (11)

Whether under four minutes is the right throughput, and whether more remains to gain.

- `coffee.labor.fact_service_performance`: `ticket_time_seconds`, `within_target_transaction_count`, `transaction_count`, `service_interval_id`, `coffeehouse_id`, `operating_week_id`
- `coffee.labor.dim_service_interval`: `service_interval_id`, `target_ticket_time_seconds`, `interval_name`
- `coffee.labor.fact_coffeehouse_operating_week`: `average_ticket_time_seconds`, `ticket_time_gap_seconds`, `coffeehouse_id`, `operating_week_id`
- `coffee.labor.dim_operating_week`: `operating_week_id`, `fiscal_year`, `fiscal_week_in_year`

### Q4 FY2025 (3)

Green Apron response after a few months, and whether August stores differ from earlier upgrades.

- `coffee.labor.fact_green_apron_weekly_outcome`: `weeks_since_install`, `transaction_count`, `transaction_count_change`, `ticket_time_seconds`, `labor_model_cohort_id`, `coffeehouse_id`, `operating_week_id`
- `coffee.labor.fact_green_apron_cohort_assignment`: `install_date`, `install_calendar_day_id`, `labor_model_cohort_id`, `coffeehouse_id`
- `coffee.labor.dim_labor_model_cohort`: `wave_name`, `wave_sequence_number`, `labor_model_cohort_id`, `program_name`
- `coffee.labor.dim_operating_week`: `operating_week_id`, `week_start_date`, `fiscal_week_in_year`

### Q4 FY2025 (4)

Whether added Green Apron staffing was to stop traffic declines or to drive transactions, and whether staffing can go further.

- `coffee.labor.fact_green_apron_weekly_outcome`: `labor_hours`, `green_apron_labor_hours`, `transaction_count`, `transaction_count_change`, `transactions_per_labor_hour`, `weeks_since_install`, `coffeehouse_id`
- `coffee.labor.fact_coffeehouse_operating_week`: `labor_hours`, `transaction_count`, `transactions_per_labor_hour`, `coffeehouse_id`, `operating_week_id`
- `coffee.labor.fact_green_apron_labor_investment`: `labor_hours`, `labor_hours_planned`, `labor_dollars`, `labor_dollars_planned`, `labor_model_cohort_id`
- `coffee.labor.dim_labor_model_cohort`: `labor_model_cohort_id`, `wave_name`

### Q4 FY2025 (6)

Whether added staffing is already in place and what further Green Apron investment remains.

- `coffee.labor.fact_green_apron_labor_investment`: `labor_hours`, `labor_hours_planned`, `labor_dollars`, `labor_dollars_planned`, `labor_dollars_remaining`, `fiscal_period_id`, `period_label`, `fiscal_year`, `labor_model_cohort_id`, `country_id`
- `coffee.labor.fact_green_apron_cohort_assignment`: `coffeehouse_id`, `labor_model_cohort_id`, `install_date`, `install_calendar_day_id`
- `coffee.labor.dim_labor_model_cohort`: `labor_model_cohort_id`, `wave_name`, `wave_sequence_number`

### Q4 FY2025 (7)

Whether closing coffeehouses are low-volume or high-cost, how much sales transfers, and how closures move restaurant margin versus overhead.

- `coffee.capital_store.fact_closure`: `average_unit_volume`, `store_operating_cost`, `sales_transferred_amount`, `transferred_transaction_count`, `restaurant_margin_effect_amount`, `overhead_effect_amount`, `coffeehouse_id`, `closure_id`, `closure_date`
- `coffee.capital_store.dim_closure`: `closure_id`, `closure_status_code`, `closure_reason_code`, `coffeehouse_id`
- `coffee.store.dim_coffeehouse`: `coffeehouse_id`, `open_status_code`, `country_id`

### Q4 FY2025 (10)

Whether the licensed business can be simplified in a way that helps company-operated coffeehouses.

- `coffee.store.fact_ownership_operating_comparison`: `ownership_type_id`, `country_id`, `comparable_sales_percent`, `average_ticket_time_seconds`, `labor_hours`, `transaction_count`, `hours_open`, `cross_ownership_sales_effect_amount`, `applicable_operations_action_code`
- `coffee.store.dim_ownership_type`: `ownership_type_id`, `ownership_type_code`, `ownership_type_name`
- `coffee.organization.dim_licensee`: `licensee_id`, `licensee_name`, `license_model_code`, `country_id`
- `coffee.store.dim_coffeehouse`: `coffeehouse_id`, `ownership_type_id`, `licensee_id`, `country_id`
- `coffee.organization.dim_country`: `country_id`, `region_name`, `country_name`

## Reading rules

- North America is `region_name` on `coffee.organization.dim_country`. The United States is `country_code` and `country_name` on that dimension.
- Company-operated and licensed are `ownership_type_code` values `company_operated` and `licensed` on `coffee.store.dim_ownership_type`.
- September closures are `closure_date` on `coffee.capital_store.fact_closure`. Underlying traffic at coffeehouses that stayed open is `transaction_count` minus `transactions_received_from_closures` on `coffee.labor.fact_coffeehouse_operating_week`.
- August Green Apron installs are `install_date` on `coffee.labor.fact_green_apron_cohort_assignment`, with `wave_name` on `coffee.labor.dim_labor_model_cohort`.
- The four-minute promise is `target_ticket_time_seconds` of 240 on `coffee.labor.dim_service_interval`, compared with `ticket_time_seconds` on `coffee.labor.fact_service_performance`.
- A 24-hour coffeehouse has `operates_24_hours` of `operates_24_hours` and overnight `hours_open` on `coffee.labor.fact_daypart_hours` where `is_overnight` is `overnight`. Extended hours add `extended_hours_transaction_count` and `extended_hours_sales_amount`.
- Fiscal 2027 remodel pace is `planned_remodel_count` on `coffee.capital_store.fact_remodel_pace` where `fiscal_year` is 2027, set beside `contractor_capacity_count` and `stores_available_to_remodel_count`.
- Coffeehouses that may still close have `open_status_code` of `identified_to_close` or a closure with `closure_status_code` of `announced`. Volume is `average_unit_volume`. Cost is `store_operating_cost`.
