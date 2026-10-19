# Northline Mobile

## Introduction

Northline Mobile operates a national mobile network. The catalog `telecom-mobile` is the ontology of usage mediation, online charging, roaming interchange, and retail billing: datasets in the Snowflake database `TELECOM_MOBILE`.

A subscription belongs to a subscriber and a billing account. Packet, voice, message, and content usage land as separate CDR facts. Online charging events, reservations, and debits are finer than a closed CDR. TAP-out and TAP-in hold roaming interchange. Cell counters are one row per cell per 15-minute interval. The questions below use the authored identities and joins. Synthetic row counts and fan-out for a 30-day window are listed with the major fact tables.

The business narrative and the full relationship table are in `business-model.md`. Loadable YAML is in `yaml/`.

## BI questions

1. Which subscription, subscriber, cell, and rate plan produced each data CDR, and how much volume did it carry?
   `telecom-mobile.usage.fact_data_cdr` joins `dim_subscription`, `dim_subscriber`, `dim_cell`, `dim_rate_plan`, and `dim_calendar_day`. `uplink_bytes` and `downlink_bytes` are measures of that CDR row.

2. Which voice CDRs were roaming, and which roaming partner and visited PLMN applied?
   `fact_voice_cdr.roaming_partner_id` is optional. When it is present it joins `dim_roaming_partner`. `visited_plmn_id` joins `dim_plmn`. Home usage leaves the roaming partner empty.

3. How many online charging events, reservations, and debits did a subscription generate?
   `telecom-mobile.charging.fact_charging_event` joins `dim_subscription`. `fact_balance_reservation` joins one charging event, one-to-one, and not every charging event has a reservation. `fact_balance_debit` joins one reservation the same way.

4. What rated charge was produced from a mediated CDR, and which invoice line billed it?
   `fact_rated_charge` may join `fact_data_cdr`, `fact_voice_cdr`, `fact_sms_cdr`, or `fact_content_cdr` one-to-one. `fact_invoice_line.rated_charge_id` may join that rated charge. Every invoice line joins `fact_invoice`.

5. Which cell sites sit in a market, and which cells belong to each site?
   `dim_cell_site.market_id` joins `dim_market` as `1:many` with a required match both ways. `dim_cell.cell_site_id` joins `dim_cell_site` the same way.

6. Who manages each market?
   `dim_market.market_manager_employee_id` joins `dim_employee` one-to-one. Every market has one manager. An employee manages at most one market.

7. What is on a billing account's invoice for the window?
   `fact_invoice` joins `dim_billing_account` one-to-one in both directions: every account has one invoice, and every invoice has one account. `fact_invoice_line` is `1:many` from that invoice with a required match both ways. `fact_document` joins the invoice one-to-one as the bill document.

8. Which TAP-out records were raised for roaming usage?
   `telecom-mobile.roaming.fact_tap_out` joins `dim_roaming_partner` with a required match both ways, and may join the voice CDR or the data CDR that was outcollected.

9. What allowance did a subscription draw, and which rated charge caused the draw?
   `fact_allowance_draw` joins `dim_subscription` and `dim_allowance_bucket`. The rated charge is optional.

10. Which mediation file did a network element emit each day, and which data CDRs were rejected?
    `fact_mediation_file` joins `dim_network_element` and `dim_calendar_day` as `1:many` with a required match both ways. `fact_mediation_reject` may join a data, voice, or SMS CDR.

11. How did a subscriber move between cells?
    `fact_handover.source_cell_id` joins `dim_cell`. The cell entered is `fact_handover_target.target_cell_id`, and that target row joins the handover one-to-one. Source and target stay on different datasets so each join to `dim_cell` is a single column.

12. Which dealer sold a subscription, and which add-ons are attached to it?
    `fact_dealer_sale` joins `dim_dealer` with a required match both ways, and joins `dim_subscription`. `bridge_subscription_addon` joins `dim_subscription` and `dim_addon`.

## Major fact tables

