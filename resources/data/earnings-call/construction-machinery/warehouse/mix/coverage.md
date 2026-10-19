# Machinery Inc end markets and power mix

Dealer stock is inventory on its own quantity fact, not a retail channel. Caterpillar machine and power processes and PACCAR truck, parts, and finance processes use separate facts and separate reporting-segment dimensions. Quantity, capacity, and price or margin are separate facts joined by fiscal period, scenario, and the business keys. Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks.

## Numbered questions

## Caterpillar

### Q2 2026 (1) Caterpillar

Is the returning 10-megawatt reciprocating engine, and the 1.5 gigawatts it can ramp toward, inside the 2030 gigawatt target or additive?

- `machinery.power.fact_power_capacity_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `engine_fuel_id`, `power_size_class_id`, `end_market_id`, `target_year_id`, `capacity_gigawatts`, `capacity_unit_count`
- `machinery.power.fact_power_capacity_target`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `target_year_id`, `target_gigawatts`
- `machinery.power.fact_project_content_quantity`: `accounting_period_id`, `scenario_id`, `project_id`, `power_technology_id`, `project_content_units`

### Q2 2026 (3) Caterpillar

Why was construction volume stronger than expected after the inventory swing, while power volume was lighter even as capacity comes on?

- `machinery.commercial.fact_cat_segment_volume`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `volume_units`
- `machinery.power.fact_power_capacity_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `engine_fuel_id`, `power_size_class_id`, `end_market_id`, `target_year_id`, `capacity_gigawatts`, `capacity_unit_count`
- `machinery.power.fact_power_capacity_target`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `target_year_id`, `target_gigawatts`

### Q2 2026 (5) Caterpillar

Are Power & Energy incremental margins near the high rate seen this quarter sustainable while capacity is being added?

- `machinery.commercial.fact_cat_segment_volume`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `volume_units`
- `machinery.power.fact_power_capacity_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `engine_fuel_id`, `power_size_class_id`, `end_market_id`, `target_year_id`, `capacity_gigawatts`, `capacity_unit_count`
- `machinery.power.fact_power_capacity_target`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `target_year_id`, `target_gigawatts`

### Q2 2026 (6) Caterpillar

For 2027 and 2028, is gas reciprocating capacity sold out, and how is the company choosing among prime, flexible, and backup uses as backup tightens?

- `machinery.power.fact_application_slot_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `power_application_id`, `target_year_id`, `open_slot_count`, `booked_slot_count`
- `machinery.power.fact_power_capacity_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `engine_fuel_id`, `power_size_class_id`, `end_market_id`, `target_year_id`, `capacity_gigawatts`, `capacity_unit_count`
- `machinery.power.fact_power_capacity_target`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `target_year_id`, `target_gigawatts`

### Q2 2026 (9) Caterpillar

How large is Power & Energy service and aftermarket today, and how does that grow as deliveries stretch into 2029 and beyond?

- `machinery.power.fact_aftermarket_service_revenue`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `service_revenue_amount`
- `machinery.power.fact_installed_base_entry_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `cat_reporting_segment_id`, `target_year_id`, `installed_base_entry_units`
- `machinery.commercial.fact_cat_segment_volume`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `volume_units`

### Q2 2026 (11) Caterpillar

How does required diesel-standby redundancy differ for training versus inference data centers, and for behind-the-meter versus grid-connected sites?

