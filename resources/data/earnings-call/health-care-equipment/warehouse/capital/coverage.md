# Surgical Supply Inc capital and products

Stryker placements and implants, Intuitive system generations, instruments per procedure, orders, backlog and supply.

Every fact below uses `fiscal_period_id` for the fiscal period and `scenario_id` for the scenario (`reported` or `guide` in `dim_scenario`). Measure descriptions in the YAML name the unit.

## Stryker (SYK)

### Q2 2026 (1)

How much of the quarter was underlying demand versus catch-up from the first-quarter disruption, across capital, vascular, hips, and medical?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2026 (5)

Were U.S. hip and knee results lighter because of share shifts?

- `surgicalsupply.supply.fact_supply_shortage_quantity`: `shortage_unit_count`, `deferred_procedure_count`, `lost_procedure_count`, `stryker_business_id`
- `surgicalsupply.supply.fact_capacity_quantity`: `planned_shift_count`, `required_shipment_unit_count`, `produced_unit_count`
- `surgicalsupply.supply.fact_field_inventory_quantity`: `field_inventory_unit_count`, `days_to_restock_count`

### Q2 2026 (6)

Was the Inari supply disruption limited to that business or did it hit other vascular products?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2026 (7)

What volume growth, capital conversion, and backlog realization are assumed in the back half?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2026 (8)

What could keep the production ramp from meeting the back-half plan?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2026 (9)

Can peripheral vascular reaccelerate once the short supply issue clears, given those procedures cannot be delayed?

- `surgicalsupply.supply.fact_supply_shortage_quantity`: `shortage_unit_count`, `deferred_procedure_count`, `lost_procedure_count`, `stryker_business_id`
- `surgicalsupply.supply.fact_capacity_quantity`: `planned_shift_count`, `required_shipment_unit_count`, `produced_unit_count`
- `surgicalsupply.supply.fact_field_inventory_quantity`: `field_inventory_unit_count`, `days_to_restock_count`

### Q2 2026 (10)

How is SmartCare and the smart-hospital offering, including Vocera, being received?

- `surgicalsupply.commercial.fact_clinical_trial_quantity`: `enrolled_patient_count`, `milestone_count`, `clinical_trial_id`
- `surgicalsupply.commercial.fact_acquisition_amount`: `acquisition_amount`, `target_revenue_amount`
- `surgicalsupply.commercial.fact_sales_channel_quantity`: `sold_unit_count`, `sales_channel_id`
- `surgicalsupply.commercial.fact_launch_quantity`: `launch_account_count`, `launch_procedure_count`

### Q2 2026 (11)

When do the intravascular-lithotripsy trials reach the market?

- `surgicalsupply.commercial.fact_clinical_trial_quantity`: `enrolled_patient_count`, `milestone_count`, `clinical_trial_id`
- `surgicalsupply.commercial.fact_acquisition_amount`: `acquisition_amount`, `target_revenue_amount`
- `surgicalsupply.commercial.fact_sales_channel_quantity`: `sold_unit_count`, `sales_channel_id`
- `surgicalsupply.commercial.fact_launch_quantity`: `launch_account_count`, `launch_procedure_count`

### Q2 2026 (12)

How much of the quarter was revenue recognition, procedure catch-up, and capital, and what recovery is still ahead?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2026 (13)

How large an organic drag was the Inari supply shortfall?

- `surgicalsupply.supply.fact_supply_shortage_quantity`: `shortage_unit_count`, `deferred_procedure_count`, `lost_procedure_count`, `stryker_business_id`
- `surgicalsupply.supply.fact_capacity_quantity`: `planned_shift_count`, `required_shipment_unit_count`, `produced_unit_count`
- `surgicalsupply.supply.fact_field_inventory_quantity`: `field_inventory_unit_count`, `days_to_restock_count`

### Q2 2026 (14)

Is the manufacturing disruption delaying recent or upcoming launches, and is the new robotics platform landing in surgery centers or hospitals?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q1 2026 (1)

How should sales and earnings cadence look for the rest of the year after reiterating the outlook despite the disruption?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q1 2026 (3)

What is changing competitively in orthopedics given the disruption, a possible spin, and sales-force moves at rivals?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q1 2026 (4)

