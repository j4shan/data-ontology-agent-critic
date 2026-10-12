# Stryker capital equipment, franchise, backlog, and supply

This slice is capital equipment and the product franchise, including orders, backlog, placements, the installed system, manufacturing capacity, and supply disruption. Hospitals, procedure volume, and reimbursement are owned outside this slice.

Foreign identities are referenced from capital rows and are partial here. Their complete populations are the datasets below, which this slice does not author.

| Identity | Column | Node |
| --- | --- | --- |
| `accounting_period_identity` | `accounting_period_id` | `sf:stryker.calendar.dim_accounting_period` |
| `accounting_period_identity` | `expected_clear_accounting_period_id` | `sf:stryker.calendar.dim_accounting_period` |
| `calendar_day_identity` | `data_expected_calendar_day_id` | `sf:stryker.calendar.dim_calendar_day` |
| `calendar_day_identity` | `expected_clearance_calendar_day_id` | `sf:stryker.calendar.dim_calendar_day` |
| `calendar_day_identity` | `market_release_calendar_day_id` | `sf:stryker.calendar.dim_calendar_day` |
| `calendar_day_identity` | `plant_recovery_calendar_day_id` | `sf:stryker.calendar.dim_calendar_day` |
| `calendar_day_identity` | `us_launch_calendar_day_id` | `sf:stryker.calendar.dim_calendar_day` |
| `country_identity` | `country_id` | `sf:stryker.customer.dim_country` |
| `currency_identity` | `currency_id` | `sf:stryker.finance.dim_currency` |
| `hospital_identity` | `hospital_id` | `sf:stryker.customer.dim_hospital` |
| `hospital_site_identity` | `hospital_site_id` | `sf:stryker.customer.dim_hospital_site` |
| `procedure_family_identity` | `procedure_family_id` | `sf:stryker.procedure.dim_procedure_family` |
| `site_of_care_identity` | `site_of_care_id` | `sf:stryker.customer.dim_site_of_care` |

## Numbered questions

### Q2 2026 (2) — Catch-up split between the third and fourth quarters

Remaining backlog and planned realization are stated by quarter cadence, including third and fourth quarter.

`stryker.commercial.fact_order_backlog`: `remaining_backlog_amount`, `planned_realization_amount`, `capital_delivery_amount`, `quarter_cadence_code`, `accounting_period_id`.
`stryker.procedure.fact_procedure_catchup`: `recovered_case_count`, `still_ahead_case_count`, `accounting_period_id`, `source_accounting_period_id`.

### Q2 2026 (6) — Whether the Inari shortage hit other vascular products

Shortage scope says whether the gap is limited to Inari or also other vascular products.

`stryker.supply.fact_supply_shortage`: `shortage_scope_code`, `product_franchise_id`, `product_id`, `lost_sales_amount`.
`stryker.commercial.fact_franchise_result`: `growth_rate`, `product_franchise_id`.

### Q2 2026 (8) — What could keep the production ramp off the back-half plan

Planned shifts are compared with the quantity that has to ship, and a constraint code names the blocker.

`stryker.supply.fact_capacity_plan`: `planned_shift_count`, `required_ship_quantity`, `ramp_constraint_code`, `meets_back_half_plan_flag`, `manufacturing_shift_id`.

### Q2 2026 (10) — Reception of SmartCare and Vocera

Hospital feedback is stored against the installed communication base.

`stryker.capital.fact_offering_reception`: `reception_score`, `installed_base_count`, `feedback_code`, `product_id`, `hospital_id`, `installed_system_id`.

### Q2 2026 (11) — When intravascular-lithotripsy trials reach the market

The milestone carries expected clearance and market-release days for the intravascular-lithotripsy indication.

`stryker.commercial.fact_trial_milestone`: `indication_code`, `milestone_status`, `expected_clearance_calendar_day_id`, `market_release_calendar_day_id`, `clinical_trial_id`.