- `machinery.power.fact_data_center_power_demand`: `accounting_period_id`, `scenario_id`, `end_market_id`, `target_year_id`, `region_id`, `data_center_demand_gigawatts`
- `machinery.market.fact_end_market_demand_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `region_id`, `end_market_demand_amount`
- `machinery.commercial.fact_cat_segment_volume`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `volume_units`

### Q1 2026 (1) Caterpillar

Which large-engine end market drove the extra capacity, and does that capacity arrive smoothly or in a lump at the end?

- `machinery.power.fact_power_capacity_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `engine_fuel_id`, `power_size_class_id`, `end_market_id`, `target_year_id`, `capacity_gigawatts`, `capacity_unit_count`
- `machinery.market.fact_end_market_demand_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `region_id`, `end_market_demand_amount`
- `machinery.power.fact_power_capacity_target`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `target_year_id`, `target_gigawatts`

### Q1 2026 (3) Caterpillar

Why add large-engine capacity rather than more gas-turbine investment?

- `machinery.power.fact_power_capacity_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `engine_fuel_id`, `power_size_class_id`, `end_market_id`, `target_year_id`, `capacity_gigawatts`, `capacity_unit_count`
- `machinery.power.fact_power_lead_time`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `lead_time_months`
- `machinery.power.fact_power_capacity_target`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `target_year_id`, `target_gigawatts`

### Q1 2026 (5) Caterpillar

Where is the tightest constraint as suppliers ramp power-generation capacity with Caterpillar, and what share of large-engine output in 2030 is prime versus backup?

- `machinery.power.fact_supplier_capacity_quantity`: `accounting_period_id`, `scenario_id`, `supplier_id`, `power_technology_id`, `target_year_id`, `supplier_capacity_units`, `constrained_capacity_units`
- `machinery.power.fact_power_capacity_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `engine_fuel_id`, `power_size_class_id`, `end_market_id`, `target_year_id`, `capacity_gigawatts`, `capacity_unit_count`
- `machinery.power.fact_power_capacity_target`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `target_year_id`, `target_gigawatts`

### Q4 2025 (2) Caterpillar

Where does the long-term power-capacity target stand through 2026 and 2027, and is there an overcapacity risk if data-center demand slows while everyone adds capacity?

- `machinery.power.fact_data_center_power_demand`: `accounting_period_id`, `scenario_id`, `end_market_id`, `target_year_id`, `region_id`, `data_center_demand_gigawatts`
- `machinery.power.fact_power_capacity_target`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `target_year_id`, `target_gigawatts`
- `machinery.market.fact_end_market_demand_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `region_id`, `end_market_demand_amount`

### Q4 2025 (4) Caterpillar

On a large announced project, how does battery storage sit alongside reciprocating engines in the order?

- `machinery.power.fact_project_content_quantity`: `accounting_period_id`, `scenario_id`, `project_id`, `power_technology_id`, `project_content_units`
- `machinery.power.fact_project_content_amount`: `accounting_period_id`, `scenario_id`, `project_id`, `power_technology_id`, `project_content_amount`
- `machinery.power.fact_power_capacity_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `engine_fuel_id`, `power_size_class_id`, `end_market_id`, `target_year_id`, `capacity_gigawatts`, `capacity_unit_count`

### Q4 2025 (5) Caterpillar

For prime power, how does the role of backup diesel versus battery storage evolve?

- `machinery.power.fact_application_slot_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `power_application_id`, `target_year_id`, `open_slot_count`, `booked_slot_count`
- `machinery.power.fact_project_content_quantity`: `accounting_period_id`, `scenario_id`, `project_id`, `power_technology_id`, `project_content_units`
- `machinery.power.fact_project_content_amount`: `accounting_period_id`, `scenario_id`, `project_id`, `power_technology_id`, `project_content_amount`

### Q4 2025 (6) Caterpillar

Was backlog growth inflated by a one-time pull-forward, separate from the project that lands next quarter?