How much of the order pause was inability to supply versus a change in hospital demand?

- `surgicalsupply.supply.fact_supply_shortage_quantity`: `shortage_unit_count`, `deferred_procedure_count`, `lost_procedure_count`, `stryker_business_id`
- `surgicalsupply.supply.fact_capacity_quantity`: `planned_shift_count`, `required_shipment_unit_count`, `produced_unit_count`
- `surgicalsupply.supply.fact_field_inventory_quantity`: `field_inventory_unit_count`, `days_to_restock_count`

### Q1 2026 (5)

Does buying a pre-commercial vascular company mean more early-stage deals now that the base is larger?

- `surgicalsupply.commercial.fact_clinical_trial_quantity`: `enrolled_patient_count`, `milestone_count`, `clinical_trial_id`
- `surgicalsupply.commercial.fact_acquisition_amount`: `acquisition_amount`, `target_revenue_amount`
- `surgicalsupply.commercial.fact_sales_channel_quantity`: `sold_unit_count`, `sales_channel_id`
- `surgicalsupply.commercial.fact_launch_quantity`: `launch_account_count`, `launch_procedure_count`

### Q1 2026 (6)

How should Inari grow from here, including any effect from a pending deal in the space?

- `surgicalsupply.commercial.fact_clinical_trial_quantity`: `enrolled_patient_count`, `milestone_count`, `clinical_trial_id`
- `surgicalsupply.commercial.fact_acquisition_amount`: `acquisition_amount`, `target_revenue_amount`
- `surgicalsupply.commercial.fact_sales_channel_quantity`: `sold_unit_count`, `sales_channel_id`
- `surgicalsupply.commercial.fact_launch_quantity`: `launch_account_count`, `launch_procedure_count`

### Q1 2026 (7)

What is driving the reacceleration in orthopedics outside the U.S. versus peers?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q1 2026 (9)

How much runway remains for Pangaea and LIFEPAK, including internationally?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q1 2026 (10)

How is the orthopedic technology portfolio being consolidated, and is the new robotics platform adding to Mako or growing on its own in surgery centers?

- `surgicalsupply.capital.fact_stryker_placement_event`: `placed_system_count`, `stryker_robot_platform_id`, `hospital_id`, `site_type_id`
- `surgicalsupply.capital.fact_stryker_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.commercial.fact_order_backlog_quantity`: `open_backlog_unit_count`, `planned_shipment_unit_count`
- `surgicalsupply.commercial.fact_equipment_order_quantity`: `ordered_unit_count`, `unfilled_unit_count`

### Q1 2026 (11)

Will Amplitude's products, once approved, be sold through the Inari sales force, and is that the model for later peripheral and coronary products?

- `surgicalsupply.commercial.fact_clinical_trial_quantity`: `enrolled_patient_count`, `milestone_count`, `clinical_trial_id`
- `surgicalsupply.commercial.fact_acquisition_amount`: `acquisition_amount`, `target_revenue_amount`
- `surgicalsupply.commercial.fact_sales_channel_quantity`: `sold_unit_count`, `sales_channel_id`
- `surgicalsupply.commercial.fact_launch_quantity`: `launch_account_count`, `launch_procedure_count`

### Q1 2026 (12)

What is the approval timing for peripheral and coronary indications?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q1 2026 (14)

How long does it take to restock the field so representatives can sell rather than recover supply?

- `surgicalsupply.supply.fact_supply_shortage_quantity`: `shortage_unit_count`, `deferred_procedure_count`, `lost_procedure_count`, `stryker_business_id`
- `surgicalsupply.supply.fact_capacity_quantity`: `planned_shift_count`, `required_shipment_unit_count`, `produced_unit_count`
- `surgicalsupply.supply.fact_field_inventory_quantity`: `field_inventory_unit_count`, `days_to_restock_count`

### Q1 2026 (15)

What ramp is expected for Mako shoulder, and how healthy is the shoulder market?

- `surgicalsupply.capital.fact_stryker_placement_event`: `placed_system_count`, `stryker_robot_platform_id`, `hospital_id`, `site_type_id`
- `surgicalsupply.capital.fact_stryker_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.commercial.fact_order_backlog_quantity`: `open_backlog_unit_count`, `planned_shipment_unit_count`
- `surgicalsupply.commercial.fact_equipment_order_quantity`: `ordered_unit_count`, `unfilled_unit_count`