### Q2 2026 (13) — Organic drag from the Inari supply shortfall

Lost sales and organic drag sit next to the underlying growth rate the franchise would have shown.

`stryker.supply.fact_supply_shortage`: `organic_drag_amount`, `lost_sales_amount`, `underlying_growth_rate`, `product_franchise_id`.

### Q2 2026 (14) — Launch delays and where the new robotics platform lands

Launch delay is tied to plant recovery, and site mix says surgery center versus hospital.

`stryker.supply.fact_product_launch`: `launch_delay_flag`, `plant_recovery_calendar_day_id`, `site_mix_code`, `capital_system_id`, `site_of_care_id`.

### Q1 2026 (4) — Order pause: supply versus hospital demand

The pause splits unfilled orders into inability to supply and a change in demand, beside underlying procedure and capital demand.

`stryker.commercial.fact_order_pause`: `unfilled_order_amount`, `supply_inability_amount`, `demand_change_amount`, `procedure_demand_amount`, `capital_demand_amount`, `hospital_id`.
`stryker.market.fact_hospital_demand`: `underlying_procedure_demand`, `underlying_capital_demand`, `hospital_id`.

### Q1 2026 (5) — Pre-commercial vascular deals versus the historical preference

Target stage is compared with the historical preference for commercial businesses.

`stryker.commercial.fact_acquisition`: `target_stage_code`, `historical_preference_code`, `deal_stage_shift_flag`, `acquisition_target_id`.

### Q1 2026 (6) — How Inari grows from here

Post-integration run rate and the effect of a pending competitive deal are on the franchise result.

`stryker.commercial.fact_franchise_result`: `post_integration_run_rate`, `competitive_deal_effect_amount`, `growth_rate`, `product_franchise_id`.

### Q1 2026 (8) — Cyber incident across MedSurg and orthopedics

Disruption amount and recovery cadence are stored by franchise group through the year.

`stryker.commercial.fact_franchise_result`: `cyber_disruption_effect_amount`, `recovery_cadence_code`, `product_franchise_id`, `accounting_period_id`.
`stryker.product.dim_product_franchise`: `franchise_group`, `franchise_code`.

### Q1 2026 (9) — Runway for Pangaea and LIFEPAK, including internationally

Remaining opportunity is stored on the franchise result with an international flag.

`stryker.commercial.fact_franchise_result`: `remaining_opportunity_amount`, `international_flag`, `growth_rate`, `country_id`, `product_franchise_id`.

### Q1 2026 (10) — Robotics portfolio consolidation and surgery-center placements

A placement is either attached to Mako or independent, and counts are split between surgery centers and hospitals.

`stryker.capital.fact_capital_placement`: `attach_to_installed_base_flag`, `independent_placement_flag`, `asc_placement_count`, `hospital_placement_count`, `capital_system_id`, `site_of_care_id`.
`stryker.capital.fact_robotics_portfolio`: `portfolio_role_code`, `capital_system_id`, `related_capital_system_id`.

### Q1 2026 (11) — Amplitude products through the Inari sales force

The channel row says whether the Inari team sells the product and whether that is the model for later peripheral and coronary products.

`stryker.commercial.fact_sales_channel`: `uses_inari_sales_force_flag`, `later_product_model_flag`, `indication_code`, `sales_force_id`, `product_id`.

### Q1 2026 (12) — Approval timing for peripheral and coronary indications

Milestone status and expected clearance day are stored by indication.

`stryker.commercial.fact_trial_milestone`: `indication_code`, `milestone_status`, `expected_clearance_calendar_day_id`, `clinical_trial_id`.

### Q1 2026 (13) — Soft-tissue robotics: capital system or remanufactured instruments

The instrument model distinguishes a capital system from remanufactured instruments and consumables.

`stryker.capital.fact_instrument_model`: `model_code`, `opportunity_flag`, `capital_system_id`, `product_id`.