High-volume landing zones for the 30-day synthetic window. The sum of all fact rows in the catalog, including smaller operational facts, is 26,507,579,080.

| Fact | Grain class | Rows | Why this is a landing zone |
| --- | --- | ---: | --- |
| `charging.fact_charging_event` | transaction | 6,300,000,000 | Authored at three events per mediated CDR. The mediated total is the published 2.1 billion CDRs per month, so the event fact is 6.3 billion rows. |
| `charging.fact_balance_reservation` | transaction | 4,200,000,000 | Authored as two reservations for every three charging events. Some charging events do not reserve. |
| `charging.fact_balance_debit` | transaction | 3,150,000,000 | Authored as three debits for every four reservations. Unused reservations expire without a debit. |
| `usage.fact_attach` | transaction | 2,400,000,000 | Synthetic mobility volume for a 25 million subscription national network over 30 days. |
| `charging.fact_rated_charge` | transaction | 2,100,000,000 | Equal to the 2.1 billion mediated CDRs. Optional one-to-one links partition that population across data, voice, SMS, and content CDRs. |
| `charging.fact_policy_event` | transaction | 1,800,000,000 | Synthetic session-control volume, below the charging-event grain and above closed CDRs. |
| `usage.fact_data_cdr` | transaction | 1,400,000,000 | 1.4 billion of the published 2.1 billion monthly CDRs. Partial records are why data outnumbers voice. |
| `usage.fact_handover` | transaction | 960,000,000 | Synthetic radio-mobility volume for the 85,000-cell footprint. |
| `charging.fact_allowance_draw` | transaction | 900,000,000 | Synthetic draw volume for subscriptions that hold an allowance bucket. |
| `usage.fact_location_update` | transaction | 600,000,000 | Synthetic mobility signaling volume, lower than handover volume. |
| `usage.fact_voice_cdr` | transaction | 520,000,000 | 520 million of the published 2.1 billion monthly CDRs. |
| `usage.fact_qos_change` | transaction | 300,000,000 | Synthetic bearer-modification volume. |
| `network.fact_cell_counter` | periodic_snapshot | 244,800,000 | 85,000 cells times 96 intervals times 30 days = 244,800,000 rows. This is a periodic snapshot, not a CDR. |
| `usage.fact_sms_cdr` | transaction | 150,000,000 | 150 million of the published 2.1 billion monthly CDRs. |
| `billing.fact_invoice_line` | transaction | 128,000,000 | 16 million invoices times an authored average of 8 lines. |
| `roaming.fact_tap_out` | transaction | 126,000,000 | Authored as 6 percent of mediated CDRs (126 million), the outcollect slice of the 2.1 billion. |

## Synthetic join statistics

Synthetic closed-form population for the stated window. Dimension and fact row counts are authored from the cited industry anchors and from structural fan-out (every parent required by an always-match rule has at least one child). Distinct parent keys, unmatched parents, null foreign keys, and average children per matched parent are derived from multiplicity. Optional-child match rates default to 0.93 when a join does not set one. Optional-parent coverage defaults to the full parent population when matched children can reach it, and otherwise to one child per observed parent. A stated coverage or matched-row count overrides that default. This is not a sampled extract.

Outbound means a foreign key on the fact. Inbound means another dataset carries that fact's identity. The full population and every join are in `statistics.md` and `statistics.json`.

### `fact_charging_event`

Online charging events are the finest usage landing zone. 3GPP treats a charging event as one chargeable-event report toward the charging function, which is finer than a closed CDR.

