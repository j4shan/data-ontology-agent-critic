# Dell price versus volume

This slice owns the category price file, the growth bridge, segment margins, and attach. Unit price stays on the price file. Unit demand stays on the traditional-demand facts. AI shipment quantity stays on the AI shipment. The growth bridge stores a price effect, a volume effect, and a share effect as separate amounts. Storage attach and shipment attach are their own facts. Channel, country, and category are owned by the traditional-demand slice and are partial here.

Identifiers owned by another slice are partial here. Their complete populations are not re-authored in this slice.

| Identity | Column on this slice | Complete population |
| --- | --- | --- |
| `ai_platform_identity` | `ai_platform_id` | `sf:dell.product.dim_ai_platform` `ai_platform_id` |
| `ai_shipment_identity` | `ai_shipment_id` | `sf:dell.supply.fact_ai_shipment` `ai_shipment_id` |
| `architecture_identity` | `architecture_id` | `sf:dell.product.dim_architecture` `architecture_id` |
| `business_unit_identity` | `business_unit_id` | `sf:dell.product.dim_business_unit` `business_unit_id` |
| `channel_identity` | `channel_id` | `sf:dell.channel.dim_channel` `channel_id` |
| `component_commodity_identity` | `component_commodity_id` | `sf:dell.component.dim_component_commodity` `component_commodity_id` |
| `country_identity` | `country_id` | `sf:dell.geography.dim_country` `country_id` |
| `customer_type_identity` | `customer_type_id` | `sf:dell.product.dim_customer_type` `customer_type_id` |
| `fiscal_quarter_identity` | `fiscal_quarter_id` | `sf:dell.geography.dim_fiscal_quarter` `fiscal_quarter_id` |
| `fiscal_year_identity` | `fiscal_year_id` | `sf:dell.geography.dim_fiscal_year` `fiscal_year_id` |
| `pc_tier_identity` | `pc_tier_id` | `sf:dell.product.dim_pc_tier` `pc_tier_id` |
| `product_category_identity` | `product_category_id` | `sf:dell.product.dim_product_category` `product_category_id` |
| `server_generation_identity` | `server_generation_id` | `sf:dell.product.dim_server_generation` `server_generation_id` |

## Numbered questions

### Q2 FY2027 (4)

How much of the margin beat came from enterprise pull-through of networking, storage, and PCs, and does that lift the margin framework when enterprise is a larger mix?

- `dell.price.fact_enterprise_pullthrough`: `networking_amount`, `storage_amount`, `pc_amount`, `margin_beat_amount`, `lifts_framework_flag`, `customer_type_id`, `fiscal_quarter_id`
- `dell.price.fact_isg_margin`: `operating_margin_rate`, `sequential_change_amount`, `fiscal_quarter_id`
- `dell.product.dim_customer_type`: `customer_type_code`

### Q2 FY2027 (6)

Is the long-discussed storage attach on AI servers starting to show up, and how long can that runway last?

- `dell.price.fact_storage_attach`: `showing_up_flag`, `attach_rate`, `attached_storage_revenue_amount`, `runway_quarters`, `ai_shipment_id`, `customer_type_id`, `fiscal_quarter_id`
- `dell.supply.fact_ai_shipment`: `shipped_quantity`, `ai_platform_id`, `fiscal_quarter_id`

### Q2 FY2027 (8)

How much of traditional server and storage upside is volume versus price, and how much price headroom is left?

- `dell.price.fact_growth_bridge`: `volume_effect_amount`, `price_effect_amount`, `product_category_id`, `fiscal_quarter_id`
- `dell.price.fact_category_price`: `price_headroom_amount`, `unit_price`, `price_change_amount`, `product_category_id`, `country_id`, `channel_id`, `fiscal_quarter_id`
- `dell.demand.fact_category_demand`: `demand_quantity`, `product_category_id`, `fiscal_quarter_id`
- `dell.product.dim_product_category`: `category_code`

### Q2 FY2027 (9)