### Q1 2026 (16)

Have customer relationships held after the cyber incident?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q4 2025 (2)

How should capital and implant pricing, and the capital-equipment environment, look this year after a strong finish?

- `surgicalsupply.product.fact_product_price`: `unit_price_amount`, `medical_product_id`
- `surgicalsupply.product.fact_product_shipment_quantity`: `shipped_unit_count`
- `surgicalsupply.capital.fact_system_price`: `system_unit_price_amount`, `upgrade_fee_amount`

### Q4 2025 (3)

What happened in trauma and extremities and in vascular versus stronger Mako, endoscopy, and instruments, including any stocking?

- `surgicalsupply.capital.fact_stryker_placement_event`: `placed_system_count`, `stryker_robot_platform_id`, `hospital_id`, `site_type_id`
- `surgicalsupply.capital.fact_stryker_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.commercial.fact_order_backlog_quantity`: `open_backlog_unit_count`, `planned_shipment_unit_count`
- `surgicalsupply.commercial.fact_equipment_order_quantity`: `ordered_unit_count`, `unfilled_unit_count`

### Q4 2025 (4)

How do a competitor's vascular acquisition and a possible orthopedic spin change the competitive landscape?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q4 2025 (6)

Is the operating-margin expansion path through 2028 still intact after recent performance?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q4 2025 (9)

How much visibility is there on destocking or sales-force disruption that affected the quarter?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q4 2025 (10)

Why use X-ray imaging rather than CT on the new robotics platform?

- `surgicalsupply.capital.fact_stryker_placement_event`: `placed_system_count`, `stryker_robot_platform_id`, `hospital_id`, `site_type_id`
- `surgicalsupply.capital.fact_stryker_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.commercial.fact_order_backlog_quantity`: `open_backlog_unit_count`, `planned_shipment_unit_count`
- `surgicalsupply.commercial.fact_equipment_order_quantity`: `ordered_unit_count`, `unfilled_unit_count`

### Q4 2025 (11)

How does the handheld robot fit with Mako 4 in the robotics portfolio?

- `surgicalsupply.capital.fact_stryker_placement_event`: `placed_system_count`, `stryker_robot_platform_id`, `hospital_id`, `site_type_id`
- `surgicalsupply.capital.fact_stryker_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.commercial.fact_order_backlog_quantity`: `open_backlog_unit_count`, `planned_shipment_unit_count`
- `surgicalsupply.commercial.fact_equipment_order_quantity`: `ordered_unit_count`, `unfilled_unit_count`

### Q4 2025 (13)

How do U.S. and international growth drivers differ?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q4 2025 (14)

Was the smaller MedSurg price benefit temporary, and does company price depend on MedSurg price recovering?

- `surgicalsupply.product.fact_product_price`: `unit_price_amount`, `medical_product_id`
- `surgicalsupply.product.fact_product_shipment_quantity`: `shipped_unit_count`
- `surgicalsupply.capital.fact_system_price`: `system_unit_price_amount`, `upgrade_fee_amount`

### Q4 2025 (15)

Is the pulmonary-embolism trial still on the published timeline, and when is the data expected?

- `surgicalsupply.commercial.fact_clinical_trial_quantity`: `enrolled_patient_count`, `milestone_count`, `clinical_trial_id`
- `surgicalsupply.commercial.fact_acquisition_amount`: `acquisition_amount`, `target_revenue_amount`
- `surgicalsupply.commercial.fact_sales_channel_quantity`: `sold_unit_count`, `sales_channel_id`
- `surgicalsupply.commercial.fact_launch_quantity`: `launch_account_count`, `launch_procedure_count`

### Q4 2025 (16)

What changes for endoscopy and other franchises as more procedures leave the inpatient-only list?

- `surgicalsupply.commercial.fact_clinical_trial_quantity`: `enrolled_patient_count`, `milestone_count`, `clinical_trial_id`
- `surgicalsupply.commercial.fact_acquisition_amount`: `acquisition_amount`, `target_revenue_amount`
- `surgicalsupply.commercial.fact_sales_channel_quantity`: `sold_unit_count`, `sales_channel_id`
- `surgicalsupply.commercial.fact_launch_quantity`: `launch_account_count`, `launch_procedure_count`

