# Food Inc input supply

General Mills and Mondelez each have their own reporting-segment dimension and brand dimension, and North America Retail appears only as a General Mills reporting segment, not as a channel. Realized price per pound or per kilogram shares brand and region keys with the matching brand-volume fact, and cocoa and wheat are carried as quantity at risk in tonnes beside cost per tonne. Coverage maps each numbered question to datasets and columns that exist in the YAML and can express the distinction the question asks.

## Numbered questions

## General Mills

### Q1 FY2027 (3) General Mills

Where did inflation land in the first quarter, how does it pace for the rest of the year, and what exit rate sits inside the high end of the 4% to 5% range?

- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `sourcing_origin_id`, `contract_cost_dollars_per_tonne`, `cost_inflation_percent`
- `food.supply.fact_hedge_coverage_rate`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `hedge_tenor_id`, `hedge_coverage_percent`
- `food.supply.fact_tariff_refund_amount`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `tariff_refund_amount`

### Q1 FY2027 (12) General Mills

What flexibility does the new partner packaging facility add, what other transformation work is underway, and when do the benefits show up?

- `food.supply.fact_packaging_capacity_quantity`: `fiscal_quarter_id`, `scenario_id`, `packaging_site_type_id`, `packaging_capacity_case_count`
- `food.supply.fact_gis_plant_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `gis_category_id`, `plant_capacity_case_count`
- `food.supply.fact_gis_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `gis_cost_program_id`, `productivity_savings_amount`

### Q1 FY2027 (14) General Mills

How exposed is the company to higher wheat costs, how covered is it if wheat keeps rising, and how much flour pass-through lifts foodservice?

- `food.supply.fact_commodity_quantity_at_risk`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `sourcing_origin_id`, `hedge_tenor_id`, `quantity_at_risk_tonnes`
- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `sourcing_origin_id`, `contract_cost_dollars_per_tonne`, `cost_inflation_percent`
- `food.supply.fact_hedge_quantity`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `hedge_tenor_id`, `hedged_quantity_tonnes`

### Q4 FY2026 (7) General Mills

How were fuel and other inflation assumptions set inside the 4% to 5% range, and how much is hedged versus assumed?

- `food.supply.fact_energy_cost`: `fiscal_quarter_id`, `scenario_id`, `energy_input_id`, `energy_cost_amount`, `energy_cost_inflation_percent`
- `food.supply.fact_hedge_quantity`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `hedge_tenor_id`, `hedged_quantity_tonnes`
- `food.supply.fact_hedge_coverage_rate`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `hedge_tenor_id`, `hedge_coverage_percent`

### Q4 FY2026 (11) General Mills

Does the 4% to 5% net inflation figure include tariff refunds, and when would those refunds land?

- `food.supply.fact_tariff_refund_amount`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `tariff_refund_amount`
- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `sourcing_origin_id`, `contract_cost_dollars_per_tonne`, `cost_inflation_percent`
- `food.supply.fact_hedge_coverage_rate`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `hedge_tenor_id`, `hedge_coverage_percent`

### Q3 FY2026 (7) General Mills

What does fiscal 2027 inflation look like with and without elevated fuel and oil-derivative costs, and how hard do savings have to work to offset it?

- `food.supply.fact_hedge_coverage_rate`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `hedge_tenor_id`, `hedge_coverage_percent`
- `food.supply.fact_energy_cost`: `fiscal_quarter_id`, `scenario_id`, `energy_input_id`, `energy_cost_amount`, `energy_cost_inflation_percent`
- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `sourcing_origin_id`, `contract_cost_dollars_per_tonne`, `cost_inflation_percent`

### Q3 FY2026 (15) General Mills

Beyond diesel, is driver tightness or other freight a headwind for next year's inflation?

- `food.supply.fact_freight_cost`: `fiscal_quarter_id`, `scenario_id`, `freight_mode_id`, `freight_cost_amount`
- `food.supply.fact_freight_quantity`: `fiscal_quarter_id`, `scenario_id`, `freight_mode_id`, `freight_tonnes`
- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `sourcing_origin_id`, `contract_cost_dollars_per_tonne`, `cost_inflation_percent`

### Q3 FY2026 (16) General Mills

What drove the decision to exit Brazil?

- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `sourcing_origin_id`, `contract_cost_dollars_per_tonne`, `cost_inflation_percent`
- `food.supply.fact_gis_plant_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `gis_category_id`, `plant_capacity_case_count`
- `food.supply.fact_gis_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `gis_cost_program_id`, `productivity_savings_amount`

### Q2 FY2026 (8) General Mills

How much holistic margin management benefit is still to come, and how does it phase between the third and fourth quarters?

- `food.supply.fact_gis_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `gis_cost_program_id`, `productivity_savings_amount`
- `food.supply.fact_packaging_capacity_quantity`: `fiscal_quarter_id`, `scenario_id`, `packaging_site_type_id`, `packaging_capacity_case_count`
- `food.supply.fact_gis_plant_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `gis_category_id`, `plant_capacity_case_count`

## Mondelez

### Q1 2026 (4) Mondelez

After cocoa fell early and then stabilized, how does management assess the cocoa market from here, including the second half?

- `food.supply.fact_commodity_spot_price`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `spot_price_dollars_per_tonne`
- `food.supply.fact_commodity_quantity_at_risk`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `sourcing_origin_id`, `hedge_tenor_id`, `quantity_at_risk_tonnes`
- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `sourcing_origin_id`, `contract_cost_dollars_per_tonne`, `cost_inflation_percent`