How much of the ISG margin gain is like-for-like uplift as customers move off older server generations, versus scale in the supply chain?

- `dell.price.fact_generation_margin`: `like_for_like_uplift_amount`, `supply_chain_scale_amount`, `server_generation_id`, `fiscal_quarter_id`
- `dell.price.fact_isg_margin`: `operating_margin_rate`, `sequential_change_amount`, `fiscal_quarter_id`
- `dell.product.dim_server_generation`: `generation_code`

### Q1 FY2027 (5)

Is the better gross-margin outlook excluding AI from price increases, mix, or where customer demand sits?

- `dell.price.fact_gross_margin`: `gross_margin_rate`, `excludes_ai_flag`, `versus_prior_view_amount`, `price_driver_amount`, `mix_driver_amount`, `demand_location_driver_amount`, `fiscal_quarter_id`
- `dell.price.fact_category_price`: `price_change_amount`, `product_category_id`, `fiscal_quarter_id`
- `dell.demand.fact_category_demand`: `demand_quantity`, `customer_type_id`, `product_category_id`, `fiscal_quarter_id`

### Q1 FY2027 (7)

What drove Client Solutions profitability sequentially and year over year, and is that drop-through sustainable?

- `dell.price.fact_csg_margin`: `operating_margin_rate`, `sequential_change_amount`, `year_ago_change_amount`, `drop_through_sustainable_flag`, `margin_from_volume_amount`, `margin_from_price_amount`, `fiscal_quarter_id`
- `dell.demand.fact_category_demand`: `demand_quantity`, `product_category_id`, `fiscal_quarter_id`
- `dell.price.fact_category_price`: `unit_price`, `price_change_amount`, `product_category_id`, `fiscal_quarter_id`
- `dell.product.dim_business_unit`: `unit_code`

### Q1 FY2027 (8)

If traditional servers are guided far faster than storage, does storage get a longer tail as server demand pulls it through?

- `dell.price.fact_storage_outlook`: `storage_growth_rate`, `server_growth_rate`, `tail_quarters`, `fiscal_quarter_id`, `fiscal_year_id`
- `dell.demand.fact_category_demand`: `demand_growth_rate`, `product_category_id`, `fiscal_quarter_id`
- `dell.product.dim_product_category`: `category_code`

### Q1 FY2027 (10)

What is the mix of x86 versus Arm servers, and is there a margin difference between those architectures?

- `dell.price.fact_architecture_margin`: `revenue_share`, `margin_rate`, `architecture_id`, `fiscal_quarter_id`
- `dell.product.dim_architecture`: `architecture_code`

### Q4 FY2026 (1)

How is AI-server profitability trending, and how are higher memory prices flowing through PCs and traditional infrastructure?

- `dell.price.fact_ai_server_margin`: `operating_margin_rate`, `gross_margin_rate`, `sequential_change_amount`, `fiscal_quarter_id`
- `dell.supply.fact_component_cost`: `cost_change_amount`, `inflation_rate`, `component_commodity_id`, `product_category_id`, `fiscal_quarter_id`
- `dell.price.fact_category_price`: `unit_price`, `price_change_amount`, `product_category_id`, `fiscal_quarter_id`
- `dell.product.dim_product_category`: `category_code`
- `dell.component.dim_component_commodity`: `commodity_code`

### Q4 FY2026 (3)

Will operating margins through the Rubin cycle be smoother than they were through Blackwell?

- `dell.price.fact_platform_margin`: `operating_margin_rate`, `smoother_than_prior_flag`, `ai_platform_id`, `fiscal_quarter_id`
- `dell.product.dim_ai_platform`: `platform_code`

### Q4 FY2026 (4)

Is storage actually turning, and will it help mix in the back half if it outgrows servers?

- `dell.price.fact_storage_outlook`: `turning_flag`, `outgrows_servers_flag`, `helps_back_half_mix_flag`, `storage_growth_rate`, `server_growth_rate`, `fiscal_quarter_id`
- `dell.price.fact_gross_margin`: `mix_driver_amount`, `fiscal_quarter_id`
- `dell.geography.dim_fiscal_quarter`: `half_code`