### Q4 2025 (17)

Is vascular still a build-out priority, including calcium management adjacent to the current portfolio?

- `surgicalsupply.commercial.fact_clinical_trial_quantity`: `enrolled_patient_count`, `milestone_count`, `clinical_trial_id`
- `surgicalsupply.commercial.fact_acquisition_amount`: `acquisition_amount`, `target_revenue_amount`
- `surgicalsupply.commercial.fact_sales_channel_quantity`: `sold_unit_count`, `sales_channel_id`
- `surgicalsupply.commercial.fact_launch_quantity`: `launch_account_count`, `launch_procedure_count`

### Q4 2025 (18)

Does Mako 4 carry a higher price than the prior system, and are there upgrade fees to add shoulder and spine?

- `surgicalsupply.capital.fact_stryker_placement_event`: `placed_system_count`, `stryker_robot_platform_id`, `hospital_id`, `site_type_id`
- `surgicalsupply.capital.fact_stryker_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.commercial.fact_order_backlog_quantity`: `open_backlog_unit_count`, `planned_shipment_unit_count`
- `surgicalsupply.commercial.fact_equipment_order_quantity`: `ordered_unit_count`, `unfilled_unit_count`

### Q4 2025 (19)

Can this year's tariff cost be absorbed or reduced over time?

- `surgicalsupply.supply.fact_supply_shortage_quantity`: `shortage_unit_count`, `deferred_procedure_count`, `lost_procedure_count`, `stryker_business_id`
- `surgicalsupply.supply.fact_capacity_quantity`: `planned_shift_count`, `required_shipment_unit_count`, `produced_unit_count`
- `surgicalsupply.supply.fact_field_inventory_quantity`: `field_inventory_unit_count`, `days_to_restock_count`

### Q4 2025 (20)

Where do Mako utilization and the share of knees and hips on Mako go from here?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q4 2025 (21)

How does price split between MedSurg and orthopedics versus last year?

- `surgicalsupply.product.fact_product_price`: `unit_price_amount`, `medical_product_id`
- `surgicalsupply.product.fact_product_shipment_quantity`: `shipped_unit_count`
- `surgicalsupply.capital.fact_system_price`: `system_unit_price_amount`, `upgrade_fee_amount`

### Q4 2025 (22)

What is behind the softer capital environment in Europe, and did European device regulation affect MedSurg there?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q4 2025 (23)

What does a specialized breast-care sales force mean for pushing more endoscopy through the installed base?

- `surgicalsupply.commercial.fact_clinical_trial_quantity`: `enrolled_patient_count`, `milestone_count`, `clinical_trial_id`
- `surgicalsupply.commercial.fact_acquisition_amount`: `acquisition_amount`, `target_revenue_amount`
- `surgicalsupply.commercial.fact_sales_channel_quantity`: `sold_unit_count`, `sales_channel_id`
- `surgicalsupply.commercial.fact_launch_quantity`: `launch_account_count`, `launch_procedure_count`

### Q2 2025 (2)

How far along is surgery-center construction beyond orthopedics, including if ablation moves to that setting?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2025 (3)

Why did the tariff estimate come down only modestly, given manufacturing locations?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2025 (4)

How much greenfield opportunity remains for Mako?

- `surgicalsupply.capital.fact_stryker_placement_event`: `placed_system_count`, `stryker_robot_platform_id`, `hospital_id`, `site_type_id`
- `surgicalsupply.capital.fact_stryker_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.commercial.fact_order_backlog_quantity`: `open_backlog_unit_count`, `planned_shipment_unit_count`
- `surgicalsupply.commercial.fact_equipment_order_quantity`: `ordered_unit_count`, `unfilled_unit_count`

### Q2 2025 (5)

How long does the MedSurg supply issue last, and how is the newest Mako, with shoulder, hip, knee, and spine, being adopted?