- `machinery.power.fact_installed_base_entry_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `cat_reporting_segment_id`, `target_year_id`, `installed_base_entry_units`
- `machinery.power.fact_project_content_quantity`: `accounting_period_id`, `scenario_id`, `project_id`, `power_technology_id`, `project_content_units`
- `machinery.power.fact_project_content_amount`: `accounting_period_id`, `scenario_id`, `project_id`, `power_technology_id`, `project_content_amount`

### Q4 2025 (7) Caterpillar

How are utility conversations tracking on using turbines in plant applications?

- `machinery.power.fact_power_capacity_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `engine_fuel_id`, `power_size_class_id`, `end_market_id`, `target_year_id`, `capacity_gigawatts`, `capacity_unit_count`
- `machinery.power.fact_application_slot_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `power_application_id`, `target_year_id`, `open_slot_count`, `booked_slot_count`
- `machinery.power.fact_power_lead_time`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `lead_time_months`

### Q4 2025 (8) Caterpillar

How does using engine waste heat for cooling at a data center compare with combined-cycle efficiency?

- `machinery.power.fact_data_center_power_demand`: `accounting_period_id`, `scenario_id`, `end_market_id`, `target_year_id`, `region_id`, `data_center_demand_gigawatts`
- `machinery.market.fact_end_market_demand_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `region_id`, `end_market_demand_amount`
- `machinery.power.fact_power_capacity_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `engine_fuel_id`, `power_size_class_id`, `end_market_id`, `target_year_id`, `capacity_gigawatts`, `capacity_unit_count`

### Q4 2025 (9) Caterpillar

How much of Construction Industries demand is replacement returning to normal versus data-center activity?

- `machinery.market.fact_end_market_demand_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `region_id`, `end_market_demand_amount`
- `machinery.power.fact_data_center_power_demand`: `accounting_period_id`, `scenario_id`, `end_market_id`, `target_year_id`, `region_id`, `data_center_demand_gigawatts`
- `machinery.commercial.fact_cat_segment_volume`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `volume_units`

### Q4 2024 (1) Caterpillar

Has the view of data-center demand changed as capacity is added?

- `machinery.power.fact_data_center_power_demand`: `accounting_period_id`, `scenario_id`, `end_market_id`, `target_year_id`, `region_id`, `data_center_demand_gigawatts`
- `machinery.market.fact_end_market_demand_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `region_id`, `end_market_demand_amount`
- `machinery.power.fact_power_capacity_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `engine_fuel_id`, `power_size_class_id`, `end_market_id`, `target_year_id`, `capacity_gigawatts`, `capacity_unit_count`

### Q4 2024 (4) Caterpillar

What are solar-turbine lead times, and is more turbine factory capacity needed?

- `machinery.power.fact_power_lead_time`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `lead_time_months`
- `machinery.power.fact_power_capacity_quantity`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `engine_fuel_id`, `power_size_class_id`, `end_market_id`, `target_year_id`, `capacity_gigawatts`, `capacity_unit_count`
- `machinery.power.fact_power_capacity_target`: `accounting_period_id`, `scenario_id`, `power_technology_id`, `target_year_id`, `target_gigawatts`

### Q4 2024 (7) Caterpillar

How do Construction Industries revenue and margin move sequentially if first-quarter pressure is concentrated there?

- `machinery.commercial.fact_cat_segment_volume`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `volume_units`
- `machinery.power.fact_aftermarket_service_revenue`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `service_revenue_amount`
- `machinery.market.fact_end_market_demand_amount`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `end_market_id`, `region_id`, `end_market_demand_amount`

### Q4 2024 (8) Caterpillar

How did Construction and Resource Industries orders change sequentially versus a strong Energy & Transportation book?

- `machinery.commercial.fact_cat_segment_volume`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `volume_units`
- `machinery.power.fact_project_content_quantity`: `accounting_period_id`, `scenario_id`, `project_id`, `power_technology_id`, `project_content_units`
- `machinery.power.fact_project_content_amount`: `accounting_period_id`, `scenario_id`, `project_id`, `power_technology_id`, `project_content_amount`

### Q4 2024 (12) Caterpillar

How are Resource Industries customer conversations and early-year orders progressing after the fourth-quarter improvement?

- `machinery.commercial.fact_cat_segment_volume`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `volume_units`
- `machinery.power.fact_project_content_quantity`: `accounting_period_id`, `scenario_id`, `project_id`, `power_technology_id`, `project_content_units`
- `machinery.power.fact_project_content_amount`: `accounting_period_id`, `scenario_id`, `project_id`, `power_technology_id`, `project_content_amount`