### Q4 FY2026 (5)

What memory-price inflation is in the fiscal 2027 outlook, and what is different this cycle in protecting margin?

- `dell.price.fact_memory_outlook`: `assumed_inflation_rate`, `margin_action_code`, `different_from_prior_cycle_flag`, `component_commodity_id`, `fiscal_year_id`, `fiscal_quarter_id`
- `dell.supply.fact_component_cost`: `inflation_rate`, `component_commodity_id`, `fiscal_quarter_id`
- `dell.geography.dim_fiscal_year`: `year_code`
- `dell.component.dim_component_commodity`: `commodity_code`

### Q4 FY2026 (8)

Are attach rates on shipped AI servers better than before, and what else is attaching?

- `dell.price.fact_shipment_attach`: `attach_rate`, `prior_attach_rate`, `improving_flag`, `attach_category_id`, `fiscal_quarter_id`
- `dell.price.dim_attach_category`: `category_code`
- `dell.supply.fact_ai_shipment`: `shipped_quantity`, `fiscal_quarter_id`
- `dell.price.fact_storage_attach`: `attach_rate`, `prior_attach_rate`, `fiscal_quarter_id`

### Q4 FY2026 (9)

Do dynamic pricing and supply access support structural PC share gains versus smaller competitors for more than the next year?

- `dell.price.fact_pc_share`: `share_rate`, `structural_gain_flag`, `holds_beyond_next_year_flag`, `dynamic_pricing_support_flag`, `smaller_competitor_supply_stress_index`, `pc_tier_id`, `fiscal_quarter_id`
- `dell.price.fact_category_price`: `unit_price`, `price_change_amount`, `product_category_id`, `fiscal_quarter_id`
- `dell.supply.fact_component_constraint`: `versus_prior_quarter_code`, `component_commodity_id`, `fiscal_quarter_id`
- `dell.product.dim_pc_tier`: `tier_code`

### Q3 FY2026 (1)

Which product categories can absorb price increases more easily than others?

- `dell.price.fact_category_price`: `price_absorption_index`, `price_change_amount`, `unit_price`, `product_category_id`, `country_id`, `channel_id`, `fiscal_quarter_id`
- `dell.product.dim_product_category`: `category_code`, `category_name`

### Q3 FY2026 (2)

How large was the sequential AI-server margin increase, does it continue next quarter, and is higher-margin attach improving?

- `dell.price.fact_ai_server_margin`: `sequential_change_amount`, `continues_next_quarter_flag`, `operating_margin_rate`, `fiscal_quarter_id`
- `dell.price.fact_shipment_attach`: `attach_rate`, `prior_attach_rate`, `improving_flag`, `attach_category_id`, `fiscal_quarter_id`

### Q3 FY2026 (4)

How much of the raised AI outlook depends on neoclouds obtaining financing versus customers Dell can already see?

- `dell.price.fact_ai_outlook`: `neocloud_financing_dependence_share`, `visible_customer_share`, `raised_revenue_amount`, `customer_type_id`, `fiscal_quarter_id`
- `dell.supply.fact_ai_order`: `order_amount`, `customer_type_id`, `fiscal_quarter_id`
- `dell.product.dim_customer_type`: `customer_type_code`

### Q3 FY2026 (5)

What lifted infrastructure margins so sharply versus the prior quarter, and how does a record AI-server quarter affect gross margin?

- `dell.price.fact_isg_margin`: `operating_margin_rate`, `sequential_change_amount`, `sharp_increase_flag`, `fiscal_quarter_id`
- `dell.price.fact_gross_margin`: `gross_margin_rate`, `ai_server_mix_effect_amount`, `fiscal_quarter_id`
- `dell.supply.fact_ai_shipment`: `shipped_quantity`, `shipped_amount`, `fiscal_quarter_id`

### Q3 FY2026 (8)

How should storage be viewed next year given commodity costs, and is the mix shifting toward Dell's own storage intellectual property?