Rows: `6,300,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `apn_id` | `dim_apn` | 6,300,000,000 | 6,300,000,000 | 0 | 80 | 0 | 78,750,000.00 |
| `balance_type_id` | `dim_balance_type` | 6,300,000,000 | 6,300,000,000 | 0 | 10 | 0 | 630,000,000.00 |
| `calendar_day_id` | `dim_calendar_day` | 6,300,000,000 | 6,300,000,000 | 0 | 30 | 0 | 210,000,000.00 |
| `network_element_id` | `dim_network_element` | 6,300,000,000 | 6,300,000,000 | 0 | 12,000 | 0 | 525,000.00 |
| `plmn_id` | `dim_plmn` | 6,300,000,000 | 6,300,000,000 | 0 | 180 | 720 | 35,000,000.00 |
| `qos_id` | `dim_qos` | 6,300,000,000 | 6,300,000,000 | 0 | 30 | 0 | 210,000,000.00 |
| `rate_plan_id` | `dim_rate_plan` | 6,300,000,000 | 6,300,000,000 | 0 | 420 | 0 | 15,000,000.00 |
| `rating_group_id` | `dim_rating_group` | 6,300,000,000 | 6,300,000,000 | 0 | 200 | 0 | 31,500,000.00 |
| `record_type_id` | `dim_record_type` | 6,300,000,000 | 6,300,000,000 | 0 | 24 | 0 | 262,500,000.00 |
| `subscriber_id` | `dim_subscriber` | 6,300,000,000 | 6,300,000,000 | 0 | 19,400,000 | 600,000 | 324.74 |
| `subscription_id` | `dim_subscription` | 6,300,000,000 | 6,300,000,000 | 0 | 24,250,000 | 750,000 | 259.79 |

Inbound:

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_balance_reservation` | `charging_event_id` | 4,200,000,000 | 4,200,000,000 | 0 | 4,200,000,000 | 2,100,000,000 | 1.00 |

### `fact_balance_reservation`

Quota reservations are the online-charging landing zone for held balance.

Rows: `4,200,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `balance_type_id` | `dim_balance_type` | 4,200,000,000 | 4,200,000,000 | 0 | 10 | 0 | 420,000,000.00 |
| `calendar_day_id` | `dim_calendar_day` | 4,200,000,000 | 4,200,000,000 | 0 | 30 | 0 | 140,000,000.00 |
| `charging_event_id` | `fact_charging_event` | 4,200,000,000 | 4,200,000,000 | 0 | 4,200,000,000 | 2,100,000,000 | 1.00 |
| `subscription_id` | `dim_subscription` | 4,200,000,000 | 4,200,000,000 | 0 | 23,750,000 | 1,250,000 | 176.84 |

Inbound:

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_balance_debit` | `balance_reservation_id` | 3,150,000,000 | 3,150,000,000 | 0 | 3,150,000,000 | 1,050,000,000 | 1.00 |

### `fact_balance_debit`

Balance debits are the landing zone for committed online-charging usage.

Rows: `3,150,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `balance_reservation_id` | `fact_balance_reservation` | 3,150,000,000 | 3,150,000,000 | 0 | 3,150,000,000 | 1,050,000,000 | 1.00 |
| `balance_type_id` | `dim_balance_type` | 3,150,000,000 | 3,150,000,000 | 0 | 10 | 0 | 315,000,000.00 |
| `calendar_day_id` | `dim_calendar_day` | 3,150,000,000 | 3,150,000,000 | 0 | 30 | 0 | 105,000,000.00 |
| `subscription_id` | `dim_subscription` | 3,150,000,000 | 3,150,000,000 | 0 | 23,250,000 | 1,750,000 | 135.48 |

Inbound:

None in this catalog.

### `fact_attach`

Network attach and registration events land here, separate from billable CDRs.

Rows: `2,400,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 2,400,000,000 | 2,400,000,000 | 0 | 30 | 0 | 80,000,000.00 |
| `cell_id` | `dim_cell` | 2,400,000,000 | 2,400,000,000 | 0 | 84,150 | 850 | 28,520.50 |
| `imsi_id` | `dim_imsi` | 2,400,000,000 | 2,400,000,000 | 0 | 24,700,000 | 1,300,000 | 97.17 |
| `msisdn_id` | `dim_msisdn` | 2,400,000,000 | 2,400,000,000 | 0 | 25,650,000 | 1,350,000 | 93.57 |
| `network_element_id` | `dim_network_element` | 2,400,000,000 | 2,400,000,000 | 0 | 12,000 | 0 | 200,000.00 |
| `plmn_id` | `dim_plmn` | 2,400,000,000 | 2,400,000,000 | 0 | 135 | 765 | 17,777,777.78 |
| `subscriber_id` | `dim_subscriber` | 2,400,000,000 | 2,400,000,000 | 0 | 19,600,000 | 400,000 | 122.45 |
| `technology_id` | `dim_technology` | 2,400,000,000 | 2,400,000,000 | 0 | 6 | 0 | 400,000,000.00 |

