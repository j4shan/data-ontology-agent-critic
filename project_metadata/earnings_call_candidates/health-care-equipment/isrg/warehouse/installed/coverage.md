# Intuitive Surgical installed system base

This slice is the installed system base: da Vinci generations, including da Vinci 5, Xi, refurbished Xi, and single-port, plus placements, utilization, features, clearances, and international go-to-market. Procedure totals and gross margin are owned outside this slice.

Foreign identities are referenced from installed-base rows and are partial here. Their complete populations are the datasets below, which this slice does not author.

| Identity | Column | Node |
| --- | --- | --- |
| `accounting_period_identity` | `accounting_period_id` | `sf:intuitive.calendar.dim_accounting_period` |
| `calendar_day_identity` | `expected_calendar_day_id` | `sf:intuitive.calendar.dim_calendar_day` |
| `competitor_identity` | `competitor_id` | `sf:intuitive.market.dim_competitor` |
| `country_identity` | `country_id` | `sf:intuitive.customer.dim_country` |
| `currency_identity` | `currency_id` | `sf:intuitive.finance.dim_currency` |
| `hospital_identity` | `hospital_id` | `sf:intuitive.customer.dim_hospital` |
| `hospital_site_identity` | `hospital_site_id` | `sf:intuitive.customer.dim_hospital_site` |
| `manufacturing_facility_identity` | `manufacturing_facility_id` | `sf:intuitive.finance.dim_manufacturing_facility` |
| `procedure_category_identity` | `procedure_category_id` | `sf:intuitive.procedure.dim_procedure_category` |
| `site_of_care_identity` | `site_of_care_id` | `sf:intuitive.customer.dim_site_of_care` |

## Numbered questions

### Q1 2026 (1) — Digital roadmap, augmented dexterity, and biopsy

The roadmap says whether each capability changes the system path or the procedure mix versus the current generation.

`intuitive.system.fact_digital_roadmap`: `roadmap_status_code`, `changes_procedure_mix_flag`, `changes_system_path_flag`, `system_feature_id`, `system_generation_id`, `procedure_category_id`.
`intuitive.procedure.fact_procedure_volume`: `procedure_count`, `procedure_category_id`.

### Q1 2026 (4) — After-hours use, da Vinci 5 utilization, and placements

Remaining after-hours capacity and utilization headroom are the bridge to additional placements.

`intuitive.system.fact_after_hours`: `after_hours_hour_count`, `remaining_after_hours_rate`, `procedure_count`, `system_generation_id`.
`intuitive.system.fact_utilization`: `utilization_rate`, `headroom_rate`, `placement_demand_count`, `system_generation_id`.
`intuitive.system.fact_system_placement`: `placement_count`, `system_generation_id`, `accounting_period_id`.

### Q1 2026 (5) — Refurbished Xi and tiered pricing by geography

Price tiers for refurbished and new systems are stored by country against the rival entry.

`intuitive.commercial.fact_price_architecture`: `price_amount`, `tier_code`, `competitive_response_flag`, `country_id`, `system_generation_id`, `competitor_id`.
`intuitive.commercial.fact_refurbished_offer`: `placement_count`, `tier_code`, `country_id`, `system_generation_id`.

### Q1 2026 (7) — Clearances and instruments before single-port adoption

Clearances and instruments that adoption still waits on are flagged on the single-port generation.

`intuitive.system.fact_clearance_milestone`: `required_before_adoption_flag`, `granted_flag`, `adoption_effect_code`, `system_generation_id`, `procedure_category_id`.
`intuitive.system.fact_instrument_requirement`: `instrument_name`, `available_flag`, `required_before_adoption_flag`, `system_generation_id`.

### Q1 2026 (8) — Distributors, refurbished systems, and the China joint venture

Each international action is stored with procedure and placement growth so the moves can be read together.

`intuitive.commercial.fact_go_to_market`: `action_code`, `procedure_growth_rate`, `placement_growth_rate`, `distributor_id`, `joint_venture_id`, `system_generation_id`, `country_id`.

### Q4 2025 (1) — Advanced imaging on existing hardware or new hardware

The feature hardware row says whether imaging uses the installed robot or needs new hardware.

`intuitive.system.fact_feature_hardware`: `hardware_requirement_code`, `installed_base_compatible_flag`, `system_feature_id`, `system_generation_id`.

### Q4 2025 (4) — Digital subscription and da Vinci 5 adoption

Subscription attach and the adoption lift sit next to subscription revenue.

`intuitive.system.fact_subscription_attach`: `attach_rate`, `adoption_lift_rate`, `subscription_revenue_amount`, `system_generation_id`, `system_feature_id`.
`intuitive.finance.fact_innovation_revenue`: `innovation_revenue_amount`, `system_generation_id`.

### Q4 2025 (6) — Lower-acuity cases: lower price or refurbished systems

The offer code says which system is used to compete for the lower-acuity case.

`intuitive.commercial.fact_lower_acuity_offer`: `offer_code`, `procedure_economics_fit_flag`, `procedure_category_id`, `system_generation_id`.

### Q3 2025 (2) — Refurbished Xi moving to new sites of care

Refurbished placements from upgrades record the site of care that receives the older system.

`intuitive.commercial.fact_refurbished_offer`: `placement_count`, `upgrade_source_flag`, `site_of_care_id`, `system_generation_id`.
`intuitive.system.fact_system_placement`: `upgrade_flag`, `new_site_flag`, `site_of_care_id`.