## PACCAR

### Q4 2025 (9) PACCAR

Why leave the North America unit outlook unchanged after raising Europe and South America, if orders look robust?

- `machinery.power.fact_project_content_quantity`: `accounting_period_id`, `scenario_id`, `project_id`, `power_technology_id`, `project_content_units`
- `machinery.commercial.fact_cat_segment_volume`: `accounting_period_id`, `scenario_id`, `cat_reporting_segment_id`, `volume_units`

### Q3 2025 (16) PACCAR

Is fourth-quarter order coverage similar by region?

- `machinery.power.fact_project_content_quantity`: `accounting_period_id`, `scenario_id`, `project_id`, `power_technology_id`, `project_content_units`
- `machinery.power.fact_project_content_amount`: `accounting_period_id`, `scenario_id`, `project_id`, `power_technology_id`, `project_content_amount`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `machinery.market.dim_end_market` | supporting population |
| `machinery.market.dim_power_application` | supporting population |
| `machinery.product.dim_power_technology` | supporting population |
| `machinery.product.dim_power_size_class` | supporting population |
| `machinery.product.dim_engine_fuel` | supporting population |
| `machinery.power.dim_supplier` | supporting population |
| `machinery.power.dim_project` | supporting population |
| `machinery.power.dim_customer_type` | supporting population |
| `machinery.power.dim_target_year` | supporting population |
| `machinery.market.dim_construction_sector` | supporting population |
| `machinery.market.dim_project_scale` | supporting population |
| `machinery.commercial.fact_cat_segment_volume` | Q2 2026 (3), Q2 2026 (5), Q2 2026 (9), Q2 2026 (11), Q4 2025 (9), Q4 2024 (7), Q4 2024 (8), Q4 2024 (12), Q4 2025 (9) |
| `machinery.market.fact_end_market_demand_amount` | Q2 2026 (11), Q1 2026 (1), Q4 2025 (2), Q4 2025 (8), Q4 2025 (9), Q4 2024 (1), Q4 2024 (7) |
| `machinery.power.fact_power_capacity_quantity` | Q2 2026 (1), Q2 2026 (3), Q2 2026 (5), Q2 2026 (6), Q1 2026 (1), Q1 2026 (3), Q1 2026 (5), Q4 2025 (4), Q4 2025 (7), Q4 2025 (8), Q4 2024 (1), Q4 2024 (4) |
| `machinery.power.fact_power_capacity_target` | Q2 2026 (1), Q2 2026 (3), Q2 2026 (5), Q2 2026 (6), Q1 2026 (1), Q1 2026 (3), Q1 2026 (5), Q4 2025 (2), Q4 2024 (4) |
| `machinery.power.fact_application_slot_quantity` | Q2 2026 (6), Q4 2025 (5), Q4 2025 (7) |
| `machinery.power.fact_project_content_quantity` | Q2 2026 (1), Q4 2025 (4), Q4 2025 (5), Q4 2025 (6), Q4 2024 (8), Q4 2024 (12), Q4 2025 (9), Q3 2025 (16) |
| `machinery.power.fact_project_content_amount` | Q4 2025 (4), Q4 2025 (5), Q4 2025 (6), Q4 2024 (8), Q4 2024 (12), Q3 2025 (16) |
| `machinery.power.fact_supplier_capacity_quantity` | Q1 2026 (5) |
| `machinery.power.fact_data_center_power_demand` | Q2 2026 (11), Q4 2025 (2), Q4 2025 (8), Q4 2025 (9), Q4 2024 (1) |
| `machinery.power.fact_aftermarket_service_revenue` | Q2 2026 (9), Q4 2024 (7) |
| `machinery.power.fact_installed_base_entry_quantity` | Q2 2026 (9), Q4 2025 (6) |
| `machinery.power.fact_power_lead_time` | Q1 2026 (3), Q4 2025 (7), Q4 2024 (4) |