Inbound:

None in this catalog.

### `fact_rated_charge`

Rating output lands here, one charge per mediated CDR, before invoice assembly.

Rows: `2,100,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 2,100,000,000 | 2,100,000,000 | 0 | 30 | 0 | 70,000,000.00 |
| `charge_type_id` | `dim_charge_type` | 2,100,000,000 | 2,100,000,000 | 0 | 16 | 0 | 131,250,000.00 |
| `content_cdr_id` | `fact_content_cdr` | 2,100,000,000 | 30,000,000 | 2,070,000,000 | 30,000,000 | 0 | 1.00 |
| `currency_id` | `dim_currency` | 2,100,000,000 | 2,100,000,000 | 0 | 12 | 0 | 175,000,000.00 |
| `data_cdr_id` | `fact_data_cdr` | 2,100,000,000 | 1,400,000,000 | 700,000,000 | 1,400,000,000 | 0 | 1.00 |
| `gl_account_id` | `dim_gl_account` | 2,100,000,000 | 2,100,000,000 | 0 | 800 | 0 | 2,625,000.00 |
| `rate_plan_id` | `dim_rate_plan` | 2,100,000,000 | 2,100,000,000 | 0 | 420 | 0 | 5,000,000.00 |
| `sms_cdr_id` | `fact_sms_cdr` | 2,100,000,000 | 150,000,000 | 1,950,000,000 | 150,000,000 | 0 | 1.00 |
| `subscription_id` | `dim_subscription` | 2,100,000,000 | 2,100,000,000 | 0 | 24,000,000 | 1,000,000 | 87.50 |
| `tariff_id` | `dim_tariff` | 2,100,000,000 | 2,037,000,000 | 63,000,000 | 1,100 | 0 | 1,851,818.18 |
| `tax_code_id` | `dim_tax_code` | 2,100,000,000 | 1,890,000,000 | 210,000,000 | 40 | 0 | 47,250,000.00 |
| `voice_cdr_id` | `fact_voice_cdr` | 2,100,000,000 | 520,000,000 | 1,580,000,000 | 520,000,000 | 0 | 1.00 |

Inbound:

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_allowance_draw` | `rated_charge_id` | 900,000,000 | 720,000,000 | 180,000,000 | 720,000,000 | 1,380,000,000 | 1.00 |
| `fact_invoice_line` | `rated_charge_id` | 128,000,000 | 89,600,000 | 38,400,000 | 89,600,000 | 2,010,400,000 | 1.00 |
| `fact_rerate` | `rated_charge_id` | 21,000,000 | 21,000,000 | 0 | 21,000,000 | 2,079,000,000 | 1.00 |

### `fact_policy_event`

Policy-control decisions land here for session authorization and QoS.