### Q3 2025 (3) — Utilization on a retained Xi after a da Vinci 5 purchase

The redeployed system stores utilization and whether a new procedure category shows up.

`intuitive.system.fact_redeployed_system`: `utilization_rate`, `new_category_flag`, `procedure_count`, `procedure_category_id`, `system_generation_id`, `installed_system_id`.
`intuitive.system.dim_installed_system`: `retained_after_upgrade_flag`, `system_generation_id`.

### Q3 2025 (5) — U.S. utilization as da Vinci 5 becomes a larger share of the base

Utilization is stored with the generation's share of the installed base.

`intuitive.system.fact_generation_mix`: `installed_share_rate`, `utilization_rate`, `installed_count`, `system_generation_id`, `country_id`.
`intuitive.system.fact_utilization`: `utilization_rate`, `generation_mix_rate`, `country_id`, `system_generation_id`.

### Q3 2025 (9) — Hub and cloud-account contribution to da Vinci use

Feature adoption and utilization show what the hub and cloud accounts add.

`intuitive.system.fact_feature_adoption`: `adoption_rate`, `utilization_rate`, `system_feature_id`, `system_generation_id`.

### Q3 2025 (11) — Procedure categories that benefit from force feedback

Adoption of force feedback is ranked by procedure category.

`intuitive.system.fact_feature_adoption`: `benefit_rank`, `adoption_rate`, `procedure_category_id`, `system_feature_id`, `system_generation_id`.

### Q2 2025 (2) — In-house instrument reprocessing and useful life

The reprocessing row says whether the work can be done in-house and how useful life changes.

`intuitive.commercial.fact_reprocessing`: `in_house_flag`, `third_party_flag`, `useful_life_days`, `useful_life_change_days`.

### Q2 2025 (3) — Capital-spending risk in placement conversations

Budget risk and the change in planned placements are what the hospital conversations record.

`intuitive.commercial.fact_capital_conversation`: `budget_risk_code`, `placement_plan_count`, `placement_plan_change_count`, `hospital_id`, `system_generation_id`.

### Q2 2025 (4) — Force-feedback capacity and instruments per procedure

Evaluation stage and capacity sit beside the change in instruments and accessories per procedure.

`intuitive.system.fact_force_feedback`: `evaluation_status_code`, `capacity_available_flag`, `instruments_per_procedure`, `instruments_per_procedure_change`, `manufacturing_facility_id`.

### Q2 2025 (5) — Placements outside the United States after Europe and Japan approvals

Placement counts after a clearance are stored by country, including Europe and Japan.

`intuitive.commercial.fact_international_placement`: `placement_count`, `post_clearance_flag`, `cadence_code`, `country_id`, `regulatory_clearance_id`, `system_generation_id`.
`intuitive.system.fact_clearance_milestone`: `granted_flag`, `country_id`, `system_generation_id`.

### Q2 2025 (6) — da Vinci 5 features at the broader launch

Features are flagged as broad-launch or still limited, with the adoption rate that follows.

`intuitive.system.fact_feature_adoption`: `broad_launch_flag`, `limited_release_flag`, `adoption_rate`, `system_feature_id`, `system_generation_id`.

## Datasets

| Qualified name | Questions served |
| --- | --- |
| `intuitive.system.dim_system_generation` | — |
| `intuitive.system.dim_installed_system` | Q3 2025 (3) |
| `intuitive.system.dim_system_feature` | — |
| `intuitive.system.fact_system_placement` | Q1 2026 (4), Q3 2025 (2) |
| `intuitive.system.fact_utilization` | Q1 2026 (4), Q3 2025 (5) |
| `intuitive.system.fact_after_hours` | Q1 2026 (4) |
| `intuitive.system.fact_redeployed_system` | Q3 2025 (3) |
| `intuitive.system.fact_generation_mix` | Q3 2025 (5) |
| `intuitive.system.fact_feature_hardware` | Q4 2025 (1) |
| `intuitive.system.fact_feature_adoption` | Q3 2025 (9), Q3 2025 (11), Q2 2025 (6) |
| `intuitive.system.fact_subscription_attach` | Q4 2025 (4) |
| `intuitive.system.fact_digital_roadmap` | Q1 2026 (1) |
| `intuitive.system.fact_force_feedback` | Q2 2025 (4) |
| `intuitive.system.dim_regulatory_clearance` | — |
| `intuitive.system.fact_clearance_milestone` | Q1 2026 (7), Q2 2025 (5) |
| `intuitive.system.fact_instrument_requirement` | Q1 2026 (7) |
| `intuitive.commercial.dim_distributor` | — |
| `intuitive.commercial.dim_joint_venture` | — |
| `intuitive.commercial.fact_go_to_market` | Q1 2026 (8) |
| `intuitive.commercial.fact_refurbished_offer` | Q1 2026 (5), Q3 2025 (2) |
| `intuitive.commercial.fact_price_architecture` | Q1 2026 (5) |
| `intuitive.commercial.fact_international_placement` | Q2 2025 (5) |
| `intuitive.commercial.fact_capital_conversation` | Q2 2025 (3) |
| `intuitive.commercial.fact_reprocessing` | Q2 2025 (2) |
| `intuitive.commercial.fact_lower_acuity_offer` | Q4 2025 (6) |
