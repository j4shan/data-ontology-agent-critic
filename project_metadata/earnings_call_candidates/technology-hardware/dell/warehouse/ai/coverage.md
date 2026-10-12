# Dell AI-server backlog and supply

This slice owns AI platforms, architecture, purchased components, suppliers, backlog, AI orders, AI shipments, and component constraints. Dell buys DRAM, NAND, CPUs, and boards. The slice does not describe a wafer fab. An AI order is the demand for an AI server. The shipment is the supply. Neither stores the category price. Country, category, and the fiscal calendar are owned by the traditional-demand slice and are partial here.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `country_identity` | `country_id` | `sf:dell.geography.dim_country` `country_id` |
| `currency_identity` | `currency_id` | `sf:dell.price.dim_currency` `currency_id` |
| `customer_type_identity` | `customer_type_id` | `sf:dell.product.dim_customer_type` `customer_type_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:dell.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `product_category_identity` | `product_category_id` | `sf:dell.product.dim_product_category` `product_category_id` |
| `workload_identity` | `workload_id` | `sf:dell.product.dim_workload` `workload_id` |

## Numbered questions

### Q2 FY2027 (2)

Should next year's growth track the AI-server partner's outlook, given the backlog jump and new CPU racks sold into agentic deployments?

- `dell.supply.fact_partner_outlook`: `partner_ai_server_growth_rate`, `dell_growth_rate`, `tracks_partner_flag`, `acie_mix_share`, `supplier_id`, `fiscal_quarter_id`
- `dell.supply.fact_ai_backlog`: `backlog_quantity`, `backlog_jump_flag`, `ai_platform_id`, `fiscal_quarter_id`
- `dell.supply.fact_cpu_rack`: `racks_sold_quantity`, `agentic_deployment_flag`, `workload_id`, `fiscal_quarter_id`
- `dell.product.dim_workload`: `workload_code`
- `dell.supplier.dim_supplier`: `ai_server_partner_flag`

### Q2 FY2027 (7)

Which supply constraints tightened or eased versus last quarter, including newly signed supply agreements?

- `dell.supply.fact_component_constraint`: `tightness_rank`, `versus_prior_quarter_code`, `limits_upside_flag`, `component_commodity_id`, `fiscal_quarter_id`
- `dell.supply.fact_supply_agreement`: `newly_signed_flag`, `coverage_quarters`, `supplier_id`, `component_commodity_id`, `fiscal_quarter_id`
- `dell.component.dim_component_commodity`: `commodity_code`

### Q1 FY2027 (9)

Beyond memory, which constraints — such as boards — limit further upside, and how do they rank?

- `dell.supply.fact_component_constraint`: `tightness_rank`, `limits_upside_flag`, `versus_prior_quarter_code`, `component_commodity_id`, `fiscal_quarter_id`
- `dell.component.dim_component_commodity`: `commodity_code`, `commodity_name`
- `dell.demand.fact_category_demand`: `demand_quantity`, `product_category_id`, `fiscal_quarter_id`

### Q4 FY2026 (2)

Why isn't traditional-server growth faster, and is inference still landing on AI servers rather than traditional servers?

- `dell.demand.fact_category_demand`: `demand_growth_rate`, `product_category_id`, `fiscal_quarter_id`
- `dell.supply.fact_inference_placement`: `placement_share`, `product_category_id`, `workload_id`, `fiscal_quarter_id`
- `dell.product.dim_product_category`: `category_code`
- `dell.product.dim_workload`: `workload_code`

### Q4 FY2026 (6)

How do AI-server orders split among enterprise, neoclouds, and sovereign buyers, and when does enterprise AI adoption show up in storage?

- `dell.supply.fact_ai_order`: `order_amount`, `order_quantity`, `customer_type_id`, `ai_platform_id`, `fiscal_quarter_id`
- `dell.price.fact_storage_attach`: `spillover_timing_quarters`, `customer_type_id`, `fiscal_quarter_id`
- `dell.product.dim_customer_type`: `customer_type_code`

### Q4 FY2026 (7)

How does the AI backlog split between Blackwell and Vera Rubin, when does that mix ship, and is there capacity if demand runs past the revenue target?

- `dell.supply.fact_ai_backlog`: `backlog_amount`, `backlog_quantity`, `ship_quarter_code`, `capacity_above_target_flag`, `ai_platform_id`, `fiscal_quarter_id`
- `dell.supply.fact_ai_capacity`: `capacity_quantity`, `above_target_available_flag`, `ai_platform_id`, `fiscal_quarter_id`
- `dell.product.dim_ai_platform`: `platform_code`

### Q3 FY2026 (7)

How long do strategically bought, below-market components help, and can longer commercial contracts be repriced?

- `dell.supply.fact_component_inventory_cost`: `below_market_flag`, `benefit_remaining_quarters`, `component_commodity_id`, `fiscal_quarter_id`
- `dell.supply.fact_supply_agreement`: `can_reprice_flag`, `repricing_timing_quarters`, `contract_type_id`, `component_commodity_id`, `fiscal_quarter_id`
- `dell.price.fact_category_price`: `unit_price`, `product_category_id`, `fiscal_quarter_id`

### Q3 FY2026 (10)

Do purchase commitments say anything about where DRAM and NAND prices are expected to go?

- `dell.supply.fact_purchase_commitment`: `commitment_amount`, `implied_price_direction`, `component_commodity_id`, `fiscal_quarter_id`
- `dell.price.fact_memory_outlook`: `assumed_inflation_rate`, `component_commodity_id`, `fiscal_year_id`, `fiscal_quarter_id`
- `dell.component.dim_component_commodity`: `commodity_code`

## Datasets

| Qualified name | Role | Questions served |
| --- | --- | --- |
| `dell.product.dim_ai_platform` | dimension | Q4 FY2026 (7) |
| `dell.product.dim_architecture` | dimension | join support |
| `dell.component.dim_component_commodity` | dimension | Q2 FY2027 (7), Q1 FY2027 (9), Q3 FY2026 (10) |
| `dell.component.dim_component` | dimension | join support |
| `dell.supplier.dim_supplier` | dimension | Q2 FY2027 (2) |
| `dell.supplier.dim_supplier_site` | dimension | join support |
| `dell.supply.dim_contract_type` | dimension | join support |
| `dell.supply.fact_ai_backlog` | fact | Q2 FY2027 (2), Q4 FY2026 (7) |
| `dell.supply.fact_ai_order` | fact | Q4 FY2026 (6) |
| `dell.supply.fact_ai_shipment` | fact | join support |
| `dell.supply.fact_cpu_rack` | fact | Q2 FY2027 (2) |
| `dell.supply.fact_component_constraint` | fact | Q2 FY2027 (7), Q1 FY2027 (9) |
| `dell.supply.fact_supply_agreement` | fact | Q2 FY2027 (7), Q3 FY2026 (7) |
| `dell.supply.fact_purchase_commitment` | fact | Q3 FY2026 (10) |
| `dell.supply.fact_component_cost` | fact | join support |
| `dell.supply.fact_component_inventory_cost` | fact | Q3 FY2026 (7) |
| `dell.supply.fact_partner_outlook` | fact | Q2 FY2027 (2) |
| `dell.supply.fact_inference_placement` | fact | Q4 FY2026 (2) |
| `dell.supply.fact_ai_capacity` | fact | Q4 FY2026 (7) |