Rows: `1,800,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 1,800,000,000 | 1,800,000,000 | 0 | 30 | 0 | 60,000,000.00 |
| `cell_id` | `dim_cell` | 1,800,000,000 | 1,440,000,000 | 360,000,000 | 76,500 | 8,500 | 18,823.53 |
| `network_element_id` | `dim_network_element` | 1,800,000,000 | 1,800,000,000 | 0 | 12,000 | 0 | 150,000.00 |
| `policy_rule_id` | `dim_policy_rule` | 1,800,000,000 | 1,800,000,000 | 0 | 60 | 0 | 30,000,000.00 |
| `qos_id` | `dim_qos` | 1,800,000,000 | 1,800,000,000 | 0 | 30 | 0 | 60,000,000.00 |
| `slice_id` | `dim_slice` | 1,800,000,000 | 720,000,000 | 1,080,000,000 | 12 | 0 | 60,000,000.00 |
| `subscription_id` | `dim_subscription` | 1,800,000,000 | 1,800,000,000 | 0 | 22,500,000 | 2,500,000 | 80.00 |

Inbound:

None in this catalog.

### `fact_data_cdr`

Packet-data CDRs, including partial PGW and SMF records, are the largest mediated-CDR landing zone.

Rows: `1,400,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `apn_id` | `dim_apn` | 1,400,000,000 | 1,400,000,000 | 0 | 80 | 0 | 17,500,000.00 |
| `calendar_day_id` | `dim_calendar_day` | 1,400,000,000 | 1,400,000,000 | 0 | 30 | 0 | 46,666,666.67 |
| `cell_id` | `dim_cell` | 1,400,000,000 | 1,400,000,000 | 0 | 84,150 | 850 | 16,636.96 |
| `cell_site_id` | `dim_cell_site` | 1,400,000,000 | 1,400,000,000 | 0 | 27,720 | 280 | 50,505.05 |
| `imsi_id` | `dim_imsi` | 1,400,000,000 | 1,400,000,000 | 0 | 23,400,000 | 2,600,000 | 59.83 |
| `mediation_file_id` | `fact_mediation_file` | 1,400,000,000 | 1,400,000,000 | 0 | 360,000 | 0 | 3,888.89 |
| `msisdn_id` | `dim_msisdn` | 1,400,000,000 | 1,400,000,000 | 0 | 24,300,000 | 2,700,000 | 57.61 |
| `network_element_id` | `dim_network_element` | 1,400,000,000 | 1,400,000,000 | 0 | 12,000 | 0 | 116,666.67 |
| `plmn_id` | `dim_plmn` | 1,400,000,000 | 1,400,000,000 | 0 | 180 | 720 | 7,777,777.78 |
| `qos_id` | `dim_qos` | 1,400,000,000 | 1,400,000,000 | 0 | 30 | 0 | 46,666,666.67 |
| `rate_plan_id` | `dim_rate_plan` | 1,400,000,000 | 1,400,000,000 | 0 | 420 | 0 | 3,333,333.33 |
| `rating_group_id` | `dim_rating_group` | 1,400,000,000 | 1,400,000,000 | 0 | 200 | 0 | 7,000,000.00 |
| `record_type_id` | `dim_record_type` | 1,400,000,000 | 1,400,000,000 | 0 | 24 | 0 | 58,333,333.33 |
| `recording_entity_id` | `dim_recording_entity` | 1,400,000,000 | 1,400,000,000 | 0 | 400 | 0 | 3,500,000.00 |
| `release_cause_id` | `dim_release_cause` | 1,400,000,000 | 1,120,000,000 | 280,000,000 | 126 | 54 | 8,888,888.89 |
| `roaming_partner_id` | `dim_roaming_partner` | 1,400,000,000 | 168,000,000 | 1,232,000,000 | 256 | 384 | 656,250.00 |
| `slice_id` | `dim_slice` | 1,400,000,000 | 490,000,000 | 910,000,000 | 12 | 0 | 40,833,333.33 |
| `subscriber_id` | `dim_subscriber` | 1,400,000,000 | 1,400,000,000 | 0 | 18,800,000 | 1,200,000 | 74.47 |
| `subscription_id` | `dim_subscription` | 1,400,000,000 | 1,400,000,000 | 0 | 23,500,000 | 1,500,000 | 59.57 |
| `technology_id` | `dim_technology` | 1,400,000,000 | 1,400,000,000 | 0 | 6 | 0 | 233,333,333.33 |

