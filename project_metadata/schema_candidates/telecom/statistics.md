# Northline Mobile synthetic statistics

Synthetic closed-form population for the stated window. Dimension and fact row counts are authored from the cited industry anchors and from structural fan-out (every parent required by an always-match rule has at least one child). Distinct parent keys, unmatched parents, null foreign keys, and average children per matched parent are derived from multiplicity. Optional-child match rates default to 0.93 when a join does not set one. Optional-parent coverage defaults to the full parent population when matched children can reach it, and otherwise to one child per observed parent. A stated coverage or matched-row count overrides that default. This is not a sampled extract.

Window: 30 days. Datasets: 173. Sum of fact-table rows in the window: 26,507,579,080.

## Major fact tables

These are the event and periodic-snapshot facts where high-volume data lands.

| Fact | Grain class | Rows in window | Basis |
| --- | --- | ---: | --- |
| `fact_charging_event` | transaction | 6,300,000,000 | Authored at three events per mediated CDR. The mediated total is the published 2.1 billion CDRs per month, so the event fact is 6.3 billion rows. |
| `fact_balance_reservation` | transaction | 4,200,000,000 | Authored as two reservations for every three charging events. Some charging events do not reserve. |
| `fact_balance_debit` | transaction | 3,150,000,000 | Authored as three debits for every four reservations. Unused reservations expire without a debit. |
| `fact_attach` | transaction | 2,400,000,000 | Synthetic mobility volume for a 25 million subscription national network over 30 days. |
| `fact_rated_charge` | transaction | 2,100,000,000 | Equal to the 2.1 billion mediated CDRs. Optional one-to-one links partition that population across data, voice, SMS, and content CDRs. |
| `fact_policy_event` | transaction | 1,800,000,000 | Synthetic session-control volume, below the charging-event grain and above closed CDRs. |
| `fact_data_cdr` | transaction | 1,400,000,000 | 1.4 billion of the published 2.1 billion monthly CDRs. Partial records are why data outnumbers voice. |
| `fact_handover` | transaction | 960,000,000 | Synthetic radio-mobility volume for the 85,000-cell footprint. |
| `fact_allowance_draw` | transaction | 900,000,000 | Synthetic draw volume for subscriptions that hold an allowance bucket. |
| `fact_location_update` | transaction | 600,000,000 | Synthetic mobility signaling volume, lower than handover volume. |
| `fact_voice_cdr` | transaction | 520,000,000 | 520 million of the published 2.1 billion monthly CDRs. |
| `fact_qos_change` | transaction | 300,000,000 | Synthetic bearer-modification volume. |
| `fact_cell_counter` | periodic_snapshot | 244,800,000 | 85,000 cells times 96 intervals times 30 days = 244,800,000 rows. This is a periodic snapshot, not a CDR. |
| `fact_sms_cdr` | transaction | 150,000,000 | 150 million of the published 2.1 billion monthly CDRs. |
| `fact_invoice_line` | transaction | 128,000,000 | 16 million invoices times an authored average of 8 lines. |
| `fact_tap_out` | transaction | 126,000,000 | Authored as 6 percent of mediated CDRs (126 million), the outcollect slice of the 2.1 billion. |

## Join statistics for major facts

### `fact_charging_event`

Online charging events are the finest usage landing zone. 3GPP treats a charging event as one chargeable-event report toward the charging function, which is finer than a closed CDR.

Population `6,300,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

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

#### Inbound

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_balance_reservation` | `charging_event_id` | 4,200,000,000 | 4,200,000,000 | 0 | 4,200,000,000 | 2,100,000,000 | 1.00 |

### `fact_balance_reservation`

Quota reservations are the online-charging landing zone for held balance.

Population `4,200,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `balance_type_id` | `dim_balance_type` | 4,200,000,000 | 4,200,000,000 | 0 | 10 | 0 | 420,000,000.00 |
| `calendar_day_id` | `dim_calendar_day` | 4,200,000,000 | 4,200,000,000 | 0 | 30 | 0 | 140,000,000.00 |
| `charging_event_id` | `fact_charging_event` | 4,200,000,000 | 4,200,000,000 | 0 | 4,200,000,000 | 2,100,000,000 | 1.00 |
| `subscription_id` | `dim_subscription` | 4,200,000,000 | 4,200,000,000 | 0 | 23,750,000 | 1,250,000 | 176.84 |

#### Inbound

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_balance_debit` | `balance_reservation_id` | 3,150,000,000 | 3,150,000,000 | 0 | 3,150,000,000 | 1,050,000,000 | 1.00 |

### `fact_balance_debit`

Balance debits are the landing zone for committed online-charging usage.

Population `3,150,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `balance_reservation_id` | `fact_balance_reservation` | 3,150,000,000 | 3,150,000,000 | 0 | 3,150,000,000 | 1,050,000,000 | 1.00 |
| `balance_type_id` | `dim_balance_type` | 3,150,000,000 | 3,150,000,000 | 0 | 10 | 0 | 315,000,000.00 |
| `calendar_day_id` | `dim_calendar_day` | 3,150,000,000 | 3,150,000,000 | 0 | 30 | 0 | 105,000,000.00 |
| `subscription_id` | `dim_subscription` | 3,150,000,000 | 3,150,000,000 | 0 | 23,250,000 | 1,750,000 | 135.48 |

#### Inbound

None in this catalog.

### `fact_attach`

Network attach and registration events land here, separate from billable CDRs.

Population `2,400,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

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

#### Inbound

None in this catalog.

### `fact_rated_charge`

Rating output lands here, one charge per mediated CDR, before invoice assembly.

Population `2,100,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

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

#### Inbound

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_allowance_draw` | `rated_charge_id` | 900,000,000 | 720,000,000 | 180,000,000 | 720,000,000 | 1,380,000,000 | 1.00 |
| `fact_invoice_line` | `rated_charge_id` | 128,000,000 | 89,600,000 | 38,400,000 | 89,600,000 | 2,010,400,000 | 1.00 |
| `fact_rerate` | `rated_charge_id` | 21,000,000 | 21,000,000 | 0 | 21,000,000 | 2,079,000,000 | 1.00 |

### `fact_policy_event`

Policy-control decisions land here for session authorization and QoS.

Population `1,800,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 1,800,000,000 | 1,800,000,000 | 0 | 30 | 0 | 60,000,000.00 |
| `cell_id` | `dim_cell` | 1,800,000,000 | 1,440,000,000 | 360,000,000 | 76,500 | 8,500 | 18,823.53 |
| `network_element_id` | `dim_network_element` | 1,800,000,000 | 1,800,000,000 | 0 | 12,000 | 0 | 150,000.00 |
| `policy_rule_id` | `dim_policy_rule` | 1,800,000,000 | 1,800,000,000 | 0 | 60 | 0 | 30,000,000.00 |
| `qos_id` | `dim_qos` | 1,800,000,000 | 1,800,000,000 | 0 | 30 | 0 | 60,000,000.00 |
| `slice_id` | `dim_slice` | 1,800,000,000 | 720,000,000 | 1,080,000,000 | 12 | 0 | 60,000,000.00 |
| `subscription_id` | `dim_subscription` | 1,800,000,000 | 1,800,000,000 | 0 | 22,500,000 | 2,500,000 | 80.00 |

#### Inbound

None in this catalog.

### `fact_data_cdr`

Packet-data CDRs, including partial PGW and SMF records, are the largest mediated-CDR landing zone.

Population `1,400,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

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

#### Inbound

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_rated_charge` | `data_cdr_id` | 2,100,000,000 | 1,400,000,000 | 700,000,000 | 1,400,000,000 | 0 | 1.00 |
| `fact_tap_out` | `data_cdr_id` | 126,000,000 | 90,000,000 | 36,000,000 | 90,000,000 | 1,310,000,000 | 1.00 |
| `fact_mediation_reject` | `data_cdr_id` | 8,400,000 | 5,600,000 | 2,800,000 | 5,600,000 | 1,394,400,000 | 1.00 |

### `fact_handover`

Mobility handovers land here, with separate source and target cell identities.

Population `960,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 960,000,000 | 960,000,000 | 0 | 30 | 0 | 32,000,000.00 |
| `handover_type_id` | `dim_handover_type` | 960,000,000 | 960,000,000 | 0 | 8 | 0 | 120,000,000.00 |
| `network_element_id` | `dim_network_element` | 960,000,000 | 960,000,000 | 0 | 12,000 | 0 | 80,000.00 |
| `source_cell_id` | `dim_cell` | 960,000,000 | 960,000,000 | 0 | 80,750 | 4,250 | 11,888.54 |
| `subscriber_id` | `dim_subscriber` | 960,000,000 | 960,000,000 | 0 | 16,000,000 | 4,000,000 | 60.00 |
| `technology_id` | `dim_technology` | 960,000,000 | 960,000,000 | 0 | 6 | 0 | 160,000,000.00 |

#### Inbound

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_handover_target` | `handover_id` | 960,000,000 | 960,000,000 | 0 | 960,000,000 | 0 | 1.00 |

### `fact_allowance_draw`

Included-allowance consumption lands here, optionally tied to a rated charge.

Population `900,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `allowance_bucket_id` | `dim_allowance_bucket` | 900,000,000 | 900,000,000 | 0 | 40 | 0 | 22,500,000.00 |
| `calendar_day_id` | `dim_calendar_day` | 900,000,000 | 900,000,000 | 0 | 30 | 0 | 30,000,000.00 |
| `rated_charge_id` | `fact_rated_charge` | 900,000,000 | 720,000,000 | 180,000,000 | 720,000,000 | 1,380,000,000 | 1.00 |
| `subscription_id` | `dim_subscription` | 900,000,000 | 900,000,000 | 0 | 17,500,000 | 7,500,000 | 51.43 |

#### Inbound

None in this catalog.

### `fact_location_update`

Location and tracking-area updates land here.

Population `600,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 600,000,000 | 600,000,000 | 0 | 30 | 0 | 20,000,000.00 |
| `cell_id` | `dim_cell` | 600,000,000 | 420,000,000 | 180,000,000 | 68,000 | 17,000 | 6,176.47 |
| `location_area_id` | `dim_location_area` | 600,000,000 | 600,000,000 | 0 | 3,200 | 0 | 187,500.00 |
| `subscriber_id` | `dim_subscriber` | 600,000,000 | 600,000,000 | 0 | 17,000,000 | 3,000,000 | 35.29 |
| `technology_id` | `dim_technology` | 600,000,000 | 600,000,000 | 0 | 6 | 0 | 100,000,000.00 |

#### Inbound

None in this catalog.

### `fact_voice_cdr`

Voice call detail records land here.

Population `520,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

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

#### Inbound

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_rated_charge` | `voice_cdr_id` | 2,100,000,000 | 520,000,000 | 1,580,000,000 | 520,000,000 | 0 | 1.00 |
| `fact_tap_out` | `voice_cdr_id` | 126,000,000 | 36,000,000 | 90,000,000 | 36,000,000 | 484,000,000 | 1.00 |
| `fact_mediation_reject` | `voice_cdr_id` | 8,400,000 | 2,000,000 | 6,400,000 | 2,000,000 | 518,000,000 | 1.00 |

### `fact_qos_change`

Mid-session QoS changes land here.

Population `300,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 300,000,000 | 300,000,000 | 0 | 30 | 0 | 10,000,000.00 |
| `cell_id` | `dim_cell` | 300,000,000 | 300,000,000 | 0 | 68,000 | 17,000 | 4,411.76 |
| `policy_rule_id` | `dim_policy_rule` | 300,000,000 | 180,000,000 | 120,000,000 | 60 | 0 | 3,000,000.00 |
| `qos_id` | `dim_qos` | 300,000,000 | 300,000,000 | 0 | 30 | 0 | 10,000,000.00 |
| `subscription_id` | `dim_subscription` | 300,000,000 | 300,000,000 | 0 | 12,500,000 | 12,500,000 | 24.00 |

