# Device Inc demand and product

Apple and Dell product configurations, shipment and sell-through quantities, installed base, server orders and PC shipments.

Every fact below uses `fiscal_period_id` for the fiscal period and `scenario_id` for the scenario (`reported` or `guide` in `dim_scenario`). Measure descriptions in the YAML name the unit.

## Apple (AAPL)

### Q3 FY2026 (3)

What adoption is expected for the Apple Upgrade Program across the installed base, and does it shorten replacement for iPhone only or also Mac and iPad?

- `device.demand.fact_installed_base_quantity`: `installed_unit_count`, `ai_capable_unit_count`, `apple_family_id`
- `device.demand.fact_upgrade_activity_quantity`: `upgrader_unit_count`, `switcher_unit_count`
- `device.apple.dim_apple_family`: `apple_family_code`

### Q2 FY2026 (3)

Which new segments — education, value, or emerging markets — is MacBook Neo reaching, and how does the roadmap address other underpenetrated markets?

- `device.demand.fact_installed_base_quantity`: `installed_unit_count`, `ai_capable_unit_count`, `apple_family_id`
- `device.demand.fact_upgrade_activity_quantity`: `upgrader_unit_count`, `switcher_unit_count`
- `device.apple.dim_apple_family`: `apple_family_code`

### Q2 FY2026 (6)

Which layers of an agentic stack does Apple build versus partners, and does that require more of Apple’s own infrastructure?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q4 FY2025 (2)

How should iPhone in China trend in the December quarter, and has that region turned?

- `device.demand.fact_installed_base_quantity`: `installed_unit_count`, `ai_capable_unit_count`, `apple_family_id`
- `device.demand.fact_upgrade_activity_quantity`: `upgrader_unit_count`, `switcher_unit_count`
- `device.apple.dim_apple_family`: `apple_family_code`

### Q4 FY2025 (5)

Are iPhone buyers shifting between upgraders and switchers, are U.S. carrier promotions helping, and where is channel inventory?

- `device.demand.fact_installed_base_quantity`: `installed_unit_count`, `ai_capable_unit_count`, `apple_family_id`
- `device.demand.fact_upgrade_activity_quantity`: `upgrader_unit_count`, `switcher_unit_count`
- `device.apple.dim_apple_family`: `apple_family_code`

### Q4 FY2025 (8)

How much of the China momentum is smartphone subsidies, and what share of buyers is using them?

- `device.demand.fact_installed_base_quantity`: `installed_unit_count`, `ai_capable_unit_count`, `apple_family_id`
- `device.demand.fact_upgrade_activity_quantity`: `upgrader_unit_count`, `switcher_unit_count`
- `device.apple.dim_apple_family`: `apple_family_code`

### Q4 FY2025 (9)

What is inside the December operating-expense step-up, and should expense growth keep outrunning revenue?

- `device.demand.fact_shipment_quantity`: `shipped_unit_count`, `product_configuration_id`, `country_id`
- `device.price.fact_product_price`: `unit_price_amount`, `product_configuration_id`
- `device.demand.fact_sellthrough_quantity`: `sellthrough_unit_count`
- `device.product.dim_product_configuration`: `configuration_name`, `apple_generation_id`, `dell_generation_id`

### Q4 FY2025 (11)

How should holiday attach of other products to iPhone be read given where consumer budgets are?

- `device.demand.fact_shipment_quantity`: `shipped_unit_count`, `product_configuration_id`, `country_id`
- `device.price.fact_product_price`: `unit_price_amount`, `product_configuration_id`
- `device.demand.fact_sellthrough_quantity`: `sellthrough_unit_count`
- `device.product.dim_product_configuration`: `configuration_name`, `apple_generation_id`, `dell_generation_id`

### Q4 FY2025 (12)

Has iPhone 17 mix shifted between Pro and Pro Max versus prior cycles?

- `device.demand.fact_shipment_quantity`: `shipped_unit_count`, `product_configuration_id`, `country_id`
- `device.price.fact_product_price`: `unit_price_amount`, `product_configuration_id`
- `device.demand.fact_sellthrough_quantity`: `sellthrough_unit_count`
- `device.product.dim_product_configuration`: `configuration_name`, `apple_generation_id`, `dell_generation_id`

### Q4 FY2025 (13)

How should the private-cloud compute build be thought about from here?

- `device.demand.fact_shipment_quantity`: `shipped_unit_count`, `product_configuration_id`, `country_id`
- `device.price.fact_product_price`: `unit_price_amount`, `product_configuration_id`
- `device.demand.fact_sellthrough_quantity`: `sellthrough_unit_count`
- `device.product.dim_product_configuration`: `configuration_name`, `apple_generation_id`, `dell_generation_id`

## Dell Technologies (DELL)

### Q2 FY2027 (1)

Is the surge in traditional servers and storage real demand and share gain, or price and pre-buying?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q2 FY2027 (2)

Should next year’s growth track the AI-server partner’s outlook, given the backlog jump and new CPU racks sold into agentic deployments?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q2 FY2027 (3)

Is “traditional” server demand still almost all enterprise, or are neoclouds in that bucket now that CPU racks are included, and how does the AI-server customer mix compare?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q2 FY2027 (4)

How much of the margin beat came from enterprise pull-through of networking, storage, and PCs, and does that lift the margin framework when enterprise is a larger mix?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q2 FY2027 (5)

How much enterprise demand is deferred because budgets cannot absorb the price increase, so buyers take part of the order now and leave the rest for next year?