Inbound:

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_rated_charge` | `data_cdr_id` | 2,100,000,000 | 1,400,000,000 | 700,000,000 | 1,400,000,000 | 0 | 1.00 |
| `fact_tap_out` | `data_cdr_id` | 126,000,000 | 90,000,000 | 36,000,000 | 90,000,000 | 1,310,000,000 | 1.00 |
| `fact_mediation_reject` | `data_cdr_id` | 8,400,000 | 5,600,000 | 2,800,000 | 5,600,000 | 1,394,400,000 | 1.00 |

### `fact_handover`

Mobility handovers land here, with separate source and target cell identities.

Rows: `960,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 960,000,000 | 960,000,000 | 0 | 30 | 0 | 32,000,000.00 |
| `handover_type_id` | `dim_handover_type` | 960,000,000 | 960,000,000 | 0 | 8 | 0 | 120,000,000.00 |
| `network_element_id` | `dim_network_element` | 960,000,000 | 960,000,000 | 0 | 12,000 | 0 | 80,000.00 |
| `source_cell_id` | `dim_cell` | 960,000,000 | 960,000,000 | 0 | 80,750 | 4,250 | 11,888.54 |
| `subscriber_id` | `dim_subscriber` | 960,000,000 | 960,000,000 | 0 | 16,000,000 | 4,000,000 | 60.00 |
| `technology_id` | `dim_technology` | 960,000,000 | 960,000,000 | 0 | 6 | 0 | 160,000,000.00 |

Inbound:

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_handover_target` | `handover_id` | 960,000,000 | 960,000,000 | 0 | 960,000,000 | 0 | 1.00 |

### `fact_allowance_draw`

Included-allowance consumption lands here, optionally tied to a rated charge.

Rows: `900,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `allowance_bucket_id` | `dim_allowance_bucket` | 900,000,000 | 900,000,000 | 0 | 40 | 0 | 22,500,000.00 |
| `calendar_day_id` | `dim_calendar_day` | 900,000,000 | 900,000,000 | 0 | 30 | 0 | 30,000,000.00 |
| `rated_charge_id` | `fact_rated_charge` | 900,000,000 | 720,000,000 | 180,000,000 | 720,000,000 | 1,380,000,000 | 1.00 |
| `subscription_id` | `dim_subscription` | 900,000,000 | 900,000,000 | 0 | 17,500,000 | 7,500,000 | 51.43 |

Inbound:

None in this catalog.

### `fact_location_update`

Location and tracking-area updates land here.

Rows: `600,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 600,000,000 | 600,000,000 | 0 | 30 | 0 | 20,000,000.00 |
| `cell_id` | `dim_cell` | 600,000,000 | 420,000,000 | 180,000,000 | 68,000 | 17,000 | 6,176.47 |
| `location_area_id` | `dim_location_area` | 600,000,000 | 600,000,000 | 0 | 3,200 | 0 | 187,500.00 |
| `subscriber_id` | `dim_subscriber` | 600,000,000 | 600,000,000 | 0 | 17,000,000 | 3,000,000 | 35.29 |
| `technology_id` | `dim_technology` | 600,000,000 | 600,000,000 | 0 | 6 | 0 | 100,000,000.00 |

Inbound:

None in this catalog.

### `fact_voice_cdr`

Voice call detail records land here.

Rows: `520,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 520,000,000 | 520,000,000 | 0 | 30 | 0 | 17,333,333.33 |
| `call_type_id` | `dim_call_type` | 520,000,000 | 520,000,000 | 0 | 12 | 0 | 43,333,333.33 |
| `cell_id` | `dim_cell` | 520,000,000 | 520,000,000 | 0 | 76,500 | 8,500 | 6,797.39 |
| `destination_zone_id` | `dim_destination_zone` | 520,000,000 | 520,000,000 | 0 | 90 | 0 | 5,777,777.78 |
| `msisdn_id` | `dim_msisdn` | 520,000,000 | 520,000,000 | 0 | 16,740,000 | 10,260,000 | 31.06 |
| `network_element_id` | `dim_network_element` | 520,000,000 | 520,000,000 | 0 | 12,000 | 0 | 43,333.33 |
| `number_prefix_id` | `dim_number_prefix` | 520,000,000 | 468,000,000 | 52,000,000 | 2,500 | 2,500 | 187,200.00 |
| `plmn_id` | `dim_plmn` | 520,000,000 | 520,000,000 | 0 | 225 | 675 | 2,311,111.11 |
| `rate_plan_id` | `dim_rate_plan` | 520,000,000 | 520,000,000 | 0 | 420 | 0 | 1,238,095.24 |
| `record_type_id` | `dim_record_type` | 520,000,000 | 520,000,000 | 0 | 24 | 0 | 21,666,666.67 |
| `release_cause_id` | `dim_release_cause` | 520,000,000 | 520,000,000 | 0 | 108 | 72 | 4,814,814.81 |
| `roaming_partner_id` | `dim_roaming_partner` | 520,000,000 | 41,600,000 | 478,400,000 | 224 | 416 | 185,714.29 |
| `subscriber_id` | `dim_subscriber` | 520,000,000 | 520,000,000 | 0 | 12,400,000 | 7,600,000 | 41.94 |
| `subscription_id` | `dim_subscription` | 520,000,000 | 520,000,000 | 0 | 15,500,000 | 9,500,000 | 33.55 |
| `technology_id` | `dim_technology` | 520,000,000 | 520,000,000 | 0 | 6 | 0 | 86,666,666.67 |
| `time_band_id` | `dim_time_band` | 520,000,000 | 520,000,000 | 0 | 8 | 0 | 65,000,000.00 |