### Q1 2026 (14) — Time to restock the field

Days to restock are compared with the share of representative time still spent on supply recovery.

`stryker.commercial.fact_field_inventory`: `days_to_restock`, `selling_time_share`, `recovery_time_share`, `channel_inventory_quantity`, `manufacturing_plant_id`, `sales_force_id`.

### Q4 2025 (3) — Trauma, vascular, Mako, endoscopy, and instruments, including stocking

Franchise growth is read next to channel stocking and destocking.

`stryker.commercial.fact_franchise_result`: `growth_rate`, `product_franchise_id`, `country_id`.
`stryker.commercial.fact_channel_inventory`: `stocking_amount`, `destocking_amount`, `product_franchise_id`.

### Q4 2025 (7) — MedSurg growth versus other device markets

MedSurg growth is stored against broader medtech market growth and a durability code.

`stryker.commercial.fact_franchise_result`: `growth_rate`, `medtech_market_growth_rate`, `durability_code`, `product_franchise_id`.

### Q4 2025 (8) — Product cycles that are incremental this year

Each launch carries a cycle stage and the growth it contributes.

`stryker.supply.fact_product_launch`: `cycle_stage_code`, `growth_contribution_amount`, `product_id`.
`stryker.product.dim_product`: `cycle_stage`, `launch_year`, `product_franchise_id`.

### Q4 2025 (9) — Visibility on destocking and sales-force disruption

Channel rows flag whether the fourth-quarter shortfall is visible and temporary.

`stryker.commercial.fact_channel_inventory`: `visibility_flag`, `temporary_effect_flag`, `destocking_amount`, `sales_force_id`, `accounting_period_id`.

### Q4 2025 (10) — X-ray imaging rather than CT on the new robotics platform

Imaging choice on the new system is stored against the related installed Mako system.

`stryker.capital.fact_robotics_portfolio`: `imaging_choice_code`, `capital_system_id`, `related_capital_system_id`.
`stryker.capital.dim_capital_system`: `imaging_mode`, `system_code`.

### Q4 2025 (11) — Handheld robot and Mako 4

Portfolio role says whether the handheld system adds to Mako 4 or stands alone.

`stryker.capital.fact_robotics_portfolio`: `portfolio_role_code`, `form_factor_code`, `capital_system_id`, `related_capital_system_id`.

### Q4 2025 (15) — Pulmonary-embolism trial timeline

The milestone says whether the trial is on the published timeline and when data is expected.

`stryker.commercial.fact_trial_milestone`: `indication_code`, `published_timeline_flag`, `data_expected_calendar_day_id`, `milestone_status`, `competitor_readout_flag`.

### Q4 2025 (17) — Vascular build-out and calcium management

The acquisition row flags vascular priority and a calcium-management adjacency.

`stryker.commercial.fact_acquisition`: `vascular_priority_flag`, `adjacency_code`, `product_franchise_id`, `target_stage_code`.

### Q4 2025 (18) — Mako 4 price and upgrade fees for shoulder and spine

System price is compared with the prior system, and upgrade fees are tied to the added procedure family.

`stryker.capital.fact_system_price`: `system_price_amount`, `prior_system_price_amount`, `upgrade_fee_amount`, `higher_price_flag`, `capital_system_id`, `prior_capital_system_id`, `procedure_family_id`.

### Q4 2025 (20) — Mako utilization and the share of knees and hips on Mako

Utilization and the share of the procedure family done on the installed system are the adoption measures.

`stryker.capital.fact_mako_utilization`: `utilization_rate`, `procedure_share_on_system`, `adoption_driver_code`, `installed_system_id`, `procedure_family_id`.

### Q4 2025 (22) — Softer capital in Europe and device regulation

European capital demand and a regulatory-friction flag are stored by country and franchise.

`stryker.commercial.fact_europe_capital`: `capital_demand_amount`, `regulatory_friction_flag`, `softness_driver_code`, `country_id`, `product_franchise_id`.