- `device.demand.fact_shipment_quantity`: `shipped_unit_count`, `product_configuration_id`, `country_id`
- `device.price.fact_product_price`: `unit_price_amount`, `product_configuration_id`
- `device.demand.fact_sellthrough_quantity`: `sellthrough_unit_count`
- `device.product.dim_product_configuration`: `configuration_name`, `apple_generation_id`, `dell_generation_id`

### Q2 FY2027 (6)

Is the long-discussed storage attach on AI servers starting to show up, and how long can that runway last?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q2 FY2027 (8)

How much of traditional server and storage upside is volume versus price, and how much price headroom is left?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q2 FY2027 (9)

How much of the ISG margin gain is like-for-like uplift as customers move off older server generations, versus scale in the supply chain?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q1 FY2027 (1)

Is the quarter’s strength a pull-forward in traditional servers and PCs, or does raising the second half mean demand continues?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q1 FY2027 (2)

How much of the traditional-server outperformance is units versus price, and does it last through this year and into next year?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q1 FY2027 (6)

Would the prior medium-term revenue framework be higher now, given agentic uses of traditional servers and share gains?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q1 FY2027 (7)

What drove Client Solutions profitability sequentially and year over year, and is that drop-through sustainable?

- `device.dell.fact_pc_shipment_quantity`: `shipped_pc_unit_count`, `dell_family_id`, `customer_segment_id`
- `device.demand.fact_pc_market_unit_quantity`: `industry_pc_unit_count`, `company_pc_unit_count`
- `device.price.fact_product_price`: `unit_price_amount`, `product_configuration_id`

### Q1 FY2027 (8)

If traditional servers are guided far faster than storage, does storage get a longer tail as server demand pulls it through?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q1 FY2027 (10)

What is the mix of x86 versus Arm servers, and is there a margin difference between those architectures?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q4 FY2026 (1)

How is AI-server profitability trending, and how are higher memory prices flowing through PCs and traditional infrastructure?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q4 FY2026 (2)

Why isn’t traditional-server growth faster, and is inference still landing on AI servers rather than traditional servers?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q4 FY2026 (3)

Will operating margins through the Rubin cycle be smoother than they were through Blackwell?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q4 FY2026 (4)

Is storage actually turning, and will it help mix in the back half if it outgrows servers?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q4 FY2026 (6)

How do AI-server orders split among enterprise, neoclouds, and sovereign buyers, and when does enterprise AI adoption show up in storage?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q4 FY2026 (7)

How does the AI backlog split between Blackwell and Vera Rubin, when does that mix ship, and is there capacity if demand runs past the revenue target?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q4 FY2026 (8)

Are attach rates on shipped AI servers better than before, and what else is attaching?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q4 FY2026 (9)

Do dynamic pricing and supply access support structural PC share gains versus smaller competitors for more than the next year?

- `device.dell.fact_pc_shipment_quantity`: `shipped_pc_unit_count`, `dell_family_id`, `customer_segment_id`
- `device.demand.fact_pc_market_unit_quantity`: `industry_pc_unit_count`, `company_pc_unit_count`
- `device.price.fact_product_price`: `unit_price_amount`, `product_configuration_id`

### Q3 FY2026 (1)

Which product categories can absorb price increases more easily than others?

- `device.demand.fact_shipment_quantity`: `shipped_unit_count`, `product_configuration_id`, `country_id`
- `device.price.fact_product_price`: `unit_price_amount`, `product_configuration_id`
- `device.demand.fact_sellthrough_quantity`: `sellthrough_unit_count`
- `device.product.dim_product_configuration`: `configuration_name`, `apple_generation_id`, `dell_generation_id`

### Q3 FY2026 (2)

How large was the sequential AI-server margin increase, does it continue next quarter, and is higher-margin attach improving?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q3 FY2026 (3)

Where is the PC refresh — still Windows end-of-life, or are new factors extending the cycle?

- `device.dell.fact_pc_shipment_quantity`: `shipped_pc_unit_count`, `dell_family_id`, `customer_segment_id`
- `device.demand.fact_pc_market_unit_quantity`: `industry_pc_unit_count`, `company_pc_unit_count`
- `device.price.fact_product_price`: `unit_price_amount`, `product_configuration_id`

### Q3 FY2026 (4)

How much of the raised AI outlook depends on neoclouds obtaining financing versus customers Dell can already see?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q3 FY2026 (5)

What lifted infrastructure margins so sharply versus the prior quarter, and how does a record AI-server quarter affect gross margin?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q3 FY2026 (6)

If traditional-server demand is up double digits but revenue is not, where is the upgrade cycle, and is double-digit growth a fair baseline?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q3 FY2026 (8)

How should storage be viewed next year given commodity costs, and is the mix shifting toward Dell’s own storage intellectual property?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`

### Q3 FY2026 (11)

As more neocloud, sovereign, and enterprise AI backlog converts, does operating margin stay in the mid-single digits or move up, and can PC share expand beyond high-end commercial?

- `device.dell.fact_server_order_quantity`: `ordered_unit_count`, `backlog_unit_count`, `dell_family_id`, `customer_type_id`
- `device.dell.fact_server_order_amount`: `order_amount`, `backlog_amount`
- `device.dell.fact_infrastructure_shipment_quantity`: `shipped_unit_count`, `attached_storage_unit_count`
- `device.finance.fact_dell_segment_amount`: `segment_revenue_amount`, `dell_segment_id`