Inbound:

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_rated_charge` | `voice_cdr_id` | 2,100,000,000 | 520,000,000 | 1,580,000,000 | 520,000,000 | 0 | 1.00 |
| `fact_tap_out` | `voice_cdr_id` | 126,000,000 | 36,000,000 | 90,000,000 | 36,000,000 | 484,000,000 | 1.00 |
| `fact_mediation_reject` | `voice_cdr_id` | 8,400,000 | 2,000,000 | 6,400,000 | 2,000,000 | 518,000,000 | 1.00 |

### `fact_qos_change`

Mid-session QoS changes land here.

Rows: `300,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 300,000,000 | 300,000,000 | 0 | 30 | 0 | 10,000,000.00 |
| `cell_id` | `dim_cell` | 300,000,000 | 300,000,000 | 0 | 68,000 | 17,000 | 4,411.76 |
| `policy_rule_id` | `dim_policy_rule` | 300,000,000 | 180,000,000 | 120,000,000 | 60 | 0 | 3,000,000.00 |
| `qos_id` | `dim_qos` | 300,000,000 | 300,000,000 | 0 | 30 | 0 | 10,000,000.00 |
| `subscription_id` | `dim_subscription` | 300,000,000 | 300,000,000 | 0 | 12,500,000 | 12,500,000 | 24.00 |

Inbound:

None in this catalog.

### `fact_cell_counter`

Radio performance counters land here at 15-minute grain.

Rows: `244,800,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 244,800,000 | 244,800,000 | 0 | 30 | 0 | 8,160,000.00 |
| `cell_id` | `dim_cell` | 244,800,000 | 244,800,000 | 0 | 85,000 | 0 | 2,880.00 |
| `cell_site_id` | `dim_cell_site` | 244,800,000 | 244,800,000 | 0 | 28,000 | 0 | 8,742.86 |
| `technology_id` | `dim_technology` | 244,800,000 | 244,800,000 | 0 | 6 | 0 | 40,800,000.00 |

Inbound:

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_counter_breach` | `cell_counter_id` | 500,000 | 500,000 | 0 | 489,600 | 244,310,400 | 1.02 |

### `fact_sms_cdr`

Short-message CDRs land here.

