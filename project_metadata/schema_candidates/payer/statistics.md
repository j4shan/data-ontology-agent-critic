# Harbor Medicare Services synthetic statistics

Synthetic closed-form population for the stated window. Dimension and fact row counts are authored from the cited industry anchors and from structural fan-out (every parent required by an always-match rule has at least one child). Distinct parent keys, unmatched parents, null foreign keys, and average children per matched parent are derived from multiplicity. Optional-child match rates default to 0.93 when a join does not set one. Optional-parent coverage defaults to the full parent population when matched children can reach it, and otherwise to one child per observed parent. A stated coverage or matched-row count overrides that default. This is not a sampled extract.

Window: 30 days. Datasets: 157. Sum of fact-table rows in the window: 5,145,930,000.

## Major fact tables

These are the event and periodic-snapshot facts where high-volume data lands.

| Fact | Grain class | Rows in window | Basis |
| --- | --- | ---: | --- |
| `fact_remit_adjustment` | transaction | 630,000,000 | Authored above the remit-line population because an 835 service line can carry more than one adjustment group. Coverage of remit lines is 70 percent. |
| `fact_accumulator_snapshot` | periodic_snapshot | 544,000,000 | 68 million members times 8 accumulator types = 544 million rows. This is a periodic snapshot, not a claim. |
| `fact_remit_line` | transaction | 504,000,000 | Authored at 1.25 remit rows per adjudicated service line, on 96 percent of the 420 million service lines, grouped onto 12 million remittance advices. |
| `fact_accumulator_entry` | transaction | 420,000,000 | Authored at one ledger posting per service line, joined to 90 percent of lines. |
| `fact_claim_line` | transaction | 420,000,000 | Authored at five lines per claim header. Headers are the CMS-scale 84 million claims in the window. |
| `fact_pricing_result` | transaction | 420,000,000 | One-to-one with the 420 million service lines. |
| `fact_eligibility_inquiry` | transaction | 336,000,000 | Authored at four inquiries per claim header. The multiple is synthetic. It is not a published HETS count. |
| `fact_eligibility_response` | transaction | 336,000,000 | Equal to the inquiry population because every inquiry has one response. |
| `fact_claim_diagnosis` | transaction | 252,000,000 | Authored at three diagnoses per claim header. |
| `fact_claim_edit` | transaction | 210,000,000 | Authored at 2.5 edit results per claim header. |
| `fact_claim_status` | transaction | 168,000,000 | Authored at two status events per claim header. |
| `fact_pharmacy_claim` | transaction | 136,000,000 | Authored at two fills per member per month across 68 million members. |
| `fact_claim_header` | transaction | 84,000,000 | 84 million headers in 30 days annualize to 1.008 billion, consistent with CMS reporting more than one billion Medicare fee-for-service claims a year. |

## Join statistics for major facts

### `fact_remit_adjustment`

CAS adjustment segments land here, one row per reason on a paid or denied remit line.

Population `630,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 630,000,000 | 630,000,000 | 0 | 30 | 0 | 21,000,000.00 |
| `carc_id` | `dim_carc` | 630,000,000 | 630,000,000 | 0 | 300 | 0 | 2,100,000.00 |
| `rarc_id` | `dim_rarc` | 630,000,000 | 441,000,000 | 189,000,000 | 440 | 660 | 1,002,272.73 |
| `remit_line_id` | `fact_remit_line` | 630,000,000 | 630,000,000 | 0 | 352,800,000 | 151,200,000 | 1.79 |

#### Inbound

None in this catalog.

### `fact_accumulator_snapshot`

Month-end benefit balances land here, one row per member per accumulator type.

Population `544,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `accumulator_type_id` | `dim_accumulator_type` | 544,000,000 | 544,000,000 | 0 | 8 | 0 | 68,000,000.00 |
| `calendar_day_id` | `dim_calendar_day` | 544,000,000 | 544,000,000 | 0 | 30 | 0 | 18,133,333.33 |
| `member_id` | `dim_member` | 544,000,000 | 544,000,000 | 0 | 68,000,000 | 0 | 8.00 |
| `plan_id` | `dim_plan` | 544,000,000 | 544,000,000 | 0 | 40 | 0 | 13,600,000.00 |

#### Inbound

None in this catalog.

### `fact_remit_line`

835 service-payment lines land here. This is the payment event grain.

Population `504,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 504,000,000 | 504,000,000 | 0 | 30 | 0 | 16,800,000.00 |
| `carc_id` | `dim_carc` | 504,000,000 | 277,200,000 | 226,800,000 | 240 | 60 | 1,155,000.00 |
| `claim_header_id` | `fact_claim_header` | 504,000,000 | 504,000,000 | 0 | 82,320,000 | 1,680,000 | 6.12 |
| `claim_line_id` | `fact_claim_line` | 504,000,000 | 504,000,000 | 0 | 403,200,000 | 16,800,000 | 1.25 |
| `member_id` | `dim_member` | 504,000,000 | 504,000,000 | 0 | 54,400,000 | 13,600,000 | 9.26 |
| `provider_id` | `dim_provider` | 504,000,000 | 504,000,000 | 0 | 780,000 | 420,000 | 646.15 |
| `remit_advice_id` | `fact_remit_advice` | 504,000,000 | 504,000,000 | 0 | 12,000,000 | 0 | 42.00 |

#### Inbound

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_remit_adjustment` | `remit_line_id` | 630,000,000 | 630,000,000 | 0 | 352,800,000 | 151,200,000 | 1.79 |

### `fact_accumulator_entry`

Adjudication postings to deductibles and out-of-pocket accumulators land here.

Population `420,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `accumulator_type_id` | `dim_accumulator_type` | 420,000,000 | 420,000,000 | 0 | 8 | 0 | 52,500,000.00 |
| `calendar_day_id` | `dim_calendar_day` | 420,000,000 | 420,000,000 | 0 | 30 | 0 | 14,000,000.00 |
| `claim_line_id` | `fact_claim_line` | 420,000,000 | 420,000,000 | 0 | 378,000,000 | 42,000,000 | 1.11 |
| `member_id` | `dim_member` | 420,000,000 | 420,000,000 | 0 | 54,400,000 | 13,600,000 | 7.72 |
| `plan_id` | `dim_plan` | 420,000,000 | 420,000,000 | 0 | 40 | 0 | 10,500,000.00 |

#### Inbound

None in this catalog.

### `fact_claim_line`

837 service lines are the atomic medical-claim landing zone.

Population `420,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `claim_header_id` | `fact_claim_header` | 420,000,000 | 420,000,000 | 0 | 84,000,000 | 0 | 5.00 |
| `diagnosis_id` | `dim_diagnosis` | 420,000,000 | 294,000,000 | 126,000,000 | 18,000 | 54,000 | 16,333.33 |
| `facility_id` | `dim_facility` | 420,000,000 | 176,400,000 | 243,600,000 | 180,000 | 0 | 980.00 |
| `fee_schedule_id` | `dim_fee_schedule` | 420,000,000 | 336,000,000 | 84,000,000 | 80 | 0 | 4,200,000.00 |
| `insurance_line_id` | `dim_insurance_line` | 420,000,000 | 420,000,000 | 0 | 6 | 0 | 70,000,000.00 |
| `member_id` | `dim_member` | 420,000,000 | 420,000,000 | 0 | 54,400,000 | 13,600,000 | 7.72 |
| `modifier_id` | `dim_modifier` | 420,000,000 | 147,000,000 | 273,000,000 | 200 | 200 | 735,000.00 |
| `ndc_id` | `dim_ndc` | 420,000,000 | 33,600,000 | 386,400,000 | 7,500 | 42,500 | 4,480.00 |
| `place_of_service_id` | `dim_place_of_service` | 420,000,000 | 420,000,000 | 0 | 50 | 0 | 8,400,000.00 |
| `plan_id` | `dim_plan` | 420,000,000 | 420,000,000 | 0 | 40 | 0 | 10,500,000.00 |
| `procedure_id` | `dim_procedure` | 420,000,000 | 420,000,000 | 0 | 4,800 | 7,200 | 87,500.00 |
| `rendering_provider_id` | `dim_provider` | 420,000,000 | 420,000,000 | 0 | 660,000 | 540,000 | 636.36 |
| `revenue_code_id` | `dim_revenue_code` | 420,000,000 | 176,400,000 | 243,600,000 | 300 | 200 | 588,000.00 |
| `service_day_id` | `dim_calendar_day` | 420,000,000 | 420,000,000 | 0 | 30 | 0 | 14,000,000.00 |

#### Inbound

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_remit_line` | `claim_line_id` | 504,000,000 | 504,000,000 | 0 | 403,200,000 | 16,800,000 | 1.25 |
| `fact_accumulator_entry` | `claim_line_id` | 420,000,000 | 420,000,000 | 0 | 378,000,000 | 42,000,000 | 1.11 |
| `fact_pricing_result` | `claim_line_id` | 420,000,000 | 420,000,000 | 0 | 420,000,000 | 0 | 1.00 |
| `fact_claim_edit` | `claim_line_id` | 210,000,000 | 168,000,000 | 42,000,000 | 168,000,000 | 252,000,000 | 1.00 |
| `fact_cob_line` | `claim_line_id` | 36,000,000 | 36,000,000 | 0 | 33,600,000 | 386,400,000 | 1.07 |
| `fact_medical_review` | `claim_line_id` | 900,000 | 900,000 | 0 | 840,000 | 419,160,000 | 1.07 |

### `fact_pricing_result`

Fee-schedule pricing results land here, one per service line.

Population `420,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 420,000,000 | 420,000,000 | 0 | 30 | 0 | 14,000,000.00 |
| `claim_line_id` | `fact_claim_line` | 420,000,000 | 420,000,000 | 0 | 420,000,000 | 0 | 1.00 |
| `fee_schedule_id` | `dim_fee_schedule` | 420,000,000 | 420,000,000 | 0 | 80 | 0 | 5,250,000.00 |
| `locality_id` | `dim_locality` | 420,000,000 | 420,000,000 | 0 | 120 | 0 | 3,500,000.00 |
| `procedure_id` | `dim_procedure` | 420,000,000 | 420,000,000 | 0 | 4,800 | 7,200 | 87,500.00 |

#### Inbound

None in this catalog.

### `fact_eligibility_inquiry`

X12 270 eligibility inquiries land here.

