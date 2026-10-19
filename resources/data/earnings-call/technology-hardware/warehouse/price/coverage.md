# Device Inc price, services and finance

Configuration price, services, geographic and Dell segment results, and enterprise margin.

Every fact below uses `fiscal_period_id` for the fiscal period and `scenario_id` for the scenario (`reported` or `guide` in `dim_scenario`). Measure descriptions in the YAML name the unit.

## Apple (AAPL)

### Q3 FY2026 (1)

How much of the guided growth slowdown is supply constraint versus currency, and which constraints are spreading?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q3 FY2026 (4)

Will the new Siri be a holiday iPhone demand driver, and what does the public beta imply for compute cost and recovery through iCloud+?

- `device.services.fact_services_revenue_amount`: `services_revenue_amount`, `service_offering_id`
- `device.services.fact_services_subscriber_quantity`: `paid_subscriber_count`, `active_account_count`
- `device.finance.fact_services_margin_rate`: `services_gross_margin_rate`

### Q3 FY2026 (5)

Can additional silicon sources ease the constraint in a useful time frame?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q3 FY2026 (7)

What is slowing Services growth, including whether the App Store is the main driver of the further deceleration in the outlook?

- `device.services.fact_services_revenue_amount`: `services_revenue_amount`, `service_offering_id`
- `device.services.fact_services_subscriber_quantity`: `paid_subscriber_count`, `active_account_count`
- `device.finance.fact_services_margin_rate`: `services_gross_margin_rate`

### Q3 FY2026 (8)

Which new markets open as more AI runs on the device?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q3 FY2026 (9)

Does Siri raise Apple’s capital intensity even with on-device work, given traffic that still hits first-party and third-party cloud?

- `device.services.fact_services_revenue_amount`: `services_revenue_amount`, `service_offering_id`
- `device.services.fact_services_subscriber_quantity`: `paid_subscriber_count`, `active_account_count`
- `device.finance.fact_services_margin_rate`: `services_gross_margin_rate`

### Q2 FY2026 (1)

Do agents imply a new phone form factor or new products, or do they sit on the current iPhone?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q2 FY2026 (2)

After June, can product gross margin stay in a narrow band despite component costs and constraints, or is visibility too short?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q2 FY2026 (4)

Has new App Store ad inventory been a meaningful piece of Services growth, and how do planned Maps ads extend that?

- `device.services.fact_services_revenue_amount`: `services_revenue_amount`, `service_offering_id`
- `device.services.fact_services_subscriber_quantity`: `paid_subscriber_count`, `active_account_count`
- `device.finance.fact_services_margin_rate`: `services_gross_margin_rate`

### Q2 FY2026 (5)

In this memory dislocation, is the priority share at the low end where competitors are strained, or profitability?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q2 FY2026 (7)

What is sustaining iPhone growth above 20% despite supply limits, and how durable is it?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q2 FY2026 (8)

How is memory, not only the main chip, being secured for iPhone, including sources outside the usual partners, and why is iPhone not expected to be constrained in June?

- `device.services.fact_services_revenue_amount`: `services_revenue_amount`, `service_offering_id`
- `device.services.fact_services_subscriber_quantity`: `paid_subscriber_count`, `active_account_count`
- `device.finance.fact_services_margin_rate`: `services_gross_margin_rate`

### Q2 FY2026 (9)

Is Services gross margin getting harder to expand because of mix, or is there still volume leverage and loss improvement left?

- `device.services.fact_services_revenue_amount`: `services_revenue_amount`, `service_offering_id`
- `device.services.fact_services_subscriber_quantity`: `paid_subscriber_count`, `active_account_count`
- `device.finance.fact_services_margin_rate`: `services_gross_margin_rate`

### Q2 FY2026 (10)

How is effort balanced between Apple’s own models and the Google collaboration, and does that require more investment?

- `device.services.fact_services_revenue_amount`: `services_revenue_amount`, `service_offering_id`
- `device.services.fact_services_subscriber_quantity`: `paid_subscriber_count`, `active_account_count`
- `device.finance.fact_services_margin_rate`: `services_gross_margin_rate`

### Q2 FY2026 (11)

Is the milder sequential product-margin move mix, currency, or both?

- `device.finance.fact_enterprise_amount`: `revenue_amount`, `gross_profit_amount`, `operating_income_amount`
- `device.finance.fact_enterprise_margin_rate`: `gross_margin_rate`, `operating_margin_rate`, `revenue_growth_rate`
- `device.finance.fact_margin_bridge_amount`: `margin_effect_amount`, `margin_effect_id`
- `device.finance.fact_product_margin_rate`: `product_gross_margin_rate`

### Q2 FY2026 (12)

In China, is Apple gaining because competitors are more supply-constrained, and how is the India iPhone opportunity evolving with the installed base and a larger middle class?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q1 FY2026 (1)

What revenue can AI add, relative to the operating-cost increase already visible?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q1 FY2026 (2)

Which one or two factors are driving iPhone strength, and how sustainable are they?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q1 FY2026 (3)

Why was Google the choice for the Siri partnership, and is there a revenue share similar to Search?

- `device.services.fact_services_revenue_amount`: `services_revenue_amount`, `service_offering_id`
- `device.services.fact_services_subscriber_quantity`: `paid_subscriber_count`, `active_account_count`
- `device.finance.fact_services_margin_rate`: `services_gross_margin_rate`