### Q4 2025 (23) — Breast-care sales force and endoscopy attachment

Calling effort of the specialized team is compared with endoscopy attachment to the installed base.

`stryker.commercial.fact_endoscopy_attachment`: `calling_effort`, `attachment_rate`, `sales_force_id`, `installed_system_id`, `product_franchise_id`.

### Q2 2025 (1) — Remanufactured instruments in soft-tissue robotics

The instrument model flags a remanufactured-instrument opportunity and the sustainability capability behind it.

`stryker.capital.fact_instrument_model`: `model_code`, `opportunity_flag`, `sustainability_capability_flag`, `capital_system_id`.

### Q2 2025 (4) — Greenfield opportunity for Mako

Placements flag greenfield accounts, and installed systems flag accounts that already have a robot.

`stryker.capital.fact_capital_placement`: `greenfield_flag`, `placement_count`, `hospital_id`, `capital_system_id`.
`stryker.capital.dim_installed_system`: `greenfield_account_flag`, `installed_flag`, `hospital_id`, `capital_system_id`.

### Q2 2025 (5) — MedSurg supply duration and adoption of the expanded Mako

Shortage status and the expected clear quarter sit beside placements for shoulder, hip, knee, and spine.

`stryker.supply.fact_supply_shortage`: `shortage_status`, `shortage_scope_code`, `expected_clear_accounting_period_id`, `product_franchise_id`.
`stryker.capital.fact_capital_placement`: `application_code`, `placement_count`, `capital_system_id`.

### Q2 2025 (6) — Inari through destocking and sales-force transition

Reported growth is stored beside destocking, underlying demand, and the flag for a return to market growth.

`stryker.commercial.fact_channel_inventory`: `reported_growth_rate`, `destocking_amount`, `underlying_demand_amount`, `return_to_market_growth_flag`, `product_franchise_id`.
`stryker.commercial.fact_sales_disruption`: `transition_flag`, `product_franchise_id`.

### Q2 2025 (8) — Drivers of record Mako system adds

Placement counts are split by application, including shoulder and spine.

`stryker.capital.fact_capital_placement`: `placement_count`, `application_code`, `capital_system_id`, `accounting_period_id`.

### Q2 2025 (10) — Interventional-spine launch, including OptiBlade

Launch metric and investment are stored on the product launch for that product.

`stryker.supply.fact_product_launch`: `launch_metric`, `investment_amount`, `product_id`, `accounting_period_id`.

### Q2 2025 (11) — Sales disruption from the Inari noncompete

Assumed lost productivity and the revenue effect in the outlook are on the sales disruption row.

`stryker.commercial.fact_sales_disruption`: `assumed_lost_productivity`, `revenue_outlook_effect_amount`, `noncompete_flag`, `sales_force_id`, `product_franchise_id`.

### Q2 2025 (12) — Limit of a single-robot strategy

The portfolio row states whether the strategy stays on one platform and whether surgeons prefer another form factor.

`stryker.capital.fact_robotics_portfolio`: `single_platform_strategy_flag`, `surgeon_preference_code`, `form_factor_code`, `capital_system_id`.

### Q2 2025 (13) — Trauma growth as the Pangaea launch is lapped

The franchise result flags the launch lap and whether a double-digit rate is still expected.

`stryker.commercial.fact_franchise_result`: `growth_rate`, `launch_lap_flag`, `double_digit_sustainable_flag`, `product_franchise_id`.

### Q2 2025 (14) — Whether the market is moving toward fully autonomous robotics

Autonomy expectation is the surgeon-adoption read next to the current platform.

`stryker.capital.fact_robotics_portfolio`: `autonomy_expectation_code`, `capital_system_id`, `related_capital_system_id`.

### Q2 2025 (18) — International Mako ramp versus the earlier U.S. ramp

International and U.S. ramp rates are stored with a flag for a structural constraint.