- `dell.price.fact_storage_outlook`: `storage_growth_rate`, `commodity_cost_pressure_amount`, `dell_ip_mix_share`, `fiscal_year_id`, `fiscal_quarter_id`
- `dell.supply.fact_component_cost`: `cost_change_amount`, `component_commodity_id`, `product_category_id`, `fiscal_quarter_id`
- `dell.demand.fact_category_demand`: `demand_growth_rate`, `product_category_id`, `fiscal_quarter_id`

### Q3 FY2026 (9)

Of the higher full-year AI revenue, how much is extra components, new orders, or existing orders shipping earlier?

- `dell.price.fact_ai_guide_bridge`: `extra_component_amount`, `new_order_amount`, `earlier_shipment_amount`, `fiscal_quarter_id`
- `dell.supply.fact_ai_order`: `order_quantity`, `order_amount`, `fiscal_quarter_id`
- `dell.supply.fact_ai_shipment`: `shipped_quantity`, `fiscal_quarter_id`

### Q3 FY2026 (11)

As more neocloud, sovereign, and enterprise AI backlog converts, does operating margin stay in the mid-single digits or move up, and can PC share expand beyond high-end commercial?

- `dell.price.fact_ai_server_margin`: `operating_margin_rate`, `mid_single_digit_flag`, `moves_up_flag`, `customer_type_id`, `fiscal_quarter_id`
- `dell.supply.fact_ai_backlog`: `backlog_quantity`, `customer_type_id`, `fiscal_quarter_id`
- `dell.price.fact_pc_share`: `share_rate`, `beyond_high_end_flag`, `pc_tier_id`, `fiscal_quarter_id`
- `dell.product.dim_customer_type`: `customer_type_code`
- `dell.product.dim_pc_tier`: `tier_code`

## Datasets

| Qualified name | Role | Questions served |
| --- | --- | --- |
| `dell.price.dim_attach_category` | dimension | Q4 FY2026 (8) |
| `dell.price.dim_currency` | dimension | join support |
| `dell.price.fact_category_price` | fact | Q2 FY2027 (8), Q1 FY2027 (5), Q1 FY2027 (7), Q4 FY2026 (1), Q4 FY2026 (9), Q3 FY2026 (1) |
| `dell.price.fact_growth_bridge` | fact | Q2 FY2027 (8) |
| `dell.price.fact_isg_margin` | fact | Q2 FY2027 (4), Q2 FY2027 (9), Q3 FY2026 (5) |
| `dell.price.fact_csg_margin` | fact | Q1 FY2027 (7) |
| `dell.price.fact_ai_server_margin` | fact | Q4 FY2026 (1), Q3 FY2026 (2), Q3 FY2026 (11) |
| `dell.price.fact_gross_margin` | fact | Q1 FY2027 (5), Q4 FY2026 (4), Q3 FY2026 (5) |
| `dell.price.fact_platform_margin` | fact | Q4 FY2026 (3) |
| `dell.price.fact_generation_margin` | fact | Q2 FY2027 (9) |
| `dell.price.fact_architecture_margin` | fact | Q1 FY2027 (10) |
| `dell.price.fact_storage_attach` | fact | Q2 FY2027 (6), Q4 FY2026 (8) |
| `dell.price.fact_shipment_attach` | fact | Q4 FY2026 (8), Q3 FY2026 (2) |
| `dell.price.fact_enterprise_pullthrough` | fact | Q2 FY2027 (4) |
| `dell.price.fact_pc_share` | fact | Q4 FY2026 (9), Q3 FY2026 (11) |
| `dell.price.fact_memory_outlook` | fact | Q4 FY2026 (5) |
| `dell.price.fact_storage_outlook` | fact | Q1 FY2027 (8), Q4 FY2026 (4), Q3 FY2026 (8) |
| `dell.price.fact_ai_outlook` | fact | Q3 FY2026 (4) |
| `dell.price.fact_ai_guide_bridge` | fact | Q3 FY2026 (9) |