### Q1 2026 (9) Mondelez

What growth and route-to-market changes come from the new North America biscuit supply-chain modernization beyond earlier plant consolidation?

- `food.supply.fact_mdlz_plant_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `mdlz_category_id`, `plant_capacity_kilograms`
- `food.supply.fact_mdlz_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `mdlz_cost_program_id`, `productivity_savings_amount`
- `food.supply.fact_gis_plant_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `gis_category_id`, `plant_capacity_case_count`

### Q4 2025 (2) Mondelez

How does the lower cocoa cost change the guidance range and the room to invest?

- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `sourcing_origin_id`, `contract_cost_dollars_per_tonne`, `cost_inflation_percent`
- `food.supply.fact_commodity_quantity_at_risk`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `sourcing_origin_id`, `hedge_tenor_id`, `quantity_at_risk_tonnes`
- `food.supply.fact_commodity_spot_price`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `spot_price_dollars_per_tonne`

### Q4 2025 (12) Mondelez

How are cocoa-growing investments outside West Africa progressing relative to traditional origins?

- `food.supply.fact_origin_investment_amount`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `sourcing_origin_id`, `origin_investment_amount`
- `food.supply.fact_commodity_quantity_at_risk`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `sourcing_origin_id`, `hedge_tenor_id`, `quantity_at_risk_tonnes`
- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `sourcing_origin_id`, `contract_cost_dollars_per_tonne`, `cost_inflation_percent`

### Q3 2025 (7) Mondelez

How does the new multiyear North America supply-chain program differ from earlier productivity programs, and are there early targets?

- `food.supply.fact_mdlz_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `mdlz_cost_program_id`, `productivity_savings_amount`
- `food.supply.fact_mdlz_plant_capacity`: `fiscal_quarter_id`, `scenario_id`, `plant_id`, `mdlz_category_id`, `plant_capacity_kilograms`
- `food.supply.fact_gis_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `gis_cost_program_id`, `productivity_savings_amount`

### Q3 2025 (8) Mondelez

How much of this year's SG&A decline is a lasting cost reduction versus spend that returns next year with the planned reinvestment?

- `food.supply.fact_mdlz_productivity_savings`: `fiscal_quarter_id`, `scenario_id`, `mdlz_cost_program_id`, `productivity_savings_amount`
- `food.supply.fact_freight_cost`: `fiscal_quarter_id`, `scenario_id`, `freight_mode_id`, `freight_cost_amount`
- `food.supply.fact_commodity_cost`: `fiscal_quarter_id`, `scenario_id`, `commodity_id`, `sourcing_origin_id`, `contract_cost_dollars_per_tonne`, `cost_inflation_percent`

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `food.supply.dim_commodity` | supporting population |
| `food.supply.dim_sourcing_origin` | supporting population |
| `food.supply.dim_hedge_tenor` | supporting population |
| `food.supply.dim_energy_input` | supporting population |
| `food.supply.dim_plant` | supporting population |
| `food.supply.dim_packaging_site_type` | supporting population |
| `food.supply.dim_freight_mode` | supporting population |
| `food.supply.dim_gis_cost_program` | supporting population |
| `food.supply.dim_mdlz_cost_program` | supporting population |
| `food.supply.fact_commodity_quantity_at_risk` | Q1 FY2027 (14), Q1 2026 (4), Q4 2025 (2), Q4 2025 (12) |
| `food.supply.fact_commodity_cost` | Q1 FY2027 (3), Q1 FY2027 (14), Q4 FY2026 (11), Q3 FY2026 (7), Q3 FY2026 (15), Q3 FY2026 (16), Q1 2026 (4), Q4 2025 (2), Q4 2025 (12), Q3 2025 (8) |
| `food.supply.fact_commodity_spot_price` | Q1 2026 (4), Q4 2025 (2) |
| `food.supply.fact_commodity_inventory_quantity` | supporting population |
| `food.supply.fact_hedge_quantity` | Q1 FY2027 (14), Q4 FY2026 (7) |
| `food.supply.fact_hedge_coverage_rate` | Q1 FY2027 (3), Q4 FY2026 (7), Q4 FY2026 (11), Q3 FY2026 (7) |
| `food.supply.fact_gis_plant_capacity` | Q1 FY2027 (12), Q3 FY2026 (16), Q2 FY2026 (8), Q1 2026 (9) |
| `food.supply.fact_mdlz_plant_capacity` | Q1 2026 (9), Q3 2025 (7) |
| `food.supply.fact_gis_productivity_savings` | Q1 FY2027 (12), Q3 FY2026 (16), Q2 FY2026 (8), Q3 2025 (7) |
| `food.supply.fact_mdlz_productivity_savings` | Q1 2026 (9), Q3 2025 (7), Q3 2025 (8) |
| `food.supply.fact_freight_quantity` | Q3 FY2026 (15) |
| `food.supply.fact_freight_cost` | Q3 FY2026 (15), Q3 2025 (8) |
| `food.supply.fact_energy_cost` | Q4 FY2026 (7), Q3 FY2026 (7) |
| `food.supply.fact_packaging_capacity_quantity` | Q1 FY2027 (12), Q2 FY2026 (8) |
| `food.supply.fact_tariff_refund_amount` | Q1 FY2027 (3), Q4 FY2026 (11) |
| `food.supply.fact_origin_investment_amount` | Q4 2025 (12) |