- `surgicalsupply.capital.fact_stryker_placement_event`: `placed_system_count`, `stryker_robot_platform_id`, `hospital_id`, `site_type_id`
- `surgicalsupply.capital.fact_stryker_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.commercial.fact_order_backlog_quantity`: `open_backlog_unit_count`, `planned_shipment_unit_count`
- `surgicalsupply.commercial.fact_equipment_order_quantity`: `ordered_unit_count`, `unfilled_unit_count`

### Q2 2025 (6)

How did Inari grow through destocking and sales-force transition, and when does growth return to the market rate?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2025 (7)

What drove the U.S. endoscopy acceleration versus the prior quarter?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2025 (8)

What is driving another quarter of record Mako system adds: shoulder, spine, or something else?

- `surgicalsupply.capital.fact_stryker_placement_event`: `placed_system_count`, `stryker_robot_platform_id`, `hospital_id`, `site_type_id`
- `surgicalsupply.capital.fact_stryker_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.commercial.fact_order_backlog_quantity`: `open_backlog_unit_count`, `planned_shipment_unit_count`
- `surgicalsupply.commercial.fact_equipment_order_quantity`: `ordered_unit_count`, `unfilled_unit_count`

### Q2 2025 (10)

How is the interventional-spine launch, including OptiBlade, tracking?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2025 (11)

How much sales disruption is assumed from the Inari noncompete and sales-force change?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2025 (12)

Is there a limit to a single-robot strategy as competitors offer multiple form factors?

- `surgicalsupply.commercial.fact_clinical_trial_quantity`: `enrolled_patient_count`, `milestone_count`, `clinical_trial_id`
- `surgicalsupply.commercial.fact_acquisition_amount`: `acquisition_amount`, `target_revenue_amount`
- `surgicalsupply.commercial.fact_sales_channel_quantity`: `sold_unit_count`, `sales_channel_id`
- `surgicalsupply.commercial.fact_launch_quantity`: `launch_account_count`, `launch_procedure_count`

### Q2 2025 (13)

Can trauma stay at a double-digit growth rate as the Pangaea launch is lapped?

- `surgicalsupply.supply.fact_supply_shortage_quantity`: `shortage_unit_count`, `deferred_procedure_count`, `lost_procedure_count`, `stryker_business_id`
- `surgicalsupply.supply.fact_capacity_quantity`: `planned_shift_count`, `required_shipment_unit_count`, `produced_unit_count`
- `surgicalsupply.supply.fact_field_inventory_quantity`: `field_inventory_unit_count`, `days_to_restock_count`

### Q2 2025 (15)

How do shoulder procedures moving into surgery centers balance volume against price?

- `surgicalsupply.product.fact_product_price`: `unit_price_amount`, `medical_product_id`
- `surgicalsupply.product.fact_product_shipment_quantity`: `shipped_unit_count`
- `surgicalsupply.capital.fact_system_price`: `system_unit_price_amount`, `upgrade_fee_amount`

### Q2 2025 (17)

How is China changing with tariffs and the local health-care market, given the company is under-indexed there?

- `surgicalsupply.supply.fact_supply_shortage_quantity`: `shortage_unit_count`, `deferred_procedure_count`, `lost_procedure_count`, `stryker_business_id`
- `surgicalsupply.supply.fact_capacity_quantity`: `planned_shift_count`, `required_shipment_unit_count`, `produced_unit_count`
- `surgicalsupply.supply.fact_field_inventory_quantity`: `field_inventory_unit_count`, `days_to_restock_count`

### Q2 2025 (18)

Is there anything structural that would make the international Mako ramp differ from the earlier U.S. ramp?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2025 (19)

Are hospitals changing capital budgets because of accelerated depreciation?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2025 (20)

Are competitor hip launches creating pressure, and is the share of procedures done robotically still rising?

- `surgicalsupply.supply.fact_supply_shortage_quantity`: `shortage_unit_count`, `deferred_procedure_count`, `lost_procedure_count`, `stryker_business_id`
- `surgicalsupply.supply.fact_capacity_quantity`: `planned_shift_count`, `required_shipment_unit_count`, `produced_unit_count`
- `surgicalsupply.supply.fact_field_inventory_quantity`: `field_inventory_unit_count`, `days_to_restock_count`

### Q2 2025 (21)

What is the commercial opportunity for Mako spine and shoulder outside the U.S.?