Population `336,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 336,000,000 | 336,000,000 | 0 | 30 | 0 | 11,200,000.00 |
| `coverage_id` | `dim_coverage` | 336,000,000 | 336,000,000 | 0 | 61,200,000 | 10,800,000 | 5.49 |
| `jurisdiction_id` | `dim_jurisdiction` | 336,000,000 | 336,000,000 | 0 | 12 | 0 | 28,000,000.00 |
| `member_id` | `dim_member` | 336,000,000 | 336,000,000 | 0 | 61,200,000 | 6,800,000 | 5.49 |
| `plan_id` | `dim_plan` | 336,000,000 | 336,000,000 | 0 | 40 | 0 | 8,400,000.00 |
| `provider_id` | `dim_provider` | 336,000,000 | 336,000,000 | 0 | 600,000 | 600,000 | 560.00 |
| `trading_partner_id` | `dim_trading_partner` | 336,000,000 | 336,000,000 | 0 | 80 | 0 | 4,200,000.00 |

#### Inbound

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_eligibility_response` | `eligibility_inquiry_id` | 336,000,000 | 336,000,000 | 0 | 336,000,000 | 0 | 1.00 |

### `fact_eligibility_response`

X12 271 eligibility responses land here, one per inquiry.

Population `336,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 336,000,000 | 336,000,000 | 0 | 30 | 0 | 11,200,000.00 |
| `eligibility_inquiry_id` | `fact_eligibility_inquiry` | 336,000,000 | 336,000,000 | 0 | 336,000,000 | 0 | 1.00 |
| `member_id` | `dim_member` | 336,000,000 | 336,000,000 | 0 | 61,200,000 | 6,800,000 | 5.49 |
| `plan_id` | `dim_plan` | 336,000,000 | 336,000,000 | 0 | 40 | 0 | 8,400,000.00 |

#### Inbound

None in this catalog.

### `fact_claim_diagnosis`

Claim diagnosis rows land here for reporting and risk inputs.

Population `252,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 252,000,000 | 252,000,000 | 0 | 30 | 0 | 8,400,000.00 |
| `claim_header_id` | `fact_claim_header` | 252,000,000 | 252,000,000 | 0 | 84,000,000 | 0 | 3.00 |
| `diagnosis_id` | `dim_diagnosis` | 252,000,000 | 252,000,000 | 0 | 25,200 | 46,800 | 10,000.00 |

#### Inbound

None in this catalog.

### `fact_claim_edit`

Pre-adjudication edit results land here.

Population `210,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 210,000,000 | 210,000,000 | 0 | 30 | 0 | 7,000,000.00 |
| `claim_header_id` | `fact_claim_header` | 210,000,000 | 210,000,000 | 0 | 84,000,000 | 0 | 2.50 |
| `claim_line_id` | `fact_claim_line` | 210,000,000 | 168,000,000 | 42,000,000 | 168,000,000 | 252,000,000 | 1.00 |
| `edit_code_id` | `dim_edit_code` | 210,000,000 | 210,000,000 | 0 | 1,125 | 375 | 186,666.67 |

#### Inbound

None in this catalog.

### `fact_claim_status`

Claim-status events land here as the header moves through receipt, acceptance, and finalization.

Population `168,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 168,000,000 | 168,000,000 | 0 | 30 | 0 | 5,600,000.00 |
| `claim_header_id` | `fact_claim_header` | 168,000,000 | 168,000,000 | 0 | 84,000,000 | 0 | 2.00 |
| `submitter_id` | `dim_submitter` | 168,000,000 | 168,000,000 | 0 | 2,500 | 0 | 67,200.00 |
| `trading_partner_id` | `dim_trading_partner` | 168,000,000 | 168,000,000 | 0 | 80 | 0 | 2,100,000.00 |

#### Inbound

None in this catalog.

### `fact_pharmacy_claim`

NCPDP pharmacy claims land here, separate from 837 service lines.