### Q1 FY2026 (4)

How is gross margin holding in the high 40s despite memory and NAND inflation — mix, Services margin, or something else?

- `device.services.fact_services_revenue_amount`: `services_revenue_amount`, `service_offering_id`
- `device.services.fact_services_subscriber_quantity`: `paid_subscriber_count`, `active_account_count`
- `device.finance.fact_services_margin_rate`: `services_gross_margin_rate`

### Q1 FY2026 (7)

If App Store growth was slower than total Services, what else drove Services and what would reaccelerate the store?

- `device.services.fact_services_revenue_amount`: `services_revenue_amount`, `service_offering_id`
- `device.services.fact_services_subscriber_quantity`: `paid_subscriber_count`, `active_account_count`
- `device.finance.fact_services_margin_rate`: `services_gross_margin_rate`

### Q1 FY2026 (9)

What is driving iPhone traction in India, and how large is the remaining installed-base opportunity?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q1 FY2026 (11)

Is AI expected to be mostly on device, and is enough data-center capacity reserved for a wide Siri launch without a hyperscale-style capital-spending surge?

- `device.services.fact_services_revenue_amount`: `services_revenue_amount`, `service_offering_id`
- `device.services.fact_services_subscriber_quantity`: `paid_subscriber_count`, `active_account_count`
- `device.finance.fact_services_margin_rate`: `services_gross_margin_rate`

### Q1 FY2026 (12)

What share of the active iPhone or device base can run Apple Intelligence, and is that why broader AI services are launching gradually?

- `device.services.fact_services_revenue_amount`: `services_revenue_amount`, `service_offering_id`
- `device.services.fact_services_subscriber_quantity`: `paid_subscriber_count`, `active_account_count`
- `device.finance.fact_services_margin_rate`: `services_gross_margin_rate`

### Q4 FY2025 (1)

Is iPhone 17 strength mainly an aging installed base replacing phones, or specific features versus prior cycles?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q4 FY2025 (3)

Was the Services upside organic, or did a partner payment or antitrust outcome contribute?

- `device.services.fact_services_revenue_amount`: `services_revenue_amount`, `service_offering_id`
- `device.services.fact_services_subscriber_quantity`: `paid_subscriber_count`, `active_account_count`
- `device.finance.fact_services_margin_rate`: `services_gross_margin_rate`

### Q4 FY2025 (4)

What accelerated Services — new-iPhone cross-sell, installed-base growth, or bundles such as Apple One and AppleCare?

- `device.services.fact_services_revenue_amount`: `services_revenue_amount`, `service_offering_id`
- `device.services.fact_services_subscriber_quantity`: `paid_subscriber_count`, `active_account_count`
- `device.finance.fact_services_margin_rate`: `services_gross_margin_rate`

### Q4 FY2025 (6)

Was September weakness in China a pause until iPhone Air arrived, and what else lifts the December view there?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q4 FY2025 (7)

Will iPhone supply still be constrained exiting December, and how much revenue did constraints hold back this quarter?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q4 FY2025 (14)

Does iPhone Air reception say anything about demand for a foldable, or are those form factors different?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q4 FY2025 (15)

Will the model strategy stay a mix of Apple’s own models, partners, and possible acquisitions, or will one path dominate?

- `device.services.fact_services_revenue_amount`: `services_revenue_amount`, `service_offering_id`
- `device.services.fact_services_subscriber_quantity`: `paid_subscriber_count`, `active_account_count`
- `device.finance.fact_services_margin_rate`: `services_gross_margin_rate`

### Q4 FY2025 (16)

Are AI features actually swaying purchases, or are record sales still about iOS retention and other factors?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

## Dell Technologies (DELL)

### Q2 FY2027 (7)

Which supply constraints tightened or eased versus last quarter, including newly signed supply agreements?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q1 FY2027 (3)

Why is the revenue guide still weighted to the back half, and is that caution or delayed demand versus the usual seasonal mix?

- `device.finance.fact_enterprise_amount`: `revenue_amount`, `gross_profit_amount`, `operating_income_amount`
- `device.finance.fact_enterprise_margin_rate`: `gross_margin_rate`, `operating_margin_rate`, `revenue_growth_rate`
- `device.finance.fact_margin_bridge_amount`: `margin_effect_amount`, `margin_effect_id`
- `device.finance.fact_product_margin_rate`: `product_gross_margin_rate`

### Q1 FY2027 (5)

Is the better gross-margin outlook excluding AI from price increases, mix, or where customer demand sits?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q1 FY2027 (9)

Beyond memory, which constraints — such as boards — limit further upside, and how do they rank?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`

### Q3 FY2026 (9)

Of the higher full-year AI revenue, how much is extra components, new orders, or existing orders shipping earlier?

- `device.finance.fact_compute_cost_amount`: `compute_cost_amount`, `recovered_amount`, `feature_id`
- `device.finance.fact_compute_request_quantity`: `request_count`, `service_offering_id`
- `device.finance.fact_capital_amount`: `capital_spend_amount`, `infrastructure_investment_amount`
- `device.services.fact_services_subscriber_quantity`: `active_account_count`, `service_offering_id`