- `surgicalsupply.capital.fact_stryker_placement_event`: `placed_system_count`, `stryker_robot_platform_id`, `hospital_id`, `site_type_id`
- `surgicalsupply.capital.fact_stryker_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.commercial.fact_order_backlog_quantity`: `open_backlog_unit_count`, `planned_shipment_unit_count`
- `surgicalsupply.commercial.fact_equipment_order_quantity`: `ordered_unit_count`, `unfilled_unit_count`

## Intuitive Surgical (ISRG)

### Q1 2026 (2)

What in the cost base, beyond a smaller tariff headwind, supported the higher gross-margin outlook, and how does da Vinci 5 contribution margin compare with Xi?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q1 2026 (3)

Can innovation-led revenue keep growing faster than procedure volumes?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q1 2026 (4)

How much further can after-hours use and da Vinci 5 utilization rise, and how does that turn into system placements?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q1 2026 (5)

How are refurbished Xi systems and tiered pricing being used against new robotic competitors in the U.S., China, and Europe?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q1 2026 (6)

Why did international instruments and accessories grow much faster than international procedures, and was that one-time or country-specific?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q1 2026 (7)

What clearances and instruments still have to arrive before single-port adoption accelerates?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q1 2026 (8)

How should the international actions, including European distributors, refurbished systems, and the China joint venture, be read together?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q4 2025 (1)

Do additional advanced-imaging features use the existing robot hardware or require new hardware?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q4 2025 (4)

What does a digital subscription add to da Vinci 5 adoption and the growth outlook?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q4 2025 (6)

For lower-acuity cases, is the answer a lower-priced form factor or refurbished systems?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q3 2025 (2)

How are refurbished Xi systems being placed as customers upgrade and move older systems to new sites of care?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q3 2025 (3)

When a hospital buys da Vinci 5 and keeps the older Xi, what utilization and new procedure categories show up on the redeployed system?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q3 2025 (4)

What gaps in cardiac care are the newer platforms meant to address?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q3 2025 (5)

How should U.S. utilization trend as da Vinci 5 becomes a larger share of the installed base?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q3 2025 (7)

How long does bariatric volume remain a drag on procedure growth?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q3 2025 (9)

How much are hub and cloud-account features contributing to da Vinci use?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q3 2025 (10)

How do capital cost, Medicare and commercial rates, instrument cost, and sterilization change the economics of placing systems in surgery centers?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q3 2025 (11)

Which procedure categories benefit most from force feedback on da Vinci 5?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2025 (2)

Can instrument reprocessing and longer useful life be done in-house?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2025 (3)

How is hospital capital-spending risk from policy changes showing up in system-placement conversations?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2025 (4)

Where do force-feedback evaluations and capacity stand, and is that already changing instruments and accessories per procedure?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`

### Q2 2025 (5)

How should system placements outside the U.S. trend after the European and Japan approvals?

- `surgicalsupply.capital.fact_stryker_placement_event`: `placed_system_count`, `stryker_robot_platform_id`, `hospital_id`, `site_type_id`
- `surgicalsupply.capital.fact_stryker_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.commercial.fact_order_backlog_quantity`: `open_backlog_unit_count`, `planned_shipment_unit_count`
- `surgicalsupply.commercial.fact_equipment_order_quantity`: `ordered_unit_count`, `unfilled_unit_count`

### Q2 2025 (6)

Which additional da Vinci 5 features arrive with the broader launch, and how do they change adoption?

- `surgicalsupply.capital.fact_intuitive_placement_event`: `placed_system_count`, `intuitive_system_generation_id`, `payment_arrangement_id`, `system_condition_id`
- `surgicalsupply.capital.fact_intuitive_installed_quantity`: `installed_system_count`, `active_system_count`
- `surgicalsupply.capital.fact_intuitive_utilization_quantity`: `system_procedure_count`, `after_hours_procedure_count`
- `surgicalsupply.capital.fact_instruments_accessories_quantity`: `instrument_unit_count`, `accessory_unit_count`, `procedure_count`
- `surgicalsupply.capital.fact_instruments_per_procedure_rate`: `instrument_units_per_procedure`, `accessory_revenue_per_procedure_amount`