#### Inbound

None in this catalog.

### `fact_cell_counter`

Radio performance counters land here at 15-minute grain.

Population `244,800,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 244,800,000 | 244,800,000 | 0 | 30 | 0 | 8,160,000.00 |
| `cell_id` | `dim_cell` | 244,800,000 | 244,800,000 | 0 | 85,000 | 0 | 2,880.00 |
| `cell_site_id` | `dim_cell_site` | 244,800,000 | 244,800,000 | 0 | 28,000 | 0 | 8,742.86 |
| `technology_id` | `dim_technology` | 244,800,000 | 244,800,000 | 0 | 6 | 0 | 40,800,000.00 |

#### Inbound

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_counter_breach` | `cell_counter_id` | 500,000 | 500,000 | 0 | 489,600 | 244,310,400 | 1.02 |

### `fact_sms_cdr`

Short-message CDRs land here.

Population `150,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

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

#### Inbound

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_rated_charge` | `sms_cdr_id` | 2,100,000,000 | 150,000,000 | 1,950,000,000 | 150,000,000 | 0 | 1.00 |
| `fact_mediation_reject` | `sms_cdr_id` | 8,400,000 | 800,000 | 7,600,000 | 800,000 | 149,200,000 | 1.00 |

### `fact_invoice_line`

Billable charge lines for the cycle land here, after rating.

Population `128,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 128,000,000 | 128,000,000 | 0 | 30 | 0 | 4,266,666.67 |
| `charge_type_id` | `dim_charge_type` | 128,000,000 | 128,000,000 | 0 | 16 | 0 | 8,000,000.00 |
| `currency_id` | `dim_currency` | 128,000,000 | 128,000,000 | 0 | 12 | 0 | 10,666,666.67 |
| `gl_account_id` | `dim_gl_account` | 128,000,000 | 128,000,000 | 0 | 800 | 0 | 160,000.00 |
| `invoice_id` | `fact_invoice` | 128,000,000 | 128,000,000 | 0 | 16,000,000 | 0 | 8.00 |
| `rated_charge_id` | `fact_rated_charge` | 128,000,000 | 89,600,000 | 38,400,000 | 89,600,000 | 2,010,400,000 | 1.00 |
| `tax_code_id` | `dim_tax_code` | 128,000,000 | 96,000,000 | 32,000,000 | 40 | 0 | 2,400,000.00 |

#### Inbound

None in this catalog.

### `fact_tap_out`

Outbound roaming usage exchanged with partners lands here.

Population `126,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

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

#### Inbound

None in this catalog.

## Dataset populations

| Dataset | Role | Volume class | Rows |
| --- | --- | --- | ---: |
| `fact_charging_event` | fact | transaction | 6,300,000,000 |
| `fact_balance_reservation` | fact | transaction | 4,200,000,000 |
| `fact_balance_debit` | fact | transaction | 3,150,000,000 |
| `fact_attach` | fact | transaction | 2,400,000,000 |
| `fact_rated_charge` | fact | transaction | 2,100,000,000 |
| `fact_policy_event` | fact | transaction | 1,800,000,000 |
| `fact_data_cdr` | fact | transaction | 1,400,000,000 |
| `fact_handover` | fact | transaction | 960,000,000 |
| `fact_handover_target` | fact | transaction | 960,000,000 |
| `fact_allowance_draw` | fact | transaction | 900,000,000 |
| `fact_location_update` | fact | transaction | 600,000,000 |
| `fact_voice_cdr` | fact | transaction | 520,000,000 |
| `fact_qos_change` | fact | transaction | 300,000,000 |
| `fact_cell_counter` | fact | periodic_snapshot | 244,800,000 |
| `fact_sms_cdr` | fact | transaction | 150,000,000 |
| `fact_invoice_line` | fact | transaction | 128,000,000 |
| `fact_tap_out` | fact | transaction | 126,000,000 |
| `fact_tap_in` | fact | transaction | 40,000,000 |
| `fact_tax_line` | fact | transaction | 32,000,000 |
| `dim_resource` | dimension | — | 30,000,000 |
| `fact_content_cdr` | fact | transaction | 30,000,000 |
| `dim_msisdn` | dimension | — | 27,000,000 |
| `dim_imsi` | dimension | — | 26,000,000 |
| `dim_service` | dimension | — | 25,000,000 |
| `dim_subscription` | dimension | — | 25,000,000 |
| `fact_bundle_snapshot` | fact | periodic_snapshot | 25,000,000 |
| `dim_sim` | dimension | — | 24,000,000 |
| `dim_device` | dimension | — | 23,000,000 |
| `dim_party` | dimension | — | 22,000,000 |
| `fact_rerate` | fact | transaction | 21,000,000 |
| `dim_contact` | dimension | — | 20,500,000 |
| `bridge_subscriber_party` | bridge | — | 20,000,000 |
| `dim_subscriber` | dimension | — | 20,000,000 |
| `fact_subscriber_snapshot` | fact | periodic_snapshot | 20,000,000 |
| `bridge_party_address` | bridge | — | 18,000,000 |
| `bridge_subscription_addon` | bridge | — | 18,000,000 |
| `dim_address` | dimension | — | 18,000,000 |
| `bridge_account_contact` | bridge | — | 16,000,000 |
| `dim_billing_account` | dimension | — | 16,000,000 |
| `fact_document` | fact | transaction | 16,000,000 |
| `fact_invoice` | fact | transaction | 16,000,000 |
| `fact_payment` | fact | transaction | 14,500,000 |
| `fact_interaction` | fact | transaction | 9,500,000 |
| `fact_mediation_reject` | fact | transaction | 8,400,000 |
| `fact_journal_line` | fact | transaction | 6,000,000 |
| `fact_topup` | fact | transaction | 6,000,000 |
| `fact_ticket_event` | fact | transaction | 4,800,000 |
| `fact_campaign_contact` | fact | transaction | 4,000,000 |
| `fact_adjustment` | fact | transaction | 3,200,000 |
| `fact_settlement_line` | fact | transaction | 2,400,000 |
| `fact_duplicate_suspect` | fact | transaction | 2,100,000 |
| `fact_dunning_event` | fact | transaction | 1,800,000 |
| `fact_network_alarm` | fact | transaction | 1,800,000 |
| `fact_trouble_ticket` | fact | transaction | 1,200,000 |
| `fact_counter_breach` | fact | transaction | 500,000 |
| `fact_dealer_sale` | fact | transaction | 420,000 |
| `fact_credit_note` | fact | transaction | 400,000 |
| `fact_mediation_file` | fact | transaction | 360,000 |
| `fact_fraud_alert` | fact | transaction | 350,000 |
| `bridge_cell_neighbor` | bridge | — | 340,000 |
| `bridge_neighbor_target` | bridge | — | 340,000 |
| `fact_promise_to_pay` | fact | transaction | 260,000 |
| `fact_sim_swap` | fact | transaction | 250,000 |
| `fact_refund` | fact | transaction | 220,000 |
| `bridge_cell_spectrum` | bridge | — | 200,000 |
| `fact_number_port` | fact | transaction | 180,000 |
| `dim_cell` | dimension | — | 85,000 |
| `fact_barring_event` | fact | transaction | 80,000 |
| `bridge_workgroup_employee` | bridge | — | 42,000 |
| `dim_employee` | dimension | — | 42,000 |
| `fact_collection_referral` | fact | transaction | 40,000 |
| `dim_cell_site` | dimension | — | 28,000 |
| `fact_sla_breach` | fact | transaction | 15,000 |
| `dim_network_element` | dimension | — | 12,000 |
| `bridge_device_capability` | bridge | — | 8,000 |
| `bridge_employee_queue` | bridge | — | 8,000 |
| `bridge_agent_skill` | bridge | — | 7,000 |
| `bridge_trunk_prefix` | bridge | — | 6,000 |
| `dim_agent` | dimension | — | 6,000 |
| `bridge_prefix_zone` | bridge | — | 5,000 |
| `dim_number_prefix` | dimension | — | 5,000 |
| `bridge_tariff_zone` | bridge | — | 4,000 |
| `fact_outage_ticket` | fact | transaction | 4,000 |
| `bridge_dealer_plan` | bridge | — | 3,600 |
| `dim_location_area` | dimension | — | 3,200 |
| `bridge_offering_price` | bridge | — | 2,400 |
| `dim_price` | dimension | — | 2,400 |
| `dim_interconnect_trunk` | dimension | — | 2,200 |
| `bridge_plan_rating_group` | bridge | — | 2,000 |
| `dim_device_model` | dimension | — | 1,800 |
| `bridge_roaming_zone` | bridge | — | 1,200 |
| `dim_dealer` | dimension | — | 1,200 |
| `dim_tariff` | dimension | — | 1,100 |
| `bridge_partner_plmn` | bridge | — | 900 |
| `dim_plmn` | dimension | — | 900 |
| `dim_gl_account` | dimension | — | 800 |
| `bridge_content_rating` | bridge | — | 700 |
| `dim_roaming_partner` | dimension | — | 640 |
| `dim_product_offering` | dimension | — | 500 |
| `dim_rate_plan` | dimension | — | 420 |
| `bridge_policy_apn` | bridge | — | 400 |
| `dim_recording_entity` | dimension | — | 400 |
| `dim_tac` | dimension | — | 400 |
| `dim_content_provider` | dimension | — | 350 |
| `dim_trouble_code` | dimension | — | 300 |
| `dim_addon` | dimension | — | 260 |
| `dim_cost_center` | dimension | — | 240 |
| `dim_country` | dimension | — | 240 |
| `dim_product_spec` | dimension | — | 220 |
| `dim_rating_group` | dimension | — | 200 |
| `bridge_campaign_plan` | bridge | — | 180 |
| `dim_discount` | dimension | — | 180 |
| `dim_release_cause` | dimension | — | 180 |
| `dim_mediation_rule` | dimension | — | 150 |
| `dim_workgroup` | dimension | — | 120 |
| `dim_destination_zone` | dimension | — | 90 |
| `dim_fraud_rule` | dimension | — | 90 |
| `dim_apn` | dimension | — | 80 |
| `dim_carrier` | dimension | — | 80 |
| `dim_department` | dimension | — | 80 |
| `fact_interconnect_invoice` | fact | transaction | 80 |
| `dim_campaign` | dimension | — | 60 |
| `dim_cost_element` | dimension | — | 60 |
| `dim_policy_rule` | dimension | — | 60 |
| `dim_tax_jurisdiction` | dimension | — | 60 |
| `dim_care_reason` | dimension | — | 50 |
| `bridge_market_channel` | bridge | — | 48 |
| `dim_adjustment_reason` | dimension | — | 40 |
| `dim_allowance_bucket` | dimension | — | 40 |
| `dim_np_operator` | dimension | — | 40 |
| `dim_queue` | dimension | — | 40 |
| `dim_tax_code` | dimension | — | 40 |
| `dim_vendor` | dimension | — | 40 |
| `bridge_slice_qos` | bridge | — | 36 |
| `dim_calendar_day` | dimension | — | 30 |
| `dim_qos` | dimension | — | 30 |
| `dim_script` | dimension | — | 30 |
| `dim_bank` | dimension | — | 25 |
| `dim_record_type` | dimension | — | 24 |
| `dim_language` | dimension | — | 20 |
| `dim_sla` | dimension | — | 20 |
| `dim_market` | dimension | — | 18 |
| `dim_cell_band` | dimension | — | 16 |
| `dim_charge_type` | dimension | — | 16 |
| `dim_barring` | dimension | — | 15 |
| `dim_call_type` | dimension | — | 12 |
| `dim_currency` | dimension | — | 12 |
| `dim_document_type` | dimension | — | 12 |
| `dim_segment` | dimension | — | 12 |
| `dim_slice` | dimension | — | 12 |
| `dim_balance_type` | dimension | — | 10 |
| `dim_core_function` | dimension | — | 10 |
| `dim_unit` | dimension | — | 10 |
| `dim_channel` | dimension | — | 8 |
| `dim_collection_agency` | dimension | — | 8 |
| `dim_credit_class` | dimension | — | 8 |
| `dim_handover_type` | dimension | — | 8 |
| `dim_journal_source` | dimension | — | 8 |
| `dim_payment_method` | dimension | — | 8 |
| `dim_subscription_status` | dimension | — | 8 |
| `dim_time_band` | dimension | — | 8 |
| `dim_account_status` | dimension | — | 6 |
| `dim_bill_cycle` | dimension | — | 6 |
| `dim_region` | dimension | — | 6 |
| `dim_sale_type` | dimension | — | 6 |
| `dim_technology` | dimension | — | 6 |
| `dim_alarm_severity` | dimension | — | 5 |
| `dim_dunning_level` | dimension | — | 5 |
| `dim_site_type` | dimension | — | 5 |
| `dim_file_format` | dimension | — | 4 |
| `dim_legal_entity` | dimension | — | 4 |
| `dim_accounting_period` | dimension | — | 1 |
| `dim_enterprise` | dimension | — | 1 |