Population `136,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `calendar_day_id` | `dim_calendar_day` | 136,000,000 | 136,000,000 | 0 | 30 | 0 | 4,533,333.33 |
| `formulary_id` | `dim_formulary` | 136,000,000 | 108,800,000 | 27,200,000 | 30 | 0 | 3,626,666.67 |
| `insurance_line_id` | `dim_insurance_line` | 136,000,000 | 136,000,000 | 0 | 6 | 0 | 22,666,666.67 |
| `member_id` | `dim_member` | 136,000,000 | 136,000,000 | 0 | 30,600,000 | 37,400,000 | 4.44 |
| `ndc_id` | `dim_ndc` | 136,000,000 | 136,000,000 | 0 | 12,500 | 37,500 | 10,880.00 |
| `pharmacy_id` | `dim_pharmacy` | 136,000,000 | 136,000,000 | 0 | 55,200 | 4,800 | 2,463.77 |
| `plan_id` | `dim_plan` | 136,000,000 | 136,000,000 | 0 | 40 | 0 | 3,400,000.00 |
| `prescriber_id` | `dim_prescriber` | 136,000,000 | 136,000,000 | 0 | 240,000 | 160,000 | 566.67 |
| `tier_id` | `dim_tier` | 136,000,000 | 136,000,000 | 0 | 6 | 0 | 22,666,666.67 |

#### Inbound

None in this catalog.

### `fact_claim_header`

837 claim headers land here. Volume concentrates on the lines, but the header is the claim grain those lines require.

Population `84,000,000` rows. Outbound joins are foreign keys on this fact. Inbound joins are other datasets that reference this fact.

#### Outbound

| Column | Universe dataset | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `bill_type_id` | `dim_bill_type` | 84,000,000 | 35,280,000 | 48,720,000 | 70 | 30 | 504,000.00 |
| `billing_provider_id` | `dim_provider` | 84,000,000 | 84,000,000 | 0 | 840,000 | 360,000 | 100.00 |
| `calendar_day_id` | `dim_calendar_day` | 84,000,000 | 84,000,000 | 0 | 30 | 0 | 2,800,000.00 |
| `claim_frequency_id` | `dim_claim_frequency` | 84,000,000 | 84,000,000 | 0 | 8 | 0 | 10,500,000.00 |
| `coverage_id` | `dim_coverage` | 84,000,000 | 84,000,000 | 0 | 54,000,000 | 18,000,000 | 1.56 |
| `drg_id` | `dim_drg` | 84,000,000 | 10,080,000 | 73,920,000 | 480 | 320 | 21,000.00 |
| `edi_batch_id` | `fact_edi_batch` | 84,000,000 | 84,000,000 | 0 | 900,000 | 0 | 93.33 |
| `facility_id` | `dim_facility` | 84,000,000 | 35,280,000 | 48,720,000 | 144,000 | 36,000 | 245.00 |
| `filing_indicator_id` | `dim_filing_indicator` | 84,000,000 | 84,000,000 | 0 | 12 | 0 | 7,000,000.00 |
| `insurance_line_id` | `dim_insurance_line` | 84,000,000 | 84,000,000 | 0 | 6 | 0 | 14,000,000.00 |
| `jurisdiction_id` | `dim_jurisdiction` | 84,000,000 | 84,000,000 | 0 | 12 | 0 | 7,000,000.00 |
| `legal_entity_id` | `dim_legal_entity` | 84,000,000 | 84,000,000 | 0 | 4 | 0 | 21,000,000.00 |
| `member_id` | `dim_member` | 84,000,000 | 84,000,000 | 0 | 54,400,000 | 13,600,000 | 1.54 |
| `place_of_service_id` | `dim_place_of_service` | 84,000,000 | 84,000,000 | 0 | 50 | 0 | 1,680,000.00 |
| `plan_id` | `dim_plan` | 84,000,000 | 84,000,000 | 0 | 40 | 0 | 2,100,000.00 |
| `principal_diagnosis_id` | `dim_diagnosis` | 84,000,000 | 84,000,000 | 0 | 28,800 | 43,200 | 2,916.67 |
| `submitter_id` | `dim_submitter` | 84,000,000 | 84,000,000 | 0 | 2,500 | 0 | 33,600.00 |
| `trading_partner_id` | `dim_trading_partner` | 84,000,000 | 84,000,000 | 0 | 80 | 0 | 1,050,000.00 |

#### Inbound

| Child dataset | Column | Child rows | Matched children | Null children | Distinct parent keys | Unmatched parents | Avg children per matched parent |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `fact_remit_line` | `claim_header_id` | 504,000,000 | 504,000,000 | 0 | 82,320,000 | 1,680,000 | 6.12 |
| `fact_claim_line` | `claim_header_id` | 420,000,000 | 420,000,000 | 0 | 84,000,000 | 0 | 5.00 |
| `fact_claim_diagnosis` | `claim_header_id` | 252,000,000 | 252,000,000 | 0 | 84,000,000 | 0 | 3.00 |
| `fact_claim_edit` | `claim_header_id` | 210,000,000 | 210,000,000 | 0 | 84,000,000 | 0 | 2.50 |
| `fact_claim_status` | `claim_header_id` | 168,000,000 | 168,000,000 | 0 | 84,000,000 | 0 | 2.00 |
| `fact_claim_admission` | `claim_header_id` | 15,120,000 | 15,120,000 | 0 | 15,120,000 | 68,880,000 | 1.00 |
| `fact_claim_note` | `claim_header_id` | 10,000,000 | 10,000,000 | 0 | 6,720,000 | 77,280,000 | 1.49 |
| `fact_attachment` | `claim_header_id` | 2,500,000 | 2,500,000 | 0 | 1,680,000 | 82,320,000 | 1.49 |
| `fact_overpayment` | `claim_header_id` | 400,000 | 400,000 | 0 | 400,000 | 83,600,000 | 1.00 |
| `fact_interest_payment` | `claim_header_id` | 200,000 | 200,000 | 0 | 200,000 | 83,800,000 | 1.00 |
| `fact_appeal` | `claim_header_id` | 180,000 | 180,000 | 0 | 180,000 | 83,820,000 | 1.00 |
| `fact_audit_sample` | `claim_header_id` | 50,000 | 50,000 | 0 | 50,000 | 83,950,000 | 1.00 |

## Dataset populations

| Dataset | Role | Volume class | Rows |
| --- | --- | --- | ---: |
| `fact_remit_adjustment` | fact | transaction | 630,000,000 |
| `fact_accumulator_snapshot` | fact | periodic_snapshot | 544,000,000 |
| `fact_remit_line` | fact | transaction | 504,000,000 |
| `fact_accumulator_entry` | fact | transaction | 420,000,000 |
| `fact_claim_line` | fact | transaction | 420,000,000 |
| `fact_pricing_result` | fact | transaction | 420,000,000 |
| `fact_eligibility_inquiry` | fact | transaction | 336,000,000 |
| `fact_eligibility_response` | fact | transaction | 336,000,000 |
| `fact_claim_diagnosis` | fact | transaction | 252,000,000 |
| `fact_claim_edit` | fact | transaction | 210,000,000 |
| `fact_claim_status` | fact | transaction | 168,000,000 |
| `fact_pharmacy_claim` | fact | transaction | 136,000,000 |
| `fact_hcc_diagnosis` | fact | transaction | 96,000,000 |
| `fact_claim_header` | fact | transaction | 84,000,000 |
| `dim_coverage` | dimension | — | 72,000,000 |
| `fact_enrollment_span` | fact | accumulating_snapshot | 72,000,000 |
| `dim_address` | dimension | — | 70,000,000 |
| `bridge_member_address` | bridge | — | 68,000,000 |
| `bridge_member_language` | bridge | — | 68,000,000 |
| `dim_member` | dimension | — | 68,000,000 |
| `fact_pcp_attribution` | fact | periodic_snapshot | 68,000,000 |
| `fact_premium_bill` | fact | periodic_snapshot | 68,000,000 |
| `fact_risk_score` | fact | periodic_snapshot | 68,000,000 |
| `fact_premium_payment` | fact | transaction | 60,000,000 |
| `fact_encounter` | fact | transaction | 50,000,000 |
| `fact_portal_event` | fact | transaction | 45,000,000 |
| `fact_cob_line` | fact | transaction | 36,000,000 |
| `fact_call_event` | fact | transaction | 24,000,000 |
| `fact_claim_admission` | fact | transaction | 15,120,000 |
| `fact_provider_payment` | fact | transaction | 12,000,000 |
| `fact_remit_advice` | fact | transaction | 12,000,000 |
| `fact_claim_note` | fact | transaction | 10,000,000 |
| `fact_call` | fact | transaction | 8,000,000 |
| `fact_capitation` | fact | transaction | 8,000,000 |
| `fact_auth_line` | fact | transaction | 6,000,000 |
| `fact_low_income_subsidy` | fact | transaction | 6,000,000 |
| `fact_letter` | fact | transaction | 5,000,000 |
| `bridge_coverage_rider` | bridge | — | 4,000,000 |
| `fact_attachment` | fact | transaction | 2,500,000 |
| `fact_auth_decision` | fact | transaction | 2,400,000 |
| `fact_prior_auth` | fact | transaction | 2,400,000 |
| `bridge_cob_coverage` | bridge | — | 2,000,000 |
| `bridge_provider_network` | bridge | — | 2,000,000 |
| `fact_fee_schedule_rate` | fact | transaction | 2,000,000 |
| `bridge_provider_specialty` | bridge | — | 1,500,000 |
| `dim_provider` | dimension | — | 1,200,000 |
| `fact_disenrollment` | fact | transaction | 1,200,000 |
| `fact_referral` | fact | transaction | 1,100,000 |
| `fact_referral_target` | fact | transaction | 1,100,000 |
| `fact_edi_batch` | fact | transaction | 900,000 |
| `fact_medical_review` | fact | transaction | 900,000 |
| `fact_premium_adjustment` | fact | transaction | 800,000 |
| `bridge_formulary_drug` | bridge | — | 400,000 |
| `bridge_prescriber_specialty` | bridge | — | 400,000 |
| `dim_prescriber` | dimension | — | 400,000 |
| `fact_overpayment` | fact | transaction | 400,000 |
| `bridge_provider_facility` | bridge | — | 250,000 |
| `fact_recovery` | fact | transaction | 250,000 |
| `bridge_facility_network` | bridge | — | 200,000 |
| `fact_interest_payment` | fact | transaction | 200,000 |
| `bridge_facility_taxonomy` | bridge | — | 180,000 |
| `dim_facility` | dimension | — | 180,000 |
| `fact_appeal` | fact | transaction | 180,000 |
| `fact_appeal_decision` | fact | transaction | 150,000 |
| `fact_withhold` | fact | transaction | 100,000 |
| `fact_grievance` | fact | transaction | 90,000 |
| `bridge_diagnosis_hcc` | bridge | — | 80,000 |
| `bridge_pharmacy_network` | bridge | — | 80,000 |
| `dim_diagnosis` | dimension | — | 72,000 |
| `dim_pharmacy` | dimension | — | 60,000 |
| `dim_ndc` | dimension | — | 50,000 |
| `fact_audit_sample` | fact | transaction | 50,000 |
| `fact_provider_enrollment` | fact | transaction | 40,000 |
| `fact_fraud_lead` | fact | transaction | 30,000 |
| `bridge_group_benefit` | bridge | — | 20,000 |
| `fact_revalidation` | fact | transaction | 20,000 |
| `bridge_employee_jurisdiction` | bridge | — | 15,000 |
| `dim_employee` | dimension | — | 15,000 |
| `bridge_procedure_category` | bridge | — | 12,000 |
| `dim_procedure` | dimension | — | 12,000 |
| `bridge_revenue_procedure` | bridge | — | 8,000 |
| `dim_group` | dimension | — | 8,000 |
| `bridge_drg_diagnosis` | bridge | — | 5,000 |
| `dim_agent` | dimension | — | 4,000 |
| `dim_submitter` | dimension | — | 2,500 |
| `bridge_edit_line` | bridge | — | 1,500 |
| `dim_edit_code` | dimension | — | 1,500 |
| `dim_rarc` | dimension | — | 1,100 |
| `bridge_plan_category` | bridge | — | 800 |
| `dim_drg` | dimension | — | 800 |
| `dim_taxonomy` | dimension | — | 800 |
| `bridge_plan_benefit` | bridge | — | 600 |
| `dim_benefit` | dimension | — | 600 |
| `dim_gl_account` | dimension | — | 600 |
| `dim_revenue_code` | dimension | — | 500 |
| `dim_drug_class` | dimension | — | 400 |
| `dim_modifier` | dimension | — | 400 |
| `dim_carc` | dimension | — | 300 |
| `bridge_state_locality` | bridge | — | 200 |
| `dim_denial_reason` | dimension | — | 200 |
| `dim_hcc` | dimension | — | 200 |
| `dim_cost_center` | dimension | — | 180 |
| `dim_specialty` | dimension | — | 180 |
| `bridge_contract_plan` | bridge | — | 120 |
| `dim_condition_code` | dimension | — | 120 |
| `dim_contract` | dimension | — | 120 |
| `dim_locality` | dimension | — | 120 |
| `dim_bill_type` | dimension | — | 100 |
| `bridge_network_plan` | bridge | — | 80 |
| `dim_fee_schedule` | dimension | — | 80 |
| `dim_occurrence_code` | dimension | — | 80 |
| `dim_service_category` | dimension | — | 80 |
| `dim_trading_partner` | dimension | — | 80 |
| `bridge_jurisdiction_state` | bridge | — | 60 |
| `dim_department` | dimension | — | 60 |
| `dim_value_code` | dimension | — | 60 |
| `dim_state` | dimension | — | 51 |
| `dim_place_of_service` | dimension | — | 50 |
| `bridge_plan_formulary` | bridge | — | 40 |
| `dim_discharge_status` | dimension | — | 40 |
| `dim_fraud_scheme` | dimension | — | 40 |
| `dim_plan` | dimension | — | 40 |
| `dim_premium_schedule` | dimension | — | 40 |
| `dim_calendar_day` | dimension | — | 30 |
| `dim_formulary` | dimension | — | 30 |
| `dim_patient_status` | dimension | — | 30 |
| `dim_network` | dimension | — | 25 |
| `dim_call_queue` | dimension | — | 20 |
| `dim_language` | dimension | — | 20 |
| `dim_auth_type` | dimension | — | 15 |
| `dim_bank` | dimension | — | 15 |
| `dim_note_type` | dimension | — | 15 |
| `dim_filing_indicator` | dimension | — | 12 |
| `dim_jurisdiction` | dimension | — | 12 |
| `dim_relation` | dimension | — | 12 |
| `dim_admission_type` | dimension | — | 10 |
| `dim_document_type` | dimension | — | 10 |
| `dim_withhold_reason` | dimension | — | 10 |
| `dim_accumulator_type` | dimension | — | 8 |
| `dim_audit_program` | dimension | — | 8 |
| `dim_claim_frequency` | dimension | — | 8 |
| `dim_interest_reason` | dimension | — | 8 |
| `dim_review_type` | dimension | — | 8 |
| `dim_cob_type` | dimension | — | 6 |
| `dim_enrollment_status` | dimension | — | 6 |
| `dim_insurance_line` | dimension | — | 6 |
| `dim_payment_method` | dimension | — | 6 |
| `dim_tier` | dimension | — | 6 |
| `dim_appeal_level` | dimension | — | 5 |
| `dim_lis_level` | dimension | — | 5 |
| `dim_currency` | dimension | — | 4 |
| `dim_gender` | dimension | — | 4 |
| `dim_legal_entity` | dimension | — | 4 |
| `dim_lob` | dimension | — | 4 |
| `dim_risk_model` | dimension | — | 4 |
| `dim_accounting_period` | dimension | — | 1 |
| `dim_enterprise` | dimension | — | 1 |

## All joins

| Child | Column | Parent | Matched children | Null children | Distinct parent keys | Unmatched parents | Parent coverage | Avg children per matched parent |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `bridge_cob_coverage` | `cob_type_id` | `dim_cob_type` | 2,000,000 | 0 | 6 | 0 | 100.0% | 333,333.33 |
| `bridge_cob_coverage` | `coverage_id` | `dim_coverage` | 2,000,000 | 0 | 1,440,000 | 70,560,000 | 2.0% | 1.39 |
| `bridge_contract_plan` | `contract_id` | `dim_contract` | 120 | 0 | 120 | 0 | 100.0% | 1.00 |
| `bridge_contract_plan` | `plan_id` | `dim_plan` | 120 | 0 | 40 | 0 | 100.0% | 3.00 |
| `bridge_coverage_rider` | `benefit_id` | `dim_benefit` | 4,000,000 | 0 | 600 | 0 | 100.0% | 6,666.67 |
| `bridge_coverage_rider` | `coverage_id` | `dim_coverage` | 4,000,000 | 0 | 3,600,000 | 68,400,000 | 5.0% | 1.11 |
| `bridge_diagnosis_hcc` | `diagnosis_id` | `dim_diagnosis` | 80,000 | 0 | 28,800 | 43,200 | 40.0% | 2.78 |
| `bridge_diagnosis_hcc` | `hcc_id` | `dim_hcc` | 80,000 | 0 | 200 | 0 | 100.0% | 400.00 |
| `bridge_drg_diagnosis` | `diagnosis_id` | `dim_diagnosis` | 5,000 | 0 | 5,000 | 67,000 | 6.9% | 1.00 |
| `bridge_drg_diagnosis` | `drg_id` | `dim_drg` | 5,000 | 0 | 800 | 0 | 100.0% | 6.25 |
| `bridge_edit_line` | `edit_code_id` | `dim_edit_code` | 1,500 | 0 | 1,500 | 0 | 100.0% | 1.00 |
| `bridge_edit_line` | `insurance_line_id` | `dim_insurance_line` | 1,500 | 0 | 6 | 0 | 100.0% | 250.00 |
| `bridge_employee_jurisdiction` | `employee_id` | `dim_employee` | 15,000 | 0 | 15,000 | 0 | 100.0% | 1.00 |
| `bridge_employee_jurisdiction` | `jurisdiction_id` | `dim_jurisdiction` | 15,000 | 0 | 12 | 0 | 100.0% | 1,250.00 |
| `bridge_facility_network` | `facility_id` | `dim_facility` | 200,000 | 0 | 180,000 | 0 | 100.0% | 1.11 |
| `bridge_facility_network` | `network_id` | `dim_network` | 200,000 | 0 | 25 | 0 | 100.0% | 8,000.00 |
| `bridge_facility_taxonomy` | `facility_id` | `dim_facility` | 180,000 | 0 | 180,000 | 0 | 100.0% | 1.00 |
| `bridge_facility_taxonomy` | `taxonomy_id` | `dim_taxonomy` | 180,000 | 0 | 800 | 0 | 100.0% | 225.00 |
| `bridge_formulary_drug` | `formulary_id` | `dim_formulary` | 400,000 | 0 | 30 | 0 | 100.0% | 13,333.33 |
| `bridge_formulary_drug` | `ndc_id` | `dim_ndc` | 400,000 | 0 | 25,000 | 25,000 | 50.0% | 16.00 |
| `bridge_formulary_drug` | `tier_id` | `dim_tier` | 400,000 | 0 | 6 | 0 | 100.0% | 66,666.67 |
| `bridge_group_benefit` | `benefit_id` | `dim_benefit` | 20,000 | 0 | 600 | 0 | 100.0% | 33.33 |
| `bridge_group_benefit` | `group_id` | `dim_group` | 20,000 | 0 | 8,000 | 0 | 100.0% | 2.50 |
| `bridge_jurisdiction_state` | `jurisdiction_id` | `dim_jurisdiction` | 60 | 0 | 12 | 0 | 100.0% | 5.00 |
| `bridge_jurisdiction_state` | `state_id` | `dim_state` | 60 | 0 | 51 | 0 | 100.0% | 1.18 |
| `bridge_member_address` | `address_id` | `dim_address` | 68,000,000 | 0 | 68,000,000 | 2,000,000 | 97.1% | 1.00 |
| `bridge_member_address` | `member_id` | `dim_member` | 68,000,000 | 0 | 68,000,000 | 0 | 100.0% | 1.00 |
| `bridge_member_language` | `language_id` | `dim_language` | 68,000,000 | 0 | 20 | 0 | 100.0% | 3,400,000.00 |
| `bridge_member_language` | `member_id` | `dim_member` | 68,000,000 | 0 | 68,000,000 | 0 | 100.0% | 1.00 |
| `bridge_network_plan` | `network_id` | `dim_network` | 80 | 0 | 25 | 0 | 100.0% | 3.20 |
| `bridge_network_plan` | `plan_id` | `dim_plan` | 80 | 0 | 40 | 0 | 100.0% | 2.00 |
| `bridge_pharmacy_network` | `network_id` | `dim_network` | 80,000 | 0 | 25 | 0 | 100.0% | 3,200.00 |
| `bridge_pharmacy_network` | `pharmacy_id` | `dim_pharmacy` | 80,000 | 0 | 60,000 | 0 | 100.0% | 1.33 |
| `bridge_plan_benefit` | `benefit_id` | `dim_benefit` | 600 | 0 | 600 | 0 | 100.0% | 1.00 |
| `bridge_plan_benefit` | `plan_id` | `dim_plan` | 600 | 0 | 40 | 0 | 100.0% | 15.00 |
| `bridge_plan_category` | `plan_id` | `dim_plan` | 800 | 0 | 40 | 0 | 100.0% | 20.00 |
| `bridge_plan_category` | `service_category_id` | `dim_service_category` | 800 | 0 | 80 | 0 | 100.0% | 10.00 |
| `bridge_plan_formulary` | `formulary_id` | `dim_formulary` | 40 | 0 | 30 | 0 | 100.0% | 1.33 |
| `bridge_plan_formulary` | `plan_id` | `dim_plan` | 40 | 0 | 40 | 0 | 100.0% | 1.00 |
| `bridge_prescriber_specialty` | `prescriber_id` | `dim_prescriber` | 400,000 | 0 | 400,000 | 0 | 100.0% | 1.00 |
| `bridge_prescriber_specialty` | `specialty_id` | `dim_specialty` | 400,000 | 0 | 180 | 0 | 100.0% | 2,222.22 |
| `bridge_procedure_category` | `procedure_id` | `dim_procedure` | 12,000 | 0 | 12,000 | 0 | 100.0% | 1.00 |
| `bridge_procedure_category` | `service_category_id` | `dim_service_category` | 12,000 | 0 | 80 | 0 | 100.0% | 150.00 |
| `bridge_provider_facility` | `facility_id` | `dim_facility` | 250,000 | 0 | 180,000 | 0 | 100.0% | 1.39 |
| `bridge_provider_facility` | `provider_id` | `dim_provider` | 250,000 | 0 | 180,000 | 1,020,000 | 15.0% | 1.39 |
| `bridge_provider_network` | `network_id` | `dim_network` | 2,000,000 | 0 | 25 | 0 | 100.0% | 80,000.00 |
| `bridge_provider_network` | `provider_id` | `dim_provider` | 2,000,000 | 0 | 960,000 | 240,000 | 80.0% | 2.08 |
| `bridge_provider_specialty` | `provider_id` | `dim_provider` | 1,500,000 | 0 | 1,080,000 | 120,000 | 90.0% | 1.39 |
| `bridge_provider_specialty` | `specialty_id` | `dim_specialty` | 1,500,000 | 0 | 180 | 0 | 100.0% | 8,333.33 |
| `bridge_revenue_procedure` | `procedure_id` | `dim_procedure` | 8,000 | 0 | 8,000 | 4,000 | 66.7% | 1.00 |
| `bridge_revenue_procedure` | `revenue_code_id` | `dim_revenue_code` | 8,000 | 0 | 500 | 0 | 100.0% | 16.00 |
| `bridge_state_locality` | `locality_id` | `dim_locality` | 200 | 0 | 120 | 0 | 100.0% | 1.67 |
| `bridge_state_locality` | `state_id` | `dim_state` | 200 | 0 | 51 | 0 | 100.0% | 3.92 |
| `dim_address` | `state_id` | `dim_state` | 70,000,000 | 0 | 51 | 0 | 100.0% | 1,372,549.02 |
| `dim_agent` | `call_queue_id` | `dim_call_queue` | 4,000 | 0 | 20 | 0 | 100.0% | 200.00 |
| `dim_agent` | `employee_id` | `dim_employee` | 4,000 | 0 | 4,000 | 11,000 | 26.7% | 1.00 |
| `dim_benefit` | `plan_id` | `dim_plan` | 600 | 0 | 40 | 0 | 100.0% | 15.00 |
| `dim_contract` | `legal_entity_id` | `dim_legal_entity` | 120 | 0 | 4 | 0 | 100.0% | 30.00 |
| `dim_contract` | `plan_id` | `dim_plan` | 120 | 0 | 40 | 0 | 100.0% | 3.00 |
| `dim_cost_center` | `department_id` | `dim_department` | 180 | 0 | 60 | 0 | 100.0% | 3.00 |
| `dim_coverage` | `group_id` | `dim_group` | 10,800,000 | 61,200,000 | 8,000 | 0 | 100.0% | 1,350.00 |
| `dim_coverage` | `legal_entity_id` | `dim_legal_entity` | 72,000,000 | 0 | 4 | 0 | 100.0% | 18,000,000.00 |
| `dim_coverage` | `member_id` | `dim_member` | 72,000,000 | 0 | 68,000,000 | 0 | 100.0% | 1.06 |
| `dim_coverage` | `plan_id` | `dim_plan` | 72,000,000 | 0 | 40 | 0 | 100.0% | 1,800,000.00 |
| `dim_department` | `legal_entity_id` | `dim_legal_entity` | 60 | 0 | 4 | 0 | 100.0% | 15.00 |
| `dim_employee` | `cost_center_id` | `dim_cost_center` | 15,000 | 0 | 180 | 0 | 100.0% | 83.33 |
| `dim_employee` | `department_id` | `dim_department` | 15,000 | 0 | 60 | 0 | 100.0% | 250.00 |
| `dim_employee` | `jurisdiction_id` | `dim_jurisdiction` | 15,000 | 0 | 12 | 0 | 100.0% | 1,250.00 |
| `dim_facility` | `provider_id` | `dim_provider` | 162,000 | 18,000 | 162,000 | 1,038,000 | 13.5% | 1.00 |
| `dim_facility` | `state_id` | `dim_state` | 180,000 | 0 | 51 | 0 | 100.0% | 3,529.41 |
| `dim_fee_schedule` | `jurisdiction_id` | `dim_jurisdiction` | 80 | 0 | 12 | 0 | 100.0% | 6.67 |
| `dim_formulary` | `plan_id` | `dim_plan` | 30 | 0 | 30 | 10 | 75.0% | 1.00 |
| `dim_gl_account` | `legal_entity_id` | `dim_legal_entity` | 600 | 0 | 4 | 0 | 100.0% | 150.00 |
| `dim_group` | `plan_id` | `dim_plan` | 8,000 | 0 | 40 | 0 | 100.0% | 200.00 |
| `dim_hcc` | `risk_model_id` | `dim_risk_model` | 200 | 0 | 4 | 0 | 100.0% | 50.00 |
| `dim_jurisdiction` | `legal_entity_id` | `dim_legal_entity` | 12 | 0 | 4 | 0 | 100.0% | 3.00 |
| `dim_legal_entity` | `enterprise_id` | `dim_enterprise` | 4 | 0 | 1 | 0 | 100.0% | 4.00 |
| `dim_locality` | `state_id` | `dim_state` | 120 | 0 | 51 | 0 | 100.0% | 2.35 |
| `dim_member` | `gender_id` | `dim_gender` | 68,000,000 | 0 | 4 | 0 | 100.0% | 17,000,000.00 |
| `dim_member` | `jurisdiction_id` | `dim_jurisdiction` | 68,000,000 | 0 | 12 | 0 | 100.0% | 5,666,666.67 |
| `dim_member` | `language_id` | `dim_language` | 68,000,000 | 0 | 20 | 0 | 100.0% | 3,400,000.00 |
| `dim_member` | `state_id` | `dim_state` | 68,000,000 | 0 | 51 | 0 | 100.0% | 1,333,333.33 |
| `dim_ndc` | `drug_class_id` | `dim_drug_class` | 50,000 | 0 | 400 | 0 | 100.0% | 125.00 |
| `dim_pharmacy` | `network_id` | `dim_network` | 60,000 | 0 | 25 | 0 | 100.0% | 2,400.00 |
| `dim_pharmacy` | `state_id` | `dim_state` | 60,000 | 0 | 51 | 0 | 100.0% | 1,176.47 |
| `dim_plan` | `jurisdiction_id` | `dim_jurisdiction` | 40 | 0 | 12 | 0 | 100.0% | 3.33 |
| `dim_plan` | `legal_entity_id` | `dim_legal_entity` | 40 | 0 | 4 | 0 | 100.0% | 10.00 |
| `dim_plan` | `lob_id` | `dim_lob` | 40 | 0 | 4 | 0 | 100.0% | 10.00 |
| `dim_premium_schedule` | `plan_id` | `dim_plan` | 40 | 0 | 40 | 0 | 100.0% | 1.00 |
| `dim_prescriber` | `state_id` | `dim_state` | 400,000 | 0 | 51 | 0 | 100.0% | 7,843.14 |
| `dim_prescriber` | `taxonomy_id` | `dim_taxonomy` | 400,000 | 0 | 800 | 0 | 100.0% | 500.00 |
| `dim_procedure` | `service_category_id` | `dim_service_category` | 12,000 | 0 | 80 | 0 | 100.0% | 150.00 |
| `dim_provider` | `specialty_id` | `dim_specialty` | 1,200,000 | 0 | 180 | 0 | 100.0% | 6,666.67 |
| `dim_provider` | `state_id` | `dim_state` | 1,200,000 | 0 | 51 | 0 | 100.0% | 23,529.41 |
| `dim_provider` | `taxonomy_id` | `dim_taxonomy` | 1,200,000 | 0 | 800 | 0 | 100.0% | 1,500.00 |
| `dim_submitter` | `trading_partner_id` | `dim_trading_partner` | 2,500 | 0 | 80 | 0 | 100.0% | 31.25 |
| `fact_accumulator_entry` | `accumulator_type_id` | `dim_accumulator_type` | 420,000,000 | 0 | 8 | 0 | 100.0% | 52,500,000.00 |
| `fact_accumulator_entry` | `calendar_day_id` | `dim_calendar_day` | 420,000,000 | 0 | 30 | 0 | 100.0% | 14,000,000.00 |
| `fact_accumulator_entry` | `claim_line_id` | `fact_claim_line` | 420,000,000 | 0 | 378,000,000 | 42,000,000 | 90.0% | 1.11 |
| `fact_accumulator_entry` | `member_id` | `dim_member` | 420,000,000 | 0 | 54,400,000 | 13,600,000 | 80.0% | 7.72 |
| `fact_accumulator_entry` | `plan_id` | `dim_plan` | 420,000,000 | 0 | 40 | 0 | 100.0% | 10,500,000.00 |
| `fact_accumulator_snapshot` | `accumulator_type_id` | `dim_accumulator_type` | 544,000,000 | 0 | 8 | 0 | 100.0% | 68,000,000.00 |
| `fact_accumulator_snapshot` | `calendar_day_id` | `dim_calendar_day` | 544,000,000 | 0 | 30 | 0 | 100.0% | 18,133,333.33 |
| `fact_accumulator_snapshot` | `member_id` | `dim_member` | 544,000,000 | 0 | 68,000,000 | 0 | 100.0% | 8.00 |
| `fact_accumulator_snapshot` | `plan_id` | `dim_plan` | 544,000,000 | 0 | 40 | 0 | 100.0% | 13,600,000.00 |
| `fact_appeal` | `appeal_level_id` | `dim_appeal_level` | 180,000 | 0 | 5 | 0 | 100.0% | 36,000.00 |
| `fact_appeal` | `calendar_day_id` | `dim_calendar_day` | 180,000 | 0 | 30 | 0 | 100.0% | 6,000.00 |
| `fact_appeal` | `claim_header_id` | `fact_claim_header` | 180,000 | 0 | 180,000 | 83,820,000 | 0.2% | 1.00 |
| `fact_appeal` | `employee_id` | `dim_employee` | 144,000 | 36,000 | 15,000 | 0 | 100.0% | 9.60 |
| `fact_appeal` | `member_id` | `dim_member` | 180,000 | 0 | 180,000 | 67,820,000 | 0.3% | 1.00 |
| `fact_appeal_decision` | `appeal_id` | `fact_appeal` | 150,000 | 0 | 149,400 | 30,600 | 83.0% | 1.00 |
| `fact_appeal_decision` | `calendar_day_id` | `dim_calendar_day` | 150,000 | 0 | 30 | 0 | 100.0% | 5,000.00 |
| `fact_appeal_decision` | `denial_reason_id` | `dim_denial_reason` | 60,000 | 90,000 | 200 | 0 | 100.0% | 300.00 |
| `fact_appeal_decision` | `employee_id` | `dim_employee` | 150,000 | 0 | 15,000 | 0 | 100.0% | 10.00 |
| `fact_attachment` | `calendar_day_id` | `dim_calendar_day` | 2,500,000 | 0 | 30 | 0 | 100.0% | 83,333.33 |
| `fact_attachment` | `claim_header_id` | `fact_claim_header` | 2,500,000 | 0 | 1,680,000 | 82,320,000 | 2.0% | 1.49 |
| `fact_attachment` | `document_type_id` | `dim_document_type` | 2,500,000 | 0 | 10 | 0 | 100.0% | 250,000.00 |
| `fact_audit_sample` | `audit_program_id` | `dim_audit_program` | 50,000 | 0 | 8 | 0 | 100.0% | 6,250.00 |
| `fact_audit_sample` | `calendar_day_id` | `dim_calendar_day` | 50,000 | 0 | 30 | 0 | 100.0% | 1,666.67 |
| `fact_audit_sample` | `claim_header_id` | `fact_claim_header` | 50,000 | 0 | 50,000 | 83,950,000 | 0.1% | 1.00 |
| `fact_auth_decision` | `calendar_day_id` | `dim_calendar_day` | 2,400,000 | 0 | 30 | 0 | 100.0% | 80,000.00 |
| `fact_auth_decision` | `denial_reason_id` | `dim_denial_reason` | 480,000 | 1,920,000 | 200 | 0 | 100.0% | 2,400.00 |
| `fact_auth_decision` | `employee_id` | `dim_employee` | 2,400,000 | 0 | 15,000 | 0 | 100.0% | 160.00 |
| `fact_auth_decision` | `prior_auth_id` | `fact_prior_auth` | 2,400,000 | 0 | 2,400,000 | 0 | 100.0% | 1.00 |
| `fact_auth_line` | `calendar_day_id` | `dim_calendar_day` | 6,000,000 | 0 | 30 | 0 | 100.0% | 200,000.00 |
| `fact_auth_line` | `prior_auth_id` | `fact_prior_auth` | 6,000,000 | 0 | 2,400,000 | 0 | 100.0% | 2.50 |
| `fact_auth_line` | `procedure_id` | `dim_procedure` | 6,000,000 | 0 | 1,200 | 10,800 | 10.0% | 5,000.00 |
| `fact_call` | `agent_id` | `dim_agent` | 8,000,000 | 0 | 4,000 | 0 | 100.0% | 2,000.00 |
| `fact_call` | `calendar_day_id` | `dim_calendar_day` | 8,000,000 | 0 | 30 | 0 | 100.0% | 266,666.67 |
| `fact_call` | `call_queue_id` | `dim_call_queue` | 8,000,000 | 0 | 20 | 0 | 100.0% | 400,000.00 |
| `fact_call` | `member_id` | `dim_member` | 6,800,000 | 1,200,000 | 6,800,000 | 61,200,000 | 10.0% | 1.00 |
| `fact_call_event` | `agent_id` | `dim_agent` | 24,000,000 | 0 | 4,000 | 0 | 100.0% | 6,000.00 |
| `fact_call_event` | `calendar_day_id` | `dim_calendar_day` | 24,000,000 | 0 | 30 | 0 | 100.0% | 800,000.00 |
| `fact_call_event` | `call_id` | `fact_call` | 24,000,000 | 0 | 8,000,000 | 0 | 100.0% | 3.00 |
| `fact_capitation` | `calendar_day_id` | `dim_calendar_day` | 8,000,000 | 0 | 30 | 0 | 100.0% | 266,666.67 |
| `fact_capitation` | `member_id` | `dim_member` | 5,600,000 | 2,400,000 | 5,600,000 | 62,400,000 | 8.2% | 1.00 |
| `fact_capitation` | `plan_id` | `dim_plan` | 8,000,000 | 0 | 40 | 0 | 100.0% | 200,000.00 |
| `fact_capitation` | `provider_id` | `dim_provider` | 8,000,000 | 0 | 60,000 | 1,140,000 | 5.0% | 133.33 |
| `fact_claim_admission` | `admission_day_id` | `dim_calendar_day` | 15,120,000 | 0 | 30 | 0 | 100.0% | 504,000.00 |
| `fact_claim_admission` | `admission_type_id` | `dim_admission_type` | 15,120,000 | 0 | 10 | 0 | 100.0% | 1,512,000.00 |
| `fact_claim_admission` | `claim_header_id` | `fact_claim_header` | 15,120,000 | 0 | 15,120,000 | 68,880,000 | 18.0% | 1.00 |
| `fact_claim_diagnosis` | `calendar_day_id` | `dim_calendar_day` | 252,000,000 | 0 | 30 | 0 | 100.0% | 8,400,000.00 |
| `fact_claim_diagnosis` | `claim_header_id` | `fact_claim_header` | 252,000,000 | 0 | 84,000,000 | 0 | 100.0% | 3.00 |
| `fact_claim_diagnosis` | `diagnosis_id` | `dim_diagnosis` | 252,000,000 | 0 | 25,200 | 46,800 | 35.0% | 10,000.00 |
| `fact_claim_edit` | `calendar_day_id` | `dim_calendar_day` | 210,000,000 | 0 | 30 | 0 | 100.0% | 7,000,000.00 |
| `fact_claim_edit` | `claim_header_id` | `fact_claim_header` | 210,000,000 | 0 | 84,000,000 | 0 | 100.0% | 2.50 |
| `fact_claim_edit` | `claim_line_id` | `fact_claim_line` | 168,000,000 | 42,000,000 | 168,000,000 | 252,000,000 | 40.0% | 1.00 |
| `fact_claim_edit` | `edit_code_id` | `dim_edit_code` | 210,000,000 | 0 | 1,125 | 375 | 75.0% | 186,666.67 |
| `fact_claim_header` | `bill_type_id` | `dim_bill_type` | 35,280,000 | 48,720,000 | 70 | 30 | 70.0% | 504,000.00 |
| `fact_claim_header` | `billing_provider_id` | `dim_provider` | 84,000,000 | 0 | 840,000 | 360,000 | 70.0% | 100.00 |
| `fact_claim_header` | `calendar_day_id` | `dim_calendar_day` | 84,000,000 | 0 | 30 | 0 | 100.0% | 2,800,000.00 |
| `fact_claim_header` | `claim_frequency_id` | `dim_claim_frequency` | 84,000,000 | 0 | 8 | 0 | 100.0% | 10,500,000.00 |
| `fact_claim_header` | `coverage_id` | `dim_coverage` | 84,000,000 | 0 | 54,000,000 | 18,000,000 | 75.0% | 1.56 |
| `fact_claim_header` | `drg_id` | `dim_drg` | 10,080,000 | 73,920,000 | 480 | 320 | 60.0% | 21,000.00 |
| `fact_claim_header` | `edi_batch_id` | `fact_edi_batch` | 84,000,000 | 0 | 900,000 | 0 | 100.0% | 93.33 |
| `fact_claim_header` | `facility_id` | `dim_facility` | 35,280,000 | 48,720,000 | 144,000 | 36,000 | 80.0% | 245.00 |
| `fact_claim_header` | `filing_indicator_id` | `dim_filing_indicator` | 84,000,000 | 0 | 12 | 0 | 100.0% | 7,000,000.00 |
| `fact_claim_header` | `insurance_line_id` | `dim_insurance_line` | 84,000,000 | 0 | 6 | 0 | 100.0% | 14,000,000.00 |
| `fact_claim_header` | `jurisdiction_id` | `dim_jurisdiction` | 84,000,000 | 0 | 12 | 0 | 100.0% | 7,000,000.00 |
| `fact_claim_header` | `legal_entity_id` | `dim_legal_entity` | 84,000,000 | 0 | 4 | 0 | 100.0% | 21,000,000.00 |
| `fact_claim_header` | `member_id` | `dim_member` | 84,000,000 | 0 | 54,400,000 | 13,600,000 | 80.0% | 1.54 |
| `fact_claim_header` | `place_of_service_id` | `dim_place_of_service` | 84,000,000 | 0 | 50 | 0 | 100.0% | 1,680,000.00 |
| `fact_claim_header` | `plan_id` | `dim_plan` | 84,000,000 | 0 | 40 | 0 | 100.0% | 2,100,000.00 |
| `fact_claim_header` | `principal_diagnosis_id` | `dim_diagnosis` | 84,000,000 | 0 | 28,800 | 43,200 | 40.0% | 2,916.67 |
| `fact_claim_header` | `submitter_id` | `dim_submitter` | 84,000,000 | 0 | 2,500 | 0 | 100.0% | 33,600.00 |
| `fact_claim_header` | `trading_partner_id` | `dim_trading_partner` | 84,000,000 | 0 | 80 | 0 | 100.0% | 1,050,000.00 |
| `fact_claim_line` | `claim_header_id` | `fact_claim_header` | 420,000,000 | 0 | 84,000,000 | 0 | 100.0% | 5.00 |
| `fact_claim_line` | `diagnosis_id` | `dim_diagnosis` | 294,000,000 | 126,000,000 | 18,000 | 54,000 | 25.0% | 16,333.33 |
| `fact_claim_line` | `facility_id` | `dim_facility` | 176,400,000 | 243,600,000 | 180,000 | 0 | 100.0% | 980.00 |
| `fact_claim_line` | `fee_schedule_id` | `dim_fee_schedule` | 336,000,000 | 84,000,000 | 80 | 0 | 100.0% | 4,200,000.00 |
| `fact_claim_line` | `insurance_line_id` | `dim_insurance_line` | 420,000,000 | 0 | 6 | 0 | 100.0% | 70,000,000.00 |
| `fact_claim_line` | `member_id` | `dim_member` | 420,000,000 | 0 | 54,400,000 | 13,600,000 | 80.0% | 7.72 |
| `fact_claim_line` | `modifier_id` | `dim_modifier` | 147,000,000 | 273,000,000 | 200 | 200 | 50.0% | 735,000.00 |
| `fact_claim_line` | `ndc_id` | `dim_ndc` | 33,600,000 | 386,400,000 | 7,500 | 42,500 | 15.0% | 4,480.00 |
| `fact_claim_line` | `place_of_service_id` | `dim_place_of_service` | 420,000,000 | 0 | 50 | 0 | 100.0% | 8,400,000.00 |
| `fact_claim_line` | `plan_id` | `dim_plan` | 420,000,000 | 0 | 40 | 0 | 100.0% | 10,500,000.00 |
| `fact_claim_line` | `procedure_id` | `dim_procedure` | 420,000,000 | 0 | 4,800 | 7,200 | 40.0% | 87,500.00 |
| `fact_claim_line` | `rendering_provider_id` | `dim_provider` | 420,000,000 | 0 | 660,000 | 540,000 | 55.0% | 636.36 |
| `fact_claim_line` | `revenue_code_id` | `dim_revenue_code` | 176,400,000 | 243,600,000 | 300 | 200 | 60.0% | 588,000.00 |
| `fact_claim_line` | `service_day_id` | `dim_calendar_day` | 420,000,000 | 0 | 30 | 0 | 100.0% | 14,000,000.00 |
| `fact_claim_note` | `calendar_day_id` | `dim_calendar_day` | 10,000,000 | 0 | 30 | 0 | 100.0% | 333,333.33 |
| `fact_claim_note` | `claim_header_id` | `fact_claim_header` | 10,000,000 | 0 | 6,720,000 | 77,280,000 | 8.0% | 1.49 |
| `fact_claim_note` | `employee_id` | `dim_employee` | 6,000,000 | 4,000,000 | 15,000 | 0 | 100.0% | 400.00 |
| `fact_claim_note` | `note_type_id` | `dim_note_type` | 10,000,000 | 0 | 15 | 0 | 100.0% | 666,666.67 |
| `fact_claim_status` | `calendar_day_id` | `dim_calendar_day` | 168,000,000 | 0 | 30 | 0 | 100.0% | 5,600,000.00 |
| `fact_claim_status` | `claim_header_id` | `fact_claim_header` | 168,000,000 | 0 | 84,000,000 | 0 | 100.0% | 2.00 |
| `fact_claim_status` | `submitter_id` | `dim_submitter` | 168,000,000 | 0 | 2,500 | 0 | 100.0% | 67,200.00 |
| `fact_claim_status` | `trading_partner_id` | `dim_trading_partner` | 168,000,000 | 0 | 80 | 0 | 100.0% | 2,100,000.00 |
| `fact_cob_line` | `calendar_day_id` | `dim_calendar_day` | 36,000,000 | 0 | 30 | 0 | 100.0% | 1,200,000.00 |
| `fact_cob_line` | `claim_line_id` | `fact_claim_line` | 36,000,000 | 0 | 33,600,000 | 386,400,000 | 8.0% | 1.07 |
| `fact_cob_line` | `cob_type_id` | `dim_cob_type` | 36,000,000 | 0 | 6 | 0 | 100.0% | 6,000,000.00 |
| `fact_cob_line` | `trading_partner_id` | `dim_trading_partner` | 18,000,000 | 18,000,000 | 80 | 0 | 100.0% | 225,000.00 |
| `fact_disenrollment` | `calendar_day_id` | `dim_calendar_day` | 1,200,000 | 0 | 30 | 0 | 100.0% | 40,000.00 |
| `fact_disenrollment` | `coverage_id` | `dim_coverage` | 1,200,000 | 0 | 1,200,000 | 70,800,000 | 1.7% | 1.00 |
| `fact_disenrollment` | `member_id` | `dim_member` | 1,200,000 | 0 | 1,200,000 | 66,800,000 | 1.8% | 1.00 |
| `fact_disenrollment` | `plan_id` | `dim_plan` | 1,200,000 | 0 | 40 | 0 | 100.0% | 30,000.00 |
| `fact_edi_batch` | `calendar_day_id` | `dim_calendar_day` | 900,000 | 0 | 30 | 0 | 100.0% | 30,000.00 |
| `fact_edi_batch` | `submitter_id` | `dim_submitter` | 900,000 | 0 | 2,500 | 0 | 100.0% | 360.00 |
| `fact_edi_batch` | `trading_partner_id` | `dim_trading_partner` | 900,000 | 0 | 80 | 0 | 100.0% | 11,250.00 |
| `fact_eligibility_inquiry` | `calendar_day_id` | `dim_calendar_day` | 336,000,000 | 0 | 30 | 0 | 100.0% | 11,200,000.00 |
| `fact_eligibility_inquiry` | `coverage_id` | `dim_coverage` | 336,000,000 | 0 | 61,200,000 | 10,800,000 | 85.0% | 5.49 |
| `fact_eligibility_inquiry` | `jurisdiction_id` | `dim_jurisdiction` | 336,000,000 | 0 | 12 | 0 | 100.0% | 28,000,000.00 |
| `fact_eligibility_inquiry` | `member_id` | `dim_member` | 336,000,000 | 0 | 61,200,000 | 6,800,000 | 90.0% | 5.49 |
| `fact_eligibility_inquiry` | `plan_id` | `dim_plan` | 336,000,000 | 0 | 40 | 0 | 100.0% | 8,400,000.00 |
| `fact_eligibility_inquiry` | `provider_id` | `dim_provider` | 336,000,000 | 0 | 600,000 | 600,000 | 50.0% | 560.00 |
| `fact_eligibility_inquiry` | `trading_partner_id` | `dim_trading_partner` | 336,000,000 | 0 | 80 | 0 | 100.0% | 4,200,000.00 |
| `fact_eligibility_response` | `calendar_day_id` | `dim_calendar_day` | 336,000,000 | 0 | 30 | 0 | 100.0% | 11,200,000.00 |
| `fact_eligibility_response` | `eligibility_inquiry_id` | `fact_eligibility_inquiry` | 336,000,000 | 0 | 336,000,000 | 0 | 100.0% | 1.00 |
| `fact_eligibility_response` | `member_id` | `dim_member` | 336,000,000 | 0 | 61,200,000 | 6,800,000 | 90.0% | 5.49 |
| `fact_eligibility_response` | `plan_id` | `dim_plan` | 336,000,000 | 0 | 40 | 0 | 100.0% | 8,400,000.00 |
| `fact_encounter` | `calendar_day_id` | `dim_calendar_day` | 50,000,000 | 0 | 30 | 0 | 100.0% | 1,666,666.67 |
| `fact_encounter` | `facility_id` | `dim_facility` | 20,000,000 | 30,000,000 | 180,000 | 0 | 100.0% | 111.11 |
| `fact_encounter` | `member_id` | `dim_member` | 50,000,000 | 0 | 20,400,000 | 47,600,000 | 30.0% | 2.45 |
| `fact_encounter` | `place_of_service_id` | `dim_place_of_service` | 50,000,000 | 0 | 50 | 0 | 100.0% | 1,000,000.00 |
| `fact_encounter` | `plan_id` | `dim_plan` | 50,000,000 | 0 | 40 | 0 | 100.0% | 1,250,000.00 |
| `fact_encounter` | `provider_id` | `dim_provider` | 50,000,000 | 0 | 240,000 | 960,000 | 20.0% | 208.33 |
| `fact_enrollment_span` | `coverage_id` | `dim_coverage` | 72,000,000 | 0 | 72,000,000 | 0 | 100.0% | 1.00 |
| `fact_enrollment_span` | `plan_id` | `dim_plan` | 72,000,000 | 0 | 40 | 0 | 100.0% | 1,800,000.00 |
| `fact_enrollment_span` | `start_day_id` | `dim_calendar_day` | 2,880,000 | 69,120,000 | 30 | 0 | 100.0% | 96,000.00 |
| `fact_fee_schedule_rate` | `fee_schedule_id` | `dim_fee_schedule` | 2,000,000 | 0 | 80 | 0 | 100.0% | 25,000.00 |
| `fact_fee_schedule_rate` | `locality_id` | `dim_locality` | 2,000,000 | 0 | 120 | 0 | 100.0% | 16,666.67 |
| `fact_fee_schedule_rate` | `procedure_id` | `dim_procedure` | 2,000,000 | 0 | 6,000 | 6,000 | 50.0% | 333.33 |
| `fact_fraud_lead` | `calendar_day_id` | `dim_calendar_day` | 30,000 | 0 | 30 | 0 | 100.0% | 1,000.00 |
| `fact_fraud_lead` | `fraud_scheme_id` | `dim_fraud_scheme` | 30,000 | 0 | 40 | 0 | 100.0% | 750.00 |
| `fact_fraud_lead` | `member_id` | `dim_member` | 12,000 | 18,000 | 12,000 | 67,988,000 | 0.0% | 1.00 |
| `fact_fraud_lead` | `provider_id` | `dim_provider` | 21,000 | 9,000 | 21,000 | 1,179,000 | 1.8% | 1.00 |
| `fact_grievance` | `calendar_day_id` | `dim_calendar_day` | 90,000 | 0 | 30 | 0 | 100.0% | 3,000.00 |
| `fact_grievance` | `member_id` | `dim_member` | 90,000 | 0 | 90,000 | 67,910,000 | 0.1% | 1.00 |
| `fact_grievance` | `plan_id` | `dim_plan` | 90,000 | 0 | 40 | 0 | 100.0% | 2,250.00 |
| `fact_hcc_diagnosis` | `calendar_day_id` | `dim_calendar_day` | 96,000,000 | 0 | 30 | 0 | 100.0% | 3,200,000.00 |
| `fact_hcc_diagnosis` | `diagnosis_id` | `dim_diagnosis` | 96,000,000 | 0 | 5,760 | 66,240 | 8.0% | 16,666.67 |
| `fact_hcc_diagnosis` | `hcc_id` | `dim_hcc` | 67,200,000 | 28,800,000 | 200 | 0 | 100.0% | 336,000.00 |
| `fact_hcc_diagnosis` | `member_id` | `dim_member` | 96,000,000 | 0 | 27,200,000 | 40,800,000 | 40.0% | 3.53 |
| `fact_hcc_diagnosis` | `risk_model_id` | `dim_risk_model` | 96,000,000 | 0 | 4 | 0 | 100.0% | 24,000,000.00 |
| `fact_interest_payment` | `calendar_day_id` | `dim_calendar_day` | 200,000 | 0 | 30 | 0 | 100.0% | 6,666.67 |
| `fact_interest_payment` | `claim_header_id` | `fact_claim_header` | 200,000 | 0 | 200,000 | 83,800,000 | 0.2% | 1.00 |
| `fact_interest_payment` | `interest_reason_id` | `dim_interest_reason` | 200,000 | 0 | 8 | 0 | 100.0% | 25,000.00 |
| `fact_interest_payment` | `provider_id` | `dim_provider` | 200,000 | 0 | 200,000 | 1,000,000 | 16.7% | 1.00 |
| `fact_letter` | `calendar_day_id` | `dim_calendar_day` | 5,000,000 | 0 | 30 | 0 | 100.0% | 166,666.67 |
| `fact_letter` | `document_type_id` | `dim_document_type` | 5,000,000 | 0 | 10 | 0 | 100.0% | 500,000.00 |
| `fact_letter` | `member_id` | `dim_member` | 5,000,000 | 0 | 4,080,000 | 63,920,000 | 6.0% | 1.23 |
| `fact_low_income_subsidy` | `calendar_day_id` | `dim_calendar_day` | 6,000,000 | 0 | 30 | 0 | 100.0% | 200,000.00 |
| `fact_low_income_subsidy` | `lis_level_id` | `dim_lis_level` | 6,000,000 | 0 | 5 | 0 | 100.0% | 1,200,000.00 |
| `fact_low_income_subsidy` | `member_id` | `dim_member` | 6,000,000 | 0 | 5,440,000 | 62,560,000 | 8.0% | 1.10 |
| `fact_medical_review` | `calendar_day_id` | `dim_calendar_day` | 900,000 | 0 | 30 | 0 | 100.0% | 30,000.00 |
| `fact_medical_review` | `claim_line_id` | `fact_claim_line` | 900,000 | 0 | 840,000 | 419,160,000 | 0.2% | 1.07 |
| `fact_medical_review` | `employee_id` | `dim_employee` | 900,000 | 0 | 15,000 | 0 | 100.0% | 60.00 |
| `fact_medical_review` | `review_type_id` | `dim_review_type` | 900,000 | 0 | 8 | 0 | 100.0% | 112,500.00 |
| `fact_overpayment` | `calendar_day_id` | `dim_calendar_day` | 400,000 | 0 | 30 | 0 | 100.0% | 13,333.33 |
| `fact_overpayment` | `claim_header_id` | `fact_claim_header` | 400,000 | 0 | 400,000 | 83,600,000 | 0.5% | 1.00 |
| `fact_overpayment` | `provider_id` | `dim_provider` | 400,000 | 0 | 400,000 | 800,000 | 33.3% | 1.00 |
| `fact_pcp_attribution` | `calendar_day_id` | `dim_calendar_day` | 68,000,000 | 0 | 30 | 0 | 100.0% | 2,266,666.67 |
| `fact_pcp_attribution` | `member_id` | `dim_member` | 68,000,000 | 0 | 68,000,000 | 0 | 100.0% | 1.00 |
| `fact_pcp_attribution` | `plan_id` | `dim_plan` | 68,000,000 | 0 | 40 | 0 | 100.0% | 1,700,000.00 |
| `fact_pcp_attribution` | `provider_id` | `dim_provider` | 68,000,000 | 0 | 180,000 | 1,020,000 | 15.0% | 377.78 |
| `fact_pharmacy_claim` | `calendar_day_id` | `dim_calendar_day` | 136,000,000 | 0 | 30 | 0 | 100.0% | 4,533,333.33 |
| `fact_pharmacy_claim` | `formulary_id` | `dim_formulary` | 108,800,000 | 27,200,000 | 30 | 0 | 100.0% | 3,626,666.67 |
| `fact_pharmacy_claim` | `insurance_line_id` | `dim_insurance_line` | 136,000,000 | 0 | 6 | 0 | 100.0% | 22,666,666.67 |
| `fact_pharmacy_claim` | `member_id` | `dim_member` | 136,000,000 | 0 | 30,600,000 | 37,400,000 | 45.0% | 4.44 |
| `fact_pharmacy_claim` | `ndc_id` | `dim_ndc` | 136,000,000 | 0 | 12,500 | 37,500 | 25.0% | 10,880.00 |
| `fact_pharmacy_claim` | `pharmacy_id` | `dim_pharmacy` | 136,000,000 | 0 | 55,200 | 4,800 | 92.0% | 2,463.77 |
| `fact_pharmacy_claim` | `plan_id` | `dim_plan` | 136,000,000 | 0 | 40 | 0 | 100.0% | 3,400,000.00 |
| `fact_pharmacy_claim` | `prescriber_id` | `dim_prescriber` | 136,000,000 | 0 | 240,000 | 160,000 | 60.0% | 566.67 |
| `fact_pharmacy_claim` | `tier_id` | `dim_tier` | 136,000,000 | 0 | 6 | 0 | 100.0% | 22,666,666.67 |
| `fact_portal_event` | `calendar_day_id` | `dim_calendar_day` | 45,000,000 | 0 | 30 | 0 | 100.0% | 1,500,000.00 |
| `fact_portal_event` | `member_id` | `dim_member` | 45,000,000 | 0 | 17,000,000 | 51,000,000 | 25.0% | 2.65 |
| `fact_premium_adjustment` | `calendar_day_id` | `dim_calendar_day` | 800,000 | 0 | 30 | 0 | 100.0% | 26,666.67 |
| `fact_premium_adjustment` | `member_id` | `dim_member` | 800,000 | 0 | 800,000 | 67,200,000 | 1.2% | 1.00 |
| `fact_premium_adjustment` | `premium_bill_id` | `fact_premium_bill` | 800,000 | 0 | 800,000 | 67,200,000 | 1.2% | 1.00 |
| `fact_premium_bill` | `calendar_day_id` | `dim_calendar_day` | 68,000,000 | 0 | 30 | 0 | 100.0% | 2,266,666.67 |
| `fact_premium_bill` | `member_id` | `dim_member` | 68,000,000 | 0 | 68,000,000 | 0 | 100.0% | 1.00 |
| `fact_premium_bill` | `plan_id` | `dim_plan` | 68,000,000 | 0 | 40 | 0 | 100.0% | 1,700,000.00 |
| `fact_premium_bill` | `premium_schedule_id` | `dim_premium_schedule` | 68,000,000 | 0 | 40 | 0 | 100.0% | 1,700,000.00 |
| `fact_premium_payment` | `calendar_day_id` | `dim_calendar_day` | 60,000,000 | 0 | 30 | 0 | 100.0% | 2,000,000.00 |
| `fact_premium_payment` | `member_id` | `dim_member` | 60,000,000 | 0 | 57,800,000 | 10,200,000 | 85.0% | 1.04 |
| `fact_premium_payment` | `payment_method_id` | `dim_payment_method` | 60,000,000 | 0 | 6 | 0 | 100.0% | 10,000,000.00 |
| `fact_premium_payment` | `premium_bill_id` | `fact_premium_bill` | 60,000,000 | 0 | 59,840,000 | 8,160,000 | 88.0% | 1.00 |
| `fact_pricing_result` | `calendar_day_id` | `dim_calendar_day` | 420,000,000 | 0 | 30 | 0 | 100.0% | 14,000,000.00 |
| `fact_pricing_result` | `claim_line_id` | `fact_claim_line` | 420,000,000 | 0 | 420,000,000 | 0 | 100.0% | 1.00 |
| `fact_pricing_result` | `fee_schedule_id` | `dim_fee_schedule` | 420,000,000 | 0 | 80 | 0 | 100.0% | 5,250,000.00 |
| `fact_pricing_result` | `locality_id` | `dim_locality` | 420,000,000 | 0 | 120 | 0 | 100.0% | 3,500,000.00 |
| `fact_pricing_result` | `procedure_id` | `dim_procedure` | 420,000,000 | 0 | 4,800 | 7,200 | 40.0% | 87,500.00 |
| `fact_prior_auth` | `auth_type_id` | `dim_auth_type` | 2,400,000 | 0 | 15 | 0 | 100.0% | 160,000.00 |
| `fact_prior_auth` | `calendar_day_id` | `dim_calendar_day` | 2,400,000 | 0 | 30 | 0 | 100.0% | 80,000.00 |
| `fact_prior_auth` | `employee_id` | `dim_employee` | 960,000 | 1,440,000 | 15,000 | 0 | 100.0% | 64.00 |
| `fact_prior_auth` | `member_id` | `dim_member` | 2,400,000 | 0 | 2,040,000 | 65,960,000 | 3.0% | 1.18 |
| `fact_prior_auth` | `plan_id` | `dim_plan` | 2,400,000 | 0 | 40 | 0 | 100.0% | 60,000.00 |
| `fact_prior_auth` | `provider_id` | `dim_provider` | 2,400,000 | 0 | 120,000 | 1,080,000 | 10.0% | 20.00 |
| `fact_provider_enrollment` | `calendar_day_id` | `dim_calendar_day` | 40,000 | 0 | 30 | 0 | 100.0% | 1,333.33 |
| `fact_provider_enrollment` | `enrollment_status_id` | `dim_enrollment_status` | 40,000 | 0 | 6 | 0 | 100.0% | 6,666.67 |
| `fact_provider_enrollment` | `jurisdiction_id` | `dim_jurisdiction` | 40,000 | 0 | 12 | 0 | 100.0% | 3,333.33 |
| `fact_provider_enrollment` | `provider_id` | `dim_provider` | 40,000 | 0 | 40,000 | 1,160,000 | 3.3% | 1.00 |
| `fact_provider_payment` | `bank_id` | `dim_bank` | 12,000,000 | 0 | 15 | 0 | 100.0% | 800,000.00 |
| `fact_provider_payment` | `calendar_day_id` | `dim_calendar_day` | 12,000,000 | 0 | 30 | 0 | 100.0% | 400,000.00 |
| `fact_provider_payment` | `jurisdiction_id` | `dim_jurisdiction` | 12,000,000 | 0 | 12 | 0 | 100.0% | 1,000,000.00 |
| `fact_provider_payment` | `provider_id` | `dim_provider` | 12,000,000 | 0 | 480,000 | 720,000 | 40.0% | 25.00 |
| `fact_provider_payment` | `remit_advice_id` | `fact_remit_advice` | 10,800,000 | 1,200,000 | 10,800,000 | 1,200,000 | 90.0% | 1.00 |
| `fact_recovery` | `calendar_day_id` | `dim_calendar_day` | 250,000 | 0 | 30 | 0 | 100.0% | 8,333.33 |
| `fact_recovery` | `overpayment_id` | `fact_overpayment` | 250,000 | 0 | 240,000 | 160,000 | 60.0% | 1.04 |
| `fact_recovery` | `provider_id` | `dim_provider` | 250,000 | 0 | 250,000 | 950,000 | 20.8% | 1.00 |
| `fact_referral` | `calendar_day_id` | `dim_calendar_day` | 1,100,000 | 0 | 30 | 0 | 100.0% | 36,666.67 |
| `fact_referral` | `member_id` | `dim_member` | 1,100,000 | 0 | 1,100,000 | 66,900,000 | 1.6% | 1.00 |
| `fact_referral` | `plan_id` | `dim_plan` | 1,100,000 | 0 | 40 | 0 | 100.0% | 27,500.00 |
| `fact_referral` | `referring_provider_id` | `dim_provider` | 1,100,000 | 0 | 60,000 | 1,140,000 | 5.0% | 18.33 |
| `fact_referral_target` | `referral_id` | `fact_referral` | 1,100,000 | 0 | 1,100,000 | 0 | 100.0% | 1.00 |
| `fact_referral_target` | `referred_provider_id` | `dim_provider` | 1,100,000 | 0 | 96,000 | 1,104,000 | 8.0% | 11.46 |
| `fact_remit_adjustment` | `calendar_day_id` | `dim_calendar_day` | 630,000,000 | 0 | 30 | 0 | 100.0% | 21,000,000.00 |
| `fact_remit_adjustment` | `carc_id` | `dim_carc` | 630,000,000 | 0 | 300 | 0 | 100.0% | 2,100,000.00 |
| `fact_remit_adjustment` | `rarc_id` | `dim_rarc` | 441,000,000 | 189,000,000 | 440 | 660 | 40.0% | 1,002,272.73 |
| `fact_remit_adjustment` | `remit_line_id` | `fact_remit_line` | 630,000,000 | 0 | 352,800,000 | 151,200,000 | 70.0% | 1.79 |
| `fact_remit_advice` | `bank_id` | `dim_bank` | 10,800,000 | 1,200,000 | 15 | 0 | 100.0% | 720,000.00 |
| `fact_remit_advice` | `billing_provider_id` | `dim_provider` | 12,000,000 | 0 | 780,000 | 420,000 | 65.0% | 15.38 |
| `fact_remit_advice` | `calendar_day_id` | `dim_calendar_day` | 12,000,000 | 0 | 30 | 0 | 100.0% | 400,000.00 |
| `fact_remit_advice` | `jurisdiction_id` | `dim_jurisdiction` | 12,000,000 | 0 | 12 | 0 | 100.0% | 1,000,000.00 |
| `fact_remit_advice` | `payment_method_id` | `dim_payment_method` | 12,000,000 | 0 | 6 | 0 | 100.0% | 2,000,000.00 |
| `fact_remit_advice` | `trading_partner_id` | `dim_trading_partner` | 12,000,000 | 0 | 80 | 0 | 100.0% | 150,000.00 |
| `fact_remit_line` | `calendar_day_id` | `dim_calendar_day` | 504,000,000 | 0 | 30 | 0 | 100.0% | 16,800,000.00 |
| `fact_remit_line` | `carc_id` | `dim_carc` | 277,200,000 | 226,800,000 | 240 | 60 | 80.0% | 1,155,000.00 |
| `fact_remit_line` | `claim_header_id` | `fact_claim_header` | 504,000,000 | 0 | 82,320,000 | 1,680,000 | 98.0% | 6.12 |
| `fact_remit_line` | `claim_line_id` | `fact_claim_line` | 504,000,000 | 0 | 403,200,000 | 16,800,000 | 96.0% | 1.25 |
| `fact_remit_line` | `member_id` | `dim_member` | 504,000,000 | 0 | 54,400,000 | 13,600,000 | 80.0% | 9.26 |
| `fact_remit_line` | `provider_id` | `dim_provider` | 504,000,000 | 0 | 780,000 | 420,000 | 65.0% | 646.15 |
| `fact_remit_line` | `remit_advice_id` | `fact_remit_advice` | 504,000,000 | 0 | 12,000,000 | 0 | 100.0% | 42.00 |
| `fact_revalidation` | `calendar_day_id` | `dim_calendar_day` | 20,000 | 0 | 30 | 0 | 100.0% | 666.67 |
| `fact_revalidation` | `jurisdiction_id` | `dim_jurisdiction` | 20,000 | 0 | 12 | 0 | 100.0% | 1,666.67 |
| `fact_revalidation` | `provider_id` | `dim_provider` | 20,000 | 0 | 20,000 | 1,180,000 | 1.7% | 1.00 |
| `fact_risk_score` | `calendar_day_id` | `dim_calendar_day` | 68,000,000 | 0 | 30 | 0 | 100.0% | 2,266,666.67 |
| `fact_risk_score` | `member_id` | `dim_member` | 68,000,000 | 0 | 68,000,000 | 0 | 100.0% | 1.00 |
| `fact_risk_score` | `plan_id` | `dim_plan` | 68,000,000 | 0 | 40 | 0 | 100.0% | 1,700,000.00 |
| `fact_risk_score` | `risk_model_id` | `dim_risk_model` | 68,000,000 | 0 | 4 | 0 | 100.0% | 17,000,000.00 |
| `fact_withhold` | `calendar_day_id` | `dim_calendar_day` | 100,000 | 0 | 30 | 0 | 100.0% | 3,333.33 |
| `fact_withhold` | `provider_payment_id` | `fact_provider_payment` | 100,000 | 0 | 100,000 | 11,900,000 | 0.8% | 1.00 |
| `fact_withhold` | `withhold_reason_id` | `dim_withhold_reason` | 100,000 | 0 | 10 | 0 | 100.0% | 10,000.00 |