Rows: `150,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 150,000,000 | 150,000,000 | 0 | 30 | 0 | 5,000,000.00 |
| `call_type_id` | `dim_call_type` | 150,000,000 | 150,000,000 | 0 | 12 | 0 | 12,500,000.00 |
| `destination_zone_id` | `dim_destination_zone` | 150,000,000 | 150,000,000 | 0 | 90 | 0 | 1,666,666.67 |
| `msisdn_id` | `dim_msisdn` | 150,000,000 | 150,000,000 | 0 | 10,800,000 | 16,200,000 | 13.89 |
| `plmn_id` | `dim_plmn` | 150,000,000 | 150,000,000 | 0 | 135 | 765 | 1,111,111.11 |
| `rate_plan_id` | `dim_rate_plan` | 150,000,000 | 150,000,000 | 0 | 420 | 0 | 357,142.86 |
| `record_type_id` | `dim_record_type` | 150,000,000 | 150,000,000 | 0 | 24 | 0 | 6,250,000.00 |
| `subscriber_id` | `dim_subscriber` | 150,000,000 | 150,000,000 | 0 | 8,000,000 | 12,000,000 | 18.75 |
| `subscription_id` | `dim_subscription` | 150,000,000 | 150,000,000 | 0 | 10,000,000 | 15,000,000 | 15.00 |

Inbound:

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_rated_charge` | `sms_cdr_id` | 2,100,000,000 | 150,000,000 | 1,950,000,000 | 150,000,000 | 0 | 1.00 |
| `fact_mediation_reject` | `sms_cdr_id` | 8,400,000 | 800,000 | 7,600,000 | 800,000 | 149,200,000 | 1.00 |

### `fact_invoice_line`

Billable charge lines for the cycle land here, after rating.

Rows: `128,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 128,000,000 | 128,000,000 | 0 | 30 | 0 | 4,266,666.67 |
| `charge_type_id` | `dim_charge_type` | 128,000,000 | 128,000,000 | 0 | 16 | 0 | 8,000,000.00 |
| `currency_id` | `dim_currency` | 128,000,000 | 128,000,000 | 0 | 12 | 0 | 10,666,666.67 |
| `gl_account_id` | `dim_gl_account` | 128,000,000 | 128,000,000 | 0 | 800 | 0 | 160,000.00 |
| `invoice_id` | `fact_invoice` | 128,000,000 | 128,000,000 | 0 | 16,000,000 | 0 | 8.00 |
| `rated_charge_id` | `fact_rated_charge` | 128,000,000 | 89,600,000 | 38,400,000 | 89,600,000 | 2,010,400,000 | 1.00 |
| `tax_code_id` | `dim_tax_code` | 128,000,000 | 96,000,000 | 32,000,000 | 40 | 0 | 2,400,000.00 |

Inbound:

None in this catalog.

### `fact_tap_out`

Outbound roaming usage exchanged with partners lands here.

Rows: `126,000,000`.

Outbound:

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 126,000,000 | 126,000,000 | 0 | 30 | 0 | 4,200,000.00 |
| `currency_id` | `dim_currency` | 126,000,000 | 126,000,000 | 0 | 12 | 0 | 10,500,000.00 |
| `data_cdr_id` | `fact_data_cdr` | 126,000,000 | 90,000,000 | 36,000,000 | 90,000,000 | 1,310,000,000 | 1.00 |
| `plmn_id` | `dim_plmn` | 126,000,000 | 126,000,000 | 0 | 900 | 0 | 140,000.00 |
| `record_type_id` | `dim_record_type` | 126,000,000 | 126,000,000 | 0 | 24 | 0 | 5,250,000.00 |
| `roaming_partner_id` | `dim_roaming_partner` | 126,000,000 | 126,000,000 | 0 | 640 | 0 | 196,875.00 |
| `subscription_id` | `dim_subscription` | 126,000,000 | 126,000,000 | 0 | 5,000,000 | 20,000,000 | 25.20 |
| `voice_cdr_id` | `fact_voice_cdr` | 126,000,000 | 36,000,000 | 90,000,000 | 36,000,000 | 484,000,000 | 1.00 |

Inbound:

None in this catalog.