## All joins

| Child | Column | Parent | Matched children | Null children | Distinct parent keys | Unmatched parents | Parent coverage | Avg children per matched parent |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `bridge_account_contact` | `billing_account_id` | `dim_billing_account` | 16,000,000 | 0 | 16,000,000 | 0 | 100.0% | 1.00 |
| `bridge_account_contact` | `contact_id` | `dim_contact` | 16,000,000 | 0 | 16,000,000 | 4,500,000 | 78.0% | 1.00 |
| `bridge_agent_skill` | `agent_id` | `dim_agent` | 7,000 | 0 | 6,000 | 0 | 100.0% | 1.17 |
| `bridge_agent_skill` | `trouble_code_id` | `dim_trouble_code` | 7,000 | 0 | 300 | 0 | 100.0% | 23.33 |
| `bridge_campaign_plan` | `campaign_id` | `dim_campaign` | 180 | 0 | 60 | 0 | 100.0% | 3.00 |
| `bridge_campaign_plan` | `rate_plan_id` | `dim_rate_plan` | 180 | 0 | 180 | 240 | 42.9% | 1.00 |
| `bridge_cell_neighbor` | `cell_id` | `dim_cell` | 340,000 | 0 | 85,000 | 0 | 100.0% | 4.00 |
| `bridge_cell_spectrum` | `cell_id` | `dim_cell` | 200,000 | 0 | 85,000 | 0 | 100.0% | 2.35 |
| `bridge_cell_spectrum` | `spectrum_band_id` | `dim_cell_band` | 200,000 | 0 | 16 | 0 | 100.0% | 12,500.00 |
| `bridge_content_rating` | `content_provider_id` | `dim_content_provider` | 700 | 0 | 350 | 0 | 100.0% | 2.00 |
| `bridge_content_rating` | `rating_group_id` | `dim_rating_group` | 700 | 0 | 200 | 0 | 100.0% | 3.50 |
| `bridge_dealer_plan` | `dealer_id` | `dim_dealer` | 3,600 | 0 | 1,200 | 0 | 100.0% | 3.00 |
| `bridge_dealer_plan` | `rate_plan_id` | `dim_rate_plan` | 3,600 | 0 | 420 | 0 | 100.0% | 8.57 |
| `bridge_device_capability` | `device_model_id` | `dim_device_model` | 8,000 | 0 | 1,800 | 0 | 100.0% | 4.44 |
| `bridge_device_capability` | `technology_id` | `dim_technology` | 8,000 | 0 | 6 | 0 | 100.0% | 1,333.33 |
| `bridge_employee_queue` | `employee_id` | `dim_employee` | 8,000 | 0 | 8,000 | 34,000 | 19.0% | 1.00 |
| `bridge_employee_queue` | `queue_id` | `dim_queue` | 8,000 | 0 | 40 | 0 | 100.0% | 200.00 |
| `bridge_market_channel` | `channel_id` | `dim_channel` | 48 | 0 | 8 | 0 | 100.0% | 6.00 |
| `bridge_market_channel` | `market_id` | `dim_market` | 48 | 0 | 18 | 0 | 100.0% | 2.67 |
| `bridge_neighbor_target` | `cell_neighbor_id` | `bridge_cell_neighbor` | 340,000 | 0 | 340,000 | 0 | 100.0% | 1.00 |
| `bridge_neighbor_target` | `neighbor_cell_id` | `dim_cell` | 340,000 | 0 | 85,000 | 0 | 100.0% | 4.00 |
| `bridge_offering_price` | `price_id` | `dim_price` | 2,400 | 0 | 2,400 | 0 | 100.0% | 1.00 |
| `bridge_offering_price` | `product_offering_id` | `dim_product_offering` | 2,400 | 0 | 500 | 0 | 100.0% | 4.80 |
| `bridge_partner_plmn` | `plmn_id` | `dim_plmn` | 900 | 0 | 900 | 0 | 100.0% | 1.00 |
| `bridge_partner_plmn` | `roaming_partner_id` | `dim_roaming_partner` | 900 | 0 | 640 | 0 | 100.0% | 1.41 |
| `bridge_party_address` | `address_id` | `dim_address` | 18,000,000 | 0 | 18,000,000 | 0 | 100.0% | 1.00 |
| `bridge_party_address` | `party_id` | `dim_party` | 18,000,000 | 0 | 17,600,000 | 4,400,000 | 80.0% | 1.02 |
| `bridge_plan_rating_group` | `rate_plan_id` | `dim_rate_plan` | 2,000 | 0 | 420 | 0 | 100.0% | 4.76 |
| `bridge_plan_rating_group` | `rating_group_id` | `dim_rating_group` | 2,000 | 0 | 200 | 0 | 100.0% | 10.00 |
| `bridge_policy_apn` | `apn_id` | `dim_apn` | 400 | 0 | 80 | 0 | 100.0% | 5.00 |
| `bridge_policy_apn` | `policy_rule_id` | `dim_policy_rule` | 400 | 0 | 60 | 0 | 100.0% | 6.67 |
| `bridge_prefix_zone` | `destination_zone_id` | `dim_destination_zone` | 5,000 | 0 | 90 | 0 | 100.0% | 55.56 |
| `bridge_prefix_zone` | `number_prefix_id` | `dim_number_prefix` | 5,000 | 0 | 5,000 | 0 | 100.0% | 1.00 |
| `bridge_roaming_zone` | `destination_zone_id` | `dim_destination_zone` | 1,200 | 0 | 90 | 0 | 100.0% | 13.33 |
| `bridge_roaming_zone` | `roaming_partner_id` | `dim_roaming_partner` | 1,200 | 0 | 640 | 0 | 100.0% | 1.88 |
| `bridge_slice_qos` | `qos_id` | `dim_qos` | 36 | 0 | 30 | 0 | 100.0% | 1.20 |
| `bridge_slice_qos` | `slice_id` | `dim_slice` | 36 | 0 | 12 | 0 | 100.0% | 3.00 |
| `bridge_subscriber_party` | `party_id` | `dim_party` | 20,000,000 | 0 | 20,000,000 | 2,000,000 | 90.9% | 1.00 |
| `bridge_subscriber_party` | `subscriber_id` | `dim_subscriber` | 20,000,000 | 0 | 20,000,000 | 0 | 100.0% | 1.00 |
| `bridge_subscription_addon` | `addon_id` | `dim_addon` | 18,000,000 | 0 | 260 | 0 | 100.0% | 69,230.77 |
| `bridge_subscription_addon` | `subscription_id` | `dim_subscription` | 18,000,000 | 0 | 12,500,000 | 12,500,000 | 50.0% | 1.44 |
| `bridge_tariff_zone` | `destination_zone_id` | `dim_destination_zone` | 4,000 | 0 | 90 | 0 | 100.0% | 44.44 |
| `bridge_tariff_zone` | `tariff_id` | `dim_tariff` | 4,000 | 0 | 1,100 | 0 | 100.0% | 3.64 |
| `bridge_trunk_prefix` | `interconnect_trunk_id` | `dim_interconnect_trunk` | 6,000 | 0 | 2,200 | 0 | 100.0% | 2.73 |
| `bridge_trunk_prefix` | `number_prefix_id` | `dim_number_prefix` | 6,000 | 0 | 5,000 | 0 | 100.0% | 1.20 |
| `bridge_workgroup_employee` | `employee_id` | `dim_employee` | 42,000 | 0 | 42,000 | 0 | 100.0% | 1.00 |
| `bridge_workgroup_employee` | `workgroup_id` | `dim_workgroup` | 42,000 | 0 | 120 | 0 | 100.0% | 350.00 |
| `dim_accounting_period` | `legal_entity_id` | `dim_legal_entity` | 1 | 0 | 1 | 3 | 25.0% | 1.00 |
| `dim_addon` | `product_offering_id` | `dim_product_offering` | 260 | 0 | 260 | 240 | 52.0% | 1.00 |
| `dim_address` | `country_id` | `dim_country` | 18,000,000 | 0 | 240 | 0 | 100.0% | 75,000.00 |
| `dim_agent` | `department_id` | `dim_department` | 6,000 | 0 | 80 | 0 | 100.0% | 75.00 |
| `dim_agent` | `employee_id` | `dim_employee` | 6,000 | 0 | 6,000 | 36,000 | 14.3% | 1.00 |
| `dim_bank` | `country_id` | `dim_country` | 25 | 0 | 25 | 215 | 10.4% | 1.00 |
| `dim_billing_account` | `bill_cycle_id` | `dim_bill_cycle` | 16,000,000 | 0 | 6 | 0 | 100.0% | 2,666,666.67 |
| `dim_billing_account` | `credit_class_id` | `dim_credit_class` | 16,000,000 | 0 | 8 | 0 | 100.0% | 2,000,000.00 |
| `dim_billing_account` | `currency_id` | `dim_currency` | 16,000,000 | 0 | 12 | 0 | 100.0% | 1,333,333.33 |
| `dim_billing_account` | `legal_entity_id` | `dim_legal_entity` | 16,000,000 | 0 | 4 | 0 | 100.0% | 4,000,000.00 |
| `dim_billing_account` | `market_id` | `dim_market` | 16,000,000 | 0 | 18 | 0 | 100.0% | 888,888.89 |
| `dim_billing_account` | `party_id` | `dim_party` | 16,000,000 | 0 | 16,000,000 | 6,000,000 | 72.7% | 1.00 |
| `dim_billing_account` | `segment_id` | `dim_segment` | 16,000,000 | 0 | 12 | 0 | 100.0% | 1,333,333.33 |
| `dim_campaign` | `channel_id` | `dim_channel` | 60 | 0 | 8 | 0 | 100.0% | 7.50 |
| `dim_carrier` | `country_id` | `dim_country` | 80 | 0 | 80 | 160 | 33.3% | 1.00 |
| `dim_cell` | `cell_site_id` | `dim_cell_site` | 85,000 | 0 | 28,000 | 0 | 100.0% | 3.04 |
| `dim_cell` | `tac_id` | `dim_tac` | 85,000 | 0 | 400 | 0 | 100.0% | 212.50 |
| `dim_cell` | `technology_id` | `dim_technology` | 85,000 | 0 | 6 | 0 | 100.0% | 14,166.67 |
| `dim_cell_site` | `address_id` | `dim_address` | 28,000 | 0 | 28,000 | 17,972,000 | 0.2% | 1.00 |
| `dim_cell_site` | `market_id` | `dim_market` | 28,000 | 0 | 18 | 0 | 100.0% | 1,555.56 |
| `dim_cell_site` | `region_id` | `dim_region` | 28,000 | 0 | 6 | 0 | 100.0% | 4,666.67 |
| `dim_cell_site` | `site_type_id` | `dim_site_type` | 28,000 | 0 | 5 | 0 | 100.0% | 5,600.00 |
| `dim_contact` | `party_id` | `dim_party` | 20,500,000 | 0 | 20,500,000 | 1,500,000 | 93.2% | 1.00 |
| `dim_content_provider` | `country_id` | `dim_country` | 350 | 0 | 240 | 0 | 100.0% | 1.46 |
| `dim_cost_center` | `department_id` | `dim_department` | 240 | 0 | 80 | 0 | 100.0% | 3.00 |
| `dim_cost_center` | `legal_entity_id` | `dim_legal_entity` | 240 | 0 | 4 | 0 | 100.0% | 60.00 |
| `dim_cost_element` | `gl_account_id` | `dim_gl_account` | 60 | 0 | 60 | 740 | 7.5% | 1.00 |
| `dim_dealer` | `channel_id` | `dim_channel` | 1,200 | 0 | 8 | 0 | 100.0% | 150.00 |
| `dim_dealer` | `market_id` | `dim_market` | 1,200 | 0 | 18 | 0 | 100.0% | 66.67 |
| `dim_department` | `legal_entity_id` | `dim_legal_entity` | 80 | 0 | 4 | 0 | 100.0% | 20.00 |
| `dim_device` | `device_model_id` | `dim_device_model` | 23,000,000 | 0 | 1,800 | 0 | 100.0% | 12,777.78 |
| `dim_device` | `subscriber_id` | `dim_subscriber` | 19,550,000 | 3,450,000 | 19,550,000 | 450,000 | 97.8% | 1.00 |
| `dim_device_model` | `vendor_id` | `dim_vendor` | 1,800 | 0 | 40 | 0 | 100.0% | 45.00 |
| `dim_discount` | `rate_plan_id` | `dim_rate_plan` | 144 | 36 | 144 | 276 | 34.3% | 1.00 |
| `dim_employee` | `cost_center_id` | `dim_cost_center` | 42,000 | 0 | 240 | 0 | 100.0% | 175.00 |
| `dim_employee` | `department_id` | `dim_department` | 42,000 | 0 | 80 | 0 | 100.0% | 525.00 |
| `dim_employee` | `market_id` | `dim_market` | 42,000 | 0 | 18 | 0 | 100.0% | 2,333.33 |
| `dim_gl_account` | `legal_entity_id` | `dim_legal_entity` | 800 | 0 | 4 | 0 | 100.0% | 200.00 |
| `dim_imsi` | `plmn_id` | `dim_plmn` | 26,000,000 | 0 | 900 | 0 | 100.0% | 28,888.89 |
| `dim_interconnect_trunk` | `carrier_id` | `dim_carrier` | 2,200 | 0 | 80 | 0 | 100.0% | 27.50 |
| `dim_interconnect_trunk` | `plmn_id` | `dim_plmn` | 2,200 | 0 | 900 | 0 | 100.0% | 2.44 |
| `dim_legal_entity` | `enterprise_id` | `dim_enterprise` | 4 | 0 | 1 | 0 | 100.0% | 4.00 |
| `dim_location_area` | `market_id` | `dim_market` | 3,200 | 0 | 18 | 0 | 100.0% | 177.78 |
| `dim_market` | `legal_entity_id` | `dim_legal_entity` | 18 | 0 | 4 | 0 | 100.0% | 4.50 |
| `dim_market` | `market_manager_employee_id` | `dim_employee` | 18 | 0 | 18 | 41,982 | 0.0% | 1.00 |
| `dim_market` | `region_id` | `dim_region` | 18 | 0 | 6 | 0 | 100.0% | 3.00 |
| `dim_msisdn` | `country_id` | `dim_country` | 27,000,000 | 0 | 240 | 0 | 100.0% | 112,500.00 |
| `dim_network_element` | `cell_site_id` | `dim_cell_site` | 8,400 | 3,600 | 8,400 | 19,600 | 30.0% | 1.00 |
| `dim_network_element` | `core_function_id` | `dim_core_function` | 12,000 | 0 | 10 | 0 | 100.0% | 1,200.00 |
| `dim_network_element` | `plmn_id` | `dim_plmn` | 12,000 | 0 | 900 | 0 | 100.0% | 13.33 |
| `dim_network_element` | `recording_entity_id` | `dim_recording_entity` | 12,000 | 0 | 400 | 0 | 100.0% | 30.00 |
| `dim_network_element` | `technology_id` | `dim_technology` | 12,000 | 0 | 6 | 0 | 100.0% | 2,000.00 |
| `dim_network_element` | `vendor_id` | `dim_vendor` | 12,000 | 0 | 40 | 0 | 100.0% | 300.00 |
| `dim_np_operator` | `country_id` | `dim_country` | 40 | 0 | 40 | 200 | 16.7% | 1.00 |
| `dim_number_prefix` | `country_id` | `dim_country` | 5,000 | 0 | 240 | 0 | 100.0% | 20.83 |
| `dim_number_prefix` | `destination_zone_id` | `dim_destination_zone` | 4,750 | 250 | 72 | 18 | 80.0% | 65.97 |
| `dim_party` | `address_id` | `dim_address` | 19,800,000 | 2,200,000 | 18,000,000 | 0 | 100.0% | 1.10 |
| `dim_party` | `country_id` | `dim_country` | 22,000,000 | 0 | 240 | 0 | 100.0% | 91,666.67 |
| `dim_plmn` | `country_id` | `dim_country` | 900 | 0 | 240 | 0 | 100.0% | 3.75 |
| `dim_policy_rule` | `qos_id` | `dim_qos` | 42 | 18 | 30 | 0 | 100.0% | 1.40 |
| `dim_policy_rule` | `slice_id` | `dim_slice` | 24 | 36 | 12 | 0 | 100.0% | 2.00 |
| `dim_price` | `currency_id` | `dim_currency` | 2,400 | 0 | 12 | 0 | 100.0% | 200.00 |
| `dim_price` | `product_offering_id` | `dim_product_offering` | 2,400 | 0 | 500 | 0 | 100.0% | 4.80 |
| `dim_product_offering` | `product_spec_id` | `dim_product_spec` | 500 | 0 | 220 | 0 | 100.0% | 2.27 |
| `dim_product_spec` | `technology_id` | `dim_technology` | 220 | 0 | 6 | 0 | 100.0% | 36.67 |
| `dim_queue` | `department_id` | `dim_department` | 40 | 0 | 40 | 40 | 50.0% | 1.00 |
| `dim_rate_plan` | `currency_id` | `dim_currency` | 420 | 0 | 12 | 0 | 100.0% | 35.00 |
| `dim_rate_plan` | `product_offering_id` | `dim_product_offering` | 420 | 0 | 420 | 80 | 84.0% | 1.00 |
| `dim_rating_group` | `charge_type_id` | `dim_charge_type` | 200 | 0 | 16 | 0 | 100.0% | 12.50 |
| `dim_recording_entity` | `core_function_id` | `dim_core_function` | 400 | 0 | 10 | 0 | 100.0% | 40.00 |
| `dim_region` | `legal_entity_id` | `dim_legal_entity` | 6 | 0 | 4 | 0 | 100.0% | 1.50 |
| `dim_resource` | `device_id` | `dim_device` | 12,000,000 | 18,000,000 | 12,000,000 | 11,000,000 | 52.2% | 1.00 |
| `dim_resource` | `service_id` | `dim_service` | 24,000,000 | 6,000,000 | 24,000,000 | 1,000,000 | 96.0% | 1.00 |
| `dim_resource` | `sim_id` | `dim_sim` | 15,000,000 | 15,000,000 | 15,000,000 | 9,000,000 | 62.5% | 1.00 |
| `dim_roaming_partner` | `country_id` | `dim_country` | 640 | 0 | 240 | 0 | 100.0% | 2.67 |
| `dim_roaming_partner` | `plmn_id` | `dim_plmn` | 640 | 0 | 640 | 260 | 71.1% | 1.00 |
| `dim_service` | `product_spec_id` | `dim_product_spec` | 25,000,000 | 0 | 220 | 0 | 100.0% | 113,636.36 |
| `dim_service` | `subscription_id` | `dim_subscription` | 25,000,000 | 0 | 25,000,000 | 0 | 100.0% | 1.00 |
| `dim_sim` | `imsi_id` | `dim_imsi` | 24,000,000 | 0 | 24,000,000 | 2,000,000 | 92.3% | 1.00 |
| `dim_sim` | `subscription_id` | `dim_subscription` | 23,040,000 | 960,000 | 23,040,000 | 1,960,000 | 92.2% | 1.00 |
| `dim_slice` | `qos_id` | `dim_qos` | 10 | 2 | 10 | 20 | 33.3% | 1.00 |
| `dim_subscriber` | `billing_account_id` | `dim_billing_account` | 20,000,000 | 0 | 16,000,000 | 0 | 100.0% | 1.25 |
| `dim_subscriber` | `party_id` | `dim_party` | 20,000,000 | 0 | 20,000,000 | 2,000,000 | 90.9% | 1.00 |
| `dim_subscription` | `market_id` | `dim_market` | 25,000,000 | 0 | 18 | 0 | 100.0% | 1,388,888.89 |
| `dim_subscription` | `msisdn_id` | `dim_msisdn` | 25,000,000 | 0 | 25,000,000 | 2,000,000 | 92.6% | 1.00 |
| `dim_subscription` | `rate_plan_id` | `dim_rate_plan` | 25,000,000 | 0 | 420 | 0 | 100.0% | 59,523.81 |
| `dim_subscription` | `subscriber_id` | `dim_subscriber` | 25,000,000 | 0 | 20,000,000 | 0 | 100.0% | 1.25 |
| `dim_tac` | `market_id` | `dim_market` | 400 | 0 | 18 | 0 | 100.0% | 22.22 |
| `dim_tariff` | `charge_type_id` | `dim_charge_type` | 1,100 | 0 | 16 | 0 | 100.0% | 68.75 |
| `dim_tariff` | `currency_id` | `dim_currency` | 1,100 | 0 | 12 | 0 | 100.0% | 91.67 |
| `dim_tariff` | `destination_zone_id` | `dim_destination_zone` | 990 | 110 | 90 | 0 | 100.0% | 11.00 |
| `dim_tax_code` | `gl_account_id` | `dim_gl_account` | 36 | 4 | 36 | 764 | 4.5% | 1.00 |
| `dim_tax_jurisdiction` | `country_id` | `dim_country` | 60 | 0 | 60 | 180 | 25.0% | 1.00 |
| `dim_workgroup` | `department_id` | `dim_department` | 120 | 0 | 80 | 0 | 100.0% | 1.50 |
| `fact_adjustment` | `adjustment_reason_id` | `dim_adjustment_reason` | 3,200,000 | 0 | 40 | 0 | 100.0% | 80,000.00 |
| `fact_adjustment` | `billing_account_id` | `dim_billing_account` | 3,200,000 | 0 | 2,400,000 | 13,600,000 | 15.0% | 1.33 |
| `fact_adjustment` | `calendar_day_id` | `dim_calendar_day` | 3,200,000 | 0 | 30 | 0 | 100.0% | 106,666.67 |
| `fact_adjustment` | `currency_id` | `dim_currency` | 3,200,000 | 0 | 12 | 0 | 100.0% | 266,666.67 |
| `fact_adjustment` | `employee_id` | `dim_employee` | 1,600,000 | 1,600,000 | 42,000 | 0 | 100.0% | 38.10 |
| `fact_allowance_draw` | `allowance_bucket_id` | `dim_allowance_bucket` | 900,000,000 | 0 | 40 | 0 | 100.0% | 22,500,000.00 |
| `fact_allowance_draw` | `calendar_day_id` | `dim_calendar_day` | 900,000,000 | 0 | 30 | 0 | 100.0% | 30,000,000.00 |
| `fact_allowance_draw` | `rated_charge_id` | `fact_rated_charge` | 720,000,000 | 180,000,000 | 720,000,000 | 1,380,000,000 | 34.3% | 1.00 |
| `fact_allowance_draw` | `subscription_id` | `dim_subscription` | 900,000,000 | 0 | 17,500,000 | 7,500,000 | 70.0% | 51.43 |
| `fact_attach` | `calendar_day_id` | `dim_calendar_day` | 2,400,000,000 | 0 | 30 | 0 | 100.0% | 80,000,000.00 |
| `fact_attach` | `cell_id` | `dim_cell` | 2,400,000,000 | 0 | 84,150 | 850 | 99.0% | 28,520.50 |
| `fact_attach` | `imsi_id` | `dim_imsi` | 2,400,000,000 | 0 | 24,700,000 | 1,300,000 | 95.0% | 97.17 |
| `fact_attach` | `msisdn_id` | `dim_msisdn` | 2,400,000,000 | 0 | 25,650,000 | 1,350,000 | 95.0% | 93.57 |
| `fact_attach` | `network_element_id` | `dim_network_element` | 2,400,000,000 | 0 | 12,000 | 0 | 100.0% | 200,000.00 |
| `fact_attach` | `plmn_id` | `dim_plmn` | 2,400,000,000 | 0 | 135 | 765 | 15.0% | 17,777,777.78 |
| `fact_attach` | `subscriber_id` | `dim_subscriber` | 2,400,000,000 | 0 | 19,600,000 | 400,000 | 98.0% | 122.45 |
| `fact_attach` | `technology_id` | `dim_technology` | 2,400,000,000 | 0 | 6 | 0 | 100.0% | 400,000,000.00 |
| `fact_balance_debit` | `balance_reservation_id` | `fact_balance_reservation` | 3,150,000,000 | 0 | 3,150,000,000 | 1,050,000,000 | 75.0% | 1.00 |
| `fact_balance_debit` | `balance_type_id` | `dim_balance_type` | 3,150,000,000 | 0 | 10 | 0 | 100.0% | 315,000,000.00 |
| `fact_balance_debit` | `calendar_day_id` | `dim_calendar_day` | 3,150,000,000 | 0 | 30 | 0 | 100.0% | 105,000,000.00 |
| `fact_balance_debit` | `subscription_id` | `dim_subscription` | 3,150,000,000 | 0 | 23,250,000 | 1,750,000 | 93.0% | 135.48 |
| `fact_balance_reservation` | `balance_type_id` | `dim_balance_type` | 4,200,000,000 | 0 | 10 | 0 | 100.0% | 420,000,000.00 |
| `fact_balance_reservation` | `calendar_day_id` | `dim_calendar_day` | 4,200,000,000 | 0 | 30 | 0 | 100.0% | 140,000,000.00 |
| `fact_balance_reservation` | `charging_event_id` | `fact_charging_event` | 4,200,000,000 | 0 | 4,200,000,000 | 2,100,000,000 | 66.7% | 1.00 |
| `fact_balance_reservation` | `subscription_id` | `dim_subscription` | 4,200,000,000 | 0 | 23,750,000 | 1,250,000 | 95.0% | 176.84 |
| `fact_barring_event` | `barring_id` | `dim_barring` | 80,000 | 0 | 15 | 0 | 100.0% | 5,333.33 |
| `fact_barring_event` | `calendar_day_id` | `dim_calendar_day` | 80,000 | 0 | 30 | 0 | 100.0% | 2,666.67 |
| `fact_barring_event` | `employee_id` | `dim_employee` | 48,000 | 32,000 | 42,000 | 0 | 100.0% | 1.14 |
| `fact_barring_event` | `subscriber_id` | `dim_subscriber` | 80,000 | 0 | 80,000 | 19,920,000 | 0.4% | 1.00 |
| `fact_bundle_snapshot` | `calendar_day_id` | `dim_calendar_day` | 25,000,000 | 0 | 30 | 0 | 100.0% | 833,333.33 |
| `fact_bundle_snapshot` | `rate_plan_id` | `dim_rate_plan` | 25,000,000 | 0 | 420 | 0 | 100.0% | 59,523.81 |
| `fact_bundle_snapshot` | `subscription_id` | `dim_subscription` | 25,000,000 | 0 | 25,000,000 | 0 | 100.0% | 1.00 |
| `fact_campaign_contact` | `calendar_day_id` | `dim_calendar_day` | 4,000,000 | 0 | 30 | 0 | 100.0% | 133,333.33 |
| `fact_campaign_contact` | `campaign_id` | `dim_campaign` | 4,000,000 | 0 | 60 | 0 | 100.0% | 66,666.67 |
| `fact_campaign_contact` | `channel_id` | `dim_channel` | 4,000,000 | 0 | 8 | 0 | 100.0% | 500,000.00 |
| `fact_campaign_contact` | `party_id` | `dim_party` | 4,000,000 | 0 | 3,300,000 | 18,700,000 | 15.0% | 1.21 |
| `fact_campaign_contact` | `script_id` | `dim_script` | 4,000,000 | 0 | 30 | 0 | 100.0% | 133,333.33 |
| `fact_cell_counter` | `calendar_day_id` | `dim_calendar_day` | 244,800,000 | 0 | 30 | 0 | 100.0% | 8,160,000.00 |
| `fact_cell_counter` | `cell_id` | `dim_cell` | 244,800,000 | 0 | 85,000 | 0 | 100.0% | 2,880.00 |
| `fact_cell_counter` | `cell_site_id` | `dim_cell_site` | 244,800,000 | 0 | 28,000 | 0 | 100.0% | 8,742.86 |
| `fact_cell_counter` | `technology_id` | `dim_technology` | 244,800,000 | 0 | 6 | 0 | 100.0% | 40,800,000.00 |
| `fact_charging_event` | `apn_id` | `dim_apn` | 6,300,000,000 | 0 | 80 | 0 | 100.0% | 78,750,000.00 |
| `fact_charging_event` | `balance_type_id` | `dim_balance_type` | 6,300,000,000 | 0 | 10 | 0 | 100.0% | 630,000,000.00 |
| `fact_charging_event` | `calendar_day_id` | `dim_calendar_day` | 6,300,000,000 | 0 | 30 | 0 | 100.0% | 210,000,000.00 |
| `fact_charging_event` | `network_element_id` | `dim_network_element` | 6,300,000,000 | 0 | 12,000 | 0 | 100.0% | 525,000.00 |
| `fact_charging_event` | `plmn_id` | `dim_plmn` | 6,300,000,000 | 0 | 180 | 720 | 20.0% | 35,000,000.00 |
| `fact_charging_event` | `qos_id` | `dim_qos` | 6,300,000,000 | 0 | 30 | 0 | 100.0% | 210,000,000.00 |
| `fact_charging_event` | `rate_plan_id` | `dim_rate_plan` | 6,300,000,000 | 0 | 420 | 0 | 100.0% | 15,000,000.00 |
| `fact_charging_event` | `rating_group_id` | `dim_rating_group` | 6,300,000,000 | 0 | 200 | 0 | 100.0% | 31,500,000.00 |
| `fact_charging_event` | `record_type_id` | `dim_record_type` | 6,300,000,000 | 0 | 24 | 0 | 100.0% | 262,500,000.00 |
| `fact_charging_event` | `subscriber_id` | `dim_subscriber` | 6,300,000,000 | 0 | 19,400,000 | 600,000 | 97.0% | 324.74 |
| `fact_charging_event` | `subscription_id` | `dim_subscription` | 6,300,000,000 | 0 | 24,250,000 | 750,000 | 97.0% | 259.79 |
| `fact_collection_referral` | `billing_account_id` | `dim_billing_account` | 40,000 | 0 | 40,000 | 15,960,000 | 0.2% | 1.00 |
| `fact_collection_referral` | `calendar_day_id` | `dim_calendar_day` | 40,000 | 0 | 30 | 0 | 100.0% | 1,333.33 |
| `fact_collection_referral` | `collection_agency_id` | `dim_collection_agency` | 40,000 | 0 | 8 | 0 | 100.0% | 5,000.00 |
| `fact_content_cdr` | `calendar_day_id` | `dim_calendar_day` | 30,000,000 | 0 | 30 | 0 | 100.0% | 1,000,000.00 |
| `fact_content_cdr` | `charge_type_id` | `dim_charge_type` | 30,000,000 | 0 | 16 | 0 | 100.0% | 1,875,000.00 |
| `fact_content_cdr` | `content_provider_id` | `dim_content_provider` | 30,000,000 | 0 | 350 | 0 | 100.0% | 85,714.29 |
| `fact_content_cdr` | `currency_id` | `dim_currency` | 30,000,000 | 0 | 12 | 0 | 100.0% | 2,500,000.00 |
| `fact_content_cdr` | `subscription_id` | `dim_subscription` | 30,000,000 | 0 | 3,750,000 | 21,250,000 | 15.0% | 8.00 |
| `fact_counter_breach` | `calendar_day_id` | `dim_calendar_day` | 500,000 | 0 | 30 | 0 | 100.0% | 16,666.67 |
| `fact_counter_breach` | `cell_counter_id` | `fact_cell_counter` | 500,000 | 0 | 489,600 | 244,310,400 | 0.2% | 1.02 |
| `fact_counter_breach` | `cell_id` | `dim_cell` | 500,000 | 0 | 8,500 | 76,500 | 10.0% | 58.82 |
| `fact_credit_note` | `billing_account_id` | `dim_billing_account` | 400,000 | 0 | 400,000 | 15,600,000 | 2.5% | 1.00 |
| `fact_credit_note` | `calendar_day_id` | `dim_calendar_day` | 400,000 | 0 | 30 | 0 | 100.0% | 13,333.33 |
| `fact_credit_note` | `currency_id` | `dim_currency` | 400,000 | 0 | 12 | 0 | 100.0% | 33,333.33 |
| `fact_credit_note` | `invoice_id` | `fact_invoice` | 360,000 | 40,000 | 360,000 | 15,640,000 | 2.2% | 1.00 |
| `fact_data_cdr` | `apn_id` | `dim_apn` | 1,400,000,000 | 0 | 80 | 0 | 100.0% | 17,500,000.00 |
| `fact_data_cdr` | `calendar_day_id` | `dim_calendar_day` | 1,400,000,000 | 0 | 30 | 0 | 100.0% | 46,666,666.67 |
| `fact_data_cdr` | `cell_id` | `dim_cell` | 1,400,000,000 | 0 | 84,150 | 850 | 99.0% | 16,636.96 |
| `fact_data_cdr` | `cell_site_id` | `dim_cell_site` | 1,400,000,000 | 0 | 27,720 | 280 | 99.0% | 50,505.05 |
| `fact_data_cdr` | `imsi_id` | `dim_imsi` | 1,400,000,000 | 0 | 23,400,000 | 2,600,000 | 90.0% | 59.83 |
| `fact_data_cdr` | `mediation_file_id` | `fact_mediation_file` | 1,400,000,000 | 0 | 360,000 | 0 | 100.0% | 3,888.89 |
| `fact_data_cdr` | `msisdn_id` | `dim_msisdn` | 1,400,000,000 | 0 | 24,300,000 | 2,700,000 | 90.0% | 57.61 |
| `fact_data_cdr` | `network_element_id` | `dim_network_element` | 1,400,000,000 | 0 | 12,000 | 0 | 100.0% | 116,666.67 |
| `fact_data_cdr` | `plmn_id` | `dim_plmn` | 1,400,000,000 | 0 | 180 | 720 | 20.0% | 7,777,777.78 |
| `fact_data_cdr` | `qos_id` | `dim_qos` | 1,400,000,000 | 0 | 30 | 0 | 100.0% | 46,666,666.67 |
| `fact_data_cdr` | `rate_plan_id` | `dim_rate_plan` | 1,400,000,000 | 0 | 420 | 0 | 100.0% | 3,333,333.33 |
| `fact_data_cdr` | `rating_group_id` | `dim_rating_group` | 1,400,000,000 | 0 | 200 | 0 | 100.0% | 7,000,000.00 |
| `fact_data_cdr` | `record_type_id` | `dim_record_type` | 1,400,000,000 | 0 | 24 | 0 | 100.0% | 58,333,333.33 |
| `fact_data_cdr` | `recording_entity_id` | `dim_recording_entity` | 1,400,000,000 | 0 | 400 | 0 | 100.0% | 3,500,000.00 |
| `fact_data_cdr` | `release_cause_id` | `dim_release_cause` | 1,120,000,000 | 280,000,000 | 126 | 54 | 70.0% | 8,888,888.89 |
| `fact_data_cdr` | `roaming_partner_id` | `dim_roaming_partner` | 168,000,000 | 1,232,000,000 | 256 | 384 | 40.0% | 656,250.00 |
| `fact_data_cdr` | `slice_id` | `dim_slice` | 490,000,000 | 910,000,000 | 12 | 0 | 100.0% | 40,833,333.33 |
| `fact_data_cdr` | `subscriber_id` | `dim_subscriber` | 1,400,000,000 | 0 | 18,800,000 | 1,200,000 | 94.0% | 74.47 |
| `fact_data_cdr` | `subscription_id` | `dim_subscription` | 1,400,000,000 | 0 | 23,500,000 | 1,500,000 | 94.0% | 59.57 |
| `fact_data_cdr` | `technology_id` | `dim_technology` | 1,400,000,000 | 0 | 6 | 0 | 100.0% | 233,333,333.33 |
| `fact_dealer_sale` | `calendar_day_id` | `dim_calendar_day` | 420,000 | 0 | 30 | 0 | 100.0% | 14,000.00 |
| `fact_dealer_sale` | `dealer_id` | `dim_dealer` | 420,000 | 0 | 1,200 | 0 | 100.0% | 350.00 |
| `fact_dealer_sale` | `employee_id` | `dim_employee` | 126,000 | 294,000 | 42,000 | 0 | 100.0% | 3.00 |
| `fact_dealer_sale` | `rate_plan_id` | `dim_rate_plan` | 420,000 | 0 | 420 | 0 | 100.0% | 1,000.00 |
| `fact_dealer_sale` | `sale_type_id` | `dim_sale_type` | 420,000 | 0 | 6 | 0 | 100.0% | 70,000.00 |
| `fact_dealer_sale` | `subscription_id` | `dim_subscription` | 420,000 | 0 | 420,000 | 24,580,000 | 1.7% | 1.00 |
| `fact_document` | `calendar_day_id` | `dim_calendar_day` | 16,000,000 | 0 | 30 | 0 | 100.0% | 533,333.33 |
| `fact_document` | `document_type_id` | `dim_document_type` | 16,000,000 | 0 | 12 | 0 | 100.0% | 1,333,333.33 |
| `fact_document` | `invoice_id` | `fact_invoice` | 16,000,000 | 0 | 16,000,000 | 0 | 100.0% | 1.00 |
| `fact_dunning_event` | `billing_account_id` | `dim_billing_account` | 1,800,000 | 0 | 1,280,000 | 14,720,000 | 8.0% | 1.41 |
| `fact_dunning_event` | `calendar_day_id` | `dim_calendar_day` | 1,800,000 | 0 | 30 | 0 | 100.0% | 60,000.00 |
| `fact_dunning_event` | `dunning_level_id` | `dim_dunning_level` | 1,800,000 | 0 | 5 | 0 | 100.0% | 360,000.00 |
| `fact_duplicate_suspect` | `calendar_day_id` | `dim_calendar_day` | 2,100,000 | 0 | 30 | 0 | 100.0% | 70,000.00 |
| `fact_duplicate_suspect` | `record_type_id` | `dim_record_type` | 2,100,000 | 0 | 24 | 0 | 100.0% | 87,500.00 |
| `fact_duplicate_suspect` | `subscription_id` | `dim_subscription` | 1,890,000 | 210,000 | 1,890,000 | 23,110,000 | 7.6% | 1.00 |
| `fact_fraud_alert` | `calendar_day_id` | `dim_calendar_day` | 350,000 | 0 | 30 | 0 | 100.0% | 11,666.67 |
| `fact_fraud_alert` | `fraud_rule_id` | `dim_fraud_rule` | 350,000 | 0 | 90 | 0 | 100.0% | 3,888.89 |
| `fact_fraud_alert` | `msisdn_id` | `dim_msisdn` | 315,000 | 35,000 | 315,000 | 26,685,000 | 1.2% | 1.00 |
| `fact_fraud_alert` | `subscriber_id` | `dim_subscriber` | 350,000 | 0 | 300,000 | 19,700,000 | 1.5% | 1.17 |
| `fact_handover` | `calendar_day_id` | `dim_calendar_day` | 960,000,000 | 0 | 30 | 0 | 100.0% | 32,000,000.00 |
| `fact_handover` | `handover_type_id` | `dim_handover_type` | 960,000,000 | 0 | 8 | 0 | 100.0% | 120,000,000.00 |
| `fact_handover` | `network_element_id` | `dim_network_element` | 960,000,000 | 0 | 12,000 | 0 | 100.0% | 80,000.00 |
| `fact_handover` | `source_cell_id` | `dim_cell` | 960,000,000 | 0 | 80,750 | 4,250 | 95.0% | 11,888.54 |
| `fact_handover` | `subscriber_id` | `dim_subscriber` | 960,000,000 | 0 | 16,000,000 | 4,000,000 | 80.0% | 60.00 |
| `fact_handover` | `technology_id` | `dim_technology` | 960,000,000 | 0 | 6 | 0 | 100.0% | 160,000,000.00 |
| `fact_handover_target` | `handover_id` | `fact_handover` | 960,000,000 | 0 | 960,000,000 | 0 | 100.0% | 1.00 |
| `fact_handover_target` | `target_cell_id` | `dim_cell` | 960,000,000 | 0 | 80,750 | 4,250 | 95.0% | 11,888.54 |
| `fact_interaction` | `agent_id` | `dim_agent` | 9,500,000 | 0 | 6,000 | 0 | 100.0% | 1,583.33 |
| `fact_interaction` | `calendar_day_id` | `dim_calendar_day` | 9,500,000 | 0 | 30 | 0 | 100.0% | 316,666.67 |
| `fact_interaction` | `care_reason_id` | `dim_care_reason` | 9,500,000 | 0 | 50 | 0 | 100.0% | 190,000.00 |
| `fact_interaction` | `channel_id` | `dim_channel` | 9,500,000 | 0 | 8 | 0 | 100.0% | 1,187,500.00 |
| `fact_interaction` | `party_id` | `dim_party` | 9,500,000 | 0 | 6,600,000 | 15,400,000 | 30.0% | 1.44 |
| `fact_interaction` | `queue_id` | `dim_queue` | 9,500,000 | 0 | 40 | 0 | 100.0% | 237,500.00 |
| `fact_interaction` | `subscriber_id` | `dim_subscriber` | 7,600,000 | 1,900,000 | 7,600,000 | 12,400,000 | 38.0% | 1.00 |
| `fact_interconnect_invoice` | `accounting_period_id` | `dim_accounting_period` | 80 | 0 | 1 | 0 | 100.0% | 80.00 |
| `fact_interconnect_invoice` | `calendar_day_id` | `dim_calendar_day` | 80 | 0 | 30 | 0 | 100.0% | 2.67 |
| `fact_interconnect_invoice` | `carrier_id` | `dim_carrier` | 80 | 0 | 80 | 0 | 100.0% | 1.00 |
| `fact_interconnect_invoice` | `currency_id` | `dim_currency` | 80 | 0 | 12 | 0 | 100.0% | 6.67 |
| `fact_invoice` | `bill_cycle_id` | `dim_bill_cycle` | 16,000,000 | 0 | 6 | 0 | 100.0% | 2,666,666.67 |
| `fact_invoice` | `billing_account_id` | `dim_billing_account` | 16,000,000 | 0 | 16,000,000 | 0 | 100.0% | 1.00 |
| `fact_invoice` | `calendar_day_id` | `dim_calendar_day` | 16,000,000 | 0 | 30 | 0 | 100.0% | 533,333.33 |
| `fact_invoice` | `currency_id` | `dim_currency` | 16,000,000 | 0 | 12 | 0 | 100.0% | 1,333,333.33 |
| `fact_invoice` | `legal_entity_id` | `dim_legal_entity` | 16,000,000 | 0 | 4 | 0 | 100.0% | 4,000,000.00 |
| `fact_invoice` | `market_id` | `dim_market` | 16,000,000 | 0 | 18 | 0 | 100.0% | 888,888.89 |
| `fact_invoice_line` | `calendar_day_id` | `dim_calendar_day` | 128,000,000 | 0 | 30 | 0 | 100.0% | 4,266,666.67 |
| `fact_invoice_line` | `charge_type_id` | `dim_charge_type` | 128,000,000 | 0 | 16 | 0 | 100.0% | 8,000,000.00 |
| `fact_invoice_line` | `currency_id` | `dim_currency` | 128,000,000 | 0 | 12 | 0 | 100.0% | 10,666,666.67 |
| `fact_invoice_line` | `gl_account_id` | `dim_gl_account` | 128,000,000 | 0 | 800 | 0 | 100.0% | 160,000.00 |
| `fact_invoice_line` | `invoice_id` | `fact_invoice` | 128,000,000 | 0 | 16,000,000 | 0 | 100.0% | 8.00 |
| `fact_invoice_line` | `rated_charge_id` | `fact_rated_charge` | 89,600,000 | 38,400,000 | 89,600,000 | 2,010,400,000 | 4.3% | 1.00 |
| `fact_invoice_line` | `tax_code_id` | `dim_tax_code` | 96,000,000 | 32,000,000 | 40 | 0 | 100.0% | 2,400,000.00 |
| `fact_journal_line` | `accounting_period_id` | `dim_accounting_period` | 6,000,000 | 0 | 1 | 0 | 100.0% | 6,000,000.00 |
| `fact_journal_line` | `calendar_day_id` | `dim_calendar_day` | 6,000,000 | 0 | 30 | 0 | 100.0% | 200,000.00 |
| `fact_journal_line` | `cost_center_id` | `dim_cost_center` | 4,800,000 | 1,200,000 | 240 | 0 | 100.0% | 20,000.00 |
| `fact_journal_line` | `cost_element_id` | `dim_cost_element` | 3,000,000 | 3,000,000 | 60 | 0 | 100.0% | 50,000.00 |
| `fact_journal_line` | `currency_id` | `dim_currency` | 6,000,000 | 0 | 12 | 0 | 100.0% | 500,000.00 |
| `fact_journal_line` | `gl_account_id` | `dim_gl_account` | 6,000,000 | 0 | 800 | 0 | 100.0% | 7,500.00 |
| `fact_journal_line` | `journal_source_id` | `dim_journal_source` | 6,000,000 | 0 | 8 | 0 | 100.0% | 750,000.00 |
| `fact_journal_line` | `legal_entity_id` | `dim_legal_entity` | 6,000,000 | 0 | 4 | 0 | 100.0% | 1,500,000.00 |
| `fact_location_update` | `calendar_day_id` | `dim_calendar_day` | 600,000,000 | 0 | 30 | 0 | 100.0% | 20,000,000.00 |
| `fact_location_update` | `cell_id` | `dim_cell` | 420,000,000 | 180,000,000 | 68,000 | 17,000 | 80.0% | 6,176.47 |
| `fact_location_update` | `location_area_id` | `dim_location_area` | 600,000,000 | 0 | 3,200 | 0 | 100.0% | 187,500.00 |
| `fact_location_update` | `subscriber_id` | `dim_subscriber` | 600,000,000 | 0 | 17,000,000 | 3,000,000 | 85.0% | 35.29 |
| `fact_location_update` | `technology_id` | `dim_technology` | 600,000,000 | 0 | 6 | 0 | 100.0% | 100,000,000.00 |
| `fact_mediation_file` | `calendar_day_id` | `dim_calendar_day` | 360,000 | 0 | 30 | 0 | 100.0% | 12,000.00 |
| `fact_mediation_file` | `file_format_id` | `dim_file_format` | 360,000 | 0 | 4 | 0 | 100.0% | 90,000.00 |
| `fact_mediation_file` | `network_element_id` | `dim_network_element` | 360,000 | 0 | 12,000 | 0 | 100.0% | 30.00 |
| `fact_mediation_file` | `recording_entity_id` | `dim_recording_entity` | 360,000 | 0 | 400 | 0 | 100.0% | 900.00 |
| `fact_mediation_reject` | `calendar_day_id` | `dim_calendar_day` | 8,400,000 | 0 | 30 | 0 | 100.0% | 280,000.00 |
| `fact_mediation_reject` | `data_cdr_id` | `fact_data_cdr` | 5,600,000 | 2,800,000 | 5,600,000 | 1,394,400,000 | 0.4% | 1.00 |
| `fact_mediation_reject` | `mediation_rule_id` | `dim_mediation_rule` | 8,400,000 | 0 | 150 | 0 | 100.0% | 56,000.00 |
| `fact_mediation_reject` | `record_type_id` | `dim_record_type` | 8,400,000 | 0 | 24 | 0 | 100.0% | 350,000.00 |
| `fact_mediation_reject` | `recording_entity_id` | `dim_recording_entity` | 8,400,000 | 0 | 400 | 0 | 100.0% | 21,000.00 |
| `fact_mediation_reject` | `sms_cdr_id` | `fact_sms_cdr` | 800,000 | 7,600,000 | 800,000 | 149,200,000 | 0.5% | 1.00 |
| `fact_mediation_reject` | `voice_cdr_id` | `fact_voice_cdr` | 2,000,000 | 6,400,000 | 2,000,000 | 518,000,000 | 0.4% | 1.00 |
| `fact_network_alarm` | `alarm_severity_id` | `dim_alarm_severity` | 1,800,000 | 0 | 5 | 0 | 100.0% | 360,000.00 |
| `fact_network_alarm` | `calendar_day_id` | `dim_calendar_day` | 1,800,000 | 0 | 30 | 0 | 100.0% | 60,000.00 |
| `fact_network_alarm` | `cell_id` | `dim_cell` | 720,000 | 1,080,000 | 17,000 | 68,000 | 20.0% | 42.35 |
| `fact_network_alarm` | `network_element_id` | `dim_network_element` | 1,800,000 | 0 | 6,600 | 5,400 | 55.0% | 272.73 |
| `fact_network_alarm` | `technology_id` | `dim_technology` | 1,800,000 | 0 | 6 | 0 | 100.0% | 300,000.00 |
| `fact_number_port` | `calendar_day_id` | `dim_calendar_day` | 180,000 | 0 | 30 | 0 | 100.0% | 6,000.00 |
| `fact_number_port` | `msisdn_id` | `dim_msisdn` | 180,000 | 0 | 180,000 | 26,820,000 | 0.7% | 1.00 |
| `fact_number_port` | `np_operator_id` | `dim_np_operator` | 180,000 | 0 | 40 | 0 | 100.0% | 4,500.00 |
| `fact_number_port` | `subscription_id` | `dim_subscription` | 144,000 | 36,000 | 144,000 | 24,856,000 | 0.6% | 1.00 |
| `fact_outage_ticket` | `calendar_day_id` | `dim_calendar_day` | 4,000 | 0 | 30 | 0 | 100.0% | 133.33 |
| `fact_outage_ticket` | `cell_site_id` | `dim_cell_site` | 3,200 | 800 | 3,200 | 24,800 | 11.4% | 1.00 |
| `fact_outage_ticket` | `network_element_id` | `dim_network_element` | 2,400 | 1,600 | 2,400 | 9,600 | 20.0% | 1.00 |
| `fact_outage_ticket` | `trouble_code_id` | `dim_trouble_code` | 4,000 | 0 | 300 | 0 | 100.0% | 13.33 |
| `fact_payment` | `bank_id` | `dim_bank` | 11,600,000 | 2,900,000 | 25 | 0 | 100.0% | 464,000.00 |
| `fact_payment` | `billing_account_id` | `dim_billing_account` | 14,500,000 | 0 | 11,200,000 | 4,800,000 | 70.0% | 1.29 |
| `fact_payment` | `calendar_day_id` | `dim_calendar_day` | 14,500,000 | 0 | 30 | 0 | 100.0% | 483,333.33 |
| `fact_payment` | `currency_id` | `dim_currency` | 14,500,000 | 0 | 12 | 0 | 100.0% | 1,208,333.33 |
| `fact_payment` | `payment_method_id` | `dim_payment_method` | 14,500,000 | 0 | 8 | 0 | 100.0% | 1,812,500.00 |
| `fact_policy_event` | `calendar_day_id` | `dim_calendar_day` | 1,800,000,000 | 0 | 30 | 0 | 100.0% | 60,000,000.00 |
| `fact_policy_event` | `cell_id` | `dim_cell` | 1,440,000,000 | 360,000,000 | 76,500 | 8,500 | 90.0% | 18,823.53 |
| `fact_policy_event` | `network_element_id` | `dim_network_element` | 1,800,000,000 | 0 | 12,000 | 0 | 100.0% | 150,000.00 |
| `fact_policy_event` | `policy_rule_id` | `dim_policy_rule` | 1,800,000,000 | 0 | 60 | 0 | 100.0% | 30,000,000.00 |
| `fact_policy_event` | `qos_id` | `dim_qos` | 1,800,000,000 | 0 | 30 | 0 | 100.0% | 60,000,000.00 |
| `fact_policy_event` | `slice_id` | `dim_slice` | 720,000,000 | 1,080,000,000 | 12 | 0 | 100.0% | 60,000,000.00 |
| `fact_policy_event` | `subscription_id` | `dim_subscription` | 1,800,000,000 | 0 | 22,500,000 | 2,500,000 | 90.0% | 80.00 |
| `fact_promise_to_pay` | `agent_id` | `dim_agent` | 260,000 | 0 | 6,000 | 0 | 100.0% | 43.33 |
| `fact_promise_to_pay` | `billing_account_id` | `dim_billing_account` | 260,000 | 0 | 260,000 | 15,740,000 | 1.6% | 1.00 |
| `fact_promise_to_pay` | `calendar_day_id` | `dim_calendar_day` | 260,000 | 0 | 30 | 0 | 100.0% | 8,666.67 |
| `fact_qos_change` | `calendar_day_id` | `dim_calendar_day` | 300,000,000 | 0 | 30 | 0 | 100.0% | 10,000,000.00 |
| `fact_qos_change` | `cell_id` | `dim_cell` | 300,000,000 | 0 | 68,000 | 17,000 | 80.0% | 4,411.76 |
| `fact_qos_change` | `policy_rule_id` | `dim_policy_rule` | 180,000,000 | 120,000,000 | 60 | 0 | 100.0% | 3,000,000.00 |
| `fact_qos_change` | `qos_id` | `dim_qos` | 300,000,000 | 0 | 30 | 0 | 100.0% | 10,000,000.00 |
| `fact_qos_change` | `subscription_id` | `dim_subscription` | 300,000,000 | 0 | 12,500,000 | 12,500,000 | 50.0% | 24.00 |
| `fact_rated_charge` | `calendar_day_id` | `dim_calendar_day` | 2,100,000,000 | 0 | 30 | 0 | 100.0% | 70,000,000.00 |
| `fact_rated_charge` | `charge_type_id` | `dim_charge_type` | 2,100,000,000 | 0 | 16 | 0 | 100.0% | 131,250,000.00 |
| `fact_rated_charge` | `content_cdr_id` | `fact_content_cdr` | 30,000,000 | 2,070,000,000 | 30,000,000 | 0 | 100.0% | 1.00 |
| `fact_rated_charge` | `currency_id` | `dim_currency` | 2,100,000,000 | 0 | 12 | 0 | 100.0% | 175,000,000.00 |
| `fact_rated_charge` | `data_cdr_id` | `fact_data_cdr` | 1,400,000,000 | 700,000,000 | 1,400,000,000 | 0 | 100.0% | 1.00 |
| `fact_rated_charge` | `gl_account_id` | `dim_gl_account` | 2,100,000,000 | 0 | 800 | 0 | 100.0% | 2,625,000.00 |
| `fact_rated_charge` | `rate_plan_id` | `dim_rate_plan` | 2,100,000,000 | 0 | 420 | 0 | 100.0% | 5,000,000.00 |
| `fact_rated_charge` | `sms_cdr_id` | `fact_sms_cdr` | 150,000,000 | 1,950,000,000 | 150,000,000 | 0 | 100.0% | 1.00 |
| `fact_rated_charge` | `subscription_id` | `dim_subscription` | 2,100,000,000 | 0 | 24,000,000 | 1,000,000 | 96.0% | 87.50 |
| `fact_rated_charge` | `tariff_id` | `dim_tariff` | 2,037,000,000 | 63,000,000 | 1,100 | 0 | 100.0% | 1,851,818.18 |
| `fact_rated_charge` | `tax_code_id` | `dim_tax_code` | 1,890,000,000 | 210,000,000 | 40 | 0 | 100.0% | 47,250,000.00 |
| `fact_rated_charge` | `voice_cdr_id` | `fact_voice_cdr` | 520,000,000 | 1,580,000,000 | 520,000,000 | 0 | 100.0% | 1.00 |
| `fact_refund` | `adjustment_reason_id` | `dim_adjustment_reason` | 220,000 | 0 | 40 | 0 | 100.0% | 5,500.00 |
| `fact_refund` | `billing_account_id` | `dim_billing_account` | 220,000 | 0 | 220,000 | 15,780,000 | 1.4% | 1.00 |
| `fact_refund` | `calendar_day_id` | `dim_calendar_day` | 220,000 | 0 | 30 | 0 | 100.0% | 7,333.33 |
| `fact_refund` | `currency_id` | `dim_currency` | 220,000 | 0 | 12 | 0 | 100.0% | 18,333.33 |
| `fact_refund` | `payment_id` | `fact_payment` | 209,000 | 11,000 | 209,000 | 14,291,000 | 1.4% | 1.00 |
| `fact_rerate` | `calendar_day_id` | `dim_calendar_day` | 21,000,000 | 0 | 30 | 0 | 100.0% | 700,000.00 |
| `fact_rerate` | `employee_id` | `dim_employee` | 4,200,000 | 16,800,000 | 42,000 | 0 | 100.0% | 100.00 |
| `fact_rerate` | `rated_charge_id` | `fact_rated_charge` | 21,000,000 | 0 | 21,000,000 | 2,079,000,000 | 1.0% | 1.00 |
| `fact_settlement_line` | `accounting_period_id` | `dim_accounting_period` | 2,400,000 | 0 | 1 | 0 | 100.0% | 2,400,000.00 |
| `fact_settlement_line` | `calendar_day_id` | `dim_calendar_day` | 2,400,000 | 0 | 30 | 0 | 100.0% | 80,000.00 |
| `fact_settlement_line` | `currency_id` | `dim_currency` | 2,400,000 | 0 | 12 | 0 | 100.0% | 200,000.00 |
| `fact_settlement_line` | `plmn_id` | `dim_plmn` | 2,400,000 | 0 | 900 | 0 | 100.0% | 2,666.67 |
| `fact_settlement_line` | `record_type_id` | `dim_record_type` | 2,400,000 | 0 | 24 | 0 | 100.0% | 100,000.00 |
| `fact_settlement_line` | `roaming_partner_id` | `dim_roaming_partner` | 2,400,000 | 0 | 640 | 0 | 100.0% | 3,750.00 |
| `fact_sim_swap` | `calendar_day_id` | `dim_calendar_day` | 250,000 | 0 | 30 | 0 | 100.0% | 8,333.33 |
| `fact_sim_swap` | `dealer_id` | `dim_dealer` | 100,000 | 150,000 | 1,200 | 0 | 100.0% | 83.33 |
| `fact_sim_swap` | `employee_id` | `dim_employee` | 175,000 | 75,000 | 42,000 | 0 | 100.0% | 4.17 |
| `fact_sim_swap` | `sim_id` | `dim_sim` | 250,000 | 0 | 250,000 | 23,750,000 | 1.0% | 1.00 |
| `fact_sim_swap` | `subscriber_id` | `dim_subscriber` | 250,000 | 0 | 250,000 | 19,750,000 | 1.2% | 1.00 |
| `fact_sla_breach` | `calendar_day_id` | `dim_calendar_day` | 15,000 | 0 | 30 | 0 | 100.0% | 500.00 |
| `fact_sla_breach` | `sla_id` | `dim_sla` | 15,000 | 0 | 20 | 0 | 100.0% | 750.00 |
| `fact_sla_breach` | `trouble_ticket_id` | `fact_trouble_ticket` | 10,500 | 4,500 | 10,500 | 1,189,500 | 0.9% | 1.00 |
| `fact_sms_cdr` | `calendar_day_id` | `dim_calendar_day` | 150,000,000 | 0 | 30 | 0 | 100.0% | 5,000,000.00 |
| `fact_sms_cdr` | `call_type_id` | `dim_call_type` | 150,000,000 | 0 | 12 | 0 | 100.0% | 12,500,000.00 |
| `fact_sms_cdr` | `destination_zone_id` | `dim_destination_zone` | 150,000,000 | 0 | 90 | 0 | 100.0% | 1,666,666.67 |
| `fact_sms_cdr` | `msisdn_id` | `dim_msisdn` | 150,000,000 | 0 | 10,800,000 | 16,200,000 | 40.0% | 13.89 |
| `fact_sms_cdr` | `plmn_id` | `dim_plmn` | 150,000,000 | 0 | 135 | 765 | 15.0% | 1,111,111.11 |
| `fact_sms_cdr` | `rate_plan_id` | `dim_rate_plan` | 150,000,000 | 0 | 420 | 0 | 100.0% | 357,142.86 |
| `fact_sms_cdr` | `record_type_id` | `dim_record_type` | 150,000,000 | 0 | 24 | 0 | 100.0% | 6,250,000.00 |
| `fact_sms_cdr` | `subscriber_id` | `dim_subscriber` | 150,000,000 | 0 | 8,000,000 | 12,000,000 | 40.0% | 18.75 |
| `fact_sms_cdr` | `subscription_id` | `dim_subscription` | 150,000,000 | 0 | 10,000,000 | 15,000,000 | 40.0% | 15.00 |
| `fact_subscriber_snapshot` | `calendar_day_id` | `dim_calendar_day` | 20,000,000 | 0 | 30 | 0 | 100.0% | 666,666.67 |
| `fact_subscriber_snapshot` | `credit_class_id` | `dim_credit_class` | 20,000,000 | 0 | 8 | 0 | 100.0% | 2,500,000.00 |
| `fact_subscriber_snapshot` | `market_id` | `dim_market` | 20,000,000 | 0 | 18 | 0 | 100.0% | 1,111,111.11 |
| `fact_subscriber_snapshot` | `segment_id` | `dim_segment` | 20,000,000 | 0 | 12 | 0 | 100.0% | 1,666,666.67 |
| `fact_subscriber_snapshot` | `subscriber_id` | `dim_subscriber` | 20,000,000 | 0 | 20,000,000 | 0 | 100.0% | 1.00 |
| `fact_tap_in` | `calendar_day_id` | `dim_calendar_day` | 40,000,000 | 0 | 30 | 0 | 100.0% | 1,333,333.33 |
| `fact_tap_in` | `currency_id` | `dim_currency` | 40,000,000 | 0 | 12 | 0 | 100.0% | 3,333,333.33 |
| `fact_tap_in` | `plmn_id` | `dim_plmn` | 40,000,000 | 0 | 900 | 0 | 100.0% | 44,444.44 |
| `fact_tap_in` | `record_type_id` | `dim_record_type` | 40,000,000 | 0 | 24 | 0 | 100.0% | 1,666,666.67 |
| `fact_tap_in` | `roaming_partner_id` | `dim_roaming_partner` | 40,000,000 | 0 | 640 | 0 | 100.0% | 62,500.00 |
| `fact_tap_out` | `calendar_day_id` | `dim_calendar_day` | 126,000,000 | 0 | 30 | 0 | 100.0% | 4,200,000.00 |
| `fact_tap_out` | `currency_id` | `dim_currency` | 126,000,000 | 0 | 12 | 0 | 100.0% | 10,500,000.00 |
| `fact_tap_out` | `data_cdr_id` | `fact_data_cdr` | 90,000,000 | 36,000,000 | 90,000,000 | 1,310,000,000 | 6.4% | 1.00 |
| `fact_tap_out` | `plmn_id` | `dim_plmn` | 126,000,000 | 0 | 900 | 0 | 100.0% | 140,000.00 |
| `fact_tap_out` | `record_type_id` | `dim_record_type` | 126,000,000 | 0 | 24 | 0 | 100.0% | 5,250,000.00 |
| `fact_tap_out` | `roaming_partner_id` | `dim_roaming_partner` | 126,000,000 | 0 | 640 | 0 | 100.0% | 196,875.00 |
| `fact_tap_out` | `subscription_id` | `dim_subscription` | 126,000,000 | 0 | 5,000,000 | 20,000,000 | 20.0% | 25.20 |
| `fact_tap_out` | `voice_cdr_id` | `fact_voice_cdr` | 36,000,000 | 90,000,000 | 36,000,000 | 484,000,000 | 6.9% | 1.00 |
| `fact_tax_line` | `currency_id` | `dim_currency` | 32,000,000 | 0 | 12 | 0 | 100.0% | 2,666,666.67 |
| `fact_tax_line` | `invoice_id` | `fact_invoice` | 32,000,000 | 0 | 16,000,000 | 0 | 100.0% | 2.00 |
| `fact_tax_line` | `tax_code_id` | `dim_tax_code` | 32,000,000 | 0 | 40 | 0 | 100.0% | 800,000.00 |
| `fact_tax_line` | `tax_jurisdiction_id` | `dim_tax_jurisdiction` | 32,000,000 | 0 | 60 | 0 | 100.0% | 533,333.33 |
| `fact_ticket_event` | `agent_id` | `dim_agent` | 4,800,000 | 0 | 6,000 | 0 | 100.0% | 800.00 |
| `fact_ticket_event` | `calendar_day_id` | `dim_calendar_day` | 4,800,000 | 0 | 30 | 0 | 100.0% | 160,000.00 |
| `fact_ticket_event` | `trouble_ticket_id` | `fact_trouble_ticket` | 4,800,000 | 0 | 1,200,000 | 0 | 100.0% | 4.00 |
| `fact_topup` | `calendar_day_id` | `dim_calendar_day` | 6,000,000 | 0 | 30 | 0 | 100.0% | 200,000.00 |
| `fact_topup` | `channel_id` | `dim_channel` | 6,000,000 | 0 | 8 | 0 | 100.0% | 750,000.00 |
| `fact_topup` | `currency_id` | `dim_currency` | 6,000,000 | 0 | 12 | 0 | 100.0% | 500,000.00 |
| `fact_topup` | `dealer_id` | `dim_dealer` | 2,400,000 | 3,600,000 | 1,200 | 0 | 100.0% | 2,000.00 |
| `fact_topup` | `payment_method_id` | `dim_payment_method` | 6,000,000 | 0 | 8 | 0 | 100.0% | 750,000.00 |
| `fact_topup` | `subscription_id` | `dim_subscription` | 6,000,000 | 0 | 3,000,000 | 22,000,000 | 12.0% | 2.00 |
| `fact_trouble_ticket` | `agent_id` | `dim_agent` | 1,080,000 | 120,000 | 6,000 | 0 | 100.0% | 180.00 |
| `fact_trouble_ticket` | `calendar_day_id` | `dim_calendar_day` | 1,200,000 | 0 | 30 | 0 | 100.0% | 40,000.00 |
| `fact_trouble_ticket` | `channel_id` | `dim_channel` | 1,200,000 | 0 | 8 | 0 | 100.0% | 150,000.00 |
| `fact_trouble_ticket` | `market_id` | `dim_market` | 1,200,000 | 0 | 18 | 0 | 100.0% | 66,666.67 |
| `fact_trouble_ticket` | `subscriber_id` | `dim_subscriber` | 1,200,000 | 0 | 1,000,000 | 19,000,000 | 5.0% | 1.20 |
| `fact_trouble_ticket` | `trouble_code_id` | `dim_trouble_code` | 1,200,000 | 0 | 300 | 0 | 100.0% | 4,000.00 |
| `fact_voice_cdr` | `calendar_day_id` | `dim_calendar_day` | 520,000,000 | 0 | 30 | 0 | 100.0% | 17,333,333.33 |
| `fact_voice_cdr` | `call_type_id` | `dim_call_type` | 520,000,000 | 0 | 12 | 0 | 100.0% | 43,333,333.33 |
| `fact_voice_cdr` | `cell_id` | `dim_cell` | 520,000,000 | 0 | 76,500 | 8,500 | 90.0% | 6,797.39 |
| `fact_voice_cdr` | `destination_zone_id` | `dim_destination_zone` | 520,000,000 | 0 | 90 | 0 | 100.0% | 5,777,777.78 |
| `fact_voice_cdr` | `msisdn_id` | `dim_msisdn` | 520,000,000 | 0 | 16,740,000 | 10,260,000 | 62.0% | 31.06 |
| `fact_voice_cdr` | `network_element_id` | `dim_network_element` | 520,000,000 | 0 | 12,000 | 0 | 100.0% | 43,333.33 |
| `fact_voice_cdr` | `number_prefix_id` | `dim_number_prefix` | 468,000,000 | 52,000,000 | 2,500 | 2,500 | 50.0% | 187,200.00 |
| `fact_voice_cdr` | `plmn_id` | `dim_plmn` | 520,000,000 | 0 | 225 | 675 | 25.0% | 2,311,111.11 |
| `fact_voice_cdr` | `rate_plan_id` | `dim_rate_plan` | 520,000,000 | 0 | 420 | 0 | 100.0% | 1,238,095.24 |
| `fact_voice_cdr` | `record_type_id` | `dim_record_type` | 520,000,000 | 0 | 24 | 0 | 100.0% | 21,666,666.67 |
| `fact_voice_cdr` | `release_cause_id` | `dim_release_cause` | 520,000,000 | 0 | 108 | 72 | 60.0% | 4,814,814.81 |
| `fact_voice_cdr` | `roaming_partner_id` | `dim_roaming_partner` | 41,600,000 | 478,400,000 | 224 | 416 | 35.0% | 185,714.29 |
| `fact_voice_cdr` | `subscriber_id` | `dim_subscriber` | 520,000,000 | 0 | 12,400,000 | 7,600,000 | 62.0% | 41.94 |
| `fact_voice_cdr` | `subscription_id` | `dim_subscription` | 520,000,000 | 0 | 15,500,000 | 9,500,000 | 62.0% | 33.55 |
| `fact_voice_cdr` | `technology_id` | `dim_technology` | 520,000,000 | 0 | 6 | 0 | 100.0% | 86,666,666.67 |
| `fact_voice_cdr` | `time_band_id` | `dim_time_band` | 520,000,000 | 0 | 8 | 0 | 100.0% | 65,000,000.00 |