`stryker.capital.fact_international_system`: `us_ramp_rate`, `international_ramp_rate`, `structural_constraint_flag`, `country_id`, `capital_system_id`.

### Q2 2025 (19) — Hospital capital budgets and accelerated depreciation

Budget change and purchasing behavior are stored with the depreciation flag.

`stryker.commercial.fact_capital_budget`: `accelerated_depreciation_flag`, `budget_change_amount`, `purchasing_behavior_code`, `capital_environment_code`, `hospital_id`.

### Q2 2025 (21) — Commercial path for Mako spine and shoulder outside the United States

Commercial path status and availability are stored by country and procedure family.

`stryker.capital.fact_international_system`: `commercial_path_status`, `international_available_flag`, `us_launch_calendar_day_id`, `country_id`, `procedure_family_id`, `capital_system_id`.

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `stryker.product.dim_product_franchise` | Q1 2026 (8) |
| `stryker.product.dim_product` | Q4 2025 (8) |
| `stryker.capital.dim_capital_system` | Q4 2025 (10) |
| `stryker.capital.dim_installed_system` | Q2 2025 (4) |
| `stryker.capital.fact_capital_placement` | Q1 2026 (10), Q2 2025 (4), Q2 2025 (5), Q2 2025 (8) |
| `stryker.capital.fact_system_price` | Q4 2025 (18) |
| `stryker.capital.fact_mako_utilization` | Q4 2025 (20) |
| `stryker.capital.fact_robotics_portfolio` | Q1 2026 (10), Q4 2025 (10), Q4 2025 (11), Q2 2025 (12), Q2 2025 (14) |
| `stryker.capital.fact_international_system` | Q2 2025 (18), Q2 2025 (21) |
| `stryker.capital.fact_instrument_model` | Q1 2026 (13), Q2 2025 (1) |
| `stryker.capital.fact_offering_reception` | Q2 2026 (10) |
| `stryker.supply.dim_manufacturing_plant` | — |
| `stryker.supply.dim_manufacturing_shift` | — |
| `stryker.supply.dim_component` | — |
| `stryker.supply.fact_supply_shortage` | Q2 2026 (6), Q2 2026 (13), Q2 2025 (5) |
| `stryker.supply.fact_capacity_plan` | Q2 2026 (8) |
| `stryker.supply.fact_product_launch` | Q2 2026 (14), Q4 2025 (8), Q2 2025 (10) |
| `stryker.commercial.dim_sales_force` | — |
| `stryker.commercial.dim_clinical_trial` | — |
| `stryker.commercial.dim_acquisition_target` | — |
| `stryker.commercial.fact_equipment_order` | — |
| `stryker.commercial.fact_order_backlog` | Q2 2026 (2) |
| `stryker.commercial.fact_order_pause` | Q1 2026 (4) |
| `stryker.commercial.fact_channel_inventory` | Q4 2025 (3), Q4 2025 (9), Q2 2025 (6) |
| `stryker.commercial.fact_field_inventory` | Q1 2026 (14) |
| `stryker.commercial.fact_trial_milestone` | Q2 2026 (11), Q1 2026 (12), Q4 2025 (15) |
| `stryker.commercial.fact_acquisition` | Q1 2026 (5), Q4 2025 (17) |
| `stryker.commercial.fact_sales_channel` | Q1 2026 (11) |
| `stryker.commercial.fact_franchise_result` | Q2 2026 (6), Q1 2026 (6), Q1 2026 (8), Q1 2026 (9), Q4 2025 (3), Q4 2025 (7), Q2 2025 (13) |
| `stryker.commercial.fact_endoscopy_attachment` | Q4 2025 (23) |
| `stryker.commercial.fact_europe_capital` | Q4 2025 (22) |
| `stryker.commercial.fact_sales_disruption` | Q2 2025 (6), Q2 2025 (11) |
| `stryker.commercial.fact_capital_budget` | Q2 2025 (19) |
